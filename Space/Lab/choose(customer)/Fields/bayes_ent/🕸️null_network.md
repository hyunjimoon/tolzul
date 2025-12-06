---
modified:
  - 2025-12-03T08:29:18-05:00
  - 2025-12-05T16:05:31-05:00
  - 2025-12-06T02:59:30-05:00
---
# 🕸️ Bayesian Entrepreneurship Null Network

> Scott Stern 타입 학자들의 **Null (기존 믿음)** 지도

---

## 🎯 Core Null (뒤집어야 할 것)

> **"Clarity maximizes information → Better decisions → Higher survival"**

## 1순위

| 학자                  | 소속             | 대표작                                | 그들의 Null                               |
| :------------------ | :------------- | :--------------------------------- | :------------------------------------- |
| **Scott Stern**     | MIT Sloan      | Bayesian Entrepreneurship (2024)   | 과학적 실험 → 전략적 선택 수렴                     |
| **Josh Gans**       | Toronto Rotman | Entrepreneurial Strategy (2019)    | 명확한 가설 → 피봇 or 더블다운                    |
| **Arnaldo Camuffo** | Bocconi        | Scientific RCT (2020)              | Scientific method = clarity → success  |
| **Ramana Nanda**    | Imperial/HBS   | Learning & Experimentation         | 정보 해상도 극대화 = 가치                        |

## 2순위

| **Patrick Bolton** | Imperial | Moral Hazard in Experiments (2024) | Killer experiment (s₁↑, s₂↑) = optimal |
| :----------------- | :------- | :--------------------------------- | :------------------------------------- |

josh lerner, paul gomper - vc, teppo

---

## 📜 핵심 논문별 Null 상세

### [[📜nanda24_prior_exp_learn]]
**Null**: "실험의 가치 = V*(pP - pF), 정보량 극대화가 최적"
**✌️U Surprise**: 때로는 덜 정보적인 실험이 전략적으로 유리

### [[📜bolton24_moral_hazard]]
**Null**: "VC는 killer experiment 선호 (s₁=s̄₁, s₂=s̄₂)"
**Setup**:
- s₁ = sensitivity (true positive rate)
- s₂ = specificity (true negative rate)
- Entrepreneur prefers false positives (continuation)
- VC prefers conclusive tests

**Key Insight for ✌️U**:
> "Entrepreneur cannot commit to designing killer experiment"
→ 창업자의 전략적 모호성은 **도덕적 해이**와 연결
→ 그러나 ✌️U는 이것이 **합리적 전략**일 수 있음을 보임

**Mechanism**:
```
VC utility:    U_I = p₀s₁αV - [p₀s₁ + (1-p₀)(1-s₂)]K - C
Entrepreneur:  U_E = p₀s₁(1-α)V + [p₀s₁ + (1-p₀)(1-s₂)]Z + Z

→ Entrepreneur always sets s₂ = s₂̲ (minimum specificity)
→ Maximizes false positives → continuation
```

**Policy Solutions** (Bolton et al.):
1. Pay for failure (X ≥ Z)
2. University validation
3. Complementary task design

### [[📜camuffo20_scientific_rct]]
**Null**: "Scientific approach = faster failure identification"
**Gap for ✌️U**: 내부 의사결정만 분석 → 외부 커뮤니케이션 연결 필요

### [[📜gans19_entrepreneurial_strategy]]
**Null**: "Choose: Control vs Collaborate vs Compete"
**Gap for ✌️U**: 선택의 명확성 가정 → 의도적 모호성 전략 누락

---

## 🔄 ✌️U의 Surprise 구조

```
Scott의 Null:     Precision ↑ → Information ↑ → Survival ↑
Bolton의 Null:    s₂ ↑ → False positive ↓ → Efficiency ↑
Nanda의 Null:     V*(pP-pF) ↑ → Value inflection ↑

✌️U Surprise:     β·V(1-V) < 0
                  → Extreme V (≈0 or ≈1) → Survival ↑
                  → Middle V → "Graveyard"
                  
Mechanism:        Analyst ← V≈0 (precise)
                  Believer ← V≈1 (vague)
                  Neither ← V≈0.5 (death zone)
```

---

## 📊 Null Network 시각화

```
                    ┌─────────────────────────────────────┐
                    │     BAYESIAN ENTREPRENEURSHIP       │
                    │         "Clarity is optimal"        │
                    └──────────────┬──────────────────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          │                        │                        │
    ┌─────▼─────┐           ┌──────▼──────┐          ┌──────▼──────┐
    │   STERN   │           │   NANDA     │          │   BOLTON    │
    │  Strategy │           │  Learning   │          │ Experiment  │
    │  Choice   │           │  V*(pP-pF)  │          │   Design    │
    └─────┬─────┘           └──────┬──────┘          └──────┬──────┘
          │                        │                        │
          └────────────────────────┼────────────────────────┘
                                   │
                          ┌────────▼────────┐
                          │    ✌️U PAPER    │
                          │  β·V(1-V) < 0   │
                          │ "Strategic      │
                          │  Ambiguity"     │
                          └─────────────────┘
```

---

## 🎓 Citation Strategy

| 인용 방식 | 대상 논문 | ✌️U에서 역할 |
|:---|:---|:---|
| **Null Setup** | Stern, Gans, Camuffo | "Economists assume..." |
| **Framework** | Nanda, Bolton | V*(pP-pF), s₁/s₂ 개념 차용 |
| **Contrast** | Bolton | Moral hazard vs Rational strategy |
| **Support** | Eisenberg, Sillince | Strategic ambiguity 문헌 |

---

## 🦾C Null Network: Commitment Trap

### Core Null (뒤집어야 할 것)

> **"Early commitment signals conviction → Attracts capital → Enables growth"**

| 학자 | 대표작 | 그들의 Null |
|:---|:---|:---|
| **Amit Zott** | Business Model Design | Commit early to coherent BM |
| **Eisenhardt** | Dynamic Capabilities | Build commitment through routines |
| **Ghemawat** | Commitment (1991) | Irreversibility = competitive advantage |
| **Christensen** | Innovator's Dilemma | Disruptors commit to new value network |

### 🦾C의 Surprise

```
Null:     Early commitment → Capital → Growth

🦾C:      Early commitment + Like-minded investors
                    ↓
          Belief homogenization (σ_belief ↓)
                    ↓
          Pivot threshold θ* = μ + kσ rises
                    ↓
          Necessary pivots blocked → "Zombie venture"
```

### Bolton 연결: Specificity as Commitment

Bolton의 s₂ (specificity)는 🦾C의 commitment와 동형:

| Bolton | 🦾C |
|:---|:---|
| s₂ ↑ = fewer false positives | Commitment ↑ = clearer signal |
| VC prefers s₂ = s̄₂ | Like-minded investors prefer high commitment |
| Entrepreneur resists | Founder needs flexibility to pivot |

**통찰**: Bolton의 "killer experiment"를 선호하는 VC = 🦾C의 "like-minded investor"
→ 둘 다 **confirmation-seeking** behavior
→ 둘 다 **pivot를 막는** 메커니즘

### Key Papers for 🦾C

| 논문 | 역할 | 인용 방식 |
|:---|:---|:---|
| [[📜ghemawat91_commitment]] | Null setup | "Economists assume..." |
| [[📜kirtley23_pivot_process]] | Support | Pivot = 점진적 과정 |
| [[📜bolton24_moral_hazard]] | Mechanism | s₂ ↔ commitment 동형 |
| [[📜nanda17_financing_risk]] | Empirical | Financing risk → safer bets |

---

## 🤹N Null Network: FOMO Dilemma

### Core Null (뒤집어야 할 것)

> **"More options = More flexibility = Better outcomes"**

| 학자 | 대표작 | 그들의 Null |
|:---|:---|:---|
| **McGrath** | Real Options (1999) | Options preserve upside |
| **Trigeorgis** | Real Options in Capital Investment | More options = higher NPV |
| **Sarasvathy** | Effectuation | Keep options open |
| **Adner & Levinthal** | Real Options & Tech Investment | Flexibility is valuable |

### 🤹N의 Surprise

```
Null:     Options ↑ → Flexibility ↑ → Value ↑

🤹N:      Options have COST (commitment cost C)
          + Options have DECAY (flexibility cost F)
                    ↓
          Optimal k* = F⁻¹(CR), where CR = C/(C+F)
                    ↓
          Too few options → Miss opportunities (FOMO)
          Too many options → Diluted commitment → Fail all
```

### News Vendor Analogy

| News Vendor | 🤹N Startup |
|:---|:---|
| Inventory Q | Number of strategic options k |
| Overage cost Co | Commitment cost C (resources tied up) |
| Underage cost Cu | Flexibility cost F (missed opportunity) |
| Q* = F⁻¹(Cu/(Cu+Co)) | k* = F⁻¹(C/(C+F)) |

### Bolton 연결: Experiment Design as Option Portfolio

Bolton의 experiment choice는 🤹N의 option portfolio와 동형:

| Bolton | 🤹N |
|:---|:---|
| Single experiment design | Single option selection |
| s₁/s₂ trade-off | C/F trade-off |
| Independent vs Complementary tasks | Industry-specific CR |

**통찰**: Bolton의 "complementary tasks" (λ > 0)는 🤹N의 **synergistic options**
→ 옵션 간 시너지가 있으면 더 많이 보유 가능
→ "Substitute tasks"는 mutually exclusive options → 적게 보유해야

### Key Papers for 🤹N

| 논문 | 역할 | 인용 방식 |
|:---|:---|:---|
| [[📜mcgrath99_falling_forward]] | Null setup | "Real options theory assumes..." |
| [[📜ewens18_cost_experimentation]] | Mechanism | Cloud → ↓C → ↑k* |
| [[📜bolton24_moral_hazard]] | Framework | Independent vs Complementary |
| [[📜cachon05_newsvendor]] | Model | CR framework |

---

## 🔗 Three Papers United: The Specificity Thread

```
                    BOLTON's s₂ (Specificity)
                           |
         ┌─────────────────┼─────────────────┐
         ↓                 ↓                 ↓
      ✌️U                🦾C               🤹N
   Vagueness V      Commitment θ      Options k
         |                 |                 |
    β·V(1-V)<0      θ*=μ+kσ rises     k*=F⁻¹(CR)
         |                 |                 |
    Extremes win    Lock-in trap      FOMO/Overcommit
         |                 |                 |
         └─────────────────┼─────────────────┘
                           ↓
              UNIFIED INSIGHT:
        "Specificity has non-monotonic returns.
         Optimal level depends on:
         - Investor heterogeneity (U)
         - Belief dynamics (C)  
         - Cost structure (N)"
```

---

*Last updated: 2025-12-03*
*For: ✌️U, 🦾C, 🤹N unified dissertation*
