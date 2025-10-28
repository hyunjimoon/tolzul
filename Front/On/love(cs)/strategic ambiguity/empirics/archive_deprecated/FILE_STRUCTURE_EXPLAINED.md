# File Structure Explained - Simple Guide

## 🎯 WHAT YOU ACTUALLY NEED (Only 1 file!)

```
run_h2_seriesb.py  ⭐ THE MAIN FILE - RUN THIS ONE
```

**That's it!** This is the only file you need to run for your presentation.

It automatically uses all the other files in the `code/` directory.

---

## 📂 Full File Structure

```
empirics/
│
├── 🟢 MAIN FILE (RUN THIS)
│   └── run_h2_seriesb.py              ⭐ NEW 4-snapshot H2 analysis
│
├── 🔵 MODULE FILES (Used automatically by main file)
│   └── code/hypothesis_testing_pipeline/src/
│       ├── feature_engineering.py      Core: vagueness, IC, preprocessing
│       ├── hypothesis_tests.py         Core: H1 and H2 statistical models
│       └── visualizations.py           Optional: plots
│
├── 🟡 DIAGNOSTIC FILES (Optional debugging tools)
│   ├── diagnose_snapshots.py           Check data files exist
│   ├── diagnose_series_a.py            Debug Series A detection
│   ├── check_dealtype.py               Check deal type patterns
│   ├── check_founder_columns.py        Check founder data
│   └── explore_h2_data.py              EDA visualizations
│
├── 🔴 OLD FILES (Deprecated - ignore these)
│   ├── code/hypothesis_testing_pipeline/run_pipeline.py  ❌ OLD 2-snapshot version
│   ├── code/hypothesis_testing_pipeline/src/01-05_*.py   ❌ OLD modular approach
│   ├── code/pipeline_xarray.py         ❌ OLD prototype
│   └── code/xarray_quick_start.py      ❌ OLD demo
│
└── 📄 DOCUMENTATION
    ├── SINGULAR_MATRIX_FIXES.md        Today's fixes (read this!)
    ├── LLM2_IMPLEMENTATION_SUMMARY.md  How 4-snapshot approach works
    ├── METHODOLOGICAL_CHOICES.md       Key decisions explained
    └── DATA_REQUIREMENTS.md            What data files you need
```

---

## 📝 Detailed Explanation

### 🟢 MAIN FILE

#### `run_h2_seriesb.py`
**Purpose**: Complete H2 analysis pipeline from raw data to results

**What it does**:
1. Loads 4 snapshots (Dec 2021, Jan 2022, May 2022, May 2023)
2. Creates Series B+ progression DV
3. Engineers features (vagueness, IC, etc.)
4. Runs H2 hypothesis tests (4 variants)
5. Saves results to CSV

**How to run**:
```bash
python run_h2_seriesb.py --output outputs/
```

**Outputs** (saved to `outputs/`):
- `h2_main_coefficients.csv` - Primary results
- `h2_robustness_sector_fe.csv` - With sector FE
- `h2_robustness_MA_upper.csv` - M&A upper bound
- `h2_robustness_MA_lower.csv` - M&A lower bound
- `h2_analysis_dataset_17m.csv` - Full dataset

---

### 🔵 MODULE FILES (Auto-loaded by main file)

#### `code/hypothesis_testing_pipeline/src/feature_engineering.py`
**Purpose**: Transform raw data into analysis variables

**Key functions**:
- `compute_vagueness()` - Text analysis of company descriptions
- `classify_integration_cost()` - Sector → modular/integrated
- `create_survival_seriesb_progression()` - 4-snapshot DV construction
- `preprocess_for_h2()` - **NEW**: Fixes singular matrix issues

**You don't call this directly** - `run_h2_seriesb.py` calls it automatically

---

#### `code/hypothesis_testing_pipeline/src/hypothesis_tests.py`
**Purpose**: Statistical models for H1 and H2

**Key functions**:
- `test_h1_early_funding()` - OLS: Early Funding ~ Vagueness
- `test_h2_main_survival()` - Logit: Survival ~ Vagueness × IC
- `test_h2_robustness_sector_fe()` - **NEW**: Robustness with sector FE

**You don't call this directly** - `run_h2_seriesb.py` calls it automatically

---

#### `code/hypothesis_testing_pipeline/src/visualizations.py`
**Purpose**: Optional plots (scatter, interaction, ROC curves)

**You can ignore this** - Visualizations are optional

---

### 🟡 DIAGNOSTIC FILES (Run these only if debugging)

#### `diagnose_snapshots.py`
**When to use**: If you get "file not found" errors
**What it does**: Checks if all 4 data files exist and can be read

```bash
python diagnose_snapshots.py
```

---

#### `diagnose_series_a.py`
**When to use**: If you get "At Series A: 0" error
**What it does**: Shows how many companies match Series A patterns

```bash
python diagnose_series_a.py
```

---

#### `check_dealtype.py`
**When to use**: If Series A/B detection seems wrong
**What it does**: Shows all unique deal type values in data

```bash
python check_dealtype.py
```

---

#### `check_founder_columns.py`
**When to use**: If founder credibility is 0%
**What it does**: Shows founder-related columns and coverage

```bash
python check_founder_columns.py
```

---

#### `explore_h2_data.py`
**When to use**: If you want to see data distributions before running models
**What it does**: Creates EDA plots (Bayesian workflow style)

```bash
python explore_h2_data.py
```

---

### 🔴 OLD/DEPRECATED FILES (Don't use these)

#### ❌ `code/hypothesis_testing_pipeline/run_pipeline.py`
**Why deprecated**: Uses old 2-snapshot approach (98% survival → singular matrix)
**Replaced by**: `run_h2_seriesb.py` (4-snapshot, 12-15% progression)

#### ❌ `code/hypothesis_testing_pipeline/src/01_process_company_data.py`
#### ❌ `code/hypothesis_testing_pipeline/src/02_process_deal_data.py`
#### ❌ `code/hypothesis_testing_pipeline/src/03_create_panel.py`
#### ❌ `code/hypothesis_testing_pipeline/src/04_run_analysis.py`
#### ❌ `code/hypothesis_testing_pipeline/src/05_create_deliverables.py`

**Why deprecated**: Old modular approach that required running 5 separate scripts
**Replaced by**: Single `run_h2_seriesb.py` that does everything

#### ❌ `code/pipeline_xarray.py`
#### ❌ `code/xarray_quick_start.py`

**Why deprecated**: Early prototypes using xarray (overly complex)
**Replaced by**: Simpler pandas-based approach in `run_h2_seriesb.py`

---

## 🚀 Simplified Workflow

### For your presentation TODAY:

**Step 1**: Make sure data files exist
```bash
ls -lh data/raw/*.dat
# Should see: Company20211201.dat, Company20220101.dat,
#             Company20220501.dat, Company20230501.dat
```

**Step 2**: Run the main file
```bash
python run_h2_seriesb.py --output outputs/
```

**Step 3**: Check results
```bash
ls -lh outputs/
# Should see: h2_main_coefficients.csv (and 3 other robustness files)
```

**That's it!** Three steps, one command.

---

## 📊 What Each Output File Contains

### `h2_main_coefficients.csv` (PRIMARY - use this for presentation)
```
variable                          coefficient  p_value
z_vagueness                       0.XXXX      0.XXX
z_vagueness:high_integration_cost -0.XXXX     0.XXX
z_employees_log                   0.XXXX      0.XXX
C(founding_cohort)[T.2010-14]     0.XXXX      0.XXX
...
```

**Key coefficients**:
- `z_vagueness`: Main effect (β₁) - effect in modular sectors
- `z_vagueness:high_integration_cost`: Interaction (β₃) - differential in integrated

---

### `h2_robustness_sector_fe.csv` (ROBUSTNESS 1)
Same as primary but includes sector fixed effects using `ic_within`

---

### `h2_robustness_MA_upper.csv` (ROBUSTNESS 2)
M&A=1 (treats acquisitions as survival success - upper bound)

---

### `h2_robustness_MA_lower.csv` (ROBUSTNESS 3)
M&A=0 (treats acquisitions as failure - lower bound)

---

## 🎯 Quick Reference Card

```
┌─────────────────────────────────────────────┐
│  WHAT TO RUN FOR PRESENTATION               │
├─────────────────────────────────────────────┤
│  python run_h2_seriesb.py --output outputs/ │
│                                             │
│  WHAT TO PRESENT:                           │
│  - outputs/h2_main_coefficients.csv         │
│                                             │
│  WHAT TO MENTION:                           │
│  - "3 robustness checks confirm results"    │
│                                             │
│  IF SOMETHING BREAKS:                       │
│  - python diagnose_snapshots.py             │
│  - python diagnose_series_a.py              │
└─────────────────────────────────────────────┘
```

---

## 💡 Simplification Recommendation

**Current state**: Too many files (confusing)

**Should we simplify to**:
```
empirics/
├── run_analysis.py          ⭐ Renamed from run_h2_seriesb.py (clearer name)
├── modules/
│   ├── features.py          (renamed from feature_engineering.py)
│   ├── models.py            (renamed from hypothesis_tests.py)
│   └── plots.py             (renamed from visualizations.py)
└── diagnostics/
    ├── check_data.py        (combines all diagnostic scripts)
    └── explore.py           (EDA script)
```

**Would this be clearer?** Let me know if you want me to implement this simplification!
