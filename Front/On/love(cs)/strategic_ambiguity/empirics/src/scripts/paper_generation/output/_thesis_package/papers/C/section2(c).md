---
title: When Commitment Becomes a Cage - Theory
version: 5.0 (Mechanism chain: dY/dE = (+)(−))
core_mechanism: E → |ΔV| → Y
modified:
  - 2025-12-04T15:00:00-05:00
---

# Chapter 2: Theory

## ¶8. Literature Gap 1: RBV Assumes Flexible Deployment

The Resource-Based View (Barney 1991) predicts: **more resources → better outcomes**. Early funding (E) provides runway, signals quality, attracts talent.

**Gap**: This assumes resources are deployed flexibly. It ignores the **commitment constraints** accompanying resource acquisition—the promises made to secure funding become chains.

---

## ¶9. Literature Gap 2: Real Options Lacks Empirical Measure

Real options theory (McGrath 1999) establishes that **flexibility has value** under uncertainty. The "option to pivot" may be a startup's most valuable asset.

**Gap**: While option value is conceptually understood, there is no accepted **empirical measure** of strategic flexibility, nor estimates of the **cost of premature commitment**.

---

## ¶10. Literature Gap 3: Org Learning Ignores Capacity Reduction

Organizational learning (Levitt & March 1988) focuses on *what* organizations learn. Less attention on **learning capacity**—the ability to update beliefs when evidence contradicts current strategy.

**Gap**: We lack understanding of how **resource accumulation reduces learning capacity**.

---

## ¶11. Our Position: E → |ΔV| → Y

We fill these gaps with a simple causal chain:

```
E (Early Funding) → |ΔV| (Strategic Flexibility) → Y (Outcome)
        ↓                      ↓                        ↓
   Lock-in effect         Adaptation capacity      L/E ratio
```

**New Notation** (money as flow, not stock):
- **E** = Early funding (first_financing_size)
- **L** = Later funding = Total_2025 - E
- **V_E** = Vagueness at early stage (V_2021)
- **V_L** = Vagueness at later stage (V_2025)
- **|ΔV|** = |V_L - V_E| (strategic flexibility)
- **Y** = L/E (later funding growth ratio)

| This Paper | Literature Gap | Our Contribution |
|:-----------|:---------------|:-----------------|
| **E → |ΔV|** | RBV ignores commitment cost | Quantify lock-in (ρ = -0.117***) |
| **|ΔV| measure** | Real Options lacks metric | |ΔV| = |V_L - V_E| |
| **|ΔV| → Y** | Org Learning ignores capacity | Flexibility → 8.8× better outcomes |

---

## ¶12. Mechanism: The Chain Effect

**Core Equation** (see [[fig1_mechanism_3panel.png]]):

$$\frac{dY}{dE} = \underbrace{\frac{dY}{d|\Delta V|}}_{(+)} \times \underbrace{\frac{d|\Delta V|}{dE}}_{(-)} = (+)(-) < 0$$

**Why does E reduce |ΔV|?**

```
High E (Early Funding)
    ↓
Specific Promise to Investors
    ↓
Like-minded Stakeholders Attracted
(employees, partners, board who share the vision)
    ↓
τ↑ (Belief Precision Increases)
Posterior: N(μ, σ²/τ) — more certain, not more accurate
    ↓
LC↓ (Learning Capacity Decreases)
Weight on new evidence: 1/(1+τ) → 0
    ↓
Pivot Probability↓
Threshold θ* = μ + kσ becomes unreachable as σ→0
    ↓
|ΔV|↓ (Strategic Flexibility Decreases)
```

**Key insight**: The trap is **epistemic**, not technical. Pivots become mathematically impossible when belief variance collapses—regardless of available resources.

### The 3-Panel Evidence

| Panel | Relationship | Finding | Interpretation |
|:---|:---|:---|:---|
| **(A)** | d|ΔV|/dE | < 0 | Funding reduces flexibility |
| **(B)** | dY/d|ΔV| | > 0 | Flexibility increases outcomes |
| **(C)** | dY/dE | < 0 | Combined: (+)(−) = (−) |

---

## ¶13. H_cost: The Core Hypothesis

From the mechanism, we derive:

> **H_cost (Cost of Commitment)**: Conditioning on same early funding E, locked-in ventures underperform flexible ventures.

$$\text{Cost} = E[Y | \text{Locked}, E] - E[Y | \text{Flexible}, E] < 0$$

**Operationalization**:
- Locked = |ΔV| ≤ median (low strategic change)
- Flexible = |ΔV| > median (high strategic change)
- E = Early funding level (matching variable)
- Y = L/E = (Total_2025 - E) / E

**Prediction**: Cost is negative across all funding deciles (see [[fig2_cost_by_decile.png]]). Lock-in hurts at every resource level.

---

## ¶14. H_supporting: Lock-in Correlation

As supporting evidence for the mechanism:

> **H_supporting**: Early funding is negatively correlated with strategic flexibility.

$$\text{Corr}(E, |ΔV|) < 0$$

**Prediction**: ρ < 0, significant at p < 0.001.

This validates the first link (E → |ΔV|) in our causal chain.

---

## Summary: The Tight Chain

| Link | Question | Hypothesis | Measure |
|:-----|:---------|:-----------|:--------|
| **E → |ΔV|** | Does funding lock you in? | H_supporting | ρ(E, |ΔV|) = -0.117*** |
| **|ΔV| → Y** | Does flexibility pay off? | **H_cost** | Escape 3.32× vs Cage 0.38× |

Everything else is supporting detail. The paper lives or dies on **H_cost: 8.8×**.

---

*"dY/dE = dY/d|ΔV| × d|ΔV|/dE = (+)(−) < 0. The trap is epistemic."*
