#!/usr/bin/env python3
"""
P3: Execution Gap - Optimal Number of Options
Figures Module - 나대용 🐅 (Builder)

Outputs:
- P3_cr_kstar_curve.png: CR vs k* policy curve
- P3_sensitivity_heatmap.png: Sensitivity to σ(D) heatmap
- P3_industry_calibration.png: Industry-specific calibration
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
from pathlib import Path
from typing import Optional, Dict, Any

# Import model module
from model import (
    NewsvendorConfig,
    CostStructure,
    generate_cr_kstar_curve,
    generate_sensitivity_analysis,
    industry_calibration,
    compute_policy_regions,
    find_optimal_k_normal,
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
OUTPUT_DIR = Path(__file__).parent / 'figures'
OUTPUT_DIR.mkdir(exist_ok=True)


def plot_cr_kstar_curve(cr_curve: pd.DataFrame,
                       save_path: Optional[Path] = None) -> plt.Figure:
    """
    Plot CR vs k* policy curve with region annotations.

    Main figure for P3: Shows how optimal option count varies with CR.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left: Main CR vs k* curve
    ax1 = axes[0]

    # Plot the curve
    ax1.plot(cr_curve['CR'], cr_curve['k_star'], 'b-', linewidth=2.5, label='Optimal k*')

    # Shade policy regions
    regions = compute_policy_regions()
    colors = {'Commit Early': '#27ae60', 'Balanced': '#f1c40f', 'Many Options': '#e74c3c'}

    for policy, (low, high) in regions.items():
        ax1.axvspan(low, high, alpha=0.2, color=colors[policy], label=policy)

    # Mark critical points
    for cr_val, label in [(0.35, 'P1 Zone\n(Flexibility trap)'), (0.65, 'P2 Zone\n(Commitment trap)')]:
        k_at_cr = cr_curve[cr_curve['CR'] >= cr_val].iloc[0]['k_star']
        ax1.axvline(cr_val, color='gray', linestyle='--', alpha=0.5)
        ax1.annotate(label, xy=(cr_val, k_at_cr), xytext=(cr_val + 0.05, k_at_cr + 1),
                    fontsize=9, ha='left',
                    arrowprops=dict(arrowstyle='->', color='gray', alpha=0.5))

    ax1.set_xlabel('Commitment Ratio (CR = C / (C + F))')
    ax1.set_ylabel('Optimal Option Count (k*)')
    ax1.set_title('H2: CR Predicts Optimal Option Portfolio\nNewsvendor Critical Fractile Solution')
    ax1.legend(loc='upper left')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, cr_curve['k_star'].max() * 1.1)
    ax1.grid(True, alpha=0.3)

    # Add formula
    ax1.text(0.7, 1.5, r'$k^* = \mu + \sigma \cdot \Phi^{-1}(CR)$',
            fontsize=12, ha='center', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # Right: Expected payoff by CR
    ax2 = axes[1]

    ax2.plot(cr_curve['CR'], cr_curve['payoff'], 'g-', linewidth=2.5)
    ax2.fill_between(cr_curve['CR'], cr_curve['payoff'], alpha=0.3, color='green')

    ax2.set_xlabel('Commitment Ratio (CR)')
    ax2.set_ylabel('Expected Payoff')
    ax2.set_title('Expected Payoff at Optimal k*\n(Higher is better)')
    ax2.set_xlim(0, 1)
    ax2.grid(True, alpha=0.3)

    # Mark optimal CR region
    optimal_cr = cr_curve.loc[cr_curve['payoff'].idxmax(), 'CR']
    ax2.axvline(optimal_cr, color='red', linestyle='--', label=f'Best CR ≈ {optimal_cr:.2f}')
    ax2.legend()

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"   Saved: {save_path}")

    return fig


def plot_sensitivity_heatmap(sensitivity: pd.DataFrame,
                            save_path: Optional[Path] = None) -> plt.Figure:
    """
    Plot heatmap showing k* sensitivity to σ(D) and CR.
    """
    fig, ax = plt.subplots(figsize=(10, 7))

    # Pivot for heatmap
    pivot = sensitivity.pivot(index='sigma', columns='CR', values='k_star')

    # Custom colormap
    colors = ['#27ae60', '#f1c40f', '#e74c3c']
    cmap = LinearSegmentedColormap.from_list('kstar', colors)

    im = ax.imshow(pivot.values, cmap=cmap, aspect='auto',
                   extent=[pivot.columns.min(), pivot.columns.max(),
                          pivot.index.min(), pivot.index.max()],
                   origin='lower')

    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Optimal k*', fontsize=11)

    # Add contour lines
    X, Y = np.meshgrid(pivot.columns, pivot.index)
    contours = ax.contour(X, Y, pivot.values, levels=[2, 4, 6], colors='white', linewidths=1.5)
    ax.clabel(contours, inline=True, fontsize=9, fmt='k*=%.0f')

    ax.set_xlabel('Commitment Ratio (CR)')
    ax.set_ylabel('Demand Uncertainty (σ)')
    ax.set_title('H1: Optimal k* = f(CR, σ)\nSensitivity to Uncertainty')

    # Add annotations for strategy zones
    ax.text(0.3, 4.5, 'Few Options\n(Commit)', fontsize=10, ha='center', color='white', fontweight='bold')
    ax.text(0.7, 4.5, 'Many Options\n(Hedge)', fontsize=10, ha='center', color='white', fontweight='bold')
    ax.text(0.5, 1.5, 'Low uncertainty:\nk* stable', fontsize=9, ha='center', color='white')

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"   Saved: {save_path}")

    return fig


def plot_industry_calibration(industries: pd.DataFrame,
                             save_path: Optional[Path] = None) -> plt.Figure:
    """
    Plot industry-specific CR calibration and optimal strategies.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: CR vs k* scatter with industry labels
    ax1 = axes[0]

    # Color by strategy
    strategy_colors = {
        'Commit early': '#27ae60',
        'Balanced': '#f1c40f',
        'Many options': '#e74c3c'
    }

    for _, row in industries.iterrows():
        color = strategy_colors.get(row['optimal_strategy'], 'gray')
        ax1.scatter(row['CR'], row['k_star'], s=150, c=color,
                   edgecolors='black', linewidth=1.5, alpha=0.8)
        ax1.annotate(row['industry'], xy=(row['CR'], row['k_star']),
                    xytext=(5, 5), textcoords='offset points', fontsize=9)

    # Add policy region bands
    ax1.axvspan(0, 0.35, alpha=0.1, color='green')
    ax1.axvspan(0.35, 0.65, alpha=0.1, color='yellow')
    ax1.axvspan(0.65, 1.0, alpha=0.1, color='red')

    # Add theoretical curve
    config = NewsvendorConfig()
    cr_range = np.linspace(0.1, 0.9, 50)
    k_theory = []
    for cr in cr_range:
        costs = CostStructure(C=cr * 100, F=(1-cr) * 100)
        k, _ = find_optimal_k_normal(costs, config)
        k_theory.append(k)

    ax1.plot(cr_range, k_theory, 'k--', alpha=0.5, linewidth=1.5, label='Theoretical curve')

    ax1.set_xlabel('Commitment Ratio (CR = C / (C + F))')
    ax1.set_ylabel('Optimal Option Count (k*)')
    ax1.set_title('Industry Calibration: CR → k*\nPositioning on CR-k* Plane')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, industries['k_star'].max() * 1.2)
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # Right: Strategy recommendation table
    ax2 = axes[1]
    ax2.axis('off')

    # Create table
    table_data = industries[['industry', 'CR', 'k_star', 'optimal_strategy']].values.tolist()
    columns = ['Industry', 'CR', 'k*', 'Strategy']

    # Round values for display
    for row in table_data:
        row[1] = f"{row[1]:.2f}"
        row[2] = f"{row[2]:.1f}"

    table = ax2.table(
        cellText=table_data,
        colLabels=columns,
        cellLoc='center',
        loc='center',
        colWidths=[0.35, 0.15, 0.15, 0.25]
    )

    # Style table
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.8)

    # Header style
    for i in range(len(columns)):
        table[(0, i)].set_facecolor('#34495e')
        table[(0, i)].set_text_props(color='white', fontweight='bold')

    # Color rows by strategy
    for i, row in enumerate(table_data):
        strategy = row[3]
        color = '#e8f8e8' if strategy == 'Commit early' else \
                '#fff8e8' if strategy == 'Balanced' else '#f8e8e8'
        for j in range(len(columns)):
            table[(i + 1, j)].set_facecolor(color)

    ax2.set_title('Industry Strategy Recommendations\n', fontsize=14, fontweight='bold')

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"   Saved: {save_path}")

    return fig


def plot_fomo_timeline(save_path: Optional[Path] = None) -> plt.Figure:
    """
    Plot FOMO Timeline - The Killer Plot for Promise Vendor.

    Shows:
    - Divergence point where FOMO signal should have triggered
    - Committed companies that missed the signal
    - Flexible companies that responded to the signal
    - Counterfactual C visualization
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: EV Transition Timeline (2016-2024)
    ax1 = axes[0]

    years = np.array([2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])

    # Market cap trajectories (normalized, illustrative)
    tesla = np.array([0.03, 0.05, 0.06, 0.08, 0.65, 1.0, 0.55, 0.45, 0.70])  # Tesla trajectory
    gm = np.array([0.05, 0.06, 0.05, 0.05, 0.06, 0.08, 0.05, 0.04, 0.05])     # GM trajectory
    ford = np.array([0.04, 0.05, 0.04, 0.04, 0.04, 0.05, 0.04, 0.03, 0.04])   # Ford trajectory
    rivian = np.array([0.0, 0.0, 0.01, 0.02, 0.05, 0.15, 0.03, 0.02, 0.02])   # Rivian trajectory

    # Scale to billions
    tesla *= 1000
    gm *= 1000
    ford *= 1000
    rivian *= 1000

    ax1.plot(years, tesla, 'g-', linewidth=3, marker='o', label='Tesla (EV-first, k=1)', markersize=8)
    ax1.plot(years, gm, 'r-', linewidth=2, marker='s', label='GM (ICE-locked, k=0)', markersize=6)
    ax1.plot(years, ford, 'orange', linewidth=2, marker='^', label='Ford (ICE-locked, k=0)', markersize=6)
    ax1.plot(years, rivian, 'b--', linewidth=2, marker='d', label='Rivian (EV-native, k=1)', markersize=6)

    # Mark FOMO signal point
    ax1.axvline(2017, color='purple', linestyle='--', linewidth=2, alpha=0.7)
    ax1.annotate('FOMO Signal\n"Model 3 ramp"',
                xy=(2017, 800), xytext=(2018.5, 850),
                fontsize=10, ha='center',
                arrowprops=dict(arrowstyle='->', color='purple', lw=2),
                bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.9))

    # Mark divergence zone
    ax1.axvspan(2017, 2021, alpha=0.1, color='purple', label='FOMO Window')

    # Counterfactual C annotation
    ax1.annotate('', xy=(2021, 1000), xytext=(2021, 80),
                arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    ax1.text(2021.3, 500, 'C ≈ $920B\n(Counterfactual\nCommitment Cost)',
            fontsize=9, color='red', ha='left', va='center',
            bbox=dict(boxstyle='round', facecolor='#ffe6e6', alpha=0.9))

    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('Market Cap ($B)', fontsize=12)
    ax1.set_title('FOMO Timeline: EV Transition 2016-2024\n"When did FOMO trigger? Who listened?"',
                 fontsize=13, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=9)
    ax1.set_xlim(2015.5, 2024.5)
    ax1.set_ylim(0, 1100)
    ax1.grid(True, alpha=0.3)

    # Right: FOMO vs Overconfidence on CR-k* plane
    ax2 = axes[1]

    # Draw optimal k* curve
    config = NewsvendorConfig()
    cr_range = np.linspace(0.05, 0.95, 100)
    k_theory = []
    for cr in cr_range:
        costs = CostStructure(C=cr * 100, F=(1-cr) * 100)
        k, _ = find_optimal_k_normal(costs, config)
        k_theory.append(k)

    ax2.plot(cr_range, k_theory, 'k-', linewidth=3, label='Optimal k*(CR)')
    ax2.fill_between(cr_range, k_theory, alpha=0.2, color='green')

    # FOMO zone (perceived high C)
    ax2.annotate('FOMO Zone\n(Perceive C↑)\n"Should I hedge?"',
                xy=(0.75, 8), fontsize=11, ha='center',
                bbox=dict(boxstyle='round', facecolor='#e6f3ff', alpha=0.9, edgecolor='blue'))

    # Overconfidence zone (perceived low C)
    ax2.annotate('Overconfidence Zone\n(Perceive C↓)\n"I\'m sure!"',
                xy=(0.25, 2), fontsize=11, ha='center',
                bbox=dict(boxstyle='round', facecolor='#ffe6e6', alpha=0.9, edgecolor='red'))

    # Mark examples
    examples = [
        ('Tesla 2017', 0.8, 1, 'green', 'o'),      # EV-first (correct high CR perception)
        ('GM 2017', 0.3, 0, 'red', 's'),           # ICE-locked (wrong low CR perception)
        ('Comma.ai', 0.7, 3, 'blue', 'd'),         # Flexible (correct)
        ('Waymo', 0.5, 1, 'orange', '^'),          # Committed (locked in)
    ]

    for name, cr, k, color, marker in examples:
        ax2.scatter(cr, k, s=150, c=color, marker=marker, edgecolors='black',
                   linewidth=1.5, zorder=5)
        offset = (10, 10) if cr < 0.5 else (-10, 10)
        ax2.annotate(name, xy=(cr, k), xytext=offset, textcoords='offset points',
                    fontsize=9, ha='left' if cr < 0.5 else 'right')

    # Arrow showing FOMO → k* increase
    ax2.annotate('', xy=(0.7, 6), xytext=(0.5, 3),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2,
                               connectionstyle='arc3,rad=0.3'))
    ax2.text(0.55, 5, 'FOMO\ntriggers', fontsize=9, color='blue', ha='center')

    # Arrow showing Overconfidence → k* decrease
    ax2.annotate('', xy=(0.3, 1), xytext=(0.5, 3),
                arrowprops=dict(arrowstyle='->', color='red', lw=2,
                               connectionstyle='arc3,rad=-0.3'))
    ax2.text(0.45, 1.5, 'Over-\nconfidence', fontsize=9, color='red', ha='center')

    ax2.set_xlabel('Perceived CR = C/(C+F)', fontsize=12)
    ax2.set_ylabel('Option Count (k)', fontsize=12)
    ax2.set_title('Same Model, Two Extremes\nFOMO ↔ Overconfidence',
                 fontsize=13, fontweight='bold')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 10)
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper left')

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"   Saved: {save_path}")

    return fig


def plot_unified_framework(save_path: Optional[Path] = None) -> plt.Figure:
    """
    Plot unified P1/P2/P3 framework on CR-k* plane.
    """
    fig, ax = plt.subplots(figsize=(12, 8))

    # Background regions
    ax.axvspan(0, 0.35, alpha=0.15, color='blue', label='P1 Zone: Flexibility Trap')
    ax.axvspan(0.65, 1.0, alpha=0.15, color='red', label='P2 Zone: Commitment Trap')
    ax.axvspan(0.35, 0.65, alpha=0.15, color='green', label='Balanced Zone')

    # Draw optimal curve
    config = NewsvendorConfig()
    cr_range = np.linspace(0.05, 0.95, 100)
    k_theory = []
    for cr in cr_range:
        costs = CostStructure(C=cr * 100, F=(1-cr) * 100)
        k, _ = find_optimal_k_normal(costs, config)
        k_theory.append(k)

    ax.plot(cr_range, k_theory, 'k-', linewidth=3, label='Optimal k*(CR)')

    # Add trap annotations
    ax.annotate('P1 Trap:\nToo vague,\nmissed commitment',
               xy=(0.15, 2), fontsize=11, ha='center',
               bbox=dict(boxstyle='round', facecolor='#cce5ff', alpha=0.8))

    ax.annotate('P2 Trap:\nOver-committed,\nlocked in',
               xy=(0.85, 8), fontsize=11, ha='center',
               bbox=dict(boxstyle='round', facecolor='#ffcccc', alpha=0.8))

    ax.annotate('Sweet Spot:\nBalanced options',
               xy=(0.5, 5), fontsize=11, ha='center',
               bbox=dict(boxstyle='round', facecolor='#ccffcc', alpha=0.8))

    # Add industry examples
    industries = industry_calibration()
    for _, row in industries.iterrows():
        ax.scatter(row['CR'], row['k_star'], s=100, c='orange',
                  edgecolors='black', zorder=5)
        ax.annotate(row['industry'].split()[0], xy=(row['CR'], row['k_star']),
                   xytext=(5, 5), textcoords='offset points', fontsize=8)

    ax.set_xlabel('Commitment Ratio (CR = C / (C + F))', fontsize=12)
    ax.set_ylabel('Option Count (k)', fontsize=12)
    ax.set_title('Unified Framework: P1-P2-P3 on CR-k* Plane\n'
                'Options Architecture Determines Strategic Sweet Spot',
                fontsize=14, fontweight='bold')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 12)
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)

    # Add formula box
    textstr = 'Newsvendor Solution:\n' + r'$k^* = \mu_D + \sigma_D \cdot \Phi^{-1}(CR)$' + \
              '\n\nwhere CR = C/(C+F)'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    ax.text(0.75, 0.15, textstr, transform=ax.transAxes, fontsize=10,
           verticalalignment='bottom', bbox=props)

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"   Saved: {save_path}")

    return fig


def generate_all_figures():
    """Generate all P3 figures"""
    print("=" * 70)
    print("P3 Figure Generation - Promise Vendor 🤹N")
    print("=" * 70)

    # Generate data
    print("\n📊 Generating model outputs...")
    config = NewsvendorConfig()
    cr_curve = generate_cr_kstar_curve(config)
    sensitivity = generate_sensitivity_analysis(config)
    industries = industry_calibration()

    # Generate figures
    print("\n🎨 Generating figures...")

    fig1 = plot_cr_kstar_curve(cr_curve, OUTPUT_DIR / 'P3_cr_kstar_curve.png')
    fig2 = plot_sensitivity_heatmap(sensitivity, OUTPUT_DIR / 'P3_sensitivity_heatmap.png')
    fig3 = plot_industry_calibration(industries, OUTPUT_DIR / 'P3_industry_calibration.png')
    fig4 = plot_unified_framework(OUTPUT_DIR / 'P3_unified_framework.png')
    fig5 = plot_fomo_timeline(OUTPUT_DIR / 'P3_fomo_timeline.png')  # KILLER PLOT

    print(f"\n✅ All P3 figures saved to: {OUTPUT_DIR}")
    print("\nFiles generated:")
    print("   - P3_cr_kstar_curve.png")
    print("   - P3_sensitivity_heatmap.png")
    print("   - P3_industry_calibration.png")
    print("   - P3_unified_framework.png")
    print("   - P3_fomo_timeline.png  ⭐ KILLER PLOT")

    return [fig1, fig2, fig3, fig4, fig5]


if __name__ == "__main__":
    figures = generate_all_figures()
    plt.show()
