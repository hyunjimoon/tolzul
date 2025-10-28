#!/usr/bin/env python3
"""
Exploratory Data Analysis (EDA) for H2 Variables
Following Bayesian Workflow visualization principles

Usage:
    python explore_h2_data.py --data outputs/h2_analysis_dataset_17m.csv --output outputs/eda/
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import argparse
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 100
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 10


def plot_univariate_distributions(df, output_dir):
    """Plot univariate distributions for all variables."""
    print("\n📊 Creating univariate distributions...")

    fig, axes = plt.subplots(3, 3, figsize=(15, 12))
    fig.suptitle('Univariate Distributions', fontsize=16, y=1.00)

    # 1. Vagueness (continuous, 0-100)
    ax = axes[0, 0]
    df['vagueness'].hist(bins=50, ax=ax, edgecolor='black', alpha=0.7)
    ax.axvline(df['vagueness'].median(), color='red', linestyle='--', label=f'Median={df["vagueness"].median():.1f}')
    ax.set_xlabel('Vagueness Score (0-100)')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Vagueness Distribution (n={df["vagueness"].notna().sum():,})')
    ax.legend()

    # 2. Early Funding (continuous, log scale)
    ax = axes[0, 1]
    early_funding = df['early_funding_musd'].dropna()
    if len(early_funding) > 0:
        early_funding_log = np.log10(early_funding + 1e-6)  # Add small constant to avoid log(0)
        early_funding_log.hist(bins=50, ax=ax, edgecolor='black', alpha=0.7)
        ax.set_xlabel('log10(Early Funding in M USD)')
        ax.set_ylabel('Frequency')
        ax.set_title(f'Early Funding Distribution (n={len(early_funding):,})')
        ax.axvline(early_funding_log.median(), color='red', linestyle='--',
                   label=f'Median=${10**early_funding_log.median():.2e}')
        ax.legend()
    else:
        ax.text(0.5, 0.5, 'No data', ha='center', va='center', transform=ax.transAxes)

    # 3. Survival (binary DV)
    ax = axes[0, 2]
    survival_counts = df['survival'].value_counts()
    survival_pct = survival_counts / survival_counts.sum() * 100
    ax.bar(['Failed (0)', 'Survived (1)'], survival_pct.reindex([0, 1], fill_value=0),
           color=['#e74c3c', '#2ecc71'], edgecolor='black', alpha=0.7)
    ax.set_ylabel('Percentage (%)')
    ax.set_title(f'Survival DV (n={df["survival"].notna().sum():,})')
    for i, (val, pct) in enumerate(zip([0, 1], survival_pct.reindex([0, 1], fill_value=0))):
        ax.text(i, pct + 1, f'{pct:.1f}%\n(n={survival_counts.get(val, 0):,})',
                ha='center', va='bottom', fontsize=9)
    ax.set_ylim(0, max(survival_pct.values) * 1.15)

    # 4. Integration Cost (binary)
    ax = axes[1, 0]
    integ_counts = df['high_integration_cost'].value_counts()
    integ_pct = integ_counts / integ_counts.sum() * 100
    ax.bar(['Modular (0)', 'Integrated (1)'], integ_pct.reindex([0, 1], fill_value=0),
           color=['#3498db', '#e67e22'], edgecolor='black', alpha=0.7)
    ax.set_ylabel('Percentage (%)')
    ax.set_title(f'Integration Cost (n={df["high_integration_cost"].notna().sum():,})')
    for i, (val, pct) in enumerate(zip([0, 1], integ_pct.reindex([0, 1], fill_value=0))):
        ax.text(i, pct + 1, f'{pct:.1f}%', ha='center', va='bottom')

    # 5. Founder Credibility (binary)
    ax = axes[1, 1]
    founder_counts = df['founder_credibility'].value_counts()
    founder_pct = founder_counts / founder_counts.sum() * 100
    ax.bar(['Non-serial (0)', 'Serial (1)'], founder_pct.reindex([0, 1], fill_value=0),
           color=['#95a5a6', '#9b59b6'], edgecolor='black', alpha=0.7)
    ax.set_ylabel('Percentage (%)')
    ax.set_title(f'Founder Credibility (n={df["founder_credibility"].notna().sum():,})')
    for i, (val, pct) in enumerate(zip([0, 1], founder_pct.reindex([0, 1], fill_value=0))):
        ax.text(i, pct + 1, f'{pct:.1f}%', ha='center', va='bottom')

    # 6. Employees (log scale)
    ax = axes[1, 2]
    df['employees_log'].hist(bins=50, ax=ax, edgecolor='black', alpha=0.7)
    ax.axvline(df['employees_log'].median(), color='red', linestyle='--',
               label=f'Median={df["employees_log"].median():.1f}')
    ax.set_xlabel('log(Employees)')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Employees Distribution (n={df["employees_log"].notna().sum():,})')
    ax.legend()

    # 7. Sector FE (categorical)
    ax = axes[2, 0]
    sector_counts = df['sector_fe'].value_counts().head(8)
    sector_pct = sector_counts / len(df) * 100
    sector_pct.plot(kind='barh', ax=ax, color='steelblue', edgecolor='black', alpha=0.7)
    ax.set_xlabel('Percentage (%)')
    ax.set_title(f'Sector Distribution (n={df["sector_fe"].notna().sum():,})')
    ax.invert_yaxis()

    # 8. Year Founded (discrete)
    ax = axes[2, 1]
    year_founded = df['year_founded'].dropna()
    if len(year_founded) > 0:
        year_founded.hist(bins=30, ax=ax, edgecolor='black', alpha=0.7)
        ax.axvline(year_founded.median(), color='red', linestyle='--',
                   label=f'Median={int(year_founded.median())}')
        ax.set_xlabel('Year Founded')
        ax.set_ylabel('Frequency')
        ax.set_title(f'Year Founded Distribution (n={len(year_founded):,})')
        ax.legend()

    # 9. Missing Data Pattern
    ax = axes[2, 2]
    missing_pct = df.isna().sum() / len(df) * 100
    missing_vars = missing_pct[missing_pct > 0].sort_values(ascending=False)
    if len(missing_vars) > 0:
        missing_vars.plot(kind='barh', ax=ax, color='#e74c3c', edgecolor='black', alpha=0.7)
        ax.set_xlabel('Missing (%)')
        ax.set_title('Missing Data Pattern')
        ax.invert_yaxis()
    else:
        ax.text(0.5, 0.5, 'No missing data', ha='center', va='center', transform=ax.transAxes)

    plt.tight_layout()
    output_path = output_dir / 'univariate_distributions.png'
    plt.savefig(output_path, bbox_inches='tight')
    print(f"  ✓ Saved: {output_path}")
    plt.close()


def plot_bivariate_with_survival(df, output_dir):
    """Plot relationships between predictors and survival DV."""
    print("\n📊 Creating bivariate plots (predictors vs survival)...")

    # Filter to valid survival cases
    df_valid = df[df['survival'].notna()].copy()

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Predictors vs Survival (DV)', fontsize=16, y=1.00)

    # 1. Vagueness vs Survival
    ax = axes[0, 0]
    for surv_val in [0, 1]:
        subset = df_valid[df_valid['survival'] == surv_val]['vagueness'].dropna()
        ax.hist(subset, bins=30, alpha=0.6, label=f'Survival={surv_val} (n={len(subset):,})',
                edgecolor='black')
    ax.set_xlabel('Vagueness Score')
    ax.set_ylabel('Frequency')
    ax.set_title('Vagueness by Survival Status')
    ax.legend()

    # 2. Integration Cost vs Survival
    ax = axes[0, 1]
    cross_tab = pd.crosstab(df_valid['high_integration_cost'], df_valid['survival'], normalize='index') * 100
    cross_tab.plot(kind='bar', ax=ax, color=['#e74c3c', '#2ecc71'], edgecolor='black', alpha=0.7)
    ax.set_xlabel('Integration Cost')
    ax.set_ylabel('Survival Rate (%)')
    ax.set_title('Survival Rate by Integration Cost')
    ax.set_xticklabels(['Modular (0)', 'Integrated (1)'], rotation=0)
    ax.legend(['Failed', 'Survived'], title='Survival')

    # 3. Founder Credibility vs Survival
    ax = axes[0, 2]
    cross_tab = pd.crosstab(df_valid['founder_credibility'], df_valid['survival'], normalize='index') * 100
    cross_tab.plot(kind='bar', ax=ax, color=['#e74c3c', '#2ecc71'], edgecolor='black', alpha=0.7)
    ax.set_xlabel('Founder Credibility')
    ax.set_ylabel('Survival Rate (%)')
    ax.set_title('Survival Rate by Founder Type')
    ax.set_xticklabels(['Non-serial (0)', 'Serial (1)'], rotation=0)
    ax.legend(['Failed', 'Survived'], title='Survival')

    # 4. Employees vs Survival
    ax = axes[1, 0]
    for surv_val in [0, 1]:
        subset = df_valid[df_valid['survival'] == surv_val]['employees_log'].dropna()
        ax.hist(subset, bins=30, alpha=0.6, label=f'Survival={surv_val}', edgecolor='black')
    ax.set_xlabel('log(Employees)')
    ax.set_ylabel('Frequency')
    ax.set_title('Employees by Survival Status')
    ax.legend()

    # 5. Sector vs Survival
    ax = axes[1, 1]
    sector_survival = df_valid.groupby('sector_fe')['survival'].agg(['mean', 'count'])
    sector_survival = sector_survival[sector_survival['count'] >= 50].sort_values('mean', ascending=False).head(8)
    (sector_survival['mean'] * 100).plot(kind='barh', ax=ax, color='steelblue', edgecolor='black', alpha=0.7)
    ax.set_xlabel('Survival Rate (%)')
    ax.set_title('Survival Rate by Sector (n≥50)')
    ax.invert_yaxis()

    # 6. Year Founded vs Survival
    ax = axes[1, 2]
    year_survival = df_valid.groupby('year_founded')['survival'].agg(['mean', 'count'])
    year_survival = year_survival[year_survival['count'] >= 20]
    ax.scatter(year_survival.index, year_survival['mean'] * 100, alpha=0.6, s=year_survival['count'])
    ax.set_xlabel('Year Founded')
    ax.set_ylabel('Survival Rate (%)')
    ax.set_title('Survival Rate by Year Founded (size=n)')
    ax.axhline(df_valid['survival'].mean() * 100, color='red', linestyle='--', label='Overall mean')
    ax.legend()

    plt.tight_layout()
    output_path = output_dir / 'bivariate_with_survival.png'
    plt.savefig(output_path, bbox_inches='tight')
    print(f"  ✓ Saved: {output_path}")
    plt.close()


def plot_interaction_exploration(df, output_dir):
    """Explore Vagueness × Integration Cost interaction (H2 main effect)."""
    print("\n📊 Creating interaction exploration plot...")

    df_valid = df[df['survival'].notna() & df['vagueness'].notna()].copy()

    # Create vagueness bins for visualization
    df_valid['vagueness_bin'] = pd.cut(df_valid['vagueness'], bins=5, labels=['Very Low', 'Low', 'Medium', 'High', 'Very High'])

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Vagueness × Integration Cost Interaction (H2)', fontsize=16)

    # 1. Survival rate by vagueness bins and integration cost
    ax = axes[0]
    interaction_data = df_valid.groupby(['vagueness_bin', 'high_integration_cost'])['survival'].agg(['mean', 'count'])
    interaction_data = interaction_data[interaction_data['count'] >= 10]  # Filter small groups

    for integ_val in [0, 1]:
        subset = interaction_data.xs(integ_val, level='high_integration_cost')
        label = 'Modular' if integ_val == 0 else 'Integrated'
        ax.plot(subset.index, subset['mean'] * 100, marker='o', label=label, linewidth=2)

    ax.set_xlabel('Vagueness Level')
    ax.set_ylabel('Survival Rate (%)')
    ax.set_title('H2: Vagueness × Integration Cost')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # 2. Heatmap of survival rates
    ax = axes[1]
    pivot = df_valid.pivot_table(values='survival', index='vagueness_bin',
                                  columns='high_integration_cost', aggfunc='mean') * 100
    sns.heatmap(pivot, annot=True, fmt='.1f', cmap='RdYlGn', ax=ax, cbar_kws={'label': 'Survival Rate (%)'})
    ax.set_xlabel('Integration Cost (0=Modular, 1=Integrated)')
    ax.set_ylabel('Vagueness Level')
    ax.set_title('Survival Rate Heatmap')

    # 3. Sample sizes
    ax = axes[2]
    sample_sizes = df_valid.pivot_table(values='survival', index='vagueness_bin',
                                        columns='high_integration_cost', aggfunc='count')
    sns.heatmap(sample_sizes, annot=True, fmt='g', cmap='Blues', ax=ax, cbar_kws={'label': 'N'})
    ax.set_xlabel('Integration Cost (0=Modular, 1=Integrated)')
    ax.set_ylabel('Vagueness Level')
    ax.set_title('Sample Sizes')

    plt.tight_layout()
    output_path = output_dir / 'interaction_exploration.png'
    plt.savefig(output_path, bbox_inches='tight')
    print(f"  ✓ Saved: {output_path}")
    plt.close()


def plot_correlation_matrix(df, output_dir):
    """Plot correlation matrix for continuous variables."""
    print("\n📊 Creating correlation matrix...")

    # Select continuous/ordinal variables
    corr_vars = ['vagueness', 'early_funding_musd', 'survival', 'high_integration_cost',
                 'founder_credibility', 'employees_log', 'year_founded']

    df_corr = df[corr_vars].dropna()

    if len(df_corr) > 0:
        fig, ax = plt.subplots(figsize=(10, 8))

        corr_matrix = df_corr.corr()
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

        sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.3f', cmap='coolwarm',
                    center=0, square=True, linewidths=1, ax=ax,
                    cbar_kws={'label': 'Pearson Correlation'})

        ax.set_title(f'Correlation Matrix (n={len(df_corr):,})', fontsize=14, pad=20)

        plt.tight_layout()
        output_path = output_dir / 'correlation_matrix.png'
        plt.savefig(output_path, bbox_inches='tight')
        print(f"  ✓ Saved: {output_path}")
        plt.close()
    else:
        print("  ⚠️  Insufficient data for correlation matrix")


def plot_bayesian_prior_predictive(df, output_dir):
    """Simulate prior predictive distributions for Bayesian perspective."""
    print("\n📊 Creating prior predictive checks (Bayesian workflow)...")

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Prior Predictive Checks (Bayesian Workflow)', fontsize=16)

    # 1. Vagueness effect on survival (logit scale)
    ax = axes[0, 0]

    # Observed data
    df_valid = df[df['survival'].notna() & df['vagueness'].notna()].copy()
    vague_bins = pd.cut(df_valid['vagueness'], bins=10)
    observed = df_valid.groupby(vague_bins)['survival'].mean()

    ax.scatter(range(len(observed)), observed * 100, s=100, alpha=0.7,
               label='Observed', color='black', zorder=10)

    # Prior predictive simulations
    np.random.seed(42)
    n_sims = 50
    for i in range(n_sims):
        # Weak prior: β ~ Normal(0, 1)
        beta = np.random.normal(0, 1)
        alpha = np.random.normal(0, 1)

        # Simulate
        vague_range = np.linspace(0, 100, 10)
        logit_p = alpha + beta * (vague_range - 50) / 50  # Standardize
        p = 1 / (1 + np.exp(-logit_p))

        ax.plot(range(10), p * 100, alpha=0.1, color='steelblue')

    ax.set_xlabel('Vagueness Decile')
    ax.set_ylabel('Survival Probability (%)')
    ax.set_title('Prior Predictive: Vagueness → Survival\n(β ~ Normal(0,1))')
    ax.legend()
    ax.set_ylim(0, 100)

    # 2. Base rate distribution
    ax = axes[0, 1]

    observed_rate = df['survival'].mean()

    # Prior predictive for base rate: logit(p) ~ Normal(0, 1.5)
    prior_logits = np.random.normal(0, 1.5, 10000)
    prior_rates = 1 / (1 + np.exp(-prior_logits))

    ax.hist(prior_rates * 100, bins=50, alpha=0.7, edgecolor='black',
            label='Prior predictive', color='steelblue')
    ax.axvline(observed_rate * 100, color='red', linestyle='--', linewidth=2,
               label=f'Observed = {observed_rate*100:.1f}%')
    ax.set_xlabel('Base Rate (%)')
    ax.set_ylabel('Frequency')
    ax.set_title('Prior Predictive: Survival Base Rate\nlogit(p) ~ Normal(0, 1.5)')
    ax.legend()

    # 3. Effect size distribution
    ax = axes[1, 0]

    # Prior on log-odds scale
    prior_effects = np.random.normal(0, 1, 10000)

    ax.hist(prior_effects, bins=50, alpha=0.7, edgecolor='black', color='steelblue')
    ax.axvline(0, color='black', linestyle='-', linewidth=1)
    ax.set_xlabel('Effect Size (log-odds)')
    ax.set_ylabel('Frequency')
    ax.set_title('Prior: Main Effects\nβ ~ Normal(0, 1)')

    # Add interpretation
    percentiles = np.percentile(prior_effects, [2.5, 50, 97.5])
    ax.text(0.05, 0.95, f'95% CI: [{percentiles[0]:.2f}, {percentiles[2]:.2f}]',
            transform=ax.transAxes, va='top', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # 4. Interaction effect
    ax = axes[1, 1]

    # Prior on interaction: β₃ ~ Normal(0, 0.5)
    prior_interaction = np.random.normal(0, 0.5, 10000)

    ax.hist(prior_interaction, bins=50, alpha=0.7, edgecolor='black', color='steelblue')
    ax.axvline(0, color='black', linestyle='-', linewidth=1)
    ax.set_xlabel('Interaction Effect (log-odds)')
    ax.set_ylabel('Frequency')
    ax.set_title('Prior: Vagueness × Integration Cost\nβ₃ ~ Normal(0, 0.5)')

    percentiles = np.percentile(prior_interaction, [2.5, 50, 97.5])
    ax.text(0.05, 0.95, f'95% CI: [{percentiles[0]:.2f}, {percentiles[2]:.2f}]',
            transform=ax.transAxes, va='top', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    output_path = output_dir / 'prior_predictive_checks.png'
    plt.savefig(output_path, bbox_inches='tight')
    print(f"  ✓ Saved: {output_path}")
    plt.close()


def create_summary_table(df, output_dir):
    """Create summary statistics table."""
    print("\n📊 Creating summary statistics table...")

    summary_stats = []

    variables = {
        'vagueness': ('Vagueness (0-100)', 'continuous'),
        'early_funding_musd': ('Early Funding (M USD)', 'continuous'),
        'survival': ('Survival (DV)', 'binary'),
        'high_integration_cost': ('Integration Cost', 'binary'),
        'founder_credibility': ('Founder Credibility', 'binary'),
        'employees_log': ('log(Employees)', 'continuous'),
        'year_founded': ('Year Founded', 'discrete'),
        'sector_fe': ('Sector', 'categorical')
    }

    for var, (label, var_type) in variables.items():
        if var not in df.columns:
            continue

        n_valid = df[var].notna().sum()
        n_missing = df[var].isna().sum()
        pct_valid = n_valid / len(df) * 100

        if var_type == 'continuous' or var_type == 'discrete':
            mean_val = df[var].mean()
            std_val = df[var].std()
            median_val = df[var].median()
            min_val = df[var].min()
            max_val = df[var].max()

            summary_stats.append({
                'Variable': label,
                'Type': var_type,
                'N Valid': f'{n_valid:,}',
                'N Missing': f'{n_missing:,}',
                '% Valid': f'{pct_valid:.1f}%',
                'Mean': f'{mean_val:.2f}' if pd.notna(mean_val) else 'N/A',
                'SD': f'{std_val:.2f}' if pd.notna(std_val) else 'N/A',
                'Median': f'{median_val:.2f}' if pd.notna(median_val) else 'N/A',
                'Min': f'{min_val:.2f}' if pd.notna(min_val) else 'N/A',
                'Max': f'{max_val:.2f}' if pd.notna(max_val) else 'N/A'
            })

        elif var_type == 'binary':
            value_counts = df[var].value_counts()
            pct_1 = value_counts.get(1, 0) / n_valid * 100 if n_valid > 0 else 0

            summary_stats.append({
                'Variable': label,
                'Type': var_type,
                'N Valid': f'{n_valid:,}',
                'N Missing': f'{n_missing:,}',
                '% Valid': f'{pct_valid:.1f}%',
                'Mean': f'{pct_1:.1f}%',
                'SD': 'N/A',
                'Median': 'N/A',
                'Min': '0',
                'Max': '1'
            })

        elif var_type == 'categorical':
            n_categories = df[var].nunique()

            summary_stats.append({
                'Variable': label,
                'Type': var_type,
                'N Valid': f'{n_valid:,}',
                'N Missing': f'{n_missing:,}',
                '% Valid': f'{pct_valid:.1f}%',
                'Mean': f'{n_categories} categories',
                'SD': 'N/A',
                'Median': 'N/A',
                'Min': 'N/A',
                'Max': 'N/A'
            })

    summary_df = pd.DataFrame(summary_stats)

    output_path = output_dir / 'summary_statistics.csv'
    summary_df.to_csv(output_path, index=False)
    print(f"  ✓ Saved: {output_path}")

    # Also print to console
    print("\n" + "="*80)
    print("SUMMARY STATISTICS")
    print("="*80)
    print(summary_df.to_string(index=False))
    print("="*80)

    return summary_df


def main():
    parser = argparse.ArgumentParser(
        description='Exploratory Data Analysis for H2 Variables (Bayesian Workflow Style)'
    )

    parser.add_argument(
        '--data',
        type=str,
        default='outputs/h2_analysis_dataset_17m.csv',
        help='Path to analysis dataset CSV'
    )

    parser.add_argument(
        '--output',
        type=str,
        default='outputs/eda',
        help='Output directory for plots'
    )

    args = parser.parse_args()

    # Create output directory
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("="*80)
    print("EXPLORATORY DATA ANALYSIS (EDA)")
    print("="*80)
    print(f"Data: {args.data}")
    print(f"Output: {output_dir}")
    print("="*80)

    # Load data
    print("\n📂 Loading data...")
    df = pd.read_csv(args.data)
    print(f"  ✓ Loaded {len(df):,} rows, {len(df.columns)} columns")

    # Run all analyses
    create_summary_table(df, output_dir)
    plot_univariate_distributions(df, output_dir)
    plot_bivariate_with_survival(df, output_dir)
    plot_interaction_exploration(df, output_dir)
    plot_correlation_matrix(df, output_dir)
    plot_bayesian_prior_predictive(df, output_dir)

    print("\n" + "="*80)
    print("✓ EDA COMPLETE")
    print("="*80)
    print(f"\nAll outputs saved to: {output_dir}/")
    print("\nGenerated files:")
    print("  - summary_statistics.csv")
    print("  - univariate_distributions.png")
    print("  - bivariate_with_survival.png")
    print("  - interaction_exploration.png")
    print("  - correlation_matrix.png")
    print("  - prior_predictive_checks.png")


if __name__ == "__main__":
    main()
