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
import statsmodels.formula.api as smf
from sklearn.metrics import roc_auc_score, brier_score_loss, log_loss

sys.path.insert(0, str(Path(__file__).parent))

from modules.features import (
    engineer_features, compute_founder_credibility, compute_serial_entrepreneur, extract_sector_fe,
    create_survival_seriesb_progression, preprocess_for_h2
)
from modules.models import (
    test_h1_early_funding, test_h2_main_growth,
    test_h3_early_funding_interaction, test_h4_growth_interaction
)
from modules.plots import (
    fig_reversal_from_models, fig_founder_interactions
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

    # VERIFICATION: Ensure critical columns survived preprocessing
    print(f"\n📊 Post-preprocessing verification:")
    print(f"   founder_credibility present: {'founder_credibility' in base.columns}")
    if 'founder_credibility' in base.columns:
        print(f"   founder_credibility stats: mean={base['founder_credibility'].mean():.3f}, std={base['founder_credibility'].std():.3f}")
    print(f"   founder_serial present: {'founder_serial' in base.columns}")
    if 'founder_serial' in base.columns:
        print(f"   founder_serial distribution: {base['founder_serial'].value_counts().to_dict()}")
        print(f"   Serial founders: {base['founder_serial'].sum():,} ({100*base['founder_serial'].mean():.1f}%)")
    print()

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

    # --- Ensure founder_serial and is_serial are present for bake-off ---
    # founder_serial should already be in analysis from preprocess_for_h2()
    if 'founder_serial' not in analysis.columns:
        print("  ⚠️  WARNING: founder_serial not found in analysis. Creating as all zeros.")
        analysis['founder_serial'] = 0

    # Create is_serial as alias for founder_serial (for backwards compatibility)
    if 'is_serial' not in analysis.columns:
        analysis['is_serial'] = analysis['founder_serial']
        print(f"  ℹ️  Created is_serial from founder_serial (n={analysis['is_serial'].sum():,})")

    # VERIFICATION: Final check before saving
    print(f"\n📊 Pre-save verification of analysis dataset:")
    print(f"   Total rows: {len(analysis):,}")
    print(f"   founder_serial present: {'founder_serial' in analysis.columns}")
    if 'founder_serial' in analysis.columns:
        print(f"   founder_serial: {analysis['founder_serial'].sum():,} serial ({100*analysis['founder_serial'].mean():.1f}%)")
    print(f"   is_serial present: {'is_serial' in analysis.columns}")
    if 'is_serial' in analysis.columns:
        print(f"   is_serial: {analysis['is_serial'].sum():,} serial ({100*analysis['is_serial'].mean():.1f}%)")
    print(f"   founder_credibility present: {'founder_credibility' in analysis.columns}")
    if 'founder_credibility' in analysis.columns:
        print(f"   founder_credibility: mean={analysis['founder_credibility'].mean():.3f}")
    print()

    # Save analysis dataset (NO column filtering - save ALL columns)
    analysis.to_csv(outdir / "h2_analysis_dataset.csv", index=False)
    print(f"✓ Saved: {outdir / 'h2_analysis_dataset.csv'}")
    print(f"  Columns saved: {list(analysis.columns)}")

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

    # --- H3: Early funding interaction with founder credibility (OLS) ---
    print("\n" + "="*80)
    print("H3: EARLY FUNDING × FOUNDER CREDIBILITY")
    print("="*80)
    h3_res = test_h3_early_funding_interaction(analysis)
    pd.DataFrame({
        'variable': h3_res.params.index,
        'coefficient': h3_res.params.values,
        'std_err': h3_res.bse.values,
        'stat': h3_res.tvalues.values,
        'p_value': h3_res.pvalues.values,
        'ci_lower': h3_res.conf_int()[0].values,
        'ci_upper': h3_res.conf_int()[1].values
    }).to_csv(outdir / "h3_coefficients.csv", index=False)
    print(f"✓ Saved: {outdir / 'h3_coefficients.csv'}")

    # --- H4: Growth interaction with founder credibility (Logit) ---
    print("\n" + "="*80)
    print("H4: GROWTH × FOUNDER CREDIBILITY")
    print("="*80)
    h4_res = test_h4_growth_interaction(analysis)
    pd.DataFrame({
        'variable': h4_res.params.index,
        'coefficient': h4_res.params.values,
        'std_err': h4_res.bse.values,
        'stat': h4_res.tvalues.values,
        'p_value': h4_res.pvalues.values,
        'ci_lower': h4_res.conf_int()[0].values,
        'ci_upper': h4_res.conf_int()[1].values
    }).to_csv(outdir / "h4_coefficients.csv", index=False)
    print(f"✓ Saved: {outdir / 'h4_coefficients.csv'}")

    # --- BAKE-OFF: Two H2 models with different moderators ---
    print("\n" + "="*80)
    print("MODERATOR BAKE-OFF: Architecture vs Credibility")
    print("="*80)

    def save_model_results(model, coef_path, metrics_path, ame_path, data_for_pred):
        """Helper to save model coefficients, fit metrics, and AME."""
        # Coefficients
        coef_df = pd.DataFrame({
            'variable': model.params.index,
            'coefficient': model.params.values,
            'std_err': model.bse.values,
            'z': model.tvalues.values,
            'p_value': model.pvalues.values,
            'ci_lower': model.conf_int()[0].values,
            'ci_upper': model.conf_int()[1].values
        })
        coef_df.to_csv(coef_path, index=False)

        # Predictions for additional metrics
        y_true = model.model.endog
        y_pred_proba = model.predict()

        # Calculate additional metrics
        try:
            auc = roc_auc_score(y_true, y_pred_proba)
        except:
            auc = float('nan')

        try:
            brier = brier_score_loss(y_true, y_pred_proba)
        except:
            brier = float('nan')

        try:
            logloss = log_loss(y_true, y_pred_proba)
        except:
            logloss = float('nan')

        # Fit metrics
        metrics_df = pd.DataFrame([{
            'nobs': float(getattr(model, 'nobs', float('nan'))),
            'prsquared': float(getattr(model, 'prsquared', float('nan'))),
            'aic': float(getattr(model, 'aic', float('nan'))),
            'bic': float(getattr(model, 'bic', float('nan'))),
            'llf': float(getattr(model, 'llf', float('nan'))),
            'converged': bool(getattr(model, 'mle_retvals', {}).get('converged', True)),
            'auc': float(auc),
            'brier': float(brier),
            'logloss': float(logloss)
        }])
        metrics_df.to_csv(metrics_path, index=False)

        # AME and level-specific slopes
        # This is simplified - for production, use get_margeff()
        # For now, calculate marginal effects at representative values
        ame_results = []

        # Get marginal effect of z_vagueness (AME)
        try:
            marg_eff = model.get_margeff(at='overall')
            vagueness_vars = [v for v in marg_eff.margeff_names if 'vagueness' in v.lower()]
            if vagueness_vars:
                vague_idx = marg_eff.margeff_names.index(vagueness_vars[0])
                ame_vagueness = marg_eff.margeff[vague_idx]
                ame_se = marg_eff.margeff_se[vague_idx]
            else:
                ame_vagueness = float('nan')
                ame_se = float('nan')
        except:
            ame_vagueness = float('nan')
            ame_se = float('nan')

        ame_results.append({
            'effect': 'AME_z_vagueness',
            'value': float(ame_vagueness),
            'std_err': float(ame_se)
        })

        # Level-specific slopes (manual calculation from coefficients)
        # For Architecture: β_vagueness (level 0), β_vagueness + β_interaction (level 1)
        # For Founder: β_vagueness (level 0), β_vagueness + β_interaction (level 1)
        try:
            # Find main effect and interaction
            vague_main = None
            interaction = None

            for var in model.params.index:
                if var == 'z_vagueness':
                    vague_main = model.params[var]
                elif 'vagueness' in var.lower() and (':' in var or '*' in var):
                    interaction = model.params[var]

            if vague_main is not None:
                # Level 0 (reference): just main effect
                ame_results.append({
                    'effect': 'slope_level_0',
                    'value': float(vague_main),
                    'std_err': float(model.bse.get('z_vagueness', float('nan')))
                })

                # Level 1: main + interaction
                if interaction is not None:
                    slope_level_1 = vague_main + interaction
                    # Note: SE calculation for sum requires covariance, simplified here
                    ame_results.append({
                        'effect': 'slope_level_1',
                        'value': float(slope_level_1),
                        'std_err': float('nan')  # Requires full covariance matrix
                    })
        except Exception as e:
            print(f"  ⚠️ Warning: Could not calculate level-specific slopes: {e}")

        ame_df = pd.DataFrame(ame_results)
        ame_df.to_csv(ame_path, index=False)

    # Model 1: Architecture (is_hardware)
    print("\nFitting H2-Architecture (is_hardware moderator)...")
    formula_arch = "growth ~ z_vagueness * is_hardware + z_employees_log + C(founding_cohort)"
    ana_arch = analysis.dropna(subset=['growth', 'z_vagueness', 'is_hardware']).copy()
    try:
        m_arch = smf.logit(formula_arch, data=ana_arch).fit(disp=False)
    except Exception:
        m_arch = smf.logit(formula_arch, data=ana_arch).fit_regularized(method='l1', alpha=0.1, disp=False, maxiter=200, warn_convergence=False)

    save_model_results(
        m_arch,
        outdir / "h2_model_architecture.csv",
        outdir / "h2_model_architecture_metrics.csv",
        outdir / "h2_model_architecture_ame.csv",
        ana_arch
    )
    print(f"✓ Saved: {outdir / 'h2_model_architecture.csv'}")
    print(f"✓ Saved: {outdir / 'h2_model_architecture_metrics.csv'}")
    print(f"✓ Saved: {outdir / 'h2_model_architecture_ame.csv'}")

    # Model 2: Credibility (is_serial)
    print("\nFitting H2-Credibility (is_serial moderator)...")
    formula_founder = "growth ~ z_vagueness * is_serial + z_employees_log + C(founding_cohort)"
    ana_founder = analysis.dropna(subset=['growth', 'z_vagueness', 'is_serial']).copy()
    try:
        m_founder = smf.logit(formula_founder, data=ana_founder).fit(disp=False)
    except Exception:
        m_founder = smf.logit(formula_founder, data=ana_founder).fit_regularized(method='l1', alpha=0.1, disp=False, maxiter=200, warn_convergence=False)

    save_model_results(
        m_founder,
        outdir / "h2_model_founder.csv",
        outdir / "h2_model_founder_metrics.csv",
        outdir / "h2_model_founder_ame.csv",
        ana_founder
    )
    print(f"✓ Saved: {outdir / 'h2_model_founder.csv'}")
    print(f"✓ Saved: {outdir / 'h2_model_founder_metrics.csv'}")
    print(f"✓ Saved: {outdir / 'h2_model_founder_ame.csv'}")

    print("\n" + "="*80)
    print("BAKE-OFF COMPLETE")
    print("="*80)

    # --- GENERATE FIGURES ---
    print("\n" + "="*80)
    print("GENERATING FIGURES")
    print("="*80)

    figures_dir = outdir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    # Figure 1: The Reversal (H1 + H2)
    print("\nGenerating Figure 1: The Reversal...")
    try:
        fig_reversal_from_models(analysis, h1_res, h2_res, figures_dir)
    except Exception as e:
        print(f"  ⚠️ Error generating Figure 1: {e}")

    # Figure 2: Founder Interactions (H3 + H4)
    print("\nGenerating Figure 2a/2b: Founder Interactions...")
    try:
        fig_founder_interactions(analysis, h3_res, h4_res, figures_dir)
    except Exception as e:
        print(f"  ⚠️ Error generating Figure 2: {e}")

    print("\n" + "="*80)
    print("ONE-TOUCH EXECUTION COMPLETE")
    print("="*80)

    print("\nGenerated Files:")
    print("\nCoefficient Tables:")
    for p in sorted(outdir.glob('*.csv')):
        print(f"  - {p.name}")
    print("\nFigures:")
    for p in sorted(figures_dir.glob('*.png')):
        print(f"  - figures/{p.name}")

if __name__ == "__main__":
    main()
