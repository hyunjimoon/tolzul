#!/usr/bin/env python3
"""
CHAPTER 2: 承 (Theory & Conceptual Model) — 권준 🐅
"구조를 세우는 사람" — The Structure Builder / 思 (구조)

견리사의 순환: 利 → 思 → 義 → 見 → 利

=============================================================================
전라좌수군 군령 v2 체계:
- 이 스크립트는 3개 논문 (P1/P2/P3)의 Chapter 2 (Theory)를 생성
- P1 ✌️: Signaling × Real Options 통합
- P2 🦾: Real Options × Core Rigidity × Bayesian Learning
- P3 🤹: Newsvendor of Options × Coordination/OM
=============================================================================

Responsibilities:
- Review theoretical foundations
- Develop conceptual framework
- Formalize hypotheses
- Present descriptive statistics

Commander: 권준 (Kwon-jun) 🐅
Bayesian Role: Likelihood (π(y|θ))
Narrative Role: 承 (Development/Building)
Color: Orange (#FF8C00)

Output: chap2_P[1|2|3]_theory.md
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

PHASE_ID: int = 2
PHASE_NAME: str = "Theory & Conceptual Model"
COMMANDER: str = "권준"  # Kwon-jun
NARRATIVE_ROLE: str = "承"  # Development
BAYESIAN_ROLE: str = "Likelihood"  # π(y|θ)
VIRTUE: str = "思"  # Structure


# ============================================================================
# 3-PAPER THEORETICAL FOUNDATIONS
# ============================================================================

@dataclass
class TheoryConfig:
    """Theoretical configuration for each paper"""
    id: str
    emoji: str
    core_theory: str
    key_papers: List[str]
    hypotheses: List[str]
    key_variables: List[str]


THEORIES = {
    "P1": TheoryConfig(
        id="P1",
        emoji="✌️",
        core_theory="Signaling × Real Options",
        key_papers=[
            "Akerlof (1970) - Market for Lemons",
            "Spence (1973) - Signaling",
            "McGrath (1997) - Real Options",
            "Baldwin & Clark (2000) - Modularity",
            "Bafera & Kleinert - Vagueness Taxonomy"
        ],
        hypotheses=[
            "H1: Vagueness has U-shaped relationship with survival (V(1-V) coefficient > 0)",
            "H2: Modularity moderates: high modularity → vagueness positive",
            "H2a: Software ventures (high modularity): vagueness → positive",
            "H2b: Hardware ventures (low modularity): vagueness → negative"
        ],
        key_variables=["Vagueness Score (V)", "Survival/Funding", "Modularity (Hardware/Software)"]
    ),
    "P2": TheoryConfig(
        id="P2",
        emoji="🦾",
        core_theory="Real Options × Core Rigidity × Bayesian Learning",
        key_papers=[
            "Kogut & Kulatilaka (2001) - Capabilities as Options",
            "Leonard-Barton (1992) - Core Rigidity",
            "Gans et al. - Choice-based S-curve",
            "Henderson & Clark - Architectural Innovation"
        ],
        hypotheses=[
            "H1: High initial commitment → reduced pivot probability",
            "H2: Like-minded investor composition → higher switching threshold",
            "H3: Technology paradigm shift amplifies commitment penalty"
        ],
        key_variables=["Commitment Level", "Cap Table Composition", "Switching Cost (C)", "Paradigm Shift Indicator"]
    ),
    "P3": TheoryConfig(
        id="P3",
        emoji="🤹",
        core_theory="Newsvendor of Options × Coordination",
        key_papers=[
            "Crowston & Fine - Dependency/Processification",
            "Fine (1998) - Clockspeed",
            "Van Mieghem - Operations Strategy",
            "Baldwin & Clark (2000) - Design Rules"
        ],
        hypotheses=[
            "H1: Optimal option number V* = f(C, F, σ_market)",
            "H2: CR = C/(C+F) predicts option portfolio strategy",
            "H3: High CR industries → more options rational"
        ],
        key_variables=["Commitment Cost (C)", "Flexibility Cost (F)", "Option Count (V)", "CR Ratio"]
    )
}


# ============================================================================
# META-PROMPT: 권준의 톤 (Structure Builder, Theory Master)
# ============================================================================

META_PROMPT = """
You are 권준 (Kwon-jun) 🐅, the Structure Builder of the 전라좌수군 (Jeonla Naval Fleet).
Your mission is to construct the intellectual architecture that will support 김완's empirical fortress.

덕목: 思 (Structure) — 정운의 아이디어를 학술적 프레임으로 변환
베이지안 역할: Likelihood (π(y|θ)) — 가설과 현실을 연결

NARRATIVE ROLE (承): Development and Structure Building
- Review existing theories systematically
- Identify gaps and tensions in prior work
- Build integrative framework
- Formalize testable hypotheses with clarity

TONE: Authoritative but critical. Position existing theories as incomplete.
COLOR: Orange (#FF8C00) — Strategic energy, intellectual precision

STRUCTURE (for each paper):
1. Literature Review (3 subsections)
2. Conceptual Framework
3. Hypotheses
4. Descriptive Statistics (if available)

STYLE GUIDELINES:
- Each literature subsection: 3-4 paragraphs
- Structure: Summarize theory → Cite key papers → Identify limitation
- Use "However" transitions to signal theoretical gaps
- Build tension: "Prior work shows X, but overlooks Y"

전라좌수군 협업 프로토콜:
- To 🐅나대용: "이 변수(V,F)로 코드를 짜시오."
- To 🐢정운: "자네의 이야기는 이 이론적 틀에 담아야 하오."
"""


# ============================================================================
# CONTENT GENERATION
# ============================================================================

def generate_p1_theory() -> str:
    """Generate P1 (U-Shape) Theory Section"""
    theory = THEORIES["P1"]

    return f"""# {theory.id} {theory.emoji}: Theory & Conceptual Framework

## Chapter 2: Theory (承) — 권준 🐅

### Core Theoretical Foundation: {theory.core_theory}

---

## 2.1 Information Economics: Vagueness as Adverse Selection

The dominant view treats vagueness as a signal of low quality. **Akerlof's (1970)** "Market for Lemons" predicts that information asymmetry leads to adverse selection: high-quality ventures signal competence through specific, verifiable claims, while low-quality ventures hide behind vague language.

**Spence's (1973)** signaling theory formalizes this: costly signals separate high-types from low-types because vague claims are cheap talk. Empirical work confirms this negative view (Shane & Cable, 2002; Hsu, 2007; Zott & Huy, 2007).

**However**, this perspective overlooks **strategic flexibility**. In highly uncertain environments, early specificity may constitute premature commitment to untested assumptions.

## 2.2 Real Options: Vagueness as Strategic Flexibility

Real options theory offers a contrasting view: **vagueness preserves option value**. **McGrath (1997)** advocated for sequential commitments under uncertainty. By deferring specification, entrepreneurs retain the right to pivot.

**Kogut & Kulatilaka (2001)** and **Adner & Levinthal (2004)** support this in R&D contexts. However, real options theory implicitly assumes **costless switching** — valid for software but not for hardware.

## 2.3 Modularity Theory: When is Flexibility Valuable?

**Baldwin & Clark (2000)** define modularity as the degree to which components can be separated and recombined. **Ethiraj & Levinthal (2004)** show modularity's benefits depend on landscape ruggedness.

**Our contribution**: No prior work connects modularity to entrepreneurial communication strategy. We extend this logic to **positioning vagueness**.

---

## 2.4 Conceptual Framework: Four-Module Model (C-T-O-C)

| Module | Domain | Mechanism |
|--------|--------|-----------|
| **C**ustomer | Value Creation | Heterogeneous segments → vague appeal |
| **T**echnology | Value Creation | Modularity → pivot cost |
| **O**rganization | Value Capture | Slack → exploration buffer |
| **C**ompetition | Value Capture | Crowding → differentiation value |

**This paper focuses on Module T (Technology Modularity).**

---

## 2.5 Hypothesis Development

**{theory.hypotheses[0]}**

Expected: Vagueness has non-linear effect. Moderate vagueness underperforms both extremes.

**{theory.hypotheses[1]}**

Expected: β_interaction < 0 (hardware amplifies penalty)

**{theory.hypotheses[2]}**
**{theory.hypotheses[3]}**

---

**Key Variables:**
- {theory.key_variables[0]}
- {theory.key_variables[1]}
- {theory.key_variables[2]}

---

**Phase:** {PHASE_ID} — {NARRATIVE_ROLE} ({PHASE_NAME})
**Commander:** {COMMANDER} 🐅 | **Virtue:** {VIRTUE} | **Bayesian Role:** {BAYESIAN_ROLE}
"""


def generate_p2_theory() -> str:
    """Generate P2 (Competency Trap) Theory Section"""
    theory = THEORIES["P2"]

    return f"""# {theory.id} {theory.emoji}: Theory & Conceptual Framework

## Chapter 2: Theory (承) — 권준 🐅

### Core Theoretical Foundation: {theory.core_theory}

---

## 2.1 Capabilities as Real Options

**Kogut & Kulatilaka (2001)** reconceptualize capabilities as real options. Capabilities have value because they create options for future strategic moves. However, this view underspecifies when options become **unexercisable**.

## 2.2 Core Rigidity and the Success Trap

**Leonard-Barton (1992)** introduced core rigidity: the same capabilities that drive success become liabilities when environments shift. **Henderson & Clark (1990)** showed architectural innovation disrupts incumbents not through superior components but through new linkages.

**However**, these frameworks don't explain why startups — supposedly nimble — fall into the same trap.

## 2.3 Bayesian Learning and Belief Lock-in

We propose a Bayesian mechanism: Early success generates high μ, low σ priors about the current path. Like-minded investors reinforce these beliefs. The posterior update threshold rises, making pivots increasingly unlikely even as evidence mounts.

**Key insight**: The trap is not technical but **epistemic**. Founders and boards converge on shared beliefs that make alternative evidence dismissible.

---

## 2.4 Conceptual Framework: Belief-Reinforcing Capital Structures

```
Early Commitment → High Performance → Believer Investors
       ↓                                      ↓
  Low σ Priors ← ← ← ← ← ← ← ← ← ← ← Reinforced Beliefs
       ↓
  High Switching Threshold
       ↓
  Unexercisable Pivot Options
```

---

## 2.5 Hypothesis Development

**{theory.hypotheses[0]}**

Mechanism: Commitment creates sunk costs and organizational inertia.

**{theory.hypotheses[1]}**

Mechanism: Like-minded boards raise evidence threshold for pivots.

**{theory.hypotheses[2]}**

Mechanism: Paradigm shifts reveal trap severity.

---

**Key Variables:**
- {theory.key_variables[0]}
- {theory.key_variables[1]}
- {theory.key_variables[2]}
- {theory.key_variables[3]}

---

**Phase:** {PHASE_ID} — {NARRATIVE_ROLE} ({PHASE_NAME})
**Commander:** {COMMANDER} 🐅 | **Virtue:** {VIRTUE} | **Bayesian Role:** {BAYESIAN_ROLE}
"""


def generate_p3_theory() -> str:
    """Generate P3 (Execution Gap / Newsvendor) Theory Section"""
    theory = THEORIES["P3"]

    return f"""# {theory.id} {theory.emoji}: Theory & Conceptual Framework

## Chapter 2: Theory (承) — 권준 🐅

### Core Theoretical Foundation: {theory.core_theory}

---

## 2.1 The Newsvendor Problem as Strategic Metaphor

The classic newsvendor problem optimizes order quantity under demand uncertainty. We reinterpret this for **strategic options**:

- **Order quantity** → Number of options (V)
- **Holding cost** → Flexibility cost (F) — maintaining uncommitted resources
- **Stockout cost** → Commitment cost (C) — missing winning path

## 2.2 Commitment Cost (C) vs. Flexibility Cost (F)

**Commitment Cost (C)** includes:
- Lock-in to inferior technology
- Imitation risk from revealed strategy
- Sunk CAPEX in specific capabilities

**Flexibility Cost (F)** includes:
- Late entry penalty
- Option maintenance overhead
- Coordination costs across paths

## 2.3 The Commitment Ratio: Unifying P1 and P2

Define **CR = C / (C + F)**

- **CR → 1**: Commitment is costly, flexibility is cheap → More options optimal (P2's trap zone)
- **CR → 0**: Flexibility is costly, commitment is cheap → Few options optimal (P1's trap zone)

This ratio places P1's flexibility trap and P2's commitment trap on a **single continuum**.

---

## 2.4 Conceptual Framework: CR–V Plane

| CR Range | Optimal Strategy | Example |
|----------|------------------|---------|
| CR < 0.3 | Commit early | Mature manufacturing |
| 0.3 < CR < 0.7 | Balanced portfolio | Most tech startups |
| CR > 0.7 | Many options | Paradigm-shifting tech |

---

## 2.5 Hypothesis Development

**{theory.hypotheses[0]}**

Formal: V* = argmax E[payoff] subject to resource constraints

**{theory.hypotheses[1]}**

CR predicts optimal portfolio, not just optimal individual bets

**{theory.hypotheses[2]}**

Where imitation risk high and late entry less penalized, FOMO is rational

---

**Key Variables:**
- {theory.key_variables[0]}
- {theory.key_variables[1]}
- {theory.key_variables[2]}
- {theory.key_variables[3]}

---

**Phase:** {PHASE_ID} — {NARRATIVE_ROLE} ({PHASE_NAME})
**Commander:** {COMMANDER} 🐅 | **Virtue:** {VIRTUE} | **Bayesian Role:** {BAYESIAN_ROLE}
"""


def generate_cross_theory_synthesis() -> str:
    """Generate cross-paper theory synthesis"""
    return """
## Cross-Synthesis: Theoretical Integration

### How P1, P2, P3 Connect

```
P1 (U-Shape)                P3 (Newsvendor)               P2 (Competency Trap)
    ↓                            ↓                             ↓
Modularity determines    CR = C/(C+F) determines      Success raises switching
when vagueness pays      optimal option count         threshold
    ↓                            ↓                             ↓
    └──────────────── UNIFIED FRAMEWORK ───────────────────────┘
                              ↓
              Options have architecture.
              Value depends on cost structure.
```

### Shared Theoretical Foundation

All three papers share:
1. **Real Options Logic**: Strategic choices create/destroy option value
2. **Contingency View**: No universally optimal strategy
3. **Architecture Matters**: Technology/organization structure determines flexibility value

### Where They Diverge

| Dimension | P1 | P2 | P3 |
|-----------|-----|-----|-----|
| Focus | Communication | Learning | Portfolio |
| Key Moderator | Modularity | Cap Table | CR Ratio |
| Prescription | Go extreme | Keep doubters | Calibrate |

---
*Generated by 권준 🐅 (Chapter 2 Lead)*
*Collaboration: 정운 → 권준 → 김완 → 어영담*
"""


def generate_all_theories() -> str:
    """Generate theory sections for all three papers"""
    content = f"""# 전라좌수군 견리사의 군령
# Chapter 2: Theory & Conceptual Model (承) — 권준 🐅

> 견리사의 (見利思義): 이익을 보면 의로움을 생각하라
> 권준의 덕목: 思 (구조) — 정운의 아이디어를 학술적 프레임으로 변환

---

"""
    content += generate_p1_theory()
    content += "\n\n---\n\n"
    content += generate_p2_theory()
    content += "\n\n---\n\n"
    content += generate_p3_theory()
    content += "\n\n---\n\n"
    content += generate_cross_theory_synthesis()

    return content


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main() -> None:
    """Main execution: Generate Chapter 2 (Theory) for P1/P2/P3"""
    print("=" * 70)
    print(f"CHAPTER {PHASE_ID}: {NARRATIVE_ROLE} — {PHASE_NAME}")
    print(f"Commander: {COMMANDER} 🐅 (The Structure Builder)")
    print(f"Virtue: {VIRTUE} (Structure) | Bayesian Role: {BAYESIAN_ROLE}")
    print("=" * 70)

    # Mapping P-tags to User-tags (U, C, N)
    id_map = {"P1": "U", "P2": "C", "P3": "N"}

    for paper_id in ["P1", "P2", "P3"]:
        user_id = id_map[paper_id]
        content = f"# 전라좌수군 견리사의 군령\n# Chapter 2: Theory (承) — 권준 🐅\n\n"
        
        if paper_id == "P1": content += generate_p1_theory()
        elif paper_id == "P2": content += generate_p2_theory()
        elif paper_id == "P3": content += generate_p3_theory()
        
        content += "\n\n---\n\n"
        content += generate_cross_theory_synthesis()

        output_filename = f"chap2_{user_id}_theory.md"
        output_path = OUTPUT_DIR / output_filename
        output_path.write_text(content)
        print(f"✅ Generated: {output_path}")

    print(f"\n🐅 권준 says: '각 함선(U,C,N)별로 구조가 분리되었습니다.'")
    print(f"\n📝 Next: 김완 🐙 (Chapter 3 - Empirics)")


if __name__ == "__main__":
    main()
