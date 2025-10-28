"""
Script 02: Process Deal Data from Pitchbook (REAL FORMAT)
Input: data/raw/Deal*.dat (pipe-delimited files with full Pitchbook schema)
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
print("SCRIPT 02: PROCESS DEAL DATA (Real Pitchbook Format)")
print("=" * 80)

# Step 1: Read Deal data files
print("\n[Step 1] Reading Deal data files...")
deal_files = list(RAW_DATA_DIR.glob("Deal*.dat"))
print(f"Found {len(deal_files)} Deal files: {[f.name for f in deal_files]}")

if len(deal_files) == 0:
    print("\n❌ ERROR: No Deal*.dat files found in data/raw/")
    print("\n📋 Expected file pattern: Deal*.dat (e.g., Deal2023.dat)")
    print(f"   Looking in: {RAW_DATA_DIR}")
    print("\n   Available files in data/raw/:")
    all_files = list(RAW_DATA_DIR.glob("*.dat"))
    for f in all_files:
        print(f"     - {f.name}")
    print("\n💡 To fix this:")
    print("   1. Download Deal data files from Pitchbook")
    print("   2. Place them in data/raw/ directory")
    print("   3. Files should be named Deal*.dat (pipe-delimited)")
    print("\n   Or if you have combined Company+Deal files:")
    print("   1. Split the data into separate Company*.dat and Deal*.dat files")
    print("   2. Ensure Deal files have the proper schema (see Deal header example)")
    print("\n⏸️  Creating empty deal panel for now...")

    # Create empty deal panel with proper schema
    deal_panel = pd.DataFrame(columns=[
        'company_id', 'company_name', 'round', 'deal_type', 'vc_round', 'deal_date',
        'deal_size', 'funding_success', 'investors', 'post_valuation'
    ])
    output_file = PROCESSED_DATA_DIR / "deal_panel.csv"
    deal_panel.to_csv(output_file, index=False)
    print(f"✓ Created empty deal panel: {output_file}")
    print("\n" + "=" * 80)
    print("⚠️  SCRIPT 02: INCOMPLETE - NO DEAL DATA FOUND")
    print("=" * 80)
    exit(0)

dfs = []
for file in deal_files:
    df = pd.read_csv(file, sep='|', encoding='utf-8', low_memory=False)
    print(f"  - {file.name}: {len(df)} rows, {len(df.columns)} columns")
    dfs.append(df)

deal_df = pd.concat(dfs, ignore_index=True)
print(f"\nTotal deals loaded: {len(deal_df)}")

# Step 2: Apply 4-step heuristic to identify Series A/B
print("\n[Step 2] Applying 4-step heuristic for Series A/B identification...")

# Convert DealDate to datetime
deal_df['DealDate'] = pd.to_datetime(deal_df['DealDate'], errors='coerce')

# Filter 1: Only Early Stage VC or Later Stage VC
print("\n  [2.1] Filter by DealType...")
vc_deals = deal_df[deal_df['DealType'].isin(['Early Stage VC', 'Later Stage VC'])].copy()
print(f"    VC deals: {len(vc_deals)} (filtered from {len(deal_df)})")

# Filter 2: Identify Series A and B by VCRound
print("\n  [2.2] Identify Series A/B...")

# Use VCRound column (Series A, Series B, Series C, etc.)
series_a_explicit = vc_deals[vc_deals['VCRound'].str.contains('Series A', case=False, na=False)].copy()
series_b_explicit = vc_deals[vc_deals['VCRound'].str.contains('Series B', case=False, na=False)].copy()

print(f"    Explicit Series A (from VCRound): {len(series_a_explicit)}")
print(f"    Explicit Series B (from VCRound): {len(series_b_explicit)}")

# For deals without explicit VCRound, use sequence-based heuristic
deals_no_series = vc_deals[~vc_deals['VCRound'].str.contains('Series', case=False, na=False)].copy()

if len(deals_no_series) > 0:
    print(f"    Deals without Series label: {len(deals_no_series)}")
    print("    Applying sequence-based heuristic...")

    # Sort by company and date
    deals_no_series = deals_no_series.sort_values(['CompanyID', 'DealDate'])

    # Assign sequence number per company
    deals_no_series['sequence'] = deals_no_series.groupby('CompanyID').cumcount() + 1

    # First VC deal = Series A, Second = Series B
    sequence_a = deals_no_series[deals_no_series['sequence'] == 1].copy()
    sequence_b = deals_no_series[deals_no_series['sequence'] == 2].copy()

    sequence_a['VCRound'] = 'Series A'
    sequence_b['VCRound'] = 'Series B'

    print(f"    Sequence-based Series A: {len(sequence_a)}")
    print(f"    Sequence-based Series B: {len(sequence_b)}")

    # Combine
    all_series_a = pd.concat([series_a_explicit, sequence_a], ignore_index=True)
    all_series_b = pd.concat([series_b_explicit, sequence_b], ignore_index=True)
else:
    all_series_a = series_a_explicit
    all_series_b = series_b_explicit

print(f"\n  Total Series A: {len(all_series_a)}")
print(f"  Total Series B: {len(all_series_b)}")

# Filter 3: Size thresholds (relaxed for real data)
print("\n  [2.3] Filter by deal size (relaxed thresholds)...")
all_series_a['DealSize'] = pd.to_numeric(all_series_a['DealSize'], errors='coerce').fillna(0)
all_series_b['DealSize'] = pd.to_numeric(all_series_b['DealSize'], errors='coerce').fillna(0)

# More lenient size filters for Series A/B
# Keep all deals with DealSize > 0 or explicitly marked as Series A/B
all_series_a['in_size_range'] = (all_series_a['DealSize'] >= 1e6) | (all_series_a['DealSize'] == 0)
all_series_b['in_size_range'] = (all_series_b['DealSize'] >= 5e6) | (all_series_b['DealSize'] == 0)

a_in_range = all_series_a['in_size_range'].sum()
b_in_range = all_series_b['in_size_range'].sum()
print(f"    Series A meeting size criteria: {a_in_range}/{len(all_series_a)}")
print(f"    Series B meeting size criteria: {b_in_range}/{len(all_series_b)}")

# Filter 4: Date filter (2020-2025 for both for broader capture)
print("\n  [2.4] Filter by date range...")
all_series_a['in_date_range'] = (all_series_a['DealDate'].dt.year >= 2020) & (all_series_a['DealDate'].dt.year <= 2025)
all_series_b['in_date_range'] = (all_series_b['DealDate'].dt.year >= 2020) & (all_series_b['DealDate'].dt.year <= 2025)

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

# Funding success: 1 if DealSize > 0 and DealStatus == Completed
series_a_final['funding_success'] = (
    (series_a_final['DealSize'] > 0) &
    (series_a_final['DealStatus'].str.contains('Completed', case=False, na=False))
).astype(int)

series_b_final['funding_success'] = (
    (series_b_final['DealSize'] > 0) &
    (series_b_final['DealStatus'].str.contains('Completed', case=False, na=False))
).astype(int)

print(f"  Series A success rate: {series_a_final['funding_success'].mean():.1%} ({series_a_final['funding_success'].sum()}/{len(series_a_final)})")
print(f"  Series B success rate: {series_b_final['funding_success'].mean():.1%} ({series_b_final['funding_success'].sum()}/{len(series_b_final)})")

# Step 4: Create deal panel file
print("\n[Step 4] Creating deal panel file...")

# Combine Series A and B
deal_panel = pd.concat([series_a_final, series_b_final], ignore_index=True)

# Select and rename columns
deal_panel = deal_panel[[
    'CompanyID', 'CompanyName', 'round', 'DealType', 'VCRound', 'DealDate',
    'DealSize', 'funding_success', 'Investors', 'PostValuation'
]].copy()

deal_panel.columns = [
    'company_id', 'company_name', 'round', 'deal_type', 'vc_round', 'deal_date',
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
print(deal_panel[['company_id', 'company_name', 'round', 'deal_size', 'funding_success', 'deal_date']].head())

print("\n" + "=" * 80)
print("TARGET COMPANIES (if found):")
print("=" * 80)
target_companies = ['Anthropic', 'Stability AI', 'Inflection', 'Character']
for target in target_companies:
    matches = deal_panel[deal_panel['company_name'].str.contains(target, case=False, na=False)]
    if len(matches) > 0:
        print(f"\n✓ {target} FOUND - {len(matches)} deals:")
        for _, row in matches.iterrows():
            print(f"  - {row['round']}: ${row['deal_size']/1e6:.1f}M ({row['deal_date']}), Success={row['funding_success']}")
    else:
        print(f"\n✗ {target} NOT FOUND")

print("\n" + "=" * 80)
print("✓ SCRIPT 02 COMPLETED SUCCESSFULLY")
print("=" * 80)


def process_deal_data(series_a_start='2021-01-01', series_a_end='2022-10-31',
                     series_b_start='2023-05-01', series_b_end='2025-10-31'):
    """
    Process Deal data with date filtering and return DataFrame

    Args:
        series_a_start: Start date for Series A filtering
        series_a_end: End date for Series A filtering
        series_b_start: Start date for Series B filtering
        series_b_end: End date for Series B filtering

    Returns:
        pd.DataFrame: Deal panel with Series A/B deals and funding success
    """
    # Read Deal data files
    deal_files = list(RAW_DATA_DIR.glob("Deal*.dat"))

    if len(deal_files) == 0:
        print("\n❌ WARNING: No Deal*.dat files found in data/raw/")
        print(f"   Looking in: {RAW_DATA_DIR}")
        all_files = list(RAW_DATA_DIR.glob("*.dat"))
        if all_files:
            print(f"   Available files: {[f.name for f in all_files]}")
        print("\n💡 Please add Deal*.dat files to data/raw/ directory")
        print("   Returning empty deal panel...")
        # Return empty dataframe with proper schema
        return pd.DataFrame(columns=[
            'company_id', 'company_name', 'round', 'deal_type', 'vc_round', 'deal_date',
            'deal_size', 'funding_success', 'investors', 'post_valuation'
        ])

    dfs = []
    for file in deal_files:
        df = pd.read_csv(file, sep='|', encoding='utf-8', low_memory=False)
        dfs.append(df)

    if len(dfs) == 0:
        return pd.DataFrame(columns=[
            'company_id', 'company_name', 'round', 'deal_type', 'vc_round', 'deal_date',
            'deal_size', 'funding_success', 'investors', 'post_valuation'
        ])

    deal_df = pd.concat(dfs, ignore_index=True)

    # Convert DealDate to datetime
    deal_df['DealDate'] = pd.to_datetime(deal_df['DealDate'], errors='coerce')

    # Filter to VC deals
    vc_deals = deal_df[deal_df['DealType'].isin(['Early Stage VC', 'Later Stage VC'])].copy()

    # Identify Series A and B
    series_a_explicit = vc_deals[vc_deals['VCRound'].str.contains('Series A', case=False, na=False)].copy()
    series_b_explicit = vc_deals[vc_deals['VCRound'].str.contains('Series B', case=False, na=False)].copy()

    # For deals without explicit VCRound, use sequence-based heuristic
    deals_no_series = vc_deals[~vc_deals['VCRound'].str.contains('Series', case=False, na=False)].copy()

    if len(deals_no_series) > 0:
        deals_no_series = deals_no_series.sort_values(['CompanyID', 'DealDate'])
        deals_no_series['sequence'] = deals_no_series.groupby('CompanyID').cumcount() + 1

        sequence_a = deals_no_series[deals_no_series['sequence'] == 1].copy()
        sequence_b = deals_no_series[deals_no_series['sequence'] == 2].copy()

        sequence_a['VCRound'] = 'Series A'
        sequence_b['VCRound'] = 'Series B'

        all_series_a = pd.concat([series_a_explicit, sequence_a], ignore_index=True)
        all_series_b = pd.concat([series_b_explicit, sequence_b], ignore_index=True)
    else:
        all_series_a = series_a_explicit
        all_series_b = series_b_explicit

    # Filter by date ranges
    series_a_final = all_series_a[
        (all_series_a['DealDate'] >= series_a_start) &
        (all_series_a['DealDate'] <= series_a_end)
    ].copy()

    series_b_final = all_series_b[
        (all_series_b['DealDate'] >= series_b_start) &
        (all_series_b['DealDate'] <= series_b_end)
    ].copy()

    # Add round labels
    series_a_final['round'] = 'Series A'
    series_b_final['round'] = 'Series B'

    # Convert DealSize to numeric
    series_a_final['DealSize'] = pd.to_numeric(series_a_final['DealSize'], errors='coerce').fillna(0)
    series_b_final['DealSize'] = pd.to_numeric(series_b_final['DealSize'], errors='coerce').fillna(0)

    # Create funding success variable
    series_a_final['funding_success'] = (
        (series_a_final['DealSize'] > 0) &
        (series_a_final['DealStatus'].str.contains('Completed', case=False, na=False))
    ).astype(int)

    series_b_final['funding_success'] = (
        (series_b_final['DealSize'] > 0) &
        (series_b_final['DealStatus'].str.contains('Completed', case=False, na=False))
    ).astype(int)

    # Combine Series A and B
    deal_panel = pd.concat([series_a_final, series_b_final], ignore_index=True)

    # Select and rename columns
    deal_panel = deal_panel[[
        'CompanyID', 'CompanyName', 'round', 'DealType', 'VCRound', 'DealDate',
        'DealSize', 'funding_success', 'Investors', 'PostValuation'
    ]].copy()

    deal_panel.columns = [
        'company_id', 'company_name', 'round', 'deal_type', 'vc_round', 'deal_date',
        'deal_size', 'funding_success', 'investors', 'post_valuation'
    ]

    deal_panel = deal_panel.sort_values(['company_id', 'round'])

    return deal_panel
