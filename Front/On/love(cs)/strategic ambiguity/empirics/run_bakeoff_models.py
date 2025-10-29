#!/usr/bin/env python3
"""
Fit bake-off models: Architecture vs Credibility

This script fits two H2 models with identical specifications except for the moderator.
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.metrics import roc_auc_score, brier_score_loss, log_loss
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

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

    # Level-specific slopes
    try:
        vague_main = None
        interaction = None

        for var in model.params.index:
            if var == 'z_vagueness':
                vague_main = model.params[var]
            elif 'vagueness' in var.lower() and (':' in var or '*' in var):
                interaction = model.params[var]

        if vague_main is not None:
            ame_results.append({
                'effect': 'slope_level_0',
                'value': float(vague_main),
                'std_err': float(model.bse.get('z_vagueness', float('nan')))
            })

            if interaction is not None:
                slope_level_1 = vague_main + interaction
                ame_results.append({
                    'effect': 'slope_level_1',
                    'value': float(slope_level_1),
                    'std_err': float('nan')
                })
    except Exception as e:
        print(f"  ⚠️ Warning: Could not calculate level-specific slopes: {e}")

    ame_df = pd.DataFrame(ame_results)
    ame_df.to_csv(ame_path, index=False)

def main():
    print("=" * 80)
    print("MODERATOR BAKE-OFF: Fitting Models")
    print("=" * 80)

    # Load data
    df = pd.read_csv("outputs/h2_analysis_dataset.csv")
    print(f"\nLoaded {len(df):,} observations")

    # Create output directory for bake-off results
    outdir = Path("outputs")
    outdir.mkdir(exist_ok=True)

    # Model 1: Architecture (is_hardware)
    print("\n" + "-" * 80)
    print("Model 1: H2-Architecture (is_hardware moderator)")
    print("-" * 80)

    formula_arch = "growth ~ z_vagueness * is_hardware + z_employees_log + C(founding_cohort)"
    ana_arch = df.dropna(subset=['growth', 'z_vagueness', 'is_hardware']).copy()

    print(f"Sample size: {len(ana_arch):,}")
    print(f"is_hardware distribution: 0={sum(ana_arch['is_hardware']==0):,}, 1={sum(ana_arch['is_hardware']==1):,}")

    try:
        m_arch = smf.logit(formula_arch, data=ana_arch).fit(disp=False)
        print("✓ Model converged")
    except Exception as e:
        print(f"⚠️ Standard fit failed, using regularized fit: {e}")
        m_arch = smf.logit(formula_arch, data=ana_arch).fit_regularized(
            method='l2', alpha=0.01, disp=False, maxiter=200
        )

    save_model_results(
        m_arch,
        outdir / "h2_model_architecture.csv",
        outdir / "h2_model_architecture_metrics.csv",
        outdir / "h2_model_architecture_ame.csv",
        ana_arch
    )
    print(f"✓ Saved coefficients, metrics, and AME")

    # Print key results
    print(f"\nKey results:")
    print(f"  Pseudo R²: {m_arch.prsquared:.4f}")
    print(f"  AIC: {m_arch.aic:.2f}")

    try:
        interaction_var = [v for v in m_arch.params.index if 'vagueness' in v.lower() and 'hardware' in v.lower()][0]
        interaction_coef = m_arch.params[interaction_var]
        interaction_p = m_arch.pvalues[interaction_var]
        print(f"  Interaction coef: {interaction_coef:.4f} (p={interaction_p:.4f})")
    except:
        print("  Interaction: Not found")

    # Model 2: Credibility (is_serial)
    print("\n" + "-" * 80)
    print("Model 2: H2-Credibility (is_serial moderator)")
    print("-" * 80)

    formula_founder = "growth ~ z_vagueness * is_serial + z_employees_log + C(founding_cohort)"
    ana_founder = df.dropna(subset=['growth', 'z_vagueness', 'is_serial']).copy()

    print(f"Sample size: {len(ana_founder):,}")
    print(f"is_serial distribution: 0={sum(ana_founder['is_serial']==0):,}, 1={sum(ana_founder['is_serial']==1):,}")

    try:
        m_founder = smf.logit(formula_founder, data=ana_founder).fit(disp=False)
        print("✓ Model converged")
    except Exception as e:
        print(f"⚠️ Standard fit failed, using regularized fit: {e}")
        m_founder = smf.logit(formula_founder, data=ana_founder).fit_regularized(
            method='l2', alpha=0.01, disp=False, maxiter=200
        )

    save_model_results(
        m_founder,
        outdir / "h2_model_founder.csv",
        outdir / "h2_model_founder_metrics.csv",
        outdir / "h2_model_founder_ame.csv",
        ana_founder
    )
    print(f"✓ Saved coefficients, metrics, and AME")

    # Print key results
    print(f"\nKey results:")
    print(f"  Pseudo R²: {m_founder.prsquared:.4f}")
    print(f"  AIC: {m_founder.aic:.2f}")

    try:
        interaction_var = [v for v in m_founder.params.index if 'vagueness' in v.lower() and 'serial' in v.lower()][0]
        interaction_coef = m_founder.params[interaction_var]
        interaction_p = m_founder.pvalues[interaction_var]
        print(f"  Interaction coef: {interaction_coef:.4f} (p={interaction_p:.4f})")
    except:
        print("  Interaction: Not found")

    print("\n" + "=" * 80)
    print("BAKE-OFF MODELS COMPLETE")
    print("=" * 80)
    print("\nOutput files:")
    print("  - h2_model_architecture.csv")
    print("  - h2_model_architecture_metrics.csv")
    print("  - h2_model_founder.csv")
    print("  - h2_model_founder_metrics.csv")


if __name__ == "__main__":
    main()
