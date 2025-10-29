#!/usr/bin/env python3
"""
W1 Pipeline (clean): produce exactly 3 outputs

Outputs:
  outputs/
    - h1_coefficients.csv
    - h2_main_coefficients.csv
    - h2_analysis_dataset.csv
"""

import argparse
from pathlib import Path
import sys
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from modules.features import (
    engineer_features, compute_founder_credibility, extract_sector_fe,
    create_survival_seriesb_progression, preprocess_for_h2
)
from modules.models import (
    test_h1_early_funding, test_h2_main_growth
)

def read_snapshot(path, encoding='utf-8'):
    try:
        return pd.read_csv(path, sep='|', encoding=encoding, low_memory=False)
    except UnicodeDecodeError:
        return pd.read_csv(path, sep='|', encoding='latin-1', low_memory=False)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', type=str, default='outputs')
    args = p.parse_args()
    outdir = Path(args.output)
    outdir.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print("W1 HYPOTHESIS TESTING (CLEAN)")
    print("=" * 80)

    # --- Load 4 snapshots for DV construction (B+ progression) ---
    data_dir = Path("data/raw")
    snaps = {
        't0': data_dir / "Company20211201.dat",
        'tm1': data_dir / "Company20220101.dat",
        'tm2': data_dir / "Company20220501.dat",
        't1': data_dir / "Company20230501.dat"
    }
    dfs = {k: read_snapshot(v) for k, v in snaps.items()}

    # --- Features from baseline ---
    base = engineer_features(dfs['t0'])
    base['founder_credibility'] = compute_founder_credibility(base)
    if 'sector_fe' not in base.columns and 'keywords' in base.columns:
        base['sector_fe'] = extract_sector_fe(base['keywords'])

    # --- H2 preprocessing (z-scores, cohorts, etc.) ---
    base = preprocess_for_h2(base)

    # --- DV: Series B+ progression (reuse existing function) ---
    dv = create_survival_seriesb_progression(
        df_baseline=dfs['t0'], df_mid1=dfs['tm1'], df_mid2=dfs['tm2'], df_endpoint=dfs['t1'],
        baseline_date="2021-12-01", mid1_date="2022-01-01", mid2_date="2022-05-01", endpoint_date="2023-05-01"
    )

    # --- Merge & Rename DV columns ---
    id_col = 'CompanyID' if 'CompanyID' in base.columns else 'company_id'
    dv = dv.rename(columns={'company_id': id_col})
    analysis = base.merge(dv, on=id_col, how='inner').copy()
    # primary DV
    analysis['growth'] = analysis['Y_primary']  # <- rename
    # NOTE: we deliberately do not keep MA upper/lower variants for W1
    # cleanup
    for col in [c for c in analysis.columns if c.startswith('Y_MA_')]:
        analysis.drop(columns=[col], inplace=True)

    # keep only non-missing growth
    analysis = analysis[analysis['growth'].notna()].copy()

    # Save analysis dataset
    analysis.to_csv(outdir / "h2_analysis_dataset.csv", index=False)
    print(f"✓ Saved: {outdir / 'h2_analysis_dataset.csv'}")

    # --- H1 (OLS) on companies with early_funding_musd ---
    h1_df = analysis[analysis['early_funding_musd'].notna()].copy()
    h1_res = test_h1_early_funding(h1_df)
    pd.DataFrame({
        'variable': h1_res.params.index,
        'coefficient': h1_res.params.values,
        'std_err': h1_res.bse.values,
        'stat': h1_res.tvalues.values,
        'p_value': h1_res.pvalues.values,
        'ci_lower': h1_res.conf_int()[0].values,
        'ci_upper': h1_res.conf_int()[1].values
    }).to_csv(outdir / "h1_coefficients.csv", index=False)
    print(f"✓ Saved: {outdir / 'h1_coefficients.csv'}")

    # --- H2 main (Logit; NO early_funding) ---
    h2_res = test_h2_main_growth(analysis)
    pd.DataFrame({
        'variable': h2_res.params.index,
        'coefficient': h2_res.params.values,
        'std_err': h2_res.bse.values,
        'stat': h2_res.tvalues.values,
        'p_value': h2_res.pvalues.values,
        'ci_lower': h2_res.conf_int()[0].values,
        'ci_upper': h2_res.conf_int()[1].values
    }).to_csv(outdir / "h2_main_coefficients.csv", index=False)
    print(f"✓ Saved: {outdir / 'h2_main_coefficients.csv'}")

    print("\nDone. Artifacts:", *[p.name for p in outdir.glob('*.csv')], sep="\n  - ")

if __name__ == "__main__":
    main()
