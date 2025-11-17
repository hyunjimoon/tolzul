"""
Diagnostic script to investigate missing step-up data.
Run: python diagnose_stepup.py
"""

import pandas as pd
import sys
from pathlib import Path

print("="*80)
print("STEP-UP DATA DIAGNOSTIC")
print("="*80)

# Load your snapshot files (adjust paths as needed)
baseline_path = "data/raw/Company20220101.dat"  # CHANGE THIS
endpoint_path = "data/raw/Company20231201.dat"  # CHANGE THIS

print(f"\n1. Loading snapshots...")
try:
    df_b = pd.read_csv(baseline_path, sep='\t', low_memory=False)
    df_e = pd.read_csv(endpoint_path, sep='\t', low_memory=False)
    print(f"   ✓ Baseline: {len(df_b):,} rows × {len(df_b.columns)} cols")
    print(f"   ✓ Endpoint: {len(df_e):,} rows × {len(df_e.columns)} cols")
except Exception as e:
    print(f"   ✗ Failed to load files: {e}")
    print(f"\n   Please update the file paths in diagnose_stepup.py:")
    print(f"     baseline_path = '{baseline_path}'")
    print(f"     endpoint_path = '{endpoint_path}'")
    sys.exit(1)

print(f"\n2. Checking for valuation columns...")

# Check baseline
val_cols_baseline = ['PreMoneyValuation', 'PostValuation', 'PostMoneyValuation']
print(f"\n   Baseline snapshot:")
for col in val_cols_baseline:
    if col in df_b.columns:
        non_null = df_b[col].notna().sum()
        pct = non_null / len(df_b) * 100
        print(f"     ✓ {col:25s}: {non_null:8,} / {len(df_b):,} ({pct:.1f}%) non-null")
        if non_null > 0:
            # Try to convert to numeric
            numeric_vals = pd.to_numeric(df_b[col], errors='coerce')
            positive = (numeric_vals > 0).sum()
            print(f"       → {positive:,} positive values")
    else:
        print(f"     ✗ {col:25s}: NOT FOUND")

# Check endpoint
print(f"\n   Endpoint snapshot:")
for col in val_cols_baseline:
    if col in df_e.columns:
        non_null = df_e[col].notna().sum()
        pct = non_null / len(df_e) * 100
        print(f"     ✓ {col:25s}: {non_null:8,} / {len(df_e):,} ({pct:.1f}%) non-null")
        if non_null > 0:
            numeric_vals = pd.to_numeric(df_e[col], errors='coerce')
            positive = (numeric_vals > 0).sum()
            print(f"       → {positive:,} positive values")
    else:
        print(f"     ✗ {col:25s}: NOT FOUND")

print(f"\n3. Calculating potential step-up values...")

# Merge by CompanyID
if 'CompanyID' not in df_b.columns or 'CompanyID' not in df_e.columns:
    print(f"   ✗ CompanyID not found in snapshots")
    sys.exit(1)

# Rename columns with suffixes
df_b = df_b.rename(columns={
    'PreMoneyValuation': 'PreMoney_t1',
    'PostValuation': 'PostMoney_t1'
})
df_e = df_e.rename(columns={
    'PreMoneyValuation': 'PreMoney_t2',
    'PostValuation': 'PostMoney_t2'
})

df_merged = df_b[['CompanyID', 'PostMoney_t1']].merge(
    df_e[['CompanyID', 'PreMoney_t2']],
    on='CompanyID',
    how='inner'
)

print(f"   Merged dataset: {len(df_merged):,} companies")

# Convert to numeric
df_merged['PostMoney_t1'] = pd.to_numeric(df_merged['PostMoney_t1'], errors='coerce')
df_merged['PreMoney_t2'] = pd.to_numeric(df_merged['PreMoney_t2'], errors='coerce')

# Count valid combinations
both_present = df_merged['PostMoney_t1'].notna() & df_merged['PreMoney_t2'].notna()
both_positive = (df_merged['PostMoney_t1'] > 0) & (df_merged['PreMoney_t2'] > 0)

print(f"\n   Valid combinations:")
print(f"     Both present (non-null): {both_present.sum():,}")
print(f"     Both positive (>0):      {both_positive.sum():,}")

if both_positive.sum() > 0:
    # Calculate step-up for valid rows
    df_valid = df_merged[both_positive].copy()
    df_valid['S_stepup'] = df_valid['PreMoney_t2'] / df_valid['PostMoney_t1']

    print(f"\n   Step-up statistics:")
    print(f"     Mean:   {df_valid['S_stepup'].mean():.2f}")
    print(f"     Median: {df_valid['S_stepup'].median():.2f}")
    print(f"     Min:    {df_valid['S_stepup'].min():.2f}")
    print(f"     Max:    {df_valid['S_stepup'].max():.2f}")

    print(f"\n   ✅ Step-up calculation should work!")
    print(f"   Expected: {both_positive.sum():,} valid S values")
else:
    print(f"\n   ❌ No valid step-up values found!")
    print(f"\n   Breakdown of missing data:")
    print(f"     PostMoney_t1 missing: {df_merged['PostMoney_t1'].isna().sum():,}")
    print(f"     PreMoney_t2 missing:  {df_merged['PreMoney_t2'].isna().sum():,}")
    print(f"     PostMoney_t1 ≤ 0:     {(df_merged['PostMoney_t1'] <= 0).sum():,}")
    print(f"     PreMoney_t2 ≤ 0:      {(df_merged['PreMoney_t2'] <= 0).sum():,}")

print(f"\n4. Checking column names in raw files...")
print(f"\n   All baseline columns ({len(df_b.columns)}):")
val_related = [c for c in df_b.columns if 'val' in c.lower() or 'money' in c.lower()]
print(f"     Valuation-related: {val_related}")

print(f"\n   All endpoint columns ({len(df_e.columns)}):")
val_related = [c for c in df_e.columns if 'val' in c.lower() or 'money' in c.lower()]
print(f"     Valuation-related: {val_related}")

print("\n" + "="*80)
print("DIAGNOSIS COMPLETE")
print("="*80)
print("\nNext steps:")
print("  1. Check if valuation columns exist in your data files")
print("  2. If columns are named differently, update features.py")
print("  3. If valuations are missing, you may need to:")
print("     - Use different snapshot dates with better coverage")
print("     - Skip H3 analysis (step-up) and only run H1/H2")
print("     - Augment data with external valuation sources")
