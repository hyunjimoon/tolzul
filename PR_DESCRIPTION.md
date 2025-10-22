# Add Pitchbook Data Analysis Pipelines with Git Metadata Tracking

## Summary

This PR adds two production-ready data analysis pipelines for processing Pitchbook data, optimized for the Management Science paper on vagueness in entrepreneurial promises. Both pipelines include automatic git metadata tracking for full reproducibility.

## What's New

### 📊 Pipeline Options

#### Option 1: xarray-only Pipeline (Recommended)
**File**: `code/pipeline_xarray.py`

- **Single unified view**: All 40+ variables visible in one xarray Dataset
- **Easy exploration**: Access data with `ds.company_vagueness`, `ds.panel_funding_success`
- **Checkpoint/resume**: Resume from any step if errors occur
- **Git metadata**: Automatic tracking of commit ID, branch, and URLs
- **File**: `output/pitchbook_analysis.nc` (120KB)

```python
import xarray as xr
ds = xr.open_dataset('output/pitchbook_analysis.nc')
print(ds.data_vars)  # See all 40+ variables
print(ds.attrs['git_commit_url'])  # Check which code generated this
```

#### Option 2: Hybrid Pipeline (For Large Datasets)
**File**: `code/pipeline_hybrid.py`

- **Optimized for 94+ columns**: Real Pitchbook format with 94 Company + 97 Deal columns
- **60% size reduction**: Columnar parquet compression vs CSV
- **Selective loading**: Read only needed columns
- **Lightweight checkpoint**: 4KB metadata file + compressed parquet data

### 📚 Documentation

**File**: `code/PIPELINE_GUIDE.md`

- Korean/English bilingual guide
- Detailed comparison of both approaches
- Usage examples and best practices
- Reproducibility instructions

## Key Features

### 🔄 Reproducibility

Both pipelines automatically record:

```python
attrs = {
    'git_commit_id': 'a84c975...',
    'git_commit_url': 'https://github.com/hyunjimoon/tolzul/commit/...',
    'git_branch': 'claude/pitchbook-pipeline-updates-011CUNKR6EKWqqHsAjq1cTAG',
    'git_branch_url': 'https://github.com/hyunjimoon/tolzul/tree/...',
    'step_01-05_status': 'completed',
    'step_01-05_timestamp': '2025-10-22T...'
}
```

You can always trace which code version generated your results!

### 🎯 5-Step Processing Pipeline

Both pipelines implement the same 5-step workflow:

1. **Step 1**: Process Company data (filter AI/ML firms, calculate vagueness scores)
2. **Step 2**: Process Deal data (identify Series A/B, create funding success variable)
3. **Step 3**: Create analysis panel (merge company + deal, each firm × 2 rounds)
4. **Step 4**: Run regression analysis (two-way and three-way interactions)
5. **Step 5**: Create deliverables (4 tables + 4 figures)

### 📈 Output Files

Both pipelines generate:

**Tables**:
- `table1_descriptives.csv` - Descriptive statistics
- `table2_model1.csv` - Vagueness × Series B interaction
- `table4_model2.csv` - Three-way interaction (vagueness × round × integration cost)
- `table3_success_rates.csv` - Success rates by sector/round

**Figures**:
- `figure1_reversal_bars.png` - Funding success reversal pattern
- `figure2_vagueness_curves.png` - Success curves by vagueness level

**Models**:
- `model_results.pkl` - Full regression results with coefficients and p-values

## Usage

### Quick Start (xarray-only)

```bash
cd "Front/On/strategic ambiguity/empirics"

# Run full pipeline
python code/pipeline_xarray.py

# View status
python code/pipeline_xarray.py --summary

# Resume from specific step (if needed)
python code/pipeline_xarray.py --from 3
```

### Quick Start (hybrid)

```bash
cd "Front/On/strategic ambiguity/empirics"

# Run full pipeline
python code/pipeline_hybrid.py

# View status
python code/pipeline_hybrid.py --summary
```

### Data Requirements

Place your Pitchbook data files in `data/raw/`:
- `Company2021.dat`, `Company2022.dat`, ..., `Company2025.dat`
- `Deal2023.dat` (or your deal data files)

**Format**: Pipe-delimited (.dat) files with headers

**Expected columns**:
- Company: CompanyID, CompanyName, Description, Keywords, TotalRaised, Employees, YearFounded
- Deal: CompanyID, DealType, VCRound, DealDate, DealSize, Investors, PostValuation, DealStatus

## Test Results

✅ Successfully tested with sample data:
- **30 AI/ML companies** processed
- **61 VC deals** (Series A/B)
- **53 observations** in final panel
- **40+ variables** stored in xarray Dataset
- All 5 pipeline steps completed successfully

## Technical Details

### Why Two Pipelines?

| Feature | xarray-only | hybrid |
|---------|------------|--------|
| **Best for** | Exploring data, seeing everything at once | Very wide data (100+ columns) |
| **Storage** | Single 120KB file | Multiple compressed files |
| **Data access** | All variables visible | Load columns on demand |
| **Complexity** | Simple, unified interface | More efficient for large datasets |
| **Recommended when** | < 100MB datasets, interactive analysis | > 100 columns, production use |

### Data Structure

**xarray-only**:
```
pitchbook_analysis.nc (120KB)
├─ company_* (30 companies × 9 variables)
├─ deal_* (61 deals × 10 variables)
└─ panel_* (53 observations × 20+ variables)
```

**Hybrid**:
```
checkpoint.nc (4KB)              # Metadata only
data/processed/
  ├─ company_master.parquet (11KB)  # 60% smaller than CSV
  ├─ deal_panel.parquet (9KB)
  └─ analysis_panel.parquet (18KB)
```

## Migration Guide

If you were using the original scripts (`01_process_company_data.py` - `05_create_deliverables.py`):

**Old approach**:
```bash
python code/01_process_company_data.py
python code/02_process_deal_data.py
python code/03_create_panel.py
python code/04_run_analysis.py
python code/05_create_deliverables.py
```

**New approach**:
```bash
# One command runs all 5 steps with checkpointing
python code/pipeline_xarray.py
```

**Benefits**:
- ✅ Automatic checkpoint/resume
- ✅ Git metadata tracking
- ✅ All data visible in one place
- ✅ Easier to debug and explore

## Reproducibility Example

You can verify which code version generated any results:

```python
import xarray as xr

# Load results
ds = xr.open_dataset('output/pitchbook_analysis.nc')

# Check metadata
print(f"Generated by: {ds.attrs['git_commit_url']}")
print(f"Branch: {ds.attrs['git_branch']}")
print(f"Completed: {ds.attrs['step_05_timestamp']}")
print(f"N observations: {ds.attrs['n_observations']}")
```

## Files Changed

**Added**:
- `code/pipeline_xarray.py` (26KB) - xarray-only pipeline
- `code/pipeline_hybrid.py` (22KB) - hybrid pipeline
- `code/PIPELINE_GUIDE.md` (5KB) - Documentation
- `output/pitchbook_analysis.nc` (120KB) - Test results
- `output/checkpoint.nc` (4KB) - Hybrid checkpoint
- `data/processed/*.parquet` (3 files) - Compressed data

**Modified**:
- `output/table1_descriptives.csv` - Updated with test data
- `output/table2_model1.csv` - Two-way interaction results
- `output/table4_model2.csv` - Three-way interaction results
- `output/figure2_vagueness_curves.png` - Updated visualization

## Testing

Both pipelines have been tested with:
- ✅ Sample Pitchbook data (8 real AI companies + 22 synthetic)
- ✅ Full 5-step processing
- ✅ Regression analysis (logit/OLS fallback)
- ✅ Deliverable generation (tables + figures)
- ✅ Checkpoint save/load
- ✅ Git metadata recording

## Next Steps

After merging this PR:

1. **Pull the code** to your local machine
2. **Copy real Pitchbook data** to `data/raw/`
3. **Run pipeline**: `python code/pipeline_xarray.py`
4. **Review results** in `output/` directory
5. **Check reproducibility**: Verify git metadata in checkpoint file

## Questions?

Refer to `code/PIPELINE_GUIDE.md` for detailed documentation, or check the inline comments in the pipeline scripts.

---

**Related Issues**: Addresses the need for reproducible Pitchbook data analysis with checkpoint/resume capability

**Breaking Changes**: None - original scripts (`01-05_*.py`) remain unchanged

**Dependencies**: Requires `pandas`, `numpy`, `xarray`, `netcdf4`, `pyarrow`, `statsmodels`, `matplotlib`, `seaborn`
