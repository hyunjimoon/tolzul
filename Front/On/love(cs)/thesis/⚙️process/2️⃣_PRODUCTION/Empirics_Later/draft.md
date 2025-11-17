# Empirics (Later): H2 Tests - Vagueness × Architecture → Series B+ Success

## 1. Hypotheses

### **H2a: Vagueness × Hardware → Later Success (−)**
```
Model: P(B+) = β₀ + β₁·V + β₂·H + β₃·(V×H) + Controls + ε
Prediction: β₃ < 0
```

**Logic:** Hardware firms cannot exercise real options cheaply due to:
- Physical asset rigidity (tooling, prototypes, supply chains)
- Engineering evaluation homogeneity (precision culture)

### **H2b: Vagueness → Later Success (+) for Software**
```
Marginal effect when H=0: β₁ > 0
```

**Logic:** Software firms can exercise options cheaply due to:
- Code refactoring << physical retooling
- Evaluator heterogeneity (market uncertainty → diverse perspectives)

---

## 2. Sample

**Conditioning:** Firms that received Series A (from Empirics_Early)  
**Expected N:** ~700 firms (70% of H1 sample)

**Observation window:** 
- Series A date + 17 months (75th percentile of B-round timeline)
- If no Series B by cutoff → code as 0

---

## 3. Variables

### **Dependent Variable: Series B+ Success (L)**
- **Type:** Binary (0/1)
- **Source:** PitchBook `next_funding_round` field
- **Coding:**
  - 1 = Received Series B, C, D, or later within 17 months
  - 0 = No further funding or only bridge/extension rounds

### **Key Independent: Hardware (H)**
- **Type:** Binary (0/1)
- **Source:** Multi-method classification
  - PitchBook industry codes (Superconducting, Ion trap, Photonic → 1)
  - Keyword detection in description (algorithm, cloud, software → 0)
  - Manual validation by domain expert (inter-rater κ > 0.85)

### **Interaction Term: V × H**
- **Construction:** Product of standardized vagueness and hardware dummy
- **Interpretation:** How hardware architecture moderates vagueness effect

### **Controls (carried from H1):**
- `is_serial_founder`
- `industry` (may drop due to collinearity with H)
- `year_founded`
- `series_a_amount` (logged)

---

## 4. Estimation Strategy

### **Model Specification:**
```python
from statsmodels.formula.api import logit

model = logit(
    formula="""
        series_b_plus ~ 
        vagueness_zscore + 
        hardware + 
        vagueness_zscore:hardware +
        is_serial + 
        log_series_a +
        C(year_founded)
    """,
    data=df
).fit(cov_type='HC3')
```

### **Marginal Effects Calculation:**
```python
# For Software (H=0)
∂P/∂V |_{H=0} = β₁
# Expected: β₁ > 0 (vagueness helps)

# For Hardware (H=1)
∂P/∂V |_{H=1} = β₁ + β₃
# Expected: β₁ + β₃ < 0 (vagueness hurts)
```

---

## 5. Expected Results

**Table 2: H2a/b Logit Results**

| Variable | β | SE | z | p | AME |
|----------|---|----|----|---|-----|
| Vagueness (V) | **+0.42** | 0.15 | 2.8 | 0.005 | +0.09 |
| Hardware (H) | −0.28 | 0.20 | −1.4 | 0.16 | −0.06 |
| V × H | **−0.85** | 0.30 | −2.8 | 0.005 | −0.18 |
| Serial Founder | 0.35 | 0.12 | 2.9 | 0.004 | +0.08 |
| log(Series A) | 0.22 | 0.08 | 2.75 | 0.006 | +0.05 |

**Interpretation:**
- **For Software (H=0):** 1 SD ↑ vagueness → +9 pp in P(Series B+) (p < 0.01)
- **For Hardware (H=1):** 1 SD ↑ vagueness → −9 pp in P(Series B+) (p < 0.01)
  - Net effect: β₁ + β₃ = 0.42 − 0.85 = −0.43
  - AME: −0.09 (reversal confirmed)

---

## 6. Mechanisms (H2c)

### **Pivot Frequency as Mediator**

**Hypothesis:** Vague promises enable more pivots in software (but not hardware).

**Test:**
```python
# Stage 1: V → Pivot Count
pivot_count = α₀ + α₁·V + α₂·H + α₃·(V×H) + ε

# Stage 2: V + Pivot → Series B+
series_b = β₀ + β₁·V + β₂·pivot + β₃·H + ε
```

**Expected:**
- α₁ > 0, α₃ < 0 (vagueness → more pivots in SW, fewer in HW)
- β₂ > 0 (pivots → later success)
- β₁ attenuates when pivot is added (partial mediation)

---

## 7. Visualizations

### **Figure 4: V × H Interaction Plot**

```
X-axis: Vagueness (z-score), range [−2, 2]
Y-axis: P(Series B+), range [0, 1]
Lines: 
  - Blue (SW): Upward slope
  - Gray (HW): Downward slope
Bands: 95% CI from delta method
```

**Annotation:** Crossover point at V ≈ 0 (median vagueness)

### **Figure 5: Pivot Distributions**

```
Box plots:
  - SW-Vague: median = 2 pivots
  - SW-Precise: median = 1 pivot
  - HW-Vague: median = 0 pivots
  - HW-Precise: median = 0 pivots
```

---

## 8. Robustness

1. **Alternative cutoff:** 12 months vs. 24 months for Series B+ → same sign
2. **Alternative H coding:** Use R&D intensity proxy → same interaction
3. **Selection correction:** Heckman two-stage (Stage 1 = getting Series A) → β₃ still negative
4. **Specification curve:** 200+ model combinations (see Appendix)

---

## Next: Pass to Discussion

See `TO_DISCUSSION.txt` for:
- Theoretical implications (VOI vs. RO reconciliation)
- Managerial implications (promise design rules)
- Limitations (selection bias, external validity)
