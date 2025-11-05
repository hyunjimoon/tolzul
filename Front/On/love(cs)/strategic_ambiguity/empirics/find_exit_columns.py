#!/usr/bin/env python
"""
Search for exit-related information in alternative columns.
"""

import pandas as pd
import sys

def find_exit_columns(data_path: str):
    """Search for exit-related columns in the data."""

    print("="*80)
    print("SEARCHING FOR EXIT-RELATED COLUMNS")
    print("="*80)

    try:
        print(f"\n📂 Reading: {data_path}")
        df = pd.read_csv(data_path, sep='|', encoding='utf-8', low_memory=False, nrows=10000)
        print(f"✓ Loaded {len(df):,} rows, {len(df.columns)} columns")
    except Exception as e:
        print(f"✗ Error: {e}")
        return

    # Search for exit-related column names
    print(f"\n🔍 Searching for columns containing exit-related keywords...")

    keywords = [
        'exit', 'Exit', 'EXIT',
        'acquire', 'Acquire', 'ACQUIRE',
        'ipo', 'IPO', 'Ipo',
        'merger', 'Merger', 'MERGER',
        'acquisition', 'Acquisition',
        'deal', 'Deal', 'DEAL',
        'outcome', 'Outcome',
        'status', 'Status', 'STATUS'
    ]

    matching_cols = []
    for col in df.columns:
        for keyword in keywords:
            if keyword in col:
                matching_cols.append(col)
                break

    if matching_cols:
        print(f"✓ Found {len(matching_cols)} potentially relevant columns:\n")

        for col in matching_cols:
            print(f"📊 {col}")
            print(f"   Non-null: {df[col].notna().sum():,} ({df[col].notna().sum()/len(df)*100:.1f}%)")

            # Show unique values if not too many
            unique_vals = df[col].nunique()
            print(f"   Unique values: {unique_vals:,}")

            if unique_vals <= 20:
                print(f"   Top values:")
                for val, count in df[col].value_counts().head(10).items():
                    print(f"     - {val}: {count:,} ({count/len(df)*100:.1f}%)")
            else:
                print(f"   Sample values:")
                sample = df[col].dropna().head(5).tolist()
                for val in sample:
                    print(f"     - {val}")
            print()
    else:
        print(f"✗ No columns found with exit-related keywords")

    # Check for any column with "Acquired", "IPO", "Public" in VALUES
    print(f"\n🔍 Searching for exit values in all columns...")

    exit_values = ['Acquired', 'IPO', 'Public', 'acquired', 'ipo', 'public']

    for col in df.columns:
        if df[col].dtype == 'object':  # Only check text columns
            for exit_val in exit_values:
                if exit_val in df[col].astype(str).values:
                    print(f"✓ Found '{exit_val}' in column: {col}")
                    count = (df[col].astype(str) == exit_val).sum()
                    print(f"   Count: {count:,}")
                    break

    print(f"\n" + "="*80)
    print(f"SEARCH COMPLETE")
    print(f"="*80)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        data_path = sys.argv[1]
    else:
        data_path = "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Front/On/love(cs)/strategic ambiguity/empirics/data/raw/Company20211201.dat"

    find_exit_columns(data_path)
