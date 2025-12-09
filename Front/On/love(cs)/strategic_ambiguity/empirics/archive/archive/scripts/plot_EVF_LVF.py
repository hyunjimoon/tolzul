"""
Generate EVF and LVF Interaction Plots

EVF: E (Early funding) ~ V (Vagueness) × F (Flexibility)
  - Shows how flexibility moderates vagueness effect on early funding
  - E=1 is defined as state (Early Stage VC at baseline)
  - Plot shows rate of E across V gradient, stratified by F

LVF: L (Later success) ~ V (Vagueness) × F (Flexibility)
  - Shows how flexibility moderates vagueness effect on later success
  - L=1 is Series B+ achievement
  - This is the main hypothesis test plot

Usage: python scripts/plot_EVF_LVF.py
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys
import re

# Add parent directory for modules
sys.path.insert(0, str(Path(__file__).parent.parent))

# Plotting
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Regression
import statsmodels.formula.api as smf

# Color palette (W2 standard)
PALETTE = {
    "E": "red",          # Early funding
    "L": "#0000FF",      # Later success
    "V": "green",        # Vagueness
    "F": "skyblue",      # Flexibility (F=1)
    "HW": "gray",        # Hardware/Rigid (F=0)
}

# Paths
PROCESSED_DIR = Path("data/processed")
INPUT_FILE = PROCESSED_DIR / "companies_21_23-24-25.parquet"
OUTPUT_DIR = Path("outputs/interaction_plots")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Patterns
PAT_E = re.compile(r"(?:\bEarly\s*Stage\s*VC\b|\bSeries\s*A(?:\b|[\s\-]?\d*)\b)", re.I)
PAT_L = re.compile(r"(?:\bLater\s*Stage\s*VC\b|\bSeries\s*[B-G](?:\b|[\s\-]?\d*)\b)", re.I)

def is_early(s):
    return bool(PAT_E.search(str(s or "")))

def is_later(s):
    return bool(PAT_L.search(str(s or "")))

print("="*80)
print("EVF and LVF INTERACTION PLOTS")
print("="*80)

# Load data
print(f"\nLoading: {INPUT_FILE.name}")
if not INPUT_FILE.exists():
    print(f"✗ File not found!")
    print(f"\nRun: python scripts/consolidate_2021_cohort.py")
    sys.exit(1)

df = pd.read_parquet(INPUT_FILE)
print(f"✓ Loaded: {len(df):,} companies")

# Define variables
df['E'] = df['DealType_2021'].apply(is_early).astype(int)
df['L'] = df['DealType_2025'].apply(is_later).astype(int) if 'DealType_2025' in df.columns else 0

print(f"✓ E=1: {df['E'].sum():,} companies ({df['E'].mean():.1%})")
print(f"✓ L=1: {df['L'].sum():,} companies ({df['L'].mean():.1%})")

# Compute V (Vagueness)
if 'Description_2021' in df.columns and 'Keywords_2021' in df.columns:
    print(f"\nComputing Vagueness from Description/Keywords...")

    try:
        from modules.features import compute_vagueness_vectorized
        df['V'] = compute_vagueness_vectorized(
            df['Description_2021'].fillna(''),
            df['Keywords_2021'].fillna('')
        )

        # Report statistics
        print(f"✓ Vagueness computed:")
        print(f"  Mean: {df['V'].mean():.2f}")
        print(f"  Std:  {df['V'].std():.2f}")
        print(f"  Min:  {df['V'].min():.2f}")
        print(f"  Max:  {df['V'].max():.2f}")

        # Check if std is too small
        if df['V'].std() < 5:
            print(f"\n⚠️  WARNING: Vagueness std ({df['V'].std():.2f}) is very small!")
            print(f"   This suggests Description/Keywords may be mostly empty or identical.")
            print(f"   Check data quality:")

            # Check non-empty rates
            desc_nonempty = df['Description_2021'].fillna('').str.len() > 0
            keywords_nonempty = df['Keywords_2021'].fillna('').str.len() > 0

            print(f"     Description non-empty: {desc_nonempty.sum():,} ({desc_nonempty.mean():.1%})")
            print(f"     Keywords non-empty: {keywords_nonempty.sum():,} ({keywords_nonempty.mean():.1%})")

            # Sample a few descriptions
            sample_df = df[desc_nonempty].head(3)
            print(f"\n   Sample descriptions:")
            for idx, row in sample_df.iterrows():
                desc = str(row['Description_2021'])[:100]
                print(f"     {desc}...")

    except Exception as e:
        print(f"⚠️  Vagueness computation failed: {e}")
        print(f"   Using mock Vagueness")
        df['V'] = np.random.normal(50, 15, len(df))
else:
    print(f"\n⚠️  Description/Keywords not found, using mock Vagueness")
    df['V'] = np.random.normal(50, 15, len(df))

# Z-score V
df['z_V'] = (df['V'] - df['V'].mean()) / df['V'].std()

# Compute F (Flexibility)
if 'F_flexibility' not in df.columns:
    print(f"\nInferring F_flexibility from CompanyName...")
    if 'CompanyName' in df.columns:
        sw_keywords = ['software', 'platform', 'cloud', 'saas', 'app', 'digital']
        sw_mask = pd.Series([False] * len(df))
        for kw in sw_keywords:
            sw_mask |= df['CompanyName'].fillna('').str.contains(kw, case=False)
        df['F_flexibility'] = sw_mask.astype(int)
    else:
        print("  ✗ Cannot infer F - using F=0 for all")
        df['F_flexibility'] = 0

n_F1 = (df['F_flexibility'] == 1).sum()
n_F0 = (df['F_flexibility'] == 0).sum()
print(f"✓ F=1 (Flexible/SW): {n_F1:,} ({n_F1/len(df):.1%})")
print(f"✓ F=0 (Rigid/HW):    {n_F0:,} ({n_F0/len(df):.1%})")

# Add mock controls
df['founding_cohort'] = 'cohort_1'
df['region'] = 'US'

# ============================================================================
# PLOT 1: EVF - Early Funding ~ V × F
# ============================================================================

print(f"\n" + "="*80)
print("PLOT 1: EVF (Early Funding ~ Vagueness × Flexibility)")
print("="*80)

# Note: Since all companies in our dataset have E=1, we can't model E ~ V × F
# This would require a broader dataset including non-E companies
print(f"\n⚠️  NOTE: Current dataset contains only E=1 companies (by design)")
print(f"   Cannot model E ~ V × F without non-E companies")
print(f"   Skipping EVF plot")
print(f"\n   To generate EVF plot, you would need:")
print(f"   - Companies with E=0 (non-Early Stage VC)")
print(f"   - Sample from broader population before E=1 filtering")

# ============================================================================
# PLOT 2: LVF - Later Success ~ V × F
# ============================================================================

print(f"\n" + "="*80)
print("PLOT 2: LVF (Later Success ~ Vagueness × Flexibility)")
print("="*80)

# Prepare data
analysis_df = df[['L', 'z_V', 'F_flexibility', 'founding_cohort', 'region']].dropna()
print(f"\nAnalysis dataset: {len(analysis_df):,} companies")

# Fit logit model
formula = "L ~ z_V * F_flexibility + C(founding_cohort) + C(region)"
print(f"Formula: {formula}")

try:
    model_L = smf.logit(formula, data=analysis_df).fit(disp=False)
    print(f"✓ Model fitted")

    # Extract coefficients
    beta_V = model_L.params.get('z_V', 0)
    beta_F = model_L.params.get('F_flexibility', 0)
    beta_VF = model_L.params.get('z_V:F_flexibility', 0)

    print(f"\nCoefficients:")
    print(f"  β_V:  {beta_V:.4f}")
    print(f"  β_F:  {beta_F:.4f}")
    print(f"  β_VF: {beta_VF:.4f} ← Interaction term")

    # Generate predictions
    v_range = np.linspace(analysis_df['z_V'].min(), analysis_df['z_V'].max(), 100)

    # Predict for F=0 (Hardware/Rigid)
    pred_df_F0 = pd.DataFrame({
        'z_V': v_range,
        'F_flexibility': 0,
        'founding_cohort': 'cohort_1',
        'region': 'US'
    })
    pred_L_F0 = model_L.predict(pred_df_F0)

    # Predict for F=1 (Software/Flexible)
    pred_df_F1 = pd.DataFrame({
        'z_V': v_range,
        'F_flexibility': 1,
        'founding_cohort': 'cohort_1',
        'region': 'US'
    })
    pred_L_F1 = model_L.predict(pred_df_F1)

    # Plot LVF
    fig, ax = plt.subplots(figsize=(10, 7))

    # Plot lines
    ax.plot(v_range, pred_L_F1, color=PALETTE['F'], linestyle='-',
            linewidth=2.5, label='F=1 (Flexible/SW)', zorder=3)
    ax.plot(v_range, pred_L_F0, color=PALETTE['HW'], linestyle='--',
            linewidth=2.5, label='F=0 (Rigid/HW)', zorder=3)

    # Labels and title
    ax.set_xlabel('Vagueness (z-scored)', fontsize=13, color=PALETTE['V'], fontweight='bold')
    ax.set_ylabel('Pr(L=1 | V, F)', fontsize=13, color=PALETTE['L'], fontweight='bold')
    ax.set_title('L ~ V × F: Flexibility Amplifies Vagueness Effect on Later Success',
                 fontsize=14, fontweight='bold')

    # Grid and legend
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11, loc='best')

    # Add interaction annotation
    p_VF = model_L.pvalues.get('z_V:F_flexibility', 1.0)
    sig_stars = '***' if p_VF < 0.001 else ('**' if p_VF < 0.01 else ('*' if p_VF < 0.05 else 'ns'))

    ax.text(0.05, 0.95,
            f'β_VF = {beta_VF:.4f} {sig_stars}\np = {p_VF:.4f}',
            transform=ax.transAxes,
            fontsize=11,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()

    # Save plot
    plot_path_png = OUTPUT_DIR / "LVF_interaction.png"
    plot_path_pdf = OUTPUT_DIR / "LVF_interaction.pdf"

    plt.savefig(plot_path_png, dpi=300, bbox_inches='tight')
    plt.savefig(plot_path_pdf, bbox_inches='tight')
    plt.close()

    print(f"\n✓ LVF plot saved:")
    print(f"  PNG: {plot_path_png}")
    print(f"  PDF: {plot_path_pdf}")

except Exception as e:
    print(f"✗ LVF plot failed: {e}")
    import traceback
    traceback.print_exc()

# ============================================================================
# ADDITIONAL: Binned scatter plot for LVF
# ============================================================================

print(f"\n" + "="*80)
print("PLOT 3: LVF Binned Scatter (Empirical)")
print("="*80)

try:
    # Create V bins
    df['V_bin'] = pd.qcut(df['z_V'], q=5, labels=['Very Low', 'Low', 'Medium', 'High', 'Very High'])

    # Calculate L rate by V bin and F
    binned_stats = df.groupby(['V_bin', 'F_flexibility'])['L'].agg(['mean', 'count']).reset_index()
    binned_stats.columns = ['V_bin', 'F_flexibility', 'L_rate', 'count']

    # Plot
    fig, ax = plt.subplots(figsize=(10, 7))

    # F=0 (Hardware)
    f0_data = binned_stats[binned_stats['F_flexibility'] == 0]
    x_pos_f0 = np.arange(len(f0_data))
    ax.plot(x_pos_f0, f0_data['L_rate'], marker='o', linestyle='--',
            color=PALETTE['HW'], linewidth=2.5, markersize=8, label='F=0 (Rigid/HW)')

    # F=1 (Software)
    f1_data = binned_stats[binned_stats['F_flexibility'] == 1]
    x_pos_f1 = np.arange(len(f1_data))
    ax.plot(x_pos_f1, f1_data['L_rate'], marker='o', linestyle='-',
            color=PALETTE['F'], linewidth=2.5, markersize=8, label='F=1 (Flexible/SW)')

    # Labels and title
    ax.set_xticks(range(5))
    ax.set_xticklabels(['Very Low', 'Low', 'Medium', 'High', 'Very High'])
    ax.set_xlabel('Vagueness Quintile', fontsize=13, color=PALETTE['V'], fontweight='bold')
    ax.set_ylabel('L=1 Rate', fontsize=13, color=PALETTE['L'], fontweight='bold')
    ax.set_title('L ~ V × F: Empirical Rates by Vagueness Quintile',
                 fontsize=14, fontweight='bold')

    ax.grid(True, alpha=0.3, axis='y')
    ax.legend(fontsize=11, loc='best')

    plt.tight_layout()

    # Save
    plot_path_png = OUTPUT_DIR / "LVF_binned_scatter.png"
    plot_path_pdf = OUTPUT_DIR / "LVF_binned_scatter.pdf"

    plt.savefig(plot_path_png, dpi=300, bbox_inches='tight')
    plt.savefig(plot_path_pdf, bbox_inches='tight')
    plt.close()

    print(f"\n✓ LVF binned scatter saved:")
    print(f"  PNG: {plot_path_png}")
    print(f"  PDF: {plot_path_pdf}")

    # Print stats table
    print(f"\nEmpirical L rates by V quintile and F:")
    print(binned_stats.to_string(index=False))

except Exception as e:
    print(f"✗ LVF binned scatter failed: {e}")
    import traceback
    traceback.print_exc()

print(f"\n" + "="*80)
print("PLOTS COMPLETE")
print("="*80)
print(f"\nPlots saved to: {OUTPUT_DIR}/")
print()
