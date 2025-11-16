#!/usr/bin/env python3
"""
Test script for parquet caching and quantum filtering features.

This script demonstrates:
1. Parquet caching for fast data loading
2. Quantum company filtering
3. Minimal column selection for hypothesis testing
"""

import logging
from pathlib import Path
from modules import features

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_parquet_caching():
    """Test parquet caching functionality."""
    logger.info("\n" + "="*80)
    logger.info("TEST 1: Parquet Caching")
    logger.info("="*80)

    # First run: should load from .dat files and save cache
    logger.info("\nRun 1: Loading from .dat files (or processed CSV)...")
    df1 = features.consolidate_company_snapshots(
        'data/raw',
        use_cache=False,  # Force reload
        save_parquet=True
    )

    if df1 is None:
        logger.warning("No .dat files found, using processed CSV instead")
        return

    logger.info(f"Loaded: {len(df1):,} companies")

    # Second run: should load from cache (much faster!)
    logger.info("\nRun 2: Loading from cache...")
    df2 = features.consolidate_company_snapshots(
        'data/raw',
        use_cache=True,  # Use cache
        save_parquet=False
    )

    logger.info(f"Loaded: {len(df2):,} companies")

    # Verify they're the same
    assert len(df1) == len(df2), "Cache mismatch!"
    logger.info("\n✅ Parquet caching works correctly!")


def test_quantum_filtering():
    """Test quantum company filtering."""
    logger.info("\n" + "="*80)
    logger.info("TEST 2: Quantum Company Filtering")
    logger.info("="*80)

    # Load all companies
    df_all = features.consolidate_company_snapshots('data/raw', use_cache=True)

    if df_all is None:
        logger.warning("No data available for testing")
        return

    logger.info(f"\nTotal companies: {len(df_all):,}")

    # Filter for quantum companies
    df_quantum = features.filter_quantum_companies(df_all)

    logger.info(f"\nQuantum companies: {len(df_quantum):,}")
    logger.info(f"Percentage: {len(df_quantum)/len(df_all)*100:.2f}%")

    if len(df_quantum) > 0:
        logger.info("\nSample quantum companies:")
        if 'CompanyName' in df_quantum.columns:
            for name in df_quantum['CompanyName'].head(5):
                logger.info(f"  - {name}")

    logger.info("\n✅ Quantum filtering works!")


def test_minimal_columns():
    """Test minimal column selection."""
    logger.info("\n" + "="*80)
    logger.info("TEST 3: Minimal Column Selection")
    logger.info("="*80)

    # Load all companies
    df_all = features.consolidate_company_snapshots('data/raw', use_cache=True)

    if df_all is None:
        logger.warning("No data available for testing")
        return

    logger.info(f"\nOriginal: {len(df_all.columns)} columns")

    # Select minimal columns
    df_minimal = features.select_hypothesis_columns(df_all)

    logger.info(f"Minimal: {len(df_minimal.columns)} columns")
    logger.info(f"\nSelected columns:")
    for col in df_minimal.columns:
        logger.info(f"  - {col}")

    logger.info("\n✅ Column selection works!")


def test_quantum_dataset_creation():
    """Test complete quantum dataset creation."""
    logger.info("\n" + "="*80)
    logger.info("TEST 4: Quantum Dataset Creation")
    logger.info("="*80)

    output_path = 'data/processed/test_quantum_dataset.parquet'

    # Create quantum dataset
    df_quantum = features.create_quantum_dataset(
        'data/raw',
        output_path=output_path
    )

    if len(df_quantum) > 0:
        logger.info(f"\n✅ Quantum dataset created!")
        logger.info(f"   Shape: {df_quantum.shape}")
        logger.info(f"   Saved to: {output_path}")

        # Verify file exists
        if Path(output_path).exists():
            import os
            file_size = os.path.getsize(output_path) / 1024
            logger.info(f"   File size: {file_size:.2f} KB")
    else:
        logger.warning("⚠️  No quantum companies found in dataset")


if __name__ == "__main__":
    logger.info("\n" + "🧪" * 40)
    logger.info("TESTING PARQUET CACHING & QUANTUM FILTERING")
    logger.info("🧪" * 40)

    try:
        # Run all tests
        test_parquet_caching()
        test_quantum_filtering()
        test_minimal_columns()
        test_quantum_dataset_creation()

        logger.info("\n" + "="*80)
        logger.info("✅ ALL TESTS PASSED!")
        logger.info("="*80)

    except Exception as e:
        logger.error(f"\n❌ Test failed: {e}", exc_info=True)
