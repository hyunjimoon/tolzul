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
def run_h1_early_funding(
    df: pd.DataFrame,
    formula: str = ("early_funding_musd ~ z_vagueness + z_employees_log + founder_serial + "
                    "is_hardware + z_firm_age + C(sector_fe) + C(founding_cohort)")
) -> RegressionResultsWrapper:
    """
    Test H1: Early funding amount is negatively affected by vagueness.

    Model: Early Funding ~ Vagueness + Controls
    Expected: α₁ < 0 (vagueness reduces early funding)

    Full specification:
        early_funding_musd ~ z_vagueness + z_employees_log + founder_serial +
                           is_hardware + z_firm_age + C(sector_fe) + C(founding_cohort)

    Controls:
        - z_employees_log: Firm size (log-transformed and z-scored)
        - founder_serial: Serial entrepreneur indicator (1=serial, 0=first-time)
        - is_hardware: Hardware/integrated architecture (1=HW, 0=SW)
        - z_firm_age: Company age in years (z-scored)
        - sector_fe: Industry fixed effects
        - founding_cohort: Cohort fixed effects

    Rationale for controls:
        - is_hardware: HW companies are capital-intensive → expect higher early funding
        - z_firm_age: Older companies may have different funding patterns
        - Together these controls should improve R² by capturing variance beyond vagueness

    Args:
        df: DataFrame with required variables
        formula: R-style formula for regression (default includes full controls)

    Returns:
        Statsmodels OLS results object
    """
    d = df.dropna(subset=['early_funding_musd', 'z_vagueness']).copy()

    # Check for constant variables and adjust formula
    adjusted_formula = formula

    # Check if founder_serial has variance (not constant)
    if 'founder_serial' in d.columns:
        founder_serial_std = d['founder_serial'].std()
        if pd.isna(founder_serial_std) or founder_serial_std == 0:
            # Remove founder_serial from formula if it's constant
            adjusted_formula = adjusted_formula.replace('+ founder_serial ', '')
            adjusted_formula = adjusted_formula.replace(' + founder_serial', '')
            print(f"  ⚠️  founder_serial is constant (std=0), removed from H1 formula")

    model = smf.ols(adjusted_formula, data=d).fit()
    return model

# -----------------------------
# H2: Main (Logit, NO early_funding)
# -----------------------------
def run_h2_main_growth(
    df: pd.DataFrame,
    formula: str = ("growth ~ z_vagueness * is_hardware + founder_serial + "
                    "z_employees_log + C(founding_cohort)")
) -> BinaryResultsWrapper:
    """
    Test H2 Main: Vagueness effect on growth is moderated by integration cost.

    ⚠️  CRITICAL: NO early_funding control (it's a MEDIATOR, not confounder)

    Model: growth ~ Vagueness × Hardware + Controls
    Expected: β₁ > 0 (positive in software sectors)
              β₃ < 0 (negative interaction, attenuated in hardware sectors)

    Full specification:
        growth ~ z_vagueness * is_hardware + founder_serial +
                 z_employees_log + C(founding_cohort)

    Controls:
        - founder_serial: Serial entrepreneur indicator (1=serial, 0=first-time)
        - z_employees_log: Firm size
        - founding_cohort: Cohort fixed effects

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

    # Check for constant variables and adjust formula
    adjusted_formula = formula

    # Check if founder_serial has variance (not constant)
    if 'founder_serial' in d.columns:
        founder_serial_std = d['founder_serial'].std()
        if pd.isna(founder_serial_std) or founder_serial_std == 0:
            # Remove founder_serial from formula if it's constant
            adjusted_formula = adjusted_formula.replace('+ founder_serial ', '')
            adjusted_formula = adjusted_formula.replace(' + founder_serial', '')
            print(f"     ⚠️  founder_serial is constant (std=0), removed from formula")

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
    print(f"     Formula: {adjusted_formula}")

    # Try normal fit
    try:
        print(f"     Stage 1: Attempting standard logit fit...")
        model = smf.logit(adjusted_formula, data=d).fit(disp=False)
        print(f"     ✓ Standard fit successful")
        return model
    except Exception:
        print(f"     ✗ Standard fit failed, trying L1 regularization...")

    # Try L1 regularization
    try:
        print(f"     Stage 2: Attempting L1 regularization (alpha=0.1)...")
        model = smf.logit(adjusted_formula, data=d).fit_regularized(
            method='l1', alpha=0.1, disp=False, maxiter=200, warn_convergence=False
        )
        print(f"     ✓ L1 (alpha=0.1) successful")
        return model
    except Exception:
        print(f"     ✗ L1 (alpha=0.1) failed, trying stronger regularization...")

    # Try stronger regularization
    try:
        print(f"     Stage 3: Attempting L1 regularization (alpha=0.5)...")
        model = smf.logit(adjusted_formula, data=d).fit_regularized(
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
def run_h3_early_funding_interaction(
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
def run_h4_growth_interaction(
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


# ========================================
# TWO-SNAPSHOT MODE (E/L/S/V/F)
# ========================================
"""
Simplified hypothesis tests for two-snapshot validation mode.

Variables:
  - E: Early event (1 if Series A at baseline)
  - L: Later success (1 if Series B+ at endpoint)
  - S: Step-up = PreMoney_t2 / PostMoney_t1 (Nanda 2024)
  - V: Vagueness (z-scored)
  - F: Flexibility = 1 - is_hardware
"""

def run_HEV(
    df: pd.DataFrame,
    formula: str = "E ~ z_V + C(founding_cohort) + C(region)"
) -> RegressionResultsWrapper:
    """
    H1 (Two-snapshot): Early event ~ Vagueness

    Model: E ~ V + Controls (OLS)
    Expected: α₁ < 0 (vagueness reduces early funding likelihood)

    Args:
        df: DataFrame with E, z_V, founding_cohort, region
        formula: R-style formula (default includes cohort and region controls)

    Returns:
        Statsmodels OLS results object
    """
    d = df.dropna(subset=['E', 'z_V']).copy()

    print(f"\n  📊 H1 (E~V) Diagnostics:")
    print(f"     Sample size: {len(d):,}")
    print(f"     E rate: {d['E'].mean():.1%}")
    print(f"     V mean: {d['z_V'].mean():.3f}, std: {d['z_V'].std():.3f}")

    model = smf.ols(formula, data=d).fit()
    return model


def run_HLVF(
    df: pd.DataFrame,
    formula: str = "L ~ z_V * F_flexibility + C(founding_cohort) + C(region)"
) -> BinaryResultsWrapper:
    """
    H2 (Two-snapshot): Later success ~ Vagueness × Flexibility

    Model: L ~ V × F + Controls (Logit)
    Expected: β₁ > 0 (positive main effect of vagueness)
              β₃ > 0 (POSITIVE interaction: flexibility AMPLIFIES vagueness benefit)

    Args:
        df: DataFrame with L, z_V, F_flexibility, founding_cohort, region
        formula: R-style formula (default includes cohort and region controls)

    Returns:
        Statsmodels logit results object
    """
    d = df.dropna(subset=['L', 'z_V', 'F_flexibility']).copy()

    print(f"\n  📊 H2 (L~V×F) Diagnostics:")
    print(f"     Sample size: {len(d):,}")
    print(f"     L rate: {d['L'].mean():.1%}")
    print(f"     F mean: {d['F_flexibility'].mean():.3f}, std: {d['F_flexibility'].std():.3f}")

    flexibility_dist = d['F_flexibility'].value_counts()
    print(f"     Flexibility distribution:")
    for val, count in flexibility_dist.items():
        pct = count / len(d) * 100
        label = 'Software (Flexible)' if val == 1 else 'Hardware (Rigid)'
        print(f"       {label}: {count:,} ({pct:.1f}%)")

    if len(flexibility_dist) > 1:
        L_by_F = d.groupby('F_flexibility')['L'].agg(['mean', 'count'])
        print(f"     L rate by flexibility:")
        for idx, row in L_by_F.iterrows():
            label = 'Software' if idx == 1 else 'Hardware'
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
            "H2 (L~V×F) model convergence failed. See diagnostics above. "
            "Data may have perfect separation or severe multicollinearity."
        )


def run_HSF(
    df: pd.DataFrame,
    formula: str = "S_stepup_log ~ z_V * F_flexibility + C(founding_cohort) + C(region)"
) -> RegressionResultsWrapper:
    """
    H3 (Two-snapshot): Step-up ~ Vagueness × Flexibility

    Model: log(S) ~ V × F + Controls (OLS, L==1 only)
    Expected: β₁ > 0 (positive main effect of vagueness)
              β₃ > 0 (POSITIVE interaction: flexibility AMPLIFIES vagueness benefit)

    IMPORTANT: Only analyzes companies with L==1 (achieved Series B+)

    Args:
        df: DataFrame with S_stepup_log, z_V, F_flexibility, L, founding_cohort, region
        formula: R-style formula (default includes cohort and region controls)

    Returns:
        Statsmodels OLS results object

    Note:
        S (Step-up) = PreMoney_t2 / PostMoney_t1 (Nanda 2024)
        Higher S indicates larger valuation jump between rounds
    """
    # Filter to L==1 companies only
    d = df[df['L'] == 1].copy()
    d = d.dropna(subset=['S_stepup_log', 'z_V', 'F_flexibility']).copy()

    print(f"\n  📊 H3 (S~V×F, L==1 only) Diagnostics:")
    print(f"     Sample size: {len(d):,} (filtered from {len(df):,} total)")

    # Early exit if no data
    if len(d) == 0:
        print(f"\n  ❌ ERROR: No valid data for H3 analysis")
        print(f"     Possible causes:")
        print(f"       - No companies with L==1 (achieved later success)")
        print(f"       - No valid S_stepup_log values (missing valuation data)")
        print(f"       - All survivors missing z_V or F_flexibility")
        print(f"\n     Debug info:")
        print(f"       Total companies: {len(df):,}")
        print(f"       L==1 survivors: {(df['L']==1).sum():,}")
        print(f"       Valid S_stepup_log: {df['S_stepup_log'].notna().sum():,}")
        print(f"       Valid z_V: {df['z_V'].notna().sum():,}")
        print(f"       Valid F_flexibility: {df['F_flexibility'].notna().sum():,}")
        raise ValueError(
            "H3 (run_HSF) requires survivors with valid step-up data. "
            "Found 0 valid observations after filtering to L==1 and dropping NAs. "
            "Check your valuation data pipeline."
        )

    print(f"     S_log mean: {d['S_stepup_log'].mean():.3f}, std: {d['S_stepup_log'].std():.3f}")
    print(f"     V mean: {d['z_V'].mean():.3f}, std: {d['z_V'].std():.3f}")

    flexibility_dist = d['F_flexibility'].value_counts()
    print(f"     Flexibility distribution:")
    for val, count in flexibility_dist.items():
        pct = count / len(d) * 100
        label = 'Software (Flexible)' if val == 1 else 'Hardware (Rigid)'
        print(f"       {label}: {count:,} ({pct:.1f}%)")

    if len(flexibility_dist) > 1:
        S_by_F = d.groupby('F_flexibility')['S_stepup_log'].agg(['mean', 'std', 'count'])
        print(f"     S_log by flexibility:")
        for idx, row in S_by_F.iterrows():
            label = 'Software' if idx == 1 else 'Hardware'
            print(f"       {label}: {row['mean']:.3f} (±{row['std']:.3f}, n={int(row['count']):,})")

    print(f"\n  🔧 Fitting H3 model...")

    # Check if we have enough categories for controls
    cohort_levels = d['founding_cohort'].nunique() if 'founding_cohort' in d.columns else 0
    region_levels = d['region'].nunique() if 'region' in d.columns else 0

    # Build formula based on available categorical levels
    if cohort_levels < 2 and region_levels < 2:
        # No categorical controls available
        simple_formula = "S_stepup_log ~ z_V * F_flexibility"
        print(f"     ⚠️  Warning: Insufficient categorical levels. Using simplified model without controls.")
        print(f"        founding_cohort levels: {cohort_levels}, region levels: {region_levels}")
        model = smf.ols(simple_formula, data=d).fit()
    elif cohort_levels < 2:
        # Only region control available
        partial_formula = "S_stepup_log ~ z_V * F_flexibility + C(region)"
        print(f"     ⚠️  Warning: Insufficient founding_cohort levels ({cohort_levels}). Using region control only.")
        model = smf.ols(partial_formula, data=d).fit()
    elif region_levels < 2:
        # Only cohort control available
        partial_formula = "S_stepup_log ~ z_V * F_flexibility + C(founding_cohort)"
        print(f"     ⚠️  Warning: Insufficient region levels ({region_levels}). Using cohort control only.")
        model = smf.ols(partial_formula, data=d).fit()
    else:
        # Full model with both controls
        model = smf.ols(formula, data=d).fit()

    print(f"     ✓ OLS fit successful")

    return model
