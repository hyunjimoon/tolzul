# Pipeline Testing Guide

## 🚀 Quick Test (Local Environment)

### Prerequisites
```bash
# Ensure you have dependencies
pip install -r requirements.txt
```

### Test Individual Steps

#### Step 1: Load Data
```bash
python -m src.cli load-data
```

**Expected output**:
```
================================================================================
STEP 1: LOAD DATA
================================================================================

📂 Loading company data from data/raw
✓ Data loaded successfully
   Total companies: 541,234
   Columns: 95
   Memory: 456.7 MB

💾 Saving parquet cache to data/processed/consolidated_companies.parquet
   Cache saved (125.3 MB)

================================================================================
STEP 1 COMPLETE ✓
================================================================================
```

**Success criteria**:
- ✅ Parquet cache created in `data/processed/`
- ✅ No import errors from `src/features`
- ✅ Company count > 0

#### Step 2: Engineer Features
```bash
python -m src.cli engineer-features
```

**Expected output**:
```
================================================================================
STEP 2: ENGINEER FEATURES
================================================================================

📂 Loading data...
✓ Loaded 541,234 companies

🔧 Computing vagueness scores...
✓ Vagueness scores computed

🏗️  Engineering features...
✓ Features engineered:
   - z_vagueness
   - is_software
   - z_employees_log
   - sector_fe
   - founding_cohort

💾 Saving to data/processed/features_engineered.parquet
✓ Saved (145.8 MB)

================================================================================
STEP 2 COMPLETE ✓
================================================================================
```

**Success criteria**:
- ✅ `features_engineered.parquet` created
- ✅ Vagueness scores computed
- ✅ HW/SW classification done

#### Step 3: Filter Datasets
```bash
python -m src.cli filter-datasets
```

**Expected output**:
```
================================================================================
STEP 3: FILTER DATASETS
================================================================================

📊 Creating dataset variants...

✓ All companies dataset:
   Companies: 541,234
   Output: outputs/all/dataset.parquet

✓ Quantum companies dataset:
   Companies: 1,144
   Output: outputs/quantum/dataset.parquet

✓ Transportation companies dataset:
   Companies: 8,567
   Output: outputs/transportation/dataset.parquet

================================================================================
STEP 3 COMPLETE ✓
================================================================================
```

**Success criteria**:
- ✅ 3 datasets created (all, quantum, transportation)
- ✅ Quantum dataset ~1,144 companies
- ✅ Files in `outputs/*/dataset.parquet`

#### Step 4: Run Models
```bash
python -m src.cli run-models --dataset all
# Or specific dataset:
python -m src.cli run-models --dataset quantum
python -m src.cli run-models --dataset transportation
```

**Expected output**:
```
================================================================================
Running Models: All Companies
================================================================================

📂 Loading outputs/all/dataset.parquet
   Companies: 541,234

🔬 Running H1: Early Funding ~ Vagueness
✓ H1 model fitted
   Vagueness coef: -0.000000556
   p-value: 0.208
   n_obs: 487,123

💾 Saved: outputs/all/models/h1_coefficients.csv

🔬 Running H2: Growth ~ Vagueness × Hardware
✓ H2 model fitted
   Interaction coef: 0.0886
   p-value: 0.061
   n_obs: 156,789

💾 Saved: outputs/all/models/h2_main_coefficients.csv
💾 Saved: outputs/all/models/h2_analysis_dataset.csv

================================================================================
STEP 4 COMPLETE ✓
================================================================================
```

**Success criteria**:
- ✅ H1 and H2 models run successfully
- ✅ Coefficient CSV files created
- ✅ Analysis dataset saved for plotting

#### Step 5: Generate Plots
```bash
python -m src.cli generate-plots --dataset all
# Or specific dataset:
python -m src.cli generate-plots --dataset quantum
```

**Expected output**:
```
================================================================================
Generating Plots: All Companies
================================================================================

📂 Loading outputs/all/models/h2_analysis_dataset.csv
   Companies: 156,789

🎨 Generating F3a plot (Vagueness × Hardware interaction)...
✓ Saved: outputs/all/figures/F3a_interaction.png
✓ Saved: outputs/all/figures/F3a_interaction.pdf

================================================================================
STEP 5 COMPLETE ✓
================================================================================
```

**Success criteria**:
- ✅ F3a plot created (THE MONEY PLOT!)
- ✅ Both PNG and PDF versions saved
- ✅ Interaction visible in plot

### Run All Steps
```bash
./run_all.sh
# Or with options:
./run_all.sh --quick  # Skip step 1 (use cached data)
./run_all.sh --dataset quantum  # Only quantum dataset
```

## 🧪 Testing src/ Module Imports

### Test in Python
```python
import sys
from pathlib import Path

# Add src to path (same as pipeline does)
sys.path.insert(0, str(Path.cwd() / 'src'))

# Test imports
from features import consolidate_company_snapshots, engineer_features
from models import test_h1_early_funding, test_h2_main_growth
from vagueness_v2 import StrategicVaguenessScorerV2
from plotting import fig_F3a_L_given_F, PALETTE
from empirical import calculate_tau_trajectory, prepare_cohort_tensor
from multiverse import build_spec_grid, run_spec_curve

print("✅ All src/ modules imported successfully!")
```

### Test import chain
```python
# This mimics what pipeline/04_run_models.py does
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd() / 'src'))

from models import test_h2_main_growth
from features import preprocess_for_h2
import pandas as pd

# Load data
df = pd.read_parquet('outputs/all/dataset.parquet')

# Preprocess
df_h2 = preprocess_for_h2(df)

# Run model
result = test_h2_main_growth(df_h2)

print(result.summary())
```

## 🔍 Validation Checklist

### After Step 1 (Load Data)
- [ ] `data/processed/consolidated_companies.parquet` exists
- [ ] File size > 100 MB
- [ ] Can load with `pd.read_parquet()`

### After Step 2 (Engineer Features)
- [ ] `data/processed/features_engineered.parquet` exists
- [ ] Contains `z_vagueness` column
- [ ] Contains `is_software` column
- [ ] Contains `sector_fe` column

### After Step 3 (Filter Datasets)
- [ ] `outputs/all/dataset.parquet` exists
- [ ] `outputs/quantum/dataset.parquet` exists (~1,144 rows)
- [ ] `outputs/transportation/dataset.parquet` exists

### After Step 4 (Run Models)
- [ ] `outputs/all/models/h1_coefficients.csv` exists
- [ ] `outputs/all/models/h2_main_coefficients.csv` exists
- [ ] `outputs/all/models/h2_analysis_dataset.csv` exists
- [ ] CSV files have non-zero rows

### After Step 5 (Generate Plots)
- [ ] `outputs/all/figures/F3a_interaction.png` exists
- [ ] `outputs/all/figures/F3a_interaction.pdf` exists
- [ ] Can open image files
- [ ] Plot shows diverging lines (Software vs Hardware)

## 🐛 Troubleshooting

### ImportError: No module named 'features'
**Problem**: `src/` not in Python path

**Solution**:
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))
```

All pipeline files already have this. If error persists:
```bash
# Run from repository root
cd /path/to/empirics_ent_strat_ops
python pipeline/01_load_data.py
```

### ImportError: No module named 'pandas'
**Problem**: Dependencies not installed

**Solution**:
```bash
pip install -r requirements.txt
```

### FileNotFoundError: data/raw/*.dat
**Problem**: No raw data files

**Solution**:
1. Place PitchBook `.dat` files in `data/raw/`
2. Or use existing parquet cache if available

### Model convergence warnings
**Problem**: Logit model fails to converge

**Solution**: Pipeline already has multi-stage fallback:
1. Tries standard MLE
2. Falls back to L1 regularization (α=0.1)
3. Falls back to stronger L1 (α=0.5)

This is automatic - no action needed.

### Empty outputs
**Problem**: No companies in filtered dataset

**Solution**:
- Check filter keywords in `src/features.py`
- Quantum keywords: "quantum", "qubit", etc.
- Transportation keywords: "autonomous", "mobility", etc.

## 📊 Expected Performance

| Step | Time | Output Size |
|------|------|-------------|
| 01 - Load | 2-5 min | 125 MB |
| 02 - Features | 5-10 min | 145 MB |
| 03 - Filter | 1-2 min | 3 × small |
| 04 - Models | 2-3 min | CSV files |
| 05 - Plots | 30 sec | PNG/PDF |
| **Total** | **~15 min** | **~270 MB** |

(Times for full dataset ~500K companies)

## ✅ Success Indicators

### Pipeline ran successfully if:
1. All 5 steps complete without errors
2. F3a plot shows clear interaction pattern
3. H2 coefficient files show expected structure
4. Quantum dataset has ~1,144 companies

### Expected Results (from current data):
- **H1**: Vagueness → Early Funding (negative, p~0.2)
- **H2**: Vagueness × Hardware → Growth (positive, p~0.06)
- **F3a**: Diverging scissors (Hardware ↑, Software →)

## 🚀 Next Steps After Testing

If all tests pass:
1. ✅ Pipeline is production-ready
2. ✅ src/ modules working correctly
3. → Ready for Step 06 (τ Trajectory)
4. → Ready for Step 07 (Multiverse)

If tests fail:
1. Check error messages
2. Verify data files exist
3. Check dependencies installed
4. Review troubleshooting section above

---

**Ready to test?** Start with:
```bash
python pipeline/01_load_data.py
```
