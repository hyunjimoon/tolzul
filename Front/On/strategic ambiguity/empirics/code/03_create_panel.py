"""
Script 03: Create Analysis Panel
Input: data/processed/company_master.csv + data/processed/deal_panel.csv
Output: data/processed/analysis_panel.csv

Steps:
1. Read company master and deal panel files
2. Join company data with deal data
3. Create panel structure (each firm × 2 rounds)
4. Add derived variables
5. Save analysis panel
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Setup paths
BASE_DIR = Path(__file__).parent.parent
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

print("=" * 80)
print("SCRIPT 03: CREATE ANALYSIS PANEL")
print("=" * 80)

# Step 1: Read processed files
print("\n[Step 1] Reading processed files...")
company_file = PROCESSED_DATA_DIR / "company_master.csv"
deal_file = PROCESSED_DATA_DIR / "deal_panel.csv"

company_df = pd.read_csv(company_file)
deal_df = pd.read_csv(deal_file)

print(f"  Company master: {len(company_df)} firms")
print(f"  Deal panel: {len(deal_df)} deals")

# Step 2: Join company and deal data
print("\n[Step 2] Joining company and deal data...")

# Merge on company_id
panel_df = deal_df.merge(
    company_df,
    on='company_id',
    how='inner'
)

print(f"  Merged panel: {len(panel_df)} observations")
print(f"  Unique firms: {panel_df['company_id'].nunique()}")

# Check for firms without both rounds
firms_with_both = panel_df.groupby('company_id')['round'].count()
firms_complete = (firms_with_both == 2).sum()
firms_partial = (firms_with_both == 1).sum()

print(f"  Firms with both A and B: {firms_complete}")
print(f"  Firms with only one round: {firms_partial}")

# Step 3: Create panel structure
print("\n[Step 3] Creating panel structure...")

# For firms with only Series A, create a missing Series B record
companies_with_a_only = panel_df[panel_df['round'] == 'Series A']['company_id'].unique()
companies_with_both_rounds = panel_df.groupby('company_id').filter(lambda x: len(x) == 2)['company_id'].unique()
companies_missing_b = set(companies_with_a_only) - set(companies_with_both_rounds)

print(f"  Companies missing Series B: {len(companies_missing_b)}")

if len(companies_missing_b) > 0:
    # Create Series B records for companies that only have Series A
    missing_b_records = []

    for company_id in companies_missing_b:
        # Get Series A record for this company
        series_a_record = panel_df[
            (panel_df['company_id'] == company_id) &
            (panel_df['round'] == 'Series A')
        ].iloc[0].to_dict()

        # Create Series B record with same firm characteristics but no funding
        series_b_record = series_a_record.copy()
        series_b_record['round'] = 'Series B'
        series_b_record['funding_success'] = 0  # No Series B funding
        series_b_record['deal_size'] = 0
        series_b_record['deal_date'] = pd.NaT
        series_b_record['investors'] = 'None'
        series_b_record['post_valuation'] = series_a_record['post_valuation']  # No change

        missing_b_records.append(series_b_record)

    # Add missing B records to panel
    missing_b_df = pd.DataFrame(missing_b_records)
    panel_df = pd.concat([panel_df, missing_b_df], ignore_index=True)

    print(f"  Added {len(missing_b_records)} Series B records for firms without Series B")

# Sort by company and round
panel_df = panel_df.sort_values(['company_id', 'round'])

print(f"  Final panel: {len(panel_df)} observations")
print(f"  Final unique firms: {panel_df['company_id'].nunique()}")

# Step 4: Add derived variables
print("\n[Step 4] Creating derived variables...")

# Series B dummy (1 = Series B, 0 = Series A)
panel_df['series_b_dummy'] = (panel_df['round'] == 'Series B').astype(int)

# Log of Series A amount (for controls)
# Get Series A amount for each firm
series_a_amounts = panel_df[panel_df['round'] == 'Series A'][['company_id', 'deal_size']].copy()
series_a_amounts.columns = ['company_id', 'series_a_amount']
panel_df = panel_df.merge(series_a_amounts, on='company_id', how='left')
panel_df['log_series_a_amount'] = np.log(panel_df['series_a_amount'] + 1)  # +1 to handle zeros

# Vagueness categories for analysis
panel_df['vagueness_category'] = pd.cut(
    panel_df['vagueness'],
    bins=[0, 50, 100],
    labels=['Precise', 'Vague'],
    include_lowest=True
)

# Integration cost label
panel_df['integration_cost_label'] = panel_df['high_integration_cost'].map({
    0: 'Low-i (API/SaaS)',
    1: 'High-i (Hardware)'
})

print("  ✓ Added series_b_dummy")
print("  ✓ Added log_series_a_amount")
print("  ✓ Added vagueness_category")
print("  ✓ Added integration_cost_label")

# Step 5: Save analysis panel
print("\n[Step 5] Saving analysis panel...")

# Select columns for final output
analysis_cols = [
    'company_id', 'company_name', 'round', 'series_b_dummy',
    'vagueness', 'vagueness_category',
    'high_integration_cost', 'integration_cost_label',
    'funding_success', 'deal_size', 'deal_date',
    'series_a_amount', 'log_series_a_amount',
    'employees', 'year_founded', 'total_raised',
    'investors', 'post_valuation'
]

analysis_panel = panel_df[analysis_cols].copy()

# Save to CSV
output_file = PROCESSED_DATA_DIR / "analysis_panel.csv"
analysis_panel.to_csv(output_file, index=False)

print(f"✓ Saved to: {output_file}")
print(f"  Rows: {len(analysis_panel)}")
print(f"  Columns: {len(analysis_panel.columns)}")

# Display summary
print("\n" + "=" * 80)
print("SUMMARY STATISTICS")
print("=" * 80)
print(f"\nTotal observations: {len(analysis_panel)}")
print(f"Unique firms: {analysis_panel['company_id'].nunique()}")
print(f"\nObservations per firm:")
print(analysis_panel.groupby('company_id').size().value_counts())

print(f"\nRound distribution:")
print(analysis_panel['round'].value_counts())

print(f"\nFunding success by round:")
success_by_round = analysis_panel.groupby('round')['funding_success'].agg(['count', 'sum', 'mean'])
print(success_by_round)

print(f"\nFunding success by integration cost and round:")
success_by_int_round = analysis_panel.groupby(['integration_cost_label', 'round'])['funding_success'].agg(['count', 'sum', 'mean'])
print(success_by_int_round)

print(f"\nFunding success by vagueness and round:")
success_by_vague_round = analysis_panel.groupby(['vagueness_category', 'round'])['funding_success'].agg(['count', 'sum', 'mean'])
print(success_by_vague_round)

print("\n" + "=" * 80)
print("FIRST 5 ROWS")
print("=" * 80)
print(analysis_panel[['company_id', 'company_name', 'round', 'vagueness',
                      'high_integration_cost', 'funding_success', 'deal_size']].head())

print("\n" + "=" * 80)
print("✓ SCRIPT 03 COMPLETED SUCCESSFULLY")
print("=" * 80)
