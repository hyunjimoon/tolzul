#!/usr/bin/env python3
"""
Fit bake-off models: Architecture vs Credibility

This script fits two H2 models with identical specifications except for the moderator.
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

def save_model_results(model, coef_path, metrics_path):
    """Helper to save model coefficients and fit metrics."""
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

    # Fit metrics
    metrics_df = pd.DataFrame([{
        'nobs': float(getattr(model, 'nobs', float('nan'))),
        'prsquared': float(getattr(model, 'prsquared', float('nan'))),
        'aic': float(getattr(model, 'aic', float('nan'))),
        'bic': float(getattr(model, 'bic', float('nan'))),
        'llf': float(getattr(model, 'llf', float('nan'))),
        'converged': bool(getattr(model, 'mle_retvals', {}).get('converged', True))
    }])
    metrics_df.to_csv(metrics_path, index=False)

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

    save_model_results(m_arch, outdir / "h2_model_architecture.csv", outdir / "h2_model_architecture_metrics.csv")
    print(f"✓ Saved coefficients and metrics")

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

    save_model_results(m_founder, outdir / "h2_model_founder.csv", outdir / "h2_model_founder_metrics.csv")
    print(f"✓ Saved coefficients and metrics")

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
