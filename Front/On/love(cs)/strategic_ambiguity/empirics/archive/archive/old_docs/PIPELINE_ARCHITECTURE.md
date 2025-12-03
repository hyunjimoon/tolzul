# Pipeline Architecture - Complete System Overview

## 🏗️ System Architecture

```
empirics_ent_strat_ops/
│
├── 📂 src/ (Unified Analysis Package)
│   ├── __init__.py      # Package initialization
│   ├── features.py      # Data loading & feature engineering
│   ├── models.py        # Statistical models (H1, H2)
│   ├── vagueness_v2.py  # Vagueness scorer V2
│   ├── plotting.py      # F-series visualization
│   ├── empirical.py     # τ trajectory & xarray utilities
│   ├── multiverse.py    # Specification curve analysis
│   ├── cli.py           # Pipeline CLI (all 5 steps)
│   └── README.md        # Module documentation
│
├── 📂 data/
│   ├── raw/             # PitchBook .dat files (gitignored)
│   └── processed/       # Parquet cache (auto-generated)
│
├── 📂 outputs/          # All results
│   ├── all/             # Full dataset results
│   │   ├── models/      # H1/H2 coefficients
│   │   └── figures/     # F3a plot
│   ├── quantum/         # Quantum subset
│   └── transportation/  # Transportation subset
│
├── 📂 config/
│   └── datasets.yaml    # Dataset configurations
│
├── 📂 modules/ (ARCHIVED - don't use!)
│   └── ...              # Old duplicate code
│
├── run_all.sh           # Master pipeline script
└── requirements.txt     # Python dependencies
```

## 🔄 Data Flow

```
┌─────────────────────────────────────────────────────────────┐
│  INPUT: PitchBook .dat files                                │
│  ├─ Company20210101.dat, Company20220101.dat, ...          │
│  └─ Deal20230501.dat (if available)                        │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 1: Load Data (python -m src.cli load-data)          │
│  ├─ src.features.consolidate_company_snapshots()           │
│  ├─ Merge all snapshots                                    │
│  ├─ Keep latest info per company                           │
│  └─ Cache to parquet (10-50x speedup)                      │
│                                                             │
│  OUTPUT: data/processed/consolidated_companies.parquet     │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 2: Engineer Features (python -m src.cli engineer-fe) │
│  ├─ src.vagueness_v2.StrategicVaguenessScorerV2           │
│  │   └─ Compute V_raw from Description + Keywords          │
│  ├─ src.features.engineer_features()                       │
│  │   ├─ z_vagueness (standardized)                         │
│  │   ├─ is_software (HW/SW classification)                 │
│  │   ├─ z_employees_log                                    │
│  │   ├─ sector_fe (sector dummies)                         │
│  │   └─ founding_cohort                                    │
│  └─ Create survival/progression variables                  │
│                                                             │
│  OUTPUT: data/processed/features_all.parquet               │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 3: Filter Datasets (python -m src.cli filter-datasets) │
│  ├─ src.features.filter_quantum_companies()                │
│  ├─ src.features.filter_transportation_companies()         │
│  └─ Create 3 variants:                                     │
│      ├─ outputs/all/dataset.parquet                        │
│      ├─ outputs/quantum/dataset.parquet                    │
│      └─ outputs/transportation/dataset.parquet             │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 4: Run Models (python -m src.cli run-models)        │
│  ├─ src.models.test_h1_early_funding()                     │
│  │   └─ E ~ V + controls (OLS)                             │
│  ├─ src.models.test_h2_main_growth()                       │
│  │   └─ L ~ V × F + controls (Logit)                       │
│  └─ For each dataset (all, quantum, transportation)        │
│                                                             │
│  OUTPUT (per dataset):                                     │
│  ├─ models/h1_coefficients.csv                             │
│  ├─ models/h2_main_coefficients.csv                        │
│  └─ models/h2_analysis_dataset.csv                         │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  STEP 5: Generate Plots (python -m src.cli generate-plots) │
│  ├─ src.plotting.fig_F3a_L_given_F()                       │
│  │   └─ Vagueness × Hardware interaction                   │
│  └─ W2 color palette (Software=skyblue, HW=gray)           │
│                                                             │
│  OUTPUT (per dataset):                                     │
│  ├─ figures/F3a_interaction.png (300 DPI)                  │
│  └─ figures/F3a_interaction.pdf (vector)                   │
└─────────────────────────────────────────────────────────────┘
                          ↓
                    ✅ COMPLETE
```

## 📋 Pipeline Steps Detail

### Step 1: Load Data
**CLI Command**: `python -m src.cli load-data` (src/cli.py)
**Module**: `src/features.py`
**Function**: `consolidate_company_snapshots()`

**What it does**:
1. Finds all `Company*.dat` files in `data/raw/`
2. Loads each snapshot with its date
3. Merges all snapshots chronologically
4. Keeps most recent info per company
5. Saves to parquet for 10-50x speedup

**Cache behavior**:
- First run: Parses .dat files (slow)
- Subsequent runs: Loads parquet (fast)
- Auto-detects cache existence

### Step 2: Engineer Features
**CLI Command**: `python -m src.cli engineer-features` (src/cli.py)
**Modules**: `src/features.py`, `src/vagueness_v2.py`
**Functions**: `engineer_features()`, `StrategicVaguenessScorerV2`

**What it does**:
1. Loads consolidated data
2. Computes vagueness scores (V2 algorithm)
3. Classifies HW vs SW from keywords
4. Creates control variables (employees, cohort, sector)
5. Standardizes all variables (z-scores)

**Key features created**:
- `z_vagueness`: Standardized vagueness score
- `is_software`: 1=Software/Flexible, 0=Hardware/Rigid
- `z_employees_log`: Log employees (standardized)
- `sector_fe`: Sector fixed effects
- `founding_cohort`: Cohort indicators

### Step 3: Filter Datasets
**CLI Command**: `python -m src.cli filter-datasets` (src/cli.py)
**Module**: `src/features.py`
**Functions**: `filter_quantum_companies()`, `filter_transportation_companies()`

**What it does**:
1. Loads feature-engineered data
2. Applies keyword filters for each dataset
3. Saves 3 variants

**Filters**:
- **Quantum**: "quantum", "qubit", "quantum computing", etc.
- **Transportation**: "autonomous", "mobility", "EV", etc.
- **All**: No filter (full dataset)

### Step 4: Run Models
**CLI Command**: `python -m src.cli run-models --dataset all` (src/cli.py)
**Module**: `src/models.py`
**Functions**: `test_h1_early_funding()`, `test_h2_main_growth()`

**What it does**:
1. Loads filtered dataset
2. Runs H1 (OLS): Early Funding ~ Vagueness
3. Runs H2 (Logit): Growth ~ Vagueness × Hardware
4. Saves coefficients and analysis dataset

**Models**:
- **H1**: `E ~ V + employees + cohort + sector`
- **H2**: `L ~ V × F + employees + cohort + sector`

**Robustness**: Multi-stage Logit fallback
1. Standard MLE (maxiter=100)
2. L1 regularization (α=0.1)
3. Stronger L1 (α=0.5)

### Step 5: Generate Plots
**CLI Command**: `python -m src.cli generate-plots --dataset all` (src/cli.py)
**Module**: `src/plotting.py`
**Function**: `fig_F3a_L_given_F()`

**What it does**:
1. Loads H2 analysis dataset
2. Generates interaction plot
3. Saves both PNG (300 DPI) and PDF (vector)

**F3a Plot** (THE MONEY PLOT):
- X-axis: Vagueness (green)
- Y-axis: P(Series B+) (blue)
- Lines:
  - Software (skyblue, solid): Positive/flat slope
  - Hardware (gray, dashed): Positive slope (diverging scissors)

## 🔧 Module Responsibilities

### src/features.py
**"Data Chef" - Prepares all ingredients**
- Load raw .dat files
- Merge snapshots
- Basic feature engineering
- HW/SW classification
- Dataset filtering

### src/vagueness_v2.py
**"Vagueness Calculator" - Specialized scorer**
- Strategic Vagueness Score computation
- Two-component algorithm:
  - S_cat: Categorical vagueness
  - S_concdef: Concreteness deficit
- Formula: `V = 0.5×max() + 0.5×mean()`

### src/models.py
**"Statistical Engine" - Runs all tests**
- H1: OLS regression
- H2: Logit regression
- Formula management
- Robust convergence

### src/plotting.py
**"Artist" - Creates all figures**
- F-series plots (F1-F6)
- W2 color palette
- Interaction visualization
- Publication-ready output

### src/empirical.py
**"Strategist" - Advanced analysis**
- τ trajectory calculation
- xarray cohort tensor
- Productive/Destructive Ambiguity indices
- State-based cohort utilities

### src/multiverse.py
**"Defender" - Robustness checks**
- Specification grid generation
- Multiverse execution
- Spec curve visualization
- Sensitivity analysis

## 🎯 Design Principles

### 1. **Separation of Concerns**
- `src/cli.py`: Pipeline orchestration CLI
- `src/`: All logic and formulas
- No analysis code in pipeline scripts

### 2. **DRY (Don't Repeat Yourself)**
- One function, one place
- No duplicate implementations
- Reusable across pipeline steps

### 3. **Modularity**
- Each step is standalone
- Can run individually
- Can skip steps (e.g., `--quick` mode)

### 4. **Caching Strategy**
- Step 1: Parquet cache (10-50x speedup)
- Step 2-5: Use cached features
- `--quick` mode skips Step 1

### 5. **Three Dataset Variants**
- All companies (baseline)
- Quantum (high-tech, high uncertainty)
- Transportation (regulatory constraints)
- Compare effect sizes across datasets

## 🚀 Usage Patterns

### Run Everything
```bash
./run_all.sh
```

### Quick Mode (Skip Step 1)
```bash
./run_all.sh --quick
```

### Single Dataset
```bash
./run_all.sh --dataset quantum
```

### Individual Steps
```bash
python -m src.cli load-data
python -m src.cli engineer-features
python -m src.cli filter-datasets
python -m src.cli run-models --dataset quantum
python -m src.cli generate-plots --dataset quantum
```

### Test Specific Module
```python
from features import consolidate_company_snapshots
from vagueness_v2 import StrategicVaguenessScorerV2
from models import test_h2_main_growth

# Use directly
df = consolidate_company_snapshots('data/raw')
scorer = StrategicVaguenessScorerV2()
result = test_h2_main_growth(df)
```

## 📊 Expected Outputs

### File Structure After Full Run
```
outputs/
├── all/
│   ├── dataset.parquet                  # Filtered data
│   ├── models/
│   │   ├── h1_coefficients.csv         # H1 results
│   │   ├── h2_main_coefficients.csv    # H2 results
│   │   └── h2_analysis_dataset.csv     # Data for plotting
│   └── figures/
│       ├── F3a_interaction.png         # THE MONEY PLOT
│       └── F3a_interaction.pdf
├── quantum/
│   └── [same structure]
└── transportation/
    └── [same structure]
```

### Output Files Per Dataset
- **1 dataset file**: Filtered companies
- **3 model files**: H1, H2 coefficients + analysis data
- **2 figure files**: PNG + PDF

**Total**: 6 files × 3 datasets = 18 files

## 🔍 Quality Checks

### After Each Step
1. **Step 1**: Check parquet file size > 100 MB
2. **Step 2**: Check `z_vagueness` column exists
3. **Step 3**: Check quantum dataset ~1,144 rows
4. **Step 4**: Check coefficient CSV files created
5. **Step 5**: Check F3a plot shows interaction

### Final Validation
```bash
python validate_pipeline.py
```

Checks:
- All output files exist
- Files have expected sizes
- Models converged
- Plots display correctly

## 📚 Related Documentation

- **src/ Modules**: `src/README.md`
- **Pipeline CLI**: `src/cli.py` - run `python -m src.cli --help`
- **Testing**: `PIPELINE_TEST_GUIDE.md`
- **Vagueness Scorer**: `docs_archive/VAGUENESS_SCORER_V2_GUIDE.md`
- **xarray Design**: `XARRAY_DESIGN_README.md`
- **State-based Cohorts**: `STATE_BASED_COHORTS_README.md`

## 🛠️ Extension Points

### Adding Step 06: τ Trajectory
```python
# python -m src.cli trajectory (future implementation)
from empirical import calculate_tau_trajectory, prepare_cohort_tensor
from models import run_trajectory_model  # TODO: Add to src/models.py
from plotting import plot_tau_evolution  # TODO: Add to src/plotting.py
```

### Adding Step 07: Multiverse
```python
# python -m src.cli multiverse (future implementation)
from multiverse import build_spec_grid, run_spec_curve, plot_spec_curve
```

### Adding New Dataset Filter
```python
# In src/features.py
def filter_biotech_companies(df):
    keywords = ['biotech', 'pharmaceutical', 'therapeutics']
    return df[df['Keywords'].str.contains('|'.join(keywords), case=False, na=False)]

# In config/datasets.yaml
datasets:
  biotech:
    name: "Biotech & Healthcare"
    filter_function: "filter_biotech_companies"
    output_dir: "outputs/biotech"
```

---

**This architecture provides a clean, modular, production-ready pipeline for your thesis analysis.** 🚀
