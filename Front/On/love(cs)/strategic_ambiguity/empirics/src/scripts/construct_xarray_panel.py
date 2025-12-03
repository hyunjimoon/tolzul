#!/usr/bin/env python3
"""
Construct xarray Panel Dataset
================================

This script constructs the xarray.Dataset based on the analysis from
analyze_for_xarray_design.py.

Uses the recommended structure:
- venture_id × window dimensions
- series_A_year coordinate (no cohort dummies!)
- at_risk variable computed from series_A_year == cohort_year

Usage:
    python construct_xarray_panel.py [--data-file PATH] [--cohort-years YEARS]
"""

import sys
import argparse
from pathlib import Path
import pandas as pd
import numpy as np
import xarray as xr
import logging
from typing import List, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_company_data(data_file: Path = None) -> pd.DataFrame:
    """Load company data from parquet file."""
    if data_file is None:
        processed_dir = Path("data/processed")
        parquet_files = list(processed_dir.glob("consolidated_companies*.parquet"))

        if not parquet_files:
            raise FileNotFoundError(
                "No consolidated parquet file found. Run analyze_for_xarray_design.py first"
            )

        data_file = max(parquet_files, key=lambda p: p.stat().st_mtime)

    logger.info(f"📂 Loading data from: {data_file}")
    df = pd.read_parquet(data_file)
    logger.info(f"✓ Loaded {len(df):,} companies")

    return df


def create_window_coordinate(cohort_years: List[int], horizon_years: List[int]) -> Tuple:
    """Create window coordinate arrays.

    Args:
        cohort_years: List of Series A years to use as cohorts
        horizon_years: List of years after Series A to track

    Returns:
        Tuple of (window_ids, window_cohort_years, window_end_years, window_horizons)
    """
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

    logger.info(f"\n📊 Window coordinate created:")
    logger.info(f"   Cohort years: {cohort_years}")
    logger.info(f"   Horizon years: {horizon_years}")
    logger.info(f"   Total windows: {n_windows}")

    return window_ids, window_cohort_years, window_end_years, window_horizons


def compute_at_risk(series_a_years: np.ndarray, window_cohort_years: List[int]) -> np.ndarray:
    """Compute at_risk variable.

    Args:
        series_a_years: Array of Series A years for each venture (length N)
        window_cohort_years: List of cohort years for each window (length W)

    Returns:
        at_risk array of shape (N, W) where at_risk[i,w]=1 if venture i's
        Series A year matches the cohort_year for window w
    """
    n_ventures = len(series_a_years)
    n_windows = len(window_cohort_years)
    at_risk = np.zeros((n_ventures, n_windows), dtype=np.int8)

    # Set at_risk[i, w] = 1 if series_A_year[i] == cohort_year[w]
    for w, cohort_year in enumerate(window_cohort_years):
        at_risk[:, w] = (series_a_years == cohort_year).astype(np.int8)

    return at_risk


def construct_xarray_dataset(
    df: pd.DataFrame,
    cohort_years: List[int] = [2021, 2022, 2023],
    horizon_years: List[int] = [1, 2, 3]
) -> xr.Dataset:
    """Construct xarray.Dataset from company DataFrame.

    Args:
        df: Company data DataFrame
        cohort_years: Years to use as cohorts (based on Series A year)
        horizon_years: Number of years after Series A to track

    Returns:
        xarray.Dataset with venture_id × window structure
    """
    logger.info("\n" + "=" * 80)
    logger.info("CONSTRUCTING XARRAY DATASET")
    logger.info("=" * 80)

    # Get company IDs
    company_id_col = 'CompanyID' if 'CompanyID' in df.columns else 'company_id'
    venture_ids = df[company_id_col].values

    # Create window coordinate
    window_ids, window_cohort_years, window_end_years, window_horizons = create_window_coordinate(cohort_years, horizon_years)
    n_windows = len(window_ids)

    # Extract Series A years
    series_a_col = None
    for col in ['SeriesAYear', 'series_a_year', 'series_A_year']:
        if col in df.columns:
            series_a_col = col
            break

    if series_a_col is None:
        logger.warning("⚠️  No Series A year column found - using YearFounded as proxy")
        series_a_col = 'YearFounded' if 'YearFounded' in df.columns else 'year_founded'

    series_a_years = pd.to_numeric(df[series_a_col], errors='coerce').fillna(0).astype(int).values

    # Extract sector
    sector_col = None
    for col in ['Sector', 'sector', 'PrimarySector']:
        if col in df.columns:
            sector_col = col
            break

    sectors = df[sector_col].fillna('Unknown').values if sector_col else np.array(['Unknown'] * len(df))

    # Initialize dataset
    logger.info("\n🏗️  Creating dataset structure...")

    ds = xr.Dataset(
        coords={
            'venture_id': venture_ids,
            'window': window_ids,
            'series_A_year': ('venture_id', series_a_years),
            'sector': ('venture_id', sectors),
            'cohort_year': ('window', window_cohort_years),
            'end_year': ('window', window_end_years),
            'horizon_years': ('window', window_horizons),
        }
    )

    logger.info(f"✓ Created coordinates:")
    logger.info(f"   venture_id: {len(venture_ids):,}")
    logger.info(f"   window: {n_windows}")

    # Compute at_risk variable
    logger.info("\n📍 Computing at_risk variable...")
    at_risk = compute_at_risk(series_a_years, window_cohort_years)
    ds['at_risk'] = (('venture_id', 'window'), at_risk)

    # Verify at_risk
    ventures_in_cohort = (at_risk.sum(axis=1) > 0).sum()
    logger.info(f"✓ at_risk computed:")
    logger.info(f"   Ventures assigned to cohorts: {ventures_in_cohort:,}")
    logger.info(f"   Ventures per cohort:")
    for cohort_year in cohort_years:
        # Count ventures where series_A_year == cohort_year
        n_in_cohort = (series_a_years == cohort_year).sum()
        logger.info(f"      {cohort_year}: {n_in_cohort:,}")

    # Add static variables
    logger.info("\n📊 Adding static variables...")

    # Employees
    emp_col = 'Employees' if 'Employees' in df.columns else 'employees'
    if emp_col in df.columns:
        employees = pd.to_numeric(df[emp_col], errors='coerce').fillna(0).values
        z_employees_log = np.log1p(employees)
        z_employees_log = (z_employees_log - z_employees_log.mean()) / z_employees_log.std()
        ds['z_employees_log'] = ('venture_id', z_employees_log.astype(np.float32))
        logger.info("   ✓ z_employees_log")

    # Founding year
    year_col = 'YearFounded' if 'YearFounded' in df.columns else 'year_founded'
    if year_col in df.columns:
        founding_years = pd.to_numeric(df[year_col], errors='coerce').fillna(0).astype(np.int16).values
        ds['founding_year'] = ('venture_id', founding_years)
        logger.info("   ✓ founding_year")

    # HQ Country
    country_col = 'HQCountry' if 'HQCountry' in df.columns else 'hq_country'
    if country_col in df.columns:
        hq_countries = df[country_col].fillna('Unknown').values
        ds['hq_country'] = ('venture_id', hq_countries)
        logger.info("   ✓ hq_country")

    # Placeholder for vagueness (to be computed by vagueness scorer)
    ds['z_vagueness'] = ('venture_id', np.zeros(len(df), dtype=np.float32))
    logger.info("   ✓ z_vagueness (placeholder)")

    # Placeholder for is_software
    ds['is_software'] = ('venture_id', np.zeros(len(df), dtype=np.int8))
    logger.info("   ✓ is_software (placeholder)")

    # Placeholder for outcomes (time-varying)
    ds['L'] = (('venture_id', 'window'), np.zeros((len(df), n_windows), dtype=np.float32))
    logger.info("   ✓ L (placeholder - Series B+ reached)")

    # Add attributes
    ds.attrs['schema_version'] = 'esi-panel.v4'
    ds.attrs['window_logic'] = 'at_risk[i,w]=1 iff series_A_year[i]==cohort_year[w]'
    ds.attrs['cohort_years'] = cohort_years
    ds.attrs['horizon_years'] = horizon_years

    logger.info("\n" + "=" * 80)
    logger.info("✅ XARRAY DATASET CONSTRUCTED")
    logger.info("=" * 80)

    return ds


def validate_dataset(ds: xr.Dataset):
    """Validate the constructed dataset."""
    logger.info("\n" + "=" * 80)
    logger.info("🔍 VALIDATING DATASET")
    logger.info("=" * 80)

    # Check at_risk makes sense
    at_risk_sum = ds.at_risk.sum('window').values
    max_cohorts = int(at_risk_sum.max())
    ventures_in_multiple = (at_risk_sum > 1).sum()

    logger.info(f"\n✓ at_risk validation:")
    logger.info(f"   Max cohorts per venture: {max_cohorts}")
    logger.info(f"   Ventures in multiple cohorts: {ventures_in_multiple}")

    if ventures_in_multiple > 0:
        logger.warning("   ⚠️  Some ventures appear in multiple cohorts (check series_A_year)")

    # Check cohort assignment
    cohort_years = ds.attrs['cohort_years']
    logger.info(f"\n✓ Cohort assignments:")
    for cohort_year in cohort_years:
        # Get ventures in this cohort
        ventures_in_cohort = (ds.series_A_year == cohort_year).sum().values
        logger.info(f"   {cohort_year}: {ventures_in_cohort:,} ventures")

    # Check data variables
    logger.info(f"\n✓ Data variables:")
    for var in ds.data_vars:
        dtype = ds[var].dtype
        shape = ds[var].shape
        n_missing = np.isnan(ds[var].values.astype(float)).sum()
        logger.info(f"   {var}: shape={shape}, dtype={dtype}, missing={n_missing:,}")

    logger.info("\n" + "=" * 80)
    logger.info("✅ VALIDATION COMPLETE")
    logger.info("=" * 80)


def main():
    """Main construction workflow."""
    parser = argparse.ArgumentParser(description='Construct xarray panel dataset')
    parser.add_argument('--data-file', type=Path, help='Path to parquet file')
    parser.add_argument('--cohort-years', type=int, nargs='+', default=[2021, 2022, 2023],
                        help='Cohort years to use (default: 2021 2022 2023)')
    parser.add_argument('--horizon-years', type=int, nargs='+', default=[1, 2, 3],
                        help='Horizon years to track (default: 1 2 3)')
    parser.add_argument('--output', type=Path, default=Path('outputs/xarray_design/panel_dataset.nc'),
                        help='Output path for netCDF file')
    args = parser.parse_args()

    try:
        # Load data
        df = load_company_data(args.data_file)

        # Construct dataset
        ds = construct_xarray_dataset(df, args.cohort_years, args.horizon_years)

        # Validate
        validate_dataset(ds)

        # Save
        output_file = args.output
        output_file.parent.mkdir(exist_ok=True, parents=True)

        logger.info(f"\n💾 Saving dataset to: {output_file}")
        ds.to_netcdf(output_file)

        file_size = output_file.stat().st_size / 1e6
        logger.info(f"✓ Saved ({file_size:.1f} MB)")

        logger.info("\n" + "=" * 80)
        logger.info("✅ COMPLETE")
        logger.info("=" * 80)
        logger.info(f"\nNext steps:")
        logger.info(f"1. Load dataset: ds = xr.open_dataset('{output_file}')")
        logger.info(f"2. Compute vagueness: Use vagueness_v2.py scorer")
        logger.info(f"3. Compute is_software: Infer from keywords/description")
        logger.info(f"4. Compute L: Track Series B+ progression across windows")
        logger.info(f"5. Run specification curve analysis")

        return 0

    except Exception as e:
        logger.error(f"❌ Error: {e}", exc_info=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())
