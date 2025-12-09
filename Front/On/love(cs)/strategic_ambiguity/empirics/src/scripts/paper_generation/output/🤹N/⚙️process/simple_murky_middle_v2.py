"""
THE SIMPLEST MURKY MIDDLE MODEL - V2

핵심 수정:
1. Murky의 페널티를 더 정교하게 모델링
2. "혼합 신호"가 왜 양쪽 모두에게 나쁜지 명확히

핵심 통찰:
Murky는 "평균"이 아니다!
- Analyst에게: "너무 리스키해 보여" → 펀딩 거절
- Believer에게: "충분히 대담하지 않아" → 펀딩 거절
- 결과: 양쪽 모두의 "최소 기준"을 충족하지 못함

모델:
E[Murky] = P_A × P_B × (V_A + V_B)/2
         = (두 투자자 모두 설득해야 하는 상황)

vs Pure:
E[Analyst] = P_A × V_A (Analyst만 설득하면 됨)
E[Believer] = P_B × V_B (Believer만 설득하면 됨)
"""

import numpy as np
import matplotlib.pyplot as plt


def run_correct_model():
    """
    수정된 모델: Murky = 두 투자자 타입 모두 설득해야 함
    """

    print("="*70)
    print("THE MURKY MIDDLE - CORRECTED MODEL")
    print("="*70)

    print("""
핵심 가정 변경:

기존 (틀린 모델):
  P_murky = avg(P_A, P_B) × 0.8  (단순 평균에 페널티)

수정 (올바른 모델):
  P_murky = P_A × P_B × α        (두 타입 모두 설득해야 함)

  여기서 α는 "혼합 신호 보너스" (1.0 ~ 2.0)
  - 만약 혼합 신호가 양쪽을 모두 부분적으로 설득하면 α > 1
  - 하지만 독립적 설득이라면 α = 1

왜 이게 맞는가?
  - Pure Analyst: Analyst만 타겟 → P_A 확률로 성공
  - Pure Believer: Believer만 타겟 → P_B 확률로 성공
  - Murky: 둘 다 타겟 → 둘 다 동시에 관심 가져야 함
         → P_A × P_B (독립 가정 시)
""")

    industries = {
        'Software': {
            'analyst': {'prob': 0.6, 'value': 1.0},
            'believer': {'prob': 0.2, 'value': 5.0},
        },
        'Hardware': {
            'analyst': {'prob': 0.5, 'value': 1.5},
            'believer': {'prob': 0.15, 'value': 4.0},
        },
        'Transportation': {
            'analyst': {'prob': 0.4, 'value': 2.0},
            'believer': {'prob': 0.1, 'value': 10.0},
        },
        'Quantum': {
            'analyst': {'prob': 0.3, 'value': 0.5},
            'believer': {'prob': 0.05, 'value': 20.0},
        },
    }

    # 다양한 α 값으로 테스트
    alpha_values = [1.0, 1.5, 2.0, 2.5, 3.0]

    print("\n" + "="*70)
    print("α 값에 따른 H_N 검증 (α = 혼합 신호 보너스)")
    print("="*70)

    for alpha in alpha_values:
        print(f"\n--- α = {alpha} ---")
        h_n_count = 0

        for industry, params in industries.items():
            p_a = params['analyst']['prob']
            v_a = params['analyst']['value']
            e_a = p_a * v_a

            p_b = params['believer']['prob']
            v_b = params['believer']['value']
            e_b = p_b * v_b

            # Murky: 곱셈 모델
            p_m = p_a * p_b * alpha  # 두 타입 모두 설득
            p_m = min(p_m, 1.0)      # 확률은 1 초과 불가
            v_m = (v_a + v_b) / 2
            e_m = p_m * v_m

            best_pure = max(e_a, e_b)
            h_n = best_pure > e_m
            if h_n:
                h_n_count += 1

            gap = (e_m - best_pure) / best_pure * 100

            print(f"{industry:<15}: E_A=${e_a:.2f}M, E_B=${e_b:.2f}M, "
                  f"E_M=${e_m:.2f}M (P_M={p_m:.1%}), Gap={gap:+.0f}%, "
                  f"H_N={'✓' if h_n else '✗'}")

        print(f"H_N holds: {h_n_count}/4 industries")

    return industries


def find_critical_alpha(industries):
    """
    H_N이 항상 성립하는 최소 α 값 찾기
    """

    print("\n" + "="*70)
    print("FINDING CRITICAL α")
    print("="*70)

    results = []

    for industry, params in industries.items():
        p_a = params['analyst']['prob']
        v_a = params['analyst']['value']
        e_a = p_a * v_a

        p_b = params['believer']['prob']
        v_b = params['believer']['value']
        e_b = p_b * v_b

        best_pure = max(e_a, e_b)
        v_m = (v_a + v_b) / 2

        # E_murky = P_A × P_B × α × V_m = best_pure 일 때 α 찾기
        # α = best_pure / (P_A × P_B × V_m)
        critical_alpha = best_pure / (p_a * p_b * v_m)

        results.append({
            'industry': industry,
            'critical_alpha': critical_alpha,
            'best_pure': best_pure,
            'p_product': p_a * p_b,
        })

        print(f"{industry:<15}: Critical α = {critical_alpha:.2f}")
        print(f"                 (α < {critical_alpha:.2f} → H_N holds)")

    max_critical = max(r['critical_alpha'] for r in results)
    print(f"\n결론: α < {max_critical:.2f} 이면 모든 산업에서 H_N 성립")

    return results


def create_simple_visual(industries, save_path):
    """
    가장 단순한 시각화
    """

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Plot 1: 세 전략 비교 (α = 1.5 사용)
    ax1 = axes[0]
    alpha = 1.5

    ind_names = list(industries.keys())
    x = np.arange(len(ind_names))
    width = 0.25

    e_analyst = []
    e_believer = []
    e_murky = []

    for params in industries.values():
        p_a, v_a = params['analyst']['prob'], params['analyst']['value']
        p_b, v_b = params['believer']['prob'], params['believer']['value']

        e_analyst.append(p_a * v_a)
        e_believer.append(p_b * v_b)

        p_m = min(p_a * p_b * alpha, 1.0)
        v_m = (v_a + v_b) / 2
        e_murky.append(p_m * v_m)

    bars1 = ax1.bar(x - width, e_analyst, width, label='Analyst', color='#2E86AB')
    bars2 = ax1.bar(x, e_believer, width, label='Believer', color='#A23B72')
    bars3 = ax1.bar(x + width, e_murky, width, label='Murky', color='#F18F01')

    ax1.set_xlabel('Industry')
    ax1.set_ylabel('Expected Value ($M)')
    ax1.set_title(f'Expected Funding by Strategy (α = {alpha})\n'
                  f'E = P(success) × Amount')
    ax1.set_xticks(x)
    ax1.set_xticklabels(ind_names)
    ax1.legend()
    ax1.grid(axis='y', alpha=0.3)

    # Plot 2: α에 따른 Gap 변화
    ax2 = axes[1]
    alpha_range = np.linspace(0.5, 4.0, 50)

    for industry, params in industries.items():
        p_a, v_a = params['analyst']['prob'], params['analyst']['value']
        p_b, v_b = params['believer']['prob'], params['believer']['value']

        e_a = p_a * v_a
        e_b = p_b * v_b
        best_pure = max(e_a, e_b)
        v_m = (v_a + v_b) / 2

        gaps = []
        for alpha in alpha_range:
            p_m = min(p_a * p_b * alpha, 1.0)
            e_m = p_m * v_m
            gap = (e_m - best_pure) / best_pure * 100
            gaps.append(gap)

        ax2.plot(alpha_range, gaps, label=industry, linewidth=2)

    ax2.axhline(y=0, color='red', linestyle='--', linewidth=2)
    ax2.fill_between(alpha_range, -100, 0, alpha=0.1, color='green')
    ax2.set_xlabel('α (Mixed Signal Bonus)')
    ax2.set_ylabel('Murky Gap vs Best Pure (%)')
    ax2.set_title('When Does H_N Hold?\n'
                  'Below red line = Pure strategy wins')
    ax2.legend()
    ax2.grid(alpha=0.3)
    ax2.set_xlim(0.5, 4.0)
    ax2.set_ylim(-80, 50)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\nSaved: {save_path}")


def print_final_model():
    """
    최종 모델 요약
    """

    print("\n" + "="*70)
    print("FINAL MODEL: THE SIMPLEST VERSION")
    print("="*70)

    print("""
┌────────────────────────────────────────────────────────────────┐
│                    THE MURKY MIDDLE MODEL                      │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  INPUT (산업별로 4개 숫자):                                    │
│    • P_A = Analyst 타겟 시 성공 확률                          │
│    • V_A = Analyst 성공 시 펀딩 금액                          │
│    • P_B = Believer 타겟 시 성공 확률                         │
│    • V_B = Believer 성공 시 펀딩 금액                         │
│                                                                │
│  MODEL:                                                        │
│    E[Analyst]  = P_A × V_A                                    │
│    E[Believer] = P_B × V_B                                    │
│    E[Murky]    = (P_A × P_B × α) × (V_A + V_B)/2             │
│                                                                │
│  KEY PARAMETER:                                                │
│    α = "혼합 신호 보너스" (typically 1.0 ~ 2.0)               │
│    • α = 1: 두 투자자 독립적으로 평가                         │
│    • α > 1: 혼합 신호가 일부 시너지                           │
│    • α < 1: 혼합 신호가 양쪽 모두 반감                        │
│                                                                │
│  HYPOTHESIS H_N:                                               │
│    max(E[Analyst], E[Believer]) > E[Murky]                    │
│                                                                │
│  CONDITION FOR H_N:                                            │
│    α < best_pure / (P_A × P_B × V_avg)                        │
│                                                                │
└────────────────────────────────────────────────────────────────┘

실무적 해석:
• Murky가 성공하려면 Analyst AND Believer 모두 관심 가져야 함
• 두 확률의 곱 (P_A × P_B)은 각각보다 훨씬 작음
• 예: P_A=0.5, P_B=0.2 → P_murky = 0.1 (각각보다 훨씬 낮음!)
• 금액이 평균이라도 확률이 너무 낮아서 기대값 손실
""")


def main():
    save_dir = "/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/output/🤹N/⚙️process/figures"

    industries = run_correct_model()
    find_critical_alpha(industries)
    create_simple_visual(industries, f"{save_dir}/fig_simple_murky_v2.png")
    print_final_model()


if __name__ == "__main__":
    main()
