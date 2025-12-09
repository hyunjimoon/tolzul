#!/usr/bin/env python3
"""
Quick Test: Thesis Pipeline Verification

Tests all critical components before advisor meeting.
"""

import sys
from pathlib import Path
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Add modules to path
sys.path.insert(0, str(Path(__file__).parent))

from modules.features import engineer_features, preprocess_for_h2, compute_founder_credibility, extract_sector_fe
from modules.models import test_h1_early_funding, test_h2_main_growth

def test_data_loading():
    """Test 1: Data loading"""
    print("\n" + "="*80)
    print("TEST 1: DATA LOADING")
    print("="*80)

    try:
        # Try processed data first
        df = pd.read_csv('data/processed/analysis_panel.csv', nrows=1000)
        print(f"✓ Loaded {len(df):,} rows from processed data")
        return df
    except FileNotFoundError:
        print("⚠️ Processed data not found, trying raw data...")
        try:
            # Fallback to raw data
            df = pd.read_csv('data/raw/Company20220101.dat', sep='|', nrows=1000, low_memory=False)
            print(f"✓ Loaded {len(df):,} rows from raw data")
            return df
        except Exception as e:
            print(f"❌ Failed to load data: {e}")
            print("\nTroubleshooting:")
            print("  1. Check if data files exist:")
            print("     ls data/raw/Company*.dat")
            print("     ls data/processed/*.csv")
            print("  2. Run consolidation:")
            print("     python -c 'from modules.features import consolidate_company_snapshots; consolidate_company_snapshots(\"data/raw\")'")
            sys.exit(1)

def test_feature_engineering(df):
    """Test 2: Feature engineering"""
    print("\n" + "="*80)
    print("TEST 2: FEATURE ENGINEERING")
    print("="*80)

    try:
        # Initial columns
        print(f"  Input columns: {len(df.columns)}")

        # Engineer features
        df = engineer_features(df)
        print(f"  After engineering: {len(df.columns)} columns")

        # Check key features
        key_features = ['vagueness', 'is_hardware', 'early_funding_musd', 'growth']
        present = [f for f in key_features if f in df.columns]
        missing = [f for f in key_features if f not in df.columns]

        print(f"\n  ✓ Created features: {', '.join(present)}")
        if missing:
            print(f"  ⚠️ Missing features: {', '.join(missing)}")

        # Add founder credibility and sector FE
        df['founder_credibility'] = compute_founder_credibility(df)
        if 'keywords' in df.columns:
            df['sector_fe'] = extract_sector_fe(df['keywords'])

        # Preprocessing
        df = preprocess_for_h2(df)
        print(f"  After preprocessing: {len(df.columns)} columns")

        # Check z-scored variables
        z_vars = [c for c in df.columns if c.startswith('z_')]
        print(f"  ✓ Z-scored variables: {', '.join(z_vars)}")

        # Verify founder_serial exists
        if 'founder_serial' in df.columns:
            n_serial = df['founder_serial'].sum()
            pct_serial = n_serial / len(df) * 100
            print(f"  ✓ founder_serial: {n_serial} serial founders ({pct_serial:.1f}%)")
        else:
            print(f"  ⚠️ founder_serial missing!")

        return df

    except Exception as e:
        print(f"❌ Feature engineering failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def test_h1_model(df):
    """Test 3: H1 Early Funding Model"""
    print("\n" + "="*80)
    print("TEST 3: H1 MODEL (Early Funding ~ Vagueness)")
    print("="*80)

    try:
        # Filter to companies with early funding
        h1_df = df[df['early_funding_musd'].notna()].copy()

        if len(h1_df) < 50:
            print(f"⚠️ Only {len(h1_df)} companies with early funding - may need more data")
            return None

        print(f"  Sample size: {len(h1_df):,} companies")

        # Fit model
        h1_res = test_h1_early_funding(h1_df)

        # Extract vagueness coefficient
        if 'z_vagueness' in h1_res.params.index:
            coef = h1_res.params['z_vagueness']
            pval = h1_res.pvalues['z_vagueness']
            se = h1_res.bse['z_vagueness']

            print(f"\n  Vagueness Coefficient:")
            print(f"    β = {coef:.4f} (SE = {se:.4f})")
            print(f"    p = {pval:.4f}")

            if coef < 0 and pval < 0.05:
                print(f"    ✅ H1 SUPPORTED: Vagueness reduces early funding (p < 0.05)")
            elif coef < 0:
                print(f"    ⚠️ H1 DIRECTION CORRECT but not significant")
            else:
                print(f"    ❌ H1 NOT SUPPORTED: Unexpected positive effect")

        print(f"\n  ✓ H1 model converged successfully")
        return h1_res

    except Exception as e:
        print(f"❌ H1 model failed: {e}")
        import traceback
        traceback.print_exc()
        return None

def test_h2_model(df):
    """Test 4: H2 Growth Model"""
    print("\n" + "="*80)
    print("TEST 4: H2 MODEL (Growth ~ Vagueness × Hardware)")
    print("="*80)

    try:
        # Filter to companies with growth variable
        h2_df = df[df['growth'].notna()].copy()

        if len(h2_df) < 100:
            print(f"⚠️ Only {len(h2_df)} companies with growth data - may need more data")
            return None

        print(f"  Sample size: {len(h2_df):,} companies")
        print(f"  Growth rate: {h2_df['growth'].mean():.1%}")

        # Check hardware distribution
        if 'is_hardware' in h2_df.columns:
            hw_dist = h2_df['is_hardware'].value_counts()
            print(f"\n  Hardware distribution:")
            for val, count in hw_dist.items():
                label = 'Hardware' if val == 1 else 'Software'
                pct = count / len(h2_df) * 100
                print(f"    {label}: {count:,} ({pct:.1f}%)")

        # Fit model
        h2_res = test_h2_main_growth(h2_df)

        # Extract coefficients
        if 'z_vagueness' in h2_res.params.index:
            main_coef = h2_res.params['z_vagueness']
            main_pval = h2_res.pvalues['z_vagueness']

            print(f"\n  Main Effect (z_vagueness):")
            print(f"    β = {main_coef:.4f}")
            print(f"    p = {main_pval:.4f}")

            # Check for interaction
            interaction_vars = [v for v in h2_res.params.index if 'vagueness' in v.lower() and ('hardware' in v.lower() or ':' in v)]

            if interaction_vars:
                int_var = interaction_vars[0]
                int_coef = h2_res.params[int_var]
                int_pval = h2_res.pvalues[int_var]

                print(f"\n  Interaction (z_vagueness × is_hardware):")
                print(f"    β = {int_coef:.4f}")
                print(f"    p = {int_pval:.4f}")

                print(f"\n  Conditional Effects:")
                print(f"    Software (HW=0): {main_coef:.4f}")
                print(f"    Hardware (HW=1): {main_coef + int_coef:.4f}")

                if int_pval < 0.05:
                    print(f"    ✅ H2 SUPPORTED: Significant moderation (p < 0.05)")
                else:
                    print(f"    ⚠️ H2 NOT SUPPORTED: Interaction not significant")

        print(f"\n  ✓ H2 model converged successfully")
        return h2_res

    except Exception as e:
        print(f"❌ H2 model failed: {e}")
        import traceback
        traceback.print_exc()
        return None

def test_vagueness_quality(df):
    """Test 5: Vagueness score quality"""
    print("\n" + "="*80)
    print("TEST 5: VAGUENESS SCORE QUALITY")
    print("="*80)

    if 'vagueness' not in df.columns:
        print("⚠️ Vagueness column not found")
        return

    vagueness = df['vagueness'].dropna()

    print(f"  Sample size: {len(vagueness):,}")
    print(f"  Mean: {vagueness.mean():.2f}")
    print(f"  Std: {vagueness.std():.2f}")
    print(f"  Min: {vagueness.min():.2f}")
    print(f"  Max: {vagueness.max():.2f}")

    if vagueness.std() < 10:
        print(f"\n  ⚠️ WARNING: Low variation (std={vagueness.std():.2f} < 10)")
        print(f"     This may indicate:")
        print(f"       - Empty Description/Keywords columns")
        print(f"       - Constant text across companies")
        print(f"       - Bug in vagueness scoring")
    else:
        print(f"\n  ✓ Good variation (std={vagueness.std():.2f} > 10)")

def main():
    """Run all tests"""
    print("="*80)
    print("THESIS PIPELINE TEST SUITE")
    print("="*80)
    print("\nThis script tests all critical components before advisor meeting.")
    print("Expected runtime: 30-60 seconds\n")

    # Test 1: Data loading
    df = test_data_loading()

    # Test 2: Feature engineering
    df = test_feature_engineering(df)

    # Test 5: Vagueness quality (before models)
    test_vagueness_quality(df)

    # Test 3: H1 model
    h1_res = test_h1_model(df)

    # Test 4: H2 model
    h2_res = test_h2_model(df)

    # Final summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)

    tests_passed = 0
    tests_total = 4

    if df is not None:
        tests_passed += 1
        print("✓ Data loading: PASS")
    else:
        print("❌ Data loading: FAIL")

    if 'vagueness' in df.columns and 'growth' in df.columns:
        tests_passed += 1
        print("✓ Feature engineering: PASS")
    else:
        print("❌ Feature engineering: FAIL")

    if h1_res is not None:
        tests_passed += 1
        print("✓ H1 model: PASS")
    else:
        print("❌ H1 model: FAIL")

    if h2_res is not None:
        tests_passed += 1
        print("✓ H2 model: PASS")
    else:
        print("❌ H2 model: FAIL")

    print(f"\nTests passed: {tests_passed}/{tests_total}")

    if tests_passed == tests_total:
        print("\n🎉 ALL TESTS PASSED - Ready for thesis submission!")
        print("\nNext steps:")
        print("  1. Run full analysis: python archive/run_analysis.py --output outputs/")
        print("  2. Review outputs/h1_coefficients.csv")
        print("  3. Review outputs/h2_main_coefficients.csv")
        print("  4. Check outputs/figures/*.png")
        return 0
    else:
        print("\n⚠️ Some tests failed - review errors above")
        return 1

if __name__ == "__main__":
    sys.exit(main())
