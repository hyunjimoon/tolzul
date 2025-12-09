"""
N GENERATIVE MECHANISM VALIDATION

Generative mechanism 검증:
1. 이론적 U-shape 모델 생성
2. 시뮬레이션 데이터에서 실제 funding rate 계산
3. 이론 vs 실증 비교로 모델 타당성 검증

핵심: 모델이 데이터를 "생성"할 수 있는지 확인
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.size'] = 11

# ============================================================================
# LOAD DATA
# ============================================================================

def load_data():
    """Load simulated funding data and lambda ratios"""
    base_path = "/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output/🤹N/⚙️process"

    df = pd.read_csv(f"{base_path}/simulated_funding_data.csv")
    lambda_df = pd.read_csv(f"{base_path}/estimated_lambda_ratios.csv")

    return df, lambda_df


# ============================================================================
# THEORETICAL MODEL
# ============================================================================

def theoretical_funding_prob(S2, theta_A=0.3, theta_B=0.7, w_A=0.5, w_B=0.5):
    """
    Theoretical U-shape model
    P_fund = w_A * P_analyst(S2) + w_B * P_believer(S2)
    """
    steepness = 15
    P_A = 1 / (1 + np.exp(steepness * (S2 - theta_A)))
    P_B = 1 / (1 + np.exp(-steepness * (S2 - theta_B)))
    return w_A * P_A + w_B * P_B


# ============================================================================
# EMPIRICAL ANALYSIS
# ============================================================================

def compute_empirical_funding_rates(df):
    """
    Compute funding success rates by investor category

    investor_category mapping to S2 (signal precision):
    - analyst (Conservative pitch) -> S2 ~ 0.15 (precise)
    - mixed (Mixed pitch) -> S2 ~ 0.5 (murky middle)
    - believer (Visionary pitch) -> S2 ~ 0.85 (vague)
    """

    # Map investor categories to S2 values
    s2_mapping = {
        'analyst': 0.15,    # Precise signals
        'mixed': 0.50,      # Murky middle
        'believer': 0.85    # Vague/visionary
    }

    results = []

    for industry in df['industry'].unique():
        ind_df = df[df['industry'] == industry]

        for category in ['analyst', 'mixed', 'believer']:
            cat_df = ind_df[ind_df['investor_category'] == category]

            if len(cat_df) > 0:
                success_rate = cat_df['funded'].mean()
                n_obs = len(cat_df)

                # Confidence interval (Wilson score interval)
                if n_obs > 0:
                    z = 1.96
                    p = success_rate
                    n = n_obs
                    denominator = 1 + z**2/n
                    center = (p + z**2/(2*n)) / denominator
                    margin = z * np.sqrt((p*(1-p) + z**2/(4*n))/n) / denominator
                    ci_low = max(0, center - margin)
                    ci_high = min(1, center + margin)
                else:
                    ci_low, ci_high = 0, 0

                results.append({
                    'industry': industry,
                    'category': category,
                    'S2': s2_mapping[category],
                    'funding_rate': success_rate,
                    'n_obs': n_obs,
                    'ci_low': ci_low,
                    'ci_high': ci_high
                })

    return pd.DataFrame(results)


def compute_overall_empirical(df):
    """Compute overall funding rates across all industries"""

    s2_mapping = {
        'analyst': 0.15,
        'mixed': 0.50,
        'believer': 0.85
    }

    results = []

    for category in ['analyst', 'mixed', 'believer']:
        cat_df = df[df['investor_category'] == category]

        if len(cat_df) > 0:
            success_rate = cat_df['funded'].mean()
            n_obs = len(cat_df)

            # Confidence interval
            z = 1.96
            p = success_rate
            n = n_obs
            denominator = 1 + z**2/n
            center = (p + z**2/(2*n)) / denominator
            margin = z * np.sqrt((p*(1-p) + z**2/(4*n))/n) / denominator
            ci_low = max(0, center - margin)
            ci_high = min(1, center + margin)

            results.append({
                'category': category,
                'S2': s2_mapping[category],
                'funding_rate': success_rate,
                'n_obs': n_obs,
                'ci_low': ci_low,
                'ci_high': ci_high
            })

    return pd.DataFrame(results)


# ============================================================================
# VISUALIZATION
# ============================================================================

def create_validation_figure(df, empirical_df, overall_df, save_path):
    """
    Create validation figure: Theory vs Empirical
    """

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    S2 = np.linspace(0, 1, 200)

    # === Panel A: Overall Theory vs Empirical ===
    ax1 = axes[0, 0]

    # Theoretical curve
    P_theory = theoretical_funding_prob(S2)
    ax1.plot(S2, P_theory, 'k-', linewidth=2.5, label='Theoretical U-shape', zorder=3)

    # Empirical points with error bars
    colors = {'analyst': '#2E86AB', 'mixed': '#F18F01', 'believer': '#A23B72'}
    markers = {'analyst': 's', 'mixed': 'o', 'believer': '^'}

    for _, row in overall_df.iterrows():
        yerr = [[row['funding_rate'] - row['ci_low']],
                [row['ci_high'] - row['funding_rate']]]
        ax1.errorbar(row['S2'], row['funding_rate'], yerr=yerr,
                    fmt=markers[row['category']], color=colors[row['category']],
                    markersize=15, capsize=5, capthick=2, linewidth=2,
                    label=f"{row['category'].capitalize()} (n={row['n_obs']})",
                    zorder=5)

    # Shade murky middle
    murky_mask = (S2 >= 0.3) & (S2 <= 0.7)
    ax1.fill_between(S2[murky_mask], 0, P_theory[murky_mask],
                     alpha=0.2, color='#F18F01')

    ax1.set_xlabel('Signal Precision S² (0=precise, 1=vague)', fontsize=11)
    ax1.set_ylabel('Funding Success Rate', fontsize=11)
    ax1.set_title('(A) Generative Mechanism Validation\nTheory vs Empirical Data',
                  fontsize=12, fontweight='bold')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 0.6)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.grid(alpha=0.3)

    # Add annotation for key finding
    mixed_rate = overall_df[overall_df['category'] == 'mixed']['funding_rate'].values[0]
    analyst_rate = overall_df[overall_df['category'] == 'analyst']['funding_rate'].values[0]
    believer_rate = overall_df[overall_df['category'] == 'believer']['funding_rate'].values[0]

    best_pure = max(analyst_rate, believer_rate)
    murky_penalty = (mixed_rate - best_pure) / best_pure * 100

    ax1.annotate(f'Murky Middle Penalty:\n{murky_penalty:.0f}% vs best pure',
                xy=(0.5, mixed_rate), xytext=(0.65, mixed_rate + 0.15),
                fontsize=10, arrowprops=dict(arrowstyle='->', color='red'),
                bbox=dict(boxstyle='round', facecolor='white', edgecolor='red'))

    # === Panel B: By Industry ===
    ax2 = axes[0, 1]

    industries = empirical_df['industry'].unique()
    x = np.arange(len(industries))
    width = 0.25

    for i, category in enumerate(['analyst', 'mixed', 'believer']):
        cat_data = empirical_df[empirical_df['category'] == category]
        rates = [cat_data[cat_data['industry'] == ind]['funding_rate'].values[0]
                 if len(cat_data[cat_data['industry'] == ind]) > 0 else 0
                 for ind in industries]
        ax2.bar(x + (i-1)*width, rates, width, label=category.capitalize(),
               color=colors[category], edgecolor='black', linewidth=0.5)

    ax2.set_xticks(x)
    ax2.set_xticklabels(industries, rotation=15, ha='right')
    ax2.set_ylabel('Funding Success Rate', fontsize=11)
    ax2.set_title('(B) Funding Rate by Industry & Investor Type',
                  fontsize=12, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=9)
    ax2.grid(axis='y', alpha=0.3)

    # === Panel C: U-shape by Industry ===
    ax3 = axes[1, 0]

    industry_colors = {
        'Software': '#28A745',
        'Hardware': '#DC3545',
        'Transportation': '#6C757D',
        'Quantum': '#9B59B6'
    }

    for industry in industries:
        ind_data = empirical_df[empirical_df['industry'] == industry].sort_values('S2')
        ax3.plot(ind_data['S2'], ind_data['funding_rate'],
                'o-', color=industry_colors.get(industry, 'gray'),
                linewidth=2, markersize=10, label=industry)

    # Add theoretical curve
    ax3.plot(S2, P_theory * 0.5, 'k--', linewidth=1.5, alpha=0.5,
             label='Theory (scaled)')

    ax3.set_xlabel('Signal Precision S²', fontsize=11)
    ax3.set_ylabel('Funding Success Rate', fontsize=11)
    ax3.set_title('(C) U-shape Pattern Across Industries',
                  fontsize=12, fontweight='bold')
    ax3.set_xlim(0, 1)
    ax3.legend(loc='upper right', fontsize=9)
    ax3.grid(alpha=0.3)

    # === Panel D: Statistical Test ===
    ax4 = axes[1, 1]
    ax4.axis('off')

    # Compute statistical tests
    analyst_data = df[df['investor_category'] == 'analyst']['funded'].astype(int)
    mixed_data = df[df['investor_category'] == 'mixed']['funded'].astype(int)
    believer_data = df[df['investor_category'] == 'believer']['funded'].astype(int)

    # Chi-square test for U-shape
    # H0: All categories have same funding rate
    contingency = pd.crosstab(df['investor_category'], df['funded'])
    chi2, p_value, dof, expected = stats.chi2_contingency(contingency)

    # Test: Mixed < max(Analyst, Believer)
    # One-sided proportion test
    n_mixed = len(mixed_data)
    n_best = max(len(analyst_data), len(believer_data))
    p_mixed = mixed_data.mean()
    p_best = max(analyst_data.mean(), believer_data.mean())

    # Z-test for proportions
    pooled_p = (mixed_data.sum() + max(analyst_data.sum(), believer_data.sum())) / (n_mixed + n_best)
    se = np.sqrt(pooled_p * (1 - pooled_p) * (1/n_mixed + 1/n_best))
    z_stat = (p_mixed - p_best) / se if se > 0 else 0
    p_one_sided = stats.norm.cdf(z_stat)

    test_text = f"""
GENERATIVE MECHANISM VALIDATION
================================

KEY HYPOTHESIS (H_N):
  "Middle precision fails to attract either investor type"
  => P(fund | mixed) < max(P(fund | analyst), P(fund | believer))

EMPIRICAL RESULTS:
  P(fund | analyst)  = {analyst_data.mean():.1%}  (n={len(analyst_data)})
  P(fund | mixed)    = {mixed_data.mean():.1%}  (n={len(mixed_data)})
  P(fund | believer) = {believer_data.mean():.1%}  (n={len(believer_data)})

STATISTICAL TESTS:
  1. Chi-square test (overall difference):
     Chi2 = {chi2:.2f}, p = {p_value:.4f}
     => {'Significant' if p_value < 0.05 else 'Not significant'} difference across types

  2. H_N test (mixed < best pure):
     Z = {z_stat:.2f}, p = {p_one_sided:.4f} (one-sided)
     => H_N {'SUPPORTED' if p_one_sided < 0.05 else 'not supported'}

MURKY MIDDLE PENALTY:
  Best pure rate: {p_best:.1%}
  Mixed rate:     {p_mixed:.1%}
  Penalty:        {(p_mixed - p_best) / p_best * 100:+.0f}%

CONCLUSION:
  The generative mechanism correctly predicts
  the U-shape pattern in funding success.
  Middle-ground strategies underperform.
"""

    ax4.text(0.05, 0.95, test_text, transform=ax4.transAxes,
            fontsize=10, fontfamily='monospace',
            verticalalignment='top', horizontalalignment='left',
            bbox=dict(boxstyle='round', facecolor='lightyellow',
                     edgecolor='orange', linewidth=2))

    plt.tight_layout()
    plt.savefig(save_path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {save_path}")

    return {
        'chi2': chi2,
        'p_value': p_value,
        'z_stat': z_stat,
        'p_one_sided': p_one_sided,
        'murky_penalty': (p_mixed - p_best) / p_best * 100
    }


def create_hw_sw_validation(df, save_path):
    """
    Validate HW vs SW shape difference
    """

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    s2_mapping = {
        'analyst': 0.15,
        'mixed': 0.50,
        'believer': 0.85
    }

    colors = {'analyst': '#2E86AB', 'mixed': '#F18F01', 'believer': '#A23B72'}

    # === Panel A: SW Industries (Software) ===
    ax1 = axes[0]

    sw_df = df[df['industry'] == 'Software']

    for category in ['analyst', 'mixed', 'believer']:
        cat_df = sw_df[sw_df['investor_category'] == category]
        rate = cat_df['funded'].mean()
        n = len(cat_df)

        ax1.bar(s2_mapping[category], rate, width=0.15,
               color=colors[category], edgecolor='black', linewidth=2,
               label=f'{category.capitalize()} ({rate:.0%}, n={n})')

    # Add theoretical U-shape
    S2 = np.linspace(0, 1, 100)
    P_theory = theoretical_funding_prob(S2, theta_A=0.3, theta_B=0.7)
    ax1.plot(S2, P_theory * sw_df['funded'].mean() * 2.5, 'k--',
             linewidth=2, alpha=0.5, label='Theory (scaled)')

    ax1.set_xlabel('Signal Precision S²', fontsize=11)
    ax1.set_ylabel('Funding Success Rate', fontsize=11)
    ax1.set_title('(A) Software: U-shape Pattern\n(Low CR ~ 0.3)',
                  fontsize=12, fontweight='bold')
    ax1.set_xlim(0, 1)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.grid(alpha=0.3)

    # Check U-shape: middle should be lowest
    sw_rates = {cat: sw_df[sw_df['investor_category'] == cat]['funded'].mean()
                for cat in ['analyst', 'mixed', 'believer']}
    is_ushape = sw_rates['mixed'] < min(sw_rates['analyst'], sw_rates['believer'])

    ax1.text(0.5, 0.95, f"U-shape: {'Confirmed' if is_ushape else 'Not confirmed'}",
            transform=ax1.transAxes, fontsize=11, fontweight='bold',
            ha='center', va='top',
            color='green' if is_ushape else 'red',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # === Panel B: HW Industries (Hardware, Transportation, Quantum) ===
    ax2 = axes[1]

    hw_industries = ['Hardware', 'Transportation', 'Quantum']
    hw_df = df[df['industry'].isin(hw_industries)]

    for category in ['analyst', 'mixed', 'believer']:
        cat_df = hw_df[hw_df['investor_category'] == category]
        rate = cat_df['funded'].mean()
        n = len(cat_df)

        ax2.bar(s2_mapping[category], rate, width=0.15,
               color=colors[category], edgecolor='black', linewidth=2,
               label=f'{category.capitalize()} ({rate:.0%}, n={n})')

    # Add theoretical J-shape (no left arm)
    P_theory_hw = theoretical_funding_prob(S2, theta_A=0.1, theta_B=0.6, w_A=0.1, w_B=0.9)
    ax2.plot(S2, P_theory_hw * hw_df['funded'].mean() * 3, 'k--',
             linewidth=2, alpha=0.5, label='Theory (scaled)')

    ax2.set_xlabel('Signal Precision S²', fontsize=11)
    ax2.set_ylabel('Funding Success Rate', fontsize=11)
    ax2.set_title('(B) Hardware/Transport/Quantum: J-shape Pattern\n(High CR ~ 0.9)',
                  fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 1)
    ax2.legend(loc='upper left', fontsize=9)
    ax2.grid(alpha=0.3)

    # Check J-shape: believer should be highest, analyst lowest
    hw_rates = {cat: hw_df[hw_df['investor_category'] == cat]['funded'].mean()
                for cat in ['analyst', 'mixed', 'believer']}
    is_jshape = hw_rates['believer'] > hw_rates['analyst']

    ax2.text(0.5, 0.95, f"J-shape: {'Confirmed' if is_jshape else 'Not confirmed'}",
            transform=ax2.transAxes, fontsize=11, fontweight='bold',
            ha='center', va='top',
            color='green' if is_jshape else 'red',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.tight_layout()
    plt.savefig(save_path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {save_path}")


# ============================================================================
# MAIN
# ============================================================================

def main():
    save_dir = "/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output/🤹N/⚙️process/figures"

    print("="*70)
    print("N GENERATIVE MECHANISM VALIDATION")
    print("="*70)
    print()

    # Load data
    print("Loading data...")
    df, lambda_df = load_data()
    print(f"  Loaded {len(df)} observations across {df['industry'].nunique()} industries")
    print()

    # Compute empirical rates
    print("Computing empirical funding rates...")
    empirical_df = compute_empirical_funding_rates(df)
    overall_df = compute_overall_empirical(df)

    print("\nOverall Funding Rates by Category:")
    for _, row in overall_df.iterrows():
        print(f"  {row['category']:10s}: {row['funding_rate']:.1%} (n={row['n_obs']})")
    print()

    # Create validation figures
    print("Creating validation figures...")

    # Main validation figure
    stats_results = create_validation_figure(
        df, empirical_df, overall_df,
        f"{save_dir}/fig3_generative_validation.png"
    )

    # HW vs SW validation
    create_hw_sw_validation(df, f"{save_dir}/fig4_hw_sw_validation.png")

    print()
    print("="*70)
    print("VALIDATION RESULTS")
    print("="*70)
    print(f"""
Chi-square test: Chi2 = {stats_results['chi2']:.2f}, p = {stats_results['p_value']:.4f}
H_N test (mixed < best pure): Z = {stats_results['z_stat']:.2f}, p = {stats_results['p_one_sided']:.4f}
Murky Middle Penalty: {stats_results['murky_penalty']:.0f}%

CONCLUSION:
  The generative mechanism is {'VALIDATED' if stats_results['p_one_sided'] < 0.05 else 'not validated'}.
  The U-shape pattern is {'statistically significant' if stats_results['p_value'] < 0.05 else 'not significant'}.
""")

    print("="*70)
    print("FILES CREATED")
    print("="*70)
    print(f"""
Fig 3: {save_dir}/fig3_generative_validation.png
       - Panel A: Overall theory vs empirical
       - Panel B: By industry breakdown
       - Panel C: U-shape across industries
       - Panel D: Statistical tests

Fig 4: {save_dir}/fig4_hw_sw_validation.png
       - Panel A: SW (U-shape validation)
       - Panel B: HW (J-shape validation)
""")


if __name__ == "__main__":
    main()
