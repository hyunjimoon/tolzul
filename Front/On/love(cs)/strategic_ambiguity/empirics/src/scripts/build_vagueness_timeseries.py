#!/usr/bin/env python3
"""
Build Vagueness Time-Series Dataset
====================================

This script creates a NetCDF dataset tracking vagueness scores (V) across multiple
years for the same companies, enabling analysis of strategic commitment changes.

Input Files (from data/raw/):
- Company20211201.parquet  (2021 snapshot)
- Company20231201.dat      (2023 snapshot)
- Company20241201.dat      (2024 snapshot)
- Company20251101.dat      (2025 snapshot)

Output:
- data/processed/vagueness_timeseries.nc

Key Variables:
- V: Vagueness score [0-100]
- delta_V: Change in V from previous observation
- description: Raw description text

Usage:
    python build_vagueness_timeseries.py           # Full run (slow, ~hours)
    python build_vagueness_timeseries.py --test    # Test with 1000 companies
    python build_vagueness_timeseries.py --sample 10000  # Sample run

Author: Claude Code
Created: 2025-12-04
"""

import pandas as pd
import numpy as np
import xarray as xr
from pathlib import Path
from datetime import datetime
import sys
import argparse
from tqdm import tqdm

# Add src to path for vagueness scorer
sys.path.insert(0, str(Path(__file__).parent.parent))

# Constants
RAW_DIR = Path(__file__).parent.parent.parent / "data" / "raw"
PROCESSED_DIR = Path(__file__).parent.parent.parent / "data" / "processed"
OUTPUT_FILE = PROCESSED_DIR / "vagueness_timeseries.nc"

# File mappings
DATA_FILES = {
    2021: RAW_DIR / "Company20211201.parquet",
    2023: RAW_DIR / "Company20231201.dat",
    2024: RAW_DIR / "Company20241201.dat",
    2025: RAW_DIR / "Company20251101.dat",
}

# Columns to keep
KEEP_COLS = [
    'CompanyID', 'CompanyName', 'Description', 'Keywords',
    'TotalRaised', 'BusinessStatus', 'OwnershipStatus',
    'CompanyFinancingStatus', 'YearFounded', 'Employees',
    'HQCountry', 'LastFinancingDealType', 'FirstFinancingDealType',
    'FirstFinancingSize', 'LastFinancingSize'
]


def load_data_file(filepath: Path, year: int) -> pd.DataFrame:
    """Load a single data file (parquet or dat)."""
    print(f"  Loading {filepath.name}...")

    if filepath.suffix == '.parquet':
        df = pd.read_parquet(filepath)
    elif filepath.suffix == '.dat':
        df = pd.read_csv(filepath, sep='|', low_memory=False, on_bad_lines='skip')
    else:
        raise ValueError(f"Unknown file type: {filepath.suffix}")

    # Standardize column names
    df.columns = [c.strip() for c in df.columns]

    # Add year column
    df['snapshot_year'] = year

    # Keep only relevant columns
    available_cols = [c for c in KEEP_COLS if c in df.columns]
    df = df[available_cols + ['snapshot_year']].copy()

    print(f"    Loaded {len(df):,} companies")
    return df


def compute_vagueness_scores(descriptions: pd.Series, batch_size: int = 500) -> np.ndarray:
    """
    Compute vagueness scores for a series of descriptions.

    Uses HybridVaguenessScorerV2 which combines:
    - Market entropy (breadth of market positioning)
    - Technology abstractness (specificity of tech claims)
    """
    try:
        from vagueness_v2 import HybridVaguenessScorerV2
        scorer = HybridVaguenessScorerV2()
        use_scorer = True
        print("    Using HybridVaguenessScorerV2")
    except ImportError as e:
        print(f"    WARNING: Scorer not available ({e}), using length-based placeholder")
        use_scorer = False

    scores = np.full(len(descriptions), np.nan)

    # Process with progress bar
    for i in tqdm(range(len(descriptions)), desc="    Scoring", leave=False):
        desc = descriptions.iloc[i]
        if pd.notna(desc) and isinstance(desc, str) and len(desc.strip()) > 10:
            if use_scorer:
                try:
                    scores[i] = scorer.score(desc)
                except Exception:
                    scores[i] = np.nan
            else:
                # Placeholder: normalized length (longer = more specific typically)
                scores[i] = max(0, min(100, 100 - len(desc) / 50))

    return scores


def find_multi_year_companies(dfs: dict, min_years: int = 2) -> set:
    """Find companies appearing in at least min_years snapshots."""
    company_years = {}

    for year, df in dfs.items():
        for cid in df['CompanyID'].unique():
            if cid not in company_years:
                company_years[cid] = []
            company_years[cid].append(year)

    return {cid for cid, years in company_years.items() if len(years) >= min_years}


def build_timeseries_dataset(sample_size: int = None, full_panel_only: bool = True) -> xr.Dataset:
    """
    Build the main time-series dataset.

    Args:
        sample_size: If set, only process this many companies (for testing)
        full_panel_only: If True, only include companies with all 4 years
    """
    print("=" * 60)
    print("Building Vagueness Time-Series Dataset")
    print("=" * 60)

    # Step 1: Load all data files
    print("\n[Step 1] Loading data files...")
    dfs = {}
    for year, filepath in DATA_FILES.items():
        if filepath.exists():
            dfs[year] = load_data_file(filepath, year)
        else:
            print(f"  WARNING: {filepath} not found, skipping year {year}")

    years = sorted(dfs.keys())

    # Step 2: Find companies appearing in multiple years
    print("\n[Step 2] Finding companies with multiple observations...")

    if full_panel_only:
        # Only companies with ALL years
        common_ids = None
        for year, df in dfs.items():
            year_ids = set(df['CompanyID'].unique())
            if common_ids is None:
                common_ids = year_ids
            else:
                common_ids &= year_ids
        multi_year_companies = common_ids
        print(f"  Companies with all {len(years)} years: {len(multi_year_companies):,}")
    else:
        multi_year_companies = find_multi_year_companies(dfs, min_years=2)
        print(f"  Companies with 2+ years: {len(multi_year_companies):,}")

    # Step 3: Sample if requested
    if sample_size and sample_size < len(multi_year_companies):
        print(f"\n[Step 3] Sampling {sample_size:,} companies...")
        np.random.seed(42)
        multi_year_companies = set(np.random.choice(
            list(multi_year_companies), size=sample_size, replace=False
        ))

    companies = sorted(multi_year_companies)
    n_companies = len(companies)
    n_years = len(years)
    print(f"  Final sample: {n_companies:,} companies × {n_years} years")

    # Step 4: Create panel structure
    print("\n[Step 4] Creating panel structure...")
    company_to_idx = {cid: i for i, cid in enumerate(companies)}
    year_to_idx = {y: i for i, y in enumerate(years)}

    # Initialize arrays
    V = np.full((n_companies, n_years), np.nan)
    descriptions = np.full((n_companies, n_years), '', dtype=object)
    company_names = np.full(n_companies, '', dtype=object)
    total_raised = np.full((n_companies, n_years), np.nan)
    first_financing_size = np.full(n_companies, np.nan)
    financing_status = np.full((n_companies, n_years), '', dtype=object)

    # Fill in data
    for year, df in tqdm(dfs.items(), desc="  Processing years"):
        df_filtered = df[df['CompanyID'].isin(multi_year_companies)]
        j = year_to_idx[year]

        for _, row in df_filtered.iterrows():
            cid = row['CompanyID']
            if cid in company_to_idx:
                i = company_to_idx[cid]

                # Description
                desc = row.get('Description', '')
                descriptions[i, j] = desc if pd.notna(desc) else ''

                # Company name (take first non-empty)
                if company_names[i] == '' and pd.notna(row.get('CompanyName')):
                    company_names[i] = row['CompanyName']

                # Total raised
                tr = row.get('TotalRaised')
                if pd.notna(tr):
                    try:
                        total_raised[i, j] = float(tr)
                    except (ValueError, TypeError):
                        pass

                # First financing size (take from any year)
                if np.isnan(first_financing_size[i]):
                    ffs = row.get('FirstFinancingSize')
                    if pd.notna(ffs):
                        try:
                            first_financing_size[i] = float(ffs)
                        except (ValueError, TypeError):
                            pass

                # Financing status
                fs = row.get('CompanyFinancingStatus', '')
                financing_status[i, j] = fs if pd.notna(fs) else ''

    # Step 5: Compute vagueness scores
    print("\n[Step 5] Computing vagueness scores...")
    for j, year in enumerate(years):
        print(f"\n  Year {year}:")
        year_descriptions = pd.Series(descriptions[:, j])
        V[:, j] = compute_vagueness_scores(year_descriptions)

        valid = ~np.isnan(V[:, j])
        print(f"    Valid scores: {valid.sum():,} / {n_companies:,} ({valid.mean()*100:.1f}%)")
        if valid.sum() > 0:
            print(f"    Mean V: {np.nanmean(V[:, j]):.2f}, Std: {np.nanstd(V[:, j]):.2f}")

    # Step 6: Compute ΔV
    print("\n[Step 6] Computing ΔV (changes in vagueness)...")
    delta_V = np.full((n_companies, n_years), np.nan)
    for j in range(1, n_years):
        delta_V[:, j] = V[:, j] - V[:, j-1]

    # Also compute total change (first to last)
    V_first = V[:, 0]
    V_last = V[:, -1]
    total_delta_V = V_last - V_first

    # Step 7: Create xarray Dataset
    print("\n[Step 7] Creating xarray Dataset...")

    ds = xr.Dataset(
        data_vars={
            # Core vagueness variables
            'V': (['company', 'year'], V, {
                'long_name': 'Vagueness Score',
                'units': 'score [0-100]',
                'description': (
                    'Vagueness score computed by HybridVaguenessScorerV2. '
                    'Measures how specific vs. vague the company description is. '
                    'Low V (0-25): specific, verifiable claims (Analyst playbook). '
                    'High V (75-100): broad, flexible positioning (Believer playbook). '
                    'Middle V (25-75): murky middle (neither clear strategy).'
                ),
                'interpretation': (
                    'V captures communicative commitment level. Low V = high commitment '
                    'to specific claims. High V = high flexibility in positioning.'
                ),
                'scorer': 'HybridVaguenessScorerV2',
                'valid_range': [0, 100],
            }),

            'delta_V': (['company', 'year'], delta_V, {
                'long_name': 'Annual Change in Vagueness',
                'units': 'score change per year',
                'description': (
                    'Change in V from previous observation year. '
                    'ΔV > 0: becoming more vague (increasing flexibility). '
                    'ΔV < 0: becoming more specific (increasing commitment). '
                    'ΔV ≈ 0: stable strategy (possible lock-in).'
                ),
                'note': 'First year has NaN (no prior observation)',
            }),

            'total_delta_V': (['company'], total_delta_V, {
                'long_name': 'Total Change in Vagueness (First to Last)',
                'units': 'score change',
                'description': 'V_last - V_first. Overall strategic drift.',
            }),

            # Raw text
            'description': (['company', 'year'], descriptions, {
                'long_name': 'Company Description',
                'description': 'Raw description text from PitchBook snapshot.',
            }),

            # Company metadata
            'company_name': (['company'], company_names, {
                'long_name': 'Company Name',
            }),

            # Financial variables
            'total_raised': (['company', 'year'], total_raised, {
                'long_name': 'Total Capital Raised',
                'units': 'USD (millions)',
                'description': 'Cumulative funding raised as of snapshot date.',
            }),

            'first_financing_size': (['company'], first_financing_size, {
                'long_name': 'First Financing Size',
                'units': 'USD (millions)',
                'description': 'Size of first financing round. Proxy for early funding.',
            }),

            'financing_status': (['company', 'year'], financing_status, {
                'long_name': 'Financing Status',
                'description': 'Company financing status (e.g., Venture Capital, Private Equity).',
            }),
        },
        coords={
            'company': companies,
            'year': years,
        },
        attrs={
            # === DATASET OVERVIEW ===
            'title': 'Vagueness Time-Series Dataset',
            'description': (
                'Panel dataset tracking vagueness scores (V) for technology ventures '
                'across multiple years (2021-2025). Enables analysis of how strategic '
                'commitment (measured via communicative vagueness) changes over time, '
                'and how early funding affects strategic flexibility (ΔV).'
            ),

            # === SOURCE INFORMATION ===
            'source': 'PitchBook company snapshots',
            'source_files': ', '.join([f.name for f in DATA_FILES.values() if f.exists()]),
            'raw_data_dir': str(RAW_DIR),

            # === TEMPORAL COVERAGE ===
            'time_coverage_start': str(min(years)),
            'time_coverage_end': str(max(years)),
            'snapshot_years': str(years),
            'n_years': n_years,
            'panel_structure': 'Balanced panel (all companies have all years)' if full_panel_only else 'Unbalanced panel',

            # === SAMPLE INFORMATION ===
            'n_companies': n_companies,
            'n_total_observations': int(np.sum(~np.isnan(V))),
            'selection_criteria': (
                'Companies appearing in all 4 annual snapshots (2021, 2023, 2024, 2025) '
                'with valid descriptions.'
            ),

            # === METHODOLOGY ===
            'vagueness_scorer': 'HybridVaguenessScorerV2',
            'vagueness_methodology': (
                'Combines market entropy (breadth of market positioning) and '
                'technology abstractness (specificity of tech claims). '
                'Score range 0-100 where 0=maximally specific, 100=maximally vague.'
            ),
            'delta_v_definition': 'ΔV_t = V_t - V_{t-1}',
            'total_delta_v_definition': 'total_ΔV = V_last - V_first',

            # === KEY VARIABLES ===
            'key_variables': 'V (vagueness), delta_V (change), total_delta_V (drift), total_raised (funding)',

            # === INTERPRETATION GUIDE ===
            'interpretation_V': (
                'Low V (0-25): Analyst playbook - specific, verifiable claims. '
                'High V (75-100): Believer playbook - broad, flexible vision. '
                'Middle V (25-75): Murky middle - neither clear strategy.'
            ),
            'interpretation_delta_V': (
                'ΔV > 0: Becoming more flexible (strategic expansion). '
                'ΔV < 0: Becoming more committed (strategic narrowing). '
                'ΔV ≈ 0: Strategic lock-in (stopped optionality).'
            ),

            # === RESEARCH CONTEXT ===
            'research_context': (
                '🦾C (Commitment Trap) paper - testing Endogenous Appropriability hypothesis: '
                'early funding leads to strategic lock-in (reduced |ΔV|).'
            ),
            'primary_hypothesis': (
                'H_funding: Early funding is inversely related to |ΔV|. '
                'More early funding → less strategic flexibility → stopped optionality.'
            ),
            'secondary_hypothesis': (
                'H_trap: Middle V companies with high early funding have worst outcomes '
                '(funded trap - committed enough to attract scrutiny, not enough to satisfy it).'
            ),

            # === USAGE NOTES ===
            'usage_notes': (
                '1. Use V for cross-sectional analysis (U-shape in outcomes). '
                '2. Use delta_V for longitudinal analysis (strategic change). '
                '3. Use total_delta_V for overall strategic drift. '
                '4. Combine with first_financing_size to test funding-lock-in hypothesis.'
            ),

            # === CREATION METADATA ===
            'created_by': 'build_vagueness_timeseries.py',
            'created_at': datetime.now().isoformat(),
            'sample_size_used': str(sample_size) if sample_size else 'full',
            'conventions': 'CF-1.8',
            'contact': 'Generated for strategic_ambiguity/empirics project',
        }
    )

    return ds


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Build vagueness time-series dataset')
    parser.add_argument('--test', action='store_true', help='Test mode (1000 companies)')
    parser.add_argument('--sample', type=int, help='Sample size (default: full)')
    parser.add_argument('--output', type=str, help='Output file path')
    args = parser.parse_args()

    # Determine sample size
    if args.test:
        sample_size = 1000
        output_file = PROCESSED_DIR / "vagueness_timeseries_test.nc"
    elif args.sample:
        sample_size = args.sample
        output_file = PROCESSED_DIR / f"vagueness_timeseries_n{sample_size}.nc"
    else:
        sample_size = None
        output_file = OUTPUT_FILE

    if args.output:
        output_file = Path(args.output)

    print("\n" + "=" * 60)
    print("VAGUENESS TIME-SERIES BUILDER")
    print("=" * 60)
    print(f"Mode: {'Test' if args.test else 'Sample' if args.sample else 'Full'}")
    print(f"Sample size: {sample_size if sample_size else 'All companies'}")
    print(f"Output: {output_file}")

    # Check input files
    print("\nInput files:")
    for year, filepath in DATA_FILES.items():
        status = "✓" if filepath.exists() else "✗"
        size = f"({filepath.stat().st_size / 1024 / 1024:.1f} MB)" if filepath.exists() else "(missing)"
        print(f"  {status} {year}: {filepath.name} {size}")

    # Build dataset
    ds = build_timeseries_dataset(sample_size=sample_size)

    # Summary statistics
    print("\n" + "=" * 60)
    print("DATASET SUMMARY")
    print("=" * 60)
    print(f"Dimensions: {dict(ds.dims)}")
    print(f"Companies: {ds.dims['company']:,}")
    print(f"Years: {list(ds.coords['year'].values)}")
    print(f"Total V observations: {int(np.sum(~np.isnan(ds['V'].values))):,}")

    # V statistics by year
    print("\nV statistics by year:")
    for i, year in enumerate(ds.coords['year'].values):
        v_year = ds['V'][:, i].values
        valid = ~np.isnan(v_year)
        if valid.sum() > 0:
            print(f"  {year}: n={valid.sum():,}, mean={np.nanmean(v_year):.1f}, "
                  f"std={np.nanstd(v_year):.1f}, "
                  f"Q1={np.nanpercentile(v_year, 25):.1f}, "
                  f"median={np.nanmedian(v_year):.1f}, "
                  f"Q3={np.nanpercentile(v_year, 75):.1f}")

    # ΔV statistics
    print("\nΔV statistics:")
    for i in range(1, len(ds.coords['year'])):
        year = ds.coords['year'].values[i]
        prev_year = ds.coords['year'].values[i-1]
        dv = ds['delta_V'][:, i].values
        valid = ~np.isnan(dv)
        if valid.sum() > 0:
            dv_valid = dv[valid]
            print(f"  {prev_year}→{year}: n={valid.sum():,}, "
                  f"mean={np.mean(dv_valid):.2f}, std={np.std(dv_valid):.2f}, "
                  f"ΔV>0: {(dv_valid > 0).mean()*100:.1f}%, "
                  f"ΔV<0: {(dv_valid < 0).mean()*100:.1f}%, "
                  f"|ΔV|<5: {(np.abs(dv_valid) < 5).mean()*100:.1f}%")

    # Total ΔV
    total_dv = ds['total_delta_V'].values
    valid_total = ~np.isnan(total_dv)
    if valid_total.sum() > 0:
        tdv = total_dv[valid_total]
        print(f"\nTotal ΔV (2021→2025): n={valid_total.sum():,}, "
              f"mean={np.mean(tdv):.2f}, std={np.std(tdv):.2f}")

    # Save dataset
    print(f"\nSaving to {output_file}...")
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    # Drop text variables for NetCDF (they cause encoding issues)
    # Create a separate parquet for text data if needed
    ds_numeric = ds.drop_vars(['description', 'company_name', 'financing_status'], errors='ignore')

    # Save numeric-only dataset to NetCDF
    ds_numeric.to_netcdf(output_file)

    # Also save full dataset with text to parquet for reference
    parquet_file = output_file.with_suffix('.parquet')
    print(f"Saving text data to {parquet_file}...")
    # Convert to DataFrame for parquet - handle 1D and 2D variables
    df_list = []
    years_list = list(ds.coords['year'].values)
    for i, company in enumerate(ds.coords['company'].values):
        for j, year in enumerate(years_list):
            row = {
                'company_id': str(company),
                'year': int(year),
            }
            # Handle 2D variables (company, year)
            for var in ['V', 'delta_V', 'description']:
                if var in ds and len(ds[var].dims) == 2:
                    val = ds[var].values[i, j]
                    if isinstance(val, (float, np.floating)) and np.isnan(val):
                        row[var] = None
                    else:
                        row[var] = val
            # Handle 1D variables (company only) - same for all years
            for var in ['company_name', 'total_raised', 'first_financing_size', 'financing_status', 'total_delta_V']:
                if var in ds and len(ds[var].dims) == 1:
                    val = ds[var].values[i]
                    if isinstance(val, (float, np.floating)) and np.isnan(val):
                        row[var] = None
                    else:
                        row[var] = val
            df_list.append(row)

    df_full = pd.DataFrame(df_list)
    df_full.to_parquet(parquet_file, index=False)
    print(f"Saved parquet with {len(df_full):,} rows")

    file_size = output_file.stat().st_size / 1024 / 1024
    print(f"Saved! File size: {file_size:.1f} MB")

    print("\n" + "=" * 60)
    print("DONE!")
    print("=" * 60)
    print(f"\nTo load this dataset:")
    print(f"  import xarray as xr")
    print(f"  ds = xr.open_dataset('{output_file}')")
    print(f"  print(ds.attrs)  # View metadata")

    return ds


if __name__ == "__main__":
    main()
