"""
Feature Engineering Module (W1 refactor)

- Vagueness: StrategicVaguenessScorer (Lo&McD 2011; Pan et al. 2018; Zuckerman 1999 based)
- Moderator: is_hardware (1=Integrated/Hardware, 0=Non-integrated/Software)
- DV stitching remains (Series B+ progression); we expose as 'growth'
- S (Step-up): PreMoney_t / PostMoney_{t-1} (Nanda 2024 definition)
"""

import pandas as pd
import numpy as np
import re
import logging
from pathlib import Path
from typing import Union, List, Optional, Tuple
from datetime import datetime

# Configure logging
logger = logging.getLogger(__name__)

# =========================================================
# 1🏗️BUILD: Data Consolidation from .dat files
# =========================================================

def load_company_snapshot(filepath: Path) -> pd.DataFrame:
    """Load single company .dat file with proper parsing.

    Args:
        filepath: Path to CompanyYYYYMMDD.dat file

    Returns:
        DataFrame with parsed company data

    Example:
        >>> df = load_company_snapshot(Path('data/raw/Company20211201.dat'))
        >>> print(df.shape)
        (50000, 95)
    """
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    # Parse pipe-delimited format
    df = pd.read_csv(filepath, sep='|', low_memory=False, encoding='utf-8')

    # Extract date from filename (e.g., Company20211201.dat → 2021-12-01)
    date_str = filepath.stem.replace('Company', '')
    df['snapshot_date'] = pd.to_datetime(date_str, format='%Y%m%d')

    logger.info(f"  Loaded {filepath.name}: {len(df):,} companies")
    return df


def consolidate_company_snapshots(
    data_dir: Union[str, Path],
    use_cache: bool = True,
    save_parquet: bool = True,
    years: Optional[List[int]] = None
) -> pd.DataFrame:
    """Merge all Company*.dat files into longitudinal dataset.

    This function:
    1. Checks for cached .parquet file first (fast load)
    2. If no cache, finds all Company*.dat files in the directory
    3. Optionally filters for specific years only (for faster loading)
    4. Loads each snapshot with its date
    5. Stacks all snapshots chronologically
    6. Keeps most recent info per company
    7. Optionally saves to .parquet for future fast loading

    Args:
        data_dir: Directory containing .dat files
        use_cache: If True, try to load from cached .parquet file first
        save_parquet: If True, save consolidated data to .parquet file
        years: Optional list of years to load (e.g., [2022, 2024, 2025]).
               If None, loads all available years.

    Returns:
        Consolidated DataFrame with all snapshots, keeping latest info per company

    Example:
        >>> # Load all years (default)
        >>> df = consolidate_company_snapshots('data/raw')

        >>> # Load only 2022, 2024, 2025 (faster!)
        >>> df = consolidate_company_snapshots('data/raw', years=[2022, 2024, 2025])

        >>> # Second run: loads from cache (much faster!)
        >>> df = consolidate_company_snapshots('data/raw')
    """
    data_path = Path(data_dir)
    if not data_path.exists():
        raise FileNotFoundError(f"Directory not found: {data_path}")

    # Define cache path (include years in cache name if filtering)
    if years:
        years_str = '_'.join(map(str, sorted(years)))
        cache_filename = f'consolidated_companies_{years_str}.parquet'
    else:
        cache_filename = 'consolidated_companies.parquet'

    cache_path = data_path.parent / 'processed' / cache_filename

    # Try to load from cache first
    if use_cache and cache_path.exists():
        logger.info(f"Loading cached data from {cache_path}...")
        try:
            df = pd.read_parquet(cache_path)
            logger.info(f"✓ Loaded {len(df):,} companies from cache (fast load!)")
            logger.info(f"  Date range: {df['snapshot_date'].min()} to {df['snapshot_date'].max()}")
            return df
        except Exception as e:
            logger.warning(f"Failed to load parquet cache: {e}. Trying pickle...")

            # Try pickle format as fallback
            pickle_path = cache_path.with_suffix('.pkl')
            if pickle_path.exists():
                try:
                    df = pd.read_pickle(pickle_path)
                    logger.info(f"✓ Loaded {len(df):,} companies from pickle cache")
                    logger.info(f"  Date range: {df['snapshot_date'].min()} to {df['snapshot_date'].max()}")
                    return df
                except Exception as e2:
                    logger.warning(f"Failed to load pickle cache: {e2}. Proceeding with .dat files...")
            else:
                logger.warning("No pickle cache found. Proceeding with .dat files...")

    # Find all Company*.dat files
    all_files = sorted(data_path.glob('Company*.dat'))

    # Filter by years if specified
    if years:
        logger.info(f"Filtering for years: {years}")
        company_files = []
        for filepath in all_files:
            # Extract year from filename (e.g., Company20220101.dat → 2022)
            date_str = filepath.stem.replace('Company', '')
            if len(date_str) >= 4:
                file_year = int(date_str[:4])
                if file_year in years:
                    company_files.append(filepath)

        logger.info(f"Selected {len(company_files)}/{len(all_files)} files matching years {years}")
    else:
        company_files = all_files

    if not company_files:
        logger.warning(f"No Company*.dat files found in {data_path}")
        logger.info("Attempting to use processed data instead...")
        return None

    logger.info(f"Found {len(company_files)} company snapshots")

    # Load all snapshots
    dfs = []
    for filepath in company_files:
        try:
            df = load_company_snapshot(filepath)
            dfs.append(df)
        except Exception as e:
            logger.error(f"  Failed to load {filepath.name}: {e}")
            continue

    if not dfs:
        raise ValueError("No company snapshots successfully loaded")

    # Stack snapshots chronologically
    df_all = pd.concat(dfs, axis=0, ignore_index=True)
    logger.info(f"Total snapshots stacked: {len(df_all):,} rows")

    # Keep most recent info per company
    id_col = 'CompanyID' if 'CompanyID' in df_all.columns else 'company_id'
    df_latest = (df_all
                 .sort_values([id_col, 'snapshot_date'])
                 .drop_duplicates(subset=id_col, keep='last'))

    logger.info(f"Consolidated {len(df_latest):,} unique companies")
    logger.info(f"Date range: {df_latest['snapshot_date'].min()} to {df_latest['snapshot_date'].max()}")

    # Save to parquet for fast future loading
    if save_parquet:
        cache_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            df_latest.to_parquet(cache_path, index=False, engine='pyarrow')
            logger.info(f"✓ Saved cache to {cache_path} for future fast loading")

            # Report file sizes
            import os
            parquet_size = os.path.getsize(cache_path) / 1024**2
            logger.info(f"  Parquet size: {parquet_size:.1f} MB")
        except ImportError:
            # Fallback to pickle if pyarrow not available
            logger.warning("⚠️  pyarrow not found. Using pickle format instead (slower but works).")
            pickle_path = cache_path.with_suffix('.pkl')
            df_latest.to_pickle(pickle_path)
            logger.info(f"✓ Saved cache to {pickle_path} (pickle format)")

            import os
            pickle_size = os.path.getsize(pickle_path) / 1024**2
            logger.info(f"  Pickle size: {pickle_size:.1f} MB")
            logger.info("  💡 Install pyarrow for better performance: pip install pyarrow")

    return df_latest


def consolidate_quantum_snapshots(
    data_dir: Union[str, Path],
    use_cache: bool = True,
    save_parquet: bool = True,
    years: Optional[List[int]] = None
) -> pd.DataFrame:
    """
    Load and consolidate quantum company snapshots with caching.

    This is a specialized version of consolidate_company_snapshots that:
    1. Loads all company snapshots
    2. Filters for quantum companies only
    3. Caches to quantum_companies_*.parquet for fast reloading

    Args:
        data_dir: Directory containing Company*.dat files
        use_cache: Load from cache if available (default: True)
        save_parquet: Save consolidated data to parquet cache (default: True)
        years: Optional list of years to load (e.g., [2022, 2024, 2025])
               If None, loads all available years

    Returns:
        DataFrame with consolidated quantum company snapshots

    Example:
        >>> # First run: slow (reads .dat files, filters, creates cache)
        >>> df_quantum = consolidate_quantum_snapshots('data/raw', years=[2022, 2024, 2025])
        >>> # Subsequent runs: fast (reads from cache)
        >>> df_quantum = consolidate_quantum_snapshots('data/raw', years=[2022, 2024, 2025])
    """
    data_path = Path(data_dir)

    if not data_path.exists():
        raise FileNotFoundError(f"Data directory not found: {data_path}")

    # Determine cache filename based on years
    if years:
        years_str = '_'.join(map(str, sorted(years)))
        cache_filename = f'quantum_companies_{years_str}.parquet'
    else:
        cache_filename = 'quantum_companies.parquet'

    cache_path = data_path.parent / 'processed' / cache_filename
    cache_path.parent.mkdir(parents=True, exist_ok=True)

    # Try to load from cache first
    if use_cache and cache_path.exists():
        logger.info(f"Loading quantum cache from {cache_path}...")
        try:
            df = pd.read_parquet(cache_path)
            logger.info(f"✓ Loaded {len(df):,} quantum companies from cache (fast load!)")
            logger.info(f"  Date range: {df['snapshot_date'].min()} to {df['snapshot_date'].max()}")
            return df
        except Exception as e:
            logger.warning(f"Failed to load parquet cache: {e}. Trying pickle...")

            # Try pickle format as fallback
            pickle_path = cache_path.with_suffix('.pkl')
            if pickle_path.exists():
                try:
                    df = pd.read_pickle(pickle_path)
                    logger.info(f"✓ Loaded {len(df):,} quantum companies from pickle cache")
                    logger.info(f"  Date range: {df['snapshot_date'].min()} to {df['snapshot_date'].max()}")
                    return df
                except Exception as e2:
                    logger.warning(f"Failed to load pickle cache: {e2}. Proceeding with .dat files...")
            else:
                logger.warning("No pickle cache found. Proceeding with .dat files...")

    # If no cache, load from .dat files and filter for quantum
    logger.info("No quantum cache found. Loading from .dat files and filtering...")

    # Load all company snapshots
    df_all = consolidate_company_snapshots(
        data_dir=data_dir,
        use_cache=use_cache,  # Use regular cache for full dataset
        save_parquet=save_parquet,
        years=years
    )

    # Filter for quantum companies
    logger.info("\nFiltering for quantum companies...")
    df_quantum = filter_quantum_companies(df_all)

    logger.info(f"\n✓ Quantum filtering complete: {len(df_quantum):,} companies ({len(df_quantum)/len(df_all)*100:.2f}%)")

    # Save quantum cache
    if save_parquet:
        logger.info(f"\nSaving quantum cache to {cache_path}...")
        try:
            df_quantum.to_parquet(cache_path, index=False, engine='pyarrow')
            cache_size = cache_path.stat().st_size / (1024 * 1024)
            logger.info(f"✓ Saved quantum cache to {cache_path} for future fast loading")
            logger.info(f"  Parquet size: {cache_size:.1f} MB")
        except ImportError:
            # Fallback to pickle if pyarrow not available
            pickle_path = cache_path.with_suffix('.pkl')
            df_quantum.to_pickle(pickle_path)
            pickle_size = pickle_path.stat().st_size / (1024 * 1024)
            logger.warning(f"⚠️  pyarrow not found. Using pickle format instead")
            logger.info(f"✓ Saved quantum pickle cache: {pickle_path.name} ({pickle_size:.1f} MB)")
            logger.info("  💡 Install pyarrow for better performance: pip install pyarrow")

    return df_quantum


# =========================================================
# Two-Snapshot Analysis Mode (Simplified E/L/S/V/F)
# =========================================================

# Deal type patterns following guidance:
# - Series A / Early Stage VC → A (baseline event)
# - Series B+ / Later Stage VC → B+ (success event)
PAT_A = re.compile(r"(?:\bEarly\s*Stage\s*VC\b|\bSeries\s*A(?:\b|[\s\-]?\d*)\b)", re.I)
PAT_Bp = re.compile(r"(?:\bLater\s*Stage\s*VC\b|\bSeries\s*[B-G](?:\b|[\s\-]?\d*)\b)", re.I)

def _is_A(s: str) -> bool:
    """Check if deal type is Series A or Early Stage VC"""
    return bool(PAT_A.search(s or ""))

def _is_BPLUS(s: str) -> bool:
    """Check if deal type is Series B+ or Later Stage VC"""
    return bool(PAT_Bp.search(s or ""))


def load_two_snapshots(baseline_path: Union[str, Path], end_path: Union[str, Path]) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load two snapshots for simplified E/L/S/V/F analysis.

    This is a lightweight alternative to consolidate_company_snapshots()
    for quick validation with just baseline and endpoint snapshots.

    Args:
        baseline_path: Path to baseline .dat file (e.g., Company20220101.dat)
        end_path: Path to endpoint .dat file (e.g., Company20231201.dat)

    Returns:
        Tuple of (df_baseline, df_end)

    Example:
        >>> df_b, df_e = load_two_snapshots('data/raw/Company20220101.dat',
        ...                                   'data/raw/Company20231201.dat')
        >>> ds = build_ELS_from_two_snapshots(df_b, df_e)
    """
    baseline_path = Path(baseline_path)
    end_path = Path(end_path)

    if not baseline_path.exists():
        raise FileNotFoundError(f"Baseline snapshot not found: {baseline_path}")
    if not end_path.exists():
        raise FileNotFoundError(f"End snapshot not found: {end_path}")

    logger.info(f"Loading baseline snapshot: {baseline_path.name}")
    df_b = pd.read_csv(baseline_path, sep='|', low_memory=False, encoding='utf-8')

    logger.info(f"Loading end snapshot: {end_path.name}")
    df_e = pd.read_csv(end_path, sep='|', low_memory=False, encoding='utf-8')

    # Parse date columns
    for df in (df_b, df_e):
        if 'LastFinancingDate' in df.columns:
            df['LastFinancingDate'] = pd.to_datetime(df['LastFinancingDate'], errors='coerce')

    logger.info(f"  Baseline: {len(df_b):,} companies")
    logger.info(f"  End: {len(df_e):,} companies")

    return df_b, df_e


def build_ELS_from_two_snapshots(df_base: pd.DataFrame, df_end: pd.DataFrame, quantum_only: bool = False) -> pd.DataFrame:
    """
    Build E/L/S/V/F variables from two snapshots (baseline → endpoint).

    Variable Definitions:
    - E: Baseline event (1 if company has Series A / Early Stage VC at baseline)
    - L: Later success (1 if company reaches Series B+ / Later Stage VC by endpoint)
    - S: Step-up = PreMoney_endpoint / PostMoney_baseline (Nanda 2024 definition)
    - V: Vagueness score from baseline text (z-scored)
    - F: Flexibility = 1 - is_hardware (from baseline keywords/description)

    Note: This is a simplified mode for quick validation. For full analysis,
    use consolidate_company_snapshots() with multiple snapshots.

    Args:
        df_base: Baseline snapshot DataFrame
        df_end: Endpoint snapshot DataFrame
        quantum_only: If True, filter to quantum-related companies only (default: False)

    Returns:
        DataFrame with columns: CompanyID, E, L, S_stepup, S_stepup_log,
                                z_V, E_scaled_A, F_flexibility, is_hardware,
                                founding_cohort, region

    Example:
        >>> df_b, df_e = load_two_snapshots('data/raw/Company20220101.dat',
        ...                                   'data/raw/Company20231201.dat')
        >>> ds = build_ELS_from_two_snapshots(df_b, df_e)
        >>> print(f"E=1 (Series A): {ds['E'].mean():.1%}")
        >>> print(f"L=1 (Series B+): {ds['L'].mean():.1%}")

        >>> # Quantum-only mode
        >>> ds_q = build_ELS_from_two_snapshots(df_b, df_e, quantum_only=True)
        >>> print(f"Quantum companies: {len(ds_q):,}")
    """
    logger.info("\n" + "="*80)
    logger.info(f"Building E/L/S/V/F from two snapshots {'(QUANTUM-ONLY MODE)' if quantum_only else ''}")
    logger.info("="*80)

    b = df_base.copy()
    e = df_end.copy()

    # Filter for quantum companies if requested
    if quantum_only:
        logger.info("\n🔬 Filtering for quantum-related companies...")
        logger.info(f"   Before filtering: {len(b):,} baseline, {len(e):,} endpoint")
        b = filter_quantum_companies(b)
        e = filter_quantum_companies(e)
        logger.info(f"   After filtering: {len(b):,} baseline, {len(e):,} endpoint")

    # Ensure required columns exist
    required_cols = ['CompanyID', 'LastFinancingDealType', 'Description', 'Keywords']
    for col in required_cols:
        if col not in b.columns:
            b[col] = pd.NA
        if col not in e.columns:
            e[col] = pd.NA

    # Optional columns
    optional_cols = ['LastFinancingDate', 'PreMoneyValuation', 'PostValuation',
                     'YearFounded', 'Country', 'Employees']
    for col in optional_cols:
        if col not in b.columns:
            b[col] = pd.NA
        if col not in e.columns:
            e[col] = pd.NA

    # Classify A / B+ for both snapshots
    logger.info("\nClassifying deal types...")
    b['is_A'] = b['LastFinancingDealType'].fillna('').apply(_is_A)
    b['is_BPLUS'] = b['LastFinancingDealType'].fillna('').apply(_is_BPLUS)
    e['is_A'] = e['LastFinancingDealType'].fillna('').apply(_is_A)
    e['is_BPLUS'] = e['LastFinancingDealType'].fillna('').apply(_is_BPLUS)

    logger.info(f"  Baseline: {b['is_A'].sum():,} Series A, {b['is_BPLUS'].sum():,} Series B+")
    logger.info(f"  Endpoint: {e['is_A'].sum():,} Series A, {e['is_BPLUS'].sum():,} Series B+")

    # Merge baseline and endpoint by CompanyID
    logger.info("\nMerging baseline and endpoint...")
    df = b.add_suffix('_t1').merge(
        e.add_suffix('_t2'),
        left_on='CompanyID_t1',
        right_on='CompanyID_t2',
        how='outer'
    )
    df.rename(columns={'CompanyID_t1': 'CompanyID'}, inplace=True)
    df['CompanyID'].fillna(df['CompanyID_t2'], inplace=True)

    logger.info(f"  Merged: {len(df):,} companies")

    # E: Baseline event (Series A at baseline)
    df['E'] = df['is_A_t1'].fillna(False).astype(int)

    # L: Later success (Series B+ at endpoint)
    df['L'] = df['is_BPLUS_t2'].fillna(False).astype(int)

    logger.info(f"\nVariable distributions:")
    logger.info(f"  E=1 (Series A at baseline): {df['E'].sum():,} ({df['E'].mean()*100:.1f}%)")
    logger.info(f"  L=1 (Series B+ at endpoint): {df['L'].sum():,} ({df['L'].mean()*100:.1f}%)")

    # S: Step-up = PreMoney_t2 / PostMoney_t1
    logger.info("\nCalculating Step-up (S)...")

    # Check if required columns exist
    if 'PreMoneyValuation_t2' not in df.columns:
        logger.warning("  ⚠️  'PreMoneyValuation_t2' column not found in endpoint snapshot!")
        logger.info(f"     Available endpoint columns with 'val' or 'money': {[c for c in df.columns if ('val' in c.lower() or 'money' in c.lower()) and '_t2' in c]}")

    if 'PostValuation_t1' not in df.columns:
        logger.warning("  ⚠️  'PostValuation_t1' column not found in baseline snapshot!")
        logger.info(f"     Available baseline columns with 'val' or 'money': {[c for c in df.columns if ('val' in c.lower() or 'money' in c.lower()) and '_t1' in c]}")

    # Try to convert to numeric
    df['PreMoney_t2'] = pd.to_numeric(df['PreMoneyValuation_t2'], errors='coerce') if 'PreMoneyValuation_t2' in df.columns else pd.NA
    df['PostMoney_t1'] = pd.to_numeric(df['PostValuation_t1'], errors='coerce') if 'PostValuation_t1' in df.columns else pd.NA

    # Diagnostic output
    n_pre_t2_notna = df['PreMoney_t2'].notna().sum()
    n_post_t1_notna = df['PostMoney_t1'].notna().sum()
    n_pre_t2_positive = (df['PreMoney_t2'] > 0).sum()
    n_post_t1_positive = (df['PostMoney_t1'] > 0).sum()

    logger.info(f"  PreMoney_t2 (endpoint): {n_pre_t2_notna:,} non-null, {n_pre_t2_positive:,} positive")
    logger.info(f"  PostMoney_t1 (baseline): {n_post_t1_notna:,} non-null, {n_post_t1_positive:,} positive")

    # Check combinations
    both_notna = df['PreMoney_t2'].notna() & df['PostMoney_t1'].notna()
    both_positive = (df['PreMoney_t2'] > 0) & (df['PostMoney_t1'] > 0)
    logger.info(f"  Both present: {both_notna.sum():,}")
    logger.info(f"  Both positive: {both_positive.sum():,}")

    def calc_stepup(row):
        if pd.notna(row['PreMoney_t2']) and pd.notna(row['PostMoney_t1']):
            if row['PreMoney_t2'] > 0 and row['PostMoney_t1'] > 0:
                return row['PreMoney_t2'] / row['PostMoney_t1']
        return pd.NA

    df['S_stepup'] = df.apply(calc_stepup, axis=1)
    df['S_stepup_log'] = df['S_stepup'].apply(lambda x: np.log(x) if pd.notna(x) and x > 0 else pd.NA)

    n_stepup = df['S_stepup'].notna().sum()
    logger.info(f"  S (step-up) calculated: {n_stepup:,} companies")
    if n_stepup > 0:
        logger.info(f"  S range: {df['S_stepup'].min():.2f} - {df['S_stepup'].max():.2f}")
        logger.info(f"  S median: {df['S_stepup'].median():.2f}")
    else:
        logger.warning("  ⚠️  WARNING: 0 valid step-up values! Check:")
        logger.warning("     - Do PreMoneyValuation and PostValuation columns exist in your .dat files?")
        logger.warning("     - Are the column names spelled correctly?")
        logger.warning("     - Are most values NULL/empty in the raw data?")

    # V: Vagueness (from baseline text)
    logger.info("\nCalculating Vagueness (V)...")
    df['V_raw'] = compute_vagueness_vectorized(
        df['Description_t1'].fillna(''),
        df['Keywords_t1'].fillna('')
    )

    # Z-score vagueness
    v_mean = df['V_raw'].mean()
    v_std = df['V_raw'].std()
    if v_std > 0:
        df['z_V'] = (df['V_raw'] - v_mean) / v_std
    else:
        df['z_V'] = 0

    logger.info(f"  V calculated: {df['V_raw'].notna().sum():,} companies")
    logger.info(f"  V mean: {v_mean:.3f}, std: {v_std:.3f}")

    # F: Flexibility (inverted hardware)
    logger.info("\nCalculifying Flexibility/Hardware (F)...")
    df['is_hardware'] = classify_hardware_vectorized(
        df['Keywords_t1'].fillna(''),
        df['Description_t1'].fillna('')
    ).astype(int)
    df['F_flexibility'] = (1 - df['is_hardware']).astype(int)

    hw_pct = df['is_hardware'].mean() * 100
    logger.info(f"  Hardware companies: {df['is_hardware'].sum():,} ({hw_pct:.1f}%)")
    logger.info(f"  Software companies: {df['F_flexibility'].sum():,} ({100-hw_pct:.1f}%)")

    # E_scaled_A: Baseline funding (scaled 0-1)
    logger.info("\nScaling baseline funding (E)...")
    df['E_raw'] = df['PostMoney_t1']
    e_valid = df['E_raw'].dropna()
    if len(e_valid) > 0 and e_valid.max() > e_valid.min():
        df['E_scaled_A'] = (df['E_raw'] - e_valid.min()) / (e_valid.max() - e_valid.min())
    else:
        df['E_scaled_A'] = pd.NA

    # Controls: founding cohort, region
    logger.info("\nAdding control variables...")
    df_temp = df.rename(columns={'YearFounded_t1': 'year_founded'})
    df['founding_cohort'] = create_founding_cohort(df_temp, 'year_founded')
    df['region'] = df['Country_t1'].fillna('Unknown')

    # Select final columns
    final_cols = [
        'CompanyID', 'E', 'L', 'S_stepup', 'S_stepup_log',
        'z_V', 'V_raw', 'E_scaled_A', 'F_flexibility', 'is_hardware',
        'founding_cohort', 'region'
    ]

    result = df[final_cols].copy()

    logger.info(f"\n✅ Two-snapshot dataset built: {len(result):,} companies × {len(final_cols)} columns")

    return result


def load_deal_snapshot(filepath: Path) -> pd.DataFrame:
    """Load single deal .dat file with proper parsing.

    Args:
        filepath: Path to DealYYYYMMDD.dat file

    Returns:
        DataFrame with parsed deal data
    """
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    df = pd.read_csv(filepath, sep='|', low_memory=False, encoding='utf-8')

    # Extract date from filename
    date_str = filepath.stem.replace('Deal', '')
    if date_str:  # If there's a date in filename
        try:
            df['snapshot_date'] = pd.to_datetime(date_str, format='%Y%m%d')
        except:
            df['snapshot_date'] = datetime.now()

    logger.info(f"  Loaded {filepath.name}: {len(df):,} deals")
    return df


# =========================================================
# Quantum & Domain-Specific Filtering
# =========================================================

def filter_quantum_companies(df: pd.DataFrame) -> pd.DataFrame:
    """Filter for quantum computing/technology related companies.

    Identifies quantum companies using keywords in:
    - Description
    - Keywords
    - Primary Industry Codes

    Args:
        df: DataFrame with company data

    Returns:
        DataFrame with only quantum-related companies

    Example:
        >>> df_all = consolidate_company_snapshots('data/raw')
        >>> df_quantum = filter_quantum_companies(df_all)
        >>> print(f"Quantum companies: {len(df_quantum):,}")
    """
    # Quantum-related keywords (comprehensive list)
    quantum_keywords = [
        'quantum', 'qubit', 'qbit', 'quantum computing', 'quantum computer',
        'quantum processor', 'quantum algorithm', 'quantum cryptography',
        'quantum encryption', 'quantum communication', 'quantum sensor',
        'quantum simulation', 'quantum annealing', 'quantum software',
        'superconducting qubit', 'topological qubit', 'ion trap',
        'quantum advantage', 'quantum supremacy', 'noisy intermediate-scale quantum',
        'nisq', 'quantum error correction', 'quantum gate'
    ]

    # Create mask for quantum companies
    mask = pd.Series(False, index=df.index)

    # Check Description column
    if 'Description' in df.columns:
        desc_mask = df['Description'].fillna('').str.lower().str.contains(
            '|'.join(quantum_keywords), case=False, regex=True, na=False
        )
        mask |= desc_mask
        logger.info(f"  Found {desc_mask.sum():,} companies via Description")

    # Check Keywords column
    if 'Keywords' in df.columns:
        kw_mask = df['Keywords'].fillna('').str.lower().str.contains(
            '|'.join(quantum_keywords), case=False, regex=True, na=False
        )
        mask |= kw_mask
        logger.info(f"  Found {kw_mask.sum():,} companies via Keywords")

    # Check Promise column (if exists)
    if 'Promise' in df.columns:
        prom_mask = df['Promise'].fillna('').str.lower().str.contains(
            '|'.join(quantum_keywords), case=False, regex=True, na=False
        )
        mask |= prom_mask
        logger.info(f"  Found {prom_mask.sum():,} companies via Promise")

    df_quantum = df[mask].copy()
    logger.info(f"\n  ✓ Total quantum companies identified: {len(df_quantum):,} ({len(df_quantum)/len(df)*100:.2f}%)")

    return df_quantum


def select_hypothesis_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Select minimal columns needed for 4 hypotheses testing.

    Core columns for hypothesis testing:
    - Identifiers: CompanyID, company_id, snapshot_date
    - IVs: Description, Keywords, Promise (for vagueness)
    - DVs: FirstFinancingSize, LastFinancingDealType, FirstFinancingDealType (for growth, early_funding)
    - Moderators: Keywords (for is_hardware classification)
    - Controls: Employees, YearFounded, TotalRaised, BusinessStatus
    - Founder: PrimaryContactPBId (for founder_credibility)

    Args:
        df: DataFrame with full company data

    Returns:
        DataFrame with only essential columns for hypothesis testing

    Example:
        >>> df_full = consolidate_company_snapshots('data/raw')
        >>> df_minimal = select_hypothesis_columns(df_full)
        >>> print(f"Columns reduced: {len(df_full.columns)} → {len(df_minimal.columns)}")
    """
    # Define essential columns for 4 hypotheses
    essential_cols = [
        # Identifiers
        'CompanyID', 'company_id', 'CompanyName',
        'snapshot_date',

        # For Vagueness (IV)
        'Description', 'Keywords', 'Promise',

        # For Early Funding (DV in H1, H3)
        'FirstFinancingSize', 'FirstFinancingDate', 'FirstFinancingDealType',

        # For Growth (DV in H2, H4)
        'LastFinancingDealType', 'LastFinancingDate',
        'CompanyFinancingStatus', 'BusinessStatus',

        # For is_hardware moderator (H2)
        # Already covered by Keywords

        # For founder_credibility moderator (H3, H4)
        'PrimaryContactPBId',

        # Controls
        'Employees', 'YearFounded', 'TotalRaised',
        'City', 'StateProvince', 'Country',  # For region controls

        # Optional (for valuation step-up)
        'LastKnownValuation', 'FirstFinancingValuation'
    ]

    # Find which columns exist in the dataframe
    existing_cols = [col for col in essential_cols if col in df.columns]

    # Report dropped columns
    dropped_cols = set(df.columns) - set(existing_cols)
    logger.info(f"  Selecting {len(existing_cols)} essential columns (dropping {len(dropped_cols)})")

    df_minimal = df[existing_cols].copy()

    # Report memory savings
    mem_full = df.memory_usage(deep=True).sum() / 1024**2
    mem_minimal = df_minimal.memory_usage(deep=True).sum() / 1024**2
    savings_pct = (1 - mem_minimal/mem_full) * 100

    logger.info(f"  Memory: {mem_full:.1f} MB → {mem_minimal:.1f} MB (saved {savings_pct:.1f}%)")

    return df_minimal


def create_quantum_dataset(
    data_dir: Union[str, Path],
    output_path: Optional[Union[str, Path]] = None,
    years: Optional[List[int]] = None
) -> pd.DataFrame:
    """Create quantum-focused minimal dataset for hypothesis testing.

    This is a convenience function that:
    1. Loads/consolidates company data (with caching)
    2. Filters for quantum companies only
    3. Selects minimal columns for hypothesis testing
    4. Optionally saves to .parquet file

    Args:
        data_dir: Directory containing raw .dat files
        output_path: Optional path to save quantum dataset as .parquet
        years: Optional list of years to load (e.g., [2022, 2024, 2025]).
               For time windows 2022-2024 and 2022-2025, use [2022, 2024, 2025].

    Returns:
        DataFrame with quantum companies and minimal columns

    Example:
        >>> # Create quantum dataset and save
        >>> df_q = create_quantum_dataset(
        ...     'data/raw',
        ...     output_path='data/processed/quantum_hypothesis_data.parquet'
        ... )
        >>> print(df_q.shape)
        (250, 18)  # 250 quantum companies, 18 essential columns

        >>> # Load only specific years (faster!)
        >>> df_q = create_quantum_dataset(
        ...     'data/raw',
        ...     output_path='data/processed/quantum_hypothesis_data.parquet',
        ...     years=[2022, 2024, 2025]
        ... )
    """
    logger.info("\n" + "="*80)
    logger.info("Creating Quantum Hypothesis Testing Dataset")
    logger.info("="*80)

    # Step 1: Load all companies (with caching)
    logger.info("\nStep 1: Loading company data...")
    df_all = consolidate_company_snapshots(
        data_dir,
        use_cache=True,
        save_parquet=True,
        years=years
    )

    if df_all is None:
        raise ValueError("Failed to load company data")

    # Step 2: Filter for quantum companies
    logger.info("\nStep 2: Filtering for quantum companies...")
    df_quantum = filter_quantum_companies(df_all)

    if len(df_quantum) == 0:
        logger.warning("⚠️  No quantum companies found!")
        return df_quantum

    # Step 3: Select minimal columns
    logger.info("\nStep 3: Selecting hypothesis testing columns...")
    df_minimal = select_hypothesis_columns(df_quantum)

    # Step 4: Save to parquet (if path provided)
    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        df_minimal.to_parquet(output_path, index=False, engine='pyarrow')

        # Report file size
        import os
        file_size = os.path.getsize(output_path) / 1024**2
        logger.info(f"\n✓ Saved quantum dataset to: {output_path}")
        logger.info(f"  File size: {file_size:.2f} MB")
        logger.info(f"  Shape: {df_minimal.shape[0]:,} companies × {df_minimal.shape[1]} columns")

    logger.info("\n" + "="*80)

    return df_minimal


# =========================================================
# Academic Vagueness (Gemini's StrategicVaguenessScorer)
# =========================================================

class StrategicVaguenessScorerV2:
    """
    Strategic Vagueness Scorer V2 - Two-component vagueness measure.

    Parameters
    ----------
    abstract_terms : list[str], optional
        Custom list of abstract/categorical terms. If None, uses default lexicon.
    unit_terms : list[str], optional
        Custom list of unit/spec terms for specificity detection. If None, uses defaults.
    use_idf : bool, default=True
        Weight abstract terms by inverse document frequency to reduce false positives.
    groupby_cols : list[str], optional
        Column names for group-wise percentile computation.
    random_state : int, default=0
        Random seed for reproducibility (currently unused but reserved).
    """

    # Default abstract terms lexicon
    DEFAULT_ABSTRACT_TERMS = [
        "platform", "solution", "ecosystem", "innovation", "AI-powered",
        "end-to-end", "digital transformation", "next-generation", "seamless",
        "synergy", "leverage", "framework", "infrastructure", "service layer",
        "suite", "experience", "future-proof", "cutting-edge", "revolutionary",
        "transformative", "strategic", "holistic", "integrated", "comprehensive",
        "robust", "scalable", "flexible", "agile", "dynamic", "optimize",
        "streamline", "enhance", "enable", "empower", "deliver", "drive",
        "value-added", "best-in-class", "world-class", "industry-leading",
        "state-of-the-art", "advanced", "sophisticated", "intelligent",
        "smart", "automated", "cloud-based", "enterprise-grade"
    ]

    # Default stopwords (generic English - do NOT remove domain terms)
    STOPWORDS = set([
        "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
        "has", "he", "in", "is", "it", "its", "of", "on", "that", "the",
        "to", "was", "will", "with", "we", "our", "this", "these", "those"
    ])

    def __init__(
        self,
        abstract_terms: Optional[List[str]] = None,
        unit_terms: Optional[List[str]] = None,
        use_idf: bool = True,
        groupby_cols: Optional[List[str]] = None,
        random_state: int = 0
    ):
        self.abstract_terms = abstract_terms or self.DEFAULT_ABSTRACT_TERMS
        self.unit_terms = unit_terms
        self.use_idf = use_idf
        self.groupby_cols = groupby_cols
        self.random_state = random_state

        # Build regex patterns
        self._abstract_pattern = self._build_abstract_pattern()
        self._idf_weights = {}
        self._fitted = False

    def _build_abstract_pattern(self) -> re.Pattern:
        """Build regex pattern for abstract terms (case-insensitive)."""
        # Escape special regex chars and handle multi-word terms
        escaped_terms = [re.escape(term) for term in self.abstract_terms]
        pattern = r'\b(' + '|'.join(escaped_terms) + r')\b'
        return re.compile(pattern, re.IGNORECASE)

    def _preprocess(self, text: str) -> str:
        """
        Preprocessing: lowercase, strip HTML, collapse whitespace.

        Parameters
        ----------
        text : str
            Raw input text

        Returns
        -------
        str
            Cleaned text
        """
        if not isinstance(text, str):
            return ""

        # Strip HTML tags
        text = re.sub(r'<[^>]+>', ' ', text)

        # Lowercase
        text = text.lower()

        # Collapse whitespace
        text = re.sub(r'\s+', ' ', text).strip()

        return text

    def _tokenize(self, text: str) -> List[str]:
        """
        Tokenize on word boundaries; keep hyphenated terms.

        Parameters
        ----------
        text : str
            Preprocessed text

        Returns
        -------
        list[str]
            Tokens
        """
        # Match words including hyphenated terms
        pattern = r'\b[\w][\w\-]*\b'
        tokens = re.findall(pattern, text)
        return tokens

    def _compute_idf(self, texts: List[str]) -> Dict[str, float]:
        """
        Compute inverse document frequency for abstract terms.

        Parameters
        ----------
        texts : list[str]
            Corpus of preprocessed texts

        Returns
        -------
        dict
            IDF weights for each abstract term
        """
        n_docs = len(texts)
        doc_freq = Counter()

        for text in texts:
            # Find unique abstract terms in this document
            matches = set(self._abstract_pattern.findall(text))
            for term in matches:
                doc_freq[term.lower()] += 1

        # Compute IDF: log(N / df)
        idf = {}
        for term in self.abstract_terms:
            df = doc_freq.get(term.lower(), 0)
            if df > 0:
                idf[term.lower()] = np.log(n_docs / df)
            else:
                idf[term.lower()] = 0.0

        return idf

    def _score_categorical_vagueness(self, text: str, tokens: List[str]) -> float:
        """
        Component (1): Categorical Vagueness → S_cat ∈ [0, 100]

        Measures reliance on abstract category terms.

        Parameters
        ----------
        text : str
            Preprocessed text
        tokens : list[str]
            Tokenized text

        Returns
        -------
        float
            S_cat score in [0, 100]
        """
        token_count = len(tokens)
        if token_count == 0:
            return 0.0

        # Find all abstract term matches
        matches = self._abstract_pattern.findall(text)

        if not matches:
            return 0.0

        # Count abstract terms
        if self.use_idf and self._fitted:
            # Weight by IDF
            weighted_count = sum(
                self._idf_weights.get(match.lower(), 1.0)
                for match in matches
            )
            # Normalize by mean IDF to keep scale consistent
            mean_idf = np.mean(list(self._idf_weights.values())) if self._idf_weights else 1.0
            if mean_idf > 0:
                count_abstract = weighted_count / mean_idf
            else:
                count_abstract = len(matches)
        else:
            count_abstract = len(matches)

        # Score with scaling factor α
        # Tuned so marketing-heavy → 60-80, technical → 20-40
        # For marketing with ~40% abstract terms: 100 * 0.4 * α = 70 → α ≈ 1.75
        alpha = 2.3  # Scaling constant

        score = 100 * (count_abstract / max(1, token_count)) * alpha

        # Clip to [0, 100]
        return min(100.0, max(0.0, score))

    def _score_concreteness_deficit(self, text: str, tokens: List[str]) -> float:
        """
        Component (2): Concreteness Deficit → S_concdef ∈ [0, 100]

        Penalizes absence of specifics (numbers, dates, versions, units, benchmarks).

        Parameters
        ----------
        text : str
            Preprocessed text
        tokens : list[str]
            Tokenized text

        Returns
        -------
        float
            S_concdef score in [0, 100]
        """
        token_count = max(1, len(tokens))

        # Feature 1: Numbers or percentages
        has_number = bool(re.search(r'\d+(\.\d+)?%?', text))
        number_density = len(re.findall(r'\d+(\.\d+)?%?', text)) / (token_count / 100)

        # Feature 2: Dates, quarters, years
        has_date = bool(re.search(
            r'\b(20\d{2}|q[1-4]\s*20\d{2}|january|february|march|april|may|june|'
            r'july|august|september|october|november|december)\b',
            text, re.IGNORECASE
        ))
        date_density = len(re.findall(
            r'\b(20\d{2}|q[1-4]\s*20\d{2}|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\b',
            text, re.IGNORECASE
        )) / (token_count / 100)

        # Feature 3: Versions or releases
        has_version = bool(re.search(
            r'\bv\d+(\.\d+){0,3}\b|version\s+\d+|release\s+\d+|sdk\s+v?\d+|api\s+v?\d+',
            text, re.IGNORECASE
        ))

        # Feature 4: Units and specs
        unit_pattern = (
            r'\b\d+\s*(nm|ghz|mhz|kw|mw|w|ms|μs|ns|gb|tb|mb|kb|kwh|mwh|'
            r'tops|flops|gflops|tflops|μm|mm|cm|m|km|mpa|gpa|kpa|pa|'
            r'hz|v|a|ma|μa|°c|°f|k|mol|cd|lm|lx|db|dbi|ppm|ppb|%|'
            r'cri|coherence|qubit|qubits|error\s+rate|fidelity)\b'
        )
        has_units = bool(re.search(unit_pattern, text, re.IGNORECASE))
        unit_density = len(re.findall(unit_pattern, text, re.IGNORECASE)) / (token_count / 100)

        # Feature 5: Benchmarks, publications, named clients
        benchmark_pattern = (
            r'\b(benchmark|published|nature|science|ieee|arxiv|acm|'
            r'customer|client|partner|pilot|deployment|production)\b'
        )
        has_benchmark = bool(re.search(benchmark_pattern, text, re.IGNORECASE))

        # Named entities (capitalized bigrams as proxy for companies/products)
        named_entities = re.findall(r'\b[A-Z][a-z]+\s+[A-Z][a-z]+\b', text)
        has_named = len(named_entities) > 0

        # Weighted combination of features
        # Use density-based squashing: 1 - exp(-density)
        w1, w2, w3, w4, w5 = 0.25, 0.20, 0.15, 0.25, 0.15

        evidence_1 = 1 - np.exp(-number_density * 0.5) if number_density > 0 else 0
        evidence_2 = 1 - np.exp(-date_density * 0.8) if date_density > 0 else 0
        evidence_3 = float(has_version)
        evidence_4 = 1 - np.exp(-unit_density * 0.6) if unit_density > 0 else 0
        evidence_5 = float(has_benchmark or has_named)

        specificity_evidence = (
            w1 * evidence_1 +
            w2 * evidence_2 +
            w3 * evidence_3 +
            w4 * evidence_4 +
            w5 * evidence_5
        )

        # Concreteness deficit is inverse of specificity
        s_concdef = 100 * (1 - specificity_evidence)

        # Clip to [0, 100]
        return min(100.0, max(0.0, s_concdef))

    def _aggregate_v_raw(self, s_cat: float, s_concdef: float) -> float:
        """
        Aggregate S_cat and S_concdef into V_raw using max-mean hybrid.

        V_raw = 0.5 * max(S_cat, S_concdef) + 0.5 * mean(S_cat, S_concdef)

        Rationale: Preserves extreme signals when either component is very high.

        Parameters
        ----------
        s_cat : float
            Categorical vagueness score
        s_concdef : float
            Concreteness deficit score

        Returns
        -------
        float
            V_raw score in [0, 100]
        """
        mean_val = 0.5 * (s_cat + s_concdef)
        max_val = max(s_cat, s_concdef)
        v_raw = 0.5 * max_val + 0.5 * mean_val
        return v_raw

    def fit(
        self,
        texts: List[str],
        y: Optional[pd.Series] = None,
        group_cols: Optional[pd.DataFrame] = None
    ):
        """
        Fit the scorer on a corpus (compute IDF weights if enabled).

        Parameters
        ----------
        texts : list[str]
            Input texts
        y : pd.Series, optional
            Ignored (for sklearn compatibility)
        group_cols : pd.DataFrame, optional
            Group columns for within-group percentile computation

        Returns
        -------
        self
        """
        # Preprocess all texts
        preprocessed = [self._preprocess(text) for text in texts]

        # Compute IDF weights if enabled
        if self.use_idf:
            self._idf_weights = self._compute_idf(preprocessed)

        self._fitted = True
        return self

    def transform(
        self,
        texts: List[str],
        group_cols: Optional[pd.DataFrame] = None
    ) -> pd.DataFrame:
        """
        Transform texts into vagueness scores.

        Parameters
        ----------
        texts : list[str]
            Input texts
        group_cols : pd.DataFrame, optional
            Group columns for within-group percentile computation

        Returns
        -------
        pd.DataFrame
            Columns: S_cat, S_concdef, V_raw, V_pct, V_minmax
        """
        results = []

        for text in texts:
            # Preprocess and tokenize
            preprocessed = self._preprocess(text)
            tokens = self._tokenize(preprocessed)

            # Compute components
            s_cat = self._score_categorical_vagueness(preprocessed, tokens)
            s_concdef = self._score_concreteness_deficit(preprocessed, tokens)

            # Aggregate
            v_raw = self._aggregate_v_raw(s_cat, s_concdef)

            results.append({
                'S_cat': s_cat,
                'S_concdef': s_concdef,
                'V_raw': v_raw
            })

        df = pd.DataFrame(results)

        # Compute percentiles
        if group_cols is not None and self.groupby_cols:
            # Within-group percentiles
            combined = pd.concat([group_cols.reset_index(drop=True), df], axis=1)
            combined['V_pct'] = combined.groupby(self.groupby_cols)['V_raw'].rank(pct=True) * 100
            df['V_pct'] = combined['V_pct']
        else:
            # Global percentiles
            df['V_pct'] = df['V_raw'].rank(pct=True) * 100

        # Compute min-max normalization
        v_min = df['V_raw'].min()
        v_max = df['V_raw'].max()
        if v_max > v_min:
            df['V_minmax'] = 100 * (df['V_raw'] - v_min) / (v_max - v_min)
        else:
            df['V_minmax'] = 50.0  # All same value

        return df

    def fit_transform(
        self,
        texts: List[str],
        y: Optional[pd.Series] = None,
        group_cols: Optional[pd.DataFrame] = None
    ) -> pd.DataFrame:
        """
        Fit and transform in one step.

        Parameters
        ----------
        texts : list[str]
            Input texts
        y : pd.Series, optional
            Ignored (for sklearn compatibility)
        group_cols : pd.DataFrame, optional
            Group columns for within-group percentile computation

        Returns
        -------
        pd.DataFrame
            Columns: S_cat, S_concdef, V_raw, V_pct, V_minmax
        """
        self.fit(texts, y, group_cols)
        return self.transform(texts, group_cols)

# Backward compatibility shim
class StrategicVaguenessScorer(StrategicVaguenessScorerV2):
    """
    Deprecated: Use StrategicVaguenessScorerV2 instead.

    This is a compatibility shim. The lexical-uncertainty component has been
    removed per research spec p.25-26. Vagueness is now computed using only
    two components: Categorical Vagueness and Concreteness Deficit.
    """

    def __init__(self, *args, **kwargs):
        warnings.warn(
            "StrategicVaguenessScorer is deprecated. "
            "Lexical uncertainty component has been removed; "
            "using two-component V (Categorical Vagueness + Concreteness Deficit). "
            "Please use StrategicVaguenessScorerV2 directly.",
            DeprecationWarning,
            stacklevel=2
        )
        super().__init__(*args, **kwargs)

# --- Scorer instance and Wrapper ---
_SCORER = StrategicVaguenessScorer()

def compute_vagueness_vectorized(descriptions: pd.Series, keywords: pd.Series) -> pd.Series:
    """
    Vectorized wrapper for StrategicVaguenessScorer using both inputs.
    """
    # Combine into a temporary DataFrame to handle alignment and missing values
    temp_df = pd.DataFrame({'description': descriptions, 'keywords': keywords})

    return temp_df.apply(
        lambda row: _SCORER.score_vagueness(row['description'], row['keywords']),
        axis=1
    )

# =========================================================
# Integration Cost → Hardware/Software classifier
# =========================================================
def classify_hardware_or_software(keywords: str, description: str = "") -> int:
    """
    Return 1 if the venture sits in high-integration 'hardware' space, else 0.
    Mapping for report language:
        1 → Hardware / Integrated (Battleship)  [Purple]
        0 → Software / Non-integrated (Lego)    [Green]
    """
    if not isinstance(keywords, str):
        keywords = ""
    text = f"{keywords} {description}".lower()

    hardware_cues = [
        "hardware", "robotics", "robot", "chip", "asic", "semiconductor", "device",
        "sensor", "fpga", "silicon", "biotech", "quantum", "autonomous vehicle", "av",
        "battery", "manufacturing", "actuator", "lidar", "camera module", "edge device"
    ]
    software_cues = [
        "software", "saas", "api", "cloud", "platform", "sdk", "microservice",
        "data", "ml", "ai", "nlp", "cv", "llm", "analytics", "developer tool"
    ]
    h = sum(kw in text for kw in hardware_cues)
    s = sum(kw in text for kw in software_cues)
    return 1 if h > s else 0

def classify_hardware_vectorized(keywords: pd.Series, descriptions: pd.Series = None) -> pd.Series:
    if descriptions is None:
        descriptions = pd.Series([""] * len(keywords), index=keywords.index)

    # Handle potential NaN values gracefully
    safe_keywords = keywords.fillna("")
    safe_descriptions = descriptions.fillna("")

    return pd.Series(
        [classify_hardware_or_software(k, d) for k, d in zip(safe_keywords, safe_descriptions)],
        index=keywords.index
    )

# =========================================================
# Funding / DV helpers
# =========================================================
def derive_early_funding(first_financing_size: pd.Series) -> pd.Series:
    """
    Convert first financing size to millions USD.

    Note: This function only converts the amount. Filtering for Series A /
    Early Stage VC is done in engineer_features() using FirstFinancingDealType.

    Args:
        first_financing_size: First financing amount in USD

    Returns:
        Funding amount in millions USD
    """
    return first_financing_size / 1e6

def create_survival_seriesb_progression(
    df_baseline: pd.DataFrame,
    df_mid1: pd.DataFrame,
    df_mid2: pd.DataFrame,
    df_endpoint: pd.DataFrame,
    baseline_date: str = "2021-12-01",
    mid1_date: str = "2022-01-01",
    mid2_date: str = "2022-05-01",
    endpoint_date: str = "2023-05-01"
) -> pd.DataFrame:
    """
    Create survival variable based on Series B+ progression (LLM2 approach).

    This addresses the singular matrix problem by using SUCCESS-BASED survival:
    - Y=1: Company progressed from Series A → Series B+ within window
    - Y=0: Company stayed at Series A or went Out of Business
    - CENSORED: Company had M&A exit (competing risk)

    Expected base rate: 12-15% (17-month window captures early movers only)

    Key features:
    1. As-of capping: Prevents data leakage (diagnostic showed 2024-2025 dates in 2021-23 snapshots)
    2. Event ordering: Uses all 4 snapshots to determine "first seen" for B+ and M&A
    3. At-risk cohort: Only companies at Series A (VC-backed) at baseline

    Args:
        df_baseline: Baseline snapshot (2021-12-01) - extract predictors
        df_mid1: Mid snapshot 1 (2022-01-01) - for event ordering
        df_mid2: Mid snapshot 2 (2022-05-01) - for event ordering
        df_endpoint: Endpoint snapshot (2023-05-01) - final outcomes
        baseline_date: Date of baseline snapshot
        mid1_date: Date of mid1 snapshot
        mid2_date: Date of mid2 snapshot
        endpoint_date: Date of endpoint snapshot

    Returns:
        DataFrame with columns:
        - company_id: Company identifier
        - Y_primary: Binary DV (1=B+ progression, 0=no progression, NaN=M&A censored)
        - Y_MA_upper: Upper bound (M&A=1)
        - Y_MA_lower: Lower bound (M&A=0)
        - at_risk: Whether company was in at-risk cohort
    """
    import re

    # Regex patterns for deal types (FIXED - matches actual PitchBook data structure)
    # PitchBook uses "Early Stage VC" / "Later Stage VC" instead of "Series A/B/C"

    # Series A: "Early Stage VC" is the primary label (~45K companies)
    A_STAGE_PAT = r"(?:\bSeries\s*A(?:[-\s]?\d+|[A-Z])?\b|\bEarly[-\s]*Stage\s*VC\b)"

    # Series B+: "Later Stage VC" is the primary label (~24K companies)
    B_PLUS_PAT = r"(?:\bLater[-\s]*Stage\s*VC\b|\bSeries\s*[B-G](?:[-\s]?\d+|[A-Z])?\b)"

    # M&A pattern (unchanged)
    MA_PAT = r"(?:Merger|Acquisition|Buyout|LBO)"
    OOB_VAL = "Out of Business"

    # Identify company ID column
    id_col = 'CompanyID' if 'CompanyID' in df_baseline.columns else 'company_id'

    def apply_asof_cap(df, snapshot_date, date_col="LastFinancingDate", type_col="LastFinancingDealType"):
        """Apply as-of date capping to prevent data leakage."""
        df = df.copy()
        snap_dt = pd.to_datetime(snapshot_date)

        # Normalize date
        d = pd.to_datetime(df[date_col], errors='coerce')

        # Cap DATE but keep TYPE (type represents current stage, date may have data entry errors)
        capped_date = d.where(d <= snap_dt)
        # IMPORTANT: We keep the deal type even if date is future - it shows current financing stage
        capped_type = df[type_col]  # Don't null out based on date

        df[date_col + "_asof"] = capped_date
        df[type_col + "_asof"] = capped_type

        # Leakage guard
        max_date = df[date_col + "_asof"].dropna().max()
        if pd.notna(max_date) and max_date > snap_dt:
            print(f"  ⚠️  WARNING: Leakage detected: {max_date} > {snap_dt}")

        # Convenience flags for this snapshot
        df["asof_is_Bplus"] = df[type_col + "_asof"].fillna("").str.contains(B_PLUS_PAT, case=False, regex=True)
        df["asof_is_Astage"] = df[type_col + "_asof"].fillna("").str.contains(A_STAGE_PAT, case=False, regex=True)
        df["asof_is_MA"] = df[type_col + "_asof"].fillna("").str.contains(MA_PAT, case=False, regex=True)

        # Debug: Show sample matches
        n_a = df["asof_is_Astage"].sum()
        n_b = df["asof_is_Bplus"].sum()
        if n_a > 0:
            print(f"        → Found {n_a:,} Series A companies")
        if n_b > 0:
            print(f"        → Found {n_b:,} Series B+ companies")

        # Check for OOB status
        if "BusinessStatus" in df.columns:
            df["asof_is_OOB"] = (df["BusinessStatus"] == OOB_VAL)
        else:
            df["asof_is_OOB"] = False

        return df

    # Apply as-of capping to all snapshots
    print("\n  📅 Applying as-of date capping (preventing data leakage):")
    df_t0 = apply_asof_cap(df_baseline, baseline_date)
    print(f"     Baseline ({baseline_date}): capped")
    df_tM1 = apply_asof_cap(df_mid1, mid1_date)
    print(f"     Mid1 ({mid1_date}): capped")
    df_tM2 = apply_asof_cap(df_mid2, mid2_date)
    print(f"     Mid2 ({mid2_date}): capped")
    df_t1 = apply_asof_cap(df_endpoint, endpoint_date)
    print(f"     Endpoint ({endpoint_date}): capped")

    # Get at-risk cohort: Series A, VC-backed, no prior B+ at baseline
    print("\n  🎯 Identifying at-risk cohort (Series A at baseline):")

    if "CompanyFinancingStatus" in df_t0.columns:
        vc = (df_t0["CompanyFinancingStatus"] == "Venture Capital-Backed")
    else:
        vc = pd.Series(True, index=df_t0.index)

    at_a = df_t0["asof_is_Astage"].fillna(False)
    no_prior_b = ~df_t0["asof_is_Bplus"].fillna(False)

    cohort_mask = vc & at_a & no_prior_b
    atrisk = df_t0.loc[cohort_mask, [id_col]].drop_duplicates(subset=[id_col])

    print(f"     Total at baseline: {len(df_t0):,}")
    print(f"     VC-backed: {vc.sum():,}")
    print(f"     At Series A: {at_a.sum():,}")
    print(f"     No prior B+: {no_prior_b.sum():,}")
    print(f"     → At-risk cohort: {len(atrisk):,}")

    # Track event ordering across all 4 snapshots
    print("\n  🔍 Tracking event ordering (first seen B+ vs M&A):")

    atrisk_ids = set(atrisk[id_col].unique())
    snapshots = [
        (0, "t0", df_t0),
        (1, "tM1", df_tM1),
        (2, "tM2", df_tM2),
        (3, "t1", df_t1)
    ]

    # Collect all events
    all_events = []
    for idx, name, df in snapshots:
        events = df[[id_col, "asof_is_Bplus", "asof_is_MA"]].copy()
        events = events[events[id_col].isin(atrisk_ids)]
        events['_snap_idx'] = idx
        all_events.append(events)

    all_events_df = pd.concat(all_events, axis=0, ignore_index=True)

    # Find first occurrence of each event type
    def first_idx(flag_col):
        subset = all_events_df.loc[all_events_df[flag_col].fillna(False), [id_col, '_snap_idx']]
        return subset.groupby(id_col)['_snap_idx'].min()

    first_b = first_idx("asof_is_Bplus")
    first_ma = first_idx("asof_is_MA")

    # OOB status at endpoint
    oob_at_t1 = df_t1[[id_col, "asof_is_OOB"]].set_index(id_col)["asof_is_OOB"]

    # Merge into result DataFrame
    result = pd.DataFrame({
        'company_id': list(atrisk_ids)
    })
    result['first_seen_B_idx'] = result['company_id'].map(first_b)
    result['first_seen_MA_idx'] = result['company_id'].map(first_ma)
    result['oob_at_t1'] = result['company_id'].map(oob_at_t1).fillna(False)

    # Compute DV variants
    print("\n  📊 Computing DV (Series B+ progression):")

    # Primary DV: Y=1 if B+ appeared after baseline (idx>=1), CENSORED if M&A before B+
    b_idx = result['first_seen_B_idx']
    m_idx = result['first_seen_MA_idx']

    cond_B = b_idx.notna() & (b_idx >= 1)  # B+ appeared after baseline
    cond_MA_preB = m_idx.notna() & ((b_idx.isna()) | (m_idx < b_idx))  # M&A before B+ (or no B+)
    cond_OOB_or_stillA = (~cond_B) & (~cond_MA_preB)  # Neither B+ nor M&A

    # Primary DV (M&A censored)
    result['Y_primary'] = np.nan
    result.loc[cond_B, 'Y_primary'] = 1
    result.loc[cond_OOB_or_stillA, 'Y_primary'] = 0
    # M&A before B+ → censored (remains NaN)

    # Robustness bounds
    result['Y_MA_upper'] = result['Y_primary'].copy()
    result.loc[cond_MA_preB & (~cond_B), 'Y_MA_upper'] = 1

    result['Y_MA_lower'] = result['Y_primary'].copy()
    result.loc[cond_MA_preB & (~cond_B), 'Y_MA_lower'] = 0

    result['at_risk'] = True

    # Diagnostics
    n_total = len(result)
    n_valid_primary = result['Y_primary'].notna().sum()
    n_success = (result['Y_primary'] == 1).sum()
    n_censored = result['Y_primary'].isna().sum()

    base_rate = n_success / n_valid_primary if n_valid_primary > 0 else 0
    censored_rate = n_censored / n_total if n_total > 0 else 0

    print(f"     N at-risk: {n_total:,}")
    print(f"     N valid (non-censored): {n_valid_primary:,}")
    print(f"     N progressed to B+: {n_success:,}")
    print(f"     Base rate (B+ progression): {base_rate:.1%}")
    print(f"     M&A censored: {n_censored:,} ({censored_rate:.1%})")

    # Sanity check
    if not (0.08 <= base_rate <= 0.20):
        print(f"     ⚠️  WARNING: Base rate {base_rate:.1%} outside expected 8-20% range")
    else:
        print(f"     ✓ Base rate within expected range (8-20%)")

    return result[['company_id', 'Y_primary', 'Y_MA_upper', 'Y_MA_lower', 'at_risk']]


# =========================================================
# Sector FE & controls
# =========================================================
def extract_sector_fe(keywords: pd.Series) -> pd.Series:
    """
    Extract sector fixed effects from Keywords column.
    """
    def classify_sector(keyword_str):
        if pd.isna(keyword_str):
            return "Other"
        kw = str(keyword_str).lower()
        if any(w in kw for w in ['biotech', 'pharma', 'drug', 'health', 'medical', 'therapeutics']):
            return "Biotech/Healthcare"
        elif any(w in kw for w in ['hardware', 'robotics', 'robot', 'chip', 'semiconductor', 'sensor', 'device']):
            return "Hardware/Robotics"
        elif any(w in kw for w in ['ai', 'machine learning', 'ml', 'artificial intelligence', 'nlp', 'computer vision', 'deep learning']):
            return "AI/ML Software"
        elif any(w in kw for w in ['fintech', 'payment', 'banking', 'crypto', 'blockchain']):
            return "FinTech"
        elif any(w in kw for w in ['data analytics', 'big data', 'business intelligence']):
            return "Data/Analytics"
        elif any(w in kw for w in ['enterprise', 'b2b', 'saas', 'cloud']):
            return "Enterprise Software"
        elif any(w in kw for w in ['consumer', 'b2c', 'mobile app', 'gaming', 'social']):
            return "Consumer Software"
        else:
            return "Other"
    return keywords.apply(classify_sector)

def compute_log_employees(employees: pd.Series) -> pd.Series:
    return np.log1p(pd.to_numeric(employees, errors='coerce').fillna(0))

def compute_firm_age(year_founded: pd.Series, current_year: int = 2024) -> pd.Series:
    years = pd.to_numeric(year_founded, errors='coerce')
    return current_year - years

# Founder credibility
def compute_founder_credibility(df: pd.DataFrame) -> pd.Series:
    """
    Compute founder credibility indicator using PrimaryContactPBId.
    """
    if 'PrimaryContactPBId' in df.columns and 'BusinessStatus' in df.columns:
        tmp = df[['PrimaryContactPBId', 'BusinessStatus']].copy()
        tmp['_has_exit'] = tmp['BusinessStatus'].isin(['Acquired', 'IPO', 'Public']).astype(int)
        has_exit = tmp.groupby('PrimaryContactPBId')['_has_exit'].transform('max')
        return has_exit.fillna(0).astype(int)
    return pd.Series(0, index=df.index)

def compute_serial_entrepreneur(df: pd.DataFrame) -> pd.Series:
    """
    Compute serial entrepreneur indicator (alias for founder credibility).
    Returns 1 if founder has had prior successful exit, 0 otherwise.
    This is used as the moderator for H2-Alt (Credibility hypothesis).
    """
    return compute_founder_credibility(df)

# =========================================================
# Orchestrator
# =========================================================
def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize & engineer all predictors needed for H1/H2.
    """
    df = df.copy()
    mapping = {
        'Description': 'description', 'Keywords': 'keywords',
        'FirstFinancingSize': 'first_financing_size',
        'FirstFinancingDealType': 'first_financing_deal_type',
        'LastFinancingDealType': 'last_financing_deal_type',
        'Employees': 'employees', 'YearFounded': 'year_founded', 'TotalRaised': 'total_raised',
        'CompanyID': 'CompanyID', 'company_id': 'company_id'
    }
    df.rename(columns=mapping, inplace=True, errors='ignore')

    # 1) Vagueness (now uses description AND keywords)
    if 'description' in df.columns and 'keywords' in df.columns:
        df['vagueness'] = compute_vagueness_vectorized(
            df['description'],
            df['keywords']
        )
    elif 'description' in df.columns:
        print("Warning: 'keywords' column not found. Vagueness score based only on description.")
        df['vagueness'] = compute_vagueness_vectorized(
            df['description'],
            pd.Series([""] * len(df), index=df.index)
        )

    # 2) Hardware/Software (moderator)
    if 'keywords' in df.columns:
        desc = df['description'] if 'description' in df.columns else None
        df['is_hardware'] = classify_hardware_vectorized(df['keywords'], desc)

    # 3) Early funding ($M) - ONLY Series A / Early Stage VC
    if 'first_financing_size' in df.columns:
        # Pattern for Series A / Early Stage VC (same as DV creation)
        A_STAGE_PAT = r"(?:\bSeries\s*A(?:[-\s]?\d+|[A-Z])?\b|\bEarly[-\s]*Stage\s*VC\b)"

        # Initialize with the funding amount
        df['early_funding_musd'] = derive_early_funding(df['first_financing_size'])

        # Filter: Set to NaN if NOT Early Stage VC / Series A
        if 'first_financing_deal_type' in df.columns:
            is_series_a = df['first_financing_deal_type'].fillna("").str.contains(
                A_STAGE_PAT, case=False, regex=True, na=False
            )
            # Keep only Series A / Early Stage VC funding
            df.loc[~is_series_a, 'early_funding_musd'] = np.nan
            print(f"  ℹ️  Early funding filtered to Series A / Early Stage VC: {is_series_a.sum():,} of {len(df):,} companies")
        else:
            print("  ⚠️  Warning: 'first_financing_deal_type' not found. Using all first financing rounds.")

    # 4) Growth (DV for H2) - Series B+ indicator
    if 'last_financing_deal_type' in df.columns:
        # Pattern for Series B+: Later Stage VC / Series B-G
        B_PLUS_PAT = r"(?:\bLater[-\s]*Stage\s*VC\b|\bSeries\s*[B-G](?:[-\s]?\d+|[A-Z])?\b)"
        df['growth'] = df['last_financing_deal_type'].fillna("").str.contains(
            B_PLUS_PAT, case=False, regex=True, na=False
        ).astype(int)
        print(f"  ✅ Growth variable created: {df['growth'].sum():,} companies with Series B+ ({df['growth'].mean()*100:.1f}%)")
    else:
        print("  ⚠️  Warning: 'last_financing_deal_type' not found. Growth variable not created.")

    # 5) Sector FE (control for H1)
    if 'keywords' in df.columns:
        df['sector_fe'] = extract_sector_fe(df['keywords'])
        sector_counts = df['sector_fe'].value_counts()
        print(f"  ✅ Sector FE created: {len(sector_counts)} sectors")
    else:
        print("  ⚠️  Warning: 'keywords' not found. Sector FE not created.")

    # 6) Controls
    if 'employees' in df.columns:
        df['employees_log'] = compute_log_employees(df['employees'])
    if 'year_founded' in df.columns:
        df['firm_age'] = compute_firm_age(df['year_founded'])

    return df

# =========================================================
# Preprocessing for H2
# =========================================================
def create_founding_cohort(df: pd.DataFrame, year_col: str = 'year_founded') -> pd.Series:
    if year_col not in df.columns:
        return pd.Series(np.nan, index=df.index)
    bins = [0, 2009, 2014, 2018, 2020, 2021, 9999]
    labels = ['≤2009', '2010-14', '2015-18', '2019-20', '2021', '2022+']
    cohort = pd.cut(df[year_col], bins=bins, labels=labels, right=True)
    return cohort.cat.remove_unused_categories()

def preprocess_for_h2(df: pd.DataFrame, fix_founder_credibility: bool = True) -> pd.DataFrame:
    out = df.copy()
    out['founding_cohort'] = create_founding_cohort(out)

    for col in ['vagueness', 'employees_log']:
        if col in out.columns and out[col].std() not in [0, np.nan]:
            out[f'z_{col}'] = (out[col] - out[col].mean()) / out[col].std()
        else:
            out[f'z_{col}'] = 0

    # CRITICAL FIX: Create founder_serial BEFORE z-scoring or dropping
    # This ensures the binary column persists even if founder_credibility has std=0
    if 'founder_credibility' in out.columns:
        # Create binary column (0 or 1) from continuous credibility
        out['founder_serial'] = (out['founder_credibility'] > 0).astype(int)

        # Now handle z-scoring (founder_credibility may be constant → drop for main spec)
        fc_std = out['founder_credibility'].std()
        if (pd.isna(fc_std) or fc_std == 0) and fix_founder_credibility:
            # Drop the continuous version but KEEP the binary founder_serial
            out = out.drop(columns=['founder_credibility'])
            print(f"  ℹ️  founder_credibility dropped (std=0), but founder_serial preserved (n={out['founder_serial'].sum():,})")
        else:
            # Create z-score if there's variation
            out['z_founder_credibility'] = (out['founder_credibility'] - out['founder_credibility'].mean()) / max(1e-9, out['founder_credibility'].std())
    else:
        # If founder_credibility doesn't exist, create founder_serial as all zeros
        out['founder_serial'] = 0
        print(f"  ⚠️  founder_credibility not found. Created founder_serial=0 for all rows.")

    # FINAL GUARD: Ensure founder_serial has stable dtype and no NaNs
    # This is belt-and-suspenders to prevent any downstream issues
    if 'founder_serial' in out.columns:
        out['founder_serial'] = out['founder_serial'].fillna(0).astype(int)
        # NEVER drop founder_serial - it's required for H3/H4
        assert 'founder_serial' in out.columns, "INTERNAL ERROR: founder_serial was dropped"

    return out
