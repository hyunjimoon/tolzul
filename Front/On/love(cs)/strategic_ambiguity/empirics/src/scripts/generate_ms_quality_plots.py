#!/usr/bin/env python3
"""
Management Science Quality Plots for Strategic Vagueness Paper

Creates publication-ready figures showing:
1. U-shape relationship between vagueness and survival across industries
2. Statistical tests and confidence intervals
3. Special focus on Transportation's "Double Bind"

Usage:
    python src/scripts/generate_ms_quality_plots.py
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

from src.data_io import load_dataframe

# Publication settings
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Color palette (colorblind-friendly)
COLORS = {
    'software': '#1f77b4',      # Blue
    'hardware': '#ff7f0e',      # Orange
    'transportation': '#d62728', # Red (highlight)
    'medtech': '#2ca02c',       # Green
    'pharma': '#9467bd',        # Purple
}

LABELS = {
    'software': 'Software/SaaS',
    'hardware': 'Hardware/Semiconductor',
    'transportation': 'Transportation',
    'medtech': 'Medical Devices',
    'pharma': 'Pharma/Biotech',
}


def load_industry_data(industry: str) -> pd.DataFrame:
    """Load and prepare industry dataset."""
    nc_path = Path(f'data/outputs/{industry}/dataset.nc')
    if not nc_path.exists():
        raise FileNotFoundError(f"Dataset not found: {nc_path}")

    # Use existing data_io loader which handles netcdf4 properly
    df = load_dataframe(nc_path)
    df_valid = df[df['vagueness'].notna() & df['growth'].notna()].copy()
    return df_valid


def compute_quartile_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Compute survival rates and CIs by quartile."""
    df['vag_q'] = pd.qcut(df['vagueness'].rank(method='first'),
                          q=4, labels=['Q1\n(Low)', 'Q2', 'Q3', 'Q4\n(High)'])

    stats_list = []
    for q in ['Q1\n(Low)', 'Q2', 'Q3', 'Q4\n(High)']:
        subset = df[df['vag_q'] == q]
        n = len(subset)
        successes = subset['growth'].sum()
        rate = subset['growth'].mean()

        # Wilson score interval for proportion CI
        z = 1.96
        denominator = 1 + z**2/n
        center = (rate + z**2/(2*n)) / denominator
        spread = z * np.sqrt((rate*(1-rate) + z**2/(4*n)) / n) / denominator
        ci_lower = max(0, center - spread)
        ci_upper = min(1, center + spread)

        stats_list.append({
            'quartile': q,
            'n': n,
            'successes': successes,
            'rate': rate * 100,
            'ci_lower': ci_lower * 100,
            'ci_upper': ci_upper * 100,
            'se': (ci_upper - ci_lower) / 2 / 1.96 * 100
        })

    return pd.DataFrame(stats_list)


def compute_ushape_test(df: pd.DataFrame) -> dict:
    """Formal U-shape test: compare extremes vs middle."""
    df['vag_q'] = pd.qcut(df['vagueness'].rank(method='first'),
                          q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

    # Get data for each group
    extreme = df[df['vag_q'].isin(['Q1', 'Q4'])]['growth']
    middle = df[df['vag_q'].isin(['Q2', 'Q3'])]['growth']

    # Two-sample proportion test
    n1, n2 = len(extreme), len(middle)
    p1, p2 = extreme.mean(), middle.mean()
    p_pooled = (extreme.sum() + middle.sum()) / (n1 + n2)

    se = np.sqrt(p_pooled * (1 - p_pooled) * (1/n1 + 1/n2))
    z_stat = (p1 - p2) / se
    p_value = 1 - stats.norm.cdf(z_stat)  # One-tailed: extreme > middle

    # Chi-squared test
    contingency = pd.crosstab(df['vag_q'], df['growth'])
    chi2, p_chi2, dof, _ = stats.chi2_contingency(contingency)

    return {
        'extreme_rate': p1 * 100,
        'middle_rate': p2 * 100,
        'diff': (p1 - p2) * 100,
        'z_stat': z_stat,
        'p_value_ushape': p_value,
        'chi2': chi2,
        'p_chi2': p_chi2
    }


def create_combined_figure(industries=['transportation', 'software', 'hardware', 'pharma']):
    """
    Create a 2x2 panel figure for Management Science.

    Layout:
    [A] Transportation (highlighted - Double Bind)
    [B] Software (benchmark - low capital, low uncertainty)
    [C] Hardware (high capital, high uncertainty)
    [D] Pharma (high capital, high uncertainty, regulatory)
    """
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.flatten()

    panel_labels = ['A', 'B', 'C', 'D']

    all_stats = {}

    for idx, industry in enumerate(industries):
        ax = axes[idx]
        print(f"  Processing {industry}...")

        try:
            df = load_industry_data(industry)
            print(f"    Loaded {len(df)} rows")
            stats_df = compute_quartile_stats(df)
            print(f"    Quartile stats: Q1={stats_df['rate'].iloc[0]:.1f}%, Q4={stats_df['rate'].iloc[3]:.1f}%")
            test_results = compute_ushape_test(df)
            print(f"    U-shape diff: {test_results['diff']:.2f}pp")
            all_stats[industry] = {'stats': stats_df, 'test': test_results, 'n': len(df)}
            print(f"    Added to all_stats (now has {len(all_stats)} industries)")

            # Bar plot
            x = np.arange(4)
            bars = ax.bar(x, stats_df['rate'],
                         color=COLORS[industry],
                         alpha=0.8 if industry == 'transportation' else 0.7,
                         edgecolor='black',
                         linewidth=1.5 if industry == 'transportation' else 1)

            # Error bars (95% CI)
            ax.errorbar(x, stats_df['rate'],
                       yerr=[stats_df['rate'] - stats_df['ci_lower'],
                             stats_df['ci_upper'] - stats_df['rate']],
                       fmt='none', ecolor='black', capsize=4, capthick=1.5)

            # U-shape connecting line
            rates = stats_df['rate'].values
            ax.plot(x, rates, 'k--', alpha=0.5, linewidth=1)

            # Highlight extreme quartiles for U-shape
            for i in [0, 3]:
                bars[i].set_edgecolor('#333333')
                bars[i].set_linewidth(2)

            # Labels
            ax.set_xticks(x)
            ax.set_xticklabels(stats_df['quartile'], fontsize=10)
            ax.set_xlabel('Promise Vagueness Level', fontsize=11)
            ax.set_ylabel('Survival to Series B+ (%)', fontsize=11)

            # Title with statistics
            title = f"({panel_labels[idx]}) {LABELS[industry]}"
            ax.set_title(title, fontsize=12, fontweight='bold', loc='left')

            # Add sample size and test result
            n = len(df)
            chi2_p = test_results['p_chi2']
            p_str = f"p < 0.001" if chi2_p < 0.001 else f"p = {chi2_p:.3f}"

            info_text = f"N = {n:,}\nχ² test: {p_str}"
            ax.text(0.97, 0.97, info_text,
                   transform=ax.transAxes,
                   fontsize=9,
                   verticalalignment='top',
                   horizontalalignment='right',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                            edgecolor='gray', alpha=0.9))

            # Add U-shape indicator
            diff = test_results['diff']
            u_text = f"U-shape: Δ = {diff:.1f}pp"
            ax.text(0.03, 0.97, u_text,
                   transform=ax.transAxes,
                   fontsize=9,
                   verticalalignment='top',
                   horizontalalignment='left',
                   fontweight='bold',
                   color='darkgreen' if diff > 0 else 'darkred')

            # Y-axis limit
            max_rate = stats_df['ci_upper'].max()
            ax.set_ylim(0, max_rate * 1.25)

            # Grid
            ax.yaxis.grid(True, linestyle='--', alpha=0.3)
            ax.set_axisbelow(True)

            # Special annotation for Transportation
            if industry == 'transportation':
                ax.annotate('Double Bind:\nHigh Capital × High Uncertainty',
                           xy=(1.5, stats_df['rate'].iloc[1]),
                           xytext=(1.5, stats_df['rate'].iloc[1] + 2),
                           fontsize=8,
                           ha='center',
                           color='darkred',
                           fontweight='bold',
                           arrowprops=dict(arrowstyle='->', color='darkred', lw=1))

        except Exception as e:
            print(f"    ERROR: {e}")
            import traceback
            traceback.print_exc()
            ax.text(0.5, 0.5, f"Error: {e}", transform=ax.transAxes,
                   ha='center', va='center')

    print(f"  Final all_stats has {len(all_stats)} industries: {list(all_stats.keys())}")
    plt.tight_layout()

    # Save
    output_dir = Path('outputs/all/figures')
    output_dir.mkdir(parents=True, exist_ok=True)

    fig.savefig(output_dir / 'fig_ushape_4panel_ms.pdf', format='pdf')
    fig.savefig(output_dir / 'fig_ushape_4panel_ms.png', format='png', dpi=300)

    print(f"\n✅ Figure saved to {output_dir}/fig_ushape_4panel_ms.pdf")

    plt.close(fig)
    return all_stats


def create_transportation_focus_figure():
    """
    Create a detailed figure focusing on Transportation's Double Bind.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Load all industries for comparison
    industries = ['software', 'hardware', 'transportation', 'medtech', 'pharma']
    all_data = {}

    for ind in industries:
        try:
            df = load_industry_data(ind)
            stats_df = compute_quartile_stats(df)
            test = compute_ushape_test(df)
            all_data[ind] = {
                'n': len(df),
                'overall_rate': df['growth'].mean() * 100,
                'q1': stats_df['rate'].iloc[0],
                'q2': stats_df['rate'].iloc[1],
                'q3': stats_df['rate'].iloc[2],
                'q4': stats_df['rate'].iloc[3],
                'murky_middle': (stats_df['rate'].iloc[1] + stats_df['rate'].iloc[2]) / 2,
                'extreme': (stats_df['rate'].iloc[0] + stats_df['rate'].iloc[3]) / 2,
                'ushape_diff': test['diff']
            }
        except:
            pass

    # Panel A: Overall survival rate comparison
    ax1 = axes[0]
    industries_sorted = sorted(all_data.keys(), key=lambda x: all_data[x]['overall_rate'])

    y_pos = np.arange(len(industries_sorted))
    rates = [all_data[ind]['overall_rate'] for ind in industries_sorted]
    colors = [COLORS.get(ind, 'gray') for ind in industries_sorted]

    bars = ax1.barh(y_pos, rates, color=colors, alpha=0.8, edgecolor='black')

    # Highlight transportation if present
    if 'transportation' in industries_sorted:
        trans_idx = industries_sorted.index('transportation')
        bars[trans_idx].set_edgecolor('darkred')
        bars[trans_idx].set_linewidth(2.5)

    ax1.set_yticks(y_pos)
    ax1.set_yticklabels([LABELS.get(ind, ind) for ind in industries_sorted])
    ax1.set_xlabel('Overall Survival Rate to Series B+ (%)', fontsize=11)
    ax1.set_title('(A) Industry Comparison: Overall Survival', fontsize=12, fontweight='bold', loc='left')

    # Add value labels
    for i, (ind, rate) in enumerate(zip(industries_sorted, rates)):
        ax1.text(rate + 0.3, i, f'{rate:.1f}%', va='center', fontsize=10)

    ax1.xaxis.grid(True, linestyle='--', alpha=0.3)
    ax1.set_xlim(0, max(rates) * 1.2)

    # Panel B: U-shape strength (Murky Middle penalty)
    ax2 = axes[1]

    # Compute "Murky Middle Penalty" = Extreme rate - Middle rate
    industries_sorted2 = sorted(all_data.keys(), key=lambda x: all_data[x]['ushape_diff'])
    diffs = [all_data[ind]['ushape_diff'] for ind in industries_sorted2]
    colors2 = [COLORS.get(ind, 'gray') for ind in industries_sorted2]

    y_pos2 = np.arange(len(industries_sorted2))
    bars2 = ax2.barh(y_pos2, diffs, color=colors2, alpha=0.8, edgecolor='black')

    # Highlight transportation if present
    if 'transportation' in industries_sorted2:
        trans_idx2 = industries_sorted2.index('transportation')
        bars2[trans_idx2].set_edgecolor('darkred')
        bars2[trans_idx2].set_linewidth(2.5)

    ax2.set_yticks(y_pos2)
    ax2.set_yticklabels([LABELS.get(ind, ind) for ind in industries_sorted2])
    ax2.set_xlabel('U-Shape Strength: (Q1+Q4)/2 − (Q2+Q3)/2 (pp)', fontsize=11)
    ax2.set_title('(B) "Murky Middle" Penalty by Industry', fontsize=12, fontweight='bold', loc='left')

    # Add value labels
    for i, (ind, diff) in enumerate(zip(industries_sorted2, diffs)):
        ax2.text(diff + 0.1, i, f'+{diff:.1f}pp', va='center', fontsize=10)

    ax2.xaxis.grid(True, linestyle='--', alpha=0.3)
    ax2.axvline(0, color='black', linewidth=0.5)

    # Add annotation
    ax2.annotate('Stronger U-shape →\nClearer "Analyst or Believer" strategy',
                xy=(max(diffs) * 0.7, len(diffs) - 1),
                fontsize=9, ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()

    # Save
    output_dir = Path('outputs/all/figures')
    fig.savefig(output_dir / 'fig_transportation_focus_ms.pdf', format='pdf')
    fig.savefig(output_dir / 'fig_transportation_focus_ms.png', format='png', dpi=300)

    print(f"✅ Figure saved to {output_dir}/fig_transportation_focus_ms.pdf")

    plt.close(fig)
    return all_data


def create_statistical_summary_table(all_stats: dict) -> pd.DataFrame:
    """Create a summary table for the paper."""
    rows = []

    for industry, data in all_stats.items():
        stats_df = data['stats']
        test = data['test']
        n = data['n']

        rows.append({
            'Industry': LABELS.get(industry, industry),
            'N': n,
            'Q1 (Low V)': f"{stats_df['rate'].iloc[0]:.1f}%",
            'Q2': f"{stats_df['rate'].iloc[1]:.1f}%",
            'Q3': f"{stats_df['rate'].iloc[2]:.1f}%",
            'Q4 (High V)': f"{stats_df['rate'].iloc[3]:.1f}%",
            'U-Shape Δ': f"+{test['diff']:.1f}pp",
            'χ² (df=3)': f"{test['chi2']:.1f}",
            'p-value': '<0.001' if test['p_chi2'] < 0.001 else f"{test['p_chi2']:.3f}"
        })

    return pd.DataFrame(rows)


def main():
    print("="*70)
    print("MANAGEMENT SCIENCE QUALITY FIGURE GENERATOR")
    print("="*70)

    # Create main 4-panel figure
    print("\n[1] Creating 4-panel U-shape figure...")
    all_stats = create_combined_figure(
        industries=['transportation', 'software', 'hardware', 'pharma']
    )

    # Create Transportation focus figure
    print("\n[2] Creating Transportation focus figure...")
    try:
        all_data = create_transportation_focus_figure()
    except Exception as e:
        print(f"    WARNING: Transportation focus figure failed: {e}")

    # Create summary table
    print("\n[2] Creating statistical summary table...")
    summary_table = create_statistical_summary_table(all_stats)

    print("\n" + "="*70)
    print("STATISTICAL SUMMARY TABLE")
    print("="*70)
    print(summary_table.to_string(index=False))

    # Save table
    output_dir = Path('outputs/all/figures')
    summary_table.to_csv(output_dir / 'table_ushape_summary.csv', index=False)
    print(f"\n✅ Table saved to {output_dir}/table_ushape_summary.csv")

    # LaTeX table
    latex = summary_table.to_latex(index=False, escape=False)
    with open(output_dir / 'table_ushape_summary.tex', 'w') as f:
        f.write(latex)
    print(f"✅ LaTeX table saved to {output_dir}/table_ushape_summary.tex")

    print("\n" + "="*70)
    print("COMPLETE")
    print("="*70)


if __name__ == '__main__':
    main()
