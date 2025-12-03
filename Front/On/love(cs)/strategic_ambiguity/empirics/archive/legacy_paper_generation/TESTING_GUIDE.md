# Paper Generation Pipeline - Testing Guide

## Quick Test Summary

✅ **All 8 sections generate successfully**
- Total output: ~87KB across 10 files
- Execution time: ~5 seconds
- Dependencies: pandas, matplotlib, seaborn

## Prerequisites

### 1. Install Dependencies

```bash
pip install pandas matplotlib seaborn
```

### 2. Verify Data Files Exist

```bash
ls -lh outputs/all/models/h1_coefficients.csv
ls -lh outputs/all/models/h2_main_coefficients.csv
```

Expected output:
```
-rw-r--r-- 1 user user 1.2K h1_coefficients.csv
-rw-r--r-- 1 user user 2.4K h2_main_coefficients.csv
```

## Test Methods

### Test 1: Generate All Sections (Recommended)

```bash
cd src/scripts/paper_generation
python generate_all.py
```

**Expected Output:**
```
✅ Successfully generated: 8/8 sections

Generated files:
   ✓ 01_Introduction.md
   ✓ 02_LiteratureReview.md
   ✓ 03_Conceptual_Model.md
   ✓ 04_Method.md
   ✓ 05_Results.md
   ✓ 06_Discussion.md
   ✓ 07_Poster.svg + 07_Poster.md
   ✓ 08_IndustryComparison.md
```

**Expected Files:**
```bash
ls -lh output/

# Should show:
# 01_Introduction.md         (3.8K)
# 02_LiteratureReview.md     (6.2K)
# 03_Conceptual_Model.md     (7.5K)
# 04_Method.md               (11K)
# 05_Results.md              (15K)
# 06_Discussion.md           (15K)
# 07_Poster.md               (2.5K)
# 07_Poster.svg              (18K)
# 08_IndustryComparison.md   (8.2K)
# spec_curve_analysis.png    (358K)
```

### Test 2: Generate Specific Sections

```bash
# Test Introduction only
python generate_all.py --sections 1

# Test Results and Discussion
python generate_all.py --sections 5 6

# Test Poster only
python generate_all.py --sections 7

# Test Industry Comparison only
python generate_all.py --sections 8
```

### Test 3: Generate Individual Sections

```bash
python generate_01_intro.py
python generate_02_litreview.py
python generate_03_conceptual.py
python generate_04_method.py
python generate_05_results.py
python generate_06_discussion.py
python generate_07_poster.py
python generate_08_industry_comparison.py
```

### Test 4: Verify Output Quality

```bash
# Check file sizes (should be non-zero)
wc -l output/*.md

# Preview Introduction
head -50 output/01_Introduction.md

# Preview Results with statistics
grep -A 5 "coefficient" output/05_Results.md

# View poster in browser
open output/07_Poster.svg  # macOS
xdg-open output/07_Poster.svg  # Linux
start output/07_Poster.svg  # Windows
```

### Test 5: Verify Data Binding

Check that actual CSV numbers appear in output:

```bash
# Extract vagueness coefficient from H1 results
grep "z_vagueness" outputs/all/models/h1_coefficients.csv

# Verify it appears in Introduction
grep -i "vagueness" output/01_Introduction.md | grep -E "\-?[0-9]+\.[0-9]+e-[0-9]+"

# Extract interaction coefficient from H2 results
grep "z_vagueness:is_hardware" outputs/all/models/h2_main_coefficients.csv

# Verify it appears in Results
grep "z_vagueness:is_hardware" output/05_Results.md
```

**Expected:** Numbers should match exactly between CSV and markdown files.

## Common Issues & Solutions

### Issue 1: `ModuleNotFoundError: No module named 'pandas'`

**Solution:**
```bash
pip install pandas matplotlib seaborn
```

### Issue 2: `FileNotFoundError: h1_coefficients.csv`

**Cause:** Analysis pipeline hasn't been run yet.

**Solution:**
```bash
# From project root
python -m src.cli load-data
python -m src.cli engineer-features
python -m src.cli filter-datasets
python -m src.cli run-models --dataset all
```

### Issue 3: Empty or Missing Output Files

**Diagnosis:**
```bash
ls -lh output/
cat output/01_Introduction.md
```

**Solution:** Re-run specific section:
```bash
python generate_01_intro.py
```

### Issue 4: Poster SVG Not Rendering

**Cause:** Some text editors don't support SVG preview.

**Solution:** Open in web browser:
```bash
# Create simple HTML wrapper
echo '<html><body><img src="07_Poster.svg" width="100%"></body></html>' > output/poster.html
open output/poster.html
```

### Issue 5: Section 8 Shows No Industry Data

**Cause:** PR #13 hasn't been merged yet, so industry-specific data doesn't exist.

**Current Behavior:** Section 8 generates with placeholder structure but no actual industry comparison data.

**Solution:** Wait for PR #13 merge, then run:
```bash
bash integrate_pr13.sh
python generate_all.py --sections 8
```

## Performance Benchmarks

| Test | Sections | Time | Output Size |
|------|----------|------|-------------|
| Full pipeline | 1-8 | ~5s | 87KB |
| Introduction only | 1 | <1s | 3.8KB |
| Results only | 5 | ~2s | 15KB + 358KB PNG |
| Poster only | 7 | <1s | 20KB (SVG+MD) |
| Industry comparison | 8 | <1s | 8.2KB |

## Validation Checklist

After running the pipeline, verify:

- [ ] All 8 sections generated without errors
- [ ] All output files have non-zero size
- [ ] Numbers in markdown match CSV source files
- [ ] Poster SVG renders in browser
- [ ] spec_curve_analysis.png created (Section 5)
- [ ] No Python tracebacks in console output
- [ ] Output directory contains 10 files total

## Advanced Testing

### Test Data Consistency

```python
import pandas as pd

# Load source data
h1 = pd.read_csv("outputs/all/models/h1_coefficients.csv", index_col=0)
h2 = pd.read_csv("outputs/all/models/h2_main_coefficients.csv", index_col=0)

# Extract key coefficients
vagueness_coef = h1.loc['z_vagueness', 'coef']
interaction_coef = h2.loc['z_vagueness:is_hardware', 'coef']

print(f"H1 Vagueness: {vagueness_coef:.3e}")
print(f"H2 Interaction: {interaction_coef:.3f}")

# Now verify these appear in markdown files
# (Use grep or manual inspection)
```

### Test META_PROMPT Extraction

```bash
# Each generator script contains a META_PROMPT
# Extract and review for LLM expansion

grep -A 50 "META_PROMPT" generate_01_intro.py
grep -A 50 "META_PROMPT" generate_05_results.py
```

### Test Pipeline Integration

```bash
# Full analysis → paper generation workflow
cd /home/user/empirics_ent_strat_ops

# Step 1: Run analysis (if needed)
python -m src.cli run-models --dataset all

# Step 2: Generate paper
cd src/scripts/paper_generation
python generate_all.py

# Step 3: Verify outputs
ls -lh output/
```

## Continuous Testing

To test after making changes:

```bash
# Clean output directory
rm -rf output/*.md output/*.svg output/*.png

# Regenerate all
python generate_all.py

# Diff with expected output (if you have baseline)
diff output/01_Introduction.md baseline/01_Introduction.md
```

## Test Coverage

| Component | Test Coverage |
|-----------|---------------|
| Data loading | ✅ CSV files read correctly |
| Data binding | ✅ Numbers inserted accurately |
| File generation | ✅ All 10 files created |
| Error handling | ✅ Missing dependencies caught |
| File size validation | ✅ Non-zero outputs verified |
| Visual output | ✅ SVG renders in browser |
| Documentation | ✅ META_PROMPT included |

## Success Criteria

**Pipeline is working correctly if:**

1. ✅ No Python errors during execution
2. ✅ All 8 sections report "✅ Generated"
3. ✅ Output directory contains 10 files
4. ✅ Total output size: ~87KB (±20%)
5. ✅ Coefficient values match CSV sources
6. ✅ Poster SVG opens in browser
7. ✅ Execution completes in <10 seconds

## Next Steps After Testing

1. **Review Content**: Open each markdown file and review quality
2. **Expand Sections**: Use META_PROMPT to expand with LLM
3. **Verify Numbers**: Double-check statistics match analysis
4. **View Poster**: Open SVG in browser for visual summary
5. **Integrate PR #13**: Follow `PR13_INTEGRATION_GUIDE.md`

## Getting Help

If tests fail:

1. Check this guide's "Common Issues" section
2. Review `README.md` for setup instructions
3. Inspect error messages for missing dependencies
4. Verify data files exist in `outputs/all/models/`
5. Check git status for uncommitted changes
