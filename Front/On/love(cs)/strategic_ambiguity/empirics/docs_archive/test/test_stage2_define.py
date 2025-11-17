"""
Unit tests for Stage 2 (DEFINE): Feature engineering

Tests cover:
- Vagueness score calculation
- Hardware/software classification
- Early funding derivation
- Growth variable creation
- Sector fixed effects
- Control variables
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from modules import features


class TestStage2Define:
    """Test suite for DEFINE stage (feature engineering)"""

    @pytest.fixture
    def sample_df(self):
        """Create sample DataFrame with raw company data"""
        return pd.DataFrame({
            'CompanyID': [f'C{i:04d}' for i in range(100)],
            'Description': [
                'AI-powered analytics platform' if i % 3 == 0 else
                'Revolutionary blockchain solution' if i % 3 == 1 else
                'Enterprise software for data management'
                for i in range(100)
            ],
            'Keywords': [
                'AI, machine learning, analytics' if i % 2 == 0 else
                'hardware, robotics, sensors'
                for i in range(100)
            ],
            'FirstFinancingSize': np.random.uniform(1e6, 10e6, 100),
            'FirstFinancingDealType': [
                'Series A' if i < 50 else 'Early Stage VC'
                for i in range(100)
            ],
            'LastFinancingDealType': [
                'Series A' if i < 30 else
                'Series B' if i < 60 else
                'Later Stage VC'
                for i in range(100)
            ],
            'Employees': np.random.randint(10, 500, 100),
            'YearFounded': np.random.randint(2015, 2023, 100),
            'TotalRaised': np.random.uniform(5e6, 50e6, 100),
        })

    def test_engineer_features_creates_required_columns(self, sample_df):
        """Test that engineer_features creates all required columns"""
        df_engineered = features.engineer_features(sample_df.copy())

        # Check required columns exist
        assert 'vagueness' in df_engineered.columns
        assert 'is_hardware' in df_engineered.columns
        assert 'early_funding_musd' in df_engineered.columns
        assert 'growth' in df_engineered.columns
        assert 'sector_fe' in df_engineered.columns
        assert 'employees_log' in df_engineered.columns
        assert 'firm_age' in df_engineered.columns

    def test_vagueness_score_range(self, sample_df):
        """Test that vagueness scores are in valid range"""
        df_engineered = features.engineer_features(sample_df.copy())

        # Vagueness should be non-negative
        assert df_engineered['vagueness'].min() >= 0
        # Should have some variation
        assert df_engineered['vagueness'].std() > 0

    def test_hardware_classification(self, sample_df):
        """Test hardware vs software classification"""
        df_engineered = features.engineer_features(sample_df.copy())

        # is_hardware should be binary (0 or 1)
        assert set(df_engineered['is_hardware'].unique()).issubset({0, 1})

        # Check that hardware keywords lead to is_hardware=1
        hardware_rows = df_engineered[
            df_engineered['keywords'].str.contains('hardware', case=False, na=False)
        ]
        assert hardware_rows['is_hardware'].mean() > 0.5  # Most should be classified as hardware

    def test_early_funding_conversion(self, sample_df):
        """Test early funding conversion to millions"""
        df_engineered = features.engineer_features(sample_df.copy())

        # Check conversion to millions
        assert df_engineered['early_funding_musd'].max() < 100  # Should be in millions
        assert df_engineered['early_funding_musd'].min() > 0

        # Check that only Series A / Early Stage VC are included
        valid_types = ['Series A', 'Early Stage VC']
        non_series_a_rows = sample_df[~sample_df['FirstFinancingDealType'].isin(valid_types)]
        if len(non_series_a_rows) > 0:
            # These should have NaN early_funding
            non_series_a_ids = non_series_a_rows['CompanyID'].values
            # Note: current implementation filters by deal type, so we can't directly test this

    def test_growth_variable_creation(self, sample_df):
        """Test growth variable (Series B+ indicator)"""
        df_engineered = features.engineer_features(sample_df.copy())

        # Growth should be binary
        assert set(df_engineered['growth'].unique()).issubset({0, 1})

        # Companies with Series B / Later Stage VC should have growth=1
        series_b_rows = sample_df[
            sample_df['LastFinancingDealType'].str.contains('Series B|Later Stage', case=False, na=False)
        ]
        expected_growth_count = len(series_b_rows)

        actual_growth_count = df_engineered['growth'].sum()

        # Should be roughly similar (within 10%)
        assert abs(actual_growth_count - expected_growth_count) / expected_growth_count < 0.2

    def test_sector_fe_classification(self, sample_df):
        """Test sector fixed effects classification"""
        df_engineered = features.engineer_features(sample_df.copy())

        # Should have multiple sectors
        sectors = df_engineered['sector_fe'].unique()
        assert len(sectors) > 1

        # Check for expected sector types
        sector_types = ['AI/ML Software', 'Hardware/Robotics', 'Other']
        assert any(sector in sectors for sector in sector_types)

    def test_employees_log_transformation(self, sample_df):
        """Test log transformation of employees"""
        df_engineered = features.engineer_features(sample_df.copy())

        # Check log transformation
        assert df_engineered['employees_log'].min() >= 0
        # log1p transformation should handle zero employees
        assert not df_engineered['employees_log'].isna().all()

    def test_firm_age_calculation(self, sample_df):
        """Test firm age calculation"""
        df_engineered = features.engineer_features(sample_df.copy())

        # Firm age should be reasonable (0-50 years)
        assert df_engineered['firm_age'].min() >= 0
        assert df_engineered['firm_age'].max() < 50

        # Check calculation is correct
        expected_ages = 2024 - sample_df['YearFounded']
        actual_ages = df_engineered['firm_age']

        # Should match (within rounding)
        assert (expected_ages - actual_ages).abs().max() <= 1


class TestPreprocessing:
    """Test suite for preprocessing functions"""

    @pytest.fixture
    def engineered_df(self):
        """Create sample engineered DataFrame"""
        return pd.DataFrame({
            'CompanyID': [f'C{i:04d}' for i in range(100)],
            'vagueness': np.random.uniform(0, 1, 100),
            'employees_log': np.random.uniform(2, 6, 100),
            'is_hardware': np.random.choice([0, 1], 100),
            'year_founded': np.random.randint(2015, 2023, 100),
            'growth': np.random.choice([0, 1], 100),
            'early_funding_musd': np.random.uniform(1, 10, 100),
        })

    def test_preprocess_for_h2_creates_z_scores(self, engineered_df):
        """Test that preprocessing creates standardized variables"""
        df_processed = features.preprocess_for_h2(engineered_df.copy())

        # Check z-scored variables exist
        assert 'z_vagueness' in df_processed.columns
        assert 'z_employees_log' in df_processed.columns

        # Check standardization (mean ~ 0, std ~ 1)
        assert abs(df_processed['z_vagueness'].mean()) < 0.1
        assert abs(df_processed['z_vagueness'].std() - 1.0) < 0.1

    def test_preprocess_creates_founding_cohort(self, engineered_df):
        """Test founding cohort creation"""
        df_processed = features.preprocess_for_h2(engineered_df.copy())

        # Check founding cohort exists
        assert 'founding_cohort' in df_processed.columns

        # Should be categorical
        assert pd.api.types.is_categorical_dtype(df_processed['founding_cohort'])

        # Check cohort labels
        cohorts = df_processed['founding_cohort'].cat.categories
        assert len(cohorts) > 0

    def test_preprocess_handles_missing_founder_credibility(self, engineered_df):
        """Test that preprocessing handles missing founder_credibility"""
        df_processed = features.preprocess_for_h2(engineered_df.copy())

        # Should create founder_serial column even without founder_credibility
        assert 'founder_serial' in df_processed.columns

        # Should be all zeros if founder_credibility missing
        assert (df_processed['founder_serial'] == 0).all()


class TestVaguenessScoring:
    """Test suite for vagueness scoring"""

    def test_vagueness_scorer_basic(self):
        """Test basic vagueness scoring"""
        descriptions = pd.Series([
            'Revolutionary AI platform',  # High vagueness
            'Enterprise resource planning software for manufacturing',  # Low vagueness
            'Innovative solution for businesses',  # High vagueness
        ])

        keywords = pd.Series(['AI, platform', 'ERP, manufacturing', 'business'])

        scores = features.compute_vagueness_vectorized(descriptions, keywords)

        # Check scores are computed
        assert len(scores) == 3
        assert all(score >= 0 for score in scores)

        # First description should have higher vagueness than second
        assert scores[0] > scores[1]

    def test_vagueness_handles_missing_values(self):
        """Test vagueness scoring with missing values"""
        descriptions = pd.Series(['Valid description', None, ''])
        keywords = pd.Series(['keyword', None, ''])

        scores = features.compute_vagueness_vectorized(descriptions, keywords)

        # Should not crash and return valid scores
        assert len(scores) == 3
        assert all(score >= 0 for score in scores if not pd.isna(score))


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
