#!/usr/bin/env python3
"""
Analyze Venture Dataset for xarray Structure Design
====================================================

This script analyzes the 541K+ venture dataset to inform xarray structure design
for nested panel data with dimensions: venture_id × window (cohort_year, end_year).

Goal: Test how promise vagueness affects funding across stages

Usage:
    python analyze_for_xarray_design.py [--data-file PATH]

Options:
    --data-file PATH    Path to parquet file (default: data/processed/consolidated_companies*.parquet)
"""

import sys
import argparse
from pathlib import Path
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_data(data_file: Path = None) -> pd.DataFrame:
    """Load consolidated company data.

    Args:
        data_file: Path to parquet file, or None to search for consolidated file

    Returns:
        DataFrame with company data
    """
    if data_file is None:
        # Search for consolidated parquet files
        processed_dir = Path("data/processed")
        parquet_files = list(processed_dir.glob("consolidated_companies*.parquet"))

        if not parquet_files:
            raise FileNotFoundError(
                "No consolidated parquet file found. Please specify --data-file or run pipeline/01_load_data.py first"
            )

        # Use the most recent file
        data_file = max(parquet_files, key=lambda p: p.stat().st_mtime)
        logger.info(f"📂 Using data file: {data_file}")

    logger.info(f"Loading {data_file}...")
    df = pd.read_parquet(data_file)
    logger.info(f"✓ Loaded {len(df):,} companies with {len(df.columns)} columns")

    return df


def analyze_venture_dimension(df: pd.DataFrame) -> Dict:
    """Analyze venture dimension (N).

    Returns summary of:
    - Unique CompanyID count
    - Geographic diversity (HQCountry)
    - Sector diversity
    """
    logger.info("\n" + "=" * 80)
    logger.info("1️⃣  VENTURE DIMENSION ANALYSIS")
    logger.info("=" * 80)

    results = {}

    # Unique companies
    company_id_col = 'CompanyID' if 'CompanyID' in df.columns else 'company_id'
    if company_id_col in df.columns:
        n_companies = df[company_id_col].nunique()
        results['n_ventures'] = n_companies
        logger.info(f"\n✓ Unique ventures (N): {n_companies:,}")
    else:
        logger.warning("⚠️  No CompanyID column found")
        results['n_ventures'] = len(df)

    # Geographic diversity
    geo_col = 'HQCountry' if 'HQCountry' in df.columns else 'hq_country'
    if geo_col in df.columns:
        country_dist = df[geo_col].value_counts()
        results['countries'] = {
            'n_countries': len(country_dist),
            'top_5': country_dist.head(5).to_dict(),
            'coverage': (df[geo_col].notna().sum() / len(df)) * 100
        }
        logger.info(f"\n📍 Geographic Diversity:")
        logger.info(f"   Total countries: {len(country_dist)}")
        logger.info(f"   Coverage: {results['countries']['coverage']:.1f}%")
        logger.info(f"   Top 5 countries:")
        for country, count in country_dist.head(5).items():
            logger.info(f"      {country}: {count:,} ({count/len(df)*100:.1f}%)")

    # Sector diversity
    sector_col = None
    for col in ['Sector', 'sector', 'PrimarySector', 'primary_sector']:
        if col in df.columns:
            sector_col = col
            break

    if sector_col:
        sector_dist = df[sector_col].value_counts()
        results['sectors'] = {
            'n_sectors': len(sector_dist),
            'top_10': sector_dist.head(10).to_dict(),
            'coverage': (df[sector_col].notna().sum() / len(df)) * 100
        }
        logger.info(f"\n🏢 Sector Diversity:")
        logger.info(f"   Total sectors: {len(sector_dist)}")
        logger.info(f"   Coverage: {results['sectors']['coverage']:.1f}%")
        logger.info(f"   Top 10 sectors:")
        for sector, count in sector_dist.head(10).items():
            logger.info(f"      {sector}: {count:,} ({count/len(df)*100:.1f}%)")

    return results


def analyze_window_dimension(df: pd.DataFrame) -> Dict:
    """Analyze window dimension candidates.

    Returns:
    - Financing date range for cohort assignment
    - Deal type progression (Seed → A → B) for outcome tracking
    """
    logger.info("\n" + "=" * 80)
    logger.info("2️⃣  WINDOW DIMENSION ANALYSIS")
    logger.info("=" * 80)

    results = {}

    # Financing dates
    date_cols = []
    for col in df.columns:
        if 'date' in col.lower() or 'year' in col.lower():
            date_cols.append(col)

    logger.info(f"\n📅 Date-related columns found: {len(date_cols)}")
    for col in date_cols[:10]:  # Show first 10
        coverage = (df[col].notna().sum() / len(df)) * 100
        logger.info(f"   {col}: {coverage:.1f}% coverage")

    # Look for Series A year
    series_a_year_col = None
    for col in ['SeriesAYear', 'series_a_year', 'series_A_year']:
        if col in df.columns:
            series_a_year_col = col
            break

    if series_a_year_col:
        series_a_years = df[series_a_year_col].dropna()
        if len(series_a_years) > 0:
            results['series_a_years'] = {
                'min': int(series_a_years.min()),
                'max': int(series_a_years.max()),
                'coverage': (len(series_a_years) / len(df)) * 100,
                'distribution': series_a_years.value_counts().sort_index().to_dict()
            }
            logger.info(f"\n💰 Series A Year Distribution:")
            logger.info(f"   Range: {results['series_a_years']['min']} - {results['series_a_years']['max']}")
            logger.info(f"   Coverage: {results['series_a_years']['coverage']:.1f}%")

            # Show distribution for recent years
            recent_years = series_a_years.value_counts().sort_index().tail(10)
            logger.info(f"   Recent years distribution:")
            for year, count in recent_years.items():
                logger.info(f"      {int(year)}: {count:,} companies")

    # Deal type progression
    deal_cols = [col for col in df.columns if 'deal' in col.lower() or 'round' in col.lower() or 'series' in col.lower()]
    logger.info(f"\n🔄 Deal progression columns found: {len(deal_cols)}")
    for col in deal_cols[:15]:
        coverage = (df[col].notna().sum() / len(df)) * 100
        logger.info(f"   {col}: {coverage:.1f}% coverage")

    return results


def analyze_key_variables(df: pd.DataFrame) -> Dict:
    """Analyze key variable distributions.

    Returns stats for:
    - Vagueness proxy: Description, Keywords (text length, specificity)
    - Exercisability: Infer HW/SW from Keywords
    - Outcomes: FirstFinancingSize (E), Series B indicators (L)
    - Controls: Employees, HQCountry, YearFounded
    """
    logger.info("\n" + "=" * 80)
    logger.info("3️⃣  KEY VARIABLE DISTRIBUTIONS")
    logger.info("=" * 80)

    results = {}

    # 🔹 VAGUENESS PROXY
    logger.info("\n📝 Vagueness Proxies:")

    desc_col = 'Description' if 'Description' in df.columns else 'description'
    if desc_col in df.columns:
        desc_lengths = df[desc_col].dropna().str.len()
        results['description'] = {
            'coverage': (df[desc_col].notna().sum() / len(df)) * 100,
            'length_stats': {
                'mean': float(desc_lengths.mean()),
                'median': float(desc_lengths.median()),
                'min': int(desc_lengths.min()),
                'max': int(desc_lengths.max())
            }
        }
        logger.info(f"   Description:")
        logger.info(f"      Coverage: {results['description']['coverage']:.1f}%")
        logger.info(f"      Length - Mean: {desc_lengths.mean():.0f}, Median: {desc_lengths.median():.0f}")
        logger.info(f"      Range: {desc_lengths.min()}-{desc_lengths.max()} chars")

    kw_col = 'Keywords' if 'Keywords' in df.columns else 'keywords'
    if kw_col in df.columns:
        kw_lengths = df[kw_col].dropna().str.len()
        results['keywords'] = {
            'coverage': (df[kw_col].notna().sum() / len(df)) * 100,
            'length_stats': {
                'mean': float(kw_lengths.mean()),
                'median': float(kw_lengths.median()),
                'min': int(kw_lengths.min()) if len(kw_lengths) > 0 else 0,
                'max': int(kw_lengths.max()) if len(kw_lengths) > 0 else 0
            }
        }
        logger.info(f"   Keywords:")
        logger.info(f"      Coverage: {results['keywords']['coverage']:.1f}%")
        logger.info(f"      Length - Mean: {kw_lengths.mean():.0f}, Median: {kw_lengths.median():.0f}")

    # 🔹 EXERCISABILITY (HW/SW)
    logger.info("\n⚙️  Exercisability (HW/SW inference):")

    # Look for existing HW/SW indicators
    hw_sw_cols = [col for col in df.columns if 'hardware' in col.lower() or 'software' in col.lower()]
    if hw_sw_cols:
        logger.info(f"   Found {len(hw_sw_cols)} HW/SW indicator columns:")
        for col in hw_sw_cols:
            if df[col].dtype in [bool, int, 'Int64']:
                value_counts = df[col].value_counts()
                logger.info(f"      {col}: {value_counts.to_dict()}")

    # Infer from keywords/description
    if kw_col in df.columns or desc_col in df.columns:
        text_col = kw_col if kw_col in df.columns else desc_col
        text_data = df[text_col].fillna('').str.lower()

        hw_keywords = ['hardware', 'chip', 'sensor', 'device', 'robotics', 'manufacturing']
        sw_keywords = ['software', 'platform', 'saas', 'app', 'cloud', 'api']

        hw_matches = text_data.str.contains('|'.join(hw_keywords), case=False, na=False).sum()
        sw_matches = text_data.str.contains('|'.join(sw_keywords), case=False, na=False).sum()

        logger.info(f"   Inferred from text:")
        logger.info(f"      Hardware mentions: {hw_matches:,} ({hw_matches/len(df)*100:.1f}%)")
        logger.info(f"      Software mentions: {sw_matches:,} ({sw_matches/len(df)*100:.1f}%)")

    # 🔹 OUTCOMES
    logger.info("\n💰 Outcomes:")

    # Early funding (E)
    financing_cols = [col for col in df.columns if 'financing' in col.lower() or 'amount' in col.lower()]
    logger.info(f"   Financing columns found: {len(financing_cols)}")
    for col in financing_cols[:10]:
        coverage = (df[col].notna().sum() / len(df)) * 100
        if coverage > 5:  # Only show meaningful columns
            logger.info(f"      {col}: {coverage:.1f}% coverage")
            if pd.api.types.is_numeric_dtype(df[col]):
                values = df[col].dropna()
                logger.info(f"         Mean: ${values.mean():,.0f}, Median: ${values.median():,.0f}")

    # Series B indicator (L)
    series_b_cols = [col for col in df.columns if 'series' in col.lower() and 'b' in col.lower()]
    logger.info(f"\n   Series B indicator columns found: {len(series_b_cols)}")
    for col in series_b_cols[:5]:
        coverage = (df[col].notna().sum() / len(df)) * 100
        logger.info(f"      {col}: {coverage:.1f}% coverage")

    # 🔹 CONTROLS
    logger.info("\n📊 Control Variables:")

    # Employees
    emp_col = 'Employees' if 'Employees' in df.columns else 'employees'
    if emp_col in df.columns:
        emp_data = pd.to_numeric(df[emp_col], errors='coerce').dropna()
        if len(emp_data) > 0:
            results['employees'] = {
                'coverage': (len(emp_data) / len(df)) * 100,
                'stats': {
                    'mean': float(emp_data.mean()),
                    'median': float(emp_data.median()),
                    'p25': float(emp_data.quantile(0.25)),
                    'p75': float(emp_data.quantile(0.75))
                }
            }
            logger.info(f"   Employees:")
            logger.info(f"      Coverage: {results['employees']['coverage']:.1f}%")
            logger.info(f"      Mean: {emp_data.mean():.0f}, Median: {emp_data.median():.0f}")
            logger.info(f"      P25: {emp_data.quantile(0.25):.0f}, P75: {emp_data.quantile(0.75):.0f}")

    # Founding year
    year_col = 'YearFounded' if 'YearFounded' in df.columns else 'year_founded'
    if year_col in df.columns:
        year_data = pd.to_numeric(df[year_col], errors='coerce').dropna()
        if len(year_data) > 0:
            results['founding_year'] = {
                'coverage': (len(year_data) / len(df)) * 100,
                'range': (int(year_data.min()), int(year_data.max())),
                'distribution': year_data.value_counts().sort_index().tail(10).to_dict()
            }
            logger.info(f"   Founding Year:")
            logger.info(f"      Coverage: {results['founding_year']['coverage']:.1f}%")
            logger.info(f"      Range: {int(year_data.min())} - {int(year_data.max())}")

    return results


def extract_sector_hierarchy(df: pd.DataFrame) -> Dict:
    """Extract sector → industry hierarchy.

    Returns:
    - Sector to industry mapping
    - Suggested groupings
    """
    logger.info("\n" + "=" * 80)
    logger.info("4️⃣  SECTOR → INDUSTRY HIERARCHY")
    logger.info("=" * 80)

    results = {}

    # Find sector column
    sector_col = None
    for col in ['Sector', 'sector', 'PrimarySector', 'primary_sector']:
        if col in df.columns:
            sector_col = col
            break

    if not sector_col:
        logger.warning("⚠️  No sector column found")
        return results

    # Get sector distribution
    sector_dist = df[sector_col].value_counts()

    logger.info(f"\n📋 Sector Distribution ({len(sector_dist)} unique sectors):")
    for i, (sector, count) in enumerate(sector_dist.items(), 1):
        if i <= 20:  # Show top 20
            logger.info(f"   {i:2d}. {sector}: {count:,} ({count/len(df)*100:.1f}%)")

    # Suggest industry groupings based on common patterns
    suggested_mappings = {
        "Transportation": ["Autonomous", "EV Charging", "Ride-sharing", "Logistics", "Mobility"],
        "Quantum": ["Quantum", "Computing HW", "Quantum SW", "Sensing"],
        "Software": ["Enterprise Software", "Consumer Software", "SaaS"],
        "Healthcare": ["Biotech", "Healthcare", "Medical"],
        "FinTech": ["FinTech", "Financial Services", "Payments"],
        "Hardware": ["Hardware", "Robotics", "Manufacturing"]
    }

    logger.info("\n🗂️  Suggested Industry Groupings:")
    actual_mappings = {}
    for industry, keywords in suggested_mappings.items():
        matched_sectors = []
        for sector in sector_dist.index:
            sector_str = str(sector).lower()
            if any(kw.lower() in sector_str for kw in keywords):
                matched_sectors.append(sector)

        if matched_sectors:
            actual_mappings[industry] = matched_sectors
            logger.info(f"\n   {industry}:")
            for sector in matched_sectors:
                count = sector_dist[sector]
                logger.info(f"      • {sector}: {count:,} companies")

    results['suggested_mappings'] = actual_mappings
    results['sector_distribution'] = sector_dist.head(20).to_dict()

    return results


def assess_data_completeness(df: pd.DataFrame) -> Dict:
    """Assess data completeness and missing rates.

    Returns:
    - Missing rates for critical variables
    - Feasibility of time-varying L construction
    """
    logger.info("\n" + "=" * 80)
    logger.info("5️⃣  DATA COMPLETENESS ASSESSMENT")
    logger.info("=" * 80)

    results = {}

    # Critical variables for xarray construction
    critical_vars = {
        'CompanyID': ['CompanyID', 'company_id'],
        'Description': ['Description', 'description'],
        'Keywords': ['Keywords', 'keywords'],
        'FirstFinancingSize': ['FirstFinancingSize', 'first_financing_size'],
        'Employees': ['Employees', 'employees'],
        'YearFounded': ['YearFounded', 'year_founded'],
        'HQCountry': ['HQCountry', 'hq_country'],
        'SeriesAYear': ['SeriesAYear', 'series_a_year', 'series_A_year']
    }

    logger.info("\n📊 Missing Rates for Critical Variables:")
    logger.info(f"\n{'Variable':<25} {'Column':<25} {'Present':<12} {'Missing':<12} {'Coverage':<10}")
    logger.info("-" * 85)

    completeness = {}
    for var_name, possible_cols in critical_vars.items():
        found = False
        for col in possible_cols:
            if col in df.columns:
                n_present = df[col].notna().sum()
                n_missing = df[col].isna().sum()
                coverage = (n_present / len(df)) * 100

                completeness[var_name] = {
                    'column': col,
                    'coverage': coverage,
                    'n_present': n_present,
                    'n_missing': n_missing
                }

                logger.info(f"{var_name:<25} {col:<25} {n_present:<12,} {n_missing:<12,} {coverage:>8.1f}%")
                found = True
                break

        if not found:
            logger.info(f"{var_name:<25} {'NOT FOUND':<25} {'-':<12} {'-':<12} {'-':<10}")
            completeness[var_name] = {'column': None, 'coverage': 0}

    results['completeness'] = completeness

    # Time-varying data feasibility
    logger.info("\n\n⏰ Time-Varying Data Feasibility:")

    # Check for multiple snapshots
    if 'snapshot_date' in df.columns:
        n_snapshots = df['snapshot_date'].nunique()
        logger.info(f"   Snapshot dates: {n_snapshots}")
        logger.info(f"   Companies per snapshot: {len(df) / n_snapshots:.0f} (avg)")
        results['time_varying_feasible'] = True
    else:
        logger.info(f"   ⚠️  No snapshot_date column - single cross-section")
        results['time_varying_feasible'] = False

    # Check for financing progression data
    financing_rounds = [col for col in df.columns if 'series' in col.lower() or 'round' in col.lower()]
    logger.info(f"   Financing round columns: {len(financing_rounds)}")
    if financing_rounds:
        logger.info(f"   Examples: {', '.join(financing_rounds[:5])}")

    return results


def generate_xarray_schema(
    venture_stats: Dict,
    window_stats: Dict,
    variable_stats: Dict,
    sector_stats: Dict,
    completeness: Dict
) -> str:
    """Generate recommended xarray schema with actual dimensions.

    Args:
        venture_stats: Results from analyze_venture_dimension
        window_stats: Results from analyze_window_dimension
        variable_stats: Results from analyze_key_variables
        sector_stats: Results from extract_sector_hierarchy
        completeness: Results from assess_data_completeness

    Returns:
        Formatted xarray schema as string
    """
    logger.info("\n" + "=" * 80)
    logger.info("6️⃣  RECOMMENDED XARRAY SCHEMA")
    logger.info("=" * 80)

    n_ventures = venture_stats.get('n_ventures', 'N')

    # Determine cohort years from Series A distribution
    cohort_years = [2021, 2022, 2023]  # Default
    if 'series_a_years' in window_stats and 'distribution' in window_stats['series_a_years']:
        # Use years with sufficient companies (>100)
        dist = window_stats['series_a_years']['distribution']
        cohort_years = sorted([int(year) for year, count in dist.items() if count >= 100])[-5:]

    end_years = list(range(cohort_years[-1] + 1, cohort_years[-1] + 4))  # 3 years forward

    schema = f"""
<xarray.Dataset>
Dimensions:
  venture_id: {n_ventures:,}
  window: {len(cohort_years) * len(end_years)}  # Cohort × End year combinations

Coordinates:
  * venture_id                  (venture_id) int64
  * window                      (window) MultiIndex[('cohort_year', 'end_year')]
    cohort_year                 (window) int16   # {cohort_years}
    end_year                    (window) int16   # {end_years}
    horizon_years               (window) int16   # computed: end - cohort

  # Industry hierarchy (Parent Reference)
    sector                      (venture_id) string   # {venture_stats.get('sectors', {}).get('n_sectors', 'N')} unique sectors
    industry                    (venture_id) string   # Grouped from sector
    dataset_source              (venture_id) string   # "transportation", "quantum", "all"

Data variables:
  # Time-varying outcomes
  L                             (venture_id, window) float32  # Series B+ reached
  at_risk                       (venture_id, window) int8     # 1 if cohort_year matches venture's Series A year
  step_up_multiple              (venture_id, window) float32  # Pre(t+1)/Post(t), NaN if L=0

  # Static predictors (measured at Series A)
  z_vagueness                   (venture_id) float32   # Standardized vagueness score
  z_vagueness_winsorized        (venture_id) float32   # Winsorized version
  v_abstract_raw                (venture_id) float32   # Categorical vagueness component
  v_concrete_deficit_raw        (venture_id) float32   # Concreteness deficit component

  # Moderators
  is_software                   (venture_id) int8     # F: exercisability (0=HW, 1=SW)
  option_level                  (venture_id) int8     # 1=Rigid, 2=Modular, 3=Flexible
  founder_is_serial             (venture_id) int8     # C: credibility

  # Controls
  E_amount_log                  (venture_id) float32  # Early funding (log USD)
  z_employees_log               (venture_id) float32  # Log employees (standardized)
  founding_year                 (venture_id) int16
  series_A_year                 (venture_id) int16    # for at_risk computation
  hq_country                    (venture_id) string

  # Metadata for validation
  company_name                  (venture_id) string
  primary_description           (venture_id) string

Attributes:
  schema_version: "esi-panel.v4"

  sector_to_industry: {{
"""

    # Add sector mappings
    if 'suggested_mappings' in sector_stats:
        for industry, sectors in sector_stats['suggested_mappings'].items():
            for sector in sectors[:3]:  # Show first 3 examples
                schema += f'    "{sector}": "{industry}",\n'

    schema += f"""  }}

  window_logic: "at_risk[i,w]=1 iff series_A_year[i]==cohort_year[w]"

  cohort_years: {cohort_years}
  end_years: {end_years}

  spec_curve_config: {{
    "n_specs": 64,
    "factors": {{
      "windows": {end_years},
      "scaling": ["z-score", "winsorized"],
      "controls_location": [True, False],
      "controls_E": [True, False],
      "interaction_C": [True, False]
    }}
  }}

  vagueness_formula: "0.5*max(v_abstract, v_concrete_deficit) + 0.5*mean(...)"

  data_quality: {{
    "n_ventures": {n_ventures:,},
    "description_coverage": {variable_stats.get('description', {}).get('coverage', 0):.1f}%,
    "employees_coverage": {variable_stats.get('employees', {}).get('coverage', 0):.1f}%,
    "founding_year_coverage": {variable_stats.get('founding_year', {}).get('coverage', 0):.1f}%
  }}

Notes:
  - at_risk variable identifies which cohort_year each venture belongs to
  - No need for is_2021cohort, is_2022cohort etc. - use series_A_year coordinate
  - L (Series B+ reached) is time-varying across windows
  - All predictors are static (measured at Series A)
"""

    logger.info(schema)

    return schema


def main():
    """Main analysis workflow."""
    parser = argparse.ArgumentParser(description='Analyze venture dataset for xarray design')
    parser.add_argument('--data-file', type=Path, help='Path to parquet file')
    args = parser.parse_args()

    logger.info("=" * 80)
    logger.info("VENTURE DATASET ANALYSIS FOR XARRAY STRUCTURE DESIGN")
    logger.info("=" * 80)

    try:
        # Load data
        df = load_data(args.data_file)

        # Run analyses
        venture_stats = analyze_venture_dimension(df)
        window_stats = analyze_window_dimension(df)
        variable_stats = analyze_key_variables(df)
        sector_stats = extract_sector_hierarchy(df)
        completeness_stats = assess_data_completeness(df)

        # Generate schema
        schema = generate_xarray_schema(
            venture_stats,
            window_stats,
            variable_stats,
            sector_stats,
            completeness_stats
        )

        # Save results
        output_dir = Path("outputs/xarray_design")
        output_dir.mkdir(exist_ok=True, parents=True)

        # Save schema
        schema_file = output_dir / "recommended_xarray_schema.txt"
        schema_file.write_text(schema)
        logger.info(f"\n💾 Schema saved to: {schema_file}")

        # Save stats as JSON
        import json
        stats_file = output_dir / "analysis_stats.json"
        stats = {
            'venture_dimension': venture_stats,
            'window_dimension': window_stats,
            'key_variables': variable_stats,
            'sector_hierarchy': sector_stats,
            'completeness': completeness_stats
        }

        # Convert numpy types to native Python for JSON serialization
        def convert_types(obj):
            if isinstance(obj, dict):
                return {k: convert_types(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_types(item) for item in obj]
            elif isinstance(obj, (np.integer, np.floating)):
                return float(obj)
            elif pd.isna(obj):
                return None
            else:
                return obj

        stats = convert_types(stats)

        stats_file.write_text(json.dumps(stats, indent=2))
        logger.info(f"📊 Statistics saved to: {stats_file}")

        logger.info("\n" + "=" * 80)
        logger.info("✅ ANALYSIS COMPLETE")
        logger.info("=" * 80)
        logger.info(f"\nNext steps:")
        logger.info(f"1. Review schema: {schema_file}")
        logger.info(f"2. Review stats: {stats_file}")
        logger.info(f"3. Use insights to construct xarray.Dataset")
        logger.info(f"4. Implement cohort_year calculation: series_A_year coordinate")
        logger.info(f"5. Implement at_risk variable: (series_A_year == cohort_year)")

        return 0

    except Exception as e:
        logger.error(f"❌ Error: {e}", exc_info=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())
