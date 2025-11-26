#!/usr/bin/env python3
"""
Pipeline Cache Manager with xarray
===================================
Expert-level caching system using xarray for intuitive coordinate-based data management.

Design Philosophy:
- Multi-dimensional coordinates for slicing/filtering
- Hash-based cache invalidation
- Lazy loading for memory efficiency
- Metadata tracking for reproducibility

Coordinate Structure:
    Dimensions:
        - company_id: Unique company identifier
        - scenario: Dataset variant (all, quantum, transportation)
        - model_type: Analysis type (H1, H2, H3)
        - cohort: Founding year cohort

    Coordinates:
        - sector: Industry sector
        - is_hardware: Hardware vs Software architecture
        - year_founded: Founding year
        - geographic_region: Location info

    Data Variables:
        - Raw: vagueness, employees, funding amounts
        - Derived: z-scored features, categorical encodings
        - Outcomes: early_funding_musd, growth indicators
        - Model: coefficients, predictions, residuals

Usage:
    from cache_manager import CacheManager

    cache = CacheManager()

    # Save step output
    cache.save_step('features', df, scenario='all')

    # Load if cache valid
    df = cache.load_step('features', scenario='all')

    # Access via xarray for advanced slicing
    ds = cache.to_xarray('features', scenario='all')
    hw_companies = ds.sel(is_hardware=True)
"""

import hashlib
import logging
import pickle
import json
from pathlib import Path
from typing import Optional, Dict, Any, List, Union
from datetime import datetime
import pandas as pd
import numpy as np
import xarray as xr

logger = logging.getLogger(__name__)


class CacheManager:
    """Manages pipeline caching with xarray coordinate structure."""

    # Pipeline step definitions
    STEPS = {
        'raw_data': {
            'description': 'Consolidated company snapshots',
            'inputs': ['data/raw/*.dat'],
            'outputs': ['company_id', 'description', 'employees', 'funding_rounds']
        },
        'features': {
            'description': 'Engineered features with vagueness scores',
            'inputs': ['raw_data'],
            'outputs': ['vagueness', 'is_hardware', 'employees_log', 'sector_fe']
        },
        'filtered': {
            'description': 'Filtered datasets by scenario',
            'inputs': ['features'],
            'outputs': ['dataset variants by filter criteria']
        },
        'models': {
            'description': 'Statistical model results',
            'inputs': ['filtered'],
            'outputs': ['h1_coefficients', 'h2_coefficients', 'predictions']
        },
        'plots': {
            'description': 'Generated figures',
            'inputs': ['models'],
            'outputs': ['F3a_interaction.png', 'fig3_H1_scatter.pdf']
        }
    }

    def __init__(self, cache_dir: str = "data/cache"):
        """Initialize cache manager.

        Args:
            cache_dir: Directory for cache storage
        """
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True, parents=True)

        # Create subdirectories for each step
        for step in self.STEPS:
            (self.cache_dir / step).mkdir(exist_ok=True, parents=True)

        # Metadata tracking
        self.metadata_file = self.cache_dir / "metadata.json"
        self.metadata = self._load_metadata()

    def _load_metadata(self) -> Dict:
        """Load cache metadata."""
        if self.metadata_file.exists():
            with open(self.metadata_file, 'r') as f:
                return json.load(f)
        return {}

    def _save_metadata(self):
        """Save cache metadata."""
        with open(self.metadata_file, 'w') as f:
            json.dump(self.metadata, f, indent=2, default=str)

    def _compute_hash(self, data: Union[pd.DataFrame, Dict, str]) -> str:
        """Compute hash for cache invalidation.

        Args:
            data: Data to hash (DataFrame, dict, or filepath)

        Returns:
            MD5 hash string
        """
        if isinstance(data, pd.DataFrame):
            # Hash DataFrame shape, columns, and sample of values
            hash_input = f"{data.shape}_{list(data.columns)}_{data.head().values.tobytes()}"
        elif isinstance(data, dict):
            hash_input = json.dumps(data, sort_keys=True)
        elif isinstance(data, (str, Path)):
            # Hash file modification time
            path = Path(data)
            if path.exists():
                hash_input = f"{path}_{path.stat().st_mtime}"
            else:
                hash_input = str(data)
        else:
            hash_input = str(data)

        return hashlib.md5(hash_input.encode()).hexdigest()

    def _get_cache_path(self, step: str, scenario: str = 'default', format: str = 'parquet') -> Path:
        """Get cache file path.

        Args:
            step: Pipeline step name
            scenario: Dataset scenario (all, quantum, transportation)
            format: File format (parquet, netcdf, pickle)

        Returns:
            Path to cache file
        """
        return self.cache_dir / step / f"{scenario}.{format}"

    def is_valid(self, step: str, scenario: str = 'default', input_hash: Optional[str] = None) -> bool:
        """Check if cache is valid for a step.

        Args:
            step: Pipeline step name
            scenario: Dataset scenario
            input_hash: Hash of input data for validation

        Returns:
            True if cache exists and is valid
        """
        cache_file = self._get_cache_path(step, scenario)

        if not cache_file.exists():
            logger.debug(f"Cache miss: {step}/{scenario} (file not found)")
            return False

        # Check metadata
        key = f"{step}_{scenario}"
        if key not in self.metadata:
            logger.debug(f"Cache miss: {step}/{scenario} (no metadata)")
            return False

        # Validate input hash if provided
        if input_hash is not None:
            cached_hash = self.metadata[key].get('input_hash')
            if cached_hash != input_hash:
                logger.debug(f"Cache invalid: {step}/{scenario} (hash mismatch)")
                return False

        logger.info(f"✓ Cache hit: {step}/{scenario}")
        return True

    def save_step(
        self,
        step: str,
        data: pd.DataFrame,
        scenario: str = 'default',
        input_hash: Optional[str] = None,
        extra_metadata: Optional[Dict] = None
    ):
        """Save pipeline step output to cache.

        Args:
            step: Pipeline step name
            data: DataFrame to cache
            scenario: Dataset scenario
            input_hash: Hash of input data for validation
            extra_metadata: Additional metadata to store
        """
        # Save as parquet (fast, compressed)
        cache_file = self._get_cache_path(step, scenario, 'parquet')
        data.to_parquet(cache_file, compression='zstd', index=False)

        # Update metadata
        key = f"{step}_{scenario}"
        self.metadata[key] = {
            'timestamp': datetime.now().isoformat(),
            'rows': len(data),
            'columns': list(data.columns),
            'input_hash': input_hash,
            'output_hash': self._compute_hash(data),
            'file': str(cache_file),
            **(extra_metadata or {})
        }
        self._save_metadata()

        logger.info(f"✓ Cached: {step}/{scenario} ({len(data):,} rows, {len(data.columns)} cols)")

    def load_step(self, step: str, scenario: str = 'default') -> Optional[pd.DataFrame]:
        """Load pipeline step output from cache.

        Args:
            step: Pipeline step name
            scenario: Dataset scenario

        Returns:
            Cached DataFrame or None if invalid
        """
        if not self.is_valid(step, scenario):
            return None

        cache_file = self._get_cache_path(step, scenario, 'parquet')
        df = pd.read_parquet(cache_file)

        logger.info(f"✓ Loaded from cache: {step}/{scenario} ({len(df):,} rows)")
        return df

    def to_xarray(
        self,
        step: str,
        scenario: str = 'default',
        index_coord: str = 'company_id'
    ) -> Optional[xr.Dataset]:
        """Convert cached DataFrame to xarray Dataset with expert coordinates.

        Args:
            step: Pipeline step name
            scenario: Dataset scenario
            index_coord: Column to use as primary dimension

        Returns:
            xarray Dataset with multi-dimensional coordinates
        """
        df = self.load_step(step, scenario)
        if df is None:
            return None

        # Ensure index coordinate exists
        if index_coord not in df.columns:
            logger.warning(f"Index coordinate '{index_coord}' not found, using integer index")
            df[index_coord] = range(len(df))

        # Identify categorical vs numeric columns
        categorical_cols = df.select_dtypes(include=['category', 'object']).columns.tolist()
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

        # Remove index_coord from both lists if present
        if index_coord in categorical_cols:
            categorical_cols.remove(index_coord)
        if index_coord in numeric_cols:
            numeric_cols.remove(index_coord)

        # Set index for conversion
        df_indexed = df.set_index(index_coord)

        # Convert to xarray Dataset
        ds = xr.Dataset.from_dataframe(df_indexed)

        # Add coordinate attributes for better semantics
        coordinate_metadata = {
            'is_hardware': {
                'long_name': 'Architecture Type',
                'description': 'Hardware (True) vs Software (False)',
                'units': 'boolean'
            },
            'founding_cohort': {
                'long_name': 'Founding Year Cohort',
                'description': 'Binned founding year for fixed effects',
                'units': 'category'
            },
            'sector_fe': {
                'long_name': 'Sector Fixed Effect',
                'description': 'Industry sector category',
                'units': 'category'
            },
            'vagueness': {
                'long_name': 'Strategic Vagueness Score',
                'description': 'V2 hybrid scorer (concrete + specificity)',
                'units': 'score (0-100)',
                'scorer': 'StrategicVaguenessScorerV2'
            },
            'z_vagueness': {
                'long_name': 'Standardized Vagueness',
                'description': 'Z-scored vagueness (mean=0, std=1)',
                'units': 'z-score'
            },
            'early_funding_musd': {
                'long_name': 'Early Stage Funding',
                'description': 'Series A or Early VC funding amount',
                'units': 'million USD'
            },
            'growth': {
                'long_name': 'Later Stage Success',
                'description': 'Reached Series B+ (binary)',
                'units': 'boolean'
            }
        }

        # Apply metadata to coordinates that exist
        for coord, attrs in coordinate_metadata.items():
            if coord in ds.data_vars:
                ds[coord].attrs.update(attrs)

        # Add dataset-level metadata
        ds.attrs.update({
            'pipeline_step': step,
            'scenario': scenario,
            'creation_time': datetime.now().isoformat(),
            'source': 'empirics_ent_strat_ops pipeline',
            'cache_manager_version': '1.0.0'
        })

        logger.info(f"✓ Converted to xarray: {step}/{scenario}")
        logger.info(f"  Dimensions: {dict(ds.dims)}")
        logger.info(f"  Coordinates: {list(ds.coords)}")
        logger.info(f"  Data variables: {len(ds.data_vars)}")

        return ds

    def save_xarray(self, step: str, dataset: xr.Dataset, scenario: str = 'default'):
        """Save xarray Dataset to cache.

        Args:
            step: Pipeline step name
            dataset: xarray Dataset to cache
            scenario: Dataset scenario
        """
        cache_file = self._get_cache_path(step, scenario, 'netcdf')

        # Save as NetCDF (preserves coordinates and metadata)
        dataset.to_netcdf(cache_file, engine='netcdf4')

        # Update metadata
        key = f"{step}_{scenario}_xarray"
        self.metadata[key] = {
            'timestamp': datetime.now().isoformat(),
            'dims': dict(dataset.dims),
            'coords': list(dataset.coords),
            'data_vars': list(dataset.data_vars),
            'file': str(cache_file)
        }
        self._save_metadata()

        logger.info(f"✓ Cached xarray: {step}/{scenario}")

    def load_xarray(self, step: str, scenario: str = 'default') -> Optional[xr.Dataset]:
        """Load xarray Dataset from cache.

        Args:
            step: Pipeline step name
            scenario: Dataset scenario

        Returns:
            xarray Dataset or None if not found
        """
        cache_file = self._get_cache_path(step, scenario, 'netcdf')

        if not cache_file.exists():
            logger.debug(f"xarray cache miss: {step}/{scenario}")
            return None

        ds = xr.open_dataset(cache_file)
        logger.info(f"✓ Loaded xarray from cache: {step}/{scenario}")
        return ds

    def clear_step(self, step: str, scenario: str = 'default'):
        """Clear cache for a specific step and scenario.

        Args:
            step: Pipeline step name
            scenario: Dataset scenario
        """
        for format in ['parquet', 'netcdf', 'pickle']:
            cache_file = self._get_cache_path(step, scenario, format)
            if cache_file.exists():
                cache_file.unlink()
                logger.info(f"✓ Cleared cache: {cache_file}")

        # Remove from metadata
        key = f"{step}_{scenario}"
        if key in self.metadata:
            del self.metadata[key]
            self._save_metadata()

    def clear_all(self):
        """Clear entire cache."""
        import shutil
        if self.cache_dir.exists():
            shutil.rmtree(self.cache_dir)
            self.cache_dir.mkdir(exist_ok=True, parents=True)
            self.metadata = {}
            logger.info("✓ Cleared entire cache")

    def summary(self) -> pd.DataFrame:
        """Get cache summary statistics.

        Returns:
            DataFrame with cache status for each step
        """
        summary_data = []

        for step in self.STEPS:
            for scenario in ['default', 'all', 'quantum', 'transportation']:
                key = f"{step}_{scenario}"
                if key in self.metadata:
                    meta = self.metadata[key]
                    summary_data.append({
                        'step': step,
                        'scenario': scenario,
                        'cached': True,
                        'timestamp': meta.get('timestamp', 'unknown'),
                        'rows': meta.get('rows', 0),
                        'columns': len(meta.get('columns', [])),
                        'file': Path(meta.get('file', '')).name
                    })

        if not summary_data:
            return pd.DataFrame(columns=['step', 'scenario', 'cached', 'timestamp', 'rows', 'columns', 'file'])

        return pd.DataFrame(summary_data).sort_values(['step', 'scenario'])


def demo_xarray_usage():
    """Demonstrate expert xarray coordinate usage."""
    print("=" * 80)
    print("XARRAY CACHE DEMO: Expert Coordinate Usage")
    print("=" * 80)

    cache = CacheManager()

    # Example: Load features as xarray
    ds = cache.to_xarray('features', scenario='all')

    if ds is not None:
        print("\n📊 Dataset Structure:")
        print(ds)

        print("\n🎯 Advanced Slicing Examples:")

        # 1. Select hardware companies only
        print("\n1. Hardware companies:")
        if 'is_hardware' in ds.data_vars:
            hw_companies = ds.where(ds.is_hardware == True, drop=True)
            print(f"   N = {hw_companies.dims.get('company_id', 0):,}")

        # 2. Select by founding cohort
        print("\n2. Companies founded 2015-18:")
        if 'founding_cohort' in ds.data_vars:
            cohort_2015 = ds.where(ds.founding_cohort == '2015-18', drop=True)
            print(f"   N = {cohort_2015.dims.get('company_id', 0):,}")

        # 3. High vagueness companies (top quartile)
        print("\n3. High vagueness (top 25%):")
        if 'vagueness' in ds.data_vars:
            q75 = ds.vagueness.quantile(0.75).values
            high_vague = ds.where(ds.vagueness >= q75, drop=True)
            print(f"   Threshold: {q75:.1f}")
            print(f"   N = {high_vague.dims.get('company_id', 0):,}")

        # 4. Grouped statistics
        print("\n4. Mean vagueness by hardware type:")
        if 'vagueness' in ds.data_vars and 'is_hardware' in ds.data_vars:
            for hw in [True, False]:
                subset = ds.where(ds.is_hardware == hw, drop=True)
                mean_vague = subset.vagueness.mean().values
                print(f"   {'Hardware' if hw else 'Software'}: {mean_vague:.2f}")

    print("\n" + "=" * 80)


if __name__ == '__main__':
    # Run demo
    demo_xarray_usage()

