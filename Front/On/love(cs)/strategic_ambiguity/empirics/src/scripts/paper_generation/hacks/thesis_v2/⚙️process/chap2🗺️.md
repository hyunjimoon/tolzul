---
modified:
  - 2025-11-29T18:00:00-05:00
---
# 🗺️ Chapter 2: Theory (承) — Theory Build

> **부사:** 🐅 권부사 (Claude) | **덕목:** 思 (구조) | **베이지안:** Likelihood π(y|θ)
> **감수:** 김U, 김C, 김N (Product QA) + 🐙 김완 (RP1 Gatekeeper)

---

## 📐 모듈 배치 (실행 순서 4, 7, 10)

| # | 모듈 | 논문 | Core Theory | QA | Day |
|---|------|------|-------------|-----|-----|
| 4 | **4UT** | P1 ✌️ | Signaling × Real Options | 김U | D1 |
| 7 | **7CT** | P2 🦾 | Bayesian × Core Rigidity | 김C | D4 |
| 10 | **10NT** | P3 🤹 | Newsvendor × Coordination | 김N | D5 |

> **🐅권부사 직접 수행** (군졸 없음)

---

## 📜 4UT: P1 ✌️ Signaling × Real Options

### 가설

| ID | Statement | Expected |
|----|-----------|----------|
| **H1** | Vagueness → lower early funding | β₁ < 0 |
| **H2** | Vagueness × SW → higher later success | β_V×F > 0 |

### 이론적 기반

| 이론 | 핵심 주장 | 우리의 기여 |
|------|----------|------------|
| Akerlof (1970) | 정보 비대칭 → 역선택 | 조건부로 뒤집힘 |
| Baldwin & Clark (2000) | Modularity → 재조합 | Positioning vagueness |

### Figure 1: Conceptual Framework
```
V(Vagueness) ──────────────────→ Early Funding (−)
      │                              
      └──── × F(Modularity) ────→ Later Success (+)
```

---

## 📜 7CT: P2 🦾 Bayesian × Core Rigidity

### 핵심 공식
$$\theta^* = \mu + k \cdot \sigma$$

- **θ***: Switching threshold (pivot 결정 기준)
- **μ**: Prior mean (현재 전략 기대값)
- **σ**: Prior variance (불확실성)
- **k**: 요구되는 evidence 강도

### 가설

| ID | Statement | Mechanism |
|----|-----------|-----------|
| **H1** | Commitment → Reduced Pivot | Sunk cost inertia |
| **H2** | Believer Board → Higher θ* | σ↓ → threshold unreachable |

### Trap Mechanism
```
Early Success → Believers Join → σ↓ → θ*↑ → Pivot Impossible
```

---

## 📜 10NT: P3 🤹 Newsvendor × Coordination

### 통합 공식
$$k^* = F_D^{-1}\left(\frac{C}{C+F}\right) = F_D^{-1}(CR)$$

| 변수 | 원천 | 정의 |
|------|------|------|
| D | P1 | Modularity → outcome distribution |
| C/F | P2 | Belief structure → cost ratio |
| k* | P3 | Optimal number of options |

### 가설

| ID | Statement | Implication |
|----|-----------|-------------|
| **H1** | CR > 0.7 → k* ↑ | More options |
| **H2** | CR < 0.3 → k* ↓ | Commit early |

---

## ✅ RP1 검증 체크리스트

| 항목 | 4UT | 7CT | 10NT |
|------|-----|-----|------|
| 가설 검증 가능? | ☐ | ☐ | ☐ |
| 개념 정의 명확? | ☐ | ☐ | ☐ |
| P1-P2-P3 연결? | ☐ | ☐ | ☐ |
| 구조적 반론 1개? | ☐ | ☐ | ☐ |

---

## 🔗 Handoff

```
🐅권부사 (4UT) → 🐅권부사 (5UE) [P1 Empirics]
🐅권부사 (7CT) → 🐅권부사 (8CE) [P2 Empirics]
🐅권부사 (10NT) → 🐅권부사 (11NE) [P3 Empirics]
```

---

*견리사의 순환: 利 → 思 → 義 → 見 → 利*
