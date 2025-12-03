#!/usr/bin/env python3
"""
Generate Industry-Specific Plots
=================================
Creates 2 plots for each industry:
1. Vagueness Distribution Histogram
2. Survival Rate by Vagueness Quartile

Usage:
    python -m src.scripts.generate_industry_plots --industries hardware software medtech pharma
    python -m src.scripts.generate_industry_plots --all
"""

import sys
from pathlib import Path
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.data_io import load_dataframe

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Industry colors
INDUSTRY_COLORS = {
    'all': '#2E86AB',
    'quantum': '#A23B72',
    'transportation': '#F18F01',
    'hardware': '#C73E1D',
    'software': '#06A77D',
    'medtech': '#8338EC',
    'pharma': '#FB5607'
}


def plot_vagueness_distribution(df: pd.DataFrame, industry_name: str, output_dir: Path):
    """
    Plot 1: Vagueness Distribution Histogram

    Shows the distribution of vagueness scores across companies in this industry.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Filter valid vagueness scores
    vagueness = df['vagueness'].dropna()

    if len(vagueness) == 0:
        print(f"   ⚠️  No vagueness data for {industry_name}")
        plt.close(fig)
        return

    # Plot histogram with KDE
    ax.hist(vagueness, bins=50, alpha=0.6, color=INDUSTRY_COLORS.get(industry_name.lower().split()[0], '#2E86AB'),
            edgecolor='black', density=True, label='Distribution')

    # Add KDE curve
    from scipy.stats import gaussian_kde
    kde = gaussian_kde(vagueness)
    x_range = np.linspace(vagueness.min(), vagueness.max(), 200)
    ax.plot(x_range, kde(x_range), color='darkred', linewidth=2.5, label='Density')

    # Add statistics
    mean_v = vagueness.mean()
    median_v = vagueness.median()
    std_v = vagueness.std()

    ax.axvline(mean_v, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_v:.1f}')
    ax.axvline(median_v, color='blue', linestyle='--', linewidth=2, label=f'Median: {median_v:.1f}')

    # Labels
    ax.set_xlabel('Vagueness Score (0-100)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Density', fontsize=13, fontweight='bold')
    ax.set_title(f'Vagueness Distribution: {industry_name}\n(N={len(vagueness):,} companies, σ={std_v:.1f})',
                 fontsize=15, fontweight='bold', pad=15)
    ax.legend(loc='best', fontsize=11, frameon=True, shadow=True)
    ax.grid(True, alpha=0.3)

    # Add text box with quartiles
    q25, q50, q75 = vagueness.quantile([0.25, 0.5, 0.75])
    stats_text = f"Quartiles:\nQ1: {q25:.1f}\nQ2: {q50:.1f}\nQ3: {q75:.1f}"
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

    plt.tight_layout()

    # Save
    figures_dir = output_dir / "figures"
    figures_dir.mkdir(exist_ok=True, parents=True)

    png_file = figures_dir / "plot1_vagueness_distribution.png"
    pdf_file = figures_dir / "plot1_vagueness_distribution.pdf"

    fig.savefig(png_file, dpi=300, bbox_inches='tight')
    fig.savefig(pdf_file, bbox_inches='tight')
    plt.close(fig)

    print(f"   ✅ Plot 1 saved: {png_file.name}")
    return png_file, pdf_file


def plot_survival_by_vagueness(df: pd.DataFrame, industry_name: str, output_dir: Path):
    """
    Plot 2: Survival Rate by Vagueness Quartile

    Shows how survival (reaching Series B+) varies across vagueness quartiles.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Filter valid data
    df_valid = df[df['vagueness'].notna() & df['growth'].notna()].copy()

    if len(df_valid) == 0:
        print(f"   ⚠️  No growth data for {industry_name}")
        plt.close(fig)
        return

    # Create vagueness quartiles (handle duplicate bin edges)
    try:
        # Try standard quartiles first
        df_valid['vagueness_quartile'] = pd.qcut(
            df_valid['vagueness'],
            q=4,
            labels=['Q1 (Low)', 'Q2', 'Q3', 'Q4 (High)'],
            duplicates='drop'  # Drop duplicate edges if data is concentrated
        )
    except ValueError:
        # Fallback: Use rank-based quartiles (always works)
        print(f"   ⚠️  Data too concentrated, using rank-based quartiles")
        df_valid['vagueness_rank'] = df_valid['vagueness'].rank(method='first', pct=True)
        df_valid['vagueness_quartile'] = pd.cut(
            df_valid['vagueness_rank'],
            bins=[0, 0.25, 0.5, 0.75, 1.0],
            labels=['Q1 (Low)', 'Q2', 'Q3', 'Q4 (High)'],
            include_lowest=True
        )

    # Calculate survival rate by quartile
    survival_by_q = df_valid.groupby('vagueness_quartile', observed=True)['growth'].agg(['mean', 'count', 'sum'])
    survival_by_q['survival_rate'] = survival_by_q['mean'] * 100
    survival_by_q['se'] = np.sqrt(survival_by_q['mean'] * (1 - survival_by_q['mean']) / survival_by_q['count']) * 100

    # Bar plot
    x_pos = np.arange(len(survival_by_q))
    bars = ax.bar(x_pos, survival_by_q['survival_rate'],
                   color=INDUSTRY_COLORS.get(industry_name.lower().split()[0], '#2E86AB'),
                   alpha=0.7, edgecolor='black', linewidth=1.5)

    # Error bars
    ax.errorbar(x_pos, survival_by_q['survival_rate'], yerr=survival_by_q['se'],
                fmt='none', ecolor='black', capsize=5, capthick=2)

    # Add value labels on bars
    for i, (idx, row) in enumerate(survival_by_q.iterrows()):
        ax.text(i, row['survival_rate'] + row['se'] + 0.5,
                f"{row['survival_rate']:.1f}%\n(n={int(row['count']):,})",
                ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Labels
    ax.set_xlabel('Vagueness Quartile', fontsize=13, fontweight='bold')
    ax.set_ylabel('Survival Rate to Series B+ (%)', fontsize=13, fontweight='bold')
    ax.set_title(f'Survival Rate by Vagueness Level: {industry_name}\n(Total N={len(df_valid):,}, Survivors={int(survival_by_q["sum"].sum()):,})',
                 fontsize=15, fontweight='bold', pad=15)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(survival_by_q.index, fontsize=11)
    ax.grid(True, alpha=0.3, axis='y')
    ax.set_ylim(0, max(survival_by_q['survival_rate']) * 1.3)

    # Add trend line
    from scipy.stats import linregress
    slope, intercept, r_value, p_value, std_err = linregress(x_pos, survival_by_q['survival_rate'])
    trend_line = slope * x_pos + intercept
    ax.plot(x_pos, trend_line, color='red', linestyle='--', linewidth=2.5,
            label=f'Trend (slope={slope:.2f}, p={p_value:.3f})')
    ax.legend(loc='best', fontsize=11, frameon=True, shadow=True)

    # Add interpretation text
    if slope > 0 and p_value < 0.05:
        interpretation = "✓ Higher vagueness → Higher survival"
    elif slope < 0 and p_value < 0.05:
        interpretation = "✗ Higher vagueness → Lower survival"
    else:
        interpretation = "~ No significant trend"

    ax.text(0.98, 0.02, interpretation, transform=ax.transAxes,
            fontsize=11, verticalalignment='bottom', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7),
            fontweight='bold')

    plt.tight_layout()

    # Save
    figures_dir = output_dir / "figures"
    figures_dir.mkdir(exist_ok=True, parents=True)

    png_file = figures_dir / "plot2_survival_by_vagueness.png"
    pdf_file = figures_dir / "plot2_survival_by_vagueness.pdf"

    fig.savefig(png_file, dpi=300, bbox_inches='tight')
    fig.savefig(pdf_file, bbox_inches='tight')
    plt.close(fig)

    print(f"   ✅ Plot 2 saved: {png_file.name}")
    return png_file, pdf_file


def generate_plots_for_industry(industry_key: str, industry_name: str, output_dir: Path):
    """Generate both plots for a single industry."""
    print(f"\n{'='*70}")
    print(f"Generating Plots: {industry_name}")
    print(f"{'='*70}")

    # Check if dataset exists
    dataset_file = output_dir / "dataset.nc"

    if not dataset_file.exists():
        print(f"   ❌ Dataset not found: {dataset_file}")
        print(f"   Run: python -m src.cli filter-datasets")
        return

    # Load data
    print(f"   📂 Loading {dataset_file}")
    df = load_dataframe(dataset_file)
    print(f"   ✓ Loaded {len(df):,} companies")

    # Generate plots
    try:
        plot_vagueness_distribution(df, industry_name, output_dir)
    except Exception as e:
        print(f"   ❌ Plot 1 failed: {e}")

    try:
        plot_survival_by_vagueness(df, industry_name, output_dir)
    except Exception as e:
        print(f"   ❌ Plot 2 failed: {e}")

    print(f"   ✅ Plots saved to {output_dir / 'figures'}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate industry-specific plots',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('--industries', nargs='+',
                        choices=['all', 'quantum', 'transportation', 'hardware', 'software', 'medtech', 'pharma'],
                        help='Which industries to plot')
    parser.add_argument('--all', action='store_true',
                        help='Generate plots for all industries')

    args = parser.parse_args()

    # Determine which industries to process
    if args.all:
        industries = ['hardware', 'software', 'medtech', 'pharma', 'quantum', 'transportation']
    elif args.industries:
        industries = args.industries
    else:
        # Default: all 6 industries
        industries = ['hardware', 'software', 'medtech', 'pharma', 'quantum', 'transportation']

    print("="*70)
    print("INDUSTRY PLOTS GENERATOR")
    print("="*70)
    print(f"Processing {len(industries)} industries: {', '.join(industries)}")

    # Industry metadata
    industry_names = {
        'all': 'All Companies',
        'quantum': 'Quantum Computing',
        'transportation': 'Transportation & Mobility',
        'hardware': 'Hardware (Computer, Semiconductor, Energy)',
        'software': 'Software (SaaS, Applications)',
        'medtech': 'Medical Technology (Devices, Supplies)',
        'pharma': 'Pharmaceutical & Biotech'
    }

    # Generate plots for each industry
    for industry_key in industries:
        output_dir = Path(f"data/outputs/{industry_key}")
        industry_name = industry_names.get(industry_key, industry_key.title())

        generate_plots_for_industry(industry_key, industry_name, output_dir)

    print("\n" + "="*70)
    print(f"✅ COMPLETE - Generated plots for {len(industries)} industries")
    print("="*70)


if __name__ == '__main__':
    main()
