"""
Visualization Module for Hypothesis Testing Pipeline

Creates diagnostic plots and figures for H1 and H2 analysis:
- Scatter plots with regression lines
- Predicted probability curves
- Residual diagnostics
- Interaction plots
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Optional, Tuple, Union
import statsmodels.api as sm
from statsmodels.regression.linear_model import RegressionResultsWrapper
from statsmodels.discrete.discrete_model import BinaryResultsWrapper
from pathlib import Path
from sklearn.metrics import roc_curve, auc, roc_auc_score

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11


# =============================================================================
# H1 VISUALIZATIONS (OLS)
# =============================================================================

def plot_h1_scatter(
    df: pd.DataFrame,
    model: RegressionResultsWrapper,
    output_path: Optional[Path] = None
) -> plt.Figure:
    """
    Create scatter plot of Early Funding vs Vagueness with regression line.

    Args:
        df: DataFrame with data
        model: Fitted H1 model
        output_path: Optional path to save figure

    Returns:
        Matplotlib figure object
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Scatter plot
    df_plot = df.dropna(subset=['vagueness', 'early_funding_musd'])
    ax.scatter(
        df_plot['vagueness'],
        df_plot['early_funding_musd'],
        alpha=0.5,
        s=50,
        edgecolors='k',
        linewidths=0.5
    )

    # Regression line (controlling for other variables at their means)
    vagueness_range = np.linspace(df_plot['vagueness'].min(), df_plot['vagueness'].max(), 100)

    # Create prediction data with controls at means
    pred_data = pd.DataFrame({
        'vagueness': vagueness_range,
        'employees_log': df_plot['employees_log'].mean() if 'employees_log' in df_plot else 0,
        'year_founded': df_plot['year_founded'].mean() if 'year_founded' in df_plot else 2020
    })

    # Add intercept for prediction
    pred_data_with_const = sm.add_constant(pred_data[['vagueness', 'employees_log', 'year_founded']])

    # Predict
    try:
        predictions = model.predict(pred_data_with_const)
        ax.plot(vagueness_range, predictions, 'r-', linewidth=2, label='Fitted line')
    except:
        # Fallback: simple univariate line
        pass

    # Labels and formatting
    ax.set_xlabel('Vagueness Score', fontsize=12, fontweight='bold')
    ax.set_ylabel('Early Funding (Million USD)', fontsize=12, fontweight='bold')
    ax.set_title('H1: Early Funding ~ Vagueness\n(Controlling for Employees & Year Founded)',
                 fontsize=14, fontweight='bold')

    # Add coefficient info
    vagueness_coef = model.params.get('vagueness', np.nan)
    vagueness_pval = model.pvalues.get('vagueness', np.nan)
    textstr = f'α₁ = {vagueness_coef:.4f}\np = {vagueness_pval:.4f}\nR² = {model.rsquared:.3f}'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=11,
            verticalalignment='top', bbox=props)

    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    if output_path:
        fig.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {output_path}")

    return fig


def plot_h1_residuals(
    model: RegressionResultsWrapper,
    output_path: Optional[Path] = None
) -> plt.Figure:
    """
    Create residual diagnostic plots for H1 model.

    Args:
        model: Fitted H1 model
        output_path: Optional path to save figure

    Returns:
        Matplotlib figure object
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # 1. Residuals vs Fitted
    axes[0, 0].scatter(model.fittedvalues, model.resid, alpha=0.5)
    axes[0, 0].axhline(y=0, color='r', linestyle='--')
    axes[0, 0].set_xlabel('Fitted Values')
    axes[0, 0].set_ylabel('Residuals')
    axes[0, 0].set_title('Residuals vs Fitted')
    axes[0, 0].grid(True, alpha=0.3)

    # 2. Q-Q plot
    sm.qqplot(model.resid, line='45', ax=axes[0, 1])
    axes[0, 1].set_title('Normal Q-Q Plot')
    axes[0, 1].grid(True, alpha=0.3)

    # 3. Scale-Location plot
    standardized_resid = model.resid / np.std(model.resid)
    axes[1, 0].scatter(model.fittedvalues, np.sqrt(np.abs(standardized_resid)), alpha=0.5)
    axes[1, 0].set_xlabel('Fitted Values')
    axes[1, 0].set_ylabel('√|Standardized Residuals|')
    axes[1, 0].set_title('Scale-Location')
    axes[1, 0].grid(True, alpha=0.3)

    # 4. Histogram of residuals
    axes[1, 1].hist(model.resid, bins=30, edgecolor='black', alpha=0.7)
    axes[1, 1].set_xlabel('Residuals')
    axes[1, 1].set_ylabel('Frequency')
    axes[1, 1].set_title('Histogram of Residuals')
    axes[1, 1].grid(True, alpha=0.3)

    fig.suptitle('H1 Model Diagnostics', fontsize=14, fontweight='bold', y=1.00)
    plt.tight_layout()

    if output_path:
        fig.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {output_path}")

    return fig


# =============================================================================
# H2 VISUALIZATIONS (LOGIT)
# =============================================================================

def plot_h2_interaction(
    df: pd.DataFrame,
    model: BinaryResultsWrapper,
    output_path: Optional[Path] = None
) -> plt.Figure:
    """
    Create interaction plot showing vagueness effect by integration cost.

    Args:
        df: DataFrame with data
        model: Fitted H2 model
        output_path: Optional path to save figure

    Returns:
        Matplotlib figure object
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Vagueness range (0-100 scale)
    v = np.linspace(0, 100, 50)

    # Get coefficients
    intercept = model.params.get('Intercept', 0)
    beta_vagueness = model.params.get('vagueness', 0)
    beta_integration = model.params.get('high_integration_cost', 0)
    beta_interaction = model.params.get('vagueness:high_integration_cost', 0)
    beta_founder = model.params.get('founder_credibility', 0)
    beta_employees = model.params.get('employees_log', 0)
    beta_year = model.params.get('year_founded', 0)

    # Control variables at means
    df_clean = df.dropna(subset=['founder_credibility', 'employees_log', 'year_founded'])
    founder_mean = df_clean['founder_credibility'].mean() if 'founder_credibility' in df_clean else 0
    employees_mean = df_clean['employees_log'].mean()
    year_mean = df_clean['year_founded'].mean()

    # Predicted probabilities for low integration cost (modular)
    # NOTE: NO early_funding control (it's a mediator)
    logit_low = (intercept +
                 beta_vagueness * v +
                 beta_founder * founder_mean +
                 beta_employees * employees_mean +
                 beta_year * year_mean)
    pred_low = 1 / (1 + np.exp(-logit_low))

    # Predicted probabilities for high integration cost (integrated)
    logit_high = (intercept +
                  beta_vagueness * v +
                  beta_integration +
                  beta_interaction * v +
                  beta_founder * founder_mean +
                  beta_employees * employees_mean +
                  beta_year * year_mean)
    pred_high = 1 / (1 + np.exp(-logit_high))

    # Plot
    ax.plot(v, pred_low, 'b-', linewidth=2.5, label='Modular (Low Integration Cost)')
    ax.plot(v, pred_high, 'r--', linewidth=2.5, label='Integrated (High Integration Cost)')

    # Formatting
    ax.set_xlabel('Vagueness Score (0-100)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Predicted P(Survival)', fontsize=12, fontweight='bold')
    ax.set_title('H2 Main: Vagueness Effect on Survival\nby Integration Cost',
                 fontsize=14, fontweight='bold')

    # Add coefficient info
    textstr = (f'β₁ (Vagueness): {beta_vagueness:.4f}\n'
               f'β₃ (Interaction): {beta_interaction:.4f}\n'
               f'p(β₁) = {model.pvalues.get("vagueness", np.nan):.4f}')
    props = dict(boxstyle='round', facecolor='lightblue', alpha=0.8)
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=11,
            verticalalignment='top', bbox=props)

    ax.legend(loc='lower right', fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_ylim([0, 1])

    plt.tight_layout()

    if output_path:
        fig.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {output_path}")

    return fig


def plot_h2_marginal_effects(
    df: pd.DataFrame,
    model: BinaryResultsWrapper,
    output_path: Optional[Path] = None
) -> plt.Figure:
    """
    Plot marginal effects of vagueness on later success probability.

    Args:
        df: DataFrame with data
        model: Fitted H2 model
        output_path: Optional path to save figure

    Returns:
        Matplotlib figure object
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Determine DV column (survival or later_success for backward compat)
    dv_col = 'survival' if 'survival' in df.columns else 'later_success'
    df_clean = df.dropna(subset=['vagueness', dv_col, 'high_integration_cost'])

    # Left plot: Low integration cost (modular)
    df_low = df_clean[df_clean['high_integration_cost'] == 0]
    if len(df_low) > 0:
        vagueness_bins = pd.cut(df_low['vagueness'], bins=5)
        success_rate = df_low.groupby(vagueness_bins, observed=True)[dv_col].mean()
        bin_centers = [interval.mid for interval in success_rate.index]

        axes[0].bar(range(len(success_rate)), success_rate.values,
                   alpha=0.7, color='blue', edgecolor='black')
        axes[0].set_xticks(range(len(success_rate)))
        axes[0].set_xticklabels([f'{c:.1f}' for c in bin_centers], rotation=45)
        axes[0].set_xlabel('Vagueness (bin center, 0-100)')
        axes[0].set_ylabel('Survival Rate')
        axes[0].set_title('Modular Sectors (Low Integration Cost)')
        axes[0].set_ylim([0, 1])
        axes[0].grid(True, alpha=0.3, axis='y')

    # Right plot: High integration cost (integrated)
    df_high = df_clean[df_clean['high_integration_cost'] == 1]
    if len(df_high) > 0:
        vagueness_bins = pd.cut(df_high['vagueness'], bins=5)
        success_rate = df_high.groupby(vagueness_bins, observed=True)[dv_col].mean()
        bin_centers = [interval.mid for interval in success_rate.index]

        axes[1].bar(range(len(success_rate)), success_rate.values,
                   alpha=0.7, color='red', edgecolor='black')
        axes[1].set_xticks(range(len(success_rate)))
        axes[1].set_xticklabels([f'{c:.1f}' for c in bin_centers], rotation=45)
        axes[1].set_xlabel('Vagueness (bin center, 0-100)')
        axes[1].set_ylabel('Survival Rate')
        axes[1].set_title('Integrated Sectors (High Integration Cost)')
        axes[1].set_ylim([0, 1])
        axes[1].grid(True, alpha=0.3, axis='y')

    fig.suptitle('H2 Main: Survival Rates by Vagueness Bins', fontsize=14, fontweight='bold')
    plt.tight_layout()

    if output_path:
        fig.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {output_path}")

    return fig


def plot_h2_roc_curve(
    df: pd.DataFrame,
    model: BinaryResultsWrapper,
    output_path: Optional[Path] = None
) -> plt.Figure:
    """
    Create ROC curve for H2 survival model.

    Args:
        df: DataFrame with data
        model: Fitted H2 model
        output_path: Optional path to save figure

    Returns:
        Matplotlib figure object
    """
    fig, ax = plt.subplots(figsize=(8, 8))

    # Determine DV column
    dv_col = 'survival' if 'survival' in df.columns else 'later_success'

    # Get predictions and actual values
    y_true = model.model.endog  # Actual values
    y_pred_proba = model.predict()  # Predicted probabilities

    # Compute ROC curve
    fpr, tpr, thresholds = roc_curve(y_true, y_pred_proba)
    roc_auc = auc(fpr, tpr)

    # Plot
    ax.plot(fpr, tpr, color='darkorange', lw=2,
            label=f'ROC curve (AUC = {roc_auc:.3f})')
    ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--',
            label='Random classifier')

    # Formatting
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('False Positive Rate', fontsize=12, fontweight='bold')
    ax.set_ylabel('True Positive Rate', fontsize=12, fontweight='bold')
    ax.set_title('H2 Survival Model: ROC Curve', fontsize=14, fontweight='bold')
    ax.legend(loc="lower right", fontsize=11)
    ax.grid(True, alpha=0.3)

    # Add diagonal
    ax.set_aspect('equal', adjustable='box')

    plt.tight_layout()

    if output_path:
        fig.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {output_path}")

    return fig


# =============================================================================
# REGRESSION TABLES (AER STYLE)
# =============================================================================

def create_regression_table(
    results: Dict,
    output_path: Optional[Path] = None
) -> pd.DataFrame:
    """
    Create AER-style regression table for all hypothesis tests.

    Args:
        results: Dictionary with 'h1', 'h2_main', 'h2_robustness' model results
        output_path: Optional path to save table as CSV

    Returns:
        DataFrame with regression results
    """
    table_data = []

    models = {
        'H1: Early Funding': results.get('h1'),
        'H2 Main: Survival': results.get('h2_main'),
        'H2 Robust: Series B': results.get('h2_robustness')
    }

    # Collect all unique variable names
    all_vars = set()
    for model in models.values():
        if model is not None:
            all_vars.update(model.params.index)

    # Prioritize key variables
    key_vars = [
        'Intercept', 'vagueness', 'high_integration_cost',
        'vagueness:high_integration_cost', 'founder_credibility',
        'employees_log', 'year_founded', 'series_a_funding', 'is_down_round'
    ]

    # Add sector FE categories
    sector_vars = [v for v in all_vars if v.startswith('C(sector_fe)')]
    ordered_vars = key_vars + sorted(sector_vars) + sorted(all_vars - set(key_vars) - set(sector_vars))

    for var in ordered_vars:
        if var not in all_vars:
            continue

        row = {'Variable': var}

        for model_name, model in models.items():
            if model is None:
                row[f'{model_name} (Coef)'] = ''
                row[f'{model_name} (SE)'] = ''
                continue

            if var in model.params:
                coef = model.params[var]
                se = model.bse[var]
                pval = model.pvalues[var]

                # Format coefficient with stars
                if pval < 0.001:
                    stars = '***'
                elif pval < 0.01:
                    stars = '**'
                elif pval < 0.05:
                    stars = '*'
                elif pval < 0.1:
                    stars = '†'
                else:
                    stars = ''

                row[f'{model_name} (Coef)'] = f'{coef:.4f}{stars}'
                row[f'{model_name} (SE)'] = f'({se:.4f})'
            else:
                row[f'{model_name} (Coef)'] = ''
                row[f'{model_name} (SE)'] = ''

        table_data.append(row)

    # Add model statistics
    table_data.append({'Variable': '---' * 20})

    # N observations
    row_n = {'Variable': 'N'}
    for model_name, model in models.items():
        if model is not None:
            row_n[f'{model_name} (Coef)'] = int(model.nobs)
            row_n[f'{model_name} (SE)'] = ''
        else:
            row_n[f'{model_name} (Coef)'] = ''
            row_n[f'{model_name} (SE)'] = ''
    table_data.append(row_n)

    # R² / Pseudo R²
    row_r2 = {'Variable': 'R² / Pseudo R²'}
    for model_name, model in models.items():
        if model is not None:
            if hasattr(model, 'rsquared'):
                row_r2[f'{model_name} (Coef)'] = f'{model.rsquared:.3f}'
            elif hasattr(model, 'prsquared'):
                row_r2[f'{model_name} (Coef)'] = f'{model.prsquared:.3f}'
            row_r2[f'{model_name} (SE)'] = ''
        else:
            row_r2[f'{model_name} (Coef)'] = ''
            row_r2[f'{model_name} (SE)'] = ''
    table_data.append(row_r2)

    # Create DataFrame
    table_df = pd.DataFrame(table_data)

    if output_path:
        table_df.to_csv(output_path, index=False)
        print(f"  ✓ Saved: {output_path}")

    return table_df


# =============================================================================
# SUMMARY VISUALIZATIONS
# =============================================================================

def plot_coefficient_comparison(
    results: Dict,
    output_path: Optional[Path] = None
) -> plt.Figure:
    """
    Create coefficient comparison plot for key hypothesis tests.

    Args:
        results: Dictionary with 'h1' and 'h2' model results
        output_path: Optional path to save figure

    Returns:
        Matplotlib figure object
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    coefficients = []
    ci_lower = []
    ci_upper = []
    labels = []
    colors = []

    # H1 vagueness coefficient
    if results.get('h1') is not None:
        h1_model = results['h1']
        coef = h1_model.params.get('vagueness', np.nan)
        ci = h1_model.conf_int()

        coefficients.append(coef)
        ci_lower.append(ci.loc['vagueness', 0])
        ci_upper.append(ci.loc['vagueness', 1])
        labels.append('H1: α₁\n(Vagueness → Early Funding)')
        colors.append('green' if coef < 0 else 'red')

    # H2 Main coefficients
    h2_model = results.get('h2_main') or results.get('h2')  # Backward compat
    if h2_model is not None:
        ci = h2_model.conf_int()

        # β₁ (main effect)
        coef = h2_model.params.get('vagueness', np.nan)
        coefficients.append(coef)
        ci_lower.append(ci.loc['vagueness', 0])
        ci_upper.append(ci.loc['vagueness', 1])
        labels.append('H2 Main: β₁\n(Vagueness - Modular)')
        colors.append('green' if coef > 0 else 'red')

        # β₃ (interaction)
        if 'vagueness:high_integration_cost' in h2_model.params:
            coef = h2_model.params.get('vagueness:high_integration_cost', np.nan)
            coefficients.append(coef)
            ci_lower.append(ci.loc['vagueness:high_integration_cost', 0])
            ci_upper.append(ci.loc['vagueness:high_integration_cost', 1])
            labels.append('H2 Main: β₃\n(Interaction)')
            colors.append('green' if coef < 0 else 'red')

    # Create error bars
    y_pos = np.arange(len(coefficients))
    errors = [
        [coefficients[i] - ci_lower[i] for i in range(len(coefficients))],
        [ci_upper[i] - coefficients[i] for i in range(len(coefficients))]
    ]

    ax.barh(y_pos, coefficients, xerr=errors, color=colors, alpha=0.7,
            edgecolor='black', linewidth=1.5, capsize=5)

    # Add vertical line at zero
    ax.axvline(x=0, color='black', linestyle='--', linewidth=1)

    # Formatting
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.set_xlabel('Coefficient Estimate (95% CI)', fontsize=12, fontweight='bold')
    ax.set_title('Key Hypothesis Test Results', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')

    # Add expected signs
    expected = ['<0 (Negative)', '>0 (Positive)', '<0 (Negative)']
    for i, (exp, coef) in enumerate(zip(expected[:len(coefficients)], coefficients)):
        ax.text(coef, i, f'  Expected: {exp}', va='center',
                fontsize=9, style='italic')

    plt.tight_layout()

    if output_path:
        fig.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {output_path}")

    return fig


# =============================================================================
# MAIN VISUALIZATION PIPELINE
# =============================================================================

def create_all_visualizations(
    df: pd.DataFrame,
    results: Dict,
    output_dir: Path
) -> Dict[str, Path]:
    """
    Create all diagnostic plots and save to output directory.

    Args:
        df: DataFrame with analysis data
        results: Dictionary with 'h1', 'h2_main', 'h2_robustness' model results
        output_dir: Directory to save plots

    Returns:
        Dictionary mapping plot names to file paths
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("\n" + "="*80)
    print("CREATING VISUALIZATIONS")
    print("="*80)

    created_files = {}

    # H1 plots
    if results.get('h1') is not None:
        print("\nH1 Visualizations:")

        # Scatter plot
        fig = plot_h1_scatter(df, results['h1'], output_dir / "h1_scatter.png")
        created_files['h1_scatter'] = output_dir / "h1_scatter.png"
        plt.close(fig)

        # Residual diagnostics
        fig = plot_h1_residuals(results['h1'], output_dir / "h1_diagnostics.png")
        created_files['h1_diagnostics'] = output_dir / "h1_diagnostics.png"
        plt.close(fig)

    # H2 Main plots
    h2_model = results.get('h2_main') or results.get('h2')  # Backward compat
    if h2_model is not None:
        print("\nH2 Main Visualizations:")

        # Interaction plot
        fig = plot_h2_interaction(df, h2_model, output_dir / "h2_interaction.png")
        created_files['h2_interaction'] = output_dir / "h2_interaction.png"
        plt.close(fig)

        # Marginal effects
        fig = plot_h2_marginal_effects(df, h2_model, output_dir / "h2_marginal_effects.png")
        created_files['h2_marginal_effects'] = output_dir / "h2_marginal_effects.png"
        plt.close(fig)

        # ROC curve
        fig = plot_h2_roc_curve(df, h2_model, output_dir / "h2_roc_curve.png")
        created_files['h2_roc_curve'] = output_dir / "h2_roc_curve.png"
        plt.close(fig)

    # Summary visualizations
    print("\nSummary Visualizations:")

    # Coefficient comparison
    fig = plot_coefficient_comparison(results, output_dir / "coefficient_comparison.png")
    created_files['coefficient_comparison'] = output_dir / "coefficient_comparison.png"
    plt.close(fig)

    # Regression table
    table = create_regression_table(results, output_dir / "regression_table.csv")
    created_files['regression_table'] = output_dir / "regression_table.csv"

    print("\n" + "="*80)
    print(f"✓ Created {len(created_files)} output files")
    print("="*80)

    return created_files


# =============================================================================
# BAKE-OFF VISUALIZATIONS
# =============================================================================

def save_univariate_distributions(df: pd.DataFrame, outdir: Path) -> None:
    """
    Save univariate distribution plot for bake-off analysis with risk labels.

    Args:
        df: DataFrame with analysis data
        outdir: Output directory for saved plot
    """
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Univariate Distributions - Bake-off Variables', fontsize=16, y=0.995)

    # 1. Vagueness (continuous)
    ax = axes[0, 0]
    if 'vagueness' in df.columns:
        vague_data = df['vagueness'].dropna()
        ax.hist(vague_data, bins=50, edgecolor='black', alpha=0.7, color='steelblue')
        ax.axvline(vague_data.median(), color='red', linestyle='--',
                   label=f'Median={vague_data.median():.1f}')
        ax.set_xlabel('Vagueness Score (0-100)')
        ax.set_ylabel('Frequency')
        ax.set_title(f'Vagueness (n={len(vague_data):,})')
        ax.legend()

    # 2. is_hardware (binary moderator)
    ax = axes[0, 1]
    if 'is_hardware' in df.columns:
        hw_counts = df['is_hardware'].value_counts()
        hw_pct = hw_counts / hw_counts.sum() * 100
        colors = ['#2ecc71', '#e67e22']  # Green for 0, Orange for 1
        bars = ax.bar(['Software (0)', 'Hardware (1)'],
                      hw_pct.reindex([0, 1], fill_value=0),
                      color=colors, edgecolor='black', alpha=0.7)
        ax.set_ylabel('Percentage (%)')
        ax.set_title(f'Integration Cost / is_hardware (n={hw_counts.sum():,})')

        # Add percentages on bars
        for i, (val, pct) in enumerate(zip([0, 1], hw_pct.reindex([0, 1], fill_value=0))):
            count = hw_counts.get(val, 0)
            ax.text(i, pct + 1, f'{pct:.1f}%\n(n={count:,})',
                   ha='center', va='bottom', fontsize=9)

        # Risk label if hardware < 10%
        hw_minority_pct = hw_pct.get(1, 0)
        if hw_minority_pct < 10:
            ax.text(0.5, 0.95, '⚠️ HIGH RISK: Severe imbalance',
                   transform=ax.transAxes, ha='center', va='top',
                   fontsize=11, fontweight='bold', color='red',
                   bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

    # 3. is_serial (binary moderator)
    ax = axes[0, 2]
    if 'is_serial' in df.columns:
        serial_counts = df['is_serial'].value_counts()
        serial_pct = serial_counts / serial_counts.sum() * 100
        colors = ['#95a5a6', '#9b59b6']  # Gray for 0, Purple for 1
        bars = ax.bar(['Non-serial (0)', 'Serial (1)'],
                      serial_pct.reindex([0, 1], fill_value=0),
                      color=colors, edgecolor='black', alpha=0.7)
        ax.set_ylabel('Percentage (%)')
        ax.set_title(f'Founder Credibility / is_serial (n={serial_counts.sum():,})')

        # Add percentages on bars
        for i, (val, pct) in enumerate(zip([0, 1], serial_pct.reindex([0, 1], fill_value=0))):
            count = serial_counts.get(val, 0)
            ax.text(i, pct + 1, f'{pct:.1f}%\n(n={count:,})',
                   ha='center', va='bottom', fontsize=9)

        # Risk label if serial < 10%
        serial_minority_pct = serial_pct.get(1, 0)
        if serial_minority_pct < 10:
            ax.text(0.5, 0.95, '⚠️ HIGH RISK: Severe imbalance',
                   transform=ax.transAxes, ha='center', va='top',
                   fontsize=11, fontweight='bold', color='red',
                   bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

    # 4. Growth (DV)
    ax = axes[1, 0]
    if 'growth' in df.columns:
        growth_counts = df['growth'].value_counts()
        growth_pct = growth_counts / growth_counts.sum() * 100
        colors = ['#e74c3c', '#2ecc71']  # Red for 0, Green for 1
        ax.bar(['No Growth (0)', 'Growth (1)'],
               growth_pct.reindex([0, 1], fill_value=0),
               color=colors, edgecolor='black', alpha=0.7)
        ax.set_ylabel('Percentage (%)')
        ax.set_title(f'Growth DV (n={growth_counts.sum():,})')

        for i, (val, pct) in enumerate(zip([0, 1], growth_pct.reindex([0, 1], fill_value=0))):
            count = growth_counts.get(val, 0)
            ax.text(i, pct + 1, f'{pct:.1f}%\n(n={count:,})',
                   ha='center', va='bottom', fontsize=9)

    # 5. Employees (control)
    ax = axes[1, 1]
    if 'employees_log' in df.columns:
        emp_data = df['employees_log'].dropna()
        ax.hist(emp_data, bins=50, edgecolor='black', alpha=0.7, color='steelblue')
        ax.axvline(emp_data.median(), color='red', linestyle='--',
                   label=f'Median={emp_data.median():.2f}')
        ax.set_xlabel('log(Employees)')
        ax.set_ylabel('Frequency')
        ax.set_title(f'Employees (n={len(emp_data):,})')
        ax.legend()

    # 6. Sector FE (control)
    ax = axes[1, 2]
    if 'sector_fe' in df.columns:
        sector_counts = df['sector_fe'].value_counts().head(8)
        sector_pct = sector_counts / len(df) * 100
        sector_pct.plot(kind='barh', ax=ax, color='steelblue', edgecolor='black', alpha=0.7)
        ax.set_xlabel('Percentage (%)')
        ax.set_title(f'Sector Distribution (n={df["sector_fe"].notna().sum():,})')
        ax.invert_yaxis()

    plt.tight_layout()
    output_path = outdir / 'univariate_distributions.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"  ✓ Saved: {output_path}")
    plt.close(fig)


def save_h2_interaction_architecture(df: pd.DataFrame, outdir: Path) -> None:
    """
    Save interaction plot: vagueness × is_hardware.

    Args:
        df: DataFrame with analysis data
        outdir: Output directory for saved plot
    """
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Filter valid data
    df_valid = df[df['growth'].notna() & df['vagueness'].notna() & df['is_hardware'].notna()].copy()

    # Create vagueness quintiles
    df_valid['vagueness_quintile'] = pd.qcut(df_valid['vagueness'], q=5, labels=['Q1', 'Q2', 'Q3', 'Q4', 'Q5'], duplicates='drop')

    # Calculate mean growth by quintile and is_hardware
    interaction_data = df_valid.groupby(['vagueness_quintile', 'is_hardware']).agg({
        'growth': ['mean', 'count']
    }).reset_index()
    interaction_data.columns = ['quintile', 'is_hardware', 'mean_growth', 'count']

    # Plot lines for each moderator level
    colors = {'Software (0)': '#2ecc71', 'Hardware (1)': '#e67e22'}
    markers = {0: 'o', 1: 's'}

    for hw_val in [0, 1]:
        subset = interaction_data[interaction_data['is_hardware'] == hw_val]
        if len(subset) > 0:
            label = 'Software (0)' if hw_val == 0 else 'Hardware (1)'
            ax.plot(range(len(subset)), subset['mean_growth'] * 100,
                   marker=markers[hw_val], markersize=10, linewidth=2.5,
                   label=label, color=colors[label])

            # Add sample size labels
            for i, (idx, row) in enumerate(subset.iterrows()):
                ax.text(i, row['mean_growth'] * 100 + 1, f"n={int(row['count'])}",
                       ha='center', va='bottom', fontsize=8, alpha=0.7)

    ax.set_xlabel('Vagueness Quintile', fontsize=12, fontweight='bold')
    ax.set_ylabel('Growth Rate (%)', fontsize=12, fontweight='bold')
    ax.set_title('H2-Architecture: Vagueness × is_hardware Interaction',
                fontsize=14, fontweight='bold')
    ax.set_xticks(range(5))
    ax.set_xticklabels(['Q1\n(Low)', 'Q2', 'Q3', 'Q4', 'Q5\n(High)'])
    ax.legend(loc='best', fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, max(interaction_data['mean_growth'].max() * 100 + 5, 20))

    plt.tight_layout()
    output_path = outdir / 'h2_interaction_architecture.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"  ✓ Saved: {output_path}")
    plt.close(fig)


def save_moderator_overlap(df: pd.DataFrame, outdir: Path, moderator: str) -> None:
    """
    Save ECDF/histogram overlap plot for moderator positivity check.

    Args:
        df: DataFrame with analysis data
        outdir: Output directory for saved plot
        moderator: Moderator variable name ("is_hardware" or "is_serial")
    """
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Filter valid data
    df_valid = df[df['vagueness'].notna() & df[moderator].notna()].copy()

    # Get groups
    group_0 = df_valid[df_valid[moderator] == 0]['vagueness']
    group_1 = df_valid[df_valid[moderator] == 1]['vagueness']

    # Labels
    if moderator == 'is_hardware':
        label_0, label_1 = 'Software (0)', 'Hardware (1)'
        colors = ['#2ecc71', '#e67e22']
    elif moderator == 'is_serial':
        label_0, label_1 = 'Non-serial (0)', 'Serial (1)'
        colors = ['#95a5a6', '#9b59b6']
    else:
        label_0, label_1 = f'{moderator}=0', f'{moderator}=1'
        colors = ['blue', 'red']

    # Left plot: Histogram overlap
    ax = axes[0]
    ax.hist(group_0, bins=30, alpha=0.5, label=f'{label_0} (n={len(group_0):,})',
            color=colors[0], edgecolor='black')
    ax.hist(group_1, bins=30, alpha=0.5, label=f'{label_1} (n={len(group_1):,})',
            color=colors[1], edgecolor='black')
    ax.set_xlabel('Vagueness Score (0-100)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=11, fontweight='bold')
    ax.set_title(f'Vagueness Distribution by {moderator}', fontsize=12, fontweight='bold')
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3, axis='y')

    # Calculate SMD
    mean_0, std_0 = group_0.mean(), group_0.std()
    mean_1, std_1 = group_1.mean(), group_1.std()
    pooled_std = np.sqrt((std_0**2 + std_1**2) / 2)
    smd = (mean_1 - mean_0) / pooled_std if pooled_std > 0 else 0

    ax.text(0.05, 0.95, f'SMD = {smd:.3f}',
            transform=ax.transAxes, fontsize=10,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    # Right plot: ECDF
    ax = axes[1]

    # Sort and compute ECDF
    sorted_0 = np.sort(group_0)
    ecdf_0 = np.arange(1, len(sorted_0) + 1) / len(sorted_0)

    sorted_1 = np.sort(group_1)
    ecdf_1 = np.arange(1, len(sorted_1) + 1) / len(sorted_1)

    ax.plot(sorted_0, ecdf_0, label=label_0, color=colors[0], linewidth=2)
    ax.plot(sorted_1, ecdf_1, label=label_1, color=colors[1], linewidth=2)

    ax.set_xlabel('Vagueness Score (0-100)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Cumulative Probability', fontsize=11, fontweight='bold')
    ax.set_title('ECDF: Positivity Check', fontsize=12, fontweight='bold')
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)

    # KS statistic
    ks_stat = np.max(np.abs(
        np.interp(sorted_0, sorted_1, ecdf_1, left=0, right=1) - ecdf_0
    ))
    ax.text(0.05, 0.95, f'KS stat = {ks_stat:.3f}',
            transform=ax.transAxes, fontsize=10,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

    plt.tight_layout()
    output_path = outdir / f'moderator_overlap_{moderator}.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"  ✓ Saved: {output_path}")
    plt.close(fig)


def save_h2_interaction(df: pd.DataFrame, outdir: Path, moderator: str) -> None:
    """
    Save interaction plot: vagueness × moderator with Wilson CI.

    Args:
        df: DataFrame with analysis data
        outdir: Output directory for saved plot
        moderator: Moderator variable name ("is_hardware" or "is_serial")
    """
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Filter valid data
    df_valid = df[df['growth'].notna() & df['vagueness'].notna() & df[moderator].notna()].copy()

    # Create vagueness quintiles
    df_valid['vagueness_quintile'] = pd.qcut(
        df_valid['vagueness'], q=5,
        labels=['Q1', 'Q2', 'Q3', 'Q4', 'Q5'],
        duplicates='drop'
    )

    # Calculate mean growth by quintile and moderator
    interaction_data = df_valid.groupby(['vagueness_quintile', moderator]).agg({
        'growth': ['sum', 'count']
    }).reset_index()
    interaction_data.columns = ['quintile', moderator, 'successes', 'trials']
    interaction_data['rate'] = interaction_data['successes'] / interaction_data['trials']

    # Wilson confidence intervals
    def wilson_ci(successes, trials, alpha=0.05):
        """Calculate Wilson score confidence interval."""
        from scipy import stats
        z = stats.norm.ppf(1 - alpha/2)
        p = successes / trials
        denominator = 1 + z**2/trials
        center = (p + z**2/(2*trials)) / denominator
        margin = z * np.sqrt(p*(1-p)/trials + z**2/(4*trials**2)) / denominator
        return center - margin, center + margin

    interaction_data['ci_lower'] = interaction_data.apply(
        lambda row: wilson_ci(row['successes'], row['trials'])[0], axis=1
    )
    interaction_data['ci_upper'] = interaction_data.apply(
        lambda row: wilson_ci(row['successes'], row['trials'])[1], axis=1
    )

    # Labels and colors
    if moderator == 'is_hardware':
        labels = {0: 'Software (0)', 1: 'Hardware (1)'}
        colors = {0: '#2ecc71', 1: '#e67e22'}
    elif moderator == 'is_serial':
        labels = {0: 'Non-serial (0)', 1: 'Serial (1)'}
        colors = {0: '#95a5a6', 1: '#9b59b6'}
    else:
        labels = {0: f'{moderator}=0', 1: f'{moderator}=1'}
        colors = {0: 'blue', 1: 'red'}

    markers = {0: 'o', 1: 's'}

    # Plot lines for each moderator level
    for mod_val in [0, 1]:
        subset = interaction_data[interaction_data[moderator] == mod_val]
        if len(subset) > 0:
            x_pos = range(len(subset))
            y_vals = subset['rate'] * 100

            # Plot line with markers
            ax.plot(x_pos, y_vals,
                   marker=markers[mod_val], markersize=10, linewidth=2.5,
                   label=labels[mod_val], color=colors[mod_val])

            # Add error bars (Wilson CI)
            ax.fill_between(x_pos,
                           subset['ci_lower'] * 100,
                           subset['ci_upper'] * 100,
                           alpha=0.2, color=colors[mod_val])

            # Add sample size labels
            for i, (idx, row) in enumerate(subset.iterrows()):
                ax.text(i, row['rate'] * 100 + 1.5,
                       f"n={int(row['trials'])}",
                       ha='center', va='bottom', fontsize=8, alpha=0.7)

    ax.set_xlabel('Vagueness Quintile', fontsize=12, fontweight='bold')
    ax.set_ylabel('Growth Rate (%)', fontsize=12, fontweight='bold')

    title_suffix = 'is_hardware' if moderator == 'is_hardware' else 'is_serial'
    ax.set_title(f'H2 Interaction: Vagueness × {title_suffix}',
                fontsize=14, fontweight='bold')

    ax.set_xticks(range(5))
    ax.set_xticklabels(['Q1\n(Low)', 'Q2', 'Q3', 'Q4', 'Q5\n(High)'])
    ax.legend(loc='best', fontsize=11)
    ax.grid(True, alpha=0.3)

    # Dynamic y-limit
    max_val = interaction_data['ci_upper'].max() * 100
    ax.set_ylim(0, max(max_val + 5, 20))

    plt.tight_layout()
    output_path = outdir / f'h2_interaction_{moderator}.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"  ✓ Saved: {output_path}")
    plt.close(fig)


# Backward compatibility wrappers
def save_h2_interaction_architecture(df: pd.DataFrame, outdir: Path) -> None:
    """Backward compatible wrapper for save_h2_interaction with is_hardware."""
    save_h2_interaction(df, outdir, "is_hardware")


def save_h2_interaction_founder(df: pd.DataFrame, outdir: Path) -> None:
    """Backward compatible wrapper for save_h2_interaction with is_serial."""
    save_h2_interaction(df, outdir, "is_serial")


# =============================================================================
# ONE-TOUCH EXECUTION: MODEL-BASED FIGURES
# =============================================================================

def fig_reversal_from_models(
    df: pd.DataFrame,
    h1: RegressionResultsWrapper,
    h2: BinaryResultsWrapper,
    outdir: Path = Path("outputs/figures")
) -> None:
    """
    Figure 1: The Reversal - dual-axis plot showing H1 and H2 predictions.

    Left axis (H1 OLS): Series A amount vs vagueness
    Right axis (H2 Logit): P(Series B+) vs vagueness, y in [0,1]

    Args:
        df: DataFrame with analysis data
        h1: Fitted H1 OLS model
        h2: Fitted H2 Logit model
        outdir: Output directory for saved plot
    """
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Create shared z_vagueness grid
    z_vague_range = np.linspace(
        df['z_vagueness'].min(),
        df['z_vagueness'].max(),
        100
    )

    # Get mean values for control variables
    z_emp_mean = df['z_employees_log'].mean()

    # Find most common founding cohort
    if 'founding_cohort' in df.columns:
        cohort_mode = df['founding_cohort'].mode()[0] if len(df['founding_cohort'].mode()) > 0 else None
    else:
        cohort_mode = None

    # --- LEFT AXIS: H1 (OLS) Series A Amount ---
    # Build prediction DataFrame for H1
    pred_df_h1 = pd.DataFrame({
        'z_vagueness': z_vague_range,
        'z_employees_log': z_emp_mean
    })

    if cohort_mode is not None:
        pred_df_h1['founding_cohort'] = cohort_mode

    if 'sector_fe' in df.columns:
        sector_mode = df['sector_fe'].mode()[0] if len(df['sector_fe'].mode()) > 0 else 'Other'
        pred_df_h1['sector_fe'] = sector_mode

    try:
        h1_pred = h1.predict(pred_df_h1)
        ax1.plot(z_vague_range, h1_pred, 'b-', linewidth=3, label='H1: Series A Amount')
        ax1.set_xlabel('Vagueness (z-score)', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Series A Amount ($M)', fontsize=12, fontweight='bold', color='b')
        ax1.tick_params(axis='y', labelcolor='b')
    except Exception as e:
        print(f"  ⚠️ Warning: Could not plot H1 predictions: {e}")

    # --- RIGHT AXIS: H2 (Logit) P(Series B+) ---
    ax2 = ax1.twinx()

    # Build prediction DataFrame for H2
    pred_df_h2 = pd.DataFrame({
        'z_vagueness': z_vague_range,
        'z_employees_log': z_emp_mean,
        'is_hardware': 0  # Reference group (software)
    })

    if cohort_mode is not None:
        pred_df_h2['founding_cohort'] = cohort_mode

    try:
        h2_pred = h2.predict(pred_df_h2)
        ax2.plot(z_vague_range, h2_pred, 'r--', linewidth=3, label='H2: P(Series B+)')
        ax2.set_ylabel('P(Series B+)', fontsize=12, fontweight='bold', color='r')
        ax2.set_ylim([0, 1])
        ax2.tick_params(axis='y', labelcolor='r')
    except Exception as e:
        print(f"  ⚠️ Warning: Could not plot H2 predictions: {e}")

    # Title and legend
    ax1.set_title('Figure 1: The Reversal - Early Funding vs Later Success',
                  fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)

    # Combine legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='best')

    plt.tight_layout()
    output_path = outdir / 'Figure_1_Reversal.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"  ✓ Saved: {output_path}")
    plt.close(fig)


def fig_founder_interactions(
    df: pd.DataFrame,
    h3: RegressionResultsWrapper,
    h4: BinaryResultsWrapper,
    outdir: Path = Path("outputs/figures")
) -> None:
    """
    Figure 2: Founder Interaction Plots (H3 and H4).

    Figure 2a (H3): Scatter + regression line per founder group (OLS)
    Figure 2b (H4): Scatter + logistic regression line per founder group (Logit)

    Uses purple palette for founder credibility:
    - Serial Founder (1): '#6f42c1'
    - Not Serial (0): '#d8bfff'

    Args:
        df: DataFrame with analysis data (must have founder_serial and founder_serial_cat)
        h3: Fitted H3 OLS model
        h4: Fitted H4 Logit model
        outdir: Output directory for saved plots
    """
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    # Ensure founder_serial and founder_serial_cat exist
    df_plot = df.copy()

    # Priority: 1) founder_serial, 2) is_serial, 3) founder_credibility
    if 'founder_serial' not in df_plot.columns:
        if 'is_serial' in df_plot.columns:
            # Use existing is_serial (created in run_analysis.py)
            df_plot['founder_serial'] = df_plot['is_serial']
        elif 'founder_credibility' in df_plot.columns:
            # Create from founder_credibility
            df_plot['founder_serial'] = (df_plot['founder_credibility'] > 0).astype(int)
        else:
            raise KeyError(
                "Cannot find 'founder_serial', 'is_serial', or 'founder_credibility'. "
                "At least one is required for Figure 2 generation. "
                "Note: 'founder_credibility' may be dropped if std=0 in preprocess_for_h2()."
            )

    if 'founder_serial_cat' not in df_plot.columns:
        df_plot['founder_serial_cat'] = df_plot['founder_serial'].map({
            0: 'Not Serial (0)',
            1: 'Serial Founder (1)'
        })

    # Palette (purple theme for founder)
    palette = {
        'Serial Founder (1)': '#6f42c1',
        'Not Serial (0)': '#d8bfff'
    }

    # --- FIGURE 2a: H3 (Early Funding - LOG TRANSFORMED) ---
    fig, ax = plt.subplots(figsize=(10, 6))

    # Filter data for H3
    df_h3 = df_plot[
        df_plot['early_funding_musd'].notna() &
        df_plot['z_vagueness'].notna() &
        df_plot['founder_serial'].notna()
    ].copy()

    # Apply log transformation to match H3 model (log1p handles zeros)
    df_h3['log_early_funding'] = np.log1p(df_h3['early_funding_musd'])

    # Scatter plot per group (using LOG-TRANSFORMED Y-axis)
    for serial_val, label in [(0, 'Not Serial (0)'), (1, 'Serial Founder (1)')]:
        subset = df_h3[df_h3['founder_serial_cat'] == label]
        if len(subset) > 0:
            ax.scatter(
                subset['z_vagueness'],
                subset['log_early_funding'],  # LOG-TRANSFORMED
                alpha=0.1,  # Reduced alpha for less visual clutter
                s=15,
                color=palette[label],
                label=f'{label} (n={len(subset):,})'
            )

    # Regression lines per group (predictions are already in log scale from H3 model)
    z_vague_range = np.linspace(df_h3['z_vagueness'].min(), df_h3['z_vagueness'].max(), 100)
    z_emp_mean = df_h3['z_employees_log'].mean()

    if 'founding_cohort' in df_h3.columns:
        cohort_mode = df_h3['founding_cohort'].mode()[0] if len(df_h3['founding_cohort'].mode()) > 0 else None
    else:
        cohort_mode = None

    if 'sector_fe' in df_h3.columns:
        sector_mode = df_h3['sector_fe'].mode()[0] if len(df_h3['sector_fe'].mode()) > 0 else 'Other'
    else:
        sector_mode = 'Other'

    # Store predictions for fill_between
    predictions_dict = {}
    for serial_val, label in [(0, 'Not Serial (0)'), (1, 'Serial Founder (1)')]:
        pred_df = pd.DataFrame({
            'z_vagueness': z_vague_range,
            'founder_serial': serial_val,
            'z_employees_log': z_emp_mean
        })

        if cohort_mode is not None:
            pred_df['founding_cohort'] = cohort_mode

        pred_df['sector_fe'] = sector_mode

        try:
            predictions = h3.predict(pred_df)
            predictions_dict[serial_val] = predictions
            ax.plot(z_vague_range, predictions, color=palette[label], linewidth=3, label=f'{label} (regression)')
        except Exception as e:
            print(f"  ⚠️ Warning: Could not plot H3 regression line for {label}: {e}")

    # Fill between lines to highlight interaction effect
    if len(predictions_dict) == 2:
        ax.fill_between(z_vague_range,
                        predictions_dict[0],
                        predictions_dict[1],
                        alpha=0.15,
                        color='gray',
                        label='Interaction effect')

    ax.set_xlabel('Vagueness (z-score)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Early Funding [Log(1 + $M)]', fontsize=12, fontweight='bold')
    ax.set_title('Figure 2a: H3 - Early Funding × Founder Credibility (OLS on Log(Y))',
                 fontsize=14, fontweight='bold')
    ax.legend(loc='best', fontsize=10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    output_path = outdir / 'Figure_2a_H3.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"  ✓ Saved: {output_path}")
    plt.close(fig)

    # --- FIGURE 2b: H4 (Growth) ---
    fig, ax = plt.subplots(figsize=(10, 6))

    # Filter data for H4
    df_h4 = df_plot[
        df_plot['growth'].notna() &
        df_plot['z_vagueness'].notna() &
        df_plot['founder_serial'].notna()
    ].copy()

    # SCATTER PLOT REMOVED: For binary outcomes, scatter creates visual noise
    # that obscures the key finding (regression line comparison).
    # Dense points at Y=0 and Y=1 make it difficult to see null interaction.
    #
    # Original scatter code (commented out):
    # for serial_val, label in [(0, 'Not Serial (0)'), (1, 'Serial Founder (1)')]:
    #     subset = df_h4[df_h4['founder_serial_cat'] == label]
    #     if len(subset) > 0:
    #         ax.scatter(
    #             subset['z_vagueness'],
    #             subset['growth'],
    #             alpha=0.15,
    #             s=15,
    #             color=palette[label],
    #             label=f'{label} (n={len(subset):,})'
    #         )

    # Logistic regression lines per group (logistic=True equivalent)
    z_vague_range = np.linspace(df_h4['z_vagueness'].min(), df_h4['z_vagueness'].max(), 100)
    z_emp_mean = df_h4['z_employees_log'].mean()

    if 'founding_cohort' in df_h4.columns:
        cohort_mode = df_h4['founding_cohort'].mode()[0] if len(df_h4['founding_cohort'].mode()) > 0 else None
    else:
        cohort_mode = None

    for serial_val, label in [(0, 'Not Serial (0)'), (1, 'Serial Founder (1)')]:
        pred_df = pd.DataFrame({
            'z_vagueness': z_vague_range,
            'founder_serial': serial_val,
            'z_employees_log': z_emp_mean
        })

        if cohort_mode is not None:
            pred_df['founding_cohort'] = cohort_mode

        try:
            # Logit model returns probabilities directly
            predictions = h4.predict(pred_df)

            # Add sample size to legend
            n_group = len(df_h4[df_h4['founder_serial'] == serial_val])
            ax.plot(z_vague_range, predictions, color=palette[label], linewidth=3,
                   label=f'{label} (n={n_group:,})')
        except Exception as e:
            print(f"  ⚠️ Warning: Could not plot H4 regression line for {label}: {e}")

    # Check interaction significance
    title = 'Figure 2b: H4 - Growth × Founder Credibility (Logit)'
    try:
        # Extract interaction term p-value
        param_names = [str(p) for p in h4.params.index]
        int_term = [p for p in param_names if 'vagueness' in p.lower() and 'serial' in p.lower()]
        if int_term and hasattr(h4, 'pvalues'):
            int_pval = h4.pvalues[int_term[0]]
            if int_pval >= 0.10:
                title += ' (Interaction Not Significant)'
    except Exception:
        pass  # If can't extract p-value, use base title

    ax.set_xlabel('Vagueness (z-score)', fontsize=12, fontweight='bold')
    ax.set_ylabel('P(Growth)', fontsize=12, fontweight='bold')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_ylim([0, 1])  # Fix y-axis to [0, 1] for probabilities
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    output_path = outdir / 'Figure_2b_H4.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"  ✓ Saved: {output_path}")
    plt.close(fig)


# =============================================================================
# 3📊PLOT1: VARIABLE DISTRIBUTIONS
# =============================================================================

def plot_variable_distributions(df: pd.DataFrame, output_path: Optional[Path] = None) -> plt.Figure:
    """Create 2x3 subplot of 5 core variables.

    Layout:
        [🧧E hist] [💰L bar] [🤙V hist]
        [💪F bar]  [💸S hist] [empty]

    Args:
        df: DataFrame with core variables
        output_path: Optional path to save figure

    Returns:
        Matplotlib figure object
    """
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Core Variable Distributions', fontsize=16, fontweight='bold', y=1.02)

    # 🧧E: Early funding (continuous)
    ax = axes[0, 0]
    if 'early_funding_musd' in df.columns:
        data = df['early_funding_musd'].dropna()
        if len(data) > 0:
            ax.hist(data, bins=50, edgecolor='black', alpha=0.7, color='steelblue')
            ax.set_xlabel('Early Funding ($M)', fontweight='bold')
            ax.set_ylabel('Count', fontweight='bold')
            ax.set_title(f'🧧E: Early Funding (n={len(data):,})', fontweight='bold')
            ax.text(0.95, 0.95, f'Mean: ${data.mean():.2f}M\nMedian: ${data.median():.2f}M',
                   transform=ax.transAxes, va='top', ha='right',
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    ax.grid(True, alpha=0.3)

    # 💰L: Growth (binary)
    ax = axes[0, 1]
    if 'growth' in df.columns:
        counts = df['growth'].value_counts().sort_index()
        colors = ['#d62728', '#2ca02c']
        ax.bar(range(len(counts)), counts.values, color=colors, edgecolor='black', alpha=0.7)
        ax.set_xticks(range(len(counts)))
        ax.set_xticklabels(['No Growth (0)', 'Growth (1)'], rotation=0)
        ax.set_ylabel('Count', fontweight='bold')
        ax.set_title(f'💰L: Growth Achievement (n={counts.sum():,})', fontweight='bold')
        pct = counts.get(1, 0) / counts.sum() * 100 if counts.sum() > 0 else 0
        ax.text(0.95, 0.95, f'Growth rate: {pct:.1f}%',
               transform=ax.transAxes, va='top', ha='right',
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    ax.grid(True, alpha=0.3, axis='y')

    # 🤙V: Vagueness (continuous)
    ax = axes[0, 2]
    if 'z_vagueness' in df.columns:
        data = df['z_vagueness'].dropna()
        if len(data) > 0:
            ax.hist(data, bins=50, edgecolor='black', alpha=0.7, color='orange')
            ax.axvline(0, color='red', linestyle='--', alpha=0.5, linewidth=2)
            ax.set_xlabel('Vagueness (z-score)', fontweight='bold')
            ax.set_ylabel('Count', fontweight='bold')
            ax.set_title(f'🤙V: Vagueness (n={len(data):,})', fontweight='bold')
            ax.text(0.95, 0.95, f'Mean: {data.mean():.2f}\nStd: {data.std():.2f}',
                   transform=ax.transAxes, va='top', ha='right',
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    ax.grid(True, alpha=0.3)

    # 💪F: Flexibility (binary)
    ax = axes[1, 0]
    if 'is_hardware' in df.columns:
        # Note: is_hardware = 1 (hardware), 0 (software/flexible)
        counts = df['is_hardware'].value_counts().sort_index()
        colors = ['#1f77b4', '#8c564b']
        ax.bar(range(len(counts)), counts.values, color=colors, edgecolor='black', alpha=0.7)
        ax.set_xticks(range(len(counts)))
        ax.set_xticklabels(['Software/Flexible (0)', 'Hardware/Rigid (1)'], rotation=0)
        ax.set_ylabel('Count', fontweight='bold')
        ax.set_title(f'💪F: Architecture (n={counts.sum():,})', fontweight='bold')
        pct_soft = counts.get(0, 0) / counts.sum() * 100 if counts.sum() > 0 else 0
        ax.text(0.95, 0.95, f'Software: {pct_soft:.1f}%',
               transform=ax.transAxes, va='top', ha='right',
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    ax.grid(True, alpha=0.3, axis='y')

    # 💸S: Step-up (continuous, optional)
    ax = axes[1, 1]
    if 'valuation_stepup' in df.columns:
        data = df['valuation_stepup'].dropna()
        if len(data) > 10:
            ax.hist(data, bins=50, edgecolor='black', alpha=0.7, color='purple')
            ax.set_xlabel('Log(Valuation Step-up)', fontweight='bold')
            ax.set_ylabel('Count', fontweight='bold')
            ax.set_title(f'💸S: Valuation Step-up (n={len(data):,})', fontweight='bold')
            ax.text(0.95, 0.95, f'Mean: {data.mean():.2f}\nMedian: {data.median():.2f}',
                   transform=ax.transAxes, va='top', ha='right',
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        else:
            ax.text(0.5, 0.5, 'Insufficient data\nfor valuation step-up',
                   ha='center', va='center', transform=ax.transAxes, fontsize=12)
            ax.set_title('💸S: Not Available', fontweight='bold')
    else:
        ax.text(0.5, 0.5, 'Valuation step-up\nnot available',
               ha='center', va='center', transform=ax.transAxes, fontsize=12)
        ax.set_title('💸S: Not Available', fontweight='bold')
    ax.grid(True, alpha=0.3)

    # Hide empty subplot
    axes[1, 2].axis('off')

    plt.tight_layout()

    if output_path:
        fig.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {output_path}")

    return fig


# =============================================================================
# 5📈PLOT2: MULTIVERSE ANALYSIS VISUALIZATIONS
# =============================================================================

def calculate_alignment(coef: float, pval: float, expected_sign: int) -> float:
    """Calculate alignment score between expected and actual results.

    Args:
        coef: Coefficient estimate
        pval: P-value
        expected_sign: Expected sign (+1 or -1)

    Returns:
        Alignment score:
            1.0: Perfect alignment (correct sign, significant)
            0.25: Partial alignment (correct sign, not significant)
            0.0: Neutral (not tested or inconclusive)
           -0.25: Partial misalignment (wrong sign, not significant)
           -1.0: Complete misalignment (wrong sign, significant)
    """
    if np.isnan(coef) or np.isnan(pval):
        return 0.0

    if pval >= 0.05:
        if np.sign(coef) == expected_sign:
            return 0.25  # Right direction but not significant
        else:
            return -0.25  # Wrong direction but not significant
    else:
        if np.sign(coef) == expected_sign:
            return 1.0  # Confirmed hypothesis
        else:
            return -1.0  # Rejected hypothesis


def plot_expectation_reality_heatmap(
    results: pd.DataFrame,
    output_path: Optional[Path] = None
) -> plt.Figure:
    """Create heatmap showing alignment between expected and actual results.

    Visual encoding:
        🟢 Green (+1.0): Expected positive, Got positive & significant
        🔴 Red (-1.0): Expected positive, Got negative & significant
        🟡 Yellow (0.25): Right direction, not significant
        ⚫ Gray (0.0): Not tested or inconclusive

    Args:
        results: DataFrame with multiverse results
        output_path: Optional path to save figure

    Returns:
        Matplotlib figure object
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Multiverse Analysis: Expectation vs Reality', fontsize=16, fontweight='bold', y=1.02)

    # Define expectations for each hypothesis
    hypotheses = {
        'H1_early_funding': {'expected_sign': -1, 'label': 'Early Funding ↓', 'coef_col': 'coef_vagueness'},
        'H2_growth': {'expected_sign': +1, 'label': 'Growth ↑', 'coef_col': 'coef_vagueness'},
        'H2_interaction': {'expected_sign': -1, 'label': 'Growth×Hardware ↓', 'coef_col': 'coef_interaction'}
    }

    for idx, (hyp_name, hyp_info) in enumerate(list(hypotheses.items())[:3]):
        ax = axes[idx // 2, idx % 2]

        # Calculate alignment scores
        if hyp_info['coef_col'] in results.columns and 'pvalue' in results.columns:
            results_hyp = results.copy()
            results_hyp['alignment'] = results_hyp.apply(
                lambda row: calculate_alignment(
                    row.get(hyp_info['coef_col'], np.nan),
                    row.get('pvalue', np.nan),
                    hyp_info['expected_sign']
                ), axis=1
            )

            # Create heatmap matrix (simplified version)
            if 'window' in results_hyp.columns and 'scaling' in results_hyp.columns:
                matrix = results_hyp.pivot_table(
                    values='alignment',
                    index='window',
                    columns='scaling',
                    aggfunc='mean'
                )

                # Custom colormap: Red-Yellow-Green
                colors = ['#d73027', '#fee08b', '#1a9850']
                cmap = sns.blend_palette(colors, as_cmap=True)

                # Plot heatmap
                sns.heatmap(
                    matrix,
                    cmap=cmap,
                    center=0,
                    vmin=-1,
                    vmax=1,
                    annot=True,
                    fmt='.2f',
                    cbar_kws={'label': 'Alignment Score'},
                    ax=ax,
                    linewidths=0.5,
                    linecolor='gray'
                )

                ax.set_title(f"{hyp_name}: {hyp_info['label']}", fontweight='bold')
                ax.set_xlabel('Scaling Method', fontweight='bold')
                ax.set_ylabel('Time Window', fontweight='bold')
            else:
                ax.text(0.5, 0.5, f'Data not available\nfor {hyp_name}',
                       ha='center', va='center', transform=ax.transAxes, fontsize=12)
        else:
            ax.text(0.5, 0.5, f'Columns not found\nfor {hyp_name}',
                   ha='center', va='center', transform=ax.transAxes, fontsize=12)

    # Summary panel (bottom right)
    ax_summary = axes[1, 1]
    ax_summary.axis('off')

    # Calculate summary statistics
    summary_text = "Summary Statistics\n" + "="*40 + "\n\n"
    for hyp_name, hyp_info in hypotheses.items():
        if hyp_info['coef_col'] in results.columns:
            results_hyp = results.copy()
            results_hyp['alignment'] = results_hyp.apply(
                lambda row: calculate_alignment(
                    row.get(hyp_info['coef_col'], np.nan),
                    row.get('pvalue', np.nan),
                    hyp_info['expected_sign']
                ), axis=1
            )

            confirmed = (results_hyp['alignment'] == 1.0).sum()
            rejected = (results_hyp['alignment'] == -1.0).sum()
            total = len(results_hyp)

            summary_text += f"{hyp_name}:\n"
            summary_text += f"  ✓ Confirmed: {confirmed}/{total} ({confirmed/total*100:.1f}%)\n"
            summary_text += f"  ✗ Rejected: {rejected}/{total} ({rejected/total*100:.1f}%)\n\n"

    ax_summary.text(0.1, 0.9, summary_text, transform=ax_summary.transAxes,
                   va='top', ha='left', fontsize=10, family='monospace',
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    plt.tight_layout()

    if output_path:
        fig.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {output_path}")

    return fig


def plot_enhanced_specification_curve(
    results: pd.DataFrame,
    hypothesis_name: str = 'vagueness_main',
    expected_sign: int = 1,
    output_path: Optional[Path] = None
) -> plt.Figure:
    """Create specification curve with visual emphasis on surprising results.

    Args:
        results: DataFrame with multiverse results
        hypothesis_name: Name of hypothesis being tested
        expected_sign: Expected sign of coefficient (+1 or -1)
        output_path: Optional path to save figure

    Returns:
        Matplotlib figure object
    """
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 1, height_ratios=[2, 1, 1], hspace=0.1)

    # Prepare data
    df = results.copy()

    # Determine coefficient and p-value columns
    coef_col = 'coefficient' if 'coefficient' in df.columns else 'coef_vagueness'
    pval_col = 'pvalue' if 'pvalue' in df.columns else 'p_vagueness'

    if coef_col not in df.columns or pval_col not in df.columns:
        print(f"Warning: Required columns not found. Available: {df.columns.tolist()}")
        return fig

    # Calculate alignment
    df['alignment'] = df.apply(
        lambda row: calculate_alignment(row[coef_col], row[pval_col], expected_sign),
        axis=1
    )
    df['matches_expectation'] = df['alignment'] > 0

    # Sort by coefficient value
    df_sorted = df.sort_values(coef_col).reset_index(drop=True)
    x = np.arange(len(df_sorted))

    # Panel 1: Coefficient curve with confidence bands
    ax1 = fig.add_subplot(gs[0])

    # Color code by alignment
    colors = []
    for _, row in df_sorted.iterrows():
        if row[pval_col] < 0.05:
            if row['matches_expectation']:
                colors.append('#1a9850')  # Green: Confirmed
            else:
                colors.append('#d73027')  # Red: Surprising
        else:
            colors.append('#969696')  # Gray: Not significant

    # Plot coefficients with error bars (if std_error available)
    if 'std_error' in df_sorted.columns:
        ax1.errorbar(
            x,
            df_sorted[coef_col],
            yerr=1.96 * df_sorted['std_error'],
            fmt='none',
            alpha=0.3,
            color='gray'
        )

    # Scatter plot with colors
    ax1.scatter(
        x,
        df_sorted[coef_col],
        c=colors,
        s=30,
        alpha=0.8,
        edgecolors='black',
        linewidth=0.5
    )

    # Add expectation zone
    ylim = ax1.get_ylim()
    if expected_sign > 0:
        ax1.axhspan(0, ylim[1], alpha=0.1, color='green', label='Expected Zone')
        ax1.axhspan(ylim[0], 0, alpha=0.1, color='red', label='Surprise Zone')
    else:
        ax1.axhspan(ylim[0], 0, alpha=0.1, color='green', label='Expected Zone')
        ax1.axhspan(0, ylim[1], alpha=0.1, color='red', label='Surprise Zone')

    ax1.axhline(0, color='black', linestyle='-', linewidth=1, alpha=0.5)
    ax1.set_ylabel('Coefficient (β)', fontsize=12, fontweight='bold')
    ax1.set_title(f'Specification Curve: {len(df_sorted)} Model Variants', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)

    # Add summary statistics
    n_confirmed = sum(c == '#1a9850' for c in colors)
    n_surprising = sum(c == '#d73027' for c in colors)
    n_inconclusive = sum(c == '#969696' for c in colors)

    ax1.text(
        0.02, 0.98,
        f'✓ Confirmed: {n_confirmed}/{len(df_sorted)} ({n_confirmed/len(df_sorted)*100:.1f}%)\n'
        f'✗ Surprising: {n_surprising}/{len(df_sorted)} ({n_surprising/len(df_sorted)*100:.1f}%)\n'
        f'○ Inconclusive: {n_inconclusive}/{len(df_sorted)} ({n_inconclusive/len(df_sorted)*100:.1f}%)',
        transform=ax1.transAxes,
        verticalalignment='top',
        fontsize=10,
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.9)
    )

    # Panel 2: Specification indicators (placeholder)
    ax2 = fig.add_subplot(gs[1], sharex=ax1)
    ax2.set_ylabel('Spec Config', fontsize=10)
    ax2.set_yticks([])
    ax2.grid(True, alpha=0.3)

    # Panel 3: P-value distribution
    ax3 = fig.add_subplot(gs[2], sharex=ax1)
    ax3.scatter(x, -np.log10(df_sorted[pval_col]), c=colors, s=10, alpha=0.6)
    ax3.axhline(-np.log10(0.05), color='black', linestyle='--', alpha=0.5, label='p=0.05')
    ax3.set_ylabel('-log₁₀(p)', fontsize=10, fontweight='bold')
    ax3.set_xlabel('Specification Index', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.legend(loc='upper right')

    plt.suptitle(f'Multiverse Analysis: {hypothesis_name}', fontsize=16, fontweight='bold', y=1.00)

    if output_path:
        fig.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {output_path}")

    return fig


# =============================================================================
# F-SERIES PLOTS (TWO-SNAPSHOT MODE: E/L/S/V/F)
# =============================================================================

# Strict color palette
PALETTE = {"E": "red", "L": "blue", "V": "green", "S": "purple", "F": "skyblue", "C": "orange"}


def _num_median(df: pd.DataFrame, col: str) -> float:
    """Return numeric median, ignoring NA."""
    return df[col].median() if col in df.columns else 0.0


def _cat_mode(df: pd.DataFrame, col: str):
    """Return most frequent value for categorical variable."""
    if col not in df.columns:
        return None
    mode_vals = df[col].mode()
    return mode_vals[0] if len(mode_vals) > 0 else None


def _fix_controls_at_median_mode(df: pd.DataFrame, cols: list) -> dict:
    """
    Return a dict with median/mode values for prediction.

    Args:
        df: DataFrame with data
        cols: List of column names to fix

    Returns:
        Dictionary with fixed values
    """
    fixed = {}
    for col in cols:
        if col not in df.columns:
            continue
        if df[col].dtype in ['object', 'category']:
            fixed[col] = _cat_mode(df, col)
        else:
            fixed[col] = _num_median(df, col)
    return fixed


def fig_F1_E_vs_V(df: pd.DataFrame, hev: RegressionResultsWrapper, outdir: Path) -> Path:
    """
    F1: E vs V scatter with OLS fit line.

    Args:
        df: DataFrame with E, z_V
        hev: OLS model from run_HEV
        outdir: Output directory

    Returns:
        Path to saved PNG
    """
    outdir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Determine E column (prefer E_scaled)
    E_col = 'E_scaled' if 'E_scaled' in df.columns else 'E'
    V_col = 'z_V'

    # Scatter plot
    df_plot = df.dropna(subset=[E_col, V_col])
    ax.scatter(df_plot[V_col], df_plot[E_col], alpha=0.5, s=30, color=PALETTE['E'], edgecolors='k', linewidths=0.3)

    # OLS fit line
    V_range = np.linspace(df_plot[V_col].min(), df_plot[V_col].max(), 100)
    pred_df = pd.DataFrame({V_col: V_range})

    # Add controls at median/mode
    control_cols = ['founding_cohort', 'region']
    fixed = _fix_controls_at_median_mode(df_plot, control_cols)
    for k, v in fixed.items():
        if v is not None:
            pred_df[k] = v

    try:
        predictions = hev.predict(pred_df)
        ax.plot(V_range, predictions, color=PALETTE['E'], linewidth=2.5, label='OLS fit')
    except Exception as e:
        print(f"  ⚠️ Could not plot F1 fit line: {e}")

    ax.set_xlabel('V (Vagueness, z-score)', fontsize=12, fontweight='bold', color=PALETTE['V'])
    ax.set_ylabel('E (Early Funding)', fontsize=12, fontweight='bold', color=PALETTE['E'])
    ax.set_title('F1. E vs V', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)

    # Caption
    ax.text(0.98, 0.02, 'Controls fixed at median/mode', transform=ax.transAxes,
            fontsize=8, ha='right', va='bottom', style='italic', color='gray')

    output_path = outdir / 'F1_E_vs_V.png'
    fig.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f"  ✓ Saved: {output_path}")
    return output_path


def fig_F2_PrL_vs_V(df: pd.DataFrame, hlvf: BinaryResultsWrapper, outdir: Path) -> Path:
    """
    F2: Predicted Pr(L=1) vs V, holding F at median.

    Args:
        df: DataFrame with L, z_V, F_flexibility
        hlvf: Logit model from run_HLVF
        outdir: Output directory

    Returns:
        Path to saved PNG
    """
    outdir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 6))

    V_col = 'z_V'
    df_plot = df.dropna(subset=['L', V_col, 'F_flexibility'])

    # V range
    V_range = np.linspace(df_plot[V_col].min(), df_plot[V_col].max(), 100)
    pred_df = pd.DataFrame({V_col: V_range})

    # Fix F at median
    F_median = _num_median(df_plot, 'F_flexibility')
    pred_df['F_flexibility'] = F_median

    # Fix founder_serial at median if present
    if 'founder_serial' in df_plot.columns:
        pred_df['founder_serial'] = _num_median(df_plot, 'founder_serial')

    # Fix controls at median/mode
    control_cols = ['founding_cohort', 'region']
    fixed = _fix_controls_at_median_mode(df_plot, control_cols)
    for k, v in fixed.items():
        if v is not None:
            pred_df[k] = v

    try:
        predictions = hlvf.predict(pred_df)
        ax.plot(V_range, predictions, color=PALETTE['L'], linewidth=2.5)
    except Exception as e:
        print(f"  ⚠️ Could not plot F2 predictions: {e}")

    ax.set_xlabel('V (Vagueness, z-score)', fontsize=12, fontweight='bold', color=PALETTE['V'])
    ax.set_ylabel('Pr(L = 1)', fontsize=12, fontweight='bold', color=PALETTE['L'])
    ax.set_title('F2. Pr(L) vs V', fontsize=14, fontweight='bold')
    ax.set_ylim([0, 1])
    ax.grid(True, alpha=0.3)

    # Caption
    ax.text(0.98, 0.02, 'F at median; other moderator + controls fixed at median/mode',
            transform=ax.transAxes, fontsize=8, ha='right', va='bottom', style='italic', color='gray')

    output_path = outdir / 'F2_PrL_vs_V.png'
    fig.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f"  ✓ Saved: {output_path}")
    return output_path


def fig_F3a_L_given_F(df: pd.DataFrame, hlvf: BinaryResultsWrapper, outdir: Path) -> Path:
    """
    F3a: L | F (V×F curves). Two lines: F=1 (skyblue, solid, upward), F=0 (skyblue, dashed, downward).

    Args:
        df: DataFrame with L, z_V, F_flexibility
        hlvf: Logit model from run_HLVF
        outdir: Output directory

    Returns:
        Path to saved PNG
    """
    outdir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 6))

    V_col = 'z_V'
    df_plot = df.dropna(subset=['L', V_col, 'F_flexibility'])

    # V range
    V_range = np.linspace(df_plot[V_col].min(), df_plot[V_col].max(), 100)

    # Fix founder_serial at median if present
    founder_median = _num_median(df_plot, 'founder_serial') if 'founder_serial' in df_plot.columns else None

    # Fix controls at median/mode
    control_cols = ['founding_cohort', 'region']
    fixed = _fix_controls_at_median_mode(df_plot, control_cols)

    # Plot for F=0 (Hardware, dashed, downward slope expected)
    pred_df_0 = pd.DataFrame({V_col: V_range, 'F_flexibility': 0})
    if founder_median is not None:
        pred_df_0['founder_serial'] = founder_median
    for k, v in fixed.items():
        if v is not None:
            pred_df_0[k] = v

    try:
        pred_0 = hlvf.predict(pred_df_0)
        ax.plot(V_range, pred_0, color=PALETTE['F'], linestyle='--', linewidth=2.5, label='F=0 (Hardware)')
    except Exception as e:
        print(f"  ⚠️ Could not plot F3a F=0 line: {e}")

    # Plot for F=1 (Software/Flexible, solid, upward slope expected)
    pred_df_1 = pd.DataFrame({V_col: V_range, 'F_flexibility': 1})
    if founder_median is not None:
        pred_df_1['founder_serial'] = founder_median
    for k, v in fixed.items():
        if v is not None:
            pred_df_1[k] = v

    try:
        pred_1 = hlvf.predict(pred_df_1)
        ax.plot(V_range, pred_1, color=PALETTE['F'], linestyle='-', linewidth=2.5, label='F=1 (Software/Flexible)')
    except Exception as e:
        print(f"  ⚠️ Could not plot F3a F=1 line: {e}")

    ax.set_xlabel('V (Vagueness, z-score)', fontsize=12, fontweight='bold', color=PALETTE['V'])
    ax.set_ylabel('Pr(L = 1)', fontsize=12, fontweight='bold', color=PALETTE['L'])
    ax.set_title('F3a. L | F (V×F)', fontsize=14, fontweight='bold')
    ax.set_ylim([0, 1])
    ax.legend(loc='best', fontsize=10)
    ax.grid(True, alpha=0.3)

    # Caption
    ax.text(0.98, 0.02, 'Other moderator + controls fixed at median/mode',
            transform=ax.transAxes, fontsize=8, ha='right', va='bottom', style='italic', color='gray')

    output_path = outdir / 'F3a_L_given_F.png'
    fig.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f"  ✓ Saved: {output_path}")
    return output_path


def fig_F3b_L_given_C(df: pd.DataFrame, h4: BinaryResultsWrapper, outdir: Path) -> Path:
    """
    F3b: L | C (V×C curves). Two lines: C=1 (orange, dash-dot), C=0 (orange, dotted).

    Args:
        df: DataFrame with growth (or L), z_V (or z_vagueness), founder_serial
        h4: Logit model from test_h4_growth_interaction
        outdir: Output directory

    Returns:
        Path to saved PNG
    """
    outdir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Determine V column
    V_col = 'z_V' if 'z_V' in df.columns else 'z_vagueness'

    # Determine DV column (growth for h4)
    DV_col = 'growth'

    df_plot = df.dropna(subset=[DV_col, V_col, 'founder_serial'])

    # V range
    V_range = np.linspace(df_plot[V_col].min(), df_plot[V_col].max(), 100)

    # Fix F at median if present
    F_median = _num_median(df_plot, 'F_flexibility') if 'F_flexibility' in df_plot.columns else None

    # Fix controls at median/mode
    control_cols = ['founding_cohort', 'z_employees_log']
    fixed = _fix_controls_at_median_mode(df_plot, control_cols)

    # Plot for C=0 (First-time, dotted)
    pred_df_0 = pd.DataFrame({V_col: V_range, 'founder_serial': 0})
    if F_median is not None:
        pred_df_0['F_flexibility'] = F_median
    for k, v in fixed.items():
        if v is not None:
            pred_df_0[k] = v

    try:
        pred_0 = h4.predict(pred_df_0)
        ax.plot(V_range, pred_0, color=PALETTE['C'], linestyle=':', linewidth=2.5, label='C=0 (First-time)')
    except Exception as e:
        print(f"  ⚠️ Could not plot F3b C=0 line: {e}")

    # Plot for C=1 (Serial, dash-dot)
    pred_df_1 = pd.DataFrame({V_col: V_range, 'founder_serial': 1})
    if F_median is not None:
        pred_df_1['F_flexibility'] = F_median
    for k, v in fixed.items():
        if v is not None:
            pred_df_1[k] = v

    try:
        pred_1 = h4.predict(pred_df_1)
        ax.plot(V_range, pred_1, color=PALETTE['C'], linestyle='-.', linewidth=2.5, label='C=1 (Serial)')
    except Exception as e:
        print(f"  ⚠️ Could not plot F3b C=1 line: {e}")

    ax.set_xlabel('V (Vagueness, z-score)', fontsize=12, fontweight='bold', color=PALETTE['V'])
    ax.set_ylabel('Pr(Growth = 1)', fontsize=12, fontweight='bold', color=PALETTE['L'])
    ax.set_title('F3b. L | C (V×C)', fontsize=14, fontweight='bold')
    ax.set_ylim([0, 1])
    ax.legend(loc='best', fontsize=10)
    ax.grid(True, alpha=0.3)

    # Caption
    ax.text(0.98, 0.02, 'F at median; controls fixed at median/mode',
            transform=ax.transAxes, fontsize=8, ha='right', va='bottom', style='italic', color='gray')

    output_path = outdir / 'F3b_L_given_C.png'
    fig.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f"  ✓ Saved: {output_path}")
    return output_path


def fig_F4_E(df: pd.DataFrame, outdir: Path) -> Path:
    """
    F4_E: Histogram of E (or E_scaled).

    Args:
        df: DataFrame with E or E_scaled
        outdir: Output directory

    Returns:
        Path to saved PNG
    """
    outdir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 5))

    E_col = 'E_scaled' if 'E_scaled' in df.columns else 'E'
    data = df[E_col].dropna()

    if len(data) == 0:
        ax.text(0.5, 0.5, 'No data available for E', ha='center', va='center',
                transform=ax.transAxes, fontsize=12)
    elif data.nunique() <= 2:
        # Binary E, use bar chart
        counts = data.value_counts().sort_index()
        ax.bar(range(len(counts)), counts.values, color=PALETTE['E'], edgecolor='black', alpha=0.7)
        ax.set_xticks(range(len(counts)))
        ax.set_xticklabels([f'{int(v)}' for v in counts.index])
        ax.set_ylabel('Count', fontweight='bold')
    else:
        # Continuous E, use histogram
        ax.hist(data, bins=30, color=PALETTE['E'], edgecolor='black', alpha=0.7)
        ax.set_xlabel('E (Early Funding)', fontweight='bold')
        ax.set_ylabel('Count', fontweight='bold')

    ax.set_title(f'F4. E Distribution (n={len(data):,})', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)

    output_path = outdir / 'F4_E.png'
    fig.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f"  ✓ Saved: {output_path}")
    return output_path


def fig_F4_L24(df: pd.DataFrame, outdir: Path) -> Path:
    """
    F4_L_2024: Bar chart of L_2024 (0/1 counts).

    Args:
        df: DataFrame with L_2024
        outdir: Output directory

    Returns:
        Path to saved PNG
    """
    outdir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 5))

    L_col = 'L_2024'
    if L_col not in df.columns:
        # Fallback to just 'L'
        L_col = 'L' if 'L' in df.columns else None

    if L_col is None or df[L_col].isna().all():
        ax.text(0.5, 0.5, 'No data available for L_2024', ha='center', va='center',
                transform=ax.transAxes, fontsize=12)
    else:
        data = df[L_col].dropna()
        counts = data.value_counts().sort_index()
        ax.bar(range(len(counts)), counts.values, color=PALETTE['L'], edgecolor='black', alpha=0.7)
        ax.set_xticks(range(len(counts)))
        ax.set_xticklabels([f'{int(v)}' for v in counts.index])
        ax.set_ylabel('Count', fontweight='bold')
        ax.set_title(f'F4. L_2024 Distribution (n={len(data):,})', fontsize=14, fontweight='bold')

    ax.grid(True, alpha=0.3, axis='y')

    output_path = outdir / 'F4_L_2024.png'
    fig.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f"  ✓ Saved: {output_path}")
    return output_path


def fig_F4_L25(df: pd.DataFrame, outdir: Path) -> Path:
    """
    F4_L_2025: Bar chart of L_2025 (0/1 counts).

    Args:
        df: DataFrame with L_2025
        outdir: Output directory

    Returns:
        Path to saved PNG
    """
    outdir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 5))

    L_col = 'L_2025'
    if L_col not in df.columns:
        # Fallback to just 'L'
        L_col = 'L' if 'L' in df.columns else None

    if L_col is None or df[L_col].isna().all():
        ax.text(0.5, 0.5, 'No data available for L_2025', ha='center', va='center',
                transform=ax.transAxes, fontsize=12)
    else:
        data = df[L_col].dropna()
        counts = data.value_counts().sort_index()
        ax.bar(range(len(counts)), counts.values, color=PALETTE['L'], edgecolor='black', alpha=0.7)
        ax.set_xticks(range(len(counts)))
        ax.set_xticklabels([f'{int(v)}' for v in counts.index])
        ax.set_ylabel('Count', fontweight='bold')
        ax.set_title(f'F4. L_2025 Distribution (n={len(data):,})', fontsize=14, fontweight='bold')

    ax.grid(True, alpha=0.3, axis='y')

    output_path = outdir / 'F4_L_2025.png'
    fig.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f"  ✓ Saved: {output_path}")
    return output_path


def fig_F4_V(df: pd.DataFrame, outdir: Path) -> Path:
    """
    F4_V: Histogram of z_V (or V).

    Args:
        df: DataFrame with z_V or V
        outdir: Output directory

    Returns:
        Path to saved PNG
    """
    outdir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 5))

    V_col = 'z_V' if 'z_V' in df.columns else 'V'
    data = df[V_col].dropna()

    if len(data) == 0:
        ax.text(0.5, 0.5, 'No data available for V', ha='center', va='center',
                transform=ax.transAxes, fontsize=12)
    else:
        ax.hist(data, bins=30, color=PALETTE['V'], edgecolor='black', alpha=0.7)
        ax.set_xlabel('V (Vagueness, z-score)', fontweight='bold')
        ax.set_ylabel('Count', fontweight='bold')
        ax.set_title(f'F4. V Distribution (n={len(data):,})', fontsize=14, fontweight='bold')

    ax.grid(True, alpha=0.3)

    output_path = outdir / 'F4_V.png'
    fig.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f"  ✓ Saved: {output_path}")
    return output_path


def fig_F5_StepUp_by_F(df: pd.DataFrame, outdir: Path) -> Path:
    """
    F5: Step-up by F (survivors only). Boxplot of S_stepup_log by F_flexibility.

    Args:
        df: DataFrame with S_stepup_log, F_flexibility, L (or L_2025)
        outdir: Output directory

    Returns:
        Path to saved PNG
    """
    outdir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 6))

    # Filter to survivors (L==1)
    L_col = 'L_2025' if 'L_2025' in df.columns else ('L' if 'L' in df.columns else None)

    if L_col is None:
        ax.text(0.5, 0.5, 'No L column available', ha='center', va='center',
                transform=ax.transAxes, fontsize=12)
    else:
        df_surv = df[df[L_col] == 1].copy()
        df_plot = df_surv.dropna(subset=['S_stepup_log', 'F_flexibility'])

        if len(df_plot) < 5:
            ax.text(0.5, 0.5, f'Insufficient survivor data (n={len(df_plot)})',
                    ha='center', va='center', transform=ax.transAxes, fontsize=12)
        else:
            # Group by F
            groups = []
            labels = []
            for f_val in sorted(df_plot['F_flexibility'].unique()):
                subset = df_plot[df_plot['F_flexibility'] == f_val]['S_stepup_log']
                groups.append(subset)
                label = 'Software (F=1)' if f_val == 1 else 'Hardware (F=0)'
                labels.append(f'{label}\n(n={len(subset)})')

            bp = ax.boxplot(groups, labels=labels, patch_artist=True, widths=0.6)
            for patch in bp['boxes']:
                patch.set_facecolor(PALETTE['S'])
                patch.set_alpha(0.7)

            ax.set_ylabel('S (Step-up, log)', fontweight='bold', color=PALETTE['S'])
            ax.set_title(f'F5. Step-up by F (Survivors only, n={len(df_plot):,})',
                         fontsize=14, fontweight='bold')

    ax.grid(True, alpha=0.3, axis='y')

    output_path = outdir / 'F5_StepUp_by_F.png'
    fig.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f"  ✓ Saved: {output_path}")
    return output_path


def fig_F6_SpecCurve(spec_df: pd.DataFrame, outdir: Path) -> Path:
    """
    F6: Specification curve. Plot coefficients across specifications.

    Args:
        spec_df: DataFrame with columns: coefficient (or coef_vagueness), pvalue, term
        outdir: Output directory

    Returns:
        Path to saved PNG
    """
    outdir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(14, 6))

    # Determine column names
    coef_col = 'coefficient' if 'coefficient' in spec_df.columns else 'coef_vagueness'
    pval_col = 'pvalue' if 'pvalue' in spec_df.columns else 'p_vagueness'

    if coef_col not in spec_df.columns:
        ax.text(0.5, 0.5, 'No coefficient column found in spec_df',
                ha='center', va='center', transform=ax.transAxes, fontsize=12)
    else:
        df_plot = spec_df.copy()

        # Sort by coefficient
        df_plot = df_plot.sort_values(coef_col).reset_index(drop=True)
        x = np.arange(len(df_plot))

        # Color by term if available
        if 'term' in df_plot.columns:
            colors = []
            for term in df_plot['term']:
                if 'V' in str(term) and 'F' in str(term):
                    colors.append(PALETTE['F'])  # V×F interaction
                elif 'V' in str(term) and 'C' in str(term):
                    colors.append(PALETTE['C'])  # V×C interaction
                elif 'V' in str(term):
                    colors.append(PALETTE['V'])  # V main effect
                else:
                    colors.append('gray')
        else:
            colors = [PALETTE['V']] * len(df_plot)

        # Plot coefficients
        ax.scatter(x, df_plot[coef_col], c=colors, s=40, alpha=0.7, edgecolors='black', linewidths=0.5)

        # Add horizontal line at 0
        ax.axhline(0, color='black', linestyle='--', linewidth=1, alpha=0.5)

        # Add confidence bands if std_error available
        if 'std_error' in df_plot.columns:
            ax.errorbar(x, df_plot[coef_col], yerr=1.96 * df_plot['std_error'],
                       fmt='none', alpha=0.2, color='gray')

        ax.set_xlabel('Specification Index', fontsize=12, fontweight='bold')
        ax.set_ylabel('Coefficient Estimate', fontsize=12, fontweight='bold')
        ax.set_title(f'F6. Specification Curve (n={len(df_plot)} specs)', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)

        # Legend if term column exists
        if 'term' in df_plot.columns:
            from matplotlib.patches import Patch
            legend_elements = [
                Patch(facecolor=PALETTE['V'], label='V (main)'),
                Patch(facecolor=PALETTE['F'], label='V×F'),
                Patch(facecolor=PALETTE['C'], label='V×C')
            ]
            ax.legend(handles=legend_elements, loc='best', fontsize=9)

    output_path = outdir / 'F6_SpecCurve.png'
    fig.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f"  ✓ Saved: {output_path}")
    return output_path


def create_F_series(df: pd.DataFrame, results: dict, outdir: Path) -> dict:
    """
    Create all F-series plots (F1-F6) in one call.

    Args:
        df: DataFrame with analysis data
        results: Dictionary with keys:
            - 'hev': OLS from models.run_HEV(...)
            - 'hlvf': Logit from models.run_HLVF(...)
            - 'h4': Logit from models.test_h4_growth_interaction(...)
            - 'hsf': (optional) OLS from models.run_HSF(...)
            - 'spec_df': DataFrame for spec curve
        outdir: Output directory for all plots

    Returns:
        Dictionary mapping figure names to Path objects:
        {'F1': Path, 'F2': Path, 'F3a': Path, 'F3b': Path,
         'F4_E': Path, 'F4_L24': Path, 'F4_L25': Path, 'F4_V': Path,
         'F5': Path, 'F6': Path}
    """
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    print("\n" + "="*80)
    print("CREATING F-SERIES PLOTS")
    print("="*80)

    paths = {}

    # F1: E vs V
    if 'hev' in results and results['hev'] is not None:
        print("\nF1: E vs V scatter with OLS fit...")
        paths['F1'] = fig_F1_E_vs_V(df, results['hev'], outdir)
    else:
        print("\n⚠️  Skipping F1: hev model not provided")

    # F2: Pr(L) vs V
    if 'hlvf' in results and results['hlvf'] is not None:
        print("\nF2: Pr(L) vs V...")
        paths['F2'] = fig_F2_PrL_vs_V(df, results['hlvf'], outdir)
    else:
        print("\n⚠️  Skipping F2: hlvf model not provided")

    # F3a: L|F
    if 'hlvf' in results and results['hlvf'] is not None:
        print("\nF3a: L | F (V×F curves)...")
        paths['F3a'] = fig_F3a_L_given_F(df, results['hlvf'], outdir)
    else:
        print("\n⚠️  Skipping F3a: hlvf model not provided")

    # F3b: L|C
    if 'h4' in results and results['h4'] is not None:
        print("\nF3b: L | C (V×C curves)...")
        paths['F3b'] = fig_F3b_L_given_C(df, results['h4'], outdir)
    else:
        print("\n⚠️  Skipping F3b: h4 model not provided")

    # F4: Distributions
    print("\nF4: Variable distributions...")
    paths['F4_E'] = fig_F4_E(df, outdir)
    paths['F4_L24'] = fig_F4_L24(df, outdir)
    paths['F4_L25'] = fig_F4_L25(df, outdir)
    paths['F4_V'] = fig_F4_V(df, outdir)

    # F5: Step-up by F
    print("\nF5: Step-up by F (survivors only)...")
    paths['F5'] = fig_F5_StepUp_by_F(df, outdir)

    # F6: Spec curve
    if 'spec_df' in results and results['spec_df'] is not None:
        print("\nF6: Specification curve...")
        paths['F6'] = fig_F6_SpecCurve(results['spec_df'], outdir)
    else:
        print("\n⚠️  Skipping F6: spec_df not provided")

    print("\n" + "="*80)
    print(f"✓ Created {len(paths)} F-series plots")
    print("="*80)

    return paths


# =============================================================================
# F-SERIES (HEV/HLVF/HSF) IMPORTS
# =============================================================================
# Import standardized F-series plotting functions with HEV/HLVF/HSF terminology
# Reference: W2 slides - ELSVF palette & interaction conventions

try:
    from modules.plots_F_series import (
        create_F_series,
        fig_F1_E_vs_V,
        fig_F2_PrL_vs_V,
        fig_F3a_L_given_F,
        fig_F3b_L_given_C,
        fig_F4_E_dist,
        fig_F4_L24_dist,
        fig_F4_L25_dist,
        fig_F4_V_dist,
        fig_F4_F_dist,
        fig_F5_stepup_by_F,
        fig_F6_spec_curve,
        PALETTE as F_SERIES_PALETTE
    )
    F_SERIES_AVAILABLE = True
except ImportError:
    F_SERIES_AVAILABLE = False
    print("⚠️  F-series module not available. Install or check imports.")


if __name__ == "__main__":
    print("Visualization Module - Standalone Test\n")
    print("=" * 80)
    print("This module is designed to be imported and used with real model results.")
    print("\nAvailable plotting suites:")
    print("  • H1/H2 plots (legacy): plot_h1_scatter, plot_h2_interaction, etc.")
    print("  • F-series (HEV/HLVF/HSF): create_F_series() from plots_F_series")
    print("\nRun the main pipeline script to generate visualizations.")
    print("=" * 80)
