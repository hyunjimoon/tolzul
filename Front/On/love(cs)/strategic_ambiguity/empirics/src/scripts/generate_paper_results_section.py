#!/usr/bin/env python3
"""
Generate Complete Results Section for Paper
============================================
Auto-generate Module #23-27 (Results) with tables, figures, and text snippets.

Output:
    - paper/results_auto.tex (LaTeX fragment to \input)
    - paper/tables/*.tex (individual tables)
    - paper/figures/*.pdf (all figures)
    - paper/results_values.json (numerical values for text)

Usage:
    python scripts/generate_paper_results_section.py --data data/processed/features_engineered.parquet
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import argparse
import json
import pandas as pd
import numpy as np
from src.models import run_h1_early_funding, run_h2_main_growth
from src.features import preprocess_for_h2
from src.data_io import load_dataframe


class PaperResultsGenerator:
    """Generate complete Results section from data."""

    def __init__(self, df, output_dir='paper'):
        self.df = df
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        # Create subdirectories
        (self.output_dir / 'tables').mkdir(exist_ok=True)
        (self.output_dir / 'figures').mkdir(exist_ok=True)

        # Store results
        self.h1_result = None
        self.h2_result = None
        self.values = {}  # Numerical values for text

    def run_analyses(self):
        """Run H1 and H2 analyses."""
        print("Running H1 (Early Funding)...")
        self.h1_result = run_h1_early_funding(self.df)

        print("Running H2 (Later Success)...")
        self.h2_result = run_h2_main_growth(self.df)

        # Extract key values
        self.extract_key_values()

    def extract_key_values(self):
        """Extract numerical values for text snippets."""
        # H1 values
        if 'z_vagueness' in self.h1_result.params:
            self.values['h1_coef'] = self.h1_result.params['z_vagueness']
            self.values['h1_se'] = self.h1_result.bse['z_vagueness']
            self.values['h1_pval'] = self.h1_result.pvalues['z_vagueness']
            self.values['h1_tstat'] = self.h1_result.tvalues['z_vagueness']
        else:
            self.values['h1_coef'] = np.nan
            self.values['h1_se'] = np.nan
            self.values['h1_pval'] = np.nan

        self.values['h1_nobs'] = int(self.h1_result.nobs)
        self.values['h1_rsquared'] = self.h1_result.rsquared

        # H2 values
        if 'z_vagueness' in self.h2_result.params:
            self.values['h2_vagueness_coef'] = self.h2_result.params['z_vagueness']
            self.values['h2_vagueness_se'] = self.h2_result.bse['z_vagueness']
            self.values['h2_vagueness_pval'] = self.h2_result.pvalues['z_vagueness']

        # Interaction term
        interaction_vars = [p for p in self.h2_result.params.index
                            if 'z_vagueness' in p and 'is_hardware' in p]
        if interaction_vars:
            var = interaction_vars[0]
            self.values['h2_interaction_coef'] = self.h2_result.params[var]
            self.values['h2_interaction_se'] = self.h2_result.bse[var]
            self.values['h2_interaction_pval'] = self.h2_result.pvalues[var]
        else:
            self.values['h2_interaction_coef'] = np.nan
            self.values['h2_interaction_se'] = np.nan
            self.values['h2_interaction_pval'] = np.nan

        self.values['h2_nobs'] = int(self.h2_result.nobs)
        self.values['h2_pseudo_rsquared'] = self.h2_result.prsquared

        # Statistical significance indicators
        self.values['h1_sig'] = self.get_significance_stars(self.values['h1_pval'])
        self.values['h2_vag_sig'] = self.get_significance_stars(self.values['h2_vagueness_pval'])
        self.values['h2_int_sig'] = self.get_significance_stars(self.values['h2_interaction_pval'])

    def get_significance_stars(self, pval):
        """Convert p-value to significance stars."""
        if pd.isna(pval):
            return ''
        if pval < 0.001:
            return '***'
        elif pval < 0.01:
            return '**'
        elif pval < 0.05:
            return '*'
        elif pval < 0.10:
            return '†'
        else:
            return ''

    def generate_table1_latex(self):
        """Generate Table 1: H1 Early Funding."""
        latex = r"""\begin{threeparttable}[htb!]
\caption{Model A: Early Funding (OLS)}
\label{tab:T1_ModelA_EarlyFunding}
\begin{tabular}{l c}
\toprule
 & Early funding (M USD) \\
\midrule
"""

        # Add coefficients
        params = self.h1_result.params
        bse = self.h1_result.bse
        pvalues = self.h1_result.pvalues

        # Intercept
        if 'Intercept' in params:
            sig = self.get_significance_stars(pvalues['Intercept'])
            latex += f"Constant & {params['Intercept']:.2e}{sig} ({bse['Intercept']:.2e}) \\\\\n"

        # Vagueness
        if 'z_vagueness' in params:
            sig = self.get_significance_stars(pvalues['z_vagueness'])
            latex += f"Vagueness (z) & {params['z_vagueness']:.2e}{sig} ({bse['z_vagueness']:.2e}) \\\\\n"

        # Employees
        if 'z_employees_log' in params:
            sig = self.get_significance_stars(pvalues['z_employees_log'])
            latex += f"Employees (log, z) & {params['z_employees_log']:.2e}{sig} ({bse['z_employees_log']:.2e}) \\\\\n"

        # Model stats
        latex += r"""\midrule
Sector FE  & Yes \\
"""
        latex += f"N          & {int(self.h1_result.nobs):,} \\\\\n"
        latex += f"$R^2$      & {self.h1_result.rsquared:.3f} \\\\\n"

        latex += r"""\bottomrule
\end{tabular}
\begin{tablenotes}[flushleft]
\item Notes: Coefficients with robust standard errors in parentheses.
Significance: $^{***}p<0.001$, $^{**}p<0.01$, $^{*}p<0.05$, $^{\dagger}p<0.10$.
\end{tablenotes}
\end{threeparttable}
"""

        # Save to file
        output_path = self.output_dir / 'tables' / 'table1_h1.tex'
        with open(output_path, 'w') as f:
            f.write(latex)

        print(f"✓ Table 1 saved to {output_path}")
        return latex

    def generate_table2_latex(self):
        """Generate Table 2: H2 Later Success."""
        latex = r"""\begin{threeparttable}[htb!]
\caption{Model B: Later Success (Logit)}
\label{tab:T2_ModelB_LaterSuccess}
\begin{tabular}{l c}
\toprule
 & Series B+ (log-odds) \\
\midrule
"""

        params = self.h2_result.params
        bse = self.h2_result.bse
        pvalues = self.h2_result.pvalues

        # Add coefficients in order
        for var in ['Intercept', 'z_vagueness', 'is_hardware']:
            if var in params:
                sig = self.get_significance_stars(pvalues[var])
                var_label = var.replace('_', ' ').replace('Intercept', 'Constant').title()
                latex += f"{var_label} & {params[var]:.3f}{sig} ({bse[var]:.3f}) \\\\\n"

        # Interaction
        interaction_vars = [p for p in params.index
                            if 'z_vagueness' in p and 'is_hardware' in p]
        if interaction_vars:
            var = interaction_vars[0]
            sig = self.get_significance_stars(pvalues[var])
            latex += f"Vagueness × Hardware & {params[var]:.3f}{sig} ({bse[var]:.3f}) \\\\\n"

        # Model stats
        latex += r"""\midrule
Cohort FE & Yes \\
"""
        latex += f"N & {int(self.h2_result.nobs):,} \\\\\n"
        latex += f"Pseudo-$R^2$ & {self.h2_result.prsquared:.3f} \\\\\n"

        latex += r"""\bottomrule
\end{tabular}
\begin{tablenotes}[flushleft]
\item Notes: Logit coefficients (log-odds) with robust standard errors in parentheses.
Significance: $^{***}p<0.001$, $^{**}p<0.01$, $^{*}p<0.05$, $^{\dagger}p<0.10$.
\end{tablenotes}
\end{threeparttable}
"""

        output_path = self.output_dir / 'tables' / 'table2_h2.tex'
        with open(output_path, 'w') as f:
            f.write(latex)

        print(f"✓ Table 2 saved to {output_path}")
        return latex

    def generate_results_text(self):
        """Generate Results section text with embedded values."""
        text = r"""% Auto-generated Results section
% Module #23-27

\section{Results}

\subsection{H1: Early Funding (OLS)}
% Paragraph 23: H1 results
"""

        # H1 interpretation (data-driven)
        h1_coef = self.values['h1_coef']
        h1_pval = self.values['h1_pval']
        h1_sig = self.values['h1_sig']

        if h1_pval < 0.05:
            if h1_coef < 0:
                text += f"""For H1, the coefficient on vagueness is \\textcolor{{blue}}{{statistically significant and negative}}: $\\hat\\beta_1 \\approx {h1_coef:.2e}$ ($p={h1_pval:.3f}$). This supports the information cost hypothesis: vague promises reduce early funding by preventing investors from updating beliefs through verifiable milestones.

"""
            else:
                text += f"""For H1, the coefficient on vagueness is unexpectedly \\textcolor{{blue}}{{positive}}: $\\hat\\beta_1 \\approx {h1_coef:.2e}$ ($p={h1_pval:.3f}$). This contradicts the information cost hypothesis and warrants further investigation.

"""
        else:
            text += f"""For H1, the coefficient on vagueness is \\textcolor{{blue}}{{statistically indistinguishable from zero}}: $\\hat\\beta_1 \\approx {h1_coef:.2e}$ ($p={h1_pval:.3f}$). This suggests that promise vagueness does not significantly impact early-stage funding in this sample.

"""

        text += r"""\input{paper/tables/table1_h1.tex}

\subsection{H2: Growth to Series B+ (Logit)}
% Paragraph 24: H2 main effect
"""

        # H2 interpretation
        h2_coef = self.values['h2_vagueness_coef']
        h2_pval = self.values['h2_vagueness_pval']
        h2_int_coef = self.values['h2_interaction_coef']
        h2_int_pval = self.values['h2_interaction_pval']

        if h2_pval < 0.05:
            direction = "negative" if h2_coef < 0 else "positive"
            text += f"""For H2, we find a statistically \\textcolor{{blue}}{{significant {direction} main effect of vagueness on growth}}: $\\hat\\alpha_1 \\approx {h2_coef:.4f}$ ($p={h2_pval:.4f}$).
"""
        else:
            text += f"""For H2, the main effect of vagueness is not statistically significant: $\\hat\\alpha_1 \\approx {h2_coef:.4f}$ ($p={h2_pval:.4f}$).
"""

        # Interaction
        if h2_int_pval < 0.10:
            direction = "negative" if h2_int_coef < 0 else "positive"
            text += f"""The interaction with hardware is {direction} and statistically significant at the 10\\% level: $\\hat\\alpha_3 \\approx {h2_int_coef:.4f}$ ($p={h2_int_pval:.3f}$). This suggests that exercisability moderates the effect of vagueness on later success.
"""
        else:
            text += f"""The interaction with hardware is \\textcolor{{blue}}{{not statistically significant}}: $\\hat\\alpha_3 \\approx {h2_int_coef:.4f}$ ($p={h2_int_pval:.3f}$).
"""

        text += r"""
\input{paper/tables/table2_h2.tex}

% Figures
\begin{figure}[p]
    \centering
    \includegraphics[width=0.9\linewidth]{paper/figures/fig2_early_funding.pdf}
    \caption{Early Funding vs. Vagueness (H1)}
    \label{fig:Fig2_EVF}
\end{figure}

\begin{figure}[p]
    \centering
    \includegraphics[width=0.9\linewidth]{paper/figures/fig3_later_success.pdf}
    \caption{Later Success vs. Vagueness by Exercisability (H2)}
    \label{fig:Fig3_LVF}
\end{figure}
"""

        # Save to file
        output_path = self.output_dir / 'results_auto.tex'
        with open(output_path, 'w') as f:
            f.write(text)

        print(f"✓ Results section saved to {output_path}")
        return text

    def save_values_json(self):
        """Save numerical values to JSON for reference."""
        output_path = self.output_dir / 'results_values.json'
        with open(output_path, 'w') as f:
            json.dump(self.values, f, indent=2, default=str)

        print(f"✓ Values saved to {output_path}")

    def generate_all(self):
        """Generate complete Results section."""
        print("\n=== Generating Complete Results Section ===\n")

        # Run analyses
        self.run_analyses()

        # Generate tables
        self.generate_table1_latex()
        self.generate_table2_latex()

        # Generate text
        self.generate_results_text()

        # Save values
        self.save_values_json()

        print("\n=== Results Section Complete ===")
        print(f"Main file: {self.output_dir / 'results_auto.tex'}")
        print(f"Tables: {self.output_dir / 'tables'}/*.tex")
        print(f"Values: {self.output_dir / 'results_values.json'}")
        print("\nTo include in your paper:")
        print(r"    \input{paper/results_auto.tex}")


def main():
    parser = argparse.ArgumentParser(
        description='Generate complete Results section for paper'
    )
    parser.add_argument(
        '--data',
        type=str,
        default='data/processed/features_engineered.nc',
        help='Path to analysis dataset (.nc or .parquet)'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='paper',
        help='Output directory'
    )

    args = parser.parse_args()

    # Load data (supports both .nc and .parquet)
    print(f"Loading data from {args.data}...")
    try:
        df = load_dataframe(args.data)
        print(f"✓ Loaded {len(df):,} observations")
        
        # Preprocess for H2 (compute z_vagueness, etc.)
        print("Preprocessing data (z-scoring, etc.)...")
        df = preprocess_for_h2(df)
        print("✓ Preprocessing complete\n")
    except FileNotFoundError:
        print(f"❌ Data file not found: {args.data}")
        print("   Run: python -m src.cli engineer-features")
        sys.exit(1)

    # Generate Results section
    generator = PaperResultsGenerator(df, output_dir=args.output)
    generator.generate_all()


if __name__ == '__main__':
    main()
