# Placeholder Variables & Future Implementation

**Date**: 2025-10-27
**Status**: Pipeline working with placeholders for single-snapshot Company data

---

## ⚠️ Variables Using Placeholders or Proxies

### 🔴 HIGH PRIORITY

#### **`survival` (Currently: Proxy)**
- **Current Implementation**: `survival = later_success` (from LastFinancingDealType)
- **Proper Implementation**:
  ```python
  survival = 1 if (company in 20230501 snapshot) AND
                  (LastFinancingDate >= 2021-11-01)
  ```
- **Data Needed**: Deal20211201.dat, Deal20220101.dat, Deal20230501.dat
- **Impact**: HIGH - This is the main DV for H2 Main model
- **Current Limitation**: Proxy may misclassify survival (e.g., got Series B in 2019 but failed in 2022)

---

### 🟡 MEDIUM PRIORITY

#### **`series_a_funding` (Currently: Proxy)**
- **Current**: `series_a_funding = early_funding_musd` (FirstFinancingSize)
- **Proper**: Extract from Deal data where `VCRound == 'Series A'`
- **Data Needed**: Deal data with VCRound column
- **Impact**: MEDIUM - Needed for H2 Robustness control variable

#### **`series_b_funding` (Currently: Missing)**
- **Current**: `series_b_funding = NaN` (all missing)
- **Proper**: Extract from Deal data where `VCRound == 'Series B'`
- **Data Needed**: Deal data with VCRound column
- **Impact**: MEDIUM - This is the DV for H2 Robustness model
- **Current Limitation**: H2 Robustness test cannot run

---

### 🟢 LOW PRIORITY

#### **`founder_credibility` (Currently: Placeholder)**
- **Current**: `founder_credibility = 0` (all companies)
- **Future Implementation**:
  ```python
  founder_credibility = (
      prior_exits * 0.3 +
      log(patents + 1) * 0.2 +
      advanced_degree * 0.2 +
      prior_companies * 0.2 +
      awards * 0.1
  )
  ```
- **Data Needed**: Founder profile data (not in Company.dat)
- **Impact**: LOW - Results may be significant without it (other controls compensate)

#### **`is_down_round` (Currently: Placeholder)**
- **Current**: `is_down_round = 0` (no down rounds detected)
- **Proper**: Compare PostValuation across rounds per company
- **Data Needed**: Deal data with PostValuation and DealDate
- **Impact**: LOW - Optional control for H2 Robustness only

#### **`sector_fe` (Currently: Working with limitations)**
- **Current**: 8 categories via keyword matching
- **Improvement**: Manual validation, better industry taxonomy, or PitchBook's PrimaryIndustry
- **Impact**: LOW - Current categorization sufficient, can be refined

#### **`vagueness` (Currently: Working)**
- **Current**: Keyword counting (vague vs precise words)
- **Enhancement**: LLM-based scoring, context-aware analysis
- **Impact**: LOW - Current method established in literature

---

## 📋 Implementation Priority

### **Phase 1: Get True Survival (After Presentation)** 🔴
1. Obtain Deal data files (3 snapshots)
2. Implement `create_survival_from_snapshots()` with Deal data
3. Modify `run_pipeline.py` to load Company + Deal data together
4. Re-run analysis with true 18-month survival window
5. Compare results to proxy-based results

### **Phase 2: Enable H2 Robustness Test** 🟡
1. Extract Series A and Series B funding from Deal data
2. Implement down round detection
3. Run H2 Robustness: `series_b_funding ~ vagueness * integration_cost + series_a_funding + controls`
4. Compare to H2 Main results

### **Phase 3: Refine Variables** 🟢
1. Implement founder_credibility if data available (optional)
2. Validate sector categorization accuracy
3. Consider LLM-based vagueness scoring (optional)

---

## 🎯 For Today's Presentation

### **What Works** ✅
- ✅ Vagueness calculation (keyword-based, 0-100 scale)
- ✅ H1 test: Early Funding ~ Vagueness + Controls
- ✅ H2 Main test: Survival(proxy) ~ Vagueness × Integration Cost
- ✅ Integration cost classification (hardware vs software)
- ✅ Sector fixed effects (8 categories)
- ✅ All visualizations (scatter, interaction, ROC, coefficient comparison)

### **What's Proxied** ⚠️
- ⚠️ Survival uses later_success (need Deal data for true 18-month window)
- ⚠️ Series A funding uses FirstFinancingSize (need Deal data for precise round)
- ⚠️ Founder credibility = 0 (low impact on results)

### **What's Missing** ❌
- ❌ H2 Robustness test (needs Series B funding from Deal data)
- ❌ Down round detection (needs Deal data)

### **Transparency Statement for Professors**

> "Our analysis uses the May 2023 Company snapshot (504K companies). The **survival variable** currently uses 'later success' (reached Series B+) as a proxy. The proper 18-month survival window requires Deal data with financing dates, which we'll implement in the next iteration. Results should be directionally correct, though the proxy may introduce some misclassification. **Founder credibility** is a placeholder (=0) as we don't have founder profile data, but other controls (firm size, age, sector) should compensate."

---

## 🔬 Technical Details

### **Current Data Flow**
```
Company20230501.dat (631 MB, 504K rows)
    ↓
Feature Engineering
    ├─ vagueness (keyword count) ✅
    ├─ integration_cost (keyword classification) ✅
    ├─ early_funding (FirstFinancingSize) ✅
    ├─ sector_fe (8 categories from Keywords) ✅
    ├─ founder_credibility = 0 ⚠️
    └─ survival = later_success ⚠️
    ↓
Hypothesis Tests
    ├─ H1: Early Funding ~ Vagueness ✅
    ├─ H2 Main: Survival(proxy) ~ Vagueness × Integration ✅
    └─ H2 Robustness: SKIPPED ❌ (needs Deal data)
    ↓
Visualizations ✅
```

### **Future Data Flow (with Deal Data)**
```
Company20230501.dat + Deal{20211201,20220101,20230501}.dat
    ↓
Feature Engineering
    ├─ TRUE survival (3-snapshot + LastFinancingDate logic) ✅
    ├─ series_a_funding (from VCRound='Series A') ✅
    ├─ series_b_funding (from VCRound='Series B') ✅
    └─ is_down_round (PostValuation comparison) ✅
    ↓
Hypothesis Tests
    ├─ H1: Early Funding ~ Vagueness ✅
    ├─ H2 Main: TRUE Survival ~ Vagueness × Integration ✅
    └─ H2 Robustness: Series B ~ Vagueness × Integration + Series A ✅
```

---

## 📞 Questions?

Review:
1. `IMPLEMENTATION_COMPLETE.md` - Full implementation details
2. `PHASE1_MAPPING_AND_GAPS.md` - Design decisions
3. This file - Placeholder status and future work

**Ready for next iteration?** Get Deal data files and implement Phase 1 (True Survival).
