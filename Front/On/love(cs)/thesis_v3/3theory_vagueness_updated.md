# Conceptual Model: Entrepreneur's Partial Commitment (EPC)

## 📋 Executive Summary (Plain English)

**The Big Question**: Should startups be vague or specific when pitching to investors?

**What Everyone Thinks**: 
- Investors say: "Be specific so we can evaluate you"
- Advisors say: "Stay flexible so you can adapt"
- Nobody agrees on which is right

**What We Found**: It depends on how easily you can change direction later
- **Software startups** can change direction cheaply (just rewrite code) → Being vague is OK
- **Hardware startups** can't pivot easily (factories, tools, regulations) → Must be specific
- Think of it like dating: if you can easily break up (software), keeping options open makes sense. If divorce is expensive (hardware), better be sure upfront.

**The Surprise**: Being vague doesn't actually help anyone—it just hurts hardware companies MORE than software companies. VCs already know this intuitively but apply the wrong medicine: they demand even MORE specificity from hardware startups, making their situation worse.

**Why This Matters**: We're systematically killing hardware startups by forcing them to commit too early when they most need flexibility. This explains why software eats the world—not because it's inherently better, but because the funding system is biased toward software's ability to be vague.

---

## 1. Core Framework: Strategic Vagueness as Design Choice

### 1.1 The Central Tension

Entrepreneurs face a fundamental design problem when communicating with stakeholders. Their promises must serve **dual purposes**: 

1. **Evaluation Device**: Enable investors to assess quality and monitor progress (Information value)
2. **Exploration Tool**: Preserve flexibility to discover optimal strategies (Option value)

We model promise vagueness V ∈ [0,1] as an **endogenous choice variable** that entrepreneurs optimize based on their venture's characteristics. Unlike prior work treating vagueness as incompetence, we show that optimal vagueness V* emerges from balancing information costs against coordination savings.

### 1.2 Visual Framework: The Vagueness-Performance Space

```
Performance
    ↑
    │      ___Software Peak
    │     /   \  (High exercisability)
    │    /     \
    │   /       \___
    │  /            \Hardware Peak
    │ /              (Low exercisability)  
    │/_______________
    └────────────────→
     0    V*₁  V*₂   1
         Promise Vagueness (V)

Key insight: V*software > V*hardware
Software ventures optimize at higher vagueness due to higher exercisability
```

### 1.3 Formal Model Setup

Consider an entrepreneur choosing vagueness V to maximize expected value across two periods:

**Period 1 (Funding Stage):**
- Entrepreneur chooses vagueness level V
- Investors observe V and form beliefs about quality θ
- Funding F(V) = α₀ - α₁·IC(V) where IC(V) = -log(1-V) is information cost

**Period 2 (Execution Stage):**
- True market state θ revealed
- Venture can pivot with coordination savings CS(V,F) = V²·F where F is exercisability
- Success probability S(V,F) = Φ(match(V,θ,F))

**Optimization Problem:**
```
max Π(V) = F(V) + δ·S(V,F) + CS(V,F)
   V

First-order condition:
∂Π/∂V = -α₁/(1-V) + 2V·F + δ·∂S/∂V = 0

Solution:
V*(F) = F/(1+F)
```

This yields our central prediction: **optimal vagueness increases with exercisability**.

## 2. Mechanism: How Vagueness Preserves Value

### 2.1 The Consideration Set Channel

Vagueness preserves what we call the **"consideration set"**—the range of strategic trajectories available for exploration:

```
Consideration Set Size: Ω(V) = V·K
where K = total possible strategies
```

Larger consideration sets enable three advantages:

1. **Parallel Experimentation**: Test multiple hypotheses simultaneously
2. **Market Discovery**: Observe which segments respond most strongly  
3. **Combinatorial Innovation**: Recombine elements from different trajectories

### 2.2 The Coordination Cost Channel

Vagueness reduces coordination friction through **deferred commitment**:

```
Coordination Savings: CS(V,F) = V²·F
where F = exercisability
```

When exercisability is high, vagueness prevents premature lock-in with stakeholders. This explains why software ventures can sustain higher vagueness without penalty.

### 2.3 The Exercisability Moderator

The net value of vagueness depends critically on exercisability F, which we decompose into experiment cost (c) and pivot cost (k):

| Component | Software (Low c, Low k) | Hardware (High c, High k) | 
|-----------|------------------------|---------------------------|
| **Experiment Cost** | $ (Cloud computing) | $$$ (Prototypes, tooling) |
| **Pivot Cost** | k ≈ 0 (Modular code) | k ≈ 1 (Manufacturing lock-in) |
| **Persuasion Gap** | Tolerance for vagueness | Demand for precision |
| **Optimal V*** | 0.7-0.9 | 0.1-0.3 |

**From your heatmap insight:**
```
When c ↓ and k ↑ (top-left yellow zone):
- Theory says V* should be HIGH (maintain flexibility)
- But VCs force LOW V (demand precision)
- This is the market failure!
```

## 3. Hypothesis Development: From Theory to Testing

### 3.1 Main Effects

**H1: Early-Stage Effect (Information Cost)**
```
Hypothesis: ∂E/∂V ≤ 0
Mechanism: Higher V → Lower information value → Potentially reduced funding
Prediction: β₁ ≤ 0 in E = β₀ + β₁·V + Controls
Finding: β₁ ≈ 0 (no effect!)
```

**H2: Later-Stage Effect (Coordination Savings)**
```
Hypothesis: ∂L/∂V|F=1 > ∂L/∂V|F=0
Mechanism: Higher V → Better pivoting ability when F high
Prediction: β₃ > 0 in L = β₀ + β₁·V + β₂·F + β₃·V×F
Finding: β₃ > 0 but both slopes negative (attenuation, not reversal)
```

### 3.2 The Market Failure Hypothesis

**H3: Systematic Misallocation**
```
Theory predicts: V*hardware = F/(1+F) ≈ 0.3-0.4 (moderate vagueness)
VCs demand: V ≈ 0.1-0.2 (high precision)
Gap: ΔV ≈ 0.2 suboptimal reduction in flexibility
Result: Higher failure rates for hardware ventures
```

### 3.3 Connecting to Stern's Framework

| Stern Strategy | Experiment Cost | Pivot Cost | Optimal V* | VC Practice | Gap |
|----------------|----------------|------------|------------|-------------|-----|
| **Disruption** | Low | Low | 0.8 | Allows V≈0.7 | Small |
| **Value Chain** | Low | Medium | 0.5 | Forces V≈0.4 | Moderate |
| **IP Strategy** | High | High | 0.6 | Forces V≈0.2 | **Large** |
| **Architectural** | Very High | Very High | 0.3 | Forces V≈0.1 | **Severe** |

## 4. Measurement Strategy

### 4.1 Operationalizing Vagueness

We develop a **Strategic Vagueness Index (SVI)** combining three dimensions:

```python
# Computational measurement
SVI = w₁·Categorical_Ambiguity + w₂·Concreteness_Deficit + w₃·Temporal_Flexibility

where:
- Categorical_Ambiguity = 1 - max(category_probability)
- Concreteness_Deficit = 1 - (concrete_words/total_words)
- Temporal_Flexibility = 1 - (time_commitments/total_commitments)
```

### 4.2 Measuring Exercisability from Your Framework

Based on your images:
```
F = f(1/c, 1/k) where:
- c = experiment cost ($ for software, $$$ for hardware)
- k = pivot cost (≈0 for software, ≈1 for hardware)
```

## 5. Empirical Context: Why Transportation?

The transportation sector provides ideal variation for testing our framework:

1. **Clear c-k variation**: Apps (low-low) vs EVs (high-high)
2. **Observable pivots**: Uber (rides→food), Cruise (delay after accident)
3. **Market shocks**: COVID forcing pivots, revealing true flexibility
4. **VC bias visible**: Hardware ventures get less funding despite higher capital needs

### 5.1 Sample Construction

| Criterion | Specification | N Excluded | N Remaining |
|-----------|--------------|------------|-------------|
| **Universe** | All transportation ventures | - | 157,234 |
| **Time Window** | Founded 2010-2020 | 19,637 | 137,597 |
| **Activity** | Raised Seed or Series A | 85,234 | 52,363 |
| **Data** | Non-missing descriptions | 10,051 | 42,312 |

**Key Split for Analysis:**
- Software (Low c, Low k): 23,847 ventures → Optimal V* ≈ 0.8
- Hardware (High c, High k): 18,465 ventures → Optimal V* ≈ 0.3
- **Gap**: Hardware forced to V ≈ 0.15 (overconstrained by ~50%)

## 6. Econometric Specification

### 6.1 Testing for Market Failure

**Model A: Early Funding**
```
log(Series_A)ᵢ = β₀ + β₁·Vᵢ + β₂·Hardwareᵢ + β₃·Vᵢ×Hardwareᵢ + Controls
```
Expected: β₃ < 0 (hardware penalized more for vagueness)

**Model B: Later Success**
```
Pr(Series_B+)ᵢ = Λ(α₀ + α₁·Vᵢ + α₂·Hardwareᵢ + α₃·Vᵢ×Hardwareᵢ + Controls)
```
Expected: α₃ < 0 (hardware suffers more from forced precision)

**Model C: Optimal Distance Test**
```
Performanceᵢ = γ₀ + γ₁·|Vᵢ - V*ᵢ| + γ₂·Hardwareᵢ + Controls
where V*ᵢ = Fᵢ/(1+Fᵢ)
```
Expected: γ₁ < 0 (deviation from optimum hurts performance)

## 7. Results Interpretation with Your Framework

Our empirical patterns now make sense through your experiment/pivot cost lens:

1. **No Early Penalty** (β₁ ≈ 0): Early investors can't distinguish strategic vagueness from confusion

2. **Differential Later Penalty**:
   - Software (low c, low k): -4.1% per unit V → Can explore efficiently
   - Hardware (high c, high k): -7.8% per unit V → Exploration too expensive

3. **The Market Failure**: Hardware needs V* ≈ 0.3-0.4 but forced to V ≈ 0.15
   - Overconstrained by ~50%
   - Can't run enough experiments before committing
   - Your heatmap shows they're in the YELLOW zone (should be vague) but treated like PURPLE (forced precise)

## 8. Theoretical Implications

### 8.1 From Scenario Planning to Consideration Sets
**Old View**: Pre-define scenarios, wait for reveal
**Our View**: Choose scenario count via vagueness, actively eliminate through experiments

### 8.2 From Static to Dynamic Optimization
**Old View**: Choose precision once
**Our View**: V evolves as V(t) = V₀ - λ·experiments_run(t)

### 8.3 From Universal to Contingent Advice
**Old View**: "Be clear" or "Stay flexible"
**Our View**: V* = F/(1+F) - calibrate to your architecture

### 8.4 The Core Market Failure
**VCs systematically disadvantage ventures that need flexibility most** (high c, high k), creating opportunity for new frameworks that correct this misallocation. Hardware ventures are forced into premature commitment precisely when the option value of vagueness is highest.