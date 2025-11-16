# E/L Hypothesis Testing Pipeline

## Overview

Complete Jupyter notebook pipeline for testing H*: β_VF > 0 (Flexibility amplifies Vagueness effect on Later success).

Follows `test_pipeline_components.ipynb` format with 5 stages:
1. 🏗️ BUILD: Data consolidation
2. 🧠 DEFINE: Variable definition
3. 📊 PLOT1: Sanity checks
4. ⚖️ TEST: Hypothesis testing
5. 📈 PLOT2: Final plots

## Files

### Main Pipeline
- **`E_L_hypothesis_pipeline.ipynb`**: Complete interactive pipeline

### Supporting Scripts
- `scripts/consolidate_2021_cohort.py`: Consolidate E=1 cohort
- `scripts/validate_E_L_design.py`: Comprehensive validation
- `scripts/diagnose_vagueness_quality.py`: Vagueness quality diagnosis
- `modules/plots_F_series.py`: F-series plotting functions

### Legacy (for reference)
- `scripts/plot_EVF_LVF.py`: Standalone plotting script (superseded by notebook; incorrectly states EVF is impossible)

## Quick Start

### Prerequisites

```bash
# 1. Ensure raw data files exist
ls data/raw/Company20211201.parquet
ls data/raw/Company20231201.parquet
ls data/raw/Company20241201.parquet
ls data/raw/Company20251101.parquet

# 2. Run consolidation
python scripts/consolidate_2021_cohort.py
```

### Run Pipeline

Open Jupyter and run all cells:

```bash
jupyter notebook E_L_hypothesis_pipeline.ipynb
```

Or run cell-by-cell to inspect each stage.

## Pipeline Stages

### Stage 1: 🏗️ BUILD

**Purpose**: Load consolidated E=1 cohort

**Input**: `data/processed/companies_21_23-24-25.parquet`

**Verifies**:
- File exists
- All companies have E=1 (Early Stage VC)
- Required columns present

**Output**: `df` DataFrame with ~45,556 E=1 companies

---

### Stage 2: 🧠 DEFINE

**Purpose**: Define E, L, V, F variables

**Variables created**:

| Variable | Definition | Expected |
|----------|------------|----------|
| **E** | Early Stage VC funding amount ($M) | Continuous, log-normal distribution |
| **E=1 cohort** | Companies in Early Stage VC state | All companies (100% by design) |
| **L** | Later Stage VC / Series B+ (2025) | Binary, 15-40% |
| **V** | Vagueness from Description/Keywords | Continuous, mean ~50, std ~15-25 |
| **F** | Flexibility (1 - is_hardware) | Binary, both 0 and 1 |

**CRITICAL Distinctions**:
- **E (amount)**: Continuous variable for regression (funding amount)
- **E=1 (state)**: Binary filter for cohort selection (Early Stage VC status)
- **E is mediator**, not confounder: Do NOT include E in L regression

---

### Stage 3: 📊 PLOT1

**Purpose**: Sanity check each variable

**Plots generated**:
1. E distribution (should be all E=1)
2. L distribution (should be 15-40%)
3. V distribution (should have reasonable variance)
4. F distribution (should have both 0 and 1)

**Pass criteria**:
- ✅ E: 100% = 1
- ✅ L: 15-40% = 1
- ✅ V: std >= 10
- ✅ F: Both values present

---

### Stage 4: ⚖️ TEST

**Purpose**: Test H*: β_VF > 0

**Model**: `L ~ z_V * F_flexibility + C(founding_cohort) + C(region)`

**Key coefficients**:
- β_V: Vagueness main effect (expect > 0)
- β_F: Flexibility main effect
- β_VF: Interaction term (TARGET: expect > 0)

**Hypothesis**:
- H0: β_VF = 0
- H1: β_VF > 0 (one-tailed test)

**Verdict**:
- ✅ REJECT H0 if β_VF > 0 and p < 0.05
- ❌ FAIL TO REJECT H0 otherwise

---

### Stage 5: 📈 PLOT2

**Purpose**: Generate final interaction plots

**Plots generated**:
- **EVF (F1b)**: E ~ V × F interaction (Early funding amount)
  - E is continuous (funding amount in $M), not binary
  - F=1 (Flexible/SW): skyblue solid line
  - F=0 (Rigid/HW): gray dashed line
  - Tests whether flexibility moderates vagueness effect on early funding
- **LVF (F3a)**: L ~ V × F interaction (Later success probability)
  - L is binary (Series B+ achievement)
  - F=1 (Flexible/SW): skyblue solid line
  - F=0 (Rigid/HW): gray dashed line
  - If β_VF > 0, lines should diverge

**Output**:
- `outputs/figures/F1b_E_given_F.png` (and `.pdf`) - EVF plot
- `outputs/figures/F3a_L_given_F.png` (and `.pdf`) - LVF plot
- All F-series plots

---

## Integration with `plots_F_series.py`

The notebook uses functions from `modules/plots_F_series.py`:

### Available Functions

| Function | Purpose | Used in Pipeline |
|----------|---------|------------------|
| `fig_F1b_E_given_F()` | EVF interaction plot (E ~ V × F) | ✅ Stage 5 |
| `fig_F3a_L_given_F()` | LVF interaction plot (L ~ V × F) | ✅ Stage 5 |
| `fig_F1_E_vs_V()` | E ~ V scatter | ❌ (E ~ V, no interaction) |
| `fig_F2_PrL_vs_V()` | Pr(L) ~ V | ❌ (no F stratification) |
| `create_F_series()` | Generate all F-series | ✅ Stage 5 (optional) |

### EVF Plot Implementation

**EVF = E ~ V × F interaction**

**E is continuous (funding amount)**:
- E = Early Stage VC funding amount in $M (continuous variable)
- E=1 cohort = Companies in Early Stage VC state (binary filter)
- These are distinct: E (amount) vs E=1 (state membership)

**Model**:
- E ~ V * F + controls (OLS regression)
- Within E=1 cohort, tests if flexibility moderates vagueness effect on funding amount

**Available in `plots_F_series.py`**:
- `fig_F1b_E_given_F()`: E ~ V × F interaction (EVF plot)
- Requires `HEV_interaction` model in results dictionary

### Comparison: `plot_EVF_LVF.py` vs `plots_F_series.py`

| Feature | `plot_EVF_LVF.py` | `plots_F_series.py` |
|---------|-------------------|---------------------|
| **EVF Plot** | Incorrectly skips | `fig_F1b_E_given_F()` ✅ |
| **LVF Plot** | Standalone script | `fig_F3a_L_given_F()` function |
| **Color Palette** | W2-compliant | W2-compliant |
| **Output** | PNG + PDF | PNG + PDF |
| **Integration** | None | Part of F-series suite |

**Recommendation**: Use notebook with `plots_F_series.py` functions (better integration).

**Note**: `plot_EVF_LVF.py` was created before realizing E is continuous (funding amount), not binary. It incorrectly states EVF is impossible. The notebook and `plots_F_series.py` have the correct implementation.

---

## Validation

### Comprehensive Validation

```bash
python scripts/validate_E_L_design.py
```

**Tests**:
1. E=1 cohort purity (100%)
2. L definition correctness
3. Temporal consistency (L monotonic increase)
4. Cohort stability (no survivorship bias)
5. Impossible transitions detection
6. Progression rate sanity (15-40%)
7. Outcome categories
8. V×F feasibility

### Vagueness Quality Diagnosis

If vagueness std < 5:

```bash
python scripts/diagnose_vagueness_quality.py
```

**Checks**:
- Description/Keywords availability
- Non-empty rates
- Sample content
- Length statistics
- Vagueness distribution
- Extreme value samples

---

## Expected Results

### If Hypothesis Supported

```
================================================================================
VERDICT
================================================================================

✅ REJECT H0: Flexibility AMPLIFIES Vagueness effect
   β_VF = 0.1890 > 0, p = 0.0078 **

   Interpretation: High vagueness helps flexible companies MORE
   than rigid companies in achieving later success.
```

**LVF Plot**: Skyblue line (F=1) steeper than gray line (F=0)

### If Hypothesis NOT Supported

```
================================================================================
VERDICT
================================================================================

❌ FAIL TO REJECT H0
   β_VF = -0.0234, p = 0.3421
   Reason: β_VF is not positive (wrong direction)
```

**LVF Plot**: Lines parallel or gray steeper than skyblue

---

## Troubleshooting

### Issue 1: File Not Found

```
❌ Consolidated file not found!
   Expected: data/processed/companies_21_23-24-25.parquet
```

**Solution**:
```bash
python scripts/consolidate_2021_cohort.py
```

### Issue 2: Vagueness Std Too Small

```
⚠️  WARNING: Vagueness std (4.37) is very small!
```

**Solution**:
```bash
python scripts/diagnose_vagueness_quality.py
```

Check:
- Description/Keywords non-empty rates
- Sample content quality
- Vagueness scorer logic

### Issue 3: F Has Only One Value

```
✗ FAIL: F has only one value!
   Interaction test will not be possible.
```

**Solution**:
- Improve F_flexibility inference logic
- Use better industry classification
- Check CompanyName keywords

### Issue 4: Model Fitting Failed

```
❌ Hypothesis test FAILED: Singular matrix
```

**Possible causes**:
- Perfect separation (all L=0 or all L=1 in one group)
- Insufficient sample size
- Control variables have no variance

**Solution**:
- Check sample size by F group
- Remove constant controls
- Use regularization (already built into `run_HLVF`)

---

## Output Files

### Plots

```
outputs/figures/
├── F1b_E_given_F.png          # EVF interaction plot (E ~ V × F)
├── F1b_E_given_F.pdf
├── F3a_L_given_F.png          # LVF interaction plot (L ~ V × F)
├── F3a_L_given_F.pdf
├── F1_E_vs_V.png              # E ~ V (if HEV provided)
├── F2_PrL_vs_V.png            # Pr(L) ~ V (if HLVF provided)
└── ... (other F-series plots)
```

### Data

```
data/processed/
├── companies_21_23-24-25.parquet           # All E=1 companies
├── companies_21_23-24-25_quantum.parquet   # Quantum subset
└── companies_21_23-24-25_transportation.parquet
```

---

## Next Steps

### 1. Industry-Specific Analysis

Run pipeline for quantum or transportation subsets:

```bash
# Quantum computing
INPUT_FILE = PROCESSED_DIR / "companies_21_23-24-25_quantum.parquet"

# Transportation
INPUT_FILE = PROCESSED_DIR / "companies_21_23-24-25_transportation.parquet"
```

### 2. Robustness Checks

Add alternative specifications:
- Different control variables
- Different time windows (2023, 2024, 2025)
- Subsample analysis

### 3. Publication

Use generated plots for:
- Paper figures (PDFs)
- Presentations (PNGs)
- Documentation

---

## References

- E/L definitions: `scripts/README_E_L_DEFINITION.md`
- Validation methods: `scripts/VALIDATION_METHODS.md`
- Implementation status: `scripts/IMPLEMENTATION_STATUS.md`
- Test format: `test_pipeline_components.ipynb`
- Color palette: W2 slides (p.29-31)

---

## Summary

✅ **Complete pipeline from raw data to hypothesis test**

1. Consolidation ensures E=1 cohort purity
2. Variable definition follows research design
3. Sanity checks catch data quality issues
4. Hypothesis test uses correct model (NO E control)
5. Interaction plots show mechanism visually

✅ **Integration with existing codebase**

- Uses `modules/plots_F_series.py` functions
- Follows `test_pipeline_components.ipynb` format
- Compatible with validation scripts

✅ **EVF and LVF implementation**

- EVF (E ~ V × F): Fully implemented using E as continuous funding amount
- E = Early funding amount ($M), E=1 = Early Stage VC state (distinct concepts)
- LVF (L ~ V × F): Fully implemented using L as binary Later success
- Both plots use W2 color palette and proper interaction visualization
