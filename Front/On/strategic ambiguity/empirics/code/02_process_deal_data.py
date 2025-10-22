"""
Script 02: Process Deal Data from Pitchbook
Input: data/raw/Deal*.dat (pipe-delimited files)
Output: data/processed/deal_panel.csv

Steps:
1. Read Deal data files
2. Apply 4-step heuristic to identify Series A/B rounds
3. Create funding success binary variable
4. Create deal panel file
"""

import pandas as pd
from pathlib import Path
from datetime import datetime

# Setup paths
BASE_DIR = Path(__file__).parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

print("=" * 80)
print("SCRIPT 02: PROCESS DEAL DATA")
print("=" * 80)

# Step 1: Read Deal data files
print("\n[Step 1] Reading Deal data files...")
deal_files = list(RAW_DATA_DIR.glob("Deal*.dat"))
print(f"Found {len(deal_files)} Deal files: {[f.name for f in deal_files]}")

dfs = []
for file in deal_files:
    df = pd.read_csv(file, sep='|', encoding='utf-8')
    dfs.append(df)
    print(f"  - {file.name}: {len(df)} rows")

deal_df = pd.concat(dfs, ignore_index=True)
print(f"\nTotal deals loaded: {len(deal_df)}")

# Step 2: Apply 4-step heuristic to identify Series A/B
print("\n[Step 2] Applying 4-step heuristic for Series A/B identification...")

# Convert DealDate to datetime
deal_df['DealDate'] = pd.to_datetime(deal_df['DealDate'])

# Filter 1: Only Early Stage VC or Later Stage VC
print("\n  [2.1] Filter by DealType...")
vc_deals = deal_df[deal_df['DealType'].isin(['Early Stage VC', 'Later Stage VC'])].copy()
print(f"    VC deals: {len(vc_deals)} (filtered from {len(deal_df)})")

# Filter 2: Identify Series A and B by VCRound or sequence
print("\n  [2.2] Identify Series A/B...")

# First attempt: Use VCRound if available
series_a_explicit = vc_deals[vc_deals['VCRound'] == 'Series A'].copy()
series_b_explicit = vc_deals[vc_deals['VCRound'] == 'Series B'].copy()
print(f"    Explicit Series A (from VCRound): {len(series_a_explicit)}")
print(f"    Explicit Series B (from VCRound): {len(series_b_explicit)}")

# For deals without explicit VCRound, use sequence-based heuristic
deals_no_round = vc_deals[~vc_deals['VCRound'].isin(['Series A', 'Series B'])].copy()

if len(deals_no_round) > 0:
    print(f"    Deals without explicit Series A/B: {len(deals_no_round)}")
    print("    Applying sequence-based heuristic (first VC = A, second = B)...")

    # Sort by company and date
    deals_no_round = deals_no_round.sort_values(['CompanyID', 'DealDate'])

    # Assign sequence number
    deals_no_round['sequence'] = deals_no_round.groupby('CompanyID').cumcount() + 1

    # First deal = Series A, Second = Series B
    sequence_a = deals_no_round[deals_no_round['sequence'] == 1].copy()
    sequence_b = deals_no_round[deals_no_round['sequence'] == 2].copy()

    sequence_a['VCRound'] = 'Series A'
    sequence_b['VCRound'] = 'Series B'

    print(f"    Sequence-based Series A: {len(sequence_a)}")
    print(f"    Sequence-based Series B: {len(sequence_b)}")

    # Combine explicit and sequence-based
    all_series_a = pd.concat([series_a_explicit, sequence_a], ignore_index=True)
    all_series_b = pd.concat([series_b_explicit, sequence_b], ignore_index=True)
else:
    all_series_a = series_a_explicit
    all_series_b = series_b_explicit

print(f"\n  Total Series A: {len(all_series_a)}")
print(f"  Total Series B: {len(all_series_b)}")

# Filter 3: Size thresholds (Series A: $2M-$15M, Series B: $10M+)
print("\n  [2.3] Filter by deal size...")
all_series_a['in_size_range'] = (all_series_a['DealSize'] >= 2e6) & (all_series_a['DealSize'] <= 15e6)
all_series_b['in_size_range'] = all_series_b['DealSize'] >= 10e6

# Note: Keep deals with $0 (failed rounds) for analysis
all_series_a.loc[all_series_a['DealSize'] == 0, 'in_size_range'] = True  # Keep failed rounds
all_series_b.loc[all_series_b['DealSize'] == 0, 'in_size_range'] = True

a_in_range = all_series_a['in_size_range'].sum()
b_in_range = all_series_b['in_size_range'].sum()
print(f"    Series A in size range or failed: {a_in_range}/{len(all_series_a)}")
print(f"    Series B in size range or failed: {b_in_range}/{len(all_series_b)}")

# Filter 4: Date filter (Series A: 2021-2022, Series B: 2023-2025)
print("\n  [2.4] Filter by date range...")
all_series_a['in_date_range'] = (all_series_a['DealDate'].dt.year >= 2021) & (all_series_a['DealDate'].dt.year <= 2022)
all_series_b['in_date_range'] = (all_series_b['DealDate'].dt.year >= 2023) & (all_series_b['DealDate'].dt.year <= 2025)

a_in_date = all_series_a['in_date_range'].sum()
b_in_date = all_series_b['in_date_range'].sum()
print(f"    Series A in date range: {a_in_date}/{len(all_series_a)}")
print(f"    Series B in date range: {b_in_date}/{len(all_series_b)}")

# Apply filters
series_a_final = all_series_a[all_series_a['in_size_range'] & all_series_a['in_date_range']].copy()
series_b_final = all_series_b[all_series_b['in_size_range'] & all_series_b['in_date_range']].copy()

print(f"\n  Final Series A deals: {len(series_a_final)}")
print(f"  Final Series B deals: {len(series_b_final)}")

# Step 3: Create funding success variable
print("\n[Step 3] Creating funding success variable...")

series_a_final['round'] = 'Series A'
series_b_final['round'] = 'Series B'

# Funding success: 1 if DealSize > 0, 0 otherwise
series_a_final['funding_success'] = (series_a_final['DealSize'] > 0).astype(int)
series_b_final['funding_success'] = (series_b_final['DealSize'] > 0).astype(int)

print(f"  Series A success rate: {series_a_final['funding_success'].mean():.1%} ({series_a_final['funding_success'].sum()}/{len(series_a_final)})")
print(f"  Series B success rate: {series_b_final['funding_success'].mean():.1%} ({series_b_final['funding_success'].sum()}/{len(series_b_final)})")

# Step 4: Create deal panel file
print("\n[Step 4] Creating deal panel file...")

# Combine Series A and B
deal_panel = pd.concat([series_a_final, series_b_final], ignore_index=True)

# Select and rename columns
deal_panel = deal_panel[[
    'CompanyID', 'round', 'DealType', 'VCRound', 'DealDate',
    'DealSize', 'funding_success', 'Investors', 'PostValuation'
]].copy()

deal_panel.columns = [
    'company_id', 'round', 'deal_type', 'vc_round', 'deal_date',
    'deal_size', 'funding_success', 'investors', 'post_valuation'
]

# Sort by company and round
deal_panel = deal_panel.sort_values(['company_id', 'round'])

# Save to CSV
output_file = PROCESSED_DATA_DIR / "deal_panel.csv"
deal_panel.to_csv(output_file, index=False)
print(f"✓ Saved to: {output_file}")
print(f"  Rows: {len(deal_panel)}")
print(f"  Columns: {len(deal_panel.columns)}")

# Display summary
print("\n" + "=" * 80)
print("SUMMARY STATISTICS")
print("=" * 80)
print(f"\nTotal deals in panel: {len(deal_panel)}")
print(f"Unique companies: {deal_panel['company_id'].nunique()}")
print(f"\nDeals by round:")
print(deal_panel['round'].value_counts())
print(f"\nOverall funding success rate: {deal_panel['funding_success'].mean():.1%}")
print(f"\nFunding success by round:")
print(deal_panel.groupby('round')['funding_success'].agg(['count', 'sum', 'mean']))

print("\n" + "=" * 80)
print("FIRST 5 ROWS")
print("=" * 80)
print(deal_panel[['company_id', 'round', 'deal_size', 'funding_success', 'deal_date']].head())

print("\n" + "=" * 80)
print("✓ SCRIPT 02 COMPLETED SUCCESSFULLY")
print("=" * 80)
