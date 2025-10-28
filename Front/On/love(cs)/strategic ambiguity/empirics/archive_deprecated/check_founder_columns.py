#!/usr/bin/env python3
"""
Check available columns for Founder Credibility feature engineering
"""
import pandas as pd

# Load baseline snapshot
df = pd.read_csv("data/raw/Company20211201.dat", sep='|', encoding='utf-8', low_memory=False)

print("="*80)
print("COLUMN CHECK FOR FOUNDER CREDIBILITY")
print("="*80)
print(f"\nTotal columns: {len(df.columns)}")

# Check for founder-related columns
founder_cols = [col for col in df.columns if any(keyword in col.lower()
                for keyword in ['primary', 'contact', 'founder', 'ceo', 'owner'])]

print("\n📋 Founder-related columns:")
for col in founder_cols:
    n_valid = df[col].notna().sum()
    n_unique = df[col].nunique()
    print(f"  - {col}: {n_valid:,} valid ({n_unique:,} unique)")
    if n_unique < 20:  # Show sample values for categorical
        print(f"    Sample values: {df[col].value_counts().head(5).to_dict()}")

# Check BusinessStatus
print("\n📋 BusinessStatus:")
if 'BusinessStatus' in df.columns:
    print(df['BusinessStatus'].value_counts().head(20))
else:
    print("  ❌ BusinessStatus column not found")

# Check for ID columns
print("\n📋 ID-related columns:")
id_cols = [col for col in df.columns if 'id' in col.lower() or 'pbid' in col.lower()]
for col in id_cols[:10]:  # Show first 10
    n_valid = df[col].notna().sum()
    n_unique = df[col].nunique()
    print(f"  - {col}: {n_valid:,} valid ({n_unique:,} unique)")
