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

# -----------------------------
# H3: Early funding interaction with founder credibility (OLS)
# -----------------------------
def test_h3_early_funding_interaction(
    df: pd.DataFrame,
    formula: str = ("early_funding_musd ~ z_vagueness * founder_serial + "
                    "z_employees_log + C(founding_cohort) + C(sector_fe)")
) -> RegressionResultsWrapper:
    """
    Test H3: Early funding interaction with founder credibility.

    Model: Early Funding ~ Vagueness × Serial Founder + Controls
    Expected: Interaction shows differential funding effects based on founder credibility

    Full specification:
        early_funding_musd ~ z_vagueness * founder_serial +
                           z_employees_log + C(founding_cohort) + C(sector_fe)

    Args:
        df: DataFrame with required variables (must have founder_credibility)
        formula: R-style formula for regression (default includes full controls)

    Returns:
        Statsmodels OLS results object
    """
    # Create founder_serial if not present
    d = df.copy()
    if 'founder_serial' not in d.columns and 'founder_credibility' in d.columns:
        d['founder_serial'] = (d['founder_credibility'] > 0).astype(int)

    # Create founder_serial_cat for plotting
    if 'founder_serial_cat' not in d.columns and 'founder_serial' in d.columns:
        d['founder_serial_cat'] = d['founder_serial'].map({
            0: 'Not Serial (0)',
            1: 'Serial Founder (1)'
        })

    d = d.dropna(subset=['early_funding_musd', 'z_vagueness', 'founder_serial']).copy()
    model = smf.ols(formula, data=d).fit()
    return model

# -----------------------------
# H4: Growth interaction with founder credibility (Logit)
# -----------------------------
def test_h4_growth_interaction(
    df: pd.DataFrame,
    formula: str = ("growth ~ z_vagueness * founder_serial + "
                    "z_employees_log + C(founding_cohort)")
) -> BinaryResultsWrapper:
    """
    Test H4: Growth interaction with founder credibility.

    Model: growth ~ Vagueness × Serial Founder + Controls
    Expected: Interaction shows differential growth effects based on founder credibility

    Full specification:
        growth ~ z_vagueness * founder_serial +
                 z_employees_log + C(founding_cohort)

    Args:
        df: DataFrame with required variables (must have founder_credibility and growth)
        formula: R-style formula for logit regression

    Returns:
        Statsmodels logit results object

    Note:
        Falls back to fit_regularized(method='l2', alpha=0.01) if convergence fails
    """
    # Create founder_serial if not present
    d = df.copy()
    if 'founder_serial' not in d.columns and 'founder_credibility' in d.columns:
        d['founder_serial'] = (d['founder_credibility'] > 0).astype(int)

    # Create founder_serial_cat for plotting
    if 'founder_serial_cat' not in d.columns and 'founder_serial' in d.columns:
        d['founder_serial_cat'] = d['founder_serial'].map({
            0: 'Not Serial (0)',
            1: 'Serial Founder (1)'
        })

    d = d.dropna(subset=['growth', 'z_vagueness', 'founder_serial']).copy()
    try:
        model = smf.logit(formula, data=d).fit(disp=False)
    except Exception:
        model = smf.logit(formula, data=d).fit_regularized(method='l2', alpha=0.01, disp=False, maxiter=200)
    return model
