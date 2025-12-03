#!/usr/bin/env python3
"""
Data I/O Utilities - NetCDF (.nc) Support
==========================================
Helper functions for saving/loading DataFrames as NetCDF files.

NetCDF advantages over Parquet:
- xarray native format (already in requirements)
- Multi-dimensional data support
- Rich metadata
- No installation issues

Usage:
    from data_io import save_dataframe, load_dataframe

    # Save
    save_dataframe(df, 'data/processed/features.nc')

    # Load
    df = load_dataframe('data/processed/features.nc')
"""

import pandas as pd
import xarray as xr
import numpy as np
from pathlib import Path
from typing import Union, Optional
import logging

logger = logging.getLogger(__name__)

# Auto-detect available NetCDF backend
def _get_netcdf_engine():
    """Detect available NetCDF backend (netcdf4 or h5netcdf)."""
    try:
        import netCDF4
        return 'netcdf4'
    except ImportError:
        try:
            import h5netcdf
            logger.info("Using h5netcdf backend (netCDF4 not available)")
            return 'h5netcdf'
        except ImportError:
            raise ImportError(
                "Neither netCDF4 nor h5netcdf found. Install one:\n"
                "  pip install netcdf4  (recommended)\n"
                "  pip install h5netcdf (pure Python alternative)"
            )

NETCDF_ENGINE = _get_netcdf_engine()


def save_dataframe(
    df: pd.DataFrame,
    filepath: Union[str, Path],
    compression: Optional[str] = 'zlib'
) -> None:
    """
    Save DataFrame as NetCDF file.

    Args:
        df: Pandas DataFrame to save
        filepath: Output path (*.nc)
        compression: Compression method ('zlib', 'lzf', None)

    Example:
        >>> df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        >>> save_dataframe(df, 'data/test.nc')
    """
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    # Convert DataFrame to xarray Dataset
    # Index becomes a coordinate
    ds = df.to_xarray()

    # Set encoding for compression
    encoding = {}
    if compression:
        for var in ds.data_vars:
            encoding[var] = {'zlib': True, 'complevel': 4}

    # Save to NetCDF (auto-detect backend)
    ds.to_netcdf(filepath, encoding=encoding, engine=NETCDF_ENGINE)

    logger.info(f"Saved DataFrame to {filepath} ({filepath.stat().st_size / 1e6:.1f} MB)")


def load_dataframe(
    filepath: Union[str, Path],
    index_col: Optional[str] = None
) -> pd.DataFrame:
    """
    Load DataFrame from NetCDF file.

    Args:
        filepath: Input path (*.nc)
        index_col: Column to set as index (optional)

    Returns:
        Pandas DataFrame

    Example:
        >>> df = load_dataframe('data/test.nc')
        >>> df = load_dataframe('data/test.nc', index_col='company_id')
    """
    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    # Load NetCDF as xarray Dataset (auto-detect backend)
    ds = xr.open_dataset(filepath, engine=NETCDF_ENGINE)

    # Convert to DataFrame
    df = ds.to_dataframe()

    # Reset index (xarray creates multi-index)
    df = df.reset_index()

    # Set index if specified
    if index_col and index_col in df.columns:
        df = df.set_index(index_col)

    # Close dataset
    ds.close()

    logger.info(f"Loaded DataFrame from {filepath}: {len(df):,} rows × {len(df.columns)} cols")

    return df


def convert_parquet_to_nc(
    parquet_path: Union[str, Path],
    nc_path: Optional[Union[str, Path]] = None
) -> Path:
    """
    Convert existing .parquet file to .nc format.

    Args:
        parquet_path: Input .parquet file
        nc_path: Output .nc file (default: same name with .nc extension)

    Returns:
        Path to output .nc file

    Example:
        >>> convert_parquet_to_nc('data/features.parquet', 'data/features.nc')
    """
    parquet_path = Path(parquet_path)

    if nc_path is None:
        nc_path = parquet_path.with_suffix('.nc')
    else:
        nc_path = Path(nc_path)

    # Load parquet
    df = pd.read_parquet(parquet_path)

    # Save as NetCDF
    save_dataframe(df, nc_path)

    logger.info(f"Converted {parquet_path} → {nc_path}")

    return nc_path


def get_data_path(
    filename: str,
    prefer_nc: bool = True
) -> Path:
    """
    Get data path, preferring .nc over .parquet if both exist.

    Args:
        filename: Base filename (with or without extension)
        prefer_nc: If True, prefer .nc over .parquet

    Returns:
        Path to data file

    Example:
        >>> path = get_data_path('features_engineered')
        >>> # Returns 'features_engineered.nc' if exists, else 'features_engineered.parquet'
    """
    base = Path(filename).with_suffix('')

    nc_path = base.with_suffix('.nc')
    parquet_path = base.with_suffix('.parquet')

    if prefer_nc:
        if nc_path.exists():
            return nc_path
        elif parquet_path.exists():
            logger.warning(f".nc not found, using .parquet: {parquet_path}")
            return parquet_path
    else:
        if parquet_path.exists():
            return parquet_path
        elif nc_path.exists():
            logger.warning(f".parquet not found, using .nc: {nc_path}")
            return nc_path

    # Neither exists
    raise FileNotFoundError(f"Neither .nc nor .parquet found for: {base}")


# Convenience functions
def quick_save(df: pd.DataFrame, name: str, directory: str = 'data/processed'):
    """Quick save with default location."""
    filepath = Path(directory) / f"{name}.nc"
    save_dataframe(df, filepath)
    return filepath


def quick_load(name: str, directory: str = 'data/processed') -> pd.DataFrame:
    """Quick load with default location."""
    filepath = Path(directory) / f"{name}.nc"
    return load_dataframe(filepath)
