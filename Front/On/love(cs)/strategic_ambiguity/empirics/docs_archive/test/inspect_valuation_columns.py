"""
Quick inspection script to check valuation column names in raw data.
Run: python inspect_valuation_columns.py
"""

import pandas as pd
import sys
from pathlib import Path

print("="*80)
print("VALUATION COLUMNS INSPECTOR")
print("="*80)

# UPDATE THESE PATHS to match your data location
baseline_path = "data/raw/Company20220101.dat"  # ← CHANGE THIS
endpoint_path = "data/raw/Company20231201.dat"  # ← CHANGE THIS

# Try to auto-detect if paths don't exist
if not Path(baseline_path).exists():
    print(f"\n⚠️  Baseline file not found: {baseline_path}")
    print("\nLooking for .dat files in data/raw/...")
    raw_dir = Path("data/raw")
    if raw_dir.exists():
        dat_files = sorted(raw_dir.glob("Company*.dat"))
        if dat_files:
            print(f"\nFound {len(dat_files)} .dat files:")
            for i, f in enumerate(dat_files, 1):
                print(f"  {i}. {f.name}")
            if len(dat_files) >= 2:
                baseline_path = str(dat_files[0])
                endpoint_path = str(dat_files[-1])
                print(f"\nAuto-selected:")
                print(f"  Baseline: {baseline_path}")
                print(f"  Endpoint: {endpoint_path}")
        else:
            print(f"\n✗ No Company*.dat files found in {raw_dir}")
            sys.exit(1)
    else:
        print(f"\n✗ data/raw directory not found")
        sys.exit(1)

print(f"\n1. Loading files...")
try:
    df_b = pd.read_csv(baseline_path, sep='\t', low_memory=False, nrows=1000)  # Sample 1000 rows
    df_e = pd.read_csv(endpoint_path, sep='\t', low_memory=False, nrows=1000)
    print(f"   ✓ Baseline: {len(df_b)} rows × {len(df_b.columns)} cols (sample)")
    print(f"   ✓ Endpoint: {len(df_e)} rows × {len(df_e.columns)} cols (sample)")
except Exception as e:
    print(f"   ✗ Error loading files: {e}")
    sys.exit(1)

print(f"\n2. Searching for valuation-related columns...")

def find_valuation_cols(df, label):
    """Find columns with 'val' or 'money' in their names."""
    val_cols = [c for c in df.columns if 'val' in c.lower() or 'money' in c.lower()]

    print(f"\n   {label}:")
    if not val_cols:
        print(f"     ✗ No valuation columns found!")
    else:
        print(f"     Found {len(val_cols)} valuation-related columns:")
        for col in sorted(val_cols):
            non_null = df[col].notna().sum()
            pct = non_null / len(df) * 100
            print(f"       • {col:35s}: {non_null:4} / {len(df)} non-null ({pct:5.1f}%)")

            # Try to show sample values
            sample_vals = df[col].dropna().head(3)
            if len(sample_vals) > 0:
                print(f"         Sample values: {list(sample_vals)[:3]}")

    return val_cols

baseline_val_cols = find_valuation_cols(df_b, "BASELINE")
endpoint_val_cols = find_valuation_cols(df_e, "ENDPOINT")

print(f"\n3. Checking for required columns...")

# Check what we need
required = {
    'baseline': ['PostValuation', 'PostMoneyValuation'],  # Either one works
    'endpoint': ['PreMoneyValuation']
}

print(f"\n   For step-up calculation, we need:")
print(f"     Baseline:  PostValuation OR PostMoneyValuation")
print(f"     Endpoint:  PreMoneyValuation")

# Check baseline
print(f"\n   Baseline check:")
has_post_baseline = False
for col in required['baseline']:
    if col in df_b.columns:
        non_null = df_b[col].notna().sum()
        print(f"     ✓ {col}: Found! ({non_null} non-null)")
        has_post_baseline = True
    else:
        print(f"     ✗ {col}: NOT FOUND")

if not has_post_baseline:
    print(f"\n     ❌ Missing post-money valuation in baseline!")

# Check endpoint
print(f"\n   Endpoint check:")
has_pre_endpoint = False
for col in required['endpoint']:
    if col in df_e.columns:
        non_null = df_e[col].notna().sum()
        print(f"     ✓ {col}: Found! ({non_null} non-null)")
        has_pre_endpoint = True
    else:
        print(f"     ✗ {col}: NOT FOUND")

if not has_pre_endpoint:
    print(f"\n     ❌ Missing pre-money valuation in endpoint!")

print(f"\n4. Diagnosis:")

if has_post_baseline and has_pre_endpoint:
    print(f"   ✅ Required columns EXIST!")
    print(f"   → Step-up calculation should work")
    print(f"   → If you still see 0 step-up values, the issue is likely:")
    print(f"      - Most values are NULL/empty in the data")
    print(f"      - Companies don't have valuations in both snapshots")
else:
    print(f"   ❌ Missing required columns!")
    print(f"\n   Possible solutions:")
    if not has_post_baseline:
        print(f"      1. Check if baseline uses different column name (see list above)")
        print(f"      2. If PostMoneyValuation is available, update features.py:")
        print(f"         Change 'PostValuation_t1' to 'PostMoneyValuation_t1'")
    if not has_pre_endpoint:
        print(f"      3. Check if endpoint uses different column name")
        print(f"      4. If PreMoneyValuation is missing, you may need to:")
        print(f"         - Use different snapshot files")
        print(f"         - Skip H3 analysis (step-up not available)")

print("\n" + "="*80)
print("INSPECTION COMPLETE")
print("="*80)
