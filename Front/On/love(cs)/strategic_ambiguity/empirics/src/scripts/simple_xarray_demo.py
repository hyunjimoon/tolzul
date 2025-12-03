#!/usr/bin/env python3
"""
Simple xarray Demo - Minimal Example
=====================================

This is the SIMPLEST possible demo of the xarray structure.
Perfect for getting a quick feel for how it works.

Usage:
    python simple_xarray_demo.py
"""

import pandas as pd
import numpy as np
import xarray as xr

# ============================================================================
# Your data file path (update this!)
# ============================================================================
DATA_FILE = "/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/data/raw/consolidated_companies_2022_2024_2025_quantum.parquet"


def simple_demo():
    """Minimal demo showing key concepts."""

    print("\n" + "=" * 80)
    print("SIMPLE XARRAY STRUCTURE DEMO")
    print("=" * 80)

    # ─────────────────────────────────────────────────────────────────────────
    # STEP 1: Load your data
    # ─────────────────────────────────────────────────────────────────────────
    print("\n📂 Step 1: Loading data...")

    df = pd.read_parquet(DATA_FILE)
    print(f"   Loaded {len(df):,} companies")

    # Use first 100 for demo
    df = df.head(100)
    print(f"   Using {len(df)} companies for demo\n")

    # ─────────────────────────────────────────────────────────────────────────
    # STEP 2: Define structure
    # ─────────────────────────────────────────────────────────────────────────
    print("📐 Step 2: Define dimensions...")

    # Dimension 1: venture_id (N companies)
    venture_ids = np.arange(len(df))
    n_ventures = len(venture_ids)

    # Dimension 2: window (cohort_year × end_year combinations)
    cohort_years = [2021, 2022, 2023]
    end_years = [2024, 2025, 2026]

    # Create all combinations
    windows = []
    window_cohort_years = []
    window_end_years = []
    window_horizons = []

    for cohort in cohort_years:
        for end in end_years:
            windows.append((cohort, end))
            window_cohort_years.append(cohort)
            window_end_years.append(end)
            window_horizons.append(end - cohort)

    n_windows = len(windows)
    window_ids = np.arange(n_windows)

    print(f"   venture_id: N = {n_ventures}")
    print(f"   window: W = {n_windows}")
    print(f"\n   Windows:")
    for i, (cohort, end) in enumerate(windows):
        print(f"      {i}: Cohort {cohort} → End {end} ({end-cohort} yr horizon)")

    # ─────────────────────────────────────────────────────────────────────────
    # STEP 3: Extract Series A years (KEY!)
    # ─────────────────────────────────────────────────────────────────────────
    print("\n🎯 Step 3: Extract Series A years...")

    # Try to find Series A year column
    series_a_col = None
    for col in ['SeriesAYear', 'series_a_year', 'YearFounded', 'year_founded']:
        if col in df.columns:
            series_a_col = col
            break

    if series_a_col:
        series_a_years = pd.to_numeric(df[series_a_col], errors='coerce').fillna(2022).astype(int).values
        print(f"   Using column: {series_a_col}")
    else:
        # Random for demo
        series_a_years = np.random.choice(cohort_years, size=n_ventures)
        print(f"   Column not found, using random for demo")

    print(f"\n   Series A year distribution:")
    for year in sorted(np.unique(series_a_years)):
        count = (series_a_years == year).sum()
        print(f"      {year}: {count} companies")

    # ─────────────────────────────────────────────────────────────────────────
    # STEP 4: Create xarray.Dataset
    # ─────────────────────────────────────────────────────────────────────────
    print("\n🏗️  Step 4: Create xarray.Dataset...")

    # Create dataset with simple coordinates (compatible with all xarray versions)
    ds = xr.Dataset(
        coords={
            'venture_id': venture_ids,
            'window': window_ids,
            'series_A_year': ('venture_id', series_a_years),  # KEY COORDINATE!
            'cohort_year': ('window', window_cohort_years),
            'end_year': ('window', window_end_years),
            'horizon_years': ('window', window_horizons),
        }
    )

    print(f"   ✓ Created dataset")

    # ─────────────────────────────────────────────────────────────────────────
    # STEP 5: Compute at_risk (THE KEY CALCULATION!)
    # ─────────────────────────────────────────────────────────────────────────
    print("\n✨ Step 5: Compute at_risk variable...")
    print("\n   Formula: at_risk[i,w] = 1 if series_A_year[i] == cohort_year[w]")

    at_risk = np.zeros((n_ventures, n_windows), dtype=np.int8)

    # For each window, check which ventures match the cohort_year
    for w, (cohort_year, end_year) in enumerate(windows):
        at_risk[:, w] = (series_a_years == cohort_year).astype(np.int8)

    ds['at_risk'] = (('venture_id', 'window'), at_risk)

    print(f"\n   ✓ Computed at_risk")
    print(f"\n   Verification by cohort:")
    for cohort_year in cohort_years:
        n_in_cohort = (series_a_years == cohort_year).sum()
        print(f"      Cohort {cohort_year}: {n_in_cohort} ventures at risk")

    # ─────────────────────────────────────────────────────────────────────────
    # STEP 6: Show structure
    # ─────────────────────────────────────────────────────────────────────────
    print("\n📊 Step 6: Dataset structure:")
    print("\n" + str(ds))

    # ─────────────────────────────────────────────────────────────────────────
    # STEP 7: Demonstrate the KEY INSIGHT
    # ─────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 80)
    print("🔑 KEY INSIGHT: No need for cohort dummy variables!")
    print("=" * 80)

    print("\n❌ OLD WAY (not recommended):")
    print("   is_2021_cohort = (series_A_year == 2021)")
    print("   is_2022_cohort = (series_A_year == 2022)")
    print("   is_2023_cohort = (series_A_year == 2023)")
    print("   # → Need N dummy variables for N cohorts!")

    print("\n✅ NEW WAY (recommended):")
    print("   series_A_year coordinate → single coordinate")
    print("   at_risk[i,w] = (series_A_year[i] == cohort_year[w])")
    print("   # → One calculation, works for all cohorts!")

    # ─────────────────────────────────────────────────────────────────────────
    # STEP 8: Show how to use at_risk
    # ─────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 80)
    print("💡 USAGE EXAMPLES")
    print("=" * 80)

    print("\n1️⃣  Get all ventures in 2022 cohort:")
    print("   cohort_2022 = ds.where(ds.series_A_year == 2022, drop=True)")

    cohort_2022 = ds.where(ds.series_A_year == 2022, drop=True)
    print(f"   → {len(cohort_2022.venture_id)} ventures")

    print("\n2️⃣  Get 2022 cohort at a specific window:")
    print("   # Window 3: Cohort 2022 → End 2024")
    print("   window_data = ds.isel(window=3)")
    print("   at_risk_ventures = window_data.where(window_data.at_risk == 1, drop=True)")

    window_data = ds.isel(window=3)
    at_risk_ventures = window_data.where(window_data.at_risk == 1, drop=True)
    print(f"   → {len(at_risk_ventures.venture_id)} ventures at risk in this window")

    print("\n3️⃣  Count ventures at risk in each window:")
    print("   for w in range(len(ds.window)):")
    print("       n_at_risk = ds.at_risk.isel(window=w).sum().values")

    print(f"\n   Results:")
    for w in range(len(ds.window)):
        cohort = ds.cohort_year.isel(window=w).values
        end = ds.end_year.isel(window=w).values
        n_at_risk = ds.at_risk.isel(window=w).sum().values
        print(f"      Window {w} (Cohort {cohort}→{end}): {n_at_risk} ventures")

    # ─────────────────────────────────────────────────────────────────────────
    # STEP 9: Inspect at_risk in detail
    # ─────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 80)
    print("🔍 DETAILED at_risk INSPECTION")
    print("=" * 80)

    print("\nFirst 5 ventures:")
    print(f"{'Venture':<10} {'Series A':<12} {'at_risk across windows'}")
    print("-" * 60)

    for i in range(min(5, n_ventures)):
        series_a = series_a_years[i]
        at_risk_row = ds.at_risk.isel(venture_id=i).values
        at_risk_str = ' '.join([str(x) for x in at_risk_row])
        print(f"{i:<10} {series_a:<12} [{at_risk_str}]")

    print("\nWindows legend:")
    for w, (cohort, end) in enumerate(windows):
        print(f"  Position {w}: Cohort {cohort}")

    print("\n👀 Notice:")
    print("  - Each venture has at_risk=1 for only ONE cohort year")
    print("  - at_risk=1 repeats across different end_years for same cohort")
    print("  - This identifies which cohort_year the venture belongs to")

    # ─────────────────────────────────────────────────────────────────────────
    # DONE!
    # ─────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 80)
    print("✅ DEMO COMPLETE!")
    print("=" * 80)

    print("\n📚 Summary:")
    print("  • xarray.Dataset has shape: (ventures={}, windows={})".format(n_ventures, n_windows))
    print("  • series_A_year coordinate identifies each venture's cohort")
    print("  • at_risk variable marks which windows each venture is active in")
    print("  • No need for separate is_2021cohort, is_2022cohort variables!")

    print("\n🎯 Key advantages:")
    print("  ✓ Performance: One coordinate vs N dummy variables")
    print("  ✓ Clarity: Explicit cohort logic")
    print("  ✓ Flexibility: Easy to add new cohorts")
    print("  ✓ Validation: at_risk makes cohort assignment explicit")

    return ds


if __name__ == '__main__':
    import sys
    from pathlib import Path

    # Check file exists
    if not Path(DATA_FILE).exists():
        print(f"\n❌ File not found: {DATA_FILE}")
        print(f"\nPlease update DATA_FILE at the top of this script.")
        print(f"\nOr run with dummy data for demo:")
        print(f"  (Creating dummy data...)")

        # Create dummy data for demo
        dummy_df = pd.DataFrame({
            'CompanyID': range(100),
            'series_A_year': np.random.choice([2021, 2022, 2023], 100),
            'Sector': np.random.choice(['Quantum', 'AI', 'Biotech'], 100),
        })
        DATA_FILE = '/tmp/dummy_companies.parquet'
        dummy_df.to_parquet(DATA_FILE)
        print(f"  ✓ Created dummy data at {DATA_FILE}")
        print()

    try:
        ds = simple_demo()
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
