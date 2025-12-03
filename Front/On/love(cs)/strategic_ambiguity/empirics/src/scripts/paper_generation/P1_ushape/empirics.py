#!/usr/bin/env python3
"""
P1: U-Shape - When Vagueness Pays
Empirics Module - 나대용 🐅 (Builder)

Variables:
- vagueness_score: V = 0.6 * S_cat + 0.4 * S_concdef
- survival: Binary (survived 3+ years)
- funding: Log(total funding amount)
- exercisability: Hardware/Software classification

Models:
- H1: OLS regression for funding
- H2: Logit with interaction for survival
"""

import numpy as np
import pandas as pd
from scipy import stats
from dataclasses import dataclass
from typing import Tuple, Dict, Any
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Reproducibility
SEED = 42
np.random.seed(SEED)


@dataclass
class P1Config:
    """Configuration for P1 empirics"""
    n_firms: int = 1000
    hw_ratio: float = 0.23  # 23% hardware (NVCA 2023)
    base_survival_rate: float = 0.35
    vagueness_effect_sw: float = 0.15  # Positive for software
    vagueness_effect_hw: float = -0.25  # Negative for hardware


def generate_dummy_data(config: P1Config = P1Config()) -> pd.DataFrame:
    """
    Generate dummy data for P1 analysis.

    Returns:
        DataFrame with columns: firm_id, vagueness_score, is_hardware,
                               survival, funding, sector, founding_year
    """
    n = config.n_firms

    # Generate vagueness scores (0-1 scale)
    vagueness_score = np.random.beta(2, 5, n)  # Skewed toward low vagueness

    # Hardware/Software classification
    is_hardware = np.random.binomial(1, config.hw_ratio, n)

    # Sector (categorical)
    sectors = ['SaaS', 'Fintech', 'Healthcare', 'Consumer', 'DeepTech', 'Hardware']
    sector = np.random.choice(sectors, n, p=[0.25, 0.15, 0.15, 0.15, 0.15, 0.15])

    # Founding year
    founding_year = np.random.choice(range(2010, 2023), n)

    # Generate survival with U-shape effect
    # U-shape: both low and high vagueness can be optimal
    # V(1-V) creates inverted U, so we need -V(1-V) for U-shape
    u_shape_effect = -4 * (vagueness_score - 0.5) ** 2 + 1  # U-shape centered at 0.5

    # Moderation by hardware
    vagueness_effect = np.where(
        is_hardware == 1,
        config.vagueness_effect_hw * vagueness_score,  # Negative for HW
        config.vagueness_effect_sw * vagueness_score   # Positive for SW
    )

    # Survival probability
    survival_prob = config.base_survival_rate + 0.1 * u_shape_effect + vagueness_effect
    survival_prob = np.clip(survival_prob, 0.05, 0.95)
    survival = np.random.binomial(1, survival_prob)

    # Funding (log-normal, affected by vagueness)
    log_funding_base = 15 + np.random.normal(0, 1.5, n)  # ~$3M median
    funding_effect = -0.3 * vagueness_score + 0.2 * survival
    log_funding = log_funding_base + funding_effect
    funding = np.exp(log_funding)

    df = pd.DataFrame({
        'firm_id': range(n),
        'vagueness_score': vagueness_score,
        'is_hardware': is_hardware,
        'survival': survival,
        'funding': funding,
        'log_funding': log_funding,
        'sector': sector,
        'founding_year': founding_year
    })

    # Z-standardize vagueness for regression
    df['z_vagueness'] = (df['vagueness_score'] - df['vagueness_score'].mean()) / df['vagueness_score'].std()
    df['z_vagueness_sq'] = df['z_vagueness'] ** 2

    return df


def run_h1_ols(df: pd.DataFrame) -> Dict[str, Any]:
    """
    H1: Vagueness has U-shaped relationship with funding (OLS)

    Model: log(Funding) = β₀ + β₁V + β₂V² + controls
    """
    # OLS regression
    formula = 'log_funding ~ z_vagueness + z_vagueness_sq + is_hardware + C(sector) + C(founding_year)'
    model = smf.ols(formula, data=df).fit()

    results = {
        'model': model,
        'beta_v': model.params.get('z_vagueness', np.nan),
        'beta_v_sq': model.params.get('z_vagueness_sq', np.nan),
        'p_v': model.pvalues.get('z_vagueness', np.nan),
        'p_v_sq': model.pvalues.get('z_vagueness_sq', np.nan),
        'r_squared': model.rsquared,
        'n_obs': model.nobs,
        'u_shape': model.params.get('z_vagueness_sq', 0) > 0  # U-shape if positive
    }

    return results


def run_h2_logit(df: pd.DataFrame) -> Dict[str, Any]:
    """
    H2: Modularity moderates vagueness effect on survival (Logit)

    Model: Pr(Survival=1) = Λ(β₀ + β₁V + β₂H + β₃(V×H) + controls)
    """
    # Add interaction term
    df = df.copy()
    df['vagueness_x_hardware'] = df['z_vagueness'] * df['is_hardware']

    # Logit regression
    formula = 'survival ~ z_vagueness + is_hardware + vagueness_x_hardware + C(sector)'
    model = smf.logit(formula, data=df).fit(disp=0)

    results = {
        'model': model,
        'beta_v': model.params.get('z_vagueness', np.nan),
        'beta_hw': model.params.get('is_hardware', np.nan),
        'beta_interaction': model.params.get('vagueness_x_hardware', np.nan),
        'p_v': model.pvalues.get('z_vagueness', np.nan),
        'p_hw': model.pvalues.get('is_hardware', np.nan),
        'p_interaction': model.pvalues.get('vagueness_x_hardware', np.nan),
        'pseudo_r_squared': model.prsquared,
        'n_obs': model.nobs,
        'hw_penalty': model.params.get('vagueness_x_hardware', 0) < 0
    }

    # Marginal effects for interpretation
    # Software: effect = beta_v
    # Hardware: effect = beta_v + beta_interaction
    results['marginal_effect_sw'] = results['beta_v']
    results['marginal_effect_hw'] = results['beta_v'] + results['beta_interaction']

    return results


def compute_coefficients_table(h1_results: Dict, h2_results: Dict) -> pd.DataFrame:
    """Create coefficient table for export"""
    rows = [
        {
            'hypothesis': 'H1',
            'variable': 'Vagueness (z)',
            'coefficient': h1_results['beta_v'],
            'p_value': h1_results['p_v'],
            'model': 'OLS'
        },
        {
            'hypothesis': 'H1',
            'variable': 'Vagueness² (z²)',
            'coefficient': h1_results['beta_v_sq'],
            'p_value': h1_results['p_v_sq'],
            'model': 'OLS'
        },
        {
            'hypothesis': 'H2',
            'variable': 'Vagueness (z)',
            'coefficient': h2_results['beta_v'],
            'p_value': h2_results['p_v'],
            'model': 'Logit'
        },
        {
            'hypothesis': 'H2',
            'variable': 'Hardware',
            'coefficient': h2_results['beta_hw'],
            'p_value': h2_results['p_hw'],
            'model': 'Logit'
        },
        {
            'hypothesis': 'H2',
            'variable': 'Vagueness × Hardware',
            'coefficient': h2_results['beta_interaction'],
            'p_value': h2_results['p_interaction'],
            'model': 'Logit'
        }
    ]
    return pd.DataFrame(rows)


def run_robustness_checks(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Run robustness checks as specified in theory.md
    """
    results = {}

    # 1. Subsample: Serial entrepreneurs (simulated as top funding quartile)
    serial_df = df[df['funding'] > df['funding'].quantile(0.75)]
    if len(serial_df) > 50:
        h2_serial = run_h2_logit(serial_df)
        results['serial_entrepreneurs'] = {
            'beta_interaction': h2_serial['beta_interaction'],
            'p_interaction': h2_serial['p_interaction'],
            'n': len(serial_df)
        }

    # 2. Time period split
    early_df = df[df['founding_year'] <= 2016]
    late_df = df[df['founding_year'] > 2016]

    if len(early_df) > 50 and len(late_df) > 50:
        h2_early = run_h2_logit(early_df)
        h2_late = run_h2_logit(late_df)
        results['time_split'] = {
            'early_beta': h2_early['beta_interaction'],
            'late_beta': h2_late['beta_interaction'],
            'consistent_sign': np.sign(h2_early['beta_interaction']) == np.sign(h2_late['beta_interaction'])
        }

    # 3. Sector-specific effects
    sector_effects = {}
    for sector in df['sector'].unique():
        sector_df = df[df['sector'] == sector]
        if len(sector_df) > 30:
            try:
                formula = 'survival ~ z_vagueness * is_hardware'
                model = smf.logit(formula, data=sector_df).fit(disp=0)
                sector_effects[sector] = model.params.get('z_vagueness:is_hardware', np.nan)
            except:
                sector_effects[sector] = np.nan
    results['sector_effects'] = sector_effects

    return results


def main():
    """Main execution for P1 empirics"""
    print("=" * 70)
    print("P1: U-Shape - When Vagueness Pays")
    print("Builder: 나대용 🐅")
    print("=" * 70)

    # Generate data
    print("\n📊 Generating dummy data...")
    df = generate_dummy_data()
    print(f"   N = {len(df)}, Hardware ratio = {df['is_hardware'].mean():.1%}")

    # Run H1
    print("\n📈 Running H1 (OLS)...")
    h1 = run_h1_ols(df)
    print(f"   β(V) = {h1['beta_v']:.4f} (p = {h1['p_v']:.4f})")
    print(f"   β(V²) = {h1['beta_v_sq']:.4f} (p = {h1['p_v_sq']:.4f})")
    print(f"   U-shape confirmed: {h1['u_shape']}")

    # Run H2
    print("\n📈 Running H2 (Logit)...")
    h2 = run_h2_logit(df)
    print(f"   β(V×HW) = {h2['beta_interaction']:.4f} (p = {h2['p_interaction']:.4f})")
    print(f"   Hardware penalty confirmed: {h2['hw_penalty']}")
    print(f"   Marginal effect (SW): {h2['marginal_effect_sw']:.4f}")
    print(f"   Marginal effect (HW): {h2['marginal_effect_hw']:.4f}")

    # Robustness
    print("\n🔍 Running robustness checks...")
    robustness = run_robustness_checks(df)

    # Coefficient table
    coef_table = compute_coefficients_table(h1, h2)
    print("\n📋 Coefficient Table:")
    print(coef_table.to_string(index=False))

    print("\n✅ P1 Empirics Complete!")

    return df, h1, h2, robustness, coef_table


if __name__ == "__main__":
    df, h1, h2, robustness, coef_table = main()
