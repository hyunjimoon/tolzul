"""
Data Quality Tests for Paper Generation
========================================
Ensures that input data meets quality standards before running analyses.
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path

# Add src to path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))

from data_io import load_dataframe


@pytest.fixture
def analysis_data():
    """Load the main analysis dataset."""
    data_path = Path('data/processed/features_engineered.nc')

    if not data_path.exists():
        # Try .parquet as fallback
        data_path = Path('data/processed/features_engineered.parquet')

    if not data_path.exists():
        pytest.skip(f"Analysis data not found. Run: make data")

    return load_dataframe(data_path)


class TestSampleSize:
    """Test that sample sizes are sufficient for statistical analysis."""

    def test_minimum_sample_size(self, analysis_data):
        """Minimum 30 observations for OLS regression (rule of thumb)."""
        n = len(analysis_data)
        assert n >= 30, f"Sample too small for valid inference: {n} < 30"

    def test_h2_balanced_classes(self, analysis_data):
        """H2 (logit) requires balanced outcome classes."""
        if 'growth' not in analysis_data.columns:
            pytest.skip("'growth' column not found")

        growth_counts = analysis_data['growth'].value_counts()
        minority_class = growth_counts.min()
        majority_class = growth_counts.max()

        # At least 10 observations in minority class
        assert minority_class >= 10, \
            f"Minority class too small: {minority_class} < 10"

        # Not too imbalanced (max 10:1 ratio)
        imbalance_ratio = majority_class / minority_class
        assert imbalance_ratio <= 10, \
            f"Classes too imbalanced: {imbalance_ratio:.1f}:1 ratio"


class TestMissingValues:
    """Test that key variables have sufficient non-missing data."""

    def test_vagueness_completeness(self, analysis_data):
        """Vagueness scores should be present for all companies."""
        if 'vagueness' not in analysis_data.columns:
            pytest.skip("'vagueness' column not found")

        missing_pct = analysis_data['vagueness'].isna().sum() / len(analysis_data) * 100

        # Allow up to 5% missing
        assert missing_pct < 5, \
            f"Too many missing vagueness scores: {missing_pct:.1f}%"

    def test_early_funding_completeness(self, analysis_data):
        """Early funding data (H1 outcome) should be mostly complete."""
        if 'early_funding_musd' not in analysis_data.columns:
            pytest.skip("'early_funding_musd' column not found")

        missing_pct = analysis_data['early_funding_musd'].isna().sum() / len(analysis_data) * 100

        # Allow up to 20% missing (some companies may not raise)
        assert missing_pct < 20, \
            f"Too many missing early funding values: {missing_pct:.1f}%"

    def test_growth_completeness(self, analysis_data):
        """Growth indicator (H2 outcome) should be complete."""
        if 'growth' not in analysis_data.columns:
            pytest.skip("'growth' column not found")

        missing_pct = analysis_data['growth'].isna().sum() / len(analysis_data) * 100

        # Growth should be binary, very few missing
        assert missing_pct < 5, \
            f"Too many missing growth values: {missing_pct:.1f}%"


class TestVariableRanges:
    """Test that variables are within expected ranges."""

    def test_vagueness_range(self, analysis_data):
        """Vagueness should be in [0, 100] range."""
        if 'vagueness' not in analysis_data.columns:
            pytest.skip("'vagueness' column not found")

        vagueness = analysis_data['vagueness'].dropna()

        assert vagueness.min() >= 0, \
            f"Vagueness has negative values: min={vagueness.min()}"

        assert vagueness.max() <= 100, \
            f"Vagueness exceeds 100: max={vagueness.max()}"

    def test_early_funding_positive(self, analysis_data):
        """Early funding amounts should be positive."""
        if 'early_funding_musd' not in analysis_data.columns:
            pytest.skip("'early_funding_musd' column not found")

        funding = analysis_data['early_funding_musd'].dropna()

        # Funding cannot be negative
        negative_count = (funding < 0).sum()
        assert negative_count == 0, \
            f"Found {negative_count} negative funding values"

        # Check for unrealistic values (> $1B)
        extreme_count = (funding > 1000).sum()
        extreme_pct = extreme_count / len(funding) * 100
        assert extreme_pct < 1, \
            f"Too many extreme funding values (>$1B): {extreme_pct:.1f}%"

    def test_growth_binary(self, analysis_data):
        """Growth should be binary (0 or 1)."""
        if 'growth' not in analysis_data.columns:
            pytest.skip("'growth' column not found")

        growth = analysis_data['growth'].dropna()
        unique_values = growth.unique()

        # Should only have 0 and 1
        assert set(unique_values).issubset({0, 1}), \
            f"Growth has non-binary values: {unique_values}"


class TestOutliers:
    """Test for unrealistic outliers that might indicate data errors."""

    def test_vagueness_no_extreme_outliers(self, analysis_data):
        """Check for suspiciously high vagueness scores."""
        if 'vagueness' not in analysis_data.columns:
            pytest.skip("'vagueness' column not found")

        vagueness = analysis_data['vagueness'].dropna()

        # More than 95% vagueness is suspicious
        extreme_high = (vagueness > 95).sum()
        extreme_pct = extreme_high / len(vagueness) * 100

        assert extreme_pct < 1, \
            f"Too many extremely high vagueness scores (>95): {extreme_pct:.1f}%"

    def test_funding_distribution_reasonable(self, analysis_data):
        """Check that funding distribution is reasonable."""
        if 'early_funding_musd' not in analysis_data.columns:
            pytest.skip("'early_funding_musd' column not found")

        funding = analysis_data['early_funding_musd'].dropna()

        # Check median is reasonable (typical seed round: $1-5M)
        median_funding = funding.median()
        assert 0.1 < median_funding < 50, \
            f"Median funding looks unrealistic: ${median_funding:.2f}M"

        # Check for zero-variance (all same value)
        funding_std = funding.std()
        assert funding_std > 0, \
            "Early funding has zero variance - data error?"


class TestVariableDistributions:
    """Test that variable distributions are appropriate for analysis."""

    def test_vagueness_has_variance(self, analysis_data):
        """Vagueness must vary across companies."""
        if 'vagueness' not in analysis_data.columns:
            pytest.skip("'vagueness' column not found")

        vagueness = analysis_data['vagueness'].dropna()
        vagueness_std = vagueness.std()

        assert vagueness_std > 0, \
            "Vagueness has zero variance - cannot run regression"

        # Should have meaningful variation (std > 5 on 0-100 scale)
        assert vagueness_std > 5, \
            f"Vagueness has too little variance: std={vagueness_std:.2f}"

    def test_is_hardware_distribution(self, analysis_data):
        """Hardware indicator should have both types."""
        if 'is_hardware' not in analysis_data.columns:
            pytest.skip("'is_hardware' column not found")

        hardware_counts = analysis_data['is_hardware'].value_counts()

        # Should have both hardware and software companies
        assert len(hardware_counts) >= 2, \
            "Only one architecture type - cannot test interaction"

        # Neither group should be too small (<10%)
        min_group_pct = hardware_counts.min() / len(analysis_data) * 100
        assert min_group_pct > 10, \
            f"Smallest architecture group too small: {min_group_pct:.1f}%"


class TestZScoreing:
    """Test that z-scored variables are properly standardized."""

    def test_z_vagueness_standardized(self, analysis_data):
        """Z-scored vagueness should have mean≈0, std≈1."""
        if 'z_vagueness' not in analysis_data.columns:
            pytest.skip("'z_vagueness' column not found")

        z_vag = analysis_data['z_vagueness'].dropna()

        mean = z_vag.mean()
        std = z_vag.std()

        # Mean should be close to 0 (within 0.01)
        assert abs(mean) < 0.01, \
            f"z_vagueness mean not centered: {mean:.4f}"

        # Std should be close to 1 (within 0.1)
        assert abs(std - 1.0) < 0.1, \
            f"z_vagueness std not 1: {std:.4f}"


class TestDataIntegrity:
    """Test for data integrity issues."""

    def test_no_duplicate_companies(self, analysis_data):
        """Check for duplicate company IDs."""
        if 'company_id' not in analysis_data.columns:
            pytest.skip("'company_id' column not found")

        n_companies = len(analysis_data)
        n_unique = analysis_data['company_id'].nunique()

        duplicates = n_companies - n_unique
        assert duplicates == 0, \
            f"Found {duplicates} duplicate company IDs"

    def test_required_columns_exist(self, analysis_data):
        """Check that all required columns for H1/H2 exist."""
        required_h1 = ['z_vagueness', 'early_funding_musd', 'sector_fe']
        required_h2 = ['z_vagueness', 'is_hardware', 'growth']

        missing_h1 = [col for col in required_h1 if col not in analysis_data.columns]
        missing_h2 = [col for col in required_h2 if col not in analysis_data.columns]

        assert len(missing_h1) == 0, \
            f"H1 missing required columns: {missing_h1}"

        assert len(missing_h2) == 0, \
            f"H2 missing required columns: {missing_h2}"


class TestFixedEffects:
    """Test that fixed effects have sufficient variation."""

    def test_sector_fe_multiple_sectors(self, analysis_data):
        """Sector fixed effects should have multiple sectors."""
        if 'sector_fe' not in analysis_data.columns:
            pytest.skip("'sector_fe' column not found")

        n_sectors = analysis_data['sector_fe'].nunique()

        assert n_sectors >= 2, \
            f"Only {n_sectors} sector(s) - need variation for fixed effects"

        # Each sector should have at least 5 companies
        sector_counts = analysis_data['sector_fe'].value_counts()
        min_sector_size = sector_counts.min()

        assert min_sector_size >= 5, \
            f"Smallest sector has only {min_sector_size} companies"

    def test_cohort_fe_multiple_cohorts(self, analysis_data):
        """Cohort fixed effects should have multiple cohorts."""
        if 'founding_cohort' not in analysis_data.columns:
            pytest.skip("'founding_cohort' column not found")

        cohort_counts = analysis_data['founding_cohort'].value_counts()
        n_cohorts = len(cohort_counts)

        assert n_cohorts >= 2, \
            f"Only {n_cohorts} cohort(s) - need variation for fixed effects"

        # Each cohort should have at least 3 companies
        min_cohort_size = cohort_counts.min()
        assert min_cohort_size >= 3, \
            f"Smallest cohort has only {min_cohort_size} companies"


class TestDescriptiveStats:
    """Test that descriptive statistics are reasonable."""

    def test_print_sample_summary(self, analysis_data):
        """Print summary statistics for manual review."""
        print("\n" + "="*60)
        print("DATA QUALITY SUMMARY")
        print("="*60)

        print(f"\nTotal companies: {len(analysis_data):,}")

        if 'vagueness' in analysis_data.columns:
            v_stats = analysis_data['vagueness'].describe()
            print(f"\nVagueness:")
            print(f"  Mean: {v_stats['mean']:.2f}")
            print(f"  Std:  {v_stats['std']:.2f}")
            print(f"  Range: [{v_stats['min']:.2f}, {v_stats['max']:.2f}]")

        if 'early_funding_musd' in analysis_data.columns:
            f_stats = analysis_data['early_funding_musd'].describe()
            print(f"\nEarly Funding (M$):")
            print(f"  Mean: {f_stats['mean']:.2f}")
            print(f"  Median: {f_stats['50%']:.2f}")
            print(f"  Range: [{f_stats['min']:.2f}, {f_stats['max']:.2f}]")

        if 'growth' in analysis_data.columns:
            growth_rate = analysis_data['growth'].mean() * 100
            print(f"\nGrowth Rate: {growth_rate:.1f}%")

        if 'is_hardware' in analysis_data.columns:
            hw_counts = analysis_data['is_hardware'].value_counts()
            hw_pct = hw_counts.get(1, 0) / len(analysis_data) * 100
            print(f"\nHardware %: {hw_pct:.1f}%")

        print("="*60 + "\n")

        # This test always passes - just for info
        assert True
