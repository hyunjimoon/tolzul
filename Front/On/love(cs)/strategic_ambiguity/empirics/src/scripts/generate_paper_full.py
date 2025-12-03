#!/usr/bin/env python3
"""
Generate Complete Paper from Template + Data
=============================================
Uses Jinja2 templates to generate paper with auto-filled values.

Architecture:
    paper/templates/main.tex.j2  → paper/output/main.tex

Values come from:
    1. Data analysis (H1/H2 results)
    2. Descriptive statistics
    3. Sample construction metrics

Usage:
    python scripts/generate_paper_full.py --data data/processed/features_engineered.parquet
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import argparse
import json
from jinja2 import Environment, FileSystemLoader
import pandas as pd
import numpy as np
from models import run_h1_early_funding, run_h2_main_growth
from data_io import load_dataframe


class PaperGenerator:
    """Generate full paper from templates and data."""

    def __init__(self, df, template_dir='paper/templates', output_dir='paper/output'):
        self.df = df
        self.template_dir = Path(template_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Set up Jinja2
        self.env = Environment(
            loader=FileSystemLoader(self.template_dir),
            block_start_string='\\BLOCK{',
            block_end_string='}',
            variable_start_string='\\VAR{',
            variable_end_string='}',
            comment_start_string='\\#{',
            comment_end_string='}',
            line_statement_prefix='%%',
            line_comment_prefix='%#',
            trim_blocks=True,
            autoescape=False,
        )

        # Values dictionary
        self.values = {}

    def compute_descriptive_stats(self):
        """Compute Module #16: Descriptive statistics."""
        print("Computing descriptive statistics...")

        stats = {}

        # Sample sizes
        stats['n_total'] = len(self.df)
        if 'sector_fe' in self.df.columns:
            stats['n_quantum'] = len(self.df[self.df.sector_fe == 'quantum'])
            stats['n_transportation'] = len(self.df[self.df.sector_fe == 'transportation'])

        # Architecture distribution
        if 'is_hardware' in self.df.columns:
            stats['n_software'] = len(self.df[self.df.is_hardware == 0])
            stats['n_hardware'] = len(self.df[self.df.is_hardware == 1])
            stats['pct_software'] = stats['n_software'] / stats['n_total'] * 100
            stats['pct_hardware'] = stats['n_hardware'] / stats['n_total'] * 100

        # Variable means and SDs
        for var in ['vagueness', 'z_vagueness', 'early_funding_musd', 'employees']:
            if var in self.df.columns:
                stats[f'{var}_mean'] = self.df[var].mean()
                stats[f'{var}_std'] = self.df[var].std()
                stats[f'{var}_min'] = self.df[var].min()
                stats[f'{var}_max'] = self.df[var].max()

        # Growth rate
        if 'growth' in self.df.columns:
            stats['growth_rate'] = self.df['growth'].mean() * 100  # Percentage

        self.values['descriptive'] = stats
        return stats

    def run_hypothesis_tests(self):
        """Run Module #23-24: Hypothesis tests."""
        print("Running hypothesis tests...")

        # H1
        h1_result = run_h1_early_funding(self.df)
        self.values['h1'] = {
            'coef': h1_result.params.get('z_vagueness', np.nan),
            'se': h1_result.bse.get('z_vagueness', np.nan),
            'pval': h1_result.pvalues.get('z_vagueness', np.nan),
            'nobs': int(h1_result.nobs),
            'rsquared': h1_result.rsquared,
        }

        # H2
        h2_result = run_h2_main_growth(self.df)
        interaction_vars = [p for p in h2_result.params.index
                            if 'z_vagueness' in p and 'is_hardware' in p]

        self.values['h2'] = {
            'vagueness_coef': h2_result.params.get('z_vagueness', np.nan),
            'vagueness_se': h2_result.bse.get('z_vagueness', np.nan),
            'vagueness_pval': h2_result.pvalues.get('z_vagueness', np.nan),
            'interaction_coef': h2_result.params[interaction_vars[0]] if interaction_vars else np.nan,
            'interaction_se': h2_result.bse[interaction_vars[0]] if interaction_vars else np.nan,
            'interaction_pval': h2_result.pvalues[interaction_vars[0]] if interaction_vars else np.nan,
            'nobs': int(h2_result.nobs),
            'pseudo_rsquared': h2_result.prsquared,
        }

    def format_number(self, value, decimals=3):
        """Format number for LaTeX."""
        if pd.isna(value):
            return "---"
        if abs(value) < 0.001:
            return f"{value:.2e}"
        return f"{value:.{decimals}f}"

    def format_pvalue(self, pval):
        """Format p-value with stars."""
        if pd.isna(pval):
            return ""
        if pval < 0.001:
            return "***"
        elif pval < 0.01:
            return "**"
        elif pval < 0.05:
            return "*"
        elif pval < 0.10:
            return "†"
        else:
            return ""

    def render_template(self, template_name, output_name=None):
        """Render a single template."""
        if output_name is None:
            output_name = template_name.replace('.j2', '')

        template = self.env.get_template(template_name)

        # Add helper functions to context
        context = {
            **self.values,
            'format_number': self.format_number,
            'format_pvalue': self.format_pvalue,
        }

        rendered = template.render(**context)

        # Save to file
        output_path = self.output_dir / output_name
        with open(output_path, 'w') as f:
            f.write(rendered)

        print(f"✓ Rendered {template_name} → {output_path}")
        return rendered

    def generate_all(self):
        """Generate complete paper."""
        print("\n=== Generating Complete Paper ===\n")

        # Compute values
        self.compute_descriptive_stats()
        self.run_hypothesis_tests()

        # Save values to JSON for reference
        values_path = self.output_dir / 'paper_values.json'
        with open(values_path, 'w') as f:
            json.dump(self.values, f, indent=2, default=str)
        print(f"✓ Values saved to {values_path}")

        # Render templates
        # self.render_template('main.tex.j2', 'main.tex')
        # self.render_template('results.tex.j2', 'results.tex')

        print("\n=== Paper Generation Complete ===")
        print(f"Output directory: {self.output_dir}")
        print(f"Main file: {self.output_dir / 'main.tex'}")


def main():
    parser = argparse.ArgumentParser(
        description='Generate complete paper from templates'
    )
    parser.add_argument(
        '--data',
        type=str,
        default='data/processed/features_engineered.nc',
        help='Path to analysis dataset (.nc or .parquet)'
    )
    parser.add_argument(
        '--templates',
        type=str,
        default='paper/templates',
        help='Template directory'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='paper/output',
        help='Output directory'
    )

    args = parser.parse_args()

    # Load data (supports both .nc and .parquet)
    print(f"Loading data from {args.data}...")
    try:
        df = load_dataframe(args.data)
        print(f"✓ Loaded {len(df):,} observations\n")
    except FileNotFoundError:
        print(f"❌ Data file not found: {args.data}")
        sys.exit(1)

    # Generate paper
    generator = PaperGenerator(df, template_dir=args.templates, output_dir=args.output)
    generator.generate_all()


if __name__ == '__main__':
    main()
