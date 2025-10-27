# Usage Examples

## 1. Quick Start with Demo Data

```bash
# Run complete pipeline with simulated data
python run_pipeline.py --demo
```

This will:
- Generate 300 simulated companies
- Compute vagueness and integration cost
- Run H1 and H2 hypothesis tests
- Create all diagnostic visualizations
- Save results to `output/`

## 2. Run with Real PitchBook Data

```bash
# Assuming you have exported PitchBook data to CSV
python run_pipeline.py --data /path/to/pb_company_export.csv --output results/
```

Expected CSV format (pipe-delimited `|`):
```
CompanyID|CompanyName|Description|Keywords|FirstFinancingSize|LastFinancingDealType|Employees|YearFounded|TotalRaised
12345|Acme AI|We provide approximately scalable AI solutions...|software, AI, cloud|5000000|Series B|50|2020|15000000
```

## 3. Programmatic Usage

```python
from run_pipeline import HypothesisTestingPipeline
import pandas as pd

# Initialize pipeline
pipeline = HypothesisTestingPipeline(
    data_path="data/my_companies.csv",
    output_dir="my_results/"
)

# Run all steps
pipeline.run_full_pipeline()

# Or run steps individually
pipeline.step_1_load_data()
pipeline.step_2_engineer_features()

# Access intermediate results
engineered_df = pipeline.df
print(engineered_df[['vagueness', 'high_integration_cost', 'early_funding_musd']].head())

# Continue with analysis
pipeline.step_3_create_xarray_dataset()
pipeline.step_4_run_hypothesis_tests()

# Access model results
h1_model = pipeline.results['h1']
h2_model = pipeline.results['h2']
print(h1_model.summary())

# Create visualizations
pipeline.step_5_create_visualizations()
pipeline.step_6_save_outputs()
```

## 4. Custom Analysis

### Custom Formulas

```python
from hypothesis_tests import run_full_hypothesis_tests

# Load your data
df = pd.read_csv("processed_data.csv")

# Run with custom formulas
results = run_full_hypothesis_tests(
    df,
    h1_formula="early_funding_musd ~ vagueness + employees_log + year_founded + total_raised",
    h2_formula="later_success ~ vagueness * high_integration_cost + early_funding_musd + firm_age + total_raised"
)

# Access results
print("H1 vagueness coefficient:", results['h1'].params['vagueness'])
print("H2 interaction term:", results['h2'].params['vagueness:high_integration_cost'])
```

### Using xarray for Subsetting

```python
import xarray as xr

# Load processed dataset
ds = xr.open_dataset("output/pb_processed_dataset.nc")

# Filter to high-vagueness companies
high_vague = ds.where(ds['vagueness'] > 0.5, drop=True)
print(f"High vagueness companies: {high_vague.dims['company_id']}")

# Group by sector (if available)
if 'sector' in ds.coords:
    sector_means = ds.groupby('sector').mean('company_id')
    print(sector_means['vagueness'])

# Select specific companies
company_subset = ds.sel(company_id=[0, 1, 2, 3, 4])

# Convert to pandas for further analysis
df_subset = company_subset.to_dataframe().reset_index()
```

## 5. Feature Engineering Only

```python
from feature_engineering import engineer_features, compute_vagueness

# Apply to your own dataframe
df = pd.read_csv("my_companies.csv")
df_engineered = engineer_features(df)

# Or compute individual features
vagueness_scores = df['Description'].apply(compute_vagueness)
```

## 6. Visualization Only

```python
from visualizations import create_all_visualizations
import pickle

# Load saved model results
with open("output/model_results.pkl", "rb") as f:
    results = pickle.load(f)

# Load data
df = pd.read_csv("processed_panel.csv")

# Create all plots
created_files = create_all_visualizations(
    df,
    results,
    output_dir="my_plots/"
)

print("Created:", created_files.keys())
```

## 7. Interpreting Results

### H1: Early Funding Effect

**Expected:** α₁ < 0 (vagueness hurts early funding)

```python
h1_model = results['h1']
vagueness_coef = h1_model.params['vagueness']
p_value = h1_model.pvalues['vagueness']

if vagueness_coef < 0 and p_value < 0.05:
    print("✓ H1 supported: Vague descriptions reduce early funding")
    print(f"  Effect size: ${vagueness_coef:.2f}M per unit vagueness")
else:
    print("✗ H1 not supported")
```

### H2: Later Success with Moderation

**Expected:** β₁ > 0 (helps in modular), β₃ < 0 (hurts in integrated)

```python
h2_model = results['h2']
beta1 = h2_model.params['vagueness']
beta3 = h2_model.params['vagueness:high_integration_cost']

# Effect in modular sectors (software, APIs)
modular_effect = beta1
print(f"Modular sector effect: {modular_effect:.4f}")

# Effect in integrated sectors (hardware, robotics)
integrated_effect = beta1 + beta3
print(f"Integrated sector effect: {integrated_effect:.4f}")

# Interaction magnitude
print(f"Moderation effect: {beta3:.4f}")

if beta1 > 0 and beta3 < 0:
    print("✓ H2 supported: Vagueness helps in modular, hurts in integrated")
```

## 8. Output Files

### xarray Datasets (`.nc`)

```python
import xarray as xr

# Load processed data
ds = xr.open_dataset("output/pb_processed_dataset.nc")
print(ds)

# Load model results
results_ds = xr.open_dataset("output/model_results.nc")
print("H1 coefficients:", results_ds['h1_coef'].values)
print("H1 p-values:", results_ds['h1_pval'].values)
```

### CSV Tables

```python
import pandas as pd

# Summary table
summary = pd.read_csv("output/hypothesis_test_summary.csv")
print(summary)

# Detailed coefficients
h1_table = pd.read_csv("output/h1_coefficients.csv")
print(h1_table)
```

## 9. Common Issues

### Missing Data

```python
# Check for missing values before analysis
df_clean = df.dropna(subset=['vagueness', 'early_funding_musd', 'later_success'])
print(f"Dropped {len(df) - len(df_clean)} rows with missing data")
```

### Integration Cost Classification

```python
from feature_engineering import classify_integration_cost

# Custom classification
df['integration_cost'] = df.apply(
    lambda row: classify_integration_cost(row['Keywords'], row['Description']),
    axis=1
)

# Verify distribution
print(df['integration_cost'].value_counts())
```

### Vagueness Scoring

```python
from feature_engineering import compute_vagueness

# Test on sample text
text = "We provide approximately scalable AI solutions for flexible deployment"
score = compute_vagueness(text)
print(f"Vagueness score: {score:.3f}")

# Custom hedge words (optional enhancement)
# Modify hedge_words list in feature_engineering.py
```

## 10. Extending the Pipeline

### Add New Controls

```python
# In your script
df['new_control'] = ...  # Add your custom variable

# Update H1 formula
results = run_full_hypothesis_tests(
    df,
    h1_formula="early_funding_musd ~ vagueness + employees_log + year_founded + new_control"
)
```

### Add New Hypotheses

```python
# Create H3 model
import statsmodels.formula.api as smf

model_h3 = smf.ols(
    "total_raised ~ vagueness * high_integration_cost + early_funding_musd",
    data=df
).fit()

print(model_h3.summary())
```

## 11. Performance Tips

For large datasets (>10,000 companies):

```python
# Use chunking for feature engineering
chunks = []
for chunk in pd.read_csv("large_file.csv", chunksize=1000):
    chunk_engineered = engineer_features(chunk)
    chunks.append(chunk_engineered)

df = pd.concat(chunks, ignore_index=True)
```

## 12. Reproducibility

```python
# Always set random seed for simulated data
import numpy as np
np.random.seed(42)

# Record pipeline version
from run_pipeline import HypothesisTestingPipeline
pipeline = HypothesisTestingPipeline(...)
print("Pipeline version:", pipeline.metadata['pipeline_version'])
```
