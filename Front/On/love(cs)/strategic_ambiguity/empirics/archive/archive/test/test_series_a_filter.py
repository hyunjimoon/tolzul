#!/usr/bin/env python3
"""
Test Series A filtering logic.
Check how many companies have FirstFinancingDealType == 'Early Stage VC'
"""

import sys
from pathlib import Path
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

sys.path.insert(0, str(Path(__file__).parent))

def main():
    print("="*80)
    print("TESTING SERIES A / EARLY STAGE VC FILTER")
    print("="*80)

    # Load existing dataset
    outdir = Path("outputs")
    dataset_path = outdir / "h2_analysis_dataset.csv"

    if not dataset_path.exists():
        print(f"ERROR: {dataset_path} not found.")
        return

    print(f"\n✓ Loading dataset: {dataset_path}")
    df = pd.read_csv(dataset_path)
    print(f"  Total companies: {len(df):,}")

    # Check current early_funding_musd
    has_early_funding = df['early_funding_musd'].notna().sum()
    print(f"\n📊 Current early_funding_musd:")
    print(f"  Non-null values: {has_early_funding:,} ({has_early_funding/len(df)*100:.1f}%)")

    # Check if we have FirstFinancingDealType in raw data
    data_dir = Path("data/raw")
    raw_file = data_dir / "Company20211201.dat"

    if raw_file.exists():
        print(f"\n📂 Checking raw data: {raw_file}")
        try:
            raw_df = pd.read_csv(raw_file, sep='|', encoding='utf-8', low_memory=False, nrows=50000)
            print(f"  Loaded {len(raw_df):,} rows (sample)")

            if 'FirstFinancingDealType' in raw_df.columns:
                print(f"\n✅ FirstFinancingDealType column found!")

                # Count different deal types
                deal_types = raw_df['FirstFinancingDealType'].value_counts().head(10)
                print(f"\n  Top 10 FirstFinancingDealType values:")
                for dtype, count in deal_types.items():
                    pct = count / len(raw_df) * 100
                    print(f"    {dtype}: {count:,} ({pct:.1f}%)")

                # Check for "Early Stage VC"
                A_STAGE_PAT = r"(?:\bSeries\s*A(?:[-\s]?\d+|[A-Z])?\b|\bEarly[-\s]*Stage\s*VC\b)"
                is_series_a = raw_df['FirstFinancingDealType'].fillna("").str.contains(
                    A_STAGE_PAT, case=False, regex=True, na=False
                )
                series_a_count = is_series_a.sum()
                print(f"\n  Series A / Early Stage VC matches: {series_a_count:,} ({series_a_count/len(raw_df)*100:.1f}%)")

                # Show some examples
                series_a_examples = raw_df.loc[is_series_a, 'FirstFinancingDealType'].value_counts().head(5)
                print(f"\n  Example matches:")
                for val, count in series_a_examples.items():
                    print(f"    '{val}': {count:,}")

                # Check what would be filtered out
                has_funding = raw_df['FirstFinancingSize'].notna()
                total_with_funding = has_funding.sum()
                series_a_with_funding = (is_series_a & has_funding).sum()
                filtered_out = total_with_funding - series_a_with_funding

                print(f"\n📊 Impact of filtering:")
                print(f"  Companies with FirstFinancingSize: {total_with_funding:,}")
                print(f"  Would keep (Series A / Early Stage VC): {series_a_with_funding:,}")
                print(f"  Would filter out: {filtered_out:,} ({filtered_out/total_with_funding*100:.1f}%)")

            else:
                print(f"\n⚠️  FirstFinancingDealType column NOT found in raw data")
                print(f"  Available columns with 'Financing' or 'Deal': {[c for c in raw_df.columns if 'Financing' in c or 'Deal' in c]}")

        except Exception as e:
            print(f"  ⚠️  Error reading raw data: {e}")
    else:
        print(f"\n⚠️  Raw data file not found: {raw_file}")

    print("\n" + "="*80)
    print("TEST COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()
