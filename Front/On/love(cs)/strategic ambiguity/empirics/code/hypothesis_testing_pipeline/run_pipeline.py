#!/usr/bin/env python3
"""
End-to-End Hypothesis Testing Pipeline

This script orchestrates the complete pipeline for testing H1 and H2:
- Data loading from CSV
- Feature engineering
- xarray Dataset management
- Hypothesis testing (OLS and Logit)
- Visualization
- Results export

Usage:
    python run_pipeline.py --data path/to/pb_company_raw.csv
    python run_pipeline.py --help
"""

import pandas as pd
import numpy as np
import xarray as xr
from pathlib import Path
import argparse
import sys
import json
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from feature_engineering import (
    engineer_features, get_feature_summary, create_analysis_dataset
)
from hypothesis_tests import (
    run_full_hypothesis_tests, results_to_xarray, create_results_summary
)
from visualizations import create_all_visualizations


class HypothesisTestingPipeline:
    """
    End-to-end pipeline for hypothesis testing using xarray for data management.
    """

    def __init__(self, data_path: str = None, output_dir: str = "output"):
        """
        Initialize pipeline.

        Args:
            data_path: Path to input CSV file
            output_dir: Directory for outputs
        """
        self.data_path = Path(data_path) if data_path else None
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.df = None
        self.ds = None  # xarray Dataset
        self.results = None
        self.results_ds = None  # xarray Dataset with results

        self.metadata = {
            'pipeline_version': '1.0.0_hypothesis_testing',
            'created_at': datetime.now().isoformat(),
            'data_source': str(self.data_path) if self.data_path else 'unknown'
        }

    def step_1_load_data(self, csv_path: str = None):
        """
        Step 1: Load raw CSV data into pandas DataFrame.

        Args:
            csv_path: Optional path to CSV file (overrides init path)
        """
        print("\n" + "="*80)
        print("STEP 1: LOAD DATA")
        print("="*80)

        if csv_path:
            self.data_path = Path(csv_path)

        if not self.data_path or not self.data_path.exists():
            raise FileNotFoundError(f"Data file not found: {self.data_path}")

        print(f"Loading: {self.data_path}")

        # Try different delimiters
        for delimiter in ['|', ',', '\t']:
            try:
                self.df = pd.read_csv(self.data_path, sep=delimiter, low_memory=False)
                if len(self.df.columns) > 1:  # Valid if multiple columns
                    break
            except:
                continue

        if self.df is None or len(self.df.columns) == 1:
            raise ValueError("Could not parse CSV file. Check delimiter.")

        print(f"  ✓ Loaded {len(self.df)} rows, {len(self.df.columns)} columns")
        print(f"  Columns: {list(self.df.columns[:10])}...")

        # Store metadata
        self.metadata['n_rows_raw'] = len(self.df)
        self.metadata['n_cols_raw'] = len(self.df.columns)

    def step_2_engineer_features(self):
        """
        Step 2: Engineer features for hypothesis testing.
        """
        print("\n" + "="*80)
        print("STEP 2: FEATURE ENGINEERING")
        print("="*80)

        if self.df is None:
            raise ValueError("Must load data first (step_1_load_data)")

        # Engineer features
        self.df = engineer_features(self.df)

        # Print summary
        print("\n" + "-"*80)
        print("Feature Summary:")
        print("-"*80)
        summary = get_feature_summary(self.df)
        print(summary)

        # Store metadata
        self.metadata['n_rows_engineered'] = len(self.df)

    def step_3_create_xarray_dataset(self):
        """
        Step 3: Convert DataFrame to xarray Dataset with proper coords.
        """
        print("\n" + "="*80)
        print("STEP 3: CREATE XARRAY DATASET")
        print("="*80)

        if self.df is None:
            raise ValueError("Must engineer features first (step_2_engineer_features)")

        # Create company IDs if not present
        if 'CompanyID' in self.df.columns:
            company_ids = self.df['CompanyID'].values
        elif 'company_id' in self.df.columns:
            company_ids = self.df['company_id'].values
        else:
            company_ids = np.arange(len(self.df))
            self.df['company_id'] = company_ids

        # Select analytical columns (updated for Phase 2 specs)
        analysis_cols = [
            'vagueness', 'high_integration_cost', 'early_funding_musd',
            'survival', 'later_success',  # Keep later_success for backward compat
            'founder_credibility', 'employees_log', 'sector_fe', 'year_founded',
            'series_a_funding', 'series_b_funding', 'is_down_round',
            'firm_age', 'total_raised'
        ]

        # Only keep columns that exist
        available_cols = [col for col in analysis_cols if col in self.df.columns]

        # Create xarray Dataset
        df_analysis = self.df[available_cols].copy()
        df_analysis['company_id'] = company_ids

        # Set index and convert to xarray
        df_analysis = df_analysis.set_index('company_id')

        self.ds = xr.Dataset.from_dataframe(df_analysis)

        # Add coordinates for hierarchical grouping
        if 'Keywords' in self.df.columns or 'keywords' in self.df.columns:
            keywords_col = 'Keywords' if 'Keywords' in self.df.columns else 'keywords'
            self.ds = self.ds.assign_coords(
                sector=('company_id', self.df[keywords_col].values)
            )

        if 'year_founded' in self.df.columns:
            self.ds = self.ds.assign_coords(
                year=('company_id', self.df['year_founded'].values)
            )

        # Add metadata as attributes
        self.ds.attrs.update(self.metadata)

        print(f"  ✓ Created xarray Dataset")
        print(f"    Dimensions: {dict(self.ds.dims)}")
        print(f"    Variables: {list(self.ds.data_vars)}")
        print(f"    Coordinates: {list(self.ds.coords)}")

    def step_4_run_hypothesis_tests(self):
        """
        Step 4: Run H1 and H2 hypothesis tests.
        """
        print("\n" + "="*80)
        print("STEP 4: HYPOTHESIS TESTING")
        print("="*80)

        if self.ds is None:
            raise ValueError("Must create xarray dataset first (step_3_create_xarray_dataset)")

        # Convert xarray back to DataFrame for modeling
        df_model = self.ds.to_dataframe().reset_index()

        # Run tests
        self.results = run_full_hypothesis_tests(df_model)

        # Convert results to xarray
        self.results_ds = results_to_xarray(self.results)

        print("\n" + "="*80)
        print("HYPOTHESIS TEST SUMMARY")
        print("="*80)
        summary = create_results_summary(self.results)
        print(summary.to_string(index=False))

        # Save summary
        summary_path = self.output_dir / "hypothesis_test_summary.csv"
        summary.to_csv(summary_path, index=False)
        print(f"\n  ✓ Saved summary: {summary_path}")

    def step_5_create_visualizations(self):
        """
        Step 5: Create all diagnostic plots.
        """
        print("\n" + "="*80)
        print("STEP 5: VISUALIZATIONS")
        print("="*80)

        if self.results is None:
            raise ValueError("Must run hypothesis tests first (step_4_run_hypothesis_tests)")

        # Convert xarray to DataFrame for plotting
        df_plot = self.ds.to_dataframe().reset_index()

        # Create visualizations
        created_files = create_all_visualizations(
            df_plot,
            self.results,
            self.output_dir
        )

        # Store in metadata
        self.metadata['visualization_files'] = {
            name: str(path) for name, path in created_files.items()
        }

    def step_6_save_outputs(self):
        """
        Step 6: Save all outputs (xarray datasets, model results).
        """
        print("\n" + "="*80)
        print("STEP 6: SAVE OUTPUTS")
        print("="*80)

        # Save xarray dataset
        if self.ds is not None:
            dataset_path = self.output_dir / "pb_processed_dataset.nc"
            self.ds.to_netcdf(dataset_path)
            print(f"  ✓ Saved xarray dataset: {dataset_path}")

        # Save results xarray
        if self.results_ds is not None:
            results_path = self.output_dir / "model_results.nc"
            self.results_ds.to_netcdf(results_path)
            print(f"  ✓ Saved model results: {results_path}")

        # Save coefficient tables
        if self.results and self.results.get('h1'):
            h1_table = pd.DataFrame({
                'Variable': self.results['h1'].params.index,
                'Coefficient': self.results['h1'].params.values,
                'Std Error': self.results['h1'].bse.values,
                'p-value': self.results['h1'].pvalues.values,
                'CI Lower': self.results['h1'].conf_int().iloc[:, 0].values,
                'CI Upper': self.results['h1'].conf_int().iloc[:, 1].values
            })
            h1_path = self.output_dir / "h1_coefficients.csv"
            h1_table.to_csv(h1_path, index=False)
            print(f"  ✓ Saved H1 coefficients: {h1_path}")

        # Save H2 Main coefficients
        h2_model = self.results.get('h2_main') or self.results.get('h2')  # Backward compat
        if self.results and h2_model:
            h2_table = pd.DataFrame({
                'Variable': h2_model.params.index,
                'Coefficient': h2_model.params.values,
                'Std Error': h2_model.bse.values,
                'p-value': h2_model.pvalues.values,
                'CI Lower': h2_model.conf_int().iloc[:, 0].values,
                'CI Upper': h2_model.conf_int().iloc[:, 1].values
            })
            h2_path = self.output_dir / "h2_main_coefficients.csv"
            h2_table.to_csv(h2_path, index=False)
            print(f"  ✓ Saved H2 Main coefficients: {h2_path}")

        # Save H2 Robustness coefficients
        if self.results and self.results.get('h2_robustness'):
            h2r_table = pd.DataFrame({
                'Variable': self.results['h2_robustness'].params.index,
                'Coefficient': self.results['h2_robustness'].params.values,
                'Std Error': self.results['h2_robustness'].bse.values,
                'p-value': self.results['h2_robustness'].pvalues.values,
                'CI Lower': self.results['h2_robustness'].conf_int().iloc[:, 0].values,
                'CI Upper': self.results['h2_robustness'].conf_int().iloc[:, 1].values
            })
            h2r_path = self.output_dir / "h2_robustness_coefficients.csv"
            h2r_table.to_csv(h2r_path, index=False)
            print(f"  ✓ Saved H2 Robustness coefficients: {h2r_path}")

        # Save metadata
        metadata_path = self.output_dir / "pipeline_metadata.json"
        with open(metadata_path, 'w') as f:
            json.dump(self.metadata, f, indent=2, default=str)
        print(f"  ✓ Saved metadata: {metadata_path}")

    def run_full_pipeline(self, data_path: str = None):
        """
        Execute complete pipeline end-to-end.

        Args:
            data_path: Optional path to data file
        """
        print("\n" + "="*80)
        print("HYPOTHESIS TESTING PIPELINE - FULL RUN")
        print("="*80)
        print(f"Version: {self.metadata['pipeline_version']}")
        print(f"Started: {self.metadata['created_at']}")

        try:
            self.step_1_load_data(data_path)
            self.step_2_engineer_features()
            self.step_3_create_xarray_dataset()
            self.step_4_run_hypothesis_tests()
            self.step_5_create_visualizations()
            self.step_6_save_outputs()

            print("\n" + "="*80)
            print("🎉 PIPELINE COMPLETED SUCCESSFULLY")
            print("="*80)
            print(f"\nOutputs saved to: {self.output_dir}")
            print(f"\nDeliverables:")
            print(f"  - pb_processed_dataset.nc (xarray dataset)")
            print(f"  - model_results.nc (model coefficients)")
            print(f"  - hypothesis_test_summary.csv (test results)")
            print(f"  - h1_coefficients.csv (H1: Early Funding)")
            print(f"  - h2_main_coefficients.csv (H2 Main: Survival)")
            print(f"  - h2_robustness_coefficients.csv (H2 Robustness: Series B)")
            print(f"  - regression_table.csv (AER-style table)")
            print(f"  - Diagnostic plots (*.png including ROC curve)")

        except Exception as e:
            print(f"\n❌ PIPELINE FAILED: {e}")
            import traceback
            traceback.print_exc()
            raise


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(
        description='Hypothesis Testing Pipeline for Promise Vagueness Research',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run with PitchBook data
  python run_pipeline.py --data data/pb_company_raw.csv

  # Specify custom output directory
  python run_pipeline.py --data data/pb_company_raw.csv --output results/

  # Use demo/simulated data
  python run_pipeline.py --demo
        """
    )

    parser.add_argument(
        '--data',
        type=str,
        help='Path to input CSV file (PitchBook format)'
    )

    parser.add_argument(
        '--output',
        type=str,
        default='output',
        help='Output directory for results (default: output/)'
    )

    parser.add_argument(
        '--demo',
        action='store_true',
        help='Run with simulated demo data'
    )

    args = parser.parse_args()

    # Create demo data if requested
    if args.demo:
        print("Creating simulated demo data...")
        np.random.seed(42)
        n = 300

        demo_df = pd.DataFrame({
            'CompanyID': range(n),
            'CompanyName': [f'Company_{i}' for i in range(n)],
            'Description': [
                f"We provide {'approximately ' if np.random.rand() > 0.5 else ''}scalable AI solutions"
                for _ in range(n)
            ],
            'Keywords': [
                np.random.choice(['software, API, cloud', 'hardware, robotics, chip'])
                for _ in range(n)
            ],
            'FirstFinancingSize': np.random.lognormal(15, 0.8, n),
            'LastFinancingDealType': np.random.choice(
                ['Series A', 'Series B', 'Series C'],
                n,
                p=[0.5, 0.3, 0.2]
            ),
            'Employees': np.random.randint(10, 500, n),
            'YearFounded': np.random.randint(2015, 2023, n),
            'TotalRaised': np.random.lognormal(16, 1, n)
        })

        # Save demo data
        demo_path = Path('data') / 'demo_data.csv'
        demo_path.parent.mkdir(exist_ok=True)
        demo_df.to_csv(demo_path, index=False, sep='|')
        print(f"  ✓ Created demo data: {demo_path}")
        args.data = str(demo_path)

    # Validate input
    if not args.data:
        parser.error("Must specify --data or --demo")

    # Run pipeline
    pipeline = HypothesisTestingPipeline(
        data_path=args.data,
        output_dir=args.output
    )

    pipeline.run_full_pipeline()


if __name__ == "__main__":
    main()
