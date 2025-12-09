#!/usr/bin/env python3
"""
Visualize E/L/S/V/F Variable Distributions

Creates comprehensive visualizations of variable distributions,
particularly useful for quantum-filtered datasets.

Usage:
    python visualize_ELSVF.py data/processed/els_quantum.csv --output plots/
    python visualize_ELSVF.py data/processed/els_all.csv
"""

import sys
import argparse
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 10)


def plot_variable_distributions(df: pd.DataFrame, output_dir: Path = None, title_suffix: str = ""):
    """
    Create comprehensive distribution plots for E/L/S/V/F variables.

    Args:
        df: DataFrame with E, L, S_stepup, S_stepup_log, z_V, V_raw, F_flexibility
        output_dir: Directory to save plots (if None, display only)
        title_suffix: Suffix to add to plot titles (e.g., "- Quantum Companies")
    """
    fig, axes = plt.subplots(3, 3, figsize=(16, 12))
    fig.suptitle(f'E/L/S/V/F Variable Distributions{title_suffix}', fontsize=16, fontweight='bold')

    # Row 1: Binary variables (E, L, F)
    # E: Early event
    ax = axes[0, 0]
    e_counts = df['E'].value_counts().sort_index()
    e_pct = df['E'].value_counts(normalize=True).sort_index() * 100
    bars = ax.bar(['No Series A (0)', 'Series A (1)'], e_counts.values, color=['#E74C3C', '#3498DB'])
    ax.set_ylabel('Count', fontsize=11)
    ax.set_title(f'E: Early Event (Series A)\nRate: {df["E"].mean():.1%}', fontsize=12, fontweight='bold')
    # Add percentage labels on bars
    for bar, pct in zip(bars, e_pct.values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{pct:.1f}%\n(n={int(height):,})',
                ha='center', va='bottom', fontsize=9)
    ax.grid(axis='y', alpha=0.3)

    # L: Later success
    ax = axes[0, 1]
    l_counts = df['L'].value_counts().sort_index()
    l_pct = df['L'].value_counts(normalize=True).sort_index() * 100
    bars = ax.bar(['No Series B+ (0)', 'Series B+ (1)'], l_counts.values, color=['#E74C3C', '#2ECC71'])
    ax.set_ylabel('Count', fontsize=11)
    ax.set_title(f'L: Later Success (Series B+)\nRate: {df["L"].mean():.1%}', fontsize=12, fontweight='bold')
    for bar, pct in zip(bars, l_pct.values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{pct:.1f}%\n(n={int(height):,})',
                ha='center', va='bottom', fontsize=9)
    ax.grid(axis='y', alpha=0.3)

    # F: Flexibility
    ax = axes[0, 2]
    f_counts = df['F_flexibility'].value_counts().sort_index()
    f_pct = df['F_flexibility'].value_counts(normalize=True).sort_index() * 100
    bars = ax.bar(['Hardware (0)', 'Software (1)'], f_counts.values, color=['#95A5A6', '#9B59B6'])
    ax.set_ylabel('Count', fontsize=11)
    ax.set_title(f'F: Flexibility (1-Hardware)\nSoftware Rate: {df["F_flexibility"].mean():.1%}',
                 fontsize=12, fontweight='bold')
    for bar, pct in zip(bars, f_pct.values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{pct:.1f}%\n(n={int(height):,})',
                ha='center', va='bottom', fontsize=9)
    ax.grid(axis='y', alpha=0.3)

    # Row 2: V (Vagueness)
    # V: Raw distribution
    ax = axes[1, 0]
    v_valid = df['V_raw'].dropna()
    if len(v_valid) > 0:
        ax.hist(v_valid, bins=30, color='#E67E22', alpha=0.7, edgecolor='black')
        ax.axvline(v_valid.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {v_valid.mean():.3f}')
        ax.axvline(v_valid.median(), color='blue', linestyle='--', linewidth=2, label=f'Median: {v_valid.median():.3f}')
        ax.set_xlabel('Vagueness (Raw)', fontsize=11)
        ax.set_ylabel('Count', fontsize=11)
        ax.set_title(f'V: Vagueness (Raw)\nN={len(v_valid):,}', fontsize=12, fontweight='bold')
        ax.legend(fontsize=9)
        ax.grid(axis='y', alpha=0.3)
    else:
        ax.text(0.5, 0.5, 'No valid V_raw data', ha='center', va='center', transform=ax.transAxes)
        ax.set_title('V: Vagueness (Raw)', fontsize=12, fontweight='bold')

    # V: Z-scored distribution
    ax = axes[1, 1]
    zv_valid = df['z_V'].dropna()
    if len(zv_valid) > 0:
        ax.hist(zv_valid, bins=30, color='#1ABC9C', alpha=0.7, edgecolor='black')
        ax.axvline(zv_valid.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {zv_valid.mean():.3f}')
        ax.axvline(0, color='gray', linestyle='-', linewidth=1, alpha=0.5, label='Zero')
        ax.set_xlabel('Vagueness (Z-scored)', fontsize=11)
        ax.set_ylabel('Count', fontsize=11)
        ax.set_title(f'z_V: Vagueness (Standardized)\nN={len(zv_valid):,}', fontsize=12, fontweight='bold')
        ax.legend(fontsize=9)
        ax.grid(axis='y', alpha=0.3)
    else:
        ax.text(0.5, 0.5, 'No valid z_V data', ha='center', va='center', transform=ax.transAxes)
        ax.set_title('z_V: Vagueness (Z-scored)', fontsize=12, fontweight='bold')

    # V by E/L status
    ax = axes[1, 2]
    if len(zv_valid) > 0:
        v_by_E = []
        labels_E = []
        for e_val in [0, 1]:
            v_subset = df[df['E'] == e_val]['z_V'].dropna()
            if len(v_subset) > 0:
                v_by_E.append(v_subset)
                labels_E.append(f'E={e_val}\n(n={len(v_subset):,})')

        if v_by_E:
            bp = ax.boxplot(v_by_E, labels=labels_E, patch_artist=True,
                           boxprops=dict(facecolor='#F39C12', alpha=0.6),
                           medianprops=dict(color='red', linewidth=2))
            ax.set_ylabel('z_V (Vagueness)', fontsize=11)
            ax.set_xlabel('Early Event Status', fontsize=11)
            ax.set_title('Vagueness by E Status', fontsize=12, fontweight='bold')
            ax.grid(axis='y', alpha=0.3)
        else:
            ax.text(0.5, 0.5, 'Insufficient data', ha='center', va='center', transform=ax.transAxes)
            ax.set_title('Vagueness by E Status', fontsize=12, fontweight='bold')
    else:
        ax.text(0.5, 0.5, 'No valid z_V data', ha='center', va='center', transform=ax.transAxes)
        ax.set_title('Vagueness by E Status', fontsize=12, fontweight='bold')

    # Row 3: S (Step-up)
    # S: Raw distribution
    ax = axes[2, 0]
    s_valid = df['S_stepup'].dropna()
    if len(s_valid) > 0:
        # Remove extreme outliers for visualization
        s_99 = s_valid.quantile(0.99)
        s_plot = s_valid[s_valid <= s_99]
        ax.hist(s_plot, bins=30, color='#8E44AD', alpha=0.7, edgecolor='black')
        ax.axvline(s_valid.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {s_valid.mean():.2f}')
        ax.axvline(s_valid.median(), color='blue', linestyle='--', linewidth=2, label=f'Median: {s_valid.median():.2f}')
        ax.set_xlabel('Step-up (Raw)', fontsize=11)
        ax.set_ylabel('Count', fontsize=11)
        ax.set_title(f'S: Step-up (Raw, 99th %ile)\nN={len(s_valid):,}', fontsize=12, fontweight='bold')
        ax.legend(fontsize=9)
        ax.grid(axis='y', alpha=0.3)
    else:
        ax.text(0.5, 0.5, 'No valid S_stepup data', ha='center', va='center', transform=ax.transAxes)
        ax.set_title('S: Step-up (Raw)', fontsize=12, fontweight='bold')

    # S: Log distribution
    ax = axes[2, 1]
    s_log_valid = df['S_stepup_log'].dropna()
    if len(s_log_valid) > 0:
        ax.hist(s_log_valid, bins=30, color='#16A085', alpha=0.7, edgecolor='black')
        ax.axvline(s_log_valid.mean(), color='red', linestyle='--', linewidth=2,
                  label=f'Mean: {s_log_valid.mean():.3f}')
        ax.axvline(s_log_valid.median(), color='blue', linestyle='--', linewidth=2,
                  label=f'Median: {s_log_valid.median():.3f}')
        ax.set_xlabel('Step-up (Log)', fontsize=11)
        ax.set_ylabel('Count', fontsize=11)
        ax.set_title(f'log(S): Step-up (Log)\nN={len(s_log_valid):,}', fontsize=12, fontweight='bold')
        ax.legend(fontsize=9)
        ax.grid(axis='y', alpha=0.3)
    else:
        ax.text(0.5, 0.5, 'No valid S_stepup_log data', ha='center', va='center', transform=ax.transAxes)
        ax.set_title('log(S): Step-up (Log)', fontsize=12, fontweight='bold')

    # S by F status (L==1 only)
    ax = axes[2, 2]
    df_L1 = df[df['L'] == 1].copy()
    if len(df_L1) > 0 and 'S_stepup_log' in df_L1.columns:
        s_by_F = []
        labels_F = []
        for f_val in [0, 1]:
            s_subset = df_L1[df_L1['F_flexibility'] == f_val]['S_stepup_log'].dropna()
            if len(s_subset) > 0:
                s_by_F.append(s_subset)
                label = 'Hardware' if f_val == 0 else 'Software'
                labels_F.append(f'{label}\n(n={len(s_subset):,})')

        if s_by_F:
            bp = ax.boxplot(s_by_F, labels=labels_F, patch_artist=True,
                           boxprops=dict(facecolor='#27AE60', alpha=0.6),
                           medianprops=dict(color='red', linewidth=2))
            ax.set_ylabel('log(S) Step-up', fontsize=11)
            ax.set_xlabel('Flexibility', fontsize=11)
            ax.set_title(f'Step-up by F (L==1 only)\nN={len(df_L1):,}', fontsize=12, fontweight='bold')
            ax.grid(axis='y', alpha=0.3)
        else:
            ax.text(0.5, 0.5, 'Insufficient data', ha='center', va='center', transform=ax.transAxes)
            ax.set_title('Step-up by F (L==1 only)', fontsize=12, fontweight='bold')
    else:
        ax.text(0.5, 0.5, 'No L==1 companies', ha='center', va='center', transform=ax.transAxes)
        ax.set_title('Step-up by F (L==1 only)', fontsize=12, fontweight='bold')

    plt.tight_layout()

    # Save or show
    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / 'ELSVF_distributions.png'
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"\n✓ Saved plot to: {output_file}")
    else:
        plt.show()

    plt.close()


def print_summary_statistics(df: pd.DataFrame, title: str = "Summary Statistics"):
    """Print summary statistics for E/L/S/V/F variables."""
    print("\n" + "=" * 70)
    print(f"{title}")
    print("=" * 70)

    print(f"\n📊 Sample Size: {len(df):,} companies")

    print(f"\n📍 Binary Variables:")
    print(f"   E (Early event):      {df['E'].sum():>6,} / {len(df):,} = {df['E'].mean():>6.1%}")
    print(f"   L (Later success):    {df['L'].sum():>6,} / {len(df):,} = {df['L'].mean():>6.1%}")
    print(f"   F (Flexibility):      {df['F_flexibility'].sum():>6,} / {len(df):,} = {df['F_flexibility'].mean():>6.1%}")

    print(f"\n📈 Continuous Variables:")

    # Vagueness
    v_valid = df['z_V'].dropna()
    if len(v_valid) > 0:
        print(f"   z_V (Vagueness):      Mean={v_valid.mean():>7.3f}, Std={v_valid.std():>7.3f}, N={len(v_valid):,}")
    else:
        print(f"   z_V (Vagueness):      No valid data")

    # Step-up
    s_valid = df['S_stepup'].dropna()
    s_log_valid = df['S_stepup_log'].dropna()
    if len(s_valid) > 0:
        print(f"   S (Step-up):          Mean={s_valid.mean():>7.2f}, Median={s_valid.median():>7.2f}, N={len(s_valid):,}")
    else:
        print(f"   S (Step-up):          No valid data")

    if len(s_log_valid) > 0:
        print(f"   log(S) (Step-up):     Mean={s_log_valid.mean():>7.3f}, Std={s_log_valid.std():>7.3f}, N={len(s_log_valid):,}")
    else:
        print(f"   log(S) (Step-up):     No valid data")

    print("\n" + "=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Visualize E/L/S/V/F variable distributions",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        'input_csv',
        type=Path,
        help='Input CSV file with E/L/S/V/F variables'
    )
    parser.add_argument(
        '--output', '-o',
        type=Path,
        default=None,
        help='Output directory for plots (if not specified, display only)'
    )
    parser.add_argument(
        '--title-suffix', '-t',
        type=str,
        default='',
        help='Suffix to add to plot titles (e.g., " - Quantum Companies")'
    )

    args = parser.parse_args()

    # Load data
    if not args.input_csv.exists():
        print(f"❌ ERROR: Input file not found: {args.input_csv}")
        return 1

    print(f"📂 Loading data from: {args.input_csv}")
    df = pd.read_csv(args.input_csv)

    # Print summary statistics
    print_summary_statistics(df, f"E/L/S/V/F Summary{args.title_suffix}")

    # Create visualizations
    print(f"\n📊 Creating visualizations...")
    plot_variable_distributions(df, args.output, args.title_suffix)

    print(f"\n✓ Visualization complete!")

    return 0


if __name__ == "__main__":
    sys.exit(main())
