# Main Pipeline - 5-Stage Multiverse Analysis 🌟

This document describes the refactored main pipeline implementing a clean, modular 5-stage analysis framework.

## 🎯 Overview

The pipeline executes the complete multiverse analysis in 5 distinct stages:

1. **1🏗️BUILD**: Load and consolidate data from .dat files
2. **2🧠DEFINE**: Engineer 5 core variables
3. **3📊PLOT1**: Visualize variable distributions
4. **4⚖️TEST**: Test 3 core hypotheses
5. **5📈PLOT2**: Run and visualize multiverse analysis

## 📦 Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

Required packages:
- pandas >= 1.5.0
- numpy >= 1.23.0
- statsmodels >= 0.14.0
- matplotlib >= 3.7.0
- seaborn >= 0.12.0
- scipy >= 1.10.0

## 🚀 Quick Start

### Basic Usage

```bash
# Run complete pipeline with processed CSV data
python main.py --skip-dat --output-dir results/

# Run with .dat files (if available)
python main.py --data-dir data/raw/ --output-dir results/
```

### Command Line Options

```bash
python main.py --help

Options:
  --data-dir DIR      Directory containing raw .dat files (default: data/raw/)
  --output-dir DIR    Output directory for results (default: results/)
  --skip-dat          Skip .dat file loading and use processed CSV instead
```

## 📂 Pipeline Stages

### 1🏗️ BUILD: Data Consolidation

**Purpose**: Load and consolidate multi-year company snapshots from .dat files.

**Functions** (in `modules/features.py`):
- `load_company_snapshot()`: Load single Company*.dat file
- `consolidate_company_snapshots()`: Merge all snapshots, keep latest info per company
- `load_deal_snapshot()`: Load deal data files

**Input**:
- `data/raw/Company*.dat` files (pipe-delimited)
- OR `data/processed/analysis_panel.csv` (fallback)

**Output**: Consolidated DataFrame with all companies

**Example .dat file structure**:
```
data/raw/
├── Company20211201.dat
├── Company20220101.dat
├── Company20220601.dat
├── Company20221201.dat
...
```

### 2🧠 DEFINE: Variable Engineering

**Purpose**: Create 5 core analytical variables with proper transformations.

**Core Variables**:

| Symbol | Variable | Type | Description |
|--------|----------|------|-------------|
| 🧧E | `early_funding_musd` | Continuous | First financing size ($M, Series A only) |
| 💰L | `growth` | Binary | Series B+ achievement (1=yes, 0=no) |
| 🤙V | `z_vagueness` | Continuous | Strategic vagueness score (z-standardized) |
| 💪F | `is_hardware` | Binary | Hardware sector (1=hardware, 0=software) |
| 💸S | `valuation_stepup` | Continuous | Log(Later/Early valuation) [optional] |

**Functions** (in `modules/features.py`):
- `engineer_features()`: Create all variables
- `preprocess_for_h2()`: Z-score normalization, cohort creation
- `compute_vagueness_vectorized()`: Academic vagueness scoring
- `classify_hardware_vectorized()`: Hardware/software classification

**Vagueness Scoring** (academic literature-based):
- Lexical Uncertainty (Loughran & McDonald 2011, 2016)
- Concreteness Deficit (Pan et al. 2018)
- Categorical Vagueness (Zuckerman 1999)

### 3📊 PLOT1: Variable Distributions

**Purpose**: Visualize distributions of all 5 core variables.

**Function** (in `modules/plots.py`):
- `plot_variable_distributions()`: Create 2×3 subplot panel

**Output**: `variable_distributions.png`

**Layout**:
```
[🧧E histogram]  [💰L bar chart]  [🤙V histogram]
[💪F bar chart]  [💸S histogram]  [empty]
```

Each plot includes:
- Mean/median statistics
- Sample size
- Distribution shape
- Missing data handling

### 4⚖️ TEST: Hypothesis Testing

**Purpose**: Test 3 core hypotheses using regression models.

**Hypotheses**:

| Code | Hypothesis | Model | Expected |
|------|------------|-------|----------|
| H🧧E🤙V | Early Funding ~ Vagueness | OLS | β < 0 (clarity premium) |
| H💰L🤙V | Growth ~ Vagueness | Logit | β > 0 (flexibility value) |
| H💰L🤙V💪F | Growth ~ Vagueness × Hardware | Logit | β_int < 0 (moderation) |

**Functions** (in `modules/models.py`):
- `test_h1_early_funding()`: Test H1 (OLS regression)
- `test_h2_main_growth()`: Test H2 main effect (Logit with L1 fallback)
- Model includes interaction term for H2 moderation

**Output**:
- `hypothesis_results.txt`: Full regression tables
- Console log with coefficient estimates and p-values

**Robust Estimation Strategy**:
1. Try standard MLE
2. Fallback to L1 regularization (α=0.1)
3. Fallback to stronger L1 (α=0.5)

### 5📈 PLOT2: Multiverse Analysis Visualization

**Purpose**: Visualize robustness across specification space.

**Functions** (in `modules/plots.py`):
- `plot_expectation_reality_heatmap()`: Alignment matrix
- `plot_enhanced_specification_curve()`: Coefficient distribution with expectation zones

**Outputs**:
- `expectation_reality_heatmap.png`: 2×2 panel showing hypothesis support
- `specification_curve_enhanced.png`: Specification curve with color-coded results

**Visual Encoding**:
- 🟢 Green: Confirmed (correct sign, p < 0.05)
- 🔴 Red: Rejected (wrong sign, p < 0.05)
- 🟡 Yellow: Partial (correct sign, p ≥ 0.05)
- ⚫ Gray: Inconclusive

**Alignment Score**:
```python
+1.0: Perfect alignment (expected sign, significant)
+0.25: Partial alignment (expected sign, not significant)
 0.0: Neutral
-0.25: Partial misalignment (wrong sign, not significant)
-1.0: Complete misalignment (wrong sign, significant)
```

## 🏗️ Architecture

### File Structure

```
empirics_ent_strat_ops/
├── main.py                      # 5-stage orchestrator (NEW)
├── modules/
│   ├── features.py              # Updated with .dat loading
│   ├── models.py                # Hypothesis testing
│   └── plots.py                 # Updated with new visualizations
├── multiverse_engine.py         # Multiverse grid execution
├── run_multiverse.py            # CLI for multiverse analysis
├── data/
│   ├── raw/                     # .dat files (gitignored)
│   └── processed/               # CSV files
├── results/                     # Pipeline outputs
└── MAIN_PIPELINE_README.md      # This file
```

### Module Responsibilities

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| `main.py` | Orchestrate 5-stage pipeline | `stage_1_build()`, `stage_2_define()`, etc. |
| `features.py` | Data loading & engineering | `consolidate_company_snapshots()`, `engineer_features()` |
| `models.py` | Statistical testing | `test_h1_early_funding()`, `test_h2_main_growth()` |
| `plots.py` | Visualization | `plot_variable_distributions()`, `plot_enhanced_specification_curve()` |

## 📊 Example Output

### Variable Distributions

![Variable Distributions](results/test_run/variable_distributions.png)

Shows:
- 🧧E: Right-skewed funding distribution
- 💰L: Growth rate (typically 10-15%)
- 🤙V: Normal distribution (z-standardized)
- 💪F: Hardware/software ratio
- 💸S: Valuation step-up (if available)

### Hypothesis Results

```
H🧧E🤙V: Early Funding ~ Vagueness
  Result: β=-0.0234, p=0.012 ✅
  Expected: β < 0 (vagueness reduces early funding)
  Supported: True

H💰L🤙V: Growth ~ Vagueness
  Result: β=0.0456, p=0.003 ✅
  Expected: β > 0 (vagueness increases growth)
  Supported: True

H💰L🤙V💪F: Growth ~ Vagueness × Hardware
  Result: β_interaction=-0.0312, p=0.045 ✅
  Expected: Moderation effect
  Supported: True
```

### Multiverse Visualization

**Expectation vs Reality Heatmap**:
- Shows alignment scores by window × scaling
- Green = confirmed, Red = rejected, Yellow = inconclusive

**Enhanced Specification Curve**:
- Top panel: Coefficient estimates sorted by value
- Middle panel: Specification configuration grid
- Bottom panel: P-value distribution
- Color-coded by alignment with expectations

## 🔧 Advanced Usage

### Running Specific Stages

```python
from main import stage_1_build, stage_2_define

# Load data only
df = stage_1_build('data/raw/', use_processed=False)

# Engineer features only
df = stage_2_define(df)
```

### Custom Multiverse Configuration

Edit `run_multiverse.py` COORDS grid:

```python
COORDS = {
    "stage": ["E", "L1", "L2"],
    "window": [
        ("2022-06", "2024-12"),  # Add custom windows
        ("2022-06", "2025-11"),
        ("2021-12", "2024-06")
    ],
    "scaling": ["zscore", "winsor99_z"],
    "moderator": ["isSoftware"],
    "ctrl_employee": [0, 1],
    "ctrl_region": [0, 1],
    "ctrl_founder": [0, 1],
    "ctrl_earlyfund": [0, 1]
}
```

Total specifications = 3 × 3 × 2 × 1 × 2 × 2 × 2 × 2 = **288**

### Logging Configuration

```python
import logging

# Set detailed logging
logging.basicConfig(level=logging.DEBUG)

# Or minimal logging
logging.basicConfig(level=logging.WARNING)
```

## 🐛 Troubleshooting

### Issue: "No Company*.dat files found"

**Solution**: Use `--skip-dat` flag to use processed CSV:
```bash
python main.py --skip-dat
```

### Issue: "ModuleNotFoundError: No module named 'pandas'"

**Solution**: Install dependencies:
```bash
pip install -r requirements.txt
```

### Issue: "H2 model convergence failed"

**Cause**: Perfect separation or multicollinearity in growth data

**Solution**: Model automatically falls back to L1 regularization. Check diagnostics:
```
  📊 H2 (Architecture) Diagnostics:
     Sample size: 1,234
     Growth rate: 12.3%
     Architecture distribution:
       Software (0): 800 (64.8%)
       Hardware (1): 434 (35.2%)
```

### Issue: Emoji rendering in plots

**Cause**: Missing font glyphs for Unicode emojis

**Solution**: Non-critical warning, plots still generated correctly. To suppress:
```python
import warnings
warnings.filterwarnings('ignore', message='Glyph.*missing from font')
```

## 📚 References

### Academic Citations

**Vagueness Measurement**:
- Loughran & McDonald (2011, JF): Lexical uncertainty
- Pan et al. (2018, SMJ): Linguistic concreteness
- Zuckerman (1999, AJS): Categorical ambiguity

**Theoretical Framework**:
- Real Options Theory (Bowman & Hurry 1993)
- Resource Flexibility (Sanchez 1995)
- Strategic Ambiguity (Eisenberg 1984)

## 🤝 Contributing

When modifying the pipeline:

1. **Follow Clean Code Principles**:
   - Type hints for all functions
   - Docstrings with Args/Returns
   - Constants at module top
   - Early returns and guard clauses
   - Logging over print statements

2. **Test Changes**:
```bash
python main.py --skip-dat --output-dir results/test/
```

3. **Update Documentation**:
   - Update this README
   - Add docstrings to new functions
   - Document breaking changes

## 📝 Version History

### v2.0 (2025-11-11)
- ✨ NEW: Modular 5-stage pipeline architecture
- ✨ NEW: .dat file consolidation support
- ✨ NEW: Variable distribution visualization
- ✨ NEW: Expectation vs reality heatmap
- ✨ NEW: Enhanced specification curve
- 🔧 IMPROVED: Clean code refactoring (type hints, logging, docstrings)
- 🔧 IMPROVED: Robust estimation with L1 fallback

### v1.0 (Previous)
- Original multiverse engine with xarray backend

## 📬 Contact

For questions or issues:
1. Check existing documentation in `README.md`, `README_MULTIVERSE.md`
2. Review code comments and docstrings
3. Examine log files (`pipeline.log`)

---

**장군님, 이 파이프라인은 이제 완전히 모듈화되어 있으며 clean code 원칙을 따릅니다!** 🎖️
