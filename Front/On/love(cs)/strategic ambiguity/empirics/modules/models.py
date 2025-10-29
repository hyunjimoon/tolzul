"""
Hypothesis Testing Module (W1 refactor)

- H1: Early_Funding ~ z_vagueness + controls (OLS)
- H2: growth ~ z_vagueness * is_hardware + controls (Logit, NO early_funding)

Conventions:
  - Moderator: is_hardware (1=Hardware/Integrated, 0=Software/Non-integrated)
  - DV: growth (Series B+ within window)
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from statsmodels.regression.linear_model import RegressionResultsWrapper
from statsmodels.discrete.discrete_model import BinaryResultsWrapper

# -----------------------------
# H1: Early funding (OLS)
# -----------------------------
def test_h1_early_funding(
    df: pd.DataFrame,
    formula: str = ("early_funding_musd ~ z_vagueness + z_employees_log + "
                    "C(sector_fe) + C(founding_cohort)")
) -> RegressionResultsWrapper:
    """
    Test H1: Early funding amount is negatively affected by vagueness.

    Model: Early Funding ~ Vagueness + Controls
    Expected: α₁ < 0 (vagueness reduces early funding)

    Full specification:
        early_funding_musd ~ z_vagueness + z_employees_log +
                           C(sector_fe) + C(founding_cohort)

    Args:
        df: DataFrame with required variables
        formula: R-style formula for regression (default includes full controls)

    Returns:
        Statsmodels OLS results object
    """
    d = df.dropna(subset=['early_funding_musd', 'z_vagueness']).copy()
    model = smf.ols(formula, data=d).fit()
    return model

# -----------------------------
# H2: Main (Logit, NO early_funding)
# -----------------------------
def test_h2_main_growth(
    df: pd.DataFrame,
    formula: str = ("growth ~ z_vagueness * is_hardware + "
                    "z_employees_log + C(founding_cohort)")
) -> BinaryResultsWrapper:
    """
    Test H2 Main: Vagueness effect on growth is moderated by integration cost.

    ⚠️  CRITICAL: NO early_funding control (it's a MEDIATOR, not confounder)

    Model: growth ~ Vagueness × is_hardware + Controls
    Expected: β₁ > 0 (positive in software sectors)
              β₃ < 0 (negative interaction, attenuated in hardware sectors)

    Full specification:
        growth ~ z_vagueness * is_hardware +
                 z_employees_log + C(founding_cohort)

    Args:
        df: DataFrame with required variables
        formula: R-style formula for logit regression

    Returns:
        Statsmodels logit results object

    Interpretation:
        - β₁ (vagueness main effect): effect in software sectors (is_hardware=0)
        - β₃ (interaction): differential effect in hardware sectors
        - Total effect in hardware = β₁ + β₃
        - NO early_funding: it's a mediator in causal chain vagueness→funding→growth
    """
    d = df.dropna(subset=['growth', 'z_vagueness', 'is_hardware']).copy()
    try:
        model = smf.logit(formula, data=d).fit(disp=False)
    except Exception:
        model = smf.logit(formula, data=d).fit_regularized(method='l2', alpha=0.01, disp=False, maxiter=200)
    return model
