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
# STORYBOARD PLOTS (🎞️ narrative)
# =============================================================================
from dataclasses import dataclass
from itertools import product

class StoryboardPlots:
    """
    Narrative plots for telling the causal story behind H1/H2.

    Panels mirror the research storyboard:
      1) Univariate distributions (vagueness, IC, growth DV)
      2) Bivariate with growth (V~G by IC; heatmap with Ns)
      3) Interaction decomposition (lines for modular vs integrated)
    """

    def __init__(self, dv_col: str = 'survival', dv_label: str = 'Growth (Series B+ within window)'):
        self.dv_col = dv_col
        self.dv_label = dv_label

    def _dv(self, df: pd.DataFrame) -> str:
        # Backward-compat: prefer explicit dv_col; fall back to 'growth' or 'survival'
        if self.dv_col in df.columns:
            return self.dv_col
        if 'growth' in df.columns:
            return 'growth'
        if 'survival' in df.columns:
            return 'survival'
        raise ValueError("No DV column found. Expected 'growth' or 'survival'.")

    def plot_univariate(self, df: pd.DataFrame, output_path: Optional[Path] = None) -> plt.Figure:
        """
        3-panel univariate overview:
          - Vagueness histogram
          - Integration cost distribution (binary)
          - DV base rate bar chart (growth=1 vs 0)
        """
        dv = self._dv(df)
        fig, axes = plt.subplots(1, 3, figsize=(16, 5))

        # 1) Vagueness
        v = df['vagueness'].astype(float)
        v = v[np.isfinite(v)]
        axes[0].hist(v, bins=30, edgecolor='black', alpha=0.7)
        axes[0].set_title("Vagueness Distribution")
        axes[0].set_xlabel("Vagueness (0–100)")
        axes[0].set_ylabel("Count")

        # 2) Integration cost
        if 'high_integration_cost' in df.columns:
            ic_counts = df['high_integration_cost'].value_counts(dropna=False).sort_index()
            axes[1].bar(['Modular(0)', 'Integrated(1)'], ic_counts.reindex([0,1]).fillna(0).values,
                        edgecolor='black', alpha=0.8)
            axes[1].set_title("Integration Cost (binary)")
            axes[1].set_ylabel("Count")
        else:
            axes[1].text(0.5, 0.5, "high_integration_cost not found", ha='center', va='center')
            axes[1].set_axis_off()

        # 3) DV base rate
        if dv in df.columns:
            dv_rate = df[dv].mean()
            axes[2].bar([self.dv_label], [dv_rate], edgecolor='black', alpha=0.8)
            axes[2].set_ylim(0, 1)
            axes[2].set_title(f"{self.dv_label} — base rate")
            axes[2].text(0, dv_rate + 0.03, f"{dv_rate:.1%}", ha='center')
        else:
            axes[2].text(0.5, 0.5, f"{dv} not found", ha='center', va='center')
            axes[2].set_axis_off()

        fig.suptitle("Storyboard — Univariate Distributions", fontsize=14, fontweight='bold')
        plt.tight_layout()
        if output_path:
            fig.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"  ✓ Saved: {output_path}")
        return fig

    def plot_bivariate_growth(self, df: pd.DataFrame, output_path: Optional[Path] = None) -> plt.Figure:
        """
        3-panel bivariate views with the growth DV:
          (a) V→G by IC (two lines from binned rates)
          (b) V×IC heatmap (cell = mean growth rate, annotate n)
          (c) Bubble: Employees vs growth by founding cohort (if columns exist)
        """
        dv = self._dv(df)
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))

        df_clean = df.dropna(subset=['vagueness', dv]).copy()
        if 'high_integration_cost' not in df_clean.columns:
            df_clean['high_integration_cost'] = 0

        # Binning
        df_clean['v_bin'] = pd.cut(df_clean['vagueness'].astype(float),
                                   bins=[0,20,40,60,80,100], include_lowest=True)

        # (a) line chart by IC
        rate = (df_clean.groupby(['high_integration_cost','v_bin'], observed=True)[dv]
                      .agg(['mean','size']).reset_index())
        for ic, dsub, color, label in [(0, rate[rate['high_integration_cost']==0], 'C0', 'Modular'),
                                       (1, rate[rate['high_integration_cost']==1], 'C1', 'Integrated')]:
            if len(dsub):
                x = np.arange(len(dsub))
                axes[0].plot(x, dsub['mean'].values, marker='o', linewidth=2, label=label)
        axes[0].set_title("Vagueness → Growth by IC")
        axes[0].set_xticks(range(len(rate['v_bin'].unique())))
        axes[0].set_xticklabels([str(c) for c in sorted(rate['v_bin'].unique())], rotation=45)
        axes[0].set_ylim(0,1); axes[0].legend(); axes[0].grid(True, alpha=0.3)

        # (b) heatmap of growth rate with Ns
        pivot = rate.pivot(index='high_integration_cost', columns='v_bin', values='mean')
        sns.heatmap(pivot, annot=True, fmt=".2f", cmap="RdYlGn", vmin=0, vmax=1, ax=axes[1],
                    cbar_kws={'label': f'P({self.dv_label})'})
        axes[1].set_title("V×IC Heatmap (cell = growth rate)")
        axes[1].set_yticklabels(['Modular(0)','Integrated(1)'], rotation=0)

        # (c) bubble: employees vs growth by cohort
        if all(c in df_clean.columns for c in ['employees_log', 'founding_cohort']):
            # average growth by (employees_log bin, cohort)
            df_clean['empl_bin'] = pd.qcut(df_clean['employees_log'], q=5, duplicates='drop')
            bubble = (df_clean.groupby(['founding_cohort','empl_bin'], observed=True)[dv]
                              .agg(['mean','size']).reset_index())
            sizes = 50 * (bubble['size'] / (bubble['size'].max() if bubble['size'].max()>0 else 1) + 0.1)
            axes[2].scatter(bubble['mean'], bubble['size'], s=sizes, alpha=0.6, edgecolor='k')
            axes[2].set_xlabel("Mean growth by (cohort, employees bin)")
            axes[2].set_ylabel("N (bubble size ∝ N)")
            axes[2].set_title("Employees × Growth by Cohort")
            axes[2].grid(True, alpha=0.3)
        else:
            axes[2].text(0.5, 0.5, "Need employees_log & founding_cohort", ha='center', va='center')
            axes[2].set_axis_off()

        fig.suptitle("Storyboard — Bivariate with Growth", fontsize=14, fontweight='bold')
        plt.tight_layout()
        if output_path:
            fig.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"  ✓ Saved: {output_path}")
        return fig

    def plot_interaction_decomposition(
        self,
        df: pd.DataFrame,
        model: Optional[BinaryResultsWrapper] = None,
        output_path: Optional[Path] = None
    ) -> plt.Figure:
        """
        Core H2 visual: predicted P(growth) vs vagueness lines by IC.
        If a fitted logit `model` is provided, use it for smooth curves.
        Otherwise, draw binned empirical rates.
        """
        dv = self._dv(df)
        fig, ax = plt.subplots(figsize=(8, 5))

        if model is not None:
            # Smooth curves using model coefficients
            v = np.linspace(0, 100, 101)
            base = pd.DataFrame({'vagueness': v})
            for ic, ls, lbl in [(0, '-', 'Modular'), (1, '--', 'Integrated')]:
                X = base.copy()
                X['high_integration_cost'] = ic
                # Fill controls with means if present
                for c in ['z_employees_log','employees_log','founding_cohort']:
                    if c in df.columns and c.startswith('z_'):
                        X[c] = 0.0
                    elif c in df.columns:
                        X[c] = df[c].mode().iloc[0] if df[c].dtype=='O' else df[c].mean()
                p = model.predict(X)
                ax.plot(v, p, ls=ls, lw=2.5, label=lbl)
        else:
            # Empirical: binned rates by IC
            d = df.dropna(subset=['vagueness', dv]).copy()
            d['v_bin'] = pd.cut(d['vagueness'], bins=[0,20,40,60,80,100], include_lowest=True)
            for ic, marker, lbl in [(0, 'o', 'Modular'), (1, 's', 'Integrated')]:
                s = (d[d['high_integration_cost']==ic]
                     .groupby('v_bin', observed=True)[dv].mean())
                ax.plot(range(len(s)), s.values, marker=marker, lw=2, label=lbl)
            ax.set_xticks(range(len(s.index))); ax.set_xticklabels([str(c) for c in s.index], rotation=45)

        ax.set_ylim(0,1); ax.grid(True, alpha=0.3)
        ax.set_xlabel("Vagueness (bins or 0–100)")
        ax.set_ylabel(f"Predicted P({self.dv_label})")
        ax.set_title("H2 Interaction: Vagueness × Integration Cost")
        ax.legend(loc='best')

        plt.tight_layout()
        if output_path:
            fig.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"  ✓ Saved: {output_path}")
        return fig


# =============================================================================
# MULTIVERSE HEATMAP (🌌 robustness across specs)
# =============================================================================

def plot_multiverse_heatmap(results_df: pd.DataFrame, output_path: Optional[Path] = None) -> plt.Figure:
    """
    Draw a heatmap summarizing H2 conclusions across model specs.

    Expected columns in results_df:
      - spec_id, dv, ic_spec, sector_fe, estimator, n, converged (bool)
      - beta_vag, p_vag  (β₁ and its p-value)
      - beta_int, p_int  (β₃ and its p-value)

    Color encodes signed evidence: sign(β) × −log10(p), clipped [0, 6]
    Column1 = β₁ (Vag→Growth in modular), Column2 = β₃ (Interaction)
    """
    if results_df is None or results_df.empty:
        raise ValueError("No multiverse results to plot.")

    dfp = results_df.copy()
    def ev(beta, p):
        if pd.isna(beta) or pd.isna(p) or p<=0:
            return 0.0
        return np.sign(beta) * np.clip(-np.log10(p), 0, 6)

    dfp['E_vag'] = [ev(b, p) for b, p in zip(dfp['beta_vag'], dfp['p_vag'])]
    dfp['E_int'] = [ev(b, p) for b, p in zip(dfp['beta_int'], dfp['p_int'])]

    # Row label = compact spec signature
    dfp['spec'] = (dfp['dv'].astype(str) + " | IC:" + dfp['ic_spec'].astype(str) +
                   " | FE:" + dfp['sector_fe'].map({True:'Y', False:'N'}).astype(str) +
                   " | est:" + dfp['estimator'].astype(str))

    mat = dfp[['E_vag','E_int']].to_numpy()
    row_labels = dfp['spec'].tolist()
    col_labels = ['β₁ (Vag→Growth, modular)', 'β₃ (Interaction)']

    fig, ax = plt.subplots(figsize=(10, max(6, 0.35*len(row_labels))))
    sns.heatmap(mat, annot=True, fmt=".2f", cmap="coolwarm", center=0,
                yticklabels=row_labels, xticklabels=col_labels, ax=ax,
                cbar_kws={'label':'sign×−log10(p)'}
                )
    ax.set_title("Multiverse Heatmap — H2 Consistency across Specifications")
    ax.set_ylabel("Model specifications")
    ax.set_xlabel("Parameters of interest")

    # Convergence border (draw a marker for non-converged)
    for i, conv in enumerate(dfp['converged'].tolist()):
        if not conv:
            ax.text(2.02, i+0.5, "×", va='center', ha='left', color='k', fontsize=12)

    plt.tight_layout()
    if output_path:
        fig.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {output_path}")
    return fig


# =============================================================================
# STORYBOARD + MV CONVENIENCE WRAPPER
# =============================================================================

def create_storyboard_and_multiverse_plots(
    df: pd.DataFrame,
    results_df: Optional[pd.DataFrame],
    output_dir: Path,
    dv_col: str = 'survival'
) -> Dict[str, Path]:
    """
    Convenience wrapper to create:
      - story_univariate.png
      - story_bivariate_growth.png
      - story_interaction.png
      - multiverse_heatmap.png  (if results_df provided)
    """
    out = {}
    output_dir = Path(output_dir); output_dir.mkdir(parents=True, exist_ok=True)

    sb = StoryboardPlots(dv_col=dv_col, dv_label='Growth (Series B+ within window)')

    fig = sb.plot_univariate(df, output_dir / "story_univariate.png")
    plt.close(fig); out['story_univariate'] = output_dir / "story_univariate.png"

    fig = sb.plot_bivariate_growth(df, output_dir / "story_bivariate_growth.png")
    plt.close(fig); out['story_bivariate_growth'] = output_dir / "story_bivariate_growth.png"

    # Optionally pass an H2 model to draw smooth curves; here we just use data
    fig = sb.plot_interaction_decomposition(df, model=None, output_path=output_dir / "story_interaction.png")
    plt.close(fig); out['story_interaction'] = output_dir / "story_interaction.png"

    if results_df is not None and len(results_df):
        fig = plot_multiverse_heatmap(results_df, output_dir / "multiverse_heatmap.png")
        plt.close(fig); out['multiverse_heatmap'] = output_dir / "multiverse_heatmap.png"

    return out


if __name__ == "__main__":
    print("Visualization Module - Standalone Test\n")
    print("=" * 80)
    print("This module is designed to be imported and used with real model results.")
    print("Run the main pipeline script to generate visualizations.")
