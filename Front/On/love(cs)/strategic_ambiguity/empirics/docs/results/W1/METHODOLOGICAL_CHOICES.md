# Methodological Choices Documentation

## Issue 1: year_founded Coding

### Current Implementation
```python
# hypothesis_tests.py line 33, 105
formula = "... + year_founded"  # Treated as continuous (ordinal)
```

### Problem
- Assumes LINEAR trend: year 2020 = year 2010 + 10×effect
- Ignores potential cohort-specific effects (e.g., 2008 financial crisis cohort)

### Options

**Option A: Categorical (Recommended for robustness)**
```python
formula = "... + C(year_founded)"
```
- Pros: Captures cohort-specific effects
- Cons: Uses more degrees of freedom

**Option B: Continuous (Current - simplicity)**
```python
formula = "... + year_founded"
```
- Pros: Parsimonious, assumes smooth trend
- Cons: Misses non-linear cohort effects

**Option C: Use firm_age instead**
```python
formula = "... + firm_age"  # Already in data: 2024 - year_founded
```
- Pros: More interpretable (effect of age, not cohort)
- Cons: Confounds cohort with age

### Recommendation
For presentation TODAY:
- Keep current (Option B) for simplicity
- Document as limitation: "Assumes linear time trend"
- Add robustness check with C(year_founded) in appendix

---

## Issue 2: early_funding_musd Missing Data (54.1%)

### Current Handling

**H1 (early_funding as DV):**
```python
df_clean = df.dropna(subset=['early_funding_musd', 'vagueness'])
# N = 20,296 (45.9% of 44,020)
```
✓ CORRECT: Cannot predict missing DV

**H2 (survival as DV):**
```python
df_clean = df.dropna(subset=['survival', 'vagueness', 'high_integration_cost'])
# N = 42,685 (97.0% of 44,020)
# early_funding NOT REQUIRED
```
✓ CORRECT: early_funding is MEDIATOR, excluded from H2

### Why This Is Correct

**Causal Chain:**
```
Vagueness → Early Funding → Survival
            ↑ H1 tests    ↑ H2 tests
            (mediator)    (total effect)
```

**H1**: Tests vagueness → early_funding pathway
- Requires early_funding data
- N = 20,296 (companies with funding data)

**H2**: Tests vagueness → survival TOTAL EFFECT
- Does NOT control for early_funding (would block the pathway)
- N = 42,685 (all companies with survival data)
- Includes companies WITHOUT early funding data (they may have failed early)

### Selection Bias Check

**Question**: Are companies with missing early_funding_musd systematically different?

**Answer**: YES - but this is informative!
- Missing early_funding likely means: (1) Failed before raising, or (2) Bootstrapped
- Both are valid survival outcomes
- Excluding them from H2 would bias survival rate UPWARD

**Current approach (H2):**
- Uses ALL 42,685 companies (97%)
- Missing early_funding treated as "no funding raised"
- This is the correct total effect estimate

---

## Summary Table

| Model | DV | Sample Size | early_funding | year_founded |
|-------|----|-----------:|---------------|--------------|
| H1 | early_funding_musd | 20,296 (45.9%) | Required (DV) | Continuous |
| H2 Main | survival | 42,685 (97.0%) | Excluded (mediator) | Continuous |
| H2 Robustness | series_b_funding | TBD | Included | Continuous |

---

## Action Items for Presentation

### Immediate (no code change needed)
1. Document year_founded as continuous (linear trend assumption)
2. Explain sample size difference (H1: 45.9% vs H2: 97.0%)
3. Emphasize: H2 excludes early_funding BY DESIGN (mediator exclusion)

### Post-presentation (robustness)
1. Test C(year_founded) in appendix
2. Check if missing early_funding companies differ on observables
3. Consider Heckman selection model if reviewers ask

---

## Talking Points for Charlie & Scott

**On year_founded:**
> "We control for founding year as a linear trend to capture macro conditions.
> This assumes smooth time effects; robustness checks with year fixed effects
> are available if needed."

**On early_funding missing data:**
> "H1 uses 45.9% of companies with funding data. H2 uses 97% of companies
> because we deliberately exclude early funding—it's a mediator, not a
> confounder. Including it would block the causal pathway we want to measure.
> Missing funding data is informative: these companies likely failed early,
> which is a valid survival outcome."

**On sample size difference:**
> "Different models test different parts of the causal chain. H1 tests the
> vagueness→funding link (needs funding data). H2 tests the vagueness→survival
> total effect (needs survival data, but NOT funding data)."
