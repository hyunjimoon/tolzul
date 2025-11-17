# Hypothesis Test: β_VF > 0

**Theory**: Flexibility (F) amplifies the effect of Vagueness (V) on Later success (L)

## Research Question

**H***: Does flexibility make it easier for vague companies to succeed?

**Formal hypothesis**:
```
Pr(L=1) = logit^-1(α + β_V·V + β_F·F + β_VF·(V×F) + controls)

H0: β_VF = 0
H1: β_VF > 0  (Flexibility amplifies Vagueness effect)
```

**Key principle**: E (Early funding) is a **mediator**, NOT a confounder
- Do NOT include E as control in L regression
- Causal path: V → E → L (E mediates V's effect on L)

## Minimal Specification

**Model**: Non-Bayesian Logit with V×F interaction
- Response: L (Later Stage VC at 2025.11)
- Main effects: z_V (Vagueness), F_flexibility (1=SW, 0=HW)
- **Interaction**: z_V × F_flexibility (this is β_VF!)
- Controls: founding_cohort, region
- **NO E control** (E is mediator)

**Statistical test**: One-tailed Wald test
- If β_VF > 0 and p < 0.05 → Reject H0
- Conclusion: SW companies benefit more from vagueness than HW

## Usage

### All companies
```bash
python scripts/test_hypothesis_VxF.py
```

### Quantum computing only
```bash
python scripts/test_hypothesis_VxF.py --industry quantum
```

### Transportation only
```bash
python scripts/test_hypothesis_VxF.py --industry transportation
```

## Output

### 1. Terminal
```
================================================================================
HYPOTHESIS TEST: β_VF > 0 (Quantum Companies)
================================================================================

H*: Flexibility amplifies the effect of Vagueness on Later success
    H0: β_VF = 0
    H1: β_VF > 0

LOGIT REGRESSION
Formula: L ~ z_V * F_flexibility + C(founding_cohort) + C(region)

Coefficients:
              Coef   Std.Err      z      P>|z|
z_V          -0.234    0.089  -2.63    0.0085
F_flexibility 0.456    0.123   3.71    0.0002
z_V:F_flexibility  0.312    0.145   2.15    0.0316  ← β_VF

HYPOTHESIS TEST
Interaction term: z_V:F_flexibility
  Coefficient:  β_VF = 0.3120
  Std Error:    SE   = 0.1450
  z-statistic:  z    = 2.152
  p-value (one-tailed): p = 0.0158

================================================================================
VERDICT: ✓ REJECT H0
================================================================================
Flexibility AMPLIFIES Vagueness effect (β_VF = 0.3120 > 0, p = 0.0158)

Significance: *
```

### 2. Files

**Coefficient table:**
- `outputs/hypothesis_VxF/coefficients_quantum.csv`

**Summary stats:**
- `outputs/hypothesis_VxF/summary_quantum.csv`

**Interaction plot:**
- `outputs/hypothesis_VxF/interaction_VxF_quantum.png`
- `outputs/hypothesis_VxF/interaction_VxF_quantum.pdf`

### 3. Interaction Plot

![Interaction plot showing two curves:
- Blue solid line (F=1, SW/Flexible, skyblue)
- Gray dashed line (F=0, HW/Rigid, gray)
X-axis: Vagueness (green)
Y-axis: Pr(L=1|V,F) (blue)
Annotation: β_VF = 0.312*
]

**Interpretation:**
- If lines diverge (positive interaction) → SW benefits more from high V
- If lines parallel (β_VF ≈ 0) → No differential effect
- If lines converge (negative interaction) → HW benefits more

## Color Code (W2 Standard)

| Variable | Color | Usage |
|----------|-------|-------|
| L (Later success) | #0000FF (blue) | Y-axis label |
| V (Vagueness) | green | X-axis label |
| F=1 (Flexible/SW) | skyblue | Solid line |
| F=0 (Rigid/HW) | gray | Dashed line |

## Current Limitations

### ⚠️ Mock Vagueness Data

Current script uses **random V** for demonstration.

**To use real vagueness**:
1. Ensure consolidated data includes `Description` and `Keywords` columns
2. Run `compute_vagueness_vectorized()` from `modules/features.py`
3. Or re-consolidate from original .dat files with Description/Keywords

**To fix consolidation script:**
```python
# In consolidate_2021_cohort.py, change:
baseline_cols = ['CompanyID', 'CompanyName', 'LastFinancingDealType',
                 'Description', 'Keywords']  # ← Add these
```

### Mock Controls

- `founding_cohort`: Currently all 'cohort_1'
- `region`: Currently all 'US'

**Real controls** should come from original .dat files.

## Relationship to W2 Slides

- **H* = W2 H₂** (p.29-31): "Flexibility amplifies the effect of Vagueness on later survival"
- **E as mediator** (p.49): Why we exclude E from L regression
- **Color palette** (p.XX): Standard colors for all figures

## Comparison with Previous Analysis

### ❌ Old approach (`analyze_2021_cohort.py`):
- Chi-square test comparing HW rate vs SW rate
- Ignores Vagueness (V)
- No interaction term
- Bar chart (rates only)

### ✓ New approach (`test_hypothesis_VxF.py`):
- Logit regression with V×F interaction
- Directly tests β_VF > 0
- Accounts for continuous V
- Interaction curve showing mechanism

## Next Steps

1. **Add real Vagueness measure**
   - Include Description/Keywords in consolidation
   - Run `compute_vagueness_vectorized()`

2. **Add real controls**
   - founding_cohort from YearFounded
   - region from HQCountry

3. **Multiple time points**
   - Test β_VF at 2yr, 3yr, 4yr separately
   - Check if interaction grows over time

4. **Robustness checks**
   - Probit instead of Logit
   - Different V measures (alternative scorers)
   - Subsample analysis (by cohort, region)
