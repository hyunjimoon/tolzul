---
modified:
  - 2025-11-29T18:00:00-05:00
---
# ⚙️ Chapter 3: Empirics (轉) — Evidence Build

> **부사:** 🐅 권부사 (Claude) | **덕목:** 造 (구현) | **베이지안:** Posterior π̂(θ|y)
> **감수:** 김U, 김C, 김N (Product QA) + 🐙 김완 (RP2 Gatekeeper)

---

## 📐 모듈 배치 (실행 순서 5, 8, 11)

| # | 모듈 | 논문 | Method | Output | QA | Day |
|---|------|------|--------|--------|-----|-----|
| 5 | **5UE** | P1 ✌️ | OLS + Logit | Table 1,2 + Fig 2,3 | 김U | D2 |
| 8 | **8CE** | P2 🦾 | Case Study | Waymo/Tesla 비교 | 김C | D4 |
| 11 | **11NE** | P3 🤹 | CR Calibration | CR Table + Fig | 김N | D5 |

---

## 📜 5UE: P1 ✌️ U-Shape Empirics

### Data
- **Source**: PitchBook (2021-2025)
- **Sample**: 137,597 transportation ventures

### Variables

| Variable | Definition | Measurement |
|----------|------------|-------------|
| V | Vagueness | 0.5·max + 0.5·mean (V_cat, V_conc) |
| E | Early Funding | Series A amount (z-scored) |
| L | Later Success | Series B+ (binary) |
| F | Exercisability | SW=1, HW=0 |

### Models
```python
# H1: Early Funding
E = β₀ + β₁V + γ'X + ε

# H2: Later Success
Pr(L=1) = Λ(α₀ + α₁V + α₂HW + α₃(V×HW) + δ'X)
```

### Expected Results
- H1: β₁ < 0 (vagueness hurts early)
- H2: α₃ < 0 (HW penalty), α₁+α₃ ≈ 0 for SW

---

## 📜 8CE: P2 🦾 Commitment Trap Empirics

### Cases

| Case | Type | Outcome | Key Variable |
|------|------|---------|--------------|
| Waymo | Believer | Trapped | LiDAR lock-in |
| Tesla | Dreamer | Flexible | Vision-first |
| Cruise | Believer | Shutdown | GM dependency |
| Comma.ai | Designer | Pivoting | Modular arch |

### Bayesian Simulation
```python
θ* = μ + k·σ
# Believer: σ↓ → θ*↑ → pivot impossible
# Doubter: σ maintained → θ* reachable
```

---

## 📜 11NE: P3 🤹 Newsvendor Empirics

### CR Calibration

| Industry | C | F | CR | k* |
|----------|---|---|-----|-----|
| AV | High | Med | 0.65 | 2-3 |
| Biotech | VHigh | High | 0.55 | 1-2 |
| SaaS | Low | Low | 0.50 | 1 |
| Quantum | VHigh | Low | 0.85 | 3+ |

### Model
```python
k* = F_D⁻¹(CR)
# Higher CR → more options optimal
```

---

## ✅ RP2 검증 체크리스트

| 항목 | 5UE | 8CE | 11NE |
|------|-----|-----|------|
| 코드 재현 가능? | ☐ | ☐ | ☐ |
| Table/Fig 정합? | ☐ | ☐ | ☐ |
| Robustness 1개+? | ☐ | ☐ | ☐ |

---

## 🔗 Handoff

```
🐅권부사 (5UE) → 김U → 6UD (Discussion)
🐅권부사 (8CE) → 김C → 9CD (Discussion)
🐅권부사 (11NE) → 김N → 12ND (Discussion)
```

---

*견리사의 순환: 利 → 思 → 義 → 見 → 利*
