#!/usr/bin/env python3
"""
Eyeball Test Plots - 각 변수의 분포와 관계를 시각화

이 스크립트는 H1/H2 모델의 모든 변수들을 시각적으로 확인할 수 있게 합니다.

Variables:
- H1: early_funding_musd ~ z_vagueness + z_employees_log + founder_serial +
      is_hardware + z_firm_age + C(sector_fe) + C(founding_cohort)
- H2: growth ~ z_vagueness * is_hardware + founder_serial + z_employees_log +
      C(founding_cohort)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Configure plotting
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10

def load_data():
    """Load features dataset."""
    data_file = Path("data/processed/features_all.parquet")

    if not data_file.exists():
        print(f"❌ Data not found: {data_file}")
        print(f"\n   Run pipeline first:")
        print(f"   python -m src.cli engineer-features")
        return None

    print(f"📂 Loading data from {data_file}")
    df = pd.read_parquet(data_file)
    print(f"   Loaded {len(df):,} companies with {len(df.columns)} features")

    # Create z-scored variables (matching Step 4 preprocessing)
    print(f"\n🔧 Creating z-scored variables...")
    for col in ['vagueness', 'employees_log', 'firm_age']:
        if col in df.columns:
            col_std = df[col].std()
            if col_std > 0 and not pd.isna(col_std):
                df[f'z_{col}'] = (df[col] - df[col].mean()) / col_std
                print(f"   ✓ Created z_{col} (μ=0.00, σ=1.00)")
            else:
                df[f'z_{col}'] = 0
                print(f"   ⚠️  {col} has zero variance, z_{col}=0")
        else:
            print(f"   ⚠️  {col} not found in dataset")

    # Check for early_funding in millions
    if 'early_funding' in df.columns and 'early_funding_musd' not in df.columns:
        # Convert to millions if needed
        if df['early_funding'].max() > 1e6:
            df['early_funding_musd'] = df['early_funding'] / 1e6
            print(f"   ✓ Created early_funding_musd (converted to millions)")
        else:
            df['early_funding_musd'] = df['early_funding']
            print(f"   ✓ Created early_funding_musd (already in millions)")

    return df

def plot_univariate_distributions(df, output_dir):
    """Plot distribution of each variable."""
    print(f"\n📊 Generating univariate distribution plots...")

    output_dir = Path(output_dir) / "eyeball_test"
    output_dir.mkdir(exist_ok=True, parents=True)

    # Define variables to plot
    continuous_vars = [
        ('z_vagueness', 'Strategic Vagueness (z-scored)', 'green'),
        ('early_funding_musd', 'Early Funding ($M)', 'red'),
        ('z_employees_log', 'Employee Count (log, z-scored)', 'orange'),
        ('z_firm_age', 'Firm Age (z-scored)', 'purple'),
    ]

    categorical_vars = [
        ('growth', 'Growth to Series B+', ['gray', 'blue']),
        ('is_hardware', 'Architecture Type', ['skyblue', 'gray']),
        ('founder_serial', 'Founder Type', ['lightcoral', 'darkred']),
    ]

    # Plot continuous variables
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()

    for i, (var, label, color) in enumerate(continuous_vars):
        ax = axes[i]

        if var not in df.columns:
            ax.text(0.5, 0.5, f'{var}\nNot Available',
                   ha='center', va='center', fontsize=14, color='red')
            ax.set_title(label, fontweight='bold')
            continue

        data = df[var].dropna()

        # Histogram
        ax.hist(data, bins=50, color=color, alpha=0.7, edgecolor='black')

        # Add mean and median lines
        mean_val = data.mean()
        median_val = data.median()

        ax.axvline(mean_val, color='darkred', linestyle='--', linewidth=2,
                  label=f'Mean: {mean_val:.2f}')
        ax.axvline(median_val, color='orange', linestyle=':', linewidth=2,
                  label=f'Median: {median_val:.2f}')

        ax.set_xlabel(label, fontsize=11, fontweight='bold')
        ax.set_ylabel('Count', fontsize=11)
        ax.set_title(f'{label}\n(μ={mean_val:.2f}, σ={data.std():.2f})',
                    fontsize=12, fontweight='bold')
        ax.legend(fontsize=9)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    file_path = output_dir / "1_continuous_distributions.png"
    plt.savefig(file_path, dpi=300, bbox_inches='tight')
    print(f"   ✓ Saved: {file_path}")
    plt.close()

    # Plot categorical variables
    fig, axes = plt.subplots(1, 3, figsize=(14, 5))

    for i, (var, label, colors) in enumerate(categorical_vars):
        ax = axes[i]

        if var not in df.columns:
            ax.text(0.5, 0.5, f'{var}\nNot Available',
                   ha='center', va='center', fontsize=14, color='red')
            ax.set_title(label, fontweight='bold')
            continue

        counts = df[var].value_counts().sort_index()

        ax.bar(counts.index, counts.values, color=colors, alpha=0.7, edgecolor='black')

        # Add value labels
        for idx, val in counts.items():
            pct = val / len(df) * 100
            ax.text(idx, val, f'{val:,}\n({pct:.1f}%)',
                   ha='center', va='bottom', fontweight='bold', fontsize=10)

        # Labels
        if var == 'growth':
            ax.set_xticklabels(['No Growth', 'Series B+'])
        elif var == 'is_hardware':
            ax.set_xticklabels(['Software', 'Hardware'])
        elif var == 'founder_serial':
            ax.set_xticklabels(['First-time', 'Serial'])

        ax.set_xlabel(label, fontsize=11, fontweight='bold')
        ax.set_ylabel('Count', fontsize=11)
        ax.set_title(label, fontsize=12, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    file_path = output_dir / "2_categorical_distributions.png"
    plt.savefig(file_path, dpi=300, bbox_inches='tight')
    print(f"   ✓ Saved: {file_path}")
    plt.close()

def plot_bivariate_relationships(df, output_dir):
    """Plot relationships between variables."""
    print(f"\n📊 Generating bivariate relationship plots...")

    output_dir = Path(output_dir) / "eyeball_test"
    output_dir.mkdir(exist_ok=True, parents=True)

    # H1 Model: early_funding vs predictors
    if 'early_funding_musd' in df.columns and 'z_vagueness' in df.columns:
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        axes = axes.flatten()

        # 1. Early Funding vs Vagueness
        ax = axes[0]
        sample_df = df[['early_funding_musd', 'z_vagueness']].dropna()
        if len(sample_df) > 10000:
            sample_df = sample_df.sample(10000, random_state=42)

        ax.scatter(sample_df['z_vagueness'], sample_df['early_funding_musd'],
                  alpha=0.3, s=20, color='green')

        # Add trend line
        z = np.polyfit(sample_df['z_vagueness'], sample_df['early_funding_musd'], 1)
        p = np.poly1d(z)
        x_line = np.linspace(sample_df['z_vagueness'].min(),
                            sample_df['z_vagueness'].max(), 100)
        ax.plot(x_line, p(x_line), "r--", linewidth=2, label=f'y={z[0]:.2f}x+{z[1]:.2f}')

        ax.set_xlabel('Vagueness (z-scored)', fontsize=11, fontweight='bold')
        ax.set_ylabel('Early Funding ($M)', fontsize=11, fontweight='bold')
        ax.set_title('H1: Early Funding ~ Vagueness', fontsize=12, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)

        # 2. Early Funding by Hardware
        ax = axes[1]
        if 'is_hardware' in df.columns:
            hw_df = df[['early_funding_musd', 'is_hardware']].dropna()
            hw_labels = ['Software', 'Hardware']

            data_to_plot = [hw_df[hw_df['is_hardware']==0]['early_funding_musd'],
                           hw_df[hw_df['is_hardware']==1]['early_funding_musd']]

            bp = ax.boxplot(data_to_plot, labels=hw_labels, patch_artist=True)
            bp['boxes'][0].set_facecolor('skyblue')
            bp['boxes'][1].set_facecolor('gray')

            ax.set_ylabel('Early Funding ($M)', fontsize=11, fontweight='bold')
            ax.set_title('H1: Early Funding by Architecture', fontsize=12, fontweight='bold')
            ax.grid(True, alpha=0.3, axis='y')

        # 3. Early Funding vs Employees
        ax = axes[2]
        if 'z_employees_log' in df.columns:
            sample_df = df[['early_funding_musd', 'z_employees_log']].dropna()
            if len(sample_df) > 10000:
                sample_df = sample_df.sample(10000, random_state=42)

            ax.scatter(sample_df['z_employees_log'], sample_df['early_funding_musd'],
                      alpha=0.3, s=20, color='orange')

            z = np.polyfit(sample_df['z_employees_log'], sample_df['early_funding_musd'], 1)
            p = np.poly1d(z)
            x_line = np.linspace(sample_df['z_employees_log'].min(),
                                sample_df['z_employees_log'].max(), 100)
            ax.plot(x_line, p(x_line), "r--", linewidth=2,
                   label=f'y={z[0]:.2f}x+{z[1]:.2f}')

            ax.set_xlabel('Employees (log, z-scored)', fontsize=11, fontweight='bold')
            ax.set_ylabel('Early Funding ($M)', fontsize=11, fontweight='bold')
            ax.set_title('H1: Early Funding ~ Employees', fontsize=12, fontweight='bold')
            ax.legend()
            ax.grid(True, alpha=0.3)

        # 4. Early Funding vs Firm Age
        ax = axes[3]
        if 'z_firm_age' in df.columns:
            sample_df = df[['early_funding_musd', 'z_firm_age']].dropna()
            if len(sample_df) > 10000:
                sample_df = sample_df.sample(10000, random_state=42)

            ax.scatter(sample_df['z_firm_age'], sample_df['early_funding_musd'],
                      alpha=0.3, s=20, color='purple')

            z = np.polyfit(sample_df['z_firm_age'], sample_df['early_funding_musd'], 1)
            p = np.poly1d(z)
            x_line = np.linspace(sample_df['z_firm_age'].min(),
                                sample_df['z_firm_age'].max(), 100)
            ax.plot(x_line, p(x_line), "r--", linewidth=2,
                   label=f'y={z[0]:.2f}x+{z[1]:.2f}')

            ax.set_xlabel('Firm Age (z-scored)', fontsize=11, fontweight='bold')
            ax.set_ylabel('Early Funding ($M)', fontsize=11, fontweight='bold')
            ax.set_title('H1: Early Funding ~ Firm Age', fontsize=12, fontweight='bold')
            ax.legend()
            ax.grid(True, alpha=0.3)

        plt.tight_layout()
        file_path = output_dir / "3_h1_bivariate.png"
        plt.savefig(file_path, dpi=300, bbox_inches='tight')
        print(f"   ✓ Saved: {file_path}")
        plt.close()

    # H2 Model: growth vs predictors
    if 'growth' in df.columns and 'z_vagueness' in df.columns:
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        axes = axes.flatten()

        # 1. Growth rate by Vagueness quintile
        ax = axes[0]
        df_h2 = df[['growth', 'z_vagueness']].dropna()
        # Use duplicates='drop' to handle duplicate bin edges
        df_h2['v_quintile'] = pd.qcut(df_h2['z_vagueness'], q=5,
                                       labels=False, duplicates='drop')
        # Create labels based on actual number of bins
        n_bins = df_h2['v_quintile'].nunique()
        bin_labels = [f'Q{i+1}' for i in range(n_bins)]
        df_h2['v_quintile'] = df_h2['v_quintile'].map(dict(enumerate(bin_labels)))

        growth_by_v = df_h2.groupby('v_quintile')['growth'].agg(['mean', 'count'])

        ax.bar(range(len(growth_by_v)), growth_by_v['mean'], color='green', alpha=0.7, edgecolor='black')
        ax.set_xticks(range(len(growth_by_v)))
        ax.set_xticklabels(growth_by_v.index)
        ax.set_xlabel('Vagueness Quintile', fontsize=11, fontweight='bold')
        ax.set_ylabel('Growth Rate', fontsize=11, fontweight='bold')
        ax.set_title(f'H2: Growth ~ Vagueness (by {n_bins} bins)', fontsize=12, fontweight='bold')

        # Add value labels
        for i, (val, cnt) in enumerate(zip(growth_by_v['mean'], growth_by_v['count'])):
            ax.text(i, val, f'{val:.2%}\n(n={int(cnt):,})',
                   ha='center', va='bottom', fontweight='bold', fontsize=9)

        ax.grid(True, alpha=0.3, axis='y')

        # 2. Growth rate by Hardware
        ax = axes[1]
        if 'is_hardware' in df.columns and df['is_hardware'].nunique() > 1:
            # Only plot if there's variation in is_hardware
            growth_by_hw = df.groupby('is_hardware')['growth'].agg(['mean', 'count'])

            # Use dynamic labels based on actual values
            hw_labels = []
            for idx in growth_by_hw.index:
                hw_labels.append('Hardware' if idx == 1 else 'Software')

            colors = ['skyblue', 'gray'][:len(growth_by_hw)]
            ax.bar(range(len(growth_by_hw)), growth_by_hw['mean'],
                  color=colors, alpha=0.7, edgecolor='black')
            ax.set_xticks(range(len(growth_by_hw)))
            ax.set_xticklabels(hw_labels)
            ax.set_ylabel('Growth Rate', fontsize=11, fontweight='bold')
            ax.set_title('H2: Growth by Architecture', fontsize=12, fontweight='bold')

            for i, (val, cnt) in enumerate(zip(growth_by_hw['mean'], growth_by_hw['count'])):
                ax.text(i, val, f'{val:.2%}\n(n={int(cnt):,})',
                       ha='center', va='bottom', fontweight='bold', fontsize=10)

            ax.grid(True, alpha=0.3, axis='y')
        else:
            # Show message when hardware data not available
            ax.text(0.5, 0.5,
                   'Hardware Data\nNot Available\n\n(is_hardware missing or constant)',
                   ha='center', va='center', fontsize=12, color='gray',
                   transform=ax.transAxes)
            ax.set_title('H2: Growth by Architecture', fontsize=12, fontweight='bold')
            ax.axis('off')

        # 3. Growth ~ Vagueness by Hardware (interaction preview)
        ax = axes[2]
        if 'is_hardware' in df.columns and df['is_hardware'].nunique() > 1:
            # Only plot if there's variation in is_hardware
            df_interact = df[['growth', 'z_vagueness', 'is_hardware']].dropna()
            # Use duplicates='drop' to handle duplicate bin edges
            df_interact['v_quintile'] = pd.qcut(df_interact['z_vagueness'], q=5,
                                                labels=False, duplicates='drop')
            # Create labels based on actual number of bins
            n_bins_interact = df_interact['v_quintile'].nunique()
            bin_labels_interact = [f'Q{i+1}' for i in range(n_bins_interact)]
            df_interact['v_quintile'] = df_interact['v_quintile'].map(dict(enumerate(bin_labels_interact)))

            growth_sw = df_interact[df_interact['is_hardware']==0].groupby('v_quintile')['growth'].mean()
            growth_hw = df_interact[df_interact['is_hardware']==1].groupby('v_quintile')['growth'].mean()

            x = range(len(growth_sw))
            ax.plot(x, growth_sw, marker='o', linewidth=2, markersize=8,
                   color='skyblue', label='Software')
            ax.plot(x, growth_hw, marker='s', linewidth=2, markersize=8,
                   color='gray', linestyle='--', label='Hardware')

            ax.set_xticks(x)
            ax.set_xticklabels(growth_sw.index)
            ax.set_xlabel('Vagueness Quintile', fontsize=11, fontweight='bold')
            ax.set_ylabel('Growth Rate', fontsize=11, fontweight='bold')
            ax.set_title(f'H2: Vagueness × Hardware Interaction ({n_bins_interact} bins)', fontsize=12, fontweight='bold')
            ax.legend()
            ax.grid(True, alpha=0.3)
        else:
            # Show message when hardware data not available
            ax.text(0.5, 0.5,
                   'Hardware Data\nNot Available\n\n(is_hardware missing or constant)',
                   ha='center', va='center', fontsize=12, color='gray',
                   transform=ax.transAxes)
            ax.set_title('H2: Vagueness × Hardware Interaction', fontsize=12, fontweight='bold')
            ax.axis('off')

        # 4. Growth rate by Founder Type
        ax = axes[3]
        if 'founder_serial' in df.columns and df['founder_serial'].nunique() > 1:
            # Only plot if there's variation in founder_serial
            growth_by_founder = df.groupby('founder_serial')['growth'].agg(['mean', 'count'])

            # Use dynamic labels based on actual values
            founder_labels = []
            for idx in growth_by_founder.index:
                founder_labels.append('Serial' if idx == 1 else 'First-time')

            colors = ['lightcoral', 'darkred'][:len(growth_by_founder)]
            ax.bar(range(len(growth_by_founder)), growth_by_founder['mean'],
                  color=colors, alpha=0.7, edgecolor='black')
            ax.set_xticks(range(len(growth_by_founder)))
            ax.set_xticklabels(founder_labels)
            ax.set_ylabel('Growth Rate', fontsize=11, fontweight='bold')
            ax.set_title('H2: Growth by Founder Type', fontsize=12, fontweight='bold')

            for i, (val, cnt) in enumerate(zip(growth_by_founder['mean'],
                                               growth_by_founder['count'])):
                ax.text(i, val, f'{val:.2%}\n(n={int(cnt):,})',
                       ha='center', va='bottom', fontweight='bold', fontsize=10)

            ax.grid(True, alpha=0.3, axis='y')
        else:
            # Show message when founder data not available
            ax.text(0.5, 0.5,
                   'Founder Type Data\nNot Available\n\n(founder_credibility missing)',
                   ha='center', va='center', fontsize=12, color='gray',
                   transform=ax.transAxes)
            ax.set_title('H2: Growth by Founder Type', fontsize=12, fontweight='bold')
            ax.axis('off')

        plt.tight_layout()
        file_path = output_dir / "4_h2_bivariate.png"
        plt.savefig(file_path, dpi=300, bbox_inches='tight')
        print(f"   ✓ Saved: {file_path}")
        plt.close()

def print_summary_statistics(df):
    """Print summary statistics for all variables."""
    print(f"\n📋 Summary Statistics")
    print("=" * 80)

    # Continuous variables
    cont_vars = ['z_vagueness', 'early_funding_musd', 'z_employees_log', 'z_firm_age']

    print(f"\nContinuous Variables:")
    print("-" * 80)
    for var in cont_vars:
        if var in df.columns:
            data = df[var].dropna()
            print(f"\n{var}:")
            print(f"  Count:  {len(data):,}")
            print(f"  Mean:   {data.mean():.4f}")
            print(f"  Std:    {data.std():.4f}")
            print(f"  Min:    {data.min():.4f}")
            print(f"  25%:    {data.quantile(0.25):.4f}")
            print(f"  50%:    {data.median():.4f}")
            print(f"  75%:    {data.quantile(0.75):.4f}")
            print(f"  Max:    {data.max():.4f}")
        else:
            print(f"\n{var}: NOT AVAILABLE")

    # Categorical variables
    cat_vars = ['growth', 'is_hardware', 'founder_serial']

    print(f"\n\nCategorical Variables:")
    print("-" * 80)
    for var in cat_vars:
        if var in df.columns:
            counts = df[var].value_counts().sort_index()
            print(f"\n{var}:")
            for idx, cnt in counts.items():
                pct = cnt / len(df) * 100
                print(f"  {idx}: {cnt:,} ({pct:.1f}%)")
        else:
            print(f"\n{var}: NOT AVAILABLE")

def main():
    """Main function."""
    print("=" * 80)
    print("EYEBALL TEST - Variable Distribution & Relationship Plots")
    print("=" * 80)

    # Load data
    df = load_data()
    if df is None:
        return 1

    # Print summary statistics
    print_summary_statistics(df)

    # Generate plots
    output_dir = Path("outputs/all")
    plot_univariate_distributions(df, output_dir)
    plot_bivariate_relationships(df, output_dir)

    print(f"\n" + "=" * 80)
    print(f"✅ EYEBALL TEST COMPLETE")
    print(f"=" * 80)
    print(f"\n📂 Plots saved to: {output_dir}/eyeball_test/")
    print(f"   1_continuous_distributions.png - 연속형 변수 분포")
    print(f"   2_categorical_distributions.png - 범주형 변수 분포")
    print(f"   3_h1_bivariate.png - H1 모델 변수 관계")
    print(f"   4_h2_bivariate.png - H2 모델 변수 관계")

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
