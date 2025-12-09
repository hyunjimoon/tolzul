"""
Empirical Analysis Module - τ Trajectory & Cohort Analysis
===========================================================

This module implements advanced empirical strategies beyond basic feature engineering:

1. τ Trajectory Calculation: τ₀, τ₁, Δτ (temporal evolution of strategic ambiguity)
2. Cohort Tensor Construction: (Venture × Cohort × Time) xarray structure
3. Proxy Indices: Productive vs Destructive Ambiguity metrics

This is the "strategic tactics" layer that proves your core thesis.

Author: Strategic Ambiguity Research Team
Date: 2025
"""

import pandas as pd
import numpy as np
import xarray as xr
from typing import List, Tuple, Dict, Optional
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


# =============================================================================
# τ TRAJECTORY CALCULATION
# =============================================================================

def calculate_tau_trajectory(
    df: pd.DataFrame,
    t0_year: int = 2021,
    t1_year: int = 2024,
    vagueness_col: str = 'z_vagueness'
) -> pd.DataFrame:
    """
    Calculate τ trajectory: τ₀, τ₁, Δτ

    τ (tau) represents strategic ambiguity level at different time points.

    Args:
        df: DataFrame with company data
        t0_year: Initial measurement year (default: 2021)
        t1_year: Final measurement year (default: 2024)
        vagueness_col: Column name for vagueness measure

    Returns:
        DataFrame with added columns: tau_0, tau_1, delta_tau

    Example:
        >>> df_with_tau = calculate_tau_trajectory(df, 2021, 2024)
        >>> df_with_tau[['company_id', 'tau_0', 'tau_1', 'delta_tau']].head()
    """
    logger.info(f"Calculating τ trajectory: t₀={t0_year}, t₁={t1_year}")

    df = df.copy()

    # τ₀: Initial vagueness (at Series A or t0)
    df['tau_0'] = df[vagueness_col]

    # τ₁: Vagueness at t1 (would need temporal vagueness data)
    # For now, use proxy: if reached Series B, assume τ decreased
    # TODO: Replace with actual temporal vagueness measurement
    if 'L' in df.columns:  # L = reached Series B
        df['tau_1'] = df['tau_0'] * (1 - 0.3 * df['L'])  # 30% reduction if successful
    else:
        logger.warning("No 'L' column found. Setting tau_1 = tau_0")
        df['tau_1'] = df['tau_0']

    # Δτ: Change in vagueness
    df['delta_tau'] = df['tau_1'] - df['tau_0']

    logger.info(f"✓ τ trajectory calculated:")
    logger.info(f"   Mean τ₀: {df['tau_0'].mean():.3f}")
    logger.info(f"   Mean τ₁: {df['tau_1'].mean():.3f}")
    logger.info(f"   Mean Δτ: {df['delta_tau'].mean():.3f}")

    return df


# =============================================================================
# COHORT TENSOR CONSTRUCTION (xarray)
# =============================================================================

def prepare_cohort_tensor(
    df: pd.DataFrame,
    cohort_years: List[int],
    horizon_years: List[int],
    value_vars: List[str] = ['z_vagueness', 'is_software', 'L']
) -> xr.Dataset:
    """
    Create (Venture × Cohort × Time) xarray tensor for panel analysis.

    This is the state-based cohort structure matching your E definition.

    Args:
        df: DataFrame with company data
        cohort_years: Snapshot years (e.g., [2021, 2022, 2023])
        horizon_years: Years forward to track (e.g., [1, 2, 3])
        value_vars: Variables to include in tensor

    Returns:
        xarray.Dataset with dimensions (company_id, window)

    Example:
        >>> ds = prepare_cohort_tensor(df, [2021, 2022, 2023], [1, 2, 3])
        >>> # Select 2022 cohort
        >>> cohort_2022 = ds.where(ds.snapshot_year == 2022, drop=True)
    """
    logger.info("Preparing cohort tensor for xarray...")

    n_companies = len(df)

    # Create window coordinates
    window_cohort_years = []
    window_end_years = []
    window_horizons = []

    for cohort_year in cohort_years:
        for horizon in horizon_years:
            end_year = cohort_year + horizon
            window_cohort_years.append(cohort_year)
            window_end_years.append(end_year)
            window_horizons.append(horizon)

    n_windows = len(window_cohort_years)
    window_ids = np.arange(n_windows)

    # Get company IDs
    if 'CompanyID' in df.columns:
        company_ids = df['CompanyID'].values
    elif 'company_id' in df.columns:
        company_ids = df['company_id'].values
    else:
        company_ids = np.arange(n_companies)

    # Initialize dataset
    ds = xr.Dataset(
        coords={
            'company_id': company_ids,
            'window': window_ids,
            'snapshot_year': ('window', window_cohort_years),
            'end_year': ('window', window_end_years),
            'horizon_years': ('window', window_horizons),
        }
    )

    # Add static variables (measured at Series A)
    for var in value_vars:
        if var in df.columns:
            ds[var] = ('company_id', df[var].values)

    # Add at_risk placeholder (would need state-based logic with Deal data)
    # For now, use event-based approximation
    if 'series_A_year' in df.columns or 'YearFounded' in df.columns:
        series_a_col = 'series_A_year' if 'series_A_year' in df.columns else 'YearFounded'
        series_a_years = pd.to_numeric(df[series_a_col], errors='coerce').fillna(2020).values

        ds['series_A_year'] = ('company_id', series_a_years)

        # Compute at_risk
        at_risk = np.zeros((n_companies, n_windows), dtype=np.int8)
        for w, cohort_year in enumerate(window_cohort_years):
            at_risk[:, w] = (series_a_years == cohort_year).astype(np.int8)

        ds['at_risk'] = (('company_id', 'window'), at_risk)

    # Add metadata
    ds.attrs['cohort_years'] = cohort_years
    ds.attrs['horizon_years'] = horizon_years
    ds.attrs['description'] = 'Cohort tensor for panel analysis'

    logger.info(f"✓ Tensor created:")
    logger.info(f"   Dimensions: {n_companies} companies × {n_windows} windows")
    logger.info(f"   Variables: {list(ds.data_vars.keys())}")

    return ds


# =============================================================================
# PROXY INDICES
# =============================================================================

def compute_productive_ambiguity_index(
    df: pd.DataFrame,
    vagueness_col: str = 'z_vagueness',
    flexibility_col: str = 'is_software',
    outcome_col: str = 'L'
) -> pd.Series:
    """
    Compute Productive Ambiguity Index.

    Productive ambiguity = High vagueness + High flexibility + Positive outcome

    Args:
        df: DataFrame with data
        vagueness_col: Vagueness measure
        flexibility_col: Flexibility indicator (1=flexible/software)
        outcome_col: Success outcome (1=reached Series B+)

    Returns:
        Series with index values [0, 1]
    """
    vagueness_high = (df[vagueness_col] > df[vagueness_col].median()).astype(int)
    flexibility_high = df[flexibility_col]
    outcome_positive = df[outcome_col] if outcome_col in df.columns else 0

    # Index = (high V) × (high F) × (success)
    index = vagueness_high * flexibility_high * outcome_positive

    logger.info(f"Productive Ambiguity Index: {index.sum()}/{len(index)} companies ({index.mean()*100:.1f}%)")

    return index


def compute_destructive_ambiguity_index(
    df: pd.DataFrame,
    vagueness_col: str = 'z_vagueness',
    flexibility_col: str = 'is_software',
    outcome_col: str = 'L'
) -> pd.Series:
    """
    Compute Destructive Ambiguity Index.

    Destructive ambiguity = High vagueness + Low flexibility + Negative outcome

    Args:
        df: DataFrame with data
        vagueness_col: Vagueness measure
        flexibility_col: Flexibility indicator (1=flexible/software)
        outcome_col: Success outcome (1=reached Series B+)

    Returns:
        Series with index values [0, 1]
    """
    vagueness_high = (df[vagueness_col] > df[vagueness_col].median()).astype(int)
    flexibility_low = 1 - df[flexibility_col]
    outcome_negative = 1 - (df[outcome_col] if outcome_col in df.columns else 0)

    # Index = (high V) × (low F) × (failure)
    index = vagueness_high * flexibility_low * outcome_negative

    logger.info(f"Destructive Ambiguity Index: {index.sum()}/{len(index)} companies ({index.mean()*100:.1f}%)")

    return index


# =============================================================================
# TRAJECTORY MODEL PREPARATION
# =============================================================================

def prepare_trajectory_model_data(
    ds: xr.Dataset,
    window_idx: int,
    outcome_var: str = 'L'
) -> pd.DataFrame:
    """
    Extract data for trajectory modeling at specific window.

    Args:
        ds: xarray.Dataset from prepare_cohort_tensor()
        window_idx: Window index to analyze
        outcome_var: Outcome variable name

    Returns:
        DataFrame ready for regression modeling
    """
    # Select window
    window_data = ds.isel(window=window_idx)

    # Get only companies at risk in this window
    at_risk_mask = window_data['at_risk'] == 1
    analysis_data = window_data.where(at_risk_mask, drop=True)

    # Convert to DataFrame
    df = pd.DataFrame({
        'company_id': analysis_data.company_id.values,
        'cohort_year': [analysis_data.snapshot_year.values] * len(analysis_data.company_id),
        'end_year': [analysis_data.end_year.values] * len(analysis_data.company_id),
    })

    # Add variables
    for var in analysis_data.data_vars:
        if var != 'at_risk':
            df[var] = analysis_data[var].values

    logger.info(f"Prepared trajectory data for window {window_idx}:")
    logger.info(f"   Cohort year: {analysis_data.snapshot_year.values}")
    logger.info(f"   End year: {analysis_data.end_year.values}")
    logger.info(f"   Companies: {len(df)}")

    return df


# =============================================================================
# COHORT COMPARISON UTILITIES
# =============================================================================

def compare_cohorts(
    ds: xr.Dataset,
    metric: str = 'L',
    cohort_years: Optional[List[int]] = None
) -> pd.DataFrame:
    """
    Compare metric across cohorts.

    Args:
        ds: xarray.Dataset
        metric: Variable to compare
        cohort_years: Years to compare (default: all)

    Returns:
        DataFrame with cohort comparison
    """
    if cohort_years is None:
        cohort_years = list(set(ds.snapshot_year.values))

    results = []
    for cohort_year in cohort_years:
        cohort_data = ds.where(ds.snapshot_year == cohort_year, drop=True)
        at_risk = cohort_data.where(cohort_data.at_risk == 1, drop=True)

        if metric in at_risk.data_vars:
            mean_value = float(at_risk[metric].mean().values)
            n_companies = int(at_risk.at_risk.sum().values)

            results.append({
                'cohort_year': cohort_year,
                f'mean_{metric}': mean_value,
                'n_companies': n_companies
            })

    df_comparison = pd.DataFrame(results)

    logger.info(f"\nCohort comparison for {metric}:")
    logger.info(df_comparison.to_string(index=False))

    return df_comparison


# =============================================================================
# EXPORT UTILITIES
# =============================================================================

def export_cohort_tensor(
    ds: xr.Dataset,
    output_path: Path,
    format: str = 'netcdf'
) -> Path:
    """
    Export cohort tensor to file.

    Args:
        ds: xarray.Dataset
        output_path: Output file path
        format: 'netcdf' or 'zarr'

    Returns:
        Path to saved file
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(exist_ok=True, parents=True)

    if format == 'netcdf':
        ds.to_netcdf(output_path)
    elif format == 'zarr':
        ds.to_zarr(output_path, mode='w')
    else:
        raise ValueError(f"Unknown format: {format}")

    file_size = output_path.stat().st_size / 1e6 if output_path.exists() else 0
    logger.info(f"✓ Tensor exported to {output_path} ({file_size:.1f} MB)")

    return output_path
