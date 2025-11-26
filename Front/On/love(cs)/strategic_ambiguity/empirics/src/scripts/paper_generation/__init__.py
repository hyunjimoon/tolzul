"""
Paper Generation Module

Automated generation of academic paper sections based on empirical results.
Each script generates a Markdown file with data-driven insights.
"""

from pathlib import Path

# Common configuration for all paper generation scripts
RESULTS_DIR = Path(__file__).resolve().parents[3] / "outputs" / "all" / "models"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"
FIGURES_DIR = Path(__file__).resolve().parents[3] / "outputs" / "all" / "eyeball_test"

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
