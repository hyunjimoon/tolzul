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
import json
import os

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

        # Use JSON for lightweight checkpoint metadata
        self.checkpoint_file = self.output_dir / "pipeline_checkpoint.json"
        self.data_dir = base_dir / "data" / "processed"
        self.data_dir.mkdir(parents=True, exist_ok=True)

        # Initialize or load checkpoint metadata
        if self.checkpoint_file.exists():
            print(f"📂 Loading checkpoint: {self.checkpoint_file}")
            with open(self.checkpoint_file, 'r') as f:
                self.checkpoint = json.load(f)
            # Recreate dataset from saved data
            self.ds = self._load_dataset_from_checkpoint()
        else:
            print("🆕 Creating new dataset")
            self.checkpoint = self._init_empty_checkpoint()
            self.ds = self._init_empty_dataset()

    def _init_empty_checkpoint(self):
        """Initialize empty checkpoint metadata"""
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

        return {
            'pipeline_version': '3.1_modular_xarray_lightweight',
            'created_at': datetime.now().isoformat(),
            'last_updated': datetime.now().isoformat(),
            'data_source': 'Pitchbook',
            'pipeline_status': 'initialized',
            'git_commit_id': git_commit,
            'git_commit_url': git_commit_url,
            'git_branch': git_branch,
            'git_branch_url': git_branch_url,
            'series_a_date_range': '2021-01-01 to 2022-10-31',
            'series_b_date_range': '2023-05-01 to 2025-10-31',
            'step_01_status': 'pending',
            'step_02_status': 'pending',
            'step_03_status': 'pending',
            'step_04_status': 'pending',
            'step_05_status': 'pending',
            'completed_steps': []
        }

    def _init_empty_dataset(self):
        """Initialize empty xarray Dataset with metadata"""
        ds = xr.Dataset(attrs=self.checkpoint.copy())
        return ds

    def _load_dataset_from_checkpoint(self):
        """Load dataset from checkpoint by reading saved files (parquet preferred)"""
        ds = xr.Dataset(attrs=self.checkpoint.copy())

        # Load company data if step 1 is completed
        if self.checkpoint.get('step_01_status') == 'completed':
            # Try parquet first (faster), fall back to CSV
            parquet_file = self.data_dir / "company_master.parquet"
            csv_file = self.data_dir / "company_master.csv"

            if parquet_file.exists():
                company_df = pd.read_parquet(parquet_file)
                company_df = company_df.set_index('company_id')
                self._dataframe_to_xarray(ds, company_df, 'company', 'company_')
                print(f"  ✅ Loaded {len(company_df)} companies from checkpoint (parquet)")
            elif csv_file.exists():
                company_df = pd.read_csv(csv_file)
                company_df = company_df.set_index('company_id')
                self._dataframe_to_xarray(ds, company_df, 'company', 'company_')
                print(f"  ✅ Loaded {len(company_df)} companies from checkpoint (CSV)")

        # Load deal data if step 2 is completed
        if self.checkpoint.get('step_02_status') == 'completed':
            # Try parquet first (faster), fall back to CSV
            parquet_file = self.data_dir / "deal_master.parquet"
            csv_file = self.data_dir / "deal_master.csv"

            if parquet_file.exists():
                deal_df = pd.read_parquet(parquet_file)
                deal_df = deal_df.set_index('deal_id')
                self._dataframe_to_xarray(ds, deal_df, 'deal', 'deal_')
                print(f"  ✅ Loaded {len(deal_df)} deals from checkpoint (parquet)")
            elif csv_file.exists():
                deal_df = pd.read_csv(csv_file)
                deal_df = deal_df.set_index('deal_id')
                self._dataframe_to_xarray(ds, deal_df, 'deal', 'deal_')
                print(f"  ✅ Loaded {len(deal_df)} deals from checkpoint (CSV)")

        # Load panel data if step 3 is completed
        if self.checkpoint.get('step_03_status') == 'completed':
            # Try parquet first (faster), fall back to CSV
            parquet_file = self.data_dir / "analysis_panel.parquet"
            csv_file = self.data_dir / "analysis_panel.csv"

            if parquet_file.exists():
                panel_df = pd.read_parquet(parquet_file)
                panel_df = panel_df.set_index('observation_id')
                self._dataframe_to_xarray(ds, panel_df, 'observation', 'panel_')
                print(f"  ✅ Loaded {len(panel_df)} observations from checkpoint (parquet)")
            elif csv_file.exists():
                panel_df = pd.read_csv(csv_file)
                panel_df = panel_df.set_index('observation_id')
                self._dataframe_to_xarray(ds, panel_df, 'observation', 'panel_')
                print(f"  ✅ Loaded {len(panel_df)} observations from checkpoint (CSV)")
        
        return ds

    def save_checkpoint(self, step_num, step_name):
        """Save lightweight checkpoint metadata (no large data)"""
        try:
            self.checkpoint['last_updated'] = datetime.now().isoformat()
            self.checkpoint['last_completed_step'] = step_name
            self.checkpoint[f'step_{step_num:02d}_status'] = 'completed'
            self.checkpoint[f'step_{step_num:02d}_timestamp'] = datetime.now().isoformat()
            
            if step_name not in self.checkpoint['completed_steps']:
                self.checkpoint['completed_steps'].append(step_name)
            
            # Save checkpoint as JSON (lightweight)
            temp_file = self.checkpoint_file.with_suffix('.json.tmp')
            with open(temp_file, 'w') as f:
                json.dump(self.checkpoint, f, indent=2)
            
            if self.checkpoint_file.exists():
                self.checkpoint_file.unlink()
            temp_file.rename(self.checkpoint_file)
            
            # Update dataset attributes
            self.ds.attrs.update(self.checkpoint)
            
            print(f"💾 Checkpoint saved: {step_name}")
            
        except OSError as e:
            if e.errno == 28:  # No space left on device
                print(f"⚠️  Warning: Could not save checkpoint due to disk space")
                print(f"   Data files are saved, you can resume from step {step_num}")
                # Update in-memory checkpoint anyway
                self.checkpoint['last_updated'] = datetime.now().isoformat()
                self.checkpoint['last_completed_step'] = step_name
                self.checkpoint[f'step_{step_num:02d}_status'] = 'completed'
                if step_name not in self.checkpoint['completed_steps']:
                    self.checkpoint['completed_steps'].append(step_name)
            else:
                raise

    def _dataframe_to_xarray(self, ds, df, dim_name, prefix):
        """
        Convert pandas DataFrame to xarray DataArrays

        Args:
            ds: xarray Dataset to add to
            df: pandas DataFrame
            dim_name: dimension name (e.g., 'company', 'deal', 'observation')
            prefix: variable name prefix (e.g., 'company_', 'deal_', 'panel_')
        """
        # Set index if not already set
        if df.index.name is None:
            df = df.reset_index(drop=True)
            df.index.name = 'idx'

        # Convert categorical columns to strings (xarray doesn't handle categoricals)
        df = df.copy()
        for col in df.columns:
            if pd.api.types.is_categorical_dtype(df[col]):
                df[col] = df[col].astype(str)

        # Store each column as separate DataArray
        for col in df.columns:
            var_name = f'{prefix}{col}'
            ds[var_name] = xr.DataArray(
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
        self._dataframe_to_xarray(self.ds, company_df, 'company', 'company_')

        # Store metadata
        self.ds.attrs['n_companies'] = len(company_df)
        self.checkpoint['n_companies'] = len(company_df)

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

        # Save deal data to CSV and Parquet for checkpointing
        deal_df_save = deal_df.reset_index()
        deal_df_save.to_csv(self.data_dir / "deal_master.csv", index=False)
        # Parquet is much faster to load for large files
        deal_df_save.to_parquet(self.data_dir / "deal_master.parquet", index=False)

        # Convert to xarray
        self._dataframe_to_xarray(self.ds, deal_df, 'deal', 'deal_')

        # Store metadata
        self.ds.attrs['n_deals'] = len(deal_df)
        self.checkpoint['n_deals'] = len(deal_df)

        if len(deal_df) == 0:
            print(f"\n  ⚠️  WARNING: Processed 0 deals")
            print(f"     This usually means no Deal*.dat files were found in data/raw/")
            print(f"     The pipeline will continue but analysis will be empty")
            print(f"     Please add Deal*.dat files to proceed with analysis")
        else:
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

        # Check if company data is in xarray dataset, if not load from disk
        if 'company' not in self.ds.dims:
            # Try parquet first (much faster), fall back to CSV
            parquet_file = self.data_dir / "company_master.parquet"
            csv_file = self.data_dir / "company_master.csv"

            if parquet_file.exists():
                print("  ℹ️  Company data not in xarray, loading from parquet (fast)...")
                company_df = pd.read_parquet(parquet_file)
                print(f"  ✅ Loaded {len(company_df)} companies from parquet")
            elif csv_file.exists():
                print("  ℹ️  Company data not in xarray, loading from CSV...")
                company_df = pd.read_csv(csv_file)
                print(f"  ✅ Loaded {len(company_df)} companies from CSV")
            else:
                raise FileNotFoundError(f"Company data not found: {csv_file}")
        else:
            # Reconstruct DataFrames from xarray - FIX: handle double-prefix correctly
            company_cols = []
            for v in self.ds.data_vars:
                if v.startswith('company_'):
                    col = v[len('company_'):]  # Slice instead of replace
                    company_cols.append(col)

            company_data = {}
            for col in company_cols:
                var_name = f'company_{col}'
                if var_name in self.ds:
                    company_data[col] = self.ds[var_name].values

            company_df = pd.DataFrame(company_data, index=self.ds['company'].values)
            company_df.index.name = 'company_id'
            company_df = company_df.reset_index()

        # Check if deal data is in xarray dataset, if not load from disk
        if 'deal' not in self.ds.dims:
            # Try parquet first (much faster), fall back to CSV
            parquet_file = self.data_dir / "deal_master.parquet"
            csv_file = self.data_dir / "deal_master.csv"

            if parquet_file.exists():
                print("  ℹ️  Deal data not in xarray, loading from parquet (fast)...")
                deal_df = pd.read_parquet(parquet_file)
                print(f"  ✅ Loaded {len(deal_df)} deals from parquet")
            elif csv_file.exists():
                print("  ℹ️  Deal data not in xarray, loading from CSV...")
                deal_df = pd.read_csv(csv_file)
                print(f"  ✅ Loaded {len(deal_df)} deals from CSV")
            else:
                raise FileNotFoundError(f"Deal data not found: {csv_file}")
        else:
            # Same fix for deals
            deal_cols = []
            for v in self.ds.data_vars:
                if v.startswith('deal_'):
                    col = v[len('deal_'):]  # Slice instead of replace
                    deal_cols.append(col)

            deal_data = {}
            for col in deal_cols:
                var_name = f'deal_{col}'
                if var_name in self.ds:
                    deal_data[col] = self.ds[var_name].values

            deal_df = pd.DataFrame(deal_data, index=self.ds['deal'].values)

        # Import and call function
        code_dir = self.base_dir / "code"
        mod = import_from_file("mod03", code_dir / "03_create_panel.py")
        panel_df = mod.create_analysis_panel(company_df, deal_df)

        # Create observation index
        panel_df['observation_id'] = range(len(panel_df))
        panel_df = panel_df.set_index('observation_id')

        # Save panel data to CSV and Parquet for checkpointing
        panel_df_save = panel_df.reset_index()
        panel_df_save.to_csv(self.data_dir / "analysis_panel.csv", index=False)
        # Parquet is much faster to load for large files
        panel_df_save.to_parquet(self.data_dir / "analysis_panel.parquet", index=False)

        # Convert to xarray
        self._dataframe_to_xarray(self.ds, panel_df, 'observation', 'panel_')

        # Store metadata
        self.ds.attrs['n_observations'] = len(panel_df)
        self.checkpoint['n_observations'] = len(panel_df)

        print(f"  ✅ Created panel with {len(panel_df)} observations")
        self.save_checkpoint(3, step_name)

    def step_04_run_analysis(self, force=False):
        """
        Step 4: Run regression analysis using imported function
        Creates: model_results.pkl and CSV tables
        """
        step_name = "04_run_analysis"

        if self.checkpoint.get('step_04_status') == 'completed' and not force:
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
        self.checkpoint['model_results_file'] = str(self.output_dir / 'model_results.pkl')

        print(f"  ✅ Analysis complete")
        self.save_checkpoint(4, step_name)

    def step_05_create_deliverables(self, force=False):
        """
        Step 5: Create figures and tables using imported function
        """
        step_name = "05_create_deliverables"

        if self.checkpoint.get('step_05_status') == 'completed' and not force:
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
        self.checkpoint['deliverables_created'] = 1
        self.checkpoint['deliverables_path'] = str(self.output_dir)

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
        print(f"  Series A: {self.checkpoint['series_a_date_range']}")
        print(f"  Series B: {self.checkpoint['series_b_date_range']}")
        print()

        for i, step in enumerate(steps, 1):
            if i < start_from:
                continue

            try:
                step(force=force_rerun)
            except Exception as e:
                print(f"\n❌ Error in step {i}: {step.__name__}")
                print(f"   {str(e)}")
                print(f"\n💡 To resume from this step: python pipeline_xarray.py --from {i}")
                import traceback
                traceback.print_exc()
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

        if 'last_completed_step' in self.checkpoint:
            print(f"\nLast completed: {self.checkpoint['last_completed_step']}")
            print(f"Last updated: {self.checkpoint['last_updated']}")
        
        print(f"\nCompleted steps: {', '.join(self.checkpoint.get('completed_steps', []))}")

        print(f"\nStep status:")
        for i in range(1, 6):
            status = self.checkpoint.get(f'step_{i:02d}_status', 'pending')
            print(f"  Step {i}: {status}")

        print(f"\nData variables in dataset:")
        for var in self.ds.data_vars:
            print(f"  - {var}: {self.ds[var].shape}")

        print(f"\nMetadata:")
        for key in ['pipeline_version', 'n_companies', 'n_deals', 'n_observations',
                    'series_a_date_range', 'series_b_date_range', 'git_commit_url']:
            if key in self.checkpoint:
                val = self.checkpoint[key]
                print(f"  - {key}: {val}")

    def search_companies(self, search_term, limit=20):
        """
        Search for companies by name
        
        Args:
            search_term: Company name to search for
            limit: Maximum results to return
        """
        if 'company_company_name' not in self.ds:
            print("⚠️  Company data not loaded yet")
            return None
        
        names = self.ds['company_company_name'].values
        ids = self.ds['company'].values
        
        # Case-insensitive search
        search_lower = search_term.lower()
        matches = []
        for i, name in enumerate(names):
            if pd.notna(name) and search_lower in str(name).lower():
                matches.append({'company_id': ids[i], 'company_name': name})
                if len(matches) >= limit:
                    break
        
        if matches:
            df = pd.DataFrame(matches)
            print(f"\n🔍 Found {len(matches)} companies matching '{search_term}':")
            for _, row in df.iterrows():
                print(f"  - {row['company_id']}: {row['company_name']}")
            return df
        else:
            print(f"\n❌ No companies found matching '{search_term}'")
            return None

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
