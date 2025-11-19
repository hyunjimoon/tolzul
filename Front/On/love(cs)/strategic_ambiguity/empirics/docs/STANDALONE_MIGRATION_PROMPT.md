# Migration Prompt: Make Empirics_Early/Later Standalone

**For**: Claude Code (separate session)
**Task**: Transform thesis run.py files into minimal, standalone Python scripts

---

## Context

You have TWO Python files that need to become **standalone** (no dependencies on the `empirics_ent_strat_ops` repository):

**Target Files** (to be modified):
1. `/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/theory/thesis/2️⃣_PRODUCTION/Empirics_Early/run.py`
2. `/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/theory/thesis/2️⃣_PRODUCTION/Empirics_Later/run.py`

**Reference File** (contains full implementations):
- `/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics_ent_strat_ops/archive/run_analysis.py`

**Goal**: Port missing functionality from reference file to make target files fully independent.

---

## Functional Gap Analysis

### **Empirics_Early/run.py** - Current vs Needed

| Function | Current Status | Needs from `archive/run_analysis.py` |
|----------|---------------|--------------------------------------|
| **Data Loading** | ❌ Synthetic data generator | ✅ Real PitchBook .dat file loading with parquet caching |
| **Vagueness Scoring** | ❌ Missing | ✅ StrategicVaguenessScorerV2 class (full implementation) |
| **H1 Regression** | ✅ Basic OLS present | ✅ Add robust SE (HC3), better controls |
| **Feature Engineering** | ❌ Minimal (z-score only) | ✅ Full preprocessing pipeline |
| **Output Generation** | ✅ Basic (table + figure) | ✅ Add CSV export, multiple formats |

### **Empirics_Later/run.py** - Current vs Needed

| Function | Current Status | Needs from `archive/run_analysis.py` |
|----------|---------------|--------------------------------------|
| **Data Loading** | ❌ Placeholder CSV | ✅ Load from H2 analysis dataset (created by Empirics_Early or archive) |
| **Vagueness Scoring** | ❌ Assumes pre-computed | ✅ Verify z_vagueness exists, else compute |
| **H2 Logit** | ✅ Basic logit present | ✅ Add multi-stage fallback for convergence |
| **DV Construction** | ❌ Assumes series_b_plus exists | ✅ `create_survival_seriesb_progression()` function |
| **Interaction Plot** | ✅ Basic plot present | ✅ Use F-series styling (color palette, fonts) |
| **AME Calculation** | ⚠️ Manual, incomplete | ✅ Proper marginal effects with SE |
| **Spec Curve** | ⚠️ Placeholder logic | ✅ Full implementation or remove if not needed |

---

## Detailed Function Mapping

### **1. Data Loading with Parquet Caching** (HIGH PRIORITY)

**Source**: `archive/run_analysis.py` lines 46-72

**Copy THIS function** to both Empirics_Early and Empirics_Later:

```python
def read_snapshot_cached(path, encoding='utf-8'):
    """
    Read .dat file with Parquet caching for 10-50x speed improvement.

    First run: Reads .dat and creates .parquet cache
    Subsequent runs: Reads .parquet (much faster!)
    """
    from pathlib import Path
    import pandas as pd

    # Parquet cache path
    parquet_path = Path(str(path).replace('.dat', '.parquet'))

    # Use cache if it exists and is newer than source
    if parquet_path.exists() and parquet_path.stat().st_mtime > path.stat().st_mtime:
        print(f"  ✓ Loading from cache: {parquet_path.name} (fast!)")
        return pd.read_parquet(parquet_path)

    # No cache - read .dat and create cache
    print(f"  ⏳ Reading .dat file: {path.name} (first run is slow...)")
    try:
        df = pd.read_csv(path, sep='|', encoding=encoding, low_memory=False)
    except UnicodeDecodeError:
        df = pd.read_csv(path, sep='|', encoding='latin-1', low_memory=False)

    # Save to Parquet cache for next time
    print(f"  💾 Caching to: {parquet_path.name} (next run will be 10-50x faster!)")
    df.to_parquet(parquet_path, index=False, compression='snappy')

    return df
```

**Integration**:
- **Empirics_Early**: Replace `load_data()` synthetic generator with real file loading
- **Empirics_Later**: Use to load h2_analysis_dataset.csv if exists, else load raw data

---

### **2. Vagueness Scoring V2** (HIGH PRIORITY)

**Source**: `/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics_ent_strat_ops/modules/vagueness_v2.py` (FULL FILE)

**Option A (Recommended)**: Copy entire `StrategicVaguenessScorerV2` class into run.py
- Pros: Fully standalone
- Cons: ~600 lines (but well-documented)

**Option B**: Import from empirics_ent_strat_ops (requires path setup)
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "empirics_ent_strat_ops"))
from modules.vagueness_v2 import StrategicVaguenessScorerV2
```

**Usage Pattern** (add to both files):
```python
def compute_vagueness(df):
    """Compute vagueness scores using V2 scorer"""
    # Combine description and keywords
    texts = (df['Description'].fillna('') + ' ' + df['Keywords'].fillna('')).tolist()

    # Initialize V2 scorer with IDF weighting
    scorer = StrategicVaguenessScorerV2(use_idf=True)

    # Fit on corpus (compute IDF weights)
    scorer.fit(texts)

    # Transform to get scores
    results = scorer.transform(texts)

    # Add to dataframe
    df['S_cat'] = results['S_cat']
    df['S_concdef'] = results['S_concdef']
    df['vagueness'] = results['V_raw']  # Primary measure
    df['vagueness_pct'] = results['V_pct']

    # Z-score for regression
    df['vagueness_zscore'] = (df['vagueness'] - df['vagueness'].mean()) / df['vagueness'].std()

    return df
```

---

### **3. Hardware/Software Classification** (MEDIUM PRIORITY)

**Source**: `modules/features.py` lines 1290-1320 (from archive imports)

**Simplified version for standalone**:

```python
def classify_hardware(keywords):
    """
    Binary HW/SW classification based on keywords.

    Returns:
        1 = Hardware/Integrated (Biotech, Hardware/Robotics)
        0 = Software/Non-integrated (all others)
    """
    if pd.isna(keywords):
        return 0

    kw = str(keywords).lower()

    # Hardware indicators
    hw_keywords = [
        'biotech', 'pharma', 'drug', 'health', 'medical', 'therapeutics',
        'hardware', 'robotics', 'robot', 'chip', 'semiconductor',
        'sensor', 'device', 'manufacturing', 'asic', 'fpga', 'quantum'
    ]

    # If ANY hardware keyword matches → HW (1)
    if any(hw_kw in kw for hw_kw in hw_keywords):
        return 1

    # Otherwise → SW (0)
    return 0

# Apply to dataframe
df['hardware'] = df['Keywords'].apply(classify_hardware)
```

---

### **4. Series B+ DV Construction** (HIGH PRIORITY for Empirics_Later)

**Source**: `modules/features.py` lines 1001-1223

**Problem**: This function is 223 lines and complex (4-snapshot LLM2 approach).

**Options**:

**Option A**: Copy full function (recommended if you need robustness)
- Get `create_survival_seriesb_progression()` from modules/features.py

**Option B**: Simplified version (if you already have series_b_plus column)
```python
def create_growth_dv(df, endpoint_date="2023-05-01"):
    """
    Simplified Series B+ DV construction.

    Assumes df has columns:
    - series_a_date: Date of Series A
    - latest_round: Last known round (e.g., "Series B", "Series C")
    - latest_round_date: Date of latest round

    Returns:
        Binary column 'growth' (1 if reached Series B+ within window)
    """
    # Convert dates
    df['series_a_date'] = pd.to_datetime(df['series_a_date'])
    df['latest_round_date'] = pd.to_datetime(df['latest_round_date'])

    # Check if Series B+ achieved
    series_b_plus_rounds = ['Series B', 'Series C', 'Series D', 'Series E+']
    df['reached_seriesb'] = df['latest_round'].isin(series_b_plus_rounds).astype(int)

    # Check if within time window (e.g., 17 months)
    endpoint = pd.to_datetime(endpoint_date)
    df['within_window'] = (df['latest_round_date'] <= endpoint).astype(int)

    # Growth = reached Series B+ AND within window
    df['growth'] = (df['reached_seriesb'] & df['within_window']).astype(int)

    return df
```

**Recommendation**: If your data already has `series_b_plus` column, skip this and use directly.

---

### **5. Multi-Stage Logit Fallback** (HIGH PRIORITY for Empirics_Later)

**Source**: `modules/models.py` lines 105-138

**Copy THIS function** to Empirics_Later/run.py:

```python
def fit_logit_robust(formula, data):
    """
    Fit logit with multi-stage fallback for convergence issues.

    Stage 1: Standard MLE
    Stage 2: L1 regularization (alpha=0.1)
    Stage 3: Stronger L1 (alpha=0.5)

    Returns: Fitted model
    """
    import statsmodels.formula.api as smf

    # Drop missing values
    required_vars = ['growth', 'vagueness_zscore', 'hardware']
    d = data.dropna(subset=required_vars).copy()

    print(f"  Sample size: {len(d):,}")

    # Stage 1: Standard fit
    try:
        print("  Stage 1: Attempting standard logit...")
        model = smf.logit(formula, data=d).fit(disp=False)
        print("  ✓ Standard fit successful")
        return model
    except Exception:
        print("  ✗ Failed, trying L1 regularization...")

    # Stage 2: L1 with alpha=0.1
    try:
        print("  Stage 2: L1 regularization (alpha=0.1)...")
        model = smf.logit(formula, data=d).fit_regularized(
            method='l1', alpha=0.1, disp=False, maxiter=200, warn_convergence=False
        )
        print("  ✓ L1 (alpha=0.1) successful")
        return model
    except Exception:
        print("  ✗ Failed, trying stronger regularization...")

    # Stage 3: L1 with alpha=0.5
    try:
        print("  Stage 3: L1 regularization (alpha=0.5)...")
        model = smf.logit(formula, data=d).fit_regularized(
            method='l1', alpha=0.5, disp=False, maxiter=200, warn_convergence=False
        )
        print("  ✓ L1 (alpha=0.5) successful")
        return model
    except Exception:
        raise RuntimeError("All logit convergence strategies failed. Check data for perfect separation.")
```

**Replace current logit call**:
```python
# OLD:
model = smf.logit(formula, data=df).fit(cov_type='HC3', maxiter=100)

# NEW:
model = fit_logit_robust(formula, df)
# Then add robust SE if needed
model_robust = model.get_robustcov_results(cov_type='HC3')
```

---

### **6. F-Series Plot Styling** (MEDIUM PRIORITY for Empirics_Later)

**Source**: `modules/plots_F_series.py` lines 45-70

**Color Palette**:
```python
# W2 Convention - EXACT colors
PALETTE = {
    "E": "red",          # Early funding
    "L": "#0000FF",      # Later success (pure blue)
    "V": "green",        # Vagueness
    "F": "skyblue",      # Flexibility/Software
    "HW": "gray",        # Hardware
}

# Line styles for interactions
LINE_STYLES = {
    'F=1': {'color': 'skyblue', 'linestyle': '-', 'linewidth': 2.5},   # Software
    'F=0': {'color': 'gray', 'linestyle': '--', 'linewidth': 2.5},     # Hardware
}
```

**Update plot_interaction() in Empirics_Later**:
```python
# Replace current plot colors with:
plt.plot(vagueness_range, pred_sw, **LINE_STYLES['F=1'], label='Software (HW=0)')
plt.plot(vagueness_range, pred_hw, **LINE_STYLES['F=0'], label='Hardware (HW=1)')

# Color axes
ax.set_xlabel('Vagueness (z-score)', fontsize=13, fontweight='bold', color=PALETTE['V'])
ax.set_ylabel('Pr(Series B+)', fontsize=13, fontweight='bold', color=PALETTE['L'])
ax.tick_params(axis='x', colors=PALETTE['V'])
ax.tick_params(axis='y', colors=PALETTE['L'])
```

---

### **7. Feature Engineering Pipeline** (MEDIUM PRIORITY)

**Source**: `archive/run_analysis.py` lines 99-106

**Minimal version**:

```python
def engineer_features(df):
    """
    Minimal feature engineering for H1/H2 tests.

    Adds:
    - vagueness scores (via V2 scorer)
    - is_hardware (binary classification)
    - z-scored variables
    - founding_cohort (categorical)
    """
    # 1. Vagueness (using V2 scorer)
    df = compute_vagueness(df)

    # 2. Hardware classification
    df['hardware'] = df['Keywords'].apply(classify_hardware)
    df['is_hardware'] = df['hardware']  # Alias for consistency

    # 3. Founding cohort
    if 'year_founded' in df.columns:
        df['founding_cohort'] = pd.cut(
            df['year_founded'],
            bins=[0, 2009, 2014, 2018, 2020, 2025],
            labels=['<2010', '2010-14', '2015-18', '2019-20', '2021']
        ).astype(str)

    # 4. Z-score employees (if exists)
    if 'employees' in df.columns:
        df['employees_log'] = np.log1p(df['employees'])
        df['z_employees_log'] = (
            (df['employees_log'] - df['employees_log'].mean()) /
            df['employees_log'].std()
        )

    # 5. Serial founder (if exists)
    if 'founder_credibility' in df.columns:
        df['is_serial'] = (df['founder_credibility'] > 0).astype(int)
    else:
        # Default to 0 if not available
        df['is_serial'] = 0

    return df
```

---

## Migration Checklist

### **For Empirics_Early/run.py**:

- [ ] Replace `load_data()` synthetic generator with `read_snapshot_cached()`
- [ ] Add `StrategicVaguenessScorerV2` class (copy from vagueness_v2.py)
- [ ] Add `compute_vagueness()` function
- [ ] Add `classify_hardware()` function
- [ ] Add `engineer_features()` pipeline
- [ ] Update `run_h1_regression()` to use robust SE (HC3)
- [ ] Update paths to load from `../../1️⃣_INPUT/data/Company*.dat`
- [ ] Add CSV export for regression coefficients
- [ ] Verify output paths: `../../3️⃣_OUTPUT/tables/` and `../../3️⃣_OUTPUT/figures/`

### **For Empirics_Later/run.py**:

- [ ] Add `fit_logit_robust()` function for convergence handling
- [ ] Replace `load_series_a_sample()` with actual data loading (from Empirics_Early output or h2_analysis_dataset.csv)
- [ ] Add DV construction if needed (`create_growth_dv()` or use existing)
- [ ] Update `plot_interaction()` with F-series color palette
- [ ] Add proper AME calculation (use statsmodels `.get_margeff()`)
- [ ] Verify interaction term is created explicitly (`vague_x_hw`)
- [ ] Update output paths
- [ ] Optional: Simplify or remove `spec_curve_analysis()` if not essential

---

## Testing Strategy

After migration, run these tests:

### **Test 1: Empirics_Early Standalone**
```bash
cd theory/thesis/2️⃣_PRODUCTION/Empirics_Early
python run.py
```

**Expected outputs**:
- `../../3️⃣_OUTPUT/tables/table1_h1_regression.txt`
- `../../3️⃣_OUTPUT/figures/fig3_h1_scatter.pdf`

**Validation**:
- Vagueness coefficient should be negative
- Sample size > 1000
- Plot shows scatter + regression line

### **Test 2: Empirics_Later Standalone**
```bash
cd theory/thesis/2️⃣_PRODUCTION/Empirics_Later
python run.py
```

**Expected outputs**:
- `../../3️⃣_OUTPUT/tables/table2_h2_logit.txt`
- `../../3️⃣_OUTPUT/figures/fig4_vxh_interaction.pdf`

**Validation**:
- Interaction term present in output
- Logit converges (check for L1 regularization messages)
- Plot shows diverging lines (software vs hardware)

---

## Priority Levels

**MUST HAVE** (without these, files won't run):
1. ✅ Vagueness Scorer V2 (full class)
2. ✅ Data loading with parquet caching
3. ✅ Multi-stage logit fallback (Empirics_Later only)
4. ✅ Hardware classification function

**SHOULD HAVE** (improves robustness):
5. ⚠️ Feature engineering pipeline
6. ⚠️ DV construction (if series_b_plus not pre-computed)
7. ⚠️ Robust SE (HC3) for H1

**NICE TO HAVE** (improves presentation):
8. ○ F-series color palette
9. ○ Proper AME calculation
10. ○ Spec curve analysis (or remove)

---

## Example: Minimal Empirics_Early/run.py Structure

```python
"""
Empirics_Early/run.py - STANDALONE VERSION
Test H1: Vagueness → Series A Funding (−)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from statsmodels.formula.api import ols

# ============================================================================
# SECTION 1: UTILITY FUNCTIONS (Ported from empirics_ent_strat_ops)
# ============================================================================

def read_snapshot_cached(path, encoding='utf-8'):
    """[Copy full implementation from archive/run_analysis.py lines 46-72]"""
    pass

class StrategicVaguenessScorerV2:
    """[Copy full class from modules/vagueness_v2.py]"""
    pass

def classify_hardware(keywords):
    """[See simplified version above]"""
    pass

def compute_vagueness(df):
    """[See usage pattern above]"""
    pass

def engineer_features(df):
    """[See minimal version above]"""
    pass

# ============================================================================
# SECTION 2: MAIN ANALYSIS
# ============================================================================

def load_data():
    """Load PitchBook data from .dat file"""
    DATA_PATH = Path("../../1️⃣_INPUT/data/Company20220101.dat")
    df = read_snapshot_cached(DATA_PATH)

    # Filter to Series A companies
    df = df[df['last_round_type'] == 'Series A'].copy()

    # Engineer features
    df = engineer_features(df)

    return df

def run_h1_regression(df):
    """[Keep existing implementation, add HC3]"""
    model = ols(formula, data=df).fit(cov_type='HC3')
    return model

def plot_h1_scatter(df, model):
    """[Keep existing implementation]"""
    pass

def main():
    df = load_data()
    model = run_h1_regression(df)
    plot_h1_scatter(df, model)

if __name__ == "__main__":
    main()
```

---

## Success Criteria

**Standalone test passes if**:
1. ✅ No import errors (no dependency on empirics_ent_strat_ops)
2. ✅ Loads real PitchBook data (not synthetic)
3. ✅ Computes vagueness using V2 scorer
4. ✅ Regression runs and produces valid coefficients
5. ✅ Outputs saved to correct directories
6. ✅ Results match archive/run_analysis.py outputs (within ±5%)

---

## Minimal Diff Approach (If Short on Time)

If you need a quick fix:

**Empirics_Early**:
```python
import sys
sys.path.insert(0, '../../../../empirics_ent_strat_ops')
from modules.vagueness_v2 import StrategicVaguenessScorerV2
from archive.run_analysis import read_snapshot_cached, engineer_features
```

**Empirics_Later**:
```python
import sys
sys.path.insert(0, '../../../../empirics_ent_strat_ops')
from modules.models import test_h2_main_growth
from modules.plots_F_series import fig_F3a_L_given_F
```

**Pros**: Minimal code changes
**Cons**: Not truly standalone (still depends on empirics repo)

---

## Next Steps

1. **Read both target files** (Empirics_Early/run.py and Empirics_Later/run.py)
2. **Identify missing functions** using gap analysis above
3. **Copy implementations** from archive/run_analysis.py and modules/
4. **Test incrementally**:
   - First get data loading working
   - Then vagueness scoring
   - Then regression
   - Finally plotting
5. **Validate results** against archive/run_analysis.py outputs

---

**Questions to ask the user**:
1. Do you want fully standalone files (no empirics_ent_strat_ops dependency)?
2. Do you already have series_b_plus column in your data, or need DV construction?
3. Should I preserve spec_curve_analysis() or remove it (seems incomplete)?
4. What is your data source: PitchBook .dat files or pre-processed CSV?

**End of Migration Prompt**
