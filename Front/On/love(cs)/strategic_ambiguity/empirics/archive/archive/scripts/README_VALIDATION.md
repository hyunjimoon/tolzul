# E and L Design Validation

## Overview

This validation suite comprehensively tests whether the E and L definitions are correctly implemented in the consolidated data.

## Files

1. **`VALIDATION_METHODS.md`** - Complete documentation of all 9 validation methods
2. **`validate_E_L_design.py`** - Executable validation script with plots

## Quick Start

```bash
# Run validation
python scripts/validate_E_L_design.py
```

## What Gets Validated

### Critical Tests (MUST PASS)

1. **E=1 Cohort Purity**
   - ✅ 100% Early Stage VC / Series A
   - ❌ NO Buyout/LBO, M&A, Later Stage VC

2. **L Definition**
   - ✅ L defined only for E=1 companies
   - ✅ L=1 means Series B+ progression

3. **Temporal Consistency**
   - ✅ L rate increases monotonically (2023 ≤ 2024 ≤ 2025)
   - ✅ Once L=1, stays L=1 (no regressions)

4. **Cohort Stability**
   - ✅ Cohort size constant (no survivorship bias)
   - ✅ LEFT JOIN preserved all E=1 companies

### Important Tests (SHOULD PASS)

5. **Impossible Transitions**
   - ✅ No backward transitions (Early → Seed/Angel)
   - ⚠️  Detect suspicious transitions (Early → Buyout/LBO)

6. **Progression Rate Sanity**
   - ✅ 2 years: 10-30% Later Stage
   - ✅ 3 years: 15-35% Later Stage
   - ✅ 4 years: 20-45% Later Stage

7. **Outcome Categories**
   - ✅ Reasonable distribution (L=1, stayed Early, failed, etc.)

8. **V×F Feasibility**
   - ✅ Description/Keywords availability
   - ✅ F_flexibility distribution

### Optional Test

9. **State-based Design**
   - If LastFinancingDate available: verify E captures "state" not "event"
   - Otherwise: SKIP

## Output

### Terminal Output

```
================================================================================
COMPREHENSIVE E AND L VALIDATION
================================================================================

Loading: companies_21_23-24-25.parquet
✓ Loaded: 45,556 companies

================================================================================
TEST 1: E=1 Cohort Purity
================================================================================

Purpose: Verify that 100% of companies are Early Stage VC / Series A

Results:
  Early Stage VC (E=1): 45,556 / 45,556 (100.0%)

Checking for EXCLUDED deal types in DealType_2021...
  ✓ Buyout/LBO: 0 found
  ✓ Merger/Acquisition: 0 found
  ✓ Later Stage VC (baseline): 0 found
  ✓ Series B+ (baseline): 0 found

✓ No contamination detected

Verdict: ✓ PASS - All companies are E=1

Plot saved: outputs/validation/test1_cohort_purity.png

[... Tests 2-9 ...]

================================================================================
VALIDATION SUMMARY
================================================================================

Critical Tests:  4 / 4 PASSED
  ✓ E=1 Cohort Purity: PASS
  ✓ L Definition: PASS
  ✓ Temporal Consistency: PASS
  ✓ Cohort Stability: PASS

Important Tests: 4 / 4 PASSED
  ✓ Impossible Transitions: PASS
  ✓ Progression Rate Sanity: PASS
  ✓ Outcome Categories: PASS
  ✓ V×F Feasibility: INFO

Warnings: 0

================================================================================
Overall Status: ✓ READY FOR ANALYSIS
================================================================================

✅ E and L design intent is correctly implemented!
   All critical tests passed. You can proceed with hypothesis testing.

Plots saved to: outputs/validation/
```

### Generated Plots

1. **`test1_cohort_purity.png`**
   - Bar chart: Top 10 deal types in baseline
   - Expected: All "Early Stage VC" or "Series A"

2. **`test3_L_progression.png`**
   - Line chart: L=1 rate over time (2023, 2024, 2025)
   - Expected: Monotonically increasing

3. **`test6_cohort_stability.png`**
   - Bar chart: Cohort size over time
   - Expected: Flat (constant 45,556)

4. **`test7_progression_sanity.png`**
   - Line chart with bands: Actual L rate vs expected range
   - Expected: Within gray bands

5. **`test8_outcome_distribution.png`**
   - Pie chart: E=1 outcomes in 2025
   - Categories: Later Stage (L=1), Still Early (L=0), Buyout/LBO, M&A, Missing, Other

## Interpretation

### ✅ ALL PASS

```
Overall Status: ✓ READY FOR ANALYSIS
```

**Meaning**: E and L are correctly implemented. Proceed with hypothesis testing.

**Actions**:
```bash
# Run hypothesis test
python scripts/test_hypothesis_VxF.py

# Or industry-specific
python scripts/test_hypothesis_VxF.py --industry quantum
python scripts/test_hypothesis_VxF.py --industry transportation
```

### ✗ CRITICAL FAIL

```
Overall Status: ✗ NOT READY
```

**Meaning**: E or L implementation has critical issues.

**Actions**:
1. Review failed tests in terminal output
2. Check sample companies shown in failures
3. Re-run consolidation with fixes:
   ```bash
   python scripts/consolidate_2021_cohort.py
   python scripts/validate_E_L_design.py
   ```

### Common Issues

#### Issue 1: E=1 Cohort Purity FAIL

**Symptom**:
```
✗ FAIL: Found 12,345 non-Early Stage companies!
Sample non-E companies:
  CompanyID  CompanyName         DealType_2021
  100000-81  Restaurant Assoc    Buyout/LBO
```

**Fix**: Consolidation script didn't filter properly
```bash
# Check consolidate_2021_cohort.py lines 50-57
# Ensure PAT_E filtering is applied
```

#### Issue 2: Temporal Consistency FAIL

**Symptom**:
```
✗ Found 234 regressions (L=1 → L=0)
  12345-67: L=1 in 2023 but L=0 in 2024
```

**Fix**: Data quality issue - investigate raw data
```bash
# Check specific companies
# May indicate:
# - Data entry errors
# - Downrounds (rare)
# - Acqui-hires (re-classified)
```

#### Issue 3: Progression Rate WARNING

**Symptom**:
```
⚠️  WARNING - Some rates outside expected range
  L_2025: 8.2% (expected 20-45%) - ⚠️  LOW
```

**Interpretation**: Could mean:
- Cohort is unusually unsuccessful (possible)
- Missing data issue (check Test 5)
- Wrong year labels (check consolidation)

**Actions**:
1. Check missing data rates
2. Verify consolidation merged correct years
3. Compare with external benchmarks

## Validation Logic

### E Definition Compliance

```python
# E=1: Early Stage VC / Series A as of 2021.12
PAT_E = re.compile(r"(?:\bEarly\s*Stage\s*VC\b|\bSeries\s*A(?:\b|[\s\-]?\d*)\b)", re.I)

# All companies must match
assert df['DealType_2021'].apply(lambda x: bool(PAT_E.search(str(x)))).all()
```

### L Definition Compliance

```python
# L=1: Later Stage VC / Series B+ at endpoint
PAT_L = re.compile(r"(?:\bLater\s*Stage\s*VC\b|\bSeries\s*[B-G](?:\b|[\s\-]?\d*)\b)", re.I)

# L defined only for E=1 companies
df_L = df[df['E_2021'] == True]  # Already filtered in consolidation

# L progression
df['L_2025'] = df['DealType_2025'].apply(lambda x: bool(PAT_L.search(str(x or ""))))
```

### Temporal Consistency Check

```python
# Monotonic increase
l_2023 = df['L_2023'].sum()
l_2024 = df['L_2024'].sum()
l_2025 = df['L_2025'].sum()

assert l_2023 <= l_2024 <= l_2025, "L counts must increase"

# Individual persistence
for idx, row in df.iterrows():
    if row['L_2023']:
        assert row['L_2024'], "Once L=1, stays L=1"
        assert row['L_2025'], "Once L=1, stays L=1"
```

## Troubleshooting

### No plots generated

**Cause**: matplotlib not installed

**Fix**:
```bash
pip install matplotlib
python scripts/validate_E_L_design.py
```

### File not found

**Cause**: Consolidation not run

**Fix**:
```bash
# Run consolidation first
python scripts/consolidate_2021_cohort.py

# Then validate
python scripts/validate_E_L_design.py
```

### All tests SKIP

**Cause**: Wrong column names

**Fix**: Check that consolidated file has:
- `DealType_2021`
- `DealType_2023`
- `DealType_2024`
- `DealType_2025`

## Next Steps

After validation passes:

1. **Run hypothesis test**:
   ```bash
   python scripts/test_hypothesis_VxF.py
   ```

2. **Review outputs**:
   ```bash
   ls outputs/hypothesis_VxF/
   ```

3. **Interpret results**:
   - Check β_VF coefficient and p-value
   - Review interaction plot
   - Compare quantum vs transportation vs all

4. **Iterate**:
   - If β_VF > 0 and p < 0.05: Hypothesis supported ✅
   - If β_VF ≈ 0 or p > 0.05: Hypothesis not supported
   - Check robustness with different controls

## References

- E definition: `scripts/README_E_L_DEFINITION.md`
- Consolidation: `scripts/consolidate_2021_cohort.py`
- Hypothesis test: `scripts/test_hypothesis_VxF.py`
- Validation methods: `scripts/VALIDATION_METHODS.md`
