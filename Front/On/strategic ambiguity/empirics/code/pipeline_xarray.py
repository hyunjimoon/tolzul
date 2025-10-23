"""
Strategic Ambiguity Pipeline - xarray Edition

Modular pipeline that imports functions from 01-05 scripts,
converts DataFrames to xarray Datasets, and provides checkpoint/resume capability.

Date Filtering:
- Series A: 2021-01-01 to 2022-10-31
- Series B: 2023-05-01 to 2025-10-31

Usage:
    python pipeline_xarray.py                # Run full pipeline
    python pipeline_xarray.py --from 3       # Resume from step 3
    python pipeline_xarray.py --summary      # Show pipeline status
"""

import xarray as xr
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import pickle
import subprocess

# Import processing functions dynamically
import importlib.util

def import_from_file(module_name, file_path):
    """Import a module from a file path"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class StrategicAmbiguityPipeline:
    """
    xarray-based pipeline for Strategic Ambiguity empirical analysis
    with checkpoint/resume capability
    """

    def __init__(self, base_dir=None, output_dir="output"):
        """
        Initialize pipeline

        Args:
            base_dir: Base directory (default: parent of code directory)
            output_dir: Output directory name
        """
        if base_dir is None:
            base_dir = Path(__file__).parent.parent
        else:
            base_dir = Path(base_dir)

        self.base_dir = base_dir
        self.output_dir = base_dir / output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.checkpoint_file = self.output_dir / "pipeline_checkpoint.pkl"

        # Initialize or load checkpoint
        if self.checkpoint_file.exists():
            print(f"📂 Loading checkpoint: {self.checkpoint_file}")
            with open(self.checkpoint_file, 'rb') as f:
                self.ds = pickle.load(f)
        else:
            print("🆕 Creating new dataset")
            self.ds = self._init_empty_dataset()

    def _init_empty_dataset(self):
        """Initialize empty xarray Dataset with metadata"""
        # Get git metadata for reproducibility
        try:
            git_commit = subprocess.check_output(
                ['git', 'rev-parse', 'HEAD'],
                cwd=self.base_dir
            ).decode('utf-8').strip()

            git_branch = subprocess.check_output(
                ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                cwd=self.base_dir
            ).decode('utf-8').strip()

            repo_url = 'https://github.com/hyunjimoon/tolzul'
            git_commit_url = f'{repo_url}/commit/{git_commit}'
            git_branch_url = f'{repo_url}/tree/{git_branch}'
        except:
            git_commit = 'unknown'
            git_branch = 'unknown'
            git_commit_url = 'unknown'
            git_branch_url = 'unknown'

        ds = xr.Dataset(
            attrs={
                'pipeline_version': '3.0_modular_xarray',
                'created_at': datetime.now().isoformat(),
                'last_updated': datetime.now().isoformat(),
                'data_source': 'Pitchbook',
                'pipeline_status': 'initialized',
                # Git metadata for reproducibility
                'git_commit_id': git_commit,
                'git_commit_url': git_commit_url,
                'git_branch': git_branch,
                'git_branch_url': git_branch_url,
                # Date filtering
                'series_a_date_range': '2021-01-01 to 2022-10-31',
                'series_b_date_range': '2023-05-01 to 2025-10-31',
                # Step completion tracking
                'step_01_status': 'pending',
                'step_02_status': 'pending',
                'step_03_status': 'pending',
                'step_04_status': 'pending',
                'step_05_status': 'pending',
            }
        )
        return ds

    def save_checkpoint(self, step_num, step_name):
        """Save current state to disk with step completion tracking"""
        self.ds.attrs['last_updated'] = datetime.now().isoformat()
        self.ds.attrs['last_completed_step'] = step_name
        self.ds.attrs[f'step_{step_num:02d}_status'] = 'completed'
        self.ds.attrs[f'step_{step_num:02d}_timestamp'] = datetime.now().isoformat()

        # Force load into memory before saving
        self.ds.load()

        # Save as pickle
        temp_file = self.checkpoint_file.with_suffix('.pkl.tmp')
        with open(temp_file, 'wb') as f:
            pickle.dump(self.ds, f)

        if self.checkpoint_file.exists():
            self.checkpoint_file.unlink()
        temp_file.rename(self.checkpoint_file)

        # Reload
        with open(self.checkpoint_file, 'rb') as f:
            self.ds = pickle.load(f)

        print(f"💾 Checkpoint saved: {step_name}")

    def _dataframe_to_xarray(self, df, dim_name, prefix):
        """
        Convert pandas DataFrame to xarray DataArrays

        Args:
            df: pandas DataFrame
            dim_name: dimension name (e.g., 'company', 'deal', 'observation')
            prefix: variable name prefix (e.g., 'company_', 'deal_', 'panel_')
        """
        # Set index if not already set
        if df.index.name is None:
            df = df.reset_index(drop=True)
            df.index.name = 'idx'

        # Store each column as separate DataArray
        for col in df.columns:
            var_name = f'{prefix}{col}'
            self.ds[var_name] = xr.DataArray(
                df[col].values,
                dims=[dim_name],
                coords={dim_name: df.index.values}
            )

    def step_01_process_company_data(self, force=False):
        """
        Step 1: Process Company data using imported function
        Creates: ds['company_*'] variables
        """
        step_name = "01_process_company"

        if 'company_vagueness' in self.ds and not force:
            print(f"⏭️  Step 1: Skipping (already completed)")
            return

        print(f"▶️  Step 1: Processing company data...")

        # Import and call function
        code_dir = self.base_dir / "code"
        mod = import_from_file("mod01", code_dir / "01_process_company_data.py")
        company_df = mod.process_company_data()

        # Set company_id as index
        company_df = company_df.set_index('company_id')

        # Convert to xarray
        self._dataframe_to_xarray(company_df, 'company', 'company_')

        # Store metadata
        self.ds.attrs['n_companies'] = len(company_df)

        print(f"  ✅ Processed {len(company_df)} AI/ML companies")
        self.save_checkpoint(1, step_name)

    def step_02_process_deal_data(self, force=False):
        """
        Step 2: Process Deal data with date filtering using imported function
        Creates: ds['deal_*'] variables
        """
        step_name = "02_process_deal"

        if 'deal_funding_success' in self.ds and not force:
            print(f"⏭️  Step 2: Skipping (already completed)")
            return

        print(f"▶️  Step 2: Processing deal data...")

        # Import and call function with date filtering
        code_dir = self.base_dir / "code"
        mod = import_from_file("mod02", code_dir / "02_process_deal_data.py")
        deal_df = mod.process_deal_data(
            series_a_start='2021-01-01',
            series_a_end='2022-10-31',
            series_b_start='2023-05-01',
            series_b_end='2025-10-31'
        )

        # Create deal_id index
        deal_df['deal_id'] = range(len(deal_df))
        deal_df = deal_df.set_index('deal_id')

        # Convert to xarray
        self._dataframe_to_xarray(deal_df, 'deal', 'deal_')

        # Store metadata
        self.ds.attrs['n_deals'] = len(deal_df)

        print(f"  ✅ Processed {len(deal_df)} deals")
        self.save_checkpoint(2, step_name)

    def step_03_create_panel(self, force=False):
        """
        Step 3: Create analysis panel using imported function
        Creates: ds['panel_*'] variables
        """
        step_name = "03_create_panel"

        if 'panel_funding_success' in self.ds and not force:
            print(f"⏭️  Step 3: Skipping (already completed)")
            return

        print(f"▶️  Step 3: Creating analysis panel...")

        # Reconstruct DataFrames from xarray
        company_cols = [v.replace('company_', '') for v in self.ds.data_vars if v.startswith('company_')]
        company_data = {col: self.ds[f'company_{col}'].values for col in company_cols}
        company_df = pd.DataFrame(company_data, index=self.ds['company'].values)
        company_df.index.name = 'company_id'
        company_df = company_df.reset_index()

        deal_cols = [v.replace('deal_', '') for v in self.ds.data_vars if v.startswith('deal_')]
        deal_data = {col: self.ds[f'deal_{col}'].values for col in deal_cols}
        deal_df = pd.DataFrame(deal_data, index=self.ds['deal'].values)

        # Import and call function
        code_dir = self.base_dir / "code"
        mod = import_from_file("mod03", code_dir / "03_create_panel.py")
        panel_df = mod.create_analysis_panel(company_df, deal_df)

        # Create observation index
        panel_df['observation_id'] = range(len(panel_df))
        panel_df = panel_df.set_index('observation_id')

        # Convert to xarray
        self._dataframe_to_xarray(panel_df, 'observation', 'panel_')

        # Store metadata
        self.ds.attrs['n_observations'] = len(panel_df)

        print(f"  ✅ Created panel with {len(panel_df)} observations")
        self.save_checkpoint(3, step_name)

    def step_04_run_analysis(self, force=False):
        """
        Step 4: Run regression analysis using imported function
        Creates: model_results.pkl and CSV tables
        """
        step_name = "04_run_analysis"

        if self.ds.attrs.get('step_04_status') == 'completed' and not force:
            print(f"⏭️  Step 4: Skipping (already completed)")
            return

        print(f"▶️  Step 4: Running analysis...")

        # Reconstruct panel DataFrame from xarray
        panel_cols = [v.replace('panel_', '') for v in self.ds.data_vars if v.startswith('panel_')]
        panel_data = {col: self.ds[f'panel_{col}'].values for col in panel_cols}
        panel_df = pd.DataFrame(panel_data, index=self.ds['observation'].values)

        # Import and call function
        code_dir = self.base_dir / "code"
        mod = import_from_file("mod04", code_dir / "04_run_analysis.py")
        results = mod.run_analysis(panel_df)

        # Save results
        with open(self.output_dir / 'model_results.pkl', 'wb') as f:
            pickle.dump(results, f)

        # Save as CSV tables
        model1 = results['model1']
        model1_results = pd.DataFrame({
            'Variable': model1.params.index,
            'Coefficient': model1.params.values,
            'p-value': model1.pvalues.values,
        })
        model1_results.to_csv(self.output_dir / 'table2_model1.csv', index=False)

        model2 = results['model2']
        model2_results = pd.DataFrame({
            'Variable': model2.params.index,
            'Coefficient': model2.params.values,
            'p-value': model2.pvalues.values,
        })
        model2_results.to_csv(self.output_dir / 'table4_model2.csv', index=False)

        self.ds.attrs['model_results_file'] = str(self.output_dir / 'model_results.pkl')

        print(f"  ✅ Analysis complete")
        self.save_checkpoint(4, step_name)

    def step_05_create_deliverables(self, force=False):
        """
        Step 5: Create figures and tables using imported function
        """
        step_name = "05_create_deliverables"

        if self.ds.attrs.get('step_05_status') == 'completed' and not force:
            print(f"⏭️  Step 5: Skipping (already completed)")
            return

        print(f"▶️  Step 5: Creating deliverables...")

        # Reconstruct panel DataFrame from xarray
        panel_cols = [v.replace('panel_', '') for v in self.ds.data_vars if v.startswith('panel_')]
        panel_data = {col: self.ds[f'panel_{col}'].values for col in panel_cols}
        panel_df = pd.DataFrame(panel_data, index=self.ds['observation'].values)

        # Import and call function
        code_dir = self.base_dir / "code"
        mod = import_from_file("mod05", code_dir / "05_create_deliverables.py")
        created_files = mod.create_deliverables(panel_df, self.output_dir)

        self.ds.attrs['deliverables_created'] = 1
        self.ds.attrs['deliverables_path'] = str(self.output_dir)

        print(f"\n  ✅ All deliverables created")
        for name, path in created_files.items():
            print(f"     - {name}: {path}")

        self.save_checkpoint(5, step_name)

    def run_pipeline(self, start_from=1, force_rerun=False):
        """
        Run entire pipeline with checkpoint support

        Args:
            start_from: Step number to start from (1-5)
            force_rerun: If True, rerun all steps even if completed
        """
        steps = [
            self.step_01_process_company_data,
            self.step_02_process_deal_data,
            self.step_03_create_panel,
            self.step_04_run_analysis,
            self.step_05_create_deliverables
        ]

        print("=" * 80)
        print("STRATEGIC AMBIGUITY EMPIRICS PIPELINE")
        print("=" * 80)
        print(f"\nDate Filtering:")
        print(f"  Series A: {self.ds.attrs['series_a_date_range']}")
        print(f"  Series B: {self.ds.attrs['series_b_date_range']}")
        print()

        for i, step in enumerate(steps, 1):
            if i < start_from:
                continue

            try:
                step(force=force_rerun)
            except Exception as e:
                print(f"\n❌ Error in step {i}: {step.__name__}")
                print(f"   {str(e)}")
                print(f"\n💡 To resume from this step: pipeline.run_pipeline(start_from={i})")
                raise

        print("\n" + "=" * 80)
        print("🎉 PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 80)
        print(f"\nCheckpoint file: {self.checkpoint_file}")
        print(f"Output directory: {self.output_dir}")
        print(f"\n💡 Next: Explore data with exploration.ipynb")

    def get_summary(self):
        """Print summary of current pipeline state"""
        print("\n" + "=" * 80)
        print("PIPELINE STATUS")
        print("=" * 80)

        print(f"\nCheckpoint file: {self.checkpoint_file}")
        print(f"Exists: {self.checkpoint_file.exists()}")

        if 'last_completed_step' in self.ds.attrs:
            print(f"\nLast completed: {self.ds.attrs['last_completed_step']}")
            print(f"Last updated: {self.ds.attrs['last_updated']}")

        print(f"\nData variables in dataset:")
        for var in self.ds.data_vars:
            print(f"  - {var}: {self.ds[var].shape}")

        print(f"\nAttributes:")
        for key in ['pipeline_version', 'n_companies', 'n_deals', 'n_observations',
                    'series_a_date_range', 'series_b_date_range', 'git_commit_url']:
            if key in self.ds.attrs:
                val = self.ds.attrs[key]
                print(f"  - {key}: {val}")

    def to_dataframe(self):
        """
        Export all panel data to a single pandas DataFrame

        Returns:
            pd.DataFrame: Analysis panel
        """
        panel_cols = [v.replace('panel_', '') for v in self.ds.data_vars if v.startswith('panel_')]
        panel_data = {col: self.ds[f'panel_{col}'].values for col in panel_cols}
        panel_df = pd.DataFrame(panel_data, index=self.ds['observation'].values)
        return panel_df


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Strategic Ambiguity Empirics Pipeline')
    parser.add_argument('--from', dest='start_from', type=int, default=1,
                        help='Start from step number (1-5)')
    parser.add_argument('--force', action='store_true',
                        help='Force rerun all steps')
    parser.add_argument('--summary', action='store_true',
                        help='Print pipeline status summary')

    args = parser.parse_args()

    # Initialize pipeline
    pipeline = StrategicAmbiguityPipeline()

    if args.summary:
        pipeline.get_summary()
    else:
        pipeline.run_pipeline(start_from=args.start_from, force_rerun=args.force)
