"""
Analyze 2021 cohort progression with statistical tests

Tracks 2021 Early Stage VC cohort over 2/3/4 years.
Includes HW/SW comparison and hypothesis testing.

Usage: python scripts/analyze_2021_cohort.py [--industry quantum|transportation]
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys
import re

# Optional: matplotlib for plots
try:
    import matplotlib.pyplot as plt
    PLOT_AVAILABLE = True
except ImportError:
    PLOT_AVAILABLE = False
    print("⚠️  matplotlib not available, plots will be skipped")

PROCESSED_DIR = Path("data/processed")

# Parse arguments
industry = None
if len(sys.argv) > 2 and sys.argv[1] == '--industry':
    industry = sys.argv[2]

# Select file
if industry == 'quantum':
    INPUT_FILE = PROCESSED_DIR / "companies_21_23-24-25_quantum.parquet"
    COHORT_NAME = "Quantum Companies"
elif industry == 'transportation':
    INPUT_FILE = PROCESSED_DIR / "companies_21_23-24-25_transportation.parquet"
    COHORT_NAME = "Transportation Companies"
else:
    INPUT_FILE = PROCESSED_DIR / "companies_21_23-24-25.parquet"
    COHORT_NAME = "All Companies"

OUTPUT_DIR = Path("outputs/cohort_2021")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("="*80)
print(f"2021 COHORT ANALYSIS - {COHORT_NAME.upper()}")
print("="*80)

# Classification patterns
PAT_A = re.compile(r"(?:\bEarly\s*Stage\s*VC\b|\bSeries\s*A(?:\b|[\s\-]?\d*)\b)", re.I)
PAT_Bp = re.compile(r"(?:\bLater\s*Stage\s*VC\b|\bSeries\s*[B-G](?:\b|[\s\-]?\d*)\b)", re.I)

def is_early(deal_type):
    return bool(PAT_A.search(deal_type or ""))

def is_later(deal_type):
    return bool(PAT_Bp.search(deal_type or ""))

# Load data
print(f"\nLoading: {INPUT_FILE.name}")
if not INPUT_FILE.exists():
    print(f"✗ File not found!")
    print(f"\nRun this first:")
    print(f"  python scripts/consolidate_2021_cohort.py")
    sys.exit(1)

df = pd.read_parquet(INPUT_FILE)
print(f"✓ Loaded: {len(df):,} companies")

# Define cohort
df['E_2021'] = df['DealType_2021'].apply(is_early)
cohort = df[df['E_2021'] == True].copy()
print(f"✓ Cohort: {len(cohort):,} Early Stage VC companies in 2021.12")

# Calculate L for each year
for year in ['2023', '2024', '2025']:
    col = f'DealType_{year}'
    if col in cohort.columns:
        cohort[f'L_{year}'] = cohort[col].apply(is_later)
    else:
        cohort[f'L_{year}'] = False
        print(f"⚠️  {col} not found, treating as L=0")

# =============================================================================
# Overall Progression Rates
# =============================================================================

print("\n" + "="*80)
print("PROGRESSION RATES")
print("="*80)

results = []
for year, delta_t in [('2023', 2), ('2024', 3), ('2025', 4)]:
    col = f'L_{year}'
    n_progressed = cohort[col].sum()
    rate = n_progressed / len(cohort) * 100

    results.append({
        'Year': year,
        'Years': delta_t,
        'L=1': n_progressed,
        'L=0': len(cohort) - n_progressed,
        'Rate': rate
    })

    print(f"\n{year} ({delta_t} years):")
    print(f"  L=1 (Later Stage): {n_progressed:>5,} / {len(cohort):,} = {rate:5.1f}%")

df_results = pd.DataFrame(results)

# =============================================================================
# HW/SW Comparison (if F_flexibility exists)
# =============================================================================

print("\n" + "="*80)
print("HW/SW COMPARISON")
print("="*80)

# Try to infer HW/SW from keywords if F_flexibility not available
if 'F_flexibility' not in cohort.columns:
    print("\n⚠️  F_flexibility not found, inferring from CompanyName...")

    if 'CompanyName' in cohort.columns:
        # SW keywords
        sw_keywords = ['software', 'platform', 'cloud', 'saas', 'app', 'digital']
        sw_mask = pd.Series([False] * len(cohort))
        for kw in sw_keywords:
            sw_mask |= cohort['CompanyName'].fillna('').str.contains(kw, case=False)

        cohort['F_flexibility'] = sw_mask.astype(int)
        print(f"   Inferred {cohort['F_flexibility'].sum()} SW companies from keywords")
    else:
        print("   Cannot infer F_flexibility (no CompanyName column)")
        cohort['F_flexibility'] = 0  # Default to HW

hw_sw_results = []
if 'F_flexibility' in cohort.columns:
    hw = cohort[cohort['F_flexibility'] == 0]
    sw = cohort[cohort['F_flexibility'] == 1]

    print(f"\nCohort split:")
    print(f"  HW (F=0): {len(hw):,} companies")
    print(f"  SW (F=1): {len(sw):,} companies")

    print(f"\nProgression by Type:")
    print(f"{'Year':<6} {'HW Rate':<12} {'SW Rate':<12} {'Diff':<10} {'p-value':<10}")
    print("-" * 60)

    for year in ['2023', '2024', '2025']:
        col = f'L_{year}'

        hw_prog = hw[col].sum()
        hw_rate = hw_prog / len(hw) * 100 if len(hw) > 0 else 0

        sw_prog = sw[col].sum()
        sw_rate = sw_prog / len(sw) * 100 if len(sw) > 0 else 0

        diff = sw_rate - hw_rate

        # Chi-square test
        from scipy.stats import chi2_contingency
        table = [
            [hw_prog, len(hw) - hw_prog],
            [sw_prog, len(sw) - sw_prog]
        ]
        chi2, p_value, dof, expected = chi2_contingency(table)

        sig = "***" if p_value < 0.001 else "**" if p_value < 0.01 else "*" if p_value < 0.05 else ""

        print(f"{year:<6} {hw_rate:5.1f}%       {sw_rate:5.1f}%       {diff:+6.1f}%    {p_value:.4f}{sig}")

        hw_sw_results.append({
            'Year': year,
            'HW_rate': hw_rate,
            'SW_rate': sw_rate,
            'Diff': diff,
            'p_value': p_value
        })

# =============================================================================
# Statistical Summary
# =============================================================================

print("\n" + "="*80)
print("STATISTICAL SUMMARY")
print("="*80)

print(f"\nCohort: {len(cohort):,} companies at Early Stage VC (2021.12)")
print(f"\nOverall progression:")
for _, row in df_results.iterrows():
    print(f"  {row['Year']} ({row['Years']}yr): {row['Rate']:.1f}% → Later Stage")

if len(hw_sw_results) > 0:
    print(f"\nHW/SW Hypothesis Test:")
    print(f"  H0: SW rate = HW rate")
    print(f"  H1: SW rate > HW rate (SW companies progress faster)")
    print(f"\n  Results:")

    for result in hw_sw_results:
        diff = result['Diff']
        p = result['p_value']

        if p < 0.05 and diff > 0:
            verdict = f"✓ REJECT H0 (SW {diff:+.1f}% faster, p={p:.4f})"
        elif p < 0.05 and diff < 0:
            verdict = f"✗ REJECT H0 (HW faster!, p={p:.4f})"
        else:
            verdict = f"○ FAIL TO REJECT H0 (p={p:.4f})"

        print(f"    {result['Year']}: {verdict}")

# =============================================================================
# Export Results
# =============================================================================

print("\n" + "="*80)
print("EXPORT")
print("="*80)

# Save summary stats
summary_path = OUTPUT_DIR / f"summary_{industry or 'all'}.csv"
df_results.to_csv(summary_path, index=False)
print(f"\n✓ Summary: {summary_path}")

if len(hw_sw_results) > 0:
    hw_sw_path = OUTPUT_DIR / f"hw_sw_comparison_{industry or 'all'}.csv"
    pd.DataFrame(hw_sw_results).to_csv(hw_sw_path, index=False)
    print(f"✓ HW/SW comparison: {hw_sw_path}")

# =============================================================================
# Simple Plot
# =============================================================================

if PLOT_AVAILABLE and len(hw_sw_results) > 0:
    print("\nGenerating plot...")

    fig, ax = plt.subplots(figsize=(8, 5))

    years = [r['Year'] for r in hw_sw_results]
    hw_rates = [r['HW_rate'] for r in hw_sw_results]
    sw_rates = [r['SW_rate'] for r in hw_sw_results]

    x = np.arange(len(years))
    width = 0.35

    ax.bar(x - width/2, hw_rates, width, label='HW (Rigid)', color='#FF6B6B')
    ax.bar(x + width/2, sw_rates, width, label='SW (Flexible)', color='#4ECDC4')

    ax.set_xlabel('Year (Follow-up)')
    ax.set_ylabel('Progression Rate (%)')
    ax.set_title(f'Later Stage VC Progression: HW vs SW\n{COHORT_NAME} (2021 Cohort)')
    ax.set_xticks(x)
    ax.set_xticklabels([f"{y}\n({i+2}yr)" for i, y in enumerate(years)])
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    # Add significance markers
    for i, result in enumerate(hw_sw_results):
        if result['p_value'] < 0.05:
            y = max(result['HW_rate'], result['SW_rate']) + 2
            ax.text(i, y, '*', ha='center', fontsize=16)

    plot_path = OUTPUT_DIR / f"hw_sw_comparison_{industry or 'all'}.png"
    plt.tight_layout()
    plt.savefig(plot_path, dpi=150, bbox_inches='tight')
    print(f"✓ Plot: {plot_path}")
    plt.close()

print("\n" + "="*80)
print("ANALYSIS COMPLETE")
print("="*80)
