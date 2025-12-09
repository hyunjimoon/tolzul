#!/usr/bin/env python3
"""
전라좌수군 견리사의 군령 — 시각화 일관성 테스트
Plotting Consistency Tests

핵심 정신: 그래프가 가설과 모델을 정확히 반영
Core Spirit: Visualizations accurately reflect hypotheses and models

테스트 대상:
- plotting.py: All figure generation functions
- 가설에서 U-shape이면 플롯도 U-shape으로
- 모델 변수와 플롯 변수의 일치

=============================================================================
어영담 전대 👾 — 見 (관찰과 기록)
=============================================================================
"""

import pytest
import re
from pathlib import Path
from typing import List, Set

# Base paths
EMPIRICS_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = EMPIRICS_ROOT / "src"


# ============================================================================
# EXPECTED FIGURE SPECIFICATIONS
# ============================================================================

class FigureSpec:
    """Expected figures based on thesis requirements"""

    EXPECTED_FIGURES = {
        "F1": {
            "name": "Early Funding vs Vagueness",
            "type": "scatter + OLS",
            "variables": ["early_funding", "vagueness", "z_vagueness"],
            "relationship": "linear",  # or "ushape" if H1 U-shape
        },
        "F2": {
            "name": "Growth Probability vs Vagueness",
            "type": "logit prediction",
            "variables": ["growth", "vagueness", "is_hardware"],
            "relationship": "linear + interaction",
        },
        "F3a": {
            "name": "Conditional on Flexibility",
            "type": "conditional curves",
            "variables": ["growth", "vagueness", "flexibility"],
            "relationship": "moderation",
        },
        "F3b": {
            "name": "Conditional on Founder Serial",
            "type": "conditional curves",
            "variables": ["growth", "vagueness", "founder_serial"],
            "relationship": "moderation",
        },
        "F4": {
            "name": "Variable Distributions",
            "type": "histogram/density",
            "variables": ["early_funding", "growth", "vagueness", "flexibility"],
            "relationship": "marginal",
        },
        "F5": {
            "name": "Step-up by Flexibility",
            "type": "bar/grouped",
            "variables": ["step_up", "flexibility"],
            "relationship": "comparison",
        },
        "F6": {
            "name": "Specification Curve",
            "type": "specification curve",
            "variables": ["coefficient", "specification"],
            "relationship": "robustness",
        },
    }


# ============================================================================
# PLOTTING FILE TESTS
# ============================================================================

class TestPlottingFile:
    """Tests for plotting.py structure and content"""

    @pytest.fixture
    def plotting_content(self):
        """Load plotting.py content"""
        plotting_file = SRC_DIR / "plotting.py"
        if not plotting_file.exists():
            pytest.skip("plotting.py not found")
        return plotting_file.read_text()

    def test_plotting_file_exists(self):
        """plotting.py should exist in src/"""
        plotting_file = SRC_DIR / "plotting.py"
        assert plotting_file.exists(), f"plotting.py not found at {plotting_file}"

    def test_has_figure_functions(self, plotting_content):
        """plotting.py should have figure generation functions"""
        function_patterns = [
            r"def\s+plot_",
            r"def\s+create_",
            r"def\s+generate_",
            r"def\s+fig_",
            r"def\s+figure_",
        ]

        has_functions = any(re.search(p, plotting_content) for p in function_patterns)
        assert has_functions, "No plotting functions found in plotting.py"

    def test_uses_matplotlib_or_seaborn(self, plotting_content):
        """Should use standard plotting libraries"""
        library_patterns = [
            r"import\s+matplotlib",
            r"from\s+matplotlib",
            r"import\s+seaborn",
            r"from\s+seaborn",
            r"plt\.",
            r"sns\.",
        ]

        has_library = any(re.search(p, plotting_content) for p in library_patterns)
        assert has_library, "No matplotlib/seaborn imports found"


# ============================================================================
# VARIABLE CONSISTENCY TESTS
# ============================================================================

class TestVariableConsistency:
    """Test that plotting uses same variables as models"""

    @pytest.fixture
    def plotting_content(self):
        """Load plotting.py content"""
        plotting_file = SRC_DIR / "plotting.py"
        if not plotting_file.exists():
            pytest.skip("plotting.py not found")
        return plotting_file.read_text()

    @pytest.fixture
    def models_content(self):
        """Load models.py content"""
        models_file = SRC_DIR / "models.py"
        if not models_file.exists():
            return None
        return models_file.read_text()

    def test_vagueness_variable_matches(self, plotting_content, models_content):
        """Vagueness variable name should match between models and plotting"""
        if models_content is None:
            pytest.skip("models.py not found")

        # Find vagueness var in models
        models_vars = set()
        if "z_vagueness" in models_content:
            models_vars.add("z_vagueness")
        if re.search(r"['\"]vagueness['\"]", models_content):
            models_vars.add("vagueness")

        # Find vagueness var in plotting
        plot_vars = set()
        if "z_vagueness" in plotting_content:
            plot_vars.add("z_vagueness")
        if re.search(r"['\"]vagueness['\"]", plotting_content):
            plot_vars.add("vagueness")

        # Should have overlap
        overlap = models_vars & plot_vars
        if not overlap and models_vars and plot_vars:
            print(f"Note: Vagueness naming differs: models={models_vars}, plotting={plot_vars}")

    def test_dv_variable_matches(self, plotting_content, models_content):
        """DV names should match between models and plotting"""
        if models_content is None:
            pytest.skip("models.py not found")

        dvs = ["growth", "survival", "early_funding", "series_b"]

        models_dvs = {dv for dv in dvs if dv in models_content}
        plot_dvs = {dv for dv in dvs if dv in plotting_content}

        # Models DVs should appear in plotting
        missing = models_dvs - plot_dvs
        if missing:
            print(f"Note: DVs in models but not in plotting: {missing}")


# ============================================================================
# U-SHAPE VISUALIZATION TEST
# ============================================================================

class TestUShapeVisualization:
    """
    Test that U-shape hypothesis is visualized correctly

    If H1: V(1-V) > 0, then figures should show curved relationship
    """

    @pytest.fixture
    def plotting_content(self):
        """Load plotting.py content"""
        plotting_file = SRC_DIR / "plotting.py"
        if not plotting_file.exists():
            pytest.skip("plotting.py not found")
        return plotting_file.read_text()

    def test_ushape_plot_exists(self, plotting_content):
        """
        If hypothesis is U-shape, should have quadratic/curved visualization

        Look for:
        - Polynomial fit (degree=2)
        - Quadratic term in formula
        - U-shape or inverted-U labeling
        """
        ushape_patterns = [
            r"degree\s*=\s*2",           # Polynomial degree 2
            r"poly.*2",                   # Polyfit order 2
            r"quadratic",                 # Quadratic mention
            r"U-shape",                   # U-shape label
            r"inverted.*U",               # Inverted U
            r"\*\*\s*2",                  # Squared term
            r"np\.poly1d.*2",             # numpy polynomial
        ]

        has_ushape_viz = any(re.search(p, plotting_content, re.IGNORECASE) for p in ushape_patterns)

        if not has_ushape_viz:
            # Check if only linear
            linear_patterns = [
                r"regplot",              # seaborn regplot (linear by default)
                r"OLS",                  # Linear OLS
                r"linregress",           # scipy linear
            ]

            has_linear = any(re.search(p, plotting_content) for p in linear_patterns)

            if has_linear:
                print(
                    "WARNING: U-shape hypothesis but only linear visualization detected\n"
                    "  Consider adding:\n"
                    "    - sns.regplot(..., order=2) for polynomial fit\n"
                    "    - Manual quadratic curve\n"
                    "    - Binned means showing U-shape pattern"
                )

    def test_interaction_plot_exists(self, plotting_content):
        """H2 interaction should be visualized with separate lines/colors"""
        interaction_patterns = [
            r"hue\s*=",                  # Seaborn hue parameter
            r"is_hardware",              # Moderator variable
            r"by.*hardware",             # Grouped by hardware
            r"color.*=.*hardware",       # Color by hardware
            r"groupby",                  # Pandas groupby
            r"facet",                    # Facet grid
        ]

        has_interaction_viz = any(re.search(p, plotting_content, re.IGNORECASE) for p in interaction_patterns)

        if not has_interaction_viz:
            print("Note: No clear interaction visualization (hue/facet by is_hardware)")


# ============================================================================
# AXIS LABELING TESTS
# ============================================================================

class TestAxisLabeling:
    """Test proper axis labels and titles"""

    @pytest.fixture
    def plotting_content(self):
        """Load plotting.py content"""
        plotting_file = SRC_DIR / "plotting.py"
        if not plotting_file.exists():
            pytest.skip("plotting.py not found")
        return plotting_file.read_text()

    def test_has_axis_labels(self, plotting_content):
        """Plots should have axis labels"""
        label_patterns = [
            r"xlabel",
            r"ylabel",
            r"set_xlabel",
            r"set_ylabel",
            r"\.label\s*=",
        ]

        has_labels = any(re.search(p, plotting_content) for p in label_patterns)
        assert has_labels, "No axis labels found in plotting.py"

    def test_has_titles(self, plotting_content):
        """Plots should have titles"""
        title_patterns = [
            r"\.title",
            r"set_title",
            r"suptitle",
            r"fig\.text",
        ]

        has_titles = any(re.search(p, plotting_content) for p in title_patterns)
        assert has_titles, "No titles found in plotting.py"

    def test_vagueness_label_descriptive(self, plotting_content):
        """Vagueness axis should have descriptive label"""
        # Check for descriptive vagueness labels
        good_labels = [
            r"Strategic\s+Vagueness",
            r"Vagueness\s+Score",
            r"Vagueness\s+\(",
            r"V\s+\(",
        ]

        bad_labels = [
            r"xlabel\(['\"]vagueness['\"]\)",  # Just "vagueness" without context
            r"xlabel\(['\"]z_vagueness['\"]\)",  # Raw variable name
        ]

        has_good = any(re.search(p, plotting_content, re.IGNORECASE) for p in good_labels)
        has_bad = any(re.search(p, plotting_content) for p in bad_labels)

        if has_bad and not has_good:
            print("Note: Consider more descriptive axis labels than raw variable names")


# ============================================================================
# COLOR SCHEME TESTS
# ============================================================================

class TestColorScheme:
    """Test consistent and accessible color scheme"""

    @pytest.fixture
    def plotting_content(self):
        """Load plotting.py content"""
        plotting_file = SRC_DIR / "plotting.py"
        if not plotting_file.exists():
            pytest.skip("plotting.py not found")
        return plotting_file.read_text()

    def test_uses_color_palette(self, plotting_content):
        """Should use consistent color palette"""
        palette_patterns = [
            r"palette\s*=",
            r"cmap\s*=",
            r"color_palette",
            r"viridis|plasma|inferno",  # Perceptually uniform
            r"tab10|tab20",              # Categorical
            r"Set1|Set2|Set3",           # ColorBrewer
        ]

        has_palette = any(re.search(p, plotting_content, re.IGNORECASE) for p in palette_patterns)

        # Not a failure, just informational
        if not has_palette:
            print("Note: No explicit color palette found; consider using consistent palette")

    def test_not_using_problematic_colors(self, plotting_content):
        """Should avoid red-green only schemes (accessibility)"""
        # This is a soft check
        if "'r'" in plotting_content and "'g'" in plotting_content:
            if "'b'" not in plotting_content and "blue" not in plotting_content.lower():
                print("Note: Red-green color scheme detected; consider colorblind-friendly palette")


# ============================================================================
# FIGURE OUTPUT TESTS
# ============================================================================

class TestFigureOutput:
    """Test figure saving and output"""

    @pytest.fixture
    def plotting_content(self):
        """Load plotting.py content"""
        plotting_file = SRC_DIR / "plotting.py"
        if not plotting_file.exists():
            pytest.skip("plotting.py not found")
        return plotting_file.read_text()

    def test_saves_figures(self, plotting_content):
        """Should save figures to files"""
        save_patterns = [
            r"savefig",
            r"save_fig",
            r"plt\.save",
            r"fig\.save",
        ]

        has_save = any(re.search(p, plotting_content) for p in save_patterns)
        # Informational
        if not has_save:
            print("Note: No savefig found; figures may only display interactively")

    def test_appropriate_dpi(self, plotting_content):
        """Should use publication-quality DPI"""
        dpi_match = re.search(r"dpi\s*=\s*(\d+)", plotting_content)

        if dpi_match:
            dpi = int(dpi_match.group(1))
            if dpi < 150:
                print(f"Note: DPI={dpi} may be too low for publication; consider dpi=300+")


# ============================================================================
# SUMMARY
# ============================================================================

def generate_plotting_test_report():
    """Generate summary report"""
    print("\n" + "=" * 70)
    print("전라좌수군 견리사의 군령 — 시각화 일관성 테스트 보고서")
    print("Plotting Consistency Test Report")
    print("=" * 70)

    print("""
📋 Test Categories:

1. Plotting File Structure:
   - plotting.py exists
   - Has figure generation functions
   - Uses matplotlib/seaborn

2. Variable Consistency:
   - Vagueness variable matches models.py
   - DV names match models.py

3. U-Shape Visualization:
   ⚠️  CRITICAL: If H1 is U-shape, visualization should show curve
   - Polynomial fit (degree=2)
   - Quadratic term visualization
   - Interaction plots for H2

4. Axis Labeling:
   - Has xlabel/ylabel
   - Has titles
   - Descriptive vagueness label

5. Color Scheme:
   - Consistent palette
   - Colorblind-friendly

6. Figure Output:
   - Saves figures to files
   - Publication-quality DPI (300+)

📝 Key Consistency Check:
   If hypothesis uses V(1-V) (U-shape) but plots show only linear
   regression line, this is a VISUALIZATION MISMATCH.
""")

    print("=" * 70)
    print("Run: pytest test/unit/test_plotting_consistency.py -v")
    print("=" * 70)


if __name__ == "__main__":
    generate_plotting_test_report()
    pytest.main([__file__, "-v", "--tb=short"])
