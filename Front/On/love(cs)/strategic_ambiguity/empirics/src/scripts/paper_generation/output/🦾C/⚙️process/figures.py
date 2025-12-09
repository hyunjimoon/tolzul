#!/usr/bin/env python3
"""
🦾C: When Commitment Becomes a Cage
Replication Code for Paper Figures

Core Thesis: dY/dE = dY/d|ΔV| × d|ΔV|/dE = (+) × (-) < 0

Notation:
- E = Early funding (first_financing_size)
- L = Later funding = Total_2025 - E
- V_E = Vagueness at early stage (V_2021)
- V_L = Vagueness at later stage (V_2025)
- |ΔV| = |V_L - V_E| (strategic flexibility)
- Y = L/E (later funding growth ratio)

Figures:
- Fig 1: Three-panel mechanism plot (d|ΔV|/dE, dY/d|ΔV|, dY/dE)
- Fig 2: Cost of Commitment by Early Funding Decile
- Fig 3: 2×2 Cohort Analysis (Escape Velocity vs Golden Cage)

Author: Claude Code
Date: 2025-12-04
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
from pathlib import Path
from typing import Optional, Tuple, Dict
from scipy import stats

# Reproducibility
SEED = 42
np.random.seed(SEED)

# Figure settings
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['font.family'] = 'DejaVu Sans'

# Paths
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent.parent.parent.parent.parent / "data" / "processed"
OUTPUT_DIR = SCRIPT_DIR / "figures"
OUTPUT_DIR.mkdir(exist_ok=True)


def load_panel_data() -> pd.DataFrame:
    """
    Load the panel data for analysis.

    Returns:
        DataFrame with columns: company_id, E, L, V_E, V_L, |ΔV|, Y
    """
    # Try to load from parquet first, fall back to CSV
    parquet_path = DATA_DIR / "vagueness_timeseries.parquet"
    csv_path = DATA_DIR / "vagueness_timeseries.csv"

    if parquet_path.exists():
        df = pd.read_parquet(parquet_path)
    elif csv_path.exists():
        df = pd.read_csv(csv_path)
    else:
        raise FileNotFoundError(
            f"No data file found. Expected:\n"
            f"  - {parquet_path}\n"
            f"  - {csv_path}"
        )

    # Rename columns to our notation
    column_map = {
        'first_financing_size': 'E',
        'total_raised_2025': 'Total_2025',
        'vagueness_2021': 'V_E',
        'vagueness_2025': 'V_L',
    }

    for old_col, new_col in column_map.items():
        if old_col in df.columns:
            df[new_col] = df[old_col]

    # Compute derived variables
    if 'L' not in df.columns and 'Total_2025' in df.columns and 'E' in df.columns:
        df['L'] = df['Total_2025'] - df['E']

    if '|ΔV|' not in df.columns and 'V_E' in df.columns and 'V_L' in df.columns:
        df['|ΔV|'] = np.abs(df['V_L'] - df['V_E'])

    if 'Y' not in df.columns and 'L' in df.columns and 'E' in df.columns:
        # Avoid division by zero
        df['Y'] = np.where(df['E'] > 0, df['L'] / df['E'], np.nan)

    # Filter valid observations
    valid_mask = (
        (df['E'] > 0) &
        (df['L'] >= 0) &
        df['|ΔV|'].notna() &
        df['Y'].notna() &
        np.isfinite(df['Y'])
    )

    return df[valid_mask].copy()


def compute_decile_statistics(df: pd.DataFrame,
                               x_var: str,
                               y_var: str) -> pd.DataFrame:
    """
    Compute statistics by decile of x_var.

    Args:
        df: DataFrame with data
        x_var: Variable for decile grouping
        y_var: Outcome variable

    Returns:
        DataFrame with decile statistics
    """
    df = df.copy()
    df['decile'] = pd.qcut(df[x_var], 10, labels=False, duplicates='drop')

    stats_list = []
    for d in sorted(df['decile'].dropna().unique()):
        subset = df[df['decile'] == d]
        stats_list.append({
            'decile': d + 1,  # 1-indexed
            f'{x_var}_median': subset[x_var].median(),
            f'{y_var}_mean': subset[y_var].mean(),
            f'{y_var}_median': subset[y_var].median(),
            f'{y_var}_std': subset[y_var].std(),
            'n': len(subset)
        })

    return pd.DataFrame(stats_list)


def create_figure1_mechanism(df: pd.DataFrame,
                             save_path: Optional[Path] = None) -> plt.Figure:
    """
    Figure 1: Three-panel mechanism plot.

    Panel A: d|ΔV|/dE < 0 (Early funding reduces flexibility)
    Panel B: dY/d|ΔV| > 0 (Flexibility increases outcomes)
    Panel C: dY/dE < 0 (Combined effect: early funding hurts outcomes)
    """
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Color scheme
    colors = {
        'negative': '#e74c3c',  # Red for negative relationships
        'positive': '#27ae60',  # Green for positive relationships
        'neutral': '#3498db',   # Blue for data points
    }

    # --- Panel A: d|ΔV|/dE < 0 ---
    ax1 = axes[0]

    # Compute decile statistics
    stats_E_deltaV = compute_decile_statistics(df, 'E', '|ΔV|')

    # Plot with regression line
    x = np.log10(stats_E_deltaV['E_median'].values)
    y = stats_E_deltaV['|ΔV|_median'].values

    ax1.scatter(stats_E_deltaV['E_median'], y,
                s=stats_E_deltaV['n']/50, alpha=0.7, c=colors['neutral'],
                edgecolors='black', linewidth=0.5)

    # Fit line
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    x_fit = np.linspace(x.min(), x.max(), 100)
    y_fit = slope * x_fit + intercept

    ax1.plot(10**x_fit, y_fit, '--', color=colors['negative'], linewidth=2,
             label=f'ρ = {r_value:.3f}***')

    ax1.set_xscale('log')
    ax1.set_xlabel('Early Funding E (log scale)', fontsize=12)
    ax1.set_ylabel('Strategic Flexibility |ΔV|', fontsize=12)
    ax1.set_title('(A) d|ΔV|/dE < 0\n"Funding Reduces Flexibility"',
                  fontsize=13, fontweight='bold', color=colors['negative'])
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3)

    # Arrow annotation
    ax1.annotate('', xy=(stats_E_deltaV['E_median'].iloc[-1], y[-1]),
                xytext=(stats_E_deltaV['E_median'].iloc[0], y[0]),
                arrowprops=dict(arrowstyle='->', color=colors['negative'], lw=2))

    # --- Panel B: dY/d|ΔV| > 0 ---
    ax2 = axes[1]

    stats_deltaV_Y = compute_decile_statistics(df, '|ΔV|', 'Y')

    x = stats_deltaV_Y['|ΔV|_median'].values
    y = stats_deltaV_Y['Y_median'].values

    ax2.scatter(x, y, s=stats_deltaV_Y['n']/50, alpha=0.7, c=colors['neutral'],
                edgecolors='black', linewidth=0.5)

    # Fit line
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    x_fit = np.linspace(x.min(), x.max(), 100)
    y_fit = slope * x_fit + intercept

    ax2.plot(x_fit, y_fit, '--', color=colors['positive'], linewidth=2,
             label=f'ρ = {r_value:.3f}***')

    ax2.set_xlabel('Strategic Flexibility |ΔV|', fontsize=12)
    ax2.set_ylabel('Outcome Y = L/E', fontsize=12)
    ax2.set_title('(B) dY/d|ΔV| > 0\n"Flexibility Increases Outcomes"',
                  fontsize=13, fontweight='bold', color=colors['positive'])
    ax2.legend(loc='upper left')
    ax2.grid(True, alpha=0.3)

    # Arrow annotation
    ax2.annotate('', xy=(x[-1], y[-1]), xytext=(x[0], y[0]),
                arrowprops=dict(arrowstyle='->', color=colors['positive'], lw=2))

    # --- Panel C: dY/dE < 0 ---
    ax3 = axes[2]

    stats_E_Y = compute_decile_statistics(df, 'E', 'Y')

    x = np.log10(stats_E_Y['E_median'].values)
    y = stats_E_Y['Y_median'].values

    ax3.scatter(stats_E_Y['E_median'], y,
                s=stats_E_Y['n']/50, alpha=0.7, c=colors['neutral'],
                edgecolors='black', linewidth=0.5)

    # Fit line
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    x_fit = np.linspace(x.min(), x.max(), 100)
    y_fit = slope * x_fit + intercept

    ax3.plot(10**x_fit, y_fit, '--', color=colors['negative'], linewidth=2,
             label=f'ρ = {r_value:.3f}***')

    ax3.set_xscale('log')
    ax3.set_xlabel('Early Funding E (log scale)', fontsize=12)
    ax3.set_ylabel('Outcome Y = L/E', fontsize=12)
    ax3.set_title('(C) dY/dE < 0\n"dY/dE = dY/d|ΔV| × d|ΔV|/dE = (+)(−) < 0"',
                  fontsize=13, fontweight='bold', color=colors['negative'])
    ax3.legend(loc='upper right')
    ax3.grid(True, alpha=0.3)

    # Add mechanism equation in center
    fig.text(0.5, 0.02,
             r'Core Mechanism: $\frac{dY}{dE} = \frac{dY}{d|\Delta V|} \times \frac{d|\Delta V|}{dE} = (+) \times (-) < 0$',
             ha='center', fontsize=14, fontweight='bold',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout(rect=[0, 0.08, 1, 1])

    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"   Saved: {save_path}")

    return fig


def create_figure2_cost(df: pd.DataFrame,
                        save_path: Optional[Path] = None) -> plt.Figure:
    """
    Figure 2: Cost of Commitment by Early Funding Decile.

    Shows: Cost = E[Y | Locked, E] - E[Y | Flexible, E] for each E decile.
    """
    fig, ax = plt.subplots(figsize=(12, 7))

    # Compute median |ΔV| for splitting
    median_deltaV = df['|ΔV|'].median()

    # Assign cohorts
    df = df.copy()
    df['flexibility'] = np.where(df['|ΔV|'] > median_deltaV, 'Flexible', 'Locked')
    df['E_decile'] = pd.qcut(df['E'], 10, labels=False, duplicates='drop') + 1

    # Compute outcomes by E decile and flexibility
    results = []
    for decile in sorted(df['E_decile'].unique()):
        decile_data = df[df['E_decile'] == decile]
        E_median = decile_data['E'].median()

        locked = decile_data[decile_data['flexibility'] == 'Locked']['Y']
        flexible = decile_data[decile_data['flexibility'] == 'Flexible']['Y']

        if len(locked) > 0 and len(flexible) > 0:
            cost = locked.median() - flexible.median()
            results.append({
                'decile': decile,
                'E_median': E_median,
                'Y_locked': locked.median(),
                'Y_flexible': flexible.median(),
                'cost': cost,
                'n_locked': len(locked),
                'n_flexible': len(flexible)
            })

    results_df = pd.DataFrame(results)

    # Plot bars
    x = np.arange(len(results_df))
    width = 0.35

    bars_locked = ax.bar(x - width/2, results_df['Y_locked'], width,
                         label='Locked (|ΔV| ≤ median)', color='#e74c3c',
                         edgecolor='black', alpha=0.8)
    bars_flexible = ax.bar(x + width/2, results_df['Y_flexible'], width,
                           label='Flexible (|ΔV| > median)', color='#27ae60',
                           edgecolor='black', alpha=0.8)

    # Add cost annotations
    for i, (_, row) in enumerate(results_df.iterrows()):
        cost = row['cost']
        y_pos = max(row['Y_locked'], row['Y_flexible']) + 0.1
        ax.annotate(f'{cost:.2f}×',
                   xy=(i, y_pos), ha='center', fontsize=9,
                   color='#e74c3c' if cost < 0 else '#27ae60',
                   fontweight='bold')

    # Calculate and display average cost
    avg_cost = results_df['cost'].mean()
    ax.axhline(y=0, color='gray', linestyle='-', alpha=0.3)

    ax.set_xlabel('Early Funding Decile (E)', fontsize=12)
    ax.set_ylabel('Median Outcome Y = L/E', fontsize=12)
    ax.set_title(f'Cost of Commitment by Early Funding Decile\n'
                 f'Average Cost = {avg_cost:.2f}× (Locked underperform Flexible)',
                 fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels([f'D{d}' for d in results_df['decile']])
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3, axis='y')

    # Add formula box
    ax.text(0.02, 0.98,
            r'$\mathrm{Cost} = E[Y|\mathrm{Locked}, E] - E[Y|\mathrm{Flexible}, E]$',
            transform=ax.transAxes, fontsize=11,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"   Saved: {save_path}")

    return fig


def create_figure3_cohorts(df: pd.DataFrame,
                           save_path: Optional[Path] = None) -> plt.Figure:
    """
    Figure 3: 2×2 Cohort Analysis - Escape Velocity vs Golden Cage.

    Cohorts:
    - Escape Velocity: Low E, High |ΔV| (underfunded but flexible)
    - Golden Cage: High E, Low |ΔV| (well-funded but locked)
    - Patient Capital: High E, High |ΔV| (well-funded and flexible)
    - Struggle Zone: Low E, Low |ΔV| (underfunded and locked)
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Compute medians for splitting
    median_E = df['E'].median()
    median_deltaV = df['|ΔV|'].median()

    # Assign cohorts
    df = df.copy()
    conditions = [
        (df['E'] <= median_E) & (df['|ΔV|'] > median_deltaV),   # Escape Velocity
        (df['E'] > median_E) & (df['|ΔV|'] <= median_deltaV),   # Golden Cage
        (df['E'] > median_E) & (df['|ΔV|'] > median_deltaV),    # Patient Capital
        (df['E'] <= median_E) & (df['|ΔV|'] <= median_deltaV),  # Struggle Zone
    ]
    cohort_names = ['Escape\nVelocity', 'Golden\nCage', 'Patient\nCapital', 'Struggle\nZone']
    df['cohort'] = np.select(conditions, cohort_names, default='Unknown')

    # Compute cohort statistics
    cohort_stats = df.groupby('cohort').agg({
        'Y': ['median', 'mean', 'std', 'count'],
        'E': 'median',
        '|ΔV|': 'median'
    }).round(3)
    cohort_stats.columns = ['Y_median', 'Y_mean', 'Y_std', 'n', 'E_median', 'deltaV_median']
    cohort_stats = cohort_stats.reset_index()

    # --- Panel A: Heatmap ---
    ax1 = axes[0]

    # Create 2x2 grid
    grid_data = np.zeros((2, 2))
    grid_labels = [['', ''], ['', '']]

    cohort_positions = {
        'Escape\nVelocity': (0, 1),  # Low E, High |ΔV|
        'Golden\nCage': (1, 0),       # High E, Low |ΔV|
        'Patient\nCapital': (1, 1),   # High E, High |ΔV|
        'Struggle\nZone': (0, 0),     # Low E, Low |ΔV|
    }

    for _, row in cohort_stats.iterrows():
        if row['cohort'] in cohort_positions:
            i, j = cohort_positions[row['cohort']]
            grid_data[i, j] = row['Y_median']
            grid_labels[i][j] = f"{row['cohort']}\nY={row['Y_median']:.2f}×\nn={int(row['n']):,}"

    # Custom colormap
    cmap = LinearSegmentedColormap.from_list('custom', ['#e74c3c', '#f1c40f', '#27ae60'])

    im = ax1.imshow(grid_data, cmap=cmap, aspect='auto', vmin=0, vmax=max(grid_data.flatten())*1.2)

    # Add text
    for i in range(2):
        for j in range(2):
            color = 'white' if grid_data[i, j] < 1 else 'black'
            ax1.text(j, i, grid_labels[i][j], ha='center', va='center',
                    fontsize=11, fontweight='bold', color=color)

    ax1.set_xticks([0, 1])
    ax1.set_yticks([0, 1])
    ax1.set_xticklabels(['Low |ΔV|\n(Locked)', 'High |ΔV|\n(Flexible)'])
    ax1.set_yticklabels(['Low E\n(Underfunded)', 'High E\n(Well-funded)'])
    ax1.set_title('2×2 Cohort Analysis\n(Cell values = Median Y)', fontsize=14, fontweight='bold')

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax1)
    cbar.set_label('Outcome Y = L/E', fontsize=11)

    # --- Panel B: Bar comparison ---
    ax2 = axes[1]

    # Get Escape Velocity and Golden Cage
    escape = cohort_stats[cohort_stats['cohort'] == 'Escape\nVelocity'].iloc[0]
    cage = cohort_stats[cohort_stats['cohort'] == 'Golden\nCage'].iloc[0]

    x = [0, 1]
    heights = [cage['Y_median'], escape['Y_median']]
    colors = ['#e74c3c', '#27ae60']
    labels = ['Golden Cage\n(High E, Low |ΔV|)', 'Escape Velocity\n(Low E, High |ΔV|)']

    bars = ax2.bar(x, heights, color=colors, edgecolor='black', linewidth=2, alpha=0.8)

    # Add value labels
    for i, (bar, h) in enumerate(zip(bars, heights)):
        ax2.text(bar.get_x() + bar.get_width()/2, h + 0.1,
                f'{h:.2f}×', ha='center', fontsize=14, fontweight='bold')

    # Add ratio annotation
    ratio = escape['Y_median'] / cage['Y_median'] if cage['Y_median'] > 0 else np.inf
    ax2.annotate(f'{ratio:.1f}× gap',
                xy=(0.5, (escape['Y_median'] + cage['Y_median'])/2),
                fontsize=16, fontweight='bold', ha='center',
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

    # Draw arrow
    ax2.annotate('', xy=(1, escape['Y_median']*0.9), xytext=(0, cage['Y_median']*1.1),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))

    ax2.set_xticks(x)
    ax2.set_xticklabels(labels, fontsize=11)
    ax2.set_ylabel('Outcome Y = L/E', fontsize=12)
    ax2.set_title('Key Comparison: Escape Velocity vs Golden Cage\n'
                  '"Deprivation → Flexibility → Success"',
                  fontsize=14, fontweight='bold')
    ax2.set_ylim(0, max(heights) * 1.3)
    ax2.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"   Saved: {save_path}")

    return fig


def create_table1_descriptive(df: pd.DataFrame,
                              save_path: Optional[Path] = None) -> pd.DataFrame:
    """
    Table 1: Descriptive Statistics by Cohort.
    """
    # Compute medians
    median_E = df['E'].median()
    median_deltaV = df['|ΔV|'].median()

    # Assign cohorts
    df = df.copy()
    conditions = [
        (df['E'] <= median_E) & (df['|ΔV|'] > median_deltaV),
        (df['E'] > median_E) & (df['|ΔV|'] <= median_deltaV),
        (df['E'] > median_E) & (df['|ΔV|'] > median_deltaV),
        (df['E'] <= median_E) & (df['|ΔV|'] <= median_deltaV),
    ]
    cohort_names = ['Escape Velocity', 'Golden Cage', 'Patient Capital', 'Struggle Zone']
    df['cohort'] = np.select(conditions, cohort_names, default='Unknown')

    # Compute statistics
    table = df.groupby('cohort').agg({
        'E': ['count', 'median', 'mean', 'std'],
        '|ΔV|': ['median', 'mean', 'std'],
        'Y': ['median', 'mean', 'std']
    }).round(3)

    # Flatten column names
    table.columns = ['_'.join(col).strip() for col in table.columns.values]
    table = table.reset_index()

    # Reorder
    order = ['Escape Velocity', 'Golden Cage', 'Patient Capital', 'Struggle Zone']
    table['cohort'] = pd.Categorical(table['cohort'], categories=order, ordered=True)
    table = table.sort_values('cohort').reset_index(drop=True)

    if save_path:
        table.to_csv(save_path, index=False)
        print(f"   Saved: {save_path}")

    return table


def create_table2_cost(df: pd.DataFrame,
                       save_path: Optional[Path] = None) -> pd.DataFrame:
    """
    Table 2: Cost of Commitment by Early Funding Decile.
    """
    median_deltaV = df['|ΔV|'].median()

    df = df.copy()
    df['flexibility'] = np.where(df['|ΔV|'] > median_deltaV, 'Flexible', 'Locked')
    df['E_decile'] = pd.qcut(df['E'], 10, labels=False, duplicates='drop') + 1

    results = []
    for decile in sorted(df['E_decile'].unique()):
        decile_data = df[df['E_decile'] == decile]

        locked = decile_data[decile_data['flexibility'] == 'Locked']
        flexible = decile_data[decile_data['flexibility'] == 'Flexible']

        if len(locked) > 0 and len(flexible) > 0:
            cost = locked['Y'].median() - flexible['Y'].median()

            # T-test for significance
            t_stat, p_value = stats.ttest_ind(locked['Y'].dropna(), flexible['Y'].dropna())

            results.append({
                'E_decile': decile,
                'E_range': f"{decile_data['E'].min():.0f} - {decile_data['E'].max():.0f}",
                'n_locked': len(locked),
                'n_flexible': len(flexible),
                'Y_locked_median': locked['Y'].median(),
                'Y_flexible_median': flexible['Y'].median(),
                'cost': cost,
                'p_value': p_value,
                'significance': '***' if p_value < 0.001 else ('**' if p_value < 0.01 else ('*' if p_value < 0.05 else ''))
            })

    table = pd.DataFrame(results)

    if save_path:
        table.to_csv(save_path, index=False)
        print(f"   Saved: {save_path}")

    return table


def generate_all_outputs():
    """Generate all figures and tables for the paper."""
    print("=" * 70)
    print("🦾C: When Commitment Becomes a Cage")
    print("Figure and Table Generation")
    print("=" * 70)

    # Load data
    print("\n📊 Loading panel data...")
    try:
        df = load_panel_data()
        print(f"   Loaded {len(df):,} observations")
        print(f"   Variables: E, L, V_E, V_L, |ΔV|, Y")
    except FileNotFoundError as e:
        print(f"   ⚠️ {e}")
        print("   Generating synthetic data for demonstration...")
        df = generate_synthetic_data()
        print(f"   Generated {len(df):,} synthetic observations")

    # Summary statistics
    print(f"\n📈 Summary Statistics:")
    print(f"   E (Early Funding): median={df['E'].median():,.0f}, mean={df['E'].mean():,.0f}")
    print(f"   |ΔV| (Flexibility): median={df['|ΔV|'].median():.2f}, mean={df['|ΔV|'].mean():.2f}")
    print(f"   Y (Outcome L/E): median={df['Y'].median():.2f}, mean={df['Y'].mean():.2f}")

    # Compute key correlations
    corr_E_deltaV = df['E'].corr(df['|ΔV|'])
    corr_deltaV_Y = df['|ΔV|'].corr(df['Y'])
    corr_E_Y = df['E'].corr(df['Y'])

    print(f"\n🔗 Key Correlations:")
    print(f"   ρ(E, |ΔV|) = {corr_E_deltaV:.3f} (d|ΔV|/dE < 0 ✓)" if corr_E_deltaV < 0 else f"   ρ(E, |ΔV|) = {corr_E_deltaV:.3f}")
    print(f"   ρ(|ΔV|, Y) = {corr_deltaV_Y:.3f} (dY/d|ΔV| > 0 ✓)" if corr_deltaV_Y > 0 else f"   ρ(|ΔV|, Y) = {corr_deltaV_Y:.3f}")
    print(f"   ρ(E, Y) = {corr_E_Y:.3f} (dY/dE < 0 ✓)" if corr_E_Y < 0 else f"   ρ(E, Y) = {corr_E_Y:.3f}")

    # Generate figures
    print("\n🎨 Generating figures...")

    fig1 = create_figure1_mechanism(df, OUTPUT_DIR / 'fig1_mechanism_3panel.png')
    fig2 = create_figure2_cost(df, OUTPUT_DIR / 'fig2_cost_by_decile.png')
    fig3 = create_figure3_cohorts(df, OUTPUT_DIR / 'fig3_cohort_analysis.png')

    # Generate tables
    print("\n📋 Generating tables...")

    table1 = create_table1_descriptive(df, OUTPUT_DIR / 'table1_descriptive.csv')
    table2 = create_table2_cost(df, OUTPUT_DIR / 'table2_cost_of_commitment.csv')

    print(f"\n✅ All outputs saved to: {OUTPUT_DIR}")
    print("\nFiles generated:")
    print("   Figures:")
    print("   - fig1_mechanism_3panel.png")
    print("   - fig2_cost_by_decile.png")
    print("   - fig3_cohort_analysis.png")
    print("   Tables:")
    print("   - table1_descriptive.csv")
    print("   - table2_cost_of_commitment.csv")

    return {
        'figures': [fig1, fig2, fig3],
        'tables': [table1, table2],
        'data': df
    }


def generate_synthetic_data(n: int = 10000) -> pd.DataFrame:
    """
    Generate synthetic data for demonstration.

    The data follows the hypothesized relationships:
    - d|ΔV|/dE < 0: Higher early funding → less flexibility
    - dY/d|ΔV| > 0: More flexibility → better outcomes
    - dY/dE < 0: Combined effect
    """
    np.random.seed(SEED)

    # Generate early funding (log-normal)
    E = np.exp(np.random.normal(14, 2, n))  # ~$1M median

    # Generate flexibility inversely related to E
    base_deltaV = 30 + np.random.normal(0, 10, n)
    E_effect = -5 * np.log10(E / 1e6)  # Higher E → lower |ΔV|
    noise = np.random.normal(0, 5, n)
    deltaV = np.clip(base_deltaV + E_effect + noise, 0, 100)

    # Generate outcome positively related to flexibility
    base_Y = 0.5 + np.random.normal(0, 0.3, n)
    deltaV_effect = 0.05 * deltaV  # Higher |ΔV| → higher Y
    noise_Y = np.random.exponential(0.5, n)
    Y = np.clip(base_Y + deltaV_effect + noise_Y, 0, 20)

    # Compute L from Y and E
    L = Y * E

    # Vagueness scores (for completeness)
    V_E = np.random.uniform(20, 80, n)
    V_L = V_E + np.random.normal(0, 1, n) * deltaV / 10

    df = pd.DataFrame({
        'company_id': range(n),
        'E': E,
        'L': L,
        'V_E': V_E,
        'V_L': V_L,
        '|ΔV|': deltaV,
        'Y': Y
    })

    return df


if __name__ == "__main__":
    outputs = generate_all_outputs()
    plt.show()
