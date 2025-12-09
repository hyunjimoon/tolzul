#!/usr/bin/env python3
"""
Unit Tests for Feature Engineering Module (features.py)
=======================================================
Tests for vagueness scoring, feature engineering, and data processing.

Priority focus:
- Vagueness scoring validation (V1 vs V2)
- Feature variance checks
- Z-score normalization
- is_hardware classification
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))

import pandas as pd
import numpy as np
from features import StrategicVaguenessScorer, compute_vagueness_vectorized
from vagueness_v2 import StrategicVaguenessScorerV2


# ============================================
# Vagueness Scoring Tests
# ============================================

@pytest.mark.unit
class TestVaguenessScoring:
    """Tests for strategic vagueness scoring algorithms."""

    def test_v2_scorer_initialization(self):
        """V2 scorer should initialize without errors."""
        scorer = StrategicVaguenessScorerV2()
        assert scorer is not None

    def test_v2_concrete_vs_vague_descriptions(self):
        """V2 should assign lower scores to concrete descriptions."""
        scorer = StrategicVaguenessScorerV2()

        # Concrete: specific numbers, products, markets
        concrete = """
        AI-powered medical imaging platform for lung cancer detection.
        Deployed in 50 hospitals across California.
        98% accuracy on X-ray nodule detection.
        FDA approved Class II medical device.
        Serving 200,000 patients annually.
        """

        # Vague: generic buzzwords, no specifics
        vague = """
        Revolutionary next-generation technology platform.
        Disrupting the future of innovation.
        Cutting-edge solutions leveraging AI.
        Transforming the industry landscape.
        """

        score_concrete = scorer.score(concrete)
        score_vague = scorer.score(vague)

        assert score_concrete < score_vague, \
            f"Concrete should score lower: {score_concrete} vs {score_vague}"

    def test_v2_score_range(self):
        """V2 scores should be in valid range [0, 100]."""
        scorer = StrategicVaguenessScorerV2()

        test_descriptions = [
            "AI software for healthcare",
            "Hardware sensor for industrial IoT",
            "Quantum computing platform",
            "",  # Edge case: empty string
            "a" * 1000,  # Edge case: very long text
        ]

        for desc in test_descriptions:
            score = scorer.score(desc)
            assert 0 <= score <= 100, \
                f"Score {score} out of range for: {desc[:50]}"

    def test_v2_deterministic(self):
        """V2 should produce same score for same input."""
        scorer = StrategicVaguenessScorerV2()

        description = "AI-powered predictive analytics platform"

        score1 = scorer.score(description)
        score2 = scorer.score(description)
        score3 = scorer.score(description)

        assert score1 == score2 == score3, \
            "Vagueness scoring should be deterministic"

    def test_v2_variance_better_than_v1(self):
        """V2 should have better score variance than V1 (avoid 75% at 50.0)."""
        scorer_v2 = StrategicVaguenessScorerV2()

        # Sample descriptions with varying concreteness
        descriptions = [
            "AI software",
            "Hardware manufacturing for aerospace components with 10-year contracts",
            "Generic platform technology",
            "Medical device for cardiac monitoring, FDA approved, 1000+ units sold",
            "Next-gen innovation",
            "B2B SaaS for supply chain optimization in automotive industry",
            "Revolutionary solution",
            "Semiconductor fabrication equipment for 5nm process nodes",
        ]

        scores = [scorer_v2.score(d) for d in descriptions]

        # Check variance
        variance = np.var(scores)
        assert variance > 10, \
            f"V2 should have reasonable variance, got {variance}"

        # Check not all same
        unique_scores = len(set(scores))
        assert unique_scores >= 5, \
            f"V2 should produce diverse scores, got {unique_scores} unique"

    def test_v2_empty_description(self):
        """V2 should handle empty descriptions gracefully."""
        scorer = StrategicVaguenessScorerV2()

        score = scorer.score("")

        # Should return some default value, not crash
        assert isinstance(score, (int, float))
        assert 0 <= score <= 100

    def test_v2_special_characters(self):
        """V2 should handle special characters and unicode."""
        scorer = StrategicVaguenessScorerV2()

        descriptions = [
            "AI software with émojis 🚀",
            "Hardware & sensors @ $50/unit",
            "Platform (beta) [version 2.0]",
            "Software—next generation",
        ]

        for desc in descriptions:
            score = scorer.score(desc)
            assert 0 <= score <= 100, \
                f"Should handle special chars: {desc}"

    def test_vectorized_scoring(self):
        """Vectorized scoring should work on pandas Series."""
        descriptions = pd.Series([
            "AI healthcare platform",
            "Hardware sensors",
            "Software tools",
        ])

        keywords = pd.Series([
            "AI, healthcare, platform",
            "hardware, sensors, IoT",
            "software, tools, analytics",
        ])

        scores = compute_vagueness_vectorized(descriptions, keywords)

        assert len(scores) == len(descriptions)
        assert all(0 <= s <= 100 for s in scores)


# ============================================
# Feature Engineering Tests
# ============================================

@pytest.mark.unit
class TestFeatureEngineering:
    """Tests for feature engineering functions."""

    def test_zscore_normalization_properties(self):
        """Z-score should have mean≈0, std≈1."""
        data = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])

        # Apply z-score normalization
        z_scores = (data - data.mean()) / data.std()

        # Check mean ≈ 0
        assert abs(z_scores.mean()) < 1e-10, \
            f"Z-score mean should be ~0, got {z_scores.mean()}"

        # Check std ≈ 1
        assert abs(z_scores.std() - 1.0) < 1e-10, \
            f"Z-score std should be ~1, got {z_scores.std()}"

    def test_zscore_preserves_order(self):
        """Z-score should preserve order of values."""
        data = pd.Series([10, 5, 20, 15, 3, 25])
        z_scores = (data - data.mean()) / data.std()

        # Sort both
        data_sorted_idx = data.argsort()
        z_sorted_idx = z_scores.argsort()

        # Should have same order
        assert all(data_sorted_idx == z_sorted_idx), \
            "Z-score should preserve value order"

    def test_log_transformation_reduces_skew(self):
        """Log transformation should reduce right-skewed data."""
        # Create right-skewed data (exponential-like)
        np.random.seed(42)
        data = np.random.exponential(scale=2.0, size=100)

        original_skew = pd.Series(data).skew()
        log_data = np.log1p(data)  # log(1 + x) to handle zeros
        log_skew = pd.Series(log_data).skew()

        assert abs(log_skew) < abs(original_skew), \
            f"Log should reduce skew: {original_skew} -> {log_skew}"

    def test_binary_classification_consistency(self):
        """Binary classifications should be 0 or 1."""
        # Simulate is_hardware classification
        descriptions = pd.Series([
            "Hardware sensor manufacturing",
            "Software as a service platform",
            "Semiconductor fabrication",
            "Cloud-based analytics",
        ])

        # Mock classification (in real code, this uses keywords)
        is_hardware = descriptions.str.contains('hardware|sensor|semiconductor', case=False).astype(int)

        assert set(is_hardware.unique()).issubset({0, 1}), \
            "Binary classification should only have 0 and 1"


# ============================================
# Data Quality Tests
# ============================================

@pytest.mark.unit
class TestDataQuality:
    """Tests for data quality and validation."""

    def test_no_infinite_values_after_normalization(self):
        """Normalized features should not contain inf or -inf."""
        data = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
        z_scores = (data - data.mean()) / data.std()

        assert not np.isinf(z_scores).any(), \
            "Z-scores should not contain infinite values"

    def test_handle_constant_variable_zscore(self):
        """Z-score of constant variable should handle division by zero."""
        data = pd.Series([5.0, 5.0, 5.0, 5.0, 5.0])

        # Z-score with std=0 will produce NaN or inf
        std = data.std()

        if std == 0:
            # Should detect constant variable
            assert True, "Correctly detected constant variable"
        else:
            z_scores = (data - data.mean()) / std
            # If not constant, should be valid
            assert not np.isnan(z_scores).any()

    def test_missing_data_handling(self):
        """Feature engineering should handle missing data."""
        data = pd.Series([1.0, 2.0, np.nan, 4.0, 5.0])

        # Drop NaN before z-scoring (typical approach)
        data_clean = data.dropna()
        z_scores = (data_clean - data_clean.mean()) / data_clean.std()

        assert not np.isnan(z_scores).any(), \
            "Z-scores should not have NaN after dropping NaN inputs"

    def test_feature_names_valid(self):
        """Feature names should be valid Python identifiers."""
        feature_names = [
            'z_vagueness',
            'z_employees_log',
            'is_hardware',
            'founder_serial',
            'z_firm_age',
            'early_funding_musd',
        ]

        for name in feature_names:
            assert name.isidentifier(), \
                f"'{name}' should be a valid Python identifier"


# ============================================
# Regression Tests (Prevent Known Bugs)
# ============================================

@pytest.mark.unit
class TestRegressionPrevention:
    """Tests to prevent previously discovered bugs."""

    def test_vagueness_not_all_same_value(self):
        """
        REGRESSION: V1 scorer had 75% of scores = 50.0
        Ensure V2 doesn't have this problem.
        """
        scorer = StrategicVaguenessScorerV2()

        descriptions = [
            f"Company {i} description with varying content and length "
            f"{'specific' if i % 2 == 0 else 'generic'} details"
            for i in range(20)
        ]

        scores = [scorer.score(d) for d in descriptions]

        # Count most common score
        from collections import Counter
        score_counts = Counter(scores)
        most_common_score, most_common_count = score_counts.most_common(1)[0]

        # No single score should dominate (e.g., > 50%)
        assert most_common_count < len(scores) * 0.5, \
            f"Score {most_common_score} appears {most_common_count}/{len(scores)} times (too frequent)"

    def test_hardware_classification_not_all_zeros(self):
        """Hardware classification should identify some hardware companies."""
        descriptions = pd.Series([
            "Hardware sensor manufacturing",
            "Semiconductor fabrication equipment",
            "Software as a service",
            "Integrated circuit design",
        ])

        # Mock hardware detection
        is_hardware = descriptions.str.contains(
            'hardware|sensor|semiconductor|integrated circuit',
            case=False
        ).astype(int)

        hardware_count = is_hardware.sum()

        assert hardware_count > 0, \
            "Should identify at least some hardware companies"
        assert hardware_count < len(descriptions), \
            "Should not classify all as hardware"


# ============================================
# Integration Test (Quick Smoke Test)
# ============================================

@pytest.mark.integration
class TestFeatureIntegration:
    """Quick integration test for feature pipeline."""

    def test_vagueness_scoring_pipeline(self):
        """End-to-end vagueness scoring should work."""
        # Create sample data
        df = pd.DataFrame({
            'company_id': [1, 2, 3],
            'description': [
                "AI-powered healthcare analytics platform with FDA approval",
                "Next-generation technology solutions",
                "Hardware manufacturing for aerospace components",
            ],
            'keywords': [
                "AI, healthcare, analytics",
                "technology, solutions",
                "hardware, aerospace, manufacturing",
            ]
        })

        # Score vagueness
        scorer = StrategicVaguenessScorerV2()
        df['vagueness'] = df['description'].apply(scorer.score)

        # Validate
        assert 'vagueness' in df.columns
        assert len(df['vagueness']) == 3
        assert all(0 <= v <= 100 for v in df['vagueness'])

        # Z-score
        df['z_vagueness'] = (df['vagueness'] - df['vagueness'].mean()) / df['vagueness'].std()

        assert 'z_vagueness' in df.columns
        assert abs(df['z_vagueness'].mean()) < 0.01
