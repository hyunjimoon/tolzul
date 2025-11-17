#!/usr/bin/env python3
"""
Pipeline Step 2: Engineer Features
===================================
Applies StrategicVaguenessScorerV2 and creates all features needed for H1/H2.

Usage:
    python pipeline/02_engineer_features.py
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import pandas as pd
import logging
from features import consolidate_company_snapshots, engineer_features
from vagueness_v2 import StrategicVaguenessScorerV2
from cache_manager import CacheManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Engineer features using V2 vagueness scorer."""
    logger.info("=" * 80)
    logger.info("STEP 2: ENGINEER FEATURES")
    logger.info("=" * 80)

    # Initialize cache manager
    cache = CacheManager()

    # Check if features already cached
    logger.info(f"\n🔍 Checking cache...")
    df_features = cache.load_step('features', scenario='all')

    if df_features is not None:
        logger.info(f"✅ Loaded from cache - skipping feature engineering")
        logger.info(f"   Cached rows: {len(df_features):,}")
        logger.info(f"   To force recompute: cache.clear_step('features', 'all')")
    else:
        # Paths
        data_dir = Path("data/raw")
        cache_dir = Path("data/processed")
        cache_dir.mkdir(exist_ok=True, parents=True)

        # Load data
        logger.info(f"\n📂 Loading company data from cache/raw")
        df = consolidate_company_snapshots(str(data_dir))

        # Compute input hash for cache validation
        input_hash = cache._compute_hash(df)

        logger.info(f"\n🔧 Engineering features with V2 scorer")
        logger.info(f"   Input rows: {len(df):,}")

        # Apply feature engineering (uses StrategicVaguenessScorerV2)
        df_features = engineer_features(df)

        # Save to cache
        logger.info(f"\n💾 Saving to cache...")
        cache.save_step(
            'features',
            df_features,
            scenario='all',
            input_hash=input_hash,
            extra_metadata={'scorer': 'StrategicVaguenessScorerV2'}
        )

    logger.info(f"\n✅ Feature engineering complete")
    logger.info(f"   Output rows: {len(df_features):,}")
    logger.info(f"   New columns: {len(df_features.columns)}")

    # Check key features
    key_features = ['vagueness', 'is_hardware', 'early_funding', 'employees_log', 'firm_age']
    available_features = [f for f in key_features if f in df_features.columns]
    logger.info(f"\n📊 Key Features Created:")
    for feat in available_features:
        if df_features[feat].dtype in ['float64', 'float32', 'int64', 'int32']:
            mean_val = df_features[feat].mean()
            std_val = df_features[feat].std()
            logger.info(f"   {feat}: mean={mean_val:.4f}, std={std_val:.4f}")
        else:
            counts = df_features[feat].value_counts()
            logger.info(f"   {feat}: {dict(counts)}")

    # Vagueness scorer details
    if 'vagueness' in df_features.columns:
        v_stats = df_features['vagueness'].describe()
        logger.info(f"\n🎯 Vagueness Score Distribution (V2):")
        logger.info(f"   Mean: {v_stats['mean']:.4f}")
        logger.info(f"   Std:  {v_stats['std']:.4f}")
        logger.info(f"   Min:  {v_stats['min']:.4f}")
        logger.info(f"   25%:  {v_stats['25%']:.4f}")
        logger.info(f"   50%:  {v_stats['50%']:.4f}")
        logger.info(f"   75%:  {v_stats['75%']:.4f}")
        logger.info(f"   Max:  {v_stats['max']:.4f}")

    # Also save to legacy location for backwards compatibility
    cache_dir = Path("data/processed")
    output_file = cache_dir / "features_all.parquet"
    logger.info(f"\n💾 Saving to legacy location: {output_file}")

    try:
        df_features.to_parquet(output_file, index=False, engine='pyarrow')
        file_size = output_file.stat().st_size
        logger.info(f"   Saved {len(df_features):,} rows ({file_size / 1e6:.1f} MB)")
    except Exception as e:
        logger.error(f"❌ Failed to save parquet file: {e}")
        return 1

    logger.info("\n" + "=" * 80)
    logger.info("STEP 2 COMPLETE ✓")
    logger.info("=" * 80)

    return 0


if __name__ == '__main__':
    sys.exit(main())
