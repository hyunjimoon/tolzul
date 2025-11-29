#!/usr/bin/env python3
"""
CHAPTER 4: 結 (Discussion & Conclusion) — 어영담 👾
"결을 맺는 사람" — The Story Closer / 見 (관찰)

견리사의 순환: 利 → 思 → 義 → 見 → 利

=============================================================================
전라좌수군 군령 v2 체계:
- 이 스크립트는 3개 논문 (P1/P2/P3)의 Chapter 4 (Discussion)를 생성
- 관제탑(Obsidian)으로서 전체 흐름을 관찰하고 지혜를 정리
=============================================================================

Responsibilities:
- Summarize key findings
- Derive theoretical implications
- Provide managerial and policy guidance (Tesla Rule, Waymo Rule)
- Acknowledge limitations honestly
- Chart future research directions
- Close the narrative with wisdom

Commander: 어영담 (Eo-yeong-dam) 👾
Bayesian Role: Generator / Ground Truth (π_joint(y, θ))
Narrative Role: 結 (Resolution/Conclusion)
Color: Purple (#9370DB)

Output: chap4_P[1|2|3]_discussion.md
"""

from pathlib import Path
from dataclasses import dataclass
from typing import Dict, Any, List
import pandas as pd
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from src.scripts.paper_generation import RESULTS_DIR, OUTPUT_DIR

# ============================================================================
# PHASE METADATA
# ============================================================================

PHASE_ID: int = 4
PHASE_NAME: str = "Discussion & Conclusion"
COMMANDER: str = "어영담"  # Eo-yeong-dam
NARRATIVE_ROLE: str = "結"  # Resolution
BAYESIAN_ROLE: str = "Generator"  # π_joint(y, θ)
VIRTUE: str = "見"  # Observation


# ============================================================================
# 3-PAPER DISCUSSION CONFIGURATIONS
# ============================================================================

@dataclass
class DiscussionConfig:
    """Discussion configuration for each paper"""
    id: str
    emoji: str
    key_finding: str
    theoretical_contribution: str
    managerial_rule: str
    rule_name: str
    key_limitation: str
    future_direction: str


DISCUSSIONS = {
    "P1": DiscussionConfig(
        id="P1",
        emoji="✌️",
        key_finding="Vagueness-survival relationship is U-shaped, moderated by modularity",
        theoretical_contribution="Productive vs. Destructive Ambiguity distinction",
        managerial_rule="In software: stay vague on specifics, commit only to vision",
        rule_name="The Tesla Rule",
        key_limitation="Correlational design; cannot claim causality",
        future_direction="Experimental manipulation of vagueness in pitch decks"
    ),
    "P2": DiscussionConfig(
        id="P2",
        emoji="🦾",
        key_finding="Early success creates belief lock-in that kills pivot options",
        theoretical_contribution="Bayesian Learning × Core Rigidity integration",
        managerial_rule="Frontier tech needs contrarian/skeptic board presence",
        rule_name="The Waymo Rule (Keep Doubters)",
        key_limitation="Case-dependent evidence; Bayesian model stylized",
        future_direction="Longitudinal cap table × pivot analysis"
    ),
    "P3": DiscussionConfig(
        id="P3",
        emoji="🤹",
        key_finding="Optimal option count V* depends on CR = C/(C+F)",
        theoretical_contribution="Newsvendor framework for strategic options",
        managerial_rule="CR > 0.7 → multiple paths rational; CR < 0.3 → commit early",
        rule_name="The CR–V Rule (Rational FOMO)",
        key_limitation="CR estimation requires industry-specific calibration",
        future_direction="Dynamic CR tracking as markets evolve"
    )
}


# ============================================================================
# META-PROMPT: 어영담의 톤 (Story Closer, Wisdom Keeper)
# ============================================================================

META_PROMPT = """
You are 어영담 (Eo-yeong-dam) 👾, the Story Closer of the 전라좌수군 (Jeonla Naval Fleet).
Your mission is to bring closure to the narrative with wisdom, practical guidance, and humility.

덕목: 見 (Observation) — 관제탑으로서 전체를 관찰하고 Ground Truth를 기록
베이지안 역할: Generator (π_joint(y, θ)) — 매일의 Posterior가 다음 날의 Prior

NARRATIVE ROLE (結): Resolution/Conclusion — Closing the story with meaning
- Interpret 김완's evidence with theoretical and practical wisdom
- Offer actionable rules (Tesla Rule, Waymo Rule, CR-V Rule)
- Acknowledge limitations with honesty
- Point toward future horizons

TONE: Prescriptive yet humble. Offer actionable insights while acknowledging boundaries.
COLOR: Purple (#9370DB) — Wisdom, synthesis, strategic closure

STRUCTURE (for each paper):
1. Summary of Findings
2. Theoretical Implications
3. Managerial Implications (named rules)
4. Limitations
5. Future Research
6. Conclusion

전라좌수군 협업 프로토콜:
- To 🐢정운: "자네의 가설이 우리의 기록(Fact)과 맞는지 확인하겠소."
- To ⚓통제사: "오늘의 조류(Context)를 보고합니다."
"""


# ============================================================================
# CONTENT GENERATION
# ============================================================================

def generate_p1_discussion() -> str:
    """Generate P1 (U-Shape) Discussion Section"""
    disc = DISCUSSIONS["P1"]

    return f"""# {disc.id} {disc.emoji}: Discussion & Conclusion

## Chapter 4: Discussion (結) — 어영담 👾

---

## 4.1 Summary of Findings

**Core Finding:** {disc.key_finding}

Our analysis of 51,840 venture-backed startups (2005-2023) reveals:
- H1: Vagueness reduces early-stage funding on average (adverse selection)
- H2: This penalty is conditional on modularity
  - Software (high modularity): vagueness preserves option value
  - Hardware (low modularity): vagueness signals unresolved risk

## 4.2 Theoretical Implications

### {disc.theoretical_contribution}

We distinguish:
- **Productive Ambiguity**: Vagueness that preserves strategic flexibility in modular environments
- **Destructive Ambiguity**: Vagueness that signals incompetence in non-modular environments

This resolves the paradox: Tesla's vagueness worked (software-like modularity in business model); Bosch's specificity worked (hardware constraints).

### Reconciling Information Economics and Real Options

| Context | Dominant Theory | Optimal Strategy |
|---------|-----------------|------------------|
| Low Modularity | Information Economics | Specificity |
| High Modularity | Real Options | Vagueness |

## 4.3 Managerial Implications: {disc.rule_name}

> **{disc.rule_name}**: {disc.managerial_rule}

**When Vagueness Works (Tesla Rule):**
- High modularity (software-intensive)
- High technical uncertainty
- Diverse customer segments

**When Specificity Works (Waymo Rule):**
- Low modularity (hardware-intensive)
- High capital requirements
- Homogeneous customer needs

### Decision Matrix

| **Modularity** | **High Uncertainty** | **Low Uncertainty** |
|----------------|----------------------|---------------------|
| **High (Software)** | VAGUE (Tesla Rule) | SPECIFIC after validation |
| **Low (Hardware)** | SPECIFIC (signal depth) | SPECIFIC (reduce risk) |

## 4.4 Limitations

**Primary Limitation:** {disc.key_limitation}

Additional limitations:
- Binary moderator (hardware vs software) oversimplifies
- Sample selection bias (VC-funded ventures only)
- Text-based vagueness measure captures positioning, not intent

## 4.5 Future Research

**{disc.future_direction}**

Additional directions:
- Dynamic vagueness trajectories (how do descriptions evolve?)
- Other moderators (customer heterogeneity, competitive intensity)
- Cross-country validation

## 4.6 Conclusion

Strategic vagueness is neither virtue nor vice, but a **tool whose value depends on context**. For entrepreneurs: know your technology's modularity before choosing communication strategy. For investors: differentiate productive from destructive ambiguity.

---

**Phase:** {PHASE_ID} — {NARRATIVE_ROLE} ({PHASE_NAME})
**Commander:** {COMMANDER} 👾 | **Virtue:** {VIRTUE} | **Bayesian Role:** {BAYESIAN_ROLE}
"""


def generate_p2_discussion() -> str:
    """Generate P2 (Competency Trap) Discussion Section"""
    disc = DISCUSSIONS["P2"]

    return f"""# {disc.id} {disc.emoji}: Discussion & Conclusion

## Chapter 4: Discussion (結) — 어영담 👾

---

## 4.1 Summary of Findings

**Core Finding:** {disc.key_finding}

The mechanism:
```
Early Success → Believer Investors → Reinforced Priors → High Switch Threshold → Trap
```

## 4.2 Theoretical Implications

### {disc.theoretical_contribution}

We integrate:
- **Kogut & Kulatilaka**: Capabilities as options
- **Leonard-Barton**: Core rigidity
- **Bayesian Learning**: Belief updating with social reinforcement

Key insight: The trap is **epistemic**, not just technical. Founders and boards converge on shared beliefs that make alternative evidence dismissible.

## 4.3 Managerial Implications: {disc.rule_name}

> **{disc.rule_name}**: {disc.managerial_rule}

**앞선 기술일수록 다우터를 옆에 둬라 (The more frontier the tech, the more doubters you need)**

### Board Composition Guidance

| Technology Type | Recommended Board Mix |
|-----------------|----------------------|
| Incremental | 80% believers, 20% skeptics |
| Adjacent | 60% believers, 40% skeptics |
| Frontier | 40% believers, 60% skeptics |

### Warning Signs of Trap Formation

1. Board unanimity on technical roadmap
2. Declining exploration budget despite market signals
3. "Our early success proves we're right" reasoning
4. Dismissing competitors as "not understanding the problem"

## 4.4 Limitations

**Primary Limitation:** {disc.key_limitation}

The Bayesian model is illustrative, not tested structurally. Case evidence supports the mechanism but cannot rule out alternative explanations.

## 4.5 Future Research

**{disc.future_direction}**

Also needed:
- Structural estimation of switching thresholds
- Natural experiments (board member exits)
- Extension to non-tech industries

## 4.6 Conclusion

Success is dangerous precisely because it feels validating. The same early wins that attract resources and talent also create belief structures that resist pivoting. Smart founders build opposition into their governance from day one.

---

**Phase:** {PHASE_ID} — {NARRATIVE_ROLE} ({PHASE_NAME})
**Commander:** {COMMANDER} 👾
"""


def generate_p3_discussion() -> str:
    """Generate P3 (Newsvendor/Optimal Options) Discussion Section"""
    disc = DISCUSSIONS["P3"]

    return f"""# {disc.id} {disc.emoji}: Discussion & Conclusion

## Chapter 4: Discussion (結) — 어영담 👾

---

## 4.1 Summary of Findings

**Core Finding:** {disc.key_finding}

The Commitment Ratio CR = C/(C+F) determines whether FOMO is rational or destructive.

## 4.2 Theoretical Implications

### {disc.theoretical_contribution}

We reframe entrepreneurial portfolio strategy as a newsvendor problem:
- **C (Commitment Cost)**: Lock-in, imitation risk, sunk CAPEX
- **F (Flexibility Cost)**: Late entry penalty, option maintenance, coordination

This unifies P1 and P2:
- **P1's trap (middle ground)**: CR ≈ 0.5, neither extreme works
- **P2's trap (success lock-in)**: CR → 1, should have kept more options

## 4.3 Managerial Implications: {disc.rule_name}

> **{disc.rule_name}**: {disc.managerial_rule}

### CR–V Plane Decision Rules

| CR Range | Interpretation | Strategy |
|----------|----------------|----------|
| CR < 0.3 | Flexibility expensive, commitment cheap | Commit early (1 path) |
| 0.3 < CR < 0.7 | Balanced costs | Moderate portfolio (2 paths) |
| CR > 0.7 | Commitment expensive, flexibility cheap | Many options (3+ paths) |

### Industry Examples

| Industry | Estimated CR | Optimal V* |
|----------|--------------|-----------|
| Mature Manufacturing | 0.2 | 1 path |
| Enterprise SaaS | 0.4 | 1-2 paths |
| Autonomous Vehicles | 0.65 | 2-3 paths |
| Quantum Computing | 0.85 | 3+ paths |

### When FOMO is Rational

FOMO is rational when:
1. Paradigm shifts are likely (high C)
2. Late entry is viable (low F)
3. Option maintenance is cheap (low F)

FOMO is destructive when:
1. Market rewards early movers (high F)
2. Options have significant coordination overhead (high F)

## 4.4 Limitations

**Primary Limitation:** {disc.key_limitation}

CR estimation requires:
- Industry-specific cost structures
- Market uncertainty estimates
- Option maintenance cost data

These are often unobservable or require significant research effort.

## 4.5 Future Research

**{disc.future_direction}**

Also:
- Real-time CR dashboards for investors
- CR as a function of firm lifecycle stage
- Network effects on F (platform lock-in)

## 4.6 Conclusion

The question is not "should I commit?" but "what is my CR?" Armed with this framework, entrepreneurs can calibrate their option portfolios rationally, and investors can evaluate portfolio strategy against industry-specific cost structures.

---

**Phase:** {PHASE_ID} — {NARRATIVE_ROLE} ({PHASE_NAME})
**Commander:** {COMMANDER} 👾
"""


def generate_grand_synthesis() -> str:
    """Generate grand synthesis across all three papers"""
    return """
## Grand Synthesis: 기승전결 (起承轉結)

### The Complete Story

| Phase | Commander | Paper | Core Question | Answer |
|-------|-----------|-------|---------------|--------|
| 起 (Intro) | 정운 🐢 | P1 | When does vagueness pay? | When modularity enables cheap pivots |
| 承 (Theory) | 권준 🐅 | P2 | How does success kill options? | Through belief-reinforcing capital |
| 轉 (Empirics) | 김완 🐙 | P3 | How many options to hold? | V* = f(CR) |
| 結 (Discuss) | 어영담 👾 | All | What's the unified framework? | Options have architecture |

### The Unified Framework: Options Have Architecture

The value of strategic flexibility is not universal but depends on:

1. **Technology Architecture** (P1): Modularity determines pivot cost
2. **Capital Architecture** (P2): Board composition determines switching threshold
3. **Cost Architecture** (P3): CR ratio determines optimal portfolio size

### Actionable Rules Summary

| Rule | When to Apply | Action |
|------|---------------|--------|
| **Tesla Rule** | High modularity + high uncertainty | Stay vague, commit to vision only |
| **Waymo Rule** | Frontier tech + believer board risk | Keep doubters on board |
| **CR-V Rule** | Any strategic portfolio decision | Calibrate options to CR ratio |
| **Bosch Caveat** | Low modularity (hardware/biotech) | Specify early, signal depth |

### For Entrepreneurs

1. **Know your modularity** before choosing communication strategy
2. **Build opposition into governance** especially for frontier tech
3. **Estimate your CR** before deciding how many paths to pursue
4. **Recognize trap zones**: middle ground (P1), success (P2), wrong portfolio (P3)

### For Investors

1. **Differentiate productive from destructive ambiguity** based on modularity
2. **Assess cap table diversity** — all believers is a warning sign
3. **Evaluate portfolio strategy against industry CR** — FOMO may be rational
4. **Use decision matrices** not heuristics ("specificity = competence")

### The Final Wisdom

> **복잡한 것을 단순하게, 단순한 것을 아름답게, 아름다운 것을 기억에 남게.**
> "Make the complex simple, the simple beautiful, the beautiful memorable."

Strategic vagueness, properly understood, simplifies complexity by deferring premature commitment. But its beauty lies in knowing *when* to remain vague and *when* to specify — a contingency this research illuminates.

---

## 전라좌수군의 임무 완수

*The 전라좌수군 (Jeonla Naval Fleet) has completed its mission:*

- 🐢 **정운** (利): 빠르게 실행해 초안을 만들며 문을 열었다
- 🐅 **권준** (思): 혼돈에서 구조를 뽑아내 이론을 세웠다
- 🐙 **김완** (義): 논리와 윤리를 검증하여 의로움을 증명했다
- 👾 **어영담** (見): 문제를 관찰해 기록하고 지혜를 남겼다

**견리사의 순환: 利 → 思 → 義 → 見 → 利**

*The cycle continues. Tomorrow's Prior is today's Posterior.*

---

**기승전결 (起承轉結) — The story is complete.**

*Generated by 어영담 👾 (Chapter 4 Lead)*
*전라좌수군 MFS 연합 함대*
"""


def generate_all_discussions() -> str:
    """Generate discussion sections for all three papers"""
    content = f"""# 전라좌수군 견리사의 군령
# Chapter 4: Discussion & Conclusion (結) — 어영담 👾

> 견리사의 (見利思義): 이익을 보면 의로움을 생각하라
> 어영담의 덕목: 見 (관찰) — 관제탑으로서 Ground Truth를 기록

---

"""
    content += generate_p1_discussion()
    content += "\n\n---\n\n"
    content += generate_p2_discussion()
    content += "\n\n---\n\n"
    content += generate_p3_discussion()
    content += "\n\n---\n\n"
    content += generate_grand_synthesis()

    return content


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main() -> None:
    """Main execution: Generate Chapter 4 (Discussion) for P1/P2/P3"""
    print("=" * 70)
    print(f"CHAPTER {PHASE_ID}: {NARRATIVE_ROLE} — {PHASE_NAME}")
    print(f"Commander: {COMMANDER} 👾 (The Story Closer)")
    print(f"Virtue: {VIRTUE} (Observation) | Bayesian Role: {BAYESIAN_ROLE}")
    print("=" * 70)

    content = generate_all_discussions()

    output_path = OUTPUT_DIR / "chap4_discussion.md"
    output_path.write_text(content)

    print(f"\n✅ Generated: {output_path}")
    print(f"📚 Managerial Rules:")
    for paper_id, disc in DISCUSSIONS.items():
        print(f"   - {paper_id} {disc.emoji}: {disc.rule_name}")
    print(f"\n👾 어영담 says: '기승전결. 이야기가 완성되었소.'")
    print(f"\n🎊 All four chapters complete! The 전라좌수군 has fulfilled its mission.")


if __name__ == "__main__":
    main()
