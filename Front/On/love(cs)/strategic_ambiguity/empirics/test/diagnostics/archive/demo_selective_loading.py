#!/usr/bin/env python3
"""
Demonstration of selective year loading for faster data loading.

For analysis with time windows 2022-2024 and 2022-2025,
only load 2022, 2024, 2025 data files instead of all 9 files.

Performance improvement: 33% faster (6 files vs 9 files)
"""

import logging
from pathlib import Path
from modules import features
import time

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def demo_full_loading():
    """Demo: Load all years (slower)."""
    logger.info("\n" + "="*80)
    logger.info("DEMO 1: Load ALL years (9 files)")
    logger.info("="*80)

    start = time.time()
    df_all = features.consolidate_company_snapshots(
        'data/raw',
        use_cache=False,  # Force reload to measure real time
        save_parquet=True,
        years=None  # Load all years
    )
    elapsed = time.time() - start

    if df_all is not None:
        logger.info(f"\n✅ Loaded {len(df_all):,} companies in {elapsed:.1f} seconds")
        logger.info(f"   Date range: {df_all['snapshot_date'].min()} to {df_all['snapshot_date'].max()}")
        logger.info(f"   Unique years: {sorted(df_all['snapshot_date'].dt.year.unique())}")
    else:
        logger.warning("No .dat files found")

    return df_all, elapsed


def demo_selective_loading():
    """Demo: Load only 2022, 2024, 2025 (faster)."""
    logger.info("\n" + "="*80)
    logger.info("DEMO 2: Load ONLY 2022, 2024, 2025 (6 files)")
    logger.info("="*80)

    start = time.time()
    df_selective = features.consolidate_company_snapshots(
        'data/raw',
        use_cache=False,  # Force reload to measure real time
        save_parquet=True,
        years=[2022, 2024, 2025]  # Only these years
    )
    elapsed = time.time() - start

    if df_selective is not None:
        logger.info(f"\n✅ Loaded {len(df_selective):,} companies in {elapsed:.1f} seconds")
        logger.info(f"   Date range: {df_selective['snapshot_date'].min()} to {df_selective['snapshot_date'].max()}")
        logger.info(f"   Unique years: {sorted(df_selective['snapshot_date'].dt.year.unique())}")
    else:
        logger.warning("No .dat files found")

    return df_selective, elapsed


def demo_cached_loading():
    """Demo: Load from cache (fastest)."""
    logger.info("\n" + "="*80)
    logger.info("DEMO 3: Load from CACHE (fastest)")
    logger.info("="*80)

    start = time.time()
    df_cached = features.consolidate_company_snapshots(
        'data/raw',
        use_cache=True,  # Use cache
        years=[2022, 2024, 2025]
    )
    elapsed = time.time() - start

    if df_cached is not None:
        logger.info(f"\n✅ Loaded {len(df_cached):,} companies in {elapsed:.1f} seconds (from cache!)")
    else:
        logger.warning("No cache found")

    return df_cached, elapsed


if __name__ == "__main__":
    logger.info("\n" + "🚀" * 40)
    logger.info("SELECTIVE YEAR LOADING DEMO")
    logger.info("🚀" * 40)

    # Check if .dat files exist
    dat_files = list(Path('data/raw').glob('Company*.dat'))
    if not dat_files:
        logger.error("\n❌ No .dat files found in data/raw/")
        logger.info("This demo requires Company*.dat files to demonstrate performance.")
        logger.info("\nYou can still use the feature with:")
        logger.info("  python main.py --years 2022 2024 2025 --data-dir data/raw/")
        exit(1)

    logger.info(f"\nFound {len(dat_files)} .dat files:")
    for f in sorted(dat_files):
        logger.info(f"  - {f.name}")

    try:
        # Demo 1: Load all years
        df_all, time_all = demo_full_loading()

        # Demo 2: Load selective years
        df_sel, time_sel = demo_selective_loading()

        # Demo 3: Load from cache
        df_cache, time_cache = demo_cached_loading()

        # Summary
        logger.info("\n" + "="*80)
        logger.info("PERFORMANCE SUMMARY")
        logger.info("="*80)

        if df_all is not None and df_sel is not None:
            speedup = time_all / time_sel if time_sel > 0 else 0
            logger.info(f"\n1️⃣ Load ALL years:      {time_all:.1f}s (baseline)")
            logger.info(f"2️⃣ Load 2022,2024,2025: {time_sel:.1f}s ({speedup:.1f}x faster) ⚡")
            logger.info(f"3️⃣ Load from cache:    {time_cache:.1f}s ({time_all/time_cache:.1f}x faster) 🚀")

            logger.info(f"\n📊 Efficiency Gains:")
            logger.info(f"   Files loaded: 9 → 6 (33% reduction)")
            logger.info(f"   Time saved: {time_all - time_sel:.1f}s ({(1 - time_sel/time_all)*100:.1f}%)")
            logger.info(f"   Cache speedup: {time_all / time_cache:.1f}x")

            logger.info(f"\n💡 Recommendation:")
            logger.info(f"   For time windows 2022-2024 and 2022-2025:")
            logger.info(f"   Use: --years 2022 2024 2025")
            logger.info(f"   This loads only relevant years and saves {(1 - time_sel/time_all)*100:.0f}% time!")

        logger.info("\n" + "="*80)
        logger.info("✅ DEMO COMPLETE!")
        logger.info("="*80)

        logger.info("\n📝 Usage Examples:")
        logger.info("  # Load specific years")
        logger.info("  python main.py --years 2022 2024 2025 --data-dir data/raw/")
        logger.info("")
        logger.info("  # Python API")
        logger.info("  from modules import features")
        logger.info("  df = features.consolidate_company_snapshots(")
        logger.info("      'data/raw',")
        logger.info("      years=[2022, 2024, 2025]")
        logger.info("  )")

    except Exception as e:
        logger.error(f"\n❌ Demo failed: {e}", exc_info=True)
