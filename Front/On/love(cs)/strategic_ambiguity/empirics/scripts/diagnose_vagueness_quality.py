"""
Diagnose Vagueness Quality

Problem: Vagueness std=4.37 is too small (mean=49.17)
This suggests Description/Keywords may be:
- Mostly empty
- Identical across companies
- Not properly loaded

This script:
1. Checks Description/Keywords availability
2. Samples actual content
3. Analyzes vagueness distribution
4. Identifies data quality issues

Usage: python scripts/diagnose_vagueness_quality.py
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys
import re

# Add parent directory for modules
sys.path.insert(0, str(Path(__file__).parent.parent))

# Paths
PROCESSED_DIR = Path("data/processed")
INPUT_FILE = PROCESSED_DIR / "companies_21_23-24-25.parquet"

print("="*80)
print("VAGUENESS QUALITY DIAGNOSIS")
print("="*80)

# Load data
print(f"\nLoading: {INPUT_FILE.name}")
if not INPUT_FILE.exists():
    print(f"✗ File not found!")
    print(f"\nRun: python scripts/consolidate_2021_cohort.py")
    sys.exit(1)

df = pd.read_parquet(INPUT_FILE)
print(f"✓ Loaded: {len(df):,} companies")

# ============================================================================
# TEST 1: Column Availability
# ============================================================================

print(f"\n" + "="*80)
print("TEST 1: Column Availability")
print("="*80)

print(f"\nColumns in dataset: {len(df.columns)}")
print(f"  {list(df.columns)}")

has_desc = 'Description_2021' in df.columns
has_keywords = 'Keywords_2021' in df.columns

print(f"\nRequired columns:")
print(f"  Description_2021: {'✓ FOUND' if has_desc else '✗ NOT FOUND'}")
print(f"  Keywords_2021:    {'✓ FOUND' if has_keywords else '✗ NOT FOUND'}")

if not has_desc or not has_keywords:
    print(f"\n✗ CRITICAL: Missing required columns for vagueness computation!")
    print(f"\nRecommendation:")
    print(f"  1. Check that consolidate_2021_cohort.py includes Description and Keywords")
    print(f"  2. Verify raw data files have Description and Keywords columns")
    print(f"  3. Re-run consolidation: python scripts/consolidate_2021_cohort.py")
    sys.exit(1)

# ============================================================================
# TEST 2: Non-Empty Rates
# ============================================================================

print(f"\n" + "="*80)
print("TEST 2: Non-Empty Rates")
print("="*80)

# Description
desc_nonempty = df['Description_2021'].fillna('').str.len() > 0
desc_rate = desc_nonempty.mean()

print(f"\nDescription_2021:")
print(f"  Non-empty: {desc_nonempty.sum():,} / {len(df):,} ({desc_rate:.1%})")
print(f"  Empty:     {(~desc_nonempty).sum():,} / {len(df):,} ({(1-desc_rate):.1%})")

# Keywords
keywords_nonempty = df['Keywords_2021'].fillna('').str.len() > 0
keywords_rate = keywords_nonempty.mean()

print(f"\nKeywords_2021:")
print(f"  Non-empty: {keywords_nonempty.sum():,} / {len(df):,} ({keywords_rate:.1%})")
print(f"  Empty:     {(~keywords_nonempty).sum():,} / {len(df):,} ({(1-keywords_rate):.1%})")

# Both
both_nonempty = desc_nonempty & keywords_nonempty
both_rate = both_nonempty.mean()

print(f"\nBoth non-empty:")
print(f"  Count: {both_nonempty.sum():,} / {len(df):,} ({both_rate:.1%})")

if desc_rate < 0.5 or keywords_rate < 0.5:
    print(f"\n⚠️  WARNING: Low non-empty rate!")
    print(f"   This will result in low vagueness variance")

# ============================================================================
# TEST 3: Sample Content
# ============================================================================

print(f"\n" + "="*80)
print("TEST 3: Sample Content (First 10 Companies)")
print("="*80)

# Sample companies with both Description and Keywords
sample_df = df[both_nonempty].head(10)

for idx, row in sample_df.iterrows():
    print(f"\nCompany: {row.get('CompanyName', 'N/A')}")

    desc = str(row['Description_2021'])
    desc_preview = desc[:150] + "..." if len(desc) > 150 else desc
    print(f"  Description: {desc_preview}")

    keywords = str(row['Keywords_2021'])
    keywords_preview = keywords[:100] + "..." if len(keywords) > 100 else keywords
    print(f"  Keywords: {keywords_preview}")

# ============================================================================
# TEST 4: Length Statistics
# ============================================================================

print(f"\n" + "="*80)
print("TEST 4: Length Statistics")
print("="*80)

# Description length
desc_lengths = df['Description_2021'].fillna('').str.len()

print(f"\nDescription_2021 length:")
print(f"  Mean:   {desc_lengths.mean():.0f} characters")
print(f"  Median: {desc_lengths.median():.0f} characters")
print(f"  Min:    {desc_lengths.min():.0f} characters")
print(f"  Max:    {desc_lengths.max():.0f} characters")
print(f"  Std:    {desc_lengths.std():.0f} characters")

# Keywords length
keywords_lengths = df['Keywords_2021'].fillna('').str.len()

print(f"\nKeywords_2021 length:")
print(f"  Mean:   {keywords_lengths.mean():.0f} characters")
print(f"  Median: {keywords_lengths.median():.0f} characters")
print(f"  Min:    {keywords_lengths.min():.0f} characters")
print(f"  Max:    {keywords_lengths.max():.0f} characters")
print(f"  Std:    {keywords_lengths.std():.0f} characters")

# ============================================================================
# TEST 5: Vagueness Computation
# ============================================================================

print(f"\n" + "="*80)
print("TEST 5: Vagueness Computation and Distribution")
print("="*80)

try:
    from modules.features import compute_vagueness_vectorized

    print(f"\nComputing vagueness for all {len(df):,} companies...")
    df['V'] = compute_vagueness_vectorized(
        df['Description_2021'].fillna(''),
        df['Keywords_2021'].fillna('')
    )

    print(f"✓ Vagueness computed")

    # Statistics
    print(f"\nVagueness distribution:")
    print(f"  Mean:   {df['V'].mean():.2f}")
    print(f"  Median: {df['V'].median():.2f}")
    print(f"  Std:    {df['V'].std():.2f}")  # ← KEY METRIC
    print(f"  Min:    {df['V'].min():.2f}")
    print(f"  Max:    {df['V'].max():.2f}")

    # Percentiles
    print(f"\nPercentiles:")
    for pct in [5, 25, 50, 75, 95]:
        val = df['V'].quantile(pct/100)
        print(f"  {pct:2d}%: {val:.2f}")

    # Check if std is too small
    if df['V'].std() < 5:
        print(f"\n⚠️  WARNING: Vagueness std ({df['V'].std():.2f}) is TOO SMALL!")
        print(f"\n   Possible causes:")
        print(f"   1. Descriptions/Keywords are too similar")
        print(f"   2. Most entries are empty (vagueness defaults to 0 or constant)")
        print(f"   3. Vagueness scorer not working correctly")

        # Analyze zero-variance issue
        print(f"\n   Checking for constant values...")

        unique_vals = df['V'].nunique()
        print(f"   Unique vagueness values: {unique_vals:,}")

        if unique_vals < 100:
            print(f"   ⚠️  Very few unique values! Showing value counts:")
            print(df['V'].value_counts().head(10))

        # Check empty entries
        empty_both = (~desc_nonempty) & (~keywords_nonempty)
        print(f"\n   Companies with empty Description AND Keywords: {empty_both.sum():,} ({empty_both.mean():.1%})")

        if empty_both.mean() > 0.5:
            print(f"   ⚠️  More than 50% have empty Description/Keywords!")
            print(f"   This causes low variance in vagueness scores")

    elif df['V'].std() < 10:
        print(f"\n⚠️  WARNING: Vagueness std ({df['V'].std():.2f}) is SMALL")
        print(f"   Expected std: 15-25 for real venture data")
        print(f"   Current std indicates limited variation")

    else:
        print(f"\n✓ Vagueness std ({df['V'].std():.2f}) looks reasonable")

    # Histogram
    print(f"\nVagueness histogram (10 bins):")
    hist, bins = np.histogram(df['V'], bins=10)
    for i, (count, left, right) in enumerate(zip(hist, bins[:-1], bins[1:])):
        bar = '█' * int(count / hist.max() * 50)
        print(f"  [{left:5.1f} - {right:5.1f}]: {count:6,} {bar}")

except Exception as e:
    print(f"✗ Vagueness computation failed: {e}")
    import traceback
    traceback.print_exc()

# ============================================================================
# TEST 6: Sample Vagueness Scores
# ============================================================================

print(f"\n" + "="*80)
print("TEST 6: Sample Vagueness Scores (Extreme Values)")
print("="*80)

if 'V' in df.columns:
    # Lowest vagueness
    print(f"\nLowest vagueness (most concrete):")
    lowest = df.nsmallest(5, 'V')
    for idx, row in lowest.iterrows():
        print(f"\n  V = {row['V']:.2f} | {row.get('CompanyName', 'N/A')}")
        desc = str(row['Description_2021'])[:100]
        keywords = str(row['Keywords_2021'])[:80]
        print(f"    Desc: {desc}...")
        print(f"    Keys: {keywords}...")

    # Highest vagueness
    print(f"\nHighest vagueness (most vague):")
    highest = df.nlargest(5, 'V')
    for idx, row in highest.iterrows():
        print(f"\n  V = {row['V']:.2f} | {row.get('CompanyName', 'N/A')}")
        desc = str(row['Description_2021'])[:100]
        keywords = str(row['Keywords_2021'])[:80]
        print(f"    Desc: {desc}...")
        print(f"    Keys: {keywords}...")

# ============================================================================
# SUMMARY
# ============================================================================

print(f"\n" + "="*80)
print("DIAGNOSIS SUMMARY")
print("="*80)

if 'V' in df.columns:
    std_v = df['V'].std()

    if std_v < 5:
        print(f"\n✗ CRITICAL ISSUE: Vagueness std = {std_v:.2f} (expected 15-25)")
        print(f"\nLikely causes:")
        print(f"  1. Description/Keywords are mostly empty ({desc_rate:.1%} / {keywords_rate:.1%} non-empty)")
        print(f"  2. Content is too homogeneous (all companies sound similar)")
        print(f"  3. Vagueness scorer returns near-constant values")

        print(f"\nRecommendations:")
        print(f"  1. CHECK RAW DATA: Verify source files have real Description/Keywords")
        print(f"  2. CONSOLIDATION: Ensure Description/Keywords are included")
        print(f"     - Open data/raw/Company20211201.parquet")
        print(f"     - Check if Description and Keywords columns exist")
        print(f"     - Check if they have meaningful content")
        print(f"  3. VAGUENESS SCORER: Review modules/features.py StrategicVaguenessScorer")

    elif std_v < 10:
        print(f"\n⚠️  WARNING: Vagueness std = {std_v:.2f} (expected 15-25)")
        print(f"\nSuggestions:")
        print(f"  - Review sample descriptions/keywords above")
        print(f"  - Check if content is too standardized")

    else:
        print(f"\n✓ Vagueness std = {std_v:.2f} looks reasonable")
        print(f"  Data quality appears acceptable for analysis")

else:
    print(f"\n✗ Vagueness computation failed - cannot assess quality")

print()
