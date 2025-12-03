# xarray Structure Design Analysis

## Overview

This guide explains how to analyze your venture dataset to inform the design of a nested panel xarray structure for testing how promise vagueness affects funding across stages.

## Goal

Design an xarray.Dataset with:
- **Dimensions**: `venture_id × window` (cohort_year, end_year)
- **Purpose**: Test how promise vagueness affects funding across stages
- **Key Innovation**: Use `series_A_year` coordinate instead of multiple cohort dummy variables

## Quick Start

### 1. Prepare Data

Place your consolidated parquet file in one of these locations:
- `data/processed/consolidated_companies_2022_2024_2025_quantum.parquet`
- Or any `data/processed/consolidated_companies*.parquet`

Alternatively, run the pipeline to generate from raw .dat files:
```bash
python pipeline/01_load_data.py
```

### 2. Run Analysis

```bash
python analyze_for_xarray_design.py
```

Or specify a custom data file:
```bash
python analyze_for_xarray_design.py --data-file /path/to/your/data.parquet
```

### 3. Review Results

The script generates:
- `outputs/xarray_design/recommended_xarray_schema.txt` - Detailed schema with actual dimensions
- `outputs/xarray_design/analysis_stats.json` - Statistical summaries

## What the Analysis Provides

### 1️⃣ Venture Dimension Analysis (N)
- Unique CompanyID count → determines venture_id dimension size
- Geographic diversity (HQCountry distribution)
- Sector diversity for stratified analysis

### 2️⃣ Window Dimension Analysis (W)
- Financing date range → informs cohort_year coordinate values
- Series A year distribution → identifies viable cohort years
- Deal type progression → validates Series B tracking feasibility

### 3️⃣ Key Variable Distributions

**Vagueness Proxies:**
- Description text length and coverage
- Keywords text length and coverage
- Informs vagueness scorer applicability

**Exercisability (HW/SW):**
- Hardware vs Software classification feasibility
- Keyword-based inference statistics
- Informs `is_software` moderator variable

**Outcomes:**
- FirstFinancingSize (E) - early funding control
- Series B indicators (L) - primary outcome variable
- Coverage and distribution statistics

**Controls:**
- Employees - firm size control
- YearFounded - cohort effects
- HQCountry - location controls

### 4️⃣ Sector → Industry Hierarchy
- Identifies unique sectors in dataset
- Suggests industry groupings:
  - Transportation (Autonomous, EV Charging, Ride-sharing)
  - Quantum (Computing HW, Quantum SW, Sensing)
  - Software (Enterprise, Consumer, SaaS)
  - Hardware (Robotics, Manufacturing)
- Provides sector-to-industry mapping for coordinate

### 5️⃣ Data Completeness Assessment
- Missing rates for all critical variables
- Time-varying data feasibility (snapshot_date presence)
- Identifies data quality issues before xarray construction

### 6️⃣ Recommended xarray Schema
- Actual dimension sizes (N, W)
- Coordinate definitions with real data ranges
- Variable specifications with coverage stats
- Attributes including sector mappings

## Key Design Insights

### ✅ Use `series_A_year` Coordinate (Recommended)

```python
# BAD: Create dummy variables for each cohort
is_2021_cohort = (ds.series_A_year == 2021)
is_2022_cohort = (ds.series_A_year == 2022)
is_2023_cohort = (ds.series_A_year == 2023)
# ... 10 cohorts = 10 variables!

# GOOD: Use series_A_year coordinate
at_risk = (ds.series_A_year == ds.cohort_year)
```

**Benefits:**
- **Performance**: Single coordinate vs N cohort variables
- **Clarity**: Explicit cohort assignment logic
- **Validation**: Easy to verify at data construction time
- **Flexibility**: Easy to add new cohorts

### ✅ Window as MultiIndex

```python
window = pd.MultiIndex.from_product(
    [cohort_years, end_years],
    names=['cohort_year', 'end_year']
)
```

Each window (w) represents a (cohort_year, end_year) pair:
- `cohort_year`: Year of Series A funding (2021, 2022, 2023)
- `end_year`: Observation endpoint (2024, 2025, 2026)
- `horizon_years`: Computed as `end_year - cohort_year`

### ✅ at_risk Variable

```python
at_risk[i, w] = 1 if series_A_year[i] == cohort_year[w] else 0
```

This identifies which ventures are "at risk" for each cohort_year, enabling proper survival analysis.

## Expected Output Structure

```
<xarray.Dataset>
Dimensions:
  venture_id: 541,234  # Actual count from your data
  window: 9             # 3 cohort_years × 3 end_years

Coordinates:
  * venture_id        (venture_id) int64
  * window            (window) MultiIndex[('cohort_year', 'end_year')]
    cohort_year       (window) int16   # [2021, 2022, 2023]
    end_year          (window) int16   # [2024, 2025, 2026]
    horizon_years     (window) int16   # [1, 2, 3, 4, 5]

    sector            (venture_id) string
    industry          (venture_id) string
    dataset_source    (venture_id) string

Data variables:
  # Time-varying
  L                   (venture_id, window) float32  # Series B+ reached
  at_risk             (venture_id, window) int8     # Cohort membership
  step_up_multiple    (venture_id, window) float32  # Valuation step-up

  # Static (at Series A)
  z_vagueness         (venture_id) float32
  is_software         (venture_id) int8
  E_amount_log        (venture_id) float32
  series_A_year       (venture_id) int16    # KEY: Used for at_risk
  ...
```

## Next Steps After Analysis

1. **Review Schema**: Check `outputs/xarray_design/recommended_xarray_schema.txt`
   - Verify dimension sizes are correct
   - Confirm cohort_year range is appropriate
   - Check variable coverage is sufficient

2. **Review Statistics**: Check `outputs/xarray_design/analysis_stats.json`
   - Look for data quality issues
   - Identify variables needing imputation
   - Verify sector distributions

3. **Construct xarray.Dataset**:
   ```python
   import xarray as xr
   import pandas as pd

   # Load analysis results
   import json
   with open('outputs/xarray_design/analysis_stats.json') as f:
       stats = json.load(f)

   # Create coordinates
   cohort_years = [2021, 2022, 2023]
   end_years = [2024, 2025, 2026]

   window = pd.MultiIndex.from_product(
       [cohort_years, end_years],
       names=['cohort_year', 'end_year']
   )

   # Create dataset
   ds = xr.Dataset(
       coords={
           'venture_id': venture_ids,
           'window': window,
           'series_A_year': ('venture_id', series_a_years),
           'sector': ('venture_id', sectors),
       }
   )

   # Add at_risk variable
   ds['at_risk'] = xr.apply_ufunc(
       lambda sa, cy: (sa == cy).astype(int),
       ds.series_A_year,
       ds.cohort_year,
       vectorize=True
   )
   ```

4. **Validate Construction**:
   ```python
   # Check at_risk makes sense
   assert ds.at_risk.sum('window').max() == 1  # Each venture in ≤1 cohort

   # Verify cohort assignment
   cohort_2021 = ds.where(ds.at_risk.sel(cohort_year=2021), drop=True)
   assert all(cohort_2021.series_A_year == 2021)
   ```

5. **Run Specification Curve Analysis**:
   ```python
   # Use window coordinate for different specifications
   specs = []
   for window_val in ds.window.values:
       result = run_regression(
           ds.sel(window=window_val),
           outcome='L',
           predictor='z_vagueness',
           moderator='is_software'
       )
       specs.append(result)
   ```

## Troubleshooting

### No Data File Found
```
FileNotFoundError: No consolidated parquet file found
```

**Solution**: Run pipeline to generate data:
```bash
python pipeline/01_load_data.py
```

### Column Names Don't Match
The analysis script searches for columns with multiple naming conventions:
- `CompanyID` or `company_id`
- `Description` or `description`
- `HQCountry` or `hq_country`

If your columns use different names, the script will report "NOT FOUND" and suggest what it's looking for.

### Insufficient Series A Data
```
Series A Year coverage: 12.5%
```

**Issue**: Too few ventures have Series A year recorded.

**Solutions**:
1. Infer from financing round data (Deal*.dat files)
2. Filter to ventures with complete financing data
3. Adjust cohort_year range to years with better coverage

### Memory Issues
For datasets >1M companies:
```bash
# Use subset for design phase
python analyze_for_xarray_design.py --data-file data/processed/sample_100k.parquet
```

## References

- xarray documentation: https://docs.xarray.dev/
- Panel data with xarray: https://xarray-contrib.github.io/
- Specification curve analysis: Simonsohn, Simmons & Nelson (2020)

## Support

For issues or questions:
1. Check analysis output in `outputs/xarray_design/`
2. Review statistics JSON for data quality issues
3. Verify data file path and format
4. Check pipeline logs for data loading errors

---

**Ready to analyze?** Run: `python analyze_for_xarray_design.py`
