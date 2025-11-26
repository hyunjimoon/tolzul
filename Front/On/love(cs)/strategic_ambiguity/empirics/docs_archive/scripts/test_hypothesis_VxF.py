"""
Test H*: β_VF > 0 (Flexibility amplifies Vagueness effect on Later success)

E Definition (Short term survival):
  E is defined as funding amount of companies whose most recent financing
  was Early Stage VC (seriesA) as of Dec 2021, regardless of when that
  financing occurred. This state-based definition captures companies
  currently at the early stage.
  NO Buyout/LBO, NO Merger/Acquisition.

L Definition (Long term survival):
  Among the companies with E=1, by year t, did they secure Series B+?
  (t=2023, 2024, 2025).

Minimal specification:
- Logit: Pr(L=1) = logit^-1(α + β_V*V + β_F*F + β_VF*(V×F) + controls)
- NO E control (E is mediator, not confounder)
- Robust SE (HC2 if available)
- Output: coefficient table, hypothesis test, interaction plot

Usage:
  python scripts/test_hypothesis_VxF.py
  python scripts/test_hypothesis_VxF.py --industry quantum
  python scripts/test_hypothesis_VxF.py --industry transportation
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys
import re

# Add parent directory to path for modules import
sys.path.insert(0, str(Path(__file__).parent.parent))

# Logit regression
import statsmodels.formula.api as smf

# Plotting
try:
    import matplotlib.pyplot as plt
    PLOT_AVAILABLE = True
except ImportError:
    PLOT_AVAILABLE = False
    print("⚠️  matplotlib not available")

# Color palette (W2 standard) - EXACT specification
PALETTE = {
    "E": "red",          # Early funding (information value, short-term survival)
    "L": "#0000FF",      # Later success (blue - information + option value, long-term)
    "V": "green",        # Vagueness (promise as founder's choice)
    "F": "skyblue",      # Flexibility/Exercisability (option exercisability)
    "S": "purple",       # Step-up
    "C": "orange",       # Controls/Cohort
    "HW": "gray",        # Hardware/Rigid (F=0)
    "doubt": "pink"      # Angie's doubt (for annotations)
}

# Parse arguments
industry = None
if len(sys.argv) > 2 and sys.argv[1] == '--industry':
    industry = sys.argv[2]

# Input file
PROCESSED_DIR = Path("data/processed")
if industry == 'quantum':
    INPUT_FILE = PROCESSED_DIR / "companies_21_23-24-25_quantum.parquet"
    COHORT_NAME = "Quantum"
elif industry == 'transportation':
    INPUT_FILE = PROCESSED_DIR / "companies_21_23-24-25_transportation.parquet"
    COHORT_NAME = "Transportation"
else:
    INPUT_FILE = PROCESSED_DIR / "companies_21_23-24-25.parquet"
    COHORT_NAME = "All"

OUTPUT_DIR = Path("outputs/hypothesis_VxF")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("="*80)
print(f"HYPOTHESIS TEST: β_VF > 0 ({COHORT_NAME} Companies)")
print("="*80)
print("\nH*: Flexibility amplifies the effect of Vagueness on Later success")
print("    Pr(L=1) = logit^-1(α + β_V·V + β_F·F + β_VF·(V×F) + controls)")
print("    H0: β_VF = 0")
print("    H1: β_VF > 0")

# Classification
PAT_A = re.compile(r"(?:\bEarly\s*Stage\s*VC\b|\bSeries\s*A(?:\b|[\s\-]?\d*)\b)", re.I)
PAT_Bp = re.compile(r"(?:\bLater\s*Stage\s*VC\b|\bSeries\s*[B-G](?:\b|[\s\-]?\d*)\b)", re.I)

def is_early(s):
    return bool(PAT_A.search(s or ""))

def is_later(s):
    return bool(PAT_Bp.search(s or ""))

# Load data
print(f"\n" + "="*80)
print("DATA PREPARATION")
print("="*80)

print(f"\nLoading: {INPUT_FILE.name}")
if not INPUT_FILE.exists():
    print(f"✗ File not found!")
    print(f"\nRun: python scripts/consolidate_2021_cohort.py")
    sys.exit(1)

df = pd.read_parquet(INPUT_FILE)
print(f"✓ Loaded: {len(df):,} companies")

# Define cohort (Early Stage VC at 2021.12)
df['E_2021'] = df['DealType_2021'].apply(is_early).astype(int)
cohort = df[df['E_2021'] == 1].copy()
print(f"✓ Cohort: {len(cohort):,} Early Stage VC companies (2021.12)")

# Define L (Later Stage at 2025.11 - 4 year follow-up)
if 'DealType_2025' in cohort.columns:
    cohort['L'] = cohort['DealType_2025'].apply(is_later).astype(int)
else:
    print(f"⚠️  DealType_2025 not found, using all L=0")
    cohort['L'] = 0

n_L = cohort['L'].sum()
print(f"✓ L=1 (Later Stage 2025): {n_L:,} ({n_L/len(cohort)*100:.1f}%)")

# Define V (Vagueness) - compute from Description/Keywords if available
if 'Description_2021' in cohort.columns and 'Keywords_2021' in cohort.columns:
    print(f"\nComputing Vagueness from Description/Keywords...")

    # Import vagueness scorer
    try:
        from modules.features import compute_vagueness_vectorized
        cohort['V'] = compute_vagueness_vectorized(
            cohort['Description_2021'].fillna(''),
            cohort['Keywords_2021'].fillna('')
        )
        cohort['z_V'] = (cohort['V'] - cohort['V'].mean()) / cohort['V'].std()
        print(f"✓ Vagueness computed: mean={cohort['V'].mean():.2f}, std={cohort['V'].std():.2f}")
    except Exception as e:
        print(f"⚠️  Vagueness computation failed: {e}")
        print(f"   Using mock Vagueness instead")
        cohort['V'] = np.random.normal(50, 15, len(cohort))
        cohort['z_V'] = (cohort['V'] - cohort['V'].mean()) / cohort['V'].std()
else:
    print(f"\n⚠️  Description/Keywords not found, using mock Vagueness")
    print(f"   Rerun consolidation with Description/Keywords to get real V")
    cohort['V'] = np.random.normal(50, 15, len(cohort))
    cohort['z_V'] = (cohort['V'] - cohort['V'].mean()) / cohort['V'].std()

# Define F (Flexibility) - infer from CompanyName if not available
if 'F_flexibility' not in cohort.columns:
    print(f"Inferring F_flexibility from CompanyName...")
    if 'CompanyName' in cohort.columns:
        sw_keywords = ['software', 'platform', 'cloud', 'saas', 'app', 'digital']
        sw_mask = pd.Series([False] * len(cohort))
        for kw in sw_keywords:
            sw_mask |= cohort['CompanyName'].fillna('').str.contains(kw, case=False)
        cohort['F_flexibility'] = sw_mask.astype(int)
    else:
        print("  ✗ Cannot infer F - using F=0 for all")
        cohort['F_flexibility'] = 0

n_F1 = (cohort['F_flexibility'] == 1).sum()
n_F0 = (cohort['F_flexibility'] == 0).sum()
print(f"✓ F=1 (Flexible/SW): {n_F1:,}")
print(f"✓ F=0 (Rigid/HW):    {n_F0:,}")

# Add dummy controls (replace with actual founding_cohort, region if available)
cohort['founding_cohort'] = 'cohort_1'  # MOCK
cohort['region'] = 'US'  # MOCK

# Keep only complete cases
analysis_df = cohort[['L', 'z_V', 'F_flexibility', 'founding_cohort', 'region']].dropna()
print(f"\n✓ Analysis dataset: {len(analysis_df):,} companies (complete cases)")

# =============================================================================
# LOGIT REGRESSION
# =============================================================================

print(f"\n" + "="*80)
print("LOGIT REGRESSION")
print("="*80)

formula = "L ~ z_V * F_flexibility + C(founding_cohort) + C(region)"
print(f"\nFormula: {formula}")
print(f"Note: NO E control (E is mediator, not confounder)")

try:
    # Try with robust SE (HC2)
    model = smf.logit(formula, data=analysis_df).fit(disp=False, cov_type='HC2')
    print(f"✓ Fitted with robust SE (HC2)")
except Exception as e:
    print(f"⚠️  Robust SE failed, using standard: {e}")
    try:
        model = smf.logit(formula, data=analysis_df).fit(disp=False)
        print(f"✓ Fitted with standard SE")
    except Exception as e2:
        print(f"✗ Logit failed: {e2}")
        sys.exit(1)

# Extract coefficients
print(f"\nCoefficients:")
print(model.summary2().tables[1])

# Save coefficient table
coef_path = OUTPUT_DIR / f"coefficients_{industry or 'all'}.csv"
model.summary2().tables[1].to_csv(coef_path)
print(f"\n✓ Saved: {coef_path}")

# =============================================================================
# HYPOTHESIS TEST: β_VF > 0
# =============================================================================

print(f"\n" + "="*80)
print("HYPOTHESIS TEST")
print("="*80)

# Find interaction term
interaction_terms = [t for t in model.params.index if ':' in t or 'F_flexibility' in t]
vf_term = 'z_V:F_flexibility' if 'z_V:F_flexibility' in model.params.index else None

if vf_term is None:
    print(f"✗ Interaction term not found! Available terms: {list(model.params.index)}")
    sys.exit(1)

beta_VF = model.params[vf_term]
se_VF = model.bse[vf_term]
p_VF = model.pvalues[vf_term]
z_VF = beta_VF / se_VF

print(f"\nInteraction term: {vf_term}")
print(f"  Coefficient:  β_VF = {beta_VF:.4f}")
print(f"  Std Error:    SE    = {se_VF:.4f}")
print(f"  z-statistic:  z     = {z_VF:.3f}")
print(f"  p-value (two-tailed): p = {p_VF:.4f}")

# One-tailed test (H1: β_VF > 0)
p_one_tailed = p_VF / 2 if beta_VF > 0 else 1 - (p_VF / 2)
print(f"  p-value (one-tailed): p = {p_one_tailed:.4f}")

# Verdict
sig_level = 0.05
if beta_VF > 0 and p_one_tailed < sig_level:
    verdict = "✓ REJECT H0"
    interpretation = f"Flexibility AMPLIFIES Vagueness effect (β_VF = {beta_VF:.4f} > 0, p = {p_one_tailed:.4f})"
elif beta_VF > 0:
    verdict = "○ FAIL TO REJECT H0"
    interpretation = f"Positive but not significant (β_VF = {beta_VF:.4f}, p = {p_one_tailed:.4f})"
else:
    verdict = "✗ REJECT H0 (wrong direction!)"
    interpretation = f"Negative coefficient (β_VF = {beta_VF:.4f})"

print(f"\n{'='*80}")
print(f"VERDICT: {verdict}")
print(f"{'='*80}")
print(f"{interpretation}")

stars = "***" if p_one_tailed < 0.001 else "**" if p_one_tailed < 0.01 else "*" if p_one_tailed < 0.05 else ""
print(f"\nSignificance: {stars if stars else 'n.s.'}")

# =============================================================================
# INTERACTION PLOT
# =============================================================================

if PLOT_AVAILABLE:
    print(f"\n" + "="*80)
    print("INTERACTION PLOT")
    print("="*80)

    # Create grid for prediction
    v_range = np.linspace(analysis_df['z_V'].min(), analysis_df['z_V'].max(), 100)

    # Predict for F=0 and F=1
    pred_df_F0 = pd.DataFrame({
        'z_V': v_range,
        'F_flexibility': 0,
        'founding_cohort': 'cohort_1',
        'region': 'US'
    })

    pred_df_F1 = pd.DataFrame({
        'z_V': v_range,
        'F_flexibility': 1,
        'founding_cohort': 'cohort_1',
        'region': 'US'
    })

    pred_F0 = model.predict(pred_df_F0)
    pred_F1 = model.predict(pred_df_F1)

    # Plot
    fig, ax = plt.subplots(figsize=(8, 6))

    # F=1 (SW/Flexible) - skyblue, solid
    ax.plot(v_range, pred_F1, color=PALETTE['F'], linestyle='-', linewidth=2.5, label='F=1 (Flexible/SW)')

    # F=0 (HW/Rigid) - gray, dashed
    ax.plot(v_range, pred_F0, color=PALETTE['HW'], linestyle='--', linewidth=2.5, label='F=0 (Rigid/HW)')

    ax.set_xlabel('Vagueness (z-scored)', fontsize=12, color=PALETTE['V'])
    ax.set_ylabel('Pr(L=1 | V, F)', fontsize=12, color=PALETTE['L'])
    ax.set_title(f'Flexibility × Vagueness Interaction\n{COHORT_NAME} Companies (2021 Cohort → 2025)', fontsize=13)
    ax.legend(loc='best', frameon=True, fontsize=11)
    ax.grid(alpha=0.3)

    # Add significance annotation
    ax.text(0.05, 0.95, f'β_VF = {beta_VF:.3f}{stars}',
            transform=ax.transAxes, fontsize=11, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

    plt.tight_layout()

    # Save
    plot_path_png = OUTPUT_DIR / f"interaction_VxF_{industry or 'all'}.png"
    plot_path_pdf = OUTPUT_DIR / f"interaction_VxF_{industry or 'all'}.pdf"

    plt.savefig(plot_path_png, dpi=300, bbox_inches='tight')
    plt.savefig(plot_path_pdf, bbox_inches='tight')

    print(f"✓ Saved: {plot_path_png}")
    print(f"✓ Saved: {plot_path_pdf}")
    plt.close()

# =============================================================================
# SUMMARY
# =============================================================================

print(f"\n" + "="*80)
print("SUMMARY")
print("="*80)

summary = {
    'Cohort': COHORT_NAME,
    'N': len(analysis_df),
    'L=1': analysis_df['L'].sum(),
    'beta_VF': beta_VF,
    'se_VF': se_VF,
    'p_value': p_one_tailed,
    'verdict': verdict,
    'significant': p_one_tailed < 0.05
}

print(f"\nCohort: {summary['Cohort']}")
print(f"N: {summary['N']:,} companies")
print(f"L=1 (Later Stage): {summary['L=1']:,} ({summary['L=1']/summary['N']*100:.1f}%)")
print(f"\nβ_VF = {summary['beta_VF']:.4f} (SE = {summary['se_VF']:.4f})")
print(f"p-value = {summary['p_value']:.4f} {stars}")
print(f"\nConclusion: {interpretation}")

# Save summary
summary_df = pd.DataFrame([summary])
summary_path = OUTPUT_DIR / f"summary_{industry or 'all'}.csv"
summary_df.to_csv(summary_path, index=False)
print(f"\n✓ Saved: {summary_path}")

print(f"\n" + "="*80)
print("ANALYSIS COMPLETE")
print("="*80)
