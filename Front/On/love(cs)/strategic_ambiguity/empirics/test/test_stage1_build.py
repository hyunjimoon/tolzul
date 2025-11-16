"""
Unit tests for Stage 1 (BUILD): Data loading and consolidation

Tests cover:
- Loading .dat files
- Parquet caching functionality
- Selective year loading
- Data validation
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import tempfile
import shutil

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from modules import features


class TestStage1Build:
    """Test suite for BUILD stage (data loading and consolidation)"""

    @pytest.fixture
    def mock_data_dir(self):
        """Create a temporary directory with mock .dat files"""
        temp_dir = tempfile.mkdtemp()
        data_dir = Path(temp_dir) / 'raw'
        data_dir.mkdir(parents=True)

        # Create mock Company*.dat files
        for year in [2022, 2023, 2024]:
            for month in ['01', '06']:
                filename = f'Company{year}{month}01.dat'
                filepath = data_dir / filename

                # Create mock data
                mock_df = pd.DataFrame({
                    'CompanyID': [f'C{year}{month}{i:04d}' for i in range(100)],
                    'Description': [f'Test company {i}' for i in range(100)],
                    'Keywords': ['AI, Machine Learning'] * 100,
                    'FirstFinancingSize': np.random.uniform(1e6, 10e6, 100),
                    'FirstFinancingDealType': ['Series A'] * 100,
                    'LastFinancingDealType': ['Series A'] * 50 + ['Series B'] * 50,
                    'Employees': np.random.randint(10, 500, 100),
                    'YearFounded': [2020] * 100,
                    'TotalRaised': np.random.uniform(5e6, 50e6, 100),
                })

                # Save as pipe-delimited
                mock_df.to_csv(filepath, sep='|', index=False)

        yield data_dir

        # Cleanup
        shutil.rmtree(temp_dir)

    def test_consolidate_basic_loading(self, mock_data_dir):
        """Test basic data loading without caching"""
        df = features.consolidate_company_snapshots(
            data_dir=mock_data_dir,
            use_cache=False,
            save_parquet=False
        )

        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0
        assert 'CompanyID' in df.columns or 'company_id' in df.columns
        assert 'snapshot_date' in df.columns

    def test_consolidate_with_caching(self, mock_data_dir):
        """Test parquet caching saves and loads correctly"""
        # First call: should create cache
        df1 = features.consolidate_company_snapshots(
            data_dir=mock_data_dir,
            use_cache=True,
            save_parquet=True
        )

        # Check cache was created
        cache_path = mock_data_dir.parent / 'processed' / 'consolidated_companies.parquet'
        assert cache_path.exists() or cache_path.with_suffix('.pkl').exists()

        # Second call: should load from cache (faster)
        df2 = features.consolidate_company_snapshots(
            data_dir=mock_data_dir,
            use_cache=True,
            save_parquet=True
        )

        # Data should be identical
        assert len(df1) == len(df2)
        assert df1.columns.tolist() == df2.columns.tolist()

    def test_selective_year_loading(self, mock_data_dir):
        """Test loading only specific years"""
        # Load only 2022 and 2024
        df_selective = features.consolidate_company_snapshots(
            data_dir=mock_data_dir,
            use_cache=False,
            save_parquet=False,
            years=[2022, 2024]
        )

        # Load all years
        df_all = features.consolidate_company_snapshots(
            data_dir=mock_data_dir,
            use_cache=False,
            save_parquet=False
        )

        # Selective should have fewer rows
        assert len(df_selective) < len(df_all)

        # Check years in selective dataset
        df_selective['year'] = pd.to_datetime(df_selective['snapshot_date']).dt.year
        unique_years = df_selective['year'].unique()
        assert all(year in [2022, 2024] for year in unique_years)

    def test_data_validation(self, mock_data_dir):
        """Test that loaded data has expected structure"""
        df = features.consolidate_company_snapshots(
            data_dir=mock_data_dir,
            use_cache=False,
            save_parquet=False
        )

        # Required columns
        id_col = 'CompanyID' if 'CompanyID' in df.columns else 'company_id'
        assert id_col in df.columns
        assert 'snapshot_date' in df.columns

        # Check data types
        assert pd.api.types.is_datetime64_any_dtype(df['snapshot_date'])

        # Check no all-null columns
        for col in df.columns:
            assert df[col].notna().any(), f"Column {col} is all NaN"

    def test_empty_directory(self):
        """Test handling of empty data directory"""
        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = Path(temp_dir) / 'raw'
            data_dir.mkdir(parents=True)

            # Should handle gracefully (no crash)
            with pytest.raises(Exception):
                features.consolidate_company_snapshots(
                    data_dir=data_dir,
                    use_cache=False,
                    save_parquet=False
                )

    def test_cache_filename_with_years(self, mock_data_dir):
        """Test that year-specific cache files are created"""
        df = features.consolidate_company_snapshots(
            data_dir=mock_data_dir,
            use_cache=True,
            save_parquet=True,
            years=[2022, 2024]
        )

        # Check for year-specific cache file
        processed_dir = mock_data_dir.parent / 'processed'
        cache_files = list(processed_dir.glob('consolidated_companies_2022_2024.*'))

        assert len(cache_files) > 0, "Year-specific cache file not created"


class TestQuantumFiltering:
    """Test suite for quantum company filtering"""

    @pytest.fixture
    def sample_df(self):
        """Create sample DataFrame for testing"""
        return pd.DataFrame({
            'CompanyID': ['C001', 'C002', 'C003', 'C004', 'C005'],
            'Description': [
                'Quantum computing platform for enterprise',
                'AI software for healthcare',
                'Quantum sensor technology',
                'Cloud infrastructure provider',
                'Quantum cryptography solutions'
            ],
            'Keywords': [
                'quantum, computing, enterprise',
                'AI, healthcare, software',
                'quantum, sensor, hardware',
                'cloud, infrastructure',
                'quantum, cryptography, security'
            ]
        })

    def test_quantum_filtering_description(self, sample_df):
        """Test quantum filtering based on description"""
        df_quantum = features.filter_quantum_companies(sample_df)

        # Should find 3 quantum companies (C001, C003, C005)
        assert len(df_quantum) == 3
        assert 'C001' in df_quantum['CompanyID'].values
        assert 'C003' in df_quantum['CompanyID'].values
        assert 'C005' in df_quantum['CompanyID'].values

    def test_quantum_filtering_empty(self):
        """Test quantum filtering with no quantum companies"""
        df_non_quantum = pd.DataFrame({
            'CompanyID': ['C001', 'C002'],
            'Description': ['Software company', 'Hardware manufacturer'],
            'Keywords': ['software, cloud', 'hardware, electronics']
        })

        df_quantum = features.filter_quantum_companies(df_non_quantum)

        assert len(df_quantum) == 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
