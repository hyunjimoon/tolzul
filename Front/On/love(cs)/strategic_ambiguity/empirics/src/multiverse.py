"""
Multiverse Analysis Module - Specification Curve Analysis
==========================================================

This module implements specification curve analysis (Simonsohn, Simmons & Nelson, 2020)
to test robustness of findings across different analytical choices.

"The Multiverse": All reasonable specifications of your hypothesis test.

Key functions:
1. build_spec_grid(): Generate all specification combinations
2. run_spec_curve(): Execute all specifications
3. plot_spec_curve(): Visualize specification curve
4. summarize_spec_curve(): Statistical summary

Author: Strategic Ambiguity Research Team
Date: 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Callable
from itertools import product
import statsmodels.api as sm
from statsmodels.regression.linear_model import RegressionResultsWrapper
from statsmodels.discrete.discrete_model import BinaryResultsWrapper
import logging

logger = logging.getLogger(__name__)


# =============================================================================
# SPECIFICATION GRID CONSTRUCTION
# =============================================================================

def build_spec_grid(
    vagueness_measures: List[str] = ['z_vagueness', 'z_vagueness_winsorized'],
    outcome_windows: List[int] = [2024, 2025, 2026],
    control_sets: List[Tuple[str, ...]] = [
        ('z_employees_log', 'founding_cohort'),
        ('z_employees_log', 'founding_cohort', 'hq_country'),
        ('z_employees_log', 'founding_cohort', 'sector_fe'),
    ],
    include_interaction_C: List[bool] = [True, False],
    include_control_E: List[bool] = [True, False]
) -> pd.DataFrame:
    """
    Build grid of all specification combinations.

    Args:
        vagueness_measures: Different vagueness operationalizations
        outcome_windows: Different outcome measurement windows
        control_sets: Different control variable combinations
        include_interaction_C: Whether to include credibility interaction
        include_control_E: Whether to include early funding control

    Returns:
        DataFrame with one row per specification

    Example:
        >>> spec_grid = build_spec_grid()
        >>> print(f"Total specifications: {len(spec_grid)}")
        >>> # Run first spec
        >>> spec = spec_grid.iloc[0]
        >>> run_single_spec(data, spec)
    """
    logger.info("Building specification grid...")

    # Generate all combinations
    specs = []
    spec_id = 0

    for vag_measure in vagueness_measures:
        for outcome_window in outcome_windows:
            for controls in control_sets:
                for interact_C in include_interaction_C:
                    for control_E in include_control_E:
                        specs.append({
                            'spec_id': spec_id,
                            'vagueness_measure': vag_measure,
                            'outcome_window': outcome_window,
                            'controls': list(controls),
                            'include_interaction_C': interact_C,
                            'include_control_E': control_E,
                            'n_controls': len(controls) + (1 if control_E else 0)
                        })
                        spec_id += 1

    spec_df = pd.DataFrame(specs)

    logger.info(f"✓ Specification grid built:")
    logger.info(f"   Total specifications: {len(spec_df)}")
    logger.info(f"   Vagueness measures: {len(vagueness_measures)}")
    logger.info(f"   Outcome windows: {len(outcome_windows)}")
    logger.info(f"   Control sets: {len(control_sets)}")

    return spec_df


# =============================================================================
# SINGLE SPECIFICATION EXECUTION
# =============================================================================

def run_single_spec(
    df: pd.DataFrame,
    spec: pd.Series,
    hypothesis: str = 'H2',
    model_func: Optional[Callable] = None
) -> Dict:
    """
    Run a single specification.

    Args:
        df: Data DataFrame
        spec: Specification row from spec_grid
        hypothesis: 'H1' or 'H2'
        model_func: Custom model function (default: use built-in)

    Returns:
        Dictionary with results {coef, se, pval, n_obs, ...}
    """
    try:
        # Extract specification parameters
        vag_measure = spec['vagueness_measure']
        controls = spec['controls']
        include_E = spec['include_control_E']
        include_C_interact = spec['include_interaction_C']

        # Build formula
        outcome = 'L' if hypothesis == 'H2' else 'E_amount_log'

        # Main effects
        predictors = [vag_measure, 'is_software']

        # Interaction (always for H2)
        if hypothesis == 'H2':
            predictors.append(f'{vag_measure}:is_software')

        # Controls
        predictors.extend(controls)

        # Early funding control (only for H2, if specified)
        if hypothesis == 'H2' and include_E:
            predictors.append('E_amount_log')

        # Credibility interaction (if specified)
        if include_C_interact and 'founder_is_serial' in df.columns:
            predictors.append('founder_is_serial')
            if hypothesis == 'H2':
                predictors.append(f'{vag_measure}:founder_is_serial')

        # Build formula string
        formula = f"{outcome} ~ {' + '.join(predictors)}"

        # Prepare data
        model_df = df.dropna(subset=[outcome, vag_measure, 'is_software'] + controls)

        # Fit model
        if hypothesis == 'H2':
            # Logit for binary outcome
            model = sm.Logit.from_formula(formula, data=model_df)
            result = model.fit(disp=False, maxiter=100)
        else:
            # OLS for continuous outcome
            model = sm.OLS.from_formula(formula, data=model_df)
            result = model.fit()

        # Extract key coefficient (interaction for H2, main effect for H1)
        if hypothesis == 'H2':
            key_param = f'{vag_measure}:is_software'
        else:
            key_param = vag_measure

        coef = result.params.get(key_param, np.nan)
        se = result.bse.get(key_param, np.nan)
        pval = result.pvalues.get(key_param, np.nan)

        return {
            'coef': coef,
            'se': se,
            'pval': pval,
            'significant_05': pval < 0.05,
            'significant_10': pval < 0.10,
            'n_obs': result.nobs,
            'formula': formula,
            'success': True,
            'error': None
        }

    except Exception as e:
        logger.warning(f"Spec {spec['spec_id']} failed: {e}")
        return {
            'coef': np.nan,
            'se': np.nan,
            'pval': np.nan,
            'significant_05': False,
            'significant_10': False,
            'n_obs': 0,
            'formula': '',
            'success': False,
            'error': str(e)
        }


# =============================================================================
# MULTIVERSE EXECUTION
# =============================================================================

def run_spec_curve(
    df: pd.DataFrame,
    spec_grid: pd.DataFrame,
    hypothesis: str = 'H2',
    n_jobs: int = 1
) -> pd.DataFrame:
    """
    Run all specifications in the grid.

    Args:
        df: Data DataFrame
        spec_grid: Specification grid from build_spec_grid()
        hypothesis: 'H1' or 'H2'
        n_jobs: Number of parallel jobs (default: 1, no parallelization)

    Returns:
        DataFrame with spec_grid + results columns

    Example:
        >>> spec_grid = build_spec_grid()
        >>> results = run_spec_curve(df, spec_grid, 'H2')
        >>> # How many specs are significant?
        >>> print(f"Significant at p<0.05: {results['significant_05'].sum()}")
    """
    logger.info(f"Running specification curve for {hypothesis}...")
    logger.info(f"   Total specifications: {len(spec_grid)}")

    results_list = []

    for idx, spec_row in spec_grid.iterrows():
        if idx % 10 == 0:
            logger.info(f"   Progress: {idx}/{len(spec_grid)}")

        result = run_single_spec(df, spec_row, hypothesis)
        results_list.append(result)

    # Combine with spec_grid
    results_df = pd.concat([
        spec_grid.reset_index(drop=True),
        pd.DataFrame(results_list)
    ], axis=1)

    # Sort by coefficient (for curve visualization)
    results_df = results_df.sort_values('coef', ascending=False).reset_index(drop=True)

    # Summary statistics
    n_success = results_df['success'].sum()
    n_sig_05 = results_df['significant_05'].sum()
    n_sig_10 = results_df['significant_10'].sum()
    median_coef = results_df['coef'].median()

    logger.info(f"\n✓ Specification curve complete:")
    logger.info(f"   Successful fits: {n_success}/{len(results_df)}")
    logger.info(f"   Significant (p<0.05): {n_sig_05}/{n_success} ({n_sig_05/n_success*100:.1f}%)")
    logger.info(f"   Significant (p<0.10): {n_sig_10}/{n_success} ({n_sig_10/n_success*100:.1f}%)")
    logger.info(f"   Median coefficient: {median_coef:.4f}")

    return results_df


# =============================================================================
# SPECIFICATION CURVE PLOTTING
# =============================================================================

def plot_spec_curve(
    results_df: pd.DataFrame,
    output_path: Optional[Path] = None,
    title: str = "Specification Curve",
    figsize: Tuple[int, int] = (12, 8)
) -> plt.Figure:
    """
    Plot specification curve with analytical choices panel.

    Creates a two-panel figure:
    - Top: Coefficient estimates sorted by magnitude
    - Bottom: Analytical choices for each specification

    Args:
        results_df: Results from run_spec_curve()
        output_path: Where to save figure (optional)
        title: Plot title
        figsize: Figure size

    Returns:
        matplotlib Figure object

    Example:
        >>> results = run_spec_curve(df, spec_grid, 'H2')
        >>> fig = plot_spec_curve(results, Path('outputs/spec_curve.png'))
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=figsize, height_ratios=[2, 1],
                                     sharex=True, gridspec_kw={'hspace': 0.05})

    # Filter successful specs
    success_df = results_df[results_df['success']].copy()
    n_specs = len(success_df)

    if n_specs == 0:
        logger.warning("No successful specifications to plot!")
        return fig

    # Top panel: Coefficient estimates
    x = np.arange(n_specs)

    # Plot coefficients
    colors = ['blue' if sig else 'gray' for sig in success_df['significant_05']]
    ax1.scatter(x, success_df['coef'], c=colors, alpha=0.6, s=20)

    # Confidence intervals
    lower = success_df['coef'] - 1.96 * success_df['se']
    upper = success_df['coef'] + 1.96 * success_df['se']
    ax1.vlines(x, lower, upper, colors='lightgray', alpha=0.3, linewidth=0.5)

    # Reference line at zero
    ax1.axhline(0, color='black', linestyle='--', linewidth=1, alpha=0.5)

    # Median line
    median_coef = success_df['coef'].median()
    ax1.axhline(median_coef, color='red', linestyle='-', linewidth=1.5,
                label=f'Median: {median_coef:.4f}')

    ax1.set_ylabel('Coefficient Estimate', fontsize=12)
    ax1.set_title(title, fontsize=14, fontweight='bold')
    ax1.legend(loc='best')
    ax1.grid(True, alpha=0.3)

    # Bottom panel: Analytical choices
    # Show key specification dimensions
    y_pos = 0
    y_labels = []

    # Vagueness measure
    for measure in success_df['vagueness_measure'].unique():
        mask = success_df['vagueness_measure'] == measure
        ax2.scatter(x[mask], [y_pos] * mask.sum(), marker='|', s=100, c='green')
    y_labels.append('Vagueness\nMeasure')
    y_pos += 1

    # Outcome window
    for window in sorted(success_df['outcome_window'].unique()):
        mask = success_df['outcome_window'] == window
        ax2.scatter(x[mask], [y_pos] * mask.sum(), marker='|', s=100, c='blue')
    y_labels.append('Outcome\nWindow')
    y_pos += 1

    # Controls
    if 'include_control_E' in success_df.columns:
        mask = success_df['include_control_E']
        ax2.scatter(x[mask], [y_pos] * mask.sum(), marker='|', s=100, c='red')
    y_labels.append('Include E\nControl')
    y_pos += 1

    # Credibility interaction
    if 'include_interaction_C' in success_df.columns:
        mask = success_df['include_interaction_C']
        ax2.scatter(x[mask], [y_pos] * mask.sum(), marker='|', s=100, c='orange')
    y_labels.append('Include C\nInteraction')
    y_pos += 1

    ax2.set_yticks(range(len(y_labels)))
    ax2.set_yticklabels(y_labels, fontsize=10)
    ax2.set_xlabel('Specification (sorted by coefficient)', fontsize=12)
    ax2.set_xlim(-5, n_specs + 5)
    ax2.grid(True, axis='x', alpha=0.3)

    plt.tight_layout()

    # Save if path provided
    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(exist_ok=True, parents=True)
        fig.savefig(output_path, dpi=300, bbox_inches='tight')
        logger.info(f"✓ Spec curve saved to: {output_path}")

    return fig


# =============================================================================
# SUMMARY STATISTICS
# =============================================================================

def summarize_spec_curve(results_df: pd.DataFrame) -> Dict:
    """
    Summarize specification curve results.

    Args:
        results_df: Results from run_spec_curve()

    Returns:
        Dictionary with summary statistics
    """
    success_df = results_df[results_df['success']]

    summary = {
        'n_total': len(results_df),
        'n_success': len(success_df),
        'n_significant_05': success_df['significant_05'].sum(),
        'n_significant_10': success_df['significant_10'].sum(),
        'pct_significant_05': success_df['significant_05'].mean() * 100,
        'pct_significant_10': success_df['significant_10'].mean() * 100,
        'median_coef': success_df['coef'].median(),
        'mean_coef': success_df['coef'].mean(),
        'min_coef': success_df['coef'].min(),
        'max_coef': success_df['coef'].max(),
        'sd_coef': success_df['coef'].std(),
        'median_pval': success_df['pval'].median(),
    }

    logger.info("\n" + "=" * 60)
    logger.info("SPECIFICATION CURVE SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Total specifications:        {summary['n_total']}")
    logger.info(f"Successful fits:             {summary['n_success']}")
    logger.info(f"Significant (p<0.05):        {summary['n_significant_05']} ({summary['pct_significant_05']:.1f}%)")
    logger.info(f"Significant (p<0.10):        {summary['n_significant_10']} ({summary['pct_significant_10']:.1f}%)")
    logger.info(f"\nCoefficient statistics:")
    logger.info(f"  Median:                    {summary['median_coef']:.4f}")
    logger.info(f"  Mean:                      {summary['mean_coef']:.4f}")
    logger.info(f"  SD:                        {summary['sd_coef']:.4f}")
    logger.info(f"  Range:                     [{summary['min_coef']:.4f}, {summary['max_coef']:.4f}]")
    logger.info("=" * 60)

    return summary


# =============================================================================
# EXTREME CASE ANALYSIS
# =============================================================================

def identify_extreme_specs(
    results_df: pd.DataFrame,
    n_top: int = 5,
    n_bottom: int = 5
) -> Dict[str, pd.DataFrame]:
    """
    Identify specifications with extreme coefficients.

    Args:
        results_df: Results from run_spec_curve()
        n_top: Number of top specs to return
        n_bottom: Number of bottom specs to return

    Returns:
        Dictionary with 'top' and 'bottom' DataFrames
    """
    success_df = results_df[results_df['success']].copy()

    top_specs = success_df.nlargest(n_top, 'coef')
    bottom_specs = success_df.nsmallest(n_bottom, 'coef')

    logger.info(f"\n🔝 Top {n_top} specifications (largest coefficients):")
    for idx, row in top_specs.iterrows():
        logger.info(f"   Spec {row['spec_id']}: coef={row['coef']:.4f}, p={row['pval']:.3f}")

    logger.info(f"\n🔽 Bottom {n_bottom} specifications (smallest coefficients):")
    for idx, row in bottom_specs.iterrows():
        logger.info(f"   Spec {row['spec_id']}: coef={row['coef']:.4f}, p={row['pval']:.3f}")

    return {'top': top_specs, 'bottom': bottom_specs}
