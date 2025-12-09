# 🤹N: Promise Vendor — Theory
## Chapter 2: Theory

**Version:** 2.0 (Promise Vendor framing)
**Core Gap:** News Vendor assumes known C, F. We provide **prediction method**.

---

## ¶8. Literature Gap 1: Real Options Assumes Known Costs

Real options theory (McGrath 1999, Adner 2002) establishes that options have value. But:

> **Gap**: Options literature assumes C (commitment cost) and F (flexibility cost) are **known** or **estimable from past data**.

Startups have no past. They cannot calibrate costs from historical demand patterns.

---

## ¶9. Literature Gap 2: Newsvendor Requires Past Data

The classic newsvendor model:
$$q^* = F^{-1}\left(\frac{C_u}{C_u + C_o}\right)$$

Where C_u (underage) and C_o (overage) come from **historical demand data**.

> **Gap**: Startups have **no past demand data** and **no price history**. How do they estimate C, F?

---

## ¶10. Our Position: Promise Vendor

We propose **Promise Vendor** — a forward-looking newsvendor:

| | News Vendor (Literature) | Promise Vendor (Ours) |
|:---|:---|:---|
| **Time** | Past → Present | **Future → Present** |
| **Input** | Historical demand | **Future promises (V)** |
| **C, F** | Known from data | **Predicted from V** |
| **Contribution** | Optimal q* | **C, F prediction method** |

### The Core Insight

```
V (Vagueness/Promise) → Investor composition → σ (belief variance)
    ↓
Low V → Like-minded investors → σ↓ → C↑ (lock-in)
High V → Diverse investors → σ maintained → F↑ (coordination)
```

---

## ¶11. Setup: C (Commitment Cost) and F (Flexibility Cost)

### Commitment Cost (C) — From 🦾C

From 🦾C, we have an **empirical estimate**:
- **C = -2.5×** per funding decile (the cost of lock-in)
- **8.8× gap** between Escape Velocity and Golden Cage

**Components of C**:
- Lock-in to inferior technology (cannot pivot)
- Sunk CAPEX in specific capabilities
- Belief homogeneity (σ↓) making pivots impossible

### Flexibility Cost (F) — Easier to Observe

**Components of F**:
- Late entry penalty (market share decay)
- Option maintenance overhead (parallel R&D)
- Coordination costs across paths

**Key insight**: F is more observable than C. C requires **counterfactual** estimation.

---

## ¶12. Critical Ratio: CR = C/(C+F)

$$CR = \frac{C}{C+F}$$

| CR | Interpretation | Strategy |
|:---|:---|:---|
| CR → 0 | C low, F high | Commit early (flexibility expensive) |
| CR = 0.5 | Balanced | Moderate options |
| CR → 1 | C high, F low | Many options (commitment dangerous) |

**FOMO Interpretation**:
- FOMO = perception that CR is high
- "저것도 해야 할 것 같아" = "C가 높아 보인다"

---

## ¶13. Optimal k* Derivation

From newsvendor logic:
$$k^* = F_D^{-1}(CR) = F_D^{-1}\left(\frac{C}{C+F}\right)$$

Where D is the distribution of option values (from ✌️U's vagueness distribution).

### Three-Paper Integration

| Paper | Contribution | Variable |
|:---|:---|:---|
| ✌️U | Vagueness distribution | **D** |
| 🦾C | Commitment cost estimate | **C = -2.5×** |
| 🤹N | Optimal formula | **k* = F_D⁻¹(CR)** |

---

## ¶14. π(D): Belief Distribution Over Paths

The distribution D comes from ✌️U's insight:
- **Low V** (precise): Narrow distribution → k*↓
- **High V** (vague): Wide distribution → k*↑

**Promise → Distribution**:
```
V → D (shape of outcome uncertainty)
V → C/F (cost structure through investor selection)
```

---

## ¶15. Boundary Conditions

| Condition | k* | Interpretation |
|:---|:---:|:---|
| CR = 0 | k* = 0 | Pure commitment (no options needed) |
| CR = 0.5 | k* = median | Balanced portfolio |
| CR = 1 | k* = max | Maximum optionality |

**Extreme cases**:
- **Pure analyst** (Low V, Low C): k* → 1 (commit)
- **Pure believer** (High V, Low F): k* → many (explore)

---

## ¶16. Hypotheses

### H1: FOMO = C↑ Signal

> Founders who experience FOMO are perceiving high commitment costs.

**Test**: FOMO intensity correlates with industry CR.

### H2: CR Predicts k*

> Industries with higher CR have firms with more strategic options.

**Test**: AV (high CR) vs SaaS (low CR) option counts.

### H3: Promise Vendor Outperforms Naive Commitment

> Firms that estimate C from V (Promise Vendor) outperform firms that commit blindly.

**Test**: Survival analysis by CR-awareness.

---

## Role in Trilogy

```
✌️U → D (distribution)
      ↓
🦾C → C = -2.5× (commitment cost)
      ↓
🤹N → k* = F_D⁻¹(C/(C+F))
```

**Punchline**: *"스타트업은 과거가 없다. 미래 약속(V)으로 C, F를 예측하라."*

---

*Ready for Empirics (¶17-27): C, F calibration from 🦾C data.*
