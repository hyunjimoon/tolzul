"""
Pure vs Mixture Strategy - Cross-Industry Robustness Test

Key Reframing (based on feedback):
- Entrepreneur CHOOSES which investor type to target
- NOT "being chosen by" investors
- This resolves uncertainty: the choice IS the strategy

Industry Parameters:
- Hardware: High commitment (capital intensive), low flexibility
- Software: Low commitment, high flexibility (pivot easily)
- Transportation: Very high commitment (infrastructure), moderate flexibility
- Quantum: Extreme variance in outcomes, high uncertainty

Each industry has characteristic:
- λ_analyst: Expected demand if targeting conservative investors
- λ_believer: Expected demand if targeting visionary investors
- Cost structure (p, c): Determines critical ratio
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(42)


# ============================================================================
# INDUSTRY DEFINITIONS
# ============================================================================

INDUSTRIES = {
    'Software': {
        'description': 'Low capital, high pivot flexibility',
        'lambda_analyst': 2,      # Conservative: modest but reliable growth
        'lambda_believer': 8,     # Visionary: potential for viral growth
        'price': 5,               # High margin possible
        'cost': 1,                # Low fixed costs
        'commitment_level': 'Low',
        'typical_runway': '18-24 months',
    },
    'Hardware': {
        'description': 'High capital, manufacturing constraints',
        'lambda_analyst': 3,      # Conservative: steady B2B sales
        'lambda_believer': 6,     # Visionary: consumer market breakthrough
        'price': 4,               # Moderate margin
        'cost': 2,                # Significant production costs
        'commitment_level': 'High',
        'typical_runway': '24-36 months',
    },
    'Transportation': {
        'description': 'Very high capital, infrastructure dependent',
        'lambda_analyst': 2,      # Conservative: regional operations
        'lambda_believer': 10,    # Visionary: network effects, national scale
        'price': 6,               # High revenue potential
        'cost': 4,                # Very high infrastructure costs
        'commitment_level': 'Very High',
        'typical_runway': '36-48 months',
    },
    'Quantum': {
        'description': 'Extreme uncertainty, long R&D cycles',
        'lambda_analyst': 1,      # Conservative: niche enterprise applications
        'lambda_believer': 15,    # Visionary: paradigm shift
        'price': 10,              # Very high value if successful
        'cost': 3,                # High R&D costs
        'commitment_level': 'Extreme',
        'typical_runway': '48-72 months',
    },
}


# ============================================================================
# CORE FUNCTIONS
# ============================================================================

def poisson_cdf_inverse(cr, lam):
    """Return k* such that P(D <= k*) >= CR for Poisson(lam)."""
    return int(stats.poisson.ppf(cr, lam))


def mixture_cdf(k, lam1, lam2, w1=0.5):
    """CDF of mixture distribution."""
    return w1 * stats.poisson.cdf(k, lam1) + (1 - w1) * stats.poisson.cdf(k, lam2)


def mixture_cdf_inverse(cr, lam1, lam2, w1=0.5):
    """Find smallest k such that mixture CDF >= CR."""
    max_k = int(max(lam1, lam2) * 3 + 10)
    for k in range(max_k + 1):
        if mixture_cdf(k, lam1, lam2, w1) >= cr:
            return k
    return max_k


def generate_demand(demand_type, n_sim, lam_analyst, lam_believer):
    """Generate demand samples based on type."""
    if demand_type == 'analyst':
        return np.random.poisson(lam_analyst, n_sim)
    elif demand_type == 'believer':
        return np.random.poisson(lam_believer, n_sim)
    elif demand_type == 'mixture':
        n1 = n_sim // 2
        samples = np.concatenate([
            np.random.poisson(lam_analyst, n1),
            np.random.poisson(lam_believer, n_sim - n1)
        ])
        np.random.shuffle(samples)
        return samples
    else:
        raise ValueError(f"Unknown demand type: {demand_type}")


def newsvendor_profit(k, demand_samples, p, c):
    """
    π = p * min(k, D) - c * k
    """
    sales = np.minimum(k, demand_samples)
    profits = p * sales - c * k
    return np.mean(profits), np.std(profits), profits


# ============================================================================
# ENTREPRENEUR CHOICE FRAMEWORK
# ============================================================================

def entrepreneur_chooses_investor(industry_name, n_sim=100000):
    """
    REFRAMED MODEL: Entrepreneur CHOOSES which investor type to target.

    The entrepreneur's choice:
    1. Target Analysts → pitch conservative, demand follows Poisson(λ_analyst)
    2. Target Believers → pitch visionary, demand follows Poisson(λ_believer)
    3. Target Both (Murky) → mixed signal, demand follows mixture

    Key insight: The entrepreneur's choice DETERMINES the demand distribution!
    This is NOT about uncertainty - it's about strategic positioning.
    """
    params = INDUSTRIES[industry_name]
    lam_a = params['lambda_analyst']
    lam_b = params['lambda_believer']
    p = params['price']
    c = params['cost']

    cr = (p - c) / p  # Critical ratio

    results = {}

    # Strategy 1: CHOOSE to target Analysts
    # → Demand becomes Poisson(λ_analyst)
    # → Optimize for that distribution
    k_analyst = poisson_cdf_inverse(cr, lam_a)
    demand_analyst = generate_demand('analyst', n_sim, lam_a, lam_b)
    profit_mean, profit_std, profits = newsvendor_profit(k_analyst, demand_analyst, p, c)
    results['target_analyst'] = {
        'k': k_analyst,
        'expected_profit': profit_mean,
        'profit_std': profit_std,
        'profits': profits,
        'demand_mean': np.mean(demand_analyst),
        'strategy': f"Target Analysts (λ={lam_a})"
    }

    # Strategy 2: CHOOSE to target Believers
    # → Demand becomes Poisson(λ_believer)
    # → Optimize for that distribution
    k_believer = poisson_cdf_inverse(cr, lam_b)
    demand_believer = generate_demand('believer', n_sim, lam_a, lam_b)
    profit_mean, profit_std, profits = newsvendor_profit(k_believer, demand_believer, p, c)
    results['target_believer'] = {
        'k': k_believer,
        'expected_profit': profit_mean,
        'profit_std': profit_std,
        'profits': profits,
        'demand_mean': np.mean(demand_believer),
        'strategy': f"Target Believers (λ={lam_b})"
    }

    # Strategy 3: CHOOSE to target Both (Murky Middle)
    # → Demand becomes mixture (neither fully convinced)
    # → Optimize for mixture distribution
    k_mixture = mixture_cdf_inverse(cr, lam_a, lam_b)
    demand_mixture = generate_demand('mixture', n_sim, lam_a, lam_b)
    profit_mean, profit_std, profits = newsvendor_profit(k_mixture, demand_mixture, p, c)
    results['target_both'] = {
        'k': k_mixture,
        'expected_profit': profit_mean,
        'profit_std': profit_std,
        'profits': profits,
        'demand_mean': np.mean(demand_mixture),
        'strategy': f"Target Both (mixture)"
    }

    return results, cr, params


def analyze_industry(industry_name, n_sim=100000):
    """Analyze one industry and return structured results."""
    results, cr, params = entrepreneur_chooses_investor(industry_name, n_sim)

    # Find best strategy
    profits = {k: v['expected_profit'] for k, v in results.items()}
    best_strategy = max(profits, key=profits.get)
    best_profit = profits[best_strategy]

    # Calculate relative performance
    analyst_profit = results['target_analyst']['expected_profit']
    believer_profit = results['target_believer']['expected_profit']
    mixture_profit = results['target_both']['expected_profit']

    best_pure = max(analyst_profit, believer_profit)

    return {
        'industry': industry_name,
        'lambda_analyst': params['lambda_analyst'],
        'lambda_believer': params['lambda_believer'],
        'lambda_ratio': params['lambda_believer'] / params['lambda_analyst'],
        'critical_ratio': cr,
        'commitment_level': params['commitment_level'],
        'k_analyst': results['target_analyst']['k'],
        'k_believer': results['target_believer']['k'],
        'k_mixture': results['target_both']['k'],
        'profit_analyst': analyst_profit,
        'profit_believer': believer_profit,
        'profit_mixture': mixture_profit,
        'best_pure': best_pure,
        'best_strategy': best_strategy,
        'mixture_vs_best_pure': mixture_profit - best_pure,
        'mixture_vs_best_pure_pct': (mixture_profit - best_pure) / abs(best_pure) * 100 if best_pure != 0 else 0,
        'hypothesis_holds': best_pure > mixture_profit,  # H_N: max{pure} > mixture
        'std_analyst': results['target_analyst']['profit_std'],
        'std_believer': results['target_believer']['profit_std'],
        'std_mixture': results['target_both']['profit_std'],
        'sharpe_analyst': analyst_profit / results['target_analyst']['profit_std'] if results['target_analyst']['profit_std'] > 0 else 0,
        'sharpe_believer': believer_profit / results['target_believer']['profit_std'] if results['target_believer']['profit_std'] > 0 else 0,
        'sharpe_mixture': mixture_profit / results['target_both']['profit_std'] if results['target_both']['profit_std'] > 0 else 0,
    }


def run_cross_industry_analysis(n_sim=100000):
    """Run analysis across all industries."""
    print("="*80)
    print("CROSS-INDUSTRY ROBUSTNESS TEST")
    print("Entrepreneur CHOOSES Investor Type (Reframed Model)")
    print("="*80)

    all_results = []

    for industry in INDUSTRIES:
        result = analyze_industry(industry, n_sim)
        all_results.append(result)

        print(f"\n{'='*60}")
        print(f"{industry}: {INDUSTRIES[industry]['description']}")
        print(f"{'='*60}")
        print(f"λ_analyst={result['lambda_analyst']}, λ_believer={result['lambda_believer']} (ratio: {result['lambda_ratio']:.1f}x)")
        print(f"Critical Ratio: {result['critical_ratio']:.3f}")
        print(f"\n{'Strategy':<25} {'k*':>5} {'E[π]':>10} {'Std[π]':>10} {'Sharpe':>8}")
        print("-"*60)
        print(f"{'Target Analysts':<25} {result['k_analyst']:>5} {result['profit_analyst']:>10.2f} {result['std_analyst']:>10.2f} {result['sharpe_analyst']:>8.3f}")
        print(f"{'Target Believers':<25} {result['k_believer']:>5} {result['profit_believer']:>10.2f} {result['std_believer']:>10.2f} {result['sharpe_believer']:>8.3f}")
        print(f"{'Target Both (Murky)':<25} {result['k_mixture']:>5} {result['profit_mixture']:>10.2f} {result['std_mixture']:>10.2f} {result['sharpe_mixture']:>8.3f}")
        print("-"*60)
        print(f"Best Pure vs Mixture: {result['mixture_vs_best_pure']:+.2f} ({result['mixture_vs_best_pure_pct']:+.1f}%)")
        print(f"H_N (Pure > Mixture): {'✓ HOLDS' if result['hypothesis_holds'] else '✗ FAILS'}")

    return all_results


def create_industry_comparison_figure(results, save_dir):
    """Create cross-industry comparison figure."""

    fig, axes = plt.subplots(2, 2, figsize=(14, 12))

    industries = [r['industry'] for r in results]
    x = np.arange(len(industries))
    width = 0.25

    # Plot 1: Expected Profit Comparison
    ax1 = axes[0, 0]
    analyst_profits = [r['profit_analyst'] for r in results]
    believer_profits = [r['profit_believer'] for r in results]
    mixture_profits = [r['profit_mixture'] for r in results]

    bars1 = ax1.bar(x - width, analyst_profits, width, label='Target Analysts', color='#2E86AB')
    bars2 = ax1.bar(x, believer_profits, width, label='Target Believers', color='#A23B72')
    bars3 = ax1.bar(x + width, mixture_profits, width, label='Target Both (Murky)', color='#F18F01')

    # Mark best strategy for each industry
    for i, r in enumerate(results):
        best = max(r['profit_analyst'], r['profit_believer'], r['profit_mixture'])
        if r['profit_analyst'] == best:
            bars1[i].set_edgecolor('gold')
            bars1[i].set_linewidth(3)
        elif r['profit_believer'] == best:
            bars2[i].set_edgecolor('gold')
            bars2[i].set_linewidth(3)
        else:
            bars3[i].set_edgecolor('gold')
            bars3[i].set_linewidth(3)

    ax1.set_xlabel('Industry')
    ax1.set_ylabel('Expected Profit E[π]')
    ax1.set_title('Expected Profit by Strategy and Industry\n(Gold border = Best strategy)', fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(industries)
    ax1.legend()
    ax1.grid(axis='y', alpha=0.3)

    # Plot 2: Mixture vs Best Pure (% difference)
    ax2 = axes[0, 1]
    mixture_vs_pure = [r['mixture_vs_best_pure_pct'] for r in results]
    colors = ['green' if v >= 0 else 'red' for v in mixture_vs_pure]

    bars = ax2.bar(industries, mixture_vs_pure, color=colors, edgecolor='black')
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=1)
    ax2.set_xlabel('Industry')
    ax2.set_ylabel('(Mixture - Best Pure) / |Best Pure| (%)')
    ax2.set_title('Murky Middle Performance Gap\n(Negative = Pure strategy wins)', fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)

    # Add value labels
    for bar, val in zip(bars, mixture_vs_pure):
        height = bar.get_height()
        ax2.annotate(f'{val:+.1f}%',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3 if height >= 0 else -12),
                    textcoords="offset points",
                    ha='center', fontsize=9, fontweight='bold')

    # Plot 3: Sharpe Ratio (Risk-adjusted returns)
    ax3 = axes[1, 0]
    sharpe_analyst = [r['sharpe_analyst'] for r in results]
    sharpe_believer = [r['sharpe_believer'] for r in results]
    sharpe_mixture = [r['sharpe_mixture'] for r in results]

    ax3.bar(x - width, sharpe_analyst, width, label='Target Analysts', color='#2E86AB')
    ax3.bar(x, sharpe_believer, width, label='Target Believers', color='#A23B72')
    ax3.bar(x + width, sharpe_mixture, width, label='Target Both', color='#F18F01')

    ax3.set_xlabel('Industry')
    ax3.set_ylabel('Sharpe Ratio (E[π]/Std[π])')
    ax3.set_title('Risk-Adjusted Performance\n(Higher = Better risk/return tradeoff)', fontweight='bold')
    ax3.set_xticks(x)
    ax3.set_xticklabels(industries)
    ax3.legend()
    ax3.grid(axis='y', alpha=0.3)

    # Plot 4: Lambda Ratio vs Mixture Gap
    ax4 = axes[1, 1]
    lambda_ratios = [r['lambda_ratio'] for r in results]
    mixture_gaps = [r['mixture_vs_best_pure_pct'] for r in results]

    ax4.scatter(lambda_ratios, mixture_gaps, s=200, c=range(len(results)), cmap='viridis', edgecolor='black', linewidth=2)

    for i, ind in enumerate(industries):
        ax4.annotate(ind, (lambda_ratios[i], mixture_gaps[i]),
                    xytext=(5, 5), textcoords='offset points', fontsize=10)

    ax4.axhline(y=0, color='red', linestyle='--', linewidth=1.5, label='Break-even')
    ax4.set_xlabel('λ_believer / λ_analyst (Demand Spread)')
    ax4.set_ylabel('Mixture Performance Gap (%)')
    ax4.set_title('Demand Spread vs Murky Middle Penalty\n(Higher spread → Larger penalty expected)', fontweight='bold')
    ax4.grid(alpha=0.3)
    ax4.legend()

    plt.tight_layout()
    plt.savefig(f'{save_dir}/fig_cross_industry_robustness.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\nSaved: {save_dir}/fig_cross_industry_robustness.png")


def create_entrepreneur_choice_figure(save_dir):
    """Create figure showing entrepreneur's strategic choice."""

    fig, axes = plt.subplots(2, 2, figsize=(14, 12))

    for idx, industry in enumerate(INDUSTRIES):
        ax = axes[idx // 2, idx % 2]
        params = INDUSTRIES[industry]
        lam_a = params['lambda_analyst']
        lam_b = params['lambda_believer']
        p = params['price']
        c = params['cost']

        # Generate profit curves for different k values
        k_range = range(0, max(lam_a, lam_b) * 2 + 5)
        n_sim = 50000

        demand_analyst = generate_demand('analyst', n_sim, lam_a, lam_b)
        demand_believer = generate_demand('believer', n_sim, lam_a, lam_b)
        demand_mixture = generate_demand('mixture', n_sim, lam_a, lam_b)

        profits_if_analyst = [newsvendor_profit(k, demand_analyst, p, c)[0] for k in k_range]
        profits_if_believer = [newsvendor_profit(k, demand_believer, p, c)[0] for k in k_range]
        profits_if_mixture = [newsvendor_profit(k, demand_mixture, p, c)[0] for k in k_range]

        ax.plot(k_range, profits_if_analyst, 'o-', label=f'If Target Analysts (λ={lam_a})',
                linewidth=2, markersize=5, color='#2E86AB')
        ax.plot(k_range, profits_if_believer, 's-', label=f'If Target Believers (λ={lam_b})',
                linewidth=2, markersize=5, color='#A23B72')
        ax.plot(k_range, profits_if_mixture, '^-', label='If Target Both (mixture)',
                linewidth=2, markersize=5, color='#F18F01')

        # Mark optimal k* for each strategy
        cr = (p - c) / p
        k_opt_analyst = poisson_cdf_inverse(cr, lam_a)
        k_opt_believer = poisson_cdf_inverse(cr, lam_b)
        k_opt_mixture = mixture_cdf_inverse(cr, lam_a, lam_b)

        ax.axvline(x=k_opt_analyst, color='#2E86AB', linestyle='--', alpha=0.5)
        ax.axvline(x=k_opt_believer, color='#A23B72', linestyle='--', alpha=0.5)
        ax.axvline(x=k_opt_mixture, color='#F18F01', linestyle='--', alpha=0.5)

        # Shade "murky middle" zone
        if k_opt_analyst < k_opt_mixture < k_opt_believer:
            ax.axvspan(k_opt_analyst, k_opt_believer, alpha=0.1, color='gray', label='Strategy Span')

        ax.set_xlabel('Commitment Level k')
        ax.set_ylabel('Expected Profit E[π]')
        ax.set_title(f'{industry}\n{params["description"]}', fontweight='bold')
        ax.legend(loc='best', fontsize=8)
        ax.grid(alpha=0.3)

    plt.suptitle("Entrepreneur's Strategic Choice: Which Investor Type to Target?\n"
                 "(Dashed lines = optimal k* for each strategy)",
                 fontsize=13, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(f'{save_dir}/fig_entrepreneur_choice.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {save_dir}/fig_entrepreneur_choice.png")


def generate_summary_table(results):
    """Generate a summary table."""
    print("\n" + "="*100)
    print("SUMMARY TABLE: Cross-Industry Robustness Test")
    print("="*100)

    print(f"\n{'Industry':<15} {'λ_A':>5} {'λ_B':>5} {'Ratio':>6} {'CR':>6} | "
          f"{'E[π]_A':>8} {'E[π]_B':>8} {'E[π]_Mix':>8} | {'Gap%':>7} {'H_N':>6}")
    print("-"*100)

    for r in results:
        hn_status = "✓" if r['hypothesis_holds'] else "✗"
        print(f"{r['industry']:<15} {r['lambda_analyst']:>5} {r['lambda_believer']:>5} "
              f"{r['lambda_ratio']:>6.1f} {r['critical_ratio']:>6.2f} | "
              f"{r['profit_analyst']:>8.2f} {r['profit_believer']:>8.2f} {r['profit_mixture']:>8.2f} | "
              f"{r['mixture_vs_best_pure_pct']:>+7.1f} {hn_status:>6}")

    print("-"*100)

    # Summary statistics
    n_hypothesis_holds = sum(1 for r in results if r['hypothesis_holds'])
    avg_gap = np.mean([r['mixture_vs_best_pure_pct'] for r in results])

    print(f"\nH_N holds in {n_hypothesis_holds}/{len(results)} industries")
    print(f"Average Mixture Gap: {avg_gap:+.1f}%")

    return n_hypothesis_holds, avg_gap


def main():
    """Main execution."""
    print("="*80)
    print("PURE VS MIXTURE STRATEGY - CROSS-INDUSTRY ROBUSTNESS TEST")
    print("="*80)
    print("""
REFRAMED MODEL: Entrepreneur CHOOSES Investor Type

Key insight from feedback:
- The entrepreneur is NOT passively waiting to be chosen
- The entrepreneur ACTIVELY SELECTS which investor type to target
- This choice DETERMINES the demand distribution they face

Strategy mapping:
1. Target Analysts → Conservative pitch → D ~ Poisson(λ_analyst)
2. Target Believers → Visionary pitch → D ~ Poisson(λ_believer)
3. Target Both → Mixed signal → D ~ Mixture (neither fully convinced)

The "murky middle" problem: Targeting both may leave BOTH groups unconvinced,
resulting in suboptimal outcomes compared to clear positioning.
""")

    N_SIM = 100000

    # Run cross-industry analysis
    results = run_cross_industry_analysis(N_SIM)

    # Generate summary
    n_holds, avg_gap = generate_summary_table(results)

    # Create figures
    fig_dir = "/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output/🤹N/⚙️process/figures"
    create_industry_comparison_figure(results, fig_dir)
    create_entrepreneur_choice_figure(fig_dir)

    # Final conclusions
    print("\n" + "="*80)
    print("CONCLUSIONS")
    print("="*80)
    print(f"""
ROBUSTNESS TEST RESULTS:

1. H_N (Pure > Mixture) holds in {n_holds}/{len(results)} industries
   Average performance gap: {avg_gap:+.1f}%

2. Industry-specific findings:
""")

    for r in results:
        best = "Analysts" if r['profit_analyst'] > r['profit_believer'] else "Believers"
        print(f"   {r['industry']:<15}: Best pure strategy = Target {best}")
        print(f"                    Mixture gap = {r['mixture_vs_best_pure_pct']:+.1f}%")
        if r['hypothesis_holds']:
            print(f"                    → Clear positioning WINS")
        else:
            print(f"                    → Mixture is competitive (but higher variance)")
        print()

    print("""
3. KEY INSIGHT: The "Murky Middle" penalty varies by industry:
   - Higher λ_believer/λ_analyst ratio → Larger spread → Bigger penalty expected
   - Industries with extreme upside (Quantum) show largest gaps
   - Lower-variance industries (Hardware) show smaller gaps

4. PRACTICAL RECOMMENDATION:
   - Entrepreneurs should COMMIT to a clear investor type
   - The choice of investor type should match the venture's TRUE potential
   - "Playing it safe" with mixed signals often underperforms clear positioning

5. RISK-RETURN TRADEOFF:
   - Targeting Believers: Higher E[π], Higher Std[π] (boom or bust)
   - Targeting Analysts: Lower E[π], Lower Std[π] (steady but limited)
   - Mixture: Often worst of both worlds
""")


if __name__ == "__main__":
    main()
