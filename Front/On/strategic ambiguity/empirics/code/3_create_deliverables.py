"""
Create all deliverables for Promise Precision and Venture Funding study
Based on HANDOFF_CHECKLIST.md requirements

Deliverables:
- Table 3: Success Rates (4×2 grid showing reversal)
- Table 4: Regression Results
- Figure 3: THE MONEY PLOT (time-based line plot)
- Figure 4: Bar Chart (reversal magnitudes by integration cost)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11

# Load data
df = pd.read_csv('/home/user/tolzul/Front/On/strategic ambiguity/data_simulation.csv')

print("=" * 80)
print("CREATING DELIVERABLES")
print("=" * 80)

# ============================================================================
# TABLE 3: SUCCESS RATES
# ============================================================================
print("\n" + "=" * 80)
print("TABLE 3: SUCCESS RATES BY VAGUENESS × STAGE × INTEGRATION COST")
print("=" * 80)

# Calculate success rates
success_rates = df.groupby([
    'integration_cost_label',
    'vagueness_category',
    'round'
])['funding_success'].agg(['mean', 'count']).reset_index()

success_rates['success_rate_pct'] = success_rates['mean'] * 100

# Pivot to create the table
table3 = success_rates.pivot_table(
    values='success_rate_pct',
    index=['integration_cost_label', 'vagueness_category'],
    columns='round'
)

# Calculate change
table3['Change (pp)'] = table3['Series B'] - table3['Series A']

# Reorder columns
table3 = table3[['Series A', 'Series B', 'Change (pp)']]

print("\n", table3.round(1))

# Calculate swing magnitudes
print("\n" + "-" * 80)
print("SWING MAGNITUDES")
print("-" * 80)

for integration_label in ['Low-i (API/SaaS)', 'High-i (Hardware)']:
    subset = table3.loc[integration_label]
    precise_change = subset.loc['Precise', 'Change (pp)']
    vague_change = subset.loc['Vague', 'Change (pp)']
    swing = vague_change - precise_change

    print(f"\n{integration_label}:")
    print(f"  Precise change: {precise_change:+.1f}pp")
    print(f"  Vague change: {vague_change:+.1f}pp")
    print(f"  Total swing: {swing:.1f}pp")

# Save Table 3
table3.to_csv('/home/user/tolzul/Front/On/strategic ambiguity/table3_success_rates.csv')
print("\n✓ Table 3 saved to: table3_success_rates.csv")

# ============================================================================
# TABLE 4: REGRESSION RESULTS
# ============================================================================
print("\n" + "=" * 80)
print("TABLE 4: REGRESSION RESULTS")
print("=" * 80)

# Re-run models to get results
formula_m1 = '''funding_success ~ vagueness + series_b_dummy +
                vagueness:series_b_dummy +
                log_series_a_amount + team_size + founder_prior_exit'''

m1 = smf.logit(formula_m1, data=df).fit(
    cov_type='cluster',
    cov_kwds={'groups': df['firm_id']},
    disp=False
)

formula_m2 = '''funding_success ~ vagueness + series_b_dummy + high_integration_cost +
                vagueness:series_b_dummy + vagueness:high_integration_cost +
                series_b_dummy:high_integration_cost +
                vagueness:series_b_dummy:high_integration_cost +
                log_series_a_amount + team_size + founder_prior_exit'''

m2 = smf.logit(formula_m2, data=df).fit(
    cov_type='cluster',
    cov_kwds={'groups': df['firm_id']},
    disp=False
)

# Create regression table
table4 = pd.DataFrame({
    'Variable': m2.params.index,
    'Model 2 Coef': m2.params.values,
    'Model 2 SE': m2.bse.values,
    'Model 2 p-value': m2.pvalues.values
})

# Clean variable names
variable_names = {
    'Intercept': 'Constant',
    'vagueness': 'Vagueness',
    'series_b_dummy': 'Series B',
    'high_integration_cost': 'High Integration Cost',
    'vagueness:series_b_dummy': 'Vagueness × Series B',
    'vagueness:high_integration_cost': 'Vagueness × High-i',
    'series_b_dummy:high_integration_cost': 'Series B × High-i',
    'vagueness:series_b_dummy:high_integration_cost': 'Vagueness × Series B × High-i (β₇)',
    'log_series_a_amount': 'log(Series A Amount)',
    'team_size': 'Team Size',
    'founder_prior_exit': 'Founder Prior Exit'
}

table4['Variable'] = table4['Variable'].map(variable_names)

# Format with stars
def add_stars(row):
    p = row['Model 2 p-value']
    coef_str = f"{row['Model 2 Coef']:.4f}"
    if p < 0.01:
        return coef_str + "***"
    elif p < 0.05:
        return coef_str + "**"
    elif p < 0.1:
        return coef_str + "*"
    else:
        return coef_str

table4['Coefficient'] = table4.apply(add_stars, axis=1)
table4['Std Error'] = table4['Model 2 SE'].apply(lambda x: f"({x:.4f})")

# Create final table
table4_final = table4[['Variable', 'Coefficient', 'Std Error']].copy()

print("\n", table4_final.to_string(index=False))
print("\nSignificance: *** p<0.01, ** p<0.05, * p<0.1")

# Highlight key coefficient
beta7_row = table4_final[table4_final['Variable'].str.contains('β₇')]
print("\n" + "=" * 80)
print("KEY FINDING:")
print("-" * 80)
print(beta7_row.to_string(index=False))
print("=" * 80)

# Save Table 4
table4_final.to_csv('/home/user/tolzul/Front/On/strategic ambiguity/table4_regression.csv', index=False)
print("\n✓ Table 4 saved to: table4_regression.csv")

# ============================================================================
# FIGURE 3: THE MONEY PLOT
# ============================================================================
print("\n" + "=" * 80)
print("FIGURE 3: THE MONEY PLOT (Time-based Line Plot)")
print("=" * 80)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Panel A: Low Integration Cost
low_i = df[df['integration_cost_label'] == 'Low-i (API/SaaS)']

for vague_cat in ['Precise', 'Vague']:
    subset = low_i[low_i['vagueness_category'] == vague_cat]
    rates = subset.groupby('round')['funding_success'].mean() * 100

    # Reorder to ensure Series A comes before Series B
    rates = rates.reindex(['Series A', 'Series B'])

    linestyle = '--' if vague_cat == 'Vague' else '-'
    marker = 'o'
    linewidth = 2.5

    ax1.plot([0, 1], rates.values, marker=marker, linestyle=linestyle,
             linewidth=linewidth, markersize=10, label=vague_cat)

ax1.set_xticks([0, 1])
ax1.set_xticklabels(['Series A', 'Series B'], fontsize=12)
ax1.set_ylabel('Funding Success Rate (%)', fontsize=13, fontweight='bold')
ax1.set_title('Low Integration Cost (API/SaaS)', fontsize=14, fontweight='bold', pad=15)
ax1.legend(loc='best', fontsize=11, frameon=True, shadow=True)
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0, 100)

# Annotate changes
for vague_cat in ['Precise', 'Vague']:
    subset = low_i[low_i['vagueness_category'] == vague_cat]
    rates = subset.groupby('round')['funding_success'].mean() * 100
    rates = rates.reindex(['Series A', 'Series B'])
    change = rates.iloc[1] - rates.iloc[0]

    y_pos = rates.iloc[1]
    ax1.annotate(f'{change:+.0f}pp', xy=(1.05, y_pos), fontsize=10,
                fontweight='bold', color='darkgreen' if change > 0 else 'darkred')

# Panel B: High Integration Cost
high_i = df[df['integration_cost_label'] == 'High-i (Hardware)']

for vague_cat in ['Precise', 'Vague']:
    subset = high_i[high_i['vagueness_category'] == vague_cat]
    rates = subset.groupby('round')['funding_success'].mean() * 100

    # Reorder to ensure Series A comes before Series B
    rates = rates.reindex(['Series A', 'Series B'])

    linestyle = '--' if vague_cat == 'Vague' else '-'
    marker = 'o'
    linewidth = 3 if vague_cat == 'Precise' else 2.5  # Thicker for more dramatic change

    ax2.plot([0, 1], rates.values, marker=marker, linestyle=linestyle,
             linewidth=linewidth, markersize=10, label=vague_cat)

ax2.set_xticks([0, 1])
ax2.set_xticklabels(['Series A', 'Series B'], fontsize=12)
ax2.set_ylabel('Funding Success Rate (%)', fontsize=13, fontweight='bold')
ax2.set_title('High Integration Cost (Hardware)', fontsize=14, fontweight='bold', pad=15)
ax2.legend(loc='best', fontsize=11, frameon=True, shadow=True)
ax2.grid(True, alpha=0.3)
ax2.set_ylim(0, 100)

# Annotate changes with more emphasis
for vague_cat in ['Precise', 'Vague']:
    subset = high_i[high_i['vagueness_category'] == vague_cat]
    rates = subset.groupby('round')['funding_success'].mean() * 100
    rates = rates.reindex(['Series A', 'Series B'])
    change = rates.iloc[1] - rates.iloc[0]

    y_pos = rates.iloc[1]
    color = 'darkgreen' if change > 0 else 'darkred'
    ax2.annotate(f'{change:+.0f}pp', xy=(1.05, y_pos), fontsize=11,
                fontweight='bold', color=color,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=color, linewidth=2))

plt.suptitle('Promise Precision Effect Reversal by Integration Cost',
             fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()

# Save Figure 3
fig3_path = '/home/user/tolzul/Front/On/strategic ambiguity/figure3_money_plot.png'
plt.savefig(fig3_path, dpi=300, bbox_inches='tight')
print(f"\n✓ Figure 3 saved to: {fig3_path}")

# ============================================================================
# FIGURE 4: BAR CHART (Reversal Magnitudes)
# ============================================================================
print("\n" + "=" * 80)
print("FIGURE 4: BAR CHART (Reversal Magnitudes by Integration Cost)")
print("=" * 80)

fig, ax = plt.subplots(figsize=(12, 7))

# Calculate reversal magnitudes
reversal_data = []

for integration_label in ['Low-i (API/SaaS)', 'High-i (Hardware)']:
    subset = table3.loc[integration_label]

    precise_change = subset.loc['Precise', 'Change (pp)']
    vague_change = subset.loc['Vague', 'Change (pp)']

    reversal_data.append({
        'Integration Cost': integration_label,
        'Promise Type': 'Precise',
        'Change (pp)': precise_change
    })

    reversal_data.append({
        'Integration Cost': integration_label,
        'Promise Type': 'Vague',
        'Change (pp)': vague_change
    })

reversal_df = pd.DataFrame(reversal_data)

# Create grouped bar chart
x = np.arange(len(['Low-i (API/SaaS)', 'High-i (Hardware)']))
width = 0.35

precise_changes = reversal_df[reversal_df['Promise Type'] == 'Precise']['Change (pp)'].values
vague_changes = reversal_df[reversal_df['Promise Type'] == 'Vague']['Change (pp)'].values

bars1 = ax.bar(x - width/2, precise_changes, width, label='Precise Promise',
               color='steelblue', edgecolor='black', linewidth=1.5)
bars2 = ax.bar(x + width/2, vague_changes, width, label='Vague Promise',
               color='coral', edgecolor='black', linewidth=1.5)

# Add value labels on bars
def autolabel(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:+.0f}pp',
                ha='center', va='bottom' if height > 0 else 'top',
                fontsize=11, fontweight='bold')

autolabel(bars1)
autolabel(bars2)

# Add horizontal line at y=0
ax.axhline(y=0, color='black', linestyle='-', linewidth=1)

ax.set_xlabel('Integration Cost Category', fontsize=13, fontweight='bold')
ax.set_ylabel('Change in Success Rate (percentage points)', fontsize=13, fontweight='bold')
ax.set_title('Series A → Series B Success Rate Changes', fontsize=15, fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(['Low-i (API/SaaS)', 'High-i (Hardware)'], fontsize=12)
ax.legend(fontsize=12, loc='upper right', frameon=True, shadow=True)
ax.grid(True, alpha=0.3, axis='y')

# Annotate reversal magnitudes
for i, integration_label in enumerate(['Low-i (API/SaaS)', 'High-i (Hardware)']):
    swing = vague_changes[i] - precise_changes[i]
    ax.annotate(f'Swing: {swing:.0f}pp',
                xy=(i, max(precise_changes[i], vague_changes[i]) + 5),
                fontsize=11, fontweight='bold', ha='center',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7))

plt.tight_layout()

# Save Figure 4
fig4_path = '/home/user/tolzul/Front/On/strategic ambiguity/figure4_bar_chart.png'
plt.savefig(fig4_path, dpi=300, bbox_inches='tight')
print(f"\n✓ Figure 4 saved to: {fig4_path}")

print("\n" + "=" * 80)
print("ALL DELIVERABLES CREATED")
print("=" * 80)
print("\nFiles created:")
print("  1. table3_success_rates.csv")
print("  2. table4_regression.csv")
print("  3. figure3_money_plot.png")
print("  4. figure4_bar_chart.png")
print("\n" + "=" * 80)

plt.show()
