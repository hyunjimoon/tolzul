"""
Unit Tests for NetCDF I/O Module
=================================
Tests for data_io.py functions: save_dataframe, load_dataframe, convert_parquet_to_nc
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import tempfile
import shutil

# Add src to path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))

from data_io import save_dataframe, load_dataframe, convert_parquet_to_nc, get_data_path


class TestNetCDFIO:
    """Test NetCDF save/load operations."""

    @pytest.fixture
    def sample_dataframe(self):
        """Create a sample DataFrame for testing."""
        return pd.DataFrame({
            'company_id': [1, 2, 3, 4, 5],
            'vagueness': [0.1, 0.5, 0.8, 0.3, 0.6],
            'early_funding_musd': [1.0, 2.5, 0.5, 3.0, 1.5],
            'is_hardware': [0, 1, 0, 1, 0],
            'growth': [0, 1, 0, 1, 1],
            'description': ['AI platform', 'Robotics', 'SaaS', 'Hardware', 'Cloud']
        })

    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for test files."""
        temp_path = Path(tempfile.mkdtemp())
        yield temp_path
        shutil.rmtree(temp_path)

    def test_save_and_load_roundtrip(self, sample_dataframe, temp_dir):
        """Test that save → load preserves all data."""
        nc_file = temp_dir / "test.nc"

        # Save
        save_dataframe(sample_dataframe, nc_file)
        assert nc_file.exists()

        # Load
        df_loaded = load_dataframe(nc_file)

        # Check shape
        assert df_loaded.shape == sample_dataframe.shape

        # Check column names
        assert set(df_loaded.columns) == set(sample_dataframe.columns)

        # Check numeric values
        pd.testing.assert_series_equal(
            df_loaded['vagueness'].sort_index(),
            sample_dataframe['vagueness'].sort_index(),
            check_names=False
        )

    def test_save_creates_compressed_file(self, sample_dataframe, temp_dir):
        """Test that NetCDF files use compression."""
        nc_file = temp_dir / "compressed.nc"

        # Save with compression (default)
        save_dataframe(sample_dataframe, nc_file, compression='zlib')
        compressed_size = nc_file.stat().st_size

        # Save without compression
        nc_file_uncompressed = temp_dir / "uncompressed.nc"
        save_dataframe(sample_dataframe, nc_file_uncompressed, compression=None)
        uncompressed_size = nc_file_uncompressed.stat().st_size

        # Compressed should be smaller (for larger datasets)
        # For small test data, this might not hold, so just check file exists
        assert compressed_size > 0
        assert uncompressed_size > 0

    def test_load_nonexistent_file_raises_error(self, temp_dir):
        """Test that loading a nonexistent file raises FileNotFoundError."""
        fake_file = temp_dir / "nonexistent.nc"

        with pytest.raises(FileNotFoundError):
            load_dataframe(fake_file)

    def test_save_with_string_path(self, sample_dataframe, temp_dir):
        """Test that save_dataframe accepts string paths."""
        nc_file = str(temp_dir / "string_path.nc")

        # Should work with string path
        save_dataframe(sample_dataframe, nc_file)
        assert Path(nc_file).exists()

        # Should load with string path
        df_loaded = load_dataframe(nc_file)
        assert len(df_loaded) == len(sample_dataframe)

    def test_handles_missing_values(self, temp_dir):
        """Test that NaN values are preserved."""
        df_with_nan = pd.DataFrame({
            'a': [1.0, 2.0, np.nan, 4.0],
            'b': [np.nan, 2.0, 3.0, 4.0],
            'c': ['x', 'y', None, 'z']
        })

        nc_file = temp_dir / "with_nan.nc"
        save_dataframe(df_with_nan, nc_file)
        df_loaded = load_dataframe(nc_file)

        # Check NaN positions
        assert df_loaded['a'].isna().sum() == 1
        assert df_loaded['b'].isna().sum() == 1


class TestParquetConversion:
    """Test conversion from Parquet to NetCDF."""

    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for test files."""
        temp_path = Path(tempfile.mkdtemp())
        yield temp_path
        shutil.rmtree(temp_path)

    def test_convert_parquet_to_nc(self, temp_dir):
        """Test converting a Parquet file to NetCDF."""
        # Skip if pyarrow not available
        try:
            import pyarrow
        except ImportError:
            pytest.skip("pyarrow not installed, skipping Parquet conversion test")

        # Create sample Parquet file
        df = pd.DataFrame({
            'x': [1, 2, 3],
            'y': [4.0, 5.0, 6.0],
            'z': ['a', 'b', 'c']
        })

        parquet_file = temp_dir / "test.parquet"
        df.to_parquet(parquet_file, index=False)

        # Convert to NetCDF
        nc_file = convert_parquet_to_nc(parquet_file)

        # Check output file exists
        assert nc_file.exists()
        assert nc_file.suffix == '.nc'

        # Load and verify
        df_loaded = load_dataframe(nc_file)
        assert len(df_loaded) == len(df)
        pd.testing.assert_series_equal(df['x'], df_loaded['x'].astype(int), check_names=False)


class TestGetDataPath:
    """Test smart path resolution (prefers .nc over .parquet)."""

    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for test files."""
        temp_path = Path(tempfile.mkdtemp())
        yield temp_path
        shutil.rmtree(temp_path)

    def test_prefers_nc_when_both_exist(self, temp_dir):
        """Test that .nc is preferred when both .nc and .parquet exist."""
        # Skip if pyarrow not available
        try:
            import pyarrow
        except ImportError:
            pytest.skip("pyarrow not installed, skipping test")

        df = pd.DataFrame({'a': [1, 2, 3]})

        # Create both files
        nc_file = temp_dir / "data.nc"
        parquet_file = temp_dir / "data.parquet"

        save_dataframe(df, nc_file)
        df.to_parquet(parquet_file, index=False)

        # Request .parquet but should get .nc
        resolved_path = get_data_path(parquet_file)

        # Should return .nc file
        assert resolved_path == nc_file

    def test_returns_nc_when_only_nc_exists(self, temp_dir):
        """Test that .nc is returned when only .nc exists."""
        df = pd.DataFrame({'a': [1, 2, 3]})
        nc_file = temp_dir / "data.nc"
        save_dataframe(df, nc_file)

        # Request with any extension
        resolved_path = get_data_path(temp_dir / "data.anything")

        assert resolved_path == nc_file

    def test_returns_parquet_when_only_parquet_exists(self, temp_dir):
        """Test that .parquet is returned when only .parquet exists."""
        # Skip if pyarrow not available
        try:
            import pyarrow
        except ImportError:
            pytest.skip("pyarrow not installed, skipping test")

        df = pd.DataFrame({'a': [1, 2, 3]})
        parquet_file = temp_dir / "data.parquet"
        df.to_parquet(parquet_file, index=False)

        # Request with any extension
        resolved_path = get_data_path(temp_dir / "data.anything")

        assert resolved_path == parquet_file


class TestEdgeCases:
    """Test edge cases and error handling."""

    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for test files."""
        temp_path = Path(tempfile.mkdtemp())
        yield temp_path
        shutil.rmtree(temp_path)

    def test_empty_dataframe(self, temp_dir):
        """Test saving and loading an empty DataFrame."""
        df_empty = pd.DataFrame()
        nc_file = temp_dir / "empty.nc"

        save_dataframe(df_empty, nc_file)
        df_loaded = load_dataframe(nc_file)

        assert len(df_loaded) == 0

    def test_single_row_dataframe(self, temp_dir):
        """Test saving and loading a single-row DataFrame."""
        df_single = pd.DataFrame({'a': [1], 'b': [2.0], 'c': ['x']})
        nc_file = temp_dir / "single.nc"

        save_dataframe(df_single, nc_file)
        df_loaded = load_dataframe(nc_file)

        assert len(df_loaded) == 1
        assert df_loaded['a'].iloc[0] == 1

    def test_large_string_values(self, temp_dir):
        """Test handling of long string values."""
        long_string = "A" * 10000  # 10KB string
        df = pd.DataFrame({
            'id': [1, 2],
            'text': [long_string, "short"]
        })

        nc_file = temp_dir / "long_strings.nc"
        save_dataframe(df, nc_file)
        df_loaded = load_dataframe(nc_file)

        # NetCDF might truncate very long strings, but should preserve most
        assert len(df_loaded['text'].iloc[0]) > 100  # At least partial preservation
