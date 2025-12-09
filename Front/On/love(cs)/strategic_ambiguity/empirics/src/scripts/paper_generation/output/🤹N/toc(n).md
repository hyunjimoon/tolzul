---
modified:
  - 2025-12-08T13:44:09-05:00
---
개선 버전

## 📍 32-Paragraph Scaffold (v2.1)

### Chapter 1: Introduction (7¶)

| ¶ | 단계 | First Sentence |
|:-:|:-:|:--|
| 1 | 📿 **Gospel** | "The Lean Startup canon prescribes a single focused option (k=1) and rapid iteration as the dominant strategy for resource-constrained ventures." |
| 2 | 🧩 **Puzzle** | "Yet in deep-tech settings such as autonomous vehicles, quantum computing and synthetic biology, ventures that maintained multiple options survived while highly focused peers with k=1 often failed." |
| 3 | 😮 **RQ** | "This paper asks when the Lean Startup prescription breaks down, and how founders should choose the number of strategic options k* under extreme uncertainty and heterogeneous investors." |
| 4 | 🔎 **Lens** | "We introduce the 'Promise Vendor' model, treating the entrepreneur as a newsvendor of strategic options who uses future promises (V) to infer commitment and flexibility costs (Cᵤ, Cₒ)." |
| 5 | 😆 **Solution** | "Our central result is that the Critical Ratio CR = Cᵤ/(Cᵤ + Cₒ) maps into an optimal option count k* = F_D⁻¹(CR), and that investor heterogeneity can render k* undefined in a 'Murky Middle' of intermediate specificity S₂ ≈ 0.5." |
| 6 | 🗺️ **Closest** | "Relative to real-options work on investment timing and discovery-driven planning, we focus on investor heterogeneity and prove conditions under which no equilibrium k* exists in the Murky Middle." |
| 7 | 🗄️ **Roadmap** | "Section 2 develops the heterogeneous payoff structure and k* non-existence result, Section 3 provides a calibrated deep-tech illustration drawing on Papers U and C, and Section 4 discusses strategic implications." |

---

### Chapter 2: Theory (9¶)

| ¶ | 내용 | 산출물 |
|:-:|:--|:--|
| 8 | **Lit: Real Options** — 불확실성 하에서 옵션가치, “wait option” (Dixit & Pindyck, Trigeorgis) | |
| 9 | **Lit: Newsvendor** — k* = F_D⁻¹(CR)에서 **Cᵤ, Cₒ가 exogenous이고 known**이라는 가정 명시 | |
| 10 | **Position**: Promise Vendor는 이를 **역전** – V와 투자자 조합으로부터 (Cᵤ, Cₒ)와 CR을 추론 | 🗄️ Comparison Table: Classic Newsvendor vs Promise Vendor |
| 11 | **Setup: Costs** — Cₒ (overage/too many options), Cᵤ (underage/too few options & lock-in) 정의, Paper C의 2.7× gap을 Cᵤ 캘리브라이션 앵커로 사용 | |
| 12 | **Investor Types**: Analyst (Cₒ 민감, S₂ 선호) vs Believer (Cᵤ 민감, S₂ 기피) | 🖼️ Fig 1: 2-Type Investor Payoff Schematic |
| 13 | **Payoff Functions**: π_A(k, S₂), π_B(k, S₂) 형태 설정 및 단조성/볼록성 가정 | |
| 14 | **Mixed Market**: π_M(k, S₂; α) = α·π_A + (1-α)·π_B, α를 투자자 조합 매개변수로 도입 | |
| 15 | **k* Non-existence**: S₂ ≈ 0.5, α ∈ (0,1)에서 ∂π_A/∂k와 ∂π_B/∂k 부호가 반대 → π_M의 내점 최적해 부재 증명 | 🖼️ Fig 2: No-Equilibrium Zone in (S₂, α) space |
| 16 | **Hypotheses**: H_N1 (CR↑ → 이론상 k*↑), H_N2 (S₂ ≈ 0.5 & mixed investors → 투자/옵션 선택 모두 억제) | |

---

### Chapter 3: Empirics / Calibration (11¶)

> **톤:** 여기서는 “강한 인과추론”이 아니라, Paper U & C에서 나온 실제 패턴과 Promise Vendor 이론이 **정합적으로 맞물리는지 보여주는 캘리브레이션/consistency check**임을 명시. :contentReference[oaicite:5]{index=5}

| ¶ | 내용 | 산출물 |
|:-:|:--|:--|
| 17 | **Context:** Paper C의 123,902개 패널에서 **Mobility vs Software**(sector_fe) 서브샘플을 추출하여, deep-tech가 상대적으로 높은 Cᵤ 환경임을 보여줌 (낮은 생존/성장, 높은 자본집약) | |
| 18 | **Sample:** Transportation·Hardware·Quantum 관련 키워드/sector를 추출한 deep-tech 서브샘플 (N ≈ 4k)와 비교군 소프트웨어 서브샘플 (N, 비율 명시) | 🗄️ Table 1: Sample by subsector (AV, EV, Fleet SaaS 등) |
| 19 | **Outcomes (DV):** 성장비율 Y = T/E, 후속자금 도달 여부(Series B+, L>0) – Paper C 정의 재사용 | |
| 20 | **Predictors (IV):** (i) S₂: Paper U의 V에서 S₂ = 1 - V로 변환, (ii) Flexibility proxy: |ΔV| quartile, (iii) sector/region별 규제·기술 불확실성 proxy를 통해 CR_high vs CR_low 그룹 정의 | 🗄️ Table 2: Variable construction & proxies |
| 21 | **Cost Calibration:** |ΔV| quartile 간 2.7× 성장 격차를 기준으로, Cᵤ/Cₒ의 합리적 범위를 역산하거나 시나리오별 CR grid 제시 (정확 수치보다는 “high vs low” 구획) | |
| 22 | **Descriptives:** subsector별 (AV, Fleet SaaS, EV 제조 등) S₂, |ΔV|, Y 분포를 요약하여, AV/딥테크에서 “높은 CR + 낮은 생존률” 패턴이 나타남을 서술 | 🗄️ Table 3: Descriptive stats by subsector |
| 23 | **Calibration Exercise:** AV (고 CR) vs Fleet SaaS (저 CR) 쌍을 선택, 각에 대해 이론적 k* 구간(k* ≈ 1-2 vs 4-5 등)을 도식적으로 제시하고, 실제 약속 텍스트에서 옵션 수 proxy(다중 use-case, 다중 기술 스택 언급 등)를 세어 alignment 여부 비교 | 🖼️ Fig 3: k* vs Observed “k-proxy” across subsectors |
| 24 | **Consistency Check 1:** “이론상 k*에 근접한 전략”(예: 고 CR+다중옵션, 저 CR+집중)을 택한 벤처들이 Y 및 Series B+ 도달에서 더 높은 성과를 보이는지, 로지스틱/회귀로 **정성적** 패턴 보고 (정량효과 크기는 보수적으로 해석) | 🗄️ Table 4: Alignment dummy → outcomes (no causal claim) |
| 25 | **Consistency Check 2 (Murky Middle):** S₂ ∈ [0.3, 0.7] & 투자자 혼합 proxy(라운드에 Analyst형/Believer형 VC가 함께 들어온 케이스)에서 **투자 규모와 후속투자 확률이 모두 낮은 영역**이 나타나는지 탐색 | 🖼️ Fig 4: Investment intensity over S₂, highlighting “no-investment zone” band |
| 26 | **Interpretation:** 위 패턴들을 통해, (i) deep-tech에선 Cᵤ가 우세한 CR-high regime임, (ii) CR-high regime에서 다중옵션 전략이 더 흔하고 성과도 더 좋다는 정합성, (iii) S₂ ≈ 0.5 영역에서 투자와 옵션 모두 위축되는 현상이, Promise Vendor 이론과 부합함을 논의 | |
| 27 | **Robustness:** S₂ 측정치 대안(Paper U의 다른 V 스케일), sector definition 변화, 옵션 proxy 정의(k-proxy alternative)를 바꿔도 정성적 결론이 유지되는지 보고 | |

---

### Chapter 4: Discussion (5¶)

| ¶ | 내용 |
|:-:|:--|
| 28 | **Link to Paper U:** V가 S₂로 변환되면서 Analyst/Believer 채널 선택을 결정하고, 극단(V≈0 또는 1)에서는 일관된 k*가 존재하는 반면, V≈0.5에서는 채널/투자자 혼선으로 k*가 붕괴됨을 연결 (U의 U-shape trough ↔ N의 k* 비존재) :contentReference[oaicite:6]{index=6} |
| 29 | **Link to Paper C:** Paper C에서 관측한 2.7× flexibility gap과 ρ(Y, |ΔV|)=0.159***를 Cᵤ의 경험적 lower bound로 해석하고, “자본이 옵션을 파괴한다”는 결과를 Cᵤ가 큰 regime의 특징으로 통합 | :contentReference[oaicite:7]{index=7} |
| 30 | **Practical: Rational FOMO:** Believer-type 투자자와 창업자의 ‘불안(FOMO)’을 비합리적 감정이 아니라, **Cᵤ가 큰 환경에서 k를 높이려는 베이지안 신호**로 재해석; 반대로 Analyst-type의 “precision anxiety”는 Cₒ가 큰 환경에서 k를 줄이려는 신호로 해석 |
| 31 | **Limitations:** (i) k 자체를 직접 관측하지 못해 proxy에 의존, (ii) Cᵤ/Cₒ를 정확히 식별하기보다 구간/시나리오 분석에 머무름, (iii) Murky Middle의 k* 비존재는 이론·시뮬레션 결과이며, 데이터는 정합성 수준에서만 지지함을 명확히 인정 |
| 32 | **Conclusion:** "In deep-tech venturing, the key question is not 'Should I focus?' but 'What is my CR?' — and in the Murky Middle where investor beliefs diverge, there may be **no stable k***, implying founders must choose a side rather than remain in ambiguous specificity." |

---

## 🔗 Three-Paper Integration (정리 버전)

```text
✌️U: V → S₂ (Specificity) → Investor Channel (Analyst vs Believer)
       ↓
🦾C: E → AOC(V) → C (Commitment Cost),
      calibrated via ρ(Y, |ΔV|)=0.159*** and a 2.7× flexibility gap
       ↓
🤹N: (S₂, Cᵤ, Cₒ) → CR = Cᵤ/(Cᵤ + Cₒ) → k* = F_D⁻¹(CR)
       ↓
       If S₂ ≈ 0.5 & mixed investors: k* UNDEFINED → No-Investment Zone

----
# Paper N: The Promise Vendor
## Table of Contents with Abstract, Figures, Tables
**Source of Truth:** `[[📢BULLETIN]]`
**Registry:** `[[🗄️REGISTRY]]`

---

## 📜 ABSTRACT

How should ventures balance FOMO (fear of missing out) with the need for focus? Lean Startup advocates "Build-Measure-Learn" with a single product ($k=1$), but in deep-tech environments where iteration costs are prohibitive ($C_u \gg C_o$), this prescription becomes fatal.

We introduce the **Promise Vendor Model** by adapting the Newsvendor framework to information economics. Just as traditional vendors optimize inventory against uncertain demand, founders should optimize their **portfolio of strategic options** ($k^*$) against uncertain market evolution:

$$k^* = F^{-1}(CR), \quad CR = \frac{C_u}{C_u + C_o}$$

Where $C_u$ is the cost of under-commitment (missed opportunities) and $C_o$ is the cost of over-commitment (wasted resources).

Analyzing the mobility sector, we show that AV ventures (high CR ≈ 0.9) optimally maintain $k^* = 4-5$ options, while Fleet Software ventures (low CR ≈ 0.3) should focus on $k^* = 1-2$. The "Murky Middle" (CR ≈ 0.5) has no stable equilibrium—ventures attempting mixture strategies satisfy neither Analyst nor Believer investors. Notably, Transportation ventures show an even stronger flexibility-growth relationship ($\rho = +0.236$) than the overall sample.

**Keywords:** Promise Vendor, Newsvendor Model, Critical Ratio, Option Portfolio, FOMO Dilemma

---

## 📑 TABLE OF CONTENTS

### Section 1: Introduction (¶75-81)
→ File: `[[section1(n)]]`

| ¶ | Role | First Sentence |
|:-:|:-----|:---------------|
| 75 | 📿 복음 | 린 스타트업: Build-Measure-Learn으로 k=1 빠르게 반복. |
| 76 | 🧩 퍼즐 | 딥테크에서는 반복 비용이 치명적 (Cᵤ >> Cₒ). |
| 77 | 😮 RQ | 반복 불가능 시, 불확실성 대처 전략은? |
| 78 | 🔎 렌즈 | Newsvendor 모델의 정보재 적용: Promise Vendor. |
| 79 | 😆 해법 | 최적 전략 = CR에 비례하는 k* 포트폴리오. |
| 80 | 🗺️ 인접 | McGrath (1997)와의 차별점. |
| 81 | 🗄️ 로드맵 | 2절 모델, 3절 검증, 4절 전략. |

### Section 2: Theory (¶82-90)
→ File: `[[section2(n)]]`

| ¶ | Role | First Sentence | Asset |
|:-:|:-----|:---------------|:------|
| 82 | 문헌: 뉴스벤더 | Arrow et al. (1951) — 수요 불확실성 하 최적 재고. | |
| 83 | 문헌: 정보재 | Shapiro & Varian (1999) — 버전닝. | |
| 84 | 문헌: 피벗 vs 포트폴리오 | 순차적 vs 병렬적 탐색. | |
| 85 | 갭 | k=1 (린) vs k=∞ (대기업) 이분법의 한계. | |
| 86 | 메커니즘: 과소/과잉 | Cᵤ (FOMO) vs Cₒ (Burn). | |
| 87 | 메커니즘: CR | Critical Ratio = Cᵤ / (Cᵤ + Cₒ). | |
| 88 | 계보: Arrow | k* = F⁻¹(CR) 변환. | |
| 89 | 모델 | π(k) = P·min(k,D) - C·k 최적화. | `[[🖼️N_S2_newsvendor]]` |
| 90 | 가설 | H₀: k*=1 vs H₁: k*>1 (CR 높을 때). | |

### Section 3: Empirics (¶91-101)
→ File: `[[section3(n)]]`

| ¶ | Role | First Sentence | Asset |
|:-:|:-----|:---------------|:------|
| 91 | 맥락 | 모빌리티 섹터: AV vs Fleet 비교. | |
| 92 | 표본 | AV(Waymo, Zoox) vs Fleet(Samsara, Motive). | |
| 93 | 측정: CR | AV: CR≈0.9 (승자독식), Fleet: CR≈0.3. | `[[🗄️N_S3_cr]]` |
| 94 | 측정: k | 동시 개발 기술 모듈 수. | |
| 95 | AV 분석 | AV k평균=5.2 → 높은 CR과 일치. | |
| 96 | Fleet 분석 | Fleet k평균=1.3 → 낮은 CR과 일치. | `[[🖼️N_S3_murky]]` |
| 97 | 성과 분석 | Starsky (k=1) 실패, 과다 옵션도 실패. | |
| 98 | 모델 적합도 | 관찰 k*와 예측 k* 간 **90%+ 상관**. | |
| 99 | 반사실적 | AV가 k=1 따랐다면 생존율 80% 감소. | |
| 100 | Transportation | **ρ(Y, \|ΔV\|) = +0.236*** — 유연성 효과 더 강함. | |
| 101 | 결론 | 최적 k*는 CR에 따라 유동적. | |

### Section 4: Discussion (¶102-106)
→ File: `[[section4(n)]]`

| ¶ | Role | First Sentence |
|:-:|:-----|:---------------|
| 102 | 공헌 1 | 린 스타트업 한계 증명: Cᵤ >> Cₒ면 "빠른 실패" = 실패. |
| 103 | 공헌 2 | Newsvendor의 전략 경영 도입: 정량적 불확실성 관리. |
| 104 | 공헌 3 | 전략적 모호성 = 고도의 **옵션 관리 역량**. |
| 105 | 한계 | CR 정확 측정의 어려움. |
| 106 | 결론 | 딥테크 창업자는 **Promise Vendor**가 되어야. |

---

## 🖼️ LIST OF FIGURES

| # | Module | Caption | Page |
|:-:|:-------|:--------|:----:|
| N.1 | `[[🖼️N_S2_newsvendor]]` | The Promise Vendor Model — Optimal Option Count | TBD |
| N.2 | `[[🖼️N_S3_murky]]` | The Murky Middle Zone — No Equilibrium | TBD |

---

## 🗄️ LIST OF TABLES

| # | Module | Caption | Page |
|:-:|:-------|:--------|:----:|
| N.1 | `[[🗄️N_S3_cr]]` | Critical Ratio by Industry | TBD |

---

## 📊 KEY NUMBERS (from [[📢BULLETIN]])

| Metric | Value |
|:-------|:------|
| AV optimal k* | 4-5 |
| Fleet optimal k* | 1-2 |
| AV CR | ≈ 0.9 |
| Fleet CR | ≈ 0.3 |
| Transportation ρ(Y, \|ΔV\|) | **+0.236*** |
| Model fit | r² > 0.90 |

---

## 📐 THE PROMISE VENDOR FORMULA

$$k^* = F^{-1}\left(\frac{C_u}{C_u + C_o}\right) = F^{-1}(CR)$$

**Where:**
- $k^*$ = Optimal number of strategic options
- $C_u$ = Under-commitment cost (FOMO)
- $C_o$ = Over-commitment cost (Burn)
- $CR$ = Critical Ratio
- $F$ = CDF of demand distribution

**Implications:**

| CR | Industry Type | Optimal k* | Strategy |
|:--:|:--------------|:----------:|:---------|
| 0.3 | Software | 1-2 | Focus |
| 0.5 | Mixed | Unstable | Avoid |
| 0.9 | Deep-tech | 4-5 | Portfolio |

---

## 🔗 CROSS-PAPER LINKS

| To Paper | Connection |
|:---------|:-----------|
| ← U | V determines investor type distribution D |
| ← C | AOC provides C and F measurements |

---

*Paper N managed by 🟠G + 🟢J*
*Verified by 🔴K*
