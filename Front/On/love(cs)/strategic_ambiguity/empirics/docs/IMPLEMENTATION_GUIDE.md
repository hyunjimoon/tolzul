# Implementation Guide: Set B → Minimal Thesis Pipeline

**Prepared for**: 권준/나대용 (中軍) → Scott Stern & Charlie Fine
**Date**: 2025-11-16
**Status**: Ready for thesis submission

---

## 1. Sector FE Simplification: 7 Sectors → Binary HW/SW

### Current (Set B): 7 Sectors
```python
# modules/features.py lines 1228-1253
def extract_sector_fe(keywords: pd.Series) -> pd.Series:
    """
    Biotech/Healthcare
    Hardware/Robotics
    AI/ML Software
    FinTech
    Data/Analytics
    Enterprise Software
    Consumer Software
    """
```

### Simplified (Recommended for Thesis): Binary HW/SW

**Mapping logic:**

| Original Sector | → | Binary Category | Rationale |
|----------------|---|-----------------|-----------|
| **Hardware/Robotics** | → | **HW (1)** | Physical products, high integration cost |
| **Biotech/Healthcare** | → | **HW (1)** | Lab equipment, clinical trials, FDA approval |
| **AI/ML Software** | → | **SW (0)** | Algorithms, cloud deployment |
| **FinTech** | → | **SW (0)** | APIs, payment processing |
| **Data/Analytics** | → | **SW (0)** | Software platforms |
| **Enterprise Software** | → | **SW (0)** | SaaS, B2B tools |
| **Consumer Software** | → | **SW (0)** | Apps, gaming, social |

### Implementation

```python
def extract_sector_binary(keywords: pd.Series) -> pd.Series:
    """
    Simplified binary sector classification for thesis.

    Returns:
        1 = Hardware/Integrated (Biotech, Hardware/Robotics)
        0 = Software/Non-integrated (all others)
    """
    def classify_hw_sw(keyword_str):
        if pd.isna(keyword_str):
            return 0  # Default to software

        kw = str(keyword_str).lower()

        # Hardware indicators (high integration cost)
        hw_keywords = [
            'biotech', 'pharma', 'drug', 'health', 'medical', 'therapeutics',
            'hardware', 'robotics', 'robot', 'chip', 'semiconductor',
            'sensor', 'device', 'manufacturing', 'asic', 'fpga'
        ]

        # If ANY hardware keyword matches → HW (1)
        if any(hw_kw in kw for hw_kw in hw_keywords):
            return 1

        # Otherwise → SW (0)
        return 0

    return keywords.apply(classify_hw_sw)
```

**Usage in H1:**
```python
# OLD (7 sectors):
"early_funding_musd ~ z_vagueness + z_employees_log + C(sector_fe) + C(founding_cohort)"

# NEW (binary HW/SW):
"early_funding_musd ~ z_vagueness + z_employees_log + is_hardware + C(founding_cohort)"
# OR omit entirely (use is_hardware from moderator analysis)
```

**Benefits:**
- ✅ Simpler interpretation (2 categories vs 7)
- ✅ Aligns with H2 moderator (is_hardware)
- ✅ Reduces risk of small cell sizes in sectors
- ✅ Clearer theoretical story (integration cost)

---

## 2. StrategicVaguenessScorerV2 (If Exists)

**STATUS**: Not found in repository.

**Options:**

### A. If you have V2 locally:
```bash
# Copy from your local machine to repo
cp /Users/hyunjimoon/path/to/StrategicVaguenessScorerV2.py \
   empirics_ent_strat_ops/modules/vagueness_v2.py
```

### B. If V2 doesn't exist yet:
Use existing `StrategicVaguenessScorer` (it's already solid with 3 academic components)

### C. Proposed V2 improvements (if needed):
```python
class StrategicVaguenessScorerV2:
    """
    Enhanced version with:
    1. Weighted components (tunable)
    2. Domain-specific dictionaries (VC vs general)
    3. Normalization options (z-score vs 0-100 scale)
    """
    def __init__(self, weights=(0.4, 0.3, 0.3)):
        # weights = (uncertainty, concreteness, categorical)
        self.w_uncertainty = weights[0]
        self.w_concreteness = weights[1]
        self.w_categorical = weights[2]
        # ... rest of implementation
```

**For now**: Proceed with V1 unless you confirm V2 exists.

---

## 3. HIGH Priority Extractions (Endorsed)

### Extract 1: StrategicVaguenessScorer

**From**: `modules/features.py` lines 837-941
**To**: Standalone function in `Empirics_Early/run.py` and `Empirics_Later/run.py`

```python
# Add to top of run.py
class StrategicVaguenessScorer:
    """Academic literature-based vagueness scorer (Lo&McD 2011; Pan 2018; Zuckerman 1999)"""

    def __init__(self):
        # Loughran & McDonald (2011, JF; 2016, JAR)
        self.lm_uncertainty = {
            'approximately', 'believe', 'could', 'depend', 'estimate', 'expect',
            'intend', 'may', 'might', 'possible', 'probable', 'risk', 'uncertain',
            'vary', 'anticipate', 'potential', 'project', 'forecast', 'seek',
            'contingent', 'future', 'unclear', 'unspecified'
        }

        # Pan et al. (2018, SMJ); Chen et al. (2015, JAR)
        self.concreteness_markers = {
            'temporal': r'\b(Q[1-4]\s*20\d{2}|20\d{2})\b',
            'quantitative_tech': r'\b(\d+[\.\d]*[xX%]?|[A-Z]{2,}\d*|\bL(evel)?\s*\d)\b',
            'acronym': r'\b[A-Z]{3,}\b'
        }

        # Hannan et al. (2007, ASQ); Zuckerman (1999, AJS)
        self.abstraction_keywords = {
            'platform', 'solution', 'ecosystem', 'technology', 'approach',
            'service', 'market', 'advanced', 'next-generation', 'sustainable',
            'cloud', 'AI', 'data', 'analytics', 'software', 'future'
        }

    def _tokenize(self, text):
        if not isinstance(text, str) or not text:
            return []
        return re.findall(r'\b\w+\b', text.lower())

    def calculate_lexical_uncertainty(self, description_words):
        """Cites: Loughran & McDonald (2011, JF; 2016, JAR)"""
        if not description_words:
            return 0.0
        uncertain_count = sum(1 for w in description_words if w in self.lm_uncertainty)
        uncertain_ratio = uncertain_count / len(description_words)
        return min(uncertain_ratio * 1000, 100)

    def calculate_concreteness_deficit(self, description_text, description_words):
        """Cites: Pan et al. (2018, SMJ); Chen et al. (2015, JAR)"""
        if not description_words:
            return 100.0

        specific_count = 0
        for pattern in self.concreteness_markers.values():
            if isinstance(description_text, str):
                specific_count += len(re.findall(pattern, description_text))

        specific_ratio = specific_count / len(description_words)
        precision_score = min(specific_ratio * 500, 100)
        return 100 - precision_score

    def calculate_categorical_vagueness(self, keyword_list):
        """Cites: Zuckerman (1999, AJS); Pontikes (2012, ASQ)"""
        if not keyword_list:
            return 100.0

        num_keywords = len(keyword_list)
        abstraction_count = sum(1 for w in keyword_list if w in self.abstraction_keywords)
        abstraction_ratio = abstraction_count / num_keywords
        uniqueness_ratio = len(set(keyword_list)) / num_keywords
        categorical_vagueness_ratio = (abstraction_ratio + uniqueness_ratio) / 2

        return categorical_vagueness_ratio * 100

    def score_vagueness(self, description, keywords):
        """Composite Vagueness score (0-100)"""
        description_words = self._tokenize(description)

        keyword_str = keywords if isinstance(keywords, str) else ""
        keyword_list = [k.strip() for k in keyword_str.lower().split(',')]
        keyword_list = [k for k in keyword_list if k]

        score_uncertainty = self.calculate_lexical_uncertainty(description_words)
        score_concreteness_deficit = self.calculate_concreteness_deficit(description, description_words)
        score_categorical = self.calculate_categorical_vagueness(keyword_list)

        composite_score = (score_uncertainty + score_concreteness_deficit + score_categorical) / 3

        return max(0, min(100, composite_score))

# Instantiate scorer
_SCORER = StrategicVaguenessScorer()

def compute_vagueness(df):
    """Apply vagueness scoring to dataframe"""
    return df.apply(
        lambda row: _SCORER.score_vagueness(row['description'], row['keywords']),
        axis=1
    )
```

### Extract 2: create_survival_seriesb_progression

**From**: `modules/features.py` lines 1001-1223
**To**: Standalone function (too long, import from modules recommended)

**Recommended approach**:
```python
# In Empirics_Later/run.py
import sys
sys.path.insert(0, '../../../../empirics_ent_strat_ops')
from modules.features import create_survival_seriesb_progression

# Use it
dv = create_survival_seriesb_progression(
    df_baseline, df_mid1, df_mid2, df_endpoint,
    baseline_date="2021-12-01",
    endpoint_date="2023-05-01"
)
```

**Why not copy**: 223 lines, complex logic, battle-tested

### Extract 3: Multi-stage Logit Fallback

**From**: `modules/models.py` lines 105-138
**To**: Wrapper function in `run.py`

```python
def fit_logit_robust(formula, data):
    """
    Fit logit with multi-stage fallback for convergence issues.

    Stage 1: Standard MLE
    Stage 2: L1 regularization (alpha=0.1)
    Stage 3: Stronger L1 (alpha=0.5)

    Returns: Fitted model
    """
    import statsmodels.formula.api as smf

    # Drop missing values
    d = data.dropna(subset=['growth', 'z_vagueness', 'is_hardware']).copy()

    # Stage 1: Standard fit
    try:
        print("  Stage 1: Attempting standard logit...")
        model = smf.logit(formula, data=d).fit(disp=False)
        print("  ✓ Standard fit successful")
        return model
    except Exception:
        print("  ✗ Failed, trying L1 regularization...")

    # Stage 2: L1 with alpha=0.1
    try:
        print("  Stage 2: L1 regularization (alpha=0.1)...")
        model = smf.logit(formula, data=d).fit_regularized(
            method='l1', alpha=0.1, disp=False, maxiter=200, warn_convergence=False
        )
        print("  ✓ L1 (alpha=0.1) successful")
        return model
    except Exception:
        print("  ✗ Failed, trying stronger regularization...")

    # Stage 3: L1 with alpha=0.5
    try:
        print("  Stage 3: L1 regularization (alpha=0.5)...")
        model = smf.logit(formula, data=d).fit_regularized(
            method='l1', alpha=0.5, disp=False, maxiter=200, warn_convergence=False
        )
        print("  ✓ L1 (alpha=0.5) successful")
        return model
    except Exception:
        raise RuntimeError("All logit convergence strategies failed")

# Usage
h2_formula = "growth ~ z_vagueness * is_hardware + z_employees_log + C(founding_cohort)"
h2_model = fit_logit_robust(h2_formula, analysis_df)
```

### Extract 4: Parquet Caching

**From**: `archive/run_analysis.py` lines 46-72
**To**: Helper function in `run.py`

```python
def read_dat_cached(path):
    """Read .dat file with parquet caching (10-50x speedup)"""
    from pathlib import Path
    import pandas as pd

    path = Path(path)
    parquet_path = path.with_suffix('.parquet')

    # Use cache if newer than source
    if parquet_path.exists() and parquet_path.stat().st_mtime > path.stat().st_mtime:
        print(f"  ✓ Loading from cache: {parquet_path.name}")
        return pd.read_parquet(parquet_path)

    # Read .dat and cache
    print(f"  ⏳ Reading .dat file: {path.name}")
    df = pd.read_csv(path, sep='|', encoding='utf-8', low_memory=False)

    print(f"  💾 Caching to: {parquet_path.name}")
    df.to_parquet(parquet_path, index=False, compression='snappy')

    return df

# Usage
df = read_dat_cached('../../1️⃣_INPUT/data/Company20220101.dat')
```

---

## 4. Prepare for Advisors (Scott Stern & Charlie Fine)

### A. Review H1 Results

**File**: `outputs/h1_coefficients.csv`

**What to check:**
```python
import pandas as pd

h1 = pd.read_csv('outputs/h1_coefficients.csv')

# Key coefficient: z_vagueness
vagueness_row = h1[h1['variable'].str.contains('vagueness', case=False)]

print("H1: Early Funding ~ Vagueness")
print("="*60)
print(f"Coefficient (z_vagueness): {vagueness_row['coefficient'].values[0]:.4f}")
print(f"Std Error: {vagueness_row['std_err'].values[0]:.4f}")
print(f"P-value: {vagueness_row['p_value'].values[0]:.4f}")
print(f"95% CI: [{vagueness_row['ci_lower'].values[0]:.4f}, {vagueness_row['ci_upper'].values[0]:.4f}]")

# Interpretation
if vagueness_row['coefficient'].values[0] < 0 and vagueness_row['p_value'].values[0] < 0.05:
    print("\n✅ H1 SUPPORTED: Vagueness reduces early funding (p < 0.05)")
elif vagueness_row['coefficient'].values[0] < 0:
    print(f"\n⚠️ H1 DIRECTION CORRECT but not significant (p = {vagueness_row['p_value'].values[0]:.3f})")
else:
    print("\n❌ H1 NOT SUPPORTED: Vagueness has positive/null effect")
```

**For presentation slides:**
- Copy coefficient, SE, p-value
- Note control variables included (employees, sector, cohort)
- Sample size (check `nobs` from model summary)

### B. Review H2 Results

**File**: `outputs/h2_main_coefficients.csv`

**What to check:**
```python
h2 = pd.read_csv('outputs/h2_main_coefficients.csv')

# Main effect
vagueness_main = h2[h2['variable'] == 'z_vagueness']

# Interaction effect
interaction = h2[h2['variable'].str.contains('vagueness.*hardware|hardware.*vagueness', case=False, regex=True)]

print("H2: Growth ~ Vagueness × Hardware")
print("="*60)
print("\nMain Effect (z_vagueness):")
print(f"  Coefficient: {vagueness_main['coefficient'].values[0]:.4f}")
print(f"  P-value: {vagueness_main['p_value'].values[0]:.4f}")

print("\nInteraction (z_vagueness:is_hardware):")
print(f"  Coefficient: {interaction['coefficient'].values[0]:.4f}")
print(f"  P-value: {interaction['p_value'].values[0]:.4f}")

# Interpretation
print("\n📊 Interpretation:")
print(f"  Software firms (HW=0): Vagueness effect = {vagueness_main['coefficient'].values[0]:.4f}")
print(f"  Hardware firms (HW=1): Vagueness effect = {vagueness_main['coefficient'].values[0] + interaction['coefficient'].values[0]:.4f}")

if interaction['p_value'].values[0] < 0.05:
    print("\n✅ H2 SUPPORTED: Significant moderation by integration cost (p < 0.05)")
else:
    print(f"\n⚠️ H2 NOT SUPPORTED: Interaction not significant (p = {interaction['p_value'].values[0]:.3f})")
```

**For presentation:**
- Report both main effect and interaction
- Calculate conditional effects (SW vs HW)
- Note: "NO early_funding control" (mediator, not confounder)

### C. Check Figures for Presentation

**Files**: `outputs/figures/*.png`

**Expected figures:**
1. **The Reversal** (`reversal_plot.png`):
   - Panel A: H1 (Early Funding ~ Vagueness) - expect negative slope
   - Panel B: H2 (Growth ~ Vagueness) - expect positive slope

2. **Interaction Plot** (`h2_interaction_is_hardware.png`):
   - Software line (blue, solid) - steep positive slope
   - Hardware line (gray, dashed) - flat/negative slope
   - Lines should diverge (scissors pattern)

3. **Founder Interactions** (`h3_*.png`, `h4_*.png`):
   - Similar format to H2 interaction
   - Serial vs Non-serial founder slopes

**Quality checklist:**
- [ ] 300 DPI resolution (suitable for print)
- [ ] Axes labeled clearly
- [ ] Legend present and readable
- [ ] No overlap between lines and text
- [ ] Color scheme is colorblind-friendly

**If figures missing**, run:
```bash
python archive/run_analysis.py --output outputs/
```

---

## 5. Quick Test Script

Create `test_thesis_pipeline.py`:

```python
#!/usr/bin/env python3
"""Quick test to verify thesis pipeline works"""

import sys
from pathlib import Path
import pandas as pd

# Add modules to path
sys.path.insert(0, str(Path(__file__).parent))

from modules.features import engineer_features, preprocess_for_h2
from modules.models import test_h1_early_funding, test_h2_main_growth

print("="*80)
print("THESIS PIPELINE TEST")
print("="*80)

# Test 1: Load sample data
print("\n1. Loading data...")
try:
    df = pd.read_csv('data/processed/analysis_panel.csv', nrows=1000)
    print(f"   ✓ Loaded {len(df)} rows")
except Exception as e:
    print(f"   ❌ Failed: {e}")
    sys.exit(1)

# Test 2: Feature engineering
print("\n2. Feature engineering...")
try:
    df = engineer_features(df)
    df = preprocess_for_h2(df)
    print(f"   ✓ Engineered {len(df.columns)} features")
except Exception as e:
    print(f"   ❌ Failed: {e}")
    sys.exit(1)

# Test 3: H1 model
print("\n3. Testing H1 model...")
try:
    h1_df = df[df['early_funding_musd'].notna()].head(500)
    h1_res = test_h1_early_funding(h1_df)
    print(f"   ✓ H1 converged (n={h1_res.nobs})")
except Exception as e:
    print(f"   ❌ Failed: {e}")
    sys.exit(1)

# Test 4: H2 model
print("\n4. Testing H2 model...")
try:
    h2_df = df[df['growth'].notna()].head(500)
    h2_res = test_h2_main_growth(h2_df)
    print(f"   ✓ H2 converged (n={h2_res.nobs})")
except Exception as e:
    print(f"   ❌ Failed: {e}")
    sys.exit(1)

print("\n" + "="*80)
print("✅ ALL TESTS PASSED - Ready for thesis submission")
print("="*80)
```

Run with:
```bash
python test_thesis_pipeline.py
```

---

## 6. Final Checklist for Advisors

### Before meeting with Scott Stern & Charlie Fine:

**Data Quality:**
- [ ] Vagueness score has std > 10 (not constant)
- [ ] Growth rate between 8-20% (Series B+ progression)
- [ ] Sample size > 10,000 for H2 (adequate power)
- [ ] No missing values in key variables (z_vagueness, is_hardware, growth)

**Model Convergence:**
- [ ] H1 converged successfully (OLS always works)
- [ ] H2 converged (check for L1 regularization warnings)
- [ ] Interaction terms present in output
- [ ] No perfect separation warnings

**Results Interpretation:**
- [ ] H1 coefficient direction matches theory (expect negative)
- [ ] H2 main effect direction clear
- [ ] H2 interaction significant (or have explanation if null)
- [ ] Marginal effects calculated (software vs hardware slopes)

**Figures:**
- [ ] Reversal plot shows clear pattern
- [ ] Interaction plot shows diverging lines
- [ ] All figures exported at 300 DPI
- [ ] Figures in both PNG (slides) and PDF (paper) format

**Documentation:**
- [ ] Can explain vagueness scoring (3 components, academic citations)
- [ ] Can defend "NO early_funding in H2" (mediator argument)
- [ ] Can explain 4-snapshot DV construction (LLM2 approach)
- [ ] Know sample sizes for each hypothesis

---

**Questions? Next Steps?**

1. **StrategicVaguenessScorerV2**: Confirm if you have this locally or if we should use V1
2. **Run test**: Execute `python archive/run_analysis.py --output test_outputs/` to verify everything works
3. **Review outputs**: Check `test_outputs/*.csv` and `test_outputs/figures/*.png`

Let me know if you need help with any of these steps! 🚀
