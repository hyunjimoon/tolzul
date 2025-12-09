"""
Unit tests for Stage 4 (TEST): Hypothesis testing

Tests cover:
- H1: Early Funding ~ Vagueness
- H2: Growth ~ Vagueness × Hardware
- Model convergence
- Result validation
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from modules import models


class TestStage4Test:
    """Test suite for TEST stage (hypothesis testing)"""

    @pytest.fixture
    def sample_analysis_df(self):
        """Create sample DataFrame for hypothesis testing"""
        np.random.seed(42)
        n = 500

        # Create realistic data with expected relationships
        z_vagueness = np.random.normal(0, 1, n)
        is_hardware = np.random.choice([0, 1], n, p=[0.7, 0.3])

        # Early funding: negatively correlated with vagueness
        early_funding_musd = np.exp(2 - 0.3 * z_vagueness + np.random.normal(0, 0.5, n))

        # Growth: positively correlated with vagueness (for software)
        logit_growth = -2 + 0.5 * z_vagueness - 0.3 * is_hardware + np.random.normal(0, 1, n)
        growth = (np.random.random(n) < 1 / (1 + np.exp(-logit_growth))).astype(int)

        return pd.DataFrame({
            'CompanyID': [f'C{i:04d}' for i in range(n)],
            'z_vagueness': z_vagueness,
            'is_hardware': is_hardware,
            'early_funding_musd': early_funding_musd,
            'growth': growth,
            'z_employees_log': np.random.normal(4, 1, n),
            'sector_fe': np.random.choice(
                ['AI/ML Software', 'Hardware/Robotics', 'FinTech', 'Other'],
                n
            ),
            'founding_cohort': pd.Categorical(
                np.random.choice(['2015-18', '2019-20', '2021', '2022+'], n)
            ),
        })

    def test_h1_early_funding_runs(self, sample_analysis_df):
        """Test that H1 model runs without errors"""
        result = models.test_h1_early_funding(sample_analysis_df)

        # Check result object
        assert result is not None
        assert hasattr(result, 'params')
        assert hasattr(result, 'pvalues')

    def test_h1_has_vagueness_coefficient(self, sample_analysis_df):
        """Test that H1 includes vagueness coefficient"""
        result = models.test_h1_early_funding(sample_analysis_df)

        # Check that z_vagueness is in the model
        assert 'z_vagueness' in result.params.index

        # Get coefficient and p-value
        beta = result.params['z_vagueness']
        pval = result.pvalues['z_vagueness']

        # Should have reasonable values
        assert not np.isnan(beta)
        assert not np.isnan(pval)
        assert 0 <= pval <= 1

    def test_h2_growth_runs(self, sample_analysis_df):
        """Test that H2 model runs without errors"""
        result = models.test_h2_main_growth(sample_analysis_df)

        # Check result object
        assert result is not None
        assert hasattr(result, 'params')
        assert hasattr(result, 'pvalues')

    def test_h2_has_vagueness_and_interaction(self, sample_analysis_df):
        """Test that H2 includes vagueness and interaction terms"""
        result = models.test_h2_main_growth(sample_analysis_df)

        # Check for vagueness main effect
        assert 'z_vagueness' in result.params.index

        # Check for interaction (may be named differently depending on statsmodels version)
        param_names = [str(p).lower() for p in result.params.index]
        has_interaction = any('vagueness' in p and 'hardware' in p for p in param_names)

        assert has_interaction, "Interaction term not found in model"

    def test_h1_with_minimal_controls(self, sample_analysis_df):
        """Test H1 with minimal controls"""
        # Simplified formula without all controls
        result = models.test_h1_early_funding(
            sample_analysis_df,
            formula="early_funding_musd ~ z_vagueness"
        )

        assert result is not None
        assert 'z_vagueness' in result.params.index

    def test_h2_with_minimal_controls(self, sample_analysis_df):
        """Test H2 with minimal controls"""
        # Simplified formula
        result = models.test_h2_main_growth(
            sample_analysis_df,
            formula="growth ~ z_vagueness * is_hardware"
        )

        assert result is not None
        assert 'z_vagueness' in result.params.index

    def test_models_handle_missing_data(self, sample_analysis_df):
        """Test that models handle missing data appropriately"""
        # Introduce some missing values
        df_missing = sample_analysis_df.copy()
        df_missing.loc[0:10, 'z_vagueness'] = np.nan
        df_missing.loc[11:20, 'early_funding_musd'] = np.nan

        # H1 should still run (drops missing)
        result_h1 = models.test_h1_early_funding(df_missing)
        assert result_h1 is not None

        # H2 should still run
        result_h2 = models.test_h2_main_growth(df_missing)
        assert result_h2 is not None

    def test_convergence_with_small_sample(self):
        """Test model behavior with very small sample"""
        np.random.seed(42)
        n = 50  # Small sample

        df_small = pd.DataFrame({
            'z_vagueness': np.random.normal(0, 1, n),
            'is_hardware': np.random.choice([0, 1], n),
            'early_funding_musd': np.random.exponential(3, n),
            'growth': np.random.choice([0, 1], n),
            'z_employees_log': np.random.normal(4, 1, n),
            'sector_fe': ['AI/ML Software'] * n,  # Single sector to avoid perfect separation
            'founding_cohort': pd.Categorical(['2019-20'] * n),
        })

        # Should handle small sample (may use regularization)
        try:
            result_h1 = models.test_h1_early_funding(
                df_small,
                formula="early_funding_musd ~ z_vagueness"
            )
            success_h1 = True
        except:
            success_h1 = False

        try:
            result_h2 = models.test_h2_main_growth(
                df_small,
                formula="growth ~ z_vagueness"
            )
            success_h2 = True
        except:
            success_h2 = False

        # At least one should succeed
        assert success_h1 or success_h2


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
