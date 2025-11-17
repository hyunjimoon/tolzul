#!/usr/bin/env python3
"""
Pipeline Step 4: Run Models
============================
Executes H1 (Early Funding ~ Vagueness) and H2 (Growth ~ Vagueness × Hardware)
for all three dataset variants.

Usage:
    python pipeline/04_run_models.py [dataset]

    dataset: all, quantum, transportation (default: all)
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import pandas as pd
import numpy as np
import yaml
import logging
from models import test_h1_early_funding, test_h2_main_growth
from features import preprocess_for_h2
from cache_manager import CacheManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def run_models_for_dataset(dataset_key: str, config: dict):
    """Run H1 and H2 models for a specific dataset."""
    dataset_config = config['datasets'][dataset_key]
    logger.info(f"\n{'='*80}")
    logger.info(f"Running Models: {dataset_config['name']}")
    logger.info(f"{'='*80}")

    # Load filtered dataset
    output_dir = Path(dataset_config['output_dir'])
    dataset_file = output_dir / "dataset.parquet"

    logger.info(f"\n📂 Loading {dataset_file}")
    df = pd.read_parquet(dataset_file)
    logger.info(f"   Companies: {len(df):,}")

    # Check for minimum sample size
    if len(df) == 0:
        logger.warning(f"⚠️  Empty dataset - skipping models")
        return

    # Create models output directory
    models_dir = output_dir / "models"
    models_dir.mkdir(exist_ok=True, parents=True)

    # Create founding_cohort (needed for both H1 and H2)
    if 'year_founded' in df.columns:
        bins = [0, 2009, 2014, 2018, 2020, 2021, 9999]
        labels = ['≤2009', '2010-14', '2015-18', '2019-20', '2021', '2022+']
        year_founded = pd.to_numeric(df['year_founded'], errors='coerce')
        df['founding_cohort'] = pd.cut(year_founded, bins=bins, labels=labels, right=True)
        df['founding_cohort'] = df['founding_cohort'].cat.remove_unused_categories()
        logger.info(f"   Created founding_cohort: {df['founding_cohort'].notna().sum():,} companies")
    else:
        df['founding_cohort'] = pd.Categorical(['Unknown'] * len(df))
        logger.warning(f"   ⚠️  year_founded not found, created dummy founding_cohort")

    # Ensure sector_fe exists (should be created by engineer_features, but add fallback)
    if 'sector_fe' not in df.columns:
        df['sector_fe'] = pd.Categorical(['Other'] * len(df))
        logger.warning(f"   ⚠️  sector_fe not found, created dummy sector_fe")

    # Create z-scored variables for H1 (H2 preprocessing will create them again, but that's OK)
    for col in ['vagueness', 'employees_log']:
        if col in df.columns:
            col_std = df[col].std()
            if col_std > 0 and not pd.isna(col_std):
                df[f'z_{col}'] = (df[col] - df[col].mean()) / col_std
            else:
                df[f'z_{col}'] = 0
                logger.warning(f"   ⚠️  {col} has zero variance, z-scored to 0")

    # ========== H1: Early Funding ~ Vagueness ==========
    logger.info(f"\n{'='*60}")
    logger.info("H1: Early Funding ~ Vagueness (OLS)")
    logger.info(f"{'='*60}")

    try:
        # Explicit formula with controls (employees + cohort)
        h1_formula = "early_funding_musd ~ z_vagueness + z_employees_log + C(founding_cohort)"
        logger.info(f"   Formula: {h1_formula}")

        # Show sample diagnostics before running
        df_h1_check = df.dropna(subset=['early_funding_musd', 'z_vagueness'])
        logger.info(f"   Sample with early funding: {len(df_h1_check):,}")

        # Detailed diagnostics on early_funding_musd
        ef_values = df_h1_check['early_funding_musd']
        logger.info(f"   Early funding diagnostics:")
        logger.info(f"     Mean:   ${ef_values.mean():.2f}M")
        logger.info(f"     Median: ${ef_values.median():.2f}M")
        logger.info(f"     Min:    ${ef_values.min():.2f}M")
        logger.info(f"     Max:    ${ef_values.max():.2f}M")
        logger.info(f"     # zeros: {(ef_values == 0).sum():,}")
        logger.info(f"     # > $0:  {(ef_values > 0).sum():,}")

        # Check if the values are actually very small (not in millions)
        if ef_values.mean() < 0.01 and ef_values.max() > 0:
            logger.warning(f"   ⚠️ WARNING: early_funding_musd values are very small!")
            logger.warning(f"   ⚠️ May need to check if first_financing_size is already in millions")
            logger.warning(f"   ⚠️ Or if it needs different conversion")

        logger.info(f"   Controls available:")
        logger.info(f"     - z_employees_log: {df_h1_check['z_employees_log'].notna().sum():,} companies")
        logger.info(f"     - founding_cohort: {df_h1_check['founding_cohort'].notna().sum():,} companies")

        h1_model = test_h1_early_funding(df, formula=h1_formula)

        # Extract coefficients into DataFrame
        h1_coef_df = pd.DataFrame({
            'coef': h1_model.params,
            'std_err': h1_model.bse,
            't': h1_model.tvalues,
            'P>|t|': h1_model.pvalues,
            'conf_low': h1_model.conf_int()[0],
            'conf_high': h1_model.conf_int()[1]
        })

        # Save coefficients
        h1_coef_file = models_dir / "h1_coefficients.csv"
        h1_coef_df.to_csv(h1_coef_file)
        logger.info(f"\n✅ H1 model complete")
        logger.info(f"   Coefficients saved to {h1_coef_file}")
        logger.info(f"   N={h1_model.nobs:.0f}, R²={h1_model.rsquared:.4f}")

        # Print key coefficients
        logger.info(f"\n   Key Coefficients:")
        if 'z_vagueness' in h1_coef_df.index:
            v_coef = h1_coef_df.loc['z_vagueness', 'coef']
            v_pval = h1_coef_df.loc['z_vagueness', 'P>|t|']
            v_sig = '***' if v_pval < 0.001 else '**' if v_pval < 0.01 else '*' if v_pval < 0.05 else ''
            logger.info(f"     Vagueness:  β={v_coef:>8.4f}, p={v_pval:.4f} {v_sig}")

        if 'z_employees_log' in h1_coef_df.index:
            e_coef = h1_coef_df.loc['z_employees_log', 'coef']
            e_pval = h1_coef_df.loc['z_employees_log', 'P>|t|']
            e_sig = '***' if e_pval < 0.001 else '**' if e_pval < 0.01 else '*' if e_pval < 0.05 else ''
            logger.info(f"     Employees:  β={e_coef:>8.4f}, p={e_pval:.4f} {e_sig}")

        # Count cohort fixed effects
        cohort_vars = [c for c in h1_coef_df.index if 'founding_cohort' in c]
        if cohort_vars:
            logger.info(f"     Cohort FE:  {len(cohort_vars)} cohorts included")

    except Exception as e:
        logger.error(f"❌ H1 model failed: {e}")
        import traceback
        traceback.print_exc()

    # ========== H2: Growth ~ Vagueness × Hardware ==========
    logger.info(f"\n{'='*60}")
    logger.info("H2: Growth ~ Vagueness × Hardware (Logit)")
    logger.info(f"{'='*60}")

    try:
        # Preprocess for H2
        df_h2 = preprocess_for_h2(df)
        logger.info(f"   Preprocessed {len(df_h2):,} companies for H2")

        # Run H2 model
        h2_model = test_h2_main_growth(df_h2)

        # Extract coefficients into DataFrame
        h2_coef_df = pd.DataFrame({
            'coef': h2_model.params,
            'std_err': h2_model.bse,
            'z': h2_model.tvalues,
            'P>|z|': h2_model.pvalues,
            'conf_low': h2_model.conf_int()[0],
            'conf_high': h2_model.conf_int()[1]
        })

        # Save coefficients
        h2_coef_file = models_dir / "h2_main_coefficients.csv"
        h2_coef_df.to_csv(h2_coef_file)
        logger.info(f"\n✅ H2 model complete")
        logger.info(f"   Coefficients saved to {h2_coef_file}")

        # Get pseudo R-squared (if available)
        pseudo_r2 = getattr(h2_model, 'prsquared', np.nan)
        logger.info(f"   N={h2_model.nobs:.0f}, Pseudo-R²={pseudo_r2:.4f}")

        # Print key coefficients
        if 'z_vagueness' in h2_coef_df.index:
            v_coef = h2_coef_df.loc['z_vagueness', 'coef']
            v_pval = h2_coef_df.loc['z_vagueness', 'P>|z|']
            logger.info(f"   Vagueness (main): β={v_coef:.4e}, p={v_pval:.4f}")

        # Check for interaction (may have different names)
        interaction_keys = [k for k in h2_coef_df.index if 'z_vagueness' in k and 'hardware' in k.lower()]
        if interaction_keys:
            int_key = interaction_keys[0]
            int_coef = h2_coef_df.loc[int_key, 'coef']
            int_pval = h2_coef_df.loc[int_key, 'P>|z|']
            logger.info(f"   Interaction (V×HW): β={int_coef:.4e}, p={int_pval:.4f}")

        # Save fitted data for plotting
        h2_data_file = models_dir / "h2_analysis_dataset.csv"
        df_h2.to_csv(h2_data_file, index=False)
        logger.info(f"   Analysis dataset saved to {h2_data_file}")

    except Exception as e:
        logger.error(f"❌ H2 model failed: {e}")
        import traceback
        traceback.print_exc()

    logger.info(f"\n{'='*80}")
    logger.info(f"Models Complete for {dataset_config['name']} ✓")
    logger.info(f"{'='*80}")


def main():
    """Run models for specified dataset or all datasets."""
    # Parse arguments
    dataset_filter = sys.argv[1] if len(sys.argv) > 1 else 'all'

    logger.info("=" * 80)
    logger.info("STEP 4: RUN MODELS")
    logger.info("=" * 80)

    # Load configuration
    config_file = Path("config/datasets.yaml")
    with open(config_file) as f:
        config = yaml.safe_load(f)

    # Determine which datasets to process
    if dataset_filter in config['datasets']:
        datasets_to_process = [dataset_filter]
    elif dataset_filter == 'all':
        datasets_to_process = list(config['datasets'].keys())
    else:
        logger.error(f"Unknown dataset: {dataset_filter}")
        logger.error(f"Available datasets: {list(config['datasets'].keys())}")
        return 1

    logger.info(f"\nProcessing datasets: {datasets_to_process}")

    # Run models for each dataset
    for dataset_key in datasets_to_process:
        run_models_for_dataset(dataset_key, config)

    logger.info("\n" + "=" * 80)
    logger.info("STEP 4 COMPLETE ✓")
    logger.info(f"Models run for {len(datasets_to_process)} dataset(s)")
    logger.info("=" * 80)

    return 0


if __name__ == '__main__':
    sys.exit(main())
