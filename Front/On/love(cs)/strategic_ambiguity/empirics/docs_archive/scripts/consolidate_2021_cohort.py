"""
Consolidate 2021 cohort data with 2023/2024/2025 endpoints

E Definition (Short term survival):
  E is defined as funding amount of companies whose most recent financing
  was Early Stage VC (seriesA) as of Dec 2021, regardless of when that
  financing occurred. This state-based definition captures companies
  currently at the early stage.

L Definition (Long term survival):
  Among the companies with E=1, by year t, did they secure Series B+?
  (t=2023, 2024, 2025).

Creates:
- data/processed/companies_21_23-24-25.parquet (E=1 cohort only)
- data/processed/companies_21_23-24-25_quantum.parquet
- data/processed/companies_21_23-24-25_transportation.parquet

Usage: python scripts/consolidate_2021_cohort.py
"""

import pandas as pd
import re
from pathlib import Path

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

# Pattern for Early Stage VC (Series A)
# Matches: "Early Stage VC", "Series A", "Series A-1", etc.
PAT_E = re.compile(r"(?:\bEarly\s*Stage\s*VC\b|\bSeries\s*A(?:\b|[\s\-]?\d*)\b)", re.I)

# Pattern for Later Stage VC (Series B+)
# Matches: "Later Stage VC", "Series B", "Series C", etc.
PAT_L = re.compile(r"(?:\bLater\s*Stage\s*VC\b|\bSeries\s*[B-G](?:\b|[\s\-]?\d*)\b)", re.I)

# Input files
BASELINE = RAW_DIR / "Company20211201.parquet"
ENDPOINTS = {
    "2023": RAW_DIR / "Company20231201.parquet",
    "2024": RAW_DIR / "Company20241201.parquet",
    "2025": RAW_DIR / "Company20251101.parquet"
}

# Output files
OUTPUT_ALL = PROCESSED_DIR / "companies_21_23-24-25.parquet"
OUTPUT_QUANTUM = PROCESSED_DIR / "companies_21_23-24-25_quantum.parquet"
OUTPUT_TRANSPORTATION = PROCESSED_DIR / "companies_21_23-24-25_transportation.parquet"

print("="*80)
print("CONSOLIDATE 2021 COHORT")
print("="*80)

# Load baseline
print(f"\nLoading baseline (2021.12)...")
if not BASELINE.exists():
    print(f"   ✗ File not found: {BASELINE}")
    exit(1)

df_baseline = pd.read_parquet(BASELINE)
print(f"   ✓ Loaded: {len(df_baseline):,} companies (all)")

# Filter for E=1 cohort (Early Stage VC / Series A only)
print(f"\nFiltering for E=1 cohort (Early Stage VC / Series A)...")
if 'LastFinancingDealType' not in df_baseline.columns:
    print(f"   ✗ ERROR: Column 'LastFinancingDealType' not found!")
    print(f"   Available columns: {list(df_baseline.columns)}")
    exit(1)

# Apply E=1 filter
df_baseline['is_E'] = df_baseline['LastFinancingDealType'].fillna('').apply(
    lambda x: bool(PAT_E.search(str(x)))
)

total_before = len(df_baseline)
df_baseline = df_baseline[df_baseline['is_E'] == True].copy()
df_baseline = df_baseline.drop(columns=['is_E'])  # Remove helper column

print(f"   ✓ Filtered: {len(df_baseline):,} companies with E=1 (from {total_before:,})")
print(f"   Excluded: {total_before - len(df_baseline):,} companies (non-Early Stage VC)")

if len(df_baseline) == 0:
    print(f"\n✗ ERROR: No companies with Early Stage VC in baseline!")
    exit(1)

# Load endpoints
endpoint_dfs = {}
for year, path in ENDPOINTS.items():
    print(f"\nLoading {year} endpoint...")
    if not path.exists():
        print(f"   ⚠️  File not found: {path}, skipping")
        continue

    df = pd.read_parquet(path)
    endpoint_dfs[year] = df
    print(f"   ✓ Loaded: {len(df):,} companies")

if len(endpoint_dfs) == 0:
    print(f"\n✗ No endpoint files found!")
    exit(1)

# Consolidate
print(f"\n" + "="*80)
print("CONSOLIDATING...")
print("="*80)

# Select key columns from baseline
baseline_cols = ['CompanyID']
if 'CompanyName' in df_baseline.columns:
    baseline_cols.append('CompanyName')
if 'LastFinancingDealType' in df_baseline.columns:
    baseline_cols.append('LastFinancingDealType')
if 'LastFinancingSize' in df_baseline.columns:
    baseline_cols.append('LastFinancingSize')
if 'Description' in df_baseline.columns:
    baseline_cols.append('Description')
if 'Keywords' in df_baseline.columns:
    baseline_cols.append('Keywords')

df_consolidated = df_baseline[baseline_cols].copy()

# Rename baseline columns
rename_dict = {}
if 'LastFinancingDealType' in df_consolidated.columns:
    rename_dict['LastFinancingDealType'] = 'DealType_2021'
if 'LastFinancingSize' in df_consolidated.columns:
    rename_dict['LastFinancingSize'] = 'E_amount_2021'
if 'Description' in df_consolidated.columns:
    rename_dict['Description'] = 'Description_2021'
if 'Keywords' in df_consolidated.columns:
    rename_dict['Keywords'] = 'Keywords_2021'

df_consolidated = df_consolidated.rename(columns=rename_dict)

print(f"\nBaseline columns: {baseline_cols}")

# Merge each endpoint
for year, df_end in endpoint_dfs.items():
    print(f"\nMerging {year} endpoint...")

    # Select columns
    merge_cols = ['CompanyID']
    if 'LastFinancingDealType' in df_end.columns:
        merge_cols.append('LastFinancingDealType')

    df_year = df_end[merge_cols].copy()
    df_year = df_year.rename(columns={'LastFinancingDealType': f'DealType_{year}'})

    # Merge
    df_consolidated = df_consolidated.merge(df_year, on='CompanyID', how='left')
    matched = df_consolidated[f'DealType_{year}'].notna().sum()
    print(f"   ✓ Matched: {matched:,} companies")

print(f"\nFinal shape: {len(df_consolidated):,} rows × {len(df_consolidated.columns)} columns")

# Save ALL companies version
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
df_consolidated.to_parquet(OUTPUT_ALL, index=False)
print(f"\n✓ Saved: {OUTPUT_ALL}")

# Create Quantum subset (if quantum-related columns exist)
quantum_keywords = ['quantum', 'qubit', 'superconducting', 'photonic', 'trapped', 'ion']

quantum_mask = pd.Series([False] * len(df_consolidated))
if 'CompanyName' in df_consolidated.columns:
    for keyword in quantum_keywords:
        quantum_mask |= df_consolidated['CompanyName'].str.contains(keyword, case=False, na=False)

df_quantum = df_consolidated[quantum_mask].copy()

if len(df_quantum) > 0:
    df_quantum.to_parquet(OUTPUT_QUANTUM, index=False)
    print(f"✓ Saved: {OUTPUT_QUANTUM} ({len(df_quantum):,} quantum companies)")
else:
    print(f"⚠️  No quantum companies found (searched: {quantum_keywords})")

# Create Transportation subset
transportation_keywords = ['autonomous', 'self-driving', 'vehicle', 'mobility', 'transportation',
                           'automotive', 'truck', 'delivery', 'logistics', 'fleet']

transportation_mask = pd.Series([False] * len(df_consolidated))
if 'CompanyName' in df_consolidated.columns:
    for keyword in transportation_keywords:
        transportation_mask |= df_consolidated['CompanyName'].str.contains(keyword, case=False, na=False)

df_transportation = df_consolidated[transportation_mask].copy()

if len(df_transportation) > 0:
    df_transportation.to_parquet(OUTPUT_TRANSPORTATION, index=False)
    print(f"✓ Saved: {OUTPUT_TRANSPORTATION} ({len(df_transportation):,} transportation companies)")
else:
    print(f"⚠️  No transportation companies found (searched: {transportation_keywords})")

print("\n" + "="*80)
print("CONSOLIDATION COMPLETE")
print("="*80)
