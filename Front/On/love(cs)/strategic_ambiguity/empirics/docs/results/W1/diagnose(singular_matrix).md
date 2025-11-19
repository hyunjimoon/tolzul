# Emergency Help Request: Singular Matrix in H2 Logistic Regression

## Context

I'm analyzing venture capital data for my research presentation TODAY. My H2 hypothesis tests whether textual vagueness in startup descriptions affects Series B+ progression, conditional on sector integration cost.

**Problem**: Getting `numpy.linalg.LinAlgError: Singular matrix` in logistic regression despite multiple preprocessing fixes.

---

## The Error

```python
model = smf.logit(formula, data=df_clean).fit(disp=False)
# Error: numpy.linalg.LinAlgError: Singular matrix
```

**Formula**:
```python
survival ~ z_vagueness * high_integration_cost + z_employees_log + C(founding_cohort)
```

---

## What I've Already Tried

### ✅ Preprocessing Applied:
1. **Z-score standardization**: `z_vagueness`, `z_employees_log`
2. **Founding cohort** (categorical): Replaced continuous `year_founded`
3. **Dropped sector_fe**: Was collinear with `high_integration_cost`
4. **Founder credibility has variation**: 3.1% (not constant)

### ❌ Still Fails

Despite all fixes, still getting singular matrix error at this line:
```
File "hypothesis_tests.py", line 161, in test_h2_main_survival
    model = smf.logit(formula, data=df_clean).fit(disp=False)
```

---

## Data Summary

**Sample Size**: 42,679 companies
**Survival Rate**: 16.87% (Series A → Series B+ progression)

**Variables**:
- `survival`: Binary (0/1) - 16.87% = 1
- `z_vagueness`: Standardized continuous (mean=0, std=1)
- `high_integration_cost`: Binary (0/1) - sector classification
- `z_employees_log`: Standardized continuous (mean=0, std=1)
- `founding_cohort`: Categorical with 5-6 levels (e.g., '≤2009', '2010-14', '2015-18', '2019-20', '2021', '2022+')

**Interaction Term**: `z_vagueness:high_integration_cost`

---

## Diagnostic Output

From preprocessing:
```
[1/4] Creating founding_cohort...
  ✓ founding_cohort created:
    {'≤2009': 180188, '2010-14': 87190, '2015-18': 76427, '2019-20': 24572, '2021': 3692, '2022+': 0}

[2/4] Standardizing continuous predictors...
  ✓ z_vagueness: mean=53.70, std=6.77
  ✓ z_employees_log: mean=2.09, std=2.31

[3/4] Creating ic_within (sector-centered integration cost)...
  ✓ ic_within created (sector-centered integration cost)
    Mean: -0.0000 (should be ~0)
    Std: 0.1923

[4/4] Checking founder_credibility...
  ✓ founder_credibility has variation (mean=0.03, std=0.17)
```

**Note**: The cohort '2022+' has 0 observations (companies founded after baseline snapshot).

---

## Hypotheses About the Problem

1. **Perfect separation in founding_cohort**: The '2022+' category has 0 observations → causes singular matrix when creating dummies?

2. **Quasi-complete separation**: Maybe some founding_cohort × survival combinations have 0 or 100% success rates?

3. **Collinearity between cohort and IC**: Maybe `founding_cohort` and `high_integration_cost` are highly correlated in the at-risk subsample (Series A companies)?

4. **Interaction term issues**: Maybe `z_vagueness:high_integration_cost` creates linear dependence with other terms?

---

## Questions for You

1. **Immediate fix**: What's the fastest way to get this working for my presentation today?
   - Drop the empty '2022+' cohort?
   - Use ridge/lasso regularization?
   - Simplify the model?

2. **Diagnostic**: What diagnostic script should I run to identify the exact source of collinearity?

3. **Alternative models**: Should I:
   - Use regularized logit (`fit_regularized(method='l2', alpha=0.01)`)?
   - Drop `founding_cohort` entirely and just use continuous `year_founded`?
   - Drop the interaction term temporarily?

4. **Theoretical validity**: If I use regularization, can I still interpret the coefficients for hypothesis testing?

---

## Desired Outcome

A logistic regression model that:
1. **Converges** without singular matrix error
2. **Tests the interaction**: `z_vagueness:high_integration_cost`
3. **Controls for cohort effects**: Via `founding_cohort` or alternative
4. **Is defensible**: For academic presentation to MIT professors today

---

## Code Snippets

### Current Model Function
```python
def test_h2_main_survival(df, formula):
    required_vars = ['survival', 'z_vagueness', 'high_integration_cost']
    df_clean = df.dropna(subset=required_vars)

    # This line fails:
    model = smf.logit(formula, data=df_clean).fit(disp=False)

    return model
```

### Attempted Regularization (not tested yet)
```python
# Try with ridge penalty
model = smf.logit(formula, data=df_clean).fit_regularized(
    method='l2',
    alpha=0.01,
    disp=False
)
```

---

## Files Available

I can provide:
1. Full dataset (`h2_analysis_dataset_17m.csv`)
2. Preprocessing code (`feature_engineering.py`)
3. Hypothesis testing code (`hypothesis_tests.py`)
4. Full error traceback

---

## Urgency

**Presentation**: TODAY (within hours)
**Need**: Working model ASAP
**Willing to**: Simplify if necessary, use regularization, change cohort specification

---

## Thank You!

Any help is greatly appreciated. I'm desperate to get this working for my presentation to Charlie Fine and Scott Stern.

**Claude Code tried**: Z-score standardization, dropping sector FE, categorical cohorts, founder credibility fixes
**Still failing**: Yes
**Time remaining**: Very little

Please help! 🙏
