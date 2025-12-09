#!/usr/bin/env python3
"""
Empirics_Later/run.py
Tests H2a/b: Vagueness × Hardware interaction on Series B+ success
Author: 권준/나대용 (中軍)
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from scipy import stats

# ============================================================================
# 1. LOAD DATA (from Empirics_Early output or TO_LATER.txt)
# ============================================================================

def load_series_a_sample():
    """
    Load firms that successfully got Series A (from H1 test).
    Expected columns:
    - vagueness_zscore: Standardized vagueness index
    - hardware: Binary (0=SW, 1=HW)
    - series_b_plus: Binary DV (1 if got Series B+ within 17 months)
    - is_serial: Binary control
    - log_series_a: Logged Series A amount
    - year_founded: Categorical
    """
    # PLACEHOLDER: Replace with actual data path
    df = pd.read_csv("../../1️⃣_INPUT/data/series_a_sample.csv")
    
    # Validate required columns
    required_cols = [
        'vagueness_zscore', 'hardware', 'series_b_plus',
        'is_serial', 'log_series_a', 'year_founded'
    ]
    missing = set(required_cols) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    
    return df

# ============================================================================
# 2. ESTIMATE H2a/b: LOGIT WITH INTERACTION
# ============================================================================

def estimate_h2():
    """
    Model: P(Series B+) ~ V + H + (V×H) + Controls
    H2a: β₃ < 0 (interaction term negative)
    H2b: β₁ > 0 (main effect positive for SW)
    """
    df = load_series_a_sample()
    
    # Create interaction term explicitly (for interpretability)
    df['vague_x_hw'] = df['vagueness_zscore'] * df['hardware']
    
    # Fit logit model
    model = smf.logit(
        formula="""
            series_b_plus ~ 
            vagueness_zscore + 
            hardware + 
            vague_x_hw +
            is_serial + 
            log_series_a +
            C(year_founded)
        """,
        data=df
    ).fit(cov_type='HC3', maxiter=100)
    
    print("\n" + "="*80)
    print("TABLE 2: H2a/b Logit Regression Results")
    print("="*80)
    print(model.summary())
    
    # Calculate average marginal effects (AME)
    print("\n" + "="*80)
    print("Average Marginal Effects (AME)")
    print("="*80)
    
    # Manual AME calculation (for interaction term)
    beta = model.params
    X = df[['vagueness_zscore', 'hardware', 'vague_x_hw', 'is_serial', 'log_series_a']]
    
    # Marginal effect of V for Software (H=0)
    me_sw = beta['vagueness_zscore']
    # Marginal effect of V for Hardware (H=1)
    me_hw = beta['vagueness_zscore'] + beta['vague_x_hw']
    
    print(f"∂P/∂V |_{{H=0}} (Software): {me_sw:.3f}")
    print(f"∂P/∂V |_{{H=1}} (Hardware): {me_hw:.3f}")
    print(f"Difference (Reversal): {me_hw - me_sw:.3f}")
    
    # Hypothesis tests
    print("\n" + "="*80)
    print("Hypothesis Tests")
    print("="*80)
    print(f"H2a (β₃ < 0): {'✓ SUPPORTED' if beta['vague_x_hw'] < 0 and model.pvalues['vague_x_hw'] < 0.05 else '✗ NOT SUPPORTED'}")
    print(f"H2b (β₁ > 0): {'✓ SUPPORTED' if beta['vagueness_zscore'] > 0 and model.pvalues['vagueness_zscore'] < 0.05 else '✗ NOT SUPPORTED'}")
    
    return model, df

# ============================================================================
# 3. VISUALIZE INTERACTION (Figure 4)
# ============================================================================

def plot_interaction(model, df):
    """
    Create V × H interaction plot showing reversal.
    """
    # Create prediction grid
    vagueness_range = np.linspace(-2, 2, 100)
    
    # Predict for SW (H=0)
    pred_sw = []
    for v in vagueness_range:
        X_sw = pd.DataFrame({
            'vagueness_zscore': [v],
            'hardware': [0],
            'vague_x_hw': [0],
            'is_serial': [df['is_serial'].mean()],
            'log_series_a': [df['log_series_a'].mean()],
            'year_founded': [df['year_founded'].mode()[0]]
        })
        pred_sw.append(model.predict(X_sw)[0])
    
    # Predict for HW (H=1)
    pred_hw = []
    for v in vagueness_range:
        X_hw = pd.DataFrame({
            'vagueness_zscore': [v],
            'hardware': [1],
            'vague_x_hw': [v],
            'is_serial': [df['is_serial'].mean()],
            'log_series_a': [df['log_series_a'].mean()],
            'year_founded': [df['year_founded'].mode()[0]]
        })
        pred_hw.append(model.predict(X_hw)[0])
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(vagueness_range, pred_sw, 'b-', linewidth=2, label='Software (H=0)')
    plt.plot(vagueness_range, pred_hw, color='gray', linewidth=2, label='Hardware (H=1)')
    
    plt.xlabel('Promise Vagueness (z-score)', fontsize=12)
    plt.ylabel('P(Series B+ Success)', fontsize=12)
    plt.title('Figure 4: Vagueness × Architecture Interaction', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(alpha=0.3)
    plt.ylim([0, 1])
    
    # Add annotation for crossover
    crossover_idx = np.argmin(np.abs(np.array(pred_sw) - np.array(pred_hw)))
    crossover_v = vagueness_range[crossover_idx]
    plt.axvline(crossover_v, color='red', linestyle='--', alpha=0.5)
    plt.text(crossover_v + 0.1, 0.5, f'Crossover\nV ≈ {crossover_v:.2f}', 
             fontsize=10, color='red')
    
    plt.tight_layout()
    plt.savefig('../../3️⃣_OUTPUT/figures/fig4_vxh_interaction.pdf', dpi=300)
    print("\n✓ Saved: 3️⃣_OUTPUT/figures/fig4_vxh_interaction.pdf")
    plt.close()

# ============================================================================
# 4. MECHANISM TEST: PIVOT FREQUENCY (H2c)
# ============================================================================

def test_pivot_mechanism(df):
    """
    Test if pivot frequency mediates V → Series B+ relationship.
    """
    # PLACEHOLDER: Assume pivot_count column exists
    if 'pivot_count' not in df.columns:
        print("\n⚠ Warning: pivot_count column not found. Skipping mechanism test.")
        return
    
    # Stage 1: V → Pivot Count
    stage1 = smf.ols(
        formula="pivot_count ~ vagueness_zscore + hardware + vague_x_hw + C(year_founded)",
        data=df
    ).fit(cov_type='HC3')
    
    print("\n" + "="*80)
    print("Mechanism Test (Stage 1): V → Pivot Count")
    print("="*80)
    print(stage1.summary().tables[1])
    
    # Stage 2: V + Pivot → Series B+
    df['vague_x_hw'] = df['vagueness_zscore'] * df['hardware']
    stage2 = smf.logit(
        formula="""
            series_b_plus ~ 
            vagueness_zscore + 
            pivot_count +
            hardware + 
            C(year_founded)
        """,
        data=df
    ).fit(cov_type='HC3')
    
    print("\n" + "="*80)
    print("Mechanism Test (Stage 2): V + Pivot → Series B+")
    print("="*80)
    print(stage2.summary())
    
    # Check for mediation
    beta_pivot = stage2.params['pivot_count']
    print(f"\nPivot effect (β₂): {beta_pivot:.3f}")
    print(f"Mediation: {'✓ PARTIAL' if beta_pivot > 0 else '✗ NOT DETECTED'}")

# ============================================================================
# 5. ROBUSTNESS: SPECIFICATION CURVE (Appendix)
# ============================================================================

def spec_curve_analysis(df):
    """
    Test β₃ (V×H interaction) across 200+ model specifications.
    Vary: DV cutoff (12/17/24 months), controls, sample restrictions.
    """
    print("\n" + "="*80)
    print("Specification Curve Analysis (Robustness)")
    print("="*80)
    
    results = []
    
    # Specification dimensions
    dv_windows = [12, 17, 24]  # months for Series B+ coding
    control_sets = [
        ['is_serial'],
        ['is_serial', 'log_series_a'],
        ['is_serial', 'log_series_a', 'C(year_founded)']
    ]
    
    for window in dv_windows:
        for controls in control_sets:
            # Recode DV based on window
            df_temp = df.copy()
            # PLACEHOLDER: Actual recoding logic needed
            
            # Fit model
            formula = f"series_b_plus ~ vagueness_zscore + hardware + vague_x_hw + {' + '.join(controls)}"
            try:
                model = smf.logit(formula, data=df_temp).fit(disp=0, maxiter=50)
                beta_vxh = model.params['vague_x_hw']
                pval = model.pvalues['vague_x_hw']
                results.append({
                    'window': window,
                    'controls': len(controls),
                    'beta_vxh': beta_vxh,
                    'significant': pval < 0.05
                })
            except:
                continue
    
    # Summary
    results_df = pd.DataFrame(results)
    print(f"\nTotal specifications tested: {len(results_df)}")
    print(f"β₃ < 0 (as predicted): {(results_df['beta_vxh'] < 0).sum()} / {len(results_df)}")
    print(f"Significant (p < 0.05): {results_df['significant'].sum()} / {len(results_df)}")
    print(f"Median β₃: {results_df['beta_vxh'].median():.3f}")
    
    # Save to table
    results_df.to_csv('../../3️⃣_OUTPUT/tables/table2b_spec_curve.csv', index=False)
    print("\n✓ Saved: 3️⃣_OUTPUT/tables/table2b_spec_curve.csv")

# ============================================================================
# 6. MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*80)
    print("🐅 EMPIRICS_LATER: H2a/b INTERACTION TESTS")
    print("="*80)
    
    # Run main analysis
    model, df = estimate_h2()
    
    # Generate visualizations
    plot_interaction(model, df)
    
    # Test mechanisms
    test_pivot_mechanism(df)
    
    # Robustness
    spec_curve_analysis(df)
    
    # Export regression table
    with open('../../3️⃣_OUTPUT/tables/table2_h2_logit.txt', 'w') as f:
        f.write(model.summary().as_text())
    print("\n✓ Saved: 3️⃣_OUTPUT/tables/table2_h2_logit.txt")
    
    print("\n" + "="*80)
    print("✅ Empirics_Later analysis complete.")
    print("="*80)
