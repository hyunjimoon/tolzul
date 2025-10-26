"""
Script 04: Run Analysis (SIMPLIFIED FOR H1 TESTING)
Input: data/processed/analysis_panel.csv
Output: results_H1_reversal.csv

H1: Vagueness reversal effect
- Model A: log(amount) ~ vagueness  [expect β₁ < 0]
- Model B: funded ~ vagueness       [expect β₁+β₃ > 0]
- Reversal = β₃ > 0
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from pathlib import Path

# Setup
BASE_DIR = Path(__file__).parent.parent
PROCESSED_DIR = BASE_DIR / "data" / "processed"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("="*80)
print("H1 REVERSAL TEST: Vagueness effect at A (amount) vs. B (probability)")
print("="*80)

# Load data
df = pd.read_csv(PROCESSED_DIR / "analysis_panel.csv")

# Prepare variables
df['log_amount'] = np.log(df['deal_size'] + 1)
df['funded'] = (df['deal_size'] > 0).astype(int)
df['vagueness_scaled'] = df['vagueness'] / 100

# Split by round (column is 'round', values are 'Series A' and 'Series B')
df_A = df[df['round'] == 'Series A'].copy()
df_B = df[df['round'] == 'Series B'].copy()

print(f"\nSample: {len(df_A)} Series A, {len(df_B)} Series B")

# ========== MODEL A: Series A Amount ==========
print("\n" + "-"*80)
print("MODEL A: Series A Funding Amount")
print("-"*80)

model_A = smf.ols('log_amount ~ vagueness_scaled + employees', data=df_A).fit()

print(f"\nβ₁ (Vagueness effect): {model_A.params['vagueness_scaled']:.4f}")
print(f"    p-value: {model_A.pvalues['vagueness_scaled']:.4f}")
print(f"    95% CI: [{model_A.conf_int().loc['vagueness_scaled', 0]:.4f}, "
      f"{model_A.conf_int().loc['vagueness_scaled', 1]:.4f}]")

# ========== MODEL B: Series B Probability ==========
print("\n" + "-"*80)
print("MODEL B: Series B Funding Probability")
print("-"*80)

model_B = smf.logit('funded ~ vagueness_scaled + employees', data=df_B).fit(disp=False)

print(f"\nβ₁+β₃ (Vagueness effect): {model_B.params['vagueness_scaled']:.4f}")
print(f"    p-value: {model_B.pvalues['vagueness_scaled']:.4f}")
print(f"    95% CI: [{model_B.conf_int().loc['vagueness_scaled', 0]:.4f}, "
      f"{model_B.conf_int().loc['vagueness_scaled', 1]:.4f}]")

# ========== REVERSAL TEST ==========
print("\n" + "="*80)
print("REVERSAL TEST")
print("="*80)

beta1 = model_A.params['vagueness_scaled']
beta1_plus_beta3 = model_B.params['vagueness_scaled']

print(f"\nβ₁ (A effect):      {beta1:.4f}")
print(f"β₁+β₃ (B effect):   {beta1_plus_beta3:.4f}")
print(f"Implied β₃:        {beta1_plus_beta3 - beta1:.4f}")

reversal = (beta1 < 0) and (beta1_plus_beta3 > 0)
print(f"\n{'✓' if reversal else '✗'} Reversal detected: {reversal}")
print(f"   Vagueness hurts at A ({beta1:.3f}), helps at B ({beta1_plus_beta3:.3f})")

# Save results
results = pd.DataFrame({
    'Model': ['A: Amount', 'B: Probability'],
    'Coefficient': [beta1, beta1_plus_beta3],
    'p-value': [model_A.pvalues['vagueness_scaled'], model_B.pvalues['vagueness_scaled']],
    'N': [len(df_A), len(df_B)]
})

output_file = OUTPUT_DIR / "results_H1_reversal.csv"
results.to_csv(output_file, index=False)
print(f"\n✓ Results saved: {output_file}")


def run_analysis(panel_df):
    """
    Run H1 reversal test
    
    Returns:
        dict: {'model_A': OLS results, 'model_B': Logit results}
    """
    # Prepare
    df = panel_df.copy()
    df['log_amount'] = np.log(df['deal_size'] + 1)
    df['funded'] = (df['deal_size'] > 0).astype(int)
    df['vagueness_scaled'] = df['vagueness'] / 100

    # Split by round (column is 'round', values are 'Series A' and 'Series B')
    df_A = df[df['round'] == 'Series A']
    df_B = df[df['round'] == 'Series B']
    
    # Models
    model_A = smf.ols('log_amount ~ vagueness_scaled + employees', data=df_A).fit()
    model_B = smf.logit('funded ~ vagueness_scaled + employees', data=df_B).fit(disp=False)
    
    return {'model_A': model_A, 'model_B': model_B}


if __name__ == "__main__":
    run_analysis(df)