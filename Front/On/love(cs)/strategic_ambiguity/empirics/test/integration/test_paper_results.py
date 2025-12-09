#!/usr/bin/env python3
"""
Integration Tests for Paper Results Reproduction
=================================================
Tests that verify published paper results can be reproduced from code.

Each test corresponds to a specific Table or Figure in the paper.

Modules covered:
- #23: H1 - Early Funding Penalty (Table 1, Figure 2)
- #24: H2 - Later Success Benefit (Table 2, Figure 3)
- #25: H2a - V×F Interaction (Figure 3)
"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))

import pandas as pd
import numpy as np
from models import run_h1_early_funding, run_h2_main_growth


# ============================================
# Paper Constants (Update with actual values)
# ============================================

class PaperConstants:
    """Constants from published paper for validation."""

    # Table 1: H1 Early Funding Regression
    # TODO: Update these with actual paper values
    TABLE1_VAGUENESS_COEF = -0.234  # Placeholder
    TABLE1_VAGUENESS_SE = 0.089     # Placeholder
    TABLE1_VAGUENESS_PVAL = 0.009   # Placeholder
    TABLE1_N_OBS = 450              # Placeholder
    TABLE1_R_SQUARED = 0.156        # Placeholder

    # Table 2: H2 Later Success Logit
    TABLE2_VAGUENESS_COEF = 0.456   # Placeholder
    TABLE2_VAGUENESS_SE = 0.112     # Placeholder
    TABLE2_INTERACTION_COEF = -0.321  # Placeholder
    TABLE2_INTERACTION_SE = 0.145   # Placeholder
    TABLE2_N_OBS = 450              # Placeholder

    # Sample sizes
    TOTAL_COMPANIES = 500           # Placeholder
    QUANTUM_COMPANIES = 450         # Placeholder

    # Tolerance for numerical comparisons
    COEF_TOLERANCE = 0.01  # Coefficients within 1%
    SE_TOLERANCE = 0.02    # Standard errors within 2%
    N_TOLERANCE = 5        # Sample size within 5 observations


# ============================================
# Module #23: H1 - Early Funding Penalty
# ============================================

@pytest.mark.integration
@pytest.mark.slow
class TestTable1_H1_EarlyFunding:
    """Tests for Table 1: H1 regression results."""

    @pytest.fixture(scope='class')
    def analysis_data(self):
        """
        Load analysis dataset.

        TODO: Replace with actual data loading logic
        For now, use test fixture from conftest.py
        """
        # In production:
        # from features import consolidate_company_snapshots, engineer_features
        # df = consolidate_company_snapshots('data/raw')
        # df = engineer_features(df)
        # df = df[df.sector_fe == 'quantum']  # Filter to quantum sector
        # return df

        # For testing:
        pytest.skip("Requires actual data - replace with real data loading")

    def test_table1_sample_size(self, analysis_data):
        """Table 1: Verify sample size matches paper."""
        result = run_h1_early_funding(analysis_data)

        assert abs(result.nobs - PaperConstants.TABLE1_N_OBS) <= PaperConstants.N_TOLERANCE, \
            f"Sample size mismatch: {result.nobs} vs {PaperConstants.TABLE1_N_OBS} (paper)"

    def test_table1_vagueness_coefficient(self, analysis_data):
        """Table 1: Verify vagueness coefficient matches paper."""
        result = run_h1_early_funding(analysis_data)

        coef = result.params['z_vagueness']
        paper_coef = PaperConstants.TABLE1_VAGUENESS_COEF

        pct_diff = abs((coef - paper_coef) / paper_coef)

        assert pct_diff < PaperConstants.COEF_TOLERANCE, \
            f"Vagueness coefficient mismatch: {coef:.3f} vs {paper_coef:.3f} (paper)"

    def test_table1_vagueness_stderr(self, analysis_data):
        """Table 1: Verify vagueness standard error matches paper."""
        result = run_h1_early_funding(analysis_data)

        se = result.bse['z_vagueness']
        paper_se = PaperConstants.TABLE1_VAGUENESS_SE

        pct_diff = abs((se - paper_se) / paper_se)

        assert pct_diff < PaperConstants.SE_TOLERANCE, \
            f"Vagueness SE mismatch: {se:.3f} vs {paper_se:.3f} (paper)"

    def test_table1_vagueness_significant(self, analysis_data):
        """Table 1: Verify vagueness coefficient is statistically significant."""
        result = run_h1_early_funding(analysis_data)

        pval = result.pvalues['z_vagueness']

        assert pval < 0.05, \
            f"Vagueness not significant: p={pval:.3f} (expected < 0.05)"

    def test_table1_rsquared(self, analysis_data):
        """Table 1: Verify R² matches paper (approximately)."""
        result = run_h1_early_funding(analysis_data)

        r2 = result.rsquared
        paper_r2 = PaperConstants.TABLE1_R_SQUARED

        # Allow larger tolerance for R² (can vary with rounding)
        assert abs(r2 - paper_r2) < 0.05, \
            f"R² mismatch: {r2:.3f} vs {paper_r2:.3f} (paper)"


# ============================================
# Module #24-25: H2 - Later Success & Interaction
# ============================================

@pytest.mark.integration
@pytest.mark.slow
class TestTable2_H2_LaterSuccess:
    """Tests for Table 2: H2 logit regression results."""

    @pytest.fixture(scope='class')
    def analysis_data(self):
        """Load analysis dataset."""
        pytest.skip("Requires actual data - replace with real data loading")

    def test_table2_sample_size(self, analysis_data):
        """Table 2: Verify sample size matches paper."""
        result = run_h2_main_growth(analysis_data)

        assert abs(result.nobs - PaperConstants.TABLE2_N_OBS) <= PaperConstants.N_TOLERANCE, \
            f"Sample size mismatch: {result.nobs} vs {PaperConstants.TABLE2_N_OBS} (paper)"

    def test_table2_vagueness_main_effect(self, analysis_data):
        """Table 2: Verify vagueness main effect matches paper."""
        result = run_h2_main_growth(analysis_data)

        coef = result.params['z_vagueness']
        paper_coef = PaperConstants.TABLE2_VAGUENESS_COEF

        pct_diff = abs((coef - paper_coef) / paper_coef)

        assert pct_diff < PaperConstants.COEF_TOLERANCE, \
            f"Vagueness main effect mismatch: {coef:.3f} vs {paper_coef:.3f} (paper)"

    def test_table2_interaction_effect(self, analysis_data):
        """Table 2 (Module #25): Verify V×F interaction matches paper."""
        result = run_h2_main_growth(analysis_data)

        # Find interaction term (may be 'z_vagueness:is_hardware' or similar)
        interaction_params = [p for p in result.params.index
                              if 'z_vagueness' in p and 'is_hardware' in p]

        assert len(interaction_params) > 0, \
            "Interaction term not found in model"

        coef = result.params[interaction_params[0]]
        paper_coef = PaperConstants.TABLE2_INTERACTION_COEF

        pct_diff = abs((coef - paper_coef) / abs(paper_coef))

        assert pct_diff < PaperConstants.COEF_TOLERANCE, \
            f"Interaction coefficient mismatch: {coef:.3f} vs {paper_coef:.3f} (paper)"

    def test_table2_interaction_significant(self, analysis_data):
        """Table 2: Verify interaction is statistically significant."""
        result = run_h2_main_growth(analysis_data)

        interaction_params = [p for p in result.params.index
                              if 'z_vagueness' in p and 'is_hardware' in p]

        pval = result.pvalues[interaction_params[0]]

        assert pval < 0.05, \
            f"Interaction not significant: p={pval:.3f} (expected < 0.05)"


# ============================================
# Figure Reproduction Tests
# ============================================

@pytest.mark.integration
@pytest.mark.slow
class TestFigureReproduction:
    """Tests for reproducing paper figures."""

    @pytest.fixture(scope='class')
    def analysis_data(self):
        """Load analysis dataset."""
        pytest.skip("Requires actual data - replace with real data loading")

    def test_figure2_evf_generated(self, analysis_data):
        """
        Figure 2: E-V-F relationship plot generation.

        Module #23: Early funding penalty visualization
        """
        # TODO: Implement figure generation
        # from plotting import plot_figure2_evf
        # fig_path = plot_figure2_evf(analysis_data)
        # assert Path(fig_path).exists()
        # assert Path(fig_path).stat().st_size > 10000

        pytest.skip("Figure generation not yet implemented")

    def test_figure3_interaction_generated(self, analysis_data):
        """
        Figure 3: L-V-F interaction plot generation.

        Module #24-25: Later success benefit with V×F interaction
        """
        # TODO: Implement figure generation
        # from plotting import plot_figure3_lvf_interaction
        # fig_path = plot_figure3_lvf_interaction(analysis_data)
        # assert Path(fig_path).exists()

        pytest.skip("Figure generation not yet implemented")

    def test_figure4_stv_trajectory(self, analysis_data):
        """
        Figure 4: S-T-V trajectory plot generation.

        Module #24: Step-up trajectories over time
        """
        pytest.skip("Figure generation not yet implemented")


# ============================================
# Cross-Table Consistency Tests
# ============================================

@pytest.mark.integration
class TestCrossTableConsistency:
    """Tests that check consistency across multiple tables/results."""

    @pytest.fixture(scope='class')
    def analysis_data(self):
        """Load analysis dataset."""
        pytest.skip("Requires actual data - replace with real data loading")

    def test_same_sample_size_across_tables(self, analysis_data):
        """Table 1 and Table 2 should use same sample (if claimed in paper)."""
        h1_result = run_h1_early_funding(analysis_data)
        h2_result = run_h2_main_growth(analysis_data)

        # If paper claims same sample for both analyses
        # assert h1_result.nobs == h2_result.nobs

        pytest.skip("Requires actual data")

    def test_control_variables_consistent(self, analysis_data):
        """Control variables should have consistent effects across models."""
        h1_result = run_h1_early_funding(analysis_data)
        h2_result = run_h2_main_growth(analysis_data)

        # Example: is_hardware should have consistent sign across models
        # h1_hw_coef = h1_result.params['is_hardware']
        # h2_hw_coef = h2_result.params['is_hardware']
        # assert np.sign(h1_hw_coef) == np.sign(h2_hw_coef)

        pytest.skip("Requires actual data")


# ============================================
# Helper: Generate Paper-Ready Tables
# ============================================

def generate_table1_latex(result, output_path='outputs/table1.tex'):
    """
    Generate LaTeX code for Table 1.

    Args:
        result: Statsmodels regression result
        output_path: Where to save .tex file

    Returns:
        LaTeX string
    """
    # Use statsmodels summary_latex
    latex = result.summary().as_latex()

    # Save to file
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(latex)

    return latex


def generate_table2_latex(result, output_path='outputs/table2.tex'):
    """
    Generate LaTeX code for Table 2.

    Args:
        result: Statsmodels logit result
        output_path: Where to save .tex file

    Returns:
        LaTeX string
    """
    latex = result.summary().as_latex()

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(latex)

    return latex


# ============================================
# Pytest Markers for Organization
# ============================================

# Run only paper reproduction tests:
# pytest test/integration/test_paper_results.py -m integration

# Run only Table 1 tests:
# pytest test/integration/test_paper_results.py::TestTable1_H1_EarlyFunding -v

# Run all except slow tests:
# pytest test/integration/test_paper_results.py -m "not slow"
