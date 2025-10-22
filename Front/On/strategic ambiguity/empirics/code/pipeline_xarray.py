"""
Pitchbook Analysis Pipeline using xarray
Inspiration: https://github.com/hyunjimoon/VaccineMisinf/blob/main/V81/tf_fx_pcsth.py

Structure:
    dimensions:
        - company: [500001-01, 500001-02, ...]
        - round: [Series A, Series B]
        - variable: [vagueness, integration_cost, funding_success, ...]

    data_vars:
        - raw_company_data: (company, variable)
        - raw_deal_data: (company, round, variable)
        - processed_panel: (company, round, variable)
        - model_results: (model, coefficient)
        - figures: (figure_id, metadata)

    attrs:
        - pipeline_version: "1.0"
        - last_updated: "2025-10-22"
        - data_source: "Pitchbook"
"""

import xarray as xr
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import pickle

class PitchbookPipeline:
    """
    xarray-based pipeline for Pitchbook analysis with checkpoint/resume capability
    """

    def __init__(self, data_dir="data", output_dir="output"):
        self.data_dir = Path(data_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.checkpoint_file = self.output_dir / "pitchbook_analysis.nc"

        # Initialize or load existing dataset
        if self.checkpoint_file.exists():
            print(f"📂 Loading existing checkpoint: {self.checkpoint_file}")
            self.ds = xr.open_dataset(self.checkpoint_file)
        else:
            print("🆕 Creating new dataset")
            self.ds = self._init_empty_dataset()

    def _init_empty_dataset(self):
        """Initialize empty xarray Dataset with metadata"""
        ds = xr.Dataset(
            attrs={
                'pipeline_version': '1.0',
                'created_at': datetime.now().isoformat(),
                'last_updated': datetime.now().isoformat(),
                'data_source': 'Pitchbook',
                'pipeline_status': 'initialized'
            }
        )
        return ds

    def save_checkpoint(self, step_name):
        """Save current state to disk"""
        self.ds.attrs['last_updated'] = datetime.now().isoformat()
        self.ds.attrs['last_completed_step'] = step_name
        self.ds.to_netcdf(self.checkpoint_file)
        print(f"💾 Checkpoint saved: {step_name}")

    def step_01_process_company_data(self, force=False):
        """
        Step 1: Process Company data
        Creates: ds['company_data'] with dims (company, variable)
        """
        step_name = "01_process_company"

        if 'company_data' in self.ds and not force:
            print(f"⏭️  Step 1: Skipping (already completed)")
            return

        print(f"▶️  Step 1: Processing company data...")

        # Read raw data
        company_files = list((self.data_dir / "raw").glob("Company*.dat"))
        dfs = [pd.read_csv(f, sep='|', low_memory=False) for f in company_files]
        company_df = pd.concat(dfs, ignore_index=True)

        # Filter AI/ML firms (simplified for demo)
        ai_keywords = ['AI', 'ML', 'machine learning', 'artificial intelligence']
        def is_ai_ml(row):
            text = f"{row.get('Description', '')} {row.get('Keywords', '')}".lower()
            return any(kw.lower() in text for kw in ai_keywords)

        company_df['is_ai_ml'] = company_df.apply(is_ai_ml, axis=1)
        ai_ml_df = company_df[company_df['is_ai_ml']].copy()

        # Calculate vagueness (simplified)
        def calc_vagueness(desc):
            if pd.isna(desc):
                return 50
            text = str(desc).lower()
            vague_words = ['approximately', 'around', 'flexible', 'scalable']
            precise_words = ['precisely', 'exactly', 'guaranteed', 'specific']
            vague_count = sum(text.count(w) for w in vague_words)
            precise_count = sum(text.count(w) for w in precise_words)
            return max(0, min(100, 50 + 10 * (vague_count - precise_count)))

        ai_ml_df['vagueness'] = ai_ml_df['Description'].apply(calc_vagueness)

        # Classify integration cost
        def calc_integration_cost(row):
            text = f"{row.get('Keywords', '')} {row.get('Description', '')}".lower()
            high_i = any(w in text for w in ['chip', 'hardware', 'robotics', 'gpu'])
            low_i = any(w in text for w in ['api', 'saas', 'software', 'cloud'])
            return 1 if high_i and not low_i else 0

        ai_ml_df['high_integration_cost'] = ai_ml_df.apply(calc_integration_cost, axis=1)

        # Convert to xarray
        # Set company_id as index
        ai_ml_df = ai_ml_df.set_index('CompanyID')

        # Select key columns
        key_cols = ['CompanyName', 'vagueness', 'high_integration_cost',
                    'Employees', 'YearFounded', 'TotalRaised']
        company_data = ai_ml_df[key_cols].to_xarray()

        # Add to dataset
        self.ds['company_data'] = company_data.to_array(dim='variable')

        print(f"  ✅ Processed {len(ai_ml_df)} AI/ML companies")
        self.save_checkpoint(step_name)

    def step_02_process_deal_data(self, force=False):
        """
        Step 2: Process Deal data
        Creates: ds['deal_data'] with dims (deal_id, variable)
        """
        step_name = "02_process_deal"

        if 'deal_data' in self.ds and not force:
            print(f"⏭️  Step 2: Skipping (already completed)")
            return

        print(f"▶️  Step 2: Processing deal data...")

        # Read raw data
        deal_files = list((self.data_dir / "raw").glob("Deal*.dat"))
        dfs = [pd.read_csv(f, sep='|', low_memory=False) for f in deal_files]
        deal_df = pd.concat(dfs, ignore_index=True)

        # Filter to VC deals
        vc_deals = deal_df[deal_df['DealType'].isin(['Early Stage VC', 'Later Stage VC'])].copy()

        # Identify Series A/B
        series_a = vc_deals[vc_deals['VCRound'].str.contains('Series A', case=False, na=False)].copy()
        series_b = vc_deals[vc_deals['VCRound'].str.contains('Series B', case=False, na=False)].copy()

        # Add round label
        series_a['round'] = 'Series A'
        series_b['round'] = 'Series B'

        # Combine
        deal_panel = pd.concat([series_a, series_b], ignore_index=True)

        # Create funding success variable
        deal_panel['DealSize'] = pd.to_numeric(deal_panel['DealSize'], errors='coerce').fillna(0)
        deal_panel['funding_success'] = (
            (deal_panel['DealSize'] > 0) &
            (deal_panel['DealStatus'].str.contains('Completed', case=False, na=False))
        ).astype(int)

        # Convert to xarray
        deal_panel['deal_id'] = range(len(deal_panel))
        deal_panel = deal_panel.set_index('deal_id')

        key_cols = ['CompanyID', 'CompanyName', 'round', 'DealSize',
                    'funding_success', 'DealDate', 'PostValuation']
        deal_data = deal_panel[key_cols].to_xarray()

        self.ds['deal_data'] = deal_data.to_array(dim='variable')

        print(f"  ✅ Processed {len(deal_panel)} deals")
        self.save_checkpoint(step_name)

    def step_03_create_panel(self, force=False):
        """
        Step 3: Create analysis panel
        Creates: ds['analysis_panel'] with dims (observation, variable)
        """
        step_name = "03_create_panel"

        if 'analysis_panel' in self.ds and not force:
            print(f"⏭️  Step 3: Skipping (already completed)")
            return

        print(f"▶️  Step 3: Creating analysis panel...")

        # Convert back to pandas for merging (could be done in xarray but pandas is easier)
        company_df = self.ds['company_data'].to_pandas().T
        deal_df = self.ds['deal_data'].to_pandas().T

        # Merge
        panel = deal_df.merge(
            company_df,
            left_on='CompanyID',
            right_index=True,
            how='inner'
        )

        # Create panel structure (each firm × 2 rounds)
        # ... (similar logic as before)

        panel['observation_id'] = range(len(panel))
        panel = panel.set_index('observation_id')

        analysis_panel = panel.to_xarray()
        self.ds['analysis_panel'] = analysis_panel.to_array(dim='variable')

        print(f"  ✅ Created panel with {len(panel)} observations")
        self.save_checkpoint(step_name)

    def step_04_run_analysis(self, force=False):
        """
        Step 4: Run regression analysis
        Creates: ds['model_results']
        """
        step_name = "04_run_analysis"

        if 'model_results' in self.ds and not force:
            print(f"⏭️  Step 4: Skipping (already completed)")
            return

        print(f"▶️  Step 4: Running analysis...")

        # Convert to pandas for statsmodels
        panel_df = self.ds['analysis_panel'].to_pandas().T

        # Run regressions (simplified)
        import statsmodels.formula.api as smf

        model1 = smf.logit(
            'funding_success ~ vagueness + series_b_dummy + vagueness:series_b_dummy',
            data=panel_df
        ).fit(disp=False)

        # Store results
        results = {
            'model1_params': model1.params,
            'model1_pvalues': model1.pvalues,
            'model1_summary': str(model1.summary())
        }

        # Save as pickled object (xarray doesn't handle complex objects well)
        with open(self.output_dir / 'model_results.pkl', 'wb') as f:
            pickle.dump(results, f)

        self.ds.attrs['model_results_file'] = str(self.output_dir / 'model_results.pkl')

        print(f"  ✅ Analysis complete")
        self.save_checkpoint(step_name)

    def step_05_create_deliverables(self, force=False):
        """
        Step 5: Create figures and tables
        """
        step_name = "05_create_deliverables"

        if self.ds.attrs.get('deliverables_created') and not force:
            print(f"⏭️  Step 5: Skipping (already completed)")
            return

        print(f"▶️  Step 5: Creating deliverables...")

        # Create figures (simplified)
        import matplotlib.pyplot as plt

        panel_df = self.ds['analysis_panel'].to_pandas().T

        # Figure 1: Bar chart
        fig, ax = plt.subplots(figsize=(10, 6))
        success_by_round = panel_df.groupby('round')['funding_success'].mean()
        success_by_round.plot(kind='bar', ax=ax)
        ax.set_title('Funding Success by Round')
        ax.set_ylabel('Success Rate')
        plt.tight_layout()
        plt.savefig(self.output_dir / 'figure1_success_by_round.png', dpi=300)
        plt.close()

        self.ds.attrs['deliverables_created'] = True
        self.ds.attrs['deliverables_path'] = str(self.output_dir)

        print(f"  ✅ Deliverables created")
        self.save_checkpoint(step_name)

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
        print("PITCHBOOK ANALYSIS PIPELINE (xarray-based)")
        print("=" * 80)

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
        for key, val in self.ds.attrs.items():
            print(f"  - {key}: {val}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Pitchbook Analysis Pipeline')
    parser.add_argument('--from', dest='start_from', type=int, default=1,
                        help='Start from step number (1-5)')
    parser.add_argument('--force', action='store_true',
                        help='Force rerun all steps')
    parser.add_argument('--summary', action='store_true',
                        help='Print pipeline status summary')

    args = parser.parse_args()

    # Initialize pipeline
    pipeline = PitchbookPipeline()

    if args.summary:
        pipeline.get_summary()
    else:
        pipeline.run_pipeline(start_from=args.start_from, force_rerun=args.force)
