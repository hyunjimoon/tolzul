최종결론: Event-based로 하자!!!

# Event-based
at_risk[i, w] = (series_A_year[i] == cohort_year[w])

# State-based (correct for user's needs):
at_risk[i, w] = (stage_at_snapshot(i, cohort_date[w]) == 'Series A')

---

# State-Based Cohorts: The Correct Approach for Your Research

## 🎯 Your E Definition (Critical!)

> "E is defined as funding amount of companies whose **most recent financing was Early Stage VC (Series A) as of Dec 2021**, regardless of when that financing occurred."

This is a **STATE-BASED** definition, not an **EVENT-BASED** definition.

## 🔑 Key Difference

### EVENT-BASED (❌ Wrong for Your Study)
**Definition**: Companies that **GOT** Series A **in 2021**

**Example**:
- Company A: Got Series A in **2019** → ❌ NOT in 2021 cohort
- Company B: Got Series A in **2021** → ✓ IN 2021 cohort

**Code**:
```python
at_risk[i, w] = (series_A_year[i] == cohort_year[w])
```

### STATE-BASED (✅ Correct for Your Study)
**Definition**: Companies **at Series A stage** as of **Dec 2021**

**Example**:
- Company A: Got Series A in **2019**, still at A in Dec 2021 → ✓ IN 2021 cohort
- Company B: Got Series A in **2021**, still at A in Dec 2021 → ✓ IN 2021 cohort
- Company C: Got Series A in **2020**, reached B in 2021 → ❌ NOT in 2021 cohort

**Code**:
```python
at_risk[i, w] = (most_recent_stage_at(i, cohort_date[w]) == 'Series A')
```

## 📊 Real Example

### Company Timeline

```
Company "QuantumSlow":
  2018: Seed
  2019: Series A ←── Got Series A here
  ...
  2021: Still at Series A
  ...
  2023: Series B

Company "QuantumFast":
  2020: Seed
  2021: Series A ←── Got Series A here
  2022: Series B ←── Quick progression
```

### Cohort Membership

#### 2021 Cohort (Dec 31, 2021 snapshot)

**EVENT-BASED (Wrong)**:
- QuantumSlow: ❌ (got Series A in 2019, not 2021)
- QuantumFast: ✓ (got Series A in 2021)

**STATE-BASED (Correct)**:
- QuantumSlow: ✓ (at Series A stage in Dec 2021)
- QuantumFast: ✓ (at Series A stage in Dec 2021)

#### 2022 Cohort (Dec 31, 2022 snapshot)

**STATE-BASED**:
- QuantumSlow: ✓ (still at Series A stage)
- QuantumFast: ❌ (progressed to Series B)

**Key insight**: QuantumSlow appears in **BOTH** 2021 and 2022 cohorts because it was stuck at Series A!

## 🚨 Why This Matters for Your Research

### Your Research Question
> "Does vagueness at Series A affect progression to Series B+?"

### What You're Actually Studying

**With STATE-BASED (Correct)**:
- Cohort = All companies currently stuck at Series A
- Includes both:
  - Recent Series A companies (might be successful)
  - Long-stuck Series A companies (might be struggling)
- Vagueness measured = Vagueness **at time they entered Series A** (whenever that was)

**With EVENT-BASED (Wrong)**:
- Cohort = Only companies that got Series A in specific year
- Misses: Companies stuck at Series A from earlier years
- This UNDERESTIMATES the "stuck at Series A" population

## 🏗️ Implementation

### Files Created

1. **`construct_state_based_xarray.py`**
   - Correct implementation for state-based cohorts
   - Uses `determine_stage_at_snapshot()` to check stage at each date
   - Computes `at_risk` based on stage, not event timing

2. **`test_state_based_cohorts.py`**
   - 5 comprehensive tests
   - Shows exact difference between approaches
   - Run: `python test_state_based_cohorts.py`

3. **`STATE_BASED_COHORTS_README.md`**
   - This documentation

### Usage

```bash
# Run tests to understand the logic
python test_state_based_cohorts.py

# Construct state-based dataset
python construct_state_based_xarray.py \
    --company-file data/processed/consolidated_companies.parquet \
    --deal-file data/processed/consolidated_deals.parquet \
    --snapshot-years 2021 2022 2023 \
    --target-stage "Series A"
```

## 📊 Expected Output Structure

```python
<xarray.Dataset>
Dimensions:
  company_id: N
  window: W

Coordinates:
  * company_id        (company_id) int64
  * window            (window) int64
    snapshot_year     (window) int64  # [2021, 2021, 2021, 2022, ...]
    end_year          (window) int64  # [2022, 2023, 2024, 2023, ...]
    horizon_years     (window) int64  # [1, 2, 3, 1, ...]

Data variables:
  at_risk             (company_id, window) int8
  # at_risk[i,w] = 1 if company i was at Series A stage on snapshot_year[w]

Attributes:
  cohort_logic: "state-based"
  target_stage: "Series A"
  description: "Companies at Series A stage as of Dec 31 of snapshot year"
```

## 🔍 How at_risk is Computed

### Pseudo-code
```python
for each company i:
    for each window w:
        snapshot_date = f"{snapshot_year[w]}-12-31"

        # Get all deals before snapshot
        deals = get_deals_before(company_i, snapshot_date)

        # Find most recent deal
        most_recent = deals.sort_by_date().last()

        # Check if at target stage
        if most_recent.deal_type == 'Series A':
            at_risk[i, w] = 1
        else:
            at_risk[i, w] = 0
```

### Key Properties

1. **Companies can be in MULTIPLE cohorts**
   - If stuck at Series A for 3 years → in 3 cohorts
   - This is EXPECTED and CORRECT

2. **Cohort size can OVERLAP**
   - 2021 cohort and 2022 cohort may share companies
   - Companies that haven't progressed appear in both

3. **Timing flexibility**
   - Company that got Series A in 2015 can be in 2021 cohort
   - As long as they're still at Series A in Dec 2021

## 🎯 What You Need

### Required Data

You **MUST** have complete financing history for each company:

```python
# For each company, you need ALL deals:
deals = pd.DataFrame({
    'CompanyID': [123, 123, 123, 456, 456, ...],
    'DealDate': ['2018-03-15', '2019-06-20', '2020-09-10', ...],
    'DealType': ['Seed', 'Series A', 'Series B', ...],
    'DealAmount': [500000, 3000000, 10000000, ...]
})
```

### Data Sources

1. **PitchBook Deal*.dat files**
   - Extract all financing rounds
   - Merge with company data

2. **Or**: Pre-processed company snapshots with stage info
   - If you have snapshots from Dec 2021, Dec 2022, etc.
   - Each snapshot should include "most recent stage"

### If You Don't Have Deal Data

You **cannot** implement state-based cohorts correctly. You would need to:

1. Get Deal data from PitchBook
2. Or use event-based approach (but this doesn't match your E definition)
3. Or redefine E to be event-based

## ✅ Validation

### How to Verify Your Implementation

```python
# Load your dataset
ds = xr.open_dataset('state_based_dataset.nc')

# Check: Companies should appear in multiple cohorts
at_risk_sum = ds.at_risk.sum('window')
companies_in_multiple = (at_risk_sum > 1).sum().values

print(f"Companies in multiple cohorts: {companies_in_multiple}")
# This should be > 0 for state-based (many companies stuck at Series A)

# Check specific company
company_123_pattern = ds.at_risk.sel(company_id=123).values
print(f"Company 123 at_risk: {company_123_pattern}")
# e.g., [1, 1, 1, 0, 0, 0] = in first 3 cohorts, then progressed
```

### Red Flags

❌ **No companies in multiple cohorts** → You implemented event-based by mistake

❌ **at_risk_sum.max() == 1 for all companies** → You implemented event-based by mistake

✅ **Many companies in 2-3 cohorts** → Correct state-based implementation

## 📚 Further Reading

- **Survival Analysis**: Cox proportional hazards (related concept)
- **Panel Data**: Repeated observations over time
- **Event History Analysis**: Tracking stage transitions

## 🤔 FAQ

**Q: Can a company be in the 2021 cohort AND 2022 cohort?**
A: Yes! If they were at Series A in Dec 2021 AND still at Series A in Dec 2022.

**Q: Doesn't this create dependency between cohorts?**
A: Yes, but this is the correct representation of reality. Companies stuck at Series A for years ARE the interesting cases for studying progression barriers.

**Q: Should I use different vagueness scores for each cohort?**
A: No, use the vagueness from when they FIRST got Series A. The promise was made then.

**Q: What if I only have YearFounded, not deal history?**
A: You cannot implement state-based cohorts. You need deal data with dates and stages.

## 🚀 Next Steps

1. **Run tests**: `python test_state_based_cohorts.py`
2. **Get Deal data**: Extract from PitchBook or your data source
3. **Run construction**: `python construct_state_based_xarray.py`
4. **Validate**: Check that companies appear in multiple cohorts
5. **Analyze**: Use the dataset for your vagueness study

---

**Remember**: Your E definition explicitly says "regardless of when that financing occurred" – this is the hallmark of STATE-BASED cohorts!
