#!/usr/bin/env python3
# Week 1 runner: EXACTLY three outputs (H1/H2 + merged dataset)

import argparse, sys, warnings
from pathlib import Path
import pandas as pd
warnings.filterwarnings('ignore')

# Flexible imports: top-level OR modules/
ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
try:
    from features import (
        engineer_features, preprocess_for_h2, create_survival_seriesb_progression,
        extract_sector_fe, compute_founder_credibility
    )
    from models import test_h1_early_funding, test_h2_main_survival
except ImportError:
    sys.path.insert(0, str(ROOT / "modules"))
    from features import (
        engineer_features, preprocess_for_h2, create_survival_seriesb_progression,
        extract_sector_fe, compute_founder_credibility
    )
    from models import test_h1_early_funding, test_h2_main_survival


def _read_snapshot(path, encoding='utf-8'):
    try:
        return pd.read_csv(path, sep='|', encoding=encoding, low_memory=False)
    except UnicodeDecodeError:
        return pd.read_csv(path, sep='|', encoding='latin-1', low_memory=False)


def main():
    ap = argparse.ArgumentParser(description="W1 pipeline: H1+H2 main only")
    ap.add_argument("--output", type=str, default="outputs", help="Output dir")
    args = ap.parse_args()
    out_dir = Path(args.output); out_dir.mkdir(parents=True, exist_ok=True)

    # --- Load snapshots for H2 DV (17-month window)
    data_dir = Path("data/raw")
    paths = {
        "t0":  data_dir / "Company20211201.dat",
        "tm1": data_dir / "Company20220101.dat",
        "tm2": data_dir / "Company20220501.dat",
        "t1":  data_dir / "Company20230501.dat",
    }
    missing = [k for k,p in paths.items() if not p.exists()]
    if missing:
        raise FileNotFoundError(
            f"Missing snapshots for H2: {', '.join(missing)}. "
            f"Expected under {data_dir}/. Provide 4 snapshots to compute Series B+ progression."
        )
    dfs = {k: _read_snapshot(p) for k, p in paths.items()}

    # --- Engineer baseline features
    print("Engineering baseline features...")
    baseline = engineer_features(dfs["t0"])
    # Add founder credibility + sector FE if not present
    baseline["founder_credibility"] = compute_founder_credibility(baseline)
    if "sector_fe" not in baseline.columns and "keywords" in baseline.columns:
        baseline["sector_fe"] = extract_sector_fe(baseline["keywords"])

    # --- Preprocess (z-scores, cohorts, within-sector prep if needed)
    print("Preprocessing for H2...")
    baseline = preprocess_for_h2(baseline)

    # --- H1: Early Funding ~ z_vagueness + controls (OLS)
    print("Running H1 (Early Funding)...")
    h1_df = baseline[baseline["early_funding_musd"].notna()].copy()
    if h1_df.empty:
        print("Warning: No H1 data found.")
        # Create empty placeholder
        h1_table = pd.DataFrame(columns=['variable', 'coefficient', 'std_err', 't', 'p_value', 'ci_lower', 'ci_upper'])
    else:
        h1_model = test_h1_early_funding(h1_df)
        h1_table = pd.DataFrame({
            "variable": h1_model.params.index,
            "coefficient": h1_model.params.values,
            "std_err": h1_model.bse.values,
            "t": h1_model.tvalues.values,
            "p_value": h1_model.pvalues.values,
            "ci_lower": h1_model.conf_int()[0].values,
            "ci_upper": h1_model.conf_int()[1].values
        })
    h1_table.to_csv(out_dir / "h1_coefficients.csv", index=False)

    # --- H2 DV: Series B+ progression within 17 months
    print("Creating H2 Survival DV...")
    surv = create_survival_seriesb_progression(
        df_baseline=dfs["t0"], df_mid1=dfs["tm1"], df_mid2=dfs["tm2"], df_endpoint=dfs["t1"],
        baseline_date="2021-12-01", mid1_date="2022-01-01", mid2_date="2022-05-01", endpoint_date="2023-05-01"
    )
    id_col = "CompanyID" if "CompanyID" in baseline.columns else "company_id"
    analysis = baseline.merge(surv.rename(columns={"company_id": id_col}), on=id_col, how="inner")
    analysis["survival"] = analysis["Y_primary"]  # M&A censored primary DV only (Week 1)
    analysis.to_csv(out_dir / "h2_analysis_dataset.csv", index=False)

    # --- H2 main: survival ~ z_vagueness * high_integration_cost + controls (Logit)
    print("Running H2 (Main Survival)...")
    h2_df = analysis[analysis["survival"].notna()].copy()
    if h2_df.empty:
        print("Warning: No H2 data found.")
        # Create empty placeholder
        h2_table = pd.DataFrame(columns=['variable', 'coefficient', 'std_err', 'z', 'p_value', 'ci_lower', 'ci_upper'])
    else:
        h2_model = test_h2_main_survival(h2_df)
        h2_table = pd.DataFrame({
            "variable": h2_model.params.index,
            "coefficient": h2_model.params.values,
            "std_err": h2_model.bse.values,
            "z": h2_model.tvalues.values,
            "p_value": h2_model.pvalues.values,
            "ci_lower": h2_model.conf_int()[0].values,
            "ci_upper": h2_model.conf_int()[1].values
        })
    h2_table.to_csv(out_dir / "h2_main_coefficients.csv", index=False)

    print("\n✓ Week‑1 outputs written:")
    for f in ["h1_coefficients.csv", "h2_main_coefficients.csv", "h2_analysis_dataset.csv"]:
        print("  -", out_dir / f)


if __name__ == "__main__":
    main()