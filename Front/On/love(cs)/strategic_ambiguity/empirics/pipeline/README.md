# Promise Precision Thesis - Modular Pipeline

Complete analysis pipeline for "Promise Precision" thesis comparing strategic vagueness effects across hardware and software ventures.

## Quick Start

Run the complete pipeline for all three datasets:

```bash
./run_all.sh
```

## Pipeline Overview

### Five-Step Modular Architecture

1. **01_load_data.py** - Load and cache raw .dat files (10-50x speedup with parquet)
2. **02_engineer_features.py** - Apply StrategicVaguenessScorerV2 and create all features
3. **03_filter_datasets.py** - Create three dataset variants (all, quantum, transportation)
4. **04_run_models.py** - Run H1/H2 models for each dataset
5. **05_generate_plots.py** - Generate F3a interaction plots

### Three Dataset Variants

- **All** - Complete dataset of venture-backed companies
- **Quantum** - Quantum computing and quantum technology companies
- **Transportation** - Autonomous vehicles, logistics, and mobility companies

## Usage Options

### Run Full Pipeline
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

### Run Individual Steps
```bash
python3 pipeline/01_load_data.py
python3 pipeline/02_engineer_features.py
python3 pipeline/03_filter_datasets.py
python3 pipeline/04_run_models.py all
python3 pipeline/05_generate_plots.py all
```

## Output Structure

```
outputs/
├── all/
│   ├── models/
│   │   ├── h1_coefficients.csv
│   │   ├── h2_main_coefficients.csv
│   │   └── h2_analysis_dataset.csv
│   └── figures/
│       ├── F3a_interaction.png
│       └── F3a_interaction.pdf
├── quantum/
│   ├── models/
│   └── figures/
└── transportation/
    ├── models/
    └── figures/
```

## Key Outputs

- **h1_coefficients.csv** - H1: Early Funding ~ Vagueness (OLS)
- **h2_main_coefficients.csv** - H2: Growth ~ Vagueness × Hardware (Logit)
- **F3a_interaction.png** - THE MONEY PLOT showing surprising reversal

## Models Tested

### H1: Information Asymmetry
```
Early Funding ~ Vagueness + Controls
```
- **Expected**: Negative coefficient (vagueness → lower early funding)
- **Result**: β = -5.56e-07, p = 0.208 (direction correct, not significant)

### H2: Integration Cost Moderation
```
Growth ~ Vagueness × Hardware + Controls
```
- **Expected**: Positive interaction (vagueness helps complex products)
- **Result**: SURPRISING REVERSAL - Vagueness helps hardware, not software
  - Main effect: β = -0.00185, p = 0.919
  - Interaction: β = 0.0886, p = 0.061 (marginally significant)

## Dependencies

See `requirements.txt`:
- pandas
- numpy
- statsmodels
- matplotlib
- pyyaml
- scipy
- scikit-learn

## Configuration

Edit `config/datasets.yaml` to:
- Modify dataset filters
- Change output directories
- Adjust vagueness scorer settings
- Configure plot styling

## Notes

- First run creates parquet cache in `data/processed/` (10-50x speedup)
- V2 vagueness scorer uses 2-component model (categorical + concreteness deficit)
- Multi-stage logit fallback handles convergence issues
- F3a uses W2 color palette (skyblue=software, gray=hardware)
