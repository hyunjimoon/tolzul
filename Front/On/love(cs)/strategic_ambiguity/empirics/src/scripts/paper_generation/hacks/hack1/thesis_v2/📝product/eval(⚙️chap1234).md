---
created: 2025-11-29
evaluator: 04_GE🟢 (Claude Code)
virtue: 造 (구축)
role: Manufacturing/Build (MIT Framework)
rally_point: RP2 (Scale Phase)
modified:
  - 2025-12-08T06:50:09-05:00
---

# ⚙️ G-Squad Engineering Handbook: The "Scale" Protocol

> **Objective**: Standardize the production of 108 paragraphs by converting "Art" into "Engineering".
> **Owner**: 🟠 G-Squad (Architect & Engineer)
> **Audience**: J-Squad (Builder), K-Squad (Auditor)

---

## 1. The "Golden Rules" of Engineering (Immutable)

### Rule #1: H₀ First (The Anchor)
*   **Principle**: Never start with "What we found". Start with "What the world believed".
*   **Implementation**:
    *   Explicitly state the Null Hypothesis (H₀) in `toc.md`.
    *   *Example*: "H₀: Vagueness is bad (Scott's Null)."
    *   **Why**: H₀ gives us something to kill. A dead H₀ is the birth of our story.

### Rule #2: Mechanism Defense (The Shield)
*   **Principle**: We cannot prove causality (V → Y). We can only prove the *path* (V → M → Y).
*   **Implementation**:
    *   Define the Mediator (M) clearly.
    *   *Example*: "V → **Investor Match** → Growth".
    *   **Why**: Reviewers attack direct links. They accept "plausible pathways".

### Rule #3: Figure-First Development (The Blueprint)
*   **Principle**: If you can't graph it, you can't write it.
*   **Implementation**:
    *   Step 1: Define axes (X=Vagueness, Y=Growth).
    *   Step 2: Draw the expected curve (U-shape).
    *   Step 3: Write the code (`figures.py`) to generate it.
    *   Step 4: Write the text *only after* the figure exists.

---

## 2. The "Gospel" Template (7-Step Standard)

Every paper (U, C, N) must follow this 7-step logic flow in its Intro/Theory:

| Step | Code | Name | Function |
|:---|:---|:---|:---|
| 1 | 📿 | **Gospel** | State the accepted wisdom (H₀). "Everyone says X." |
| 2 | 🧩 | **Puzzle** | Show a data point that breaks H₀. "But look at Y." |
| 3 | 😮 | **RQ** | Ask the Research Question. "When is X actually Z?" |
| 4 | 🔎 | **Lens** | Introduce our unique framework. "Viewed through Lens L..." |
| 5 | 😆 | **Solution** | Present our finding (H₁). "We find that..." |
| 6 | 🗺️ | **Closest** | Position against nearest rival. "Unlike Smith (2020)..." |
| 7 | 🗄️ | **Roadmap** | "Section 2 does A, Section 3 does B." |

---

## 3. Variable Notation Standard (ISO-108)

To ensure interoperability between U, C, and N papers:

### 3.1 Core Variables (EVLF Framework)

| Variable | Symbol | Definition | Measurement | Paper |
|:---|:---|:---|:---|:---|
| **Early Funding** | $E$ | 단기 생존 지표 | Series A 금액 (USD, z-score) | U, C |
| **Vagueness** | $V$ | 약속 모호성 | Composite index [0,1] | U, N |
| **Later Success** | $L$ | 장기 생존 지표 | Series B+ 달성 (binary) | U, C |
| **Flexibility** | $|\Delta V|$ | 전략 피벗 역량 | $|V_{late} - V_{early}|$ [0,1] | C |
| **Options** | $k^*$ | 최적 옵션 수 | Integer ≥ 1 | N |

### 3.2 Vagueness (V) Composition

```
V = 0.5 × max(V_cat, V_conc) + 0.5 × mean(V_cat, V_conc), scaled to [0,1]
```

| Component | Name | Definition | Literature |
|:---|:---|:---|:---|
| $V_{cat}$ | Categorical Vagueness | 추상적 키워드 사용 ("platform", "solution") | Zuckerman 1999, Pontikes 2012 |
| $V_{conc}$ | Concreteness Deficit | 구체적 참조 부재 ("Level 4", "95%", "Q3 2024") | Pan et al. 2018 |

### 3.3 Paper N Cost Variables (Newsvendor)

| Variable | Symbol | Definition | Outcome |
|:---|:---|:---|:---|
| **Overage Cost** | $C_o$ | 너무 모호할 때의 비용 | 투자자 혼란 → 어려운 펀딩 (생존 가능) |
| **Underage Cost** | $C_u$ | 너무 정밀할 때의 비용 | 피벗 불가 → 벤처 사망 |
| **Critical Ratio** | $CR$ | $C_u / (C_u + C_o)$ | Deep-tech: $C_u >> C_o$ → $CR → 1$ → $k^* → HIGH$ |

### 3.4 Hypothesis Notation

| Hypothesis | Prediction | Model Specification |
|:---|:---|:---|
| **H1** (Early Penalty) | $\beta_1 < 0$ | $E_i = \beta_0 + \beta_1 V_i + \Gamma'X_i + C_{cohort} + \varepsilon_i$ |
| **H2** (Later Benefit) | $\alpha_V < 0$ | $Pr(L_i=1) = logit^{-1}(\alpha_0 + \alpha_1 V + \delta X + C_{cohort})$ |
| **H_cost** | $E[Y|flex, E] > E[Y|rigid, E]$ | Paper C counterfactual framework |
| **H_N1** | High CR → High $k^*$ | Paper N newsvendor calibration |

---

## 4. Lessons Learned (The "Black Box" Log)

### From ✌️U (The U-Shape)
*   **Lesson**: Parametric models ($V^2$) force symmetry.
*   **Fix**: Use **Quantile Regression** or Binning to let the data reveal asymmetry.

### From 🦾C (The Trap)
*   **Lesson**: "Funding" is ambiguous.
*   **Fix**: Split into **Flow** ($L/E$ ratio) vs **Stock** (Total $). Flow reveals efficiency.
*   **Lesson**: Pivot Direction vs Magnitude.
*   **Fix**: "Magnitude of pivot ($|\Delta V|$)" predicts growth better than "Direction". Focus on the *size* of the jump, not the landing spot.

### From 🤹N (The Newsvendor)
*   **Lesson**: "Cost" is confusing.
*   **Fix**: Distinguish **Flexibility Cost** (maintenance) vs **Switching Cost** (change).

---

## 5. Action Items for Scale Phase

1.  **[ ] Update `toc(n).md`**: Apply Rule #1 (H₀: $k^*=1$).
2.  **[ ] Refactor `figures.py`**: Ensure all plots use the ISO-108 notation.
3.  **[ ] Audit `assets.json`**: Verify every "Done" asset maps to a specific paragraph.

**Signed**: 🟠 G-Squad Leader
