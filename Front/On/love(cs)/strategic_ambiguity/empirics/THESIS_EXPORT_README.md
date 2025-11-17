# Thesis Export Guide

## One-Touch Export to Production Folder

This script runs the full empirics pipeline and exports outputs to your thesis production folder structure.

### Quick Start

```bash
# Navigate to empirics directory
cd /Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics

# Activate your Python environment
source myenv/bin/activate  # or conda activate myenv

# Run one-touch export
./export_to_thesis.sh
```

### What It Does

1. **Runs full pipeline** (Steps 1-5):
   - Loads raw data
   - Engineers features (with Hybrid V2+Concrete vagueness scorer)
   - Filters datasets (all, quantum, transportation)
   - Runs H1/H2 models
   - Generates plots

2. **Generates thesis-specific figures**:
   - `fig1_tradeoff.pdf` - VOI vs RO conceptual diagram
   - `fig2_architecture.pdf` - Hardware vs Software illustration
   - `fig3_H1_scatter.pdf` - Vagueness vs Early Funding scatter

3. **Exports to production folder**:
   ```
   /Users/hyunjimoon/tolzul/Front/On/love(cs)/thesis/⚙️process/3️⃣_OUTPUT/
   ├── Theory/
   │   ├── fig1_tradeoff.pdf          ← Conceptual VOI/RO tradeoff
   │   └── fig2_architecture.pdf       ← HW vs SW architectures
   ├── Empirics_Early/
   │   ├── fig3_H1_scatter.pdf         ← E ~ V scatter plot
   │   └── table1_H1_regression.txt    ← H1 OLS coefficients
   └── Empirics_Later/
       ├── fig4_vxh_interaction.pdf    ← THE MONEY PLOT (scissors)
       └── table2_H2_logit.txt         ← H2 logit coefficients
   ```

### Options

```bash
# Quick mode (skip data loading, use cache)
./export_to_thesis.sh --quick

# Specific dataset only
./export_to_thesis.sh --dataset quantum
./export_to_thesis.sh --dataset transportation

# Both options
./export_to_thesis.sh --quick --dataset all
```

### Output Files

| Section | File | Description |
|---------|------|-------------|
| **Theory** | fig1_tradeoff.pdf | Conceptual diagram showing VOI vs RO tradeoff |
| | fig2_architecture.pdf | Hardware (Battleship) vs Software (Lego) |
| **Empirics_Early** | fig3_H1_scatter.pdf | Scatter plot: Vagueness vs Series A funding |
| | table1_H1_regression.txt | H1 OLS regression table (β₁ < 0 expected) |
| **Empirics_Later** | fig4_vxh_interaction.pdf | V×H interaction plot (scissors pattern) |
| | table2_H2_logit.txt | H2 logit regression table (β₃ < 0 expected) |

### Expected Runtime

- **Full run**: ~5-10 minutes (depends on data size)
- **Quick mode**: ~2-3 minutes (uses cached data)

### Troubleshooting

**Problem**: "ModuleNotFoundError: No module named 'pandas'"
- **Solution**: Activate your Python environment first:
  ```bash
  source myenv/bin/activate
  ```

**Problem**: "Directory not found" error
- **Solution**: Check paths in `export_to_thesis.sh` match your Mac directory structure
  - Empirics code: `/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics`
  - Thesis output: `/Users/hyunjimoon/tolzul/Front/On/love(cs)/thesis/⚙️process/3️⃣_OUTPUT`

**Problem**: Missing figures
- **Solution**: Run pipeline first without export:
  ```bash
  ./run_all.sh
  python3 thesis_figures.py
  ```

**Problem**: Vagueness scores have wrong distribution
- **Solution**: Check that you're using Hybrid scorer. Verify in logs:
  ```
  🔧 Fitting Hybrid vagueness scorer on corpus (one-time)...
  ✅ Hybrid scorer fitted (V2 + Concrete Features)
  ```

### Validation

After export, check that all files exist:

```bash
# List all exported files
find /Users/hyunjimoon/tolzul/Front/On/love\(cs\)/thesis/⚙️process/3️⃣_OUTPUT -type f

# Expected output (6 files):
# Theory/fig1_tradeoff.pdf
# Theory/fig2_architecture.pdf
# Empirics_Early/fig3_H1_scatter.pdf
# Empirics_Early/table1_H1_regression.txt
# Empirics_Later/fig4_vxh_interaction.pdf
# Empirics_Later/table2_H2_logit.txt
```

### Integration with Thesis Production

Once exported, integrate with your production workflow:

```bash
# Navigate to thesis production folder
cd /Users/hyunjimoon/tolzul/Front/On/love\(cs\)/thesis/⚙️process/2️⃣_PRODUCTION

# Copy draft.md files to each section (if not already there)
# Edit draft.md files to reference the figures/tables from 3️⃣_OUTPUT

# Run production pipeline (if you have one)
bash run_all.sh  # This would compile draft.md + figures into final output
```

### Files Created

This export creates two new scripts:

1. **`export_to_thesis.sh`** - Main export script
   - Runs pipeline
   - Generates thesis figures
   - Copies outputs to production folder

2. **`thesis_figures.py`** - Figure generator
   - Creates conceptual diagrams (fig1, fig2)
   - Creates H1 scatter plot (fig3)
   - Can be run standalone: `python3 thesis_figures.py [dataset]`

### Next Steps

After successful export:

1. ✅ Review figures in `3️⃣_OUTPUT/`
2. ✅ Verify tables have expected coefficients (β₁ < 0, β₃ < 0)
3. ✅ Copy production `draft.md` files to each section
4. ✅ Reference figures in your thesis text
5. ✅ Run thesis compilation pipeline

---

## Manual Export (Advanced)

If you want to run steps individually:

```bash
# Step 1: Run pipeline
./run_all.sh

# Step 2: Generate thesis figures
python3 thesis_figures.py all

# Step 3: Manual copy
THESIS_OUT="/Users/hyunjimoon/tolzul/Front/On/love(cs)/thesis/⚙️process/3️⃣_OUTPUT"

# Theory
cp outputs/all/figures/fig1_tradeoff.pdf $THESIS_OUT/Theory/
cp outputs/all/figures/fig2_architecture.pdf $THESIS_OUT/Theory/

# Empirics_Early
cp outputs/all/figures/fig3_H1_scatter.pdf $THESIS_OUT/Empirics_Early/
# ... (see export_to_thesis.sh for full copy commands)
```

---

## Questions?

- Pipeline issues: Check `PIPELINE_GUIDE.md`
- Vagueness scorer: Check `VARIABLES.md`
- Git workflow: Check `.git/` and branch `claude/select-vagueness-variant-*`
