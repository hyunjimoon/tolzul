# Experiments Directory

Tools for testing and improving the vagueness scoring pipeline.

## 🚨 Problem Identified

The current pipeline uses **V1 vagueness scorer** which produces:
```
25%:  50.0000
50%:  50.0000
75%:  50.0000  ← 75% of companies have EXACTLY this score!
```

This **severely limits statistical power** for H1/H2 models.

## 🔬 Experiment Scripts

### 1. `test_vagueness_variants.py`

Tests 6 different scoring approaches to find which has best variance:

**Variants tested:**
1. **V1 (Current)** - Old 3-component scorer → Too concentrated at 50.0
2. **V2 Standard** - 2-component with IDF weighting → Better variance
3. **V2 No IDF** - Same but without IDF → Simpler, still better than V1
4. **V2 MinMax** - Uses min-max normalization → Full 0-100 range
5. **Concrete Features** - Counts numbers/dates/metrics → Good spread
6. **Hybrid** - 50% V2 + 50% Concrete → Best of both worlds

**Metrics evaluated:**
- **IQR** (Interquartile Range) - Higher = more spread
- **CV** (Coefficient of Variation) - Higher = more relative variance
- **Spike @50%** - Lower = less concentration at midpoint

**Usage:**
```bash
python3 experiments/test_vagueness_variants.py
```

**Outputs:**
- `experiments/outputs/vagueness_distributions_comparison.png` - Visual comparison
- `experiments/outputs/vagueness_variants_sample.csv` - Score samples for each variant
- `experiments/outputs/vagueness_variants_stats.csv` - Summary statistics

### 2. `switch_to_v2_scorer.py`

Automatically updates `src/features.py` to use V2 scorer instead of V1.

**What it does:**
1. Adds `from vagueness_v2 import StrategicVaguenessScorerV2` import
2. Replaces `_SCORER = StrategicVaguenessScorer()` with V2 instance
3. Updates `compute_vagueness_vectorized()` to use V2 API
4. Creates backup of original file

**Usage:**
```bash
python3 experiments/switch_to_v2_scorer.py
```

**After switching:**
```bash
# Re-run feature engineering with V2
rm data/processed/features_all.parquet
python3 pipeline/02_engineer_features.py

# Continue pipeline
python3 pipeline/03_filter_datasets.py
python3 pipeline/04_run_models.py all
```

**To restore V1:**
```bash
mv src/features.py.backup src/features.py
```

## 📊 Expected Results

**V1 (Current):**
```
Mean: 48.72, Std: 6.12, IQR: 0.00, Spike@50: 75%
```

**V2 Standard (Expected):**
```
Mean: 45-55, Std: 15-25, IQR: 20-35, Spike@50: <10%
```

**Why This Matters:**

With V1's concentration at 50.0:
- ❌ Most companies look identical (no differentiation)
- ❌ Weak correlations with outcomes (low statistical power)
- ❌ Non-significant p-values even if real effect exists

With better variance:
- ✅ Clear differentiation between vague vs. concrete companies
- ✅ Stronger correlations detectable
- ✅ Significant effects can emerge

## 🎯 Recommended Action

1. **Test variants first:**
   ```bash
   python3 experiments/test_vagueness_variants.py
   ```

2. **Review the comparison table** - Pick variant with:
   - Highest IQR (spread)
   - Highest CV (relative variance)
   - Lowest Spike@50 (less concentration)

3. **If V2 is best, switch to it:**
   ```bash
   python3 experiments/switch_to_v2_scorer.py
   ```

4. **Re-run pipeline:**
   ```bash
   ./run_all.sh
   ```

5. **Compare H1/H2 results** - Check if:
   - p-values improve
   - Effect sizes become clearer
   - Model fit improves (R², Pseudo-R²)

## 🔍 Root Cause

The issue is in `src/features.py` line 1034:
```python
_SCORER = StrategicVaguenessScorer()  # ← OLD V1 SCORER
```

Should be:
```python
_SCORER_V2 = StrategicVaguenessScorerV2(use_idf=True, random_state=42)  # ← NEW V2
```

The V2 implementation exists in `src/vagueness_v2.py` but was never integrated into the pipeline!

## 📈 Next Steps

After switching to best variant:

1. **Re-run full pipeline** for all 3 datasets
2. **Check vagueness distribution** in Step 2 logs:
   - Should see IQR > 20 (not 0)
   - Should see Std > 15 (not 6)
   - Should see <10% at median (not 75%)

3. **Compare H1/H2 results**:
   - Check if p-values drop below 0.05
   - Check if coefficients are larger
   - Check if interaction effects are clearer

4. **Document which variant was chosen** and why
