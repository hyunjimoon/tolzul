#!/usr/bin/env python3
"""
Diagnostic script to understand PitchBook snapshot structure.

This will help us design the proper survival variable.
"""

import pandas as pd
from pathlib import Path

# File paths
snapshots = {
    '20211201': 'data/raw/Company20211201.dat',
    '20220101': 'data/raw/Company20220101.dat',
    '20220501': 'data/raw/Company20220501.dat',
    '20230501': 'data/raw/Company20230501.dat'
}

print("="*80)
print("PITCHBOOK SNAPSHOT DIAGNOSTIC")
print("="*80)

# Load all snapshots
dfs = {}
for date, path in snapshots.items():
    if not Path(path).exists():
        print(f"\n❌ File not found: {path}")
        continue

    # Try different encodings
    for encoding in ['utf-8', 'latin-1', 'cp1252']:
        try:
            df = pd.read_csv(path, sep='|', encoding=encoding, low_memory=False)
            dfs[date] = df
            print(f"\n✓ Loaded {date}: {len(df):,} rows, {len(df.columns)} columns")
            print(f"  Encoding: {encoding}")
            break
        except:
            continue

if not dfs:
    print("\n❌ Could not load any snapshots!")
    exit(1)

# Analyze data structure
print("\n" + "="*80)
print("SNAPSHOT COMPARISON")
print("="*80)

# 1. Column analysis
print("\n1. COLUMNS AVAILABLE:")
first_df = list(dfs.values())[0]
print(f"   Total columns: {len(first_df.columns)}")
print(f"   Sample columns: {list(first_df.columns[:20])}")

# Check for key survival indicators
key_cols = ['LastFinancingDate', 'LastFinancingSize', 'CompanyStatus',
            'StatusDate', 'ExitDate', 'ExitType', 'ActiveInactiveStatus']
print("\n   Key survival columns present:")
for col in key_cols:
    present = "✓" if col in first_df.columns else "✗"
    print(f"     {present} {col}")

# 2. Company ID tracking
print("\n2. COMPANY ID TRACKING:")
id_col = 'CompanyID' if 'CompanyID' in first_df.columns else 'company_id'

company_sets = {}
for date, df in dfs.items():
    company_sets[date] = set(df[id_col].dropna().unique())
    print(f"   {date}: {len(company_sets[date]):,} unique companies")

# 3. Overlap analysis
if len(company_sets) >= 2:
    print("\n3. OVERLAP ANALYSIS:")
    dates = sorted(company_sets.keys())

    for i in range(len(dates)-1):
        date1, date2 = dates[i], dates[i+1]
        set1, set2 = company_sets[date1], company_sets[date2]

        both = set1 & set2
        only_first = set1 - set2
        only_second = set2 - set1

        print(f"\n   {date1} → {date2}:")
        print(f"     In both:           {len(both):,} ({len(both)/len(set1)*100:.1f}%)")
        print(f"     Only in {date1}:   {len(only_first):,} ({len(only_first)/len(set1)*100:.1f}%) ← DISAPPEARED?")
        print(f"     Only in {date2}:   {len(only_second):,} ({len(only_second)/len(set2)*100:.1f}%) ← NEW ENTRIES?")

# 4. LastFinancingDate analysis (if available)
if 'LastFinancingDate' in first_df.columns:
    print("\n4. LAST FINANCING DATE ANALYSIS:")

    for date, df in dfs.items():
        df_copy = df.copy()
        df_copy['LastFinancingDate'] = pd.to_datetime(df_copy['LastFinancingDate'], errors='coerce')

        valid_dates = df_copy['LastFinancingDate'].dropna()
        if len(valid_dates) > 0:
            snapshot_date = pd.to_datetime(date, format='%Y%m%d')

            # How many have recent funding (within 24 months)?
            cutoff = snapshot_date - pd.DateOffset(months=24)
            recent_funding = (valid_dates >= cutoff).sum()

            print(f"\n   Snapshot {date} (as of {snapshot_date.date()}):")
            print(f"     Companies with LastFinancingDate: {len(valid_dates):,} ({len(valid_dates)/len(df)*100:.1f}%)")
            print(f"     Recent funding (≤24mo ago):      {recent_funding:,} ({recent_funding/len(valid_dates)*100:.1f}%)")
            print(f"     Oldest LastFinancingDate:         {valid_dates.min().date()}")
            print(f"     Newest LastFinancingDate:         {valid_dates.max().date()}")

# 5. Recommendations
print("\n" + "="*80)
print("RECOMMENDATIONS")
print("="*80)

if len(company_sets) >= 2:
    dates = sorted(company_sets.keys())
    first_set = company_sets[dates[0]]
    last_set = company_sets[dates[-1]]

    growth_rate = len(last_set) / len(first_set) - 1

    if growth_rate > 0.1:  # Database growing by >10%
        print("\n⚠️  DATABASE IS GROWING OVER TIME")
        print("    This is a CUMULATIVE database, not a true panel!")
        print("    → Companies don't 'disappear' - PitchBook adds them retroactively")
        print("\n✓ RECOMMENDED SURVIVAL DEFINITION:")

        if 'LastFinancingDate' in first_df.columns:
            print("    Option A (BEST): Activity-based survival")
            print("      - Baseline: Extract predictors from earliest snapshot")
            print("      - Survival = 1 if LastFinancingDate within X months of endpoint")
            print("      - This captures TRUE business activity")
        else:
            print("    Option B: Use 'later_success' as proxy")
            print("      - Survival = reached Series B+ funding")
            print("      - Document as limitation")
    else:
        print("\n✓ TRUE PANEL STRUCTURE DETECTED")
        print("    Can use presence-based survival (exists in both snapshots)")

print("\n" + "="*80)
