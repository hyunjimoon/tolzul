#!/usr/bin/env python3
"""
Convert Parquet Files to NetCDF
================================
Batch convert all .parquet files in data/processed to .nc format.

This allows using NetCDF instead of Parquet (better for users without pyarrow).

Usage:
    python scripts/convert_to_netcdf.py
    python scripts/convert_to_netcdf.py --directory data/processed --pattern "*.parquet"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import argparse
from data_io import convert_parquet_to_nc, save_dataframe
import pandas as pd


def convert_all_parquet(
    directory: str = 'data/processed',
    pattern: str = '*.parquet',
    remove_original: bool = False
):
    """
    Convert all .parquet files in directory to .nc.

    Args:
        directory: Directory to search for .parquet files
        pattern: Glob pattern for matching files
        remove_original: Whether to delete .parquet after conversion
    """
    directory = Path(directory)

    if not directory.exists():
        print(f"❌ Directory not found: {directory}")
        return

    # Find all parquet files
    parquet_files = list(directory.glob(pattern))

    if not parquet_files:
        print(f"No .parquet files found in {directory}")
        return

    print(f"Found {len(parquet_files)} .parquet files to convert\n")

    success_count = 0
    fail_count = 0

    for parquet_path in parquet_files:
        try:
            print(f"Converting {parquet_path.name}...")

            # Convert
            nc_path = convert_parquet_to_nc(parquet_path)

            # Check sizes
            parquet_size = parquet_path.stat().st_size / 1e6
            nc_size = nc_path.stat().st_size / 1e6

            print(f"  ✓ {parquet_path.name} ({parquet_size:.1f} MB)")
            print(f"    → {nc_path.name} ({nc_size:.1f} MB)")
            print(f"    Ratio: {nc_size/parquet_size:.2f}x\n")

            success_count += 1

            # Remove original if requested
            if remove_original:
                parquet_path.unlink()
                print(f"  🗑️  Removed {parquet_path.name}\n")

        except Exception as e:
            print(f"  ❌ Failed: {e}\n")
            fail_count += 1

    print(f"=== Conversion Complete ===")
    print(f"Success: {success_count}")
    print(f"Failed: {fail_count}")

    if success_count > 0:
        print(f"\n💡 Update your scripts to use .nc files:")
        print(f"   from data_io import load_dataframe")
        print(f"   df = load_dataframe('data/processed/your_file.nc')")


def main():
    parser = argparse.ArgumentParser(
        description='Convert Parquet files to NetCDF format'
    )
    parser.add_argument(
        '--directory',
        type=str,
        default='data/processed',
        help='Directory to search for .parquet files'
    )
    parser.add_argument(
        '--pattern',
        type=str,
        default='*.parquet',
        help='Glob pattern for matching files'
    )
    parser.add_argument(
        '--remove-original',
        action='store_true',
        help='Remove .parquet files after successful conversion'
    )

    args = parser.parse_args()

    convert_all_parquet(
        directory=args.directory,
        pattern=args.pattern,
        remove_original=args.remove_original
    )


if __name__ == '__main__':
    main()
