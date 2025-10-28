# EMERGENCY FIX: Drop empty founding_cohort before regression

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

# Load the dataset
df = pd.read_csv("outputs/h2_analysis_dataset_17m.csv")

print("="*80)
print("EMERGENCY FIX: HANDLING SINGULAR MATRIX")
print("="*80)

# Check founding_cohort distribution
print("\n1. Original founding_cohort distribution:")
print(df['founding_cohort'].value_counts().sort_index())

# Drop rows with empty/problematic cohorts
print("\n2. Filtering out problematic cohorts...")
df_clean = df[df['founding_cohort'].notna()].copy()

# Remove '2022+' if it exists and has 0 or very few observations
if '2022+' in df_clean['founding_cohort'].unique():
    count_2022 = (df_clean['founding_cohort'] == '2022+').sum()
    print(f"   Found '2022+' category with {count_2022} observations")
    if count_2022 < 100:
        print(f"   → Dropping '2022+' (too few observations)")
        df_clean = df_clean[df_clean['founding_cohort'] != '2022+']

# Check for other small categories
print("\n3. Checking for small categories:")
cohort_counts = df_clean['founding_cohort'].value_counts()
for cohort, count in cohort_counts.items():
    if count < 100:
        print(f"   ⚠️  '{cohort}': only {count} observations (may cause issues)")

# Drop missing survival values
df_clean = df_clean[df_clean['survival'].notna()].copy()

print(f"\n4. Final sample size: {len(df_clean):,}")
print(f"   Survival rate: {df_clean['survival'].mean():.2%}")

# Try the regression
print("\n5. Testing regression...")
formula = "survival ~ z_vagueness * high_integration_cost + z_employees_log + C(founding_cohort)"

try:
    print(f"   Formula: {formula}")
    model = smf.logit(formula, data=df_clean).fit(disp=False, maxiter=100)
    print(f"   ✓ SUCCESS! Model converged")

    # Show key results
    print("\n" + "="*80)
    print("KEY RESULTS")
    print("="*80)

    beta1 = model.params.get('z_vagueness', np.nan)
    beta3 = model.params.get('z_vagueness:high_integration_cost', np.nan)
    pval1 = model.pvalues.get('z_vagueness', np.nan)
    pval3 = model.pvalues.get('z_vagueness:high_integration_cost', np.nan)

    print(f"\nβ₁ (Vagueness main effect): {beta1:.4f} (p={pval1:.4f})")
    print(f"β₃ (Interaction): {beta3:.4f} (p={pval3:.4f})")

    if beta1 > 0 and pval1 < 0.05:
        print(f"\n✓ H2 SUPPORTED: Vagueness helps in modular sectors!")
    else:
        print(f"\n~ H2 NOT SUPPORTED")

    # Save results
    coeffs = pd.DataFrame({
        'variable': model.params.index,
        'coefficient': model.params.values,
        'std_err': model.bse.values,
        'z': model.tvalues.values,
        'p_value': model.pvalues.values,
        'ci_lower': model.conf_int()[0].values,
        'ci_upper': model.conf_int()[1].values
    })

    coeffs.to_csv("outputs/h2_EMERGENCY_FIX_results.csv", index=False)
    print(f"\n✓ Saved: outputs/h2_EMERGENCY_FIX_results.csv")

except Exception as e:
    print(f"   ✗ FAILED: {e}")
    print("\n   → Try simplifying further:")
    print("      Option 1: Drop founding_cohort entirely, use continuous year_founded")
    print("      Option 2: Collapse cohorts into 3 groups (old/mid/new)")
    print("      Option 3: Use sklearn LogisticRegression with Ridge (L2)")

print("\n" + "="*80)
