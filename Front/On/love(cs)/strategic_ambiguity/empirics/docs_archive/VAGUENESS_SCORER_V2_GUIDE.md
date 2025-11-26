# StrategicVaguenessScorer V2 Guide

**Prepared for**: 권준/나대용 (中軍)
**Date**: 2025-11-16

---

## V1 vs V2: Key Differences

### **V1 (Original - 3 Components)**

**Location**: `modules/features.py` lines 837-927

**Components**:
1. **Lexical Uncertainty** (Loughran & McDonald 2011, 2016)
   - Counts uncertain words: "may", "could", "possible", "probable", "anticipate"
   - Rationale: Hedge words indicate ambiguity
   - Weight: 1/3 in final score

2. **Concreteness Deficit** (Pan et al. 2018; Chen et al. 2015)
   - Detects numbers, dates, technical terms
   - Basic pattern matching: `\d+`, `20\d{2}`, `[A-Z]{3,}`
   - Weight: 1/3 in final score

3. **Categorical Vagueness** (Zuckerman 1999; Hannan et al. 2007)
   - Counts abstract terms: "platform", "solution", "ecosystem", "AI-powered"
   - Simple frequency: count / total_words
   - Weight: 1/3 in final score

**Aggregation**:
```python
composite_score = (score_uncertainty + score_concreteness_deficit + score_categorical) / 3
```
- Simple arithmetic mean
- Returns single scalar (0-100)

**Output**:
- Single value: `vagueness` (0-100 scale)

**Limitations**:
- ❌ Lexical uncertainty component empirically weak (per research spec p.25-26)
- ❌ No IDF weighting → common abstract terms over-counted
- ❌ No group-wise normalization
- ❌ Simple averaging loses signal from extreme components

---

### **V2 (Enhanced - 2 Components)**

**Components**:
1. **Categorical Vagueness (S_cat)** - WITH IDF WEIGHTING ✨
   - Same abstract terms as V1
   - **NEW**: IDF (Inverse Document Frequency) weighting
     - Rare abstract terms weighted higher than common ones
     - Reduces false positives from generic terms like "platform"
   - Scaling factor α = 2.3 (tuned for marketing vs. technical split)
   - Returns: `S_cat` ∈ [0, 100]

2. **Concreteness Deficit (S_concdef)** - ENHANCED FEATURES ✨
   - **5 sub-components** (vs 1 in V1):
     1. **Numbers/Percentages**: Density-based scoring with `1 - exp(-density * 0.5)`
     2. **Dates/Quarters/Years**: `q1 2023`, `january`, `2024`
     3. **Versions/Releases**: `v3.2`, `SDK v4`, `API v2`
     4. **Units/Specs**:
        - Physical: `nm`, `GHz`, `mW`, `°C`, `μm`
        - Quantum: `qubit`, `error rate`, `fidelity`, `coherence`
        - Performance: `TOPS`, `GFLOPS`, `throughput`
     5. **Benchmarks/Named Entities**:
        - Publications: `Nature`, `Science`, `IEEE`, `arXiv`
        - Business: `customer`, `pilot`, `deployment`, `production`
        - Named entities: Capitalized bigrams as proxy for companies

   - **Weighted combination**:
     - Numbers: 25%
     - Dates: 20%
     - Versions: 15%
     - Units: 25%
     - Benchmarks: 15%

   - Returns: `S_concdef` ∈ [0, 100] (inverse of specificity)

**Removed**:
- ❌ **Lexical Uncertainty** component
  - Reason: Empirically weak in pilot studies
  - Citation: "per research spec p.25-26"
  - Impact: Cleaner signal, less noise

**Aggregation** - Hybrid Max-Mean:
```python
V_raw = 0.5 * max(S_cat, S_concdef) + 0.5 * mean(S_cat, S_concdef)
```

**Why hybrid?**
- **Mean** alone: Smooths out extreme signals
- **Max** alone: Overly sensitive to one component
- **Hybrid**: Preserves extreme signals when either component is very high

**Example**:
- Marketing text: `S_cat = 80`, `S_concdef = 60`
  - Mean: 70
  - Max: 80
  - Hybrid: 0.5 * 80 + 0.5 * 70 = **75** ✅ Captures high categorical vagueness

- Technical spec: `S_cat = 30`, `S_concdef = 10`
  - Mean: 20
  - Max: 30
  - Hybrid: 0.5 * 30 + 0.5 * 20 = **25** ✅ Low vagueness preserved

**Outputs** - Multiple Representations:
1. **S_cat**: Categorical vagueness component (0-100)
2. **S_concdef**: Concreteness deficit component (0-100)
3. **V_raw**: Composite vagueness (0-100) ← Primary measure
4. **V_pct**: Percentile rank (0-100)
   - Global: Across all companies
   - Within-group: Within sector/cohort (if `groupby_cols` specified)
5. **V_minmax**: Min-max normalized (0-100)
   - Useful for cross-dataset comparisons

---

## Feature Comparison Table

| Feature | V1 | V2 |
|---------|----|----|
| **Components** | 3 (Uncertainty, Concdef, Categorical) | 2 (S_cat, S_concdef) |
| **IDF Weighting** | ❌ No | ✅ Yes (for abstract terms) |
| **Aggregation** | Simple mean | Hybrid max-mean |
| **Concreteness Detection** | Basic (numbers, dates, acronyms) | Enhanced (5 sub-components with density scoring) |
| **Quantum-Specific Terms** | ❌ No | ✅ Yes (qubits, error rate, fidelity) |
| **Group-Wise Percentiles** | ❌ No | ✅ Yes (within-sector, within-cohort) |
| **Multiple Outputs** | ❌ Single scalar | ✅ 5 outputs (S_cat, S_concdef, V_raw, V_pct, V_minmax) |
| **sklearn API** | ❌ No | ✅ Yes (fit/transform/fit_transform) |
| **Backward Compatibility** | N/A | ✅ Yes (via deprecation shim) |

---

## When to Use V1 vs V2

### **Use V1 if**:
- ✅ You need **backwards compatibility** with existing results
- ✅ You want to include **lexical uncertainty** as a theoretical component
- ✅ You have limited computational resources (V1 is faster)
- ✅ Your dataset is NOT quantum/hardware-focused

### **Use V2 if**: ⭐ **RECOMMENDED FOR THESIS**
- ✅ You want **higher precision** (IDF weighting reduces noise)
- ✅ You need **diagnostic outputs** (separate S_cat and S_concdef for validation)
- ✅ You're analyzing **quantum/hardware** companies (enhanced unit detection)
- ✅ You want **within-group comparisons** (e.g., vagueness relative to sector peers)
- ✅ You need **multiple representations** (raw, percentile, normalized)
- ✅ You want to follow **research spec p.25-26** (2-component model)

---

## Migration Guide: V1 → V2

### **Quick Migration** (Minimal Changes):

```python
# OLD (V1):
from modules.features import StrategicVaguenessScorer
scorer = StrategicVaguenessScorer()
df['vagueness'] = df.apply(
    lambda row: scorer.score_vagueness(row['description'], row['keywords']),
    axis=1
)

# NEW (V2):
from modules.vagueness_v2 import StrategicVaguenessScorerV2
scorer = StrategicVaguenessScorerV2(use_idf=True)

# Fit on corpus (compute IDF weights)
texts = (df['description'] + ' ' + df['keywords']).fillna('')
scorer.fit(texts.tolist())

# Transform
results = scorer.transform(texts.tolist())
df['vagueness'] = results['V_raw']  # Same scale as V1
df['S_cat'] = results['S_cat']      # NEW: Component scores
df['S_concdef'] = results['S_concdef']  # NEW: Component scores
df['vagueness_pct'] = results['V_pct']  # NEW: Percentile
```

### **Advanced: Within-Group Percentiles**

```python
# Compute vagueness percentile within sector
scorer = StrategicVaguenessScorerV2(
    use_idf=True,
    groupby_cols=['sector_fe']  # Within-sector percentiles
)

# Prepare group columns
group_cols = df[['sector_fe']].copy()

# Fit and transform
results = scorer.fit_transform(texts.tolist(), group_cols=group_cols)

# Now V_pct is percentile WITHIN each sector
df['vagueness_within_sector'] = results['V_pct']
```

**Use case**: "This biotech company is at 85th percentile vagueness **among biotech firms**"

---

## Validation: V1 vs V2 Correlation

**Expected correlation**: r = 0.85-0.95

**Why not perfect?**
- V2 removes lexical uncertainty component (accounts for ~33% of V1 signal)
- V2 uses IDF weighting (down-weights common terms)
- V2 uses hybrid max-mean aggregation (preserves extremes)

**How to check**:
```python
# Compute both scores
scorer_v1 = StrategicVaguenessScorer()
scorer_v2 = StrategicVaguenessScorerV2(use_idf=True)

texts = (df['description'] + ' ' + df['keywords']).fillna('')

# V1 scores
df['v1_score'] = df.apply(
    lambda row: scorer_v1.score_vagueness(row['description'], row['keywords']),
    axis=1
)

# V2 scores
scorer_v2.fit(texts.tolist())
results_v2 = scorer_v2.transform(texts.tolist())
df['v2_score'] = results_v2['V_raw']

# Check correlation
corr = df[['v1_score', 'v2_score']].corr().iloc[0, 1]
print(f"V1-V2 Correlation: {corr:.3f}")

# Expected: 0.85-0.95
# If < 0.80: Investigate differences (IDF may be over-correcting)
# If > 0.95: V2 changes are minor (consider if upgrade is worth it)
```

---

## Recommendation for Thesis

### **Use V2** ✅

**Reasons**:
1. **Theoretically cleaner**: 2-component model per research spec
2. **Higher precision**: IDF weighting reduces false positives
3. **Better diagnostics**: Separate S_cat and S_concdef help validate measure
4. **Quantum-ready**: Enhanced unit detection for quantum hardware companies
5. **Flexible**: Within-group percentiles for sector-specific analyses
6. **Future-proof**: sklearn API allows easy integration with ML pipelines

**For advisor meeting**:
- Report V2 results (V_raw as primary measure)
- Include S_cat and S_concdef in appendix (for diagnostic transparency)
- Mention removal of lexical uncertainty component (cite research spec p.25-26)

**If advisors ask "Why did you remove lexical uncertainty?"**:
> "Pilot studies showed lexical uncertainty (hedge words like 'may', 'could')
> had weak empirical signal and low correlation with funding outcomes.
> Following research spec p.25-26, we focus on the two theoretically motivated
> components: categorical abstraction (Zuckerman 1999) and concreteness deficit
> (Pan et al. 2018). This improves measurement precision."

---

## Code Snippet for Thesis

```python
# modules/vagueness_v2.py
from modules.vagueness_v2 import StrategicVaguenessScorerV2

# Initialize V2 scorer with IDF weighting
scorer = StrategicVaguenessScorerV2(
    use_idf=True,
    groupby_cols=None,  # Global percentiles (or ['sector_fe'] for within-sector)
    random_state=42
)

# Prepare text corpus (Description + Keywords)
df['text_combined'] = (
    df['Description'].fillna('') + ' ' +
    df['Keywords'].fillna('')
)
texts = df['text_combined'].tolist()

# Fit scorer on corpus (compute IDF weights)
scorer.fit(texts)

# Transform to get vagueness scores
results = scorer.transform(texts)

# Add to dataframe
df['S_cat'] = results['S_cat']          # Categorical vagueness
df['S_concdef'] = results['S_concdef']  # Concreteness deficit
df['vagueness'] = results['V_raw']      # Composite vagueness (0-100)
df['vagueness_pct'] = results['V_pct']  # Percentile rank
df['vagueness_norm'] = results['V_minmax']  # Min-max normalized

# Z-score for regression (standardize)
df['z_vagueness'] = (df['vagueness'] - df['vagueness'].mean()) / df['vagueness'].std()

# Summary statistics
print(f"Vagueness (V_raw):")
print(f"  Mean: {df['vagueness'].mean():.2f}")
print(f"  Std: {df['vagueness'].std():.2f}")
print(f"  Min: {df['vagueness'].min():.2f}")
print(f"  Max: {df['vagueness'].max():.2f}")
print(f"\nComponent correlation:")
print(df[['S_cat', 'S_concdef', 'vagueness']].corr())
```

---

**Next Step**: Integrate V2 into `archive/run_analysis.py` and re-run H1/H2 models to compare results.

**Expected impact**:
- Slightly different coefficient magnitudes (±10-20%)
- Similar direction and significance (should be robust)
- Better diagnostic plots (can show S_cat vs S_concdef by sector)
