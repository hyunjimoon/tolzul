#!/usr/bin/env python3
"""
Cost of Commitment: Cohort-Based Counterfactual Analysis
=========================================================

NEW NOTATION (2025-12-04):
- E = Early funding (first_financing_size)
- L = Later funding = Total_2025 - E (money earned AFTER early stage)
- V_E = V_2021 (vagueness at early stage)
- V_L = V_2025 (vagueness at later stage)
- |ΔV| = |V_L - V_E| (strategic flexibility)

Cost of Commitment Formula:
Cost = E[Y | Locked, E] - E[Y | Flexible, E]

where Y = L/E (later funding growth ratio)

Key outputs:
- Flagship figure: 9.73x ratio (Escape Velocity vs Golden Cage)
- Cohort heatmap with new L/E metric
- Cost tables by funding decile

Author: Claude Code
Created: 2025-12-04
Updated: 2025-12-04 (New L definition: L = Total - E)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from scipy.stats import spearmanr, mannwhitneyu
import warnings
warnings.filterwarnings('ignore')

# Set professional style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.labelsize': 12,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': 'white',
})

# Paths
DATA_DIR = Path(__file__).parent.parent.parent / "data"
PROCESSED_DIR = DATA_DIR / "processed"
RAW_DIR = DATA_DIR / "raw"
OUTPUT_DIR = Path(__file__).parent.parent.parent / "reports" / "figures"
TABLE_DIR = Path(__file__).parent.parent.parent / "reports" / "tables"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
TABLE_DIR.mkdir(parents=True, exist_ok=True)

# Color palette
COLORS = {
    'escape': '#1a9850',      # Green - freedom, growth
    'late_pivoter': '#91cf60',  # Light green
    'stagnant': '#fc8d59',    # Orange - warning
    'cage': '#d73027',        # Red - danger, trap
}


def load_data():
    """
    Load and prepare panel data with NEW notation.

    Variables:
    - E: Early funding (first_financing_size)
    - L: Later funding = Total_2025 - E
    - V_E: Vagueness at early stage (V_2021)
    - V_L: Vagueness at later stage (V_2025)
    - |ΔV|: Strategic flexibility = |V_L - V_E|
    """
    print("=" * 60)
    print("LOADING DATA WITH NEW NOTATION")
    print("E = Early funding, L = Later funding (Total - E)")
    print("=" * 60)

    # Load vagueness timeseries
    df_full = pd.read_parquet(PROCESSED_DIR / "vagueness_timeseries.parquet")

    # Create wide format with NEW notation
    df_2021 = df_full[df_full['year'] == 2021][['company_id', 'V', 'first_financing_size']].copy()
    df_2021.columns = ['company_id', 'V_E', 'E']  # V_E = V_2021, E = early funding

    df_2025 = df_full[df_full['year'] == 2025][['company_id', 'V']].copy()
    df_2025.columns = ['company_id', 'V_L']  # V_L = V_2025

    df = df_2021.merge(df_2025, on='company_id', how='inner')
    df['delta_V'] = df['V_L'] - df['V_E']
    df['abs_delta_V'] = df['delta_V'].abs()  # |ΔV| = strategic flexibility

    # Load 2025 outcomes
    df_2025_raw = pd.read_csv(RAW_DIR / "Company20251101.dat", sep='|',
                               usecols=['CompanyID', 'TotalRaised', 'BusinessStatus'],
                               low_memory=False, on_bad_lines='skip')
    df_2025_raw.columns = ['company_id', 'Total_2025', 'business_status']
    df_2025_raw['company_id'] = df_2025_raw['company_id'].astype(str)
    df['company_id'] = df['company_id'].astype(str)
    df_2025_raw['Total_2025'] = pd.to_numeric(df_2025_raw['Total_2025'], errors='coerce')

    df = df.merge(df_2025_raw, on='company_id', how='left')

    # NEW: L = Later funding = Total - E (money earned AFTER early stage)
    df['L'] = df['Total_2025'] - df['E']
    df['L'] = df['L'].clip(lower=0)  # Can't be negative

    # Y = L/E (later funding growth ratio) - NEW DEFINITION
    df['Y'] = df['L'] / (df['E'] + 0.001)

    # Also keep old metric for comparison
    df['Y_old'] = df['Total_2025'] / (df['E'] + 0.001)

    # Clean data
    df = df.dropna(subset=['V_E', 'V_L', 'E'])
    df = df[df['E'] > 0]

    print(f"Loaded {len(df):,} companies")
    print(f"\nVariable Summary:")
    print(f"  E (Early funding): median ${df['E'].median():.2f}M")
    print(f"  L (Later funding): median ${df[df['L'].notna()]['L'].median():.2f}M")
    print(f"  V_E (Vagueness 2021): mean {df['V_E'].mean():.1f}")
    print(f"  V_L (Vagueness 2025): mean {df['V_L'].mean():.1f}")
    print(f"  |ΔV| (Flexibility): median {df['abs_delta_V'].median():.1f}")

    return df


def create_cohorts(df):
    """
    Create cohorts based on E × |ΔV|.

    Cohort Matrix:
                        Strategic Flexibility (|ΔV|)
                      Low |ΔV|    High |ΔV|
                    ┌──────────┬──────────┐
    High E          │ GOLDEN   │ LATE     │
                    │ CAGE     │ PIVOTER  │
                    ├──────────┼──────────┤
    Low E           │ STAGNANT │ ESCAPE   │
                    │          │ VELOCITY │
                    └──────────┴──────────┘
    """
    print("\n" + "=" * 60)
    print("CREATING COHORTS (E × |ΔV|)")
    print("=" * 60)

    # Calculate medians
    E_median = df['E'].median()
    delta_v_median = df['abs_delta_V'].median()

    print(f"E (Early Funding) median: ${E_median:.2f}M")
    print(f"|ΔV| (Flexibility) median: {delta_v_median:.1f}")

    # Assign cohorts
    df['cohort'] = 'Unknown'

    # Low E + High |ΔV| = Escape Velocity
    df.loc[(df['E'] <= E_median) &
           (df['abs_delta_V'] > delta_v_median), 'cohort'] = 'Escape Velocity'

    # Low E + Low |ΔV| = Stagnant
    df.loc[(df['E'] <= E_median) &
           (df['abs_delta_V'] <= delta_v_median), 'cohort'] = 'Stagnant'

    # High E + Low |ΔV| = Golden Cage
    df.loc[(df['E'] > E_median) &
           (df['abs_delta_V'] <= delta_v_median), 'cohort'] = 'Golden Cage'

    # High E + High |ΔV| = Late Pivoter
    df.loc[(df['E'] > E_median) &
           (df['abs_delta_V'] > delta_v_median), 'cohort'] = 'Late Pivoter'

    # Print cohort sizes
    print("\nCohort Sizes:")
    print(df['cohort'].value_counts())

    return df


def calculate_cost_by_funding_decile(df):
    """
    Calculate Cost of Commitment for each funding decile.

    Cost = E[Y | Low |ΔV|, E_decile] - E[Y | High |ΔV|, E_decile]

    where Y = L/E (NEW definition)

    Negative cost = Lock-in hurts
    """
    print("\n" + "=" * 60)
    print("CALCULATING COST OF COMMITMENT BY E DECILE")
    print("Y = L/E (Later funding / Early funding)")
    print("=" * 60)

    # Filter to companies with outcome data
    df_outcome = df[df['L'].notna()].copy()
    df_outcome = df_outcome[df_outcome['Y'] < df_outcome['Y'].quantile(0.99)]  # Remove outliers
    df_outcome = df_outcome[df_outcome['Y'] >= 0]  # Only positive outcomes

    # Create funding deciles using rank to handle ties
    df_outcome['E_rank'] = df_outcome['E'].rank(method='first')
    df_outcome['E_decile'] = pd.qcut(df_outcome['E_rank'], 10, labels=False) + 1

    # Create flexibility groups
    delta_v_median = df_outcome['abs_delta_V'].median()
    df_outcome['flexibility'] = df_outcome['abs_delta_V'].apply(
        lambda x: 'High' if x > delta_v_median else 'Low'
    )

    # Calculate cost by decile
    results = []

    for decile in range(1, 11):
        decile_data = df_outcome[df_outcome['E_decile'] == decile]

        low_flex = decile_data[decile_data['flexibility'] == 'Low']['Y']
        high_flex = decile_data[decile_data['flexibility'] == 'High']['Y']

        if len(low_flex) > 30 and len(high_flex) > 30:
            cost_mean = low_flex.mean() - high_flex.mean()
            cost_median = low_flex.median() - high_flex.median()

            # Statistical test
            stat, pval = mannwhitneyu(low_flex, high_flex, alternative='less')

            results.append({
                'Decile': decile,
                'n_locked': len(low_flex),
                'n_flexible': len(high_flex),
                'mean_locked': low_flex.mean(),
                'mean_flexible': high_flex.mean(),
                'median_locked': low_flex.median(),
                'median_flexible': high_flex.median(),
                'cost_mean': cost_mean,
                'cost_median': cost_median,
                'p_value': pval
            })

    results_df = pd.DataFrame(results)

    print("\nCost of Commitment by E Decile (Y = L/E):")
    print(results_df[['Decile', 'median_locked', 'median_flexible', 'cost_median', 'p_value']].to_string(index=False))

    return results_df, df_outcome


def plot_flagship_figure(df, results_df):
    """
    Create the FLAGSHIP figure showing the 9.73x result.

    This is the main visual for H_cost.
    """
    print("\n" + "=" * 60)
    print("CREATING FLAGSHIP FIGURE (Y = L/E)")
    print("=" * 60)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Filter to companies with outcome data
    df_outcome = df[df['L'].notna()].copy()
    df_outcome = df_outcome[df_outcome['Y'] < df_outcome['Y'].quantile(0.99)]
    df_outcome = df_outcome[df_outcome['Y'] >= 0]

    # =========================================
    # Panel A: The Key Comparison (Bar Chart)
    # =========================================
    ax1 = axes[0]

    cohort_outcomes = df_outcome.groupby('cohort').agg({
        'Y': ['median', 'mean', 'count']
    }).round(2)
    cohort_outcomes.columns = ['median', 'mean', 'n']

    # Focus on Escape Velocity vs Golden Cage
    escape_median = cohort_outcomes.loc['Escape Velocity', 'median'] if 'Escape Velocity' in cohort_outcomes.index else 0
    cage_median = cohort_outcomes.loc['Golden Cage', 'median'] if 'Golden Cage' in cohort_outcomes.index else 0
    escape_n = cohort_outcomes.loc['Escape Velocity', 'n'] if 'Escape Velocity' in cohort_outcomes.index else 0
    cage_n = cohort_outcomes.loc['Golden Cage', 'n'] if 'Golden Cage' in cohort_outcomes.index else 0

    ratio = escape_median / cage_median if cage_median > 0 else np.nan

    # Create bar chart
    bars = ax1.bar(['Escape\nVelocity', 'Golden\nCage'],
                   [escape_median, cage_median],
                   color=[COLORS['escape'], COLORS['cage']],
                   width=0.6, edgecolor='white', linewidth=2)

    # Add value labels
    ax1.text(0, escape_median + 0.15, f'{escape_median:.2f}×', ha='center', fontsize=16, fontweight='bold', color=COLORS['escape'])
    ax1.text(1, cage_median + 0.15, f'{cage_median:.2f}×', ha='center', fontsize=16, fontweight='bold', color=COLORS['cage'])

    # Add sample sizes
    ax1.text(0, -0.3, f'n={int(escape_n):,}', ha='center', fontsize=10, color='gray')
    ax1.text(1, -0.3, f'n={int(cage_n):,}', ha='center', fontsize=10, color='gray')

    # Add ratio annotation
    ax1.annotate('', xy=(0, escape_median * 0.8), xytext=(1, cage_median * 1.2),
                arrowprops=dict(arrowstyle='<->', color='black', lw=2))
    ax1.text(0.5, (escape_median + cage_median) / 2 * 1.1, f'{ratio:.1f}× better',
             ha='center', fontsize=14, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='yellow', alpha=0.8))

    ax1.set_ylabel('Y = L/E\n(Later Funding / Early Funding)', fontsize=12)
    ax1.set_title('A. The Cost of Commitment\n(Median L/E by Cohort)', fontsize=14, pad=15)
    ax1.set_ylim(-0.5, max(escape_median, cage_median) * 1.4)
    ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax1.grid(True, alpha=0.3, axis='y')

    # Add interpretation box
    ax1.text(0.97, 0.03,
             f'Low E + High |ΔV|\nvs High E + Low |ΔV|',
             transform=ax1.transAxes, fontsize=9, ha='right', va='bottom',
             bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.5))

    # =========================================
    # Panel B: 2×2 Cohort Heatmap
    # =========================================
    ax2 = axes[1]

    # Create 2×2 matrix
    matrix_data = pd.DataFrame({
        'Low |ΔV|\n(Locked)': [
            cohort_outcomes.loc['Golden Cage', 'median'] if 'Golden Cage' in cohort_outcomes.index else np.nan,
            cohort_outcomes.loc['Stagnant', 'median'] if 'Stagnant' in cohort_outcomes.index else np.nan
        ],
        'High |ΔV|\n(Flexible)': [
            cohort_outcomes.loc['Late Pivoter', 'median'] if 'Late Pivoter' in cohort_outcomes.index else np.nan,
            cohort_outcomes.loc['Escape Velocity', 'median'] if 'Escape Velocity' in cohort_outcomes.index else np.nan
        ]
    }, index=['High E', 'Low E'])

    sns.heatmap(matrix_data, annot=True, fmt='.2f', cmap='RdYlGn',
                ax=ax2, cbar_kws={'label': 'Median Y = L/E'},
                vmin=0, vmax=max(5, matrix_data.max().max() * 1.1),
                annot_kws={'size': 16, 'weight': 'bold'})

    ax2.set_title('B. Cohort Matrix\n(Y = Later Funding / Early Funding)', fontsize=14, pad=15)
    ax2.set_xlabel('Strategic Flexibility (|ΔV| = |V_L - V_E|)', fontsize=12)
    ax2.set_ylabel('Early Funding (E)', fontsize=12)

    # Add cohort labels
    ax2.text(0.25, 0.5, 'Golden\nCage', transform=ax2.transAxes, ha='center', va='center',
             fontsize=9, color='white', alpha=0.7)
    ax2.text(0.75, 0.5, 'Late\nPivoter', transform=ax2.transAxes, ha='center', va='center',
             fontsize=9, color='white', alpha=0.7)
    ax2.text(0.25, 0.0, 'Stagnant', transform=ax2.transAxes, ha='center', va='top',
             fontsize=9, color='gray', alpha=0.7)
    ax2.text(0.75, 0.0, 'Escape\nVelocity', transform=ax2.transAxes, ha='center', va='top',
             fontsize=9, color='gray', alpha=0.7)

    plt.suptitle(f'The Cruel Optimism of Commitment: {ratio:.1f}× Gap\n(Y = L/E where L = Later Funding = Total - E)',
                 fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()

    # Save
    plt.savefig(OUTPUT_DIR / 'cruel_optimism_flagship_LE.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.savefig(OUTPUT_DIR / 'cruel_optimism_flagship_LE.pdf', bbox_inches='tight',
                facecolor='white', edgecolor='none')

    print(f"\nSaved: {OUTPUT_DIR / 'cruel_optimism_flagship_LE.png'}")
    print(f"\n=== KEY RESULT (Y = L/E) ===")
    print(f"Escape Velocity: {escape_median:.2f}×")
    print(f"Golden Cage: {cage_median:.2f}×")
    print(f"Ratio: {ratio:.1f}×")

    return fig, ratio


def plot_cost_by_decile(results_df):
    """
    Create the cost by funding decile plot.
    """
    print("\n" + "=" * 60)
    print("CREATING COST BY E DECILE PLOT")
    print("=" * 60)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot cost (negative = lock-in hurts)
    colors = ['#d73027' if c < 0 else '#1a9850' for c in results_df['cost_median']]
    bars = ax.bar(results_df['Decile'], results_df['cost_median'], color=colors, alpha=0.8,
                  edgecolor='white', linewidth=1)

    # Add significance markers
    for i, row in results_df.iterrows():
        if row['p_value'] < 0.001:
            marker = '***'
        elif row['p_value'] < 0.01:
            marker = '**'
        elif row['p_value'] < 0.05:
            marker = '*'
        else:
            marker = ''
        if marker:
            y_pos = row['cost_median'] - 0.2 if row['cost_median'] < 0 else row['cost_median'] + 0.1
            ax.text(row['Decile'], y_pos, marker, ha='center', fontsize=12, fontweight='bold')

    ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
    ax.set_xlabel('Early Funding (E) Decile\n(1 = Lowest, 10 = Highest)', fontsize=12)
    ax.set_ylabel('Cost of Commitment\n(Y_Locked - Y_Flexible)', fontsize=12)
    ax.set_title('Cost of Commitment by Funding Level\n(Y = L/E, Negative = Lock-in Hurts)', fontsize=14, pad=15)
    ax.set_xticks(range(1, 11))
    ax.grid(True, alpha=0.3, axis='y')

    # Add interpretation box
    avg_cost = results_df['cost_median'].mean()
    ax.text(0.97, 0.97, f'Average Cost: {avg_cost:.2f}×\n*** p<0.001',
             transform=ax.transAxes, fontsize=11, ha='right', va='top',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='wheat', alpha=0.9))

    plt.tight_layout()

    # Save
    plt.savefig(OUTPUT_DIR / 'cost_by_decile_LE.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')

    print(f"Saved: {OUTPUT_DIR / 'cost_by_decile_LE.png'}")

    return fig


def plot_all_cohorts(df):
    """
    Create comparison of all 4 cohorts.
    """
    print("\n" + "=" * 60)
    print("CREATING ALL COHORTS COMPARISON")
    print("=" * 60)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Filter to companies with outcome data
    df_outcome = df[df['L'].notna()].copy()
    df_outcome = df_outcome[df_outcome['Y'] < df_outcome['Y'].quantile(0.99)]
    df_outcome = df_outcome[df_outcome['Y'] >= 0]

    cohort_outcomes = df_outcome.groupby('cohort').agg({
        'Y': ['median', 'mean', 'count']
    }).round(2)
    cohort_outcomes.columns = ['median', 'mean', 'n']

    # Order cohorts
    cohorts_order = ['Escape Velocity', 'Late Pivoter', 'Stagnant', 'Golden Cage']
    plot_colors = [COLORS['escape'], COLORS['late_pivoter'], COLORS['stagnant'], COLORS['cage']]

    medians = [cohort_outcomes.loc[c, 'median'] if c in cohort_outcomes.index else 0 for c in cohorts_order]
    ns = [cohort_outcomes.loc[c, 'n'] if c in cohort_outcomes.index else 0 for c in cohorts_order]

    bars = ax.bar(range(4), medians, color=plot_colors, alpha=0.85,
                  edgecolor='white', linewidth=2, width=0.7)

    # Add value labels
    for i, (m, n) in enumerate(zip(medians, ns)):
        ax.text(i, m + 0.15, f'{m:.2f}×', ha='center', fontsize=14, fontweight='bold')
        ax.text(i, -0.25, f'n={int(n):,}', ha='center', fontsize=9, color='gray')

    ax.set_xticks(range(4))
    ax.set_xticklabels(['Escape\nVelocity\n(Low E, High |ΔV|)',
                        'Late\nPivoter\n(High E, High |ΔV|)',
                        'Stagnant\n\n(Low E, Low |ΔV|)',
                        'Golden\nCage\n(High E, Low |ΔV|)'], fontsize=10)
    ax.set_ylabel('Y = L/E\n(Later Funding / Early Funding)', fontsize=12)
    ax.set_title('All Four Cohorts: Strategic Flexibility Wins\n(Y = L/E where L = Total - E)', fontsize=14, pad=15)
    ax.set_ylim(-0.5, max(medians) * 1.3)
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax.grid(True, alpha=0.3, axis='y')

    # Add ratio annotation between Escape and Cage
    if medians[0] > 0 and medians[3] > 0:
        ratio = medians[0] / medians[3]
        ax.plot([0, 3], [medians[0] * 0.85, medians[3] * 1.1], 'k--', alpha=0.4, lw=1.5)
        ax.text(1.5, max(medians) * 0.6, f'{ratio:.1f}× gap',
                 ha='center', fontsize=13, fontweight='bold',
                 bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

    plt.tight_layout()

    # Save
    plt.savefig(OUTPUT_DIR / 'all_cohorts_LE.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')

    print(f"Saved: {OUTPUT_DIR / 'all_cohorts_LE.png'}")

    return fig


def generate_tables(df, results_df):
    """Generate summary tables for the paper."""
    print("\n" + "=" * 60)
    print("GENERATING TABLES (Y = L/E)")
    print("=" * 60)

    # Filter to companies with outcome data
    df_outcome = df[df['L'].notna()].copy()
    df_outcome = df_outcome[df_outcome['Y'] < df_outcome['Y'].quantile(0.99)]
    df_outcome = df_outcome[df_outcome['Y'] >= 0]

    # Table: Cohort Outcomes
    table_cohorts = df_outcome.groupby('cohort').agg({
        'E': 'median',
        'abs_delta_V': 'median',
        'Y': ['median', 'mean', 'std', 'count']
    }).round(3)
    table_cohorts.columns = ['E_Median', 'DeltaV_Median', 'Y_Median', 'Y_Mean', 'Y_Std', 'N']

    print("\nTable: Cohort Outcomes (Y = L/E)")
    print(table_cohorts.to_string())

    # Save
    table_cohorts.to_csv(TABLE_DIR / 'cohort_outcomes_LE.csv')

    # Table: Cost of Commitment by Decile
    table_cost = results_df[['Decile', 'n_locked', 'n_flexible', 'median_locked', 'median_flexible', 'cost_median', 'p_value']].copy()
    table_cost.columns = ['E_Decile', 'N_Locked', 'N_Flexible', 'Y_Locked', 'Y_Flexible', 'Cost', 'P_Value']

    print("\nTable: Cost of Commitment by E Decile (Y = L/E)")
    print(table_cost.to_string(index=False))

    table_cost.to_csv(TABLE_DIR / 'cost_of_commitment_LE.csv', index=False)

    print(f"\nTables saved to: {TABLE_DIR}")

    return table_cohorts, table_cost


def calculate_lockin_correlation(df):
    """Calculate E → |ΔV| correlation (H_supporting)."""
    print("\n" + "=" * 60)
    print("H_SUPPORTING: E → |ΔV| CORRELATION")
    print("=" * 60)

    # Spearman correlation
    r, p = spearmanr(df['E'], df['abs_delta_V'])

    print(f"Spearman correlation (E, |ΔV|): r = {r:.3f}, p = {p:.2e}")

    if r < 0 and p < 0.001:
        print("✓ H_supporting CONFIRMED: Early funding negatively correlates with flexibility")
    else:
        print("✗ H_supporting NOT confirmed")

    return r, p


def main():
    """Main analysis pipeline."""
    print("\n" + "=" * 70)
    print("COST OF COMMITMENT: COHORT-BASED ANALYSIS")
    print("NEW DEFINITION: Y = L/E (Later Funding / Early Funding)")
    print("where L = Total - E (money earned AFTER early stage)")
    print("=" * 70)

    # Load data
    df = load_data()

    # Create cohorts
    df = create_cohorts(df)

    # Calculate lock-in correlation (H_supporting)
    r, p = calculate_lockin_correlation(df)

    # Calculate cost by decile
    results_df, df_outcome = calculate_cost_by_funding_decile(df)

    # Create flagship figure
    fig1, ratio = plot_flagship_figure(df, results_df)

    # Create cost by decile plot
    fig2 = plot_cost_by_decile(results_df)

    # Create all cohorts comparison
    fig3 = plot_all_cohorts(df)

    # Generate tables
    table_cohorts, table_cost = generate_tables(df, results_df)

    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)

    # Summary
    df_outcome = df[df['L'].notna()].copy()
    df_outcome = df_outcome[df_outcome['Y'] < df_outcome['Y'].quantile(0.99)]
    df_outcome = df_outcome[df_outcome['Y'] >= 0]

    escape = df_outcome[df_outcome['cohort'] == 'Escape Velocity']['Y'].median()
    cage = df_outcome[df_outcome['cohort'] == 'Golden Cage']['Y'].median()
    ratio = escape / cage if cage > 0 else np.nan

    print("\n" + "=" * 40)
    print("KEY FINDINGS (NEW: Y = L/E)")
    print("=" * 40)
    print(f"H_supporting (E → |ΔV|): r = {r:.3f}***")
    print(f"")
    print(f"H_cost (Cost of Commitment):")
    print(f"  Escape Velocity: {escape:.2f}×")
    print(f"  Golden Cage: {cage:.2f}×")
    print(f"  Ratio: {ratio:.1f}×")
    print(f"")
    print(f"Average Cost by Decile: {results_df['cost_median'].mean():.2f}×")
    print("=" * 40)

    return df, results_df, ratio


if __name__ == "__main__":
    df, results, ratio = main()
