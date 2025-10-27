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


if __name__ == "__main__":
    print("Visualization Module - Standalone Test\n")
    print("=" * 80)
    print("This module is designed to be imported and used with real model results.")
    print("Run the main pipeline script to generate visualizations.")
