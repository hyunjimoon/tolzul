# 🚀 Run This Locally - Quick Reference

## Simplest Path to Understanding xarray Structure

### Step 1: Get the Code
```bash
cd /Users/hyunjimoon/tolzul/Front/On/love\(cs\)/strategic_ambiguity/empirics_ent_strat_ops

# Pull latest changes
git pull origin claude/add-cohort-year-calc-01Sjiez7LYew3s7j636arybn
```

### Step 2: Run Simple Demo (5 minutes)
```bash
# This is the EASIEST way to understand the structure
python simple_xarray_demo.py
```

**What you'll see:**
- How `venture_id × window` dimensions work
- How `series_A_year` coordinate identifies cohorts
- How `at_risk[i,w]` is computed from `series_A_year == cohort_year`
- Visual matrix showing which ventures are "at risk" in which windows

**Example output:**
```
First 5 ventures:
Venture    Series A     at_risk across windows
------------------------------------------------------------
0          2022         [0 0 0 1 1 1 0 0 0]  ← at risk for cohort 2022 only
1          2021         [1 1 1 0 0 0 0 0 0]  ← at risk for cohort 2021 only
2          2023         [0 0 0 0 0 0 1 1 1]  ← at risk for cohort 2023 only
```

### Step 3: (Optional) Full Exploration
```bash
# More detailed analysis with statistics
python explore_xarray_structure.py
```

This creates `xarray_demo.nc` that you can load later:
```python
import xarray as xr
ds = xr.open_dataset('xarray_demo.nc')
print(ds)
```

## Your Data File

Both scripts use this path by default:
```
/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/data/raw/consolidated_companies_2022_2024_2025_quantum.parquet
```

If your file is elsewhere, edit the `DATA_FILE` variable at the top of the script.

## Key Insight You'll Learn

**Instead of this** (creating N dummy variables):
```python
is_2021_cohort = (series_A_year == 2021)
is_2022_cohort = (series_A_year == 2022)
is_2023_cohort = (series_A_year == 2023)
# ... need 10 variables for 10 cohorts!
```

**Do this** (one coordinate + computed at_risk):
```python
ds.coords['series_A_year'] = series_a_years  # Store once

# Compute at_risk for any window
at_risk[i, w] = (ds.series_A_year[i] == ds.cohort_year[w])
```

## The Output Structure

```
<xarray.Dataset>
Dimensions:
  venture_id: 100      # Your companies (using 100 for demo)
  window: 9            # 3 cohorts × 3 horizons

Coordinates:
  series_A_year  (venture_id) int16   # 🔑 KEY: Each venture's cohort year
  cohort_year    (window) int16        # Each window's cohort
  end_year       (window) int16        # Each window's end year

Data variables:
  at_risk        (venture_id, window) int8   # 🎯 Cohort membership indicator
```

## After Running Demo

### Use it in your analysis:
```python
import xarray as xr

# Load your demo dataset
ds = xr.open_dataset('xarray_demo.nc')

# Select 2022 cohort only
cohort_2022 = ds.where(ds.series_A_year == 2022, drop=True)

# Analyze a specific window
window_3 = ds.isel(window=3)  # Cohort 2022 → End 2024
at_risk_in_window = window_3.where(window_3.at_risk == 1, drop=True)

# Test vagueness effect
import statsmodels.api as sm
X = at_risk_in_window.z_vagueness.values
y = at_risk_in_window.L.values  # Series B+ reached
model = sm.OLS(y, sm.add_constant(X)).fit()
print(model.summary())
```

## Questions?

**Q: The script says "File not found"?**
- Check the path matches your actual file location
- Or just run it anyway - `simple_xarray_demo.py` creates dummy data automatically

**Q: I want to use my full dataset, not just 100 companies?**
- Edit `df = df.head(100)` line to `df = df.head(10000)` or remove it entirely
- Note: Full dataset may take longer to process

**Q: Can I modify the cohort years?**
- Yes! Change `cohort_years = [2021, 2022, 2023]` to your preferred years
- Everything else adapts automatically

**Q: How do I add real vagueness scores?**
- After running demo, see `construct_xarray_panel.py` for production version
- Use `vagueness_v2.py` scorer to compute real scores
- Replace placeholder `z_vagueness` with real values

---

**Bottom line:** Just run `python simple_xarray_demo.py` and read the output carefully! 🎯

Everything you need to understand is right there in the printed output.
