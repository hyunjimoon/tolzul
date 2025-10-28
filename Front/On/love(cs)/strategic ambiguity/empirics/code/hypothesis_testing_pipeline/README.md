# Hypothesis Testing Pipeline for Promise Vagueness Research

---

## ⚠️ DEPRECATION NOTICE

**This documentation is for the OLD pipeline (now archived).**

**Please use the NEW pipeline instead**: `../../run_h2_seriesb.py`

**Documentation**: See `../../README_START_HERE.md`

**What changed**:
- OLD: 2-snapshot approach (singular matrix error)
- NEW: 4-snapshot approach (12-15% progression rate) ✓

**Old files archived to**: `../../archive_deprecated/`

---

## 🎯 Research Objective (Historical Reference Only)

Test how **promise vagueness** affects (1) early funding amounts and (2) later success, conditional on sector integration cost.

## 📚 Hypotheses

| ID | Relationship | Expected Sign | Model Type |
|----|---------------|---------------|-------------|
| **H1** | Early Funding ~ Vagueness + Controls | Negative (α₁ < 0) | OLS |
| **H2** | Later Success ~ Vagueness × Integration Cost + Early Funding + Controls | Positive in modular (β₁ > 0); attenuated in integrated (β₃ < 0) | Logit |

### H1: Early Funding Effect
**Model:** `log(Early Funding) ~ Vagueness + Employees + Year Founded`

**Expected:** α₁ < 0 (vague promises lead to lower early funding)

**Interpretation:** Investors discount vague promises when deciding initial funding amounts.

### H2: Later Success Effect with Moderation
**Model:** `Later Success ~ Vagueness × Integration Cost + Early Funding + Employees + Year Founded`

**Expected:**
- β₁ > 0 (vagueness helps in modular sectors)
- β₃ < 0 (effect attenuated in integrated sectors)

**Interpretation:** Vagueness provides strategic flexibility that helps in modular sectors (software, APIs) but hurts in integrated sectors (hardware, robotics).

---

## 🚀 Quick Start

### Installation

```bash
# Install required packages
pip install -r requirements.txt
```

### Run with Demo Data

```bash
# Generate and run with simulated data
python run_pipeline.py --demo
```

### Run with Real Data

```bash
# Run with PitchBook CSV export
python run_pipeline.py --data path/to/pb_company_raw.csv --output results/
```

---

## 📁 Pipeline Structure

```
hypothesis_testing_pipeline/
├── run_pipeline.py           # Main orchestration script
├── src/
│   ├── feature_engineering.py   # Vagueness & integration cost computation
│   ├── hypothesis_tests.py      # H1 (OLS) & H2 (Logit) models
│   └── visualizations.py        # Diagnostic plots
├── data/                     # Input data directory
├── output/                   # Results and deliverables
│   ├── pb_processed_dataset.nc          # xarray dataset
│   ├── model_results.nc                 # Model coefficients (xarray)
│   ├── hypothesis_test_summary.csv      # Test results summary
│   ├── h1_coefficients.csv              # H1 detailed results
│   ├── h2_coefficients.csv              # H2 detailed results
│   ├── h1_scatter.png                   # H1 visualization
│   ├── h1_diagnostics.png               # H1 residual plots
│   ├── h2_interaction.png               # H2 interaction plot
│   └── coefficient_comparison.png       # Summary plot
└── README.md
```

---

## 🔧 Pipeline Steps

### Step 1: Load Data
Reads PitchBook CSV export with pipe-delimited format:
- Company information
- Descriptions and keywords
- Financing data
- Employee counts

### Step 2: Feature Engineering
Computes derived variables:

#### **Vagueness Score** (0-1 scale)
Uses LIWC-style keyword counting:
```python
hedge_words = ["maybe", "approximately", "likely", "potential", "scalable", "flexible"]
vagueness = count(hedge_words) / total_words
```

#### **Integration Cost Classification**
- **High Integration (1):** hardware, robotics, chips, biotech
- **Low Integration (0):** software, APIs, SaaS, cloud

#### **Funding Variables**
- `early_funding_musd`: First financing size in millions
- `later_success`: Binary indicator for reaching Series B+

#### **Controls**
- `employees_log`: Log-transformed employee count
- `year_founded`: Founding year
- `firm_age`: Current age of firm

### Step 3: Create xarray Dataset
Converts engineered features to xarray format with:
- Dimensions: company_id
- Coordinates: sector, year
- Data variables: all analysis features
- Attributes: metadata and provenance

### Step 4: Run Hypothesis Tests

#### H1: OLS Regression
```python
model1 = ols("early_funding_musd ~ vagueness + employees_log + year_founded")
```

**Test:** Is α₁ < 0?

#### H2: Logit Regression
```python
model2 = logit("later_success ~ vagueness * high_integration_cost + early_funding_musd + employees_log + year_founded")
```

**Tests:**
- Is β₁ > 0? (main effect in modular)
- Is β₃ < 0? (interaction term)

### Step 5: Create Visualizations
Generates diagnostic plots:

1. **H1 Scatter Plot:** Early funding vs vagueness with regression line
2. **H1 Diagnostics:** Residual plots (4-panel)
3. **H2 Interaction Plot:** Predicted probability curves by integration cost
4. **H2 Marginal Effects:** Success rates across vagueness bins
5. **Coefficient Comparison:** Forest plot of key estimates

### Step 6: Save Outputs
Exports results in multiple formats:
- **xarray NetCDF** (`.nc`): Efficient binary storage with metadata
- **CSV tables**: Human-readable coefficients and summaries
- **PNG plots**: High-resolution diagnostics (300 DPI)
- **JSON metadata**: Pipeline provenance and settings

---

## 📊 Output Files

### Primary Deliverables

| File | Description |
|------|-------------|
| `pb_processed_dataset.nc` | xarray Dataset with all engineered features |
| `model_results.nc` | xarray Dataset with model coefficients and statistics |
| `hypothesis_test_summary.csv` | Summary table comparing estimated vs expected signs |

### Detailed Results

| File | Description |
|------|-------------|
| `h1_coefficients.csv` | H1 OLS coefficients, standard errors, p-values, CIs |
| `h2_coefficients.csv` | H2 Logit coefficients, standard errors, p-values, CIs |
| `pipeline_metadata.json` | Pipeline version, timestamps, data source |

### Visualizations

| File | Description |
|------|-------------|
| `h1_scatter.png` | Early funding vs vagueness with fitted line |
| `h1_diagnostics.png` | 4-panel residual diagnostics |
| `h2_interaction.png` | Predicted probability curves by integration cost |
| `h2_marginal_effects.png` | Success rates by vagueness bins |
| `coefficient_comparison.png` | Forest plot of key hypothesis tests |

---

## 🔬 Expected Results

### H1: Early Funding
**Expected:** α₁ < 0 (vagueness hurts early funding)

**Interpretation:**
- More vague descriptions → Lower Series A amounts
- Investors demand clarity for initial commitments

### H2: Later Success
**Expected:** β₁ > 0, β₃ < 0 (vagueness helps in modular, hurts in integrated)

**Interpretation:**
- In modular sectors (software): Vagueness provides strategic flexibility → Higher Series B probability
- In integrated sectors (hardware): Vagueness signals uncertainty → Lower Series B probability
- **Interaction effect:** β₃ < 0 confirms moderation by integration cost

---

## 🛠️ Advanced Usage

### Custom Formulas

```python
from hypothesis_tests import run_full_hypothesis_tests

# Custom H1 formula with additional controls
results = run_full_hypothesis_tests(
    df,
    h1_formula="early_funding_musd ~ vagueness + employees_log + year_founded + total_raised",
    h2_formula="later_success ~ vagueness * high_integration_cost + early_funding_musd + firm_age"
)
```

### xarray Operations

```python
import xarray as xr

# Load processed dataset
ds = xr.open_dataset("output/pb_processed_dataset.nc")

# Filter by sector
software_firms = ds.where(ds['high_integration_cost'] == 0, drop=True)

# Group by year
annual_vagueness = ds.groupby('year').mean('company_id')

# Save subset
software_firms.to_netcdf("output/software_firms.nc")
```

### Programmatic Access

```python
from run_pipeline import HypothesisTestingPipeline

# Initialize
pipeline = HypothesisTestingPipeline(
    data_path="data/pb_company.csv",
    output_dir="my_results/"
)

# Run specific steps
pipeline.step_1_load_data()
pipeline.step_2_engineer_features()
pipeline.step_3_create_xarray_dataset()

# Access intermediate results
df_engineered = pipeline.df
xr_dataset = pipeline.ds

# Continue pipeline
pipeline.step_4_run_hypothesis_tests()
pipeline.step_5_create_visualizations()
pipeline.step_6_save_outputs()
```

---

## 📖 Input Data Format

Expected CSV columns (PitchBook export format):

| Column | Type | Description |
|--------|------|-------------|
| `CompanyID` | int | Unique company identifier |
| `CompanyName` | str | Company name |
| `Description` | str | Company description (for vagueness scoring) |
| `Keywords` | str | Industry keywords (for integration cost) |
| `FirstFinancingSize` | float | First financing amount in USD |
| `LastFinancingDealType` | str | Last deal type (e.g., "Series B") |
| `Employees` | int | Employee count |
| `YearFounded` | int | Year company was founded |
| `TotalRaised` | float | Total capital raised in USD |

*Note: Column names are case-insensitive and support both PascalCase and snake_case variants.*

---

## 🧪 Testing

### Unit Tests
```bash
# Test feature engineering
python src/feature_engineering.py

# Test hypothesis tests (with simulated data)
python src/hypothesis_tests.py

# Test visualizations
python src/visualizations.py
```

### Integration Test
```bash
# Full pipeline with demo data
python run_pipeline.py --demo
```

---

## 📚 Dependencies

See `requirements.txt`:
- `pandas >= 1.5.0` - Data manipulation
- `numpy >= 1.24.0` - Numerical operations
- `xarray >= 2023.1.0` - Multi-dimensional arrays
- `statsmodels >= 0.14.0` - Statistical models
- `matplotlib >= 3.7.0` - Plotting
- `seaborn >= 0.12.0` - Statistical visualization

---

## 🤝 Contributing

This pipeline follows modular design principles:
- **Separation of concerns:** Each module handles one responsibility
- **Type hints:** All functions include type annotations
- **Docstrings:** Comprehensive documentation with examples
- **Error handling:** Graceful handling of missing data
- **Reproducibility:** Random seeds and metadata tracking

---

## 📝 Citation

If you use this pipeline in your research, please cite:

```bibtex
@software{hypothesis_testing_pipeline,
  title = {Hypothesis Testing Pipeline for Promise Vagueness Research},
  author = {[Your Name]},
  year = {2024},
  url = {https://github.com/[your-repo]/hypothesis_testing_pipeline}
}
```

---

## 📧 Support

For issues or questions:
- Open an issue on GitHub
- Review existing documentation in this README
- Check function docstrings in source code

---

## 🔖 Version History

- **v1.0.0** (2024-10-27): Initial release
  - H1 and H2 hypothesis tests
  - xarray-based data management
  - Comprehensive visualization suite
  - Modular architecture

---

## ⚖️ License

MIT License - see LICENSE file for details
