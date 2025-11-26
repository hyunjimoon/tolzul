"""
Analyze E→L progression rates over multiple time horizons.

Tracks the SAME cohort (Early Stage VC at baseline 2022.01) over:
- 2.0 years → 2023.12
- 2.5 years → 2024.06
- 3.0 years → 2025.01

This answers: "What % of companies at Early Stage in 2022 progress to
Later Stage within 2/2.5/3 years?"

Run: python tests/analyze_progression_timeline.py
"""

import pandas as pd
import numpy as np
import sys
import re
from pathlib import Path

print("="*80)
print("PROGRESSION TIMELINE ANALYSIS")
print("="*80)
print("\nCohort: Companies at Early Stage VC at baseline (2022.01)")
print("Follow-up periods: 2.0, 2.5, 3.0, 3.9 years")
print()

# =============================================================================
# Configuration
# =============================================================================

BASELINE = "2022.01"
BASELINE_PATH = "data/raw/Company20220101.dat"

# Define observation endpoints
ENDPOINTS = {
    "2.0yr": {
        "date": "2023.12",
        "path": "data/raw/Company20231201.dat",
        "years": 2.0
    },
    "2.5yr": {
        "date": "2024.06",
        "path": "data/raw/Company20240601.dat",
        "years": 2.5
    },
    "3.0yr": {
        "date": "2024.12",
        "path": "data/raw/Company20241201.dat",
        "years": 3.0
    },
    "3.9yr": {
        "date": "2025.11",
        "path": "data/raw/Company20251101.dat",
        "years": 3.9
    }
}

# Classification patterns (from features.py)
PAT_A = re.compile(r"(?:\bEarly\s*Stage\s*VC\b|\bSeries\s*A(?:\b|[\s\-]?\d*)\b)", re.I)
PAT_Bp = re.compile(r"(?:\bLater\s*Stage\s*VC\b|\bSeries\s*[B-G](?:\b|[\s\-]?\d*)\b)", re.I)

def _is_A(deal_type: str) -> bool:
    """Check if deal type is Series A or Early Stage VC"""
    return bool(PAT_A.search(deal_type or ""))

def _is_BPLUS(deal_type: str) -> bool:
    """Check if deal type is Series B+ or Later Stage VC"""
    return bool(PAT_Bp.search(deal_type or ""))

def load_snapshot(path: str, name: str):
    """Load a snapshot with pipe/tab delimiter detection"""
    try:
        df = pd.read_csv(path, sep='|', low_memory=False)
    except:
        try:
            df = pd.read_csv(path, sep='\t', low_memory=False)
        except Exception as e:
            print(f"   ✗ Error loading {name}: {e}")
            return None

    # Detect deal type column
    deal_col = None
    for col in ['LastFinancingDealType', 'LastDealType', 'DealType']:
        if col in df.columns:
            deal_col = col
            break

    if deal_col is None:
        print(f"   ✗ Could not find deal type column in {name}")
        return None

    # Classify
    df['is_A'] = df[deal_col].fillna('').apply(_is_A)
    df['is_BPLUS'] = df[deal_col].fillna('').apply(_is_BPLUS)

    return df

# =============================================================================
# Load Data
# =============================================================================

print("\n" + "="*80)
print("STEP 1: Define 2022 Cohort")
print("="*80)

# Load baseline (defines cohort)
print(f"Loading baseline snapshot ({BASELINE})...")
df_baseline = load_snapshot(BASELINE_PATH, f"Baseline")
if df_baseline is None:
    sys.exit(1)

# Define cohort: E=1 at baseline
cohort_ids = set(df_baseline[df_baseline['is_A'] == True]['CompanyID'])
print(f"✓ Cohort: {len(cohort_ids):,} companies at Early Stage VC in {BASELINE}")

# Load endpoint snapshots
print(f"\nLoading endpoint snapshots...")
endpoint_data = {}
for period, info in ENDPOINTS.items():
    df_end = load_snapshot(info['path'], period)
    if df_end is not None:
        endpoint_data[period] = df_end
        print(f"   ✓ {period} ({info['date']})")
    else:
        print(f"   ⚠️  {period} - file not found, skipping")

if len(endpoint_data) == 0:
    print(f"\n✗ No endpoint data available!")
    sys.exit(1)

# =============================================================================
# Calculate Progression Rates
# =============================================================================

print("\n" + "="*80)
print("STEP 2: Track 2022 Cohort Progression")
print("="*80)

results = []

for period in sorted(endpoint_data.keys()):
    df_end = endpoint_data[period]
    info = ENDPOINTS[period]

    print(f"\n{period} ({info['date']}, Δt = {info['years']} years):")

    # Merge baseline cohort with endpoint (LEFT JOIN to keep all cohort members!)
    df_merged = df_baseline[df_baseline['is_A'] == True][['CompanyID']].merge(
        df_end[['CompanyID', 'is_A', 'is_BPLUS']],
        on='CompanyID',
        how='left'  # ← Keep ALL baseline cohort members
    )

    n_cohort = len(df_merged)  # Should always be 46,129!

    # Three categories (mutually exclusive)
    n_progressed = (df_merged['is_BPLUS'] == True).sum()  # Later Stage at endpoint
    n_stayed = (df_merged['is_A'] == True).sum()          # Still Early Stage at endpoint
    n_other = n_cohort - n_progressed - n_stayed          # Missing/Failed/Acquired/IPO

    rate = n_progressed / n_cohort * 100 if n_cohort > 0 else 0

    print(f"   L=1 (Later Stage):  {n_progressed:,} ({n_progressed/n_cohort*100:.1f}%)")
    print(f"   L=0 (Still Early):  {n_stayed:,} ({n_stayed/n_cohort*100:.1f}%)")
    print(f"   Missing/Other:      {n_other:,} ({n_other/n_cohort*100:.1f}%)")
    print(f"   Total cohort:       {n_cohort:,} (fixed)")

    results.append({
        'period': period,
        'years': info['years'],
        'date': info['date'],
        'cohort_size': n_cohort,
        'progressed': n_progressed,
        'stayed_early': n_stayed,
        'other': n_other,
        'progression_rate': rate
    })

# =============================================================================
# Summary Table
# =============================================================================

print("\n" + "="*80)
print("STEP 3: Summary")
print("="*80)

if len(results) > 0:
    df_results = pd.DataFrame(results)

    print("\n2022 Cohort Progression (46,129 companies):")
    print()
    print(f"{'Period':<10} {'L=1 (Later)':<15} {'L=0 (Early)':<15} {'Missing':<12} {'L=1 Rate':<10}")
    print("-" * 70)

    for _, row in df_results.iterrows():
        print(f"{row['period']:<10} {row['progressed']:>6,} ({row['progressed']/row['cohort_size']*100:4.1f}%)  "
              f"{row['stayed_early']:>6,} ({row['stayed_early']/row['cohort_size']*100:4.1f}%)  "
              f"{row['other']:>6,} ({row['other']/row['cohort_size']*100:4.1f}%)  "
              f"{row['progression_rate']:>6.1f}%")

    print()
    print("Note:")
    print(f"  • Fixed cohort: All companies at Early Stage VC in Jan 2022")
    print(f"  • L=1: Progressed to Later Stage VC (outcome of interest)")
    print(f"  • L=0: Still at Early Stage VC")
    print(f"  • Missing: Failed, acquired, IPO, or missing data")

    # Calculate progression velocity
    if len(results) > 1:
        print("\nProgression Velocity:")
        for i in range(1, len(results)):
            prev = results[i-1]
            curr = results[i]
            delta_years = curr['years'] - prev['years']
            delta_rate = curr['progression_rate'] - prev['progression_rate']
            velocity = delta_rate / delta_years if delta_years > 0 else 0

            print(f"  {prev['period']} → {curr['period']}: "
                  f"+{delta_rate:.1f}% over {delta_years:.1f} years "
                  f"(+{velocity:.1f}%/year)")

    # =============================================================================
    # HW/SW Split Analysis
    # =============================================================================

    print("\n" + "="*80)
    print("HW/SW Comparison")
    print("="*80)

    # Check if F_flexibility column exists in baseline
    if 'F_flexibility' in df_baseline.columns:
        # Split cohort by HW/SW
        cohort_baseline = df_baseline[df_baseline['is_A'] == True].copy()
        hw_cohort = cohort_baseline[cohort_baseline['F_flexibility'] == 0]['CompanyID']
        sw_cohort = cohort_baseline[cohort_baseline['F_flexibility'] == 1]['CompanyID']

        print(f"\nCohort split:")
        print(f"  HW (F=0): {len(hw_cohort):,} companies")
        print(f"  SW (F=1): {len(sw_cohort):,} companies")

        # Calculate progression for each group
        hw_results = []
        sw_results = []

        for period in sorted(endpoint_data.keys()):
            df_end = endpoint_data[period]
            info = ENDPOINTS[period]

            # HW cohort
            hw_merged = pd.DataFrame({'CompanyID': hw_cohort}).merge(
                df_end[['CompanyID', 'is_BPLUS']],
                on='CompanyID',
                how='left'
            )
            hw_progressed = (hw_merged['is_BPLUS'] == True).sum()
            hw_rate = hw_progressed / len(hw_cohort) * 100 if len(hw_cohort) > 0 else 0

            # SW cohort
            sw_merged = pd.DataFrame({'CompanyID': sw_cohort}).merge(
                df_end[['CompanyID', 'is_BPLUS']],
                on='CompanyID',
                how='left'
            )
            sw_progressed = (sw_merged['is_BPLUS'] == True).sum()
            sw_rate = sw_progressed / len(sw_cohort) * 100 if len(sw_cohort) > 0 else 0

            hw_results.append({
                'period': period,
                'years': info['years'],
                'progressed': hw_progressed,
                'rate': hw_rate
            })

            sw_results.append({
                'period': period,
                'years': info['years'],
                'progressed': sw_progressed,
                'rate': sw_rate
            })

        # Print comparison table
        print(f"\nProgression Rates by Type:")
        print()
        print(f"{'Period':<10} {'HW (Rigid)':<20} {'SW (Flexible)':<20} {'Diff':<10}")
        print("-" * 65)

        for i, period in enumerate(sorted(endpoint_data.keys())):
            hw = hw_results[i]
            sw = sw_results[i]
            diff = sw['rate'] - hw['rate']

            print(f"{period:<10} {hw['progressed']:>5,} / {len(hw_cohort):>5,} ({hw['rate']:5.1f}%)  "
                  f"{sw['progressed']:>5,} / {len(sw_cohort):>5,} ({sw['rate']:5.1f}%)  "
                  f"{diff:+6.1f}%")

        print()
        print("Note:")
        print(f"  • HW = F_flexibility=0 (rigid architecture)")
        print(f"  • SW = F_flexibility=1 (flexible software)")
        print(f"  • Diff = SW rate - HW rate (positive means SW progresses faster)")

    else:
        print("\n⚠️  F_flexibility column not found in baseline data")
        print("   Cannot split by HW/SW. Available columns:")
        print(f"   {[c for c in df_baseline.columns if 'flex' in c.lower() or 'architecture' in c.lower()]}")

# =============================================================================
# Export Results
# =============================================================================

print("\n" + "="*80)
print("STEP 4: Export")
print("="*80)

if len(results) > 0:
    output_dir = Path("outputs/diagnostics")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "progression_timeline.csv"
    df_results.to_csv(output_path, index=False)
    print(f"\n✓ Results saved to: {output_path}")

    # Also create detailed cohort tracking file
    print("\nCreating detailed cohort tracking file...")

    # Track each company across all time points
    cohort_df = df_baseline[df_baseline['is_A'] == True][['CompanyID']].copy()
    cohort_df['baseline'] = 'Early Stage VC'

    for period in sorted(endpoint_data.keys()):
        df_end = endpoint_data[period]

        # Merge to get status at this endpoint
        merged = cohort_df[['CompanyID']].merge(
            df_end[['CompanyID', 'is_A', 'is_BPLUS']],
            on='CompanyID',
            how='left'
        )

        # Determine status
        def status(row):
            if pd.isna(row['is_A']) and pd.isna(row['is_BPLUS']):
                return 'Missing'
            elif row['is_BPLUS']:
                return 'Later Stage'
            elif row['is_A']:
                return 'Early Stage'
            else:
                return 'Other'

        cohort_df[period] = merged.apply(status, axis=1)

    cohort_path = output_dir / "cohort_tracking_detailed.csv"
    cohort_df.to_csv(cohort_path, index=False)
    print(f"✓ Detailed tracking saved to: {cohort_path}")
    print(f"  ({len(cohort_df):,} companies tracked)")

print("\n" + "="*80)
print("ANALYSIS COMPLETE")
print("="*80)
