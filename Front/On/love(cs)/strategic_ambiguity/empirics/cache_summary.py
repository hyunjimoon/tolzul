#!/usr/bin/env python3
"""
Cache Summary Tool
==================
View cache status and perform cache operations.

Usage:
    python3 cache_summary.py                 # Show cache summary
    python3 cache_summary.py --clear all     # Clear entire cache
    python3 cache_summary.py --clear features # Clear specific step
    python3 cache_summary.py --demo          # Run xarray demo
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from cache_manager import CacheManager, demo_xarray_usage
import pandas as pd


def print_cache_summary(cache: CacheManager):
    """Print formatted cache summary."""
    print("=" * 80)
    print("PIPELINE CACHE SUMMARY")
    print("=" * 80)
    print()

    summary_df = cache.summary()

    if len(summary_df) == 0:
        print("❌ No cached data found")
        print()
        print("Run pipeline steps to populate cache:")
        print("  python3 pipeline/02_engineer_features.py")
        print("  python3 pipeline/04_run_models.py")
        return

    print(f"📦 Total cached steps: {len(summary_df)}")
    print()

    # Group by step
    for step in summary_df['step'].unique():
        step_data = summary_df[summary_df['step'] == step]
        print(f"\n🔹 {step.upper()}")
        print("  " + "-" * 76)

        for _, row in step_data.iterrows():
            scenario = row['scenario']
            timestamp = row['timestamp'][:19] if len(row['timestamp']) > 19 else row['timestamp']
            rows = row['rows']
            cols = row['columns']
            file = row['file']

            print(f"  {scenario:15s} │ {timestamp} │ {rows:>8,} rows × {cols:>3} cols │ {file}")

    print()
    print("=" * 80)
    print()
    print("💡 Tips:")
    print("  • To use cached data, simply run pipeline steps normally")
    print("  • Cache is invalidated automatically when inputs change")
    print("  • Force recompute: python3 cache_summary.py --clear <step>")
    print("  • View xarray structure: python3 cache_summary.py --demo")
    print()


def clear_cache(cache: CacheManager, target: str):
    """Clear cache for specified target."""
    if target == 'all':
        print(f"⚠️  Clearing ENTIRE cache...")
        cache.clear_all()
        print(f"✓ All cache cleared")
    else:
        scenarios = ['default', 'all', 'quantum', 'transportation']
        for scenario in scenarios:
            cache.clear_step(target, scenario)
        print(f"✓ Cleared cache for step: {target}")


def main():
    """Main entry point."""
    cache = CacheManager()

    # Parse arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1]

        if arg == '--demo':
            # Run xarray demo
            demo_xarray_usage()
            return 0

        elif arg == '--clear':
            if len(sys.argv) < 3:
                print("❌ Usage: python3 cache_summary.py --clear <step|all>")
                return 1
            target = sys.argv[2]
            clear_cache(cache, target)
            return 0

        elif arg == '--help':
            print(__doc__)
            return 0

    # Default: show summary
    print_cache_summary(cache)
    return 0


if __name__ == '__main__':
    sys.exit(main())
