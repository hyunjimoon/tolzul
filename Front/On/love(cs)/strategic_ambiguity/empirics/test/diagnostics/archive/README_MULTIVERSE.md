# Multiverse Analysis Engine 🐢🐅

xarray-based multiverse engine testing vagueness → funding/success hypotheses across specification space.

## 🎯 Overview

This engine implements a comprehensive multiverse analysis framework for testing strategic ambiguity (vagueness) hypotheses in venture funding. It systematically tests hypotheses across a multidimensional specification grid, providing robust evidence for:

- **H1 (Early Stage)**: Vagueness → Early Funding (Expected: negative, clarity premium)
- **H2 (Later Stage)**: Vagueness → Growth (Expected: positive, flexibility value)
- **Moderation**: Effects amplified by option exercisability and software industry

## 📦 Installation

### Dependencies

```bash
pip install -r requirements.txt
```

Required packages:
- pandas >= 2.0
- numpy >= 1.24
- xarray >= 2023.1
- statsmodels >= 0.14
- patsy >= 0.5
- scipy >= 1.10
- matplotlib >= 3.7
- seaborn >= 0.12

## 🚀 Quick Start

### 1. Run Multiverse Analysis

```bash
python run_multiverse.py --input /path/to/your/data.csv --outdir results/
```

### 2. View Results

Results will be saved to `results/`:
- `multiverse_results.nc` - xarray Dataset (NetCDF format)
- `spec_table.csv` - Full specification table
- `summary_stats.txt` - Summary statistics
- `*.png` - Visualization heatmaps and curves

## 📊 Specification Grid

The multiverse spans **384 specifications**:

```python
{
    "stage": ["E", "L1", "L2"],           # 3 stages
    "window": [3 time windows],            # 3 windows
    "scaling": ["zscore", "winsor99_z"],  # 2 methods
    "moderator": ["option", "software"],  # 2 moderators
    "ctrl_employee": [0, 1],              # 2 toggles
    "ctrl_region": [0, 1],                # 2 toggles
    "ctrl_founder": [0, 1],               # 2 toggles
    "ctrl_earlyfund": [0, 1]              # 2 toggles
}
# 3 × 3 × 2 × 2 × 2 × 2 × 2 × 2 = 384 specifications
```

## 🏗️ Architecture

### Data Pipeline

1. **Window Filtering**: Filter by founding year using `patsy.dmatrix()` for TRUE nobs
2. **Moderator Creation**: `isSoftware = 1 - is_hardware`
3. **Scaling**: Z-score transformation of ALL continuous variables
   - `vagueness` → `z_vagueness` (aliased as `V`)
   - `employees_log` → `z_employees_log`
   - `early_funding_musd` → `z_early_funding_musd`

### Model Fitting

**Stage E (Early - OLS):**
```
z_early_funding_musd ~ V + controls
```

**Stages L1/L2 (Later - Logit):**
```
growth ~ V * moderator + z_early_funding_musd + controls
```

**3-Stage Fallback for Logit:**
1. MLE (maximum likelihood)
2. L1 regularization (α=0.1)
3. L1 regularization (α=0.5)

### Evidence Metrics

For each coefficient:

```python
evidence_score = sign(coef) * -log10(p)
is_consistent = (sign == expected) & (p < 0.05)
is_surprise = (sign != expected) & (p < 0.05)
```

## 📈 Expected Signs

| Effect | Stage E | Stage L1 | Stage L2 | Rationale |
|--------|---------|----------|----------|-----------|
| vag_main | **-1** | **+1** | **+1** | Clarity premium → Flexibility value |
| vagXoption | **+1** | **+1** | **+1** | Flexible architecture amplifies |
| vagXsoftware | **+1** | **+1** | **+1** | Software industry amplifies |

## 📂 File Structure

```
empirics_ent_strat_ops/
├── multiverse_engine.py        # Core analysis engine
├── run_multiverse.py            # CLI orchestrator
├── requirements.txt             # Package dependencies
└── README_MULTIVERSE.md         # This file

results/                         # Output directory
├── multiverse_results.nc        # xarray Dataset
├── spec_table.csv               # Full results table
├── summary_stats.txt            # Summary statistics
├── multiverse_h1_heatmap.png    # Early stage evidence
├── spec_curve_h1.png            # H1 specification curve
├── multiverse_h2_option_heatmap.png   # Option interaction
└── multiverse_h2_software_heatmap.png # Software interaction
```

## 🔬 Usage Examples

### Basic Analysis

```bash
python run_multiverse.py \
  --input data/startups.csv \
  --outdir results/
```

### Quiet Mode

```bash
python run_multiverse.py \
  --input data/startups.csv \
  --outdir results/ \
  --quiet
```

### Load Results in Python

```python
import xarray as xr
import pandas as pd

# Load xarray Dataset
ds = xr.open_dataset('results/multiverse_results.nc')

# Slice by specification
early_zscore = ds.sel(stage='E', scaling='zscore')
print(early_zscore['evidence_score_vag_main'].values)

# Load as DataFrame
df = pd.read_csv('results/spec_table.csv')
consistent = df[df['is_consistent_vag_main'] == 1]
print(f"Consistent specifications: {len(consistent)}/{len(df)}")
```

## 🎨 Visualization

The engine generates direction-aware heatmaps where:
- **Green** indicates effects in expected direction
- **Red** indicates effects opposite to expected
- **Color intensity** reflects evidence strength

## ✅ Validation Checklist

- [x] Window filtering uses `patsy.dmatrix()` for TRUE nobs
- [x] `STAGE_PATTERNS` defined as module constants
- [x] `isSoftware = 1 - is_hardware` created
- [x] ALL continuous vars z-scored (vagueness, employees_log, early_funding_musd)
- [x] Formula builder includes all ctrl_* toggles
- [x] 3-stage fallback: MLE → L1(0.1) → L1(0.5)
- [x] `estimation_method` recorded in results
- [x] Returns `nobs` from design matrix
- [x] H1 uses z_early_funding_musd as DV
- [x] H2 uses z_early_funding_musd when ctrl_earlyfund=1
- [x] Expected signs: E vag_main=-1, L1/L2 vag_main=+1
- [x] Evidence metrics computed correctly
- [x] xarray structure with all 18 data_vars
- [x] Outputs: .nc, .csv, .png files
- [x] Type hints on public functions
- [x] Numpy-style docstrings
- [x] Clean code (<500 lines)
- [x] Random seed for reproducibility

## 📋 Input Data Format

Required columns in CSV:

```
vagueness               # Core IV (0-100)
growth                  # Binary DV for L1/L2 (0/1)
early_funding_musd      # Continuous DV for E (USD millions)
year                    # Founding year (YYYY)
option_exercisability_level  # Moderator (1-5 scale)
is_hardware             # Industry (0=software, 1=hardware)
employees_log           # Log employees
founder_credibility     # Founder score (0-10)
region                  # Geographic region
founding_cohort         # Cohort identifier
down_round_flag         # Down round indicator (0/1)
```

## 🐛 Troubleshooting

### No convergence warnings
The 3-stage fallback automatically handles convergence issues by progressively adding regularization.

### Missing data
Missing values are handled by `patsy.dmatrix()` which drops incomplete observations.

### Memory issues
For very large datasets, consider reducing the specification grid or processing in batches.

## 📚 References

- Steegen et al. (2016). "Increasing Transparency Through a Multiverse Analysis"
- Simonsohn et al. (2020). "Specification curve analysis"
- xarray documentation: https://docs.xarray.dev/

## 🙏 Citation

If you use this engine in your research, please cite:

```bibtex
@software{multiverse_engine_2025,
  title = {Multiverse Analysis Engine for Strategic Ambiguity Research},
  year = {2025},
  note = {xarray-based specification curve analysis}
}
```

---

必死則生 🐢🐅

*"If you are desperate, you will live"*
