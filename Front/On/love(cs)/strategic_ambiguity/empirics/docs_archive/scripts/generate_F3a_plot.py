#!/usr/bin/env python3
"""
Generate F3a Interaction Plot (L | F) from Current Results

Inputs:
- outputs/h2_model_architecture.csv (coefficients)
- outputs/h2_analysis_dataset.csv (for predictions)

Outputs:
- outputs/figures/F3a_L_given_F_CURRENT.png (300 DPI)
- outputs/figures/F3a_L_given_F_CURRENT.pdf

Author: 권준/나대용 (中軍)
Date: 2025-11-16
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

# Add modules to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# W2 Color Palette (EXACT)
PALETTE = {
    "E": "red",
    "L": "#0000FF",  # Pure blue
    "V": "green",
    "F": "skyblue",  # Flexibility/Software
    "HW": "gray",    # Hardware/Rigid
}

LINE_STYLES = {
    'F=1': {'color': PALETTE['F'], 'linestyle': '-', 'linewidth': 2.5},   # Software
    'F=0': {'color': PALETTE['HW'], 'linestyle': '--', 'linewidth': 2.5}, # Hardware
}

def load_data():
    """Load analysis dataset"""
    print("📂 Loading data...")

    data_path = Path("outputs/h2_analysis_dataset.csv")

    if not data_path.exists():
        raise FileNotFoundError(
            f"Data file not found: {data_path}\n"
            "Please run: python archive/run_analysis.py --output outputs/"
        )

    df = pd.read_csv(data_path)
    print(f"✓ Loaded {len(df):,} rows")

    # Check required columns
    required = ['growth', 'z_vagueness', 'is_hardware', 'z_employees_log', 'founding_cohort']
    missing = [c for c in required if c not in df.columns]

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    return df

def fit_model(df):
    """Fit H2 logit model with architecture moderator"""
    print("\n📊 Fitting H2 model...")

    formula = "growth ~ z_vagueness * is_hardware + z_employees_log + C(founding_cohort)"

    # Filter to valid data
    analysis_df = df.dropna(subset=['growth', 'z_vagueness', 'is_hardware']).copy()

    print(f"  Sample size: {len(analysis_df):,}")
    print(f"  Growth rate: {analysis_df['growth'].mean():.1%}")

    # Try standard fit first
    try:
        print("  Attempting standard logit...")
        model = smf.logit(formula, data=analysis_df).fit(disp=False)
        print("  ✓ Standard fit successful")
    except Exception:
        print("  ✗ Standard fit failed, trying L1 regularization...")
        try:
            model = smf.logit(formula, data=analysis_df).fit_regularized(
                method='l1', alpha=0.1, disp=False, maxiter=200, warn_convergence=False
            )
            print("  ✓ L1 regularization (alpha=0.1) successful")
        except Exception:
            model = smf.logit(formula, data=analysis_df).fit_regularized(
                method='l1', alpha=0.5, disp=False, maxiter=200, warn_convergence=False
            )
            print("  ✓ L1 regularization (alpha=0.5) successful")

    # Print key coefficients
    print("\n  Key Coefficients:")
    if 'z_vagueness' in model.params.index:
        print(f"    z_vagueness: {model.params['z_vagueness']:.4f} (p={model.pvalues['z_vagueness']:.3f})")

    interaction_vars = [v for v in model.params.index if 'vagueness' in v.lower() and 'hardware' in v.lower()]
    if interaction_vars:
        int_var = interaction_vars[0]
        print(f"    {int_var}: {model.params[int_var]:.4f} (p={model.pvalues[int_var]:.3f})")

    return model, analysis_df

def create_F3a_plot(model, df):
    """Create F3a: L | F interaction plot"""
    print("\n📊 Generating F3a plot...")

    fig, ax = plt.subplots(figsize=(10, 6))

    # Vagueness range
    V_range = np.linspace(df['z_vagueness'].min(), df['z_vagueness'].max(), 100)

    # Fix controls at median/mode
    z_emp_median = df['z_employees_log'].median() if 'z_employees_log' in df.columns else 0
    cohort_mode = df['founding_cohort'].mode()[0] if 'founding_cohort' in df.columns else '2015-18'

    # Predict for Software (is_hardware = 0)
    pred_df_sw = pd.DataFrame({
        'z_vagueness': V_range,
        'is_hardware': 0,
        'z_employees_log': z_emp_median,
        'founding_cohort': cohort_mode
    })

    try:
        Pr_sw = model.predict(pred_df_sw)
        ax.plot(V_range, Pr_sw, label='Software (is_hardware=0)', **LINE_STYLES['F=1'])
        print("  ✓ Software line plotted")
    except Exception as e:
        print(f"  ⚠️ Could not plot software line: {e}")

    # Predict for Hardware (is_hardware = 1)
    pred_df_hw = pd.DataFrame({
        'z_vagueness': V_range,
        'is_hardware': 1,
        'z_employees_log': z_emp_median,
        'founding_cohort': cohort_mode
    })

    try:
        Pr_hw = model.predict(pred_df_hw)
        ax.plot(V_range, Pr_hw, label='Hardware (is_hardware=1)', **LINE_STYLES['F=0'])
        print("  ✓ Hardware line plotted")
    except Exception as e:
        print(f"  ⚠️ Could not plot hardware line: {e}")

    # Styling
    ax.set_xlabel('Vagueness (z-score)', fontsize=13, fontweight='bold', color=PALETTE['V'])
    ax.set_ylabel('Pr(Series B+)', fontsize=13, fontweight='bold', color=PALETTE['L'])
    ax.set_title('F3a. Growth ~ Vagueness × Integration Cost', fontsize=15, fontweight='bold')
    ax.set_ylim([0, 1])

    # Color axes
    ax.tick_params(axis='x', colors=PALETTE['V'])
    ax.tick_params(axis='y', colors=PALETTE['L'])
    ax.spines['bottom'].set_color(PALETTE['V'])
    ax.spines['left'].set_color(PALETTE['L'])

    # Legend
    ax.legend(loc='upper left', fontsize=11, framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle='--')

    # Caption
    caption = (
        f'Controls fixed at median/mode\n'
        f'Sample: N={len(df):,} Series A companies\n'
        f'E omitted: mediator, not control'
    )
    ax.text(0.98, 0.02, caption, transform=ax.transAxes, fontsize=8,
            ha='right', va='bottom', style='italic', color='gray')

    plt.tight_layout()

    # Save
    outdir = Path("outputs/figures")
    outdir.mkdir(parents=True, exist_ok=True)

    # PNG for slides
    png_path = outdir / "F3a_L_given_F_CURRENT.png"
    fig.savefig(png_path, dpi=300, bbox_inches='tight', format='png')
    print(f"  ✓ Saved: {png_path}")

    # PDF for LaTeX
    pdf_path = outdir / "F3a_L_given_F_CURRENT.pdf"
    fig.savefig(pdf_path, dpi=300, bbox_inches='tight', format='pdf')
    print(f"  ✓ Saved: {pdf_path}")

    plt.close(fig)

    return png_path, pdf_path

def print_interpretation(model):
    """Print marginal effects for interpretation"""
    print("\n" + "="*80)
    print("MARGINAL EFFECTS INTERPRETATION")
    print("="*80)

    # Extract coefficients
    if 'z_vagueness' not in model.params.index:
        print("⚠️ z_vagueness not found in model")
        return

    beta_main = model.params['z_vagueness']

    # Find interaction term
    interaction_vars = [v for v in model.params.index if 'vagueness' in v.lower() and 'hardware' in v.lower()]

    if not interaction_vars:
        print("⚠️ Interaction term not found")
        return

    int_var = interaction_vars[0]
    beta_int = model.params[int_var]

    # Conditional effects
    print(f"\nConditional Effects:")
    print(f"  Software (is_hardware=0): β = {beta_main:.4f}")
    print(f"  Hardware (is_hardware=1): β = {beta_main + beta_int:.4f}")
    print(f"  Difference: Δ = {beta_int:.4f}")

    # Significance
    p_main = model.pvalues['z_vagueness']
    p_int = model.pvalues[int_var]

    print(f"\nSignificance:")
    print(f"  Main effect: p = {p_main:.4f} {'✓' if p_main < 0.05 else '✗'}")
    print(f"  Interaction: p = {p_int:.4f} {'✓' if p_int < 0.05 else '⚠️ (marginal)'}")

    # Interpretation
    print(f"\nInterpretation:")
    if beta_main + beta_int > 0 and abs(beta_main) < 0.01:
        print("  → Vagueness helps HARDWARE firms (positive slope)")
        print("  → Vagueness has NO effect on SOFTWARE firms (flat)")
        print("  → REVERSAL: Opposite of hypothesis, but theoretically interesting!")
    elif beta_main > 0 and beta_int < 0:
        print("  → Vagueness helps SOFTWARE firms (positive main effect)")
        print("  → Effect attenuated for HARDWARE firms (negative interaction)")
        print("  → Consistent with hypothesis")
    else:
        print("  → Complex pattern - review plot for visual interpretation")

def main():
    print("="*80)
    print("F3a PLOT GENERATION (Current Data)")
    print("="*80)

    # Load data
    df = load_data()

    # Fit model
    model, analysis_df = fit_model(df)

    # Create plot
    png_path, pdf_path = create_F3a_plot(model, analysis_df)

    # Interpret
    print_interpretation(model)

    print("\n" + "="*80)
    print("✅ F3a plot generation complete")
    print("="*80)
    print(f"\nFiles created:")
    print(f"  • {png_path} (for PowerPoint slides)")
    print(f"  • {pdf_path} (for LaTeX paper)")

if __name__ == "__main__":
    main()
