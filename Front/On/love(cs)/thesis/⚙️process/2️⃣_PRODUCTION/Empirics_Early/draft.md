# Empirics (Early): H1 Test - Vagueness → Series A Funding

## 1. Hypothesis

**H1:** Firms with vague promises secure **less** Series A funding than firms with precise promises.

```
Model: E = α₀ + α₁·V + Controls + ε
Prediction: α₁ < 0
```

---

## 2. Sample

**Population:** Quantum computing ventures, 2019-2024  
**Inclusion criteria:**
- Received Series A funding during baseline year (2021)
- Company description available in PitchBook
- Minimum 50 words in description (for vagueness calculation)

**Expected N:** ~1,000 firms

---

## 3. Variables

### **Dependent Variable: Series A Amount (E)**
- **Source:** PitchBook `series_a_amount` field
- **Transformation:** log(E + 1) for skewness correction
- **Unit:** Millions USD

### **Independent Variable: Vagueness (V)**
- **Source:** Composite index from `description` field
- **Components:**
  1. **Categorical Vagueness:** Count of abstract keywords (platform, solution, ecosystem, etc.)
  2. **Concreteness Deficit:** 1 - (specific references / total words)
     - Specific = numbers, dates, technical terms
- **Normalization:** z-score for interpretability

### **Controls:**
| Variable | Type | Source | Rationale |
|----------|------|--------|-----------|
| `is_serial_founder` | Binary | PitchBook founder profiles | Credibility signal |
| `industry` | Categorical | PitchBook industry tags | Fixed effects |
| `year_founded` | Continuous | PitchBook | Firm maturity |
| `hq_country` | Categorical | PitchBook | Geographic FE |

---

## 4. Estimation Strategy

### **Model Specification:**
```python
from statsmodels.formula.api import ols

model = ols(
    formula="""
        log_series_a ~ 
        vagueness_zscore + 
        is_serial + 
        C(industry) + 
        C(year_founded) + 
        C(hq_country)
    """,
    data=df
).fit(cov_type='HC3')  # Robust SEs
```

### **Diagnostics:**
- [ ] VIF < 5 for multicollinearity
- [ ] Breusch-Pagan test for heteroskedasticity
- [ ] Q-Q plot for normality of residuals

---

## 5. Expected Results

**Table 1: H1 Regression Results**

| Variable | β | SE | t | p | 95% CI |
|----------|---|----|----|---|--------|
| Vagueness (z) | **−0.15** | 0.05 | −3.0 | 0.003 | [−0.25, −0.05] |
| Serial Founder | 0.22 | 0.08 | 2.75 | 0.006 | [0.06, 0.38] |
| (Industry FE) | ✓ | ✓ | ✓ | ✓ | ✓ |
| (Year FE) | ✓ | ✓ | ✓ | ✓ | ✓ |
| (Country FE) | ✓ | ✓ | ✓ | ✓ | ✓ |

**Interpretation:**  
A 1 SD increase in vagueness → 15% decrease in Series A funding (α₁ = −0.15, p < 0.01).

---

## 6. Robustness Checks

1. **Alternative DV:** Use raw amount (not logged) → expect same sign
2. **Alternative IV:** Use only categorical vagueness (not composite) → expect same sign
3. **Subsample:** Exclude top 5% funding outliers → expect stronger effect
4. **Specification curve:** Test across 100+ model combinations (see Appendix)

---

## 7. Visualization

**Figure 3: Vagueness → Series A Scatter**

```
X-axis: Vagueness (z-score), range [−3, 3]
Y-axis: Series A Amount ($M), log scale
Color: Red gradient (darker = more vague)
Line: OLS fit with 95% CI band
```

**Expected pattern:** Downward slope (supporting H1)

---

## Next: Pass to Empirics_Later

See `TO_LATER.txt` for:
- Sample passed forward (N ≈ 700 who got Series A)
- Variables carried over
- Expected outputs for H2a/b tests
