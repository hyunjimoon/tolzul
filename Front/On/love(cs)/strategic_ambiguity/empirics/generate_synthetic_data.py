#!/usr/bin/env python3
"""
Generate synthetic data for demonstrating the moderator bake-off pipeline.
This creates realistic-looking data with known properties for testing.
"""

import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

def generate_synthetic_analysis_dataset(n=5000):
    """
    Generate synthetic H2 analysis dataset with realistic properties.

    Key features:
    - is_hardware: ~15% prevalence (moderate imbalance)
    - is_serial: ~25% prevalence (acceptable balance)
    - Vagueness: continuous 0-100
    - Growth: ~12% base rate (realistic for Series B progression)
    """

    # Base features
    data = {
        'CompanyID': range(1, n+1),
        'vagueness': np.random.beta(2, 2, n) * 100,  # Bell curve 0-100
        'is_hardware': np.random.binomial(1, 0.15, n),  # 15% hardware
        'is_serial': np.random.binomial(1, 0.25, n),  # 25% serial
        'employees_log': np.random.normal(2.5, 1.0, n),  # log employees
        'year_founded': np.random.choice(range(2015, 2022), n),
    }

    df = pd.DataFrame(data)

    # Create founding cohort
    df['founding_cohort'] = pd.cut(
        df['year_founded'],
        bins=[0, 2016, 2018, 2020, 2022],
        labels=['≤2016', '2017-18', '2019-20', '2021+']
    )

    # Standardize for modeling
    df['z_vagueness'] = (df['vagueness'] - df['vagueness'].mean()) / df['vagueness'].std()
    df['z_employees_log'] = (df['employees_log'] - df['employees_log'].mean()) / df['employees_log'].std()

    # Generate growth outcome with true interaction effects
    # Model: logit(P(growth)) = intercept + vagueness + moderator + interaction + controls

    # Architecture model: vagueness helps MORE in software (negative interaction)
    logit_arch = (
        -2.0 +  # Baseline (12% base rate)
        0.3 * df['z_vagueness'] +  # Positive main effect
        -0.2 * df['is_hardware'] +  # Hardware baseline lower
        -0.4 * df['z_vagueness'] * df['is_hardware'] +  # Negative interaction (attenuation)
        0.1 * df['z_employees_log'] +  # Size helps
        np.random.normal(0, 0.5, n)  # Noise
    )
    prob_arch = 1 / (1 + np.exp(-logit_arch))

    # Founder model: vagueness helps MORE for first-timers (negative interaction)
    logit_founder = (
        -2.0 +  # Baseline
        0.35 * df['z_vagueness'] +  # Positive main effect
        0.3 * df['is_serial'] +  # Serial baseline higher
        -0.25 * df['z_vagueness'] * df['is_serial'] +  # Negative interaction (substitution)
        0.1 * df['z_employees_log'] +
        np.random.normal(0, 0.5, n)
    )
    prob_founder = 1 / (1 + np.exp(-logit_founder))

    # Use average of both models for final outcome (makes both plausible)
    prob_combined = (prob_arch + prob_founder) / 2
    df['growth'] = np.random.binomial(1, prob_combined)

    # Add some other columns for compatibility
    df['sector_fe'] = np.random.choice(
        ['AI/ML Software', 'Enterprise Software', 'Hardware/Robotics',
         'Biotech/Healthcare', 'FinTech', 'Other'],
        n,
        p=[0.25, 0.20, 0.15, 0.15, 0.15, 0.10]
    )

    df['early_funding_musd'] = np.random.lognormal(0, 1, n) * 2  # Mean ~$5M
    df['founder_credibility'] = df['is_serial']  # Alias

    print(f"Generated {n:,} synthetic observations")
    print(f"\nKey statistics:")
    print(f"  - is_hardware: {df['is_hardware'].mean():.1%}")
    print(f"  - is_serial: {df['is_serial'].mean():.1%}")
    print(f"  - Growth rate: {df['growth'].mean():.1%}")
    print(f"  - Vagueness mean: {df['vagueness'].mean():.1f}")

    return df


if __name__ == "__main__":
    # Generate dataset
    df = generate_synthetic_analysis_dataset(n=5000)

    # Save to outputs
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / "h2_analysis_dataset.csv"
    df.to_csv(output_path, index=False)
    print(f"\n✓ Saved to: {output_path}")
