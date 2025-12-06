#!/usr/bin/env python3
"""
Multi-Variable Lock-in Analysis with Full ΔV Trajectory
=========================================================

Tests multiple lock-in mechanisms beyond funding:
1. Employee Lock-in: More employees → less strategic flexibility
2. Valuation Lock-in: Higher valuation → more locked in
3. Investor Lock-in: More investors → board pressure reduces flexibility
4. Growth Lock-in: Early success traps companies in current strategy

Also uses FULL ΔV trajectory (3 windows) instead of just scalar:
- Window 1: 2021→2023 (ΔV_1)
- Window 2: 2023→2024 (ΔV_2)
- Window 3: 2024→2025 (ΔV_3)

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


def load_data_with_additional_vars():
    """Load vagueness timeseries and merge with additional variables."""
    print("=" * 60)
    print("LOADING DATA WITH ADDITIONAL VARIABLES")
    print("=" * 60)

    # Load parquet with all vagueness data
    df_full = pd.read_parquet(PROCESSED_DIR / "vagueness_timeseries.parquet")
    print(f"Loaded {len(df_full):,} rows from vagueness timeseries")

    # Create wide format for V at each year
    df_2021 = df_full[df_full['year'] == 2021][['company_id', 'V', 'first_financing_size', 'company_name']].copy()
    df_2021.columns = ['company_id', 'V_2021', 'early_funding', 'company_name']

    df_2023 = df_full[df_full['year'] == 2023][['company_id', 'V']].copy()
    df_2023.columns = ['company_id', 'V_2023']

    df_2024 = df_full[df_full['year'] == 2024][['company_id', 'V']].copy()
    df_2024.columns = ['company_id', 'V_2024']

    df_2025 = df_full[df_full['year'] == 2025][['company_id', 'V']].copy()
    df_2025.columns = ['company_id', 'V_2025']

    # Merge all years
    df = df_2021.merge(df_2023, on='company_id', how='inner')
    df = df.merge(df_2024, on='company_id', how='inner')
    df = df.merge(df_2025, on='company_id', how='inner')

    # Calculate THREE ΔV windows (not just total!)
    df['delta_V_1'] = df['V_2023'] - df['V_2021']  # Window 1: 2021→2023
    df['delta_V_2'] = df['V_2024'] - df['V_2023']  # Window 2: 2023→2024
    df['delta_V_3'] = df['V_2025'] - df['V_2024']  # Window 3: 2024→2025
    df['total_delta_V'] = df['V_2025'] - df['V_2021']  # Total: 2021→2025

    # Absolute values for flexibility measurement
    df['abs_delta_V_1'] = df['delta_V_1'].abs()
    df['abs_delta_V_2'] = df['delta_V_2'].abs()
    df['abs_delta_V_3'] = df['delta_V_3'].abs()
    df['abs_total_delta_V'] = df['total_delta_V'].abs()

    # Average flexibility across windows
    df['avg_abs_delta_V'] = (df['abs_delta_V_1'] + df['abs_delta_V_2'] + df['abs_delta_V_3']) / 3

    print(f"Companies with all 4 years: {len(df):,}")

    # Load 2021 raw data for additional variables (parquet format)
    try:
        df_2021_raw = pd.read_parquet(RAW_DIR / "Company20211201.parquet",
                                       columns=['CompanyID', 'Employees', 'LastKnownValuation',
                                               'ActiveInvestors', 'FormerInvestors', 'GrowthRate',
                                               'YearFounded'])
        df_2021_raw.columns = ['company_id', 'employees_2021', 'valuation_2021',
                               'active_investors', 'former_investors', 'growth_rate_2021',
                               'year_founded']
        df_2021_raw['company_id'] = df_2021_raw['company_id'].astype(str)
        df['company_id'] = df['company_id'].astype(str)

        # Convert to numeric
        for col in ['employees_2021', 'valuation_2021', 'active_investors',
                    'former_investors', 'growth_rate_2021', 'year_founded']:
            df_2021_raw[col] = pd.to_numeric(df_2021_raw[col], errors='coerce')

        df = df.merge(df_2021_raw, on='company_id', how='left')
        print(f"Merged with 2021 variables: {df['employees_2021'].notna().sum():,} with employees")

    except Exception as e:
        print(f"Warning: Could not load 2021 raw data: {e}")
        # Create empty columns to avoid KeyError later
        for col in ['employees_2021', 'valuation_2021', 'active_investors',
                    'former_investors', 'growth_rate_2021', 'year_founded']:
            df[col] = np.nan

    # Load 2025 raw data for outcome variables
    try:
        df_2025_raw = pd.read_csv(RAW_DIR / "Company20251101.dat", sep='|',
                                   usecols=['CompanyID', 'TotalRaised', 'LastKnownValuation',
                                           'Employees', 'GrowthRate', 'BusinessStatus'],
                                   low_memory=False, on_bad_lines='skip')
        df_2025_raw.columns = ['company_id', 'total_raised_2025', 'valuation_2025',
                               'employees_2025', 'growth_rate_2025', 'business_status']
        df_2025_raw['company_id'] = df_2025_raw['company_id'].astype(str)

        for col in ['total_raised_2025', 'valuation_2025', 'employees_2025', 'growth_rate_2025']:
            df_2025_raw[col] = pd.to_numeric(df_2025_raw[col], errors='coerce')

        df = df.merge(df_2025_raw, on='company_id', how='left')
        print(f"Merged with 2025 outcomes: {df['total_raised_2025'].notna().sum():,} with total raised")

    except Exception as e:
        print(f"Warning: Could not load 2025 raw data: {e}")

    # Calculate derived variables
    df['funding_growth'] = df['total_raised_2025'] / (df['early_funding'] + 0.001)
    df['employee_growth'] = df['employees_2025'] / (df['employees_2021'] + 1)
    df['valuation_growth'] = df['valuation_2025'] / (df['valuation_2021'] + 0.001)
    df['total_investors'] = df['active_investors'].fillna(0) + df['former_investors'].fillna(0)

    # Company age in 2021
    df['company_age_2021'] = 2021 - df['year_founded']
    df.loc[df['company_age_2021'] < 0, 'company_age_2021'] = np.nan
    df.loc[df['company_age_2021'] > 100, 'company_age_2021'] = np.nan

    return df


def plot_delta_v_trajectory(df):
    """
    Plot ΔV across the three time windows to show trajectory patterns.
    """
    print("\n" + "=" * 60)
    print("PLOT: ΔV TRAJECTORY ANALYSIS")
    print("=" * 60)

    fig, axes = plt.subplots(2, 2, figsize=(14, 12))

    # Panel 1: Distribution of |ΔV| by window
    ax1 = axes[0, 0]

    windows = ['2021→2023', '2023→2024', '2024→2025']
    data = [df['abs_delta_V_1'].dropna(), df['abs_delta_V_2'].dropna(), df['abs_delta_V_3'].dropna()]

    bp = ax1.boxplot(data, labels=windows, patch_artist=True)
    colors = ['#3498db', '#2ecc71', '#e74c3c']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    means = [d.mean() for d in data]
    ax1.plot(range(1, 4), means, 'ko-', markersize=10, label='Mean')

    ax1.set_ylabel('|ΔV| (Strategic Flexibility)', fontsize=11)
    ax1.set_xlabel('Time Window', fontsize=11)
    ax1.set_title('Panel 1: Strategic Flexibility Over Time\n(Do companies become more locked in?)', fontsize=12)
    ax1.legend()
    ax1.grid(True, alpha=0.3, axis='y')

    print("\n|ΔV| by Time Window:")
    for i, w in enumerate(windows):
        print(f"  {w}: mean={means[i]:.2f}, median={data[i].median():.2f}")

    # Panel 2: Trajectory patterns by early funding
    ax2 = axes[0, 1]

    # Split by early funding
    df_plot = df.dropna(subset=['early_funding', 'abs_delta_V_1', 'abs_delta_V_2', 'abs_delta_V_3'])
    funding_median = df_plot['early_funding'].median()

    low_fund = df_plot[df_plot['early_funding'] <= funding_median]
    high_fund = df_plot[df_plot['early_funding'] > funding_median]

    x = [1, 2, 3]
    low_means = [low_fund['abs_delta_V_1'].mean(), low_fund['abs_delta_V_2'].mean(), low_fund['abs_delta_V_3'].mean()]
    high_means = [high_fund['abs_delta_V_1'].mean(), high_fund['abs_delta_V_2'].mean(), high_fund['abs_delta_V_3'].mean()]

    ax2.plot(x, low_means, 'o-', color='#2ecc71', linewidth=2, markersize=10, label=f'Low Early Funding (n={len(low_fund):,})')
    ax2.plot(x, high_means, 'o-', color='#e74c3c', linewidth=2, markersize=10, label=f'High Early Funding (n={len(high_fund):,})')

    ax2.set_xticks([1, 2, 3])
    ax2.set_xticklabels(['2021→2023', '2023→2024', '2024→2025'])
    ax2.set_ylabel('Mean |ΔV|', fontsize=11)
    ax2.set_xlabel('Time Window', fontsize=11)
    ax2.set_title('Panel 2: Flexibility Trajectory by Funding Level\n(Does funding lock-in persist over time?)', fontsize=12)
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # Panel 3: Cumulative flexibility (sum of |ΔV| across windows)
    ax3 = axes[1, 0]

    df_plot['cumulative_flexibility'] = df_plot['abs_delta_V_1'] + df_plot['abs_delta_V_2'] + df_plot['abs_delta_V_3']

    x = np.log10(df_plot['early_funding'] + 0.001)
    y = df_plot['cumulative_flexibility']

    ax3.scatter(x, y, alpha=0.2, s=5, c='steelblue')

    # Trend line
    mask = ~(np.isnan(x) | np.isnan(y))
    z = np.polyfit(x[mask], y[mask], 1)
    p = np.poly1d(z)
    x_range = np.linspace(x[mask].min(), x[mask].max(), 100)
    ax3.plot(x_range, p(x_range), 'r-', linewidth=2, label=f'Trend')

    r, pval = spearmanr(df_plot['early_funding'], df_plot['cumulative_flexibility'])
    ax3.text(0.05, 0.95, f'Spearman r = {r:.3f}***' if pval < 0.001 else f'r = {r:.3f}',
             transform=ax3.transAxes, fontsize=11, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    ax3.set_xlabel('Early Funding (log₁₀ $M)', fontsize=11)
    ax3.set_ylabel('Cumulative |ΔV| (sum of 3 windows)', fontsize=11)
    ax3.set_title('Panel 3: Total Flexibility vs Early Funding\n(Cumulative strategic change across all windows)', fontsize=12)
    ax3.grid(True, alpha=0.3)

    # Panel 4: Early vs Late pivots
    ax4 = axes[1, 1]

    # Classify by when they pivoted most
    df_plot['pivot_timing'] = 'Mixed'
    df_plot.loc[df_plot['abs_delta_V_1'] > df_plot[['abs_delta_V_2', 'abs_delta_V_3']].max(axis=1), 'pivot_timing'] = 'Early (2021-23)'
    df_plot.loc[df_plot['abs_delta_V_3'] > df_plot[['abs_delta_V_1', 'abs_delta_V_2']].max(axis=1), 'pivot_timing'] = 'Late (2024-25)'

    # Outcome by pivot timing
    pivot_outcomes = df_plot.groupby('pivot_timing').agg({
        'funding_growth': 'mean',
        'company_id': 'count'
    }).rename(columns={'company_id': 'n'})

    pivot_outcomes = pivot_outcomes.reindex(['Early (2021-23)', 'Mixed', 'Late (2024-25)'])

    colors = ['#2ecc71', '#f1c40f', '#e74c3c']
    bars = ax4.bar(range(len(pivot_outcomes)), pivot_outcomes['funding_growth'], color=colors, alpha=0.7)

    ax4.set_xticks(range(len(pivot_outcomes)))
    ax4.set_xticklabels(pivot_outcomes.index, fontsize=10)
    ax4.set_ylabel('Mean Funding Growth (Total 2025 / Early)', fontsize=11)
    ax4.set_title('Panel 4: Outcome by Pivot Timing\n(When did the biggest strategic change occur?)', fontsize=12)
    ax4.grid(True, alpha=0.3, axis='y')

    # Add n labels
    for i, (idx, row) in enumerate(pivot_outcomes.iterrows()):
        ax4.text(i, row['funding_growth'] + 1, f'n={int(row["n"]):,}', ha='center', fontsize=9)

    print("\nPivot Timing → Funding Growth:")
    print(pivot_outcomes.round(2))

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'delta_v_trajectory_analysis.png', dpi=150, bbox_inches='tight')
    plt.savefig(OUTPUT_DIR / 'delta_v_trajectory_analysis.pdf', bbox_inches='tight')
    print(f"\nSaved: {OUTPUT_DIR / 'delta_v_trajectory_analysis.png'}")

    return fig


def plot_multivariable_lockin(df):
    """
    Plot lock-in effects from multiple variables: Employees, Valuation, Investors.
    """
    print("\n" + "=" * 60)
    print("PLOT: MULTI-VARIABLE LOCK-IN ANALYSIS")
    print("=" * 60)

    fig, axes = plt.subplots(2, 3, figsize=(16, 10))

    lock_in_vars = [
        ('early_funding', 'Early Funding ($M)', 'Funding Lock-in'),
        ('employees_2021', 'Employees (2021)', 'Employee Lock-in'),
        ('valuation_2021', 'Valuation (2021, $M)', 'Valuation Lock-in'),
        ('total_investors', 'Total Investors', 'Investor Lock-in'),
        ('growth_rate_2021', 'Growth Rate (2021)', 'Success Trap'),
        ('company_age_2021', 'Company Age (years)', 'Age Lock-in')
    ]

    results = []

    for i, (var, label, title) in enumerate(lock_in_vars):
        ax = axes[i // 3, i % 3]

        # Filter valid data
        df_plot = df.dropna(subset=[var, 'abs_total_delta_V'])
        df_plot = df_plot[df_plot[var] > 0]  # Remove zeros for log

        if len(df_plot) < 100:
            ax.text(0.5, 0.5, f'Insufficient data\nn={len(df_plot)}',
                   ha='center', va='center', fontsize=12)
            ax.set_title(title)
            continue

        # Log transform if needed
        if var in ['early_funding', 'valuation_2021', 'employees_2021']:
            x = np.log10(df_plot[var] + 0.001)
            xlabel = f'{label} (log₁₀)'
        else:
            x = df_plot[var]
            xlabel = label

        y = df_plot['abs_total_delta_V']

        # Scatter
        ax.scatter(x, y, alpha=0.1, s=3, c='steelblue')

        # Trend line
        mask = ~(np.isnan(x) | np.isnan(y) | np.isinf(x) | np.isinf(y))
        if mask.sum() > 100:
            z = np.polyfit(x[mask], y[mask], 1)
            p = np.poly1d(z)
            x_range = np.linspace(np.percentile(x[mask], 5), np.percentile(x[mask], 95), 100)
            ax.plot(x_range, p(x_range), 'r-', linewidth=2)

            # Correlation
            r, pval = spearmanr(df_plot[var], df_plot['abs_total_delta_V'])
            results.append({'Variable': title, 'r': r, 'p': pval, 'n': len(df_plot)})

            sig = '***' if pval < 0.001 else '**' if pval < 0.01 else '*' if pval < 0.05 else ''
            sign = '✓' if r < 0 else '✗'
            ax.text(0.05, 0.95, f'{sign} r = {r:.3f}{sig}\nn = {len(df_plot):,}',
                   transform=ax.transAxes, fontsize=10, verticalalignment='top',
                   bbox=dict(boxstyle='round', facecolor='lightgreen' if r < 0 else 'lightyellow', alpha=0.7))

        ax.set_xlabel(xlabel, fontsize=10)
        ax.set_ylabel('|ΔV| (Strategic Flexibility)', fontsize=10)
        ax.set_title(title, fontsize=11)
        ax.grid(True, alpha=0.3)

    plt.suptitle('Multi-Variable Lock-in Analysis\n(Negative correlation = Lock-in confirmed ✓)', fontsize=14, y=1.02)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'multivariable_lockin_analysis.png', dpi=150, bbox_inches='tight')
    plt.savefig(OUTPUT_DIR / 'multivariable_lockin_analysis.pdf', bbox_inches='tight')
    print(f"\nSaved: {OUTPUT_DIR / 'multivariable_lockin_analysis.png'}")

    # Print results table
    print("\n" + "=" * 60)
    print("LOCK-IN CORRELATION SUMMARY")
    print("=" * 60)
    results_df = pd.DataFrame(results)
    results_df['Interpretation'] = results_df['r'].apply(lambda x: 'Lock-in CONFIRMED' if x < 0 else 'No lock-in')
    print(results_df.to_string(index=False))

    return fig, results_df


def plot_lock_in_interaction(df):
    """
    Plot interaction between funding and other lock-in variables.
    Shows whether employee/valuation lock-in is stronger at high funding.
    """
    print("\n" + "=" * 60)
    print("PLOT: LOCK-IN INTERACTION EFFECTS")
    print("=" * 60)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Prepare data
    df_plot = df.dropna(subset=['early_funding', 'employees_2021', 'abs_total_delta_V'])
    df_plot = df_plot[(df_plot['early_funding'] > 0) & (df_plot['employees_2021'] > 0)]

    if len(df_plot) < 500:
        print("Insufficient data for interaction analysis")
        return None

    # Create quartiles
    df_plot['funding_q'] = pd.qcut(df_plot['early_funding'].rank(method='first'),
                                    2, labels=['Low Funding', 'High Funding'])
    df_plot['employee_q'] = pd.qcut(df_plot['employees_2021'].rank(method='first'),
                                     2, labels=['Small Team', 'Large Team'])

    # Panel 1: Funding × Employee interaction on |ΔV|
    ax1 = axes[0]

    interaction = df_plot.groupby(['funding_q', 'employee_q'])['abs_total_delta_V'].mean().unstack()

    x = [0, 1]
    ax1.plot(x, interaction.loc['Low Funding'], 'o-', color='#2ecc71', linewidth=2, markersize=10, label='Low Funding')
    ax1.plot(x, interaction.loc['High Funding'], 'o-', color='#e74c3c', linewidth=2, markersize=10, label='High Funding')

    ax1.set_xticks([0, 1])
    ax1.set_xticklabels(['Small Team', 'Large Team'])
    ax1.set_ylabel('Mean |ΔV| (Strategic Flexibility)', fontsize=11)
    ax1.set_xlabel('Team Size', fontsize=11)
    ax1.set_title('Funding × Employee Interaction\n(Does funding amplify employee lock-in?)', fontsize=12)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Check if lines cross or diverge
    low_diff = interaction.loc['Low Funding', 'Large Team'] - interaction.loc['Low Funding', 'Small Team']
    high_diff = interaction.loc['High Funding', 'Large Team'] - interaction.loc['High Funding', 'Small Team']

    interaction_effect = high_diff - low_diff
    ax1.text(0.5, 0.05, f'Interaction effect: {interaction_effect:.2f}\n(Negative = Funding amplifies lock-in)',
             transform=ax1.transAxes, fontsize=10, ha='center',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    print("\nFunding × Employee Interaction:")
    print(interaction.round(2))
    print(f"Interaction effect: {interaction_effect:.2f}")

    # Panel 2: 2x2 heatmap of outcomes
    ax2 = axes[1]

    # Add funding growth outcome
    df_outcome = df_plot.dropna(subset=['funding_growth'])

    if len(df_outcome) > 100:
        outcome_table = df_outcome.groupby(['funding_q', 'employee_q']).agg({
            'funding_growth': 'mean',
            'abs_total_delta_V': 'mean'
        })

        # Reshape for heatmap
        heatmap_data = outcome_table['funding_growth'].unstack()

        sns.heatmap(heatmap_data, annot=True, fmt='.1f', cmap='RdYlGn', ax=ax2,
                   cbar_kws={'label': 'Mean Funding Growth'})
        ax2.set_title('Funding Growth by Funding × Team Size\n(Which combination wins?)', fontsize=12)
        ax2.set_xlabel('Team Size', fontsize=11)
        ax2.set_ylabel('Early Funding Level', fontsize=11)

        print("\nFunding Growth by Funding × Team Size:")
        print(heatmap_data.round(1))
    else:
        ax2.text(0.5, 0.5, 'Insufficient outcome data', ha='center', va='center')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'lockin_interaction_analysis.png', dpi=150, bbox_inches='tight')
    plt.savefig(OUTPUT_DIR / 'lockin_interaction_analysis.pdf', bbox_inches='tight')
    print(f"\nSaved: {OUTPUT_DIR / 'lockin_interaction_analysis.png'}")

    return fig


def main():
    """Main analysis pipeline."""
    print("\n" + "=" * 70)
    print("MULTI-VARIABLE LOCK-IN ANALYSIS")
    print("Testing: Employees, Valuation, Investors, Growth, Age")
    print("Using: Full ΔV Trajectory (3 windows)")
    print("=" * 70)

    # Load data
    df = load_data_with_additional_vars()

    # Summary statistics
    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)
    print(f"Total companies: {len(df):,}")
    print(f"With employees: {df['employees_2021'].notna().sum():,}")
    print(f"With valuation: {df['valuation_2021'].notna().sum():,}")
    print(f"With investors: {df['total_investors'].notna().sum():,}")
    print(f"With growth rate: {df['growth_rate_2021'].notna().sum():,}")

    print("\nΔV Statistics by Window:")
    for col in ['abs_delta_V_1', 'abs_delta_V_2', 'abs_delta_V_3', 'abs_total_delta_V']:
        print(f"  {col}: mean={df[col].mean():.2f}, std={df[col].std():.2f}")

    # Generate plots
    fig1 = plot_delta_v_trajectory(df)
    fig2, results = plot_multivariable_lockin(df)
    fig3 = plot_lock_in_interaction(df)

    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
    print(f"\nOutput files saved to: {OUTPUT_DIR}")
    print("  - delta_v_trajectory_analysis.png")
    print("  - multivariable_lockin_analysis.png")
    print("  - lockin_interaction_analysis.png")

    return df, results


if __name__ == "__main__":
    df, results = main()
