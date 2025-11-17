# Diagnostic Tests for E/L/S Analysis

This folder contains critical diagnostic tests for validating data quality and methodology assumptions in the entrepreneurship strategy analysis.

## Test Scripts

### 1. **verify_EL_definition.py** - E/L Definition Validation

**Purpose:** Checks whether the current E (Early funding) and L (Later success) definitions correctly capture the intended populations.

**Research Question:** Is the "narrow" definition (E=1 only if LastFinancing = Series A at baseline) excluding successful "fast-growing" companies who progressed to Series B+ before baseline?

**What it Tests:**
- Compares **narrow** vs **broad** E/L definitions
- Narrow: E=1 if LastFinancing = "Series A" at baseline (2022.01)
- Broad: E=1 if LastFinancing ≥ "Series A" at baseline (includes B+)
- Identifies companies excluded by narrow definition
- Calculates L (later success) rates for each group
- Detects logically impossible cases (E=0 & L=1)

**Key Outputs:**
```
E (narrow): N companies
E (broad): N+X companies
Excluded: X companies (these got A→B+ before baseline)
L rate for narrow E: Y%
L rate for excluded: Z%
```

**Decision Criteria:**
- If X > 25,000 AND Z% > Y% → Switch to broad definition (features.py:466)
- If X < 10,000 OR Z% < Y% → Keep narrow definition, document limitation
- Critical finding: Excluded companies are more successful, creating selection bias

**Usage:**
```bash
python tests/verify_EL_definition.py
```

**Data Requirements:**
- `data/raw/Company20220101.dat` (baseline snapshot)
- `data/raw/Company20231201.dat` (endpoint snapshot)
- Pipe-delimited PitchBook format with `LastFinancingDealType` column

---

### 2. **test_consecutive_rounds.py** - Bridge Rounds Detection

**Purpose:** Tests whether later VC funding (L) was the VERY NEXT round after early funding (E), or if there were bridge rounds in between.

**Research Question:** Does the step-up calculation (S = PreMoney_t2 / PostMoney_t1) accurately measure A→B growth, or is it confounded by intermediate bridge rounds?

**What it Tests:**
- Identifies E→L transition companies (Series A at baseline → B+ at endpoint)
- Checks for round count columns (TotalFundingRounds, etc.)
- Calculates round_diff = rounds_t2 - rounds_t1
- Analyzes deal type transition patterns (A→B vs A→C vs A→B via bridge)
- Date-based timing analysis as fallback proxy

**Key Outputs:**
```
E→L transitions: N companies
Round count data available: Yes/No

IF round data available:
  Exactly 1 round difference (consecutive): X%
  >1 round difference (bridge rounds): Y%

Deal type transitions:
  A → B: N1 companies
  A → C: N2 companies
  A → A: N3 companies (concerning - stalled?)
```

**Decision Criteria:**
- If Y% > 40% (bridge rounds common) → Options:
  - **Censor**: Exclude non-consecutive from H3/HSF analysis
  - **Request data**: Get full deal-level history to properly code rounds
  - **Document**: Note as major limitation
- If Y% < 20% (mostly consecutive) → Use full E→L sample

**Usage:**
```bash
python tests/test_consecutive_rounds.py
```

**Data Requirements:**
- Same as verify_EL_definition.py
- Ideally also has round count columns (e.g., `TotalFundingRounds`)

---

## Classification Logic

Both scripts use **identical regex patterns** from `modules/features.py` to ensure consistency:

```python
PAT_A = r"(?:\bEarly\s*Stage\s*VC\b|\bSeries\s*A(?:\b|[\s\-]?\d*)\b)"
PAT_Bp = r"(?:\bLater\s*Stage\s*VC\b|\bSeries\s*[B-G](?:\b|[\s\-]?\d*)\b)"
```

**Matches for Series A (E):**
- "Early Stage VC"
- "Series A"
- "Series A-II" (second closing)
- "Series A - 1" (tranche)

**Matches for Series B+ (L):**
- "Later Stage VC"
- "Series B", "Series C", "Series D", "Series E", "Series F", "Series G"
- With variants: "Series B-II", "Series C - 1", etc.

---

## Relationship to Research Design

### Theoretical Model (W2 Slides)
```
V (Vagueness) → E (Early funding) → L (Later success) → S (Step-up)
                ↓                   ↗
                └─────(mediator)────┘
```

**Why These Tests Matter:**

1. **verify_EL_definition.py:** Tests whether E correctly captures "received early VC"
   - Affects HEV (H1): E ~ V + controls
   - Affects HLVF (H2): L ~ V × F (NO E control - mediator principle)
   - Wrong E definition → biased coefficient estimates

2. **test_consecutive_rounds.py:** Tests whether S measures true A→B growth
   - Affects HSF (H3): S ~ V × F + controls (survivors only)
   - Bridge rounds → S confounded by multiple funding events
   - Wrong S measurement → spurious interaction effects

---

## Expected Findings (Pre-Analysis Hypotheses)

### verify_EL_definition.py:
- **Predicted:** 30,000-40,000 fast-growing companies excluded
- **Predicted:** Excluded companies have HIGHER L rates (15-25% vs 3-5%)
- **Implication:** Current narrow definition creates downward bias in E→L effects

### test_consecutive_rounds.py:
- **Predicted:** 40-60% of E→L companies had bridge rounds
- **Predicted:** Round count data available (60% probability)
- **Implication:** H3 (step-up) analysis needs censoring or additional controls

---

## Reporting to Advisors

When presenting these diagnostic findings, include:

1. **Tables:**
   - E/L classification comparison (narrow vs broad)
   - Transition matrices (baseline → endpoint)
   - Round count distributions

2. **Key Metrics:**
   - N excluded by narrow definition
   - L rates by group
   - % with consecutive rounds
   - Median days between funding

3. **Methodological Decisions:**
   - Which E/L definition chosen and why
   - How bridge rounds handled in H3 analysis
   - Robustness checks planned

4. **Limitations Acknowledged:**
   - Companies may have had funding before entering PitchBook
   - "LastFinancing" only shows most recent, not full history
   - Timing based on deal dates, not actual cash-in-bank dates

---

## Notes

- Both scripts auto-detect pipe (`|`) or tab (`\t`) delimiters
- Runtime: ~30-60 seconds per script on 400k+ companies
- Memory usage: ~2GB for full dataset
- Compatible with Python 3.8+
- No external dependencies beyond pandas, numpy

---

**Last Updated:** 2025-11-12
**Author:** Claude (with human validation)
**Related:** See `modules/features.py` for production classification logic
