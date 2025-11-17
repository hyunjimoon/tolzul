#!/usr/bin/env python3
"""
Pipeline Step 3: Filter Datasets
=================================
Creates three dataset variants: all, quantum, transportation.

Usage:
    python pipeline/03_filter_datasets.py
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import pandas as pd
import yaml
import logging
from features import (
    consolidate_company_snapshots,
    filter_quantum_companies,
    filter_transportation_companies
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Filter datasets into three variants."""
    logger.info("=" * 80)
    logger.info("STEP 3: FILTER DATASETS")
    logger.info("=" * 80)

    # Load configuration
    config_file = Path("config/datasets.yaml")
    with open(config_file) as f:
        config = yaml.safe_load(f)

    # Paths
    cache_dir = Path("data/processed")
    features_file = cache_dir / "features_all.parquet"

    # Load engineered features
    logger.info(f"\n📂 Loading engineered features from {features_file}")

    # Check if file exists and is valid
    if not features_file.exists():
        logger.error(f"❌ Features file not found: {features_file}")
        logger.error(f"   Run pipeline/02_engineer_features.py first")
        return 1

    # Try to load with error handling for corrupted files
    try:
        df_all = pd.read_parquet(features_file)
    except Exception as e:
        logger.error(f"❌ Failed to load parquet file: {e}")
        logger.error(f"   File may be corrupted. Deleting and re-running Step 2 may help.")
        logger.error(f"   Run: rm {features_file} && python3 pipeline/02_engineer_features.py")
        return 1

    logger.info(f"   Total companies: {len(df_all):,}")
    logger.info(f"   Columns: {len(df_all.columns)}")

    # Check for text columns used in filtering
    text_cols = ['Description', 'Keywords', 'Promise', 'description', 'keywords', 'promise']
    available_text_cols = [c for c in text_cols if c in df_all.columns]
    logger.info(f"   Text columns available for filtering: {available_text_cols}")
    if not available_text_cols:
        logger.warning(f"   ⚠️  No standard text columns found! Filters may not work.")
        logger.info(f"   Available columns (first 20): {df_all.columns.tolist()[:20]}")

    # Process each dataset variant
    filter_functions = {
        'quantum': filter_quantum_companies,
        'transportation': filter_transportation_companies
    }

    for dataset_key, dataset_config in config['datasets'].items():
        logger.info(f"\n{'='*60}")
        logger.info(f"Processing: {dataset_config['name']}")
        logger.info(f"{'='*60}")

        # Apply filter if specified
        filter_func_name = dataset_config.get('filter_function')
        if filter_func_name and filter_func_name in ['filter_quantum_companies', 'filter_transportation_companies']:
            logger.info(f"   Applying filter: {filter_func_name}")
            filter_func = filter_functions[dataset_key]
            df_filtered = filter_func(df_all)
        else:
            logger.info(f"   No filter (using all companies)")
            df_filtered = df_all.copy()

        # Save filtered dataset
        output_dir = Path(dataset_config['output_dir'])
        output_dir.mkdir(exist_ok=True, parents=True)

        output_file = output_dir / "dataset.parquet"
        logger.info(f"\n💾 Saving to {output_file}")
        df_filtered.to_parquet(output_file, index=False)
        logger.info(f"   Saved {len(df_filtered):,} companies ({output_file.stat().st_size / 1e6:.1f} MB)")
        logger.info(f"   Percentage of total: {len(df_filtered)/len(df_all)*100:.2f}%")

        # Summary statistics
        if 'vagueness' in df_filtered.columns:
            v_mean = df_filtered['vagueness'].mean()
            v_std = df_filtered['vagueness'].std()
            logger.info(f"\n📊 Summary Statistics:")
            logger.info(f"   Vagueness: mean={v_mean:.4f}, std={v_std:.4f}")

        if 'is_hardware' in df_filtered.columns:
            hw_counts = df_filtered['is_hardware'].value_counts()
            # is_hardware is stored as int (1/0), not bool (True/False)
            hw_count = hw_counts.get(1, 0) + hw_counts.get(True, 0)  # Check both
            sw_count = hw_counts.get(0, 0) + hw_counts.get(False, 0)  # Check both
            logger.info(f"   Hardware companies: {hw_count:,}")
            logger.info(f"   Software companies: {sw_count:,}")

    logger.info("\n" + "=" * 80)
    logger.info("STEP 3 COMPLETE ✓")
    logger.info(f"Created {len(config['datasets'])} dataset variants")
    logger.info("=" * 80)

    return 0


if __name__ == '__main__':
    sys.exit(main())
