# Multiverse Engine Design Patterns for Iteration Efficiency

## Analysis of `docs_archive/run/multiverse_engine.py`

This document identifies powerful design patterns from the multiverse engine that can dramatically improve pipeline iteration efficiency.

---

## 🎯 Key Design Patterns Identified

### 1. **3-Stage Robust Model Fitting** ⭐⭐⭐
**Current Problem**: Your pipeline crashes when logit models fail to converge (perfect separation, collinearity, etc.)

**Multiverse Solution** (lines 366-398):
```python
# Stage 1: Try MLE (best if it works)
try:
    model = smf.logit(formula, data=d).fit(disp=False, maxiter=100)
    return extract_results(model, d, nobs, stage, 'logit_mle', 0)
except:
    pass

# Stage 2: L1 regularization α=0.1 (mild shrinkage)
try:
    model = smf.logit(formula, data=d).fit_regularized(
        method='l1', alpha=0.1, disp=False, maxiter=200
    )
    return extract_results(model, d, nobs, stage, 'logit_l1_0.1', 1)
except:
    pass

# Stage 3: L1 regularization α=0.5 (stronger shrinkage)
try:
    model = smf.logit(formula, data=d).fit_regularized(
        method='l1', alpha=0.5, disp=False, maxiter=200
    )
    return extract_results(model, d, nobs, stage, 'logit_l1_0.5', 2)
except:
    return null_result(nobs, 3, 'failed')
```

**Benefits**:
- ✅ **Never crashes** - always returns a result
- ✅ **Tracks which method worked** via `warning_code` (0=MLE, 1=L1_0.1, 2=L1_0.5, 3=failed)
- ✅ **Optimal when possible** - tries MLE first before regularization
- ✅ **Transparent** - you know when results are regularized

**How to Integrate**:
```python
# In src/models.py, replace current H2 fitting:

def test_h2_main_growth_robust(df: pd.DataFrame, formula: str = None):
    """H2 with 3-stage fallback for robustness."""

    if formula is None:
        formula = "growth ~ z_vagueness * is_hardware + z_employees_log + C(founding_cohort)"

    # Prepare data
    df_clean = df.dropna(subset=['growth', 'z_vagueness', 'is_hardware']).copy()

    # Stage 1: MLE
    try:
        model = smf.logit(formula, data=df_clean).fit(disp=False, maxiter=100)
        logger.info("✓ Model converged (MLE)")
        return model, 'mle'
    except:
        logger.warning("⚠ MLE failed, trying L1 regularization...")

    # Stage 2: L1 α=0.1
    try:
        model = smf.logit(formula, data=df_clean).fit_regularized(
            method='l1', alpha=0.1, disp=False, maxiter=200
        )
        logger.info("✓ Model converged (L1 α=0.1)")
        return model, 'l1_0.1'
    except:
        logger.warning("⚠ L1(0.1) failed, trying stronger regularization...")

    # Stage 3: L1 α=0.5
    try:
        model = smf.logit(formula, data=df_clean).fit_regularized(
            method='l1', alpha=0.5, disp=False, maxiter=200
        )
        logger.info("✓ Model converged (L1 α=0.5)")
        return model, 'l1_0.5'
    except Exception as e:
        raise RuntimeError(f"All estimation methods failed: {e}")
```

---

### 2. **xarray Multiverse Coordinates** ⭐⭐⭐

**Current Approach**: You cache by scenario (all, quantum, transportation)

**Multiverse Approach**: Track EVERY specification dimension as coordinates:

```python
<xarray.Dataset>
Dimensions:
  spec_id: 1,152  # (3 stages × 2 moderators × 4 windows × 2 scaling × 12 control combos)

Coordinates:
  * stage           (spec_id) category  # E, L1, L2
  * moderator       (spec_id) category  # option_level, isSoftware
  * window          (spec_id) object    # ('2015-01', '2021-12')
  * scaling         (spec_id) category  # zscore, winsor99_z
  * ctrl_employee   (spec_id) int       # 0 or 1
  * ctrl_region     (spec_id) int       # 0 or 1
  * ctrl_founder    (spec_id) int       # 0 or 1
  * ctrl_earlyfund  (spec_id) int       # 0 or 1

Data Variables:
  coef_vag_main     (spec_id) float64   # Main vagueness coefficient
  p_vag_main        (spec_id) float64   # P-value
  coef_vagXsoftware (spec_id) float64   # Interaction coefficient
  nobs              (spec_id) int       # Sample size
  fit_stat          (spec_id) float64   # AIC or pseudo-R²
  warning_code      (spec_id) int       # Which estimation method worked
```

**Power of This Approach**:
```python
# Slice by specification dimension
ds_hardware = ds.sel(moderator='isSoftware')
ds_early = ds.sel(stage='E')
ds_2019_2021 = ds.sel(window=('2019-01', '2021-12'))

# Filter by estimation success
ds_mle_only = ds.where(ds.warning_code == 0, drop=True)

# Grouped statistics across specifications
median_coef = ds.coef_vag_main.median(dim='spec_id')
significant_specs = (ds.p_vag_main < 0.05).sum().values

# Check robustness across control combinations
for emp_ctrl in [0, 1]:
    subset = ds.where(ds.ctrl_employee == emp_ctrl, drop=True)
    print(f"Employee control={emp_ctrl}: β={subset.coef_vag_main.mean().values:.3f}")
```

**How to Integrate**:

Update `cache_manager.py` to support specification dimensions:

```python
def save_model_multiverse(
    self,
    results_list: List[Dict],
    scenario: str = 'all'
) -> xr.Dataset:
    """Save multiverse analysis results as xarray Dataset.

    Args:
        results_list: List of dicts with keys:
            - stage, moderator, window, scaling, ctrl_* (coordinates)
            - coef_vag_main, p_vag_main, nobs, etc. (data variables)

    Returns:
        xarray Dataset with multiverse structure
    """
    # Convert to DataFrame
    df = pd.DataFrame(results_list)

    # Create multi-index from specification coordinates
    coord_cols = ['stage', 'moderator', 'window', 'scaling',
                  'ctrl_employee', 'ctrl_region', 'ctrl_founder', 'ctrl_earlyfund']
    df = df.set_index(coord_cols)

    # Convert to xarray
    ds = xr.Dataset.from_dataframe(df)

    # Add metadata
    ds.attrs.update({
        'scenario': scenario,
        'n_specifications': len(df),
        'creation_time': datetime.now().isoformat()
    })

    # Save to cache
    self.save_xarray(f'models_multiverse', ds, scenario=scenario)

    return ds
```

---

### 3. **Dynamic Formula Builder** ⭐⭐

**Current Problem**: Hard-coded formulas in models.py

**Multiverse Solution** (lines 163-224):
```python
def build_formula(stage: str, moderator: str,
                 ctrl_employee: int, ctrl_region: int,
                 ctrl_founder: int, ctrl_earlyfund: int,
                 df: pd.DataFrame) -> str:
    """Build formula dynamically based on spec + data availability."""

    controls = []

    # Only include controls that actually exist in data
    if "founding_cohort" in df.columns:
        controls.append("C(founding_cohort)")

    if ctrl_employee == 1 and "z_employees_log" in df.columns:
        controls.append("z_employees_log")

    if ctrl_region == 1 and "region" in df.columns:
        controls.append("C(region)")

    # Build formula
    if stage == "E":
        rhs = ["V"] + controls
        return "z_early_funding_musd ~ " + " + ".join(rhs)
    else:
        M = "option_exercisability_level" if moderator == "option_level" else "isSoftware"
        rhs = [f"V * {M}"] + controls
        return "growth ~ " + " + ".join(rhs)
```

**Benefits**:
- ✅ **Flexible** - adapts to available data
- ✅ **Safe** - checks column existence before building formula
- ✅ **Supports multiverse** - easy to iterate over control specifications

**How to Integrate**:
```python
# In src/models.py:

class FormulaBuilder:
    """Dynamic formula construction for H1/H2 with control specifications."""

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.available_cols = set(df.columns)

    def build_h1(self,
                 include_employees: bool = True,
                 include_cohort: bool = True,
                 include_sector: bool = False) -> str:
        """Build H1 formula dynamically."""

        controls = []

        if include_employees and 'z_employees_log' in self.available_cols:
            controls.append('z_employees_log')

        if include_cohort and 'founding_cohort' in self.available_cols:
            controls.append('C(founding_cohort)')

        if include_sector and 'sector_fe' in self.available_cols:
            controls.append('C(sector_fe)')

        rhs = ['z_vagueness'] + controls
        return 'early_funding_musd ~ ' + ' + '.join(rhs)

    def build_h2(self,
                 include_employees: bool = True,
                 include_cohort: bool = True,
                 include_early_funding: bool = False) -> str:
        """Build H2 formula dynamically."""

        controls = []

        if include_employees and 'z_employees_log' in self.available_cols:
            controls.append('z_employees_log')

        if include_cohort and 'founding_cohort' in self.available_cols:
            controls.append('C(founding_cohort)')

        # CRITICAL: Early funding is a MEDIATOR, not confounder!
        if include_early_funding and 'z_early_funding_musd' in self.available_cols:
            controls.append('z_early_funding_musd')

        rhs = ['z_vagueness * is_hardware'] + controls
        return 'growth ~ ' + ' + '.join(rhs)

# Usage:
builder = FormulaBuilder(df)
formula_baseline = builder.build_h2(include_employees=True, include_cohort=True)
formula_with_funding = builder.build_h2(include_early_funding=True)  # Robustness check
```

---

### 4. **Patsy-Based Accurate nobs** ⭐

**Current Problem**: `len(df)` includes rows that will be dropped by statsmodels due to missing values in formula

**Multiverse Solution** (lines 349-353):
```python
# Get TRUE nobs using patsy design matrix
try:
    design_matrix = patsy.dmatrix(formula.split('~')[1], df, return_type='dataframe')
    d = df.loc[design_matrix.index].copy()
    nobs = len(d)  # This is the ACTUAL sample size statsmodels will use
except Exception:
    return null_result(0, 3, 'failed')
```

**Why This Matters**:
- ✅ **Accurate sample sizes** - matches what statsmodels actually uses
- ✅ **Prevents reporting errors** - no more "reported N=10,000 but model used N=8,000"
- ✅ **Catches formula errors early** - fails fast if formula is malformed

**How to Integrate**:
```python
def get_effective_sample_size(formula: str, df: pd.DataFrame) -> Tuple[pd.DataFrame, int]:
    """Get DataFrame and sample size that statsmodels will actually use."""
    import patsy

    # Extract RHS of formula
    rhs = formula.split('~')[1].strip()

    # Build design matrix (this mimics what statsmodels does internally)
    design_matrix = patsy.dmatrix(rhs, df, return_type='dataframe')

    # Get rows that survived (no missing values in any predictor)
    df_clean = df.loc[design_matrix.index].copy()
    nobs = len(df_clean)

    return df_clean, nobs

# Usage in models.py:
formula = "growth ~ z_vagueness * is_hardware + z_employees_log + C(founding_cohort)"
df_model, n_effective = get_effective_sample_size(formula, df)

logger.info(f"Effective sample size: {n_effective:,} (from {len(df):,} input rows)")
model = smf.logit(formula, data=df_model).fit()
```

---

### 5. **Systematic Evidence Computation** ⭐⭐

**Multiverse Approach** (lines 405-438):
```python
def compute_evidence(coef: float, p: float, expected_sign: int) -> Tuple[float, int, int]:
    """
    Compute evidence metrics for hypothesis testing.

    Returns:
        - evidence_score: sign(coef) * -log10(p)  # Direction-weighted significance
        - is_consistent: 1 if sign matches expected and p < 0.05
        - is_surprise: 1 if sign opposes expected and p < 0.05
    """
    # Evidence score: positive if consistent, negative if surprising
    score = np.sign(coef) * (-np.log10(max(p, 1e-12)))

    # Consistency: right direction + significant
    consistent = int((np.sign(coef) == expected_sign) and (p < ALPHA))

    # Surprise: wrong direction + significant
    surprise = int((np.sign(coef) != expected_sign) and (p < ALPHA))

    return score, consistent, surprise

# Expected signs for hypotheses:
EXPECTED_SIGNS = {
    "vag_main": {"E": -1, "L1": +1, "L2": +1},  # E: vague→less funding, L: vague→more success
    "vagXoption": +1,       # Options amplify vagueness benefit
    "vagXsoftware": +1      # Software amplifies vagueness benefit
}
```

**Benefits**:
- ✅ **Standardized metrics** across all specifications
- ✅ **Easy to aggregate** - count consistent specs, average evidence scores
- ✅ **Detects surprising results** - flags when data contradicts theory

**How to Integrate**:
```python
# Add to src/models.py:

def compute_hypothesis_evidence(model_results: pd.DataFrame,
                                hypothesis: str,
                                expected_sign: int) -> Dict[str, Any]:
    """Compute evidence metrics for a hypothesis across specifications.

    Args:
        model_results: DataFrame with columns 'coef', 'pval'
        hypothesis: Name of hypothesis (e.g., 'H1_vagueness_main')
        expected_sign: Expected coefficient sign (-1 or +1)

    Returns:
        Dict with evidence metrics
    """
    evidence_scores = []
    consistent_count = 0
    surprise_count = 0

    for _, row in model_results.iterrows():
        coef = row['coef']
        pval = row['pval']

        if pd.notna(coef) and pd.notna(pval):
            # Direction-weighted significance
            score = np.sign(coef) * (-np.log10(max(pval, 1e-12)))
            evidence_scores.append(score)

            # Count consistent results
            if np.sign(coef) == expected_sign and pval < 0.05:
                consistent_count += 1

            # Count surprising results
            if np.sign(coef) != expected_sign and pval < 0.05:
                surprise_count += 1

    return {
        'hypothesis': hypothesis,
        'n_specs': len(model_results),
        'median_evidence': np.median(evidence_scores),
        'mean_evidence': np.mean(evidence_scores),
        'pct_consistent': 100 * consistent_count / len(model_results),
        'pct_surprise': 100 * surprise_count / len(model_results),
        'pct_significant': 100 * (consistent_count + surprise_count) / len(model_results)
    }
```

---

### 6. **Null Result Pattern** ⭐

**Multiverse Solution** (lines 293-324):
```python
def null_result(nobs: int, warning_code: int, method: str) -> Dict[str, Any]:
    """Return structured null result when model fails."""
    return {
        'coef_vag_main': np.nan,
        'p_vag_main': np.nan,
        'coef_vagXoption': np.nan,
        'p_vagXoption': np.nan,
        'nobs': nobs,
        'fit_stat': np.nan,
        'warning_code': warning_code,  # 3 = failed
        'estimation_method': method
    }
```

**Benefits**:
- ✅ **Never crashes** - always returns valid structure
- ✅ **Preserves metadata** - you know which spec failed
- ✅ **Easy aggregation** - NaN values handled gracefully

---

## 📊 Recommended Integration Priority

### Priority 1: Immediate Impact (Do First) 🔥

1. **3-Stage Robust Logit Fitting** → Prevents pipeline crashes
2. **Formula Builder** → Enables rapid specification testing
3. **Patsy-based nobs** → Accurate sample size reporting

### Priority 2: Medium-Term Efficiency (Next Sprint) 📈

4. **xarray Multiverse Coordinates** → Systematic spec testing
5. **Evidence Computation** → Standardized result interpretation

### Priority 3: Long-Term Robustness (Future) 🎯

6. **Specification Curve Visualization** → Publication-ready robustness plots
7. **Automatic Multiverse Caching** → Cache each specification separately

---

## 💡 Concrete Next Steps

### Step 1: Make H2 Models Crash-Proof (30 minutes)

```python
# Edit src/models.py to use 3-stage fallback
# This ALONE will save you hours of debugging!
```

### Step 2: Add Formula Builder (1 hour)

```python
# Create FormulaBuilder class in src/models.py
# Enables rapid iteration over control specifications
```

### Step 3: Update Cache for Multiverse (2 hours)

```python
# Extend cache_manager.py with multiverse support
# Save results with specification coordinates
```

### Step 4: Add Evidence Metrics (1 hour)

```python
# Create evidence computation functions
# Standardize result interpretation
```

---

## 🎯 Expected Efficiency Gains

| Improvement | Time Saved | Frustration Reduced |
|-------------|------------|---------------------|
| Robust logit fitting | 2-4 hours/week | ⭐⭐⭐⭐⭐ |
| Formula builder | 1-2 hours/week | ⭐⭐⭐⭐ |
| xarray multiverse | 3-5 hours/week | ⭐⭐⭐⭐⭐ |
| Evidence metrics | 1 hour/week | ⭐⭐⭐ |

**Total estimated time savings: 7-12 hours/week** 🚀

---

## 📚 Further Reading

- Multiverse analysis: [Steegen et al. (2016)](https://journals.sagepub.com/doi/10.1177/1745691616658637)
- Specification curves: [Simonsohn et al. (2020)](https://www.nature.com/articles/s41562-020-0912-z)
- xarray for scientific computing: [xarray.pydata.org](http://xarray.pydata.org/)
