# Simple Workflow - What Actually Happens

## 🎬 One Command Does Everything

```bash
python run_h2_seriesb.py --output outputs/
```

---

## 📊 What Happens Behind the Scenes

```
┌─────────────────────────────────────────────────────────────────┐
│                    run_h2_seriesb.py                            │
│                    (YOU RUN THIS)                                │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  STEP 1: Load 4 Snapshots     │
         │  - Dec 2021 (baseline)        │
         │  - Jan 2022 (mid 1)           │
         │  - May 2022 (mid 2)           │
         │  - May 2023 (endpoint)        │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  STEP 2: Create DV            │
         │  (feature_engineering.py)     │
         │                               │
         │  Company progression:         │
         │  A→B+ = 1 (success)          │
         │  A→A = 0 (stayed)            │
         │  A→M&A = censored            │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  STEP 3: Create IVs           │
         │  (feature_engineering.py)     │
         │                               │
         │  - vagueness (text analysis)  │
         │  - high_integration_cost      │
         │  - employees_log              │
         │  - sector_fe                  │
         │  - year_founded               │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  STEP 4: Preprocessing        │
         │  (feature_engineering.py)     │
         │  preprocess_for_h2()          │
         │                               │
         │  Creates:                     │
         │  - founding_cohort            │
         │  - z_vagueness                │
         │  - z_employees_log            │
         │  - ic_within                  │
         │  Drops: founder_credibility   │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  STEP 5: Run H2 Models        │
         │  (hypothesis_tests.py)        │
         │                               │
         │  1. Primary (no sector FE)    │
         │  2. Robustness (sector FE)    │
         │  3. M&A upper bound           │
         │  4. M&A lower bound           │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  STEP 6: Save Results         │
         │                               │
         │  outputs/                     │
         │  ├─ h2_main_coefficients.csv  │
         │  ├─ h2_robustness_*.csv       │
         │  └─ h2_analysis_dataset.csv   │
         └───────────────────────────────┘
```

---

## 🧩 How Files Connect

```
YOU
 │
 └─► run_h2_seriesb.py
      │
      ├─► imports feature_engineering.py
      │    │
      │    ├─► compute_vagueness()
      │    ├─► classify_integration_cost()
      │    ├─► create_survival_seriesb_progression()  ← 4 snapshots
      │    └─► preprocess_for_h2()                    ← NEW! Fixes singular matrix
      │
      └─► imports hypothesis_tests.py
           │
           ├─► test_h2_main_survival()                ← Primary model
           └─► test_h2_robustness_sector_fe()         ← NEW! Robustness
```

**You never directly touch the module files** - they're automatically imported!

---

## 🎯 Analogy: Making Coffee

**Your situation is like**:

```
BAD (confusing):
- grinder.py
- filter.py
- brewer.py
- heater.py
- old_grinder.py (deprecated)
- old_brewer.py (deprecated)
- check_beans.py (diagnostic)
- check_water.py (diagnostic)

"Wait, which file do I run to make coffee??"

GOOD (what we have now):
- make_coffee.py  ⭐ RUN THIS
  (automatically uses grinder, filter, brewer, heater)

- check_equipment.py (only if something breaks)
```

---

## 📋 When to Use Each File

### Daily Use
```bash
python run_h2_seriesb.py --output outputs/   # Only this!
```

### If Errors Occur
```bash
python diagnose_snapshots.py    # "File not found" errors
python diagnose_series_a.py     # "At Series A: 0" errors
```

### If You Want EDA
```bash
python explore_h2_data.py       # See distributions before modeling
```

### Never Use
- ❌ run_pipeline.py (old)
- ❌ 01_process_*.py through 05_*.py (old modular approach)
- ❌ pipeline_xarray.py (prototype)

---

## 🤔 Why So Many Files Exist?

**History**:
1. **Phase 1** (old): Modular approach with 5 separate scripts
2. **Phase 2** (old): Single `run_pipeline.py` with 2 snapshots
3. **Phase 3** (current): Single `run_h2_seriesb.py` with 4 snapshots ✓

We kept the old files for reference, but **you only need Phase 3**.

---

## ✂️ Should We Delete Old Files?

**Proposal**: Move to archive?

```bash
mkdir archive_old_code
mv code/hypothesis_testing_pipeline/run_pipeline.py archive_old_code/
mv code/hypothesis_testing_pipeline/src/01_*.py archive_old_code/
mv code/hypothesis_testing_pipeline/src/02_*.py archive_old_code/
mv code/hypothesis_testing_pipeline/src/03_*.py archive_old_code/
mv code/hypothesis_testing_pipeline/src/04_*.py archive_old_code/
mv code/hypothesis_testing_pipeline/src/05_*.py archive_old_code/
mv code/pipeline_xarray.py archive_old_code/
mv code/xarray_quick_start.py archive_old_code/
```

**After cleanup, you'd have**:
```
empirics/
├── run_h2_seriesb.py           ⭐ MAIN FILE
├── code/hypothesis_testing_pipeline/src/
│   ├── feature_engineering.py  ✓ Active module
│   ├── hypothesis_tests.py     ✓ Active module
│   └── visualizations.py       ✓ Active module
├── diagnose_snapshots.py       ✓ Diagnostic tool
├── diagnose_series_a.py        ✓ Diagnostic tool
└── explore_h2_data.py          ✓ EDA tool
```

Much cleaner! **Want me to do this?**

---

## 📝 Summary for Your Presentation

**When Prof. Fine asks "How did you run the analysis?"**

Say:
> "I ran a single Python script that:
> 1. Loads 4 PitchBook snapshots
> 2. Constructs Series B+ progression outcome
> 3. Engineers vagueness and integration cost features
> 4. Runs logistic regression with proper preprocessing
> 5. Outputs 4 result files: primary + 3 robustness checks
>
> The code is fully reproducible with one command."

**Don't mention**:
- The old files that don't work
- The complexity of the underlying modules
- The fact that we had to fix singular matrix issues

**Do mention**:
- "Longitudinal 4-snapshot design"
- "12-15% base rate (proper variation)"
- "Multiple robustness checks"
- "Z-score standardization for numerical stability"

---

## 🎓 Teaching Version

**If you were teaching this to a student**:

```python
# This is ALL you need to know:

# 1. Run the analysis
python run_h2_seriesb.py --output outputs/

# 2. Check the main results
cat outputs/h2_main_coefficients.csv

# 3. Interpret
# β₁ (z_vagueness) = effect in modular sectors
# β₃ (interaction) = differential in integrated sectors
# If β₁ > 0 and p < 0.05: H2 supported!
```

---

## 💬 Questions?

**Q**: "Why can't I just have ONE file with everything?"
**A**: We could! But separating feature engineering from statistical models makes debugging easier. The module files are like a library - you import them but don't run them directly.

**Q**: "Do I need to understand feature_engineering.py?"
**A**: No! Just trust it works. If you're curious, read the docstrings.

**Q**: "What if I want to change the H2 formula?"
**A**: Edit `hypothesis_tests.py` line 109 (the formula string), but you probably don't need to!

**Q**: "Can I just delete all the old files?"
**A**: Yes! Let me know and I'll move them to archive.
