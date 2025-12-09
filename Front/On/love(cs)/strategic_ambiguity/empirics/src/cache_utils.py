#!/usr/bin/env python3
"""
Cache Validation Utilities
===========================
Smart cache invalidation using mtime + metadata strategy.

Usage:
    from src.cache_utils import is_cache_valid, save_cache_metadata, load_cache_metadata

    if is_cache_valid('features_all.nc', source_files=['data/raw/*.dat'], version='2.0'):
        df = load_from_cache()
    else:
        df = recompute()
        save_with_metadata(df, version='2.0')
"""

import json
from pathlib import Path
from typing import List, Union, Optional, Dict
import logging

logger = logging.getLogger(__name__)

# Current pipeline version (increment when you change core logic)
PIPELINE_VERSION = "2.0"


def get_cache_metadata_path(cache_file: Path) -> Path:
    """Get metadata file path for a cache file.

    Example:
        data/processed/features_all.nc → data/processed/.features_all.nc.meta
    """
    return cache_file.parent / f".{cache_file.name}.meta"


def save_cache_metadata(
    cache_file: Path,
    source_files: List[Path],
    pipeline_version: str = PIPELINE_VERSION,
    extra: Optional[Dict] = None
) -> None:
    """Save metadata alongside cache file.

    Args:
        cache_file: Path to cache file (e.g., features_all.nc)
        source_files: List of source files used to generate cache
        pipeline_version: Version of pipeline code
        extra: Additional metadata to store
    """
    metadata = {
        'pipeline_version': pipeline_version,
        'cache_file': str(cache_file),
        'cache_mtime': cache_file.stat().st_mtime if cache_file.exists() else None,
        'sources': [
            {
                'path': str(f),
                'mtime': f.stat().st_mtime if f.exists() else None
            }
            for f in source_files
        ]
    }

    if extra:
        metadata['extra'] = extra

    meta_path = get_cache_metadata_path(cache_file)
    with open(meta_path, 'w') as f:
        json.dump(metadata, f, indent=2)

    logger.debug(f"Saved cache metadata to {meta_path}")


def load_cache_metadata(cache_file: Path) -> Optional[Dict]:
    """Load metadata for cache file.

    Returns:
        Metadata dict if exists, else None
    """
    meta_path = get_cache_metadata_path(cache_file)

    if not meta_path.exists():
        return None

    try:
        with open(meta_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.warning(f"Failed to load metadata: {e}")
        return None


def is_cache_valid(
    cache_file: Union[str, Path],
    source_files: Optional[List[Union[str, Path]]] = None,
    pipeline_version: str = PIPELINE_VERSION,
    check_metadata: bool = True
) -> bool:
    """Check if cache is valid (not stale).

    Validation steps:
    1. Cache file must exist
    2. If metadata exists:
       a. Pipeline version must match
       b. All source files must be OLDER than cache
    3. If no metadata: assume valid (backward compatibility)

    Args:
        cache_file: Path to cache file
        source_files: Optional list of source files to check mtime
        pipeline_version: Current pipeline version
        check_metadata: If False, only check file existence

    Returns:
        True if cache is valid, False if needs regeneration

    Example:
        >>> # Simple check
        >>> is_cache_valid('data/processed/features_all.nc')
        True

        >>> # Full check with sources
        >>> is_cache_valid(
        ...     'data/processed/features_all.nc',
        ...     source_files=['data/raw/Company_2024-11.dat'],
        ...     pipeline_version='2.0'
        ... )
        False  # Need to regenerate if version or data changed
    """
    cache_file = Path(cache_file)

    # Step 1: File existence check
    if not cache_file.exists():
        logger.debug(f"Cache invalid: {cache_file} does not exist")
        return False

    # Step 2: Skip metadata checks if disabled
    if not check_metadata:
        logger.debug(f"Cache valid: {cache_file} exists (metadata check disabled)")
        return True

    # Step 3: Load metadata
    metadata = load_cache_metadata(cache_file)

    if metadata is None:
        # No metadata file → assume valid (backward compatibility)
        logger.debug(f"Cache valid: {cache_file} exists, no metadata to check")
        return True

    # Step 4: Check pipeline version
    cached_version = metadata.get('pipeline_version')
    if cached_version != pipeline_version:
        logger.info(f"Cache invalid: Pipeline upgraded {cached_version} → {pipeline_version}")
        return False

    # Step 5: Check source file mtimes
    if source_files:
        cache_mtime = cache_file.stat().st_mtime

        for source in source_files:
            source_path = Path(source)
            if not source_path.exists():
                logger.warning(f"Source file missing: {source_path}")
                continue

            source_mtime = source_path.stat().st_mtime
            if source_mtime > cache_mtime:
                logger.info(f"Cache invalid: {source_path.name} is newer than cache")
                return False

    # All checks passed
    logger.debug(f"Cache valid: {cache_file}")
    return True


def invalidate_cache(cache_file: Union[str, Path]) -> None:
    """Delete cache file and its metadata.

    Args:
        cache_file: Path to cache file to delete
    """
    cache_file = Path(cache_file)
    meta_path = get_cache_metadata_path(cache_file)

    if cache_file.exists():
        cache_file.unlink()
        logger.info(f"Deleted cache: {cache_file}")

    if meta_path.exists():
        meta_path.unlink()
        logger.debug(f"Deleted metadata: {meta_path}")


# Example usage in cli.py
def example_usage():
    """
    Example: How to integrate into src/cli.py

    # Before (current code):
    if output_file.exists():
        df = load_dataframe(output_file)
        return df

    # After (with smart cache):
    from src.cache_utils import is_cache_valid, save_cache_metadata

    source_files = list(Path('data/raw').glob('Company*.dat'))

    if is_cache_valid(output_file, source_files=source_files):
        logger.info("⚡ Cache valid, loading...")
        df = load_dataframe(output_file)
        return df
    else:
        logger.info("♻️  Cache stale, regenerating...")
        df = engineer_features(data)
        save_dataframe(df, output_file)
        save_cache_metadata(output_file, source_files=source_files)
        return df
    """
    pass
