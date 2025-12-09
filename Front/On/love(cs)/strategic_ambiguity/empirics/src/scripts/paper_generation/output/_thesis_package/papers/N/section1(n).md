# 🤹N: Promise Vendor — Optimal Number of Options
## Chapter 1: Introduction

**Version:** 2.0 (Promise Vendor framing)
**Core Contribution:** C, F 예측 방법론 (미래 → 현재)

---

## Abstract

The newsvendor model optimizes inventory using **past demand data** to estimate costs. But startups have no past. How do they decide how many strategic options to maintain?

We introduce the **Promise Vendor** model: entrepreneurs use **future promises** (strategic positioning vagueness V) to predict commitment costs (C) and flexibility costs (F), then optimize option count k*. Using 🦾C's commitment cost estimate (Cost = -2.5× per funding decile), we show that **FOMO is a rational Bayesian signal** — anxiety about missing alternatives reflects high perceived C.

$$k^* = F_D^{-1}\left(\frac{C}{C+F}\right)$$

---

## ¶1. Gospel (H₀): News Vendor — 과거가 현재를 결정

> **The Newsvendor Gospel**: With historical demand data, we know underage cost (C_u) and overage cost (C_o). The optimal inventory q* = F⁻¹(C_u/(C_u+C_o)).

This model assumes costs are **known** from past experience. The critical ratio CR = C_u/(C_u+C_o) is observable.

**Problem**: Startups have no past. How do they estimate C and F?

---

## ¶2. Puzzle: 스타트업은 과거가 없다

In the AV industry:
- **Waymo**: High commitment (LiDAR-first), massive funding, locked in
- **Tesla**: High commitment (vision-only), but different bet
- **Comma.ai**: Low commitment, maintained flexibility, pivoted successfully

Traditional newsvendor logic cannot explain why low-resource Comma.ai outperformed billion-dollar Waymo. The costs C, F were **not known in advance** — they emerged from strategic choices.

**The puzzle**: Without historical data, how do startups decide how many options (k) to maintain?

---

## ¶3. RQ: 미래 약속으로 C, F를 예측할 수 있는가?

> **Research Question**: Can future promises (strategic positioning V) predict commitment and flexibility costs?

From 🦾C, we know:
- High early funding (E↑) → Lock-in → |ΔV|↓ → Y↓
- **Commitment Cost = -2.5×** per decile (quantified!)

This suggests V → C is estimable. The question is: **How?**

---

## ¶4. Lens: Promise Vendor — 미래 → 현재

We propose the **Promise Vendor** model:

| | News Vendor (H₀) | Promise Vendor (H₁) |
|:---|:---|:---|
| **시간 방향** | 과거 → 현재 | **미래 → 현재** |
| **입력** | 과거 수요 데이터 | **미래 약속 (V)** |
| **C, F** | 알려진 값 | **V로부터 예측** |

**Mechanism**:
```
V (Vagueness/Promise) → Investor composition → σ (belief variance)
    ↓
Low V (precise promise) → Like-minded investors → σ↓ → C↑ (lock-in cost)
High V (vague promise) → Diverse investors → σ maintained → F↑ (coordination cost)
```

---

## ¶5. Solution: FOMO = C↑ Signal

**Core Result**:

$$k^* = F_D^{-1}\left(\frac{C}{C+F}\right)$$

Where:
- **D** = Vagueness distribution (from ✌️U)
- **C** = Commitment cost = -2.5× (from 🦾C)
- **F** = Flexibility cost (coordination overhead)

### FOMO as Bayesian Signal

```
FOMO 발동: "저것도 해야 할 것 같아"
    ↓
옵션 +1 요구
    ↓
= Underage cost 높다고 인식
    ↓
= Commitment Cost (C) ↑
    ↓
CR ↑ → k* ↑
```

**Insight**: FOMO is not irrational. It's a **Bayesian signal that C is high**.

| CR Range | k* | Strategy | FOMO Level |
|:---|:---:|:---|:---|
| CR < 0.3 | Low | Commit early | Low (C is low) |
| 0.3 < CR < 0.7 | Medium | Balanced | Moderate |
| CR > 0.7 | High | Many options | High (C is high) |

---

## ¶6. Positioning: Closest Papers

| Paper | Focus | Gap We Fill |
|:---|:---|:---|
| Adner (2002) | Real options value | **When to exercise** (not how many) |
| McGrath (1999) | Option thinking | **No cost estimation** method |
| Kogut & Kulatilaka (2001) | Platform options | **Assumes known costs** |

**Our contribution**: Method to **predict** C, F from V (future promises).

---

## ¶7. Roadmap

| Chapter | Content | Key Output |
|:---|:---|:---|
| [[chap2_theory]] | Promise Vendor model derivation | k* = F_D⁻¹(CR) |
| [[chap3_empirics]] | C, F calibration from 🦾C data | CR by industry |
| [[chap4_discussion]] | Three-paper integration | Unified framework |

---

## Connection to Trilogy

```
✌️U → D (Vagueness distribution: which V levels succeed?)
      ↓
🦾C → C = -2.5× (Commitment cost: what's the lock-in penalty?)
      ↓
🤹N → k* = F_D⁻¹(C/(C+F)) (Optimal options: how many to hold?)
```

**Punchline**: *"FOMO는 C가 높다는 Bayesian signal. 불안은 생존 본능이다."*

---

*Ready for Theory development (¶8-16).*
