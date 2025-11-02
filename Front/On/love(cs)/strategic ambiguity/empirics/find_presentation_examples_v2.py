#!/usr/bin/env python3
"""
Presentation Examples Finder (v2 - Simplified)
===============================================
Extract 4 representative companies for presentation from h2_analysis_dataset.csv

This version works with the actual pipeline output:
- Loads h2_analysis_dataset.csv (has vagueness, is_hardware, growth)
- Loads Company20211201.dat (has names, descriptions, keywords)
- Merges them and selects 4 diverse examples

Target: 4 companies with diverse outcomes
- Domains: AI Software(1), Autonomous Vehicles(1), Quantum Computing(2)
- Growth outcomes: High growth (1), Low growth (0), Mixed
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def read_snapshot_cached(path: Path, encoding: str = 'utf-8') -> pd.DataFrame:
    """
    Read .dat or .csv file with Parquet caching for 10-50x speed improvement.
    """
    path = Path(path)

    # Determine file type and cache path
    if path.suffix == '.dat':
        parquet_path = path.with_suffix('.parquet')
        sep = '|'
    elif path.suffix == '.csv':
        parquet_path = Path(str(path).replace('.csv', '.parquet'))
        sep = ','
    else:
        raise ValueError(f"Unsupported file type: {path.suffix}")

    # Use cache if it exists and is newer than source
    if parquet_path.exists() and parquet_path.stat().st_mtime > path.stat().st_mtime:
        print(f"  ✓ Loading from cache: {parquet_path.name}")
        return pd.read_parquet(parquet_path)

    # No cache - read file and create cache
    print(f"  ⏳ Reading {path.suffix} file: {path.name} (creating cache...)")
    try:
        df = pd.read_csv(path, sep=sep, encoding=encoding, low_memory=False)
    except UnicodeDecodeError:
        print(f"  ⚠️  UTF-8 failed, trying latin-1...")
        df = pd.read_csv(path, sep=sep, encoding='latin-1', low_memory=False)

    print(f"  💾 Caching to: {parquet_path.name}")
    df.to_parquet(parquet_path, index=False, compression='snappy')

    return df


def classify_domain_custom(keywords: str, description: str) -> str:
    """
    Classify domain: AI Software, Autonomous Vehicles, Quantum Computing, Other
    """
    if pd.isna(keywords):
        keywords = ""
    if pd.isna(description):
        description = ""

    text = f"{keywords} {description}".lower()

    # Quantum Computing (highest priority)
    if any(k in text for k in ["quantum", "qbit", "qubit"]):
        return "Quantum Computing"

    # Autonomous Vehicles
    if any(k in text for k in ["autonomous vehicle", "self-driving", "av ", "adas", "autonomous driving"]):
        return "Autonomous Vehicles"

    # AI Software
    if any(k in text for k in ["artificial intelligence", "ai ", "machine learning", "ml ",
                                "deep learning", "neural network", "nlp", "computer vision",
                                "natural language"]):
        return "AI Software"

    return "Other"


def find_presentation_cohort(
    analysis_path: Path,
    company_path: Path,
    output_path: Path = None
) -> pd.DataFrame:
    """
    Select 4 representative companies from h2_analysis_dataset.csv

    Args:
        analysis_path: Path to h2_analysis_dataset.csv
        company_path: Path to Company20211201.dat
        output_path: Optional output path

    Returns:
        DataFrame with 4 selected companies
    """
    print("="*80)
    print("PRESENTATION EXAMPLES FINDER (v2)")
    print("="*80)

    # Load analysis dataset (has outcomes and computed features)
    print(f"\n📂 Loading analysis dataset...")
    df_analysis = read_snapshot_cached(analysis_path)
    print(f"  ✓ Loaded {len(df_analysis):,} companies with outcomes")

    # Load company info (has names, descriptions, keywords)
    print(f"\n📂 Loading company information...")
    df_company = read_snapshot_cached(company_path)
    print(f"  ✓ Loaded {len(df_company):,} companies")

    # Merge
    print(f"\n🔗 Merging datasets...")
    df = df_analysis.merge(
        df_company[['CompanyID', 'CompanyName', 'Description', 'Keywords']],
        on='CompanyID',
        how='left'
    )
    print(f"  ✓ Merged dataset: {len(df):,} rows")

    # Apply domain classification
    print(f"\n🔧 Classifying domains...")
    df['domain'] = df.apply(
        lambda row: classify_domain_custom(
            row.get('Keywords', ""),
            row.get('Description', "")
        ),
        axis=1
    )
    domain_counts = df['domain'].value_counts()
    print(f"  ✓ Domain distribution:")
    for domain, count in domain_counts.items():
        print(f"    - {domain}: {count:,}")

    # Growth outcome summary
    print(f"\n📊 Growth outcome distribution:")
    if 'growth' in df.columns:
        print(f"  Mean growth: {df['growth'].mean():.3f}")
        print(f"  Growth > 0.5: {(df['growth'] > 0.5).sum():,} companies")
        print(f"  Growth < 0.5: {(df['growth'] <= 0.5).sum():,} companies")

    # Select 4 representative companies
    print(f"\n🎯 Selecting 4 representative companies...")

    target_domains = {
        'AI Software': 1,
        'Autonomous Vehicles': 1,
        'Quantum Computing': 2
    }

    selected = []

    for domain, target_count in target_domains.items():
        domain_df = df[df['domain'] == domain].copy()
        print(f"\n  {domain}: {len(domain_df)} candidates")

        if len(domain_df) == 0:
            print(f"    ⚠️  No companies found")
            continue

        # Try to get diverse growth outcomes
        # For 2 companies: get 1 high growth (>0.5) and 1 low growth (<=0.5)
        # For 1 company: get highest vagueness
        if target_count == 2 and len(domain_df) >= 2:
            # High growth
            high_growth = domain_df[domain_df['growth'] > 0.5]
            if len(high_growth) > 0:
                best_high = high_growth.nlargest(1, 'vagueness', keep='first')
                selected.append(best_high)
                print(f"    ✓ Selected 1 high-growth company (growth={best_high['growth'].values[0]:.3f})")
                domain_df = domain_df[domain_df['CompanyID'] != best_high['CompanyID'].values[0]]

            # Low growth
            low_growth = domain_df[domain_df['growth'] <= 0.5]
            if len(low_growth) > 0:
                best_low = low_growth.nlargest(1, 'vagueness', keep='first')
                selected.append(best_low)
                print(f"    ✓ Selected 1 low-growth company (growth={best_low['growth'].values[0]:.3f})")
            elif len(domain_df) > 0:
                # Fallback: any remaining company
                best = domain_df.nlargest(1, 'vagueness', keep='first')
                selected.append(best)
                print(f"    ✓ Selected 1 company (fallback)")

        elif target_count == 1:
            # Just pick the one with highest vagueness
            best = domain_df.nlargest(1, 'vagueness', keep='first')
            selected.append(best)
            print(f"    ✓ Selected 1 company (vagueness={best['vagueness'].values[0]:.3f})")

    if len(selected) == 0:
        print(f"\n❌ ERROR: No companies selected!")
        return pd.DataFrame()

    df_final = pd.concat(selected, ignore_index=True)

    # Create output table
    print(f"\n📋 Final selection: {len(df_final)} companies")

    df_export = pd.DataFrame()
    df_export['company_id'] = df_final['CompanyID']
    df_export['company_name'] = df_final['CompanyName']
    df_export['domain'] = df_final['domain']
    df_export['description'] = df_final['Description'].fillna("").str[:200] + "..."
    df_export['keywords'] = df_final['Keywords']
    df_export['vagueness'] = df_final['vagueness'].round(3)
    df_export['is_hardware'] = df_final['is_hardware']
    df_export['growth'] = df_final['growth'].round(3)
    if 'is_serial' in df_final.columns:
        df_export['is_serial'] = df_final['is_serial']

    # Print results
    print("\n" + "="*80)
    print("SELECTED COMPANIES")
    print("="*80)
    for idx, row in df_export.iterrows():
        print(f"\n{idx+1}. {row['company_name']}")
        print(f"   ID: {row['company_id']}")
        print(f"   Domain: {row['domain']}")
        print(f"   Vagueness: {row['vagueness']:.3f}")
        print(f"   Hardware: {row['is_hardware']}")
        print(f"   Growth: {row['growth']:.3f}")

    # Save
    if output_path:
        df_export.to_csv(output_path, index=False)
        print(f"\n✅ Saved to: {output_path}")

    return df_export


def main():
    """Main execution"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Find 4 representative companies from h2_analysis_dataset.csv"
    )
    parser.add_argument(
        '--analysis',
        type=str,
        default='outputs/h2_analysis_dataset.csv',
        help='Path to h2_analysis_dataset.csv'
    )
    parser.add_argument(
        '--company',
        type=str,
        default='data/raw/Company20211201.dat',
        help='Path to Company snapshot'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='outputs/presentation_examples.csv',
        help='Output CSV file'
    )

    args = parser.parse_args()

    # Create output directory
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Find 4 companies
    df_examples = find_presentation_cohort(
        Path(args.analysis),
        Path(args.company),
        output_path
    )

    if len(df_examples) < 4:
        print(f"\n⚠️  WARNING: Only found {len(df_examples)} companies (target: 4)")
        print("Consider:")
        print("  - Expanding domain definitions")
        print("  - Using different selection criteria")

    print("\n✅ Done!")
    return df_examples


if __name__ == "__main__":
    main()
