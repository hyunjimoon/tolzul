#!/usr/bin/env python3
"""
P1: U-Shape - When Vagueness Pays
Figures Module - 나대용 🐅 (Builder)

Outputs:
- P1_u_shape_survival.png: U-shape survival vs vagueness
- P1_hw_sw_comparison.png: Hardware vs Software interaction
- P1_coefficient_table.png: Coefficient table visualization
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path
from typing import Optional, Dict, Any

# Import empirics module
from empirics import (
    generate_dummy_data,
    run_h1_ols,
    run_h2_logit,
    P1Config,
    SEED
)

# Reproducibility
np.random.seed(SEED)

# Figure settings
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

# Output directory
OUTPUT_DIR = Path(__file__).parent / 'output'
OUTPUT_DIR.mkdir(exist_ok=True)


def plot_u_shape_survival(df: pd.DataFrame, save_path: Optional[Path] = None) -> plt.Figure:
    """
    Plot U-shape relationship between vagueness and survival.

    Key insight: Both extreme clarity and extreme vagueness can be optimal,
    while moderate vagueness underperforms.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left: Scatter with lowess smoothing
    ax1 = axes[0]

    # Bin vagueness scores for better visualization
    df['vagueness_bin'] = pd.cut(df['vagueness_score'], bins=20)
    bin_means = df.groupby('vagueness_bin').agg({
        'vagueness_score': 'mean',
        'survival': 'mean'
    }).dropna()

    # Plot binned means
    ax1.scatter(bin_means['vagueness_score'], bin_means['survival'],
                s=100, alpha=0.7, c='steelblue', edgecolors='white', linewidth=1)

    # Fit quadratic curve
    x = df['vagueness_score'].values
    y = df['survival'].values
    z = np.polyfit(x, y, 2)
    p = np.poly1d(z)
    x_line = np.linspace(0, 1, 100)
    y_line = p(x_line)

    ax1.plot(x_line, y_line, 'r-', linewidth=2.5, label=f'Quadratic fit')

    # Mark optimal points
    optimal_low = x_line[np.argmax(y_line[:50])]
    optimal_high = x_line[50 + np.argmax(y_line[50:])]

    ax1.axvline(optimal_low, color='green', linestyle='--', alpha=0.5, label=f'Optimal low: {optimal_low:.2f}')
    ax1.axvline(optimal_high, color='green', linestyle='--', alpha=0.5, label=f'Optimal high: {optimal_high:.2f}')

    ax1.set_xlabel('Vagueness Score (V)')
    ax1.set_ylabel('Survival Rate')
    ax1.set_title('H1: U-Shape Relationship\nVagueness vs. Survival')
    ax1.legend(loc='lower right')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 0.7)
    ax1.grid(True, alpha=0.3)

    # Right: Marginal effects by vagueness level
    ax2 = axes[1]

    # Calculate survival rates by vagueness quintile
    df['vagueness_quintile'] = pd.qcut(df['vagueness_score'], 5, labels=['Q1\n(Low)', 'Q2', 'Q3', 'Q4', 'Q5\n(High)'])
    quintile_survival = df.groupby('vagueness_quintile')['survival'].mean()

    colors = ['#2ecc71', '#f1c40f', '#e74c3c', '#f1c40f', '#2ecc71']  # Green at extremes
    bars = ax2.bar(quintile_survival.index, quintile_survival.values, color=colors, edgecolor='black', linewidth=1)

    ax2.set_xlabel('Vagueness Quintile')
    ax2.set_ylabel('Survival Rate')
    ax2.set_title('Survival by Vagueness Quintile\n(U-Shape Evidence)')
    ax2.set_ylim(0, 0.6)
    ax2.grid(True, alpha=0.3, axis='y')

    # Add value labels
    for bar, val in zip(bars, quintile_survival.values):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f'{val:.1%}', ha='center', va='bottom', fontsize=10)

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"   Saved: {save_path}")

    return fig


def plot_hw_sw_comparison(df: pd.DataFrame, h2_results: Dict[str, Any],
                          save_path: Optional[Path] = None) -> plt.Figure:
    """
    Plot Hardware vs Software interaction effect.

    Key insight: Vagueness helps software (cheap pivots) but hurts hardware (costly pivots).
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left: Survival rates by vagueness and HW/SW
    ax1 = axes[0]

    # Split by hardware/software
    hw_df = df[df['is_hardware'] == 1]
    sw_df = df[df['is_hardware'] == 0]

    # Bin and calculate survival
    for label, subset, color, marker in [
        ('Software', sw_df, '#3498db', 'o'),
        ('Hardware', hw_df, '#e74c3c', 's')
    ]:
        subset = subset.copy()
        subset['vag_bin'] = pd.cut(subset['vagueness_score'], bins=10)
        bin_data = subset.groupby('vag_bin').agg({
            'vagueness_score': 'mean',
            'survival': 'mean'
        }).dropna()

        ax1.scatter(bin_data['vagueness_score'], bin_data['survival'],
                   s=80, alpha=0.7, c=color, marker=marker, label=label)

        # Fit linear trend
        if len(bin_data) > 2:
            z = np.polyfit(bin_data['vagueness_score'], bin_data['survival'], 1)
            p = np.poly1d(z)
            x_line = np.linspace(bin_data['vagueness_score'].min(),
                                bin_data['vagueness_score'].max(), 50)
            ax1.plot(x_line, p(x_line), color=color, linewidth=2, alpha=0.7)

    ax1.set_xlabel('Vagueness Score (V)')
    ax1.set_ylabel('Survival Rate')
    ax1.set_title('H2: Modularity Moderation\nVagueness Effect by Technology Type')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 1)

    # Right: Marginal effects visualization
    ax2 = axes[1]

    # Marginal effects from logit
    effects = [h2_results['marginal_effect_sw'], h2_results['marginal_effect_hw']]
    labels = ['Software\n(High Modularity)', 'Hardware\n(Low Modularity)']
    colors = ['#3498db', '#e74c3c']

    bars = ax2.bar(labels, effects, color=colors, edgecolor='black', linewidth=1.5)

    # Add significance stars
    p_values = [h2_results['p_v'], h2_results['p_interaction']]  # Approximate
    for i, (bar, effect) in enumerate(zip(bars, effects)):
        stars = '***' if p_values[i] < 0.01 else '**' if p_values[i] < 0.05 else '*' if p_values[i] < 0.1 else ''
        y_pos = effect + 0.02 if effect > 0 else effect - 0.05
        ax2.text(bar.get_x() + bar.get_width()/2, y_pos,
                f'{effect:.3f}{stars}', ha='center', va='bottom' if effect > 0 else 'top',
                fontsize=12, fontweight='bold')

    ax2.axhline(0, color='black', linewidth=0.5)
    ax2.set_ylabel('Marginal Effect of Vagueness on Survival')
    ax2.set_title('Marginal Effects by Technology Type\n(β + β_interaction for Hardware)')
    ax2.set_ylim(min(effects) - 0.2, max(effects) + 0.2)
    ax2.grid(True, alpha=0.3, axis='y')

    # Add annotation
    ax2.annotate('Vagueness helps\nSoftware (cheap pivots)',
                xy=(0, effects[0]), xytext=(0.3, effects[0] + 0.15),
                fontsize=9, ha='center',
                arrowprops=dict(arrowstyle='->', color='gray'))
    ax2.annotate('Vagueness hurts\nHardware (costly pivots)',
                xy=(1, effects[1]), xytext=(0.7, effects[1] - 0.15),
                fontsize=9, ha='center',
                arrowprops=dict(arrowstyle='->', color='gray'))

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"   Saved: {save_path}")

    return fig


def plot_coefficient_table(h1_results: Dict, h2_results: Dict,
                           save_path: Optional[Path] = None) -> plt.Figure:
    """
    Create visual coefficient table.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')

    # Table data
    columns = ['Variable', 'Coefficient', 'Std. Error', 'p-value', 'Significance']
    data = [
        ['H1: Vagueness (z)', f"{h1_results['beta_v']:.4f}", '-', f"{h1_results['p_v']:.4f}",
         '***' if h1_results['p_v'] < 0.01 else '**' if h1_results['p_v'] < 0.05 else '*'],
        ['H1: Vagueness² (z²)', f"{h1_results['beta_v_sq']:.4f}", '-', f"{h1_results['p_v_sq']:.4f}",
         '***' if h1_results['p_v_sq'] < 0.01 else '**' if h1_results['p_v_sq'] < 0.05 else '*'],
        ['H2: Vagueness (z)', f"{h2_results['beta_v']:.4f}", '-', f"{h2_results['p_v']:.4f}",
         '***' if h2_results['p_v'] < 0.01 else '**' if h2_results['p_v'] < 0.05 else '*'],
        ['H2: Hardware', f"{h2_results['beta_hw']:.4f}", '-', f"{h2_results['p_hw']:.4f}",
         '***' if h2_results['p_hw'] < 0.01 else '**' if h2_results['p_hw'] < 0.05 else '*'],
        ['H2: Vagueness × Hardware', f"{h2_results['beta_interaction']:.4f}", '-',
         f"{h2_results['p_interaction']:.4f}",
         '***' if h2_results['p_interaction'] < 0.01 else '**' if h2_results['p_interaction'] < 0.05 else '*'],
    ]

    # Create table
    table = ax.table(
        cellText=data,
        colLabels=columns,
        cellLoc='center',
        loc='center',
        colWidths=[0.35, 0.15, 0.15, 0.15, 0.12]
    )

    # Style table
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.2, 1.8)

    # Header style
    for i in range(len(columns)):
        table[(0, i)].set_facecolor('#34495e')
        table[(0, i)].set_text_props(color='white', fontweight='bold')

    # Alternate row colors
    for i in range(1, len(data) + 1):
        for j in range(len(columns)):
            if i % 2 == 0:
                table[(i, j)].set_facecolor('#ecf0f1')

    ax.set_title('P1 Regression Results: Vagueness and Startup Performance\n',
                fontsize=14, fontweight='bold')

    # Add notes
    fig.text(0.5, 0.02, '*** p<0.01, ** p<0.05, * p<0.1 | H1: OLS (DV: log funding) | H2: Logit (DV: survival)',
             ha='center', fontsize=9, style='italic')

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"   Saved: {save_path}")

    return fig


def generate_all_figures():
    """Generate all P1 figures"""
    print("=" * 70)
    print("P1 Figure Generation - 나대용 🐅")
    print("=" * 70)

    # Generate data
    print("\n📊 Generating data...")
    df = generate_dummy_data()

    # Run models
    print("📈 Running models...")
    h1 = run_h1_ols(df)
    h2 = run_h2_logit(df)

    # Generate figures
    print("\n🎨 Generating figures...")

    fig1 = plot_u_shape_survival(df, OUTPUT_DIR / 'P1_u_shape_survival.png')
    fig2 = plot_hw_sw_comparison(df, h2, OUTPUT_DIR / 'P1_hw_sw_comparison.png')
    fig3 = plot_coefficient_table(h1, h2, OUTPUT_DIR / 'P1_coefficient_table.png')

    print(f"\n✅ All P1 figures saved to: {OUTPUT_DIR}")
    print("\nFiles generated:")
    print("   - P1_u_shape_survival.png")
    print("   - P1_hw_sw_comparison.png")
    print("   - P1_coefficient_table.png")

    return [fig1, fig2, fig3]


if __name__ == "__main__":
    figures = generate_all_figures()
    plt.show()
