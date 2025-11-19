# Documentation Archive Index

This directory contains archived documentation, scripts, and results from previous iterations of the thesis pipeline. These files are preserved for reference but are **not used in the current pipeline**.

**Current Pipeline Location**: See `../pipeline/` and `../PIPELINE_GUIDE.md`

---

## 📚 Documentation Files (Previous Iterations)

### Advisor & Presentation Materials
- **ADVISOR_1SLIDE_SUMMARY.md** - 1-slide summary for advisor meeting (Stern & Fine)
  - H1/H2 findings, theoretical contributions, F3a "money plot"
  - **Superseded by**: Current model outputs in `outputs/*/models/`

- **ADVISOR_REVIEW.md** - Full technical review for advisor presentation
  - H1/H2 interpretation, marginal effects, Q&A prep
  - **Superseded by**: Generated coefficient tables and plots

### Implementation & Design Guides
- **IMPLEMENTATION_GUIDE.md** - Set B → minimal thesis pipeline guide
  - Feature parity check, HW/SW sector simplification
  - HIGH priority extractions (vagueness, DV, logit, caching)
  - **Superseded by**: Current `src/` and `pipeline/` structure

- **STANDALONE_MIGRATION_PROMPT.md** - Guide for making thesis run.py files standalone
  - Comprehensive migration guide for separate Claude session
  - 7 function mappings, gap analysis
  - **Status**: Thesis files remain external (not integrated)

- **F_SERIES_PLOTS_GUIDE.md** - Visual narrative explanation of F1/F2/F3a plots
  - F1: Early funding ~ vagueness
  - F2: Average growth effect
  - F3a: THE MONEY PLOT (interaction with diverging lines)
  - **Superseded by**: `pipeline/05_generate_plots.py`

- **F_SERIES_README.md** - Earlier version of F-series plot documentation
  - **Superseded by**: F_SERIES_PLOTS_GUIDE.md

- **VAGUENESS_SCORER_V2_GUIDE.md** - V1 vs V2 vagueness scorer comparison
  - Feature table, migration guide, validation approach
  - **Still relevant**: See `experiments/test_vagueness_variants.py`

### Pipeline Documentation (Old Versions)
- **MAIN_PIPELINE_README.md** - Original main pipeline documentation
  - **Superseded by**: `PIPELINE_GUIDE.md` (root) and `pipeline/README.md`

- **PARQUET_QUANTUM_README.md** - Guide for parquet caching and quantum filtering
  - **Integrated into**: `pipeline/01_load_data.py` and `pipeline/03_filter_datasets.py`

- **README.md** - Old root README
  - **Superseded by**: `PIPELINE_GUIDE.md`

- **README_PIPELINE.md** - Another old pipeline README
  - **Superseded by**: `PIPELINE_GUIDE.md`

---

## 🗂️ Archived Directories

### `results/` - Old Analysis Results
**Created**: Pre-pipeline refactor
**Last modified**: Nov 15, 2025

Contains outputs from the old `run/` directory structure:
- `W1/` - Week 1 results
- `multiverse_results/` - Multiverse analysis outputs
- `test_run/` - Test run outputs
- Various PNG plots (heatmaps, spec curves, distributions)
- `hypothesis_results.txt`, `summary_stats.txt`, `spec_table.csv`

**Superseded by**: `outputs/all/`, `outputs/quantum/`, `outputs/transportation/`

### `run/` - Old Run Scripts
**Created**: Original pipeline structure
**Last modified**: Nov 15, 2025

Contains old execution scripts:
- `main.py` - Old main entry point
- `run_full_pipeline.sh` - Old bash runner
- `run_multiverse.py` - Multiverse analysis script
- `multiverse_engine.py` - Multiverse analysis engine
- `demo_F_series_HEV_HLVF_HSF.py` - F-series demo for H/E/V/L/F framework

**Superseded by**: `run_all.sh`, `pipeline/01-05_*.py`

### `scripts/` - Old Utility Scripts
**Created**: Various dates
**Last modified**: Nov 15-16, 2025

Contains standalone scripts and READMEs:

**Documentation:**
- `IMPLEMENTATION_STATUS.md` - Implementation tracking (outdated)
- `README_2021_COHORT.md` - 2021 cohort analysis guide
- `README_E_L_DEFINITION.md` - Early/Later variable definitions
- `README_HYPOTHESIS_TEST.md` - Hypothesis testing guide
- `README_VALIDATION.md` - Validation methods guide
- `VALIDATION_METHODS.md` - Detailed validation procedures

**Scripts:**
- `generate_F3a_plot.py` - F3a interaction plot generator (standalone)
  - **Superseded by**: `pipeline/05_generate_plots.py`
- `analyze_2021_cohort.py` - 2021 cohort analysis
- `consolidate_2021_cohort.py` - 2021 data consolidation
- `convert_dat_to_parquet.py` - DAT to Parquet converter
  - **Integrated into**: `pipeline/01_load_data.py`
- `diagnose_vagueness_quality.py` - Vagueness scorer diagnostics
  - **Superseded by**: `experiments/test_vagueness_variants.py`
- `plot_EVF_LVF.py` - E/V/F and L/V/F plotting
- `test_consolidated_data.py` - Data consolidation tests
- `test_hypothesis_VxF.py` - V×F hypothesis testing
- `validate_E_L_design.py` - E/L variable validation

### `test/` - Old Test Directory
**Created**: Original test framework
**Last modified**: Nov 15, 2025

Contains old test scripts and documentation:
- `README.md` - Test directory README
- `README copy.md` - Duplicate README
- `TEST_INSTRUCTIONS.md` - Testing instructions
- `analyze_progression_timeline.py` - Progression timeline analysis
- `check_founder_data.py` - Founder data validation

**Superseded by**: `validate_pipeline.py` (root)

---

## 📄 Archived Root Files

### Notebooks
- **E_L_hypothesis_pipeline.ipynb** - Jupyter notebook for E/L hypothesis testing
  - Interactive analysis of Early/Later framework
  - **Superseded by**: Modular `pipeline/` scripts

### Test Scripts
- **test_thesis_pipeline.py** - Old automated verification script
  - 5 test stages: data, features, vagueness, H1, H2
  - **Superseded by**: `validate_pipeline.py`

### Diagnostic Outputs
- **vagueness_diagnosis.txt** - Diagnostic output from vagueness quality check
  - Analysis of vagueness score distribution
  - **Note**: Identified the V1 vs V2 scorer issue now addressed in `experiments/`

- **pipeline.log** - Old pipeline execution log
  - Historical log from previous runs

---

## 🔄 Migration Path: Old → New

### Old Structure (Archived)
```
run/main.py                    → run_all.sh
run/run_full_pipeline.sh       → run_all.sh
scripts/generate_F3a_plot.py   → pipeline/05_generate_plots.py
scripts/convert_dat_to_parquet → pipeline/01_load_data.py
scripts/diagnose_vagueness     → experiments/test_vagueness_variants.py
test/                          → validate_pipeline.py
results/                       → outputs/{all,quantum,transportation}/
```

### Current Structure (Active)
```
pipeline/
  01_load_data.py              ← Data loading + parquet caching
  02_engineer_features.py      ← Feature engineering + V2 scorer
  03_filter_datasets.py        ← Dataset filtering (all/quantum/transport)
  04_run_models.py             ← H1/H2 model execution
  05_generate_plots.py         ← F3a plot generation

src/
  features.py                  ← Feature engineering functions
  vagueness_v2.py              ← V2 vagueness scorer
  models.py                    ← H1/H2/H3/H4 hypothesis tests

experiments/
  test_vagueness_variants.py   ← Test different scorers
  switch_to_v2_scorer.py       ← Auto-switch to V2

run_all.sh                     ← Master pipeline runner
validate_pipeline.py           ← Pipeline validation
PIPELINE_GUIDE.md              ← Complete usage guide
```

---

## 📊 Key Insights from Archived Work

### Vagueness Scorer Evolution
1. **V1** (archived) - 3-component scorer
   - Issue: 75% of companies at score = 50.0
   - Low variance → weak statistical power
   - See: `vagueness_diagnosis.txt`

2. **V2** (current) - 2-component scorer
   - Categorical vagueness + Concreteness deficit
   - IDF weighting, better variance
   - See: `src/vagueness_v2.py`, `experiments/`

### F-Series Plots
- **F1**: Early funding ~ vagueness (information asymmetry)
- **F2**: Average growth effect (skip if moderation exists)
- **F3a**: THE MONEY PLOT - Vagueness × Hardware interaction
  - Surprising reversal: Vagueness helps hardware, not software
  - See: `F_SERIES_PLOTS_GUIDE.md`

### Dataset Evolution
- Started with single dataset analysis
- Added quantum filtering (parquet caching)
- **Current**: 3-dataset pipeline (all, quantum, transportation)
- See: `PARQUET_QUANTUM_README.md`

---

## 🎯 Why These Files Were Archived

1. **Consolidation**: Multiple READMEs → Single `PIPELINE_GUIDE.md`
2. **Modularization**: Monolithic scripts → `pipeline/01-05_*.py`
3. **Standardization**: Ad-hoc utilities → Integrated pipeline
4. **Clarity**: Scattered docs → Organized structure
5. **Maintenance**: Duplicate code → Single source of truth

---

## ⚠️ Important Notes

- **Do not delete** - These files provide historical context and may contain useful analysis code
- **Do not use** - The current pipeline supersedes all archived implementations
- **Reference only** - Consult for understanding design decisions or theoretical background
- **Preserved commits** - All files remain in git history even if moved

---

## 📞 Questions?

If you need to understand:
- **Why a design decision was made** → Check implementation guides
- **How V1 vs V2 scorer differs** → See `VAGUENESS_SCORER_V2_GUIDE.md`
- **What F-series plots mean** → See `F_SERIES_PLOTS_GUIDE.md`
- **Old analysis results** → Check `results/` subdirectories
- **Current pipeline** → See `../PIPELINE_GUIDE.md` (root directory)

---

**Last Updated**: November 16, 2025
**Archive Reason**: Pipeline reorganization and consolidation
**Status**: Reference only - not used in active pipeline
