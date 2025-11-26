#!/usr/bin/env python3
"""
Smoke Test for Two-Snapshot Analysis Mode

Tests the simplified E/L/S/V/F analysis pipeline:
1. Load two snapshots (baseline + endpoint)
2. Build E/L/S/V/F variables
3. Run three hypothesis tests (H1, H2, H3)

Prerequisites:
    You need to have the Crunchbase snapshot data files:
    - data/dat/2022-01-01_crunchbase_snapshot.dat (baseline)
    - data/dat/2023-12-01_crunchbase_snapshot.dat (endpoint)

    Create the data/dat/ directory and place your snapshot files there.

Usage:
    python smoke_test_two_snapshot.py              # All companies
    python smoke_test_two_snapshot.py --quantum    # Quantum companies only
"""

import sys
import argparse
from pathlib import Path
import pandas as pd
import numpy as np

# Add modules to path
sys.path.insert(0, str(Path(__file__).parent))

from modules.features import load_two_snapshots, build_ELS_from_two_snapshots
from modules.models import run_HEV, run_HLVF, run_HSF


def main(quantum_only: bool = False):
    print("=" * 70)
    print(f"SMOKE TEST: Two-Snapshot Analysis (E/L/S/V/F){' - QUANTUM ONLY' if quantum_only else ''}")
    print("=" * 70)
    if quantum_only:
        print("\n🔬 MODE: Quantum-related companies only")
        print("   Filtering using quantum keywords in Description/Keywords/Promise")

    # ============================================================
    # STEP 1: Load two snapshots
    # ============================================================
    print("\n📂 STEP 1: Loading two snapshots...")

    baseline_path = Path("data/raw/Company20231201.dat")
    end_path = Path("data/raw/Company20240601.dat")

    # Check if files exist
    if not baseline_path.exists():
        print(f"❌ ERROR: Baseline snapshot not found: {baseline_path}")
        print(f"   Please ensure the file exists in the data/dat/ directory")
        return 1

    if not end_path.exists():
        print(f"❌ ERROR: Endpoint snapshot not found: {end_path}")
        print(f"   Please ensure the file exists in the data/dat/ directory")
        return 1

    try:
        df_base, df_end = load_two_snapshots(baseline_path, end_path)
        print(f"✓ Loaded baseline: {len(df_base):,} rows")
        print(f"✓ Loaded endpoint: {len(df_end):,} rows")
    except Exception as e:
        print(f"❌ ERROR loading snapshots: {e}")
        return 1

    # ============================================================
    # STEP 2: Build E/L/S/V/F variables
    # ============================================================
    print(f"\n🔧 STEP 2: Building E/L/S/V/F variables{'(quantum-only)' if quantum_only else ''}...")

    try:
        df_els = build_ELS_from_two_snapshots(df_base, df_end, quantum_only=quantum_only)
        print(f"✓ Built ELS DataFrame: {len(df_els):,} rows × {len(df_els.columns)} columns")
        print(f"  Columns: {', '.join(df_els.columns)}")

        # Print summary statistics
        print(f"\n  📊 Variable Summary:")
        print(f"     E (Early event): {df_els['E'].sum():,} / {len(df_els):,} = {df_els['E'].mean():.1%}")
        print(f"     L (Later success): {df_els['L'].sum():,} / {len(df_els):,} = {df_els['L'].mean():.1%}")

        s_valid = df_els['S_stepup'].notna()
        print(f"     S (Step-up): {s_valid.sum():,} valid values")
        if s_valid.sum() > 0:
            print(f"       Mean: {df_els.loc[s_valid, 'S_stepup'].mean():.2f}")
            print(f"       Median: {df_els.loc[s_valid, 'S_stepup'].median():.2f}")
            print(f"       Range: [{df_els.loc[s_valid, 'S_stepup'].min():.2f}, {df_els.loc[s_valid, 'S_stepup'].max():.2f}]")

        v_valid = df_els['z_V'].notna()
        print(f"     V (Vagueness): {v_valid.sum():,} valid values")
        if v_valid.sum() > 0:
            print(f"       Mean: {df_els.loc[v_valid, 'z_V'].mean():.3f}")
            print(f"       Std: {df_els.loc[v_valid, 'z_V'].std():.3f}")

        print(f"     F (Flexibility): {df_els['F_flexibility'].sum():,} / {len(df_els):,} = {df_els['F_flexibility'].mean():.1%}")

    except Exception as e:
        print(f"❌ ERROR building E/L/S/V/F: {e}")
        import traceback
        traceback.print_exc()
        return 1

    # ============================================================
    # STEP 3: Run hypothesis tests
    # ============================================================
    print("\n🧪 STEP 3: Running hypothesis tests...")

    # H1: E ~ V
    print("\n" + "-" * 70)
    print("H1: Early event ~ Vagueness (E ~ V)")
    print("-" * 70)
    try:
        model_h1 = run_HEV(df_els)
        print(f"\n{model_h1.summary()}")

        # Extract key coefficient
        if 'z_V' in model_h1.params:
            coef_v = model_h1.params['z_V']
            pval_v = model_h1.pvalues['z_V']
            print(f"\n  🔑 Key Result (z_V):")
            print(f"     Coefficient: {coef_v:.4f}")
            print(f"     P-value: {pval_v:.4f}")
            print(f"     Expected sign: negative (<0)")
            print(f"     Actual sign: {'✓ negative' if coef_v < 0 else '✗ positive'}")

    except Exception as e:
        print(f"❌ ERROR running H1: {e}")
        import traceback
        traceback.print_exc()

    # H2: L ~ V × F
    print("\n" + "-" * 70)
    print("H2: Later success ~ Vagueness × Flexibility (L ~ V × F)")
    print("-" * 70)
    try:
        model_h2 = run_HLVF(df_els)
        print(f"\n{model_h2.summary()}")

        # Extract key coefficients
        if 'z_V' in model_h2.params:
            coef_v = model_h2.params['z_V']
            pval_v = model_h2.pvalues['z_V']
            print(f"\n  🔑 Key Results:")
            print(f"     z_V (main effect):")
            print(f"       Coefficient: {coef_v:.4f}")
            print(f"       P-value: {pval_v:.4f}")
            print(f"       Expected sign: positive (>0)")
            print(f"       Actual sign: {'✓ positive' if coef_v > 0 else '✗ negative'}")

        if 'z_V:F_flexibility' in model_h2.params:
            coef_int = model_h2.params['z_V:F_flexibility']
            pval_int = model_h2.pvalues['z_V:F_flexibility']
            print(f"     z_V:F_flexibility (interaction):")
            print(f"       Coefficient: {coef_int:.4f}")
            print(f"       P-value: {pval_int:.4f}")
            print(f"       Expected sign: positive (>0) - flexibility AMPLIFIES vagueness benefit")
            print(f"       Actual sign: {'✓ positive' if coef_int > 0 else '✗ negative'}")

    except Exception as e:
        print(f"❌ ERROR running H2: {e}")
        import traceback
        traceback.print_exc()

    # H3: S ~ V × F (L==1 only)
    print("\n" + "-" * 70)
    print("H3: Step-up ~ Vagueness × Flexibility (S ~ V × F, L==1 only)")
    print("-" * 70)
    try:
        model_h3 = run_HSF(df_els)
        print(f"\n{model_h3.summary()}")

        # Extract key coefficients
        if 'z_V' in model_h3.params:
            coef_v = model_h3.params['z_V']
            pval_v = model_h3.pvalues['z_V']
            print(f"\n  🔑 Key Results:")
            print(f"     z_V (main effect):")
            print(f"       Coefficient: {coef_v:.4f}")
            print(f"       P-value: {pval_v:.4f}")
            print(f"       Expected sign: positive (>0)")
            print(f"       Actual sign: {'✓ positive' if coef_v > 0 else '✗ negative'}")

        if 'z_V:F_flexibility' in model_h3.params:
            coef_int = model_h3.params['z_V:F_flexibility']
            pval_int = model_h3.pvalues['z_V:F_flexibility']
            print(f"     z_V:F_flexibility (interaction):")
            print(f"       Coefficient: {coef_int:.4f}")
            print(f"       P-value: {pval_int:.4f}")
            print(f"       Expected sign: positive (>0) - flexibility AMPLIFIES vagueness benefit")
            print(f"       Actual sign: {'✓ positive' if coef_int > 0 else '✗ negative'}")

    except Exception as e:
        print(f"❌ ERROR running H3: {e}")
        import traceback
        traceback.print_exc()

    # ============================================================
    # SUMMARY
    # ============================================================
    print("\n" + "=" * 70)
    print("✓ SMOKE TEST COMPLETE")
    print("=" * 70)
    print("\nNext steps:")
    print("  1. Review the hypothesis test results above")
    print("  2. Check that coefficient signs match expectations")
    print("  3. If all looks good, proceed with full analysis")
    print("")

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Two-snapshot smoke test for E/L/S/V/F analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '--quantum', '-q',
        action='store_true',
        help='Filter to quantum-related companies only'
    )
    args = parser.parse_args()
    sys.exit(main(quantum_only=args.quantum))
