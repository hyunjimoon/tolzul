"""
Quick test script for F-series plotting suite.
Run with: python test_F_series.py
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add modules to path
sys.path.insert(0, str(Path(__file__).parent / "modules"))

from modules import plots, models

print("="*80)
print("F-SERIES PLOTTING SUITE - QUICK TEST")
print("="*80)

# ============================================================================
# 1. Generate synthetic data
# ============================================================================
print("\n1. Generating synthetic test data...")

np.random.seed(42)
n = 200

df = pd.DataFrame({
    # Core variables (E/L/S/V/F)
    'E': np.random.uniform(0, 10, n),  # Early funding
    'E_scaled': np.random.uniform(0, 10, n),
    'L': np.random.binomial(1, 0.4, n),  # Later success
    'L_2024': np.random.binomial(1, 0.4, n),
    'L_2025': np.random.binomial(1, 0.35, n),
    'V': np.random.normal(50, 15, n),  # Vagueness (raw)
    'z_V': np.random.normal(0, 1, n),  # Vagueness (z-scored)
    'F_flexibility': np.random.binomial(1, 0.6, n),  # 1=Software, 0=Hardware
    'S_stepup_log': np.random.normal(0.5, 0.8, n),  # Step-up (log)

    # Moderator
    'founder_serial': np.random.binomial(1, 0.3, n),

    # Controls
    'founding_cohort': np.random.choice(['2015-2017', '2018-2020', '2021-2023'], n),
    'region': np.random.choice(['US', 'EU', 'Asia'], n),
    'z_employees_log': np.random.normal(0, 1, n),

    # For old W1 compatibility
    'z_vagueness': np.random.normal(0, 1, n),
    'growth': np.random.binomial(1, 0.4, n),
})

print(f"   ✓ Created synthetic dataset: {len(df)} rows × {len(df.columns)} cols")
print(f"   Sample columns: {list(df.columns[:6])}")

# ============================================================================
# 2. Fit models
# ============================================================================
print("\n2. Fitting models on synthetic data...")

try:
    # HEV: E ~ V (OLS)
    print("   - Fitting HEV (E ~ z_V)...")
    hev = models.run_HEV(df)
    print(f"     ✓ HEV fitted. Coef(z_V) = {hev.params.get('z_V', np.nan):.3f}")
except Exception as e:
    print(f"     ✗ HEV failed: {e}")
    hev = None

try:
    # HLVF: L ~ V × F (Logit)
    print("   - Fitting HLVF (L ~ z_V × F_flexibility)...")
    hlvf = models.run_HLVF(df)
    print(f"     ✓ HLVF fitted. Coef(z_V) = {hlvf.params.get('z_V', np.nan):.3f}")
except Exception as e:
    print(f"     ✗ HLVF failed: {e}")
    hlvf = None

try:
    # H4: growth ~ V × C (Logit)
    print("   - Fitting H4 (growth ~ z_vagueness × founder_serial)...")
    h4 = models.test_h4_growth_interaction(df)
    v_param = 'z_V' if 'z_V' in h4.params else 'z_vagueness'
    print(f"     ✓ H4 fitted. Coef({v_param}) = {h4.params.get(v_param, np.nan):.3f}")
except Exception as e:
    print(f"     ✗ H4 failed: {e}")
    h4 = None

# HSF: S ~ V × F (OLS, survivors only)
try:
    print("   - Fitting HSF (S ~ z_V × F_flexibility, L==1 only)...")
    hsf = models.run_HSF(df)
    print(f"     ✓ HSF fitted. Coef(z_V) = {hsf.params.get('z_V', np.nan):.3f}")
except Exception as e:
    print(f"     ✗ HSF failed: {e}")
    hsf = None

# ============================================================================
# 3. Create spec_df for F6
# ============================================================================
print("\n3. Creating specification curve data...")

spec_df = pd.DataFrame({
    'coefficient': np.random.normal(0.05, 0.15, 50),
    'pvalue': np.random.uniform(0, 0.15, 50),
    'std_error': np.random.uniform(0.02, 0.08, 50),
    'term': np.random.choice(['V', 'VxF', 'VxC'], 50)
})
print(f"   ✓ Created spec_df: {len(spec_df)} specifications")

# ============================================================================
# 4. Generate all F-series plots
# ============================================================================
print("\n4. Generating F-series plots...")

outdir = Path("outputs/F_series_test")
results = {
    'hev': hev,
    'hlvf': hlvf,
    'h4': h4,
    'hsf': hsf,
    'spec_df': spec_df
}

try:
    paths = plots.create_F_series(df, results, outdir)

    print("\n" + "="*80)
    print("✅ SUCCESS - All plots generated!")
    print("="*80)
    print(f"\nGenerated {len(paths)} plots in: {outdir.absolute()}")
    print("\nFiles created:")
    for name, path in sorted(paths.items()):
        size_kb = path.stat().st_size / 1024 if path.exists() else 0
        print(f"   ✓ {name:8s} → {path.name:20s} ({size_kb:.1f} KB)")

    print("\n" + "="*80)
    print("QUICK VISUAL CHECK:")
    print("="*80)
    print(f"\nOpen the output directory to view plots:")
    print(f"   {outdir.absolute()}")
    print("\nExpected outputs:")
    print("   • F1_E_vs_V.png (red scatter + fit)")
    print("   • F2_PrL_vs_V.png (blue curve)")
    print("   • F3a_L_given_F.png (skyblue solid + dashed)")
    print("   • F3b_L_given_C.png (orange dash-dot + dotted)")
    print("   • F4_E.png, F4_L_2024.png, F4_L_2025.png, F4_V.png")
    print("   • F5_StepUp_by_F.png (purple boxes)")
    print("   • F6_SpecCurve.png (color-coded scatter)")

except Exception as e:
    print("\n" + "="*80)
    print("❌ ERROR during plot generation")
    print("="*80)
    print(f"\n{type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "="*80)
print("TEST COMPLETE")
print("="*80)
