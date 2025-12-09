# Strategic Ambiguity Empirics Pipeline

[![Tests](https://github.com/hyunjimoon/empirics_ent_strat_ops/actions/workflows/test.yml/badge.svg)](https://github.com/hyunjimoon/empirics_ent_strat_ops/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/hyunjimoon/empirics_ent_strat_ops/branch/main/graph/badge.svg)](https://codecov.io/gh/hyunjimoon/empirics_ent_strat_ops)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

Empirical analysis pipeline for strategic ambiguity research in venture capital.

## Features

- **Hypothesis Testing**: H1, H2, H3, H4 models with statistical validation
- **Two-Snapshot Validation**: E/L/S trajectory analysis
- **Vagueness Scoring**: Strategic ambiguity measurement (V1, V2)
- **Multiverse Analysis**: Specification curve robustness checks
- **Publication Figures**: F-series visualization generation

## Installation

```bash
# Clone repository
git clone https://github.com/hyunjimoon/empirics_ent_strat_ops.git
cd empirics_ent_strat_ops

# Install dependencies
pip install -r requirements.txt
```

## Running Tests

```bash
# Run all tests
pytest test/unit/test_models.py -v

# Run with coverage
pytest test/unit/test_models.py --cov=src/models

# Run specific test class
pytest test/unit/test_models.py::TestH1EarlyFunding -v
```

## Test Coverage

**Current Status:**
- ✅ `models.py` - 100% coverage (53 tests)
  - H1: Early funding ~ vagueness (OLS)
  - H2: Growth ~ vagueness × hardware (Logit)
  - H3: Log funding ~ vagueness × founder (OLS)
  - H4: Growth ~ vagueness × founder (Logit)
  - Two-snapshot: E/L/S validation

**Test Suite Features:**
- 15 reusable fixtures with synthetic data
- Edge case handling (missing data, perfect separation)
- Statistical property validation
- Convergence robustness checks

## Pipeline Structure

```
src/
├── models.py          # Hypothesis testing (627 lines) ✓ tested
├── features.py        # Data loading & feature engineering (1,538 lines)
├── plotting.py        # Publication figures (1,012 lines)
├── cache_manager.py   # Pipeline caching (506 lines)
├── cli.py            # Command-line interface (898 lines)
└── vagueness_v2.py   # Strategic vagueness scorer (647 lines)

test/
├── conftest.py           # Shared fixtures
└── unit/
    └── test_models.py    # Hypothesis testing tests (53 tests)
```

## Usage

### Data Analysis Pipeline

```bash
# Load and engineer features
python -m src.cli load-data
python -m src.cli engineer-features

# Run hypothesis tests
python -m src.cli run-models --dataset quantum

# Generate figures
python -m src.cli generate-plots --dataset quantum
```

### Paper Generation Pipeline (NEW!)

**Complete pipeline** (Data → Analysis → Paper PDF):

```bash
make all
```

**Quick rebuild** (skip data processing):

```bash
make quick
```

**Individual steps**:

```bash
# Step 1: Process data
make data

# Step 2: Run statistical analyses and generate Results section
make analysis

# Step 3: Generate tables
make tables

# Step 4: Generate figures
make figures

# Step 5: Compile LaTeX to PDF
make paper
```

**Key outputs**:
- `paper/results_auto.tex` - Auto-generated Results section (Module #23-27)
- `paper/tables/*.tex` - LaTeX tables (Table 1-2)
- `paper/figures/*.pdf` - All figures (Fig 2-3)
- `paper/output/main.pdf` - Final paper PDF

See [`docs/PAPER_PIPELINE_GUIDE.md`](docs/PAPER_PIPELINE_GUIDE.md) for detailed documentation.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Run tests: `pytest test/unit/ -v`
4. Submit a pull request

## Citation

If you use this code in your research, please cite:

```bibtex
@software{strategic_ambiguity_empirics,
  title = {Strategic Ambiguity Empirics Pipeline},
  author = {Moon, Hyunji},
  year = {2024},
  url = {https://github.com/hyunjimoon/empirics_ent_strat_ops}
}
```

## License

MIT License
