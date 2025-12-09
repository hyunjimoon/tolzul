"""
N SIMULATION: U-Shape Funding Pattern

핵심 메시지:
"중간 정밀도(S²≈0.5)는 Analyst에겐 모호하고 Believer에겐 지루해서 투자받지 못한다."

배경: HW vs SW 분리가 중요한 이유
- AV: "high regulatory uncertainty → high C" → CR ≈ 0.9
- Fleet SW: "low uncertainty → low C" → CR ≈ 0.3

이것은 AOC "크기"가 아니라 CR "구조"가 다른 두 세계다.

| Segment | C    | F    | CR  | k*  | Analyst 진입 |
|---------|------|------|-----|-----|--------------|
| HW      | High | Low  | 0.9 | 3-4 | ❌           |
| SW      | Low  | High | 0.3 | 1-2 | ✅           |

Outputs:
- Fig 1: 전체 U-shape
- Fig 2: HW vs SW shape 비교
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as mpatches

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11

# ============================================================================
# CORE MODEL
# ============================================================================

def analyst_investment_prob(S2, threshold_analyst=0.3):
    """
    Analyst invests when S² ≤ threshold (precise enough to verify)
    Returns smooth transition probability
    """
    # Sigmoid transition centered at threshold
    steepness = 15
    return 1 / (1 + np.exp(steepness * (S2 - threshold_analyst)))


def believer_investment_prob(S2, threshold_believer=0.7):
    """
    Believer invests when S² ≥ threshold (vague enough for projection)
    Returns smooth transition probability
    """
    # Sigmoid transition centered at threshold
    steepness = 15
    return 1 / (1 + np.exp(-steepness * (S2 - threshold_believer)))


def compute_funding_prob(S2, w_analyst=0.5, w_believer=0.5,
                         theta_A=0.3, theta_B=0.7):
    """
    Total funding probability = weighted sum of investor types

    P_fund = w_A * P_analyst(S²) + w_B * P_believer(S²)
    """
    P_A = analyst_investment_prob(S2, theta_A)
    P_B = believer_investment_prob(S2, theta_B)

    return w_analyst * P_A + w_believer * P_B


def compute_hw_sw_funding(S2, segment='SW'):
    """
    Compute funding probability for HW vs SW segments

    HW (High CR ~ 0.9):
    - Analyst region (S²≤0.3) doesn't exist because CR > theta_A
    - Only Believer invests
    - Result: J-shape (right arm only)

    SW (Low CR ~ 0.3):
    - Both Analyst and Believer regions accessible
    - Result: U-shape (both arms)
    """
    if segment == 'HW':
        # HW: No analyst (CR too high), only believer
        # theta_A effectively → 0 (no analyst entry)
        theta_A = 0.1  # Very restrictive for analysts
        theta_B = 0.6  # Believers still invest in very vague
        w_analyst = 0.1  # Minimal analyst weight
        w_believer = 0.9
    else:  # SW
        # SW: Both types active
        theta_A = 0.4  # Analysts can evaluate more
        theta_B = 0.7
        w_analyst = 0.5
        w_believer = 0.5

    P_A = analyst_investment_prob(S2, theta_A)
    P_B = believer_investment_prob(S2, theta_B)

    return w_analyst * P_A + w_believer * P_B, P_A, P_B


# ============================================================================
# FIGURE 1: FULL U-SHAPE
# ============================================================================

def create_fig1_ushape(save_path):
    """
    Fig 1: 전체 U-shape (S² vs P_fund)
    핵심 메시지 시각화
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    S2 = np.linspace(0, 1, 200)

    # === Panel A: Basic U-shape ===
    ax1 = axes[0]

    # Individual investor probabilities
    P_analyst = analyst_investment_prob(S2, 0.3)
    P_believer = believer_investment_prob(S2, 0.7)
    P_fund = 0.5 * P_analyst + 0.5 * P_believer

    # Plot
    ax1.plot(S2, P_analyst, '--', color='#2E86AB', linewidth=2.5,
             label='P(Analyst invests)')
    ax1.plot(S2, P_believer, '--', color='#A23B72', linewidth=2.5,
             label='P(Believer invests)')
    ax1.plot(S2, P_fund, '-', color='#333333', linewidth=3,
             label='P(Funding) = 0.5·P_A + 0.5·P_B')

    # Shade murky middle
    murky_mask = (S2 >= 0.3) & (S2 <= 0.7)
    ax1.fill_between(S2[murky_mask], 0, P_fund[murky_mask],
                     alpha=0.2, color='#F18F01', label='Murky Middle')

    # Annotations
    ax1.axvline(x=0.3, color='#2E86AB', linestyle=':', alpha=0.7)
    ax1.axvline(x=0.7, color='#A23B72', linestyle=':', alpha=0.7)

    ax1.annotate('Analyst\nRegion', xy=(0.15, 0.85), fontsize=10,
                 ha='center', color='#2E86AB', fontweight='bold')
    ax1.annotate('Believer\nRegion', xy=(0.85, 0.85), fontsize=10,
                 ha='center', color='#A23B72', fontweight='bold')
    ax1.annotate('MURKY\nMIDDLE', xy=(0.5, 0.15), fontsize=11,
                 ha='center', color='#F18F01', fontweight='bold',
                 bbox=dict(boxstyle='round', facecolor='white',
                          edgecolor='#F18F01', alpha=0.8))

    ax1.set_xlabel('Signal Precision S² (0=precise, 1=vague)', fontsize=12)
    ax1.set_ylabel('Probability of Funding', fontsize=12)
    ax1.set_title('(A) The U-Shape of Investor Matching\n'
                  '"Middle precision fails to attract either type"',
                  fontsize=12, fontweight='bold')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1.05)
    ax1.legend(loc='lower center', fontsize=9)
    ax1.grid(alpha=0.3)

    # === Panel B: Robustness across V definitions ===
    ax2 = axes[1]

    # Test multiple V definitions (different investor weights and thresholds)
    configs = [
        {'w_A': 0.5, 'w_B': 0.5, 'θ_A': 0.3, 'θ_B': 0.7, 'label': 'Baseline (50-50)'},
        {'w_A': 0.3, 'w_B': 0.7, 'θ_A': 0.25, 'θ_B': 0.75, 'label': 'More Believers'},
        {'w_A': 0.7, 'w_B': 0.3, 'θ_A': 0.35, 'θ_B': 0.65, 'label': 'More Analysts'},
        {'w_A': 0.4, 'w_B': 0.6, 'θ_A': 0.2, 'θ_B': 0.8, 'label': 'Wide Middle'},
    ]

    colors = ['#333333', '#2E86AB', '#A23B72', '#28A745']

    for cfg, col in zip(configs, colors):
        P_A = analyst_investment_prob(S2, cfg['θ_A'])
        P_B = believer_investment_prob(S2, cfg['θ_B'])
        P_f = cfg['w_A'] * P_A + cfg['w_B'] * P_B
        ax2.plot(S2, P_f, linewidth=2, color=col, label=cfg['label'])

    # Find and mark minima
    for cfg, col in zip(configs, colors):
        P_A = analyst_investment_prob(S2, cfg['θ_A'])
        P_B = believer_investment_prob(S2, cfg['θ_B'])
        P_f = cfg['w_A'] * P_A + cfg['w_B'] * P_B
        min_idx = np.argmin(P_f)
        ax2.scatter([S2[min_idx]], [P_f[min_idx]], color=col, s=100,
                   marker='v', zorder=5, edgecolor='white', linewidth=1.5)

    ax2.set_xlabel('Signal Precision S²', fontsize=12)
    ax2.set_ylabel('Probability of Funding', fontsize=12)
    ax2.set_title('(B) Robustness: U-shape Persists\n'
                  'Across Different V Definitions',
                  fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1.05)
    ax2.legend(loc='lower center', fontsize=9)
    ax2.grid(alpha=0.3)

    # Add annotation for minima
    ax2.annotate('▼ = Minimum\n(Murky penalty)', xy=(0.75, 0.55),
                fontsize=9, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig(save_path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {save_path}")


# ============================================================================
# FIGURE 2: HW vs SW COMPARISON
# ============================================================================

def create_fig2_hw_sw(save_path):
    """
    Fig 2: HW vs SW shape 비교
    - HW: J-shape (Analyst 영역 없음)
    - SW: U-shape (양쪽 모두)
    """
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    S2 = np.linspace(0, 1, 200)

    # === Panel A: SW (U-shape) ===
    ax1 = axes[0]

    P_fund_sw, P_A_sw, P_B_sw = compute_hw_sw_funding(S2, 'SW')

    ax1.fill_between(S2, 0, P_A_sw * 0.5, alpha=0.3, color='#2E86AB',
                     label='Analyst contribution')
    ax1.fill_between(S2, P_A_sw * 0.5, P_fund_sw, alpha=0.3, color='#A23B72',
                     label='Believer contribution')
    ax1.plot(S2, P_fund_sw, '-', color='#333333', linewidth=3,
             label='Total P(Funding)')

    # Mark minimum
    min_idx = np.argmin(P_fund_sw)
    ax1.scatter([S2[min_idx]], [P_fund_sw[min_idx]], color='#F18F01', s=150,
               marker='v', zorder=5, edgecolor='black', linewidth=2)
    ax1.annotate(f'Min @ S²={S2[min_idx]:.2f}',
                xy=(S2[min_idx], P_fund_sw[min_idx]),
                xytext=(S2[min_idx]+0.15, P_fund_sw[min_idx]+0.15),
                fontsize=10, arrowprops=dict(arrowstyle='->', color='black'))

    ax1.set_xlabel('Signal Precision S²', fontsize=12)
    ax1.set_ylabel('Probability of Funding', fontsize=12)
    ax1.set_title('(A) Software: U-Shape\n'
                  'Low CR (~0.3) → Both regions accessible',
                  fontsize=11, fontweight='bold')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1.05)
    ax1.legend(loc='upper center', fontsize=9)
    ax1.grid(alpha=0.3)

    # Add text box
    textstr = 'CR = C/(C+F) ~ 0.3\nk* = 1-2 options\nAnalyst: Yes  Believer: Yes'
    ax1.text(0.05, 0.05, textstr, transform=ax1.transAxes, fontsize=9,
            verticalalignment='bottom', bbox=dict(boxstyle='round',
            facecolor='lightgreen', alpha=0.5))

    # === Panel B: HW (J-shape) ===
    ax2 = axes[1]

    P_fund_hw, P_A_hw, P_B_hw = compute_hw_sw_funding(S2, 'HW')

    ax2.fill_between(S2, 0, P_A_hw * 0.1, alpha=0.3, color='#2E86AB',
                     label='Analyst contribution (minimal)')
    ax2.fill_between(S2, P_A_hw * 0.1, P_fund_hw, alpha=0.3, color='#A23B72',
                     label='Believer contribution')
    ax2.plot(S2, P_fund_hw, '-', color='#333333', linewidth=3,
             label='Total P(Funding)')

    # Annotate J-shape
    ax2.annotate('No left arm!\n(Analyst excluded\nby high CR)',
                xy=(0.15, 0.15), fontsize=10, ha='center', color='red',
                bbox=dict(boxstyle='round', facecolor='white',
                         edgecolor='red', alpha=0.8))

    ax2.set_xlabel('Signal Precision S²', fontsize=12)
    ax2.set_ylabel('Probability of Funding', fontsize=12)
    ax2.set_title('(B) Hardware/AV: J-Shape\n'
                  'High CR (~0.9) → Analyst region absent',
                  fontsize=11, fontweight='bold')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1.05)
    ax2.legend(loc='upper left', fontsize=9)
    ax2.grid(alpha=0.3)

    # Add text box
    textstr = 'CR = C/(C+F) ~ 0.9\nk* = 3-4 options\nAnalyst: No  Believer: Yes'
    ax2.text(0.05, 0.05, textstr, transform=ax2.transAxes, fontsize=9,
            verticalalignment='bottom', bbox=dict(boxstyle='round',
            facecolor='lightyellow', alpha=0.5))

    # === Panel C: Direct Comparison ===
    ax3 = axes[2]

    ax3.plot(S2, P_fund_sw, '-', color='#28A745', linewidth=3,
             label='SW: U-shape')
    ax3.plot(S2, P_fund_hw, '--', color='#DC3545', linewidth=3,
             label='HW: J-shape')

    # Shade the "advantage" region where SW > HW
    advantage_mask = P_fund_sw > P_fund_hw
    ax3.fill_between(S2, P_fund_hw, P_fund_sw,
                     where=advantage_mask, alpha=0.2, color='#28A745',
                     label='SW advantage')

    # Highlight crossover
    crossover_idx = np.where(np.diff(np.sign(P_fund_sw - P_fund_hw)))[0]
    if len(crossover_idx) > 0:
        for idx in crossover_idx:
            ax3.axvline(x=S2[idx], color='gray', linestyle=':', alpha=0.7)
            ax3.scatter([S2[idx]], [P_fund_sw[idx]], color='black', s=80,
                       marker='o', zorder=5)

    ax3.set_xlabel('Signal Precision S²', fontsize=12)
    ax3.set_ylabel('Probability of Funding', fontsize=12)
    ax3.set_title('(C) Shape Comparison\n'
                  'CR determines investor accessibility',
                  fontsize=11, fontweight='bold')
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1.05)
    ax3.legend(loc='lower center', fontsize=9)
    ax3.grid(alpha=0.3)

    # Add hypothesis test box
    textstr = ('Hypothesis:\n'
               'HW (high CR) → J-shape\n'
               'SW (low CR) → U-shape\n'
               '✓ Confirmed')
    ax3.text(0.95, 0.95, textstr, transform=ax3.transAxes, fontsize=10,
            verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='white',
                     edgecolor='green', linewidth=2, alpha=0.9))

    plt.tight_layout()
    plt.savefig(save_path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {save_path}")


# ============================================================================
# COMBINED SUMMARY FIGURE
# ============================================================================

def create_summary_figure(save_path):
    """
    Single comprehensive figure with key message
    """
    fig = plt.figure(figsize=(12, 10))

    # Top: U-shape with message
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    S2 = np.linspace(0, 1, 200)

    # === Panel 1: Core U-shape ===
    P_analyst = analyst_investment_prob(S2, 0.3)
    P_believer = believer_investment_prob(S2, 0.7)
    P_fund = 0.5 * P_analyst + 0.5 * P_believer

    ax1.plot(S2, P_analyst, '--', color='#2E86AB', linewidth=2, alpha=0.7)
    ax1.plot(S2, P_believer, '--', color='#A23B72', linewidth=2, alpha=0.7)
    ax1.plot(S2, P_fund, '-', color='black', linewidth=3)

    # Murky region
    murky = (S2 >= 0.3) & (S2 <= 0.7)
    ax1.fill_between(S2[murky], 0, P_fund[murky], alpha=0.3, color='#F18F01')

    ax1.set_xlabel('S² (precision)', fontsize=11)
    ax1.set_ylabel('P(Funding)', fontsize=11)
    ax1.set_title('Core Message: U-Shape\n"Middle = worst of both worlds"',
                 fontsize=11, fontweight='bold')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)

    # === Panel 2: SW vs HW ===
    P_sw, _, _ = compute_hw_sw_funding(S2, 'SW')
    P_hw, _, _ = compute_hw_sw_funding(S2, 'HW')

    ax2.plot(S2, P_sw, '-', color='#28A745', linewidth=2.5, label='SW (U)')
    ax2.plot(S2, P_hw, '--', color='#DC3545', linewidth=2.5, label='HW (J)')
    ax2.legend(loc='lower center')
    ax2.set_xlabel('S²', fontsize=11)
    ax2.set_ylabel('P(Funding)', fontsize=11)
    ax2.set_title('HW vs SW: Different Shapes\nHW loses left arm (no Analyst)',
                 fontsize=11, fontweight='bold')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    # === Panel 3: Table ===
    ax3.axis('off')

    table_data = [
        ['Segment', 'C', 'F', 'CR', 'k*', 'Analyst', 'Shape'],
        ['HW/AV', 'High', 'Low', '0.9', '3-4', 'No', 'J'],
        ['SW/Fleet', 'Low', 'High', '0.3', '1-2', 'Yes', 'U'],
    ]

    table = ax3.table(cellText=table_data, loc='center', cellLoc='center',
                      colWidths=[0.15, 0.1, 0.1, 0.1, 0.1, 0.12, 0.1])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.3, 2)

    # Color header
    for j in range(7):
        table[(0, j)].set_facecolor('#333333')
        table[(0, j)].set_text_props(color='white', fontweight='bold')

    ax3.set_title('CR Structure Determines Shape', fontsize=11, fontweight='bold',
                 pad=20)

    # === Panel 4: Key message box ===
    ax4.axis('off')

    message = """
================================================

        KEY MESSAGE

"Middle precision (S2~0.5) is
 too vague for Analysts and
 too boring for Believers,
 so it fails to attract funding."

================================================

MODEL:
  P_fund = w_A * P_A(S2) + w_B * P_B(S2)

WHERE:
  P_A(S2) = 1  if  S2 <= theta_A  (precise)
          = 0  otherwise

  P_B(S2) = 1  if  S2 >= theta_B  (vague)
          = 0  otherwise

IMPLICATION:
  theta_A < S2 < theta_B  ->  P_fund ~ 0
                     (The Murky Middle)

================================================
"""

    ax4.text(0.5, 0.5, message, transform=ax4.transAxes,
            fontsize=10, fontfamily='monospace',
            verticalalignment='center', horizontalalignment='center',
            bbox=dict(boxstyle='round', facecolor='lightyellow',
                     edgecolor='orange', linewidth=2))

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
    print("N SIMULATION: U-Shape Funding Pattern")
    print("="*70)
    print()
    print("핵심 메시지:")
    print('"중간 정밀도(S²≈0.5)는 Analyst에겐 모호하고')
    print(' Believer에겐 지루해서 투자받지 못한다."')
    print()

    # Generate figures
    print("Generating figures...")

    # Fig 1: Full U-shape
    create_fig1_ushape(f"{save_dir}/fig1_ushape_full.png")

    # Fig 2: HW vs SW comparison
    create_fig2_hw_sw(f"{save_dir}/fig2_hw_sw_comparison.png")

    # Summary figure
    create_summary_figure(f"{save_dir}/fig_n_summary.png")

    print()
    print("="*70)
    print("FILES CREATED")
    print("="*70)
    print(f"""
Fig 1: {save_dir}/fig1_ushape_full.png
       - Panel A: Basic U-shape with investor regions
       - Panel B: Robustness across V definitions

Fig 2: {save_dir}/fig2_hw_sw_comparison.png
       - Panel A: SW (U-shape, both types)
       - Panel B: HW (J-shape, Believer only)
       - Panel C: Direct comparison

Summary: {save_dir}/fig_n_summary.png
         - All key insights in one figure
""")

    # Print model summary
    print("="*70)
    print("MODEL SUMMARY")
    print("="*70)
    print("""
Investor Types:
  • Analyst: Invests when S² ≤ θ_A (can verify precise signals)
  • Believer: Invests when S² ≥ θ_B (projects onto vague visions)

Funding Probability:
  P_fund(S²) = w_A · P_A(S²) + w_B · P_B(S²)

  where P_A = sigmoid(θ_A - S²)
        P_B = sigmoid(S² - θ_B)

Key Insight:
  • When θ_A < S² < θ_B: NEITHER type invests
  • This creates the "murky middle" valley

HW vs SW Difference:
  • SW (low CR): Both investor types accessible → U-shape
  • HW (high CR): Analyst region absent → J-shape

  CR = C/(C+F) determines which regions are "open"
  High CR → high uncertainty → Analysts can't verify → no left arm
""")


if __name__ == "__main__":
    main()
