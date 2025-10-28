#!/usr/bin/env python3
"""
Complete Hypothesis Testing Pipeline (H1 + H2)

Tests:
  H1: Early Funding ~ Vagueness (OLS)
  H2: Series B+ Progression ~ Vagueness × Integration Cost (Logit)

Usage:
    python run_analysis.py --output outputs/
    python run_analysis.py --output outputs/ --h1-only  # Test H1 only
    python run_analysis.py --output outputs/ --h2-only  # Test H2 only
"""

import pandas as pd
import numpy as np
from pathlib import Path
import argparse
import sys
import warnings
warnings.filterwarnings('ignore')

# Add modules to path
sys.path.insert(0, str(Path(__file__).parent))

from modules.features import (
    engineer_features, compute_founder_credibility, extract_sector_fe,
    create_survival_seriesb_progression, preprocess_for_h2
)
from modules.models import (
    test_h1_early_funding, test_h2_main_survival, test_h2_robustness_sector_fe,
    MultiverseRunner
)
from modules.plots import create_storyboard_and_multiverse_plots


def read_snapshot(path, encoding='utf-8'):
    """Read snapshot with encoding fallback."""
    try:
        return pd.read_csv(path, sep='|', encoding=encoding, low_memory=False)
    except UnicodeDecodeError:
        print(f"  Trying latin-1 encoding for {path.name}")
        return pd.read_csv(path, sep='|', encoding='latin-1', low_memory=False)


def run_h1_analysis(df_baseline, output_dir):
    """Run H1: Early Funding ~ Vagueness."""
    print("\n" + "="*80)
    print("H1: EARLY FUNDING ~ VAGUENESS (OLS)")
    print("="*80)

    # Filter to companies with funding data
    df_h1 = df_baseline[df_baseline['early_funding_musd'].notna()].copy()

    print(f"  Sample size: {len(df_h1):,} (companies with funding data)")
    print(f"  Mean early funding: ${df_h1['early_funding_musd'].mean():.2f}M")
    print(f"  Median early funding: ${df_h1['early_funding_musd'].median():.2f}M")

    # Apply preprocessing (z-scores, cohorts)
    df_h1 = preprocess_for_h2(df_h1)

    # Test H1
    h1_result = test_h1_early_funding(df_h1)

    # Save results
    h1_coeffs = pd.DataFrame({
        'variable': h1_result.params.index,
        'coefficient': h1_result.params.values,
        'std_err': h1_result.bse.values,
        't': h1_result.tvalues.values,
        'p_value': h1_result.pvalues.values,
        'ci_lower': h1_result.conf_int()[0].values,
        'ci_upper': h1_result.conf_int()[1].values
    })

    output_file = output_dir / "h1_coefficients.csv"
    h1_coeffs.to_csv(output_file, index=False)
    print(f"\n  ✓ Saved: {output_file}")

    return h1_result


def run_h2_analysis(dfs, output_dir):
    """Run H2: Series B+ Progression ~ Vagueness × Integration Cost."""
    print("\n" + "="*80)
    print("H2: SERIES B+ PROGRESSION ANALYSIS")
    print("="*80)
    print(f"Window: 17 months (2021-12-01 → 2023-05-01)")
    print(f"Expected base rate: 12-15%")

    # Create Series B+ progression DV
    print("\n" + "="*80)
    print("STEP 1: CREATE SERIES B+ PROGRESSION DV")
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

    survival_df.to_csv(output_dir / "h2_dv_seriesb_17m.csv", index=False)
    print(f"  ✓ Saved: {output_dir / 'h2_dv_seriesb_17m.csv'}")

    # Engineer features from baseline
    print("\n" + "="*80)
    print("STEP 2: ENGINEER FEATURES (FROM BASELINE)")
    print("="*80)

    df_baseline = engineer_features(dfs['t0'])

    # Add founder credibility
    df_baseline['founder_credibility'] = compute_founder_credibility(df_baseline)

    # Add sector FE if needed
    if 'sector_fe' not in df_baseline.columns and 'keywords' in df_baseline.columns:
        df_baseline['sector_fe'] = extract_sector_fe(df_baseline['keywords'])

    # Apply H2 preprocessing
    print("\n" + "="*80)
    print("STEP 3: H2 PREPROCESSING")
    print("="*80)

    df_baseline = preprocess_for_h2(df_baseline)

    # Merge DV with predictors
    print("\n" + "="*80)
    print("STEP 4: MERGE DV WITH PREDICTORS")
    print("="*80)

    id_col = 'CompanyID' if 'CompanyID' in df_baseline.columns else 'company_id'

    analysis_df = df_baseline.merge(
        survival_df.rename(columns={'company_id': id_col}),
        on=id_col,
        how='inner'
    )

    print(f"  ✓ Merged dataset: {len(analysis_df):,} companies in at-risk cohort")

    # Rename Y columns for compatibility
    analysis_df['survival'] = analysis_df['Y_primary']
    analysis_df['survival_MA_upper'] = analysis_df['Y_MA_upper']
    analysis_df['survival_MA_lower'] = analysis_df['Y_MA_lower']

    # Save merged dataset
    analysis_df.to_csv(output_dir / "h2_analysis_dataset.csv", index=False)
    print(f"  ✓ Saved: {output_dir / 'h2_analysis_dataset.csv'}")

    # Run hypothesis tests
    print("\n" + "="*80)
    print("STEP 5: RUN H2 HYPOTHESIS TESTS")
    print("="*80)

    # Primary spec (M&A censored, no sector FE)
    print("\n[PRIMARY] H2 Main (M&A censored, no sector FE):")
    df_primary = analysis_df[analysis_df['survival'].notna()].copy()
    print(f"  N = {len(df_primary):,}")
    print(f"  Survival rate: {df_primary['survival'].mean():.2%}")

    h2_main_result = test_h2_main_survival(df_primary)

    # Save main results
    main_coeffs = pd.DataFrame({
        'variable': h2_main_result.params.index,
        'coefficient': h2_main_result.params.values,
        'std_err': h2_main_result.bse.values,
        'z': h2_main_result.tvalues.values,
        'p_value': h2_main_result.pvalues.values,
        'ci_lower': h2_main_result.conf_int()[0].values,
        'ci_upper': h2_main_result.conf_int()[1].values
    })
    main_coeffs.to_csv(output_dir / "h2_main_coefficients.csv", index=False)
    print(f"\n  ✓ Saved: {output_dir / 'h2_main_coefficients.csv'}")

    # Robustness: With sector FE
    print("\n[ROBUSTNESS] H2 with Sector FE + ic_within:")
    h2_sector_result = test_h2_robustness_sector_fe(df_primary)

    sector_coeffs = pd.DataFrame({
        'variable': h2_sector_result.params.index,
        'coefficient': h2_sector_result.params.values,
        'std_err': h2_sector_result.bse.values,
        'z': h2_sector_result.tvalues.values,
        'p_value': h2_sector_result.pvalues.values,
        'ci_lower': h2_sector_result.conf_int()[0].values,
        'ci_upper': h2_sector_result.conf_int()[1].values
    })
    sector_coeffs.to_csv(output_dir / "h2_robustness_sector_fe.csv", index=False)
    print(f"  ✓ Saved: {output_dir / 'h2_robustness_sector_fe.csv'}")

    # Robustness: M&A upper bound
    print("\n[ROBUSTNESS] H2 with M&A=1 (upper bound):")
    df_upper = analysis_df.copy()
    df_upper['survival'] = df_upper['survival_MA_upper']
    df_upper = df_upper[df_upper['survival'].notna()]
    print(f"  N = {len(df_upper):,}")
    print(f"  Survival rate: {df_upper['survival'].mean():.2%}")

    h2_upper_result = test_h2_main_survival(df_upper)
    upper_coeffs = pd.DataFrame({
        'variable': h2_upper_result.params.index,
        'coefficient': h2_upper_result.params.values,
        'std_err': h2_upper_result.bse.values,
        'z': h2_upper_result.tvalues.values,
        'p_value': h2_upper_result.pvalues.values,
        'ci_lower': h2_upper_result.conf_int()[0].values,
        'ci_upper': h2_upper_result.conf_int()[1].values
    })
    upper_coeffs.to_csv(output_dir / "h2_robustness_MA_upper.csv", index=False)
    print(f"  ✓ Saved: {output_dir / 'h2_robustness_MA_upper.csv'}")

    # Robustness: M&A lower bound
    print("\n[ROBUSTNESS] H2 with M&A=0 (lower bound):")
    df_lower = analysis_df.copy()
    df_lower['survival'] = df_lower['survival_MA_lower']
    df_lower = df_lower[df_lower['survival'].notna()]
    print(f"  N = {len(df_lower):,}")
    print(f"  Survival rate: {df_lower['survival'].mean():.2%}")

    h2_lower_result = test_h2_main_survival(df_lower)
    lower_coeffs = pd.DataFrame({
        'variable': h2_lower_result.params.index,
        'coefficient': h2_lower_result.params.values,
        'std_err': h2_lower_result.bse.values,
        'z': h2_lower_result.tvalues.values,
        'p_value': h2_lower_result.pvalues.values,
        'ci_lower': h2_lower_result.conf_int()[0].values,
        'ci_upper': h2_lower_result.conf_int()[1].values
    })
    lower_coeffs.to_csv(output_dir / "h2_robustness_MA_lower.csv", index=False)
    print(f"  ✓ Saved: {output_dir / 'h2_robustness_MA_lower.csv'}")

    # Return results and analysis dataset for storyboard/multiverse if needed
    return {
        'main': h2_main_result,
        'sector_fe': h2_sector_result,
        'ma_upper': h2_upper_result,
        'ma_lower': h2_lower_result,
        'analysis_df': analysis_df
    }


def main():
    parser = argparse.ArgumentParser(
        description='Complete Hypothesis Testing Pipeline (H1 + H2)',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--output',
        type=str,
        default='outputs',
        help='Output directory (default: outputs/)'
    )

    parser.add_argument(
        '--h1-only',
        action='store_true',
        help='Test H1 only (early funding)'
    )

    parser.add_argument(
        '--h2-only',
        action='store_true',
        help='Test H2 only (series B+ progression)'
    )

    parser.add_argument(
        '--storyboard',
        action='store_true',
        help='Create storyboard plots (narrative visualizations)'
    )

    parser.add_argument(
        '--multiverse',
        action='store_true',
        help='Run multiverse grid and create heatmap'
    )

    args = parser.parse_args()
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("="*80)
    print("HYPOTHESIS TESTING PIPELINE")
    print("="*80)

    # Determine what to test
    test_h1 = not args.h2_only
    test_h2 = not args.h1_only

    if test_h1 and test_h2:
        print("Testing: H1 (Early Funding) + H2 (Series B+ Progression)")
    elif test_h1:
        print("Testing: H1 (Early Funding) only")
    else:
        print("Testing: H2 (Series B+ Progression) only")

    print("="*80)

    # Load data
    data_dir = Path("data/raw")

    if test_h2:
        # Need all 4 snapshots for H2
        snapshots = {
            't0': data_dir / "Company20211201.dat",
            'tm1': data_dir / "Company20220101.dat",
            'tm2': data_dir / "Company20220501.dat",
            't1': data_dir / "Company20230501.dat"
        }

        print("\n" + "="*80)
        print("LOADING 4 SNAPSHOTS (FOR H2)")
        print("="*80)

        dfs = {}
        for name, path in snapshots.items():
            if not path.exists():
                raise FileNotFoundError(f"Snapshot not found: {path}")

            df = read_snapshot(path)
            dfs[name] = df
            print(f"  ✓ {name} ({path.name}): {len(df):,} rows, {len(df.columns)} columns")

    elif test_h1:
        # Only need baseline for H1
        baseline_path = data_dir / "Company20211201.dat"

        print("\n" + "="*80)
        print("LOADING BASELINE SNAPSHOT (FOR H1)")
        print("="*80)

        if not baseline_path.exists():
            raise FileNotFoundError(f"Baseline not found: {baseline_path}")

        df_baseline = read_snapshot(baseline_path)
        print(f"  ✓ Baseline ({baseline_path.name}): {len(df_baseline):,} rows")

        # Engineer features
        print("\n" + "="*80)
        print("ENGINEERING FEATURES")
        print("="*80)

        df_baseline = engineer_features(df_baseline)
        df_baseline['founder_credibility'] = compute_founder_credibility(df_baseline)

        if 'sector_fe' not in df_baseline.columns and 'keywords' in df_baseline.columns:
            df_baseline['sector_fe'] = extract_sector_fe(df_baseline['keywords'])

    # Run tests
    results = {}

    if test_h1:
        if not test_h2:
            # H1-only mode, use df_baseline we loaded
            results['h1'] = run_h1_analysis(df_baseline, output_dir)
        else:
            # H1+H2 mode, engineer features from baseline snapshot
            df_baseline = engineer_features(dfs['t0'])
            df_baseline['founder_credibility'] = compute_founder_credibility(df_baseline)

            if 'sector_fe' not in df_baseline.columns and 'keywords' in df_baseline.columns:
                df_baseline['sector_fe'] = extract_sector_fe(df_baseline['keywords'])

            results['h1'] = run_h1_analysis(df_baseline, output_dir)

    if test_h2:
        results['h2'] = run_h2_analysis(dfs, output_dir)

    # === Optional: Storyboard & Multiverse ===
    if (args.storyboard or args.multiverse) and test_h2:
        print("\n" + "="*80)
        print("STORYBOARD & MULTIVERSE ANALYSIS")
        print("="*80)

        # Get analysis dataset from H2 results
        analysis_df = results['h2']['analysis_df']

        mv_results = None
        if args.multiverse:
            print("\n" + "="*80)
            print("RUNNING MULTIVERSE GRID (no window toggle)")
            print("="*80)
            grid = {
                'dv': ['Y_primary', 'Y_MA_upper', 'Y_MA_lower'],
                'ic_spec': ['binary', 'within'],
                'sector_fe': [False, True],
                'estimator': ['logit', 'ridge']
            }
            mv = MultiverseRunner()
            mv_results = mv.run(analysis_df, grid)
            mv_results.to_csv(output_dir / "multiverse_results.csv", index=False)
            print(f"  ✓ Saved: {output_dir / 'multiverse_results.csv'}")

        if args.storyboard:
            print("\n" + "="*80)
            print("CREATING STORYBOARD PLOTS")
            print("="*80)
            created = create_storyboard_and_multiverse_plots(
                df=analysis_df,
                results_df=mv_results,
                output_dir=output_dir,
                dv_col='survival'
            )
            for k, p in created.items():
                print(f"  ✓ {k}: {p}")

    # Summary
    print("\n" + "="*80)
    print("✓ ANALYSIS COMPLETE")
    print("="*80)
    print(f"\nOutputs saved to: {output_dir}/")

    if test_h1:
        print("\nH1 Results:")
        print(f"  - h1_coefficients.csv")

    if test_h2:
        print("\nH2 Results:")
        print(f"  - h2_main_coefficients.csv (primary)")
        print(f"  - h2_robustness_sector_fe.csv (with sector FE)")
        print(f"  - h2_robustness_MA_upper.csv (M&A=1)")
        print(f"  - h2_robustness_MA_lower.csv (M&A=0)")
        print(f"  - h2_analysis_dataset.csv (full data)")
        print(f"  - h2_dv_seriesb_17m.csv (DV construction)")

        if args.storyboard:
            print("\nStoryboard Plots:")
            print(f"  - story_univariate.png")
            print(f"  - story_bivariate_growth.png")
            print(f"  - story_interaction.png")

        if args.multiverse:
            print("\nMultiverse Analysis:")
            print(f"  - multiverse_results.csv")
            print(f"  - multiverse_heatmap.png")


if __name__ == "__main__":
    main()
