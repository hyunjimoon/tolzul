#!/usr/bin/env python3
"""
Funding Trajectories × Strategic Flexibility Analysis
======================================================

Compares two strategic paths:
- Path A "Escape Velocity": Low early funding → High ΔV → High later funding
- Path B "Golden Cage": High early funding → Low ΔV → Low later funding

Tests the hypothesis: Early funding creates lock-in that hurts long-term outcomes.

Author: Claude Code
Created: 2025-12-04
"""

import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from scipy.stats import spearmanr, mannwhitneyu
import warnings
warnings.filterwarnings('ignore')

# Paths
DATA_DIR = Path(__file__).parent.parent.parent / "data"
PROCESSED_DIR = DATA_DIR / "processed"
RAW_DIR = DATA_DIR / "raw"
OUTPUT_DIR = Path(__file__).parent.parent.parent / "reports" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_data():
    """Load vagueness timeseries and funding data."""
    print("=" * 60)
    print("LOADING DATA")
    print("=" * 60)

    # Load parquet with all data
    df_full = pd.read_parquet(PROCESSED_DIR / "vagueness_timeseries.parquet")
    print(f"Loaded {len(df_full):,} rows")

    # Create wide format with early and later funding
    df_2021 = df_full[df_full['year'] == 2021][['company_id', 'V', 'first_financing_size', 'company_name']].copy()
    df_2021.columns = ['company_id', 'V_2021', 'early_funding', 'company_name']

    df_2025 = df_full[df_full['year'] == 2025][['company_id', 'V']].copy()
    df_2025.columns = ['company_id', 'V_2025']

    # Merge
    df = df_2021.merge(df_2025, on='company_id', how='inner')

    # Calculate delta V
    df['delta_V'] = df['V_2025'] - df['V_2021']
    df['abs_delta_V'] = df['delta_V'].abs()

    # Load 2025 raw data to get total raised (as proxy for "later funding")
    try:
        df_2025_raw = pd.read_csv(RAW_DIR / "Company20251101.dat", sep='|',
                                   usecols=['CompanyID', 'TotalRaised'],
                                   low_memory=False, on_bad_lines='skip')
        df_2025_raw.columns = ['company_id', 'total_raised_2025']
        df_2025_raw['company_id'] = df_2025_raw['company_id'].astype(str)
        df['company_id'] = df['company_id'].astype(str)
        df = df.merge(df_2025_raw, on='company_id', how='left')
        df['total_raised_2025'] = pd.to_numeric(df['total_raised_2025'], errors='coerce')
    except Exception as e:
        print(f"Warning: Could not load 2025 total raised: {e}")
        df['total_raised_2025'] = np.nan

    # Calculate funding growth
    df['funding_growth'] = df['total_raised_2025'] / (df['early_funding'] + 0.001)  # Avoid div by zero

    # Filter complete cases
    df_clean = df.dropna(subset=['V_2021', 'V_2025', 'early_funding'])
    print(f"Complete cases: {len(df_clean):,}")

    # Additional filter for funding growth analysis
    df_funding = df_clean[df_clean['total_raised_2025'].notna() & (df_clean['early_funding'] > 0)]
    print(f"With funding growth data: {len(df_funding):,}")

    return df_clean, df_funding


def classify_paths(df):
    """Classify companies into strategic path types."""
    # Use median splits for clarity
    early_median = df['early_funding'].median()
    delta_median = df['abs_delta_V'].median()

    df = df.copy()

    # Classify
    def get_path(row):
        high_early = row['early_funding'] > early_median
        high_delta = row['abs_delta_V'] > delta_median

        if not high_early and high_delta:
            return 'A: Escape Velocity\n(Low Early, High ΔV)'
        elif high_early and not high_delta:
            return 'B: Golden Cage\n(High Early, Low ΔV)'
        elif not high_early and not high_delta:
            return 'C: Constrained\n(Low Early, Low ΔV)'
        else:
            return 'D: Resourced & Flexible\n(High Early, High ΔV)'

    df['path_type'] = df.apply(get_path, axis=1)

    # Also create quartile-based classification for finer analysis
    df['early_q'] = pd.qcut(df['early_funding'].rank(method='first'), 4, labels=['Q1_Low', 'Q2', 'Q3', 'Q4_High'])
    df['delta_q'] = pd.qcut(df['abs_delta_V'].rank(method='first'), 4, labels=['Q1_Low', 'Q2', 'Q3', 'Q4_High'])

    return df


def plot_funding_trajectories(df, df_funding):
    """Generate the main funding trajectory plots."""
    print("\n" + "=" * 60)
    print("GENERATING PLOTS")
    print("=" * 60)

    fig = plt.figure(figsize=(16, 12))

    # Panel 1: Path Classification Scatter
    ax1 = fig.add_subplot(2, 2, 1)

    # Log transform for better visualization
    x = np.log10(df['early_funding'] + 0.001)
    y = df['abs_delta_V']

    # Color by path type
    path_colors = {
        'A: Escape Velocity\n(Low Early, High ΔV)': '#2ecc71',  # Green - best
        'B: Golden Cage\n(High Early, Low ΔV)': '#e74c3c',      # Red - trap
        'C: Constrained\n(Low Early, Low ΔV)': '#3498db',       # Blue
        'D: Resourced & Flexible\n(High Early, High ΔV)': '#f1c40f'  # Yellow
    }

    for path, color in path_colors.items():
        mask = df['path_type'] == path
        ax1.scatter(x[mask], y[mask], c=color, alpha=0.3, s=10, label=path.split('\n')[0])

    # Add quadrant lines
    early_median = np.log10(df['early_funding'].median() + 0.001)
    delta_median = df['abs_delta_V'].median()
    ax1.axvline(early_median, color='gray', linestyle='--', alpha=0.5)
    ax1.axhline(delta_median, color='gray', linestyle='--', alpha=0.5)

    # Labels
    ax1.text(early_median - 1, delta_median + 5, 'A: Escape\nVelocity ⭐', fontsize=10, color='#2ecc71', weight='bold')
    ax1.text(early_median + 0.3, delta_median - 3, 'B: Golden\nCage 💀', fontsize=10, color='#e74c3c', weight='bold')

    ax1.set_xlabel('Early Funding (log₁₀ $M)', fontsize=11)
    ax1.set_ylabel('|ΔV| (Strategic Change 2021→2025)', fontsize=11)
    ax1.set_title('Panel 1: Strategic Path Classification\n(408K Companies)', fontsize=12)
    ax1.legend(loc='upper right', fontsize=8)
    ax1.grid(True, alpha=0.3)

    # Panel 2: Funding Growth by Path Type
    ax2 = fig.add_subplot(2, 2, 2)

    if len(df_funding) > 100:
        # Cap outliers for visualization
        df_plot = df_funding.copy()
        cap = df_plot['funding_growth'].quantile(0.95)
        df_plot['funding_growth_capped'] = df_plot['funding_growth'].clip(upper=cap)

        # Box plot
        path_order = ['A: Escape Velocity\n(Low Early, High ΔV)',
                      'D: Resourced & Flexible\n(High Early, High ΔV)',
                      'C: Constrained\n(Low Early, Low ΔV)',
                      'B: Golden Cage\n(High Early, Low ΔV)']

        colors = ['#2ecc71', '#f1c40f', '#3498db', '#e74c3c']

        box_data = []
        labels = []
        for path in path_order:
            data = df_plot[df_plot['path_type'] == path]['funding_growth_capped'].dropna()
            if len(data) > 0:
                box_data.append(data)
                labels.append(path.split('\n')[0].replace('A: ', '').replace('B: ', '').replace('C: ', '').replace('D: ', ''))

        bp = ax2.boxplot(box_data, labels=labels, patch_artist=True)
        for patch, color in zip(bp['boxes'], colors[:len(box_data)]):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)

        # Add means
        means = [d.mean() for d in box_data]
        ax2.plot(range(1, len(means) + 1), means, 'ko', markersize=8)

        ax2.set_ylabel('Funding Growth (Total 2025 / Early Funding)', fontsize=11)
        ax2.set_title('Panel 2: Funding Outcome by Path Type\n(Higher = Better Fundraising Trajectory)', fontsize=12)
        ax2.tick_params(axis='x', rotation=15)
        ax2.grid(True, alpha=0.3, axis='y')

        # Print statistics
        print("\nFunding Growth by Path Type:")
        for i, path in enumerate(path_order):
            if i < len(box_data):
                print(f"  {labels[i]}: mean={means[i]:.1f}x, median={box_data[i].median():.1f}x, n={len(box_data[i])}")
    else:
        ax2.text(0.5, 0.5, 'Insufficient funding\ngrowth data', ha='center', va='center', fontsize=12)
        ax2.set_title('Panel 2: Funding Growth (Data Limited)')

    # Panel 3: Heatmap of Early→ΔV→Later Flow
    ax3 = fig.add_subplot(2, 2, 3)

    if len(df_funding) > 100:
        # Create later funding quartiles
        df_funding_plot = df_funding.copy()
        df_funding_plot['later_q'] = pd.qcut(df_funding_plot['total_raised_2025'], 4,
                                              labels=['Q1_Low', 'Q2', 'Q3', 'Q4_High'])

        # Transition matrix: Early Q × Delta Q → % reaching High Later Q
        pivot = df_funding_plot.groupby(['early_q', 'delta_q']).apply(
            lambda x: (x['later_q'] == 'Q4_High').mean() * 100
        ).unstack()

        sns.heatmap(pivot, annot=True, fmt='.0f', cmap='RdYlGn', ax=ax3,
                    cbar_kws={'label': '% Reaching Top Funding Quartile'})
        ax3.set_xlabel('|ΔV| Quartile (Strategic Flexibility)', fontsize=11)
        ax3.set_ylabel('Early Funding Quartile', fontsize=11)
        ax3.set_title('Panel 3: Success Rate (% Reaching Top Later Funding)\n(Green = High Success)', fontsize=12)
    else:
        ax3.text(0.5, 0.5, 'Insufficient data', ha='center', va='center', fontsize=12)

    # Panel 4: Key Statistics Summary
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.axis('off')

    # Calculate statistics
    stats_text = """
    KEY FINDINGS: Funding Trajectories × Strategic Flexibility

    ═══════════════════════════════════════════════════════════════

    PATH A "ESCAPE VELOCITY" (Low Early Funding + High ΔV)
    • Companies that stayed flexible despite limited early resources
    • Hypothesis: These should show BEST long-term funding outcomes
    • n = {:,}

    PATH B "GOLDEN CAGE" (High Early Funding + Low ΔV)
    • Companies locked into early strategy by significant funding
    • Hypothesis: These should show WORSE long-term outcomes (TRAP!)
    • n = {:,}

    ═══════════════════════════════════════════════════════════════

    CORRELATION TEST:
    • Early Funding × |ΔV|: r = {:.3f}
      (Negative = funding reduces flexibility)

    • |ΔV| × Later Funding: r = {:.3f}
      (Positive = flexibility helps future fundraising)

    ═══════════════════════════════════════════════════════════════
    """.format(
        len(df[df['path_type'].str.contains('Escape')]),
        len(df[df['path_type'].str.contains('Golden')]),
        spearmanr(df['early_funding'], df['abs_delta_V'])[0],
        spearmanr(df_funding['abs_delta_V'], df_funding['total_raised_2025'])[0] if len(df_funding) > 100 else np.nan
    )

    ax4.text(0.05, 0.95, stats_text, transform=ax4.transAxes, fontsize=10,
             verticalalignment='top', fontfamily='monospace',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'funding_trajectories_analysis.png', dpi=150, bbox_inches='tight')
    plt.savefig(OUTPUT_DIR / 'funding_trajectories_analysis.pdf', bbox_inches='tight')
    print(f"\nSaved: {OUTPUT_DIR / 'funding_trajectories_analysis.png'}")

    return fig


def statistical_tests(df, df_funding):
    """Run statistical tests comparing path types."""
    print("\n" + "=" * 60)
    print("STATISTICAL TESTS")
    print("=" * 60)

    # Test 1: Is early funding negatively correlated with |ΔV|?
    r1, p1 = spearmanr(df['early_funding'], df['abs_delta_V'])
    print(f"\n1. Early Funding × |ΔV|:")
    print(f"   Spearman r = {r1:.4f}, p = {p1:.2e}")
    print(f"   Interpretation: {'Funding REDUCES flexibility' if r1 < 0 else 'No lock-in effect'}")

    if len(df_funding) > 100:
        # Test 2: Does |ΔV| predict later funding success?
        r2, p2 = spearmanr(df_funding['abs_delta_V'], df_funding['total_raised_2025'])
        print(f"\n2. |ΔV| × Later Funding:")
        print(f"   Spearman r = {r2:.4f}, p = {p2:.2e}")
        print(f"   Interpretation: {'Flexibility HELPS future funding' if r2 > 0 else 'No flexibility benefit'}")

        # Test 3: Compare Path A vs Path B outcomes
        path_a = df_funding[df_funding['path_type'].str.contains('Escape')]['funding_growth']
        path_b = df_funding[df_funding['path_type'].str.contains('Golden')]['funding_growth']

        if len(path_a) > 10 and len(path_b) > 10:
            stat, p3 = mannwhitneyu(path_a.dropna(), path_b.dropna(), alternative='greater')
            print(f"\n3. Path A vs Path B (Mann-Whitney U):")
            print(f"   Path A mean = {path_a.mean():.2f}x, Path B mean = {path_b.mean():.2f}x")
            print(f"   U = {stat:.0f}, p = {p3:.4f}")
            print(f"   Interpretation: {'Escape Velocity BEATS Golden Cage!' if p3 < 0.05 else 'No significant difference'}")


def main():
    """Main analysis pipeline."""
    print("\n" + "=" * 70)
    print("FUNDING TRAJECTORIES × STRATEGIC FLEXIBILITY ANALYSIS")
    print("Testing: Does early funding create a 'Golden Cage'?")
    print("=" * 70)

    # Load data
    df, df_funding = load_data()

    # Classify paths
    df = classify_paths(df)
    df_funding = classify_paths(df_funding)

    # Path distribution
    print("\nPath Distribution:")
    print(df['path_type'].value_counts())

    # Generate plots
    fig = plot_funding_trajectories(df, df_funding)

    # Statistical tests
    statistical_tests(df, df_funding)

    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)

    return df, df_funding


if __name__ == "__main__":
    df, df_funding = main()
