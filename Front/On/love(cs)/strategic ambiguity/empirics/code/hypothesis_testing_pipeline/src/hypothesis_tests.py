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
    formula: str = ("early_funding_musd ~ z_vagueness + z_employees_log + "
                   "C(sector_fe) + C(founding_cohort)")
) -> RegressionResultsWrapper:
    """
    Test H1: Early funding amount is negatively affected by vagueness.

    Model: Early Funding ~ Vagueness + Controls
    Expected: α₁ < 0 (vagueness reduces early funding)

    Full specification (UPDATED - fixes from ChatGPT diagnosis):
        early_funding_musd ~ z_vagueness + z_employees_log +
                           C(sector_fe) + C(founding_cohort)

    Changes from original:
        - Uses z-scores for numerical stability
        - Dropped founder_credibility (constant, causes collinearity)
        - Dropped high_integration_cost (collinear with sector_fe)
        - Uses founding_cohort instead of year_founded (cohort effects)

    Args:
        df: DataFrame with required variables
        formula: R-style formula for regression (default includes full controls)

    Returns:
        Statsmodels OLS results object

    Interpretation:
        - Vagueness coefficient (α₁) should be negative
        - Negative coefficient means more vague promises lead to lower funding
        - Controls for founder quality, sector, firm size, and age
    """
    # Drop missing values
    df_clean = df.dropna(subset=['early_funding_musd', 'z_vagueness'])

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
    vagueness_coef = model.params.get('z_vagueness', np.nan)
    vagueness_pval = model.pvalues.get('z_vagueness', np.nan)

    print(f"\n{'='*80}")
    print("H1 HYPOTHESIS TEST")
    print(f"{'='*80}")
    print(f"Expected: α₁ < 0 (vagueness negatively affects early funding)")
    print(f"Estimated α₁: {vagueness_coef:.6f}")
    print(f"p-value: {vagueness_pval:.4f}")
    print(f"95% CI: [{model.conf_int().loc['z_vagueness', 0]:.6f}, "
          f"{model.conf_int().loc['z_vagueness', 1]:.6f}]")

    if vagueness_coef < 0 and vagueness_pval < 0.05:
        print(f"✓ H1 SUPPORTED: Vagueness has significant negative effect (α₁={vagueness_coef:.4f}, p<0.05)")
    elif vagueness_coef < 0:
        print(f"~ H1 PARTIAL: Vagueness negative but not significant (α₁={vagueness_coef:.4f}, p={vagueness_pval:.4f})")
    else:
        print(f"✗ H1 NOT SUPPORTED: Vagueness coefficient not negative (α₁={vagueness_coef:.4f})")

    return model


# =============================================================================
# H2: SURVIVAL ~ VAGUENESS × INTEGRATION COST (LOGIT)
# =============================================================================

def test_h2_main_survival(
    df: pd.DataFrame,
    formula: str = ("survival ~ z_vagueness * high_integration_cost + "
                   "z_employees_log + C(founding_cohort)")
) -> BinaryResultsWrapper:
    """
    Test H2 Main: Vagueness effect on survival is moderated by integration cost.

    ⚠️  CRITICAL: NO early_funding control (it's a MEDIATOR, not confounder)

    Model: Survival ~ Vagueness × Integration Cost + Controls
    Expected: β₁ > 0 (positive in modular sectors)
              β₃ < 0 (negative interaction, attenuated in integrated sectors)

    Full specification (UPDATED - fixes from ChatGPT diagnosis):
        survival ~ z_vagueness * high_integration_cost +
                   z_employees_log + C(founding_cohort)

    CRITICAL FIXES:
        1. DROPPED C(sector_fe) - collinear with high_integration_cost
        2. Uses z-scores for numerical stability
        3. DROPPED founder_credibility - constant (all zeros)
        4. Uses founding_cohort instead of year_founded

    For robustness with sector FE, use test_h2_robustness_sector_fe() instead.

    Args:
        df: DataFrame with required variables
        formula: R-style formula for logit regression

    Returns:
        Statsmodels logit results object

    Interpretation:
        - β₁ (vagueness main effect): effect in modular sectors (high_integration_cost=0)
        - β₃ (interaction): differential effect in integrated sectors
        - Total effect in integrated = β₁ + β₃
        - NO early_funding: it's a mediator in causal chain vagueness→funding→survival
    """
    # Drop missing values
    required_vars = ['survival', 'z_vagueness', 'high_integration_cost']
    df_clean = df.dropna(subset=required_vars)

    if len(df_clean) == 0:
        raise ValueError("No valid observations after removing missing values")

    print(f"\n{'='*80}")
    print("H2 MAIN: SURVIVAL ~ VAGUENESS × INTEGRATION COST (LOGIT)")
    print(f"{'='*80}")
    print(f"Sample size: {len(df_clean)}")
    print(f"Formula: {formula}")
    print(f"Survival rate: {df_clean['survival'].mean():.2%}")

    # Fit logit model
    model = smf.logit(formula, data=df_clean).fit(disp=False)

    print(f"\n{model.summary()}")

    # Extract key coefficients
    beta1 = model.params.get('z_vagueness', np.nan)
    beta3 = model.params.get('z_vagueness:high_integration_cost', np.nan)
    pval1 = model.pvalues.get('z_vagueness', np.nan)
    pval3 = model.pvalues.get('z_vagueness:high_integration_cost', np.nan)

    # Total effect in integrated sectors
    total_effect_integrated = beta1 + beta3

    print(f"\n{'='*80}")
    print("H2 HYPOTHESIS TEST")
    print(f"{'='*80}")
    print(f"Expected: β₁ > 0 (positive in modular), β₃ < 0 (attenuated in integrated)")
    print(f"\nβ₁ (Vagueness main effect - modular sectors): {beta1:.6f} (p={pval1:.4f})")
    print(f"   95% CI: [{model.conf_int().loc['z_vagueness', 0]:.6f}, "
          f"{model.conf_int().loc['z_vagueness', 1]:.6f}]")
    print(f"\nβ₃ (Interaction term): {beta3:.6f} (p={pval3:.4f})")
    if 'z_vagueness:high_integration_cost' in model.conf_int().index:
        print(f"   95% CI: [{model.conf_int().loc['z_vagueness:high_integration_cost', 0]:.6f}, "
              f"{model.conf_int().loc['z_vagueness:high_integration_cost', 1]:.6f}]")
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


def test_h2_robustness_sector_fe(
    df: pd.DataFrame,
    formula: str = ("survival ~ z_vagueness * ic_within + "
                   "z_employees_log + C(sector_fe) + C(founding_cohort)")
) -> BinaryResultsWrapper:
    """
    Test H2 Robustness: With sector FE using within-sector centered integration cost.

    This robustness check addresses collinearity by using ic_within (sector-centered
    integration cost) instead of high_integration_cost. This allows including both
    sector FE (captures between-sector differences) and ic_within (captures
    within-sector variation in integration cost).

    Model: Survival ~ Vagueness × IC_within + Controls + Sector FE
    Expected: Similar pattern to H2 Main (β₁ > 0, β₃ < 0)

    Args:
        df: DataFrame with required variables (must have ic_within from preprocess_for_h2)
        formula: R-style formula for logit regression

    Returns:
        Statsmodels logit results object

    Interpretation:
        - Tests whether vagueness effect persists when controlling for sector FE
        - ic_within captures within-sector variation in integration cost
        - Complements H2 Main's between-sector comparison
    """
    # Drop missing values
    required_vars = ['survival', 'z_vagueness', 'ic_within']
    df_clean = df.dropna(subset=required_vars)

    if len(df_clean) == 0:
        raise ValueError("No valid observations after removing missing values")

    print(f"\n{'='*80}")
    print("H2 ROBUSTNESS: WITH SECTOR FE + IC_WITHIN (LOGIT)")
    print(f"{'='*80}")
    print(f"Sample size: {len(df_clean)}")
    print(f"Formula: {formula}")
    print(f"Survival rate: {df_clean['survival'].mean():.2%}")

    # Fit logit model
    model = smf.logit(formula, data=df_clean).fit(disp=False)

    print(f"\n{model.summary()}")

    # Extract key coefficients
    beta1 = model.params.get('z_vagueness', np.nan)
    beta3 = model.params.get('z_vagueness:ic_within', np.nan)
    pval1 = model.pvalues.get('z_vagueness', np.nan)
    pval3 = model.pvalues.get('z_vagueness:ic_within', np.nan)

    # Total effect at high IC (ic_within = 1 std above mean)
    total_effect_high_ic = beta1 + beta3

    print(f"\n{'='*80}")
    print("H2 ROBUSTNESS TEST RESULTS")
    print(f"{'='*80}")
    print(f"β₁ (Vagueness main effect): {beta1:.6f} (p={pval1:.4f})")
    print(f"β₃ (Interaction with ic_within): {beta3:.6f} (p={pval3:.4f})")
    print(f"\nTotal effect at high IC (+1 SD): {total_effect_high_ic:.6f}")

    # Check hypothesis
    h2_robust = beta1 > 0 and pval1 < 0.05
    print(f"\n{'='*80}")
    if h2_robust:
        print(f"✓ H2 ROBUSTNESS SUPPORTED")
        print(f"  - Vagueness effect persists with sector FE (β₁={beta1:.4f}, p<0.05)")
        if beta3 < 0:
            print(f"  - Effect attenuated at high IC (β₃={beta3:.4f})")
    else:
        print(f"✗ H2 ROBUSTNESS NOT SUPPORTED")
        print(f"  - Vagueness effect not significant with sector FE (β₁={beta1:.4f}, p={pval1:.4f})")

    return model


# =============================================================================
# H2 ROBUSTNESS: SERIES B FUNDING ~ VAGUENESS × INTEGRATION COST
# =============================================================================

def test_h2_robustness(
    df: pd.DataFrame,
    formula: str = ("series_b_funding ~ vagueness * high_integration_cost + "
                   "series_a_funding + is_down_round + founder_credibility + "
                   "employees_log + C(sector_fe) + year_founded")
) -> RegressionResultsWrapper:
    """
    Test H2 Robustness: Vagueness effect on Series B funding conditional on Series A.

    This is a robustness check that:
    1. Uses continuous DV (Series B funding amount) instead of binary survival
    2. Controls for Series A funding to isolate later-stage effects
    3. Includes down_round indicator as requested by user

    Model: Series B Funding ~ Vagueness × Integration Cost + Series A Funding +
                              Down Rounds + Controls
    Expected: Similar pattern to H2 Main (β₁ > 0, β₃ < 0)

    Args:
        df: DataFrame with required variables
        formula: R-style formula for OLS regression

    Returns:
        Statsmodels OLS results object

    Interpretation:
        - Tests whether vagueness effect persists when controlling for early funding
        - Down rounds indicator captures valuation decreases
        - Complements H2 Main's binary survival outcome
    """
    # Drop missing values
    required_vars = ['series_b_funding', 'vagueness', 'high_integration_cost', 'series_a_funding']
    df_clean = df.dropna(subset=required_vars)

    if len(df_clean) == 0:
        raise ValueError("No valid observations after removing missing values")

    print(f"\n{'='*80}")
    print("H2 ROBUSTNESS: SERIES B FUNDING ~ VAGUENESS × INTEGRATION COST + SERIES A")
    print(f"{'='*80}")
    print(f"Sample size: {len(df_clean)}")
    print(f"Formula: {formula}")
    print(f"Mean Series B funding: ${df_clean['series_b_funding'].mean():.2f}M")
    print(f"Mean Series A funding: ${df_clean['series_a_funding'].mean():.2f}M")

    if 'is_down_round' in df_clean.columns:
        down_rate = df_clean['is_down_round'].mean()
        print(f"Down round rate: {down_rate:.1%}")

    # Fit OLS model
    model = smf.ols(formula, data=df_clean).fit()

    print(f"\n{model.summary()}")

    # Extract key coefficients
    beta1 = model.params.get('vagueness', np.nan)
    beta3 = model.params.get('vagueness:high_integration_cost', np.nan)
    pval1 = model.pvalues.get('vagueness', np.nan)
    pval3 = model.pvalues.get('vagueness:high_integration_cost', np.nan)

    # Series A coefficient
    beta_a = model.params.get('series_a_funding', np.nan)
    pval_a = model.pvalues.get('series_a_funding', np.nan)

    print(f"\n{'='*80}")
    print("H2 ROBUSTNESS TEST RESULTS")
    print(f"{'='*80}")
    print(f"β₁ (Vagueness main effect): {beta1:.6f} (p={pval1:.4f})")
    print(f"β₃ (Interaction term): {beta3:.6f} (p={pval3:.4f})")
    print(f"β_A (Series A funding control): {beta_a:.6f} (p={pval_a:.4f})")

    # Total effect in integrated sectors
    total_effect_integrated = beta1 + beta3
    print(f"\nTotal effect in integrated sectors (β₁+β₃): {total_effect_integrated:.6f}")

    # Check hypothesis
    h2_robust = beta1 > 0 and pval1 < 0.05
    print(f"\n{'='*80}")
    if h2_robust:
        print(f"✓ H2 ROBUSTNESS SUPPORTED")
        print(f"  - Vagueness effect persists after controlling for Series A (β₁={beta1:.4f}, p<0.05)")
    else:
        print(f"✗ H2 ROBUSTNESS NOT SUPPORTED")
        print(f"  - Vagueness effect not significant after controlling for Series A (β₁={beta1:.4f}, p={pval1:.4f})")

    return model


# =============================================================================
# COMBINED ANALYSIS
# =============================================================================

def run_full_hypothesis_tests(
    df: pd.DataFrame,
    h1_formula: Optional[str] = None,
    h2_formula: Optional[str] = None,
    h2_robust_formula: Optional[str] = None,
    run_robustness: bool = True
) -> Dict[str, Union[RegressionResultsWrapper, BinaryResultsWrapper]]:
    """
    Run H1, H2 main, and H2 robustness tests.

    Args:
        df: DataFrame with all required variables
        h1_formula: Optional custom formula for H1
        h2_formula: Optional custom formula for H2 main
        h2_robust_formula: Optional custom formula for H2 robustness
        run_robustness: Whether to run H2 robustness test (default: True)

    Returns:
        Dictionary with 'h1', 'h2_main', and 'h2_robustness' model results
    """
    results = {}

    print("\n" + "="*80)
    print("COMPREHENSIVE HYPOTHESIS TESTING PIPELINE")
    print("="*80)
    print(f"\nTotal observations: {len(df)}")
    print(f"\nVariable availability:")
    required_vars = [
        'vagueness', 'early_funding_musd', 'survival', 'high_integration_cost',
        'founder_credibility', 'employees_log', 'sector_fe', 'year_founded',
        'series_a_funding', 'series_b_funding', 'is_down_round'
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

    # Run H2 Main
    try:
        if h2_formula:
            results['h2_main'] = test_h2_main_survival(df, h2_formula)
        else:
            results['h2_main'] = test_h2_main_survival(df)
    except Exception as e:
        print(f"\n❌ H2 Main test failed: {e}")
        results['h2_main'] = None

    # Run H2 Robustness
    if run_robustness:
        try:
            if h2_robust_formula:
                results['h2_robustness'] = test_h2_robustness(df, h2_robust_formula)
            else:
                results['h2_robustness'] = test_h2_robustness(df)
        except Exception as e:
            print(f"\n❌ H2 Robustness test failed: {e}")
            results['h2_robustness'] = None

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
