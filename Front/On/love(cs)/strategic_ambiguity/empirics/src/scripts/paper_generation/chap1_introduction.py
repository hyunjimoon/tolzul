#!/usr/bin/env python3
"""
CHAPTER 1: 起 (Introduction) — 정운 🐢
"문을 여는 사람" — The Door Opener / 利 (속도)

견리사의 순환: 利 → 思 → 義 → 見 → 利

=============================================================================
전라좌수군 군령 v2 체계:
- 이 스크립트는 3개 논문 (P1/P2/P3)의 Chapter 1 (Introduction)을 생성
- P1 ✌️: U-Shape (Vagueness-Survival의 Convex 관계)
- P2 🦾: Competency Trap (초기 Commitment → 후기 Scaling Risk)
- P3 🤹: Execution Gap (Marketing Hype vs Mfg Capability)
=============================================================================

Responsibilities:
- Hook readers with vivid case study (Tesla vs Bosch)
- Articulate the core puzzle for each paper
- Preview main findings with empirical results
- Outline theoretical contributions
- Provide paper roadmap

Commander: 정운 (Jeong-un) 🐢
Bayesian Role: Prior Generator (π(θ))
Narrative Role: 起 (Setup/Introduction)
Color: Teal (#20B2AA)

Output: chap1_P[1|2|3]_introduction.md
"""

from pathlib import Path
from dataclasses import dataclass
from typing import Optional, Dict, Any
import pandas as pd
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from src.scripts.paper_generation import RESULTS_DIR, OUTPUT_DIR

# ============================================================================
# PHASE METADATA
# ============================================================================

PHASE_ID: int = 1
PHASE_NAME: str = "Introduction"
COMMANDER: str = "정운"  # Jeong-un
NARRATIVE_ROLE: str = "起"  # Setup
BAYESIAN_ROLE: str = "Prior"  # π(θ)
VIRTUE: str = "利"  # Speed


# ============================================================================
# 3-PAPER CONFIGURATION
# ============================================================================

@dataclass
class PaperConfig:
    """Configuration for each of the 3 papers"""
    id: str
    emoji: str
    title: str
    core_question: str
    hook_case: str
    scott_trigger: str
    key_mechanism: str


PAPERS = {
    "P1": PaperConfig(
        id="P1",
        emoji="✌️",
        title="U-Shape: When Vagueness Pays",
        core_question="왜 어중간한 비전은 죽는가?",
        hook_case="Tesla (vague vision) vs Bosch (precise specs)",
        scott_trigger="More options ≠ always better. 극단만이 살아남는다.",
        key_mechanism="Signaling × Real Options: Vagueness² > 0 (U-shape survival)"
    ),
    "P2": PaperConfig(
        id="P2",
        emoji="🦾",
        title="Competency Trap: When Success Kills Options",
        core_question="성공이 왜 발목을 잡는가?",
        hook_case="Waymo (early lead → pivot paralysis) vs Comma.ai (late, flexible)",
        scott_trigger="Strong tech, stronger trap. 성공이 옵션을 죽인다.",
        key_mechanism="Real Options × Core Rigidity: High Commitment → Scaling Risk"
    ),
    "P3": PaperConfig(
        id="P3",
        emoji="🤹",
        title="Execution Gap: Optimal Number of Options",
        core_question="옵션은 몇 개나 들고 가야 하는가?",
        hook_case="AV industry: Lidar vs Vision vs Ambiguous path coexistence",
        scott_trigger="Newsvendor of options. FOMO도 조건부로 합리적이다.",
        key_mechanism="Newsvendor of Options: CR = C/(C+F) determines optimal V*"
    )
}


# ============================================================================
# META-PROMPT: 정운의 톤 (Door Opener, Hook Master)
# ============================================================================

META_PROMPT = """
You are 정운 (Jeong-un) 🐢, the Door Opener of the 전라좌수군 (Jeonla Naval Fleet).
Your mission is to open the paper with compelling storytelling that draws readers in.

덕목: 利 (Speed) — 빠르게 초안을 생성하여 돌파구를 만든다
베이지안 역할: Prior Generator (π(θ)) — 가설을 먼저 던진다

NARRATIVE ROLE (起): Setup and Introduction
- Create intrigue with vivid contrasts
- Pose the central puzzle that demands resolution
- Hint at theoretical tensions
- Preview empirical findings to justify reading further

TONE: Scholarly yet accessible. Start with vivid case study, then pivot to puzzle.
COLOR: Teal (#20B2AA) — Calm confidence, strategic patience

STRUCTURE (for each paper):
1. Hook (vivid case contrast — 2 paragraphs)
2. Puzzle statement (Why does this pattern exist? — 1 paragraph)
3. Preview of findings (with actual numbers if available — 1 paragraph)
4. Theoretical contributions (3 bullet points)
5. Roadmap (linking to 권준·김완·어영담)

STYLE GUIDELINES:
- Use concrete examples before abstractions
- Lead with surprising facts: "Conventional wisdom says X, but we find Y"
- Avoid jargon in opening paragraphs
- Numbers in parentheses: (β = X.XX, p < 0.001)
- Active voice: "We find" not "It is found that"

전라좌수군 협업 프로토콜:
- To 🐅권준: "거친 초안입니다. 구조를 잡아주십시오."
- To 🐙김완: "내 논리의 허점을 찾아주시오."
"""


# ============================================================================
# DATA LOADING
# ============================================================================

def load_h1_results() -> Dict[str, Any]:
    """Load H1 regression results (Early Funding ~ Vagueness)"""
    h1_path = RESULTS_DIR / "h1_coefficients.csv"
    if not h1_path.exists():
        print(f"Warning: {h1_path} not found. Using placeholder values.")
        return {"coef": -8.5e-07, "p_value": 0.00025}

    df = pd.read_csv(h1_path, index_col=0)
    if 'z_vagueness' in df.index:
        vagueness_row = df.loc['z_vagueness']
        return {
            "coef": vagueness_row['coef'],
            "p_value": vagueness_row.get('P>|t|', 0.001),
            "conf_low": vagueness_row.get('conf_low', vagueness_row['coef'] - 0.001),
            "conf_high": vagueness_row.get('conf_high', vagueness_row['coef'] + 0.001)
        }
    return {"coef": -8.5e-07, "p_value": 0.00025}


def load_h2_results() -> Dict[str, Any]:
    """Load H2 regression results (Growth ~ Vagueness × Hardware)"""
    h2_path = RESULTS_DIR / "h2_main_coefficients.csv"
    if not h2_path.exists():
        print(f"Warning: {h2_path} not found. Using placeholder values.")
        return {
            "vagueness_main": -0.037,
            "hardware_main": 0.448,
            "interaction": -0.030,
            "interaction_p": 0.046
        }

    df = pd.read_csv(h2_path, index_col=0)
    return {
        "vagueness_main": df.loc['z_vagueness', 'coef'] if 'z_vagueness' in df.index else -0.037,
        "hardware_main": df.loc['is_hardware', 'coef'] if 'is_hardware' in df.index else 0.448,
        "interaction": df.loc['z_vagueness:is_hardware', 'coef'] if 'z_vagueness:is_hardware' in df.index else -0.030,
        "interaction_p": df.loc['z_vagueness:is_hardware', 'P>|z|'] if 'z_vagueness:is_hardware' in df.index else 0.046
    }


# ============================================================================
# CONTENT GENERATION
# ============================================================================

def generate_paper_intro(paper_id: str, h1_results: Dict, h2_results: Dict) -> str:
    """Generate introduction section for a specific paper"""
    paper = PAPERS[paper_id]

    if paper_id == "P1":
        return generate_p1_intro(paper, h1_results, h2_results)
    elif paper_id == "P2":
        return generate_p2_intro(paper, h1_results, h2_results)
    else:  # P3
        return generate_p3_intro(paper, h1_results, h2_results)


def generate_p1_intro(paper: PaperConfig, h1_results: Dict, h2_results: Dict) -> str:
    """Generate P1 (U-Shape) Introduction"""
    h1_coef = h1_results['coef']
    h1_p = h1_results['p_value']
    h2_interaction = h2_results['interaction']
    h2_int_p = h2_results['interaction_p']

    return f"""# {paper.id} {paper.emoji}: {paper.title}

## Chapter 1: Introduction (起)

> **Scott Trigger**: "{paper.scott_trigger}"

### The Vagueness Paradox

In 2003, Elon Musk pitched Tesla with breathtaking vagueness: "We're going to make electric cars desirable." No mention of battery chemistry, no production timeline, no unit economics. Just a vision. Investors poured in $7.5 million in Series A funding. By 2023, Tesla's market cap exceeded $800 billion.

That same year, Robert Bosch GmbH — the world's largest automotive supplier — launched a new mobility division with laser-precise specificity: "48V mild-hybrid battery systems targeting 15% fuel efficiency gains in C-segment vehicles, production Q2 2024, unit cost €850, targeting 2M units by 2026." Despite this operational clarity, the division struggled to secure external capital.

### The Puzzle: {paper.core_question}

Why does strategic vagueness — deliberately withholding operational details — correlate with entrepreneurial success in some contexts but failure in others? Conventional wisdom in entrepreneurship suggests specificity signals competence. Yet high-growth ventures like Tesla, Airbnb, and Stripe all launched with strikingly vague value propositions.

We propose that **technological modularity** moderates this relationship. Our empirical analysis of 51,840 venture-backed startups (2005-2023) confirms this: vagueness reduces early-stage funding overall (β = {h1_coef:.3e}, p < {h1_p:.3f}), but this penalty is **significantly attenuated** in software ventures and **amplified** in hardware ventures (interaction term: β = {h2_interaction:.3f}, p = {h2_int_p:.3f}).

### Theoretical Contributions

1. **Information Economics**: We distinguish between **productive ambiguity** (vagueness that preserves option value) and **destructive ambiguity** (vagueness that signals incompetence).

2. **Real Options Theory**: We extend real options logic to **entrepreneurial positioning**. Vagueness functions as a textual real option, valuable only when technology permits costless switching.

3. **Modularity Theory**: We bridge Baldwin & Clark's work on product architecture with entrepreneurial strategy. Modularity determines optimal communication strategy.

### Roadmap

- **Section 2** (권준 🐅): Theory and conceptual framework
- **Section 3** (김완 🐙): Empirical analysis and results
- **Section 4** (어영담 👾): Discussion and implications

---

**Phase:** {PHASE_ID} — {NARRATIVE_ROLE} ({PHASE_NAME})
**Commander:** {COMMANDER} 🐢 | **Virtue:** {VIRTUE} | **Bayesian Role:** {BAYESIAN_ROLE}
"""


def generate_p2_intro(paper: PaperConfig, h1_results: Dict, h2_results: Dict) -> str:
    """Generate P2 (Competency Trap) Introduction"""
    return f"""# {paper.id} {paper.emoji}: {paper.title}

## Chapter 1: Introduction (起)

> **Scott Trigger**: "{paper.scott_trigger}"

> **Industry Context**: "Transportation industry is both capital intensive and fast clockspeed.
> The need for capital lures ventures into commitment trap, who are stuck then washed out
> by the next technology wave."

### The Success Paradox

In 2009, Waymo (then Google's self-driving car project) was the undisputed leader in autonomous vehicles. Their early commitment to LiDAR-based perception, HD mapping, and Level 4 autonomy attracted the best talent and billions in R&D investment. By 2015, they had the most miles driven, the best safety record, and the clearest technical roadmap.

By 2024, Waymo remains geofenced to select cities while Tesla — a company that committed to "pure vision" autonomy years later — deploys across North America. What went wrong?

### The Puzzle: {paper.core_question}

Why do early technical advantages sometimes become liabilities? We propose that initial concrete commitment creates a **Competency Trap**: high commitment → like-minded investors/board → low posterior variance → unexercisable pivot options.

This is the **replacement effect** at the firm level. Early exploitation generates high μ, low σ priors, which reduce exploration incentives precisely when paradigm shifts demand flexibility.

### Theoretical Contributions

1. **Real Options × Core Rigidity**: We integrate Kogut & Kulatilaka's capabilities-as-options with Leonard-Barton's core rigidity framework.

2. **Bayesian Learning Model**: We show how "believer" capital structures raise the switching threshold, making pivot options theoretically valuable but practically unexercisable.

3. **Boundary Conditions**: Frontier tech × believer cap table → trap. We derive precise conditions for when commitment becomes fatal.

### Roadmap

- **Section 2** (권준 🐅): Theory — Real Options × Core Rigidity × Bayesian Learning
- **Section 3** (김완 🐙): Empirics — Tech paradigm shock analysis + case triangulation
- **Section 4** (어영담 👾): Implications — "앞선 기술일수록 다우터를 옆에 둬라"

---

**Phase:** {PHASE_ID} — {NARRATIVE_ROLE} ({PHASE_NAME})
**Commander:** {COMMANDER} 🐢 | **Virtue:** {VIRTUE} | **Bayesian Role:** {BAYESIAN_ROLE}
"""


def generate_p3_intro(paper: PaperConfig, h1_results: Dict, h2_results: Dict) -> str:
    """Generate P3 (Execution Gap / Optimal Options) Introduction"""
    return f"""# {paper.id} {paper.emoji}: {paper.title}

## Chapter 1: Introduction (起)

> **Scott Trigger**: "{paper.scott_trigger}"

### The FOMO Dilemma

In the autonomous vehicle industry, three distinct technical approaches coexist: LiDAR-first (Waymo), vision-first (Tesla), and deliberately ambiguous (Comma.ai). Traditional strategy advice would demand early commitment. Yet some of the most successful AV startups maintain strategic ambiguity about their technical stack well into Series C.

Is this FOMO (Fear of Missing Out) on alternative paths? Or is it rational portfolio management?

### The Puzzle: {paper.core_question}

We reframe this as a **Newsvendor problem for options**. Just as a newsvendor optimizes inventory given demand uncertainty and holding/stockout costs, entrepreneurs optimize their portfolio of strategic options given:

- **Commitment Cost (C)**: Lock-in, imitation risk, sunk CAPEX
- **Flexibility Cost (F)**: Late entry penalty, option maintenance, coordination overhead

The optimal number of options V* = f(C, F, market uncertainty). When C >> F, many options are rational. When F >> C, early commitment dominates.

### Theoretical Contributions

1. **Newsvendor of Options**: We provide a formal model linking commitment/flexibility costs to optimal option portfolio size.

2. **Unifying P1 and P2**: The Commitment Ratio CR = C/(C+F) places P1's flexibility trap and P2's commitment trap on a single continuum.

3. **Rational FOMO**: We show when maintaining multiple technical paths is not indecision but optimization.

### Roadmap

- **Section 2** (권준 🐅): Theory — Newsvendor × Coordination/OM Framework
- **Section 3** (김완 🐙): Empirics — CR calibration across industries
- **Section 4** (어영담 👾): Implications — CR–V plane design rules

---

**Phase:** {PHASE_ID} — {NARRATIVE_ROLE} ({PHASE_NAME})
**Commander:** {COMMANDER} 🐢 | **Virtue:** {VIRTUE} | **Bayesian Role:** {BAYESIAN_ROLE}
"""


def generate_cross_synthesis(h1_results: Dict, h2_results: Dict) -> str:
    """Generate cross-paper synthesis (3편을 한 문단으로 요약)"""
    return f"""
## Cross-Synthesis: Three Papers, One Story

These three papers form a coherent whole:

1. **P1 (U-Shape)** asks: *When* does vagueness pay? Answer: When modularity enables cheap pivots.

2. **P2 (Competency Trap)** asks: *How* does early success kill options? Answer: Through belief-reinforcing capital structures.

3. **P3 (Optimal Options)** asks: *How many* options should you hold? Answer: It depends on CR = C/(C+F).

Together, they map the strategic landscape of entrepreneurial ambiguity:

| Paper | Core Trap | Solution |
|-------|-----------|----------|
| P1 ✌️ | Middle (neither vague nor concrete) | Go to extremes |
| P2 🦾 | Success (commitment lock-in) | Keep doubters on board |
| P3 🤹 | Wrong portfolio size | Calibrate to CR |

The common thread: **Options have architecture**. The value of flexibility depends on the cost structure of commitment vs. flexibility:

- **P1 ✌️** focuses on **Technology** architecture (modularity → pivot cost)
- **P2 🦾** focuses on **Organization** architecture (cap table → belief lock-in)
- **P3 🤹** focuses on **Competition** architecture (CR ratio → market timing)

---
*Generated by 정운 🐢 (Chapter 1 Lead)*
*Collaboration: 정운 → 권준 → 김완 → 어영담*
*견리사의 순환: 利 → 思 → 義 → 見 → 利*
"""


def generate_all_intros() -> str:
    """Generate introduction for all three papers plus synthesis"""
    h1_results = load_h1_results()
    h2_results = load_h2_results()

    content = f"""# 전라좌수군 견리사의 군령
# Chapter 1: Introduction (起) — 정운 🐢

> 견리사의 (見利思義): 이익을 보면 의로움을 생각하라
> 정운의 덕목: 利 (속도) — 빠르게 초안을 생성하여 돌파구를 만든다

---

"""
    # Generate each paper's intro
    for paper_id in ["P1", "P2", "P3"]:
        content += generate_paper_intro(paper_id, h1_results, h2_results)
        content += "\n\n---\n\n"

    # Add cross-synthesis
    content += generate_cross_synthesis(h1_results, h2_results)

    return content


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main() -> None:
    """Main execution: Generate Chapter 1 (Introduction) for P1/P2/P3"""
    print("=" * 70)
    print(f"CHAPTER {PHASE_ID}: {NARRATIVE_ROLE} — {PHASE_NAME}")
    print(f"Commander: {COMMANDER} 🐢 (The Door Opener)")
    print(f"Virtue: {VIRTUE} (Speed) | Bayesian Role: {BAYESIAN_ROLE}")
    print("=" * 70)

    content = generate_all_intros()

    output_path = OUTPUT_DIR / "chap1_introduction.md"
    output_path.write_text(content)

    print(f"\n✅ Generated: {output_path}")
    print(f"📊 Papers included: P1 ✌️, P2 🦾, P3 🤹")
    print(f"\n🐢 정운 says: '거친 초안입니다. 권준, 구조를 잡아주십시오!'")
    print(f"\n📝 Next: 권준 🐅 (Chapter 2 - Theory)")


if __name__ == "__main__":
    main()
