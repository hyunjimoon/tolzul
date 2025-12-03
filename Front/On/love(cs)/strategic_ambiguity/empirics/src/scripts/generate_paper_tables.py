#!/usr/bin/env python3
"""
Generate LaTeX Tables for Paper
================================
Auto-generate publication-ready tables from regression results.

Usage:
    python scripts/generate_paper_tables.py --output outputs/paper_tables/
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import argparse
import pandas as pd
from models import run_h1_early_funding, run_h2_main_growth
from data_io import load_dataframe


def format_coef_se(coef, se, pval, stars=True):
    """
    Format coefficient with standard error and significance stars.

    Args:
        coef: Coefficient value
        se: Standard error
        pval: P-value
        stars: Whether to add significance stars

    Returns:
        Formatted string: "0.234*** (0.089)"
    """
    # Significance stars
    if stars:
        if pval < 0.01:
            star = '***'
        elif pval < 0.05:
            star = '**'
        elif pval < 0.10:
            star = '*'
        else:
            star = ''
    else:
        star = ''

    # Format: coefficient with stars, SE in parentheses
    return f"{coef:.3f}{star}\n({se:.3f})"


def generate_table1_h1(df, output_path='outputs/paper_tables/table1_h1.tex'):
    """
    Generate Table 1: H1 Early Funding Regression.

    Module #23: Early funding penalty from vagueness

    Args:
        df: Analysis dataset
        output_path: Where to save LaTeX file

    Returns:
        LaTeX table string
    """
    print("Generating Table 1: H1 Early Funding Regression...")

    result = run_h1_early_funding(df)

    # Extract key coefficients
    params = result.params
    bse = result.bse
    pvalues = result.pvalues

    # Build LaTeX table manually for control
    latex = r"""
\begin{table}[htbp]
\centering
\caption{Strategic Vagueness and Early Funding (H1)}
\label{tab:h1_early_funding}
\begin{tabular}{lc}
\toprule
& \textbf{Early Funding (M\$)} \\
\midrule
"""

    # Add coefficients
    for var in ['z_vagueness', 'z_employees_log', 'founder_serial',
                'is_hardware', 'z_firm_age']:
        if var in params:
            formatted = format_coef_se(params[var], bse[var], pvalues[var])
            var_label = var.replace('_', ' ').title()
            latex += f"{var_label} & {formatted} \\\\\n"

    # Add fixed effects
    latex += r"\midrule"
    latex += "\nSector FE & Yes \\\\\n"
    latex += "Cohort FE & Yes \\\\\n"

    # Add model stats
    latex += r"\midrule"
    latex += f"\nObservations & {int(result.nobs):,} \\\\\n"
    latex += f"R-squared & {result.rsquared:.3f} \\\\\n"
    latex += f"Adj. R-squared & {result.rsquared_adj:.3f} \\\\\n"

    latex += r"""\bottomrule
\end{tabular}
\begin{tablenotes}
\small
\item Notes: Standard errors in parentheses. *** p<0.01, ** p<0.05, * p<0.10.
\item DV: Early funding amount in millions USD.
\item IV: Strategic vagueness (z-scored).
\end{tablenotes}
\end{table}
"""

    # Save to file
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(latex)

    print(f"✓ Table 1 saved to {output_path}")
    return latex


def generate_table2_h2(df, output_path='outputs/paper_tables/table2_h2.tex'):
    """
    Generate Table 2: H2 Later Success Logit Regression.

    Module #24-25: Later success benefit with V×F interaction

    Args:
        df: Analysis dataset
        output_path: Where to save LaTeX file

    Returns:
        LaTeX table string
    """
    print("Generating Table 2: H2 Later Success Regression...")

    result = run_h2_main_growth(df)

    params = result.params
    bse = result.bse
    pvalues = result.pvalues

    latex = r"""
\begin{table}[htbp]
\centering
\caption{Strategic Vagueness, Flexibility, and Later Success (H2)}
\label{tab:h2_later_success}
\begin{tabular}{lc}
\toprule
& \textbf{Later Success (Logit)} \\
\midrule
"""

    # Main effects
    for var in ['z_vagueness', 'is_hardware', 'z_employees_log', 'founder_serial']:
        if var in params:
            formatted = format_coef_se(params[var], bse[var], pvalues[var])
            var_label = var.replace('_', ' ').title()
            latex += f"{var_label} & {formatted} \\\\\n"

    # Interaction term (find it)
    interaction_vars = [p for p in params.index
                        if 'z_vagueness' in p and 'is_hardware' in p]
    if interaction_vars:
        var = interaction_vars[0]
        formatted = format_coef_se(params[var], bse[var], pvalues[var])
        latex += f"Vagueness × Hardware & {formatted} \\\\\n"

    # Fixed effects
    latex += r"\midrule"
    latex += "\nCohort FE & Yes \\\\\n"

    # Model stats
    latex += r"\midrule"
    latex += f"\nObservations & {int(result.nobs):,} \\\\\n"
    latex += f"Pseudo R-squared & {result.prsquared:.3f} \\\\\n"
    latex += f"Log-likelihood & {result.llf:.1f} \\\\\n"

    latex += r"""\bottomrule
\end{tabular}
\begin{tablenotes}
\small
\item Notes: Standard errors in parentheses. *** p<0.01, ** p<0.05, * p<0.10.
\item DV: Later success (1 = achieved Series B+ within window).
\item IV: Strategic vagueness (z-scored), is\_hardware (1=hardware/integrated, 0=software).
\item Interaction term tests H2a: flexibility moderates vagueness effect.
\end{tablenotes}
\end{table}
"""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(latex)

    print(f"✓ Table 2 saved to {output_path}")
    return latex


def generate_descriptive_stats(df, output_path='outputs/paper_tables/table_descriptive.tex'):
    """
    Generate Descriptive Statistics Table.

    Module #16: Variables overview (E/L/V/F)

    Args:
        df: Analysis dataset
        output_path: Where to save LaTeX file

    Returns:
        LaTeX table string
    """
    print("Generating Descriptive Statistics Table...")

    # Select key variables
    vars_of_interest = ['E', 'L', 'V', 'F', 'z_vagueness',
                        'early_funding_musd', 'growth']

    # Filter to available columns
    available_vars = [v for v in vars_of_interest if v in df.columns]

    stats = df[available_vars].describe().T

    latex = r"""
\begin{table}[htbp]
\centering
\caption{Descriptive Statistics}
\label{tab:descriptive_stats}
\begin{tabular}{lrrrrr}
\toprule
\textbf{Variable} & \textbf{N} & \textbf{Mean} & \textbf{Std} & \textbf{Min} & \textbf{Max} \\
\midrule
"""

    for var in available_vars:
        if var in stats.index:
            row = stats.loc[var]
            var_label = var.replace('_', ' ').title()
            latex += f"{var_label} & {row['count']:.0f} & {row['mean']:.2f} & " \
                     f"{row['std']:.2f} & {row['min']:.2f} & {row['max']:.2f} \\\\\n"

    latex += r"""\bottomrule
\end{tabular}
\begin{tablenotes}
\small
\item Notes: E = Early event (Series A at baseline), L = Later success (Series B+ at endpoint),
\item V = Vagueness score [0-100], F = Flexibility (1 - is\_hardware).
\end{tablenotes}
\end{table}
"""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(latex)

    print(f"✓ Descriptive stats saved to {output_path}")
    return latex


def main():
    """Main function to generate all paper tables."""
    parser = argparse.ArgumentParser(
        description='Generate LaTeX tables for paper'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='outputs/paper_tables/',
        help='Output directory for LaTeX files'
    )
    parser.add_argument(
        '--data',
        type=str,
        default='data/processed/features_engineered.nc',
        help='Path to analysis dataset (.nc or .parquet)'
    )

    args = parser.parse_args()

    # Load data (supports both .nc and .parquet)
    print(f"Loading data from {args.data}...")
    try:
        df = load_dataframe(args.data)
        print(f"✓ Loaded {len(df):,} observations")
    except FileNotFoundError:
        print(f"❌ Data file not found: {args.data}")
        print("   Run: python -m src.cli engineer-features")
        sys.exit(1)

    # Generate tables
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        # Table 1: H1
        generate_table1_h1(df, output_dir / 'table1_h1.tex')

        # Table 2: H2
        generate_table2_h2(df, output_dir / 'table2_h2.tex')

        # Descriptive stats
        generate_descriptive_stats(df, output_dir / 'table_descriptive.tex')

        print("\n✅ All tables generated successfully!")
        print(f"   Output directory: {output_dir}")

    except Exception as e:
        print(f"\n❌ Error generating tables: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
