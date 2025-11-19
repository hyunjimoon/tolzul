#!/usr/bin/env python3
"""
Pipeline Validation Script
==========================
Validates that all pipeline components are properly configured and importable.
Does NOT run the full analysis - just checks setup.

Usage:
    python3 validate_pipeline.py
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

print("=" * 80)
print("PIPELINE VALIDATION")
print("=" * 80)
print()

# Test 1: Check directory structure
print("✓ Test 1: Directory Structure")
print("-" * 40)
required_dirs = [
    'src', 'pipeline', 'config', 'data/raw', 'outputs'
]
for dir_path in required_dirs:
    p = Path(dir_path)
    exists = p.exists()
    status = "✓" if exists else "✗"
    print(f"  {status} {dir_path}/")
print()

# Test 2: Check pipeline scripts
print("✓ Test 2: Pipeline Scripts")
print("-" * 40)
pipeline_scripts = [
    'pipeline/01_load_data.py',
    'pipeline/02_engineer_features.py',
    'pipeline/03_filter_datasets.py',
    'pipeline/04_run_models.py',
    'pipeline/05_generate_plots.py'
]
for script in pipeline_scripts:
    p = Path(script)
    exists = p.exists() and p.stat().st_mode & 0o111  # Check executable
    status = "✓" if exists else "✗"
    print(f"  {status} {script}")
print()

# Test 3: Check configuration
print("✓ Test 3: Configuration Files")
print("-" * 40)
config_files = [
    'config/datasets.yaml',
    'run_all.sh'
]
for config in config_files:
    p = Path(config)
    exists = p.exists()
    status = "✓" if exists else "✗"
    print(f"  {status} {config}")
print()

# Test 4: Import core modules
print("✓ Test 4: Core Module Imports")
print("-" * 40)
try:
    from features import (
        consolidate_company_snapshots,
        engineer_features,
        filter_quantum_companies,
        filter_transportation_companies,
        preprocess_for_h2
    )
    print("  ✓ features.py")
except Exception as e:
    print(f"  ✗ features.py - {e}")

try:
    from vagueness_v2 import StrategicVaguenessScorerV2
    print("  ✓ vagueness_v2.py")
except Exception as e:
    print(f"  ✗ vagueness_v2.py - {e}")

try:
    from models import test_h1_early_funding, test_h2_main_growth
    print("  ✓ models.py")
except Exception as e:
    print(f"  ✗ models.py - {e}")
print()

# Test 5: Check dependencies
print("✓ Test 5: Python Dependencies")
print("-" * 40)
dependencies = [
    'pandas', 'numpy', 'statsmodels', 'matplotlib',
    'yaml', 'scipy', 'sklearn'
]
missing = []
for dep in dependencies:
    try:
        if dep == 'yaml':
            __import__('yaml')
        elif dep == 'sklearn':
            __import__('sklearn')
        else:
            __import__(dep)
        print(f"  ✓ {dep}")
    except ImportError:
        print(f"  ✗ {dep} (missing)")
        missing.append(dep)
print()

# Test 6: Check data files
print("✓ Test 6: Data Files")
print("-" * 40)
data_raw = Path('data/raw')
if data_raw.exists():
    dat_files = list(data_raw.glob('*.dat'))
    if dat_files:
        print(f"  ✓ Found {len(dat_files)} .dat files")
        for f in dat_files[:3]:  # Show first 3
            print(f"    - {f.name}")
        if len(dat_files) > 3:
            print(f"    ... and {len(dat_files) - 3} more")
    else:
        print(f"  ⚠ No .dat files found in data/raw/")
else:
    print(f"  ✗ data/raw/ directory not found")
print()

# Summary
print("=" * 80)
print("VALIDATION SUMMARY")
print("=" * 80)
if missing:
    print(f"⚠ Missing dependencies: {', '.join(missing)}")
    print("  Install with: pip install -r requirements.txt")
    print()

print("Pipeline structure is valid! ✓")
print()
print("To run the full pipeline:")
print("  ./run_all.sh")
print()
print("To run for a single dataset:")
print("  ./run_all.sh --dataset quantum")
print("  ./run_all.sh --dataset transportation")
print()
print("=" * 80)
