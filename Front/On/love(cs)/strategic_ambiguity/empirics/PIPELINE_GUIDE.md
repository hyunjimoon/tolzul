# Promise Precision Thesis - Complete Pipeline Guide

**One-command analysis for all three datasets: `./run_all.sh`**

## Overview

This repository contains a modular, production-ready pipeline for the "Promise Precision" thesis analyzing strategic vagueness effects across hardware and software ventures.

### Key Innovation: Three Dataset Variants

- **All Companies** - Complete dataset of venture-backed firms
- **Quantum Computing** - Quantum technology and computing companies
- **Transportation & Mobility** - Autonomous vehicles, logistics, and mobility companies

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Place Data Files

Put your PitchBook .dat files in `data/raw/`:
- Company snapshots (snapshot dates as filenames)
- Financing data
- Founder credentials

### 3. Run Complete Pipeline

```bash
./run_all.sh
```

This executes all 5 steps for all 3 datasets (~5-15 minutes depending on data size).

### 4. View Results

```
outputs/
├── all/models/h1_coefficients.csv          # H1 for all companies
├── all/models/h2_main_coefficients.csv     # H2 for all companies
├── all/figures/F3a_interaction.png         # The "money plot"
├── quantum/models/...                       # Quantum subset results
├── quantum/figures/...                      # Quantum subset plots
├── transportation/models/...                # Transportation subset results
└── transportation/figures/...               # Transportation subset plots
```

## Pipeline Architecture

### Five-Step Modular Design

```
01_load_data.py          → Load .dat files, create parquet cache (10-50x speedup)
02_engineer_features.py  → Apply V2 vagueness scorer, create all features
03_filter_datasets.py    → Split into three dataset variants
04_run_models.py         → Run H1/H2 for each dataset
05_generate_plots.py     → Generate F3a interaction plots
```

Each script is standalone and can be run independently.

### Directory Structure

```
empirics_ent_strat_ops/
├── run_all.sh                 # Master pipeline script
├── validate_pipeline.py       # Validation script
├── config/
│   └── datasets.yaml          # Dataset configuration
├── pipeline/
│   ├── 01_load_data.py
│   ├── 02_engineer_features.py
│   ├── 03_filter_datasets.py
│   ├── 04_run_models.py
│   ├── 05_generate_plots.py
│   └── README.md
├── src/
│   ├── features.py            # Feature engineering + filters
│   ├── vagueness_v2.py        # StrategicVaguenessScorerV2
│   └── models.py              # H1/H2 hypothesis tests
├── data/
│   ├── raw/                   # Your .dat files go here
│   └── processed/             # Parquet cache (auto-generated)
├── outputs/
│   ├── all/
│   ├── quantum/
│   └── transportation/
├── modules/                   # Original implementations (archived)
├── archive/                   # Legacy analysis scripts
└── docs_archive/              # Documentation from previous sessions
```

## Usage Examples

### Run Full Pipeline (All Datasets)

```bash
./run_all.sh
```

### Quick Mode (Skip Data Loading)

```bash
./run_all.sh --quick
```

### Single Dataset

```bash
./run_all.sh --dataset quantum
./run_all.sh --dataset transportation
```

### Individual Steps

```bash
python3 pipeline/01_load_data.py
python3 pipeline/02_engineer_features.py
python3 pipeline/03_filter_datasets.py
python3 pipeline/04_run_models.py quantum
python3 pipeline/05_generate_plots.py quantum
```

## Models Tested

### H1: Information Asymmetry Hypothesis

```
Early Funding ~ Vagueness + Controls
```

**Theory**: Information asymmetry → vagueness reduces early funding

**Current Results** (all companies):
- Vagueness coefficient: β = -5.56e-07, p = 0.208
- Direction correct (negative), not statistically significant
- Need to check quantum and transportation subsets for stronger effects

### H2: Integration Cost Moderation Hypothesis

```
Growth ~ Vagueness × Hardware + Controls
```

**Theory**: Integration costs moderate vagueness effects

**Current Results** (all companies) - SURPRISING REVERSAL:
- Main effect (software): β = -0.00185, p = 0.919 (null)
- Interaction (hardware): β = 0.0886, p = 0.061 (marginally significant)
- **Finding**: Vagueness helps hardware firms, not software!

**Theoretical Interpretation**:
- Hardware firms face high switching costs → vagueness preserves pivot options
- Software firms already flexible → vagueness adds no value
- Aligns with real options theory, modularity literature

## Key Features

### StrategicVaguenessScorerV2

**Two-component vagueness measure** (removed lexical uncertainty per research spec):

1. **Categorical Vagueness (S_cat)**
   - IDF-weighted abstract term counting
   - Enhanced quantum/hardware unit detection
   - Scaling factor α = 2.3

2. **Concreteness Deficit (S_concdef)**
   - 5 sub-features: numbers, dates, versions, units, benchmarks
   - Density-based squashing function
   - Weighted combination

**Output**: `V_raw = 0.5 × max(S_cat, S_concdef) + 0.5 × mean(...)`

See `docs_archive/VAGUENESS_SCORER_V2_GUIDE.md` for full details.

### Dataset Filtering

**Quantum Companies**: Filter by keywords in Description/Keywords/Promise
- quantum, qubit, quantum computing, quantum processor
- quantum algorithm, quantum cryptography, quantum sensor
- superconducting qubit, ion trap, quantum error correction
- nisq, quantum gate, quantum advantage

**Transportation Companies**: Filter by keywords
- autonomous vehicle, self-driving, mobility, logistics
- electric vehicle, ev charging, drone delivery
- rideshare, micromobility, e-scooter, bike share
- lidar, radar, sensor fusion, fleet management
- last mile delivery, warehouse automation

### Parquet Caching

First run creates parquet cache in `data/processed/`:
- 10-50x speedup for subsequent runs
- Preserves dtypes and reduces memory usage
- Auto-detects cache and skips re-parsing .dat files

### Multi-Stage Logit Fallback

H2 logit models use robust convergence strategy:
1. Standard MLE (maxiter=100)
2. L1 regularization (α=0.1) if step 1 fails
3. L1 regularization (α=0.5) if step 2 fails

Ensures models converge even with small sample sizes (quantum/transportation subsets).

## Configuration

Edit `config/datasets.yaml` to:
- Add new dataset filters
- Change output directories
- Adjust vagueness scorer settings
- Configure plot styling

Example:
```yaml
datasets:
  biotech:
    name: "Biotech & Healthcare"
    description: "Biotech and healthcare companies"
    filter_function: "filter_biotech_companies"  # Add to features.py
    output_dir: "outputs/biotech"
```

## Validation

Check pipeline setup without running full analysis:

```bash
python3 validate_pipeline.py
```

Validates:
- Directory structure
- Pipeline scripts (executable)
- Configuration files
- Module imports
- Python dependencies
- Data files

## Output Files

### Model Results

- `h1_coefficients.csv` - H1 regression coefficients with p-values
- `h2_main_coefficients.csv` - H2 logit coefficients with p-values
- `h2_analysis_dataset.csv` - Preprocessed data used for H2 (for plotting)

### Figures

- `F3a_interaction.png` - THE MONEY PLOT (300 DPI)
- `F3a_interaction.pdf` - Vector version for publication

**F3a Plot**: Shows Vagueness × Hardware interaction
- Software (skyblue solid line): Vagueness effect near zero or negative
- Hardware (gray dashed line): Vagueness effect positive (diverging scissors)
- Controls held at means (employees, founding cohort)

## Dependencies

See `requirements.txt`:
```
pandas>=1.3.0
numpy>=1.21.0
statsmodels>=0.13.0
matplotlib>=3.4.0
pyyaml>=5.4.0
scipy>=1.7.0
scikit-learn>=0.24.0
```

## Troubleshooting

### No .dat files found
- Place PitchBook data files in `data/raw/`
- Files should have snapshot dates as filenames

### Import errors
- Run `pip install -r requirements.txt`
- Check Python version >= 3.8

### Model convergence issues
- Multi-stage fallback should handle most cases
- For quantum/transportation: may need more companies or looser convergence criteria
- Edit `pipeline/04_run_models.py` to adjust `maxiter` or `alpha` parameters

### Memory issues with large datasets
- Parquet cache helps significantly
- Use `--quick` mode to skip re-loading
- Consider filtering to specific snapshot dates in `01_load_data.py`

## Related Documentation

- `pipeline/README.md` - Detailed pipeline documentation
- `docs_archive/VAGUENESS_SCORER_V2_GUIDE.md` - V1 vs V2 comparison
- `docs_archive/F_SERIES_PLOTS_GUIDE.md` - Plot roles and interpretation
- `docs_archive/STANDALONE_MIGRATION_PROMPT.md` - Guide for making thesis files standalone
- `docs_archive/ADVISOR_1SLIDE_SUMMARY.md` - Presentation materials

## Support

For issues or questions:
1. Check validation: `python3 validate_pipeline.py`
2. Review logs in terminal output
3. Check individual script outputs in `outputs/*/`

## Next Steps

1. **Run pipeline**: `./run_all.sh`
2. **Review results**: Compare H1/H2 across three datasets
3. **Check F3a plots**: Look for differential effects across subsets
4. **Prepare presentation**: Use outputs for advisor meeting

**Expected insights**:
- Quantum companies may show stronger vagueness effects (high technical uncertainty)
- Transportation companies may show different moderation patterns (regulatory constraints)
- Compare effect sizes across datasets for robustness

---

**Ready to run? Just execute: `./run_all.sh`** 🚀
