"""
Generate simulation data for Promise Precision and Venture Funding study
Based on HANDOFF_CHECKLIST.md requirements

Target Numbers to Reproduce:
- Precise hardware: 75% → 28% (-47pp)
- Vague hardware: 52% → 63% (+11pp)
- Total swing: 58pp in high-i vs 17pp in low-i
- Three-way interaction: β₇ ≈ -0.065, p < 0.003
"""

import numpy as np
import pandas as pd
from scipy import stats

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
N_FIRMS = 75  # Total firms
N_LOW_I = 35  # Low integration cost (API/SaaS)
N_HIGH_I = 40  # High integration cost (hardware/chips)

# Firm names
low_i_firms = [f"API_Firm_{i:02d}" for i in range(1, N_LOW_I + 1)]
high_i_firms = [f"Hardware_Firm_{i:02d}" for i in range(1, N_HIGH_I + 1)]
all_firms = low_i_firms + high_i_firms

# Create base firm characteristics
firm_data = []

for i, firm_name in enumerate(all_firms):
    is_high_i = i >= N_LOW_I

    # Generate firm-level characteristics
    firm_info = {
        'firm_id': i,
        'firm_name': firm_name,
        'high_integration_cost': int(is_high_i),

        # Vagueness score (0-100, fixed per firm)
        # Roughly 50/50 split between vague (>50) and precise (<50)
        'vagueness': np.random.uniform(10, 90),

        # Control variables
        'series_a_amount': np.random.uniform(2e6, 15e6),  # $2M-$15M
        'team_size': np.random.randint(5, 50),
        'founder_prior_exit': np.random.binomial(1, 0.3),  # 30% have prior exit
    }

    firm_data.append(firm_info)

df_firms = pd.DataFrame(firm_data)

# Create panel data (each firm appears twice: Series A and Series B)
panel_data = []

for _, firm in df_firms.iterrows():
    # Series A attempt
    row_a = firm.to_dict()
    row_a['series_b_dummy'] = 0
    row_a['round'] = 'Series A'
    panel_data.append(row_a)

    # Series B attempt
    row_b = firm.to_dict()
    row_b['series_b_dummy'] = 1
    row_b['round'] = 'Series B'
    panel_data.append(row_b)

df_panel = pd.DataFrame(panel_data)

# Generate funding success based on the target pattern
# Key insight: We need to match these success rates:
# Low-i (API/SaaS):
#   - Precise at A: ~65%, at B: ~70% (slight improvement, +5pp)
#   - Vague at A: ~55%, at B: ~60% (slight improvement, +5pp)
#   - Reversal magnitude: ~10pp
# High-i (Hardware):
#   - Precise at A: 75%, at B: 28% (-47pp)
#   - Vague at A: 52%, at B: 63% (+11pp)
#   - Reversal magnitude: 58pp

def generate_funding_success(row):
    """Generate funding success with logistic probability

    Target patterns:
    Low-i (API/SaaS):
      - Precise: A=65%, B=70% (+5pp)
      - Vague: A=55%, B=60% (+5pp)
    High-i (Hardware):
      - Precise: A=75%, B=28% (-47pp)
      - Vague: A=52%, B=63% (+11pp)
    """

    vagueness_centered = (row['vagueness'] - 50) / 50  # Center and scale
    is_series_b = row['series_b_dummy']
    is_high_i = row['high_integration_cost']

    # Classify as vague or precise based on vagueness score
    is_vague = row['vagueness'] > 50

    # Control effects (small)
    base_logit = 0.0
    base_logit += 0.1 * np.log(row['series_a_amount'] / 1e6)
    base_logit += 0.01 * row['team_size']
    base_logit += 0.2 * row['founder_prior_exit']

    # Pattern-based approach to match targets
    if is_high_i:
        # High integration cost (Hardware)
        if is_vague:
            # Vague: 52% → 63% (+11pp)
            if is_series_b:
                base_prob = 0.63
            else:
                base_prob = 0.52
        else:
            # Precise: 75% → 28% (-47pp)
            if is_series_b:
                base_prob = 0.28
            else:
                base_prob = 0.75
    else:
        # Low integration cost (API/SaaS)
        if is_vague:
            # Vague: 55% → 60% (+5pp)
            if is_series_b:
                base_prob = 0.60
            else:
                base_prob = 0.55
        else:
            # Precise: 65% → 70% (+5pp)
            if is_series_b:
                base_prob = 0.70
            else:
                base_prob = 0.65

    # Add continuous variation based on exact vagueness score
    # (so it's not purely binary)
    vagueness_adjustment = 0.05 * vagueness_centered * (1 if is_vague else -1)
    base_prob = np.clip(base_prob + vagueness_adjustment, 0.05, 0.95)

    # Add small control effects
    control_effect = base_logit / 10  # Small influence
    base_prob = np.clip(base_prob + control_effect, 0.05, 0.95)

    # Add noise
    prob = np.clip(base_prob + np.random.normal(0, 0.08), 0.01, 0.99)

    # Generate binary outcome
    return np.random.binomial(1, prob)

# Apply to all rows
df_panel['funding_success'] = df_panel.apply(generate_funding_success, axis=1)

# Add log-transformed series A amount
df_panel['log_series_a_amount'] = np.log(df_panel['series_a_amount'])

# Create categorical variables for visualization
df_panel['vagueness_category'] = pd.cut(df_panel['vagueness'],
                                         bins=[0, 50, 100],
                                         labels=['Precise', 'Vague'])

df_panel['integration_cost_label'] = df_panel['high_integration_cost'].map({
    0: 'Low-i (API/SaaS)',
    1: 'High-i (Hardware)'
})

# Save to CSV
output_path = '/home/user/tolzul/Front/On/strategic ambiguity/data_simulation.csv'
df_panel.to_csv(output_path, index=False)

print("=" * 70)
print("SIMULATION DATA GENERATED")
print("=" * 70)
print(f"\nTotal firms: {N_FIRMS}")
print(f"  - Low integration cost (API/SaaS): {N_LOW_I}")
print(f"  - High integration cost (Hardware): {N_HIGH_I}")
print(f"\nPanel observations: {len(df_panel)} (each firm × 2 rounds)")
print(f"\nData saved to: {output_path}")

# Quick validation: Check success rates
print("\n" + "=" * 70)
print("SUCCESS RATES BY CATEGORY")
print("=" * 70)

for integration_label in ['Low-i (API/SaaS)', 'High-i (Hardware)']:
    print(f"\n{integration_label}:")
    subset = df_panel[df_panel['integration_cost_label'] == integration_label]

    for vague_label in ['Precise', 'Vague']:
        subset2 = subset[subset['vagueness_category'] == vague_label]

        # Series A
        series_a = subset2[subset2['series_b_dummy'] == 0]
        success_rate_a = series_a['funding_success'].mean() * 100

        # Series B
        series_b = subset2[subset2['series_b_dummy'] == 1]
        success_rate_b = series_b['funding_success'].mean() * 100

        change = success_rate_b - success_rate_a

        print(f"  {vague_label}:")
        print(f"    Series A: {success_rate_a:.1f}%")
        print(f"    Series B: {success_rate_b:.1f}%")
        print(f"    Change: {change:+.1f}pp")

print("\n" + "=" * 70)
print("DATA PREVIEW")
print("=" * 70)
print(df_panel.head(10))

print("\n" + "=" * 70)
print("DESCRIPTIVE STATISTICS")
print("=" * 70)
print(df_panel[['vagueness', 'series_a_amount', 'team_size',
                'founder_prior_exit', 'funding_success']].describe())
