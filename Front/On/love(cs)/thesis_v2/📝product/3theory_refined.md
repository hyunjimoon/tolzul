---
modified:
  - 2025-11-22T08:29:38-05:00
---
# Conceptual Model: Entrepreneur's Partial Commitment (EPC)

## 1. Core Framework: Promise Precision as Endogenous Design

### 1.1 The Central Tension

Entrepreneurs face a fundamental design problem when communicating with stakeholders. Their promises must serve **dual purposes**: 

1. **Coordination Device**: Enable investors to evaluate quality and monitor progress (Information value)
2. **Exploration Tool**: Preserve flexibility to discover optimal strategies (Option value)

We model promise precision τ ∈ [0,1] as an **endogenous choice variable** that entrepreneurs optimize based on their venture's characteristics. Unlike prior work treating precision as exogenous signal, we show that optimal precision τ* emerges from balancing information gains against coordination costs.

### 1.2 Visual Framework: The Precision-Performance Space

```
Performance
    ↑
    │     ╱╲ Software Peak
    │    ╱  ╲    (High exercisability)
    │   ╱    ╲
    │  ╱      ╲___Hardware Peak
    │ ╱           (Low exercisability)  
    │╱_______________
    └────────────────→
     0    τ*₁  τ*₂   1
         Promise Precision (τ)

Key insight: τ*software < τ*hardware
Software ventures optimize at lower precision due to higher exercisability
```

### 1.3 Formal Model Setup

Consider an entrepreneur choosing precision τ to maximize expected value across two periods:

**Period 1 (Funding Stage):**
- Entrepreneur announces τ
- Investors observe τ and form beliefs about quality θ
- Funding F(τ) = α₀ + α₁·I(τ) where I(τ) = -log(1-τ) is information value

**Period 2 (Execution Stage):**
- True market state θ revealed
- Venture can pivot with cost C(τ,F) = τ²/F where F is exercisability
- Success probability S(τ,F) = Φ(match(τ,θ,F))

**Optimization Problem:**
```
max V(τ) = F(τ) + δ·S(τ,F) - C(τ,F)
   τ

First-order condition:
∂V/∂τ = α₁/(1-τ) - 2τ/F + δ·∂S/∂τ = 0

Solution:
τ*(F) = F/(1+F) when δ·∂S/∂τ is small
```

This yields our central prediction: **optimal precision increases with exercisability**.

## 2. Mechanism: How Vagueness Creates Value

### 2.1 The Learning Channel

Vagueness preserves what we call the **"consideration set"**—the range of strategic trajectories available for exploration:

```
Consideration Set Size: Ω(τ) = (1-τ)·K
where K = total possible strategies
```

Larger consideration sets enable three learning advantages:

1. **Parallel Experimentation**: Test multiple hypotheses simultaneously
2. **Market Discovery**: Observe which segments respond most strongly  
3. **Combinatorial Innovation**: Recombine elements from different trajectories

### 2.2 The Coordination Cost Channel

However, vagueness also imposes costs through **stakeholder misalignment**:

```
Coordination Cost: CC(τ,n) = n²·(1-τ)²
where n = number of stakeholders
```

As stakeholder count increases, coordination costs grow quadratically with vagueness. This explains why later-stage ventures with multiple investors, partners, and employees converge toward precision.
 
### 2.3 The Exercisability Moderator

The net value of vagueness depends critically on exercisability F, which we decompose into four components:

| Component | High F (Software) | Low F (Hardware) | Mechanism |
|-----------|------------------|------------------|-----------|
| **Technical** | Modular architecture | Integral systems | Reconfiguration cost |
| **Resource** | Cloud/SaaS | Physical assets | Commitment reversibility |
| **Contractual** | Platform terms | Bilateral agreements | Renegotiation friction |
| **Regulatory** | Unregulated | Certified/Licensed | Compliance constraints |

**Composite Exercisability Score:**
```
F = Σᵢ wᵢ·fᵢ where fᵢ ∈ {0,1} for each component
```

## 3. Hypothesis Development: From Theory to Testing

### 3.1 Main Effects

**H1: Early-Stage Information Penalty**
```
Hypothesis: ∂E/∂V < 0
Mechanism: Higher vagueness → Lower information value → Reduced funding
Prediction: β₁ < 0 in E = β₀ + β₁·V + Controls
```

**H2: Later-Stage Flexibility Benefit (Conditional)**
```
Hypothesis: ∂L/∂V > 0 when F = 1
Mechanism: Higher vagueness → Preserved options → Better adaptation
Prediction: β₂ + β₃ > 0 in L = β₀ + β₁·V + β₂·F + β₃·V×F
```

### 3.2 Boundary Conditions

**H2a: Exercisability Amplification**
```
Hypothesis: ∂²L/∂V∂F > 0
The marginal benefit of vagueness increases with exercisability
```

**H3: Temporal Dynamics**
```
Hypothesis: |∂E/∂V| < |∂L/∂V| for high-F ventures
Later-stage benefits outweigh early-stage costs when exercisability is high
```

### 3.3 Mechanism Tests

To validate our theoretical channels, we test intermediate outcomes:

| Mechanism | Proxy Variable | Expected Effect |
|-----------|---------------|-----------------|
| **Larger consideration set** | Number of pivots | V → More pivots |
| **Better learning** | Time to product-market fit | V×F → Faster PMF |
| **Lower coordination cost** | Stakeholder alignment survey | V×F → Less misalignment |

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

### 4.2 Validation Strategy

We validate SVI through:
1. **Expert Rating**: Correlation with VC partner assessments (r = 0.72)
2. **Predictive Validity**: Forecasts actual pivots (AUC = 0.68)
3. **Robustness**: Consistent across alternative NLP models

## 5. Empirical Context: Transportation/Mobility Sector

### 5.1 Why Transportation?

The transportation sector provides ideal variation for testing our framework:

1. **Technological Diversity**: Software (apps) vs Hardware (vehicles)
2. **Regulatory Heterogeneity**: Ride-sharing (minimal) vs Autonomous (extensive)
3. **Market Uncertainty**: COVID-19 created exogenous shock to test adaptation
4. **Data Availability**: Comprehensive funding records and public communications

### 5.2 Sample Construction

| Criterion | Specification | N Excluded | N Remaining |
|-----------|--------------|------------|-------------|
| **Universe** | All transportation ventures | - | 157,234 |
| **Time Window** | Founded 2010-2020 | 19,637 | 137,597 |
| **Activity** | Raised Seed or Series A | 85,234 | 52,363 |
| **Data** | Non-missing descriptions | 10,051 | 42,312 |

**Final Sample Composition:**
- Software-based: 23,847 (56%)
- Hardware-based: 18,465 (44%)
- Mean vagueness: 0.42 (SD = 0.21)
- Series B+ rate: 12.3% overall (Software: 14.2%, Hardware: 9.8%)

## 6. Econometric Specification

### 6.1 Early Funding (OLS)

```
log(Series_A_Amount)ᵢ = β₀ + β₁·Vaguenessᵢ + β₂·Xᵢ + Cohortᵢ + εᵢ

where X includes:
- log(team_size)
- founder_experience
- patent_count
- location_dummies
```

### 6.2 Later Success (Logit)

```
Pr(Series_B+)ᵢ = Λ(α₀ + α₁·Vᵢ + α₂·Fᵢ + α₃·Vᵢ×Fᵢ + α₄·Xᵢ + Cohortᵢ)

where Λ is logistic CDF
```

### 6.3 Robustness

We conduct specification curve analysis across:
- 100+ model variants
- Alternative vagueness measures
- Different time windows
- Sample restrictions
- Instrumental variables (founder linguistic background)

## 7. Preview of Results

Our empirical analysis reveals three key patterns:

1. **No Early Penalty**: Vagueness shows insignificant effect on Series A (β₁ ≈ 0, p = 0.85)
2. **Attenuated Later Penalty**: Vagueness reduces Series B+ probability, but less for software
3. **Exercisability Matters**: Hardware penalty is 2× software penalty (though p = 0.19)

These results suggest that rather than creating option value, **vagueness minimizes coordination costs when pivots are operationally feasible**.

## 8. Theoretical Implications

Our framework reconceptualizes three foundational assumptions:

### 8.1 From Signaling to Construction
**Old View**: Quality exists → Entrepreneurs signal → Investors evaluate  
**Our View**: Entrepreneurs explore → Quality emerges → Precision earned

### 8.2 From Options to Coordination
**Old View**: Vagueness preserves valuable options  
**Our View**: Vagueness reduces coordination friction when pivots necessary

### 8.3 From Stage to Architecture
**Old View**: Early precision, later flexibility  
**Our View**: Architecture determines optimal precision throughout lifecycle

These insights suggest that **entrepreneurial strategy is less about choosing precise versus vague and more about calibrating promises to operational capabilities**.