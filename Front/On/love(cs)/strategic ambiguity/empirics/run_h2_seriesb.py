#!/usr/bin/env python3
"""
H2 Analysis with Series B+ Progression (LLM2 Approach)

This script implements the methodologically correct survival variable:
- DV: Series A → Series B+ progression within 17 months
- Baseline: 2021-12-01 (extract predictors)
- Endpoint: 2023-05-01 (measure outcomes)
- Expected base rate: 12-15%

Key fixes:
1. As-of date capping (prevents data leakage)
2. 4-snapshot event ordering (B+ vs M&A timing)
3. At-risk cohort (Series A only, VC-backed)
4. M&A censoring (competing risk)

Usage:
    python run_h2_seriesb.py --output outputs/
"""

import pandas as pd
import numpy as np
from pathlib import Path
import argparse
import sys
import warnings
warnings.filterwarnings('ignore')

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "code/hypothesis_testing_pipeline/src"))

from feature_engineering import (
    engineer_features, compute_founder_credibility, extract_sector_fe,
    create_survival_seriesb_progression
)
from hypothesis_tests import run_full_hypothesis_tests, create_results_summary
from visualizations import create_all_visualizations


def read_snapshot(path, encoding='utf-8'):
    """Read snapshot with encoding fallback."""
    try:
        return pd.read_csv(path, sep='|', encoding=encoding, low_memory=False)
    except UnicodeDecodeError:
        print(f"  Trying latin-1 encoding for {path.name}")
        return pd.read_csv(path, sep='|', encoding='latin-1', low_memory=False)


def main():
    parser = argparse.ArgumentParser(
        description='H2 Analysis: Series B+ Progression (17-month window)',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--output',
        type=str,
        default='outputs',
        help='Output directory (default: outputs/)'
    )

    args = parser.parse_args()
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("="*80)
    print("H2: SERIES B+ PROGRESSION ANALYSIS (LLM2 APPROACH)")
    print("="*80)
    print(f"Window: 17 months (2021-12-01 → 2023-05-01)")
    print(f"DV: Series A → Series B+ progression")
    print(f"Expected base rate: 12-15%")
    print("="*80)

    # File paths
    data_dir = Path("data/raw")
    snapshots = {
        't0': data_dir / "Company20211201.dat",
        'tm1': data_dir / "Company20220101.dat",
        'tm2': data_dir / "Company20220501.dat",
        't1': data_dir / "Company20230501.dat"
    }

    # Load all 4 snapshots
    print("\n" + "="*80)
    print("STEP 1: LOAD 4 SNAPSHOTS")
    print("="*80)

    dfs = {}
    for name, path in snapshots.items():
        if not path.exists():
            raise FileNotFoundError(f"Snapshot not found: {path}")

        df = read_snapshot(path)
        dfs[name] = df
        print(f"  ✓ {name} ({path.name}): {len(df):,} rows, {len(df.columns)} columns")

    # Create Series B+ progression DV
    print("\n" + "="*80)
    print("STEP 2: CREATE SERIES B+ PROGRESSION DV")
    print("="*80)

    survival_df = create_survival_seriesb_progression(
        df_baseline=dfs['t0'],
        df_mid1=dfs['tm1'],
        df_mid2=dfs['tm2'],
        df_endpoint=dfs['t1'],
        baseline_date="2021-12-01",
        mid1_date="2022-01-01",
        mid2_date="2022-05-01",
        endpoint_date="2023-05-01"
    )

    # Save survival DV
    survival_df.to_csv(output_dir / "h2_dv_seriesb_17m.csv", index=False)
    print(f"\n  ✓ Saved: {output_dir / 'h2_dv_seriesb_17m.csv'}")

    # Engineer features from baseline snapshot
    print("\n" + "="*80)
    print("STEP 3: ENGINEER FEATURES (FROM BASELINE)")
    print("="*80)

    # Use baseline (t0) for all predictors
    df_baseline = dfs['t0'].copy()

    # Standard feature engineering
    print("\n  Running standard feature engineering...")
    df_baseline = engineer_features(df_baseline)

    # Add custom features
    print("\n  Adding custom features...")

    # founder_credibility
    if 'founder_credibility' not in df_baseline.columns:
        df_baseline['founder_credibility'] = compute_founder_credibility(df_baseline)
        serial_rate = df_baseline['founder_credibility'].mean()
        print(f"    ✓ founder_credibility: {serial_rate:.1%} serial founders")

    # sector_fe
    if 'sector_fe' not in df_baseline.columns and 'keywords' in df_baseline.columns:
        df_baseline['sector_fe'] = extract_sector_fe(df_baseline['keywords'])
        print(f"    ✓ sector_fe: {df_baseline['sector_fe'].nunique()} categories")

    # Merge survival DV with predictors
    print("\n" + "="*80)
    print("STEP 4: MERGE DV WITH PREDICTORS")
    print("="*80)

    id_col = 'CompanyID' if 'CompanyID' in df_baseline.columns else 'company_id'

    # Merge (only keep at-risk companies)
    analysis_df = df_baseline.merge(
        survival_df.rename(columns={'company_id': id_col}),
        on=id_col,
        how='inner'  # Only at-risk companies
    )

    print(f"  ✓ Merged dataset: {len(analysis_df):,} companies in at-risk cohort")

    # Rename Y_primary to survival for compatibility
    analysis_df['survival'] = analysis_df['Y_primary']
    analysis_df['survival_MA_upper'] = analysis_df['Y_MA_upper']
    analysis_df['survival_MA_lower'] = analysis_df['Y_MA_lower']

    # Save merged dataset
    analysis_df.to_csv(output_dir / "h2_analysis_dataset_17m.csv", index=False)
    print(f"  ✓ Saved: {output_dir / 'h2_analysis_dataset_17m.csv'}")

    # Run hypothesis tests
    print("\n" + "="*80)
    print("STEP 5: RUN HYPOTHESIS TESTS")
    print("="*80)

    # Primary spec (M&A censored)
    print("\n[PRIMARY] H2 Main (M&A censored):")
    df_primary = analysis_df[analysis_df['survival'].notna()].copy()
    print(f"  N = {len(df_primary):,}")

    results = run_full_hypothesis_tests(df_primary)

    # Save results
    summary = create_results_summary(results)
    summary.to_csv(output_dir / "h2_main_coefficients.csv", index=False)
    print(f"\n  ✓ Saved: {output_dir / 'h2_main_coefficients.csv'}")

    # Robustness: M&A upper bound
    print("\n[ROBUSTNESS] H2 with M&A=1 (upper bound):")
    df_upper = analysis_df.copy()
    df_upper['survival'] = df_upper['survival_MA_upper']
    df_upper = df_upper[df_upper['survival'].notna()]
    print(f"  N = {len(df_upper):,}")

    results_upper = run_full_hypothesis_tests(df_upper)
    summary_upper = create_results_summary(results_upper)
    summary_upper.to_csv(output_dir / "h2_robustness_MA_upper.csv", index=False)
    print(f"  ✓ Saved: {output_dir / 'h2_robustness_MA_upper.csv'}")

    # Robustness: M&A lower bound
    print("\n[ROBUSTNESS] H2 with M&A=0 (lower bound):")
    df_lower = analysis_df.copy()
    df_lower['survival'] = df_lower['survival_MA_lower']
    df_lower = df_lower[df_lower['survival'].notna()]
    print(f"  N = {len(df_lower):,}")

    results_lower = run_full_hypothesis_tests(df_lower)
    summary_lower = create_results_summary(results_lower)
    summary_lower.to_csv(output_dir / "h2_robustness_MA_lower.csv", index=False)
    print(f"  ✓ Saved: {output_dir / 'h2_robustness_MA_lower.csv'}")

    # Create visualizations
    print("\n" + "="*80)
    print("STEP 6: CREATE VISUALIZATIONS")
    print("="*80)

    create_all_visualizations(df_primary, results, output_dir=output_dir)

    print("\n" + "="*80)
    print("✓ H2 ANALYSIS COMPLETE")
    print("="*80)
    print(f"\nOutputs saved to: {output_dir}/")
    print("\nKey files:")
    print(f"  - h2_dv_seriesb_17m.csv (DV construction)")
    print(f"  - h2_analysis_dataset_17m.csv (merged predictors + DV)")
    print(f"  - h2_main_coefficients.csv (primary results)")
    print(f"  - h2_robustness_MA_upper.csv (upper bound)")
    print(f"  - h2_robustness_MA_lower.csv (lower bound)")
    print(f"  - Visualizations: h1_scatter.png, h2_interaction.png, etc.")


if __name__ == "__main__":
    main()
