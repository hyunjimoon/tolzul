#!/usr/bin/env python3
"""
Generate HTML report for moderator bake-off (Quarto-free version)
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime

def assess_risk(minority_pct):
    if minority_pct < 10:
        return "🔴 HIGH RISK"
    elif minority_pct < 20:
        return "🟡 MEDIUM RISK"
    else:
        return "🟢 LOW RISK"

def score_balance(minority_pct):
    if minority_pct < 10:
        return 0
    elif minority_pct < 20:
        return 5
    else:
        return 10

def score_significance(p_value):
    if np.isnan(p_value):
        return 0
    if p_value < 0.01:
        return 10
    elif p_value < 0.05:
        return 7
    elif p_value < 0.10:
        return 4
    else:
        return 0

def score_fit(pseudo_r2):
    return min(pseudo_r2 * 100, 10)

def score_theory(interaction_coef, expected_negative=True):
    if np.isnan(interaction_coef):
        return 0
    if expected_negative:
        return 10 if interaction_coef < 0 else 0
    else:
        return 10 if interaction_coef > 0 else 0

def main():
    print("Generating HTML bake-off report...")

    # Load data
    df = pd.read_csv("outputs/h2_analysis_dataset.csv")
    arch_coef = pd.read_csv("outputs/h2_model_architecture.csv")
    arch_metrics = pd.read_csv("outputs/h2_model_architecture_metrics.csv")
    founder_coef = pd.read_csv("outputs/h2_model_founder.csv")
    founder_metrics = pd.read_csv("outputs/h2_model_founder_metrics.csv")

    # Calculate key statistics
    hw_counts = df['is_hardware'].value_counts()
    hw_pct = (hw_counts / hw_counts.sum() * 100).to_dict()
    hw_minority = hw_pct.get(1, 0)
    hw_risk = assess_risk(hw_minority)

    serial_counts = df['is_serial'].value_counts()
    serial_pct = (serial_counts / serial_counts.sum() * 100).to_dict()
    serial_minority = serial_pct.get(1, 0)
    serial_risk = assess_risk(serial_minority)

    # Extract metrics
    arch_n = arch_metrics['nobs'].values[0]
    arch_pseudo_r2 = arch_metrics['prsquared'].values[0]
    arch_aic = arch_metrics['aic'].values[0]

    founder_n = founder_metrics['nobs'].values[0]
    founder_pseudo_r2 = founder_metrics['prsquared'].values[0]
    founder_aic = founder_metrics['aic'].values[0]

    # Extract interaction coefficients
    try:
        arch_interaction_row = arch_coef[
            arch_coef['variable'].str.contains('is_hardware', na=False) &
            arch_coef['variable'].str.contains('vagueness', na=False)
        ]
        arch_interaction_coef = arch_interaction_row['coefficient'].values[0]
        arch_interaction_p = arch_interaction_row['p_value'].values[0]
    except:
        arch_interaction_coef = np.nan
        arch_interaction_p = np.nan

    try:
        founder_interaction_row = founder_coef[
            founder_coef['variable'].str.contains('is_serial', na=False) &
            founder_coef['variable'].str.contains('vagueness', na=False)
        ]
        founder_interaction_coef = founder_interaction_row['coefficient'].values[0]
        founder_interaction_p = founder_interaction_row['p_value'].values[0]
    except:
        founder_interaction_coef = np.nan
        founder_interaction_p = np.nan

    # Calculate scores
    arch_balance_score = score_balance(hw_minority)
    arch_sig_score = score_significance(arch_interaction_p)
    arch_fit_score = score_fit(arch_pseudo_r2)
    arch_theory_score = score_theory(arch_interaction_coef)
    arch_total = (arch_balance_score * 0.4 +
                  (arch_sig_score + arch_fit_score) / 2 * 0.4 +
                  arch_theory_score * 0.2)

    founder_balance_score = score_balance(serial_minority)
    founder_sig_score = score_significance(founder_interaction_p)
    founder_fit_score = score_fit(founder_pseudo_r2)
    founder_theory_score = score_theory(founder_interaction_coef)
    founder_total = (founder_balance_score * 0.4 +
                     (founder_sig_score + founder_fit_score) / 2 * 0.4 +
                     founder_theory_score * 0.2)

    winner = "Architecture (is_hardware)" if arch_total > founder_total else "Credibility (is_serial)"

    # Generate HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moderator Bake-off Report</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
        }}
        .header p {{
            margin: 10px 0 0 0;
            opacity: 0.9;
        }}
        .section {{
            background: white;
            padding: 30px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h2 {{
            color: #667eea;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}
        h3 {{
            color: #764ba2;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #667eea;
            color: white;
            font-weight: bold;
        }}
        tr:hover {{
            background-color: #f5f5f5;
        }}
        .metric {{
            display: inline-block;
            background: #e7f3ff;
            padding: 10px 20px;
            border-radius: 5px;
            margin: 5px;
        }}
        .winner {{
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            font-size: 1.3em;
            margin: 20px 0;
        }}
        .plot {{
            text-align: center;
            margin: 20px 0;
        }}
        .plot img {{
            max-width: 100%;
            border-radius: 5px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .risk-high {{
            color: #e74c3c;
            font-weight: bold;
        }}
        .risk-medium {{
            color: #f39c12;
            font-weight: bold;
        }}
        .risk-low {{
            color: #27ae60;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Moderator Bake-off Report</h1>
        <p>Integration Cost vs Founder Credibility - Decision Memo for H2</p>
        <p>Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    </div>

    <div class="section">
        <h2>1. Executive Summary</h2>
        <p>This report compares two alternative moderators for H2:</p>
        <ul>
            <li><strong>H2-Architecture</strong>: Integration Cost (is_hardware)</li>
            <li><strong>H2-Alt (Credibility)</strong>: Founder Credibility (is_serial)</li>
        </ul>
        <p>Both models use identical specifications except for the moderator, evaluated on:</p>
        <ul>
            <li>Data Quality (40%): Distribution balance, sample sizes</li>
            <li>Statistical Evidence (40%): Significance, model fit</li>
            <li>Theory Fit (20%): Sign consistency, interpretability</li>
        </ul>
    </div>

    <div class="section">
        <h2>2. Data Quality Assessment</h2>

        <h3>Moderator Balance</h3>
        <table>
            <tr>
                <th>Moderator</th>
                <th>Minority %</th>
                <th>Minority N</th>
                <th>Majority N</th>
                <th>Risk Level</th>
            </tr>
            <tr>
                <td>is_hardware (Architecture)</td>
                <td>{hw_minority:.1f}%</td>
                <td>{hw_counts.get(1, 0):,}</td>
                <td>{hw_counts.get(0, 0):,}</td>
                <td class="risk-{'high' if hw_minority < 10 else 'medium' if hw_minority < 20 else 'low'}">{hw_risk}</td>
            </tr>
            <tr>
                <td>is_serial (Credibility)</td>
                <td>{serial_minority:.1f}%</td>
                <td>{serial_counts.get(1, 0):,}</td>
                <td>{serial_counts.get(0, 0):,}</td>
                <td class="risk-{'high' if serial_minority < 10 else 'medium' if serial_minority < 20 else 'low'}">{serial_risk}</td>
            </tr>
        </table>

        <div class="plot">
            <img src="outputs/bakeoff/univariate_distributions.png" alt="Univariate Distributions">
        </div>
    </div>

    <div class="section">
        <h2>3. H2-Architecture (is_hardware)</h2>

        <h3>Model Results</h3>
        <div class="metric">N = {int(arch_n):,}</div>
        <div class="metric">Pseudo R² = {arch_pseudo_r2:.4f}</div>
        <div class="metric">AIC = {arch_aic:.1f}</div>
        <div class="metric">Interaction Coef = {arch_interaction_coef:.4f}</div>
        <div class="metric">p-value = {arch_interaction_p:.4f}</div>

        <h3>Coefficient Table</h3>
        {arch_coef.to_html(index=False, float_format='%.4f')}

        <h3>Interaction Plot</h3>
        <div class="plot">
            <img src="outputs/bakeoff/h2_interaction_architecture.png" alt="Architecture Interaction">
        </div>
    </div>

    <div class="section">
        <h2>4. H2-Credibility (is_serial)</h2>

        <h3>Model Results</h3>
        <div class="metric">N = {int(founder_n):,}</div>
        <div class="metric">Pseudo R² = {founder_pseudo_r2:.4f}</div>
        <div class="metric">AIC = {founder_aic:.1f}</div>
        <div class="metric">Interaction Coef = {founder_interaction_coef:.4f}</div>
        <div class="metric">p-value = {founder_interaction_p:.4f}</div>

        <h3>Coefficient Table</h3>
        {founder_coef.to_html(index=False, float_format='%.4f')}

        <h3>Interaction Plot</h3>
        <div class="plot">
            <img src="outputs/bakeoff/h2_interaction_founder.png" alt="Founder Interaction">
        </div>
    </div>

    <div class="section">
        <h2>5. Head-to-Head Comparison</h2>

        <h3>Decision Scorecard</h3>
        <table>
            <tr>
                <th>Criterion</th>
                <th>Architecture</th>
                <th>Credibility</th>
            </tr>
            <tr>
                <td>Data Quality: Balance (10pt)</td>
                <td>{arch_balance_score:.1f}</td>
                <td>{founder_balance_score:.1f}</td>
            </tr>
            <tr>
                <td>Statistical: Significance (10pt)</td>
                <td>{arch_sig_score:.1f}</td>
                <td>{founder_sig_score:.1f}</td>
            </tr>
            <tr>
                <td>Statistical: Model Fit (10pt)</td>
                <td>{arch_fit_score:.1f}</td>
                <td>{founder_fit_score:.1f}</td>
            </tr>
            <tr>
                <td>Theory: Sign Consistency (10pt)</td>
                <td>{arch_theory_score:.1f}</td>
                <td>{founder_theory_score:.1f}</td>
            </tr>
            <tr style="background-color: #f0f0f0; font-weight: bold;">
                <td>TOTAL SCORE (Weighted)</td>
                <td>{arch_total:.1f}/10</td>
                <td>{founder_total:.1f}/10</td>
            </tr>
        </table>

        <h3>Detailed Metrics</h3>
        <table>
            <tr>
                <th>Dimension</th>
                <th>Architecture</th>
                <th>Credibility</th>
            </tr>
            <tr>
                <td>Sample Balance</td>
                <td>{hw_risk.split()[1]}</td>
                <td>{serial_risk.split()[1]}</td>
            </tr>
            <tr>
                <td>Minority Class %</td>
                <td>{hw_minority:.1f}%</td>
                <td>{serial_minority:.1f}%</td>
            </tr>
            <tr>
                <td>Interaction Coef</td>
                <td>{arch_interaction_coef:.4f}</td>
                <td>{founder_interaction_coef:.4f}</td>
            </tr>
            <tr>
                <td>Interaction p-value</td>
                <td>{arch_interaction_p:.4f}</td>
                <td>{founder_interaction_p:.4f}</td>
            </tr>
            <tr>
                <td>Pseudo R²</td>
                <td>{arch_pseudo_r2:.3f}</td>
                <td>{founder_pseudo_r2:.3f}</td>
            </tr>
            <tr>
                <td>AIC</td>
                <td>{arch_aic:.1f}</td>
                <td>{founder_aic:.1f}</td>
            </tr>
            <tr>
                <td>Sign Consistency</td>
                <td>{'✓' if arch_interaction_coef < 0 else '✗'}</td>
                <td>{'✓' if founder_interaction_coef < 0 else '✗'}</td>
            </tr>
        </table>
    </div>

    <div class="winner">
        <h2 style="margin: 0;">🏆 WINNER: {winner}</h2>
        <p style="margin: 10px 0 0 0;">Score: {max(arch_total, founder_total):.1f} vs {min(arch_total, founder_total):.1f} (margin: {abs(arch_total - founder_total):.1f} points)</p>
    </div>

    <div class="section">
        <h2>6. Decision & Recommendation</h2>
        <h3>Rationale</h3>
        <p><strong>Key Findings:</strong></p>
        <ul>
            <li>Architecture shows {'stronger' if arch_total > founder_total else 'weaker'} overall performance</li>
            <li>Data balance: Architecture ({hw_minority:.1f}%) vs Credibility ({serial_minority:.1f}%)</li>
            <li>Statistical significance: Architecture (p={arch_interaction_p:.4f}) vs Credibility (p={founder_interaction_p:.4f})</li>
            <li>Model fit: Architecture (R²={arch_pseudo_r2:.3f}) vs Credibility (R²={founder_pseudo_r2:.3f})</li>
        </ul>

        <h3>Next Steps</h3>
        <ol>
            <li>Adopt <strong>{winner}</strong> as primary H2 moderator for main paper</li>
            <li>Report alternative as robustness check in appendix</li>
            <li>Develop theoretical narrative emphasizing the winning moderator</li>
            <li>Create interaction plots and marginal effects for main text</li>
        </ol>
    </div>

    <div class="section">
        <h2>7. Reproducibility</h2>
        <p><strong>Analysis Pipeline:</strong></p>
        <pre style="background: #f5f5f5; padding: 15px; border-radius: 5px; overflow-x: auto;">
cd "Front/On/love(cs)/strategic ambiguity/empirics"

# Generate synthetic data (or use real data)
python generate_synthetic_data.py

# Fit bake-off models
python run_bakeoff_models.py

# Generate visualizations
python -c "
import sys; sys.path.insert(0, 'modules')
from plots import *
from pathlib import Path
import pandas as pd
outdir = Path('outputs/bakeoff')
outdir.mkdir(parents=True, exist_ok=True)
df = pd.read_csv('outputs/h2_analysis_dataset.csv')
save_univariate_distributions(df, outdir)
save_h2_interaction_architecture(df, outdir)
save_h2_interaction_founder(df, outdir)
"

# Generate report
python generate_bakeoff_report.py
        </pre>
    </div>

</body>
</html>"""

    # Save HTML
    output_path = Path("moderator_bakeoff_report.html")
    with open(output_path, 'w') as f:
        f.write(html)

    print(f"✓ Report saved to: {output_path}")
    print("\nYou can open this file in any web browser to view the full report.")

if __name__ == "__main__":
    main()
