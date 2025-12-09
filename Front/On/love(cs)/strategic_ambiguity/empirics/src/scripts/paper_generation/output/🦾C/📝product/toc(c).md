---
title: 🦾C - When Commitment Becomes a Cage TOC (v2.0)
structure: 4 chapters × 32 paragraphs (7+9+11+5)
thesis: AOC = f(V) → Calcification mathematized → 8.8× gap
core_mechanism: dY/dE = dY/d|ΔV| × d|ΔV|/dE = (+) × (-) < 0
modified:
  - 2025-12-06T16:15:00-05:00
key_updates_v2:
  - AOC = f(V) 수리 모델 도입
  - Dixit-Pindyck 정합성 명시
  - "Calcification" = 비가역적 투자의 수식화
  - 32¶ 구조로 확장 (기존 26¶ → 32¶)
---

# 🦾C: When Commitment Becomes a Cage — TOC v2.0

> 🌙통제사: 이순신 | 최종수정: 2025-12-06

---

## 🎯 Core Thesis (v2.0)

> **Calcification Mathematized**: AOC = f(V), where AOC′(V) > 0
> **Mechanism**: Capital → Promise → σ↓ → Learning blocked → Y↓
> **Result**: Escape Velocity (3.32×) vs Golden Cage (0.38×) = **8.8× gap**

### v1.0 → v2.0 핵심 수정

| 항목 | v1.0 | v2.0 | 근거 |
|:--|:--|:--|:--|
| **AOC** | 암묵적 개념 | **AOC = f(V) 수리 모델** | Thesis 초안 |
| **Calcification** | 은유 | **비가역적 투자의 수식화** | Dixit-Pindyck 정합 |
| **구조** | 26¶ | **32¶** (7+9+11+5) | 표준화 |

---

## 📐 Theoretical Foundation: AOC = f(V)

### Abandonment Option Cost Model

$$AOC(V) = \int_0^V \frac{\partial \text{Sunk Cost}}{\partial v} \cdot P(\text{pivot needed}) \, dv$$

**Properties**:
- AOC′(V) > 0: 자본 증가 → AOC 증가
- AOC″(V) > 0: 가속도 증가 (convex)
- **Critical threshold V***: AOC(V*) = Expected Pivot Value → "죽음의 나선" 진입

### Dixit-Pindyck Integration

| Dixit-Pindyck | This Paper | Mapping |
|:--------------|:-----------|:--------|
| Irreversibility | Promise rigidity | 약속 = 비가역적 투자 |
| Uncertainty | Market/tech flux | σ_env |
| Option value | Flexibility value | |ΔV| capacity |
| **Trigger point** | **V*** | AOC = Pivot value |

### Calcification Mechanism (The Math of Rigidity)

```
Stage 1: Promise (Cognitive)
  Founder says: "We will do X"
  → Investor expectation set
  
Stage 2: Contract (Legal)  
  Promise codified in term sheet
  → Board oversight activated
  
Stage 3: Asset (Physical)
  Capital deployed to X-specific assets
  → Sunk cost accumulated
  
Stage 4: Calcification (Locked)
  AOC(V) > Pivot Value
  → Pivot economically irrational
  → "Golden Cage"
```

---

## 📍 32-Paragraph Scaffold (v2.0)

### Chapter 1: Introduction (7¶)

| ¶ | 단계 | First Sentence |
|:-:|:-:|:--|
| 1 | 📿 **Gospel** | "Resource-based theory holds that more capital enables more experimentation, accelerating learning and improving outcomes (Barney 1991, Nanda & Rhodes-Kropf 2016)." |
| 2 | 🧩 **Puzzle** | "Yet among ventures with similar early funding, those who changed strategy ('Escape Velocity') grew 8.8× more than those who maintained initial commitments ('Golden Cage')." |
| 3 | 😮 **RQ** | "When does early success become a trap—converting resource advantage into strategic rigidity?" |
| 4 | 🔎 **Lens** | "We develop AOC = f(V): Abandonment Option Cost as an endogenous function of capital, mathematizing how commitment 'calcifies' into irreversibility." |
| 5 | 😆 **Solution** | "Capital requests commitment, commitment homogenizes teams, and homogeneity blocks the learning that enables adaptation—what got you funded prevents your growth." |
| 6 | 🗺️ **Closest** | "Unlike Nanda (2020) who studies experimentation benefits and Dixit-Pindyck (1994) who model option exercise, we endogenize AOC as f(V) to explain why resources hurt." |
| 7 | 🗄️ **Roadmap** | "Section 2 derives the AOC = f(V) model with Calcification stages, Section 3 tests commitment costs across funding deciles, and Section 4 connects to Papers U and N." |

### Chapter 2: Theory (9¶)

| ¶ | 내용 | 산출물 |
|:-:|:--|:--|
| 8 | **Lit: RBV Gap** — Assumes flexible deployment, ignores commitment constraints | |
| 9 | **Lit: Real Options Gap** — Models exercise, but AOC treated as exogenous | |
| 10 | **Lit: Org Learning Gap** — Ignores how resources reduce learning capacity | |
| 11 | **Position**: AOC = f(V) endogenizes rigidity | 🗄️ Notation Table |
| 12 | **Model: AOC(V)** — Properties: AOC′>0, AOC″>0, threshold V* | 🖼️ Fig 1: AOC Curve |
| 13 | **Calcification 4 Stages**: Promise → Contract → Asset → Lock | 🖼️ Fig 2: 4-Stage |
| 14 | **Mechanism: E → \|ΔV\|** — Funding → promise → homogeneity → σ↓ | |
| 15 | **Mechanism: \|ΔV\| → Y** — Flexibility → adaptation → growth | |
| 16 | **Hypotheses**: H_cost (8.8× gap), H_supporting (ρ < 0) | |

### Chapter 3: Empirics (11¶)

| ¶ | 내용 | 산출물 |
|:-:|:--|:--|
| 17 | Context: Panel 180K+ ventures × 4 years | |
| 18 | Sample: Complete E, L, V trajectory data | |
| 19 | DV: Y = L/E (later/early funding ratio) | |
| 20 | IV: E = first financing size | |
| 21 | Measure: \|ΔV\| = \|V_later - V_early\| | |
| 22 | Measure: AOC proxy via commitment indicators | 🗄️ Table 1: Descriptives |
| 23 | Cohort Design: 2×2 (E × \|ΔV\|) | 🖼️ Fig 3: Cohort Matrix |
| 24 | H_supporting Test: ρ(E, \|ΔV\|) = -0.117*** | |
| 25 | **Main Result**: Escape 3.32× vs Cage 0.38× = **8.8×** | 🖼️ Fig 4: Flagship |
| 26 | Cost by Decile: -2.5× average per decile | 🗄️ Table 2: Cost Table |
| 27 | Robustness: Alternative measures, industries | |

### Chapter 4: Discussion (5¶)

| ¶ | 내용 |
|:-:|:--|
| 28 | **Theory Contribution**: AOC = f(V) endogenizes Dixit-Pindyck |
| 29 | **Link to Paper U**: V determines investor channel → AOC accumulation rate |
| 30 | **Link to Paper N**: Cost = -2.5× calibrates C in CR = C/(C+F) |
| 31 | **Practical Implication**: Maintain "doubters" for σ preservation |
| 32 | Conclusion: "Deprivation → Flexibility → Success is not 대기만성 but AOC avoidance." |

---

## 🔗 Three-Paper Integration

```
✌️U: V → Investor Match
       ↓ V determines AOC accumulation rate
🦾C (This Paper): E → AOC(V) → |ΔV|↓ → Y↓
       ↓ Cost = -2.5× per decile
🤹N: C (from Paper C) → CR = C/(C+F) → k*
```

### Shared Conclusion: Murky Middle = Death Zone

| Paper | Mechanism | This Paper's Role |
|:------|:----------|:------------------|
| ✌️U | U-shape (β₂ > 0) | V ≈ 0.5 → fastest AOC accumulation |
| 🦾C | 8.8× gap | **Calcification proof** |
| 🤹N | k* non-existence | C calibration via -2.5× |

---

## 📊 산출물 Checklist (v2.0)

| ID | 내용 | ¶ | 상태 |
|:--|:--|:-:|:-:|
| Fig 1 | AOC(V) Curve with V* threshold | 12 | ⬜ |
| Fig 2 | Calcification 4 Stages | 13 | ⬜ |
| Fig 3 | 2×2 Cohort Matrix | 23 | ⬜ |
| Fig 4 | Escape vs Cage (8.8× gap) | 25 | ⬜ |
| Table 1 | Descriptive Statistics | 22 | ⬜ |
| Table 2 | Cost by Decile (-2.5×) | 26 | ⬜ |

---

## 🔑 핵심 용어 (v2.0)

| 용어 | 정의 | 수식 |
|:--|:--|:--|
| **AOC** | Abandonment Option Cost | AOC = f(V), AOC′ > 0 |
| **V*** | Calcification threshold | AOC(V*) = E[Pivot Value] |
| **Calcification** | Irreversible commitment | 4-stage: Promise→Contract→Asset→Lock |
| **8.8×** | Escape vs Cage gap | 3.32× / 0.38× |
| **-2.5×** | Per-decile commitment cost | E[Y\|Flex] - E[Y\|Lock] |

---

*v2.0: AOC = f(V) 수리모델, Dixit-Pindyck 정합, Calcification 4단계, 32¶ 확장*
