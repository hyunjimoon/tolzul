#!/usr/bin/env python3
"""
전라좌수군 견리사의 군령 — Vagueness 스코어러 테스트
Vagueness Scorer Unit Tests

핵심 정신: 측정의 일관성과 재현가능성
Core Spirit: Consistency and Reproducibility of Measurement

테스트 대상:
- vagueness_v2.py: Two-component scorer (categorical + concreteness deficit)
- vagueness_v3.py: Entropy-based scorer (market entropy + tech abstractness)
- features.py: Integration and normalization

=============================================================================
김완 전대 🐙 — 義 (비판적 검증)
=============================================================================
"""

import pytest
import sys
from pathlib import Path

# Add source to path
EMPIRICS_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = EMPIRICS_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))
sys.path.insert(0, str(EMPIRICS_ROOT))


# ============================================================================
# TEST DATA — 표준 테스트 케이스
# ============================================================================

class TestCases:
    """Standard test cases for vagueness scoring"""

    # HIGH VAGUENESS: Abstract, no concrete details
    HIGH_VAGUENESS = {
        "description": """
        We are building a revolutionary platform that leverages cutting-edge
        technology to transform the industry. Our innovative solution creates
        unprecedented value for stakeholders through seamless integration and
        holistic approaches to complex challenges.
        """,
        "keywords": ["platform", "innovation", "technology", "solution"],
        "expected_range": (60, 100)  # High vagueness expected
    }

    # LOW VAGUENESS: Specific, concrete details
    LOW_VAGUENESS = {
        "description": """
        Our Series A product is a 50kW DC fast charger ($45,000 unit price)
        certified to CHAdeMO 2.0 and CCS1 standards. We've deployed 127 units
        across 23 states since Q3 2022, with 99.2% uptime. Revenue: $5.7M in
        2023, targeting $12M in 2024. Team: 3 ex-Tesla engineers, 2 MIT PhDs.
        """,
        "keywords": ["EV charger", "hardware", "CHAdeMO", "50kW DC"],
        "expected_range": (0, 40)  # Low vagueness expected
    }

    # MEDIUM VAGUENESS: Mixed concrete and abstract
    MEDIUM_VAGUENESS = {
        "description": """
        Our AI-powered analytics platform helps enterprises optimize operations.
        We process 10M events/day with 50ms latency. Currently serving Fortune 500
        clients. Our proprietary algorithms improve efficiency by up to 30%.
        """,
        "keywords": ["AI", "analytics", "enterprise", "optimization"],
        "expected_range": (30, 70)  # Medium vagueness expected
    }


# ============================================================================
# VAGUENESS V2 TESTS
# ============================================================================

class TestVaguenessV2:
    """Tests for HybridVaguenessScorerV2"""

    @pytest.fixture
    def scorer_v2(self):
        """Import and instantiate V2 scorer"""
        try:
            from vagueness_v2 import HybridVaguenessScorerV2
            return HybridVaguenessScorerV2()
        except ImportError as e:
            pytest.skip(f"Could not import vagueness_v2: {e}")

    def test_high_vagueness_scores_high(self, scorer_v2):
        """High vagueness text should score high (60-100)"""
        case = TestCases.HIGH_VAGUENESS

        score = scorer_v2.score(case["description"], case["keywords"])
        v_raw = score.get("V_raw", score.get("vagueness", 0))

        assert case["expected_range"][0] <= v_raw <= case["expected_range"][1], \
            f"High vagueness text scored {v_raw}, expected {case['expected_range']}"

    def test_low_vagueness_scores_low(self, scorer_v2):
        """Low vagueness text should score low (0-40)"""
        case = TestCases.LOW_VAGUENESS

        score = scorer_v2.score(case["description"], case["keywords"])
        v_raw = score.get("V_raw", score.get("vagueness", 0))

        assert case["expected_range"][0] <= v_raw <= case["expected_range"][1], \
            f"Low vagueness text scored {v_raw}, expected {case['expected_range']}"

    def test_ordering_preserved(self, scorer_v2):
        """LOW < MEDIUM < HIGH vagueness ordering should be preserved"""
        low_score = scorer_v2.score(
            TestCases.LOW_VAGUENESS["description"],
            TestCases.LOW_VAGUENESS["keywords"]
        ).get("V_raw", 0)

        medium_score = scorer_v2.score(
            TestCases.MEDIUM_VAGUENESS["description"],
            TestCases.MEDIUM_VAGUENESS["keywords"]
        ).get("V_raw", 0)

        high_score = scorer_v2.score(
            TestCases.HIGH_VAGUENESS["description"],
            TestCases.HIGH_VAGUENESS["keywords"]
        ).get("V_raw", 0)

        assert low_score < medium_score < high_score, \
            f"Ordering violated: LOW({low_score}) < MEDIUM({medium_score}) < HIGH({high_score})"

    def test_score_range(self, scorer_v2):
        """Scores should be in [0, 100] range"""
        for case in [TestCases.HIGH_VAGUENESS, TestCases.LOW_VAGUENESS, TestCases.MEDIUM_VAGUENESS]:
            score = scorer_v2.score(case["description"], case["keywords"])
            v_raw = score.get("V_raw", score.get("vagueness", 0))

            assert 0 <= v_raw <= 100, f"Score {v_raw} out of [0, 100] range"

    def test_empty_input_handling(self, scorer_v2):
        """Empty inputs should be handled gracefully"""
        score = scorer_v2.score("", [])

        # Should return a valid score dictionary
        assert isinstance(score, dict)
        # Should not crash

    def test_reproducibility(self, scorer_v2):
        """Same input should produce same output"""
        case = TestCases.MEDIUM_VAGUENESS

        score1 = scorer_v2.score(case["description"], case["keywords"])
        score2 = scorer_v2.score(case["description"], case["keywords"])

        v1 = score1.get("V_raw", score1.get("vagueness", 0))
        v2 = score2.get("V_raw", score2.get("vagueness", 0))

        assert v1 == v2, f"Non-reproducible scores: {v1} != {v2}"


# ============================================================================
# VAGUENESS V3 TESTS
# ============================================================================

class TestVaguenessV3:
    """Tests for entropy-based vagueness scorer V3"""

    @pytest.fixture
    def scorer_v3(self):
        """Import and instantiate V3 scorer"""
        try:
            from vagueness_v3 import EntropyVaguenessScorer
            return EntropyVaguenessScorer()
        except ImportError as e:
            pytest.skip(f"Could not import vagueness_v3: {e}")

    def test_score_returns_dict(self, scorer_v3):
        """V3 scorer should return dictionary with expected keys"""
        case = TestCases.MEDIUM_VAGUENESS

        score = scorer_v3.score(case["description"], case["keywords"])

        assert isinstance(score, dict)
        # Check for expected keys (may vary by implementation)
        expected_keys = {"V_market_entropy", "V_tech_abstractness", "V_composite"}
        actual_keys = set(score.keys())

        # At least some expected keys should be present
        assert len(expected_keys & actual_keys) > 0, \
            f"Expected some of {expected_keys}, got {actual_keys}"

    def test_ordering_similar_to_v2(self, scorer_v3):
        """V3 ordering should be similar to V2"""
        low_score = scorer_v3.score(
            TestCases.LOW_VAGUENESS["description"],
            TestCases.LOW_VAGUENESS["keywords"]
        ).get("V_composite", 0)

        high_score = scorer_v3.score(
            TestCases.HIGH_VAGUENESS["description"],
            TestCases.HIGH_VAGUENESS["keywords"]
        ).get("V_composite", 0)

        # Low should be less than high (basic ordering)
        assert low_score < high_score, \
            f"V3 ordering violated: LOW({low_score}) should be < HIGH({high_score})"


# ============================================================================
# AGGREGATION FORMULA TESTS
# ============================================================================

class TestAggregationFormula:
    """
    Test the vagueness aggregation formula

    Current formula (from vagueness_v2.py):
        V_raw = 0.5 * max(S_cat, S_concdef) + 0.5 * mean(S_cat, S_concdef)

    This is a max-mean hybrid, NOT the V(1-V) from hypothesis!
    """

    def test_aggregation_formula_documentation(self):
        """Test that aggregation formula is properly documented"""
        vagueness_file = SRC_DIR / "vagueness_v2.py"

        if not vagueness_file.exists():
            pytest.skip("vagueness_v2.py not found")

        content = vagueness_file.read_text()

        # Check for formula documentation
        formula_patterns = [
            r"V_raw\s*=",
            r"0\.5\s*\*\s*max",
            r"0\.5\s*\*\s*mean",
        ]

        found_formula = any(pattern in content for pattern in formula_patterns)

        assert found_formula, \
            "Aggregation formula V_raw = 0.5*max + 0.5*mean not found in vagueness_v2.py"

    def test_max_mean_properties(self):
        """
        Test mathematical properties of max-mean aggregation:
        - When S_cat == S_concdef: V_raw = S_cat
        - When one is 0: V_raw = 0.75 * max_val
        """
        # Property 1: Equal components
        s_cat = 60
        s_concdef = 60
        v_raw = 0.5 * max(s_cat, s_concdef) + 0.5 * 0.5 * (s_cat + s_concdef)
        assert v_raw == 60, f"When equal, V_raw should equal components: {v_raw}"

        # Property 2: One component is 0
        s_cat = 80
        s_concdef = 0
        v_raw = 0.5 * max(s_cat, s_concdef) + 0.5 * 0.5 * (s_cat + s_concdef)
        # = 0.5 * 80 + 0.5 * 40 = 40 + 20 = 60
        assert v_raw == 60, f"With one 0, V_raw should be 0.75*max: {v_raw}"


# ============================================================================
# U-SHAPE TRANSFORMATION TESTS
# ============================================================================

class TestUShapeTransformation:
    """
    Test U-shape transformations for hypothesis testing

    H1: V(1-V) coefficient > 0

    If V is in [0, 1]:
        V(1-V) peaks at V = 0.5
        V(1-V) = 0 when V = 0 or V = 1

    If V is in [0, 100]:
        V(100-V)/10000 peaks at V = 50
    """

    def test_ushape_formula_v01_range(self):
        """Test V(1-V) formula for V in [0, 1]"""
        # Peak at V = 0.5
        v = 0.5
        ushape = v * (1 - v)
        assert ushape == 0.25, f"Peak value should be 0.25, got {ushape}"

        # Zero at boundaries
        assert 0 * (1 - 0) == 0, "V(1-V) should be 0 at V=0"
        assert 1 * (1 - 1) == 0, "V(1-V) should be 0 at V=1"

        # Symmetric around 0.5
        v1, v2 = 0.3, 0.7
        assert abs(v1 * (1 - v1) - v2 * (1 - v2)) < 0.001, \
            "V(1-V) should be symmetric around 0.5"

    def test_ushape_formula_v0100_range(self):
        """Test V(100-V) formula for V in [0, 100]"""
        # Peak at V = 50
        v = 50
        ushape = v * (100 - v) / 10000  # Normalized to [0, 0.25]
        assert ushape == 0.25, f"Peak value should be 0.25, got {ushape}"

        # Zero at boundaries
        assert 0 * (100 - 0) / 10000 == 0, "Should be 0 at V=0"
        assert 100 * (100 - 100) / 10000 == 0, "Should be 0 at V=100"

    def test_ushape_feature_creation(self):
        """Test creating U-shape feature from vagueness scores"""
        # Simulate vagueness scores [0, 100]
        vagueness_scores = [0, 25, 50, 75, 100]

        # Create U-shape feature
        ushape_features = [v * (100 - v) / 10000 for v in vagueness_scores]

        # Expected: [0, 0.1875, 0.25, 0.1875, 0]
        expected = [0, 0.1875, 0.25, 0.1875, 0]

        for v, u, e in zip(vagueness_scores, ushape_features, expected):
            assert abs(u - e) < 0.0001, f"U-shape({v}) = {u}, expected {e}"


# ============================================================================
# INTEGRATION WITH FEATURES.PY
# ============================================================================

class TestFeaturesIntegration:
    """Test integration with features.py"""

    def test_features_imports_vagueness(self):
        """features.py should import vagueness scorer"""
        features_file = SRC_DIR / "features.py"

        if not features_file.exists():
            pytest.skip("features.py not found")

        content = features_file.read_text()

        import_patterns = [
            r"from\s+vagueness",
            r"import\s+.*vagueness",
            r"HybridVaguenessScorer",
        ]

        has_import = any(__import__('re').search(p, content) for p in import_patterns)

        assert has_import, "features.py should import vagueness scorer"

    def test_compute_vagueness_function_exists(self):
        """features.py should have compute_vagueness function"""
        features_file = SRC_DIR / "features.py"

        if not features_file.exists():
            pytest.skip("features.py not found")

        content = features_file.read_text()

        assert "def compute_vagueness" in content, \
            "features.py should have compute_vagueness function"


# ============================================================================
# SUMMARY
# ============================================================================

def generate_scorer_test_report():
    """Generate summary report"""
    print("\n" + "=" * 70)
    print("전라좌수군 견리사의 군령 — Vagueness 스코어러 테스트 보고서")
    print("Vagueness Scorer Test Report")
    print("=" * 70)

    print("""
📋 Test Categories:

1. VaguenessV2 Tests:
   - High vagueness → High score (60-100)
   - Low vagueness → Low score (0-40)
   - Ordering: LOW < MEDIUM < HIGH
   - Score range: [0, 100]
   - Reproducibility

2. VaguenessV3 Tests:
   - Score returns expected keys
   - Ordering similar to V2

3. Aggregation Formula Tests:
   - V_raw = 0.5*max + 0.5*mean
   - Mathematical properties

4. U-Shape Transformation Tests:
   - V(1-V) for [0,1] range
   - V(100-V)/10000 for [0,100] range
   - Feature creation

5. Features Integration Tests:
   - Import vagueness scorer
   - compute_vagueness function exists
""")

    print("=" * 70)
    print("Run: pytest test/unit/test_vagueness_scorer.py -v")
    print("=" * 70)


if __name__ == "__main__":
    generate_scorer_test_report()
    pytest.main([__file__, "-v", "--tb=short"])
