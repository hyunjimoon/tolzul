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

    # Print diagnostics
    print(f"\n  📊 H2 (Architecture) Diagnostics:")
    print(f"     Sample size: {len(d):,}")
    print(f"     Growth rate: {d['growth'].mean():.1%}")

    hw_dist = d['is_hardware'].value_counts()
    print(f"     Architecture distribution:")
    for val, count in hw_dist.items():
        pct = count / len(d) * 100
        label = 'Hardware' if val == 1 else 'Software'
        print(f"       {label} ({val}): {count:,} ({pct:.1f}%)")

    if len(hw_dist) > 1:
        growth_by_hw = d.groupby('is_hardware')['growth'].agg(['mean', 'count'])
        print(f"     Growth by architecture:")
        for idx, row in growth_by_hw.iterrows():
            label = 'Hardware' if idx == 1 else 'Software'
            print(f"       {label}: {row['mean']:.1%} (n={int(row['count']):,})")

    print(f"\n  🔧 Fitting H2 model...")

    # Try normal fit
    try:
        print(f"     Stage 1: Attempting standard logit fit...")
        model = smf.logit(formula, data=d).fit(disp=False)
        print(f"     ✓ Standard fit successful")
        return model
    except Exception:
        print(f"     ✗ Standard fit failed, trying L1 regularization...")

    # Try L1 regularization
    try:
        print(f"     Stage 2: Attempting L1 regularization (alpha=0.1)...")
        model = smf.logit(formula, data=d).fit_regularized(
            method='l1', alpha=0.1, disp=False, maxiter=200, warn_convergence=False
        )
        print(f"     ✓ L1 (alpha=0.1) successful")
        return model
    except Exception:
        print(f"     ✗ L1 (alpha=0.1) failed, trying stronger regularization...")

    # Try stronger regularization
    try:
        print(f"     Stage 3: Attempting L1 regularization (alpha=0.5)...")
        model = smf.logit(formula, data=d).fit_regularized(
            method='l1', alpha=0.5, disp=False, maxiter=200, warn_convergence=False
        )
        print(f"     ✓ L1 (alpha=0.5) successful")
        return model
    except Exception:
        raise RuntimeError(
            "H2 model convergence failed. See diagnostics above. "
            "Data may have perfect separation or severe multicollinearity."
        )

# -----------------------------
# H3: Early funding interaction with founder credibility (OLS)
# -----------------------------
def test_h3_early_funding_interaction(
    df: pd.DataFrame,
    formula: str = ("log_early_funding ~ z_vagueness * founder_serial + "
                    "z_employees_log + C(founding_cohort) + C(sector_fe)")
) -> RegressionResultsWrapper:
    """
    Test H3: Early funding interaction with founder credibility.

    Model: Log(Early Funding) ~ Vagueness × Serial Founder + Controls
    Expected: Interaction shows differential funding effects based on founder credibility

    IMPORTANT: Uses log1p transformation to handle extreme positive skew in funding data.
    This is standard practice for heavily skewed financial variables.

    Full specification:
        log_early_funding ~ z_vagueness * founder_serial +
                           z_employees_log + C(founding_cohort) + C(sector_fe)

    Where: log_early_funding = np.log1p(early_funding_musd)

    Args:
        df: DataFrame with required variables (must have founder_credibility)
        formula: R-style formula for regression (default includes full controls)

    Returns:
        Statsmodels OLS results object
    """
    # Create founder_serial if not present
    d = df.copy()

    # Priority: 1) founder_serial, 2) is_serial, 3) founder_credibility
    if 'founder_serial' not in d.columns:
        if 'is_serial' in d.columns:
            # Use existing is_serial (created in run_analysis.py)
            d['founder_serial'] = d['is_serial']
        elif 'founder_credibility' in d.columns:
            # Create from founder_credibility
            d['founder_serial'] = (d['founder_credibility'] > 0).astype(int)
        else:
            raise KeyError(
                "Cannot find 'founder_serial', 'is_serial', or 'founder_credibility'. "
                "At least one is required for H3 analysis. "
                "Note: 'founder_credibility' may be dropped if std=0 in preprocess_for_h2()."
            )

    # Create founder_serial_cat for plotting
    if 'founder_serial_cat' not in d.columns and 'founder_serial' in d.columns:
        d['founder_serial_cat'] = d['founder_serial'].map({
            0: 'Not Serial (0)',
            1: 'Serial Founder (1)'
        })

    # Apply log1p transformation to handle extreme positive skew
    # log1p(x) = log(1 + x) handles zeros gracefully
    d['log_early_funding'] = np.log1p(d['early_funding_musd'])

    # Drop rows with missing values in key variables
    d = d.dropna(subset=['log_early_funding', 'z_vagueness', 'founder_serial']).copy()

    # Print diagnostic to show transformation effect
    print(f"\n  📊 H3 Transformation Diagnostics:")
    print(f"     Original early_funding_musd:")
    print(f"       Mean: ${d['early_funding_musd'].mean():.2f}M, Median: ${d['early_funding_musd'].median():.2f}M")
    print(f"       Max: ${d['early_funding_musd'].max():.2f}M, Skew: {d['early_funding_musd'].skew():.2f}")
    print(f"     Log-transformed log_early_funding:")
    print(f"       Mean: {d['log_early_funding'].mean():.2f}, Median: {d['log_early_funding'].median():.2f}")
    print(f"       Max: {d['log_early_funding'].max():.2f}, Skew: {d['log_early_funding'].skew():.2f}")

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
        Falls back to fit_regularized(method='l1', alpha=0.01) if convergence fails
    """
    # Create founder_serial if not present
    d = df.copy()

    # Priority: 1) founder_serial, 2) is_serial, 3) founder_credibility
    if 'founder_serial' not in d.columns:
        if 'is_serial' in d.columns:
            # Use existing is_serial (created in run_analysis.py)
            d['founder_serial'] = d['is_serial']
        elif 'founder_credibility' in d.columns:
            # Create from founder_credibility
            d['founder_serial'] = (d['founder_credibility'] > 0).astype(int)
        else:
            raise KeyError(
                "Cannot find 'founder_serial', 'is_serial', or 'founder_credibility'. "
                "At least one is required for H4 analysis. "
                "Note: 'founder_credibility' may be dropped if std=0 in preprocess_for_h2()."
            )

    # Create founder_serial_cat for plotting
    if 'founder_serial_cat' not in d.columns and 'founder_serial' in d.columns:
        d['founder_serial_cat'] = d['founder_serial'].map({
            0: 'Not Serial (0)',
            1: 'Serial Founder (1)'
        })

    d = d.dropna(subset=['growth', 'z_vagueness', 'founder_serial']).copy()

    # Print diagnostics to help troubleshoot convergence issues
    print(f"\n  📊 H4 Diagnostics:")
    print(f"     Sample size: {len(d):,}")
    print(f"     Growth rate: {d['growth'].mean():.1%}")

    # Check founder distribution
    founder_dist = d['founder_serial'].value_counts()
    print(f"     Founder distribution:")
    for val, count in founder_dist.items():
        pct = count / len(d) * 100
        label = 'Serial' if val == 1 else 'Not Serial'
        print(f"       {label} ({val}): {count:,} ({pct:.1f}%)")

    # Check growth by founder group
    if len(founder_dist) > 1:
        growth_by_founder = d.groupby('founder_serial')['growth'].agg(['mean', 'count'])
        print(f"     Growth by founder type:")
        for idx, row in growth_by_founder.iterrows():
            label = 'Serial' if idx == 1 else 'Not Serial'
            print(f"       {label}: {row['mean']:.1%} (n={int(row['count']):,})")

    # Multi-stage fallback strategy
    print(f"\n  🔧 Fitting H4 model...")

    # Stage 1: Try normal MLE
    try:
        print(f"     Stage 1: Attempting standard logit fit...")
        model = smf.logit(formula, data=d).fit(disp=False)
        print(f"     ✓ Standard fit successful")
        return model
    except Exception as e1:
        print(f"     ✗ Standard fit failed: {type(e1).__name__}")

    # Stage 2: Try L1 with alpha=0.1 (moderate regularization)
    try:
        print(f"     Stage 2: Attempting L1 regularization (alpha=0.1)...")
        model = smf.logit(formula, data=d).fit_regularized(
            method='l1', alpha=0.1, disp=False, maxiter=200, warn_convergence=False
        )
        print(f"     ✓ L1 (alpha=0.1) successful")
        return model
    except Exception as e2:
        print(f"     ✗ L1 (alpha=0.1) failed: {type(e2).__name__}")

    # Stage 3: Try L1 with alpha=0.5 (strong regularization)
    try:
        print(f"     Stage 3: Attempting L1 regularization (alpha=0.5)...")
        model = smf.logit(formula, data=d).fit_regularized(
            method='l1', alpha=0.5, disp=False, maxiter=200, warn_convergence=False
        )
        print(f"     ✓ L1 (alpha=0.5) successful")
        return model
    except Exception as e3:
        print(f"     ✗ L1 (alpha=0.5) failed: {type(e3).__name__}")

    # Stage 4: Try simplified model without interaction
    try:
        print(f"     Stage 4: Attempting simplified model (no interaction)...")
        simple_formula = "growth ~ z_vagueness + founder_serial + z_employees_log + C(founding_cohort)"
        model = smf.logit(simple_formula, data=d).fit_regularized(
            method='l1', alpha=0.1, disp=False, maxiter=200, warn_convergence=False
        )
        print(f"     ✓ Simplified model successful (no interaction term)")
        print(f"     ⚠️  WARNING: Interaction term dropped due to convergence issues")
        return model
    except Exception as e4:
        print(f"     ✗ Simplified model failed: {type(e4).__name__}")

    # Stage 5: Last resort - main effects only
    try:
        print(f"     Stage 5: Attempting main effects only...")
        minimal_formula = "growth ~ z_vagueness + founder_serial"
        model = smf.logit(minimal_formula, data=d).fit_regularized(
            method='l1', alpha=0.5, disp=False, maxiter=200, warn_convergence=False
        )
        print(f"     ✓ Main effects only model successful")
        print(f"     ⚠️  WARNING: Controls and interaction dropped due to convergence issues")
        return model
    except Exception as e5:
        print(f"     ✗ Main effects only failed: {type(e5).__name__}")

    # All stages failed - raise informative error
    print(f"\n  ❌ ERROR: All H4 fallback strategies failed")
    print(f"     This suggests severe data issues:")
    print(f"     - Possible perfect separation (all Y=0 or Y=1 in one group)")
    print(f"     - Extreme multicollinearity")
    print(f"     - Insufficient sample size in founder groups")
    print(f"")
    print(f"     Recommendations:")
    print(f"     1. Check founder_serial distribution (should have both 0 and 1)")
    print(f"     2. Check growth distribution by founder type")
    print(f"     3. Consider collecting more data")
    print(f"     4. Consider alternative moderators (e.g., is_hardware)")
    print(f"")

    raise RuntimeError(
        "H4 model convergence failed across all fallback strategies. "
        "See diagnostics above for details. Data may have perfect separation or "
        "severe multicollinearity."
    )
