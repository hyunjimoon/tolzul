# 🔧 EPC Framework: Quick Reference Guide

## Core Formula: Optimal Promise Precision

```
τ*(F) = F/(1+F)
```
Where:
- τ = promise precision ∈ [0,1]
- F = exercisability (composite score)

## The Three Key Equations

### 1. Information Value (Early Stage)
```
I(τ) = -log(1-τ)
```
*Interpretation*: Precision increases investor's information gain logarithmically

### 2. Coordination Cost (Execution Stage)
```
C(τ,F) = τ²/F
```
*Interpretation*: Costs rise quadratically with precision, inversely with flexibility

### 3. Consideration Set Size
```
Ω(τ) = (1-τ)·K
```
*Interpretation*: Strategic options decrease linearly with precision

## Exercisability Components (F-Score)

```python
F = w₁·f_tech + w₂·f_resource + w₃·f_contract + w₄·f_regulatory

where each f_i ∈ {0,1}:
- f_tech = 1 if modular architecture
- f_resource = 1 if variable costs  
- f_contract = 1 if platform model
- f_regulatory = 1 if permissionless
```

## Strategic Vagueness Index (SVI)

```python
SVI = 0.4·Categorical_Ambiguity + 
      0.4·Concreteness_Deficit + 
      0.2·Temporal_Flexibility
```

Components:
- **Categorical Ambiguity**: 1 - max(P(category))
- **Concreteness Deficit**: 1 - (concrete_words/total_words)  
- **Temporal Flexibility**: 1 - (time_commits/total_commits)

## Empirical Specifications

### Early Funding (OLS)
```
E_i = β₀ + β₁·V_i + β₂·X_i + Cohort_i + ε_i
Expected: β₁ ≈ 0 (no effect found)
```

### Later Success (Logit)  
```
Pr(L_i=1) = Λ(α₀ + α₁·V_i + α₂·F_i + α₃·V_i×F_i + α₄·X_i)
Expected: α₃ > 0 (attenuation by exercisability)
```

## The 2×2 Strategic Matrix

```
         Low F (Hardware)        High F (Software)
    ┌──────────────────────┬──────────────────────┐
Low │ SIGNAL QUALITY       │ HEDGE BETS           │
 V  │ Traditional VC model │ Balanced approach    │
    │ Example: Bosch       │ Example: Waymo       │
    ├──────────────────────┼──────────────────────┤
High│ COORDINATION TRAP    │ STRATEGIC AMBIGUITY  │
 V  │ Worst outcomes       │ Minimize coord costs │
    │ Example: Better Place│ Example: Tesla, Uber │
    └──────────────────────┴──────────────────────┘
```

## Decision Rules for Entrepreneurs

### When to be Precise (High τ)
- Hardware/physical products (Low F)
- Regulated industries
- B2B with specific customers
- High capital requirements

### When to be Vague (Low τ)
- Software/digital products (High F)  
- Platform business models
- Uncertain customer segments
- Rapid iteration possible

## Key Insights

1. **Quality is Endogenous**: τ* emerges from learning, not signaling
2. **Architecture > Timing**: Exercisability matters more than funding stage
3. **Coordination > Options**: Vagueness reduces friction, doesn't create value

## Measurement Validation

| Test | Method | Result |
|------|--------|--------|
| Expert validity | VC ratings correlation | r = 0.72 |
| Predictive validity | Forecasts pivots | AUC = 0.68 |
| Robustness | Alternative NLP | ρ = 0.81 |

## The Counter-Intuitive Finding

**Hypothesis**: Vagueness hurts early, helps later  
**Finding**: Vagueness hurts always, but less with high exercisability  
**Insight**: Coordination costs dominate option value

## Formula for Earned Precision

```
Precision_Evolution = τ₀ + λ·t·(1-τ₀)·F

where:
- τ₀ = initial precision
- λ = learning rate  
- t = time
- F = exercisability
```

*This captures how ventures "earn" precision through market learning*