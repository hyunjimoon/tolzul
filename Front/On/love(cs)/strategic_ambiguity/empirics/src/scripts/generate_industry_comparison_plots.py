#!/usr/bin/env python3
"""
Generate Industry Comparison Plots
===================================
Creates comparative visualizations across 6 industries in a single plot.

Usage:
    python -m src.scripts.generate_industry_comparison_plots
    python -m src.scripts.generate_industry_comparison_plots --industries hardware software medtech pharma quantum transportation
"""

import sys
from pathlib import Path
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict
import warnings
warnings.filterwarnings('ignore')

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.data_io import load_dataframe

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# Industry colors (consistent with individual plots)
INDUSTRY_COLORS = {
    'quantum': '#A23B72',
    'transportation': '#F18F01',
    'hardware': '#C73E1D',
    'software': '#06A77D',
    'medtech': '#8338EC',
    'pharma': '#FB5607'
}

INDUSTRY_NAMES = {
    'quantum': 'Quantum',
    'transportation': 'Transportation',
    'hardware': 'Hardware',
    'software': 'Software',
    'medtech': 'MedTech',
    'pharma': 'Pharma'
}


def load_all_industries(industries: List[str]) -> Dict[str, pd.DataFrame]:
    """Load datasets for all specified industries."""
    datasets = {}

    for industry in industries:
        dataset_file = Path(f"data/outputs/{industry}/dataset.nc")

        if not dataset_file.exists():
            print(f"   ⚠️  Skipping {industry}: dataset not found at {dataset_file}")
            continue

        try:
            df = load_dataframe(dataset_file)
            datasets[industry] = df
            print(f"   ✓ Loaded {industry}: {len(df):,} companies")
        except Exception as e:
            print(f"   ❌ Failed to load {industry}: {e}")

    return datasets


def plot_vagueness_comparison(datasets: Dict[str, pd.DataFrame], output_dir: Path):
    """
    Comparison Plot 1: Vagueness Distribution Across Industries

    Shows violin plots + box plots for each industry side-by-side.
    """
    fig, ax = plt.subplots(figsize=(14, 7))

    # Prepare data for plotting
    data_list = []
    for industry, df in datasets.items():
        vagueness = df['vagueness'].dropna()
        for val in vagueness:
            data_list.append({
                'Industry': INDUSTRY_NAMES.get(industry, industry.title()),
                'Vagueness': val
            })

    if not data_list:
        print("   ⚠️  No vagueness data available")
        plt.close(fig)
        return

    plot_df = pd.DataFrame(data_list)

    # Create violin plot
    parts = ax.violinplot(
        [datasets[ind]['vagueness'].dropna() for ind in datasets.keys()],
        positions=range(len(datasets)),
        widths=0.7,
        showmeans=True,
        showmedians=True
    )

    # Color the violins
    for i, (industry, pc) in enumerate(zip(datasets.keys(), parts['bodies'])):
        pc.set_facecolor(INDUSTRY_COLORS.get(industry, '#2E86AB'))
        pc.set_alpha(0.6)

    # Add box plots on top
    bp = ax.boxplot(
        [datasets[ind]['vagueness'].dropna() for ind in datasets.keys()],
        positions=range(len(datasets)),
        widths=0.3,
        patch_artist=True,
        showfliers=False,
        boxprops=dict(facecolor='white', alpha=0.7),
        medianprops=dict(color='red', linewidth=2)
    )

    # Styling
    ax.set_xticks(range(len(datasets)))
    ax.set_xticklabels([INDUSTRY_NAMES.get(ind, ind.title()) for ind in datasets.keys()],
                       rotation=45, ha='right', fontsize=12)
    ax.set_ylabel('Vagueness Score (0-100)', fontsize=13, fontweight='bold')
    ax.set_title('Vagueness Distribution Comparison Across Industries\n(Violin + Box Plot)',
                 fontsize=15, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3, axis='y')
    ax.set_ylim(0, 105)

    # Add sample sizes
    for i, (industry, df) in enumerate(datasets.items()):
        n = df['vagueness'].notna().sum()
        mean_v = df['vagueness'].mean()
        ax.text(i, 102, f'n={n:,}\nμ={mean_v:.1f}',
                ha='center', va='top', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

    plt.tight_layout()

    # Save
    output_dir.mkdir(exist_ok=True, parents=True)
    png_file = output_dir / "comparison_1_vagueness_distribution.png"
    pdf_file = output_dir / "comparison_1_vagueness_distribution.pdf"

    fig.savefig(png_file, dpi=300, bbox_inches='tight')
    fig.savefig(pdf_file, bbox_inches='tight')
    plt.close(fig)

    print(f"   ✅ Comparison Plot 1 saved: {png_file.name}")
    return png_file, pdf_file


def plot_survival_comparison(datasets: Dict[str, pd.DataFrame], output_dir: Path):
    """
    Comparison Plot 2: Survival Rate Across Industries

    Shows overall survival rate (Series B+) for each industry.
    """
    fig, ax = plt.subplots(figsize=(12, 7))

    # Calculate survival rates
    survival_data = []
    for industry, df in datasets.items():
        if 'growth' not in df.columns:
            continue

        total = len(df)
        survivors = df['growth'].sum()
        rate = (survivors / total * 100) if total > 0 else 0

        # Calculate 95% CI
        p = rate / 100
        se = np.sqrt(p * (1 - p) / total) * 100 if total > 0 else 0

        survival_data.append({
            'industry': industry,
            'name': INDUSTRY_NAMES.get(industry, industry.title()),
            'rate': rate,
            'se': se,
            'total': total,
            'survivors': int(survivors)
        })

    if not survival_data:
        print("   ⚠️  No survival data available")
        plt.close(fig)
        return

    survival_df = pd.DataFrame(survival_data)
    survival_df = survival_df.sort_values('rate', ascending=False)

    # Bar plot
    x_pos = np.arange(len(survival_df))
    bars = ax.bar(
        x_pos,
        survival_df['rate'],
        color=[INDUSTRY_COLORS.get(ind, '#2E86AB') for ind in survival_df['industry']],
        alpha=0.7,
        edgecolor='black',
        linewidth=1.5
    )

    # Error bars
    ax.errorbar(
        x_pos,
        survival_df['rate'],
        yerr=survival_df['se'],
        fmt='none',
        ecolor='black',
        capsize=5,
        capthick=2
    )

    # Add value labels
    for i, row in survival_df.iterrows():
        ax.text(
            list(survival_df.index).index(i),
            row['rate'] + row['se'] + 0.3,
            f"{row['rate']:.1f}%\n({row['survivors']:,}/{row['total']:,})",
            ha='center',
            va='bottom',
            fontsize=10,
            fontweight='bold'
        )

    # Styling
    ax.set_xticks(x_pos)
    ax.set_xticklabels(survival_df['name'], rotation=45, ha='right', fontsize=12)
    ax.set_ylabel('Survival Rate to Series B+ (%)', fontsize=13, fontweight='bold')
    ax.set_title('Overall Survival Rate Comparison Across Industries\n(Series B+ Achievement)',
                 fontsize=15, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3, axis='y')
    ax.set_ylim(0, max(survival_df['rate']) * 1.4)

    # Add overall mean line
    overall_mean = survival_df['rate'].mean()
    ax.axhline(overall_mean, color='red', linestyle='--', linewidth=2,
               label=f'Mean: {overall_mean:.1f}%')
    ax.legend(loc='upper right', fontsize=11)

    plt.tight_layout()

    # Save
    png_file = output_dir / "comparison_2_survival_rate.png"
    pdf_file = output_dir / "comparison_2_survival_rate.pdf"

    fig.savefig(png_file, dpi=300, bbox_inches='tight')
    fig.savefig(pdf_file, bbox_inches='tight')
    plt.close(fig)

    print(f"   ✅ Comparison Plot 2 saved: {png_file.name}")
    return png_file, pdf_file


def plot_vagueness_survival_relationship(datasets: Dict[str, pd.DataFrame], output_dir: Path):
    """
    Comparison Plot 3: Vagueness-Survival Relationship by Industry

    Shows how survival rate varies with vagueness level for each industry.
    """
    fig, ax = plt.subplots(figsize=(12, 8))

    # For each industry, calculate survival rate by vagueness quartile
    for industry, df in datasets.items():
        if 'vagueness' not in df.columns or 'growth' not in df.columns:
            continue

        df_valid = df[df['vagueness'].notna() & df['growth'].notna()].copy()

        if len(df_valid) < 20:  # Skip if too few samples
            continue

        # Create quartiles (with duplicate handling)
        try:
            df_valid['vagueness_quartile'] = pd.qcut(
                df_valid['vagueness'],
                q=4,
                labels=[1, 2, 3, 4],
                duplicates='drop'
            )
        except ValueError:
            # Fallback to rank-based
            df_valid['vagueness_rank'] = df_valid['vagueness'].rank(method='first', pct=True)
            df_valid['vagueness_quartile'] = pd.cut(
                df_valid['vagueness_rank'],
                bins=[0, 0.25, 0.5, 0.75, 1.0],
                labels=[1, 2, 3, 4],
                include_lowest=True
            )

        # Calculate survival by quartile
        survival_by_q = df_valid.groupby('vagueness_quartile', observed=True)['growth'].agg(['mean', 'count'])
        survival_by_q['survival_rate'] = survival_by_q['mean'] * 100

        # Plot line
        quartiles = [1, 2, 3, 4]
        rates = [survival_by_q.loc[q, 'survival_rate'] if q in survival_by_q.index else np.nan
                 for q in quartiles]

        ax.plot(
            quartiles,
            rates,
            marker='o',
            markersize=10,
            linewidth=2.5,
            label=INDUSTRY_NAMES.get(industry, industry.title()),
            color=INDUSTRY_COLORS.get(industry, '#2E86AB'),
            alpha=0.8
        )

    # Styling
    ax.set_xlabel('Vagueness Quartile (1=Low, 4=High)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Survival Rate to Series B+ (%)', fontsize=13, fontweight='bold')
    ax.set_title('Vagueness-Survival Relationship Across Industries\n(Does Higher Vagueness Help or Hurt?)',
                 fontsize=15, fontweight='bold', pad=20)
    ax.set_xticks([1, 2, 3, 4])
    ax.set_xticklabels(['Q1\n(Low)', 'Q2', 'Q3', 'Q4\n(High)'], fontsize=11)
    ax.legend(loc='best', fontsize=11, frameon=True, shadow=True, ncol=2)
    ax.grid(True, alpha=0.3)

    # Add interpretation guide
    interpretation = (
        "Upward slope → Vagueness helps survival\n"
        "Downward slope → Specificity helps survival\n"
        "Flat → No effect"
    )
    ax.text(0.02, 0.98, interpretation, transform=ax.transAxes,
            fontsize=9, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    plt.tight_layout()

    # Save
    png_file = output_dir / "comparison_3_vagueness_survival_relationship.png"
    pdf_file = output_dir / "comparison_3_vagueness_survival_relationship.pdf"

    fig.savefig(png_file, dpi=300, bbox_inches='tight')
    fig.savefig(pdf_file, bbox_inches='tight')
    plt.close(fig)

    print(f"   ✅ Comparison Plot 3 saved: {png_file.name}")
    return png_file, pdf_file


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate industry comparison plots',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('--industries', nargs='+',
                        default=['hardware', 'software', 'medtech', 'pharma', 'quantum', 'transportation'],
                        help='Which industries to compare (default: all 6)')
    parser.add_argument('--output', type=str, default='data/outputs/comparisons',
                        help='Output directory for comparison plots')

    args = parser.parse_args()

    print("="*70)
    print("INDUSTRY COMPARISON PLOTS GENERATOR")
    print("="*70)
    print(f"Comparing {len(args.industries)} industries: {', '.join(args.industries)}")

    # Load all datasets
    print("\n📂 Loading industry datasets...")
    datasets = load_all_industries(args.industries)

    if not datasets:
        print("\n❌ No datasets found. Run 'python -m src.cli filter-datasets' first.")
        return 1

    print(f"\n✓ Loaded {len(datasets)} industries successfully")

    # Create output directory
    output_dir = Path(args.output)
    output_dir.mkdir(exist_ok=True, parents=True)

    # Generate comparison plots
    print("\n" + "="*70)
    print("Generating Comparison Plots")
    print("="*70)

    try:
        plot_vagueness_comparison(datasets, output_dir)
    except Exception as e:
        print(f"   ❌ Comparison Plot 1 failed: {e}")
        import traceback
        traceback.print_exc()

    try:
        plot_survival_comparison(datasets, output_dir)
    except Exception as e:
        print(f"   ❌ Comparison Plot 2 failed: {e}")
        import traceback
        traceback.print_exc()

    try:
        plot_vagueness_survival_relationship(datasets, output_dir)
    except Exception as e:
        print(f"   ❌ Comparison Plot 3 failed: {e}")
        import traceback
        traceback.print_exc()

    print("\n" + "="*70)
    print(f"✅ COMPLETE - Comparison plots saved to {output_dir}")
    print("="*70)
    print("\nGenerated files:")
    print("  - comparison_1_vagueness_distribution.png/pdf")
    print("  - comparison_2_survival_rate.png/pdf")
    print("  - comparison_3_vagueness_survival_relationship.png/pdf")


if __name__ == '__main__':
    main()
