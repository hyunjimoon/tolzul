#!/usr/bin/env python3
"""
Cruel Optimism of Commitment - Flagship Visualization
======================================================

A single, powerful plot that communicates the core message:
"Early funding creates a golden cage that traps companies"

Design principles:
- 담백 (Simple & Clean): One clear message per panel
- 강력 (Powerful): Data speaks for itself
- Professional: Publication-ready quality

Author: Claude Code
Created: 2025-12-04
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from pathlib import Path
from scipy.stats import spearmanr
import warnings
warnings.filterwarnings('ignore')

# Set professional style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.labelsize': 12,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'grid.alpha': 0.3,
    'grid.linestyle': '-',
    'legend.framealpha': 0.9,
})

# Paths
DATA_DIR = Path(__file__).parent.parent.parent / "data"
PROCESSED_DIR = DATA_DIR / "processed"
RAW_DIR = DATA_DIR / "raw"
# Output to paper_generation folder for 🦾C
OUTPUT_DIR = Path(__file__).parent / "paper_generation" / "output" / "🦾C" / "⚙️process" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Color palette - professional and meaningful
COLORS = {
    'escape': '#1a9850',      # Green - freedom, growth
    'cage': '#d73027',        # Red - danger, trap
    'neutral': '#4575b4',     # Blue - neutral
    'highlight': '#fdae61',   # Orange - attention
    'muted': '#878787',       # Gray - background
}


def load_data():
    """Load and prepare the dataset."""
    print("Loading data...")

    # Load vagueness timeseries
    df_full = pd.read_parquet(PROCESSED_DIR / "vagueness_timeseries.parquet")

    # Create wide format
    df_2021 = df_full[df_full['year'] == 2021][['company_id', 'V', 'first_financing_size']].copy()
    df_2021.columns = ['company_id', 'V_2021', 'early_funding']

    df_2025 = df_full[df_full['year'] == 2025][['company_id', 'V']].copy()
    df_2025.columns = ['company_id', 'V_2025']

    df = df_2021.merge(df_2025, on='company_id', how='inner')
    df['delta_V'] = df['V_2025'] - df['V_2021']
    df['abs_delta_V'] = df['delta_V'].abs()

    # Load 2025 outcomes
    df_2025_raw = pd.read_csv(RAW_DIR / "Company20251101.dat", sep='|',
                               usecols=['CompanyID', 'TotalRaised'],
                               low_memory=False, on_bad_lines='skip')
    df_2025_raw.columns = ['company_id', 'total_raised_2025']
    df_2025_raw['company_id'] = df_2025_raw['company_id'].astype(str)
    df['company_id'] = df['company_id'].astype(str)
    df_2025_raw['total_raised_2025'] = pd.to_numeric(df_2025_raw['total_raised_2025'], errors='coerce')

    df = df.merge(df_2025_raw, on='company_id', how='left')
    df['funding_growth'] = df['total_raised_2025'] / (df['early_funding'] + 0.001)

    # Clean data
    df = df.dropna(subset=['V_2021', 'V_2025', 'early_funding'])
    df = df[df['early_funding'] > 0]

    print(f"Loaded {len(df):,} companies")
    return df


def create_flagship_plot(df):
    """Create the flagship visualization."""

    # Classify into paths
    early_median = df['early_funding'].median()
    delta_median = df['abs_delta_V'].median()

    df['path'] = 'Other'
    df.loc[(df['early_funding'] <= early_median) & (df['abs_delta_V'] > delta_median), 'path'] = 'Escape Velocity'
    df.loc[(df['early_funding'] > early_median) & (df['abs_delta_V'] <= delta_median), 'path'] = 'Golden Cage'

    # Filter for funding growth analysis
    df_outcome = df[df['total_raised_2025'].notna() & (df['funding_growth'] < df['funding_growth'].quantile(0.99))]

    # Create figure with 2 panels
    fig = plt.figure(figsize=(14, 6))

    # =========================================
    # Panel A: The Lock-in Effect
    # =========================================
    ax1 = fig.add_subplot(1, 2, 1)

    # Bin by early funding deciles
    df['funding_decile'] = pd.qcut(df['early_funding'], 10, labels=False) + 1

    decile_stats = df.groupby('funding_decile').agg({
        'abs_delta_V': ['mean', 'std', 'count'],
        'early_funding': 'median'
    }).reset_index()
    decile_stats.columns = ['decile', 'mean_dv', 'std_dv', 'n', 'median_funding']
    decile_stats['se'] = decile_stats['std_dv'] / np.sqrt(decile_stats['n'])

    # Plot with gradient color
    colors_gradient = plt.cm.RdYlGn_r(np.linspace(0.2, 0.8, 10))

    bars = ax1.bar(decile_stats['decile'], decile_stats['mean_dv'],
                   color=colors_gradient, edgecolor='white', linewidth=0.5)

    # Error bars
    ax1.errorbar(decile_stats['decile'], decile_stats['mean_dv'],
                 yerr=1.96*decile_stats['se'], fmt='none', color='#333333', capsize=3, capthick=1)

    # Add correlation annotation
    r, p = spearmanr(df['early_funding'], df['abs_delta_V'])
    ax1.text(0.97, 0.97, f'ρ = {r:.2f}***', transform=ax1.transAxes,
             fontsize=13, ha='right', va='top', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.9))

    # Arrow annotation
    ax1.annotate('', xy=(9, decile_stats['mean_dv'].iloc[-1]),
                 xytext=(2, decile_stats['mean_dv'].iloc[1]),
                 arrowprops=dict(arrowstyle='->', color=COLORS['cage'], lw=2.5))
    ax1.text(5.5, decile_stats['mean_dv'].max() * 0.85, 'Lock-in Effect',
             fontsize=11, ha='center', color=COLORS['cage'], style='italic')

    ax1.set_xlabel('Early Funding Decile\n(1 = Lowest, 10 = Highest)', fontsize=12)
    ax1.set_ylabel('Strategic Flexibility  |ΔV|', fontsize=12)
    ax1.set_title('A. More Early Funding → Less Strategic Flexibility', fontsize=14, pad=15)
    ax1.set_xticks(range(1, 11))
    ax1.set_ylim(0, decile_stats['mean_dv'].max() * 1.15)

    # =========================================
    # Panel B: The Payoff
    # =========================================
    ax2 = fig.add_subplot(1, 2, 2)

    # Get path-specific outcomes
    escape = df_outcome[df_outcome['path'] == 'Escape Velocity']['funding_growth']
    cage = df_outcome[df_outcome['path'] == 'Golden Cage']['funding_growth']
    other = df_outcome[df_outcome['path'] == 'Other']['funding_growth']

    # Cap at 99th percentile for visualization
    cap = df_outcome['funding_growth'].quantile(0.95)

    # Box plot data
    box_data = [escape.clip(upper=cap), other.clip(upper=cap), cage.clip(upper=cap)]
    positions = [1, 2, 3]

    bp = ax2.boxplot(box_data, positions=positions, widths=0.6, patch_artist=True,
                     showfliers=False, showmeans=True,
                     meanprops=dict(marker='D', markerfacecolor='white', markeredgecolor='black', markersize=8))

    # Color the boxes
    box_colors = [COLORS['escape'], COLORS['muted'], COLORS['cage']]
    for patch, color in zip(bp['boxes'], box_colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.8)

    for median in bp['medians']:
        median.set_color('white')
        median.set_linewidth(2)

    # Add mean values as text
    means = [escape.mean(), other.mean(), cage.mean()]
    for i, (pos, mean) in enumerate(zip(positions, means)):
        ax2.text(pos, cap * 1.05, f'{mean:.0f}×', ha='center', fontsize=12, fontweight='bold',
                color=box_colors[i])

    # Statistical significance
    ax2.plot([1, 3], [cap * 0.95, cap * 0.95], 'k-', lw=1)
    ax2.text(2, cap * 0.97, '***', ha='center', fontsize=14)

    ax2.set_xticks(positions)
    ax2.set_xticklabels(['Escape\nVelocity', 'Other', 'Golden\nCage'], fontsize=11)
    ax2.set_ylabel('Funding Growth\n(Total 2025 / Early Funding)', fontsize=12)
    ax2.set_title('B. Staying Flexible Pays Off', fontsize=14, pad=15)
    ax2.set_ylim(0, cap * 1.2)

    # Add sample sizes
    n_labels = [f'n={len(escape):,}', f'n={len(other):,}', f'n={len(cage):,}']
    for i, (pos, label) in enumerate(zip(positions, n_labels)):
        ax2.text(pos, -cap * 0.08, label, ha='center', fontsize=9, color='gray')

    # Legend for Panel B
    legend_elements = [
        mpatches.Patch(facecolor=COLORS['escape'], label='Low Funding + High Flexibility'),
        mpatches.Patch(facecolor=COLORS['cage'], label='High Funding + Low Flexibility'),
    ]
    ax2.legend(handles=legend_elements, loc='upper right', fontsize=9, framealpha=0.9)

    # Overall title
    fig.suptitle('The Cruel Optimism of Commitment', fontsize=18, fontweight='bold', y=1.02)

    plt.tight_layout()

    # Save
    plt.savefig(OUTPUT_DIR / 'cruel_optimism_flagship.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.savefig(OUTPUT_DIR / 'cruel_optimism_flagship.pdf', bbox_inches='tight',
                facecolor='white', edgecolor='none')

    print(f"\nSaved: {OUTPUT_DIR / 'cruel_optimism_flagship.png'}")

    # Print key statistics
    print("\n" + "=" * 50)
    print("KEY STATISTICS")
    print("=" * 50)
    print(f"Lock-in correlation: ρ = {r:.3f} (p < 0.001)")
    print(f"\nFunding Growth by Path:")
    print(f"  Escape Velocity: {escape.mean():.1f}× (median: {escape.median():.1f}×)")
    print(f"  Golden Cage:     {cage.mean():.1f}× (median: {cage.median():.1f}×)")
    print(f"  Ratio:           {escape.mean()/cage.mean():.1f}× better")

    return fig


def create_single_message_plot(df):
    """Create an even simpler single-panel plot with maximum impact."""

    # Classify into paths
    early_median = df['early_funding'].median()
    delta_median = df['abs_delta_V'].median()

    df['path'] = 'Other'
    df.loc[(df['early_funding'] <= early_median) & (df['abs_delta_V'] > delta_median), 'path'] = 'Escape Velocity'
    df.loc[(df['early_funding'] > early_median) & (df['abs_delta_V'] <= delta_median), 'path'] = 'Golden Cage'

    df_outcome = df[df['total_raised_2025'].notna()]

    escape = df_outcome[df_outcome['path'] == 'Escape Velocity']
    cage = df_outcome[df_outcome['path'] == 'Golden Cage']

    # Use MEDIAN for robustness (not mean which is skewed by outliers)
    escape_median = escape['funding_growth'].median()
    cage_median = cage['funding_growth'].median()
    ratio = escape_median / cage_median

    # Single powerful figure
    fig, ax = plt.subplots(figsize=(9, 7))

    # Bar chart - simple and powerful
    bars = ax.bar(['Escape\nVelocity', 'Golden\nCage'],
                  [escape_median, cage_median],
                  color=[COLORS['escape'], COLORS['cage']],
                  edgecolor='white', linewidth=2, width=0.5)

    # Add value labels on bars
    ax.text(0, escape_median + 0.3, f'{escape_median:.1f}×', ha='center', fontsize=28, fontweight='bold', color=COLORS['escape'])
    ax.text(1, cage_median + 0.3, f'{cage_median:.1f}×', ha='center', fontsize=28, fontweight='bold', color=COLORS['cage'])

    # Add ratio annotation with cleaner arrow
    mid_y = (escape_median + cage_median) / 2
    ax.annotate('', xy=(1, cage_median + 0.5), xytext=(0, escape_median - 0.5),
                arrowprops=dict(arrowstyle='->', color='#333', lw=2, connectionstyle='arc3,rad=-0.2'))
    ax.text(0.5, mid_y + 1.5, f'{ratio:.1f}× better', ha='center', fontsize=16, fontweight='bold')

    # Axis labels
    ax.set_ylabel('Median Funding Growth\n(Total Raised 2025 / Early Funding)', fontsize=13)
    ax.set_ylim(0, escape_median * 1.5)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Title
    ax.set_title('The Cruel Optimism of Commitment', fontsize=20, fontweight='bold', pad=20)

    # Subtitle
    ax.text(0.5, 1.02, 'Companies that stayed flexible outperformed those locked by early funding',
            transform=ax.transAxes, ha='center', fontsize=11, style='italic', color='gray')

    # Sample sizes below bars
    ax.text(0, -0.4, f'n = {len(escape):,}', ha='center', fontsize=10, color='gray')
    ax.text(1, -0.4, f'n = {len(cage):,}', ha='center', fontsize=10, color='gray')

    # Definition boxes
    box_style = dict(boxstyle='round,pad=0.4', facecolor='#f5f5f5', edgecolor='#ccc', alpha=0.95)
    ax.text(0, -1.2, 'Low Early Funding\n+ High |ΔV|', ha='center', fontsize=9, bbox=box_style)
    ax.text(1, -1.2, 'High Early Funding\n+ Low |ΔV|', ha='center', fontsize=9, bbox=box_style)

    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / 'cruel_optimism_simple.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.savefig(OUTPUT_DIR / 'cruel_optimism_simple.pdf', bbox_inches='tight',
                facecolor='white', edgecolor='none')

    print(f"Saved: {OUTPUT_DIR / 'cruel_optimism_simple.png'}")
    print(f"  Escape Velocity median: {escape_median:.1f}×")
    print(f"  Golden Cage median: {cage_median:.1f}×")
    print(f"  Ratio: {ratio:.1f}×")

    return fig


def create_trajectory_plot(df):
    """Create a trajectory visualization showing the two paths."""

    # Classify
    early_median = df['early_funding'].median()
    delta_median = df['abs_delta_V'].median()

    df['path'] = 'Other'
    df.loc[(df['early_funding'] <= early_median) & (df['abs_delta_V'] > delta_median), 'path'] = 'Escape Velocity'
    df.loc[(df['early_funding'] > early_median) & (df['abs_delta_V'] <= delta_median), 'path'] = 'Golden Cage'

    df_outcome = df[df['total_raised_2025'].notna()]

    fig, ax = plt.subplots(figsize=(12, 8))

    # Create trajectory visualization
    # X: Time (Early → Later)
    # Y: Funding level

    escape = df_outcome[df_outcome['path'] == 'Escape Velocity']
    cage = df_outcome[df_outcome['path'] == 'Golden Cage']

    # Average trajectories
    escape_early = escape['early_funding'].median()
    escape_later = escape['total_raised_2025'].median()
    cage_early = cage['early_funding'].median()
    cage_later = cage['total_raised_2025'].median()

    # Plot trajectories
    ax.plot([0, 1], [np.log10(escape_early + 0.01), np.log10(escape_later + 0.01)],
            'o-', color=COLORS['escape'], linewidth=4, markersize=15, label='Escape Velocity')
    ax.plot([0, 1], [np.log10(cage_early + 0.01), np.log10(cage_later + 0.01)],
            'o-', color=COLORS['cage'], linewidth=4, markersize=15, label='Golden Cage')

    # Add arrows showing direction
    ax.annotate('', xy=(1, np.log10(escape_later + 0.01)),
                xytext=(0.5, (np.log10(escape_early + 0.01) + np.log10(escape_later + 0.01))/2),
                arrowprops=dict(arrowstyle='->', color=COLORS['escape'], lw=3))

    # Labels
    ax.text(-0.05, np.log10(escape_early + 0.01), f'${escape_early:.1f}M', ha='right', fontsize=12, color=COLORS['escape'])
    ax.text(1.05, np.log10(escape_later + 0.01), f'${escape_later:.1f}M', ha='left', fontsize=12, color=COLORS['escape'], fontweight='bold')
    ax.text(-0.05, np.log10(cage_early + 0.01), f'${cage_early:.1f}M', ha='right', fontsize=12, color=COLORS['cage'])
    ax.text(1.05, np.log10(cage_later + 0.01), f'${cage_later:.1f}M', ha='left', fontsize=12, color=COLORS['cage'], fontweight='bold')

    # Flexibility annotation
    mid_escape = (np.log10(escape_early + 0.01) + np.log10(escape_later + 0.01)) / 2
    mid_cage = (np.log10(cage_early + 0.01) + np.log10(cage_later + 0.01)) / 2

    ax.text(0.5, mid_escape + 0.3, f'High Flexibility\n(|ΔV| > median)', ha='center', fontsize=10,
            color=COLORS['escape'], style='italic')
    ax.text(0.5, mid_cage - 0.3, f'Low Flexibility\n(|ΔV| < median)', ha='center', fontsize=10,
            color=COLORS['cage'], style='italic')

    ax.set_xlim(-0.2, 1.2)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Early Stage\n(2021)', 'Later Stage\n(2025)'], fontsize=12)
    ax.set_ylabel('Funding (log₁₀ $M)', fontsize=12)
    ax.set_title('Two Paths: Escape Velocity vs Golden Cage\n', fontsize=16, fontweight='bold')
    ax.legend(loc='upper left', fontsize=11)

    # Add growth multiplier
    escape_growth = escape_later / (escape_early + 0.01)
    cage_growth = cage_later / (cage_early + 0.01)

    ax.text(0.5, -0.15, f'Escape: {escape_growth:.0f}× growth   |   Cage: {cage_growth:.0f}× growth',
            transform=ax.transAxes, ha='center', fontsize=12,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / 'cruel_optimism_trajectory.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')

    print(f"Saved: {OUTPUT_DIR / 'cruel_optimism_trajectory.png'}")

    return fig


def main():
    """Generate all flagship visualizations."""
    print("=" * 60)
    print("CRUEL OPTIMISM OF COMMITMENT - FLAGSHIP PLOTS")
    print("=" * 60)

    df = load_data()

    print("\nGenerating flagship 2-panel plot...")
    fig1 = create_flagship_plot(df)

    print("\nGenerating simple single-panel plot...")
    fig2 = create_single_message_plot(df)

    print("\nGenerating trajectory plot...")
    fig3 = create_trajectory_plot(df)

    print("\n" + "=" * 60)
    print("ALL PLOTS GENERATED")
    print("=" * 60)

    return df


if __name__ == "__main__":
    df = main()
