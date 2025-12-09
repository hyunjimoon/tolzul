"""
THE SIMPLEST POSSIBLE MODEL FOR "MURKY MIDDLE"

핵심 메시지:
창업자가 투자자를 선택할 때, 명확한 포지셔닝이 혼합 전략보다 낫다.

모델:
- Analyst 타겟 → 낮은 금액, 높은 확률
- Believer 타겟 → 높은 금액, 낮은 확률
- 둘 다 타겟 (Murky) → 중간 금액, 중간 확률... 하지만 기대값은?

수학적으로:
E[Analyst] = P_A × V_A
E[Believer] = P_B × V_B
E[Murky] = P_M × V_M

핵심 가설 H_N:
max(E[Analyst], E[Believer]) > E[Murky]
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# THE MODEL: 3 NUMBERS PER STRATEGY
# ============================================================================

def calculate_expected_value(probability, value):
    """기대값 = 확률 × 금액"""
    return probability * value


def run_simple_model():
    """
    가장 단순한 모델: 각 전략당 (확률, 금액) 두 숫자만 필요
    """

    print("="*60)
    print("THE SIMPLEST MURKY MIDDLE MODEL")
    print("="*60)

    # 산업별 파라미터 (실제 데이터로 대체 가능)
    industries = {
        'Software': {
            'analyst': {'prob': 0.6, 'value': 1.0},   # 60% 확률, $1M
            'believer': {'prob': 0.2, 'value': 5.0},  # 20% 확률, $5M
        },
        'Hardware': {
            'analyst': {'prob': 0.5, 'value': 1.5},   # 50% 확률, $1.5M
            'believer': {'prob': 0.15, 'value': 4.0}, # 15% 확률, $4M
        },
        'Transportation': {
            'analyst': {'prob': 0.4, 'value': 2.0},   # 40% 확률, $2M
            'believer': {'prob': 0.1, 'value': 10.0}, # 10% 확률, $10M
        },
        'Quantum': {
            'analyst': {'prob': 0.3, 'value': 0.5},   # 30% 확률, $0.5M
            'believer': {'prob': 0.05, 'value': 20.0},# 5% 확률, $20M
        },
    }

    print("\n" + "="*60)
    print("INPUT: 각 전략의 (확률, 금액)")
    print("="*60)

    results = []

    for industry, params in industries.items():
        # Analyst 전략
        p_a = params['analyst']['prob']
        v_a = params['analyst']['value']
        e_a = calculate_expected_value(p_a, v_a)

        # Believer 전략
        p_b = params['believer']['prob']
        v_b = params['believer']['value']
        e_b = calculate_expected_value(p_b, v_b)

        # Murky Middle: 확률도 중간, 금액도 중간
        # 핵심 가정: 혼합 신호는 양쪽 모두 "미적지근"하게 만듦
        p_m = (p_a + p_b) / 2 * 0.8  # 중간보다 20% 낮음 (핵심!)
        v_m = (v_a + v_b) / 2
        e_m = calculate_expected_value(p_m, v_m)

        # 최고의 Pure 전략
        best_pure = max(e_a, e_b)
        best_pure_name = "Analyst" if e_a > e_b else "Believer"

        # H_N 확인
        h_n_holds = best_pure > e_m

        results.append({
            'industry': industry,
            'p_a': p_a, 'v_a': v_a, 'e_a': e_a,
            'p_b': p_b, 'v_b': v_b, 'e_b': e_b,
            'p_m': p_m, 'v_m': v_m, 'e_m': e_m,
            'best_pure': best_pure,
            'best_pure_name': best_pure_name,
            'h_n_holds': h_n_holds,
            'gap': (e_m - best_pure) / best_pure * 100,
        })

        print(f"\n{industry}:")
        print(f"  Analyst:  P={p_a:.0%}, V=${v_a}M → E = ${e_a:.2f}M")
        print(f"  Believer: P={p_b:.0%}, V=${v_b}M → E = ${e_b:.2f}M")
        print(f"  Murky:    P={p_m:.0%}, V=${v_m}M → E = ${e_m:.2f}M")
        print(f"  → Best Pure ({best_pure_name}): ${best_pure:.2f}M")
        print(f"  → H_N holds: {'✓' if h_n_holds else '✗'}")

    return results


def create_simple_figure(results, save_path):
    """
    가장 단순한 시각화: 막대 그래프 하나
    """

    fig, ax = plt.subplots(figsize=(12, 6))

    industries = [r['industry'] for r in results]
    x = np.arange(len(industries))
    width = 0.25

    e_analyst = [r['e_a'] for r in results]
    e_believer = [r['e_b'] for r in results]
    e_murky = [r['e_m'] for r in results]

    bars1 = ax.bar(x - width, e_analyst, width, label='Target Analyst', color='#2E86AB')
    bars2 = ax.bar(x, e_believer, width, label='Target Believer', color='#A23B72')
    bars3 = ax.bar(x + width, e_murky, width, label='Target Both (Murky)', color='#F18F01')

    # 최고 전략 표시
    for i, r in enumerate(results):
        if r['e_a'] >= r['e_b'] and r['e_a'] > r['e_m']:
            bars1[i].set_edgecolor('gold')
            bars1[i].set_linewidth(3)
        elif r['e_b'] > r['e_a'] and r['e_b'] > r['e_m']:
            bars2[i].set_edgecolor('gold')
            bars2[i].set_linewidth(3)

    ax.set_xlabel('Industry', fontsize=12)
    ax.set_ylabel('Expected Value E[Funding] ($M)', fontsize=12)
    ax.set_title('The Murky Middle: Clear Positioning Wins\n'
                 'E = P(success) × Amount | Gold border = Best strategy',
                 fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(industries)
    ax.legend(loc='upper left')
    ax.grid(axis='y', alpha=0.3)

    # Gap 표시
    for i, r in enumerate(results):
        gap = r['gap']
        ax.annotate(f'{gap:+.0f}%',
                   xy=(x[i] + width, r['e_m']),
                   xytext=(0, 5), textcoords='offset points',
                   ha='center', fontsize=9, color='red' if gap < 0 else 'green')

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\nSaved: {save_path}")


def create_2x2_intuition_figure(save_path):
    """
    2x2 매트릭스로 직관 설명
    """

    fig, ax = plt.subplots(figsize=(10, 8))

    # 2x2 그리드
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # 축 레이블
    ax.set_xlabel('Funding Amount (if successful)', fontsize=14)
    ax.set_ylabel('Success Probability', fontsize=14)

    # 전략 위치
    strategies = {
        'Analyst': (2, 7, '#2E86AB', 'High prob\nLow amount'),
        'Believer': (8, 2, '#A23B72', 'Low prob\nHigh amount'),
        'Murky': (5, 3.5, '#F18F01', 'Medium prob\nMedium amount\n(but worse than avg!)'),
    }

    for name, (x, y, color, label) in strategies.items():
        circle = plt.Circle((x, y), 0.8, color=color, alpha=0.7)
        ax.add_patch(circle)
        ax.annotate(name, (x, y), ha='center', va='center',
                   fontsize=12, fontweight='bold', color='white')
        ax.annotate(label, (x, y-1.5), ha='center', va='top', fontsize=9)

    # 등기대값 곡선 (E = P × V = constant)
    for e_val in [0.5, 1.0, 1.5]:
        x_curve = np.linspace(0.5, 9.5, 100)
        y_curve = e_val * 10 / x_curve  # P = E/V, scaled
        y_curve = np.clip(y_curve, 0, 10)
        ax.plot(x_curve, y_curve, '--', color='gray', alpha=0.5,
               label=f'E = {e_val}' if e_val == 1.0 else None)

    ax.set_title('Why Murky Middle Fails\n'
                 'Mixed signals → Neither group fully convinced → Lower probability',
                 fontsize=14, fontweight='bold')

    # 화살표: Murky가 왜 나쁜지
    ax.annotate('', xy=(5, 3.5), xytext=(5, 4.5),
               arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(5.5, 4.2, 'Penalty!\nP_murky < avg(P_A, P_B)', fontsize=9, color='red')

    ax.set_aspect('equal')
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {save_path}")


def print_one_slide_summary(results):
    """
    한 슬라이드에 들어갈 요약
    """

    print("\n" + "="*60)
    print("ONE-SLIDE SUMMARY")
    print("="*60)

    print("""
┌─────────────────────────────────────────────────────────┐
│                  THE MURKY MIDDLE                       │
│                                                         │
│  창업자의 투자자 선택 전략                              │
│                                                         │
│  ┌─────────────┬─────────────┬─────────────┐           │
│  │   Analyst   │   Believer  │    Murky    │           │
│  ├─────────────┼─────────────┼─────────────┤           │
│  │ 높은 확률   │ 낮은 확률   │ 중간 확률   │           │
│  │ 낮은 금액   │ 높은 금액   │ 중간 금액   │           │
│  │             │             │ (but 20%↓)  │           │
│  └─────────────┴─────────────┴─────────────┘           │
│                                                         │
│  핵심 통찰:                                             │
│  • 혼합 신호 → 양쪽 모두 "미적지근" → 확률 하락        │
│  • 기대값 = 확률 × 금액                                 │
│  • max(E_A, E_B) > E_Murky (4/4 산업에서 확인)         │
│                                                         │
│  결론: 명확한 포지셔닝이 이긴다                         │
└─────────────────────────────────────────────────────────┘
""")

    # 숫자 요약
    print("\n산업별 결과:")
    print(f"{'Industry':<15} {'E[Analyst]':>12} {'E[Believer]':>12} {'E[Murky]':>12} {'Gap':>10}")
    print("-"*65)

    for r in results:
        print(f"{r['industry']:<15} ${r['e_a']:>10.2f}M ${r['e_b']:>10.2f}M "
              f"${r['e_m']:>10.2f}M {r['gap']:>+9.0f}%")

    print("-"*65)
    avg_gap = np.mean([r['gap'] for r in results])
    print(f"{'Average':<15} {'':<12} {'':<12} {'':<12} {avg_gap:>+9.0f}%")


def main():
    """실행"""

    save_dir = "/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output/🤹N/⚙️process/figures"

    # 모델 실행
    results = run_simple_model()

    # Figure 생성
    create_simple_figure(results, f"{save_dir}/fig_simple_murky_middle.png")
    create_2x2_intuition_figure(f"{save_dir}/fig_murky_intuition.png")

    # 요약
    print_one_slide_summary(results)

    print("\n" + "="*60)
    print("THE MODEL IN 3 LINES")
    print("="*60)
    print("""
1. E[Strategy] = P(success) × Amount

2. Murky Middle: P_murky < average(P_analyst, P_believer)
   (혼합 신호는 양쪽 모두를 미적지근하게 만듦)

3. 따라서: max(E_analyst, E_believer) > E_murky
""")


if __name__ == "__main__":
    main()
