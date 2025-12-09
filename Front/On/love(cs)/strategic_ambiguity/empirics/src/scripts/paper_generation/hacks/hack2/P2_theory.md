# P2: Competency Trap - When Success Kills Options

## Core Theory: Real Options x Core Rigidity x Bayesian Learning

### 권준 🐅 (承 - Structure Builder)

---

## 1. Theoretical Foundation

### 1.1 Capabilities as Real Options

**Kogut & Kulatilaka (2001)**: Capabilities have value because they create options for future strategic moves.

**However**, this view underspecifies when options become **unexercisable**.

### 1.2 Core Rigidity and the Success Trap

**Leonard-Barton (1992)**: Core rigidity - the same capabilities that drive success become liabilities when environments shift.

**Henderson & Clark (1990)**: Architectural innovation disrupts incumbents not through superior components but through new linkages.

**However**, these frameworks don't explain why startups - supposedly nimble - fall into the same trap.

### 1.3 Bayesian Learning and Belief Lock-in

We propose a **Bayesian mechanism**:
- Early success generates high μ, low σ priors about the current path
- Like-minded investors reinforce these beliefs
- The posterior update threshold rises
- Pivots become increasingly unlikely even as evidence mounts

**Key insight**: The trap is not technical but **epistemic**. Founders and boards converge on shared beliefs that make alternative evidence dismissible.

---

## 2. Conceptual Framework: Belief-Reinforcing Capital Structures

```
Early Commitment → High Performance → Believer Investors
       ↓                                      ↓
  Low σ Priors ← ← ← ← ← ← ← ← ← ← ← Reinforced Beliefs
       ↓
  High Switching Threshold
       ↓
  Unexercisable Pivot Options
```

---

## 3. Hypotheses

### H1: Commitment → Reduced Pivot Probability
High initial commitment → reduced pivot probability

### H2: Believer Composition → Higher Threshold
Like-minded investor composition → higher switching threshold

### H3: Paradigm Shift Amplifies
Technology paradigm shift amplifies commitment penalty

---

## 4. Key Variables

| Variable | Symbol | Definition |
|----------|--------|------------|
| Prior Mean | `μ₀` | Initial belief about current path value |
| Prior Uncertainty | `σ₀` | Initial uncertainty (variance) |
| Evidence Strength | `e` | Strength of disconfirming evidence |
| Believer Ratio | `r` | Proportion of like-minded investors |
| Switching Threshold | `τ` | Evidence required to trigger pivot |

---

## 5. Bayesian Update Model

### Prior Distribution
```
θ ~ N(μ₀, σ₀²)
```

### Likelihood (Evidence)
```
y | θ ~ N(θ, σ_e²)
```

### Posterior Update
```
μ_post = (σ_e² * μ₀ + σ₀² * y) / (σ₀² + σ_e²)
σ_post² = (σ₀² * σ_e²) / (σ₀² + σ_e²)
```

### Switching Threshold
```
τ = f(σ₀, r)

where:
- Low σ₀ → High τ (confident priors resist update)
- High r → High τ (homogeneous boards amplify)
```

---

## 6. Simulation Parameters

| Parameter | Low Commitment | High Commitment |
|-----------|---------------|-----------------|
| μ₀ | 0.5 | 0.8 |
| σ₀ | 0.3 | 0.1 |
| Believer ratio | 0.3 | 0.8 |
| Switching threshold | 0.3 | 0.7 |

---

*Commander: 권준 🐅 | Virtue: 思 (Structure) | Bayesian Role: Likelihood π(y|θ)*
