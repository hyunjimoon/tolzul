# Abstract v3 → v4 CHANGELOG

**Date:** 2025-11-30
**Author:** 🐅 권준 (Kwon-T)
**Reviewed by:** 통제사 지시에 따른 최종 수정

---

## Summary

v4는 정운(利/Tone), 김완(義/Rigor), Moon(統/Commander)의 통합 피드백을 반영한 최종 버전입니다.

**핵심 변경 원칙:**
1. **Verbal-first, Math-second** (특히 Paper N)
2. **Non-monotonic (convex)** 표현으로 U-shape 명확화
3. **"Mathematically unexercisable"** 구문 강화 및 clarifying clause 추가
4. **Data claims 완화** — "calibrate and illustrate" 표현
5. **Notation 일관성** — 문서 끝에 참조 섹션 추가

---

## Detailed Changes

### 0. Global Tone & Numbers

| Location | v3 | v4 | Issue |
|----------|----|----|-------|
| Integrated | "even well-executed startups fail" | "even well-run startups can fail" | #004 |
| Paper U | ✅ Already "more than 130,000" | (no change) | #005 |
| Paper N | "calibrate the model using modularity measures" | "calibrate and illustrate this rule using... tens of thousands of mobility ventures" | #006, #041 |
| Integrated | "survival often favors the extremes" | (no change) | #007 |

### 1. Paper U — Hypothesis Alignment

| Section | v3 | v4 | Issue |
|---------|----|----|-------|
| H1 표현 | "Survival is convex in vagueness (β_{V²} > 0)" | "Survival is **non-monotonic (convex)** in promise vagueness, with ventures at either extreme—'hyper-concrete' or 'masterfully vague'—surviving at higher rates than those in the middle (β_{V(1-V)} < 0, equivalently β_{V²} > 0)" | #002, #003 |
| H2 | (same) | (same) | — |
| 마지막 문장 | "Startups fail not because they execute poorly, but because they choose a playbook..." | "The insight that both extremes can succeed—while the middle fails—suggests that the core capability is not executing a playbook well, but *choosing* the right playbook in the first place." | #004, #016 |
| Methods | "construct a text-based vagueness index... duration models" | Added: "estimate **duration models of post–Series A survival** with sector, geography, and cohort controls. The empirical strategy treats vagueness as potentially endogenous, using instrumental variable approaches where appropriate." | #006 |
| Hypotheses | Inline text | **Itemized list** for clarity | (structural) |

### 2. Paper C — Environment & Trap Language

| Section | v3 | v4 | Issue |
|---------|----|----|-------|
| Opening | "In shifting, capital-intensive industries" | "In **shifting, capital-intensive industries such as autonomous vehicles**" | #009 |
| Trap mechanism | "lie beyond the evidence threshold that the board's posterior beliefs would ever sanction" | "become **mathematically unexercisable**—they lie beyond the evidence threshold that the board's posterior beliefs would ever sanction. A venture may 'have' the option to pivot on paper, but its internal decision-making apparatus will never generate the conviction required to exercise it." | #010 |
| Prediction | "The model implies that ventures... are especially vulnerable" | "The model **implies that ventures combining strong early success with homogeneous boards are especially vulnerable during paradigm shifts**, because their belief dynamics make pivots unusually hard to justify—even when external evidence warrants a change of course." | #008 |
| Evidence verb | "test these ideas" | "illustrate these ideas" | (tone) |

### 3. Paper N — CR Rule & Equation Order (#044)

| Section | v3 | v4 | Issue |
|---------|----|----|-------|
| **Structure** | Equation first, explanation second | **Verbal description first** → "the optimal number of options increases with the Critical Ratio—the share of total cost that comes from committing to the wrong path rather than staying flexible" → **then** formal expression k* = F_{π(D)}^{-1}(CR) | #044 |
| CR definition | "where C is the cost of committing to the wrong path and F is the cost of maintaining flexibility" | "where C is the cost of **wrong commitment** (choosing a path that fails) and F is the cost of **maintaining flexibility** (spreading resources across multiple options)" | (clarity) |
| Data claim | "calibrate the model using modularity measures and cost proxies derived from the mobility venture dataset" | "**calibrate and illustrate** this rule using cost proxies and parameters derived from **tens of thousands of mobility ventures**" | #006, #041 |
| Closing | "cost-calibrated rule of thumb that founders can approximate from observable industry parameters" | Added: "The model does not promise exact answers, but it provides a principled framework for thinking about the commitment-flexibility tradeoff." | #012 |

### 4. Integrated Abstract — Glue Text

| Section | v3 | v4 | Issue |
|---------|----|----|-------|
| Context | "capital-intensive, technology-heterogeneous markets like autonomous mobility" | "**capital-intensive, technology-heterogeneous markets such as autonomous mobility**" | #013, #043 |
| Paper C summary | "belief dynamics render them unexercisable" | "strategic options... become **mathematically unexercisable**—they lie beyond the evidence threshold that the board's posterior beliefs would ever sanction" | #010 |
| Paper N summary | "optimal count k* depends on the Critical Ratio" | "Using newsvendor logic, I show that the optimal count k* increases with the **Critical Ratio** CR = C/(C+F)—the share of total cost that comes from committing to the wrong path rather than staying flexible. This turns 'how many options?' into a **cost-calibrated rule of thumb**..." | #044 |
| Causal chain | Implicit | Explicit with notation: "Paper U shows how **promise design** shapes investor beliefs about possible futures (π(D)); Paper C shows how **governance** determines the costs of commitment versus flexibility (C, F); Paper N combines beliefs and costs into an explicit **portfolio rule** (k* = F_{π(D)}^{-1}(CR))" | (structure) |

### 5. New Addition: Notation Reference

문서 끝에 **Notation Reference** 섹션 추가:
- V, θ*, σ, μ, k*, CR, C, F, π(D)
- β_{V²}, β_{V(1-V)}, β_{VT}

이는 김완의 일관성 요구(Rigor)를 충족합니다.

---

## Issue Registry Status Update

| Issue | Status | Note |
|-------|--------|------|
| #002 | ⚓ MERGED | H1 convex structure implemented |
| #003 | ⚓ MERGED | Null = Action School implied |
| #004 | ⚓ MERGED | Execution wording softened |
| #005 | ⚓ MERGED | "more than 130,000" |
| #006 | ⚓ MERGED | "calibrate and illustrate" + "tens of thousands" |
| #007 | ⚓ MERGED | "often favors the extremes" |
| #008 | ⚓ MERGED | "implies... especially vulnerable" |
| #009 | ⚓ MERGED | "shifting, capital-intensive industries such as AV" |
| #010 | ⚓ MERGED | "mathematically unexercisable" + clarifying clause |
| #011 | ⚓ MERGED | Verbal first, math second |
| #012 | ⚓ MERGED | "rule of thumb... approximate" |
| #041 | ⚓ MERGED | Data claim softened |
| #043 | ⚓ MERGED | "technology-heterogeneous" in Integrated |
| #044 | ⚓ MERGED | N verbal→equation order |
| #045 | ⚓ MERGED | Notation consistency |

---

## Files Generated

1. `thesis_abstracts_v4.tex` — Final abstract file
2. `abstract_v3_v4_changelog.md` — This file

---

**필사즉생 (必死卽生)**

⚓ 권준 (Kwon-T) — 전라좌수군 중군
