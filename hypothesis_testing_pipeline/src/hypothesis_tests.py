"""
Hypothesis Testing Module

Implements H1 and H2 models for testing promise vagueness effects on
funding outcomes, conditional on sector integration cost.

Models:
    H1: Early Funding ~ Vagueness + Controls (OLS)
        Expected: α₁ < 0 (vagueness negatively affects early funding)

    H2: Later Success ~ Vagueness × Integration Cost + Early Funding + Controls (Logit)
        Expected: β₁ > 0 in modular sectors (positive main effect)
                  β₃ < 0 (interaction term, attenuated in integrated sectors)
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.regression.linear_model import RegressionResultsWrapper
from statsmodels.discrete.discrete_model import BinaryResultsWrapper
from typing import Dict, Tuple, Optional, Union
import xarray as xr


# =============================================================================
# H1: EARLY FUNDING ~ VAGUENESS (OLS)
# =============================================================================

def test_h1_early_funding(
    df: pd.DataFrame,
    formula: str = "early_funding_musd ~ vagueness + employees_log + year_founded"
) -> RegressionResultsWrapper:
    """
    Test H1: Early funding amount is negatively affected by vagueness.

    Model: log(Early Funding) ~ Vagueness + Controls
    Expected: α₁ < 0

    Args:
        df: DataFrame with required variables
        formula: R-style formula for regression (default includes basic controls)

    Returns:
        Statsmodels OLS results object

    Interpretation:
        - Vagueness coefficient (α₁) should be negative
        - Negative coefficient means more vague promises lead to lower funding
    """
    # Drop missing values
    df_clean = df.dropna(subset=['early_funding_musd', 'vagueness'])

    if len(df_clean) == 0:
        raise ValueError("No valid observations after removing missing values")

    print(f"\n{'='*80}")
    print("H1: EARLY FUNDING ~ VAGUENESS (OLS)")
    print(f"{'='*80}")
    print(f"Sample size: {len(df_clean)}")
    print(f"Formula: {formula}")

    # Fit OLS model
    model = smf.ols(formula, data=df_clean).fit()

    print(f"\n{model.summary()}")

    # Check hypothesis
    vagueness_coef = model.params.get('vagueness', np.nan)
    vagueness_pval = model.pvalues.get('vagueness', np.nan)

    print(f"\n{'='*80}")
    print("H1 HYPOTHESIS TEST")
    print(f"{'='*80}")
    print(f"Expected: α₁ < 0 (vagueness negatively affects early funding)")
    print(f"Estimated α₁: {vagueness_coef:.6f}")
    print(f"p-value: {vagueness_pval:.4f}")
    print(f"95% CI: [{model.conf_int().loc['vagueness', 0]:.6f}, "
          f"{model.conf_int().loc['vagueness', 1]:.6f}]")

    if vagueness_coef < 0 and vagueness_pval < 0.05:
        print(f"✓ H1 SUPPORTED: Vagueness has significant negative effect (α₁={vagueness_coef:.4f}, p<0.05)")
    elif vagueness_coef < 0:
        print(f"~ H1 PARTIAL: Vagueness negative but not significant (α₁={vagueness_coef:.4f}, p={vagueness_pval:.4f})")
    else:
        print(f"✗ H1 NOT SUPPORTED: Vagueness coefficient not negative (α₁={vagueness_coef:.4f})")

    return model


# =============================================================================
# H2: LATER SUCCESS ~ VAGUENESS × INTEGRATION COST (LOGIT)
# =============================================================================

def test_h2_later_success(
    df: pd.DataFrame,
    formula: str = ("later_success ~ vagueness * high_integration_cost + "
                   "early_funding_musd + employees_log + year_founded")
) -> BinaryResultsWrapper:
    """
    Test H2: Vagueness effect on later success is moderated by integration cost.

    Model: Later Success ~ Vagueness × Integration Cost + Early Funding + Controls
    Expected: β₁ > 0 (positive in modular sectors)
              β₃ < 0 (negative interaction, attenuated in integrated sectors)

    Args:
        df: DataFrame with required variables
        formula: R-style formula for logit regression

    Returns:
        Statsmodels logit results object

    Interpretation:
        - β₁ (vagueness main effect): effect in modular sectors (high_integration_cost=0)
        - β₃ (interaction): differential effect in integrated sectors
        - Total effect in integrated = β₁ + β₃
    """
    # Drop missing values
    required_vars = ['later_success', 'vagueness', 'high_integration_cost', 'early_funding_musd']
    df_clean = df.dropna(subset=required_vars)

    if len(df_clean) == 0:
        raise ValueError("No valid observations after removing missing values")

    print(f"\n{'='*80}")
    print("H2: LATER SUCCESS ~ VAGUENESS × INTEGRATION COST (LOGIT)")
    print(f"{'='*80}")
    print(f"Sample size: {len(df_clean)}")
    print(f"Formula: {formula}")
    print(f"Success rate: {df_clean['later_success'].mean():.2%}")

    # Fit logit model
    model = smf.logit(formula, data=df_clean).fit(disp=False)

    print(f"\n{model.summary()}")

    # Extract key coefficients
    beta1 = model.params.get('vagueness', np.nan)
    beta3 = model.params.get('vagueness:high_integration_cost', np.nan)
    pval1 = model.pvalues.get('vagueness', np.nan)
    pval3 = model.pvalues.get('vagueness:high_integration_cost', np.nan)

    # Total effect in integrated sectors
    total_effect_integrated = beta1 + beta3

    print(f"\n{'='*80}")
    print("H2 HYPOTHESIS TEST")
    print(f"{'='*80}")
    print(f"Expected: β₁ > 0 (positive in modular), β₃ < 0 (attenuated in integrated)")
    print(f"\nβ₁ (Vagueness main effect - modular sectors): {beta1:.6f} (p={pval1:.4f})")
    print(f"   95% CI: [{model.conf_int().loc['vagueness', 0]:.6f}, "
          f"{model.conf_int().loc['vagueness', 1]:.6f}]")
    print(f"\nβ₃ (Interaction term): {beta3:.6f} (p={pval3:.4f})")
    if 'vagueness:high_integration_cost' in model.conf_int().index:
        print(f"   95% CI: [{model.conf_int().loc['vagueness:high_integration_cost', 0]:.6f}, "
              f"{model.conf_int().loc['vagueness:high_integration_cost', 1]:.6f}]")
    print(f"\nTotal effect in integrated sectors (β₁+β₃): {total_effect_integrated:.6f}")

    # Check hypothesis
    h2_part1 = beta1 > 0 and pval1 < 0.05
    h2_part2 = beta3 < 0

    print(f"\n{'='*80}")
    if h2_part1 and h2_part2:
        print(f"✓ H2 FULLY SUPPORTED")
        print(f"  - Vagueness helps in modular sectors (β₁={beta1:.4f}, p<0.05)")
        print(f"  - Effect attenuated in integrated sectors (β₃={beta3:.4f})")
    elif h2_part1:
        print(f"~ H2 PARTIALLY SUPPORTED")
        print(f"  - Vagueness helps in modular sectors (β₁={beta1:.4f}, p<0.05)")
        print(f"  - But interaction term not negative (β₃={beta3:.4f})")
    else:
        print(f"✗ H2 NOT SUPPORTED")
        print(f"  - Main effect not positive or significant (β₁={beta1:.4f}, p={pval1:.4f})")

    return model


# =============================================================================
# COMBINED ANALYSIS
# =============================================================================

def run_full_hypothesis_tests(
    df: pd.DataFrame,
    h1_formula: Optional[str] = None,
    h2_formula: Optional[str] = None
) -> Dict[str, Union[RegressionResultsWrapper, BinaryResultsWrapper]]:
    """
    Run both H1 and H2 tests and return results.

    Args:
        df: DataFrame with all required variables
        h1_formula: Optional custom formula for H1
        h2_formula: Optional custom formula for H2

    Returns:
        Dictionary with 'h1' and 'h2' model results
    """
    results = {}

    print("\n" + "="*80)
    print("COMPREHENSIVE HYPOTHESIS TESTING PIPELINE")
    print("="*80)
    print(f"\nTotal observations: {len(df)}")
    print(f"\nVariable availability:")
    required_vars = [
        'vagueness', 'early_funding_musd', 'later_success',
        'high_integration_cost', 'employees_log', 'year_founded'
    ]
    for var in required_vars:
        if var in df.columns:
            n_valid = df[var].notna().sum()
            print(f"  - {var}: {n_valid}/{len(df)} ({n_valid/len(df)*100:.1f}%)")

    # Run H1
    try:
        if h1_formula:
            results['h1'] = test_h1_early_funding(df, h1_formula)
        else:
            results['h1'] = test_h1_early_funding(df)
    except Exception as e:
        print(f"\n❌ H1 test failed: {e}")
        results['h1'] = None

    # Run H2
    try:
        if h2_formula:
            results['h2'] = test_h2_later_success(df, h2_formula)
        else:
            results['h2'] = test_h2_later_success(df)
    except Exception as e:
        print(f"\n❌ H2 test failed: {e}")
        results['h2'] = None

    print("\n" + "="*80)
    print("HYPOTHESIS TESTING COMPLETE")
    print("="*80)

    return results


# =============================================================================
# RESULTS TO XARRAY
# =============================================================================

def results_to_xarray(results: Dict[str, Union[RegressionResultsWrapper, BinaryResultsWrapper]]) -> xr.Dataset:
    """
    Convert statsmodels results to xarray Dataset for storage.

    Args:
        results: Dictionary of model results from run_full_hypothesis_tests

    Returns:
        xarray Dataset with coefficients, p-values, and metadata
    """
    # Extract H1 results
    h1_model = results.get('h1')
    h2_model = results.get('h2')

    data_vars = {}

    if h1_model is not None:
        h1_vars = list(h1_model.params.index)
        data_vars['h1_coef'] = (['h1_var'], h1_model.params.values)
        data_vars['h1_pval'] = (['h1_var'], h1_model.pvalues.values)
        data_vars['h1_stderr'] = (['h1_var'], h1_model.bse.values)

        # Confidence intervals
        ci = h1_model.conf_int()
        data_vars['h1_ci_lower'] = (['h1_var'], ci.iloc[:, 0].values)
        data_vars['h1_ci_upper'] = (['h1_var'], ci.iloc[:, 1].values)

    if h2_model is not None:
        h2_vars = list(h2_model.params.index)
        data_vars['h2_coef'] = (['h2_var'], h2_model.params.values)
        data_vars['h2_pval'] = (['h2_var'], h2_model.pvalues.values)
        data_vars['h2_stderr'] = (['h2_var'], h2_model.bse.values)

        # Confidence intervals
        ci = h2_model.conf_int()
        data_vars['h2_ci_lower'] = (['h2_var'], ci.iloc[:, 0].values)
        data_vars['h2_ci_upper'] = (['h2_var'], ci.iloc[:, 1].values)

    # Create dataset
    ds = xr.Dataset(
        data_vars,
        coords={
            'h1_var': h1_vars if h1_model else [],
            'h2_var': h2_vars if h2_model else []
        },
        attrs={
            'h1_nobs': int(h1_model.nobs) if h1_model else 0,
            'h1_rsquared': float(h1_model.rsquared) if h1_model else np.nan,
            'h1_rsquared_adj': float(h1_model.rsquared_adj) if h1_model else np.nan,
            'h1_aic': float(h1_model.aic) if h1_model else np.nan,
            'h2_nobs': int(h2_model.nobs) if h2_model else 0,
            'h2_pseudo_rsquared': float(h2_model.prsquared) if h2_model else np.nan,
            'h2_aic': float(h2_model.aic) if h2_model else np.nan,
        }
    )

    return ds


# =============================================================================
# RESULTS COMPARISON TABLE
# =============================================================================

def create_results_summary(results: Dict[str, Union[RegressionResultsWrapper, BinaryResultsWrapper]]) -> pd.DataFrame:
    """
    Create summary table comparing estimated vs expected signs.

    Args:
        results: Dictionary of model results

    Returns:
        DataFrame with hypothesis test summary
    """
    h1_model = results.get('h1')
    h2_model = results.get('h2')

    summary_data = []

    # H1 Summary
    if h1_model is not None:
        vagueness_coef = h1_model.params.get('vagueness', np.nan)
        vagueness_pval = h1_model.pvalues.get('vagueness', np.nan)

        summary_data.append({
            'Hypothesis': 'H1',
            'Parameter': 'α₁ (Vagueness)',
            'Expected Sign': 'Negative (<0)',
            'Estimated': vagueness_coef,
            'p-value': vagueness_pval,
            'Significant': '✓' if vagueness_pval < 0.05 else '✗',
            'Sign Match': '✓' if vagueness_coef < 0 else '✗',
            'Hypothesis Supported': '✓' if (vagueness_coef < 0 and vagueness_pval < 0.05) else '✗'
        })

    # H2 Summary
    if h2_model is not None:
        beta1 = h2_model.params.get('vagueness', np.nan)
        beta3 = h2_model.params.get('vagueness:high_integration_cost', np.nan)
        pval1 = h2_model.pvalues.get('vagueness', np.nan)
        pval3 = h2_model.pvalues.get('vagueness:high_integration_cost', np.nan)

        summary_data.append({
            'Hypothesis': 'H2',
            'Parameter': 'β₁ (Vagueness - modular)',
            'Expected Sign': 'Positive (>0)',
            'Estimated': beta1,
            'p-value': pval1,
            'Significant': '✓' if pval1 < 0.05 else '✗',
            'Sign Match': '✓' if beta1 > 0 else '✗',
            'Hypothesis Supported': '✓' if (beta1 > 0 and pval1 < 0.05) else '✗'
        })

        summary_data.append({
            'Hypothesis': 'H2',
            'Parameter': 'β₃ (Interaction)',
            'Expected Sign': 'Negative (<0)',
            'Estimated': beta3,
            'p-value': pval3,
            'Significant': '✓' if pval3 < 0.05 else '✗',
            'Sign Match': '✓' if beta3 < 0 else '✗',
            'Hypothesis Supported': '✗'  # Interaction less critical
        })

    summary_df = pd.DataFrame(summary_data)
    return summary_df


if __name__ == "__main__":
    # Example usage with simulated data
    print("Hypothesis Testing Module - Example Usage\n")
    print("=" * 80)

    # Create simulated data
    np.random.seed(42)
    n = 500

    simulated_data = pd.DataFrame({
        'vagueness': np.random.uniform(0, 1, n),
        'high_integration_cost': np.random.binomial(1, 0.3, n),
        'early_funding_musd': np.random.lognormal(1, 0.5, n),
        'later_success': np.random.binomial(1, 0.4, n),
        'employees_log': np.random.normal(3, 0.5, n),
        'year_founded': np.random.randint(2015, 2023, n)
    })

    # Introduce expected relationships
    simulated_data['early_funding_musd'] -= simulated_data['vagueness'] * 2  # H1: negative
    simulated_data['later_success'] = (
        (simulated_data['vagueness'] * 0.5 * (1 - simulated_data['high_integration_cost']) +
         np.random.normal(0, 0.1, n)) > 0.3
    ).astype(int)  # H2: positive in modular

    # Run tests
    results = run_full_hypothesis_tests(simulated_data)

    # Create summary
    print("\n" + "=" * 80)
    print("RESULTS SUMMARY TABLE")
    print("=" * 80)
    summary = create_results_summary(results)
    print(summary.to_string(index=False))
