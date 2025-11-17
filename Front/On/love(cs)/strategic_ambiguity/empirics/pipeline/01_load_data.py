#!/usr/bin/env python3
"""
Pipeline Step 1: Load and Cache Data
====================================
Loads .dat files from data/raw and creates parquet cache for fast loading.
10-50x speedup for subsequent runs.

Usage:
    python pipeline/01_load_data.py
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import pandas as pd
import logging
from features import consolidate_company_snapshots

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Load raw .dat files and create parquet cache."""
    logger.info("=" * 80)
    logger.info("STEP 1: LOAD DATA")
    logger.info("=" * 80)

    # Paths
    data_dir = Path("data/raw")
    cache_dir = Path("data/processed")
    cache_dir.mkdir(exist_ok=True, parents=True)

    cache_file = cache_dir / "consolidated_companies.parquet"

    # Load data (uses parquet cache if available)
    logger.info(f"\n📂 Loading company data from {data_dir}")
    df = consolidate_company_snapshots(str(data_dir))

    logger.info(f"\n✅ Data loaded successfully")
    logger.info(f"   Total companies: {len(df):,}")
    logger.info(f"   Columns: {len(df.columns)}")
    logger.info(f"   Memory: {df.memory_usage(deep=True).sum() / 1e6:.1f} MB")

    # Save cache if not exists
    if not cache_file.exists():
        logger.info(f"\n💾 Saving parquet cache to {cache_file}")
        df.to_parquet(cache_file, index=False)
        logger.info(f"   Cache saved ({cache_file.stat().st_size / 1e6:.1f} MB)")
    else:
        logger.info(f"\n✓ Parquet cache already exists at {cache_file}")

    # Summary statistics
    logger.info("\n📊 Data Summary:")
    if 'Description' in df.columns:
        logger.info(f"   Companies with descriptions: {df['Description'].notna().sum():,}")
    if 'FirstFinancingSize' in df.columns:
        logger.info(f"   Companies with financing data: {df['FirstFinancingSize'].notna().sum():,}")
    if 'YearFounded' in df.columns:
        years = df['YearFounded'].dropna()
        logger.info(f"   Founding years range: {int(years.min())} - {int(years.max())}")

    logger.info("\n" + "=" * 80)
    logger.info("STEP 1 COMPLETE ✓")
    logger.info("=" * 80)

    return 0


if __name__ == '__main__':
    sys.exit(main())
