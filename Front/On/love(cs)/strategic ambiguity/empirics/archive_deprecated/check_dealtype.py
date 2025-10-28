#!/usr/bin/env python3
"""
EMERGENCY FIX: Check actual LastFinancingDealType values
"""
import pandas as pd
from pathlib import Path

# Load baseline snapshot
df = pd.read_csv("data/raw/Company20211201.dat", sep='|', encoding='utf-8', low_memory=False)

print("Sample LastFinancingDealType values:")
print(df['LastFinancingDealType'].value_counts().head(30))

print("\n\nSeries A related:")
series_a = df[df['LastFinancingDealType'].str.contains('Series A', case=False, na=False)]
print(f"Count with 'Series A': {len(series_a)}")
print(series_a['LastFinancingDealType'].value_counts().head(20))
