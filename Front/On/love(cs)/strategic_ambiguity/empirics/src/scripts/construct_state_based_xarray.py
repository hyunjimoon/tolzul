#!/usr/bin/env python3
"""
Construct State-Based xarray Panel Dataset
===========================================

This implements the CORRECT logic for state-based cohorts:

"E is defined as funding amount of companies whose most recent financing
was Early Stage VC (Series A) as of Dec 2021, regardless of when that
financing occurred."

Key difference from event-based:
- Event-based: "Companies that GOT Series A in 2021"
- State-based: "Companies whose CURRENT STAGE is Series A as of Dec 2021"

Usage:
    python construct_state_based_xarray.py [--data-file PATH]
"""

import sys
import argparse
from pathlib import Path
import pandas as pd
import numpy as np
import xarray as xr
import logging
from typing import List, Tuple, Dict
from datetime import datetime

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
                "No consolidated parquet file found."
            )

        data_file = max(parquet_files, key=lambda p: p.stat().st_mtime)

    logger.info(f"📂 Loading data from: {data_file}")
    df = pd.read_parquet(data_file)
    logger.info(f"✓ Loaded {len(df):,} companies")

    return df


def determine_stage_at_snapshot(
    company_deals: pd.DataFrame,
    snapshot_date: str
) -> str:
    """Determine company's financing stage as of snapshot date.

    Args:
        company_deals: DataFrame with columns ['DealDate', 'DealType']
        snapshot_date: Date string 'YYYY-MM-DD'

    Returns:
        Stage name or 'Unknown'
    """
    if len(company_deals) == 0:
        return 'Unknown'

    # Filter deals before snapshot
    snapshot_dt = pd.to_datetime(snapshot_date)
    deals_before = company_deals[pd.to_datetime(company_deals['DealDate']) <= snapshot_dt]

    if len(deals_before) == 0:
        return 'Unknown'

    # Get most recent deal
    most_recent = deals_before.sort_values('DealDate').iloc[-1]
    return most_recent['DealType']


def compute_state_based_at_risk(
    company_ids: np.ndarray,
    deal_data: pd.DataFrame,
    snapshot_years: List[int],
    target_stage: str = 'Series A'
) -> Tuple[np.ndarray, Dict]:
    """Compute at_risk for state-based cohorts.

    Args:
        company_ids: Array of company IDs
        deal_data: DataFrame with columns ['CompanyID', 'DealDate', 'DealType']
        snapshot_years: Years for snapshots (e.g., [2021, 2022, 2023])
        target_stage: Stage to identify (default: 'Series A')

    Returns:
        Tuple of (at_risk array, stage_info dict)
    """
    logger.info(f"\n🔍 Computing state-based at_risk...")
    logger.info(f"   Target stage: {target_stage}")
    logger.info(f"   Snapshot years: {snapshot_years}")

    n_companies = len(company_ids)
    n_snapshots = len(snapshot_years)
    at_risk = np.zeros((n_companies, n_snapshots), dtype=np.int8)

    # Track stage at each snapshot for debugging
    stage_info = {year: {} for year in snapshot_years}

    for i, company_id in enumerate(company_ids):
        if i % 100 == 0:
            logger.info(f"   Processing company {i:,}/{n_companies:,}")

        # Get all deals for this company
        company_deals = deal_data[deal_data['CompanyID'] == company_id]

        for s, snapshot_year in enumerate(snapshot_years):
            snapshot_date = f"{snapshot_year}-12-31"
            stage = determine_stage_at_snapshot(company_deals, snapshot_date)

            # Company is "at risk" if at target stage on snapshot date
            if stage == target_stage:
                at_risk[i, s] = 1
                stage_info[snapshot_year][company_id] = stage

    # Log summary
    logger.info(f"\n✓ State-based at_risk computed:")
    for s, year in enumerate(snapshot_years):
        n_at_stage = at_risk[:, s].sum()
        logger.info(f"   {year} snapshot: {n_at_stage:,} companies at {target_stage} stage")

    return at_risk, stage_info


def create_window_coordinate(
    snapshot_years: List[int],
    horizon_years: List[int]
) -> Tuple:
    """Create window coordinate arrays.

    Args:
        snapshot_years: Years for cohort snapshots (e.g., [2021, 2022, 2023])
        horizon_years: Years after snapshot to observe (e.g., [1, 2, 3])

    Returns:
        Tuple of (window_ids, window_snapshot_years, window_end_years, window_horizons)
    """
    window_snapshot_years = []
    window_end_years = []
    window_horizons = []

    for snapshot_year in snapshot_years:
        for horizon in horizon_years:
            end_year = snapshot_year + horizon
            window_snapshot_years.append(snapshot_year)
            window_end_years.append(end_year)
            window_horizons.append(horizon)

    n_windows = len(window_snapshot_years)
    window_ids = np.arange(n_windows)

    logger.info(f"\n📊 Window coordinate created:")
    logger.info(f"   Snapshot years: {snapshot_years}")
    logger.info(f"   Horizon years: {horizon_years}")
    logger.info(f"   Total windows: {n_windows}")

    return window_ids, window_snapshot_years, window_end_years, window_horizons


def construct_state_based_dataset(
    company_df: pd.DataFrame,
    deal_df: pd.DataFrame,
    snapshot_years: List[int] = [2021, 2022, 2023],
    horizon_years: List[int] = [1, 2, 3],
    target_stage: str = 'Series A'
) -> xr.Dataset:
    """Construct xarray.Dataset with state-based cohorts.

    Args:
        company_df: Company data with ID, sector, etc.
        deal_df: Deal data with CompanyID, DealDate, DealType
        snapshot_years: Years to take snapshots (default: [2021, 2022, 2023])
        horizon_years: Years forward to observe (default: [1, 2, 3])
        target_stage: Stage for cohort membership (default: 'Series A')

    Returns:
        xarray.Dataset with state-based at_risk variable
    """
    logger.info("\n" + "=" * 80)
    logger.info("CONSTRUCTING STATE-BASED XARRAY DATASET")
    logger.info("=" * 80)

    # Get company IDs
    company_id_col = 'CompanyID' if 'CompanyID' in company_df.columns else 'company_id'
    company_ids = company_df[company_id_col].values
    n_companies = len(company_ids)

    logger.info(f"\n📊 Dataset dimensions:")
    logger.info(f"   Companies: {n_companies:,}")

    # Create window coordinates
    window_ids, window_snapshot_years, window_end_years, window_horizons = \
        create_window_coordinate(snapshot_years, horizon_years)
    n_windows = len(window_ids)

    # Extract sector
    sector_col = None
    for col in ['Sector', 'sector', 'PrimarySector']:
        if col in company_df.columns:
            sector_col = col
            break

    sectors = company_df[sector_col].fillna('Unknown').values if sector_col else \
        np.array(['Unknown'] * n_companies)

    # Initialize dataset
    logger.info("\n🏗️  Creating dataset structure...")

    ds = xr.Dataset(
        coords={
            'company_id': company_ids,
            'window': window_ids,
            'sector': ('company_id', sectors),
            'snapshot_year': ('window', window_snapshot_years),
            'end_year': ('window', window_end_years),
            'horizon_years': ('window', window_horizons),
        }
    )

    # Compute state-based at_risk
    at_risk, stage_info = compute_state_based_at_risk(
        company_ids,
        deal_df,
        snapshot_years,
        target_stage
    )

    ds['at_risk'] = (('company_id', 'window'), at_risk)

    # Add metadata
    ds.attrs['schema_version'] = 'esi-state-based.v1'
    ds.attrs['cohort_logic'] = 'state-based'
    ds.attrs['target_stage'] = target_stage
    ds.attrs['snapshot_years'] = snapshot_years
    ds.attrs['horizon_years'] = horizon_years
    ds.attrs['description'] = (
        f'State-based cohorts: Companies at {target_stage} stage '
        f'as of Dec 31 of snapshot year'
    )

    logger.info("\n" + "=" * 80)
    logger.info("✅ STATE-BASED DATASET CONSTRUCTED")
    logger.info("=" * 80)

    return ds, stage_info


def validate_state_based_dataset(ds: xr.Dataset, stage_info: Dict):
    """Validate the state-based dataset."""
    logger.info("\n" + "=" * 80)
    logger.info("🔍 VALIDATING STATE-BASED DATASET")
    logger.info("=" * 80)

    snapshot_years = ds.attrs['snapshot_years']

    # Check at_risk patterns
    logger.info(f"\n✓ Cohort sizes by snapshot:")
    for s, year in enumerate(snapshot_years):
        n_at_risk = ds.at_risk.isel(window=s).sum().values
        logger.info(f"   {year}: {n_at_risk:,} companies at target stage")

    # Check if companies can appear in multiple cohorts (they should!)
    at_risk_sum = ds.at_risk.sum('window').values
    max_cohorts = int(at_risk_sum.max())

    companies_in_multiple = (at_risk_sum > 1).sum()
    logger.info(f"\n✓ State-based cohort overlap:")
    logger.info(f"   Max snapshots per company: {max_cohorts}")
    logger.info(f"   Companies in multiple snapshots: {companies_in_multiple}")
    logger.info(f"   This is EXPECTED for state-based cohorts!")

    # Show example
    if companies_in_multiple > 0:
        example_idx = np.where(at_risk_sum > 1)[0][0]
        company_id = ds.company_id.values[example_idx]
        at_risk_pattern = ds.at_risk.sel(company_id=company_id).values

        logger.info(f"\n   Example: Company {company_id}")
        logger.info(f"   at_risk pattern: {at_risk_pattern}")
        logger.info(f"   Interpretation: At target stage in {at_risk_sum[example_idx]} snapshots")

    logger.info("\n" + "=" * 80)
    logger.info("✅ VALIDATION COMPLETE")
    logger.info("=" * 80)


def main():
    """Main execution."""
    parser = argparse.ArgumentParser(description='Construct state-based xarray dataset')
    parser.add_argument('--company-file', type=Path, help='Path to company parquet file')
    parser.add_argument('--deal-file', type=Path, help='Path to deal parquet file')
    parser.add_argument('--snapshot-years', type=int, nargs='+', default=[2021, 2022, 2023],
                        help='Snapshot years (default: 2021 2022 2023)')
    parser.add_argument('--horizon-years', type=int, nargs='+', default=[1, 2, 3],
                        help='Horizon years (default: 1 2 3)')
    parser.add_argument('--target-stage', type=str, default='Series A',
                        help='Target stage (default: Series A)')
    parser.add_argument('--output', type=Path,
                        default=Path('outputs/xarray_design/state_based_dataset.nc'),
                        help='Output path for netCDF file')
    args = parser.parse_args()

    try:
        # Load company data
        company_df = load_company_data(args.company_file)

        # Load deal data (you'll need to implement this based on your Deal*.dat files)
        if args.deal_file:
            deal_df = pd.read_parquet(args.deal_file)
        else:
            logger.warning("⚠️  No deal file provided. Cannot compute real at_risk.")
            logger.warning("    Create mock deal data for demonstration.")
            # Create mock deal data for demo
            deal_df = create_mock_deal_data(company_df)

        # Construct dataset
        ds, stage_info = construct_state_based_dataset(
            company_df,
            deal_df,
            args.snapshot_years,
            args.horizon_years,
            args.target_stage
        )

        # Validate
        validate_state_based_dataset(ds, stage_info)

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

        return 0

    except Exception as e:
        logger.error(f"❌ Error: {e}", exc_info=True)
        return 1


def create_mock_deal_data(company_df: pd.DataFrame) -> pd.DataFrame:
    """Create mock deal data for demonstration."""
    logger.info("\n🎭 Creating mock deal data for demonstration...")

    company_id_col = 'CompanyID' if 'CompanyID' in company_df.columns else 'company_id'
    company_ids = company_df[company_id_col].values[:100]  # Use subset

    deals = []
    np.random.seed(42)

    for company_id in company_ids:
        # Random number of deals (1-5)
        n_deals = np.random.randint(1, 6)

        # Generate deal progression
        stages = ['Seed', 'Series A', 'Series B', 'Series C']
        years = [2018, 2019, 2020, 2021, 2022, 2023]

        current_stage = 0
        for _ in range(n_deals):
            if current_stage < len(stages):
                deal_year = np.random.choice(years)
                deals.append({
                    'CompanyID': company_id,
                    'DealDate': f"{deal_year}-{np.random.randint(1,13):02d}-{np.random.randint(1,29):02d}",
                    'DealType': stages[current_stage],
                    'DealAmount': np.random.randint(1, 50) * 1e6
                })
                # Sometimes progress, sometimes stay at same stage
                if np.random.random() > 0.3:
                    current_stage += 1

    deal_df = pd.DataFrame(deals)
    logger.info(f"   Created {len(deals):,} mock deals for {len(company_ids)} companies")

    return deal_df


if __name__ == '__main__':
    sys.exit(main())
