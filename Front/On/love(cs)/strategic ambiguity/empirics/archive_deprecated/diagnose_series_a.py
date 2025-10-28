#!/usr/bin/env python3
"""
Diagnostic: Check actual LastFinancingDealType values in data
Run this and copy the output to ChatGPT
"""
import pandas as pd
from pathlib import Path

# Load baseline snapshot
print("Loading Company20211201.dat...")
df = pd.read_csv("data/raw/Company20211201.dat", sep='|', encoding='utf-8', low_memory=False)

print(f"\nTotal rows: {len(df):,}")
print(f"Total columns: {len(df.columns)}")

# Check LastFinancingDealType column
print("\n" + "="*80)
print("TOP 50 LastFinancingDealType VALUES (most common):")
print("="*80)
print(df['LastFinancingDealType'].value_counts().head(50))

# Check for Series A patterns
print("\n" + "="*80)
print("CHECKING FOR 'SERIES A' PATTERNS:")
print("="*80)

# Try different patterns
patterns_to_check = [
    'Series A',
    'series a',
    'SERIES A',
    'Series A-',
    'Early Stage',
    'Seed',
    'Angel'
]

for pattern in patterns_to_check:
    count = df['LastFinancingDealType'].fillna("").str.contains(pattern, case=False, na=False).sum()
    if count > 0:
        print(f"✓ Pattern '{pattern}': {count:,} companies")
        # Show sample values
        sample = df[df['LastFinancingDealType'].fillna("").str.contains(pattern, case=False, na=False)]['LastFinancingDealType'].value_counts().head(5)
        print(f"  Sample values: {list(sample.index)}")
    else:
        print(f"✗ Pattern '{pattern}': 0 companies")

# Check CompanyFinancingStatus
print("\n" + "="*80)
print("CompanyFinancingStatus VALUES:")
print("="*80)
print(df['CompanyFinancingStatus'].value_counts().head(20))

# Show sample of companies that are VC-backed
print("\n" + "="*80)
print("SAMPLE: VC-BACKED COMPANIES' DEAL TYPES:")
print("="*80)
vc_backed = df[df['CompanyFinancingStatus'] == 'Venture Capital-Backed']
print(f"VC-backed count: {len(vc_backed):,}")
print("\nTheir LastFinancingDealType distribution:")
print(vc_backed['LastFinancingDealType'].value_counts().head(30))

print("\n" + "="*80)
print("COPY ALL OUTPUT ABOVE TO CHATGPT")
print("="*80)
