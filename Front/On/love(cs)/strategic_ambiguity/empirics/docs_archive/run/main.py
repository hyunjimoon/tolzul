#!/usr/bin/env python3
"""
Main Pipeline Orchestrator for Multiverse Analysis

This script executes the complete 5-stage pipeline:
1. 🏗️BUILD: Load and consolidate .dat files
2. 🧠DEFINE: Engineer 5 core variables
3. 📊PLOT1: Visualize variable distributions
4. ⚖️TEST: Test 3 core hypotheses
5. 📈PLOT2: Run and visualize multiverse analysis

Usage:
    python main.py --data-dir data/raw/ --output-dir results/
    python main.py --skip-dat  # Use processed CSV instead
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional, List

import pandas as pd
import numpy as np

# Import modules
from modules import features, models, plots

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('pipeline.log')
    ]
)
logger = logging.getLogger(__name__)


def stage_1_build(
    data_dir: str,
    use_processed: bool = False,
    use_cache: bool = True,
    years: Optional[List[int]] = None,
    quantum_only: bool = False
) -> pd.DataFrame:
    """
    1🏗️BUILD: Load and consolidate data.

    Args:
        data_dir: Directory containing .dat files
        use_processed: If True, use processed CSV instead of .dat files
        use_cache: If True, use cached .parquet file (much faster!)
        years: Optional list of years to load (e.g., [2022, 2024, 2025]).
               For time windows 2022-2024 and 2022-2025, use [2022, 2024, 2025].
        quantum_only: If True, load only quantum companies (creates separate cache)

    Returns:
        Consolidated DataFrame
    """
    logger.info("\n" + "="*80)
    logger.info("1🏗️ STAGE 1: BUILD - Loading and consolidating data")
    logger.info("="*80)

    if use_processed:
        logger.info("Using processed CSV data...")
        processed_path = Path(data_dir).parent / 'processed' / 'analysis_panel.csv'

        if not processed_path.exists():
            raise FileNotFoundError(f"Processed data not found: {processed_path}")

        df = pd.read_csv(processed_path)
        logger.info(f"  → Loaded {len(df):,} rows from {processed_path}")

    else:
        # Choose loading function based on quantum_only flag
        if quantum_only:
            logger.info("Loading QUANTUM companies only...")
            if years:
                logger.info(f"  Years: {years} (selective loading)")

            df = features.consolidate_quantum_snapshots(
                data_dir,
                use_cache=use_cache,
                save_parquet=True,  # Always save for future fast loading
                years=years
            )
        else:
            if years:
                logger.info(f"Loading .dat files for years: {years} (selective loading)...")
            else:
                logger.info("Loading .dat files (with parquet caching)...")

            df = features.consolidate_company_snapshots(
                data_dir,
                use_cache=use_cache,
                save_parquet=True,  # Always save for future fast loading
                years=years
            )

        if df is None:
            logger.warning("No .dat files found, falling back to processed CSV...")
            return stage_1_build(data_dir, use_processed=True)

    logger.info(f"\n  ✅ Build complete: {len(df):,} companies loaded")
    logger.info(f"     Columns: {len(df.columns)}")
    logger.info(f"     Memory: {df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")

    return df


def stage_2_define(df: pd.DataFrame) -> pd.DataFrame:
    """
    2🧠DEFINE: Engineer 5 core variables.

    Variables:
        🧧E (early_funding_musd): First financing size in $M
        💰L (growth): Binary indicator for Series B+ achievement
        🤙V (z_vagueness): Standardized vagueness score
        💪F (is_hardware): Binary indicator for hardware sector (inverted flexibility)
        💸S (valuation_stepup): Optional - valuation step-up ratio

    Args:
        df: Raw DataFrame

    Returns:
        DataFrame with engineered features
    """
    logger.info("\n" + "="*80)
    logger.info("2🧠 STAGE 2: DEFINE - Engineering core variables")
    logger.info("="*80)

    # Apply feature engineering
    logger.info("  Applying feature engineering...")
    df = features.engineer_features(df)

    # Apply preprocessing for H2 (z-scores, cohorts)
    logger.info("  Preprocessing for hypothesis testing...")
    df = features.preprocess_for_h2(df, fix_founder_credibility=True)

    # Report variable statistics
    logger.info("\n  Core Variables Summary:")

    if 'early_funding_musd' in df.columns:
        early = df['early_funding_musd'].dropna()
        logger.info(f"    🧧E early_funding_musd: n={len(early):,}, mean=${early.mean():.2f}M, median=${early.median():.2f}M")

    if 'growth' in df.columns:
        growth_rate = df['growth'].mean() * 100
        logger.info(f"    💰L growth: n={df['growth'].notna().sum():,}, rate={growth_rate:.1f}%")

    if 'z_vagueness' in df.columns:
        vague = df['z_vagueness'].dropna()
        logger.info(f"    🤙V z_vagueness: n={len(vague):,}, mean={vague.mean():.2f}, std={vague.std():.2f}")

    if 'is_hardware' in df.columns:
        hw_pct = df['is_hardware'].mean() * 100
        logger.info(f"    💪F is_hardware: n={df['is_hardware'].notna().sum():,}, hardware={hw_pct:.1f}%")

    logger.info(f"\n  ✅ Feature engineering complete: {len(df.columns)} columns")

    # Save analysis panel for multiverse analysis
    analysis_panel_path = Path('data/processed/analysis_panel.csv')
    analysis_panel_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(analysis_panel_path, index=False)
    logger.info(f"\n  💾 Saved analysis panel: {analysis_panel_path} ({len(df):,} rows)")

    return df


def stage_3_plot1(df: pd.DataFrame, output_dir: Path) -> None:
    """
    3📊PLOT1: Visualize variable distributions.

    Args:
        df: DataFrame with engineered features
        output_dir: Output directory for plots
    """
    logger.info("\n" + "="*80)
    logger.info("3📊 STAGE 3: PLOT1 - Visualizing variable distributions")
    logger.info("="*80)

    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / 'variable_distributions.png'

    logger.info("  Creating distribution plots...")
    fig = plots.plot_variable_distributions(df, output_path=output_path)

    logger.info(f"\n  ✅ Distributions plotted: {output_path}")


def stage_4_test(df: pd.DataFrame, output_dir: Path) -> dict:
    """
    4⚖️TEST: Test 3 core hypotheses.

    Hypotheses:
        H🧧E🤙V: early_funding ~ vagueness (expect β < 0)
        H💰L🤙V: growth ~ vagueness (expect β > 0)
        H💰L🤙V💪F: growth ~ vagueness × is_hardware (interaction)

    Args:
        df: DataFrame with features
        output_dir: Output directory for results

    Returns:
        Dictionary of model results
    """
    logger.info("\n" + "="*80)
    logger.info("4⚖️ STAGE 4: TEST - Testing core hypotheses")
    logger.info("="*80)

    results = {}

    # H1: Early funding ~ vagueness
    logger.info("\n  Testing H🧧E🤙V: Early Funding ~ Vagueness")
    try:
        h1 = models.test_h1_early_funding(df)
        results['h1'] = h1

        beta = h1.params.get('z_vagueness', np.nan)
        pval = h1.pvalues.get('z_vagueness', np.nan)

        status = "✅" if (beta < 0 and pval < 0.05) else "❌"
        logger.info(f"    Result: β={beta:.4f}, p={pval:.4f} {status}")
        logger.info(f"    Expected: β < 0 (vagueness reduces early funding)")
        logger.info(f"    Supported: {beta < 0 and pval < 0.05}")

    except Exception as e:
        logger.error(f"    Failed: {e}")
        results['h1'] = None

    # H2: Growth ~ vagueness
    logger.info("\n  Testing H💰L🤙V: Growth ~ Vagueness")
    try:
        h2_main = models.test_h2_main_growth(df)
        results['h2_main'] = h2_main

        beta = h2_main.params.get('z_vagueness', np.nan)
        pval = h2_main.pvalues.get('z_vagueness', np.nan)

        status = "✅" if (beta > 0 and pval < 0.05) else "❌"
        logger.info(f"    Result: β={beta:.4f}, p={pval:.4f} {status}")
        logger.info(f"    Expected: β > 0 (vagueness increases growth)")
        logger.info(f"    Supported: {beta > 0 and pval < 0.05}")

    except Exception as e:
        logger.error(f"    Failed: {e}")
        results['h2_main'] = None

    # H2 Interaction: Growth ~ vagueness × hardware
    logger.info("\n  Testing H💰L🤙V💪F: Growth ~ Vagueness × Hardware")
    try:
        # H2 model already includes interaction
        if 'h2_main' in results and results['h2_main'] is not None:
            h2 = results['h2_main']

            # Try to find interaction term
            param_names = [str(p) for p in h2.params.index]
            int_terms = [p for p in param_names if 'vagueness' in p.lower() and 'hardware' in p.lower()]

            if int_terms:
                int_term = int_terms[0]
                beta_int = h2.params[int_term]
                pval_int = h2.pvalues[int_term]

                status = "✅" if (beta_int != 0 and pval_int < 0.05) else "❌"
                logger.info(f"    Result: β_interaction={beta_int:.4f}, p={pval_int:.4f} {status}")
                logger.info(f"    Expected: Moderation effect (hardware attenuates vagueness benefit)")
                logger.info(f"    Supported: {pval_int < 0.05}")
            else:
                logger.warning("    Interaction term not found in model")

    except Exception as e:
        logger.error(f"    Failed: {e}")

    logger.info(f"\n  ✅ Hypothesis testing complete")

    # Save results summary
    output_path = output_dir / 'hypothesis_results.txt'
    with open(output_path, 'w') as f:
        f.write("HYPOTHESIS TEST RESULTS\n")
        f.write("="*80 + "\n\n")

        for hyp_name, model in results.items():
            if model is not None:
                f.write(f"{hyp_name}:\n")
                f.write(str(model.summary()) + "\n\n")

    logger.info(f"  Results saved to: {output_path}")

    return results


def stage_5_plot2(df: pd.DataFrame, output_dir: Path) -> None:
    """
    5📈PLOT2: Run and visualize multiverse analysis.

    Creates:
        - Expectation vs Reality heatmap
        - Enhanced specification curve

    Args:
        df: DataFrame with features
        output_dir: Output directory for plots
    """
    logger.info("\n" + "="*80)
    logger.info("5📈 STAGE 5: PLOT2 - Multiverse analysis visualization")
    logger.info("="*80)

    # Check if multiverse results exist
    multiverse_dir = Path('multiverse_results')

    if not multiverse_dir.exists():
        logger.warning("  Multiverse results directory not found")
        logger.info("  To generate multiverse results, run:")
        logger.info("    python run_multiverse.py --input data/processed/analysis_panel.csv --outdir multiverse_results/")
        return

    # Look for results file
    results_files = list(multiverse_dir.glob('spec_table*.csv'))

    if not results_files:
        logger.warning("  No multiverse results files found")
        return

    results_path = results_files[0]
    logger.info(f"  Loading multiverse results from: {results_path}")

    try:
        results = pd.read_csv(results_path)
        logger.info(f"    → Loaded {len(results):,} specifications")

        # Create expectation vs reality heatmap
        logger.info("\n  Creating expectation vs reality heatmap...")
        heatmap_path = output_dir / 'expectation_reality_heatmap.png'
        plots.plot_expectation_reality_heatmap(results, output_path=heatmap_path)

        # Create enhanced specification curve
        logger.info("\n  Creating enhanced specification curve...")
        curve_path = output_dir / 'specification_curve_enhanced.png'
        plots.plot_enhanced_specification_curve(
            results,
            hypothesis_name='Vagueness → Growth',
            expected_sign=1,
            output_path=curve_path
        )

        logger.info(f"\n  ✅ Multiverse visualizations complete")

    except Exception as e:
        logger.error(f"  Failed to create multiverse visualizations: {e}")


def create_quantum_dataset_cli(
    data_dir: str = 'data/raw/',
    output_path: str = 'data/processed/quantum_hypothesis_data.parquet'
) -> None:
    """
    CLI wrapper for creating quantum-focused dataset.

    Args:
        data_dir: Directory containing raw .dat files
        output_path: Path to save quantum dataset
    """
    logger.info("\n" + "🔬" * 40)
    logger.info("QUANTUM DATASET CREATION")
    logger.info("🔬" * 40)

    try:
        df_quantum = features.create_quantum_dataset(data_dir, output_path)

        logger.info("\n" + "="*80)
        logger.info("✅ QUANTUM DATASET CREATED!")
        logger.info("="*80)
        logger.info(f"\nDataset shape: {df_quantum.shape[0]:,} companies × {df_quantum.shape[1]} columns")
        logger.info(f"Saved to: {output_path}")

    except Exception as e:
        logger.error(f"\n❌ Quantum dataset creation failed: {e}", exc_info=True)
        sys.exit(1)


def main(
    data_dir: str = 'data/raw/',
    output_dir: str = 'results/',
    skip_dat: bool = False,
    quantum_only: bool = False,
    use_quantum_cache: bool = False,
    years: Optional[List[int]] = None
) -> None:
    """
    Execute complete 5-stage pipeline.

    Args:
        data_dir: Directory containing raw .dat files
        output_dir: Output directory for results
        skip_dat: If True, skip .dat loading and use processed CSV
        quantum_only: If True, create quantum dataset only and exit
        use_quantum_cache: If True, use quantum company cache (quantum_companies_*.parquet)
        years: Optional list of years to load (e.g., [2022, 2024, 2025]).
               For time windows 2022-2024 and 2022-2025, use [2022, 2024, 2025]
               to load only 6 files instead of all 9 (33% faster).
    """
    # Special mode: Create quantum dataset only
    if quantum_only:
        create_quantum_dataset_cli(
            data_dir,
            output_path='data/processed/quantum_hypothesis_data.parquet'
        )
        return

    logger.info("\n" + "🌟" * 40)
    logger.info("MULTIVERSE ANALYSIS PIPELINE")
    logger.info("🌟" * 40)

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    try:
        # 1🏗️BUILD
        df = stage_1_build(data_dir, use_processed=skip_dat, use_cache=True, years=years, quantum_only=use_quantum_cache)

        # 2🧠DEFINE
        df = stage_2_define(df)

        # 3📊PLOT1
        stage_3_plot1(df, output_path)

        # 4⚖️TEST
        results = stage_4_test(df, output_path)

        # 5📈PLOT2
        stage_5_plot2(df, output_path)

        logger.info("\n" + "="*80)
        logger.info("✅ PIPELINE COMPLETE!")
        logger.info("="*80)
        logger.info(f"\nResults saved to: {output_path.absolute()}")
        logger.info("\nGenerated files:")
        for file in sorted(output_path.glob('*')):
            logger.info(f"  - {file.name}")

    except Exception as e:
        logger.error(f"\n❌ Pipeline failed: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Multiverse Analysis Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Use .dat files (if available)
  python main.py --data-dir data/raw/ --output-dir results/

  # Use processed CSV (skip .dat loading)
  python main.py --skip-dat --output-dir results/

  # Custom directories
  python main.py --data-dir /path/to/data --output-dir /path/to/output
        """
    )

    parser.add_argument(
        '--data-dir',
        default='data/raw/',
        help='Directory containing raw .dat files (default: data/raw/)'
    )

    parser.add_argument(
        '--output-dir',
        default='results/',
        help='Output directory for results (default: results/)'
    )

    parser.add_argument(
        '--skip-dat',
        action='store_true',
        help='Skip .dat file loading and use processed CSV instead'
    )

    parser.add_argument(
        '--quantum-only',
        action='store_true',
        help='Create quantum-focused dataset only (filters quantum companies, saves minimal columns)'
    )

    parser.add_argument(
        '--use-quantum-cache',
        action='store_true',
        help='Use quantum company cache (quantum_companies_*.parquet) for pipeline. '
             'Creates separate cache from regular companies cache.'
    )

    parser.add_argument(
        '--years',
        type=int,
        nargs='+',
        help='Specific years to load (e.g., --years 2022 2024 2025). '
             'Default: load all years. Use [2022, 2024, 2025] for time windows 2022-2024 and 2022-2025.'
    )

    args = parser.parse_args()

    main(
        data_dir=args.data_dir,
        output_dir=args.output_dir,
        skip_dat=args.skip_dat,
        quantum_only=args.quantum_only,
        use_quantum_cache=args.use_quantum_cache,
        years=args.years
    )
