#!/usr/bin/env python3
"""
Debug script to:
1. Check funding success issue (왜 0%인지)
2. Search for target companies
"""
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

# Search for target companies
print("=" * 80)
print("SEARCHING FOR TARGET COMPANIES")
print("=" * 80)

company_file = BASE_DIR / "data" / "processed" / "company_master.csv"
if company_file.exists():
    df = pd.read_csv(company_file)
    print(f"\nLoaded {len(df)} companies")
    
    targets = ["Builder.ai", "builder", "Inflection", "Ghost Autonomy", "ghost"]
    
    for target in targets:
        print(f"\n🔍 Searching for '{target}'...")
        mask = df['company_name'].str.contains(target, case=False, na=False)
        matches = df[mask][['company_id', 'company_name', 'vagueness']].head(10)
        if len(matches) > 0:
            print(f"  Found {len(matches)} matches:")
            for _, row in matches.iterrows():
                print(f"    - {row['company_id']}: {row['company_name']} (vagueness={row['vagueness']})")
        else:
            print(f"  No matches found")
else:
    print(f"❌ {company_file} not found")

# Check deal data for funding_success = 0% issue
print("\n" + "=" * 80)
print("CHECKING DEAL DATA (funding_success = 0% 문제)")
print("=" * 80)

deal_file = BASE_DIR / "data" / "processed" / "deal_master.csv"
if deal_file.exists():
    df = pd.read_csv(deal_file)
    print(f"\nLoaded {len(df)} deals")
    print(f"Columns: {df.columns.tolist()}")
    
    if 'funding_success' in df.columns:
        print(f"\nFunding success: {df['funding_success'].sum()}/{len(df)} = {df['funding_success'].mean():.1%}")
    
    # Check status columns
    status_cols = [c for c in df.columns if 'status' in c.lower()]
    print(f"\nStatus columns: {status_cols}")
    
    if status_cols:
        for col in status_cols:
            print(f"\n{col} value counts:")
            print(df[col].value_counts().head(5))
    
    # Check size columns
    size_cols = [c for c in df.columns if 'size' in c.lower()]
    print(f"\nSize columns: {size_cols}")
    
    if size_cols:
        for col in size_cols:
            print(f"\n{col} stats:")
            print(f"  Non-zero: {(df[col] > 0).sum()}/{len(df)}")
            print(f"  Mean: ${df[col].mean():,.0f}")
else:
    print(f"❌ {deal_file} not found - run step 2 first")
