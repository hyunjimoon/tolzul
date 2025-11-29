#!/usr/bin/env python3
"""
P2: Competency Trap - When Success Kills Options
Figures Module - 나대용 🐅 (Builder)

Outputs:
- P2_belief_lockin_diagram.png: μ,σ → threshold visualization
- P2_pivot_threshold_curve.png: Pivot threshold vs σ curve
- P2_case_comparison.png: Waymo vs Comma.ai comparison
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
from pathlib import Path
from typing import Optional, Dict, Any

# Import simulation module
from simulation import (
    P2Config,
    Prior,
    CapTable,
    Investor,
    InvestorType,
    compute_switching_threshold,
    run_monte_carlo_simulation,
    analyze_threshold_dynamics,
    case_study_waymo_vs_comma,
    simulate_belief_trajectory,
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


def plot_belief_lockin_diagram(save_path: Optional[Path] = None) -> plt.Figure:
    """
    Plot the belief lock-in mechanism diagram.

    Shows how (μ, σ) evolves and how threshold changes with believer composition.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: Threshold heatmap (σ vs believer_ratio)
    ax1 = axes[0]

    sigma_range = np.linspace(0.05, 0.4, 50)
    believer_range = np.linspace(0.1, 0.9, 50)
    S, B = np.meshgrid(sigma_range, believer_range)

    config = P2Config()
    Z = np.zeros_like(S)
    for i in range(len(believer_range)):
        for j in range(len(sigma_range)):
            Z[i, j] = compute_switching_threshold(S[i, j], B[i, j], config)

    # Custom colormap: green (low threshold) to red (high threshold)
    colors = ['#27ae60', '#f1c40f', '#e74c3c']
    cmap = LinearSegmentedColormap.from_list('threshold', colors)

    im = ax1.contourf(S, B, Z, levels=20, cmap=cmap)
    cbar = plt.colorbar(im, ax=ax1)
    cbar.set_label('Switching Threshold (τ)', fontsize=11)

    # Add contour lines
    contours = ax1.contour(S, B, Z, levels=[0.3, 0.5, 0.7], colors='white', linewidths=1.5)
    ax1.clabel(contours, inline=True, fontsize=9, fmt='τ=%.1f')

    # Mark trap zone
    ax1.annotate('TRAP ZONE\n(High τ)', xy=(0.1, 0.8), fontsize=11,
                color='white', fontweight='bold', ha='center')
    ax1.annotate('AGILE ZONE\n(Low τ)', xy=(0.35, 0.2), fontsize=11,
                color='white', fontweight='bold', ha='center')

    ax1.set_xlabel('Prior Uncertainty (σ)')
    ax1.set_ylabel('Believer Ratio')
    ax1.set_title('Switching Threshold Landscape\n(μ,σ) → Pivot Threshold (τ)')

    # Right: Belief trajectory example
    ax2 = axes[1]

    # Simulate two trajectories
    config_sim = P2Config(n_periods=15)

    # High commitment (trap)
    trap_prior = Prior(0.8, 0.1)
    trap_cap = CapTable([Investor(InvestorType.BELIEVER, Prior(0.8, 0.1), 0.8)])
    trap_traj = simulate_belief_trajectory(trap_prior, trap_cap, 0.3, config_sim)

    # Low commitment (agile)
    agile_prior = Prior(0.6, 0.3)
    agile_cap = CapTable([Investor(InvestorType.DOUBTER, Prior(0.4, 0.3), 0.6)])
    agile_traj = simulate_belief_trajectory(agile_prior, agile_cap, 0.3, config_sim)

    periods = range(len(trap_traj['mu']))

    # Plot belief means
    ax2.plot(periods, trap_traj['mu'], 'r-', linewidth=2.5, label='High Commitment (Trap)', marker='o', markersize=4)
    ax2.plot(periods, agile_traj['mu'], 'g-', linewidth=2.5, label='Low Commitment (Agile)', marker='s', markersize=4)

    # Plot thresholds as horizontal bands
    trap_threshold = trap_traj['threshold'][0] if trap_traj['threshold'] else 0.7
    agile_threshold = agile_traj['threshold'][0] if agile_traj['threshold'] else 0.3

    ax2.axhline(1 - trap_threshold, color='r', linestyle='--', alpha=0.5, label=f'Trap pivot trigger: {1-trap_threshold:.2f}')
    ax2.axhline(1 - agile_threshold, color='g', linestyle='--', alpha=0.5, label=f'Agile pivot trigger: {1-agile_threshold:.2f}')

    # Mark pivot points
    if agile_traj['pivot_triggered']:
        ax2.axvline(agile_traj['pivot_period'], color='g', linestyle=':', alpha=0.7)
        ax2.annotate('Pivot!', xy=(agile_traj['pivot_period'], 0.3), fontsize=10, color='green')

    ax2.set_xlabel('Time Period')
    ax2.set_ylabel('Belief Mean (μ)')
    ax2.set_title('Belief Trajectory Over Time\n(Evidence: True alternative value = 0.3)')
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 1)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"   Saved: {save_path}")

    return fig


def plot_pivot_threshold_curve(mc_results: pd.DataFrame,
                               save_path: Optional[Path] = None) -> plt.Figure:
    """
    Plot pivot probability vs prior uncertainty (σ) for different believer ratios.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left: Pivot probability curves by believer ratio
    ax1 = axes[0]

    believer_levels = [0.2, 0.5, 0.8]
    colors = ['#27ae60', '#f1c40f', '#e74c3c']
    labels = ['Low believers (20%)', 'Medium believers (50%)', 'High believers (80%)']

    for br, color, label in zip(believer_levels, colors, labels):
        subset = mc_results[np.abs(mc_results['believer_ratio'] - br) < 0.05]
        subset = subset.groupby('sigma').agg({'pivot_probability': 'mean'}).reset_index()

        ax1.plot(subset['sigma'], subset['pivot_probability'],
                color=color, linewidth=2.5, marker='o', markersize=5, label=label)

    ax1.set_xlabel('Prior Uncertainty (σ)')
    ax1.set_ylabel('Pivot Probability')
    ax1.set_title('H2: Believer Ratio Moderates Pivot Probability\n(Higher σ → Easier to pivot)')
    ax1.legend()
    ax1.set_xlim(0.05, 0.4)
    ax1.set_ylim(0, 1)
    ax1.grid(True, alpha=0.3)

    # Add key insight annotation
    ax1.annotate('Competency Trap:\nLow σ + High believers\n→ Pivot blocked',
                xy=(0.1, 0.2), xytext=(0.2, 0.4),
                fontsize=10, ha='center',
                bbox=dict(boxstyle='round', facecolor='#ffcccc', alpha=0.8),
                arrowprops=dict(arrowstyle='->', color='gray'))

    # Right: Threshold vs σ curve
    ax2 = axes[1]

    threshold_df = analyze_threshold_dynamics()

    for br, color, label in zip(believer_levels, colors, labels):
        subset = threshold_df[threshold_df['believer_ratio'] == br]
        ax2.plot(subset['sigma'], subset['threshold'],
                color=color, linewidth=2.5, label=label)

    ax2.set_xlabel('Prior Uncertainty (σ)')
    ax2.set_ylabel('Switching Threshold (τ)')
    ax2.set_title('Switching Threshold vs Prior Uncertainty\n(Lower σ → Higher barrier to pivot)')
    ax2.legend()
    ax2.set_xlim(0.05, 0.5)
    ax2.set_ylim(0.2, 0.9)
    ax2.grid(True, alpha=0.3)

    # Shade trap zone
    ax2.axhspan(0.6, 0.9, alpha=0.2, color='red', label='Trap zone (τ > 0.6)')

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"   Saved: {save_path}")

    return fig


def plot_case_comparison(case_results: Dict[str, Dict],
                        save_path: Optional[Path] = None) -> plt.Figure:
    """
    Plot Waymo vs Comma.ai case comparison.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    companies = list(case_results.keys())
    colors = ['#e74c3c', '#27ae60']  # Red for Waymo (trapped), Green for Comma (agile)

    # Left: Parameter comparison
    ax1 = axes[0]

    metrics = ['prior_sigma', 'believer_ratio', 'threshold', 'pivot_probability']
    metric_labels = ['Prior σ', 'Believer Ratio', 'Threshold (τ)', 'Pivot Prob.']
    x = np.arange(len(metrics))
    width = 0.35

    waymo_vals = [case_results['Waymo'][m] for m in metrics]
    comma_vals = [case_results['Comma.ai'][m] for m in metrics]

    bars1 = ax1.bar(x - width/2, waymo_vals, width, label='Waymo', color=colors[0], edgecolor='black')
    bars2 = ax1.bar(x + width/2, comma_vals, width, label='Comma.ai', color=colors[1], edgecolor='black')

    ax1.set_ylabel('Value')
    ax1.set_title('Case Comparison: Waymo vs Comma.ai\n(Commitment Structure → Pivot Ability)')
    ax1.set_xticks(x)
    ax1.set_xticklabels(metric_labels)
    ax1.legend()
    ax1.set_ylim(0, 1)
    ax1.grid(True, alpha=0.3, axis='y')

    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax1.annotate(f'{height:.2f}',
                        xy=(bar.get_x() + bar.get_width()/2, height),
                        xytext=(0, 3), textcoords="offset points",
                        ha='center', va='bottom', fontsize=9)

    # Right: Summary diagram
    ax2 = axes[1]
    ax2.axis('off')

    # Draw comparison boxes
    waymo_box = mpatches.FancyBboxPatch((0.05, 0.5), 0.4, 0.4,
                                        boxstyle="round,pad=0.02",
                                        facecolor='#ffcccc', edgecolor='red', linewidth=2)
    comma_box = mpatches.FancyBboxPatch((0.55, 0.5), 0.4, 0.4,
                                        boxstyle="round,pad=0.02",
                                        facecolor='#ccffcc', edgecolor='green', linewidth=2)

    ax2.add_patch(waymo_box)
    ax2.add_patch(comma_box)

    # Waymo text
    ax2.text(0.25, 0.85, 'Waymo', fontsize=14, fontweight='bold', ha='center', color='red')
    ax2.text(0.25, 0.75, f"High commitment", fontsize=10, ha='center')
    ax2.text(0.25, 0.65, f"σ = {case_results['Waymo']['prior_sigma']:.2f} (confident)", fontsize=10, ha='center')
    ax2.text(0.25, 0.55, f"Believers: {case_results['Waymo']['believer_ratio']:.0%}", fontsize=10, ha='center')

    # Comma text
    ax2.text(0.75, 0.85, 'Comma.ai', fontsize=14, fontweight='bold', ha='center', color='green')
    ax2.text(0.75, 0.75, f"Low commitment", fontsize=10, ha='center')
    ax2.text(0.75, 0.65, f"σ = {case_results['Comma.ai']['prior_sigma']:.2f} (uncertain)", fontsize=10, ha='center')
    ax2.text(0.75, 0.55, f"Believers: {case_results['Comma.ai']['believer_ratio']:.0%}", fontsize=10, ha='center')

    # Outcome boxes
    ax2.text(0.25, 0.35, '[X] TRAPPED', fontsize=12, fontweight='bold', ha='center', color='red')
    ax2.text(0.25, 0.25, f"Pivot prob: {case_results['Waymo']['pivot_probability']:.0%}", fontsize=10, ha='center')
    ax2.text(0.25, 0.15, "Geofenced, limited scale", fontsize=9, ha='center', style='italic')

    ax2.text(0.75, 0.35, '[OK] AGILE', fontsize=12, fontweight='bold', ha='center', color='green')
    ax2.text(0.75, 0.25, f"Pivot prob: {case_results['Comma.ai']['pivot_probability']:.0%}", fontsize=10, ha='center')
    ax2.text(0.75, 0.15, "Rapid iteration, wider deployment", fontsize=9, ha='center', style='italic')

    # Arrow showing mechanism
    ax2.annotate('', xy=(0.5, 0.7), xytext=(0.5, 0.3),
                arrowprops=dict(arrowstyle='<->', color='gray', lw=2))
    ax2.text(0.5, 0.5, 'Switching\nThreshold', fontsize=10, ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor='gray'))

    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.set_title('Competency Trap Mechanism\n', fontsize=14, fontweight='bold')

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"   Saved: {save_path}")

    return fig


def generate_all_figures():
    """Generate all P2 figures"""
    print("=" * 70)
    print("P2 Figure Generation - 나대용 🐅")
    print("=" * 70)

    # Run simulations
    print("\n🎲 Running simulations...")
    mc_results = run_monte_carlo_simulation()
    case_results = case_study_waymo_vs_comma()

    # Generate figures
    print("\n🎨 Generating figures...")

    fig1 = plot_belief_lockin_diagram(OUTPUT_DIR / 'P2_belief_lockin_diagram.png')
    fig2 = plot_pivot_threshold_curve(mc_results, OUTPUT_DIR / 'P2_pivot_threshold_curve.png')
    fig3 = plot_case_comparison(case_results, OUTPUT_DIR / 'P2_case_comparison.png')

    print(f"\n✅ All P2 figures saved to: {OUTPUT_DIR}")
    print("\nFiles generated:")
    print("   - P2_belief_lockin_diagram.png")
    print("   - P2_pivot_threshold_curve.png")
    print("   - P2_case_comparison.png")

    return [fig1, fig2, fig3]


if __name__ == "__main__":
    figures = generate_all_figures()
    plt.show()
