"""
Script 05: Create Deliverables
Input: data/processed/analysis_panel.csv
Output: 4 tables + 4 figures in output/

Deliverables:
- Table 1: Descriptive statistics
- Table 3: Success rates by sector
- Figure 1: Bar chart (reversal pattern)
- Figure 2: Success curves by vagueness
- Figure 3: Four-line plot (vagueness × round × integration cost)
- Figure 4: Magnitude bars (differential effects)
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for headless environments
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Setup paths
BASE_DIR = Path(__file__).parent.parent
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

print("=" * 80)
print("SCRIPT 05: CREATE DELIVERABLES")
print("=" * 80)

# Read analysis panel
print("\n[Step 1] Reading analysis panel...")
panel_file = PROCESSED_DATA_DIR / "analysis_panel.csv"
df = pd.read_csv(panel_file)
print(f"  Total observations: {len(df)}")

# ============================================================================
# TABLE 1: DESCRIPTIVE STATISTICS
# ============================================================================
print("\n[Step 2] Creating Table 1: Descriptive Statistics...")

desc_vars = ['vagueness', 'high_integration_cost', 'funding_success',
             'deal_size', 'employees', 'total_raised']

desc_stats = df[desc_vars].describe().T
desc_stats['median'] = df[desc_vars].median()
desc_stats = desc_stats[['count', 'mean', 'median', 'std', 'min', 'max']]

table1_file = OUTPUT_DIR / "table1_descriptives.csv"
desc_stats.to_csv(table1_file)
print(f"  ✓ Saved: {table1_file}")
print("\n", desc_stats)

# ============================================================================
# TABLE 3: SUCCESS RATES BY SECTOR
# ============================================================================
print("\n[Step 3] Creating Table 3: Success Rates by Sector...")

# Calculate success rates by vagueness category, round, and integration cost
success_rates = df.groupby(['vagueness_category', 'round', 'integration_cost_label']).agg({
    'funding_success': ['count', 'sum', 'mean']
}).round(3)

success_rates.columns = ['N', 'Successes', 'Success_Rate']
success_rates = success_rates.reset_index()

# Pivot for better readability
success_pivot = success_rates.pivot_table(
    index=['integration_cost_label', 'vagueness_category'],
    columns='round',
    values='Success_Rate'
)

table3_file = OUTPUT_DIR / "table3_success_rates.csv"
success_pivot.to_csv(table3_file)
print(f"  ✓ Saved: {table3_file}")
print("\n", success_pivot)

# ============================================================================
# FIGURE 1: BAR CHART (REVERSAL PATTERN)
# ============================================================================
print("\n[Step 4] Creating Figure 1: Reversal Pattern (Bar Chart)...")

fig, ax = plt.subplots(figsize=(12, 7))

# Calculate success rates for precise vs vague at A and B
success_by_vague_round = df.groupby(['vagueness_category', 'round'])['funding_success'].mean().unstack()

x = np.arange(len(success_by_vague_round.index))
width = 0.35

bars1 = ax.bar(x - width/2, success_by_vague_round['Series A'], width,
               label='Series A', color='steelblue', alpha=0.8)
bars2 = ax.bar(x + width/2, success_by_vague_round['Series B'], width,
               label='Series B', color='coral', alpha=0.8)

ax.set_xlabel('Promise Type', fontsize=13, fontweight='bold')
ax.set_ylabel('Funding Success Rate', fontsize=13, fontweight='bold')
ax.set_title('Funding Success Reversal: Precise vs. Vague Promises\n(Series A → Series B)',
             fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(success_by_vague_round.index)
ax.legend(fontsize=11)
ax.set_ylim(0, 1.1)
ax.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1%}',
                ha='center', va='bottom', fontsize=10)

plt.tight_layout()
fig1_file = OUTPUT_DIR / "figure1_reversal_bars.png"
plt.savefig(fig1_file, dpi=300, bbox_inches='tight')
plt.close()
print(f"  ✓ Saved: {fig1_file}")

# ============================================================================
# FIGURE 2: SUCCESS CURVES BY VAGUENESS
# ============================================================================
print("\n[Step 5] Creating Figure 2: Success Curves by Vagueness...")

fig, ax = plt.subplots(figsize=(12, 7))

# Group by vagueness bins and round
df['vagueness_bin'] = pd.cut(df['vagueness'], bins=[0, 30, 50, 70, 100],
                               labels=['0-30', '30-50', '50-70', '70-100'])

vague_curves = df.groupby(['vagueness_bin', 'round'])['funding_success'].mean().unstack()

for col in vague_curves.columns:
    ax.plot(range(len(vague_curves.index)), vague_curves[col],
            marker='o', linewidth=2.5, markersize=8,
            label=col, alpha=0.8)

ax.set_xlabel('Vagueness Level', fontsize=13, fontweight='bold')
ax.set_ylabel('Funding Success Rate', fontsize=13, fontweight='bold')
ax.set_title('How Vagueness Affects Funding Success Across Rounds',
             fontsize=14, fontweight='bold')
ax.set_xticks(range(len(vague_curves.index)))
ax.set_xticklabels(vague_curves.index)
ax.legend(fontsize=11, title='Round')
ax.grid(alpha=0.3)
ax.set_ylim(0, 1.1)

plt.tight_layout()
fig2_file = OUTPUT_DIR / "figure2_vagueness_curves.png"
plt.savefig(fig2_file, dpi=300, bbox_inches='tight')
plt.close()
print(f"  ✓ Saved: {fig2_file}")

# ============================================================================
# FIGURE 3: FOUR-LINE PLOT (THREE-WAY INTERACTION)
# ============================================================================
print("\n[Step 6] Creating Figure 3: Four-Line Plot (Three-way Interaction)...")

fig, ax = plt.subplots(figsize=(12, 7))

# Calculate success rates by integration cost, vagueness category, and round
four_way = df.groupby(['integration_cost_label', 'vagueness_category', 'round'])['funding_success'].mean()
four_way = four_way.reset_index()

# Create 4 lines: High-i Precise, High-i Vague, Low-i Precise, Low-i Vague
colors = {'High-i (Hardware)': ['#d62728', '#ff7f0e'],  # Red, Orange
          'Low-i (API/SaaS)': ['#1f77b4', '#2ca02c']}   # Blue, Green
markers = {'Precise': 'o', 'Vague': 's'}
linestyles = {'Precise': '-', 'Vague': '--'}

for int_cost in four_way['integration_cost_label'].unique():
    for i, vague_cat in enumerate(['Precise', 'Vague']):
        data = four_way[
            (four_way['integration_cost_label'] == int_cost) &
            (four_way['vagueness_category'] == vague_cat)
        ]

        if len(data) > 0:
            x_vals = [0 if r == 'Series A' else 1 for r in data['round']]
            y_vals = data['funding_success'].values

            label = f"{int_cost}, {vague_cat}"
            color = colors[int_cost][i]
            marker = markers[vague_cat]
            linestyle = linestyles[vague_cat]

            ax.plot(x_vals, y_vals, marker=marker, linewidth=2.5,
                    markersize=10, label=label, color=color,
                    linestyle=linestyle, alpha=0.85)

ax.set_xlabel('Funding Round', fontsize=13, fontweight='bold')
ax.set_ylabel('Funding Success Rate', fontsize=13, fontweight='bold')
ax.set_title('Three-Way Interaction: Vagueness × Round × Integration Cost',
             fontsize=14, fontweight='bold')
ax.set_xticks([0, 1])
ax.set_xticklabels(['Series A', 'Series B'])
ax.legend(fontsize=10, loc='best', framealpha=0.9)
ax.grid(alpha=0.3)
ax.set_ylim(0, 1.15)

plt.tight_layout()
fig3_file = OUTPUT_DIR / "figure3_four_lines.png"
plt.savefig(fig3_file, dpi=300, bbox_inches='tight')
plt.close()
print(f"  ✓ Saved: {fig3_file}")

# ============================================================================
# FIGURE 4: MAGNITUDE BARS (DIFFERENTIAL EFFECTS)
# ============================================================================
print("\n[Step 7] Creating Figure 4: Magnitude Bars...")

fig, ax = plt.subplots(figsize=(12, 7))

# Calculate change from A to B for each group
changes = []
for int_cost in df['integration_cost_label'].unique():
    for vague_cat in ['Precise', 'Vague']:
        subset = df[
            (df['integration_cost_label'] == int_cost) &
            (df['vagueness_category'] == vague_cat)
        ]

        if len(subset) > 0:
            a_rate = subset[subset['round'] == 'Series A']['funding_success'].mean()
            b_rate = subset[subset['round'] == 'Series B']['funding_success'].mean()
            change = (b_rate - a_rate) * 100  # Percentage points

            changes.append({
                'Group': f"{int_cost}\n{vague_cat}",
                'Change': change,
                'IntCost': int_cost,
                'Vagueness': vague_cat
            })

changes_df = pd.DataFrame(changes)

# Create bar chart
x_pos = range(len(changes_df))
colors_map = {
    ('High-i (Hardware)', 'Precise'): '#d62728',
    ('High-i (Hardware)', 'Vague'): '#ff7f0e',
    ('Low-i (API/SaaS)', 'Precise'): '#1f77b4',
    ('Low-i (API/SaaS)', 'Vague'): '#2ca02c'
}

bar_colors = [colors_map[(row['IntCost'], row['Vagueness'])]
              for _, row in changes_df.iterrows()]

bars = ax.bar(x_pos, changes_df['Change'], color=bar_colors, alpha=0.8, edgecolor='black')

ax.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
ax.set_xlabel('Group (Integration Cost & Promise Type)', fontsize=13, fontweight='bold')
ax.set_ylabel('Change in Success Rate (pp)\n(Series B - Series A)', fontsize=13, fontweight='bold')
ax.set_title('Differential Effects: How Success Changes from Series A to B',
             fontsize=14, fontweight='bold')
ax.set_xticks(x_pos)
ax.set_xticklabels(changes_df['Group'], fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Add value labels
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:+.1f}pp',
            ha='center', va='bottom' if height > 0 else 'top',
            fontsize=10, fontweight='bold')

plt.tight_layout()
fig4_file = OUTPUT_DIR / "figure4_magnitude_bars.png"
plt.savefig(fig4_file, dpi=300, bbox_inches='tight')
plt.close()
print(f"  ✓ Saved: {fig4_file}")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 80)
print("DELIVERABLES SUMMARY")
print("=" * 80)
print("\nTables created:")
print("  1. table1_descriptives.csv")
print("  2. table2_model1.csv (from script 04)")
print("  3. table3_success_rates.csv")
print("  4. table4_model2.csv (from script 04)")
print("\nFigures created:")
print("  1. figure1_reversal_bars.png")
print("  2. figure2_vagueness_curves.png")
print("  3. figure3_four_lines.png")
print("  4. figure4_magnitude_bars.png")

print("\n" + "=" * 80)
print("✓ SCRIPT 05 COMPLETED SUCCESSFULLY")
print("=" * 80)
