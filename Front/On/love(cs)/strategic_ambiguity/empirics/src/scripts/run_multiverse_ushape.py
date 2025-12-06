"""
Multiverse U-Shape Analysis

Runs the U-shape hypothesis test across multiple vagueness metrics.
Outputs a comparative table to assess robustness of findings.

Usage:
    python src/scripts/run_multiverse_ushape.py
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from scipy import stats
import xarray as xr
from datetime import datetime

from src.multiverse_vagueness import VaguenessMultiverse, VAGUENESS_METRICS


def run_ushape_test(df: pd.DataFrame, vagueness_col: str) -> dict:
    """
    Run U-shape hypothesis test for a single vagueness metric.

    Returns dict with regression results.
    """
    # Standardize vagueness
    z_vag = (df[vagueness_col] - df[vagueness_col].mean()) / df[vagueness_col].std()
    df_temp = df.copy()
    df_temp['z_vag'] = z_vag
    df_temp['z_vag_sq'] = z_vag ** 2

    # Prepare controls
    controls = []
    if 'founder_serial' in df.columns:
        controls.append('founder_serial')
    if 'z_employees_log' in df.columns:
        controls.append('z_employees_log')
    if 'founding_cohort' in df.columns:
        df_temp['founding_cohort_cat'] = df_temp['founding_cohort'].astype(str)
        controls.append('C(founding_cohort_cat)')

    control_str = ' + '.join(controls) if controls else '1'

    # Drop NaN
    df_clean = df_temp.dropna(subset=['growth', 'z_vag'])

    # H0: Linear model
    formula_h0 = f"growth ~ z_vag + {control_str}"
    try:
        model_h0 = smf.logit(formula_h0, data=df_clean).fit(disp=0, maxiter=100)
        beta_1 = model_h0.params.get('z_vag', np.nan)
        beta_1_pval = model_h0.pvalues.get('z_vag', np.nan)
        llf_h0 = model_h0.llf
        n_obs = model_h0.nobs
    except Exception as e:
        print(f"  Warning: H0 fit failed - {e}")
        return None

    # H1: Quadratic model
    formula_h1 = f"growth ~ z_vag + z_vag_sq + {control_str}"
    try:
        model_h1 = smf.logit(formula_h1, data=df_clean).fit(disp=0, maxiter=100)
        beta_2 = model_h1.params.get('z_vag_sq', np.nan)
        beta_2_pval = model_h1.pvalues.get('z_vag_sq', np.nan)
        llf_h1 = model_h1.llf
    except Exception as e:
        print(f"  Warning: H1 fit failed - {e}")
        return None

    # LR test
    lr_stat = 2 * (llf_h1 - llf_h0)
    lr_pval = 1 - stats.chi2.cdf(lr_stat, df=1)

    # Determine shape
    if beta_2 > 0:
        shape = "U-shape"
    elif beta_2 < 0:
        shape = "Inverted-U"
    else:
        shape = "Linear"

    return {
        'n_obs': int(n_obs),
        'beta_1': beta_1,
        'beta_1_pval': beta_1_pval,
        'beta_2': beta_2,
        'beta_2_pval': beta_2_pval,
        'lr_stat': lr_stat,
        'lr_pval': lr_pval,
        'shape': shape,
        'shape_significant': (beta_2_pval < 0.05),
    }


def main():
    print("="*70)
    print("MULTIVERSE U-SHAPE ANALYSIS")
    print("Testing robustness across multiple vagueness metrics")
    print("="*70)

    # Load data
    data_path = Path('outputs/all/models/h2_analysis_dataset.csv')
    print(f"\nLoading data from {data_path}...")
    df = pd.read_csv(data_path, low_memory=False)
    print(f"  N = {len(df):,}")

    # Check if multiverse file exists, otherwise compute
    multiverse_path = Path('outputs/all/vagueness_multiverse.nc')

    if multiverse_path.exists():
        print(f"\nLoading precomputed metrics from {multiverse_path}...")
        ds = xr.open_dataset(multiverse_path)
    else:
        print("\nComputing all vagueness metrics (this may take a few minutes)...")
        mv = VaguenessMultiverse()
        ds = mv.compute_all_metrics(df)
        mv.save(ds, str(multiverse_path))

    # Run U-shape test for each metric
    results = []

    for metric_key in VAGUENESS_METRICS.keys():
        if metric_key not in ds.data_vars:
            print(f"  Skipping {metric_key} (not in dataset)")
            continue

        print(f"\nTesting: {VAGUENESS_METRICS[metric_key]['name']}")

        # Add metric to df
        df_test = df.copy()
        df_test[metric_key] = ds[metric_key].values

        # Run test
        result = run_ushape_test(df_test, metric_key)

        if result is not None:
            result['metric'] = metric_key
            result['metric_name'] = VAGUENESS_METRICS[metric_key]['name']
            result['scorer'] = VAGUENESS_METRICS[metric_key]['scorer_class']
            results.append(result)

            print(f"  β₁ = {result['beta_1']:.4f} (p={result['beta_1_pval']:.2e})")
            print(f"  β₂ = {result['beta_2']:.4f} (p={result['beta_2_pval']:.2e})")
            print(f"  Shape: {result['shape']} {'*' if result['shape_significant'] else ''}")

    # Also test the original vagueness column
    if 'vagueness' in df.columns:
        print(f"\nTesting: Original vagueness (from CSV)")
        result = run_ushape_test(df, 'vagueness')
        if result is not None:
            result['metric'] = 'vagueness_original'
            result['metric_name'] = 'Original (CSV)'
            result['scorer'] = 'HybridVaguenessScorerV2'
            results.append(result)
            print(f"  β₁ = {result['beta_1']:.4f} (p={result['beta_1_pval']:.2e})")
            print(f"  β₂ = {result['beta_2']:.4f} (p={result['beta_2_pval']:.2e})")
            print(f"  Shape: {result['shape']} {'*' if result['shape_significant'] else ''}")

    # Create summary table
    results_df = pd.DataFrame(results)

    print("\n" + "="*70)
    print("MULTIVERSE SUMMARY TABLE")
    print("="*70)

    summary = results_df[[
        'metric_name', 'beta_1', 'beta_1_pval', 'beta_2', 'beta_2_pval', 'shape', 'shape_significant'
    ]].copy()
    summary.columns = ['Metric', 'β₁', 'p(β₁)', 'β₂', 'p(β₂)', 'Shape', 'Sig.']

    # Format for display
    summary['β₁'] = summary['β₁'].apply(lambda x: f"{x:.4f}")
    summary['p(β₁)'] = summary['p(β₁)'].apply(lambda x: f"{x:.2e}")
    summary['β₂'] = summary['β₂'].apply(lambda x: f"{x:.4f}")
    summary['p(β₂)'] = summary['p(β₂)'].apply(lambda x: f"{x:.2e}")
    summary['Sig.'] = summary['Sig.'].apply(lambda x: "Yes" if x else "No")

    print(summary.to_string(index=False))

    # Save results
    output_path = Path('outputs/all/models/multiverse_ushape_results.csv')
    results_df.to_csv(output_path, index=False)
    print(f"\nResults saved to {output_path}")

    # Key findings
    print("\n" + "="*70)
    print("KEY FINDINGS")
    print("="*70)

    n_ushape = (results_df['shape'] == 'U-shape').sum()
    n_inverted = (results_df['shape'] == 'Inverted-U').sum()
    n_significant = results_df['shape_significant'].sum()
    n_total = len(results_df)

    print(f"  Total metrics tested: {n_total}")
    print(f"  U-shape: {n_ushape}")
    print(f"  Inverted-U: {n_inverted}")
    print(f"  Significant quadratic term: {n_significant}")

    if n_inverted > n_ushape:
        print("\n  CONCLUSION: Inverted-U pattern is more robust across metrics")
        print("  → Middle vagueness levels appear optimal for growth")
    elif n_ushape > n_inverted:
        print("\n  CONCLUSION: U-shape pattern is more robust across metrics")
        print("  → Extreme vagueness levels appear optimal for growth")
    else:
        print("\n  CONCLUSION: Mixed results - shape depends on metric choice")


if __name__ == "__main__":
    main()
