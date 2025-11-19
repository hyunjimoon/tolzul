# F-Series Plotting Suite: HEV/HLVF/HSF Refactoring

**Complete reference for standardized two-snapshot analysis figures**

---

## 📋 Overview

The F-series plotting suite provides publication-ready figures for two-snapshot analysis using unified **HEV/HLVF/HSF** terminology, aligned with W2 slide conventions.

### Terminology Mapping

| **New (Standard)** | **Old** | **Model** | **Formula** |
|-------------------|---------|-----------|-------------|
| **HEV** | H1 | OLS | `E ~ V + controls` |
| **HLVF** | H2 | Logit | `L ~ V × F + controls` **(NO E)** |
| **HSF** | H3 | OLS | `S ~ V × F + controls` (L==1 only) |

### CRITICAL Principle: HLVF NO-E Rule

**HLVF MUST NOT include early_funding (E) as a control.**

**Rationale** (from W2 slides p.49):
- E is a **mediator** in the causal chain: `V → E → L`
- Controlling for E would **block** the causal path from vagueness to later success
- This is a **design decision**, not an omission

```
Correct:   V → E → L   (E is mediator)
Incorrect: V → L ← E   (E is confounder)
```

---

## 🎨 W2 Color Palette (Strict)

```python
PALETTE = {
    "E": "red",           # Early event
    "L": "#0000FF",       # Later success (pure blue)
    "V": "green",         # Vagueness
    "S": "purple",        # Step-up
    "F": "skyblue",       # Flexibility
    "C": "orange"         # Serial founder
}
```

### Axis Coloring Rules

- **X-axis with V**: green labels/ticks/spine
- **Y-axis with L probability**: blue labels/ticks

### Interaction Line Styles

| **Condition** | **Color** | **Style** | **Expected Slope** |
|--------------|-----------|-----------|-------------------|
| F=1 (flexible/software) | skyblue | solid (`-`) | ↑ upward |
| F=0 (hardware) | skyblue | dashed (`--`) | ↓ downward/flat |
| C=1 (serial founder) | orange | dash-dot (`-.`) | varies |
| C=0 (first-time) | orange | dotted (`:`) | varies |

---

## 📊 Figure Specifications (10 Figures)

### F1: E vs V (HEV)
**File**: `F1_E_vs_V.[png|pdf]`

- **Model**: HEV (E ~ V + controls)
- **Type**: Scatter + OLS fit line
- **Colors**: Red points, red line, green x-axis
- **Shows**: Negative relationship between vagueness and early funding

### F2: Pr(L) vs V (HLVF)
**File**: `F2_PrL_vs_V.[png|pdf]`

- **Model**: HLVF (L ~ V × F, **NO E**)
- **Type**: Predicted probability curve
- **Colors**: Blue curve, green x-axis, blue y-axis
- **Fixed**: F at median/mode, other controls at medians
- **Caption**: "E omitted by design: mediator, not control"

### F3a: L | F (V×F Interaction from HLVF)
**File**: `F3a_L_given_F.[png|pdf]`

- **Model**: HLVF (L ~ V × F, **NO E**)
- **Type**: Two conditional curves
- **Lines**:
  - F=1 (flexible/software): skyblue, solid, ↑ upward slope
  - F=0 (hardware): skyblue, dashed, ↓ downward/flat slope
- **Fixed**: C (serial) and other controls at medians/modes
- **Shows**: Flexibility moderates vagueness effect on later success

### F3b: L | C (V×C Interaction)
**File**: `F3b_L_given_C.[png|pdf]`

- **Model**: H4 (growth ~ V × C + controls)
- **Type**: Two conditional curves
- **Lines**:
  - C=1 (serial founder): orange, dash-dot
  - C=0 (first-time founder): orange, dotted
- **Fixed**: F and other controls at medians/modes
- **Shows**: Founder experience moderates vagueness effect

### F4: Distributions (5 Separate Figures)

**Files**: `F4_[E|L24|L25|V|F]_dist.[png|pdf]`

1. **F4_E_dist**: E distribution, red, x-axis red labels
2. **F4_L24_dist**: L_2024 distribution, blue bars
3. **F4_L25_dist**: L_2025 distribution, blue bars
4. **F4_V_dist**: V distribution, green, x-axis green labels
5. **F4_F_dist**: F distribution, skyblue bars, labels "Hardware (0)" / "Software (1)"

### F5: Step-up by F (HSF)
**File**: `F5_stepup_by_F.[png|pdf]`

- **Model**: HSF (S ~ V × F, **L==1 only**)
- **Type**: Boxplot by flexibility
- **Colors**: Purple boxes, purple y-axis
- **Filter**: Survivors only (L==1)
- **Caption**: "L==1 (survivors) only"
- **Shows**: Distribution of valuation step-up by company type

### F6: Specification Curve (Multiverse)
**File**: `F6_spec_curve.[png|pdf]`

- **Input**: DataFrame with `coefficient`, `pvalue`, `term`
- **Type**: Scatter plot, sorted by coefficient
- **Colors**:
  - V (main effect): green
  - V×F (interaction): skyblue
  - V×C (interaction): orange
- **Features**: Horizontal line at 0, optional error bars (±1.96 SE)
- **Shows**: Robustness of results across model specifications

---

## 🚀 Quick Start

### Installation

```bash
# Pull latest code
git pull origin claude/implement-F-series-plots-011CV3bYfAgYgWDRXnZpz8dk

# Ensure dependencies
pip install pandas numpy matplotlib statsmodels scipy
```

### Basic Usage

```python
from pathlib import Path
from modules import models
from modules.plots_F_series import create_F_series

# 1. Load your data
df = ...  # Your two-snapshot DataFrame

# 2. Fit models (HEV/HLVF/HSF)
results = {
    'HEV': models.run_HEV(df),      # E ~ V
    'HLVF': models.run_HLVF(df),    # L ~ V × F (NO E!)
    'h4': models.test_h4_growth_interaction(df),  # For F3b
    'HSF': models.run_HSF(df),      # S ~ V × F (L==1 only)
    'spec_df': my_spec_df           # Optional, for F6
}

# 3. Generate all figures
outdir = Path('outputs/figures')
paths = create_F_series(df, results, outdir)

# Result: 10 figures × 2 formats = 20 files
# paths = {
#     'F1': {'png': Path('...'), 'pdf': Path('...')},
#     'F2': {'png': Path('...'), 'pdf': Path('...')},
#     ...
# }
```

### Run Demo

```bash
python demo_F_series_HEV_HLVF_HSF.py
```

**Output**: 10 figure sets in `outputs/figures/` with both PNG (300dpi) and PDF formats.

---

## 📐 Technical Specifications

### Helper Functions

#### `median_or_mode(series)`
Returns median for numeric variables, mode (majority) for categorical/binary.

```python
>>> median_or_mode(pd.Series([0, 0, 0, 1, 1]))  # Binary
0
>>> median_or_mode(pd.Series([1.2, 3.4, 5.6]))  # Numeric
3.4
```

#### `fix_controls_at_medianmode(df, cols)`
Fixes control variables and other moderators at sample medians/modes.

```python
>>> fix_controls_at_medianmode(df, ['F_flexibility', 'founding_cohort'])
{'F_flexibility': 1, 'founding_cohort': '2018-2020'}
```

#### `color_axis_for_var(ax, xvar, yvar)`
Colors axis labels/ticks/spines according to W2 rules.

```python
>>> color_axis_for_var(ax, xvar='z_V', yvar='L')
# X-axis → green, Y-axis → blue
```

#### `save_figure(fig, outdir, filename_base)`
Saves figure in multiple formats (PNG + PDF).

```python
>>> save_figure(fig, Path('outputs/figures'), 'F1_E_vs_V')
{'png': Path('outputs/figures/F1_E_vs_V.png'),
 'pdf': Path('outputs/figures/F1_E_vs_V.pdf')}
```

### Figure Settings

```python
FIGURE_DPI = 300
FIGURE_FORMATS = ['png', 'pdf']
TITLE_FONTSIZE = 16
LABEL_FONTSIZE = 13
LEGEND_FONTSIZE = 10
```

---

## 🔍 Validation Checklist

Use this checklist to verify your figures meet W2 specifications:

### Global Checks
- [ ] All figures saved as PNG (300dpi) + PDF
- [ ] Filenames use `F[1-6]_*.[png|pdf]` pattern
- [ ] Output directory is `outputs/figures/`
- [ ] All titles use HEV/HLVF/HSF terminology (no H1/H2)

### Color Checks
- [ ] E elements are **red**
- [ ] L elements are **pure blue (#0000FF)**
- [ ] V elements are **green**
- [ ] S elements are **purple**
- [ ] F elements are **skyblue**
- [ ] C elements are **orange**

### Axis Checks
- [ ] X-axis with V: green labels/ticks/spine
- [ ] Y-axis with L probability: blue labels
- [ ] No axis label/legend overlap (tight_layout used)

### Interaction Plot Checks (F3a, F3b)
- [ ] F3a: F=1 is skyblue solid (upward)
- [ ] F3a: F=0 is skyblue dashed (downward/flat)
- [ ] F3b: C=1 is orange dash-dot
- [ ] F3b: C=0 is orange dotted
- [ ] Other moderator fixed at median/mode

### HLVF NO-E Checks
- [ ] F2 caption mentions "E omitted by design"
- [ ] F3a caption mentions "E omitted: mediator, not control"
- [ ] HLVF model does NOT include early_funding
- [ ] Documentation references W2 p.49

---

## 🔄 Backward Compatibility

### Legacy Code Support

Old H1/H2 functions remain in `plots.py` for backward compatibility:

```python
# Old way (still works)
from modules.plots import plot_h1_scatter, plot_h2_interaction

# New way (preferred)
from modules.plots_F_series import fig_F1_E_vs_V, fig_F3a_L_given_F
```

### Model Key Variants

The orchestrator accepts both uppercase and lowercase keys:

```python
# All equivalent
results = {'HEV': model, ...}
results = {'hev': model, ...}
results = {'H1': model, ...}  # Legacy
```

---

## 📚 References

### W2 Slides
- **p.49**: "Early Funding: Mediator or Confounder?" (NO-E principle)
- **ELSVF Palette**: Standard colors for two-snapshot variables
- **Interaction Conventions**: Line styles and slope expectations

### Models Module
- `run_HEV(df)` → `modules/models.py:384-409`
- `run_HLVF(df)` → `modules/models.py:412-485` (NO early_funding control)
- `run_HSF(df)` → `modules/models.py:488-564` (L==1 filter)
- `test_h4_growth_interaction(df)` → `modules/models.py:216-367`

### Key Comments in Code
```python
# models.py line 417-418
"""
CRITICAL: NO early_funding control (it's a MEDIATOR, not confounder)
"""

# plots_F_series.py line 5-7
"""
CRITICAL: HLVF uses NO early_funding control (E is mediator, not confounder)
Reference: W2 slides p.49 "Early Funding: Mediator or Confounder?"
"""
```

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'plots_F_series'"

**Solution**: Ensure you're in the project root and `modules/plots_F_series.py` exists.

```bash
ls -la modules/plots_F_series.py
python -c "from modules.plots_F_series import create_F_series"
```

### "ValueError: H3 requires survivors with valid step-up data"

**Solution**: H3/HSF analysis requires valuation data. If unavailable, skip it:

```python
results = {
    'HEV': hev,
    'HLVF': hlvf,
    'h4': h4,
    # 'HSF': None,  # Skip if no valuation data
    'spec_df': spec_df
}
```

See `diagnose_stepup.py` and `inspect_valuation_columns.py` for data diagnostics.

### "KeyError: 'HEV'" or "'HLVF'"

**Solution**: Use uppercase keys or provide both variants:

```python
# Correct
results = {'HEV': model, 'HLVF': model2, ...}

# Also works (backward compatible)
results = {'hev': model, 'hlvf': model2, ...}
```

### Figures look wrong / colors don't match

**Solution**:
1. Verify you're using `plots_F_series.create_F_series()`, not old functions
2. Check that matplotlib backend supports color rendering
3. View PDFs to confirm colors (PNG rendering may vary)

---

## 📝 Summary

### What Changed

| **Aspect** | **Before** | **After** |
|-----------|-----------|----------|
| Terminology | H1/H2/H3 | HEV/HLVF/HSF |
| Module | Embedded in plots.py | Separate plots_F_series.py |
| Early funding in HLVF | Inconsistent | **Never included** (enforced) |
| Color spec | Variable | W2 strict palette |
| Output formats | PNG only | PNG + PDF |
| Axis coloring | None | V=green, L=blue |
| Line styles | Arbitrary | W2 convention (solid/dashed/etc.) |

### Key Benefits

✅ **Consistent**: All figures follow W2 slide conventions
✅ **Correct**: NO-E principle enforced in HLVF
✅ **Complete**: 10 figures covering all analyses
✅ **Quality**: 300dpi PNG + vector PDF
✅ **Documented**: Comprehensive inline comments and docstrings
✅ **Tested**: Demo script with synthetic data

---

## 🎓 Citation

If you use these figures in publications, acknowledge:

> "Figures generated using standardized F-series plotting suite (HEV/HLVF/HSF terminology), following W2 slide conventions. HLVF analysis omits early funding control by design (mediator principle)."

---

**Last Updated**: 2025-11-12
**Version**: 1.0
**Branch**: `claude/implement-F-series-plots-011CV3bYfAgYgWDRXnZpz8dk`
