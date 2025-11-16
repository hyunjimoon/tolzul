"""
Multiverse Analysis Engine for Vagueness → Funding/Success Hypotheses

Tests hypotheses across specification space using xarray-based multiverse approach.
Implements OLS for early stage and Logit for later stages with robust fallback strategies.
"""

import numpy as np
import pandas as pd
import xarray as xr
import statsmodels.formula.api as smf
import patsy
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Tuple, Any, Optional
import warnings

# ============================================================================
# CONSTANTS
# ============================================================================

STAGE_MAP = {
    "E":  {"model": "ols",   "dv": "z_early_funding_musd"},
    "L1": {"model": "logit", "dv": "growth"},
    "L2": {"model": "logit", "dv": "growth"}
}

EXPECTED_SIGNS = {
    "vag_main": {"E": -1, "L1": +1, "L2": +1},
    "vagXoption": +1,
    "vagXsoftware": +1
}

CONT_VARS = ["vagueness", "employees_log", "early_funding_musd"]
ALPHA = 0.05

STAGE_PATTERNS = {
    'series_a': r'(?i)series\s*a',
    'series_b_plus': r'(?i)series\s*[b-z]'
}

# ============================================================================
# DATA PIPELINE
# ============================================================================

def filter_window(df: pd.DataFrame, window: Tuple[str, str]) -> pd.DataFrame:
    """
    Filter dataframe by founding year within time window.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe with 'year' column
    window : tuple of str
        (start_date, end_date) in 'YYYY-MM' format

    Returns
    -------
    pd.DataFrame
        Filtered dataframe
    """
    start, end = map(pd.to_datetime, window)
    df = df.copy()

    # Handle both 'year' and 'year_founded' column names
    year_col = 'year' if 'year' in df.columns else 'year_founded'
    if year_col not in df.columns:
        raise ValueError(f"Dataset must contain either 'year' or 'year_founded' column")

    # Drop rows with missing year values
    df = df[df[year_col].notna()].copy()

    # Convert year to datetime (end of year for filtering)
    df['year_end'] = pd.to_datetime(df[year_col].astype(int).astype(str) + "-12-31")
    filtered = df[(df['year_end'] >= start) & (df['year_end'] <= end)].copy()
    return filtered


def create_moderators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create moderator variables for consistent directionality.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe

    Returns
    -------
    pd.DataFrame
        Dataframe with isSoftware = 1 - is_hardware
    """
    d = df.copy()
    if 'is_hardware' in d.columns:
        d['isSoftware'] = 1 - d['is_hardware']
    return d


def apply_scaling(df: pd.DataFrame, method: str) -> pd.DataFrame:
    """
    Apply scaling to ALL continuous variables.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    method : str
        'zscore' or 'winsor99_z'

    Returns
    -------
    pd.DataFrame
        Dataframe with z_* columns for all continuous variables
    """
    d = df.copy()

    for col in CONT_VARS:
        if col not in d.columns:
            continue

        s = d[col].astype(float)

        # Check if we have sufficient valid data
        valid_count = s.notna().sum()
        if valid_count < 2:
            # Not enough data to compute z-score, set to NaN
            d[f"z_{col}"] = np.nan
            continue

        # Winsorization if requested
        if method == "winsor99_z":
            # Suppress percentile warnings for small samples
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                lo, hi = np.nanpercentile(s, 1), np.nanpercentile(s, 99)
            s = s.clip(lo, hi)

        # Z-score transformation with warning suppression
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            mu = np.nanmean(s)
            sd = np.nanstd(s)

        # Handle edge cases
        if np.isnan(mu) or np.isnan(sd) or sd == 0:
            d[f"z_{col}"] = np.nan
        else:
            d[f"z_{col}"] = (s - mu) / sd

    # Create shorthand V for vagueness
    if "z_vagueness" in d.columns:
        d["V"] = d["z_vagueness"]
    else:
        d["V"] = np.nan

    return d


# ============================================================================
# MODEL FITTING
# ============================================================================

def build_formula(stage: str, moderator: str,
                 ctrl_employee: int, ctrl_region: int,
                 ctrl_founder: int, ctrl_earlyfund: int,
                 df: pd.DataFrame) -> str:
    """
    Build statsmodels formula string for specification.

    Parameters
    ----------
    stage : str
        'E', 'L1', or 'L2'
    moderator : str
        'option_level' or 'isSoftware'
    ctrl_employee : int
        Include employee control (0 or 1)
    ctrl_region : int
        Include region FE (0 or 1)
    ctrl_founder : int
        Include founder credibility (0 or 1)
    ctrl_earlyfund : int
        Include early funding control in H2 (0 or 1)
    df : pd.DataFrame
        Data to check for column availability

    Returns
    -------
    str
        Formula string for statsmodels
    """
    controls = []

    # Always include founding cohort FE if available
    if "founding_cohort" in df.columns:
        controls.append("C(founding_cohort)")

    # Employee control
    if ctrl_employee == 1 and "z_employees_log" in df.columns:
        controls.append("z_employees_log")

    # Region FE
    if ctrl_region == 1 and "region" in df.columns:
        controls.append("C(region)")

    # Founder credibility
    if ctrl_founder == 1 and "founder_credibility" in df.columns:
        controls.append("founder_credibility")

    if stage == "E":
        # H1: z_early_funding ~ vagueness + controls
        rhs = ["V"] + controls
        return "z_early_funding_musd ~ " + " + ".join(rhs)
    else:
        # H2: growth ~ vagueness * moderator + controls
        M = "option_exercisability_level" if moderator == "option_level" else "isSoftware"
        rhs = [f"V * {M}"]

        # Add early funding control if specified
        if ctrl_earlyfund == 1 and "z_early_funding_musd" in df.columns:
            rhs.append("z_early_funding_musd")

        rhs.extend(controls)
        return "growth ~ " + " + ".join(rhs)


def extract_results(model: Any, df: pd.DataFrame, nobs: int,
                   stage: str, method: str, warning_code: int) -> Dict[str, Any]:
    """
    Extract coefficients and compute metrics from fitted model.

    Parameters
    ----------
    model : statsmodels model
        Fitted regression model
    df : pd.DataFrame
        Data used for fitting
    nobs : int
        Number of observations
    stage : str
        Stage identifier
    method : str
        Estimation method used
    warning_code : int
        0=success, 1=fallback1, 2=fallback2, 3=failed

    Returns
    -------
    dict
        Results dictionary with coefficients and metrics
    """
    params = model.params.to_dict()
    pvalues = model.pvalues.to_dict()

    # Extract main vagueness effect
    coef_vag = params.get('V', np.nan)
    p_vag = pvalues.get('V', np.nan)

    # Extract interactions
    coef_vagXopt = params.get('V:option_exercisability_level', np.nan)
    p_vagXopt = pvalues.get('V:option_exercisability_level', np.nan)

    coef_vagXsw = params.get('V:isSoftware', np.nan)
    p_vagXsw = pvalues.get('V:isSoftware', np.nan)

    # Model fit statistic
    if method == 'ols':
        fit_stat = model.aic
    else:
        fit_stat = getattr(model, 'prsquared', np.nan)

    # DV statistics
    dv_name = STAGE_MAP[stage]['dv']
    dv_rate = df[dv_name].mean() if dv_name in df.columns else np.nan
    downround_share = df.get('down_round_flag', pd.Series([np.nan])).mean()

    return {
        'coef_vag_main': coef_vag,
        'p_vag_main': p_vag,
        'coef_vagXoption': coef_vagXopt,
        'p_vagXoption': p_vagXopt,
        'coef_vagXsoftware': coef_vagXsw,
        'p_vagXsoftware': p_vagXsw,
        'nobs': nobs,
        'fit_stat': fit_stat,
        'dv_rate': dv_rate,
        'downround_share': downround_share,
        'warning_code': warning_code,
        'estimation_method': method
    }


def null_result(nobs: int, warning_code: int, method: str) -> Dict[str, Any]:
    """
    Return null result dictionary for failed fits.

    Parameters
    ----------
    nobs : int
        Number of observations
    warning_code : int
        Warning code (typically 3 for failure)
    method : str
        Estimation method attempted

    Returns
    -------
    dict
        Null results dictionary with NaN values
    """
    return {
        'coef_vag_main': np.nan,
        'p_vag_main': np.nan,
        'coef_vagXoption': np.nan,
        'p_vagXoption': np.nan,
        'coef_vagXsoftware': np.nan,
        'p_vagXsoftware': np.nan,
        'nobs': nobs,
        'fit_stat': np.nan,
        'dv_rate': np.nan,
        'downround_share': np.nan,
        'warning_code': warning_code,
        'estimation_method': method
    }


def fit_specification(df: pd.DataFrame, stage: str, formula: str) -> Dict[str, Any]:
    """
    Fit model with 3-stage fallback strategy for logit.

    For OLS (stage E): Direct fit
    For Logit (stages L1, L2): MLE → L1(α=0.1) → L1(α=0.5)

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    stage : str
        Stage identifier ('E', 'L1', 'L2')
    formula : str
        Model formula

    Returns
    -------
    dict
        Results dictionary with coefficients and diagnostics
    """
    # Get TRUE nobs using patsy design matrix
    try:
        design_matrix = patsy.dmatrix(formula.split('~')[1], df, return_type='dataframe')
        d = df.loc[design_matrix.index].copy()
        nobs = len(d)
    except Exception:
        return null_result(0, 3, 'failed')

    if stage == "E":
        # OLS for early stage
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                model = smf.ols(formula, data=d).fit()
            return extract_results(model, d, nobs, stage, 'ols', 0)
        except Exception:
            return null_result(nobs, 3, 'failed')
    else:
        # Logit with 3-stage fallback
        # Stage 1: MLE
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                model = smf.logit(formula, data=d).fit(disp=False, maxiter=100)
            return extract_results(model, d, nobs, stage, 'logit_mle', 0)
        except Exception:
            pass

        # Stage 2: L1 regularization (α=0.1)
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                model = smf.logit(formula, data=d).fit_regularized(
                    method='l1', alpha=0.1, disp=False, maxiter=200,
                    warn_convergence=False
                )
            return extract_results(model, d, nobs, stage, 'logit_l1_0.1', 1)
        except Exception:
            pass

        # Stage 3: L1 regularization (α=0.5)
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                model = smf.logit(formula, data=d).fit_regularized(
                    method='l1', alpha=0.5, disp=False, maxiter=200,
                    warn_convergence=False
                )
            return extract_results(model, d, nobs, stage, 'logit_l1_0.5', 2)
        except Exception:
            return null_result(nobs, 3, 'failed')


# ============================================================================
# EVIDENCE METRICS
# ============================================================================

def compute_evidence(coef: float, p: float, expected_sign: int) -> Tuple[float, int, int]:
    """
    Compute evidence metrics for hypothesis testing.

    Parameters
    ----------
    coef : float
        Coefficient estimate
    p : float
        P-value
    expected_sign : int
        Expected sign (-1 or +1)

    Returns
    -------
    tuple of (float, int, int)
        (evidence_score, is_consistent, is_surprise)
        - evidence_score: sign(coef) * -log10(p)
        - is_consistent: 1 if sign matches expected and p < 0.05
        - is_surprise: 1 if sign opposes expected and p < 0.05
    """
    if np.isnan(coef) or np.isnan(p):
        return 0.0, 0, 0

    # Evidence score: direction-weighted significance
    score = np.sign(coef) * (-np.log10(max(p, 1e-12)))

    # Consistency check
    consistent = int((np.sign(coef) == expected_sign) and (p < ALPHA))

    # Surprise check (opposite direction + significant)
    surprise = int((np.sign(coef) != expected_sign) and (p < ALPHA))

    return score, consistent, surprise


# ============================================================================
# VISUALIZATION
# ============================================================================

def plot_multiverse_heatmap(ds: xr.Dataset, var_key: str,
                           expected_sign: int, figsize: Tuple[int, int] = (16, 8)) -> plt.Figure:
    """
    Create specification curve heatmap with direction-aware colors.

    Parameters
    ----------
    ds : xr.Dataset
        Multiverse results dataset
    var_key : str
        Variable to visualize (e.g., 'evidence_score_vag_main')
    expected_sign : int
        Expected sign for color mapping (-1 or +1)
    figsize : tuple of int
        Figure size (width, height)

    Returns
    -------
    matplotlib.figure.Figure
        Heatmap figure
    """
    # Convert to dataframe and sort specifications
    df = ds.to_dataframe().reset_index()
    df['sort_key'] = df.apply(lambda r: (
        r['stage'], r['moderator'], r['window'][0], r['window'][1],
        r['scaling'], r['ctrl_employee'], r['ctrl_region'],
        r['ctrl_founder'], r['ctrl_earlyfund']
    ), axis=1)
    df = df.sort_values('sort_key')

    # Create pivot table
    pivot = df.pivot_table(
        values=var_key,
        index='window',
        columns=df.index,
        aggfunc='first'
    )

    # Direction-aware color mapping
    vmax = np.nanmax(np.abs(pivot.values))
    cmap = 'RdYlGn' if expected_sign > 0 else 'RdYlGn_r'

    # Create heatmap
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(pivot, cmap=cmap, center=0, vmax=vmax, vmin=-vmax,
                cbar_kws={'label': var_key}, ax=ax,
                xticklabels=False, yticklabels=True)

    ax.set_title(f'Multiverse Analysis: {var_key}', fontsize=14, fontweight='bold')
    ax.set_xlabel('Specification Index', fontsize=12)
    ax.set_ylabel('Time Window', fontsize=12)

    plt.tight_layout()
    return fig


def plot_specification_curve(ds: xr.Dataset, var_key: str,
                             expected_sign: int, figsize: Tuple[int, int] = (16, 6)) -> plt.Figure:
    """
    Create specification curve plot showing ordered effect sizes.

    Parameters
    ----------
    ds : xr.Dataset
        Multiverse results dataset
    var_key : str
        Variable to visualize
    expected_sign : int
        Expected sign for highlighting
    figsize : tuple of int
        Figure size

    Returns
    -------
    matplotlib.figure.Figure
        Specification curve figure
    """
    df = ds.to_dataframe().reset_index()
    df = df.sort_values(var_key)

    fig, ax = plt.subplots(figsize=figsize)

    # Color by consistency with expected sign
    colors = ['green' if (np.sign(x) == expected_sign and not np.isnan(x))
              else 'red' for x in df[var_key]]

    ax.scatter(range(len(df)), df[var_key], c=colors, alpha=0.6, s=20)
    ax.axhline(y=0, color='black', linestyle='--', linewidth=1)

    ax.set_xlabel('Specification (sorted by effect size)', fontsize=12)
    ax.set_ylabel(var_key, fontsize=12)
    ax.set_title(f'Specification Curve: {var_key}', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig
