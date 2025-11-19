"""
Demonstration: F-Series Plots with HEV/HLVF/HSF Terminology

This script shows how to generate standardized figures using the refactored
plotting suite with proper HEV/HLVF/HSF naming conventions.

Terminology (aligned with W2 slides):
- HEV: E ~ V + controls (OLS) - Early event ~ Vagueness
- HLVF: L ~ V × F + controls (Logit) - Later success ~ Vagueness × Flexibility
  CRITICAL: NO early_funding control (E is mediator, not confounder)
- HSF: S ~ V × F + controls (OLS, L==1 only) - Step-up ~ Vagueness × Flexibility

Reference: W2 slides p.49 "Early Funding: Mediator or Confounder?"
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Import models and plots
from modules import models
from modules.plots_F_series import create_F_series

print("="*80)
print("F-SERIES DEMONSTRATION (HEV/HLVF/HSF)")
print("="*80)

# =============================================================================
# STEP 1: Generate Synthetic Data
# =============================================================================

print("\n1. Generating synthetic data...")

np.random.seed(42)
n = 500

df = pd.DataFrame({
    # Core variables (ELSVF)
    'E': np.random.binomial(1, 0.15, n),  # Early event (Series A at baseline)
    'E_scaled': np.random.uniform(0, 10, n),
    'L': np.random.binomial(1, 0.12, n),  # Later success (Series B+ at endpoint)
    'L_2024': np.random.binomial(1, 0.12, n),
    'L_2025': np.random.binomial(1, 0.10, n),
    'V': np.random.normal(50, 15, n),  # Vagueness (raw)
    'z_V': np.random.normal(0, 1, n),  # Vagueness (z-scored)
    'F_flexibility': np.random.binomial(1, 0.7, n),  # 1=Software/Flexible, 0=Hardware
    'S_stepup_log': np.random.normal(0.5, 0.8, n),  # Step-up (log)

    # Moderators
    'founder_serial': np.random.binomial(1, 0.25, n),  # Serial founder

    # Controls
    'founding_cohort': np.random.choice(['2015-2017', '2018-2020', '2021-2023'], n),
    'region': np.random.choice(['US', 'EU', 'Asia'], n),
    'z_employees_log': np.random.normal(0, 1, n),

    # For H4 compatibility
    'z_vagueness': np.random.normal(0, 1, n),
    'growth': np.random.binomial(1, 0.12, n),
})

print(f"   ✓ Created dataset: {len(df):,} rows × {len(df.columns)} columns")

# =============================================================================
# STEP 2: Fit Models (HEV/HLVF/HSF)
# =============================================================================

print("\n2. Fitting models (HEV/HLVF/HSF terminology)...")

# HEV: E ~ V + controls (OLS)
print("\n   a) HEV: E ~ V + controls")
try:
    hev = models.run_HEV(df)
    coef_v = hev.params.get('z_V', np.nan)
    pval_v = hev.pvalues.get('z_V', np.nan)
    print(f"      ✓ HEV fitted: β(V) = {coef_v:.3f}, p = {pval_v:.3f}")
except Exception as e:
    print(f"      ✗ HEV failed: {e}")
    hev = None

# HLVF: L ~ V × F + controls (Logit, NO E)
print("\n   b) HLVF: L ~ V × F + controls (NO E - mediator principle)")
try:
    hlvf = models.run_HLVF(df)
    coef_v = hlvf.params.get('z_V', np.nan)
    coef_vxf = hlvf.params.get('z_V:F_flexibility', np.nan)
    print(f"      ✓ HLVF fitted: β(V) = {coef_v:.3f}, β(V×F) = {coef_vxf:.3f}")
    print(f"      ⚠️  CRITICAL: NO early_funding control (E is mediator)")
except Exception as e:
    print(f"      ✗ HLVF failed: {e}")
    hlvf = None

# H4: growth ~ V × C (for F3b)
print("\n   c) H4: growth ~ V × C (founder interaction)")
try:
    h4 = models.test_h4_growth_interaction(df)
    v_param = 'z_V' if 'z_V' in h4.params else 'z_vagueness'
    coef_v = h4.params.get(v_param, np.nan)
    print(f"      ✓ H4 fitted: β({v_param}) = {coef_v:.3f}")
except Exception as e:
    print(f"      ✗ H4 failed: {e}")
    h4 = None

# HSF: S ~ V × F (OLS, L==1 only)
print("\n   d) HSF: S ~ V × F (survivors only)")
try:
    hsf = models.run_HSF(df)
    coef_v = hsf.params.get('z_V', np.nan)
    print(f"      ✓ HSF fitted: β(V) = {coef_v:.3f}")
except ValueError as e:
    print(f"      ⚠️  HSF skipped: {str(e)[:80]}...")
    hsf = None
except Exception as e:
    print(f"      ✗ HSF failed: {e}")
    hsf = None

# =============================================================================
# STEP 3: Create Specification Curve Data (F6)
# =============================================================================

print("\n3. Creating specification curve data...")

spec_df = pd.DataFrame({
    'coefficient': np.random.normal(0.05, 0.12, 60),
    'pvalue': np.random.uniform(0, 0.15, 60),
    'std_error': np.random.uniform(0.02, 0.06, 60),
    'term': np.random.choice(['V', 'VxF', 'VxC'], 60)
})

print(f"   ✓ Created spec_df: {len(spec_df)} specifications")

# =============================================================================
# STEP 4: Generate All F-Series Plots
# =============================================================================

print("\n4. Generating F-series plots (F1-F6)...")

outdir = Path("outputs/figures")
outdir.mkdir(parents=True, exist_ok=True)

# Package results with HEV/HLVF/HSF keys
results = {
    'HEV': hev,  # E ~ V
    'HLVF': hlvf,  # L ~ V × F (NO E)
    'h4': h4,  # For F3b
    'HSF': hsf,  # S ~ V × F (L==1 only)
    'spec_df': spec_df
}

try:
    paths = create_F_series(df, results, outdir)

    print("\n" + "="*80)
    print("✅ SUCCESS - All F-series plots generated!")
    print("="*80)

    print(f"\nOutput directory: {outdir.absolute()}")
    print(f"\nGenerated {len(paths)} figure sets:")

    for fig_name in sorted(paths.keys()):
        formats = ', '.join(paths[fig_name].keys())
        print(f"  • {fig_name}: {formats}")

    print("\n" + "="*80)
    print("FIGURE INVENTORY (HEV/HLVF/HSF Terminology)")
    print("="*80)
    print("\nF1: E vs V (HEV)")
    print("    - Scatter + OLS fit line")
    print("    - Red color (E), green x-axis (V)")
    print("\nF2: Pr(L) vs V (HLVF)")
    print("    - Blue curve, F at median")
    print("    - CRITICAL: NO early_funding control")
    print("\nF3a: L | F (V×F from HLVF)")
    print("    - F=1: skyblue, solid, ↑ slope")
    print("    - F=0: skyblue, dashed, ↓/flat slope")
    print("\nF3b: L | C (V×C)")
    print("    - C=1: orange, dash-dot")
    print("    - C=0: orange, dotted")
    print("\nF4: Distributions (5 figures)")
    print("    - F4_E_dist, F4_L24_dist, F4_L25_dist")
    print("    - F4_V_dist, F4_F_dist")
    print("\nF5: Step-up by F (HSF)")
    print("    - Purple boxplots, L==1 only")
    print("\nF6: Specification curve")
    print("    - Color-coded by term (V/V×F/V×C)")

    print("\n" + "="*80)
    print("KEY PRINCIPLES")
    print("="*80)
    print("✓ HEV/HLVF/HSF terminology (no H1/H2)")
    print("✓ HLVF: NO early_funding control (E is mediator)")
    print("✓ W2 color palette: E=red, L=#0000FF, V=green, S=purple, F=skyblue, C=orange")
    print("✓ Axis coloring: V=green, L=blue")
    print("✓ Interaction line styles (solid/dashed/dash-dot/dotted)")
    print("✓ Both PNG (300dpi) + PDF formats")

except Exception as e:
    print("\n" + "="*80)
    print("❌ ERROR during plot generation")
    print("="*80)
    print(f"\n{type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "="*80)
print("DEMONSTRATION COMPLETE")
print("="*80)
print("\nNext steps:")
print("  1. Review figures in outputs/figures/")
print("  2. Verify HEV/HLVF/HSF labels and colors")
print("  3. Check NO-E principle in HLVF plots (F2, F3a)")
print("  4. Use with real data: python demo_F_series_HEV_HLVF_HSF.py")
