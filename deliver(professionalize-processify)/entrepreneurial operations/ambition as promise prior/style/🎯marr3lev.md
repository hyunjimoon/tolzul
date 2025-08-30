[[2025-08-08|25-08-08]], [[2025-08-15|25-08-15]], [[2025-01-23|25-01-23]]

# 🎯 Marr's Three Levels: Entrepreneurial Promise Architecture

## 1. Computation Level - What and Why

**Goal**: Design optimal entrepreneurial promise architectures (μ, τ) that balance resource mobilization against adaptive capacity under fundamental constraints

**Core Insight**: 
1. Not only marketing but also operations matters - promises must both attract resources AND be deliverable
2. Not only promise level but also precision matters - specificity determines learning capacity

**Input Variables**:
- Operational complexity: n (exponential delivery difficulty)
- Value structure: V_sd (sell & deliver), V_snd (sell & not deliver), V_ns (not sell)
- Information cost: c (evidence acquisition expense)
- Learning threshold: ε (minimum belief revision capacity)

**Output**: 
- Optimal belief architecture (μ*, τ*) where:
  - μ ∈ [0,1]: aspiration level (promise ambition)
  - τ ∈ [0,∞): precision parameter (promise specificity)

**Constraints**: Four interlocking forces shape feasible architectures
1. **Physical (P1)**: Operations bound feasibility through d(φ) = (1-φ)^n
2. **Financial (P2)**: Markets reward bold promises through p(φ) increasing
3. **Flexibility (P3)**: Learning requires |μ(t+1)-μ(t)| > ε/(τ+1)
4. **Precision (P4)**: Information costs C(τ) = c·ln(τ+1)

## 2. Algorithm Level - How

**Core Propositions**:

**Proposition 1 (Financial-Physical Balance)**: 
When V_snd ≈ V_ns and n=1: φ* = (V_sd - V_ns)/(V_sd - V_snd)
- Financial incentives alone drive toward maximum promises
- Physical constraints create interior optimum

**Proposition 2 (Physical Dominance)**:
When V_ns = V_snd = 0: φ* = 1/(n+1)
- Operational complexity n determines optimal promise level
- Higher complexity → more conservative promises

**Proposition 3 (Learning Trap)**:
Learning trap occurs when μ(1-μ) < ε(τ+1)
- High precision prevents belief revision
- Creates structural rigidity regardless of evidence

**Proposition 4 (Optimal Architecture)**:
Joint optimum: (μ*, τ*) = (1/(n+1), V·n/[c(n+1)²] - 1)
- Aspiration determined by operational complexity
- Precision determined by value/cost ratio

**Bayesian Update Mechanics**:
- Prior: Beta(μτ, (1-μ)τ)
- Update magnitude: Δμ ∝ 1/(τ+1)
- Critical threshold: τ_crit = μ(1-μ)/ε - 1

**Decision Process**:
1. Assess operational complexity n (cannot change)
2. Evaluate value structure V (market given)
3. Choose μ* = 1/(n+1) for optimal aspiration
4. Set τ* based on V/c ratio and evidence availability
5. Increase τ monotonically as evidence accumulates

## 3. Implementation Level - With What

**Model Architecture**: Five progressive models revealing constraint interactions

**Model 1 (Baseline)**:
- State: Binary {Success, Failure}
- Decision: None (promises irrelevant)
- Result: V₀ = p₀V_sd + (1-p₀)V_ns
- Insight: Null hypothesis - what if promises don't matter?

**Model 2 (Marketing Only)**:
- State: Binary with p(φ) = p₀ + αφ
- Decision: Promise level φ
- Result: φ* = 1 (corner solution)
- Insight: Financial incentives alone → maximum promises
- Implements: Pure persuasion dynamics

**Model 3 (Marketing + Operations)**:
- State: Ternary {Sell&Deliver, Sell&NotDeliver, NotSell}
- Decision: Promise level φ with d(φ) = (1-φ)^n
- Result: φ* = 1/(n+1)
- Insight: Physical reality creates interior optimum
- Implements: Propositions 1 & 2

**Model 4 (Add Flexibility)**:
- State: Distributional φ ~ Beta(μτ, (1-μ)τ)
- Decision: Aspiration μ (precision τ fixed)
- Result: Learning capacity μ(1-μ)τ⁻¹ ≥ L_min
- Insight: Extreme beliefs inhibit adaptation
- Implements: Proposition 3

**Model 5 (Full Architecture)**:
- State: Joint optimization over (μ, τ)
- Decision: Both aspiration and precision
- Result: (μ*, τ*) = (1/(n+1), max{0, V·n/[c(n+1)²] - 1})
- Insight: Precision as strategic investment
- Implements: Proposition 4

**Computational Framework**:
- Language: Probabilistic programming (Gen.jl/WebPPL)
- Core object: Beta(μτ, (1-μ)τ) belief distributions
- Interface: Natural language → (μ,τ) extraction → outcome simulation

**Empirical Validation**:
- Tesla: Adaptive trajectory τ: 5→12→25→40
- Nikola: Rigid τ≈100 from inception
- BetterPlace: High τ with honest μ → operational failure
- Theranos: High τ with dishonest μ → fraud

**Key Innovation**: 
Precision creates learning traps through mathematical mechanism—explaining both operational failure (honest high τ) and fraud (dishonest high τ) through identical structural rigidity.
