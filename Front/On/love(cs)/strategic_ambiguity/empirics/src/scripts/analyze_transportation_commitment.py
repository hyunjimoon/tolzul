#!/usr/bin/env python3
"""
Transportation Ventures: Cruel Optimism of Commitment Analysis
================================================================

Generates Plot 1 (Stopped Optionality) and Plot 2 (Funded Trap Heatmap)
for Transportation ventures specifically.

This script tests the key hypothesis:
- H_funding: Early funding → reduced |ΔV| (stopped optionality)
- H_trap: Middle V × High Funding = worst outcomes (funded trap)

Author: Claude Code
Created: 2025-12-04
"""

import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from scipy.stats import spearmanr, pearsonr
import warnings
warnings.filterwarnings('ignore')

# Paths
DATA_DIR = Path(__file__).parent.parent.parent / "data"
PROCESSED_DIR = DATA_DIR / "processed"
RAW_DIR = DATA_DIR / "raw"
OUTPUT_DIR = Path(__file__).parent.parent.parent / "reports" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Transportation keywords for filtering
TRANSPORTATION_KEYWORDS = [
    'transport', 'logistics', 'delivery', 'shipping', 'freight',
    'vehicle', 'automotive', 'fleet', 'mobility', 'autonomous',
    'electric vehicle', 'ev ', 'drone', 'aviation', 'aerospace',
    'trucking', 'supply chain', 'last mile', 'rideshare', 'ride-hailing',
    'car', 'bus', 'train', 'rail', 'maritime', 'cargo'
]


def load_and_filter_transportation():
    """Load vagueness timeseries and filter for Transportation companies."""
    print("=" * 60)
    print("LOADING DATA")
    print("=" * 60)

    # Load NetCDF for numeric data
    ds = xr.open_dataset(PROCESSED_DIR / "vagueness_timeseries.nc")
    print(f"Loaded {ds.sizes['company']:,} companies × {ds.sizes['year']} years")

    # Load parquet for descriptions (to identify Transportation)
    df_full = pd.read_parquet(PROCESSED_DIR / "vagueness_timeseries.parquet")
    print(f"Loaded parquet with {len(df_full):,} rows")

    # Also load raw 2021 data for Keywords
    df_2021_raw = pd.read_parquet(RAW_DIR / "Company20211201.parquet")
    keywords_map = df_2021_raw.set_index('CompanyID')['Keywords'].to_dict()

    # Get 2021 descriptions for sector identification
    df_2021 = df_full[df_full['year'] == 2021].copy()
    df_2021['keywords'] = df_2021['company_id'].map(keywords_map).fillna('')

    # Identify Transportation companies
    def is_transportation(row):
        text = f"{row.get('description', '')} {row.get('keywords', '')}".lower()
        return any(kw in text for kw in TRANSPORTATION_KEYWORDS)

    df_2021['is_transport'] = df_2021.apply(is_transportation, axis=1)
    transport_companies = set(df_2021[df_2021['is_transport']]['company_id'])

    print(f"\nTransportation companies identified: {len(transport_companies):,}")

    # Filter main dataset
    df_transport = df_full[df_full['company_id'].isin(transport_companies)].copy()
    print(f"Transportation records: {len(df_transport):,}")

    # Create panel structure
    df_panel = df_transport.pivot(index='company_id', columns='year', values='V')
    df_panel.columns = [f'V_{y}' for y in df_panel.columns]

    # Add delta_V
    df_delta = df_transport.pivot(index='company_id', columns='year', values='delta_V')
    df_delta.columns = [f'delta_V_{y}' for y in df_delta.columns]
    df_panel = df_panel.join(df_delta)

    # Add first financing
    df_meta = df_transport[df_transport['year'] == 2021][['company_id', 'first_financing_size', 'company_name']].set_index('company_id')
    df_panel = df_panel.join(df_meta)

    # Calculate total delta V
    df_panel['total_delta_V'] = df_panel['V_2025'] - df_panel['V_2021']
    df_panel['abs_total_delta_V'] = df_panel['total_delta_V'].abs()

    # Filter to complete cases
    df_panel = df_panel.dropna(subset=['V_2021', 'V_2025', 'first_financing_size'])
    print(f"Complete cases (with funding data): {len(df_panel):,}")

    return df_panel, ds


def plot1_stopped_optionality(df):
    """
    Plot 1: Stopped Optionality

    X-axis: First Financing Size (log scale)
    Y-axis: |total_delta_V| (absolute strategic flexibility)

    Expected: Negative correlation (more funding → less strategic change)
    """
    print("\n" + "=" * 60)
    print("PLOT 1: STOPPED OPTIONALITY")
    print("=" * 60)

    # Prepare data
    x = df['first_financing_size'].values
    y = df['abs_total_delta_V'].values

    # Remove zeros for log scale
    mask = (x > 0) & (~np.isnan(x)) & (~np.isnan(y))
    x_valid = x[mask]
    y_valid = y[mask]

    # Log transform funding
    x_log = np.log10(x_valid + 0.001)

    # Correlation
    r_spearman, p_spearman = spearmanr(x_valid, y_valid)
    r_pearson, p_pearson = pearsonr(x_log, y_valid)

    print(f"Sample size: {len(x_valid):,}")
    print(f"Spearman correlation: r = {r_spearman:.3f}, p = {p_spearman:.4f}")
    print(f"Pearson (log funding): r = {r_pearson:.3f}, p = {p_pearson:.4f}")

    # Create figure
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: Scatter plot
    ax1 = axes[0]
    ax1.scatter(x_valid, y_valid, alpha=0.3, s=20, c='steelblue', edgecolors='none')

    # Add trend line
    z = np.polyfit(x_log, y_valid, 1)
    p_fit = np.poly1d(z)
    x_range = np.logspace(np.log10(x_valid.min()), np.log10(x_valid.max()), 100)
    ax1.plot(x_range, p_fit(np.log10(x_range)), 'r-', linewidth=2, label=f'Trend (r={r_spearman:.2f})')

    ax1.set_xscale('log')
    ax1.set_xlabel('First Financing Size ($M)', fontsize=12)
    ax1.set_ylabel('|ΔV| (2021→2025)', fontsize=12)
    ax1.set_title('Transportation: Stopped Optionality Test\n(More Funding → Less Strategic Flexibility?)', fontsize=13)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Annotation
    sign = "✓ CONFIRMED" if r_spearman < 0 else "✗ NOT CONFIRMED"
    ax1.text(0.05, 0.95, f'H_funding: {sign}\nSpearman r = {r_spearman:.3f}***' if p_spearman < 0.001 else f'H_funding: {sign}\nSpearman r = {r_spearman:.3f} (p={p_spearman:.3f})',
             transform=ax1.transAxes, fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # Right: Box plot by funding quartile
    ax2 = axes[1]
    df_plot = df.copy()
    df_plot['funding_quartile'] = pd.qcut(df_plot['first_financing_size'], 4, labels=['Q1 (Low)', 'Q2', 'Q3', 'Q4 (High)'])

    # Box plot
    funding_groups = ['Q1 (Low)', 'Q2', 'Q3', 'Q4 (High)']
    box_data = [df_plot[df_plot['funding_quartile'] == q]['abs_total_delta_V'].dropna() for q in funding_groups]

    bp = ax2.boxplot(box_data, labels=funding_groups, patch_artist=True)
    colors = ['#2ecc71', '#f1c40f', '#e67e22', '#e74c3c']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    # Add means
    means = [d.mean() for d in box_data]
    ax2.plot(range(1, 5), means, 'ko-', markersize=8, label='Mean')

    ax2.set_xlabel('First Financing Quartile', fontsize=12)
    ax2.set_ylabel('|ΔV| (2021→2025)', fontsize=12)
    ax2.set_title('Strategic Flexibility by Funding Level\n(Lower = More "Locked In")', fontsize=13)
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')

    # Print quartile statistics
    print("\n|ΔV| by Funding Quartile:")
    for i, q in enumerate(funding_groups):
        print(f"  {q}: mean={means[i]:.2f}, median={box_data[i].median():.2f}, n={len(box_data[i])}")

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'plot1_stopped_optionality_transportation.png', dpi=150, bbox_inches='tight')
    plt.savefig(OUTPUT_DIR / 'plot1_stopped_optionality_transportation.pdf', bbox_inches='tight')
    print(f"\nSaved: {OUTPUT_DIR / 'plot1_stopped_optionality_transportation.png'}")

    return fig


def plot2_funded_trap_heatmap(df):
    """
    Plot 2: Funded Trap Heatmap

    X-axis: Funding Quartile
    Y-axis: V Quartile (2021)
    Color: Mean |ΔV| (strategic flexibility)

    Expected: Middle V × High Funding = lowest |ΔV| (most locked in = trap)
    """
    print("\n" + "=" * 60)
    print("PLOT 2: FUNDED TRAP HEATMAP")
    print("=" * 60)

    # Create quartiles
    df_plot = df.copy()
    df_plot['V_quartile'] = pd.qcut(df_plot['V_2021'], 4, labels=['Q1 (Low V)', 'Q2', 'Q3', 'Q4 (High V)'])
    df_plot['funding_quartile'] = pd.qcut(df_plot['first_financing_size'], 4, labels=['Low', 'Med-Low', 'Med-High', 'High'])

    # Create pivot table: mean |ΔV|
    pivot_abs_dv = df_plot.pivot_table(
        values='abs_total_delta_V',
        index='V_quartile',
        columns='funding_quartile',
        aggfunc='mean'
    )

    # Also compute count
    pivot_count = df_plot.pivot_table(
        values='abs_total_delta_V',
        index='V_quartile',
        columns='funding_quartile',
        aggfunc='count'
    )

    print("\nMean |ΔV| by V×Funding (Lower = More Locked In):")
    print(pivot_abs_dv.round(2))

    print("\nSample sizes:")
    print(pivot_count.astype(int))

    # Create figure
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: Heatmap of |ΔV| (flexibility)
    ax1 = axes[0]
    sns.heatmap(pivot_abs_dv, annot=True, fmt='.1f', cmap='RdYlGn',
                ax=ax1, cbar_kws={'label': 'Mean |ΔV|'})
    ax1.set_title('Strategic Flexibility (|ΔV|) by V × Funding\n(Red = Locked In, Green = Flexible)', fontsize=12)
    ax1.set_xlabel('First Financing Quartile', fontsize=11)
    ax1.set_ylabel('Vagueness Quartile (V_2021)', fontsize=11)

    # Right: Interaction visualization
    ax2 = axes[1]

    # Plot lines for each funding level
    v_quartiles = ['Q1 (Low V)', 'Q2', 'Q3', 'Q4 (High V)']
    funding_levels = ['Low', 'Med-Low', 'Med-High', 'High']
    colors = ['#2ecc71', '#f1c40f', '#e67e22', '#e74c3c']

    for i, fund in enumerate(funding_levels):
        y_vals = [pivot_abs_dv.loc[v, fund] for v in v_quartiles]
        ax2.plot(range(4), y_vals, 'o-', color=colors[i], linewidth=2, markersize=8, label=f'Funding: {fund}')

    ax2.set_xticks(range(4))
    ax2.set_xticklabels(['Low V\n(Analyst)', 'Q2\n(Middle)', 'Q3\n(Middle)', 'High V\n(Believer)'])
    ax2.set_xlabel('Vagueness Level', fontsize=11)
    ax2.set_ylabel('Mean |ΔV| (Strategic Flexibility)', fontsize=11)
    ax2.set_title('Funding × Vagueness Interaction\n(Funded Trap = Middle V + High Funding)', fontsize=12)
    ax2.legend(loc='upper right')
    ax2.grid(True, alpha=0.3)

    # Identify trap cells
    middle_v = ['Q2', 'Q3']
    extreme_v = ['Q1 (Low V)', 'Q4 (High V)']

    trap_avg = pivot_abs_dv.loc[middle_v, 'High'].mean()
    extreme_avg = pivot_abs_dv.loc[extreme_v, 'High'].mean()

    trap_penalty = extreme_avg - trap_avg

    print(f"\n=== FUNDED TRAP TEST ===")
    print(f"Middle V × High Funding (trap): mean |ΔV| = {trap_avg:.2f}")
    print(f"Extreme V × High Funding: mean |ΔV| = {extreme_avg:.2f}")
    print(f"Trap Effect: {trap_penalty:.2f} (positive = trap confirmed)")

    # Add annotation
    if trap_penalty > 0:
        ax2.annotate('FUNDED\nTRAP', xy=(1.5, trap_avg), fontsize=12, color='red', weight='bold',
                    ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'plot2_funded_trap_heatmap_transportation.png', dpi=150, bbox_inches='tight')
    plt.savefig(OUTPUT_DIR / 'plot2_funded_trap_heatmap_transportation.pdf', bbox_inches='tight')
    print(f"\nSaved: {OUTPUT_DIR / 'plot2_funded_trap_heatmap_transportation.png'}")

    return fig, pivot_abs_dv


def main():
    """Main analysis pipeline."""
    print("\n" + "=" * 70)
    print("TRANSPORTATION VENTURES: CRUEL OPTIMISM OF COMMITMENT ANALYSIS")
    print("=" * 70)

    # Load and filter data
    df, ds = load_and_filter_transportation()

    # Summary statistics
    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)
    print(f"V_2021: mean={df['V_2021'].mean():.1f}, std={df['V_2021'].std():.1f}")
    print(f"V_2025: mean={df['V_2025'].mean():.1f}, std={df['V_2025'].std():.1f}")
    print(f"total_delta_V: mean={df['total_delta_V'].mean():.2f}, std={df['total_delta_V'].std():.2f}")
    print(f"|total_delta_V|: mean={df['abs_total_delta_V'].mean():.2f}, std={df['abs_total_delta_V'].std():.2f}")
    print(f"first_financing_size: median={df['first_financing_size'].median():.2f}M, mean={df['first_financing_size'].mean():.2f}M")

    # Generate plots
    fig1 = plot1_stopped_optionality(df)
    fig2, heatmap_data = plot2_funded_trap_heatmap(df)

    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
    print(f"\nOutput files saved to: {OUTPUT_DIR}")
    print("  - plot1_stopped_optionality_transportation.png")
    print("  - plot2_funded_trap_heatmap_transportation.png")

    # Show plots interactively if not in headless mode
    try:
        plt.show()
    except:
        pass

    return df, heatmap_data


if __name__ == "__main__":
    df, heatmap = main()
