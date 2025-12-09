#!/usr/bin/env python3
"""
전라좌수군 견리사의 군령 — 모델 일관성 테스트
Regression Models Consistency Tests

핵심 정신: 가설과 회귀모형의 일치
Core Spirit: Alignment between Hypothesis and Regression Model

테스트 대상:
- H1: V(1-V) coefficient > 0 (U-shape survival)
- H2: β₁ > 0 (software), β₃ < 0 (hardware interaction)
- H3: Founder credibility interaction
- H4: Resource constraint effects

=============================================================================
나대용 전대 🐅 — 實行 (구현 검증)
=============================================================================
"""

import pytest
import re
from pathlib import Path
from typing import Dict, List, Optional

# Base paths
EMPIRICS_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = EMPIRICS_ROOT / "src"


# ============================================================================
# HYPOTHESIS SPECIFICATIONS
# ============================================================================

class HypothesisSpec:
    """
    Hypothesis specifications from chap2_theory.py

    P1 (Technology): U-Shape
    - H1: Vagueness has U-shaped relationship with survival (V(1-V) coefficient > 0)
    - H2: Modularity moderates: high modularity → vagueness positive

    P2 (Organization): Competency Trap
    - H1: Early fundraising success → belief lock-in
    - H2: Cap table concentration moderates flexibility

    P3 (Competition): Execution Gap
    - H1: CR = C/(C+F) determines pivot capability
    - H2: Time pressure moderates optimal option count
    """

    # Expected variable names in models.py
    P1_VARIABLES = {
        "dv": ["growth", "survival", "series_b"],
        "iv_linear": ["z_vagueness", "vagueness"],
        "iv_ushape": ["vagueness_ushape", "vagueness_squared", "z_vagueness_sq"],
        "moderator": ["is_hardware", "modularity", "flexibility"],
        "interaction": ["z_vagueness:is_hardware", "z_vagueness*is_hardware"],
    }

    # Expected regression formula patterns
    EXPECTED_FORMULAS = {
        "H1_linear": r"growth\s*~.*z_vagueness",
        "H1_ushape": r"growth\s*~.*vagueness.*\*.*\(1.*-.*vagueness\)",
        "H1_squared": r"growth\s*~.*vagueness.*\*\*.*2",
        "H2_interaction": r"z_vagueness\s*\*\s*is_hardware",
    }


# ============================================================================
# MODEL FILE TESTS
# ============================================================================

class TestModelsFile:
    """Tests for models.py structure and content"""

    @pytest.fixture
    def models_content(self):
        """Load models.py content"""
        models_file = SRC_DIR / "models.py"
        if not models_file.exists():
            pytest.skip("models.py not found")
        return models_file.read_text()

    def test_models_file_exists(self):
        """models.py should exist in src/"""
        models_file = SRC_DIR / "models.py"
        assert models_file.exists(), f"models.py not found at {models_file}"

    def test_has_h1_model(self, models_content):
        """models.py should have H1 model (early funding)"""
        h1_patterns = [
            r"H1",
            r"early.*funding",
            r"Model.*1",
        ]

        has_h1 = any(re.search(p, models_content, re.IGNORECASE) for p in h1_patterns)
        assert has_h1, "H1 model not found in models.py"

    def test_has_h2_model(self, models_content):
        """models.py should have H2 model (growth moderation)"""
        h2_patterns = [
            r"H2",
            r"growth.*moderation",
            r"is_hardware",
            r"Model.*2",
        ]

        has_h2 = any(re.search(p, models_content, re.IGNORECASE) for p in h2_patterns)
        assert has_h2, "H2 model not found in models.py"

    def test_uses_vagueness_variable(self, models_content):
        """models.py should use vagueness as predictor"""
        vagueness_patterns = [
            r"z_vagueness",
            r"vagueness",
            r"V\s*~",
        ]

        has_vagueness = any(re.search(p, models_content) for p in vagueness_patterns)
        assert has_vagueness, "Vagueness variable not found in models.py"


# ============================================================================
# FORMULA CONSISTENCY TESTS
# ============================================================================

class TestFormulaConsistency:
    """
    Test that regression formulas match hypotheses

    CRITICAL: If H1 says V(1-V), then regression should include that term
    """

    @pytest.fixture
    def models_content(self):
        """Load models.py content"""
        models_file = SRC_DIR / "models.py"
        if not models_file.exists():
            pytest.skip("models.py not found")
        return models_file.read_text()

    def test_ushape_term_present(self, models_content):
        """
        Test: If hypothesis uses V(1-V), models.py should have quadratic term

        EXPECTED FAILURE until models.py is updated!
        """
        ushape_patterns = [
            r"vagueness.*\*.*\(1\s*-\s*vagueness\)",
            r"vagueness_ushape",
            r"vagueness_squared",
            r"z_vagueness_sq",
            r"I\(.*vagueness.*\*\*.*2\)",  # statsmodels I() notation
            r"np\.square\(.*vagueness",
        ]

        has_ushape = any(re.search(p, models_content, re.IGNORECASE) for p in ushape_patterns)

        if not has_ushape:
            # Check if it's linear only
            linear_only = re.search(r"growth.*~.*z_vagueness\s*\+", models_content)

            if linear_only:
                pytest.fail(
                    "FORMULA MISMATCH:\n"
                    "  Hypothesis H1: V(1-V) coefficient > 0 (U-shape)\n"
                    "  models.py: Linear vagueness only (no quadratic term)\n"
                    "\n"
                    "ACTION REQUIRED:\n"
                    "  Update regression formula to include:\n"
                    "    + I(z_vagueness**2)  # for statsmodels\n"
                    "  or use pre-computed:\n"
                    "    + vagueness_ushape   # from features.py"
                )

    def test_interaction_term_present(self, models_content):
        """Test: H2 requires vagueness × is_hardware interaction"""
        interaction_patterns = [
            r"z_vagueness\s*\*\s*is_hardware",
            r"z_vagueness\s*:\s*is_hardware",
            r"vagueness.*is_hardware",
        ]

        has_interaction = any(re.search(p, models_content) for p in interaction_patterns)
        assert has_interaction, \
            "H2 requires vagueness × is_hardware interaction, not found in models.py"

    def test_no_mediator_as_control(self, models_content):
        """
        Test: early_funding should NOT be control in growth model

        Reason: early_funding is MEDIATOR, not confounder
        Including mediator as control biases causal effect
        """
        # Check for growth model
        growth_model_match = re.search(
            r"growth.*~.*early_funding",
            models_content,
            re.IGNORECASE
        )

        if growth_model_match:
            pytest.fail(
                "MEDIATION ERROR:\n"
                "  early_funding appears as control in growth model\n"
                "  early_funding is a MEDIATOR between vagueness → growth\n"
                "  Including it as control introduces mediator bias\n"
                "\n"
                "ACTION: Remove early_funding from growth regression controls"
            )


# ============================================================================
# VARIABLE NAMING CONSISTENCY
# ============================================================================

class TestVariableNaming:
    """Test consistent variable naming across files"""

    def test_standardized_vagueness_name(self):
        """Vagueness variable should use consistent name"""
        files_to_check = [
            SRC_DIR / "models.py",
            SRC_DIR / "features.py",
            SRC_DIR / "plotting.py",
        ]

        vagueness_names: Dict[str, List[str]] = {}

        for filepath in files_to_check:
            if not filepath.exists():
                continue

            content = filepath.read_text()

            # Find vagueness variable names
            names = set()
            if "z_vagueness" in content:
                names.add("z_vagueness")
            if re.search(r"['\"]vagueness['\"]", content):
                names.add("vagueness")
            if "V_raw" in content:
                names.add("V_raw")
            if "V_minmax" in content:
                names.add("V_minmax")

            vagueness_names[filepath.name] = list(names)

        # Report inconsistencies
        all_names = set()
        for names in vagueness_names.values():
            all_names.update(names)

        if len(all_names) > 2:
            report = "VARIABLE NAMING INCONSISTENCY:\n"
            for filename, names in vagueness_names.items():
                report += f"  {filename}: {names}\n"
            print(report)

    def test_dependent_variable_consistency(self):
        """DV should be consistent: growth, survival, or series_b"""
        models_file = SRC_DIR / "models.py"
        plotting_file = SRC_DIR / "plotting.py"

        if not models_file.exists():
            pytest.skip("models.py not found")

        models_content = models_file.read_text()

        # Expected DV names
        expected_dvs = ["growth", "survival", "series_b", "early_funding"]

        found_dvs = []
        for dv in expected_dvs:
            if re.search(rf"['\"]?{dv}['\"]?\s*~", models_content):
                found_dvs.append(dv)

        assert len(found_dvs) > 0, \
            f"No expected DV found in models.py. Expected one of {expected_dvs}"


# ============================================================================
# CONTROL VARIABLE TESTS
# ============================================================================

class TestControlVariables:
    """Test appropriate control variables"""

    @pytest.fixture
    def models_content(self):
        """Load models.py content"""
        models_file = SRC_DIR / "models.py"
        if not models_file.exists():
            pytest.skip("models.py not found")
        return models_file.read_text()

    def test_has_industry_controls(self, models_content):
        """Should control for industry effects"""
        industry_patterns = [
            r"industry",
            r"sector",
            r"C\(industry\)",  # statsmodels categorical
            r"fe_industry",
        ]

        has_industry = any(re.search(p, models_content, re.IGNORECASE) for p in industry_patterns)
        # This is a soft check - may not be required
        if not has_industry:
            print("Note: No explicit industry controls found")

    def test_has_time_controls(self, models_content):
        """Should control for time/cohort effects"""
        time_patterns = [
            r"year",
            r"cohort",
            r"founded_year",
            r"vintage",
            r"C\(year\)",
        ]

        has_time = any(re.search(p, models_content, re.IGNORECASE) for p in time_patterns)
        # This is a soft check
        if not has_time:
            print("Note: No explicit time/cohort controls found")


# ============================================================================
# STATISTICAL METHOD TESTS
# ============================================================================

class TestStatisticalMethods:
    """Test appropriate statistical methods"""

    @pytest.fixture
    def models_content(self):
        """Load models.py content"""
        models_file = SRC_DIR / "models.py"
        if not models_file.exists():
            pytest.skip("models.py not found")
        return models_file.read_text()

    def test_uses_appropriate_estimator(self, models_content):
        """Should use OLS for continuous, Logit for binary"""
        # Check for OLS usage
        has_ols = re.search(r"OLS|ols|smf\.ols", models_content)

        # Check for Logit usage
        has_logit = re.search(r"Logit|logit|smf\.logit", models_content)

        assert has_ols or has_logit, \
            "Should use OLS for continuous DV or Logit for binary DV"

    def test_robust_standard_errors(self, models_content):
        """Should use robust standard errors"""
        robust_patterns = [
            r"HC[0-3]",
            r"robust",
            r"cov_type",
            r"cluster",
        ]

        has_robust = any(re.search(p, models_content, re.IGNORECASE) for p in robust_patterns)
        # Informational - not required
        if not has_robust:
            print("Note: No explicit robust SE specification found")


# ============================================================================
# SUMMARY
# ============================================================================

def generate_models_test_report():
    """Generate summary report"""
    print("\n" + "=" * 70)
    print("전라좌수군 견리사의 군령 — 모델 일관성 테스트 보고서")
    print("Models Consistency Test Report")
    print("=" * 70)

    print("""
📋 Test Categories:

1. Model File Structure:
   - models.py exists
   - H1, H2 models present
   - Uses vagueness variable

2. Formula Consistency:
   ⚠️  CRITICAL: U-shape term V(1-V) or V² should be present
   - Interaction term z_vagueness × is_hardware
   - No mediator as control (early_funding)

3. Variable Naming:
   - Consistent vagueness naming across files
   - Consistent DV naming

4. Control Variables:
   - Industry controls
   - Time/cohort controls

5. Statistical Methods:
   - Appropriate estimator (OLS/Logit)
   - Robust standard errors

📝 Key Finding:
   If H1 specifies V(1-V) coefficient > 0, but models.py only has
   linear z_vagueness, this is a FORMULA MISMATCH that needs fixing.
""")

    print("=" * 70)
    print("Run: pytest test/unit/test_models_consistency.py -v")
    print("=" * 70)


if __name__ == "__main__":
    generate_models_test_report()
    pytest.main([__file__, "-v", "--tb=short"])
