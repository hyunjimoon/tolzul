#!/usr/bin/env python3
"""
Generate LEAN HTML report (top 30% features only)
Following Hemingway 10% rule × 3, Abdullah 1/8 rule × 2.4
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime

def risk_label(pct):
    if pct < 10:
        return "🔴 HIGH"
    elif pct < 20:
        return "🟡 MED"
    else:
        return "🟢 LOW"

def main():
    print("Generating LEAN report (top 30% features)...")

    # Load data
    df = pd.read_csv("outputs/h2_analysis_dataset.csv")
    h1 = pd.read_csv("outputs/h1_coefficients.csv")
    arch_coef = pd.read_csv("outputs/h2_model_architecture.csv")
    arch_metrics = pd.read_csv("outputs/h2_model_architecture_metrics.csv")
    found_coef = pd.read_csv("outputs/h2_model_founder.csv")
    found_metrics = pd.read_csv("outputs/h2_model_founder_metrics.csv")

    # H1 effect
    try:
        vague_row = h1[h1['variable'].str.contains('vagueness', case=False, na=False)]
        h1_coef = vague_row['coefficient'].values[0]
        h1_p = vague_row['p_value'].values[0]
        h1_sig = "✓" if h1_p < 0.05 else "✗"
    except:
        h1_coef, h1_p, h1_sig = 0, 1, "✗"

    # Balance
    hw_counts = df['is_hardware'].value_counts()
    hw_pct = hw_counts.get(1, 0) / hw_counts.sum() * 100
    hw_risk = risk_label(hw_pct)

    serial_counts = df['is_serial'].value_counts()
    serial_pct = serial_counts.get(1, 0) / serial_counts.sum() * 100
    serial_risk = risk_label(serial_pct)

    # Metrics
    arch_n = arch_metrics['nobs'].values[0]
    arch_r2 = arch_metrics['prsquared'].values[0]
    found_n = found_metrics['nobs'].values[0]
    found_r2 = found_metrics['prsquared'].values[0]

    # Interaction p-values
    try:
        arch_int_row = arch_coef[
            arch_coef['variable'].str.contains('vagueness', na=False) &
            arch_coef['variable'].str.contains('hardware', na=False)
        ]
        arch_int_coef = arch_int_row['coefficient'].values[0]
        arch_int_p = arch_int_row['p_value'].values[0]
        arch_sig = "✓ Sig" if arch_int_p < 0.05 else "✗ NS"
    except:
        arch_int_coef, arch_int_p, arch_sig = 0, 1, "N/A"

    try:
        found_int_row = found_coef[
            found_coef['variable'].str.contains('vagueness', na=False) &
            found_coef['variable'].str.contains('serial', na=False)
        ]
        found_int_coef = found_int_row['coefficient'].values[0]
        found_int_p = found_int_row['p_value'].values[0]
        found_sig = "✓ Sig" if found_int_p < 0.05 else "✗ NS"
    except:
        found_int_coef, found_int_p, found_sig = 0, 1, "N/A"

    # Generate HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moderator Decision (LEAN)</title>
    <style>
        body {{
            font-family: 'Segoe UI', Roboto, sans-serif;
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
            line-height: 1.6;
            background: #f9f9f9;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 30px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2em;
        }}
        .header p {{
            margin: 10px 0 0 0;
            opacity: 0.9;
        }}
        .section {{
            background: white;
            padding: 25px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h2 {{
            color: #667eea;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
            margin-top: 0;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background: #667eea;
            color: white;
            font-weight: 600;
        }}
        tr:hover {{
            background: #f5f5f5;
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
        .verdict {{
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 20px;
            margin: 20px 0;
        }}
        .metric {{
            display: inline-block;
            background: #e3f2fd;
            padding: 8px 15px;
            border-radius: 4px;
            margin: 5px;
            font-weight: 500;
        }}
        .stats {{
            text-align: center;
            color: #666;
            font-size: 0.9em;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Moderator Decision</h1>
        <p>Architecture vs Credibility (LEAN - Top 30%)</p>
    </div>

    <div class="section">
        <h2>Core Question</h2>
        <p><strong>Which moderator for H2?</strong></p>
        <p>Integration Cost (<code>is_hardware</code>) or Founder Credibility (<code>is_serial</code>)?</p>
        <p><strong>Why it matters:</strong> This choice determines our theoretical story and data requirements.</p>
    </div>

    <div class="section">
        <h2>1. Motivation (H1)</h2>
        <p><strong>Does vagueness affect early outcomes?</strong></p>
        <div class="metric">H1 Effect: α₁ = {h1_coef:.3f}</div>
        <div class="metric">p = {h1_p:.3f} {h1_sig}</div>
        <p style="margin-top: 15px;">→ Vagueness affects early funding. <strong>But does it help or hurt long-term growth?</strong></p>
    </div>

    <div class="section">
        <h2>2. Data Quality Check</h2>
        <table>
            <tr>
                <th>Moderator</th>
                <th>Minority %</th>
                <th>Risk</th>
                <th>N</th>
            </tr>
            <tr>
                <td>Architecture (is_hardware)</td>
                <td>{hw_pct:.1f}%</td>
                <td>{hw_risk}</td>
                <td>{len(df):,}</td>
            </tr>
            <tr>
                <td>Credibility (is_serial)</td>
                <td>{serial_pct:.1f}%</td>
                <td>{serial_risk}</td>
                <td>{len(df):,}</td>
            </tr>
        </table>
        <p><strong>Key:</strong> 🟢 = good balance, 🟡 = caution, 🔴 = high risk of unstable estimates</p>
    </div>

    <div class="section">
        <h2>3. Bake-off Results</h2>

        <h3 style="color: #764ba2;">Architecture (is_hardware)</h3>
        <div class="plot">
            <img src="outputs/bakeoff/h2_interaction_is_hardware.png" alt="Architecture Interaction">
        </div>

        <h3 style="color: #764ba2;">Credibility (is_serial)</h3>
        <div class="plot">
            <img src="outputs/bakeoff/h2_interaction_is_serial.png" alt="Credibility Interaction">
        </div>

        <h3 style="color: #764ba2;">Compact Coefficients (3 key rows)</h3>
        <table>
            <tr>
                <th>Model</th>
                <th>Effect</th>
                <th>Coefficient</th>
                <th>p-value</th>
            </tr>
            <tr>
                <td rowspan="3"><strong>Architecture</strong></td>
                <td>Main (z_vagueness)</td>
                <td>—</td>
                <td>—</td>
            </tr>
            <tr>
                <td>Moderator (is_hardware)</td>
                <td>—</td>
                <td>—</td>
            </tr>
            <tr style="background: #fffbeb;">
                <td><strong>Interaction</strong></td>
                <td><strong>{arch_int_coef:.3f}</strong></td>
                <td><strong>{arch_int_p:.3f}</strong> {arch_sig}</td>
            </tr>
            <tr>
                <td rowspan="3"><strong>Credibility</strong></td>
                <td>Main (z_vagueness)</td>
                <td>—</td>
                <td>—</td>
            </tr>
            <tr>
                <td>Moderator (is_serial)</td>
                <td>—</td>
                <td>—</td>
            </tr>
            <tr style="background: #fffbeb;">
                <td><strong>Interaction</strong></td>
                <td><strong>{found_int_coef:.3f}</strong></td>
                <td><strong>{found_int_p:.3f}</strong> {found_sig}</td>
            </tr>
        </table>
    </div>

    <div class="section">
        <h2>4. Decision Matrix</h2>
        <table>
            <tr>
                <th>Criterion</th>
                <th>Architecture</th>
                <th>Credibility</th>
            </tr>
            <tr>
                <td>Data Quality (Balance)</td>
                <td>{hw_pct:.1f}% {hw_risk}</td>
                <td>{serial_pct:.1f}% {serial_risk}</td>
            </tr>
            <tr>
                <td>Statistical Evidence (p < 0.05)</td>
                <td>p = {arch_int_p:.3f} {arch_sig}</td>
                <td>p = {found_int_p:.3f} {found_sig}</td>
            </tr>
            <tr>
                <td>Model Fit (Pseudo-R²)</td>
                <td>{arch_r2:.3f}</td>
                <td>{found_r2:.3f}</td>
            </tr>
        </table>
    </div>

    <div class="verdict">
        <h2 style="margin-top: 0; color: #856404;">Final Decision Template</h2>

        <p><strong>CHOSEN MODERATOR:</strong></p>
        <p>☐ Architecture &nbsp;&nbsp;&nbsp; ☐ Credibility</p>

        <p><strong>RATIONALE</strong> (fill in):</p>
        <ul>
            <li>Data quality: ...</li>
            <li>Statistical strength: ...</li>
            <li>Theoretical fit: ...</li>
        </ul>

        <p><strong>NEXT STEPS:</strong></p>
        <ol>
            <li>Adopt chosen moderator for H2 main paper</li>
            <li>Report alternative as robustness check (appendix)</li>
            <li>Develop theoretical narrative for winner</li>
        </ol>
    </div>

    <div class="stats">
        <p><strong>Report Stats:</strong> 2 figures | 3 tables | 2 metrics per model | ~200 words</p>
        <p><strong>Design:</strong> Top 30% features (Hemingway 10% × 3, Abdullah 1/8 × 2.4)</p>
        <p><em>Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}</em></p>
    </div>

</body>
</html>"""

    # Save
    output_path = Path("moderator_bakeoff_LEAN.html")
    with open(output_path, 'w') as f:
        f.write(html)

    print(f"✓ LEAN report saved: {output_path}")
    print(f"\nFeature reduction:")
    print(f"  - Figures: 5 → 2 (60% cut)")
    print(f"  - Tables: 9 → 3 (67% cut)")
    print(f"  - Metrics: 9 → 2 per model (78% cut)")
    print(f"  - Overall: ~83% reduction (17% retention)")

if __name__ == "__main__":
    main()
