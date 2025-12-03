#!/usr/bin/env python3
"""
Explore xarray Structure - Interactive Demo
============================================

This script constructs an xarray.Dataset from your parquet file and
provides interactive exploration to understand the data structure.

Usage:
    python explore_xarray_structure.py

This will:
1. Load your parquet file
2. Construct xarray.Dataset with venture_id × window
3. Show structure and provide exploration examples
4. Demonstrate at_risk calculation
"""

import pandas as pd
import numpy as np
import xarray as xr
from pathlib import Path
import sys

# Your local file path
DATA_FILE = "/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/data/raw/consolidated_companies_2022_2024_2025_quantum.parquet"


def load_and_inspect_parquet(filepath):
    """Load parquet and show basic info."""
    print("=" * 80)
    print("📂 LOADING PARQUET FILE")
    print("=" * 80)
    print(f"\nFile: {filepath}\n")

    df = pd.read_parquet(filepath)

    print(f"✓ Loaded {len(df):,} rows × {len(df.columns)} columns")
    print(f"\nFirst 5 column names:")
    for i, col in enumerate(df.columns[:5], 1):
        print(f"  {i}. {col}")

    print(f"\nAll columns ({len(df.columns)} total):")
    for i, col in enumerate(df.columns, 1):
        dtype = df[col].dtype
        n_missing = df[col].isna().sum()
        pct_missing = (n_missing / len(df)) * 100
        print(f"  {i:2d}. {col:<30} {str(dtype):<15} {pct_missing:5.1f}% missing")

    return df


def identify_key_columns(df):
    """Identify which columns we'll use for xarray construction."""
    print("\n" + "=" * 80)
    print("🔍 IDENTIFYING KEY COLUMNS")
    print("=" * 80)

    # Map column names (case-insensitive search)
    column_map = {}

    # Company ID
    for col in ['CompanyID', 'company_id', 'id', 'CompanyId']:
        if col in df.columns:
            column_map['company_id'] = col
            break

    # Series A Year
    for col in ['SeriesAYear', 'series_a_year', 'series_A_year', 'YearFounded', 'year_founded']:
        if col in df.columns:
            column_map['series_a_year'] = col
            break

    # Description (for vagueness)
    for col in ['Description', 'description', 'PrimaryDescription']:
        if col in df.columns:
            column_map['description'] = col
            break

    # Keywords
    for col in ['Keywords', 'keywords', 'Tags']:
        if col in df.columns:
            column_map['keywords'] = col
            break

    # Employees
    for col in ['Employees', 'employees', 'EmployeeCount']:
        if col in df.columns:
            column_map['employees'] = col
            break

    # Sector
    for col in ['Sector', 'sector', 'PrimarySector', 'Industry']:
        if col in df.columns:
            column_map['sector'] = col
            break

    # Country
    for col in ['HQCountry', 'hq_country', 'Country', 'country']:
        if col in df.columns:
            column_map['country'] = col
            break

    # Founding Year
    for col in ['YearFounded', 'year_founded', 'FoundingYear', 'founded']:
        if col in df.columns:
            column_map['founding_year'] = col
            break

    print("\n✓ Mapped columns:")
    for key, col in column_map.items():
        coverage = (df[col].notna().sum() / len(df)) * 100
        print(f"  {key:<20} → {col:<30} ({coverage:.1f}% coverage)")

    if len(column_map) < 3:
        print("\n⚠️  Warning: Could not find enough key columns!")
        print("Available columns:", list(df.columns))

    return column_map


def construct_minimal_xarray(df, column_map):
    """Construct minimal xarray.Dataset to demonstrate structure."""
    print("\n" + "=" * 80)
    print("🏗️  CONSTRUCTING XARRAY.DATASET")
    print("=" * 80)

    # Get company IDs
    id_col = column_map.get('company_id')
    if id_col:
        venture_ids = df[id_col].values[:1000]  # Use first 1000 for demo
        df_subset = df.head(1000).copy()
    else:
        venture_ids = np.arange(len(df[:1000]))
        df_subset = df.head(1000).copy()

    n_ventures = len(venture_ids)
    print(f"\n📊 Using {n_ventures:,} ventures (subset for demo)")

    # Define cohort years and horizons
    cohort_years = [2021, 2022, 2023]
    horizon_years = [1, 2, 3]  # Years after Series A

    print(f"\n⏰ Window structure:")
    print(f"  Cohort years: {cohort_years}")
    print(f"  Horizon years: {horizon_years} (years after Series A)")

    # Create window combinations
    windows = []
    window_cohort_years = []
    window_end_years = []
    window_horizons = []

    for cohort_year in cohort_years:
        for horizon in horizon_years:
            end_year = cohort_year + horizon
            windows.append((cohort_year, end_year))
            window_cohort_years.append(cohort_year)
            window_end_years.append(end_year)
            window_horizons.append(horizon)

    n_windows = len(windows)
    window_ids = np.arange(n_windows)

    print(f"\n  Total windows: {n_windows}")
    print(f"  Window combinations:")
    for cohort, end in windows:
        print(f"    Cohort {cohort} → End {end} (horizon: {end - cohort} years)")

    # Extract Series A years (needed before dataset creation)
    series_a_col = column_map.get('series_a_year', column_map.get('founding_year'))
    if series_a_col:
        series_a_years = pd.to_numeric(df_subset[series_a_col], errors='coerce').fillna(2020).astype(int).values
    else:
        # Random for demo
        series_a_years = np.random.choice(cohort_years, size=n_ventures)

    # Initialize dataset
    print(f"\n🔧 Creating xarray.Dataset...")

    ds = xr.Dataset(
        coords={
            'venture_id': venture_ids,
            'window': window_ids,
            'series_A_year': ('venture_id', series_a_years),
            'cohort_year': ('window', window_cohort_years),
            'end_year': ('window', window_end_years),
            'horizon_years': ('window', window_horizons),
        }
    )

    # Add sector
    sector_col = column_map.get('sector')
    if sector_col:
        sectors = df_subset[sector_col].fillna('Unknown').values
    else:
        sectors = np.array(['Quantum'] * n_ventures)

    ds.coords['sector'] = ('venture_id', sectors)

    # Add country
    country_col = column_map.get('country')
    if country_col:
        countries = df_subset[country_col].fillna('Unknown').values
    else:
        countries = np.array(['USA'] * n_ventures)

    ds.coords['hq_country'] = ('venture_id', countries)

    print(f"✓ Created coordinates:")
    print(f"  Venture-level: venture_id, series_A_year, sector, hq_country")
    print(f"  Window-level: cohort_year, end_year, horizon_years")

    # Compute at_risk variable
    print(f"\n🎯 Computing at_risk variable...")
    print(f"  Logic: at_risk[i,w] = 1 if series_A_year[i] == cohort_year[w]")

    at_risk = np.zeros((n_ventures, n_windows), dtype=np.int8)

    for w, (cohort_year, end_year) in enumerate(windows):
        at_risk[:, w] = (series_a_years == cohort_year).astype(np.int8)

    ds['at_risk'] = (('venture_id', 'window'), at_risk)

    # Verify at_risk
    print(f"\n  Verification:")
    for cohort_year in cohort_years:
        n_in_cohort = (series_a_years == cohort_year).sum()
        print(f"    Cohort {cohort_year}: {n_in_cohort} ventures")

    # Add static variables
    print(f"\n📊 Adding variables...")

    # Employees
    emp_col = column_map.get('employees')
    if emp_col:
        employees = pd.to_numeric(df_subset[emp_col], errors='coerce').fillna(10).values
        z_employees_log = np.log1p(employees)
        z_employees_log = (z_employees_log - z_employees_log.mean()) / (z_employees_log.std() + 1e-6)
        ds['z_employees_log'] = ('venture_id', z_employees_log.astype(np.float32))
        print(f"  ✓ z_employees_log (standardized log)")

    # Founding year
    founding_col = column_map.get('founding_year')
    if founding_col:
        founding_years = pd.to_numeric(df_subset[founding_col], errors='coerce').fillna(2020).astype(np.int16).values
        ds['founding_year'] = ('venture_id', founding_years)
        print(f"  ✓ founding_year")

    # Placeholder vagueness (would be computed by scorer)
    np.random.seed(42)
    vagueness_raw = np.random.randn(n_ventures).astype(np.float32)
    z_vagueness = (vagueness_raw - vagueness_raw.mean()) / vagueness_raw.std()
    ds['z_vagueness'] = ('venture_id', z_vagueness)
    print(f"  ✓ z_vagueness (demo: random values)")

    # Placeholder is_software (would be inferred from keywords)
    is_software = np.random.choice([0, 1], size=n_ventures).astype(np.int8)
    ds['is_software'] = ('venture_id', is_software)
    print(f"  ✓ is_software (demo: random values)")

    # Time-varying outcome: L (Series B+ reached)
    print(f"\n  Time-varying variables:")

    # L: Series B+ reached (time-varying)
    L = np.zeros((n_ventures, n_windows), dtype=np.float32)

    # Simulate: ventures reach Series B with some probability that increases with horizon
    for w, (cohort_year, end_year) in enumerate(windows):
        horizon = end_year - cohort_year
        # Only ventures in this cohort (at_risk=1) can reach Series B
        prob_series_b = 0.1 * horizon  # 10% per year
        L[:, w] = (at_risk[:, w] == 1) * (np.random.rand(n_ventures) < prob_series_b)

    ds['L'] = (('venture_id', 'window'), L)
    print(f"  ✓ L (Series B+ reached, demo: simulated)")

    # Add attributes
    ds.attrs['schema_version'] = 'esi-panel.v4'
    ds.attrs['window_logic'] = 'at_risk[i,w]=1 iff series_A_year[i]==cohort_year[w]'
    ds.attrs['description'] = 'Demo xarray.Dataset for exploring structure'
    ds.attrs['cohort_years'] = cohort_years
    ds.attrs['horizon_years'] = horizon_years

    print(f"\n✓ Dataset constructed!")

    return ds, df_subset


def explore_dataset(ds):
    """Interactive exploration of the dataset."""
    print("\n" + "=" * 80)
    print("🔍 EXPLORING XARRAY.DATASET STRUCTURE")
    print("=" * 80)

    print("\n" + "─" * 80)
    print("📐 Dataset Overview")
    print("─" * 80)
    print(ds)

    print("\n" + "─" * 80)
    print("📊 Dimensions")
    print("─" * 80)
    for dim, size in ds.dims.items():
        print(f"  {dim}: {size:,}")

    print("\n" + "─" * 80)
    print("🗺️  Coordinates (venture-level)")
    print("─" * 80)
    print(f"  series_A_year range: {ds.series_A_year.min().values} - {ds.series_A_year.max().values}")
    print(f"  series_A_year distribution:")
    for year in sorted(ds.series_A_year.values):
        if year != 0:  # Skip missing
            count = (ds.series_A_year == year).sum().values
            if count > 0:
                print(f"    {year}: {count} ventures")

    print(f"\n  sectors: {len(np.unique(ds.sector.values))} unique")
    sector_counts = pd.Series(ds.sector.values).value_counts()
    print(f"  Top 5 sectors:")
    for sector, count in sector_counts.head(5).items():
        print(f"    {sector}: {count}")

    print(f"\n  countries: {len(np.unique(ds.hq_country.values))} unique")
    country_counts = pd.Series(ds.hq_country.values).value_counts()
    print(f"  Top 5 countries:")
    for country, count in country_counts.head(5).items():
        print(f"    {country}: {count}")

    print("\n" + "─" * 80)
    print("⏰ Coordinates (window-level)")
    print("─" * 80)
    print(f"  cohort_year: {sorted(set(ds.cohort_year.values))}")
    print(f"  end_year: {sorted(set(ds.end_year.values))}")
    print(f"  horizon_years: {sorted(set(ds.horizon_years.values))}")

    print(f"\n  Window structure ({len(ds.window)} total):")
    for i, window in enumerate(ds.window.values):
        cohort = ds.cohort_year.isel(window=i).values
        end = ds.end_year.isel(window=i).values
        horizon = ds.horizon_years.isel(window=i).values
        print(f"    Window {i}: Cohort {cohort} → End {end} (horizon={horizon})")

    print("\n" + "─" * 80)
    print("📊 Data Variables")
    print("─" * 80)
    for var in ds.data_vars:
        dims = ds[var].dims
        shape = ds[var].shape
        dtype = ds[var].dtype

        # Count non-zero/non-nan
        values = ds[var].values
        if np.issubdtype(dtype, np.floating):
            n_nonzero = (~np.isnan(values)).sum()
        else:
            n_nonzero = (values != 0).sum()

        print(f"  {var}:")
        print(f"    Dimensions: {dims}")
        print(f"    Shape: {shape}")
        print(f"    Dtype: {dtype}")
        print(f"    Non-zero/Non-nan: {n_nonzero:,}")

        if var == 'at_risk':
            # Show at_risk statistics
            print(f"    Total at_risk=1: {(values == 1).sum():,}")
            print(f"    By cohort:")
            for i, cohort_year in enumerate(sorted(set(ds.cohort_year.values))):
                cohort_windows = ds.cohort_year == cohort_year
                n_at_risk = ds['at_risk'].sel(window=cohort_windows).sum().values
                print(f"      Cohort {cohort_year}: {n_at_risk:,} at-risk observations")


def demonstrate_usage(ds):
    """Demonstrate how to use the dataset."""
    print("\n" + "=" * 80)
    print("💡 USAGE EXAMPLES")
    print("=" * 80)

    print("\n" + "─" * 80)
    print("Example 1: Select a specific cohort")
    print("─" * 80)

    cohort_year = 2022
    print(f"\nCode:")
    print(f"  cohort_2022 = ds.where(ds.cohort_year == {cohort_year}, drop=True)")

    cohort_2022 = ds.where(ds.cohort_year == cohort_year, drop=True)

    print(f"\nResult:")
    print(f"  Windows in cohort: {len(cohort_2022.window)}")
    print(f"  Ventures at risk: {cohort_2022.at_risk.sum().values}")

    print("\n" + "─" * 80)
    print("Example 2: Get ventures in 2022 cohort only")
    print("─" * 80)

    print(f"\nCode:")
    print(f"  ventures_2022 = ds.where(ds.series_A_year == {cohort_year}, drop=True)")

    ventures_2022 = ds.where(ds.series_A_year == cohort_year, drop=True)

    print(f"\nResult:")
    print(f"  Ventures with Series A in {cohort_year}: {len(ventures_2022.venture_id)}")
    print(f"  Their sectors: {np.unique(ventures_2022.sector.values)[:5]}")

    print("\n" + "─" * 80)
    print("Example 3: Analyze Series B success by horizon")
    print("─" * 80)

    print(f"\nCode:")
    print(f"  for horizon in [1, 2, 3]:")
    print(f"      windows_h = ds.where(ds.horizon_years == horizon, drop=True)")
    print(f"      success_rate = windows_h.L.mean().values")

    print(f"\nResult:")
    for horizon in sorted(set(ds.horizon_years.values)):
        windows_h = ds.where(ds.horizon_years == horizon, drop=True)
        success_rate = windows_h.L.mean().values * 100
        print(f"  Horizon {horizon} years: {success_rate:.1f}% reached Series B+")

    print("\n" + "─" * 80)
    print("Example 4: Test vagueness effect (H2 model)")
    print("─" * 80)

    print(f"\nCode:")
    print(f"  # Select a specific window")
    print(f"  window_idx = 4  # Cohort 2022, End 2024")
    print(f"  data = ds.isel(window=window_idx)")
    print(f"  ")
    print(f"  # Get ventures at risk in this window")
    print(f"  at_risk_mask = data.at_risk == 1")
    print(f"  analysis_data = data.where(at_risk_mask, drop=True)")

    window_idx = 4
    data = ds.isel(window=window_idx)
    at_risk_mask = data.at_risk == 1
    analysis_data = data.where(at_risk_mask, drop=True)

    cohort = data.cohort_year.values
    end = data.end_year.values

    print(f"\nResult:")
    print(f"  Window: Cohort {cohort} → End {end}")
    print(f"  Ventures at risk: {analysis_data.at_risk.sum().values}")
    print(f"  Reached Series B+: {analysis_data.L.sum().values}")
    print(f"  Success rate: {analysis_data.L.mean().values * 100:.1f}%")

    # Simulate simple correlation
    vagueness = analysis_data.z_vagueness.values.flatten()
    outcome = analysis_data.L.values.flatten()

    # Remove NaN
    mask = ~(np.isnan(vagueness) | np.isnan(outcome))
    if mask.sum() > 10:
        corr = np.corrcoef(vagueness[mask], outcome[mask])[0, 1]
        print(f"\n  Correlation(vagueness, Series B+): {corr:.3f}")

    print("\n" + "─" * 80)
    print("Example 5: Compare HW vs SW ventures")
    print("─" * 80)

    print(f"\nCode:")
    print(f"  hw_ventures = ds.where(ds.is_software == 0, drop=True)")
    print(f"  sw_ventures = ds.where(ds.is_software == 1, drop=True)")

    hw_ventures = ds.where(ds.is_software == 0, drop=True)
    sw_ventures = ds.where(ds.is_software == 1, drop=True)

    print(f"\nResult:")
    print(f"  Hardware ventures: {len(hw_ventures.venture_id)}")
    print(f"  Software ventures: {len(sw_ventures.venture_id)}")

    # Calculate success rates (only where at_risk=1)
    hw_success = hw_ventures.L.where(hw_ventures.at_risk == 1).mean().values * 100
    sw_success = sw_ventures.L.where(sw_ventures.at_risk == 1).mean().values * 100

    print(f"\n  Series B+ success rates (where at_risk):")
    print(f"    Hardware: {hw_success:.1f}%")
    print(f"    Software: {sw_success:.1f}%")


def save_for_inspection(ds, output_file="xarray_demo.nc"):
    """Save dataset for later inspection."""
    print("\n" + "=" * 80)
    print("💾 SAVING DATASET")
    print("=" * 80)

    print(f"\nSaving to: {output_file}")
    ds.to_netcdf(output_file)

    file_size = Path(output_file).stat().st_size / 1e6
    print(f"✓ Saved ({file_size:.1f} MB)")

    print(f"\nTo reload later:")
    print(f"  import xarray as xr")
    print(f"  ds = xr.open_dataset('{output_file}')")
    print(f"  print(ds)")


def main():
    """Main execution."""
    print("\n" + "█" * 80)
    print("█" + " " * 78 + "█")
    print("█" + "  XARRAY STRUCTURE EXPLORER - Interactive Demo".center(78) + "█")
    print("█" + " " * 78 + "█")
    print("█" * 80)

    # Check if file exists
    if not Path(DATA_FILE).exists():
        print(f"\n❌ File not found: {DATA_FILE}")
        print(f"\nPlease update DATA_FILE path at the top of this script.")
        return 1

    try:
        # Load and inspect
        df = load_and_inspect_parquet(DATA_FILE)

        # Identify columns
        column_map = identify_key_columns(df)

        # Construct xarray
        ds, df_subset = construct_minimal_xarray(df, column_map)

        # Explore structure
        explore_dataset(ds)

        # Demonstrate usage
        demonstrate_usage(ds)

        # Save
        save_for_inspection(ds)

        print("\n" + "█" * 80)
        print("█" + " " * 78 + "█")
        print("█" + "  ✅ EXPLORATION COMPLETE!".center(78) + "█")
        print("█" + " " * 78 + "█")
        print("█" * 80)

        print("\n📚 Next steps:")
        print("  1. Review the structure above")
        print("  2. Load the saved file: ds = xr.open_dataset('xarray_demo.nc')")
        print("  3. Try the examples with your own queries")
        print("  4. Compute real vagueness scores using vagueness_v2.py")
        print("  5. Infer is_software from keywords/description")
        print("  6. Track real Series B+ progression for L variable")
        print("  7. Run specification curve analysis")

        return 0

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
