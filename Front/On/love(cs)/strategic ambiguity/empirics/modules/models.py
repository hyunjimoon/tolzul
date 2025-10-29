# models.py
"""
Hypothesis Models for W1
- H1 (OLS): early_funding_musd ~ z_vagueness + controls
- H2 Main (Logit): growth ~ z_vagueness * is_hardware + controls  (NO early_funding)
- Robustness with sector FE: growth ~ z_vagueness * ic_within + controls + C(sector_fe)
"""

from __future__ import annotations
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from statsmodels.regression.linear_model import RegressionResultsWrapper
from statsmodels.discrete.discrete_model import BinaryResultsWrapper
from typing import Optional

# -------- helpers --------
def _add_optional_terms(formula: str, df: pd.DataFrame, terms: list[str]) -> str:
    dynamic = []
    for t in terms:
        if t in df.columns:
            s = pd.to_numeric(df[t], errors='coerce')
            if s.notna().sum() > 1 and s.std(ddof=0) > 0:
                dynamic.append(t)
    if dynamic:
        return formula + " + " + " + ".join(dynamic)
    return formula

# -------- H1 --------
def test_h1_early_funding(
    df: pd.DataFrame,
    formula: Optional[str] = None
) -> RegressionResultsWrapper:
    d = df.dropna(subset=['early_funding_musd','z_vagueness']).copy()
    if formula is None:
        base = "early_funding_musd ~ z_vagueness + z_employees_log + C(founding_cohort) + C(sector_fe)"
        base = _add_optional_terms(base, d, ['z_founder_credibility'])
        formula = base
    model = smf.ols(formula, data=d).fit()
    return model

# -------- H2 Main (NO early_funding) --------
def test_h2_main_growth(
    df: pd.DataFrame,
    formula: Optional[str] = None
) -> BinaryResultsWrapper:
    # ensure DV present
    dv = 'growth' if 'growth' in df.columns else 'survival'
    req = ['z_vagueness','is_hardware', dv]
    d = df.dropna(subset=[c for c in req if c in df.columns]).copy()

    if formula is None:
        base = f"{dv} ~ z_vagueness * is_hardware + z_employees_log + C(founding_cohort)"
        base = _add_optional_terms(base, d, ['z_founder_credibility'])
        formula = base
    try:
        model = smf.logit(formula, data=d).fit(disp=False)
    except Exception:
        model = smf.logit(formula, data=d).fit_regularized(method='l2', alpha=0.01, disp=False, maxiter=200)
    return model

# Back-compat wrapper name (기존 run_analysis가 사용)
def test_h2_main_survival(df: pd.DataFrame, formula: Optional[str]=None) -> BinaryResultsWrapper:
    if 'growth' not in df.columns and 'survival' in df.columns:
        df = df.copy(); df['growth'] = df['survival']
    return test_h2_main_growth(df, formula)

# -------- H2 Robustness with sector FE --------
def test_h2_robustness_sector_fe(
    df: pd.DataFrame,
    formula: Optional[str] = None
) -> BinaryResultsWrapper:
    d = df.dropna(subset=['growth','z_vagueness','ic_within']).copy() if 'growth' in df.columns else df.dropna(subset=['survival','z_vagueness','ic_within']).copy()
    dv = 'growth' if 'growth' in d.columns else 'survival'
    if formula is None:
        base = f"{dv} ~ z_vagueness * ic_within + z_employees_log + C(founding_cohort) + C(sector_fe)"
        base = _add_optional_terms(base, d, ['z_founder_credibility'])
        formula = base
    try:
        model = smf.logit(formula, data=d).fit(disp=False)
    except Exception:
        model = smf.logit(formula, data=d).fit_regularized(method='l2', alpha=0.01, disp=False, maxiter=200)
    return model
