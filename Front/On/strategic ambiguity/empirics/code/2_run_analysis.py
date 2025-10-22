"""
Run statistical analysis for Promise Precision and Venture Funding study
Based on HANDOFF_CHECKLIST.md requirements

Models:
1. Base Reversal Effect (H1, H2)
2. Three-way Interaction (H3)
"""

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.iolib.summary2 import summary_col

# Load data
df = pd.read_csv('/home/user/tolzul/Front/On/strategic ambiguity/data_simulation.csv')

print("=" * 80)
print("PROMISE PRECISION AND VENTURE FUNDING - STATISTICAL ANALYSIS")
print("=" * 80)
print(f"\nDataset: {len(df)} observations from {df['firm_id'].nunique()} firms")
print(f"Panel structure: Each firm appears in 2 rounds (Series A and Series B)")

# ============================================================================
# MODEL 1: Base Reversal Effect
# ============================================================================
print("\n" + "=" * 80)
print("MODEL 1: BASE REVERSAL EFFECT")
print("=" * 80)
print("\nHypotheses:")
print("  H1: β₁ > 0 (vagueness HELPS at Series A)")
print("  H2: β₃ < 0 (effect reverses at Series B)")
print()

formula_m1 = '''funding_success ~ vagueness + series_b_dummy +
                vagueness:series_b_dummy +
                log_series_a_amount + team_size + founder_prior_exit'''

# Fit logistic regression with clustered standard errors
m1 = smf.logit(formula_m1, data=df).fit(
    cov_type='cluster',
    cov_kwds={'groups': df['firm_id']},
    disp=False
)

print(m1.summary())

# Test hypotheses
print("\n" + "-" * 80)
print("HYPOTHESIS TESTS - MODEL 1")
print("-" * 80)

beta1 = m1.params['vagueness']
p1 = m1.pvalues['vagueness']
print(f"\nH1 (vagueness helps at Series A): β₁ = {beta1:.4f}, p = {p1:.4f}")
if beta1 > 0 and p1 < 0.05:
    print("  ✓ SUPPORTED: Vagueness has positive effect at Series A (p < 0.05)")
else:
    print("  ✗ NOT SUPPORTED")

beta3 = m1.params['vagueness:series_b_dummy']
p3 = m1.pvalues['vagueness:series_b_dummy']
print(f"\nH2 (effect reverses at Series B): β₃ = {beta3:.4f}, p = {p3:.4f}")
if beta3 < 0 and p3 < 0.05:
    print("  ✓ SUPPORTED: Effect reverses at Series B (p < 0.05)")
else:
    print("  ✗ NOT SUPPORTED")

# ============================================================================
# MODEL 2: Three-way Interaction (Integration Cost Mechanism)
# ============================================================================
print("\n" + "=" * 80)
print("MODEL 2: THREE-WAY INTERACTION (INTEGRATION COST MECHANISM)")
print("=" * 80)
print("\nHypothesis:")
print("  H3: β₇ < 0 (reversal 2-3× stronger in high-integration-cost sectors)")
print()

formula_m2 = '''funding_success ~ vagueness + series_b_dummy + high_integration_cost +
                vagueness:series_b_dummy + vagueness:high_integration_cost +
                series_b_dummy:high_integration_cost +
                vagueness:series_b_dummy:high_integration_cost +
                log_series_a_amount + team_size + founder_prior_exit'''

# Fit logistic regression with clustered standard errors
m2 = smf.logit(formula_m2, data=df).fit(
    cov_type='cluster',
    cov_kwds={'groups': df['firm_id']},
    disp=False
)

print(m2.summary())

# Test hypothesis
print("\n" + "-" * 80)
print("HYPOTHESIS TEST - MODEL 2")
print("-" * 80)

beta7 = m2.params['vagueness:series_b_dummy:high_integration_cost']
p7 = m2.pvalues['vagueness:series_b_dummy:high_integration_cost']
print(f"\nH3 (reversal stronger in high-i): β₇ = {beta7:.4f}, p = {p7:.4f}")
if beta7 < 0 and p7 < 0.01:
    print("  ✓ SUPPORTED: Reversal 2-3× stronger in high-i sectors (p < 0.01)")
elif beta7 < 0 and p7 < 0.05:
    print("  ~ SUPPORTED: Reversal stronger in high-i sectors (p < 0.05)")
else:
    print("  ✗ NOT SUPPORTED")

# ============================================================================
# SIDE-BY-SIDE COMPARISON
# ============================================================================
print("\n" + "=" * 80)
print("SIDE-BY-SIDE MODEL COMPARISON")
print("=" * 80)

comparison = summary_col(
    [m1, m2],
    model_names=['Model 1\n(Base)', 'Model 2\n(Three-way)'],
    stars=True,
    float_format='%.4f',
    info_dict={
        'N': lambda x: f"{int(x.nobs)}",
        'Log-Likelihood': lambda x: f"{x.llf:.2f}",
        'AIC': lambda x: f"{x.aic:.2f}",
        'BIC': lambda x: f"{x.bic:.2f}"
    }
)

print(comparison)

# ============================================================================
# MARGINAL EFFECTS ANALYSIS
# ============================================================================
print("\n" + "=" * 80)
print("MARGINAL EFFECTS OF VAGUENESS BY STAGE AND INTEGRATION COST")
print("=" * 80)

# Calculate predicted probabilities for key scenarios
scenarios = pd.DataFrame({
    'vagueness': [25, 75, 25, 75, 25, 75, 25, 75],
    'series_b_dummy': [0, 0, 1, 1, 0, 0, 1, 1],
    'high_integration_cost': [0, 0, 0, 0, 1, 1, 1, 1],
    'log_series_a_amount': [np.log(df['series_a_amount'].mean())] * 8,
    'team_size': [df['team_size'].mean()] * 8,
    'founder_prior_exit': [df['founder_prior_exit'].mean()] * 8
})

scenarios['predicted_prob'] = m2.predict(scenarios)

print("\nPredicted Probabilities (Model 2):")
print("-" * 80)
print(f"{'Scenario':<40} {'Predicted Prob':<15}")
print("-" * 80)

labels = [
    "Precise, Series A, Low-i",
    "Vague, Series A, Low-i",
    "Precise, Series B, Low-i",
    "Vague, Series B, Low-i",
    "Precise, Series A, High-i",
    "Vague, Series A, High-i",
    "Precise, Series B, High-i",
    "Vague, Series B, High-i"
]

for label, prob in zip(labels, scenarios['predicted_prob']):
    print(f"{label:<40} {prob:.2%}")

# Save model results
print("\n" + "=" * 80)
print("SAVING RESULTS")
print("=" * 80)

# Save coefficient tables
results_df = pd.DataFrame({
    'Variable': m2.params.index,
    'Coefficient': m2.params.values,
    'Std Error': m2.bse.values,
    'z-value': m2.tvalues.values,
    'p-value': m2.pvalues.values,
    'CI Lower': m2.conf_int()[0].values,
    'CI Upper': m2.conf_int()[1].values
})

results_df.to_csv('/home/user/tolzul/Front/On/strategic ambiguity/model2_coefficients.csv', index=False)
print("\n✓ Model 2 coefficients saved to: model2_coefficients.csv")

# Save predicted probabilities
scenarios['scenario'] = labels
scenarios.to_csv('/home/user/tolzul/Front/On/strategic ambiguity/predicted_probabilities.csv', index=False)
print("✓ Predicted probabilities saved to: predicted_probabilities.csv")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
