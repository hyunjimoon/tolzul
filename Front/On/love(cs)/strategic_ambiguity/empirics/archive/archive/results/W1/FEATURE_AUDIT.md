# Feature Audit: Message Delivery Utility Analysis

## Core Message
**"Which moderator—Architecture (is_hardware) or Credibility (is_serial)—should we choose for H2?"**

---

## Current Feature Inventory

### Variables (8 total)
1. `vagueness` (z_vagueness) - Independent variable
2. `is_hardware` - Architecture moderator (candidate)
3. `is_serial` - Credibility moderator (candidate)
4. `growth` - Dependent variable (H2)
5. `early_funding_musd` - Dependent variable (H1)
6. `z_employees_log` - Control
7. `founding_cohort` - Control (categorical)
8. `sector_fe` - Control (not in main models)

### Tables (9 total)
1. H1 coefficients (7 columns × N rows)
2. Architecture coefficients (7 columns × N rows)
3. Architecture metrics (9 metrics)
4. Architecture AME (3 effects)
5. Founder coefficients (7 columns × N rows)
6. Founder metrics (9 metrics)
7. Founder AME (3 effects)
8. Comparison matrix (11 rows × 3 columns)
9. Manifest validation table

### Figures (5 total)
1. Univariate distributions (6 subplots)
2. Moderator overlap - is_hardware (2 subplots)
3. Moderator overlap - is_serial (2 subplots)
4. Interaction plot - is_hardware (Wilson CI)
5. Interaction plot - is_serial (Wilson CI)

### Metrics (9 per model)
1. nobs
2. prsquared (Pseudo-R²)
3. aic
4. bic
5. llf
6. converged
7. auc
8. brier
9. logloss

---

## Message Delivery Utility Ranking

### **Priority 1: ESSENTIAL (Top 30% - KEEP)**

| Rank | Feature | Type | Utility Score | Rationale |
|------|---------|------|---------------|-----------|
| 1 | **Interaction plots** (2) | Figure | 100 | **Direct visualization of core hypothesis** |
| 2 | **Interaction coef + p-value** | Table cell | 95 | **Statistical evidence of moderation** |
| 3 | **Moderator balance (minority %)** | Table cell | 90 | **Data quality check - critical for validity** |
| 4 | **Pseudo-R²** | Metric | 85 | **Model fit - single best metric** |
| 5 | **H1 vagueness effect** | Table row | 80 | **Motivation: "Why explore moderation?"** |
| 6 | **Sample size (N)** | Metric | 75 | **Power/precision indicator** |

**TOTAL: 6 items (30% of ~20 total elements)**

---

### **Priority 2: IMPORTANT (Next 30% - CONSIDER)**

| Rank | Feature | Type | Utility Score | Rationale |
|------|---------|------|---------------|-----------|
| 7 | Main effect (z_vagueness) | Table row | 70 | Contextualizes interaction |
| 8 | Risk labels (🔴/🟡/🟢) | Visual | 65 | Quick data quality signal |
| 9 | AIC | Metric | 60 | Model comparison |
| 10 | Comparison matrix (compact) | Table | 55 | Side-by-side summary |
| 11 | Moderator effect (β₂) | Table row | 50 | Baseline difference |

---

### **Priority 3: SUPPORTING (Next 30% - OPTIONAL)**

| Rank | Feature | Type | Utility Score | Rationale |
|------|---------|------|---------------|-----------|
| 12 | Univariate distributions | Figure | 45 | Shows balance visually |
| 13 | Overlap plots (SMD/KS) | Figure | 40 | Positivity assumption |
| 14 | AME table | Table | 35 | Marginal effects |
| 15 | Control coefficients | Table rows | 30 | Transparency |
| 16 | CI bounds | Table columns | 25 | Precision |

---

### **Priority 4: DETAIL (Bottom 10% - CUT)**

| Rank | Feature | Type | Utility Score | Rationale |
|------|---------|------|---------------|-----------|
| 17 | Level-specific slopes | Table | 20 | Redundant with interaction |
| 18 | AUC, Brier, LogLoss | Metrics | 15 | Overkill for logit model |
| 19 | BIC, LLF | Metrics | 10 | Redundant with AIC |
| 20 | Converged flag | Metric | 5 | Assume convergence |
| 21 | Sector FE details | Variable | 5 | Not in main models |
| 22 | Founding cohort details | Variable | 5 | Control noise |
| 23 | Z-statistics | Table column | 3 | Redundant with p-value |
| 24 | Standard errors | Table column | 3 | Redundant with CI |
| 25 | Manifest table | Table | 1 | Meta - not substantive |

---

## Simplification Strategy (Top 30%)

### **KEEP (6 items)**
1. ✅ **2 Interaction plots** (is_hardware, is_serial) - with Wilson CI + N labels
2. ✅ **Compact coefficient table** - 3 rows only:
   - z_vagueness (main)
   - moderator (main)
   - interaction (z_vagueness × moderator)
3. ✅ **Balance + Risk table** - 2 columns:
   - Minority %
   - Risk label (🔴/🟡/🟢)
4. ✅ **Pseudo-R² + N** - 2 metrics only
5. ✅ **H1 effect (1 row)** - z_vagueness coefficient + p-value
6. ✅ **Decision matrix (compact)** - 4 rows × 2 columns:
   - Data Quality
   - Statistical Evidence
   - Model Fit
   - Verdict (human input)

### **CUT (19 items)**
- ❌ All AME tables
- ❌ AUC, Brier, LogLoss
- ❌ BIC, LLF, converged flag
- ❌ Overlap plots (SMD/KS)
- ❌ Univariate distributions (6 subplots)
- ❌ Full coefficient tables (controls)
- ❌ Manifest validation table
- ❌ CI bounds, SE, Z-stats (keep p-value only)
- ❌ Sector FE, founding cohort details

---

## Result: LEAN Report Structure

**Section 1: Core Question** (2 sentences)
- What moderator for H2?
- Why does it matter?

**Section 2: H1 Motivation** (1 table row + 1 sentence)
- Vagueness → Early Funding (α₁, p-value)
- "Now: does this help or hurt growth?"

**Section 3: Data Quality** (1 table: 2 rows × 3 columns)
- Architecture: Minority %, Risk, N
- Credibility: Minority %, Risk, N

**Section 4: Bake-off** (2 plots + 1 table)
- Plot 1: Architecture interaction
- Plot 2: Credibility interaction
- Table: Compact coefficients (3 rows × 4 columns)

**Section 5: Decision** (1 table: 4 rows × 2 columns)
- Data Quality: [score]
- Statistical Evidence: [interaction p-value]
- Model Fit: [Pseudo-R²]
- **Verdict**: [HUMAN INPUT]

**Total**: 2 plots + 3 tables + ~200 words

---

## Comparison

| Aspect | FULL Version | LEAN Version (30%) | Reduction |
|--------|--------------|-------------------|-----------|
| Figures | 5 (13 subplots) | 2 (2 subplots) | **-85%** |
| Tables | 9 (200+ cells) | 3 (30 cells) | **-85%** |
| Metrics per model | 9 | 2 | **-78%** |
| Variables shown | 8 | 4 | **-50%** |
| Report length | ~3000 words | ~500 words | **-83%** |

**Hemingway Ratio**: 17% retention (better than 10%!)
**Abdullah Ratio**: 30% features (better than 12.5%!)
