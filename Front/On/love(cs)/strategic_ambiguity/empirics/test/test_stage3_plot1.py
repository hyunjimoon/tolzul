"""
Unit tests for Stage 3 (PLOT1): Variable distribution visualization

Tests cover:
- Distribution plot creation
- Plot file saving
- Plot content validation
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import tempfile

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from modules import plots


class TestStage3Plot1:
    """Test suite for PLOT1 stage (distribution visualization)"""

    @pytest.fixture
    def sample_processed_df(self):
        """Create sample processed DataFrame with all required variables"""
        np.random.seed(42)
        return pd.DataFrame({
            'early_funding_musd': np.random.exponential(3, 1000),
            'growth': np.random.choice([0, 1], 1000, p=[0.7, 0.3]),
            'z_vagueness': np.random.normal(0, 1, 1000),
            'is_hardware': np.random.choice([0, 1], 1000, p=[0.6, 0.4]),
            'valuation_stepup': np.random.lognormal(0, 0.5, 1000),
        })

    def test_plot_variable_distributions_creates_file(self, sample_processed_df):
        """Test that plot file is created"""
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / 'test_distributions.png'

            plots.plot_variable_distributions(
                sample_processed_df,
                output_path=output_path
            )

            assert output_path.exists()
            assert output_path.stat().st_size > 0  # File not empty

    def test_plot_handles_missing_variables(self):
        """Test that plotting handles missing optional variables"""
        df_minimal = pd.DataFrame({
            'early_funding_musd': np.random.exponential(3, 100),
            'growth': np.random.choice([0, 1], 100),
            'z_vagueness': np.random.normal(0, 1, 100),
        })

        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / 'test_distributions.png'

            # Should not crash even with missing optional variables
            try:
                plots.plot_variable_distributions(
                    df_minimal,
                    output_path=output_path
                )
                success = True
            except Exception as e:
                success = False
                print(f"Failed: {e}")

            assert success

    def test_plot_with_empty_dataframe(self):
        """Test handling of empty DataFrame"""
        df_empty = pd.DataFrame()

        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / 'test_distributions.png'

            # Should handle gracefully
            with pytest.raises(Exception):
                plots.plot_variable_distributions(
                    df_empty,
                    output_path=output_path
                )


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
