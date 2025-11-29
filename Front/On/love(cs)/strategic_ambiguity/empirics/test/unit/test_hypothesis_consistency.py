#!/usr/bin/env python3
"""
전라좌수군 견리사의 군령 — 가설-구현 일관성 테스트
Hypothesis-Implementation Consistency Tests

핵심 정신: 理論(이론)과 實踐(실천)의 一致(일치)
Core Spirit: Alignment between Theory and Practice

테스트 대상:
- P1 H1: V(1-V) coefficient > 0 (U-shape survival)
- 가설에서 정의한 수식이 실제 구현 코드에 반영되어 있는지 확인

=============================================================================
김완 전대 🐙 — 義 (비판적 검증)
=============================================================================
"""

import pytest
import re
import ast
from pathlib import Path
from typing import List, Tuple, Set

# Base paths
EMPIRICS_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = EMPIRICS_ROOT / "src"
SCRIPTS_DIR = SRC_DIR / "scripts" / "paper_generation"


# ============================================================================
# FORMULA DEFINITIONS — 가설에서 정의한 수식들
# ============================================================================

class FormulaSpec:
    """Formula specification from hypothesis"""

    # P1 H1: U-Shape Hypothesis
    # OLD: V² coefficient > 0
    # NEW: V(1-V) coefficient > 0 (equivalent but different parameterization)

    OLD_USHAPE_PATTERNS = [
        r"V\*\*2",           # V**2 (Python)
        r"V\^2",             # V^2 (LaTeX/math notation)
        r"V²",               # V² (Unicode)
        r"Vagueness²",       # Full name
        r"vagueness\*\*2",   # lowercase python
        r"z_vagueness\*\*2", # standardized
    ]

    NEW_USHAPE_PATTERNS = [
        r"V\s*\*\s*\(1\s*-\s*V\)",           # V * (1 - V)
        r"V\(1-V\)",                          # V(1-V) compact
        r"V\s*\(1\s*-\s*V\)",                # V (1 - V)
        r"vagueness\s*\*\s*\(1\s*-\s*vagueness\)",  # full name
        r"z_vagueness\s*\*\s*\(1\s*-\s*z_vagueness\)",  # standardized
    ]

    # Linear vagueness (no U-shape term)
    LINEAR_PATTERNS = [
        r"~\s*z_vagueness\s*\+",              # OLS formula
        r"z_vagueness\s*\*\s*is_hardware",    # Interaction only
    ]


# ============================================================================
# TEST HELPERS
# ============================================================================

def scan_file_for_patterns(filepath: Path, patterns: List[str]) -> List[Tuple[int, str, str]]:
    """
    Scan a file for regex patterns.

    Returns:
        List of (line_number, matched_pattern, line_content)
    """
    matches = []
    try:
        content = filepath.read_text(encoding='utf-8')
        lines = content.split('\n')

        for i, line in enumerate(lines, 1):
            for pattern in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    matches.append((i, pattern, line.strip()))

    except Exception as e:
        print(f"Error reading {filepath}: {e}")

    return matches


def get_python_files(directory: Path) -> List[Path]:
    """Get all Python files in directory recursively"""
    return list(directory.rglob("*.py"))


# ============================================================================
# CONSISTENCY TESTS
# ============================================================================

class TestHypothesisFormulaConsistency:
    """
    Test that hypothesis formulas are consistently implemented

    견리사의 義 (의로움): 비판적으로 검증하되 건설적으로
    """

    def test_old_formula_deprecated(self):
        """
        Test: OLD V² formula should NOT appear in active code

        Files should use V(1-V) instead of V²
        Exceptions: Legacy comments, documentation explaining change
        """
        old_matches = []

        for py_file in get_python_files(SRC_DIR):
            # Skip test files and archive
            if 'test' in str(py_file) or 'archive' in str(py_file):
                continue

            matches = scan_file_for_patterns(py_file, FormulaSpec.OLD_USHAPE_PATTERNS)
            if matches:
                old_matches.append((py_file, matches))

        # Report findings
        if old_matches:
            report = "\n=== OLD FORMULA (V²) DETECTED ===\n"
            for filepath, matches in old_matches:
                report += f"\n📁 {filepath.relative_to(EMPIRICS_ROOT)}\n"
                for line_num, pattern, content in matches:
                    report += f"   Line {line_num}: {content[:80]}...\n"

            # This is a WARNING, not failure - document what needs update
            print(report)

        # Count: should ideally be 0 or few (only in comments)
        total_old = sum(len(m) for _, m in old_matches)
        assert total_old <= 2, f"Found {total_old} old V² formulas that may need updating"

    def test_new_formula_present_in_theory(self):
        """
        Test: NEW V(1-V) formula should be in theory chapter

        H1: Vagueness has U-shaped relationship with survival (V(1-V) coefficient > 0)
        """
        theory_file = SCRIPTS_DIR / "chap2_theory.py"

        if not theory_file.exists():
            pytest.skip("chap2_theory.py not found")

        matches = scan_file_for_patterns(theory_file, FormulaSpec.NEW_USHAPE_PATTERNS)

        assert len(matches) > 0, \
            "V(1-V) formula not found in chap2_theory.py - H1 hypothesis should use new formula"

    def test_regression_model_matches_hypothesis(self):
        """
        Test: Regression models should implement the formula from hypothesis

        If H1 says V(1-V), then models.py should have V(1-V) term
        Current: models.py uses LINEAR vagueness only
        Expected: models.py should have V(1-V) or equivalent quadratic term
        """
        models_file = SRC_DIR / "models.py"

        if not models_file.exists():
            pytest.skip("models.py not found")

        # Check for U-shape implementation
        new_matches = scan_file_for_patterns(models_file, FormulaSpec.NEW_USHAPE_PATTERNS)
        old_matches = scan_file_for_patterns(models_file, FormulaSpec.OLD_USHAPE_PATTERNS)

        ushape_implemented = len(new_matches) > 0 or len(old_matches) > 0

        # Check for linear-only (no U-shape)
        linear_matches = scan_file_for_patterns(models_file, FormulaSpec.LINEAR_PATTERNS)

        if not ushape_implemented and len(linear_matches) > 0:
            pytest.fail(
                f"INCONSISTENCY DETECTED:\n"
                f"  - Theory (H1): V(1-V) coefficient > 0 (U-shape)\n"
                f"  - Implementation (models.py): Linear vagueness only\n"
                f"  - Found {len(linear_matches)} linear specifications without U-shape term\n"
                f"\n"
                f"ACTION REQUIRED:\n"
                f"  Add V(1-V) or V**2 term to regression formulas in models.py"
            )

    def test_feature_engineering_has_ushape_term(self):
        """
        Test: features.py should compute U-shape term for regression

        Expected:
            df['vagueness_ushape'] = df['vagueness'] * (1 - df['vagueness']/100)
        or:
            df['vagueness_squared'] = df['vagueness'] ** 2
        """
        features_file = SRC_DIR / "features.py"

        if not features_file.exists():
            pytest.skip("features.py not found")

        content = features_file.read_text()

        # Check for U-shape feature creation
        ushape_patterns = [
            r"vagueness_ushape",
            r"vagueness_squared",
            r"V_ushape",
            r"V_squared",
            r"\*\s*\(1\s*-\s*.*vagueness",
            r"\*\*\s*2",
        ]

        has_ushape_feature = any(re.search(p, content, re.IGNORECASE) for p in ushape_patterns)

        if not has_ushape_feature:
            pytest.fail(
                "FEATURE ENGINEERING MISSING U-SHAPE TERM:\n"
                "  features.py does not compute vagueness_ushape or vagueness_squared\n"
                "\n"
                "ACTION REQUIRED:\n"
                "  Add to engineer_features():\n"
                "    df['vagueness_ushape'] = df['vagueness'] * (100 - df['vagueness']) / 10000\n"
                "  or:\n"
                "    df['vagueness_squared'] = df['vagueness'] ** 2"
            )


class TestPaperSectionConsistency:
    """
    Test that P1/P2/P3 sections are consistent across chapters

    견리사의 見 (관찰): 전체를 조망하며 일관성 확인
    """

    def test_p1_domain_consistency(self):
        """P1 should consistently be about Technology domain"""
        expected_domain = "Technology"

        for chap_file in SCRIPTS_DIR.glob("chap*.py"):
            content = chap_file.read_text()

            # Find P1 domain assignment
            p1_match = re.search(r'P1.*domain.*["\'](\w+)["\']', content, re.IGNORECASE)

            if p1_match:
                found_domain = p1_match.group(1)
                assert found_domain == expected_domain, \
                    f"P1 domain mismatch in {chap_file.name}: expected '{expected_domain}', found '{found_domain}'"

    def test_p2_domain_consistency(self):
        """P2 should consistently be about Organization domain"""
        expected_domain = "Organization"

        for chap_file in SCRIPTS_DIR.glob("chap*.py"):
            content = chap_file.read_text()

            p2_match = re.search(r'P2.*domain.*["\'](\w+)["\']', content, re.IGNORECASE)

            if p2_match:
                found_domain = p2_match.group(1)
                assert found_domain == expected_domain, \
                    f"P2 domain mismatch in {chap_file.name}: expected '{expected_domain}', found '{found_domain}'"

    def test_p3_domain_consistency(self):
        """P3 should consistently be about Competition domain"""
        expected_domain = "Competition"

        for chap_file in SCRIPTS_DIR.glob("chap*.py"):
            content = chap_file.read_text()

            p3_match = re.search(r'P3.*domain.*["\'](\w+)["\']', content, re.IGNORECASE)

            if p3_match:
                found_domain = p3_match.group(1)
                assert found_domain == expected_domain, \
                    f"P3 domain mismatch in {chap_file.name}: expected '{expected_domain}', found '{found_domain}'"

    def test_emoji_consistency(self):
        """Test that emojis are consistent across all files"""
        expected_emojis = {
            "P1": "✌️",
            "P2": "🦾",  # Updated from 🕳️ → 🪾 → 🦾
            "P3": "🤹"   # Updated from 🧩 → 🤹
        }

        for chap_file in SCRIPTS_DIR.glob("chap*.py"):
            content = chap_file.read_text()

            for paper_id, expected_emoji in expected_emojis.items():
                # Look for paper emoji definition
                pattern = rf'{paper_id}.*emoji.*["\']([^"\']+)["\']'
                match = re.search(pattern, content, re.IGNORECASE)

                if match:
                    found_emoji = match.group(1)
                    assert found_emoji == expected_emoji, \
                        f"Emoji mismatch for {paper_id} in {chap_file.name}: expected '{expected_emoji}', found '{found_emoji}'"


class TestBayesianWorkflowConsistency:
    """
    Test Bayesian workflow role assignments are consistent

    견리사의 순환: 利 → 思 → 義 → 見 → 利
    """

    EXPECTED_ROLES = {
        1: "Prior",        # 정운 - 起
        2: "Likelihood",   # 권준 - 承
        3: "Calibration",  # 김완/나대용 - 轉
        4: "Generator",    # 어영담 - 結
    }

    def test_chapter_bayesian_roles(self):
        """Each chapter should have correct Bayesian role"""

        for chap_num, expected_role in self.EXPECTED_ROLES.items():
            chap_file = SCRIPTS_DIR / f"chap{chap_num}_*.py"
            files = list(SCRIPTS_DIR.glob(f"chap{chap_num}_*.py"))

            if not files:
                continue

            chap_file = files[0]
            content = chap_file.read_text()

            # Look for Bayesian role mention
            if expected_role.lower() not in content.lower():
                print(f"Warning: Chapter {chap_num} may be missing '{expected_role}' role reference")


# ============================================================================
# INTEGRATION TEST — Cross-file Consistency
# ============================================================================

class TestCrossFileConsistency:
    """
    Test consistency across multiple files

    통제사의 조망: 전체 함대의 일관성 확인
    """

    def test_vagueness_scorer_matches_models(self):
        """
        Test: Vagueness scoring in vagueness_v2.py should produce values
        compatible with what models.py expects

        If models.py expects normalized [0,1] but vagueness_v2.py outputs [0,100],
        there should be a normalization step in features.py
        """
        vagueness_file = SRC_DIR / "vagueness_v2.py"
        features_file = SRC_DIR / "features.py"

        if not vagueness_file.exists() or not features_file.exists():
            pytest.skip("Required files not found")

        features_content = features_file.read_text()

        # Check for normalization
        normalization_patterns = [
            r"vagueness\s*/\s*100",
            r"minmax",
            r"normalize",
            r"scale",
        ]

        has_normalization = any(re.search(p, features_content, re.IGNORECASE) for p in normalization_patterns)

        # This is informational, not a hard failure
        if not has_normalization:
            print("Note: No explicit vagueness normalization found in features.py")

    def test_plotting_variables_match_models(self):
        """
        Test: Variables used in plotting.py should match those from models.py

        If models.py uses 'z_vagueness', plotting.py should also use 'z_vagueness'
        """
        models_file = SRC_DIR / "models.py"
        plotting_file = SRC_DIR / "plotting.py"

        if not models_file.exists() or not plotting_file.exists():
            pytest.skip("Required files not found")

        models_content = models_file.read_text()
        plotting_content = plotting_file.read_text()

        # Extract variable names from models.py
        model_vars = set(re.findall(r'z_\w+', models_content))
        plot_vars = set(re.findall(r'z_\w+', plotting_content))

        # Variables in models should be available in plotting
        models_only = model_vars - plot_vars

        if models_only:
            print(f"Note: Variables in models.py but not in plotting.py: {models_only}")


# ============================================================================
# SUMMARY REPORT
# ============================================================================

def generate_consistency_report():
    """Generate a summary report of all consistency checks"""

    print("\n" + "=" * 70)
    print("전라좌수군 견리사의 군령 — 일관성 검사 보고서")
    print("Hypothesis-Implementation Consistency Report")
    print("=" * 70)

    checks = [
        ("V² → V(1-V) Migration", "Check if old formula deprecated"),
        ("H1 Formula in Theory", "V(1-V) coefficient > 0 in chap2_theory.py"),
        ("Regression Implementation", "models.py should have U-shape term"),
        ("Feature Engineering", "features.py should compute U-shape feature"),
        ("P1/P2/P3 Domains", "Technology/Organization/Competition"),
        ("Emoji Consistency", "✌️/🦾/🤹 across all files"),
        ("Bayesian Roles", "Prior → Likelihood → Calibration → Generator"),
    ]

    print("\n📋 Consistency Checks:")
    for name, description in checks:
        print(f"  • {name}: {description}")

    print("\n" + "=" * 70)
    print("Run: pytest test/unit/test_hypothesis_consistency.py -v")
    print("=" * 70)


if __name__ == "__main__":
    generate_consistency_report()
    pytest.main([__file__, "-v", "--tb=short"])
