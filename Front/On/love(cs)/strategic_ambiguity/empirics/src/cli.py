#!/usr/bin/env python3
"""
Strategic Vagueness Analysis Pipeline CLI
==========================================
Unified command-line interface for running the full analysis pipeline.

Usage:
    python -m src.cli load-data
    python -m src.cli engineer-features
    python -m src.cli filter-datasets
    python -m src.cli run-models [--dataset all|quantum|transportation]
    python -m src.cli generate-plots [--dataset all|quantum|transportation]
    python -m src.cli run-all

Available Commands:
    load-data          Load .dat files and create parquet cache
    engineer-features  Apply vagueness scorer and create features
    filter-datasets    Create dataset variants (all, quantum, transportation)
    run-models         Run H1/H2 statistical models
    generate-plots     Generate F-series plots (F3a interaction plot)
    run-all            Execute complete pipeline (steps 1-5)
"""

import argparse
import sys
from pathlib import Path
import pandas as pd
import numpy as np
import yaml
import logging
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

# Import local modules (using relative imports for package execution)
from .features import (
    consolidate_company_snapshots,
    engineer_features,
    filter_quantum_companies,
    filter_transportation_companies,
    preprocess_for_h2
)
from .models import test_h1_early_funding, test_h2_main_growth
from .vagueness_v2 import StrategicVaguenessScorerV2

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# W2 color palette
PALETTE = {
    "E": "red",
    "L": "#0000FF",
    "V": "green",
    "F": "skyblue",
    "HW": "gray"
}


# ============================================================================
# STEP 1: LOAD DATA
# ============================================================================

def cmd_load_data(args):
    """Load raw .dat files and create parquet cache."""
    logger.info("=" * 80)
    logger.info("STEP 1: LOAD DATA")
    logger.info("=" * 80)

    # Paths
    data_dir = Path("data/raw")
    cache_dir = Path("data/processed")
    cache_dir.mkdir(exist_ok=True, parents=True)

    cache_file = cache_dir / "consolidated_companies.parquet"

    # Load data (uses parquet cache if available)
    logger.info(f"\n📂 Loading company data from {data_dir}")
    df = consolidate_company_snapshots(str(data_dir))

    logger.info(f"\n✅ Data loaded successfully")
    logger.info(f"   Total companies: {len(df):,}")
    logger.info(f"   Columns: {len(df.columns)}")
    logger.info(f"   Memory: {df.memory_usage(deep=True).sum() / 1e6:.1f} MB")

    # Save cache if not exists
    if not cache_file.exists():
        logger.info(f"\n💾 Saving parquet cache to {cache_file}")
        df.to_parquet(cache_file, index=False)
        logger.info(f"   Cache saved ({cache_file.stat().st_size / 1e6:.1f} MB)")
    else:
        logger.info(f"\n✓ Parquet cache already exists at {cache_file}")

    # Summary statistics
    logger.info("\n📊 Data Summary:")
    if 'Description' in df.columns:
        logger.info(f"   Companies with descriptions: {df['Description'].notna().sum():,}")
    if 'FirstFinancingSize' in df.columns:
        logger.info(f"   Companies with financing data: {df['FirstFinancingSize'].notna().sum():,}")
    if 'YearFounded' in df.columns:
        years = df['YearFounded'].dropna()
        logger.info(f"   Founding years range: {int(years.min())} - {int(years.max())}")

    logger.info("\n" + "=" * 80)
    logger.info("STEP 1 COMPLETE ✓")
    logger.info("=" * 80)

    return 0


# ============================================================================
# STEP 2: ENGINEER FEATURES
# ============================================================================

def cmd_engineer_features(args):
    """Engineer features using V2 vagueness scorer."""
    logger.info("=" * 80)
    logger.info("STEP 2: ENGINEER FEATURES")
    logger.info("=" * 80)

    # Paths
    data_dir = Path("data/raw")
    cache_dir = Path("data/processed")
    cache_dir.mkdir(exist_ok=True, parents=True)

    output_file = cache_dir / "features_all.parquet"

    # Check if features already exist (SPEED BOOST!)
    if output_file.exists():
        logger.info(f"\n⚡ Features cache found at {output_file}")
        logger.info(f"   Loading pre-computed features (10x faster!)...")
        try:
            df_features = pd.read_parquet(output_file)
            logger.info(f"   ✓ Loaded {len(df_features):,} companies with {len(df_features.columns)} features")
            logger.info(f"\n💡 TIP: To force re-computation, delete {output_file}")

            # Skip to validation and return
            if 'vagueness' in df_features.columns:
                v_stats = df_features['vagueness'].describe()
                logger.info(f"\n🎯 Vagueness Score Distribution (V2):")
                logger.info(f"   Mean: {v_stats['mean']:.4f}, Std: {v_stats['std']:.4f}")

            logger.info("\n" + "=" * 80)
            logger.info("STEP 2 COMPLETE ✓ (using cache)")
            logger.info("=" * 80)
            return 0
        except Exception as e:
            logger.warning(f"   ⚠️  Cache load failed: {e}")
            logger.info(f"   Falling back to re-computation...")

    # Load data
    logger.info(f"\n📂 Loading company data from cache/raw")
    df = consolidate_company_snapshots(str(data_dir))

    logger.info(f"\n🔧 Engineering features with V2 scorer")
    logger.info(f"   Input rows: {len(df):,}")

    # Apply feature engineering (uses StrategicVaguenessScorerV2)
    df_features = engineer_features(df)

    logger.info(f"\n✅ Feature engineering complete")
    logger.info(f"   Output rows: {len(df_features):,}")
    logger.info(f"   New columns: {len(df_features.columns)}")

    # Check key features
    key_features = ['vagueness', 'is_hardware', 'early_funding', 'employees_log', 'firm_age']
    available_features = [f for f in key_features if f in df_features.columns]
    logger.info(f"\n📊 Key Features Created:")
    for feat in available_features:
        if df_features[feat].dtype in ['float64', 'float32', 'int64', 'int32']:
            mean_val = df_features[feat].mean()
            std_val = df_features[feat].std()
            logger.info(f"   {feat}: mean={mean_val:.4f}, std={std_val:.4f}")
        else:
            counts = df_features[feat].value_counts()
            logger.info(f"   {feat}: {dict(counts)}")

    # Vagueness scorer details
    if 'vagueness' in df_features.columns:
        v_stats = df_features['vagueness'].describe()
        logger.info(f"\n🎯 Vagueness Score Distribution (V2):")
        logger.info(f"   Mean: {v_stats['mean']:.4f}")
        logger.info(f"   Std:  {v_stats['std']:.4f}")
        logger.info(f"   Min:  {v_stats['min']:.4f}")
        logger.info(f"   25%:  {v_stats['25%']:.4f}")
        logger.info(f"   50%:  {v_stats['50%']:.4f}")
        logger.info(f"   75%:  {v_stats['75%']:.4f}")
        logger.info(f"   Max:  {v_stats['max']:.4f}")

    # Save engineered dataset
    output_file = cache_dir / "features_all.parquet"
    logger.info(f"\n💾 Saving engineered features to {output_file}")

    try:
        df_features.to_parquet(output_file, index=False, engine='pyarrow')
        # Validate the file was written correctly by checking size
        file_size = output_file.stat().st_size
        if file_size == 0:
            logger.error(f"❌ Parquet file is empty (0 bytes)! Write may have failed.")
            return 1
        logger.info(f"   Saved {len(df_features):,} rows ({file_size / 1e6:.1f} MB)")

        # Quick validation: try reading metadata to ensure file is valid
        import pyarrow.parquet as pq
        pq.read_metadata(output_file)
        logger.info(f"   ✓ Parquet file validated successfully")

    except Exception as e:
        logger.error(f"❌ Failed to save/validate parquet file: {e}")
        # Clean up potentially corrupted file
        if output_file.exists():
            output_file.unlink()
            logger.info(f"   Removed corrupted file: {output_file}")
        return 1

    logger.info("\n" + "=" * 80)
    logger.info("STEP 2 COMPLETE ✓")
    logger.info("=" * 80)

    return 0


# ============================================================================
# STEP 3: FILTER DATASETS
# ============================================================================

def cmd_filter_datasets(args):
    """Filter datasets into three variants."""
    logger.info("=" * 80)
    logger.info("STEP 3: FILTER DATASETS")
    logger.info("=" * 80)

    # Load configuration
    config_file = Path("config/datasets.yaml")
    with open(config_file) as f:
        config = yaml.safe_load(f)

    # Paths
    cache_dir = Path("data/processed")
    features_file = cache_dir / "features_all.parquet"

    # Load engineered features
    logger.info(f"\n📂 Loading engineered features from {features_file}")

    # Check if file exists and is valid
    if not features_file.exists():
        logger.error(f"❌ Features file not found: {features_file}")
        logger.error(f"   Run 'python -m src.cli engineer-features' first")
        return 1

    # Try to load with error handling for corrupted files
    try:
        df_all = pd.read_parquet(features_file)
    except Exception as e:
        logger.error(f"❌ Failed to load parquet file: {e}")
        logger.error(f"   File may be corrupted. Deleting and re-running Step 2 may help.")
        logger.error(f"   Run: rm {features_file} && python -m src.cli engineer-features")
        return 1

    logger.info(f"   Total companies: {len(df_all):,}")
    logger.info(f"   Columns: {len(df_all.columns)}")

    # Check for text columns used in filtering
    text_cols = ['Description', 'Keywords', 'Promise', 'description', 'keywords', 'promise']
    available_text_cols = [c for c in text_cols if c in df_all.columns]
    logger.info(f"   Text columns available for filtering: {available_text_cols}")
    if not available_text_cols:
        logger.warning(f"   ⚠️  No standard text columns found! Filters may not work.")
        logger.info(f"   Available columns (first 20): {df_all.columns.tolist()[:20]}")

    # Process each dataset variant
    filter_functions = {
        'quantum': filter_quantum_companies,
        'transportation': filter_transportation_companies
    }

    for dataset_key, dataset_config in config['datasets'].items():
        logger.info(f"\n{'='*60}")
        logger.info(f"Processing: {dataset_config['name']}")
        logger.info(f"{'='*60}")

        # Check if filtered dataset already exists (SPEED BOOST!)
        output_dir = Path(dataset_config['output_dir'])
        output_dir.mkdir(exist_ok=True, parents=True)
        output_file = output_dir / "dataset.parquet"

        if output_file.exists():
            logger.info(f"   ⚡ Filtered dataset cache found at {output_file}")
            try:
                df_filtered = pd.read_parquet(output_file)
                logger.info(f"   ✓ Loaded {len(df_filtered):,} companies (skip filtering)")
                logger.info(f"   Percentage of total: {len(df_filtered)/len(df_all)*100:.2f}%")

                # Show summary
                if 'vagueness' in df_filtered.columns:
                    v_mean = df_filtered['vagueness'].mean()
                    logger.info(f"   Vagueness: mean={v_mean:.4f}")

                logger.info(f"   💡 TIP: To force re-filtering, delete {output_file}")
                continue  # Skip to next dataset
            except Exception as e:
                logger.warning(f"   ⚠️  Cache load failed: {e}, re-filtering...")

        # Apply filter if specified
        filter_func_name = dataset_config.get('filter_function')
        if filter_func_name and filter_func_name in ['filter_quantum_companies', 'filter_transportation_companies']:
            logger.info(f"   Applying filter: {filter_func_name}")
            filter_func = filter_functions[dataset_key]
            df_filtered = filter_func(df_all)
        else:
            logger.info(f"   No filter (using all companies)")
            df_filtered = df_all.copy()

        # Save filtered dataset
        logger.info(f"\n💾 Saving to {output_file}")
        df_filtered.to_parquet(output_file, index=False)
        logger.info(f"   Saved {len(df_filtered):,} companies ({output_file.stat().st_size / 1e6:.1f} MB)")
        logger.info(f"   Percentage of total: {len(df_filtered)/len(df_all)*100:.2f}%")

        # Summary statistics
        if 'vagueness' in df_filtered.columns:
            v_mean = df_filtered['vagueness'].mean()
            v_std = df_filtered['vagueness'].std()
            logger.info(f"\n📊 Summary Statistics:")
            logger.info(f"   Vagueness: mean={v_mean:.4f}, std={v_std:.4f}")

        if 'is_hardware' in df_filtered.columns:
            hw_counts = df_filtered['is_hardware'].value_counts()
            # is_hardware is stored as int (1/0), not bool (True/False)
            hw_count = hw_counts.get(1, 0) + hw_counts.get(True, 0)  # Check both
            sw_count = hw_counts.get(0, 0) + hw_counts.get(False, 0)  # Check both
            logger.info(f"   Hardware companies: {hw_count:,}")
            logger.info(f"   Software companies: {sw_count:,}")

    logger.info("\n" + "=" * 80)
    logger.info("STEP 3 COMPLETE ✓")
    logger.info(f"Created {len(config['datasets'])} dataset variants")
    logger.info("=" * 80)

    return 0


# ============================================================================
# STEP 4: RUN MODELS
# ============================================================================

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

    # Ensure is_hardware exists (should be created by engineer_features, but add fallback)
    if 'is_hardware' not in df.columns:
        df['is_hardware'] = 0  # Default to software
        logger.warning(f"   ⚠️  is_hardware not found, created is_hardware=0 (all software)")

    # Create founder_serial (needed for both H1 and H2)
    if 'founder_serial' not in df.columns:
        if 'founder_credibility' in df.columns:
            df['founder_serial'] = (df['founder_credibility'] > 0).astype(int)
            serial_count = df['founder_serial'].sum()
            logger.info(f"   Created founder_serial from founder_credibility: {serial_count:,} serial founders")
        else:
            df['founder_serial'] = 0
            logger.warning(f"   ⚠️  founder_credibility not found, created founder_serial=0 for all")

    # Create z-scored variables for H1 (H2 preprocessing will create them again, but that's OK)
    for col in ['vagueness', 'employees_log', 'firm_age']:
        if col in df.columns:
            col_std = df[col].std()
            if col_std > 0 and not pd.isna(col_std):
                df[f'z_{col}'] = (df[col] - df[col].mean()) / col_std
            else:
                df[f'z_{col}'] = 0
                logger.warning(f"   ⚠️  {col} has zero variance, z-scored to 0")
        else:
            # Create dummy z-scored variable if base column doesn't exist
            if col == 'firm_age':
                df[f'z_{col}'] = 0
                logger.warning(f"   ⚠️  {col} not found, created z_{col}=0 for all")

    # ========== H1: Early Funding ~ Vagueness ==========
    logger.info(f"\n{'='*60}")
    logger.info("H1: Early Funding ~ Vagueness (OLS)")
    logger.info(f"{'='*60}")

    try:
        h1_model = test_h1_early_funding(df)

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

        # Print key coefficient
        if 'z_vagueness' in h1_coef_df.index:
            v_coef = h1_coef_df.loc['z_vagueness', 'coef']
            v_pval = h1_coef_df.loc['z_vagueness', 'P>|t|']
            logger.info(f"   Vagueness: β={v_coef:.4e}, p={v_pval:.4f}")

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


def cmd_run_models(args):
    """Run models for specified dataset or all datasets."""
    dataset_filter = args.dataset

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


# ============================================================================
# STEP 5: GENERATE PLOTS
# ============================================================================

def generate_f3a_plot(df: pd.DataFrame, output_dir: Path, dataset_name: str):
    """Generate F3a interaction plot (Vagueness × Hardware).

    Args:
        df: DataFrame with H2 analysis data
        output_dir: Directory to save plots
        dataset_name: Name of dataset for title
    """
    logger.info(f"\n📊 Generating F3a plot (Vagueness × Hardware)")

    # Prepare data
    df_plot = df.dropna(subset=['z_vagueness', 'is_hardware', 'growth']).copy()
    logger.info(f"   Plotting N={len(df_plot):,} companies")

    # Fit logit model (matching H2 specification)
    formula = "growth ~ z_vagueness * is_hardware + founder_serial + z_employees_log + C(founding_cohort)"

    # Check for constant variables and adjust formula
    include_founder_serial = True
    if 'founder_serial' in df_plot.columns:
        founder_serial_std = df_plot['founder_serial'].std()
        if pd.isna(founder_serial_std) or founder_serial_std == 0:
            # Remove founder_serial from formula if it's constant
            formula = formula.replace('+ founder_serial ', '')
            formula = formula.replace(' + founder_serial', '')
            include_founder_serial = False
            logger.info(f"   ⚠️  founder_serial is constant (std=0), removed from formula")

    logger.info(f"   Formula: {formula}")

    try:
        # Try standard MLE
        model = smf.logit(formula, data=df_plot).fit(disp=0, maxiter=100)
        logger.info(f"   ✓ Model converged (standard MLE)")
    except Exception as e:
        logger.warning(f"   Standard MLE failed, trying L1 regularization...")
        try:
            model = smf.logit(formula, data=df_plot).fit_regularized(
                method='l1', alpha=0.1, disp=0, maxiter=100
            )
            logger.info(f"   ✓ Model converged (L1 regularization α=0.1)")
        except Exception as e2:
            logger.error(f"   ❌ Model failed to converge: {e2}")
            return

    # Create prediction grid
    v_range = np.linspace(df_plot['z_vagueness'].min(), df_plot['z_vagueness'].max(), 100)

    # Reference values for controls (fix at median/mode)
    emp_mean = df_plot['z_employees_log'].mean()
    founder_serial_mode = df_plot['founder_serial'].mode()[0] if 'founder_serial' in df_plot.columns else 0

    # Get cohort mode and preserve categorical dtype
    if 'founding_cohort' in df_plot.columns:
        cohort_mode = df_plot['founding_cohort'].mode()[0]
        cohort_categories = df_plot['founding_cohort'].cat.categories if hasattr(df_plot['founding_cohort'], 'cat') else None
    else:
        cohort_mode = '2015-18'
        cohort_categories = None

    # Build prediction data - must match formula exactly
    # All values must be arrays of the same length for statsmodels formula API
    n_points = len(v_range)

    # Predictions for SW (is_hardware=False)
    pred_dict_sw = {
        'z_vagueness': v_range,
        'is_hardware': np.repeat(False, n_points),
        'z_employees_log': np.repeat(emp_mean, n_points),
        'founding_cohort': np.repeat(cohort_mode, n_points)
    }
    if include_founder_serial:
        pred_dict_sw['founder_serial'] = np.repeat(founder_serial_mode, n_points)

    pred_data_sw = pd.DataFrame(pred_dict_sw)

    # Ensure categorical dtype for founding_cohort
    if cohort_categories is not None:
        pred_data_sw['founding_cohort'] = pd.Categorical(
            pred_data_sw['founding_cohort'],
            categories=cohort_categories
        )

    prob_sw = model.predict(pred_data_sw)

    # Predictions for HW (is_hardware=True)
    pred_dict_hw = {
        'z_vagueness': v_range,
        'is_hardware': np.repeat(True, n_points),
        'z_employees_log': np.repeat(emp_mean, n_points),
        'founding_cohort': np.repeat(cohort_mode, n_points)
    }
    if include_founder_serial:
        pred_dict_hw['founder_serial'] = np.repeat(founder_serial_mode, n_points)

    pred_data_hw = pd.DataFrame(pred_dict_hw)

    # Ensure categorical dtype for founding_cohort
    if cohort_categories is not None:
        pred_data_hw['founding_cohort'] = pd.Categorical(
            pred_data_hw['founding_cohort'],
            categories=cohort_categories
        )

    prob_hw = model.predict(pred_data_hw)

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 7))

    # Plot lines
    ax.plot(v_range, prob_sw, color=PALETTE['F'], linestyle='-', linewidth=2.5,
            label='Software (F=1)', zorder=3)
    ax.plot(v_range, prob_hw, color=PALETTE['HW'], linestyle='--', linewidth=2.5,
            label='Hardware (F=0)', zorder=3)

    # Styling
    ax.set_xlabel('Strategic Vagueness (z-scored)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Pr(Growth to Series B+)', fontsize=14, fontweight='bold')
    ax.set_title(f'F3a: Integration Cost Moderation Effect\n{dataset_name}',
                 fontsize=16, fontweight='bold', pad=20)
    ax.legend(loc='best', fontsize=12, frameon=True, shadow=True)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add coefficient annotations
    try:
        v_coef = model.params.get('z_vagueness', np.nan)
        int_coef = model.params.get('z_vagueness:is_hardware[T.True]', np.nan)
        v_pval = model.pvalues.get('z_vagueness', np.nan)
        int_pval = model.pvalues.get('z_vagueness:is_hardware[T.True]', np.nan)

        annotation = (
            f"Main Effect (V): β={v_coef:.4f}, p={v_pval:.3f}\n"
            f"Interaction (V×HW): β={int_coef:.4f}, p={int_pval:.3f}"
        )
        ax.text(0.05, 0.95, annotation, transform=ax.transAxes,
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    except Exception as e:
        logger.warning(f"   Could not add coefficient annotation: {e}")

    plt.tight_layout()

    # Save plots
    figures_dir = output_dir / "figures"
    figures_dir.mkdir(exist_ok=True, parents=True)

    png_file = figures_dir / "F3a_interaction.png"
    pdf_file = figures_dir / "F3a_interaction.pdf"

    fig.savefig(png_file, dpi=300, bbox_inches='tight')
    fig.savefig(pdf_file, bbox_inches='tight')
    plt.close(fig)

    logger.info(f"   ✅ F3a plot saved:")
    logger.info(f"      PNG: {png_file}")
    logger.info(f"      PDF: {pdf_file}")


def generate_plots_for_dataset(dataset_key: str, config: dict):
    """Generate plots for a specific dataset."""
    dataset_config = config['datasets'][dataset_key]
    logger.info(f"\n{'='*80}")
    logger.info(f"Generating Plots: {dataset_config['name']}")
    logger.info(f"{'='*80}")

    # Load H2 analysis dataset
    output_dir = Path(dataset_config['output_dir'])
    models_dir = output_dir / "models"
    h2_data_file = models_dir / "h2_analysis_dataset.csv"

    if not h2_data_file.exists():
        logger.error(f"❌ H2 dataset not found: {h2_data_file}")
        logger.error(f"   Run 'python -m src.cli run-models' first")
        return

    logger.info(f"\n📂 Loading {h2_data_file}")
    df = pd.read_csv(h2_data_file)
    logger.info(f"   Companies: {len(df):,}")

    # Generate F3a plot
    try:
        generate_f3a_plot(df, output_dir, dataset_config['name'])
    except Exception as e:
        logger.error(f"❌ F3a plot failed: {e}")
        import traceback
        traceback.print_exc()

    logger.info(f"\n{'='*80}")
    logger.info(f"Plots Complete for {dataset_config['name']} ✓")
    logger.info(f"{'='*80}")


def cmd_generate_plots(args):
    """Generate plots for specified dataset or all datasets."""
    dataset_filter = args.dataset

    logger.info("=" * 80)
    logger.info("STEP 5: GENERATE PLOTS")
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

    # Generate plots for each dataset
    for dataset_key in datasets_to_process:
        generate_plots_for_dataset(dataset_key, config)

    logger.info("\n" + "=" * 80)
    logger.info("STEP 5 COMPLETE ✓")
    logger.info(f"Plots generated for {len(datasets_to_process)} dataset(s)")
    logger.info("=" * 80)

    return 0


# ============================================================================
# RUN ALL STEPS
# ============================================================================

def cmd_run_all(args):
    """Execute complete pipeline (steps 1-5)."""
    logger.info("=" * 80)
    logger.info("RUNNING COMPLETE PIPELINE (Steps 1-5)")
    logger.info("=" * 80)

    steps = [
        ('Step 1: Load Data', cmd_load_data),
        ('Step 2: Engineer Features', cmd_engineer_features),
        ('Step 3: Filter Datasets', cmd_filter_datasets),
        ('Step 4: Run Models', lambda a: cmd_run_models(type('obj', (object,), {'dataset': 'all'}))),
        ('Step 5: Generate Plots', lambda a: cmd_generate_plots(type('obj', (object,), {'dataset': 'all'}))),
    ]

    for step_name, step_func in steps:
        logger.info(f"\n{'='*80}")
        logger.info(f"🚀 Starting: {step_name}")
        logger.info(f"{'='*80}\n")

        result = step_func(args)
        if result != 0:
            logger.error(f"\n❌ Pipeline failed at {step_name}")
            return result

    logger.info("\n" + "=" * 80)
    logger.info("🎉 COMPLETE PIPELINE FINISHED SUCCESSFULLY")
    logger.info("=" * 80)
    logger.info("\n📊 Results available in:")
    logger.info("   - outputs/all/")
    logger.info("   - outputs/quantum/")
    logger.info("   - outputs/transportation/")

    return 0


# ============================================================================
# CLI MAIN
# ============================================================================

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Strategic Vagueness Analysis Pipeline',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m src.cli load-data
  python -m src.cli run-models --dataset quantum
  python -m src.cli run-all
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # load-data
    subparsers.add_parser('load-data', help='Load .dat files and create parquet cache')

    # engineer-features
    subparsers.add_parser('engineer-features', help='Apply vagueness scorer and create features')

    # filter-datasets
    subparsers.add_parser('filter-datasets', help='Create dataset variants')

    # run-models
    parser_models = subparsers.add_parser('run-models', help='Run H1/H2 statistical models')
    parser_models.add_argument('--dataset', default='all',
                               choices=['all', 'quantum', 'transportation'],
                               help='Which dataset to process (default: all)')

    # generate-plots
    parser_plots = subparsers.add_parser('generate-plots', help='Generate F-series plots')
    parser_plots.add_argument('--dataset', default='all',
                              choices=['all', 'quantum', 'transportation'],
                              help='Which dataset to process (default: all)')

    # run-all
    subparsers.add_parser('run-all', help='Execute complete pipeline (steps 1-5)')

    args = parser.parse_args()

    # Map commands to functions
    commands = {
        'load-data': cmd_load_data,
        'engineer-features': cmd_engineer_features,
        'filter-datasets': cmd_filter_datasets,
        'run-models': cmd_run_models,
        'generate-plots': cmd_generate_plots,
        'run-all': cmd_run_all,
    }

    if args.command is None:
        parser.print_help()
        return 1

    if args.command not in commands:
        logger.error(f"Unknown command: {args.command}")
        parser.print_help()
        return 1

    # Execute command
    return commands[args.command](args)


if __name__ == '__main__':
    sys.exit(main())
