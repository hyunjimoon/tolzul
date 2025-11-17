"""
Test whether later VC funding (L) was the VERY NEXT round after early funding (E).

This checks if companies had bridge rounds between Series A (baseline) and
Series B+ (endpoint), which would invalidate the step-up calculation.

Run: python test_consecutive_rounds.py
"""

import pandas as pd
import numpy as np
import sys
import re
from pathlib import Path

print("="*80)
print("CONSECUTIVE ROUNDS TEST")
print("="*80)
print("\nPurpose: Check if L funding was immediately after E funding")
print("         (or if there were bridge rounds in between)")

# UPDATE THESE PATHS
baseline_path = "data/raw/Company20220101.dat"
endpoint_path = "data/raw/Company20231201.dat"

print(f"\n1. Loading snapshots...")
try:
    # Try pipe-delimited first (PitchBook format)
    df_b = pd.read_csv(baseline_path, sep='|', low_memory=False)
    df_e = pd.read_csv(endpoint_path, sep='|', low_memory=False)
    print(f"   ✓ Using pipe-delimited format (|)")
except Exception:
    # Fallback to tab-delimited
    try:
        df_b = pd.read_csv(baseline_path, sep='\t', low_memory=False)
        df_e = pd.read_csv(endpoint_path, sep='\t', low_memory=False)
        print(f"   ✓ Using tab-delimited format (\\t)")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        sys.exit(1)

print(f"   ✓ Baseline: {len(df_b):,} companies")
print(f"   ✓ Endpoint: {len(df_e):,} companies")

# Detect deal type column
print(f"\n2. Detecting deal type column...")
possible_names = [
    'LastFinancingDealType',
    'LastDealType',
    'DealType',
    'FundingType',
    'LastFinancingType'
]

deal_col = None
for col in possible_names:
    if col in df_b.columns:
        deal_col = col
        print(f"   ✓ Found: '{deal_col}'")
        break

if deal_col is None:
    print(f"   ✗ Could not find deal type column")
    candidates = [c for c in df_b.columns if any(x in c.lower() for x in ['deal', 'financing', 'type', 'round'])]
    print(f"   Candidates: {candidates[:10]}")
    sys.exit(1)

# Check if we have round number or sequence data
print(f"\n3. Checking for round sequence data...")
round_cols = [c for c in df_b.columns if any(x in c.lower() for x in ['round', 'sequence', 'number', 'count', 'total'])]
print(f"   Found {len(round_cols)} potential round-related columns:")
for col in round_cols[:15]:
    print(f"     • {col}")

# Check for deal/funding history columns
history_cols = [c for c in df_b.columns if any(x in c.lower() for x in ['history', 'all', 'total', 'count', 'num'])]
print(f"\n   Found {len(history_cols)} potential history columns:")
for col in history_cols[:15]:
    print(f"     • {col}")

# Merge to get E→L transitions
print(f"\n4. Identifying E→L transition companies...")

# Classification functions (from features.py - using SAME regex patterns)
# These patterns match PitchBook's actual format
PAT_A = re.compile(r"(?:\bEarly\s*Stage\s*VC\b|\bSeries\s*A(?:\b|[\s\-]?\d*)\b)", re.I)
PAT_Bp = re.compile(r"(?:\bLater\s*Stage\s*VC\b|\bSeries\s*[B-G](?:\b|[\s\-]?\d*)\b)", re.I)

def _is_A(deal_type: str) -> bool:
    """Check if deal type is Series A or Early Stage VC"""
    return bool(PAT_A.search(deal_type or ""))

def _is_BPLUS(deal_type: str) -> bool:
    """Check if deal type is Series B+ or Later Stage VC"""
    return bool(PAT_Bp.search(deal_type or ""))

df_b['is_A'] = df_b[deal_col].fillna('').apply(_is_A)
df_b['is_BPLUS'] = df_b[deal_col].fillna('').apply(_is_BPLUS)
df_e['is_A'] = df_e[deal_col].fillna('').apply(_is_A)
df_e['is_BPLUS'] = df_e[deal_col].fillna('').apply(_is_BPLUS)

# Merge with all available columns
all_cols_b = list(df_b.columns)
all_cols_e = list(df_e.columns)

df_merged = df_b.merge(
    df_e,
    on='CompanyID',
    how='inner',
    suffixes=('_t1', '_t2')
)

# Identify E→L transitions (narrow definition)
E_narrow = df_merged['is_A_t1'] == True
L_narrow = df_merged['is_BPLUS_t2'] == True
E_to_L = df_merged[E_narrow & L_narrow].copy()

print(f"   E→L transitions (narrow): {len(E_to_L):,} companies")
print(f"     (LastFinancing = Series A at baseline → Series B+ at endpoint)")

if len(E_to_L) == 0:
    print(f"\n   ⚠️  No E→L transitions found with narrow definition!")
    print(f"   Try broad definition (E = A or B+ at baseline)...")
    E_broad = (df_merged['is_A_t1'] | df_merged['is_BPLUS_t1']) == True
    E_to_L = df_merged[E_broad & L_narrow].copy()
    print(f"   E→L transitions (broad): {len(E_to_L):,} companies")

# Analyze deal type progression
print(f"\n5. Analyzing deal type progression...")

deal_col_t1 = f"{deal_col}_t1"
deal_col_t2 = f"{deal_col}_t2"

if deal_col_t1 in E_to_L.columns and deal_col_t2 in E_to_L.columns:
    transitions = E_to_L.groupby([deal_col_t1, deal_col_t2]).size().reset_index(name='count')
    transitions = transitions.sort_values('count', ascending=False)

    print(f"\n   Top 20 most common transitions:")
    print(f"   {'Baseline':<25} → {'Endpoint':<25} {'Count':>10}")
    print(f"   {'-'*25}   {'-'*25} {'-'*10}")

    for _, row in transitions.head(20).iterrows():
        print(f"   {str(row[deal_col_t1]):<25} → {str(row[deal_col_t2]):<25} {row['count']:>10,}")

# Check for specific column that might indicate round number
print(f"\n6. Checking for explicit round number/count columns...")

# Common column names that might have this info
candidate_cols = [
    'TotalFundingRounds',
    'NumFundingRounds',
    'FundingRoundCount',
    'RoundNumber',
    'RoundCount',
    'TotalRounds',
    'NumberOfRounds'
]

found_round_col = None
for col in candidate_cols:
    if f"{col}_t1" in df_merged.columns and f"{col}_t2" in df_merged.columns:
        found_round_col = col
        print(f"   ✓ Found round count column: {col}")
        break

if found_round_col:
    col_t1 = f"{found_round_col}_t1"
    col_t2 = f"{found_round_col}_t2"

    E_to_L['round_diff'] = pd.to_numeric(E_to_L[col_t2], errors='coerce') - pd.to_numeric(E_to_L[col_t1], errors='coerce')

    valid_diff = E_to_L['round_diff'].notna()

    if valid_diff.sum() > 0:
        print(f"\n   Round count difference analysis:")
        print(f"     Valid data: {valid_diff.sum():,} companies")
        print(f"\n     Distribution of rounds between snapshots:")
        print(E_to_L['round_diff'].value_counts().sort_index().head(10))

        consecutive = (E_to_L['round_diff'] == 1).sum()
        pct_consecutive = consecutive / valid_diff.sum() * 100 if valid_diff.sum() > 0 else 0

        print(f"\n   🎯 KEY FINDING:")
        print(f"     Exactly 1 round difference (consecutive): {consecutive:,} ({pct_consecutive:.1f}%)")
        print(f"     More than 1 round (bridge rounds): {(E_to_L['round_diff'] > 1).sum():,}")

        if (E_to_L['round_diff'] > 1).sum() > 0:
            print(f"\n   ⚠️  WARNING: Bridge rounds detected!")
            print(f"     These companies may have had intermediate funding between A and B+")
            print(f"     Step-up calculation (PreMoney_t2 / PostMoney_t1) may not reflect true A→B growth")
    else:
        print(f"   ✗ No valid round count data")
else:
    print(f"   ✗ No explicit round count column found")
    print(f"\n   Available columns in merged data:")
    cols_with_round = [c for c in df_merged.columns if 'round' in c.lower()]
    if cols_with_round:
        for c in cols_with_round[:10]:
            print(f"     • {c}")
    else:
        print(f"     (none with 'round' in name)")

# Date-based analysis
print(f"\n7. Checking for date columns to infer round timing...")

date_cols = [c for c in df_b.columns if any(x in c.lower() for x in ['date', 'year', 'time'])]
print(f"   Found {len(date_cols)} date-related columns:")
for col in date_cols[:10]:
    print(f"     • {col}")

# Check if LastFinancingDate exists
last_date_col = None
for col in ['LastFinancingDate', 'LastFundingDate', 'FinancingDate', 'DealDate']:
    if col in df_b.columns:
        last_date_col = col
        print(f"\n   ✓ Found date column: {last_date_col}")
        break

if last_date_col:
    col_t1 = f"{last_date_col}_t1"
    col_t2 = f"{last_date_col}_t2"

    if col_t1 in df_merged.columns and col_t2 in df_merged.columns:
        # Try to parse dates
        df_merged['date_t1'] = pd.to_datetime(df_merged[col_t1], errors='coerce')
        df_merged['date_t2'] = pd.to_datetime(df_merged[col_t2], errors='coerce')

        E_to_L_dates = df_merged[E_narrow & L_narrow].copy()
        E_to_L_dates = E_to_L_dates[E_to_L_dates['date_t1'].notna() & E_to_L_dates['date_t2'].notna()]

        if len(E_to_L_dates) > 0:
            E_to_L_dates['days_between'] = (E_to_L_dates['date_t2'] - E_to_L_dates['date_t1']).dt.days

            print(f"\n   Timing between E and L funding:")
            print(f"     Valid data: {len(E_to_L_dates):,} companies")
            print(f"     Median days: {E_to_L_dates['days_between'].median():.0f}")
            print(f"     Mean days: {E_to_L_dates['days_between'].mean():.0f}")
            print(f"\n     Distribution:")
            print(f"       < 6 months:  {(E_to_L_dates['days_between'] < 180).sum():,}")
            print(f"       6-12 months: {((E_to_L_dates['days_between'] >= 180) & (E_to_L_dates['days_between'] < 365)).sum():,}")
            print(f"       1-2 years:   {((E_to_L_dates['days_between'] >= 365) & (E_to_L_dates['days_between'] < 730)).sum():,}")
            print(f"       > 2 years:   {(E_to_L_dates['days_between'] >= 730).sum():,}")

print("\n" + "="*80)
print("ANALYSIS COMPLETE")
print("="*80)

print(f"\nSUMMARY:")
print(f"")
print(f"To determine if later VC was the VERY NEXT round after early VC:")
print(f"")
if found_round_col:
    print(f"✓ Round count data available → Can detect bridge rounds")
    print(f"  Use: {found_round_col}_t2 - {found_round_col}_t1 == 1 for consecutive")
else:
    print(f"✗ No explicit round count column found")
    print(f"")
    print(f"Alternative approaches:")
    print(f"  1. Request deal-level data (all rounds, not just LastFinancing)")
    print(f"  2. Use date gaps as proxy (but unreliable)")
    print(f"  3. Manually code round numbers from deal type strings")
    print(f"  4. Accept limitation and document in paper")
    print(f"")
    print(f"RECOMMENDATION:")
    print(f"  If >20% of E→L companies had bridge rounds, consider:")
    print(f"    - Censoring them from H3 (step-up) analysis")
    print(f"    - Getting full deal history data")
    print(f"    - Using only companies with consecutive rounds")
