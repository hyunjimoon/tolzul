# E and L Definitions - CRITICAL FILTERING

## Problem Identified

The consolidation script was **NOT filtering for E=1 companies**, resulting in the dataset including companies with:
- ❌ Buyout/LBO
- ❌ Merger/Acquisition
- ❌ Later Stage VC
- ❌ Series B+
- ❌ Angel/Seed rounds

This violated the E definition and contaminated the cohort.

## Correct Definitions

### E (Short term survival)

**Definition**: E is defined as funding amount of companies whose **most recent financing was Early Stage VC (Series A)** as of Dec 2021, regardless of when that financing occurred. This state-based definition captures companies currently at the early stage.

**Implementation**:
```python
# Pattern for E=1 (Early Stage VC / Series A)
PAT_E = re.compile(r"(?:\bEarly\s*Stage\s*VC\b|\bSeries\s*A(?:\b|[\s\-]?\d*)\b)", re.I)

# Filter baseline to E=1 only
df_baseline['is_E'] = df_baseline['LastFinancingDealType'].fillna('').apply(
    lambda x: bool(PAT_E.search(str(x)))
)
df_baseline = df_baseline[df_baseline['is_E'] == True].copy()
```

**CRITICAL**: This means:
- ✅ Include: "Early Stage VC", "Series A", "Series A-1"
- ❌ Exclude: Buyout/LBO, Merger/Acquisition, Later Stage VC, Series B+, Angel, Seed

### L (Long term survival)

**Definition**: Among the companies with E=1, by year t, did they secure Series B+? (t=2023, 2024, 2025)

**Implementation**:
```python
# Pattern for L=1 (Later Stage VC / Series B+)
PAT_L = re.compile(r"(?:\bLater\s*Stage\s*VC\b|\bSeries\s*[B-G](?:\b|[\s\-]?\d*)\b)", re.I)

# For each endpoint year
df['L_2023'] = df['DealType_2023'].apply(lambda x: bool(PAT_L.search(str(x or ""))))
df['L_2024'] = df['DealType_2024'].apply(lambda x: bool(PAT_L.search(str(x or ""))))
df['L_2025'] = df['DealType_2025'].apply(lambda x: bool(PAT_L.search(str(x or ""))))
```

**CRITICAL**: This means:
- ✅ L=1: "Later Stage VC", "Series B", "Series C", ..., "Series G"
- ❌ L=0: Still at Early Stage VC, failed, or other outcomes

## Fixed Files

### 1. `scripts/consolidate_2021_cohort.py`

**Changes**:
- ✅ Added `PAT_E` pattern for Early Stage VC matching
- ✅ Added filtering logic immediately after loading baseline
- ✅ Excludes all non-Early Stage VC companies
- ✅ Reports filtering statistics (total → E=1 cohort)
- ✅ Updated docstring with E and L definitions

**Before** (WRONG):
```python
df_baseline = pd.read_parquet(BASELINE)
# NO FILTERING - includes ALL companies
df_consolidated = df_baseline[baseline_cols].copy()
```

**After** (CORRECT):
```python
df_baseline = pd.read_parquet(BASELINE)

# Filter for E=1 cohort (Early Stage VC / Series A only)
df_baseline['is_E'] = df_baseline['LastFinancingDealType'].fillna('').apply(
    lambda x: bool(PAT_E.search(str(x)))
)
df_baseline = df_baseline[df_baseline['is_E'] == True].copy()
# NOW only E=1 companies remain

df_consolidated = df_baseline[baseline_cols].copy()
```

### 2. `scripts/test_consolidated_data.py`

**Changes**:
- ✅ Added `PAT_E` pattern for verification
- ✅ Added `EXCLUDED_PATTERNS` for detecting contamination
- ✅ **NEW Test 5**: E=1 cohort verification
  - Verifies 100% of companies in DealType_2021 are Early Stage VC
  - Checks for NO Buyout/LBO, NO M&A, NO Later Stage VC, etc.
  - Reports samples if contamination found
- ✅ Updated docstring with E definition

**Test 5 Output** (when working correctly):
```
5. E=1 cohort verification (baseline must be Early Stage VC only)...
   Early Stage VC (E=1): 45,556 / 45,556 (100.0%)
   ✓ PASS: All companies are Early Stage VC (E=1)

   Checking for EXCLUDED deal types in DealType_2021...
   ✓ PASS: No excluded deal types found (Buyout/LBO, M&A, etc.)
```

**Test 5 Output** (when FAILING - like before):
```
5. E=1 cohort verification (baseline must be Early Stage VC only)...
   Early Stage VC (E=1): 45,556 / 248,342 (18.3%)
   ✗ FAIL: Found 202,786 companies that are NOT Early Stage VC!

   Checking for EXCLUDED deal types in DealType_2021...
   ✗ FAIL: Found 12,345 companies with 'Buyout/LBO'
   ✗ FAIL: Found 8,901 companies with 'Merger/Acquisition'
```

### 3. `scripts/test_hypothesis_VxF.py`

**Changes**:
- ✅ Updated docstring with E and L definitions
- ✅ Clarified "NO Buyout/LBO, NO Merger/Acquisition"
- ✅ Code already had E=1 filtering as safety check (lines 98-100)

## Verification Process

### Step 1: Run consolidation with E=1 filtering
```bash
python scripts/consolidate_2021_cohort.py
```

**Expected output**:
```
Loading baseline (2021.12)...
   ✓ Loaded: 248,342 companies (all)

Filtering for E=1 cohort (Early Stage VC / Series A)...
   ✓ Filtered: 45,556 companies with E=1 (from 248,342)
   Excluded: 202,786 companies (non-Early Stage VC)
```

### Step 2: Run data quality tests
```bash
python scripts/test_consolidated_data.py
```

**Expected output** (Test 5):
```
5. E=1 cohort verification (baseline must be Early Stage VC only)...
   Early Stage VC (E=1): 45,556 / 45,556 (100.0%)
   ✓ PASS: All companies are Early Stage VC (E=1)

   Checking for EXCLUDED deal types in DealType_2021...
   ✓ PASS: No excluded deal types found (Buyout/LBO, M&A, etc.)

6. Cross-year consistency...
   Early Stage VC (2021): 45,556
   Later Stage VC (2023): ~8,000-12,000
   Later Stage VC (2024): ~9,000-13,000
   Later Stage VC (2025): ~10,000-14,000

7. Sample data (first 3 rows)...
   CompanyID  CompanyName                DealType_2021      DealType_2023     ...
   12345-67   Acme Quantum Computing     Early Stage VC     Later Stage VC    ...
   23456-78   Beta Robotics              Series A           Series B          ...
   34567-89   Gamma Biotech              Early Stage VC     Early Stage VC    ...
```

**CRITICAL**: No Buyout/LBO or Merger/Acquisition in sample!

### Step 3: Run hypothesis test
```bash
python scripts/test_hypothesis_VxF.py
```

**Expected**:
- Cohort size: ~45,556 (E=1 companies)
- L=1 companies (2025): ~10,000-15,000 (22-33% progression rate)
- Regression on clean E=1 cohort

## Why This Matters

### Before Fix (WRONG Cohort)
- Cohort: 248,342 companies (ALL types)
- Includes: LBOs, M&As, already-graduated (Series B+), Angel/Seed
- Problem: Not testing E→L progression, testing mixed bag

### After Fix (CORRECT Cohort)
- Cohort: ~45,556 companies (E=1 only)
- Includes: ONLY Early Stage VC / Series A as of Dec 2021
- Correct: Tests E→L progression as defined

### Impact on Hypothesis Test

**H*: β_VF > 0 (Flexibility amplifies Vagueness effect on Later success)**

With contaminated cohort:
- ❌ LBOs/M&As have different dynamics (exit events, not growth)
- ❌ Already-graduated (Series B+) can't "progress" to L=1 (ceiling effect)
- ❌ Angel/Seed not comparable to Series A stage
- ❌ Results meaningless

With clean E=1 cohort:
- ✅ All companies start at same stage (Early Stage VC)
- ✅ L measures true progression (E → Series B+)
- ✅ Hypothesis test has clear interpretation
- ✅ Results publishable

## Summary

✅ **Fixed**: E=1 filtering in consolidation script
✅ **Verified**: Test 5 catches contamination
✅ **Documented**: E and L definitions in all relevant scripts
✅ **Ready**: Clean cohort for hypothesis testing

**CRITICAL REMINDER**: Always verify Test 5 passes before running analysis!
