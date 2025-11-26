# Quick Test Instructions for F-Series Plots

## Option 1: Run the Test Script (Recommended)

```bash
# 1. Make sure you have the required packages
pip install pandas numpy matplotlib statsmodels

# 2. Run the test script
python test_F_series.py

# 3. View the outputs
open outputs/F_series_test/    # macOS
xdg-open outputs/F_series_test/ # Linux
explorer outputs\F_series_test\ # Windows
```

**Expected output:**
- 10 PNG files in `outputs/F_series_test/`
- Console output showing model fits and file sizes
- All plots should render without errors

---

## Option 2: Minimal Interactive Test (Python REPL)

```python
import pandas as pd
import numpy as np
from pathlib import Path
from modules import models, plots

# Quick synthetic data
np.random.seed(42)
n = 100
df = pd.DataFrame({
    'E': np.random.uniform(0, 10, n),
    'L': np.random.binomial(1, 0.4, n),
    'z_V': np.random.normal(0, 1, n),
    'F_flexibility': np.random.binomial(1, 0.6, n),
    'founder_serial': np.random.binomial(1, 0.3, n),
    'founding_cohort': np.random.choice(['2015-2017', '2018-2020'], n),
    'region': np.random.choice(['US', 'EU'], n),
    'z_vagueness': np.random.normal(0, 1, n),
    'growth': np.random.binomial(1, 0.4, n),
    'z_employees_log': np.random.normal(0, 1, n),
    'S_stepup_log': np.random.normal(0.5, 0.8, n),
})

# Fit models
hev = models.run_HEV(df)
hlvf = models.run_HLVF(df)
h4 = models.test_h4_growth_interaction(df)

# Generate plots
results = {'hev': hev, 'hlvf': hlvf, 'h4': h4, 'spec_df': None}
paths = plots.create_F_series(df, results, Path("outputs/test"))

print(f"Created {len(paths)} plots in outputs/test/")
```

---

## Option 3: Test with Your Real Data

```python
from pathlib import Path
from modules import models, plots

# Load your actual data
df = pd.read_csv("your_data.csv")  # or however you load it

# Fit the models
results = {
    'hev': models.run_HEV(df),
    'hlvf': models.run_HLVF(df),
    'h4': models.test_h4_growth_interaction(df),
    'spec_df': your_spec_df  # Optional
}

# Generate all F-series plots
paths = plots.create_F_series(df, results, Path("outputs/F_series"))

# View results
for name, path in paths.items():
    print(f"{name}: {path}")
```

---

## What to Check in the Outputs

### Visual Checks

1. **F1_E_vs_V.png**
   - ✅ Red scatter points
   - ✅ Red OLS fit line
   - ✅ X-axis label in green ("V")
   - ✅ Y-axis label in red ("E")

2. **F2_PrL_vs_V.png**
   - ✅ Blue curve
   - ✅ Y-axis from 0 to 1
   - ✅ Caption about median conditioning

3. **F3a_L_given_F.png**
   - ✅ Two skyblue lines
   - ✅ Solid line (F=1, Software)
   - ✅ Dashed line (F=0, Hardware)
   - ✅ Legend distinguishes them

4. **F3b_L_given_C.png**
   - ✅ Two orange lines
   - ✅ Dash-dot line (C=1, Serial)
   - ✅ Dotted line (C=0, First-time)

5. **F4_*.png** (4 distribution plots)
   - ✅ Correct colors: E=red, L=blue, V=green
   - ✅ Appropriate chart types (histograms/bars)

6. **F5_StepUp_by_F.png**
   - ✅ Purple boxplots
   - ✅ Compares F=0 vs F=1

7. **F6_SpecCurve.png**
   - ✅ Scatter points color-coded by term
   - ✅ Horizontal line at y=0
   - ✅ Legend with V, V×F, V×C

### File Checks

```bash
# Check all files exist
ls -lh outputs/F_series_test/*.png

# Should see:
# F1_E_vs_V.png
# F2_PrL_vs_V.png
# F3a_L_given_F.png
# F3b_L_given_C.png
# F4_E.png
# F4_L_2024.png
# F4_L_2025.png
# F4_V.png
# F5_StepUp_by_F.png
# F6_SpecCurve.png
```

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'pandas'"
```bash
pip install pandas numpy matplotlib statsmodels scipy
```

### "Model convergence failed"
This is expected with random synthetic data. The plots should still generate (some may show warnings but still save files).

### Plots look wrong
Check that:
1. Your data has the expected columns (E, L, z_V, F_flexibility, etc.)
2. The models fitted successfully (check return values aren't None)
3. You're using the correct column names (z_V vs V, L vs growth, etc.)

---

## Quick Verification Commands

```bash
# Count outputs
ls outputs/F_series_test/*.png | wc -l
# Should output: 10

# Check file sizes (should all be > 0)
du -h outputs/F_series_test/*.png

# View a specific plot
# macOS:
open outputs/F_series_test/F3a_L_given_F.png

# Linux:
xdg-open outputs/F_series_test/F3a_L_given_F.png
```
