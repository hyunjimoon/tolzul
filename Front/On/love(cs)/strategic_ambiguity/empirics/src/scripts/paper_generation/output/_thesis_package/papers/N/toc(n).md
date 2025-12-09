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
