# Quick Diagnostic: Check for Perfect Collinearity

import pandas as pd
import numpy as np

# Load the analysis dataset
df = pd.read_csv("outputs/h2_analysis_dataset_17m.csv")

print("="*80)
print("DIAGNOSING SINGULAR MATRIX ISSUE")
print("="*80)

# Check founding_cohort distribution IN THE ANALYSIS SAMPLE
print("\n1. Founding Cohort Distribution (at-risk companies):")
print(df['founding_cohort'].value_counts().sort_index())

# Check survival rate by cohort
print("\n2. Survival Rate by Founding Cohort:")
cohort_survival = df.groupby('founding_cohort')['survival'].agg(['count', 'sum', 'mean'])
cohort_survival['survival_rate'] = cohort_survival['mean'] * 100
print(cohort_survival)

# Check for perfect separation
print("\n3. Check for Perfect Separation:")
for cohort in df['founding_cohort'].unique():
    mask = df['founding_cohort'] == cohort
    surv_rate = df.loc[mask, 'survival'].mean()
    n = mask.sum()
    if surv_rate == 0 or surv_rate == 1:
        print(f"  ⚠️  WARNING: Cohort '{cohort}' has perfect separation (rate={surv_rate:.1%}, n={n})")
    elif n < 100:
        print(f"  ⚠️  WARNING: Cohort '{cohort}' has very few observations (n={n})")

# Check high_integration_cost distribution
print("\n4. Integration Cost Distribution:")
print(df['high_integration_cost'].value_counts())
print(f"Modular (0): {(df['high_integration_cost']==0).sum():,}")
print(f"Integrated (1): {(df['high_integration_cost']==1).sum():,}")

# Check correlation between founding_cohort and high_IC
print("\n5. Integration Cost by Founding Cohort:")
ic_by_cohort = pd.crosstab(df['founding_cohort'], df['high_integration_cost'], normalize='index') * 100
print(ic_by_cohort)

# Check for quasi-complete separation
print("\n6. Vagueness Distribution:")
print(f"z_vagueness: mean={df['z_vagueness'].mean():.2f}, std={df['z_vagueness'].std():.2f}, min={df['z_vagueness'].min():.2f}, max={df['z_vagueness'].max():.2f}")

print("\n7. Check for NA values:")
required_vars = ['survival', 'z_vagueness', 'high_integration_cost', 'z_employees_log', 'founding_cohort']
for var in required_vars:
    n_missing = df[var].isna().sum()
    print(f"  {var}: {n_missing} missing ({n_missing/len(df)*100:.1f}%)")

print("\n" + "="*80)
print("DIAGNOSIS COMPLETE")
print("="*80)
