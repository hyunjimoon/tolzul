"""
F-Series Plotting Suite for Two-Snapshot Analysis (HEV/HLVF/HSF)

Unified Terminology:
- HEV: E ~ V + controls (OLS) - Early event ~ Vagueness
- HLVF: L ~ V × F + controls (Logit) - Later success ~ Vagueness × Flexibility
  CRITICAL: NO early_funding control (E is mediator, not confounder)
- HSF: S ~ V × F + controls (OLS, L==1 only) - Step-up ~ Vagueness × Flexibility

Reference: W2 slides p.49 "Early Funding: Mediator or Confounder?"

Color Palette (W2 Convention - EXACT):
- E (Early event): red - information value, short-term survival
- L (Later success): #0000FF (pure blue) - information + option value, long-term
- V (Vagueness): green - promise as founder's choice
- S (Step-up): purple
- F (Flexibility): skyblue - exercisability, flexibility
- C (Serial founder): orange
- HW (Hardware/Rigid): gray
- doubt (Angie's doubt): pink

Interaction Line Styles:
- L | F=1 (flexible/software): skyblue, solid, ↑ slope
- L | F=0 (hardware/rigid): gray, dashed, ↓/flat slope
- L | C=1 (serial): orange, dash-dot
- L | C=0 (first-time): orange, dotted

Axis Coloring Rules:
- X-axis with V: green labels/ticks/spine
- Y-axis with L probability: blue labels
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Optional, Dict
from statsmodels.regression.linear_model import RegressionResultsWrapper
from statsmodels.discrete.discrete_model import BinaryResultsWrapper

# =============================================================================
# GLOBAL CONFIGURATION
# =============================================================================

# Strict color palette (W2 convention - EXACT specification)
PALETTE = {
    "E": "red",          # Early funding (information value, short-term survival)
    "L": "#0000FF",      # Later success (blue - information + option value, long-term)
    "V": "green",        # Vagueness (promise as founder's choice)
    "F": "skyblue",      # Flexibility/Exercisability (option exercisability)
    "S": "purple",       # Step-up
    "C": "orange",       # Controls/Cohort/Serial founder
    "HW": "gray",        # Hardware/Rigid (F=0)
    "doubt": "pink"      # Angie's doubt (for annotations)
}

# Standard figure settings
FIGURE_DPI = 300
FIGURE_FORMATS = ['png', 'pdf']  # Save both formats
TITLE_FONTSIZE = 16
LABEL_FONTSIZE = 13
LEGEND_FONTSIZE = 10

# Line styles for interactions
LINE_STYLES = {
    'F=1': {'color': PALETTE['F'], 'linestyle': '-', 'linewidth': 2.5},   # Flexible/SW: skyblue, solid
    'F=0': {'color': PALETTE['HW'], 'linestyle': '--', 'linewidth': 2.5}, # Rigid/HW: gray, dashed
    'C=1': {'color': PALETTE['C'], 'linestyle': '-.', 'linewidth': 2.5},  # Serial: orange, dash-dot
    'C=0': {'color': PALETTE['C'], 'linestyle': ':', 'linewidth': 2.5},   # First-time: orange, dotted
}


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def median_or_mode(series: pd.Series):
    """
    Return median for numeric, mode (majority) for discrete/binary.

    Args:
        series: Pandas Series

    Returns:
        Median for numeric, most frequent value for categorical
    """
    if series.dtype in ['object', 'category', 'bool']:
        mode_vals = series.mode()
        return mode_vals[0] if len(mode_vals) > 0 else None
    else:
        return series.median()


def fix_controls_at_medianmode(df: pd.DataFrame, cols: list) -> dict:
    """
    Fix control variables and other moderators at median/mode.

    Args:
        df: DataFrame with data
        cols: List of column names to fix

    Returns:
        Dictionary with fixed values
    """
    fixed = {}
    for col in cols:
        if col not in df.columns:
            continue
        fixed[col] = median_or_mode(df[col].dropna())
    return fixed


def color_axis_for_var(ax: plt.Axes, xvar: Optional[str] = None, yvar: Optional[str] = None):
    """
    Color axis labels/ticks/spines according to variable type.

    Rules:
    - x=V: green axis
    - y=L probability: blue axis

    Args:
        ax: Matplotlib axes
        xvar: X variable name ('V', 'z_V', etc.)
        yvar: Y variable name ('L', 'Pr(L)', etc.)
    """
    # X-axis coloring
    if xvar and ('V' in xvar or 'vagueness' in xvar.lower()):
        ax.xaxis.label.set_color(PALETTE['V'])
        ax.tick_params(axis='x', colors=PALETTE['V'])
        ax.spines['bottom'].set_color(PALETTE['V'])

    # Y-axis coloring
    if yvar and ('L' in yvar or 'later' in yvar.lower() or 'Pr' in yvar):
        ax.yaxis.label.set_color(PALETTE['L'])
        ax.tick_params(axis='y', colors=PALETTE['L'])
        ax.spines['left'].set_color(PALETTE['L'])


def save_figure(fig: plt.Figure, outdir: Path, filename_base: str) -> Dict[str, Path]:
    """
    Save figure in multiple formats (PNG + PDF).

    Args:
        fig: Matplotlib figure
        outdir: Output directory
        filename_base: Base filename (without extension)

    Returns:
        Dictionary mapping format to Path
    """
    outdir.mkdir(parents=True, exist_ok=True)
    paths = {}

    for fmt in FIGURE_FORMATS:
        path = outdir / f"{filename_base}.{fmt}"
        fig.savefig(path, dpi=FIGURE_DPI, bbox_inches='tight', format=fmt)
        paths[fmt] = path
        print(f"  ✓ Saved: {path}")

    return paths


# =============================================================================
# F1: E vs V (HEV)
# =============================================================================

def fig_F1_E_vs_V(df: pd.DataFrame, hev: RegressionResultsWrapper, outdir: Path) -> Dict[str, Path]:
    """
    F1: E vs V scatter with HEV OLS fit.

    Model: HEV (E ~ V + controls)

    Args:
        df: DataFrame with E, z_V
        hev: OLS model from run_HEV
        outdir: Output directory

    Returns:
        Dictionary of saved file paths
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Determine E column
    E_col = 'E_scaled' if 'E_scaled' in df.columns else 'E'
    V_col = 'z_V'

    # Scatter plot
    df_plot = df.dropna(subset=[E_col, V_col])
    ax.scatter(df_plot[V_col], df_plot[E_col],
               alpha=0.3, s=20, color=PALETTE['E'],
               edgecolors='k', linewidths=0.2)

    # OLS fit line
    V_range = np.linspace(df_plot[V_col].min(), df_plot[V_col].max(), 100)
    pred_df = pd.DataFrame({V_col: V_range})

    # Fix controls at median/mode
    control_cols = ['founding_cohort', 'region']
    fixed = fix_controls_at_medianmode(df_plot, control_cols)
    for k, v in fixed.items():
        if v is not None:
            pred_df[k] = v

    try:
        predictions = hev.predict(pred_df)
        ax.plot(V_range, predictions, color=PALETTE['E'], linewidth=3, label='HEV fit')
    except Exception as e:
        print(f"  ⚠️ Could not plot F1 fit line: {e}")

    # Labels and title
    ax.set_xlabel('V (Vagueness, z-score)', fontsize=LABEL_FONTSIZE, fontweight='bold')
    ax.set_ylabel('E (Early Event)', fontsize=LABEL_FONTSIZE, fontweight='bold')
    ax.set_title('F1. HEV: E vs V', fontsize=TITLE_FONTSIZE, fontweight='bold')

    # Color axes
    color_axis_for_var(ax, xvar='V', yvar=None)

    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(loc='best', fontsize=LEGEND_FONTSIZE)

    # Caption
    ax.text(0.98, 0.02, 'Controls fixed at median/mode',
            transform=ax.transAxes, fontsize=8,
            ha='right', va='bottom', style='italic', color='gray')

    plt.tight_layout()

    # Save
    paths = save_figure(fig, outdir, 'F1_E_vs_V')
    plt.close(fig)

    return paths


# =============================================================================
# F1b: E | F (V×F Interaction for Early Funding)
# =============================================================================

def fig_F1b_E_given_F(df: pd.DataFrame, hev_interaction: RegressionResultsWrapper, outdir: Path) -> Dict[str, Path]:
    """
    F1b: E | F conditional curves (V×F interaction for early funding).

    Model: E ~ V × F + controls (OLS with interaction)
    Shows: F=1 (skyblue, solid), F=0 (gray, dashed)

    Args:
        df: DataFrame with E, z_V, F_flexibility
        hev_interaction: OLS model with E ~ z_V * F_flexibility + controls
        outdir: Output directory

    Returns:
        Dictionary of saved file paths
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Determine E column
    E_col = 'E_scaled' if 'E_scaled' in df.columns else 'E'
    V_col = 'z_V'
    df_plot = df.dropna(subset=[E_col, V_col, 'F_flexibility'])

    # V range
    V_range = np.linspace(df_plot[V_col].min(), df_plot[V_col].max(), 100)

    # Fix other controls at median/mode
    control_cols = ['founding_cohort', 'region']
    fixed = fix_controls_at_medianmode(df_plot, control_cols)

    # Plot F=0 (Hardware/Rigid, dashed)
    pred_df_0 = pd.DataFrame({V_col: V_range, 'F_flexibility': 0})
    for k, v in fixed.items():
        if v is not None:
            pred_df_0[k] = v

    try:
        pred_0 = hev_interaction.predict(pred_df_0)
        ax.plot(V_range, pred_0,
                label='E | F=0 (rigid/hardware)',
                color=PALETTE['HW'], linestyle='--', linewidth=2.5)
    except Exception as e:
        print(f"  ⚠️ Could not plot F1b F=0 line: {e}")

    # Plot F=1 (Software/Flexible, solid)
    pred_df_1 = pd.DataFrame({V_col: V_range, 'F_flexibility': 1})
    for k, v in fixed.items():
        if v is not None:
            pred_df_1[k] = v

    try:
        pred_1 = hev_interaction.predict(pred_df_1)
        ax.plot(V_range, pred_1,
                label='E | F=1 (flexible/software)',
                color=PALETTE['F'], linestyle='-', linewidth=2.5)
    except Exception as e:
        print(f"  ⚠️ Could not plot F1b F=1 line: {e}")

    # Labels and title
    ax.set_xlabel('V (Vagueness, z-score)', fontsize=LABEL_FONTSIZE, fontweight='bold', color=PALETTE['V'])
    ax.set_ylabel('E (Early Funding Amount)', fontsize=LABEL_FONTSIZE, fontweight='bold', color=PALETTE['E'])
    ax.set_title('F1b. EVF: E | F (V×F Interaction)', fontsize=TITLE_FONTSIZE, fontweight='bold')

    # Legend with fixed anchor
    ax.legend(loc='upper left', fontsize=LEGEND_FONTSIZE, framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle='--')

    # Caption
    caption = 'Controls fixed at median/mode\nE = Early funding amount (continuous)'
    ax.text(0.98, 0.02, caption,
            transform=ax.transAxes, fontsize=8,
            ha='right', va='bottom', style='italic', color='gray')

    plt.tight_layout()

    # Save
    paths = save_figure(fig, outdir, 'F1b_E_given_F')
    plt.close(fig)

    return paths


# =============================================================================
# F2: Pr(L) vs V (HLVF)
# =============================================================================

def fig_F2_PrL_vs_V(df: pd.DataFrame, hlvf: BinaryResultsWrapper, outdir: Path) -> Dict[str, Path]:
    """
    F2: Predicted Pr(L=1) vs V using HLVF.

    Model: HLVF (L ~ V × F, NO E)
    CRITICAL: E omitted by design (mediator, not control)

    Args:
        df: DataFrame with L, z_V, F_flexibility
        hlvf: Logit model from run_HLVF
        outdir: Output directory

    Returns:
        Dictionary of saved file paths
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    V_col = 'z_V'
    df_plot = df.dropna(subset=['L', V_col, 'F_flexibility'])

    # V range
    V_range = np.linspace(df_plot[V_col].min(), df_plot[V_col].max(), 100)
    pred_df = pd.DataFrame({V_col: V_range})

    # Fix F at median/mode (majority)
    F_fixed = median_or_mode(df_plot['F_flexibility'])
    pred_df['F_flexibility'] = F_fixed

    # Fix other controls
    control_cols = ['founding_cohort', 'region', 'founder_serial']
    fixed = fix_controls_at_medianmode(df_plot, control_cols)
    for k, v in fixed.items():
        if v is not None:
            pred_df[k] = v

    try:
        predictions = hlvf.predict(pred_df)
        ax.plot(V_range, predictions, color=PALETTE['L'], linewidth=3)
    except Exception as e:
        print(f"  ⚠️ Could not plot F2 predictions: {e}")

    # Labels and title
    ax.set_xlabel('V (Vagueness, z-score)', fontsize=LABEL_FONTSIZE, fontweight='bold')
    ax.set_ylabel('Pr(L = 1)', fontsize=LABEL_FONTSIZE, fontweight='bold')
    ax.set_title('F2. HLVF: Pr(L) vs V', fontsize=TITLE_FONTSIZE, fontweight='bold')
    ax.set_ylim([0, 1])

    # Color axes
    color_axis_for_var(ax, xvar='V', yvar='L')

    ax.grid(True, alpha=0.3, linestyle='--')

    # Caption with NO-E principle
    caption = f'F at median ({F_fixed:.1f}); controls at median/mode\nE omitted by design: mediator, not control'
    ax.text(0.98, 0.02, caption,
            transform=ax.transAxes, fontsize=8,
            ha='right', va='bottom', style='italic', color='gray')

    plt.tight_layout()

    # Save
    paths = save_figure(fig, outdir, 'F2_PrL_vs_V')
    plt.close(fig)

    return paths


# =============================================================================
# F3a: L | F (V×F Interaction from HLVF)
# =============================================================================

def fig_F3a_L_given_F(df: pd.DataFrame, hlvf: BinaryResultsWrapper, outdir: Path) -> Dict[str, Path]:
    """
    F3a: L | F conditional curves (V×F interaction).

    Model: HLVF (L ~ V × F, NO E)
    Shows: F=1 (skyblue, solid, ↑), F=0 (skyblue, dashed, ↓/flat)

    Args:
        df: DataFrame with L, z_V, F_flexibility
        hlvf: Logit model from run_HLVF
        outdir: Output directory

    Returns:
        Dictionary of saved file paths
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    V_col = 'z_V'
    df_plot = df.dropna(subset=['L', V_col, 'F_flexibility'])

    # V range
    V_range = np.linspace(df_plot[V_col].min(), df_plot[V_col].max(), 100)

    # Fix other moderator (C) and controls at median/mode
    control_cols = ['founding_cohort', 'region', 'founder_serial']
    fixed = fix_controls_at_medianmode(df_plot, control_cols)

    # Plot F=0 (Hardware, dashed, downward/flat)
    pred_df_0 = pd.DataFrame({V_col: V_range, 'F_flexibility': 0})
    for k, v in fixed.items():
        if v is not None:
            pred_df_0[k] = v

    try:
        pred_0 = hlvf.predict(pred_df_0)
        ax.plot(V_range, pred_0,
                label='L | F=0 (hardware)',
                **LINE_STYLES['F=0'])
    except Exception as e:
        print(f"  ⚠️ Could not plot F3a F=0 line: {e}")

    # Plot F=1 (Software/Flexible, solid, upward)
    pred_df_1 = pd.DataFrame({V_col: V_range, 'F_flexibility': 1})
    for k, v in fixed.items():
        if v is not None:
            pred_df_1[k] = v

    try:
        pred_1 = hlvf.predict(pred_df_1)
        ax.plot(V_range, pred_1,
                label='L | F=1 (flexible/software)',
                **LINE_STYLES['F=1'])
    except Exception as e:
        print(f"  ⚠️ Could not plot F3a F=1 line: {e}")

    # Labels and title
    ax.set_xlabel('V (Vagueness, z-score)', fontsize=LABEL_FONTSIZE, fontweight='bold')
    ax.set_ylabel('Pr(L = 1)', fontsize=LABEL_FONTSIZE, fontweight='bold')
    ax.set_title('F3a. HLVF: L | F (V×F Interaction)', fontsize=TITLE_FONTSIZE, fontweight='bold')
    ax.set_ylim([0, 1])

    # Color axes
    color_axis_for_var(ax, xvar='V', yvar='L')

    # Legend with fixed anchor
    ax.legend(loc='upper left', fontsize=LEGEND_FONTSIZE, framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle='--')

    # Caption
    caption = 'Other moderator (C) + controls fixed at median/mode\nE omitted: mediator, not control'
    ax.text(0.98, 0.02, caption,
            transform=ax.transAxes, fontsize=8,
            ha='right', va='bottom', style='italic', color='gray')

    plt.tight_layout()

    # Save
    paths = save_figure(fig, outdir, 'F3a_L_given_F')
    plt.close(fig)

    return paths


# =============================================================================
# F3b: L | C (V×C Interaction)
# =============================================================================

def fig_F3b_L_given_C(df: pd.DataFrame, h4: BinaryResultsWrapper, outdir: Path) -> Dict[str, Path]:
    """
    F3b: L | C conditional curves (V×C interaction).

    Shows: C=1 (orange, dash-dot), C=0 (orange, dotted)

    Args:
        df: DataFrame with growth/L, z_V/z_vagueness, founder_serial
        h4: Logit model from test_h4_growth_interaction
        outdir: Output directory

    Returns:
        Dictionary of saved file paths
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Detect V column from model's formula (critical for prediction)
    model_formula = str(h4.model.formula) if hasattr(h4.model, 'formula') else ''
    if 'z_vagueness' in model_formula:
        V_col = 'z_vagueness'
    elif 'z_V' in model_formula or 'z_V' in df.columns:
        V_col = 'z_V'
    else:
        V_col = 'z_vagueness'  # Fallback

    # Verify column exists
    if V_col not in df.columns:
        print(f"  ⚠️ Warning: {V_col} not in DataFrame, trying alternate...")
        V_col = 'z_V' if 'z_V' in df.columns else 'z_vagueness'

    df_plot = df.dropna(subset=['growth', V_col, 'founder_serial'])

    # V range
    V_range = np.linspace(df_plot[V_col].min(), df_plot[V_col].max(), 100)

    # Fix F and controls at median/mode
    control_cols = ['F_flexibility', 'founding_cohort', 'z_employees_log']
    fixed = fix_controls_at_medianmode(df_plot, control_cols)

    # Plot C=0 (First-time, dotted)
    pred_df_0 = pd.DataFrame({V_col: V_range, 'founder_serial': 0})
    for k, v in fixed.items():
        if v is not None:
            pred_df_0[k] = v

    try:
        pred_0 = h4.predict(pred_df_0)
        ax.plot(V_range, pred_0,
                label='L | C=0 (first-time founder)',
                **LINE_STYLES['C=0'])
    except Exception as e:
        print(f"  ⚠️ Could not plot F3b C=0 line: {e}")

    # Plot C=1 (Serial, dash-dot)
    pred_df_1 = pd.DataFrame({V_col: V_range, 'founder_serial': 1})
    for k, v in fixed.items():
        if v is not None:
            pred_df_1[k] = v

    try:
        pred_1 = h4.predict(pred_df_1)
        ax.plot(V_range, pred_1,
                label='L | C=1 (serial founder)',
                **LINE_STYLES['C=1'])
    except Exception as e:
        print(f"  ⚠️ Could not plot F3b C=1 line: {e}")

    # Labels and title
    ax.set_xlabel('V (Vagueness, z-score)', fontsize=LABEL_FONTSIZE, fontweight='bold')
    ax.set_ylabel('Pr(Growth = 1)', fontsize=LABEL_FONTSIZE, fontweight='bold')
    ax.set_title('F3b. L | C (V×C Interaction)', fontsize=TITLE_FONTSIZE, fontweight='bold')
    ax.set_ylim([0, 1])

    # Color axes
    color_axis_for_var(ax, xvar='V', yvar='L')

    # Legend with fixed anchor
    ax.legend(loc='upper left', fontsize=LEGEND_FONTSIZE, framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle='--')

    # Caption
    caption = 'F + controls fixed at median/mode'
    ax.text(0.98, 0.02, caption,
            transform=ax.transAxes, fontsize=8,
            ha='right', va='bottom', style='italic', color='gray')

    plt.tight_layout()

    # Save
    paths = save_figure(fig, outdir, 'F3b_L_given_C')
    plt.close(fig)

    return paths


# =============================================================================
# F4: Distributions (5 separate 1×1 figures)
# =============================================================================

def fig_F4_E_dist(df: pd.DataFrame, outdir: Path) -> Dict[str, Path]:
    """F4-E: Distribution of E (Early event)."""
    fig, ax = plt.subplots(figsize=(8, 5))

    E_col = 'E_scaled' if 'E_scaled' in df.columns else 'E'
    data = df[E_col].dropna()

    if len(data) == 0:
        ax.text(0.5, 0.5, 'No data available for E',
                ha='center', va='center', transform=ax.transAxes, fontsize=12)
    elif data.nunique() <= 2:
        # Binary
        counts = data.value_counts().sort_index()
        ax.bar(range(len(counts)), counts.values, color=PALETTE['E'], edgecolor='black', alpha=0.7, width=0.6)
        ax.set_xticks(range(len(counts)))
        ax.set_xticklabels([f'{int(v)}' for v in counts.index])
        ax.set_ylabel('Count', fontweight='bold')
    else:
        # Continuous
        ax.hist(data, bins=30, color=PALETTE['E'], edgecolor='black', alpha=0.7)
        ax.set_ylabel('Count', fontweight='bold')

    ax.set_xlabel('E (Early Event)', fontsize=LABEL_FONTSIZE, fontweight='bold', color=PALETTE['E'])
    ax.set_title(f'F4-E. E Distribution (n={len(data):,})', fontsize=TITLE_FONTSIZE, fontweight='bold')
    ax.tick_params(axis='x', colors=PALETTE['E'])
    ax.grid(True, alpha=0.3, axis='y', linestyle='--')

    plt.tight_layout()
    paths = save_figure(fig, outdir, 'F4_E_dist')
    plt.close(fig)
    return paths


def fig_F4_L24_dist(df: pd.DataFrame, outdir: Path) -> Dict[str, Path]:
    """F4-L24: Distribution of L_2024."""
    fig, ax = plt.subplots(figsize=(8, 5))

    L_col = 'L_2024' if 'L_2024' in df.columns else 'L'
    if L_col not in df.columns or df[L_col].isna().all():
        ax.text(0.5, 0.5, 'No data available for L_2024',
                ha='center', va='center', transform=ax.transAxes, fontsize=12)
    else:
        data = df[L_col].dropna()
        counts = data.value_counts().sort_index()
        ax.bar(range(len(counts)), counts.values, color=PALETTE['L'], edgecolor='black', alpha=0.7, width=0.6)
        ax.set_xticks(range(len(counts)))
        ax.set_xticklabels([f'{int(v)}' for v in counts.index])
        ax.set_ylabel('Count', fontweight='bold')
        ax.set_title(f'F4-L24. L_2024 Distribution (n={len(data):,})', fontsize=TITLE_FONTSIZE, fontweight='bold')

    ax.set_xlabel('L_2024', fontsize=LABEL_FONTSIZE, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y', linestyle='--')

    plt.tight_layout()
    paths = save_figure(fig, outdir, 'F4_L24_dist')
    plt.close(fig)
    return paths


def fig_F4_L25_dist(df: pd.DataFrame, outdir: Path) -> Dict[str, Path]:
    """F4-L25: Distribution of L_2025."""
    fig, ax = plt.subplots(figsize=(8, 5))

    L_col = 'L_2025' if 'L_2025' in df.columns else 'L'
    if L_col not in df.columns or df[L_col].isna().all():
        ax.text(0.5, 0.5, 'No data available for L_2025',
                ha='center', va='center', transform=ax.transAxes, fontsize=12)
    else:
        data = df[L_col].dropna()
        counts = data.value_counts().sort_index()
        ax.bar(range(len(counts)), counts.values, color=PALETTE['L'], edgecolor='black', alpha=0.7, width=0.6)
        ax.set_xticks(range(len(counts)))
        ax.set_xticklabels([f'{int(v)}' for v in counts.index])
        ax.set_ylabel('Count', fontweight='bold')
        ax.set_title(f'F4-L25. L_2025 Distribution (n={len(data):,})', fontsize=TITLE_FONTSIZE, fontweight='bold')

    ax.set_xlabel('L_2025', fontsize=LABEL_FONTSIZE, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y', linestyle='--')

    plt.tight_layout()
    paths = save_figure(fig, outdir, 'F4_L25_dist')
    plt.close(fig)
    return paths


def fig_F4_V_dist(df: pd.DataFrame, outdir: Path) -> Dict[str, Path]:
    """F4-V: Distribution of V (Vagueness)."""
    fig, ax = plt.subplots(figsize=(8, 5))

    V_col = 'z_V' if 'z_V' in df.columns else 'V'
    data = df[V_col].dropna()

    if len(data) == 0:
        ax.text(0.5, 0.5, 'No data available for V',
                ha='center', va='center', transform=ax.transAxes, fontsize=12)
    else:
        ax.hist(data, bins=30, color=PALETTE['V'], edgecolor='black', alpha=0.7)
        ax.set_ylabel('Count', fontweight='bold')
        ax.set_title(f'F4-V. V Distribution (n={len(data):,})', fontsize=TITLE_FONTSIZE, fontweight='bold')

    ax.set_xlabel('V (Vagueness, z-score)', fontsize=LABEL_FONTSIZE, fontweight='bold', color=PALETTE['V'])
    ax.tick_params(axis='x', colors=PALETTE['V'])
    ax.grid(True, alpha=0.3, linestyle='--')

    plt.tight_layout()
    paths = save_figure(fig, outdir, 'F4_V_dist')
    plt.close(fig)
    return paths


def fig_F4_F_dist(df: pd.DataFrame, outdir: Path) -> Dict[str, Path]:
    """F4-F: Distribution of F (Flexibility)."""
    fig, ax = plt.subplots(figsize=(8, 5))

    F_col = 'F_flexibility'
    if F_col not in df.columns or df[F_col].isna().all():
        ax.text(0.5, 0.5, 'No data available for F',
                ha='center', va='center', transform=ax.transAxes, fontsize=12)
    else:
        data = df[F_col].dropna()
        counts = data.value_counts().sort_index()
        ax.bar(range(len(counts)), counts.values, color=PALETTE['F'], edgecolor='black', alpha=0.7, width=0.6)
        ax.set_xticks(range(len(counts)))
        ax.set_xticklabels(['Hardware (0)', 'Software (1)'] if len(counts) == 2 else [f'{int(v)}' for v in counts.index])
        ax.set_ylabel('Count', fontweight='bold')
        ax.set_title(f'F4-F. F Distribution (n={len(data):,})', fontsize=TITLE_FONTSIZE, fontweight='bold')

    ax.set_xlabel('F (Flexibility)', fontsize=LABEL_FONTSIZE, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y', linestyle='--')

    plt.tight_layout()
    paths = save_figure(fig, outdir, 'F4_F_dist')
    plt.close(fig)
    return paths


# =============================================================================
# F5: Step-up by F (HSF, Survivors Only)
# =============================================================================

def fig_F5_stepup_by_F(df: pd.DataFrame, outdir: Path) -> Dict[str, Path]:
    """
    F5: Step-up by F (survivors only, HSF analysis).

    Model: HSF (S ~ V × F, L==1 only)

    Args:
        df: DataFrame with S_stepup_log, F_flexibility, L
        outdir: Output directory

    Returns:
        Dictionary of saved file paths
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    # Filter to survivors
    L_col = 'L_2025' if 'L_2025' in df.columns else ('L' if 'L' in df.columns else None)

    if L_col is None:
        ax.text(0.5, 0.5, 'No L column available',
                ha='center', va='center', transform=ax.transAxes, fontsize=12)
    else:
        df_surv = df[df[L_col] == 1].copy()
        df_plot = df_surv.dropna(subset=['S_stepup_log', 'F_flexibility'])

        if len(df_plot) < 5:
            ax.text(0.5, 0.5, f'Insufficient survivor data (n={len(df_plot)})',
                    ha='center', va='center', transform=ax.transAxes, fontsize=12)
        else:
            # Boxplot by F
            groups = []
            labels = []
            for f_val in sorted(df_plot['F_flexibility'].unique()):
                subset = df_plot[df_plot['F_flexibility'] == f_val]['S_stepup_log']
                groups.append(subset)
                label = 'Software (F=1)' if f_val == 1 else 'Hardware (F=0)'
                labels.append(f'{label}\n(n={len(subset)})')

            bp = ax.boxplot(groups, labels=labels, patch_artist=True, widths=0.6)
            for patch in bp['boxes']:
                patch.set_facecolor(PALETTE['S'])
                patch.set_alpha(0.7)

            ax.set_ylabel('S (Step-up, log)', fontsize=LABEL_FONTSIZE, fontweight='bold', color=PALETTE['S'])
            ax.set_title(f'F5. HSF: Step-up by F (Survivors, n={len(df_plot):,})',
                         fontsize=TITLE_FONTSIZE, fontweight='bold')
            ax.tick_params(axis='y', colors=PALETTE['S'])

    ax.grid(True, alpha=0.3, axis='y', linestyle='--')

    # Caption
    ax.text(0.98, 0.02, 'L==1 (survivors) only',
            transform=ax.transAxes, fontsize=8,
            ha='right', va='bottom', style='italic', color='gray')

    plt.tight_layout()
    paths = save_figure(fig, outdir, 'F5_stepup_by_F')
    plt.close(fig)
    return paths


# =============================================================================
# F6: Specification Curve (Multiverse)
# =============================================================================

def fig_F6_spec_curve(spec_df: pd.DataFrame, outdir: Path) -> Dict[str, Path]:
    """
    F6: Specification curve showing coefficients across model variants.

    Color coding:
    - Expected & significant: green
    - Unexpected & significant: red
    - Not significant: gray

    Args:
        spec_df: DataFrame with columns: coefficient, pvalue, term
        outdir: Output directory

    Returns:
        Dictionary of saved file paths
    """
    fig, ax = plt.subplots(figsize=(14, 6))

    # Determine column names
    coef_col = 'coefficient' if 'coefficient' in spec_df.columns else 'coef_vagueness'
    pval_col = 'pvalue' if 'pvalue' in spec_df.columns else 'p_vagueness'

    if coef_col not in spec_df.columns:
        ax.text(0.5, 0.5, 'No coefficient column found',
                ha='center', va='center', transform=ax.transAxes, fontsize=12)
    else:
        df_plot = spec_df.copy()

        # Sort by coefficient
        df_plot = df_plot.sort_values(coef_col).reset_index(drop=True)
        x = np.arange(len(df_plot))

        # Color by term and significance
        colors = []
        for idx, row in df_plot.iterrows():
            term = str(row.get('term', ''))
            pval = row.get(pval_col, 1.0)

            # Determine color
            if 'VxF' in term or ('V' in term and 'F' in term):
                colors.append(PALETTE['F'])  # V×F interaction
            elif 'VxC' in term or ('V' in term and 'C' in term):
                colors.append(PALETTE['C'])  # V×C interaction
            elif 'V' in term:
                colors.append(PALETTE['V'])  # V main effect
            else:
                colors.append('gray')

        # Plot coefficients
        ax.scatter(x, df_plot[coef_col], c=colors, s=40, alpha=0.7,
                  edgecolors='black', linewidths=0.5, zorder=3)

        # Add horizontal line at 0
        ax.axhline(0, color='black', linestyle='--', linewidth=1, alpha=0.5, zorder=2)

        # Add confidence bands if available
        if 'std_error' in df_plot.columns:
            ax.errorbar(x, df_plot[coef_col], yerr=1.96 * df_plot['std_error'],
                       fmt='none', alpha=0.2, color='gray', zorder=1)

        ax.set_xlabel('Specification Index (sorted by coefficient)',
                     fontsize=LABEL_FONTSIZE, fontweight='bold')
        ax.set_ylabel('Coefficient Estimate', fontsize=LABEL_FONTSIZE, fontweight='bold')
        ax.set_title(f'F6. Specification Curve (n={len(df_plot)} variants)',
                    fontsize=TITLE_FONTSIZE, fontweight='bold')
        ax.grid(True, alpha=0.3, linestyle='--')

        # Legend
        if 'term' in df_plot.columns:
            from matplotlib.patches import Patch
            legend_elements = [
                Patch(facecolor=PALETTE['V'], label='V (main effect)'),
                Patch(facecolor=PALETTE['F'], label='V×F (interaction)'),
                Patch(facecolor=PALETTE['C'], label='V×C (interaction)')
            ]
            ax.legend(handles=legend_elements, loc='upper left', fontsize=LEGEND_FONTSIZE, framealpha=0.9)

    plt.tight_layout()
    paths = save_figure(fig, outdir, 'F6_spec_curve')
    plt.close(fig)
    return paths


# =============================================================================
# ORCHESTRATOR: Create All F-Series Figures
# =============================================================================

def create_F_series(df: pd.DataFrame, results: dict, outdir: Path) -> Dict[str, Dict[str, Path]]:
    """
    Create all F-series plots (F1-F6) with HEV/HLVF/HSF terminology.

    Args:
        df: DataFrame with analysis data
        results: Dictionary with keys:
            - 'HEV' or 'hev': OLS from models.run_HEV(...)
            - 'HEV_interaction' or 'hev_interaction': OLS with V×F for EVF plot
            - 'HLVF' or 'hlvf': Logit from models.run_HLVF(...)
            - 'h4': Logit from models.test_h4_growth_interaction(...)
            - 'HSF' or 'hsf': (optional) OLS from models.run_HSF(...)
            - 'spec_df': DataFrame for spec curve
        outdir: Output directory (will create outputs/figures/)

    Returns:
        Nested dictionary: {figure_name: {format: Path}}
        Example: {'F1': {'png': Path('...'), 'pdf': Path('...')}, ...}
    """
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    print("\n" + "="*80)
    print("CREATING F-SERIES PLOTS (HEV/HLVF/HSF)")
    print("="*80)
    print("Reference: W2 slides - ELSVF palette & interaction conventions")
    print("CRITICAL: HLVF has NO early_funding control (E is mediator)")
    print("="*80)

    all_paths = {}

    # Normalize keys (handle both HEV and hev)
    def get_model(key_variants):
        for key in key_variants:
            if key in results and results[key] is not None:
                return results[key]
        return None

    hev = get_model(['HEV', 'hev'])
    hlvf = get_model(['HLVF', 'hlvf'])
    h4 = get_model(['h4', 'H4'])
    hsf = get_model(['HSF', 'hsf'])
    spec_df = results.get('spec_df')

    # F1: E vs V
    if hev is not None:
        print("\nF1: E vs V (HEV)...")
        all_paths['F1'] = fig_F1_E_vs_V(df, hev, outdir)
    else:
        print("\n⚠️  Skipping F1: HEV model not provided")

    # F1b: E | F (V×F interaction for early funding)
    hev_interaction = get_model(['HEV_interaction', 'hev_interaction'])
    if hev_interaction is not None:
        print("\nF1b: E | F (V×F interaction)...")
        all_paths['F1b'] = fig_F1b_E_given_F(df, hev_interaction, outdir)
    else:
        print("\n⚠️  Skipping F1b: HEV interaction model not provided")

    # F2: Pr(L) vs V
    if hlvf is not None:
        print("\nF2: Pr(L) vs V (HLVF, NO E)...")
        all_paths['F2'] = fig_F2_PrL_vs_V(df, hlvf, outdir)
    else:
        print("\n⚠️  Skipping F2: HLVF model not provided")

    # F3a: L|F
    if hlvf is not None:
        print("\nF3a: L | F (V×F from HLVF)...")
        all_paths['F3a'] = fig_F3a_L_given_F(df, hlvf, outdir)
    else:
        print("\n⚠️  Skipping F3a: HLVF model not provided")

    # F3b: L|C
    if h4 is not None:
        print("\nF3b: L | C (V×C)...")
        all_paths['F3b'] = fig_F3b_L_given_C(df, h4, outdir)
    else:
        print("\n⚠️  Skipping F3b: h4 model not provided")

    # F4: Distributions (5 separate figures)
    print("\nF4: Variable distributions (5 figures)...")
    all_paths['F4_E'] = fig_F4_E_dist(df, outdir)
    all_paths['F4_L24'] = fig_F4_L24_dist(df, outdir)
    all_paths['F4_L25'] = fig_F4_L25_dist(df, outdir)
    all_paths['F4_V'] = fig_F4_V_dist(df, outdir)
    all_paths['F4_F'] = fig_F4_F_dist(df, outdir)

    # F5: Step-up by F
    print("\nF5: Step-up by F (HSF, survivors)...")
    all_paths['F5'] = fig_F5_stepup_by_F(df, outdir)

    # F6: Spec curve
    if spec_df is not None and len(spec_df) > 0:
        print("\nF6: Specification curve...")
        all_paths['F6'] = fig_F6_spec_curve(spec_df, outdir)
    else:
        print("\n⚠️  Skipping F6: spec_df not provided")

    print("\n" + "="*80)
    print(f"✓ Created {len(all_paths)} F-series figures")
    print(f"✓ Output directory: {outdir.absolute()}")
    print("="*80)

    # Summary
    total_files = sum(len(paths) for paths in all_paths.values())
    print(f"\nTotal files: {total_files} ({len(FIGURE_FORMATS)} formats × {len(all_paths)} figures)")
    print("\nFigure inventory:")
    for fig_name in sorted(all_paths.keys()):
        formats = ', '.join(all_paths[fig_name].keys())
        print(f"  • {fig_name}: {formats}")

    return all_paths


# =============================================================================
# BACKWARD COMPATIBILITY ALIASES
# =============================================================================

# Allow old function names to map to new ones
fig_F1_E_vs_V.__doc__ += "\n\nAlias: Previously known as H1 (E ~ V)"
fig_F2_PrL_vs_V.__doc__ += "\n\nAlias: Previously known as H2 main effect"
fig_F3a_L_given_F.__doc__ += "\n\nAlias: Previously known as H2 V×F interaction"
fig_F5_stepup_by_F.__doc__ += "\n\nAlias: Previously known as H3 (S ~ V × F)"


if __name__ == "__main__":
    print("="*80)
    print("F-SERIES PLOTTING MODULE (HEV/HLVF/HSF)")
    print("="*80)
    print("\nThis module generates standardized figures for two-snapshot analysis.")
    print("\nTerminology:")
    print("  • HEV: E ~ V + controls (OLS)")
    print("  • HLVF: L ~ V × F + controls (Logit, NO E)")
    print("  • HSF: S ~ V × F + controls (OLS, L==1 only)")
    print("\nUsage:")
    print("  from modules.plots_F_series import create_F_series")
    print("  paths = create_F_series(df, results, Path('outputs/figures'))")
    print("\nSee module docstring for full specifications.")
    print("="*80)
