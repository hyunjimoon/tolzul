# Archive

This folder contains deprecated files that have been superseded by newer implementations.

## Deprecated Documentation

- **PIPELINE_README.md** - Superseded by `../MAIN_PIPELINE_README.md`
- **README_MULTIVERSE.md** - Integrated into main pipeline documentation
- **IMPLEMENTATION_CHECKLIST.md** - Checklist from initial implementation phase

## Deprecated Scripts

- **run_analysis.py** - Superseded by `../main.py` (5-stage pipeline)
- **demo_selective_loading.py** - Demo script for selective year loading feature
- **test_parquet_quantum.py** - Demo script for parquet caching and quantum filtering

## Deprecated Shell Scripts

- **run_multiverse_pipeline.sh** - Used deprecated `run_analysis.py`, superseded by `../run_full_pipeline.sh`
- **run_full_pipeline.sh** (old version) - Used deprecated `run_analysis.py`, replaced with new version

### Why These Scripts Were Deprecated

The old shell scripts relied on `run_analysis.py` which has been replaced by the cleaner `main.py` 5-stage pipeline. The new `run_full_pipeline.sh` in the root directory uses:
1. `main.py` for the 5-stage pipeline (BUILD → DEFINE → PLOT1 → TEST → PLOT2)
2. `run_multiverse.py` for multiverse analysis (still active!)

## Current Active Files

### Main Pipeline
- **`../main.py`** - 5-stage pipeline orchestrator
  ```bash
  # Regular analysis
  python main.py --years 2022 2024 2025

  # Quantum companies only
  python main.py --use-quantum-cache --years 2022 2024 2025
  ```

### Multiverse Analysis (STILL ACTIVE!)
**⚠️ IMPORTANT**: `run_multiverse.py` and `multiverse_engine.py` are **NOT deprecated**!

- **`../run_multiverse.py`** - Executes multiverse analysis (288 specifications)
- **`../multiverse_engine.py`** - Multiverse analysis engine

The division of labor:
- `main.py` Stage 5 (PLOT2): **Visualizes** existing multiverse results
- `run_multiverse.py`: **Executes** the actual multiverse analysis

### Shell Scripts
- **`../run_full_pipeline.sh`** - New one-touch pipeline execution
  ```bash
  ./run_full_pipeline.sh data/raw results multiverse_results "2022 2024 2025"
  ```

### Documentation
- `../MAIN_PIPELINE_README.md` - Pipeline overview
- `../PARQUET_QUANTUM_README.md` - Caching features
- `../SELECTIVE_LOADING_GUIDE.md` - Selective year loading

## Cache Files

### Regular Companies Cache
```
data/processed/consolidated_companies_2022_2024_2025.parquet
```

### Quantum Companies Cache (New!)
```
data/processed/quantum_companies_2022_2024_2025.parquet
```

Both caches are created automatically and provide 20x speedup on subsequent runs.

Last updated: 2025-11-11
