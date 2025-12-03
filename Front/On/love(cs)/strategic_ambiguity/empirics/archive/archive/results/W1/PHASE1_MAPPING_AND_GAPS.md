# Phase 1: Family 1 → Family 2 Mapping & Gap Analysis

**Date**: 2025-10-27
**Purpose**: Charlie Fine & Scott Stern 교수님 보고용 pipeline refactoring

---

## 1. FUNCTIONAL MAPPING TABLE

| Family 1 Component | Key Functions | Family 2 Target | Status | Notes |
|-------------------|---------------|-----------------|--------|-------|
| **pipeline_xarray.py** | Pipeline orchestration, checkpoint/resume | **run_pipeline.py** | ✅ MAPPED | Both use step-based architecture |
| **01_process_company.py** | AI/ML filtering, vagueness calculation, integration cost classification | **feature_engineering.py** | ⚠️ PARTIAL | Vagueness formula differs, missing survival logic |
| **02_process_deal_data.py** | Series A/B identification, date filtering, funding_success calculation | **feature_engineering.py** | ⚠️ PARTIAL | Missing 3-snapshot logic for survival |
| **03_create_panel.py** | Panel construction (firm × round), missing Series B records | **feature_engineering.py** | ❌ GAP | New requirement uses survival, not panel structure |
| **04_run_analysis.py** | H1 (OLS on Series A), H2 (Logit on Series B), reversal test | **hypothesis_tests.py** | ⚠️ PARTIAL | H2 needs survival DV, missing robustness test |
| **05_create_deliverables.py** | 4 tables + 4 figures (bar/line/interaction plots) | **visualizations.py** | ✅ MAPPED | Structure compatible, needs ROC curve |
| **exploration.ipynb** | xarray tutorial, three-way interaction visualization | N/A (archive) | ✅ REFERENCE | High-quality interaction plots to reuse |
| **pipeline_simple.ipynb** | Simplified walkthrough, Korean documentation | N/A (archive) | ✅ REFERENCE | Statistical logic patterns |

---

## 2. VARIABLE MAPPING

### 2.1 Feature Engineering Variables

| Family 1 Variable | Formula/Logic | Family 2 Target | Implementation Status |
|-------------------|---------------|-----------------|----------------------|
| `vagueness` | Formula: `50 + 10*(vague_count - precise_count)`, range [0,100] | `vagueness` | ✅ EXISTS (different scale: 0-1) |
| `high_integration_cost` | Keywords: chip/asic/robotics=1, api/saas=0 | `high_integration_cost` | ✅ EXISTS |
| `early_funding_musd` | FirstFinancingSize in millions | `early_funding_musd` | ✅ EXISTS |
| `funding_success` (Series A) | DealSize > 0 AND Status=="Completed" | N/A | ❌ DEPRECATED (not in new spec) |
| `funding_success` (Series B) | Same as Series A | N/A | ❌ DEPRECATED |
| `later_success` | Binary for Series B+ funding | N/A | ❌ REPLACE with `survival` |
| **`survival`** | **NEW**: in 20230501 snapshot AND LastFinancingDate >= 2021-11-01 | **`survival`** | ❌ MISSING (critical) |
| `log_series_a_amount` | log(Series A size + 1) | N/A | ⚠️ NEEDED for H2 robustness |
| `employees_log` | log(employees+1) | `employees_log` | ✅ EXISTS (named `compute_log_employees`) |
| `year_founded` | From company data | `firm_age` | ✅ EXISTS (as derived feature) |
| **`founder_credibility`** | **NEW**: Not in Family 1 | **`founder_credibility`** | ❌ MISSING (placeholder=0 OK) |
| `sector_fe` | For fixed effects | N/A | ❌ MISSING (use industry/keywords) |

### 2.2 Hypothesis Test Variables

| Test | Family 1 Specification | Family 2 Target | Gap |
|------|------------------------|-----------------|-----|
| **H1** | `log(Series A amount) ~ vagueness + employees` | `early_funding_musd ~ vagueness + founder_credibility + high_integration_cost + log(employees+1) + sector_fe + year_founded` | ⚠️ Missing controls: founder_credibility, sector_fe, year_founded |
| **H2 Main** | `funded (Series B) ~ vagueness + employees` | `survival ~ vagueness * high_integration_cost + founder_credibility + log(employees+1) + sector_fe + year_founded` | ❌ DV changed from `later_success` to `survival`, NO early_funding control (mediator) |
| **H2 Robustness** | N/A | `series_b_funding ~ vagueness * high_integration_cost + series_a_funding + controls` | ❌ MISSING (new requirement) |

---

## 3. DATA PROCESSING LOGIC MAPPING

### 3.1 Snapshot Processing (NEW REQUIREMENT)

| Task | Family 1 Logic | Family 2 Target | Status |
|------|----------------|-----------------|--------|
| Load 3 snapshots | N/A (single dataset) | Load 20211201, 20220101, 20230501 | ❌ MISSING |
| Survival definition | N/A | `(company in 20230501) AND (LastFinancingDate >= 2021-11-01)` | ❌ MISSING |
| 18-month window | Series B date filter: 2023-05-01 to 2025-10-31 | **Clarification needed**: Is 18-month window from 20230501 backwards (to ~2021-11-01)? | ⚠️ AMBIGUOUS |
| Down rounds | N/A | Flag but not exclude | ❌ MISSING |

### 3.2 Company Filtering

| Filter | Family 1 | Family 2 | Status |
|--------|----------|----------|--------|
| AI/ML sector | Keyword matching (extensive list) | Same | ✅ COMPATIBLE |
| Date range | Series A: 2021-01-01 to 2022-10-31 | Use snapshot dates | ⚠️ NEEDS ALIGNMENT |

### 3.3 Panel Structure

| Aspect | Family 1 | Family 2 | Decision Needed |
|--------|----------|----------|-----------------|
| Panel format | Long format (firm × round) | N/A | ❌ DEPRECATED: Use cross-sectional with survival |
| Missing Series B | Impute with `funding_success=0` | N/A | ❌ NOT NEEDED (survival is binary) |

---

## 4. CRITICAL GAPS & ACTION ITEMS

### 🔴 HIGH PRIORITY (MUST IMPLEMENT TODAY)

1. **Survival Variable (feature_engineering.py)**
   - [ ] Implement `create_survival_from_snapshots(deal_data)` function
   - [ ] Load 3 snapshots: 20211201, 20220101, 20230501
   - [ ] Logic: `survival = (company_id in snapshot_20230501) AND (LastFinancingDate >= "2021-11-01")`
   - [ ] Clarify 18-month window interpretation

2. **H2 Main Model (hypothesis_tests.py)**
   - [ ] Replace DV from `later_success` to `survival`
   - [ ] Add interaction term: `vagueness * high_integration_cost`
   - [ ] **CRITICAL**: Do NOT include `early_funding` as control (mediator)
   - [ ] Add controls: `founder_credibility`, `log(employees+1)`, `sector_fe`, `year_founded`

3. **H2 Robustness Test (hypothesis_tests.py)**
   - [ ] New function: `run_h2_robustness(data)`
   - [ ] Model: `series_b_funding ~ vagueness * high_integration_cost + series_a_funding + controls`
   - [ ] Extract series_a_funding and series_b_funding from deal data

4. **founder_credibility Variable (feature_engineering.py)**
   - [ ] Decision: Use placeholder `founder_credibility = 0` for today
   - [ ] Document in code: "TODO: Implement founder credibility score (e.g., prior exits, patents, degrees)"

5. **sector_fe Variable (feature_engineering.py)**
   - [ ] Extract from Keywords or PrimaryIndustry columns
   - [ ] Categorical variable for regression

### 🟡 MEDIUM PRIORITY (NICE TO HAVE)

6. **Down Rounds Detection (feature_engineering.py)**
   - [ ] Flag: `is_down_round = (PostValuation_t < PostValuation_{t-1})`
   - [ ] Add to dataset but do not exclude

7. **ROC Curve (visualizations.py)**
   - [ ] Add `plot_h2_roc_curve()` for logistic regression diagnostic

8. **Vagueness Scale Standardization**
   - [ ] Family 1: 0-100 scale, Family 2: 0-1 scale
   - [ ] Decision: Use 0-100 scale (easier interpretation for professors)

### 🟢 LOW PRIORITY (DEFER TO TOMORROW)

9. **Perfect Data Cleaning**
   - Use placeholders today, iterate tomorrow

10. **Advanced Founder Credibility**
    - Use `founder_credibility=0` today, implement scraping tomorrow

---

## 5. FILE STRUCTURE CHANGES

### Current Structure
```
empirics/code/
├── pipeline_xarray.py                    # Family 1 controller (DELETE)
├── hypothesis_testing_pipeline/
│   ├── run_pipeline.py                   # Family 2 controller (KEEP)
│   └── src/
│       ├── 01_process_company.py         # DELETE
│       ├── 02_process_deal.py            # DELETE
│       ├── 03_create_panel.py            # DELETE
│       ├── 04_run_analysis.py            # DELETE
│       ├── 05_create_deliverables.py     # DELETE
│       ├── feature_engineering.py        # UPDATE
│       ├── hypothesis_tests.py           # UPDATE
│       └── visualizations.py             # UPDATE
├── exploration.ipynb                     # ARCHIVE
└── pipeline_simple.ipynb                 # ARCHIVE
```

### Target Structure (Phase 4)
```
empirics/
├── code/
│   ├── hypothesis_testing_pipeline/
│   │   ├── run_pipeline.py
│   │   └── src/
│   │       ├── feature_engineering.py
│   │       ├── hypothesis_tests.py
│   │       └── visualizations.py
│   └── results_validation.qmd            # NEW
├── outputs/
│   ├── analysis_ready_data.csv
│   ├── h1_results.json
│   ├── h2_results.json
│   └── figures/
└── archive/
    ├── exploration.ipynb
    ├── pipeline_simple.ipynb
    └── old_pipeline/                     # Family 1 files
```

---

## 6. NOTEBOOKS → FAMILY 2 REUSE PATTERNS

### From exploration.ipynb
- **Three-way interaction plot** (vagueness × round × integration cost)
  - Source: Cell 15-17 in exploration.ipynb
  - Target: `visualizations.py::plot_h2_interaction()`
  - Quality: High (publication-ready with error bars)

### From pipeline_simple.ipynb
- **Vagueness calculation logic**
  - Source: Cell 5 (hedge word frequency)
  - Target: `feature_engineering.py::compute_vagueness()`
  - Note: Korean comments explain intuition well

- **Deal filtering heuristic**
  - Source: Cell 7-9 (4-step Series A/B identification)
  - Target: Adapt for snapshot-based survival logic
  - Note: Do NOT reuse panel structure

---

## 7. QUESTIONS FOR USER APPROVAL

### Q1: 18-Month Window Clarification
> "Survival uses 18-month window from 20230501"

**Interpretation A**: Companies must have received financing between 2021-11-01 and 2023-05-01 (18 months backwards)?
**Interpretation B**: Companies must survive until 18 months AFTER 2023-05-01 (i.e., 2024-11-01)?

**Proposed**: Use Interpretation A: `LastFinancingDate >= 2021-11-01 AND company in 20230501 snapshot`

### Q2: Down Rounds
> "Down rounds flagged but not excluded"

**Question**: Should down rounds affect survival calculation, or just be a control variable?

**Proposed**: Add `is_down_round` as a feature, but do NOT change survival definition

### Q3: founder_credibility Placeholder
**Question**: OK to use `founder_credibility=0` for all firms today, implement proper calculation tomorrow?

**Proposed**: Yes, document as TODO in code

### Q4: sector_fe Source
**Question**: Which column should be used for sector fixed effects? Options:
- PrimaryIndustry (if available)
- Keywords (extract via clustering)
- Manual classification based on vagueness keywords

**Proposed**: Use Keywords → create 3-5 sector categories

---

## 8. SUCCESS CRITERIA FOR PHASE 1

- [x] Mapping table created (Family 1 → Family 2)
- [x] Gap list identified (11 items)
- [x] Critical gaps prioritized (5 must-implement items)
- [ ] User approval on questions Q1-Q4
- [ ] Ready to proceed to Phase 2 implementation

---

**Next Step**: Await user approval to proceed with Phase 2 implementation.
