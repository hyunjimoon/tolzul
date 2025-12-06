"""
U 논문 U-Shape 분석 스크립트
TOC v5.0: G ~ V (H₀) → G ~ V + V² (H₁)
"""
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from scipy import stats
from pathlib import Path

def main():
    print("="*60)
    print("U: Promise Precision and Venture Growth")
    print("U-Shape Hypothesis Test (TOC v5.0)")
    print("="*60)

    # 데이터 로드
    df = pd.read_csv('outputs/all/models/h2_analysis_dataset.csv')
    print(f"\nTotal N: {len(df):,}")

    # V² 생성
    df['z_vagueness_sq'] = df['z_vagueness'] ** 2

    # 분석용 데이터
    df_clean = df.dropna(subset=['growth', 'z_vagueness']).copy()
    print(f"Analysis N: {len(df_clean):,}")
    print(f"Growth rate: {df_clean['growth'].mean():.1%}")

    # ========================================
    # H₀: Linear (Scott's Null)
    # ========================================
    print("\n" + "="*60)
    print("H₀ TEST: G ~ β₁V + Controls (Scott's Null)")
    print("="*60)

    m1 = smf.logit(
        "growth ~ z_vagueness + z_employees_log + C(founding_cohort)",
        data=df_clean
    ).fit(disp=0)

    print(f"N = {m1.nobs:.0f}, Pseudo-R² = {m1.prsquared:.4f}")
    print(f"\nβ₁ (z_vagueness): {m1.params['z_vagueness']:.4f}")
    print(f"   SE: {m1.bse['z_vagueness']:.4f}")
    print(f"   p-value: {m1.pvalues['z_vagueness']:.4f}")

    h0_rejected = m1.pvalues['z_vagueness'] > 0.05
    print(f"\n→ H₀ {'REJECTED' if h0_rejected else 'NOT rejected'}: β₁ {'≈ 0' if h0_rejected else '≠ 0'}")

    # ========================================
    # H₁: Quadratic (U-shape)
    # ========================================
    print("\n" + "="*60)
    print("H₁ TEST: G ~ β₁V + β₂V² + Controls (U-shape)")
    print("="*60)

    m2 = smf.logit(
        "growth ~ z_vagueness + z_vagueness_sq + z_employees_log + C(founding_cohort)",
        data=df_clean
    ).fit(disp=0)

    print(f"N = {m2.nobs:.0f}, Pseudo-R² = {m2.prsquared:.4f}")
    print(f"\nβ₁ (z_vagueness): {m2.params['z_vagueness']:.4f}")
    print(f"   p-value: {m2.pvalues['z_vagueness']:.4f}")
    print(f"\nβ₂ (z_vagueness²): {m2.params['z_vagueness_sq']:.4f}")
    print(f"   SE: {m2.bse['z_vagueness_sq']:.4f}")
    print(f"   p-value: {m2.pvalues['z_vagueness_sq']:.4f}")

    beta2 = m2.params['z_vagueness_sq']
    pval2 = m2.pvalues['z_vagueness_sq']

    if beta2 > 0 and pval2 < 0.05:
        print("\n✅ H₁ SUPPORTED: β₂ > 0 (U-shape confirmed)")
    elif beta2 > 0:
        print(f"\n⚠️ β₂ > 0 but p = {pval2:.4f} > 0.05")
    else:
        print(f"\n❌ β₂ = {beta2:.4f} < 0 → Inverted U-shape (∩)")

    # ========================================
    # LR Test
    # ========================================
    print("\n" + "="*60)
    print("MODEL COMPARISON: Likelihood Ratio Test")
    print("="*60)

    lr_stat = 2 * (m2.llf - m1.llf)
    lr_pval = 1 - stats.chi2.cdf(lr_stat, df=1)
    print(f"LR χ²: {lr_stat:.4f}")
    print(f"p-value: {lr_pval:.4f}")
    print(f"→ Quadratic term {'IMPROVES' if lr_pval < 0.05 else 'does NOT improve'} fit")

    # ========================================
    # 결과 저장
    # ========================================
    results = pd.DataFrame({
        'model': ['H₀ (Linear)', 'H₁ (Quadratic)'],
        'beta_V': [m1.params['z_vagueness'], m2.params['z_vagueness']],
        'beta_V_pval': [m1.pvalues['z_vagueness'], m2.pvalues['z_vagueness']],
        'beta_V2': [np.nan, m2.params['z_vagueness_sq']],
        'beta_V2_pval': [np.nan, m2.pvalues['z_vagueness_sq']],
        'pseudo_r2': [m1.prsquared, m2.prsquared],
        'n_obs': [m1.nobs, m2.nobs],
        'llf': [m1.llf, m2.llf]
    })

    out_path = Path('outputs/all/models/ushape_test_results.csv')
    results.to_csv(out_path, index=False)
    print(f"\n💾 Results saved: {out_path}")

    # 요약
    print("\n" + "="*60)
    print("SUMMARY FOR TOC v5.0 (¶25-26)")
    print("="*60)
    print(results.to_string(index=False))

if __name__ == "__main__":
    main()
