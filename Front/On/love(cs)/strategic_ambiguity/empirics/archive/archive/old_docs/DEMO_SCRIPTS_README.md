# xarray Demo Scripts - Quick Start Guide

## Overview

Two demo scripts to help you understand the xarray structure for cohort analysis:

1. **`simple_xarray_demo.py`** - Ultra-simple, focused demo (START HERE!)
2. **`explore_xarray_structure.py`** - Comprehensive interactive exploration

## Which Script Should I Use?

### 🎯 Start with `simple_xarray_demo.py` if you want:
- Quick 5-minute demo
- Focus on the KEY concept: `at_risk` calculation
- Minimal output, clear explanations
- See exactly how `series_A_year` coordinate works

### 🔍 Use `explore_xarray_structure.py` if you want:
- Full dataset exploration
- All variables and coordinates
- Statistical summaries
- Multiple usage examples
- Saved netCDF output for later inspection

## Quick Start

### Step 1: Update File Path

Edit the `DATA_FILE` variable at the top of either script:

```python
# Change this line:
DATA_FILE = "/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/data/raw/consolidated_companies_2022_2024_2025_quantum.parquet"

# To your actual file path (if different)
```

### Step 2: Run the Demo

**Option A: Simple Demo** (recommended first!)
```bash
cd /Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics_ent_strat_ops
python simple_xarray_demo.py
```

**Option B: Full Exploration**
```bash
python explore_xarray_structure.py
```

## What You'll Learn

### Key Concept: The `at_risk` Variable

**OLD WAY** (❌ Not recommended):
```python
# Need separate dummy for each cohort
is_2021_cohort = (series_A_year == 2021)
is_2022_cohort = (series_A_year == 2022)
is_2023_cohort = (series_A_year == 2023)
# ... 10 cohorts = 10 variables!
```

**NEW WAY** (✅ Recommended):
```python
# Single coordinate + computed at_risk
ds.coords['series_A_year'] = series_a_years  # One coordinate

# at_risk computed on-the-fly for any window
at_risk[i, w] = (ds.series_A_year[i] == ds.cohort_year[w])
```

### Dataset Structure

```
<xarray.Dataset>
Dimensions:
  venture_id: N      # Your companies
  window: W          # Cohort × End year combinations

Coordinates:
  * venture_id       (venture_id) int64
  * window           (window) MultiIndex[('cohort_year', 'end_year')]
    series_A_year    (venture_id) int16    # 🔑 KEY: Each venture's cohort
    cohort_year      (window) int16         # Window's cohort
    end_year         (window) int16         # Window's end year

Data variables:
  at_risk            (venture_id, window) int8   # 🎯 KEY: Cohort membership
  L                  (venture_id, window) float32  # Series B+ reached
  z_vagueness        (venture_id) float32
  is_software        (venture_id) int8
  ...
```

## Example Outputs

### Simple Demo Output

```
📂 Step 1: Loading data...
   Loaded 541,234 companies
   Using 100 companies for demo

📐 Step 2: Define dimensions...
   venture_id: N = 100
   window: W = 9

   Windows:
      0: Cohort 2021 → End 2024 (3 yr horizon)
      1: Cohort 2021 → End 2025 (4 yr horizon)
      2: Cohort 2021 → End 2026 (5 yr horizon)
      3: Cohort 2022 → End 2024 (2 yr horizon)
      ...

🎯 Step 3: Extract Series A years...
   Series A year distribution:
      2021: 32 companies
      2022: 35 companies
      2023: 33 companies

✨ Step 5: Compute at_risk variable...
   Formula: at_risk[i,w] = 1 if series_A_year[i] == cohort_year[w]

   Verification by cohort:
      Cohort 2021: 32 ventures at risk
      Cohort 2022: 35 ventures at risk
      Cohort 2023: 33 ventures at risk
```

### Detailed at_risk Inspection

```
First 5 ventures:
Venture    Series A     at_risk across windows
------------------------------------------------------------
0          2022         [0 0 0 1 1 1 0 0 0]
1          2021         [1 1 1 0 0 0 0 0 0]
2          2023         [0 0 0 0 0 0 1 1 1]
3          2022         [0 0 0 1 1 1 0 0 0]
4          2021         [1 1 1 0 0 0 0 0 0]

Windows legend:
  Position 0-2: Cohort 2021
  Position 3-5: Cohort 2022
  Position 6-8: Cohort 2023

👀 Notice:
  - Each venture has at_risk=1 for only ONE cohort year
  - at_risk=1 repeats across different end_years for same cohort
  - This identifies which cohort_year the venture belongs to
```

## Usage Examples

### Example 1: Select 2022 Cohort Only

```python
# Get all ventures with Series A in 2022
cohort_2022 = ds.where(ds.series_A_year == 2022, drop=True)

print(f"Ventures in 2022 cohort: {len(cohort_2022.venture_id)}")
# → 35 ventures
```

### Example 2: Analyze Specific Window

```python
# Window 3: Cohort 2022 → End 2024 (2-year horizon)
window_data = ds.isel(window=3)

# Get only ventures at risk in this window
at_risk_ventures = window_data.where(window_data.at_risk == 1, drop=True)

print(f"Ventures at risk: {len(at_risk_ventures.venture_id)}")
# → 35 ventures (all 2022 cohort)
```

### Example 3: Compare Cohorts

```python
# Compare Series B success across cohorts
for cohort_year in [2021, 2022, 2023]:
    cohort = ds.where(ds.series_A_year == cohort_year, drop=True)

    # Average L (Series B reached) across windows where at_risk
    success_rate = cohort.L.where(cohort.at_risk == 1).mean().values

    print(f"Cohort {cohort_year}: {success_rate*100:.1f}% reached Series B+")
```

## Troubleshooting

### File Not Found Error

```
❌ File not found: /Users/hyunjimoon/.../consolidated_companies_2022_2024_2025_quantum.parquet
```

**Solution 1**: Update the `DATA_FILE` path in the script

**Solution 2**: The `simple_xarray_demo.py` script will automatically create dummy data if file is not found

### Missing Column Errors

The scripts search for columns with multiple naming conventions:
- Series A Year: `'SeriesAYear'`, `'series_a_year'`, `'YearFounded'`
- Company ID: `'CompanyID'`, `'company_id'`, `'id'`
- Sector: `'Sector'`, `'sector'`, `'PrimarySector'`

If your columns have different names, the script will use fallback values or create demo data.

### Import Errors

```bash
# Install required packages
pip install pandas numpy xarray netcdf4
```

## Next Steps After Running Demo

1. **Understand the structure**
   - Review the output carefully
   - Pay special attention to the `at_risk` calculation
   - See how `series_A_year` coordinate eliminates need for dummy variables

2. **Load full dataset**
   ```bash
   python explore_xarray_structure.py
   ```

3. **Inspect saved output**
   ```python
   import xarray as xr
   ds = xr.open_dataset('xarray_demo.nc')
   print(ds)
   ```

4. **Construct real dataset**
   - Run `analyze_for_xarray_design.py` for full analysis
   - Run `construct_xarray_panel.py` to build production dataset
   - Add real vagueness scores using `vagueness_v2.py`
   - Infer `is_software` from keywords/description
   - Track Series B+ progression for `L` variable

5. **Run analysis**
   - Test H1: Vagueness effect on early funding
   - Test H2: Vagueness × Hardware interaction
   - Specification curve across different windows
   - Robustness checks with different cohort definitions

## Key Advantages of This Approach

### 🚀 Performance
- Single `series_A_year` coordinate vs N dummy variables
- Faster computation and lower memory usage
- More efficient xarray operations

### 📖 Clarity
- Explicit cohort assignment logic
- Easy to understand: `at_risk = (series_A_year == cohort_year)`
- Clear validation and debugging

### 🔧 Flexibility
- Easy to add new cohorts (just extend `cohort_years` list)
- No need to create new dummy variables
- Works with any number of cohorts

### ✅ Validation
- `at_risk` makes cohort assignment explicit and verifiable
- Easy to check: each venture should be in exactly one cohort
- Clear error detection if data issues exist

## Files Overview

```
empirics_ent_strat_ops/
├── simple_xarray_demo.py              # 🎯 START HERE: Minimal focused demo
├── explore_xarray_structure.py        # 🔍 Full interactive exploration
├── analyze_for_xarray_design.py       # 📊 Dataset analysis for design
├── construct_xarray_panel.py          # 🏗️  Production dataset constructor
├── XARRAY_DESIGN_README.md            # 📚 Complete design guide
└── DEMO_SCRIPTS_README.md             # 📖 This file
```

## Questions?

**Q: Why use xarray instead of pandas?**
A: xarray handles multi-dimensional data naturally. Our data has two dimensions (venture × window), making xarray ideal. It also provides labeled coordinates, making analysis code clearer.

**Q: What if I have more cohort years?**
A: Just extend the `cohort_years` list. No need to create new variables. That's the beauty of this approach!

**Q: Can I use different window definitions?**
A: Yes! Change `cohort_years` and `horizon_years` to match your needs. The structure adapts automatically.

**Q: How do I add more variables?**
A: Add them to the dataset after construction:
```python
ds['new_variable'] = ('venture_id', values)  # Static variable
ds['time_varying'] = (('venture_id', 'window'), values)  # Time-varying
```

---

**Ready to explore?** Run `python simple_xarray_demo.py` now! 🚀
