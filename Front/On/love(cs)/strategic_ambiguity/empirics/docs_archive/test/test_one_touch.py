#!/usr/bin/env python3
"""
Quick test for one-touch execution: H3/H4 models and Figure 1/2 generation.
Uses existing h2_analysis_dataset.csv to avoid re-running full pipeline.
"""

import sys
from pathlib import Path
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

sys.path.insert(0, str(Path(__file__).parent))

from modules.models import (
    test_h1_early_funding, test_h2_main_growth,
    test_h3_early_funding_interaction, test_h4_growth_interaction
)
from modules.plots import (
    fig_reversal_from_models, fig_founder_interactions
)

def main():
    print("="*80)
    print("ONE-TOUCH EXECUTION TEST")
    print("="*80)

    # Load existing dataset
    outdir = Path("outputs")
    dataset_path = outdir / "h2_analysis_dataset.csv"

    if not dataset_path.exists():
        print(f"ERROR: {dataset_path} not found. Run full pipeline first.")
        return

    print(f"\n✓ Loading dataset: {dataset_path}")
    df = pd.read_csv(dataset_path)
    print(f"  Rows: {len(df):,}")
    print(f"  Columns: {len(df.columns)}")

    # Check required columns
    required = ['z_vagueness', 'early_funding_musd', 'growth',
                'founder_credibility', 'z_employees_log', 'founding_cohort']
    missing = [c for c in required if c not in df.columns]
    if missing:
        print(f"\nERROR: Missing columns: {missing}")
        return

    # Fit H1
    print("\n" + "="*80)
    print("H1: EARLY FUNDING")
    print("="*80)
    h1_res = test_h1_early_funding(df)
    print(f"✓ H1 fitted: R² = {h1_res.rsquared:.3f}")

    # Fit H2
    print("\n" + "="*80)
    print("H2: GROWTH × ARCHITECTURE")
    print("="*80)
    h2_res = test_h2_main_growth(df)
    print(f"✓ H2 fitted: Pseudo R² = {h2_res.prsquared:.3f}")

    # Fit H3
    print("\n" + "="*80)
    print("H3: EARLY FUNDING × FOUNDER CREDIBILITY")
    print("="*80)
    h3_res = test_h3_early_funding_interaction(df)
    print(f"✓ H3 fitted: R² = {h3_res.rsquared:.3f}")

    # Save H3 coefficients
    pd.DataFrame({
        'variable': h3_res.params.index,
        'coefficient': h3_res.params.values,
        'std_err': h3_res.bse.values,
        'stat': h3_res.tvalues.values,
        'p_value': h3_res.pvalues.values,
        'ci_lower': h3_res.conf_int()[0].values,
        'ci_upper': h3_res.conf_int()[1].values
    }).to_csv(outdir / "h3_coefficients.csv", index=False)
    print(f"✓ Saved: {outdir / 'h3_coefficients.csv'}")

    # Fit H4
    print("\n" + "="*80)
    print("H4: GROWTH × FOUNDER CREDIBILITY")
    print("="*80)
    h4_res = test_h4_growth_interaction(df)
    print(f"✓ H4 fitted: Pseudo R² = {h4_res.prsquared:.3f}")

    # Save H4 coefficients
    pd.DataFrame({
        'variable': h4_res.params.index,
        'coefficient': h4_res.params.values,
        'std_err': h4_res.bse.values,
        'stat': h4_res.tvalues.values,
        'p_value': h4_res.pvalues.values,
        'ci_lower': h4_res.conf_int()[0].values,
        'ci_upper': h4_res.conf_int()[1].values
    }).to_csv(outdir / "h4_coefficients.csv", index=False)
    print(f"✓ Saved: {outdir / 'h4_coefficients.csv'}")

    # Generate Figures
    print("\n" + "="*80)
    print("GENERATING FIGURES")
    print("="*80)

    figures_dir = outdir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    # Figure 1: The Reversal
    print("\nGenerating Figure 1: The Reversal...")
    try:
        fig_reversal_from_models(df, h1_res, h2_res, figures_dir)
        print("✓ Figure 1 generated successfully")
    except Exception as e:
        print(f"⚠️ Error generating Figure 1: {e}")
        import traceback
        traceback.print_exc()

    # Figure 2: Founder Interactions
    print("\nGenerating Figure 2a/2b: Founder Interactions...")
    try:
        fig_founder_interactions(df, h3_res, h4_res, figures_dir)
        print("✓ Figure 2a/2b generated successfully")
    except Exception as e:
        print(f"⚠️ Error generating Figure 2: {e}")
        import traceback
        traceback.print_exc()

    print("\n" + "="*80)
    print("TEST COMPLETE")
    print("="*80)

    print("\nGenerated Files:")
    print("\nCoefficient Tables:")
    for p in sorted(outdir.glob('h*.csv')):
        print(f"  - {p.name}")
    print("\nFigures:")
    for p in sorted(figures_dir.glob('*.png')):
        print(f"  - figures/{p.name}")

if __name__ == "__main__":
    main()
