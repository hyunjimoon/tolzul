# Pitchbook Data Analysis Pipeline Guide

두 가지 pipeline 옵션이 제공됩니다 (Two pipeline options available):

## Option 1: xarray-only Pipeline (선호 / Preferred)
**File**: `pipeline_xarray.py`

### 특징 (Features):
- ✅ **모든 데이터를 한번에 볼 수 있음** (See all data at once)
- 📊 40+ variables visible in single xarray Dataset
- 🔍 Easy inspection: `ds.company_vagueness`, `ds.panel_funding_success`
- 📦 Single file: `output/pitchbook_analysis.nc` (120KB)
- 🔄 Git metadata included for reproducibility

### 사용법 (Usage):
```bash
# Run full pipeline
python code/pipeline_xarray.py

# Resume from specific step
python code/pipeline_xarray.py --from 3

# Force rerun all steps
python code/pipeline_xarray.py --force

# View status
python code/pipeline_xarray.py --summary
```

### 장점 (Advantages):
1. **Single unified view** - All data in one Dataset
2. **Easy exploration** - `ds.data_vars` shows all variables
3. **Reproducibility** - Git commit/branch URLs in attrs
4. **Checkpoint/resume** - Resume from any step

### Data Structure:
```
pitchbook_analysis.nc (120KB)
├─ company_* (30 companies × 9 variables)
├─ deal_* (61 deals × 10 variables)
└─ panel_* (53 observations × 20+ variables)

attrs:
  - git_commit_url: https://github.com/hyunjimoon/tolzul/commit/...
  - step_01-05_status: completed
  - n_companies: 30, n_deals: 61, n_observations: 53
```

---

## Option 2: Hybrid Pipeline (xarray + parquet)
**File**: `pipeline_hybrid.py`

### 특징 (Features):
- ⚡ **94+ columns 최적화** (Optimized for 94+ columns)
- 💾 Columnar compression (60% size reduction)
- 🎯 Load specific columns only
- 🪶 Lightweight checkpoint (4KB metadata only)

### 사용법 (Usage):
```bash
# Run full pipeline
python code/pipeline_hybrid.py

# Resume from specific step
python code/pipeline_hybrid.py --from 2

# View status
python code/pipeline_hybrid.py --summary
```

### 장점 (Advantages):
1. **Efficient storage** - Parquet compression for wide data
2. **Selective loading** - Read only needed columns
3. **Better for 94+ columns** - Optimized for real Pitchbook format
4. **Faster I/O** - Columnar format

### Data Structure:
```
checkpoint.nc (4KB) - metadata only
data/processed/
  ├─ company_master.parquet (11KB, 30 rows × 94 columns)
  ├─ deal_panel.parquet (9KB, 61 rows × 97 columns)
  └─ analysis_panel.parquet (18KB, 53 rows × merged)
```

---

## 어떤 것을 사용해야 하나요? (Which one to use?)

### Use **xarray-only** (`pipeline_xarray.py`) if:
- ✅ 전체 데이터를 한눈에 보고 싶을 때 (Want to see all data at once)
- ✅ Interactive exploration and analysis
- ✅ Small to medium datasets (< 100MB)
- ✅ You prefer unified xarray interface

### Use **hybrid** (`pipeline_hybrid.py`) if:
- ✅ Very wide data (100+ columns)
- ✅ Need to load specific columns only
- ✅ Storage efficiency is critical
- ✅ Working with large Pitchbook datasets (1000+ companies)

---

## Git Metadata (Reproducibility)

Both pipelines automatically record:
```python
attrs = {
    'git_commit_id': 'caf6e2f...',
    'git_commit_url': 'https://github.com/hyunjimoon/tolzul/commit/...',
    'git_branch': 'claude/pitchbook-data-analysis-011CUNKR6EKWqqHsAjq1cTAG',
    'git_branch_url': 'https://github.com/hyunjimoon/tolzul/tree/...',
    'github_pr_url': '',  # Fill this when PR is created
}
```

**To check which code generated your results:**
```python
import xarray as xr

# xarray-only
ds = xr.open_dataset('output/pitchbook_analysis.nc')
print(ds.attrs['git_commit_url'])

# hybrid
checkpoint = xr.open_dataset('output/checkpoint.nc')
print(checkpoint.attrs['git_commit_url'])
```

---

## Output Files

Both pipelines generate:

### Tables:
- `table1_descriptives.csv` - Descriptive statistics
- `table2_model1.csv` - Two-way interaction results
- `table4_model2.csv` - Three-way interaction results
- `table3_success_rates.csv` - Success rates by sector

### Figures:
- `figure1_reversal_bars.png` - Funding success reversal pattern
- `figure2_vagueness_curves.png` - Success curves by vagueness level

### Models:
- `model_results.pkl` - Full regression results

---

## 다음 단계 (Next Steps)

1. **Pull this code to your local machine:**
   ```bash
   git pull origin claude/pitchbook-data-analysis-011CUNKR6EKWqqHsAjq1cTAG
   ```

2. **Copy your real Pitchbook data:**
   ```bash
   # Copy Company2021.dat, Company2022.dat, etc. to:
   Front/On/strategic ambiguity/empirics/data/raw/
   ```

3. **Run the pipeline:**
   ```bash
   cd "Front/On/strategic ambiguity/empirics"
   python code/pipeline_xarray.py  # or pipeline_hybrid.py
   ```

4. **View results:**
   ```bash
   ls -lh output/  # See generated files
   python code/pipeline_xarray.py --summary  # Check status
   ```

---

## Support

If you encounter issues:
1. Check `pipeline_xarray.py --summary` for step completion status
2. Resume from failed step: `--from N`
3. Check error messages for missing columns/files
4. Verify data format matches expected pipe-delimited (.dat) format

## 참고 (Reference)

- Original scripts: `01_process_company_data.py` - `05_create_deliverables.py`
- VaccineMisinf inspiration: https://github.com/hyunjimoon/VaccineMisinf/blob/main/V81/tf_fx_pcsth.py
