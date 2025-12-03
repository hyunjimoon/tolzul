#!/usr/bin/env python3
"""
Generate 2D Transportation Analysis Plots
==========================================
Creates systematic visualizations based on:
- Axis 1: Customer Heterogeneity (B2C, B2B, B2G)
- Axis 2: Pivoting Cost (Software, Fleet, Infrastructure)

Generates 3 plots:
1. 3×3 Heatmap: Sample size by segment
2. 3×3 Heatmap: Mean vagueness by segment
3. 3×3 Heatmap: Vagueness effect on survival by segment

Usage:
    python -m src.scripts.generate_transportation_2d_plots
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.data_io import load_dataframe, save_dataframe
from src.transportation_segmentation import categorize_transportation_companies


def create_segment_matrix(df: pd.DataFrame, value_col: str, agg_func='mean') -> pd.DataFrame:
    """
    Create 3×3 matrix of values by customer type and tech stack.

    Args:
        df: Segmented dataframe
        value_col: Column to aggregate
        agg_func: Aggregation function ('mean', 'count', 'slope')

    Returns:
        3×3 DataFrame with customer types as rows, tech stacks as columns
    """
    customer_order = ['B2C', 'B2B', 'B2G']
    tech_order = ['Software', 'Fleet', 'Infrastructure']

    if agg_func == 'slope':
        # Calculate vagueness-survival slope for each segment
        matrix_data = []
        for customer in customer_order:
            row_data = []
            for tech in tech_order:
                segment_df = df[(df['customer_type'] == customer) & (df['tech_stack'] == tech)].copy()

                if len(segment_df) < 20:  # Need minimum sample
                    row_data.append(np.nan)
                    continue

                # Create quartiles
                try:
                    segment_df['vag_quartile'] = pd.qcut(segment_df['vagueness'], q=4, labels=[1,2,3,4], duplicates='drop')
                except:
                    segment_df['vag_rank'] = segment_df['vagueness'].rank(pct=True)
                    segment_df['vag_quartile'] = pd.cut(segment_df['vag_rank'], bins=[0,0.25,0.5,0.75,1.0], labels=[1,2,3,4])

                # Calculate survival rate by quartile
                survival_by_q = segment_df.groupby('vag_quartile', observed=True)['growth'].mean()

                if len(survival_by_q) >= 3:
                    x = np.array([1, 2, 3, 4])[:len(survival_by_q)]
                    y = survival_by_q.values
                    slope, _, _, _, _ = linregress(x, y)
                    row_data.append(slope * 100)  # Convert to percentage points per quartile
                else:
                    row_data.append(np.nan)

            matrix_data.append(row_data)

        matrix = pd.DataFrame(matrix_data, index=customer_order, columns=tech_order)

    else:
        # Standard aggregation
        pivot = df.pivot_table(
            values=value_col,
            index='customer_type',
            columns='tech_stack',
            aggfunc=agg_func
        )

        # Reindex to ensure consistent order
        matrix = pivot.reindex(index=customer_order, columns=tech_order)

    return matrix


def plot_heatmap_1_sample_size(df: pd.DataFrame, output_dir: Path):
    """
    Plot 1: Sample Size Heatmap (3×3)

    Shows number of companies in each segment.
    """
    fig, ax = plt.subplots(figsize=(10, 8))

    # Create matrix
    matrix = create_segment_matrix(df, 'vagueness', agg_func='count')

    # Plot heatmap
    sns.heatmap(
        matrix,
        annot=True,
        fmt='.0f',
        cmap='YlOrRd',
        cbar_kws={'label': 'Number of Companies'},
        linewidths=1,
        linecolor='black',
        ax=ax,
        vmin=0
    )

    ax.set_xlabel('Technology Stack\n(Pivoting Cost →)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Customer Type\n(Heterogeneity →)', fontsize=13, fontweight='bold')
    ax.set_title('Transportation Segment Distribution\n(Sample Size by Customer × Technology)',
                 fontsize=15, fontweight='bold', pad=20)

    # Add total
    total = matrix.sum().sum()
    ax.text(1.5, -0.3, f'Total: {total:.0f} companies',
            ha='center', fontsize=11, fontweight='bold',
            transform=ax.transData)

    plt.tight_layout()

    # Save
    output_dir.mkdir(exist_ok=True, parents=True)
    png_file = output_dir / "transport_2d_1_sample_size.png"
    pdf_file = output_dir / "transport_2d_1_sample_size.pdf"

    fig.savefig(png_file, dpi=300, bbox_inches='tight')
    fig.savefig(pdf_file, bbox_inches='tight')
    plt.close(fig)

    print(f"   ✅ Plot 1 saved: {png_file.name}")
    return png_file, pdf_file


def plot_heatmap_2_mean_vagueness(df: pd.DataFrame, output_dir: Path):
    """
    Plot 2: Mean Vagueness Heatmap (3×3)

    Shows average vagueness score in each segment.
    """
    fig, ax = plt.subplots(figsize=(10, 8))

    # Create matrix
    matrix = create_segment_matrix(df, 'vagueness', agg_func='mean')

    # Plot heatmap
    sns.heatmap(
        matrix,
        annot=True,
        fmt='.1f',
        cmap='coolwarm',
        cbar_kws={'label': 'Mean Vagueness Score'},
        linewidths=1,
        linecolor='black',
        ax=ax,
        vmin=70,
        vmax=90,
        center=80
    )

    ax.set_xlabel('Technology Stack\n(Pivoting Cost →)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Customer Type\n(Heterogeneity →)', fontsize=13, fontweight='bold')
    ax.set_title('Mean Vagueness by Segment\n(Does Software use more vague language?)',
                 fontsize=15, fontweight='bold', pad=20)

    # Add interpretation
    interpretation = (
        "Prediction: Software (low pivoting cost) → Higher vagueness\n"
        "Prediction: Infrastructure (high pivoting cost) → Lower vagueness"
    )
    ax.text(1.5, 3.5, interpretation,
            ha='center', fontsize=9, style='italic',
            transform=ax.transData,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    plt.tight_layout()

    # Save
    png_file = output_dir / "transport_2d_2_mean_vagueness.png"
    pdf_file = output_dir / "transport_2d_2_mean_vagueness.pdf"

    fig.savefig(png_file, dpi=300, bbox_inches='tight')
    fig.savefig(pdf_file, bbox_inches='tight')
    plt.close(fig)

    print(f"   ✅ Plot 2 saved: {png_file.name}")
    return png_file, pdf_file


def plot_heatmap_3_vagueness_effect(df: pd.DataFrame, output_dir: Path):
    """
    Plot 3: Vagueness Effect on Survival Heatmap (3×3)

    Shows slope of vagueness-survival relationship in each segment.
    Positive = vagueness helps, Negative = specificity helps
    """
    fig, ax = plt.subplots(figsize=(10, 8))

    # Create matrix (slope calculation)
    matrix = create_segment_matrix(df, 'growth', agg_func='slope')

    # Plot heatmap with diverging colormap
    sns.heatmap(
        matrix,
        annot=True,
        fmt='.2f',
        cmap='RdYlGn',  # Red = negative (bad), Green = positive (good)
        cbar_kws={'label': 'Vagueness Effect\n(% points per quartile)'},
        linewidths=1,
        linecolor='black',
        ax=ax,
        center=0,  # Zero is white
        vmin=-2,
        vmax=2
    )

    ax.set_xlabel('Technology Stack\n(Pivoting Cost →)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Customer Type\n(Heterogeneity →)', fontsize=13, fontweight='bold')
    ax.set_title('Vagueness Effect on Survival by Segment\n(H2a × H2b Test: Green = Vagueness Helps, Red = Hurts)',
                 fontsize=15, fontweight='bold', pad=20)

    # Add interpretation
    interpretation = (
        "H2a: B2C (high heterogeneity) → Positive (green)\n"
        "H2b: Software (low pivoting cost) → Positive (green)\n"
        "Expected: Top-left should be greenest"
    )
    ax.text(1.5, 3.5, interpretation,
            ha='center', fontsize=9, style='italic',
            transform=ax.transData,
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    plt.tight_layout()

    # Save
    png_file = output_dir / "transport_2d_3_vagueness_effect.png"
    pdf_file = output_dir / "transport_2d_3_vagueness_effect.pdf"

    fig.savefig(png_file, dpi=300, bbox_inches='tight')
    fig.savefig(pdf_file, bbox_inches='tight')
    plt.close(fig)

    print(f"   ✅ Plot 3 saved: {png_file.name}")
    return png_file, pdf_file


def main():
    """Main entry point."""
    print("="*70)
    print("TRANSPORTATION 2D ANALYSIS")
    print("="*70)

    # Load transportation dataset
    transport_file = Path("data/outputs/transportation/dataset.nc")

    if not transport_file.exists():
        print(f"\n❌ Transportation dataset not found at {transport_file}")
        print("   Run: python -m src.cli filter-datasets")
        return 1

    print(f"\n📂 Loading {transport_file}")
    df_transport = load_dataframe(transport_file)
    print(f"   ✓ Loaded {len(df_transport):,} transportation companies")

    # Categorize by customer × technology
    print("\n🔍 Categorizing by Customer Type × Tech Stack...")
    df_segmented = categorize_transportation_companies(df_transport)

    # Show distribution
    print("\nCustomer Type Distribution:")
    print(df_segmented['customer_type'].value_counts())
    print("\nTech Stack Distribution:")
    print(df_segmented['tech_stack'].value_counts())

    # Save segmented dataset
    segmented_file = Path("data/outputs/transportation/dataset_segmented.nc")
    save_dataframe(df_segmented, segmented_file)
    print(f"\n💾 Saved segmented dataset to {segmented_file}")

    # Generate plots
    output_dir = Path("data/outputs/transportation/figures_2d")
    print(f"\n📊 Generating 3 heatmap plots...")

    try:
        plot_heatmap_1_sample_size(df_segmented, output_dir)
    except Exception as e:
        print(f"   ❌ Plot 1 failed: {e}")

    try:
        plot_heatmap_2_mean_vagueness(df_segmented, output_dir)
    except Exception as e:
        print(f"   ❌ Plot 2 failed: {e}")

    try:
        plot_heatmap_3_vagueness_effect(df_segmented, output_dir)
    except Exception as e:
        print(f"   ❌ Plot 3 failed: {e}")

    print("\n" + "="*70)
    print(f"✅ COMPLETE - Saved to {output_dir}")
    print("="*70)


if __name__ == '__main__':
    main()
