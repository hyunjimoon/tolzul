"""
Strategic Vagueness Analysis - Core Modules
============================================

This package contains all core analysis modules for the
Promise Precision / Strategic Vagueness research project.

Modules:
    features      - Data loading and feature engineering
    models        - Statistical models (H1, H2)
    vagueness_v2  - Strategic vagueness scorer V2
    plotting      - F-series visualization
    empirical     - τ trajectory and xarray utilities
    multiverse    - Specification curve analysis
    cli           - Command-line interface for pipeline

Usage:
    from src.features import consolidate_company_snapshots
    from src.models import run_h1_early_funding, run_h2_main_growth
    from src.vagueness_v2 import StrategicVaguenessScorerV2

CLI Usage:
    python -m src.cli load-data
    python -m src.cli run-all
"""

__version__ = '2.0.0'
__author__ = 'Promise Precision Team'

# Key functions available for import:
# from src.features import (
#     consolidate_company_snapshots,
#     engineer_features,
#     filter_quantum_companies,
#     filter_transportation_companies,
# )
# from src.models import (
#     run_h1_early_funding,
#     run_h2_main_growth,
# )
# from src.vagueness_v2 import StrategicVaguenessScorerV2

__all__ = [
    'consolidate_company_snapshots',
    'engineer_features',
    'filter_quantum_companies',
    'filter_transportation_companies',
    'run_h1_early_funding',
    'run_h2_main_growth',
    'StrategicVaguenessScorerV2',
]
