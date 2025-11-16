#!/usr/bin/env python
"""
Diagnostic script to check founder credibility data availability.
Run this to understand why all founders appear as non-serial.
"""

import pandas as pd
from pathlib import Path

def check_founder_data(data_path: str):
    """Check if founder credibility can be computed from raw data."""

    print("="*80)
    print("FOUNDER CREDIBILITY DATA DIAGNOSTIC")
    print("="*80)

    # Try to read the data
    try:
        print(f"\n📂 Reading data from: {data_path}")
        df = pd.read_csv(data_path, sep='|', encoding='utf-8', low_memory=False, nrows=10000)
        print(f"✓ Successfully loaded {len(df):,} rows (first 10,000 for speed)")
    except FileNotFoundError:
        print(f"✗ File not found: {data_path}")
        return
    except Exception as e:
        print(f"✗ Error reading file: {e}")
        return

    print(f"\n📋 Total columns: {len(df.columns)}")

    # Check for required columns
    print(f"\n🔍 Checking for required columns...")

    required_cols = {
        'PrimaryContactPBId': 'Founder identifier (required to link founders across companies)',
        'BusinessStatus': 'Company status (required to identify Acquired/IPO/Public exits)'
    }

    for col, description in required_cols.items():
        if col in df.columns:
            print(f"✓ {col}: FOUND")
            print(f"   {description}")

            # Show sample data
            non_null = df[col].notna().sum()
            print(f"   Non-null values: {non_null:,} ({non_null/len(df)*100:.1f}%)")

            if col == 'BusinessStatus':
                # Show distribution
                print(f"   Top 5 values:")
                top_vals = df[col].value_counts().head(5)
                for val, count in top_vals.items():
                    print(f"     - {val}: {count:,} ({count/len(df)*100:.1f}%)")

                # Check for exit statuses
                exit_statuses = ['Acquired', 'IPO', 'Public']
                has_exit = df[col].isin(exit_statuses).sum()
                print(f"   Companies with exits (Acquired/IPO/Public): {has_exit:,} ({has_exit/len(df)*100:.1f}%)")

            elif col == 'PrimaryContactPBId':
                # Check unique founders
                unique_founders = df[col].nunique()
                print(f"   Unique founders: {unique_founders:,}")

                if unique_founders > 0:
                    # Check if any founder has multiple companies
                    founder_counts = df[col].value_counts()
                    multi_company = (founder_counts > 1).sum()
                    print(f"   Founders with multiple companies: {multi_company:,} ({multi_company/unique_founders*100:.1f}%)")

                    if multi_company > 0:
                        print(f"   Top 5 most prolific founders:")
                        for founder_id, count in founder_counts.head(5).items():
                            print(f"     - Founder {founder_id}: {count} companies")
        else:
            print(f"✗ {col}: NOT FOUND")
            print(f"   {description}")
            print(f"   ⚠️  This column is required for computing serial entrepreneur status")

    # Try to compute founder credibility
    print(f"\n🧮 Attempting to compute founder credibility...")

    if 'PrimaryContactPBId' in df.columns and 'BusinessStatus' in df.columns:
        # Replicate the logic from compute_founder_credibility()
        tmp = df[['PrimaryContactPBId', 'BusinessStatus']].copy()
        tmp['_has_exit'] = tmp['BusinessStatus'].isin(['Acquired', 'IPO', 'Public']).astype(int)

        # Group by founder and check if they have any exits
        founder_exits = tmp.groupby('PrimaryContactPBId')['_has_exit'].max()
        serial_founders = (founder_exits > 0).sum()
        total_founders = len(founder_exits)

        print(f"✓ Computation successful")
        print(f"   Total unique founders: {total_founders:,}")
        print(f"   Serial founders (with exits): {serial_founders:,} ({serial_founders/total_founders*100:.1f}%)")
        print(f"   Non-serial founders: {total_founders - serial_founders:,} ({(total_founders - serial_founders)/total_founders*100:.1f}%)")

        if serial_founders == 0:
            print(f"\n⚠️  WARNING: No serial founders found!")
            print(f"   Possible reasons:")
            print(f"   1. This is a baseline snapshot (2021-12) with very young companies")
            print(f"   2. Exit data is incomplete or not yet recorded")
            print(f"   3. The sample period is too short to observe exits")
            print(f"")
            print(f"   Recommendation: Use a later snapshot or combine multiple snapshots")
            print(f"   to identify founders who have exits by endpoint (2023-05)")
    else:
        print(f"✗ Cannot compute - missing required columns")

    print(f"\n" + "="*80)
    print(f"DIAGNOSTIC COMPLETE")
    print(f"="*80)


if __name__ == "__main__":
    import sys

    # Default to Mac Dropbox path
    default_path = "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Front/On/love(cs)/strategic ambiguity/empirics/data/raw/Company20211201.dat"

    if len(sys.argv) > 1:
        data_path = sys.argv[1]
    else:
        data_path = default_path
        print(f"No path provided, using default: {data_path}")
        print(f"Usage: python check_founder_data.py <path_to_data.dat>")
        print()

    check_founder_data(data_path)

    print(f"\n💡 TIP: Also check the endpoint snapshot (2023-05) which may have more exits:")
    endpoint_path = data_path.replace("20211201", "20230501")
    if Path(endpoint_path).exists():
        print(f"   python check_founder_data.py \"{endpoint_path}\"")
