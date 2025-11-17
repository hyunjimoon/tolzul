#!/usr/bin/env python3
"""
Generate Thesis-Specific Figures
=================================
Creates figures needed for thesis production folder that aren't generated
by the main pipeline:

- fig1_tradeoff.pdf: Conceptual VOI vs RO tradeoff
- fig2_architecture.pdf: Conceptual hardware vs software illustration
- fig3_H1_scatter.pdf: Vagueness vs Early Funding scatter plot

Usage:
    python3 thesis_figures.py [dataset]

    dataset: all, quantum, transportation (default: all)
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
import seaborn as sns
import logging
import statsmodels.formula.api as smf

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

# W2 color palette
PALETTE = {
    "E": "red",
    "L": "#0000FF",
    "V": "green",
    "F": "skyblue",
    "HW": "gray"
}


def generate_fig1_tradeoff(output_dir: Path):
    """Generate conceptual figure showing VOI vs RO tradeoff.

    Shows the theoretical tradeoff between:
    - Value of Information (VOI): Specificity helps investors learn
    - Real Options (RO): Vagueness preserves flexibility
    """
    logger.info("📊 Generating fig1_tradeoff.pdf...")

    fig, ax = plt.subplots(figsize=(10, 6))

    # Generate curves
    vagueness = np.linspace(0, 100, 100)

    # VOI: Decreases with vagueness (investors learn less)
    voi = 100 - vagueness + np.random.normal(0, 5, 100)

    # RO: Increases with vagueness (more flexibility)
    ro = vagueness + np.random.normal(0, 5, 100)

    # Plot curves
    ax.plot(vagueness, voi, color=PALETTE['L'], linewidth=3, label='Value of Information (VOI)', alpha=0.8)
    ax.plot(vagueness, ro, color=PALETTE['E'], linewidth=3, label='Real Options (RO)', alpha=0.8)

    # Shade regions
    ax.fill_between(vagueness, 0, voi, color=PALETTE['L'], alpha=0.1)
    ax.fill_between(vagueness, 0, ro, color=PALETTE['E'], alpha=0.1)

    # Mark optimal point (crossover)
    crossover_idx = np.argmin(np.abs(voi - ro))
    crossover_x = vagueness[crossover_idx]
    crossover_y = voi[crossover_idx]
    ax.plot(crossover_x, crossover_y, 'o', color='black', markersize=12, zorder=10)
    ax.annotate('Optimal\nVagueness',
                xy=(crossover_x, crossover_y),
                xytext=(crossover_x + 15, crossover_y + 15),
                fontsize=11, fontweight='bold',
                arrowprops=dict(arrowstyle='->', lw=2, color='black'))

    # Labels
    ax.set_xlabel('Promise Vagueness →', fontsize=14, fontweight='bold')
    ax.set_ylabel('Value', fontsize=14, fontweight='bold')
    ax.set_title('Fig 1: Theoretical Tradeoff - VOI vs Real Options',
                 fontsize=16, fontweight='bold', pad=20)

    # Legend
    ax.legend(loc='center left', fontsize=12, frameon=True, shadow=True)

    # Grid
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 120)

    # Clean up spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()

    # Save
    output_file = output_dir / "fig1_tradeoff.pdf"
    fig.savefig(output_file, dpi=300, bbox_inches='tight')
    logger.info(f"  ✓ Saved: {output_file}")

    plt.close(fig)


def generate_fig2_architecture(output_dir: Path):
    """Generate conceptual figure showing hardware vs software architectures.

    Illustrates:
    - Hardware (Battleship): Integrated, irreversible
    - Software (Lego): Modular, reversible
    """
    logger.info("📊 Generating fig2_architecture.pdf...")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # --- Left: Hardware (Battleship) ---
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.set_aspect('equal')

    # Draw integrated monolithic structure
    battleship = FancyBboxPatch((1, 2), 8, 4, boxstyle="round,pad=0.1",
                                 facecolor='purple', edgecolor='black',
                                 linewidth=3, alpha=0.6)
    ax1.add_patch(battleship)

    # Add internal components (tightly coupled)
    components = [
        Rectangle((2, 3), 1.5, 1.5, facecolor='darkviolet', edgecolor='white', linewidth=2),
        Rectangle((4, 3), 1.5, 1.5, facecolor='darkviolet', edgecolor='white', linewidth=2),
        Rectangle((6, 3), 1.5, 1.5, facecolor='darkviolet', edgecolor='white', linewidth=2),
    ]
    for comp in components:
        ax1.add_patch(comp)

    # Add arrows showing tight coupling
    for i in range(2):
        arrow = FancyArrowPatch((2.75 + i*2, 3.75), (4 + i*2, 3.75),
                               arrowstyle='<->', mutation_scale=20,
                               linewidth=2, color='white')
        ax1.add_patch(arrow)

    ax1.text(5, 7, 'Hardware\n(Battleship)', ha='center', va='top',
             fontsize=16, fontweight='bold', color='purple')
    ax1.text(5, 1, 'Integrated • Irreversible', ha='center', va='top',
             fontsize=11, style='italic', color='purple')

    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['left'].set_visible(False)

    # --- Right: Software (Lego) ---
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.set_aspect('equal')

    # Draw modular blocks
    lego_blocks = [
        Rectangle((1, 6), 1.5, 1.5, facecolor='limegreen', edgecolor='black', linewidth=2),
        Rectangle((3, 6), 1.5, 1.5, facecolor='limegreen', edgecolor='black', linewidth=2),
        Rectangle((5, 6), 1.5, 1.5, facecolor='limegreen', edgecolor='black', linewidth=2),
        Rectangle((7, 6), 1.5, 1.5, facecolor='limegreen', edgecolor='black', linewidth=2),
        Rectangle((2, 4), 1.5, 1.5, facecolor='limegreen', edgecolor='black', linewidth=2),
        Rectangle((4, 4), 1.5, 1.5, facecolor='limegreen', edgecolor='black', linewidth=2),
        Rectangle((6, 4), 1.5, 1.5, facecolor='limegreen', edgecolor='black', linewidth=2),
        Rectangle((3, 2), 1.5, 1.5, facecolor='limegreen', edgecolor='black', linewidth=2),
        Rectangle((5, 2), 1.5, 1.5, facecolor='limegreen', edgecolor='black', linewidth=2),
    ]
    for block in lego_blocks:
        ax2.add_patch(block)

    # Add separation arrows
    arrow1 = FancyArrowPatch((4.5, 5.5), (5.5, 5.5),
                            arrowstyle='<->', mutation_scale=15,
                            linewidth=2, color='darkgreen', linestyle='--')
    ax2.add_patch(arrow1)

    ax2.text(5, 8.5, 'Software\n(Lego)', ha='center', va='top',
             fontsize=16, fontweight='bold', color='darkgreen')
    ax2.text(5, 1, 'Modular • Reversible', ha='center', va='top',
             fontsize=11, style='italic', color='darkgreen')

    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax2.spines['left'].set_visible(False)

    # Overall title
    fig.suptitle('Fig 2: Architecture Types - Integration Cost Moderator',
                 fontsize=16, fontweight='bold', y=0.98)

    plt.tight_layout()

    # Save
    output_file = output_dir / "fig2_architecture.pdf"
    fig.savefig(output_file, dpi=300, bbox_inches='tight')
    logger.info(f"  ✓ Saved: {output_file}")

    plt.close(fig)


def generate_fig3_h1_scatter(df: pd.DataFrame, output_dir: Path, dataset_name: str):
    """Generate H1 scatter plot: Vagueness vs Early Funding.

    Args:
        df: DataFrame with vagueness and early_funding_musd columns
        output_dir: Directory to save figure
        dataset_name: Name of dataset (for title)
    """
    logger.info(f"📊 Generating fig3_H1_scatter.pdf for {dataset_name}...")

    # Filter to companies with Series A funding
    df_h1 = df[df['early_funding_musd'].notna()].copy()

    # Create z-scored variables if they don't exist
    if 'z_vagueness' not in df_h1.columns and 'vagueness' in df_h1.columns:
        v_mean = df_h1['vagueness'].mean()
        v_std = df_h1['vagueness'].std()
        if v_std > 0:
            df_h1['z_vagueness'] = (df_h1['vagueness'] - v_mean) / v_std
        else:
            df_h1['z_vagueness'] = 0

    if 'z_employees_log' not in df_h1.columns and 'employees_log' in df_h1.columns:
        e_mean = df_h1['employees_log'].mean()
        e_std = df_h1['employees_log'].std()
        if e_std > 0:
            df_h1['z_employees_log'] = (df_h1['employees_log'] - e_mean) / e_std
        else:
            df_h1['z_employees_log'] = 0

    # Create founding_cohort if it doesn't exist
    if 'founding_cohort' not in df_h1.columns and 'year_founded' in df_h1.columns:
        bins = [0, 2009, 2014, 2018, 2020, 2021, 9999]
        labels = ['≤2009', '2010-14', '2015-18', '2019-20', '2021', '2022+']
        year_founded = pd.to_numeric(df_h1['year_founded'], errors='coerce')
        df_h1['founding_cohort'] = pd.cut(year_founded, bins=bins, labels=labels, right=True)

    # Drop rows missing required variables
    required_cols = ['z_vagueness', 'z_employees_log', 'founding_cohort']
    df_h1 = df_h1.dropna(subset=required_cols).copy()

    if len(df_h1) == 0:
        logger.warning(f"  ⚠ No companies with Series A funding in {dataset_name}")
        return

    # Fit OLS regression with controls (matching H1 model specification)
    formula = "early_funding_musd ~ z_vagueness + z_employees_log + C(founding_cohort)"
    try:
        model = smf.ols(formula, data=df_h1).fit()
        v_coef = model.params['z_vagueness']
        v_pval = model.pvalues['z_vagueness']
        r_squared = model.rsquared

        # Create prediction line (partial effect of vagueness, holding controls at mean)
        z_v_range = np.linspace(df_h1['z_vagueness'].min(), df_h1['z_vagueness'].max(), 100)
        emp_mean = df_h1['z_employees_log'].mean()
        cohort_mode = df_h1['founding_cohort'].mode()[0]

        pred_data = pd.DataFrame({
            'z_vagueness': z_v_range,
            'z_employees_log': [emp_mean] * len(z_v_range),
            'founding_cohort': [cohort_mode] * len(z_v_range)
        })
        y_pred = model.predict(pred_data)

        # Convert z_vagueness back to raw vagueness scale for visualization
        # z = (x - mean) / std, so x = z * std + mean
        v_mean = df_h1['vagueness'].mean()
        v_std = df_h1['vagueness'].std()
        x_line = z_v_range * v_std + v_mean

    except Exception as e:
        logger.warning(f"  ⚠ Regression failed: {e}, using simple bivariate regression")
        # Fallback to simple regression
        from scipy import stats
        slope, intercept, r_value, v_pval, std_err = stats.linregress(
            df_h1['vagueness'],
            df_h1['early_funding_musd']
        )
        v_coef = slope
        r_squared = r_value**2
        x_line = np.array([df_h1['vagueness'].min(), df_h1['vagueness'].max()])
        y_pred = slope * x_line + intercept

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 7))

    # Scatter plot with transparency
    scatter = ax.scatter(
        df_h1['vagueness'],
        df_h1['early_funding_musd'],
        c=df_h1['is_hardware'],
        cmap='RdYlGn_r',  # Red=HW, Green=SW
        alpha=0.5,
        s=30,
        edgecolors='black',
        linewidths=0.5
    )

    # Plot regression line
    ax.plot(x_line, y_pred, '--', color=PALETTE['E'], linewidth=2.5,
            label=f'OLS (with controls): β={v_coef:.2f}, p={v_pval:.3f}', alpha=0.8)

    # Labels and title
    ax.set_xlabel('Promise Vagueness (V)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Series A Funding ($M)', fontsize=14, fontweight='bold')
    ax.set_title(f'Fig 3: H1 Test - Early Funding vs Vagueness\n({dataset_name} companies)',
                 fontsize=16, fontweight='bold', pad=20)

    # Colorbar for hardware/software
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Architecture Type', fontsize=12)
    cbar.set_ticks([0, 1])
    cbar.set_ticklabels(['Software', 'Hardware'])

    # Legend
    ax.legend(loc='upper right', fontsize=11, frameon=True, shadow=True)

    # Grid
    ax.grid(True, alpha=0.3, linestyle='--')

    # Add hypothesis annotation
    ax.text(0.02, 0.98,
            'H1: β(vagueness) < 0\n(more vague → less funding)\n\nControls: Employees, Cohort',
            transform=ax.transAxes,
            fontsize=10,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # Statistics box
    stats_text = f'N = {len(df_h1):,}\nR² = {r_squared:.3f}'
    ax.text(0.98, 0.02,
            stats_text,
            transform=ax.transAxes,
            fontsize=10,
            verticalalignment='bottom',
            horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

    plt.tight_layout()

    # Save
    output_file = output_dir / "fig3_H1_scatter.pdf"
    fig.savefig(output_file, dpi=300, bbox_inches='tight')
    logger.info(f"  ✓ Saved: {output_file}")

    plt.close(fig)


def main():
    """Generate all thesis-specific figures."""
    logger.info("=" * 80)
    logger.info("GENERATING THESIS-SPECIFIC FIGURES")
    logger.info("=" * 80)

    # Get dataset name from command line
    dataset = sys.argv[1] if len(sys.argv) > 1 else "all"

    logger.info(f"\nDataset: {dataset}")
    logger.info("")

    # Output directory
    output_dir = Path(f"outputs/{dataset}/figures")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate conceptual figures (Theory)
    logger.info("Theory Figures:")
    generate_fig1_tradeoff(output_dir)
    generate_fig2_architecture(output_dir)
    logger.info("")

    # Generate H1 scatter (Empirics_Early)
    logger.info("Empirics_Early Figures:")

    # Load dataset
    dataset_file = Path(f"outputs/{dataset}/dataset.parquet")

    if not dataset_file.exists():
        logger.warning(f"⚠ Dataset not found: {dataset_file}")
        logger.warning("  Run pipeline first: ./run_all.sh")
    else:
        df = pd.read_parquet(dataset_file)
        generate_fig3_h1_scatter(df, output_dir, dataset)

    logger.info("")
    logger.info("=" * 80)
    logger.info("✓ THESIS FIGURES COMPLETE")
    logger.info("=" * 80)
    logger.info("")
    logger.info(f"Output directory: {output_dir}")
    logger.info("")

    return 0


if __name__ == '__main__':
    sys.exit(main())
