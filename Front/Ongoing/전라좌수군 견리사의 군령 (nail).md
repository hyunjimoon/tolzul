---
modified:
  - 2025-12-03T17:27:19-05:00
  - 2025-12-04T05:19:39-05:00
version: 3
---
# 견리사의 군령 v3.0

> 통제사: ⚓ 이순신 문현지 | 필사즉생: 12척 → 133척

---

## §1 Mission

**목표**: 3논문 × 32단락 = Management Science 게재

|   📦    | 논문                | 핵심 IP        | Target |
| :-----: | :---------------- | :----------- | :----- |
| [[U✌️]] | Vagueness Paradox | V(1-V) ≤ 0   | MS     |
| [[C🦾]] | Commitment Trap   | θ* = μ + kσ  | SMJ    |
| [[N🤹]] | FOMO Dilemma      | k* = F⁻¹(CR) | M&SOM  |

---

## §2 Flow: 오직 그대를 지키오

```
🔵 O (input) → 🟢 J (draft) → 🟠 G (structure) → 🔴 K (verify) → 🔵 O (archive)
     ↑________________________________________________↓
```

|   #   |                Agent                | Platform | Input    | Output             |   → To   |
| :---: | :---------------------------------: | :------: | :------- | :----------------- | :------: |
| 11-13 | [[11_OU🔵]]/[[12_OC🔵]]/[[13_ON🔵]] | Obsidian | 문헌       | papers-thesis.base |    J     |
|   8   |            [[08_JID🟢]]             |   GPT    | RQ, 문헌   | Intro Draft        | 06_GID🟠 |
|   9   |             [[09_JT🟢]]             |   GPT    | 가설       | Theory Draft       | 05_GT🟠  |
|  10   |             [[10_JE🟢]]             |   GPT    | 데이터      | Empirics Draft     | 04_GE🟠  |
|   6   |            [[06_GID🟠]]             |  Claude  | J Draft  | Intro Final        |    K     |
|   5   |             [[05_GT🟠]]             |  Claude  | J Draft  | Theory Final       |    K     |
|   4   |             [[04_GE🟠]]             |  Claude  | J Draft  | Code + Figures     |    K     |
|   1   |             [[01_KU🔴]]             |  Gemini  | G Output | ✌️U Approval       |    M     |
|   2   |             [[02_KC🔴]]             |  Gemini  | G Output | 🦾C Approval       |    M     |
|   3   |             [[03_KN🔴]]             |  Gemini  | G Output | 🤹N Approval       |    M     |
|   7   |         [[0_M_統/README\|M]]         |  Human   | K Output | 투고 승인              |    -     |

---

## §3 Products

### 통합 공식

$$k^* = F_D^{-1}\left(\frac{C}{C+F}\right)$$

| 변수 | 정의 | 논문 |
|:---|:---|:---:|
| V | 약속 모호성 [0,1] | ✌️U |
| C | Commitment cost | 🦾C, 🤹N |
| F | Flexibility cost | 🦾C, 🤹N |
| CR | C/(C+F) | 🤹N |
| D | Outcome distribution | ✌️U → 🤹N |

### ✌️U 핵심 실증 결과 (2024-12-04 검증완료)

**U-Shape 가설 확정**: 모든 산업에서 U-shape 패턴 확인 (χ² test, p < 0.001)

| Industry | N | Q1 (Low V) | Q2 | Q3 | Q4 (High V) | U-Shape Δ |
|:---|---:|---:|---:|---:|---:|---:|
| Transportation | 154,148 | 5.7% | 2.9% | 4.0% | 8.6% | +3.7pp |
| Software | 226,896 | 7.8% | 4.8% | 6.8% | 8.0% | +2.1pp |
| Hardware | 50,390 | 6.0% | 3.7% | 3.9% | 8.7% | +3.6pp |
| Pharma | 56,947 | 8.8% | 5.7% | 6.2% | 10.6% | +3.7pp |

**핵심 발견**:
- "Murky Middle" 패널티: 중간 모호성(Q2,Q3)이 극단(Q1,Q4)보다 생존율 2-4%p 낮음
- Transportation "Double Bind": High Capital × High Uncertainty → 가장 큰 U-shape 효과
- 비대칭 J-shape: Q4 > Q1 (High Vagueness가 더 유리)

**파일 위치**: `outputs/all/figures/fig_ushape_4panel_ms.pdf`

### 32단락 구조

| Ch | 단락 | Pod | Agents |
|:---:|:---:|:---:|:---:|
| Intro | 7 | ID | 08_JID🟢 ↔ 06_GID🟠 |
| Theory | 9 | T | 09_JT🟢 ↔ 05_GT🟠 |
| Empirics | 11 | E | 10_JE🟢 ↔ 04_GE🟠 |
| Discussion | 5 | ID | 08_JID🟢 ↔ 06_GID🟠 |

---

## §4 Rally Points

![[papers-thesis.base]]

| RP | Phase | Gatekeeper | 승인 조건 |
|:---:|:---|:---:|:---|
| 0 | Concept | J | Hook + RQ |
| 1 | Theory | G | 가설 정합성 |
| 2 | Empirics | G | 코드 재현성 |
| 3 | QA | K | MS-Fit 검증 |
| 4 | Integration | M | Ch.4 통합 |
| 5 | Submit | M | 투고 승인 |

---

## §5 Communication

| 신호 | 의미 |
|:---:|:---|
| 🇰🇷 | 승인 |
| 😆 | 돌파 |
| 🚨 | Veto |
| 🔴/🟡/🟢 | Critical/Important/Normal |

**언어**: 메타 🇰🇷, 산출물 🇺🇸

---

## Appendix

### A. Fleet

| 🎨 | Code | Folder | Role |
|:---:|:---:|:---|:---|
| 🌙 | M (7) | [[0_M_統]] | 통제사 |
| 🔵 | O (11-13) | [[1_O_見]] | DB |
| 🟢 | J (8-10) | [[3_J_利]] | 빠른실행 |
| 🟠 | G (4-6) | [[2_G_思]] | 구조화 |
| 🔴 | K (1-3) | [[4_K_義]] | 검증 |

### B. Visuals

![[13_agent_matrix.svg]]
![[FLEET.base]]

### C. 학술 근거

MIT Product Design & Development (Ulrich & Eppinger):
- Complex System Development → 3논문 병렬
- Heavyweight PM → 통제사
- Rally Points → RP0-5

---

*필사즉생 (必死卽生)*
