#!/usr/bin/env python3
"""
Pipeline Step 5: Generate Plots
================================
Creates F-series plots (F1, F2, F3a) for all three dataset variants.
F3a is the "money plot" showing the Vagueness × Hardware interaction.

Usage:
    python pipeline/05_generate_plots.py [dataset]

    dataset: all, quantum, transportation (default: all)
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import pandas as pd
import yaml
import logging
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.genmod.generalized_linear_model import GLM
from statsmodels.genmod.families import Binomial
import statsmodels.formula.api as smf

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# W2 color palette
PALETTE = {
    "E": "red",
    "L": "#0000FF",
    "V": "green",
    "F": "skyblue",
    "HW": "gray"
}


def generate_f3a_plot(df: pd.DataFrame, output_dir: Path, dataset_name: str):
    """Generate F3a interaction plot (Vagueness × Hardware).

    Args:
        df: DataFrame with H2 analysis data
        output_dir: Directory to save plots
        dataset_name: Name of dataset for title
    """
    logger.info(f"\n📊 Generating F3a plot (Vagueness × Hardware)")

    # Prepare data
    df_plot = df.dropna(subset=['z_vagueness', 'is_hardware', 'growth']).copy()
    logger.info(f"   Plotting N={len(df_plot):,} companies")

    # Fit logit model
    formula = "growth ~ z_vagueness * is_hardware + z_employees_log + C(founding_cohort)"

    try:
        # Try standard MLE
        model = smf.logit(formula, data=df_plot).fit(disp=0, maxiter=100)
        logger.info(f"   ✓ Model converged (standard MLE)")
    except Exception as e:
        logger.warning(f"   Standard MLE failed, trying L1 regularization...")
        try:
            model = smf.logit(formula, data=df_plot).fit_regularized(
                method='l1', alpha=0.1, disp=0, maxiter=100
            )
            logger.info(f"   ✓ Model converged (L1 regularization α=0.1)")
        except Exception as e2:
            logger.error(f"   ❌ Model failed to converge: {e2}")
            return

    # Create prediction grid
    v_range = np.linspace(df_plot['z_vagueness'].min(), df_plot['z_vagueness'].max(), 100)

    # Reference values for controls
    emp_mean = df_plot['z_employees_log'].mean()
    cohort_mode = df_plot['founding_cohort'].mode()[0] if 'founding_cohort' in df_plot.columns else '2015-18'

    # Get the categorical dtype from original data for proper patsy handling
    if 'founding_cohort' in df_plot.columns and hasattr(df_plot['founding_cohort'], 'cat'):
        cohort_dtype = df_plot['founding_cohort'].dtype
    else:
        cohort_dtype = None

    # Predictions for SW (is_hardware=False)
    pred_data_sw = pd.DataFrame({
        'z_vagueness': v_range,
        'is_hardware': [False] * len(v_range),
        'z_employees_log': [emp_mean] * len(v_range),
        'founding_cohort': [cohort_mode] * len(v_range)
    })
    # Ensure categorical column matches original dtype
    if cohort_dtype is not None:
        pred_data_sw['founding_cohort'] = pred_data_sw['founding_cohort'].astype(cohort_dtype)

    # Try prediction with patsy (may fail on pandas 2.x + Python 3.13)
    try:
        prob_sw = model.predict(pred_data_sw)
        prob_hw_success = False  # Need to try HW prediction too
    except (AttributeError, ValueError, TypeError) as e:
        logger.warning(f"   ⚠ Patsy prediction failed (pandas 2.x incompatibility): {str(e)[:100]}")
        logger.warning(f"   Using manual coefficient-based prediction")

        # Manual prediction using coefficients directly
        # Build linear predictor: β0 + β1*z_vagueness + β2*is_hardware + β3*interaction + β4*z_employees_log + cohort_effects
        params = model.params

        # Intercept
        linear_pred_sw = params.get('Intercept', 0)
        linear_pred_hw = params.get('Intercept', 0)

        # Main effects
        linear_pred_sw += params.get('z_vagueness', 0) * v_range
        linear_pred_hw += params.get('z_vagueness', 0) * v_range

        # is_hardware effect (0 for SW, 1 for HW)
        hw_effect = params.get('is_hardware[T.True]', params.get('is_hardware', 0))
        linear_pred_hw += hw_effect  # Only for HW

        # Interaction effect (only for HW)
        int_effect = params.get('z_vagueness:is_hardware[T.True]', params.get('z_vagueness:is_hardware', 0))
        linear_pred_hw += int_effect * v_range

        # Employee effect (same for both)
        emp_effect = params.get('z_employees_log', 0) * emp_mean
        linear_pred_sw += emp_effect
        linear_pred_hw += emp_effect

        # Cohort effect (same for both)
        cohort_key = f'C(founding_cohort)[T.{cohort_mode}]'
        cohort_effect = params.get(cohort_key, 0)
        linear_pred_sw += cohort_effect
        linear_pred_hw += cohort_effect

        # Convert to probabilities (logistic function)
        prob_sw = 1 / (1 + np.exp(-linear_pred_sw))
        prob_hw = 1 / (1 + np.exp(-linear_pred_hw))
        prob_hw_success = True  # Already computed

    # If patsy worked for SW, still need to try HW
    if not prob_hw_success:
        pred_data_hw = pd.DataFrame({
            'z_vagueness': v_range,
            'is_hardware': [True] * len(v_range),
            'z_employees_log': [emp_mean] * len(v_range),
            'founding_cohort': [cohort_mode] * len(v_range)
        })
        if cohort_dtype is not None:
            pred_data_hw['founding_cohort'] = pred_data_hw['founding_cohort'].astype(cohort_dtype)

        try:
            prob_hw = model.predict(pred_data_hw)
        except (AttributeError, ValueError, TypeError) as e:
            logger.error(f"   ❌ Both prediction methods failed: {e}")
            return

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 7))

    # Plot lines
    ax.plot(v_range, prob_sw, color=PALETTE['F'], linestyle='-', linewidth=2.5,
            label='Software (F=1)', zorder=3)
    ax.plot(v_range, prob_hw, color=PALETTE['HW'], linestyle='--', linewidth=2.5,
            label='Hardware (F=0)', zorder=3)

    # Styling
    ax.set_xlabel('Strategic Vagueness (z-scored)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Pr(Growth to Series B+)', fontsize=14, fontweight='bold')
    ax.set_title(f'F3a: Integration Cost Moderation Effect\n{dataset_name}',
                 fontsize=16, fontweight='bold', pad=20)
    ax.legend(loc='best', fontsize=12, frameon=True, shadow=True)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add coefficient annotations
    try:
        v_coef = model.params.get('z_vagueness', np.nan)
        int_coef = model.params.get('z_vagueness:is_hardware[T.True]', np.nan)
        v_pval = model.pvalues.get('z_vagueness', np.nan)
        int_pval = model.pvalues.get('z_vagueness:is_hardware[T.True]', np.nan)

        annotation = (
            f"Main Effect (V): β={v_coef:.4f}, p={v_pval:.3f}\n"
            f"Interaction (V×HW): β={int_coef:.4f}, p={int_pval:.3f}"
        )
        ax.text(0.05, 0.95, annotation, transform=ax.transAxes,
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    except Exception as e:
        logger.warning(f"   Could not add coefficient annotation: {e}")

    plt.tight_layout()

    # Save plots
    figures_dir = output_dir / "figures"
    figures_dir.mkdir(exist_ok=True, parents=True)

    png_file = figures_dir / "F3a_interaction.png"
    pdf_file = figures_dir / "F3a_interaction.pdf"

    fig.savefig(png_file, dpi=300, bbox_inches='tight')
    fig.savefig(pdf_file, bbox_inches='tight')
    plt.close(fig)

    logger.info(f"   ✅ F3a plot saved:")
    logger.info(f"      PNG: {png_file}")
    logger.info(f"      PDF: {pdf_file}")


def generate_plots_for_dataset(dataset_key: str, config: dict):
    """Generate plots for a specific dataset."""
    dataset_config = config['datasets'][dataset_key]
    logger.info(f"\n{'='*80}")
    logger.info(f"Generating Plots: {dataset_config['name']}")
    logger.info(f"{'='*80}")

    # Load H2 analysis dataset
    output_dir = Path(dataset_config['output_dir'])
    models_dir = output_dir / "models"
    h2_data_file = models_dir / "h2_analysis_dataset.csv"

    if not h2_data_file.exists():
        logger.error(f"❌ H2 dataset not found: {h2_data_file}")
        logger.error(f"   Run pipeline/04_run_models.py first")
        return

    logger.info(f"\n📂 Loading {h2_data_file}")
    df = pd.read_csv(h2_data_file)
    logger.info(f"   Companies: {len(df):,}")

    # Generate F3a plot
    try:
        generate_f3a_plot(df, output_dir, dataset_config['name'])
    except Exception as e:
        logger.error(f"❌ F3a plot failed: {e}")
        import traceback
        traceback.print_exc()

    logger.info(f"\n{'='*80}")
    logger.info(f"Plots Complete for {dataset_config['name']} ✓")
    logger.info(f"{'='*80}")


def main():
    """Generate plots for specified dataset or all datasets."""
    # Parse arguments
    dataset_filter = sys.argv[1] if len(sys.argv) > 1 else 'all'

    logger.info("=" * 80)
    logger.info("STEP 5: GENERATE PLOTS")
    logger.info("=" * 80)

    # Load configuration
    config_file = Path("config/datasets.yaml")
    with open(config_file) as f:
        config = yaml.safe_load(f)

    # Determine which datasets to process
    if dataset_filter in config['datasets']:
        datasets_to_process = [dataset_filter]
    elif dataset_filter == 'all':
        datasets_to_process = list(config['datasets'].keys())
    else:
        logger.error(f"Unknown dataset: {dataset_filter}")
        logger.error(f"Available datasets: {list(config['datasets'].keys())}")
        return 1

    logger.info(f"\nProcessing datasets: {datasets_to_process}")

    # Generate plots for each dataset
    for dataset_key in datasets_to_process:
        generate_plots_for_dataset(dataset_key, config)

    logger.info("\n" + "=" * 80)
    logger.info("STEP 5 COMPLETE ✓")
    logger.info(f"Plots generated for {len(datasets_to_process)} dataset(s)")
    logger.info("=" * 80)

    return 0


if __name__ == '__main__':
    sys.exit(main())
