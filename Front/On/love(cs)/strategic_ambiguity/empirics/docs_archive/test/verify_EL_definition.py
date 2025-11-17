"""
Verify E/L definition logic in current code.
Checks how many companies are misclassified.
"""

import pandas as pd
import numpy as np
import sys
import re
from pathlib import Path

print("="*80)
print("E/L DEFINITION VERIFICATION")
print("="*80)

# Load your actual snapshots
baseline_path = "data/raw/Company20220101.dat"  # UPDATE THIS
endpoint_path = "data/raw/Company20231201.dat"  # UPDATE THIS

print(f"\n1. Loading snapshots...")
# Try both pipe and tab delimiters
try:
    df_b = pd.read_csv(baseline_path, sep='|', low_memory=False)
    df_e = pd.read_csv(endpoint_path, sep='|', low_memory=False)
    print(f"   ✓ Using pipe-delimited format (|)")
except Exception as e:
    print(f"   Pipe delimiter failed, trying tab...")
    df_b = pd.read_csv(baseline_path, sep='\t', low_memory=False)
    df_e = pd.read_csv(endpoint_path, sep='\t', low_memory=False)
    print(f"   ✓ Using tab-delimited format (\\t)")

print(f"   ✓ Baseline: {len(df_b):,} companies")
print(f"   ✓ Endpoint: {len(df_e):,} companies")

# Detect deal type column name (flexible column name handling)
print(f"\n1a. Detecting deal type column...")
possible_names = [
    'LastFinancingDealType',
    'LastDealType',
    'DealType',
    'FundingType',
    'LastFinancingType',
    'FinancingDealType',
    'LastFundingType',
    'LastRoundType'
]

deal_col = None
for col in possible_names:
    if col in df_b.columns:
        deal_col = col
        print(f"   ✓ Found deal type column: '{deal_col}'")
        break

if deal_col is None:
    print(f"\n   ✗ Could not auto-detect deal type column!")
    print(f"\n   Available columns with 'deal', 'financing', 'type', or 'round' in name:")
    candidates = [c for c in df_b.columns if any(x in c.lower() for x in ['deal', 'financing', 'type', 'round', 'funding'])]
    if candidates:
        for i, c in enumerate(candidates[:20], 1):
            print(f"      {i}. {c}")
    else:
        print(f"      (none found)")
    print(f"\n   Please update the script with the correct column name.")
    print(f"   Add it to 'possible_names' list or use:")
    print(f"      deal_col = 'YourActualColumnName'")
    sys.exit(1)

# Verify endpoint has same column
if deal_col not in df_e.columns:
    print(f"\n   ✗ ERROR: '{deal_col}' found in baseline but NOT in endpoint!")
    print(f"   Endpoint columns with 'deal/financing/type': {[c for c in df_e.columns if any(x in c.lower() for x in ['deal', 'financing', 'type'])]}")
    sys.exit(1)

# DIAGNOSTIC: Show actual values in the deal type column
print(f"\n1b. Inspecting actual deal type values...")
print(f"   Baseline - Top 20 most common values:")
baseline_top = df_b[deal_col].value_counts().head(20)
for val, count in baseline_top.items():
    pct = count / len(df_b) * 100
    print(f"      '{val}': {count:,} ({pct:.1f}%)")

print(f"\n   Endpoint - Top 20 most common values:")
endpoint_top = df_e[deal_col].value_counts().head(20)
for val, count in endpoint_top.items():
    pct = count / len(df_e) * 100
    print(f"      '{val}': {count:,} ({pct:.1f}%)")

# Check for Series A patterns
print(f"\n   Looking for 'Series A' patterns in baseline:")
series_a_like = df_b[df_b[deal_col].fillna('').str.contains('A', case=False, na=False)][deal_col].value_counts().head(10)
if len(series_a_like) > 0:
    print(f"   Found {len(series_a_like)} unique values containing 'A':")
    for val, count in series_a_like.items():
        print(f"      '{val}': {count:,}")
else:
    print(f"   ⚠️  No values containing 'A' found!")

# Helper functions (from features.py - using SAME regex patterns)
# These patterns match PitchBook's actual format
PAT_A = re.compile(r"(?:\bEarly\s*Stage\s*VC\b|\bSeries\s*A(?:\b|[\s\-]?\d*)\b)", re.I)
PAT_Bp = re.compile(r"(?:\bLater\s*Stage\s*VC\b|\bSeries\s*[B-G](?:\b|[\s\-]?\d*)\b)", re.I)

def _is_A(deal_type: str) -> bool:
    """Check if deal type is Series A or Early Stage VC"""
    return bool(PAT_A.search(deal_type or ""))

def _is_BPLUS(deal_type: str) -> bool:
    """Check if deal type is Series B+ or Later Stage VC"""
    return bool(PAT_Bp.search(deal_type or ""))

# Classify
print(f"\n2. Classifying deal types at baseline...")
df_b['is_A'] = df_b[deal_col].fillna('').apply(_is_A)
df_b['is_BPLUS'] = df_b[deal_col].fillna('').apply(_is_BPLUS)

print(f"\n   Baseline (2022.01) LastFinancing distribution:")
print(f"     Series A only:     {df_b['is_A'].sum():8,} ({df_b['is_A'].mean()*100:5.1f}%)")
print(f"     Series B+ only:    {df_b['is_BPLUS'].sum():8,} ({df_b['is_BPLUS'].mean()*100:5.1f}%)")
print(f"     A or B+ (combined): {(df_b['is_A'] | df_b['is_BPLUS']).sum():8,} ({(df_b['is_A'] | df_b['is_BPLUS']).mean()*100:5.1f}%)")

# Check endpoint
print(f"\n3. Classifying deal types at endpoint...")
df_e['is_A'] = df_e[deal_col].fillna('').apply(_is_A)
df_e['is_BPLUS'] = df_e[deal_col].fillna('').apply(_is_BPLUS)

print(f"\n   Endpoint (2023.12) LastFinancing distribution:")
print(f"     Series A only:     {df_e['is_A'].sum():8,} ({df_e['is_A'].mean()*100:5.1f}%)")
print(f"     Series B+ only:    {df_e['is_BPLUS'].sum():8,} ({df_e['is_BPLUS'].mean()*100:5.1f}%)")

# Merge and analyze
print(f"\n4. Merging and analyzing E/L definitions...")
df_merged = df_b[['CompanyID', 'is_A', 'is_BPLUS', deal_col]].merge(
    df_e[['CompanyID', 'is_A', 'is_BPLUS', deal_col]],
    on='CompanyID',
    how='inner',
    suffixes=('_t1', '_t2')
)

print(f"   Merged: {len(df_merged):,} companies")

# Current definition (NARROW)
df_merged['E_narrow'] = df_merged['is_A_t1'].astype(int)
df_merged['L_narrow'] = df_merged['is_BPLUS_t2'].astype(int)

# Proposed definition (BROAD)
df_merged['E_broad'] = (df_merged['is_A_t1'] | df_merged['is_BPLUS_t1']).astype(int)
df_merged['L_broad'] = (df_merged['is_BPLUS_t2']).astype(int)

print(f"\n5. Comparing definitions...")
print(f"\n   CURRENT (Narrow) Definition:")
print(f"     E=1 (LastFinancing = A at baseline):     {df_merged['E_narrow'].sum():8,} ({df_merged['E_narrow'].mean()*100:5.1f}%)")
print(f"     L=1 (LastFinancing = B+ at endpoint):    {df_merged['L_narrow'].sum():8,} ({df_merged['L_narrow'].mean()*100:5.1f}%)")

print(f"\n   PROPOSED (Broad) Definition:")
print(f"     E=1 (LastFinancing ≥ A at baseline):     {df_merged['E_broad'].sum():8,} ({df_merged['E_broad'].mean()*100:5.1f}%)")
print(f"     L=1 (LastFinancing ≥ B+ at endpoint):    {df_merged['L_broad'].sum():8,} ({df_merged['L_broad'].mean()*100:5.1f}%)")

print(f"\n   DIFFERENCE (who gets reclassified):")
diff = df_merged['E_broad'].sum() - df_merged['E_narrow'].sum()
print(f"     E: +{diff:,} companies ({diff/len(df_merged)*100:.1f}% of total)")
print(f"        These are companies with LastFinancing = B+ at baseline")

# Critical check: Companies who reached B+ before baseline
print(f"\n6. 🚨 CRITICAL: Fast-growing companies excluded by current definition")
fast_growers = df_merged[df_merged['is_BPLUS_t1'] == True]
print(f"   Companies with Series B+ at baseline: {len(fast_growers):,}")
print(f"   Current definition: E=0 for these ← ❌ WRONG?")
print(f"   These companies DID get Series A (earlier), but are excluded!")

# Transition matrix
print(f"\n7. Transition patterns (E → L):")
print(f"\n   CURRENT Definition:")
transition_narrow = pd.crosstab(
    df_merged['E_narrow'],
    df_merged['L_narrow'],
    rownames=['E'],
    colnames=['L'],
    margins=True
)
print(transition_narrow)

print(f"\n   PROPOSED Definition:")
transition_broad = pd.crosstab(
    df_merged['E_broad'],
    df_merged['L_broad'],
    rownames=['E'],
    colnames=['L'],
    margins=True
)
print(transition_broad)

# Impossible cases
print(f"\n8. Logical consistency check:")
impossible = df_merged[(df_merged['E_narrow'] == 0) & (df_merged['L_narrow'] == 1)]
print(f"   E=0 & L=1 (impossible under funnel logic): {len(impossible):,}")
if len(impossible) > 0:
    print(f"   Sample cases:")
    deal_col_t1 = f"{deal_col}_t1"
    deal_col_t2 = f"{deal_col}_t2"
    print(impossible[[deal_col_t1, deal_col_t2]].head(10))

print("\n" + "="*80)
print("ANALYSIS COMPLETE")
print("="*80)

print(f"\nRECOMMENDATION:")
print(f"")
print(f"Current definition excludes {diff:,} companies who received Series A")
print(f"but progressed to Series B+ before baseline.")
print(f"")
print(f"These are SUCCESS cases, not failures!")
print(f"")
print(f"Suggested fix in features.py line 466:")
print(f"  # Old (excludes fast growers):")
print(f"  df['E'] = df['is_A_t1'].fillna(False).astype(int)")
print(f"")
print(f"  # New (includes all who reached Series A):")
print(f"  df['E'] = (df['is_A_t1'] | df['is_BPLUS_t1']).fillna(False).astype(int)")
print(f"")
print(f"This aligns with research question: 'Did company receive early funding?'")
