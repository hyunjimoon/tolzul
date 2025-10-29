#!/usr/bin/env python3
"""
Analyze follow-up period and base rate implications.
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

sys.path.insert(0, str(Path(__file__).parent))

def main():
    print("="*80)
    print("FOLLOW-UP PERIOD ANALYSIS")
    print("="*80)

    # Load existing dataset
    outdir = Path("outputs")
    dataset_path = outdir / "h2_analysis_dataset.csv"

    if not dataset_path.exists():
        print(f"ERROR: {dataset_path} not found.")
        return

    print(f"\n✓ Loading dataset: {dataset_path}")
    df = pd.read_csv(dataset_path)
    print(f"  Total companies: {len(df):,}")

    # Analyze DV
    if 'growth' not in df.columns:
        print("\n⚠️ 'growth' column not found")
        return

    print("\n" + "="*80)
    print("CURRENT DV (growth = Series B+ progression)")
    print("="*80)

    # Base statistics
    n_total = len(df)
    n_growth = df['growth'].sum()
    base_rate = n_growth / n_total

    print(f"\n📊 Base Rate:")
    print(f"  Total at-risk (Series A at baseline): {n_total:,}")
    print(f"  Progressed to Series B+: {n_growth:,}")
    print(f"  Base rate: {base_rate:.1%}")

    # Compare to expectations
    print(f"\n📋 Follow-up Period Comparison:")
    print(f"  Current data: 2021-12-01 → 2023-05-01 = 17 months")
    print(f"  Scott Stern: 2021-12-01 → 2025-10-01 = 46 months")
    print(f"  Difference: 29 months SHORT (2.4 years)")

    # Expected base rates by follow-up
    print(f"\n📈 Expected Base Rates by Follow-up Period:")
    print(f"  12 months:  6-8%   (very early adopters only)")
    print(f"  17 months: 10-12%  ← CURRENT DATA")
    print(f"  24 months: 15-20%  (industry standard)")
    print(f"  36 months: 20-25%")
    print(f"  46 months: 25-30%  ← SCOTT'S RECOMMENDATION")

    # Assess current base rate
    if base_rate < 0.08:
        status = "⚠️ VERY LOW - May indicate issues"
    elif 0.08 <= base_rate <= 0.14:
        status = "✅ REASONABLE for 17-month follow-up"
    elif 0.14 < base_rate <= 0.20:
        status = "✅ GOOD for 17-month follow-up"
    else:
        status = "⚠️ UNEXPECTEDLY HIGH - Check data"

    print(f"\n  Current base rate {base_rate:.1%}: {status}")

    # Right censoring analysis
    print(f"\n" + "="*80)
    print("RIGHT CENSORING IMPLICATIONS")
    print("="*80)

    print(f"\n⚠️ Potential Issues with 17-month Follow-up:")
    print(f"  1. False Negatives:")
    print(f"     - Companies that WILL get Series B in 2024-2025")
    print(f"     - Currently labeled Y=0 (no progression)")
    print(f"     - Actual label should be Y=1 (success)")
    print(f"")
    print(f"  2. Selection Bias:")
    print(f"     - Only captures 'fast movers' (Series B in <17 months)")
    print(f"     - Misses 'slow but steady' companies")
    print(f"     - May bias results toward 'hype-driven' outcomes")
    print(f"")
    print(f"  3. Effect Size Underestimation:")
    print(f"     - H2 effect (vagueness → Series B↓) may be understated")
    print(f"     - True effect size likely larger with longer follow-up")

    # Statistical power
    print(f"\n" + "="*80)
    print("STATISTICAL POWER ANALYSIS")
    print("="*80)

    # Rough power calculation
    alpha = 0.05
    n = n_total
    p0 = base_rate

    print(f"\n  Sample size: {n:,}")
    print(f"  Base rate: {p0:.1%}")

    # For logistic regression, rough rule of thumb: need 10 events per predictor
    n_events = n_growth
    n_predictors = 5  # z_vagueness, is_hardware, interaction, controls
    events_per_predictor = n_events / n_predictors

    print(f"  Events (Y=1): {n_events:,}")
    print(f"  Predictors: {n_predictors}")
    print(f"  Events per predictor: {events_per_predictor:.1f}")

    if events_per_predictor >= 10:
        power_status = "✅ ADEQUATE (≥10 events/predictor)"
    elif events_per_predictor >= 5:
        power_status = "⚠️ MARGINAL (5-10 events/predictor)"
    else:
        power_status = "❌ INSUFFICIENT (<5 events/predictor)"

    print(f"  Power status: {power_status}")

    # Recommendations
    print(f"\n" + "="*80)
    print("RECOMMENDATIONS")
    print("="*80)

    print(f"\n1. ✅ ACKNOWLEDGE in paper:")
    print(f"   'Our follow-up period (17 months) is shorter than ideal.'")
    print(f"   'Results may underestimate true effect sizes due to right censoring.'")

    print(f"\n2. 🔄 ROBUSTNESS CHECK:")
    print(f"   - Vary definition of 'success' (e.g., Series A+ funding growth)")
    print(f"   - Use survival analysis with time-to-event")
    print(f"   - Sensitivity analysis with different follow-up windows")

    print(f"\n3. 📊 REPORT:")
    print(f"   - Explicitly state: 'Base rate {base_rate:.1%} reflects 17-month follow-up'")
    print(f"   - Compare to industry benchmarks for similar periods")
    print(f"   - Discuss limitations in interpretation")

    print(f"\n4. 🎯 FRAMING:")
    print(f"   - Frame as 'early-stage progression' (not ultimate success)")
    print(f"   - 'Companies that rapidly achieved Series B within 17 months'")
    print(f"   - This may actually be MORE aligned with vagueness hypothesis")
    print(f"     (vague → slower, more careful evaluation → delayed Series B)")

    print("\n" + "="*80)

if __name__ == "__main__":
    main()
