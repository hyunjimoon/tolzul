# 📋 Task: Code Comparison & Minimal Spec Validation

## Context
I have two sets of Python implementations for "Promise Precision" thesis:

**Set A (Current - Minimal):**
- `/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/theory/thesis/2️⃣_PRODUCTION/Empirics_Early/run.py`
- `/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/theory/thesis/2️⃣_PRODUCTION/Empirics_Later/run.py`

**Set B (Legacy - Potentially Over-spec):**
- `/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/modules/features.py`
- `/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/modules/models.py`
- `/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/modules/plots_F_series.py`

---

## Your Tasks

### 1. **Feature Parity Check**
Compare functionality between Set A and Set B. Answer:
- [ ] Does Set A cover all ESSENTIAL features from Set B?
- [ ] What features in Set B are NOT in Set A? (List them)
- [ ] Are any Set B features over-engineered for thesis purposes?

**Essential Features (must-have):**
- Vagueness index calculation (z-score normalization)
- Hardware/Software classification
- H1: OLS regression (early funding ~ vagueness)
- H2: Logit regression (Series B+ ~ vagueness × hardware)
- Figure generation (scatter + interaction plot)
- Table export (regression results)

**Non-essential (nice-to-have but not critical):**
- Advanced feature engineering (cohorts, sector FE, etc.)
- Multiple specification tests
- Extensive logging/error handling

---

### 2. **Code Quality Assessment**
For Set A (run.py files), evaluate:
- [ ] **Correctness:** Do statistical models match paper specs?
- [ ] **Completeness:** Missing any critical steps?
- [ ] **Maintainability:** Is code readable/documented enough?

**Specific Checks:**
```python
# H1 Model (Empirics_Early/run.py)
"log_series_a ~ vagueness_zscore + is_serial + C(hq_country) + C(founding_year)"
# ✓ Should include controls for serial founder, location, year

# H2 Model (Empirics_Later/run.py)
"series_b_plus ~ vagueness_zscore + hardware + vague_x_hw + is_serial + log_series_a"
# ✓ Should include interaction term (vague_x_hw)
# ✓ Should use logit for binary DV
```

---

### 3. **Integration Feasibility**
Can Set A run standalone with only:
- `1️⃣_INPUT/data/series_a_sample.csv`
- Standard libraries (pandas, numpy, matplotlib, statsmodels)

**Test:**
```bash
cd /Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/theory/thesis/2️⃣_PRODUCTION/Empirics_Early
python3 run.py  # Should generate fig + table
```

If it fails, what dependencies from Set B are needed?

---

### 4. **Refactor Recommendations**
If Set B has useful components, suggest:
- **What to extract:** Specific functions/classes to port to Set A
- **What to discard:** Over-engineered features not needed for thesis
- **How to merge:** Minimal integration strategy

**Example Format:**
```python
# FROM: empirics/modules/features.py
def calculate_vagueness_zscore(text_series):
    """Extract this if Set A lacks proper normalization"""
    pass

# DISCARD: empirics/modules/features.py
def load_company_snapshot(filepath):
    """Too complex - Set A uses simple CSV"""
    pass
```

---

## Output Format

Please provide a structured report:

```markdown
# Code Comparison Report

## 1. Feature Parity Matrix
| Feature | Set A (run.py) | Set B (modules) | Status |
|---------|----------------|-----------------|--------|
| Vagueness calc | ✓ (inline) | ✓ (features.py) | Equivalent |
| H1 regression | ✓ | ✓ (models.py) | ✓ Set A sufficient |
| ... | ... | ... | ... |

## 2. Critical Gaps in Set A
- [ ] Missing: Advanced control variables (sector FE)
- [ ] Missing: Robust SE calculation (HC3 implemented but untested)
- ...

## 3. Over-engineered in Set B
- ❌ load_company_snapshot(): Unnecessary for CSV workflow
- ❌ Extensive logging: Thesis doesn't need production-level logs
- ...

## 4. Integration Priority
**High (extract these):**
1. `features.py::StrategicVaguenessScorer` (lines 50-120) → Better than inline calc
2. `models.py::test_h2_main_growth` spec curve logic (lines 80-100)

**Low (skip):**
3. Cohort analysis functions (not needed)

## 5. Final Recommendation
☑️ Set A is **production-ready** for thesis with minor enhancements:
   - Add vagueness calculation validation from Set B
   - Keep current simplicity for .sh integration

OR

⚠️ Set A needs significant work:
   - Port XYZ from Set B before run_all.sh will work
```

---

## Success Criteria

Your report should enable me to:
1. Run `bash run_all.sh` successfully (INPUT → OUTPUT)
2. Know exactly what (if anything) to port from Set B
3. Confidently submit thesis outputs to advisors (Scott Stern, Charlie Fine)

---

*Prepared by: 권준/나대용 (中軍)*  
*For: Claude Code analysis*
