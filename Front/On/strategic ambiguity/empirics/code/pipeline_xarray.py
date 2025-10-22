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

    def __init__(self, data_dir="data", output_dir="output", sample_size=None):
        self.data_dir = Path(data_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.sample_size = sample_size  # For POC: read only first N rows

        # Use pickle format only
        if self.sample_size:
            print(f"🔬 POC MODE: Using sample_size={sample_size} rows")
            self.checkpoint_file = self.output_dir / f"pitchbook_analysis_sample{sample_size}.pkl"
        else:
            self.checkpoint_file = self.output_dir / "pitchbook_analysis.pkl"

        # Initialize or load
        if self.checkpoint_file.exists():
            print(f"📂 Loading checkpoint: {self.checkpoint_file}")
            with open(self.checkpoint_file, 'rb') as f:
                self.ds = pickle.load(f)
        else:
            print("🆕 Creating new dataset")
            self.ds = self._init_empty_dataset()

    def _init_empty_dataset(self):
        """Initialize empty xarray Dataset with metadata including git info"""
        import subprocess

        # Get git metadata for reproducibility
        try:
            git_commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'],
                                                  cwd=Path(__file__).parent.parent).decode('utf-8').strip()
            git_branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                                                  cwd=Path(__file__).parent.parent).decode('utf-8').strip()
            git_remote = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'],
                                                  cwd=Path(__file__).parent.parent).decode('utf-8').strip()

            # Construct GitHub URL
            if 'github.com' in git_remote or 'hyunjimoon/tolzul' in git_remote:
                repo_url = 'https://github.com/hyunjimoon/tolzul'
                git_commit_url = f'{repo_url}/commit/{git_commit}'
                git_branch_url = f'{repo_url}/tree/{git_branch}'
            else:
                git_commit_url = f'commit:{git_commit}'
                git_branch_url = f'branch:{git_branch}'
        except:
            git_commit = 'unknown'
            git_branch = 'unknown'
            git_commit_url = 'unknown'
            git_branch_url = 'unknown'

        ds = xr.Dataset(
            attrs={
                'pipeline_version': '2.0_xarray_only',
                'created_at': datetime.now().isoformat(),
                'last_updated': datetime.now().isoformat(),
                'data_source': 'Pitchbook',
                'pipeline_status': 'initialized',
                # Git metadata for reproducibility
                'git_commit_id': git_commit,
                'git_commit_url': git_commit_url,
                'git_branch': git_branch,
                'git_branch_url': git_branch_url,
                'github_pr_url': '',  # Will be filled when PR is created
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

        self.ds.load()

        # Save as pickle
        temp_file = self.checkpoint_file.with_suffix('.pkl.tmp')
        with open(temp_file, 'wb') as f:
            pickle.dump(self.ds, f)

        if self.checkpoint_file.exists():
            self.checkpoint_file.unlink()
        temp_file.rename(self.checkpoint_file)

        # Reopen
        with open(self.checkpoint_file, 'rb') as f:
            self.ds = pickle.load(f)

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

        # Read Company2023.dat
        company_file = "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Front/On/strategic ambiguity/empirics/data/raw/Company20230501.dat"
        
        # Read with sample_size for POC
        if self.sample_size:
            print(f"  🔬 Reading first {self.sample_size} rows for POC...")
            company_df = pd.read_csv(company_file, sep='|', low_memory=False, nrows=self.sample_size)
        else:
            company_df = pd.read_csv(company_file, sep='|', low_memory=False)
        print(f"  ✓ Loaded {len(company_df)} rows")

        # Filter AI/ML firms (simplified for demo)
        ai_keywords = ['AI', 'ML', 'machine learning', 'artificial intelligence']
        def is_ai_ml(row):
            text = f"{row.get('Description', '')} {row.get('Keywords', '')}".lower()
            return any(kw.lower() in text for kw in ai_keywords)

        company_df['is_ai_ml'] = company_df.apply(is_ai_ml, axis=1)
        ai_ml_df = company_df[company_df['is_ai_ml']].copy()

        # Calculate vagueness based on LIWC certitude approach
        # Certitude words indicate clarity, specificity, certainty
        certitude_words = [
            # Absolute/totality words
            'always', 'never', 'all', 'none', 'every', 'completely', 'entirely',
            'totally', 'absolutely', 'full', 'whole', 'total', 'entire',
            # Certainty markers
            'definitely', 'certainly', 'obviously', 'clearly', 'surely',
            'indeed', 'undoubtedly', 'of course', 'without doubt',
            # Specific determiners and precision
            'specifically', 'precisely', 'exactly', 'particular', 'definite',
            'explicit', 'concrete', 'actual', 'real', 'true', 'certain',
            # Modal certainty
            'must', 'will', 'shall', 'have to',
            # Other clarity markers
            'basic', 'fundamental', 'essential', 'critical', 'key',
            'not only', 'in fact', 'guarantee', 'proven', 'established'
        ]
        
        def calc_vagueness(desc):
            """Calculate vagueness as 100 - certitude percentage"""
            if pd.isna(desc) or len(str(desc).strip()) == 0:
                return 50  # neutral for missing
            
            text = str(desc).lower()
            words = text.split()
            
            if len(words) == 0:
                return 50
            
            # Count certitude words
            certitude_count = sum(1 for word in words if word in certitude_words)
            
            # Also check multi-word phrases
            for phrase in ['of course', 'not only', 'without doubt', 'in fact', 'have to']:
                certitude_count += text.count(phrase)
            
            # Certitude score = percentage of certitude words
            certitude_score = (certitude_count / len(words)) * 100
            
            # Vagueness = 100 - certitude (higher = more vague)
            vagueness = 100 - certitude_score
            
            return max(0, min(100, vagueness))

        ai_ml_df['vagueness'] = ai_ml_df['Description'].apply(calc_vagueness)

        # Classify integration cost
        def calc_integration_cost(row):
            text = f"{row.get('Keywords', '')} {row.get('Description', '')}".lower()
            high_i = any(w in text for w in ['chip', 'hardware', 'robotics', 'gpu'])
            low_i = any(w in text for w in ['api', 'saas', 'software', 'cloud'])
            return 1 if high_i and not low_i else 0

        ai_ml_df['high_integration_cost'] = ai_ml_df.apply(calc_integration_cost, axis=1)

        # Convert to xarray - store each column separately to handle mixed types
        # This allows viewing all data in one Dataset while avoiding dtype issues
        ai_ml_df = ai_ml_df.set_index('CompanyID')

        # Store each column as separate DataArray (handles mixed str/int/float types)
        for col in ai_ml_df.columns:
            var_name = f'company_{col}'
            self.ds[var_name] = xr.DataArray(
                ai_ml_df[col].values,
                dims=['company'],
                coords={'company': ai_ml_df.index.values}
            )

        # Store row count for reference
        self.ds.attrs['n_companies'] = len(ai_ml_df)

        print(f"  ✅ Processed {len(ai_ml_df)} AI/ML companies")
        self.save_checkpoint(1, step_name)

    def step_02_process_deal_data(self, force=False):
        """
        Step 2: Process Deal data with specific date filtering
        Series A: 2021-01-01 to 2022-10-31
        Series B: 2023-05-01 to 2025-10-31
        Creates: ds['deal_data'] with dims (deal_id, variable)
        """
        step_name = "02_process_deal"

        if 'deal_data' in self.ds and not force:
            print(f"⏭️  Step 2: Skipping (already completed)")
            return

        print(f"▶️  Step 2: Processing deal data...")

        # Read Deal2023.dat
        deal_file = "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Front/On/strategic ambiguity/empirics/data/raw/Deal20230501.dat"
        
        # Read with sample_size for POC
        if self.sample_size:
            print(f"  🔬 Reading first {self.sample_size} rows for POC...")
            deal_df = pd.read_csv(deal_file, sep='|', low_memory=False, nrows=self.sample_size)
        else:
            deal_df = pd.read_csv(deal_file, sep='|', low_memory=False)
        print(f"  ✓ Loaded {len(deal_df)} rows")
        
        # Debug: Show column names
        print(f"\n  📊 Available columns: {', '.join(deal_df.columns[:10])}...")
        
        # Debug: Check what DealType values exist
        if 'DealType' in deal_df.columns:
            print(f"\n  📊 DealType value counts:")
            print(deal_df['DealType'].value_counts().head(10))
        
        # Filter to VC deals - use flexible matching
        vc_deals = deal_df[deal_df['DealType'].str.contains('VC', case=False, na=False)].copy()
        print(f"\n  ✓ Found {len(vc_deals)} VC deals")
        
        if len(vc_deals) == 0:
            print(f"  ⚠️  No VC deals found, using all deals")
            vc_deals = deal_df.copy()
        
        # Debug: Check VCRound column
        if 'VCRound' in vc_deals.columns:
            print(f"\n  📊 VCRound value counts:")
            print(vc_deals['VCRound'].value_counts().head(10))

        # Convert DealDate to datetime for filtering
        vc_deals['DealDate'] = pd.to_datetime(vc_deals['DealDate'], errors='coerce')
        
        # Filter by date ranges
        # Series A: 2021-01-01 to 2022-10-31
        # Series B: 2023-05-01 to 2025-10-31
        series_a = vc_deals[
            (vc_deals['DealDate'] >= '2021-01-01') & 
            (vc_deals['DealDate'] <= '2022-10-31')
        ].copy()
        
        series_b = vc_deals[
            (vc_deals['DealDate'] >= '2023-05-01') & 
            (vc_deals['DealDate'] <= '2025-10-31')
        ].copy()
        
        print(f"\n  ✓ Series A deals (2021-01-01 to 2022-10-31): {len(series_a)}")
        print(f"  ✓ Series B deals (2023-05-01 to 2025-10-31): {len(series_b)}")
        
        # Additional filtering by round type if available
        if 'VCRound' in vc_deals.columns:
            early_rounds = ['1st Round', 'Seed Round', 'Angel', 'Series A']
            later_rounds = ['2nd Round', '3rd Round', '4th Round', 'Series B', 'Later Stage VC']
            
            # Apply round filters to respective date ranges
            series_a = series_a[series_a['VCRound'].isin(early_rounds) | series_a['VCRound'].isna()]
            series_b = series_b[series_b['VCRound'].isin(later_rounds) | series_b['VCRound'].isna()]
            
            print(f"  ✓ After round filtering: Series A={len(series_a)}, Series B={len(series_b)}")

        # Add round label
        series_a['round'] = 'Series A'
        series_b['round'] = 'Series B'

        # Combine
        if len(series_a) > 0 or len(series_b) > 0:
            deal_panel = pd.concat([series_a, series_b], ignore_index=True)
        else:
            print(f"\n  ⚠️  WARNING: No deals found after filtering!")
            print(f"  💡 TIP: Check if date ranges contain data")
            print(f"  ⏭️  Creating minimal dummy data to continue pipeline")
            # Create dummy data
            deal_panel = pd.DataFrame({
                'CompanyID': ['DUMMY001'],
                'DealSize': [1000000],
                'DealStatus': ['Completed'],
                'round': ['Series A'],
                'VCRound': ['Series A'],
                'DealType': ['Early Stage VC'],
                'DealDate': [pd.Timestamp('2021-06-01')]
            })

        # Create funding success variable
        deal_panel['DealSize'] = pd.to_numeric(deal_panel['DealSize'], errors='coerce').fillna(0)
        deal_panel['funding_success'] = (
            (deal_panel['DealSize'] > 0) &
            (deal_panel['DealStatus'].str.contains('Completed', case=False, na=False))
        ).astype(int)

        # Convert to xarray - store each column separately
        deal_panel['deal_id'] = range(len(deal_panel))
        deal_panel = deal_panel.set_index('deal_id')

        # Store each column as separate DataArray
        for col in deal_panel.columns:
            var_name = f'deal_{col}'
            self.ds[var_name] = xr.DataArray(
                deal_panel[col].values,
                dims=['deal'],
                coords={'deal': deal_panel.index.values}
            )

        self.ds.attrs['n_deals'] = len(deal_panel)
        self.ds.attrs['series_a_date_range'] = '2021-01-01 to 2022-10-31'
        self.ds.attrs['series_b_date_range'] = '2023-05-01 to 2025-10-31'

        print(f"  ✅ Processed {len(deal_panel)} deals")
        self.save_checkpoint(2, step_name)

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

        # Convert xarray variables back to pandas DataFrames
        company_cols = [v for v in self.ds.data_vars if v.startswith('company_')]
        deal_cols = [v for v in self.ds.data_vars if v.startswith('deal_')]

        company_data = {}
        for col in company_cols:
            col_name = col.replace('company_', '')
            company_data[col_name] = self.ds[col].values

        company_df = pd.DataFrame(company_data, index=self.ds['company'].values)

        deal_data = {}
        for col in deal_cols:
            col_name = col.replace('deal_', '')
            deal_data[col_name] = self.ds[col].values

        deal_df = pd.DataFrame(deal_data, index=self.ds['deal'].values)
        
        # Debug: Check CompanyID overlap
        print(f"\n  📊 Company data: {len(company_df)} companies")
        print(f"  📊 Deal data: {len(deal_df)} deals")
        
        if len(company_df) > 0:
            print(f"\n  🔍 Sample Company IDs: {list(company_df.index[:5])}")
        
        if len(deal_df) > 0 and 'CompanyID' in deal_df.columns:
            print(f"  🔍 Sample Deal CompanyIDs: {list(deal_df['CompanyID'].head(5))}")
            
            # Check overlap
            company_ids = set(company_df.index)
            deal_company_ids = set(deal_df['CompanyID'].dropna())
            overlap = company_ids.intersection(deal_company_ids)
            
            print(f"\n  🎯 CompanyID overlap: {len(overlap)} companies have both company and deal data")
            if len(overlap) > 0:
                print(f"     Sample overlapping IDs: {list(overlap)[:5]}")
            else:
                print(f"  ⚠️  WARNING: No overlapping CompanyIDs found!")
                print(f"  💡 TIP: Company and Deal data may be from different sources or time periods")

        # Merge on CompanyID
        panel = deal_df.merge(
            company_df,
            left_on='CompanyID',
            right_index=True,
            how='inner',
            suffixes=('_deal', '_company')
        )

        # Add derived variables
        panel['series_b_dummy'] = (panel['round'] == 'Series B').astype(int)
        panel['observation_id'] = range(len(panel))
        panel = panel.set_index('observation_id')

        # Store panel data (each column separately)
        for col in panel.columns:
            var_name = f'panel_{col}'
            self.ds[var_name] = xr.DataArray(
                panel[col].values,
                dims=['observation'],
                coords={'observation': panel.index.values}
            )

        self.ds.attrs['n_observations'] = len(panel)

        print(f"  ✅ Created panel with {len(panel)} observations")
        self.save_checkpoint(3, step_name)

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

        # Convert panel variables back to pandas DataFrame
        panel_cols = [v for v in self.ds.data_vars if v.startswith('panel_')]
        panel_data = {}
        for col in panel_cols:
            col_name = col.replace('panel_', '')
            panel_data[col_name] = self.ds[col].values

        panel_df = pd.DataFrame(panel_data, index=self.ds['observation'].values)
        
        # Check if we have data
        if len(panel_df) == 0:
            print(f"\n  ⚠️  ERROR: No panel data available for analysis!")
            print(f"  💡 TIP: Check step 2 and 3 - there may be no matching deals")
            print(f"  ⏭️  Skipping analysis step")
            return
        
        print(f"\n  ✓ Panel has {len(panel_df)} observations")

        # Prepare for regression
        panel_df['vagueness_scaled'] = panel_df['vagueness'] / 100

        # Normalize column names (handle case sensitivity)
        panel_df.columns = [col.lower() for col in panel_df.columns]

        # Check if required columns exist, otherwise use simplified formula
        required_cols = ['log_series_a_amount', 'employees']
        available_cols = [col for col in required_cols if col in panel_df.columns]

        # Run regressions
        import statsmodels.formula.api as smf

        # Model 1: Two-way interaction
        if available_cols:
            controls = ' + '.join(available_cols)
            model1_formula = f"""
                funding_success ~ vagueness_scaled + series_b_dummy +
                                  vagueness_scaled:series_b_dummy + {controls}
            """
        else:
            model1_formula = """
                funding_success ~ vagueness_scaled + series_b_dummy +
                                  vagueness_scaled:series_b_dummy
            """

        try:
            model1 = smf.logit(model1_formula, data=panel_df).fit(disp=False)
        except:
            print("  ⚠️  Logit failed, using OLS")
            model1 = smf.ols(model1_formula, data=panel_df).fit()

        # Model 2: Three-way interaction
        if available_cols:
            controls = ' + '.join(available_cols)
            model2_formula = f"""
                funding_success ~ vagueness_scaled + series_b_dummy + high_integration_cost +
                                  vagueness_scaled:series_b_dummy +
                                  vagueness_scaled:high_integration_cost +
                                  series_b_dummy:high_integration_cost +
                                  vagueness_scaled:series_b_dummy:high_integration_cost + {controls}
            """
        else:
            model2_formula = """
                funding_success ~ vagueness_scaled + series_b_dummy + high_integration_cost +
                                  vagueness_scaled:series_b_dummy +
                                  vagueness_scaled:high_integration_cost +
                                  series_b_dummy:high_integration_cost +
                                  vagueness_scaled:series_b_dummy:high_integration_cost
            """

        try:
            model2 = smf.logit(model2_formula, data=panel_df).fit(disp=False)
        except:
            print("  ⚠️  Logit failed, using OLS")
            model2 = smf.ols(model2_formula, data=panel_df).fit()

        # Store results as pickled object
        results = {
            'model1_params': model1.params.to_dict(),
            'model1_pvalues': model1.pvalues.to_dict(),
            'model1_summary': str(model1.summary()),
            'model2_params': model2.params.to_dict(),
            'model2_pvalues': model2.pvalues.to_dict(),
            'model2_summary': str(model2.summary())
        }

        with open(self.output_dir / 'model_results.pkl', 'wb') as f:
            pickle.dump(results, f)

        # Save as CSV tables
        model1_results = pd.DataFrame({
            'Variable': model1.params.index,
            'Coefficient': model1.params.values,
            'p-value': model1.pvalues.values,
        })
        model1_results.to_csv(self.output_dir / 'table2_model1.csv', index=False)

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
        Step 5: Create figures and tables
        """
        step_name = "05_create_deliverables"

        if self.ds.attrs.get('deliverables_created') and not force:
            print(f"⏭️  Step 5: Skipping (already completed)")
            return

        print(f"▶️  Step 5: Creating deliverables...")

        # Convert panel variables back to pandas DataFrame
        panel_cols = [v for v in self.ds.data_vars if v.startswith('panel_')]
        panel_data = {}
        for col in panel_cols:
            col_name = col.replace('panel_', '')
            panel_data[col_name] = self.ds[col].values

        panel_df = pd.DataFrame(panel_data, index=self.ds['observation'].values)

        # Import plotting libraries
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import seaborn as sns

        sns.set_style("whitegrid")

        # Normalize column names
        panel_df.columns = [col.lower() for col in panel_df.columns]

        # Table 1: Descriptive statistics
        print("\n  Creating Table 1: Descriptive statistics")
        # Use only available columns
        desc_vars_candidates = ['vagueness', 'high_integration_cost', 'funding_success',
                                 'dealsize', 'employees', 'totalraised']
        desc_vars = [v for v in desc_vars_candidates if v in panel_df.columns]

        if desc_vars:
            desc_stats = panel_df[desc_vars].describe().T
            desc_stats['median'] = panel_df[desc_vars].median()
            desc_stats = desc_stats[['count', 'mean', 'median', 'std', 'min', 'max']]
            desc_stats.to_csv(self.output_dir / 'table1_descriptives.csv')
            print(f"    ✅ Saved table1_descriptives.csv")
        else:
            print(f"    ⚠️  Skipped table1 (no numeric columns found)")

        # Table 3: Success rates by sector
        print("\n  Creating Table 3: Success rates")
        required_for_table3 = ['vagueness_category', 'round', 'integration_cost_label', 'funding_success']
        if all(col in panel_df.columns for col in required_for_table3):
            success_rates = panel_df.groupby(['vagueness_category', 'round', 'integration_cost_label']).agg({
                'funding_success': ['count', 'sum', 'mean']
            }).round(3)
            success_rates.columns = ['N', 'Successes', 'Success_Rate']
            success_rates = success_rates.reset_index()
            success_pivot = success_rates.pivot_table(
                index=['integration_cost_label', 'vagueness_category'],
                columns='round',
                values='Success_Rate'
            )
            success_pivot.to_csv(self.output_dir / 'table3_success_rates.csv')
            print(f"    ✅ Saved table3_success_rates.csv")
        else:
            print(f"    ⚠️  Skipped table3 (missing required columns)")

        # Figure 1: Reversal pattern bars
        print("\n  Creating Figure 1: Reversal bars")
        if all(col in panel_df.columns for col in ['vagueness_category', 'round', 'funding_success']):
            fig, ax = plt.subplots(figsize=(12, 7))
            success_by_vague_round = panel_df.groupby(['vagueness_category', 'round'])['funding_success'].mean().unstack()

            x = np.arange(len(success_by_vague_round.index))
            width = 0.35

            bars1 = ax.bar(x - width/2, success_by_vague_round['Series A'], width,
                           label='Series A', color='steelblue', alpha=0.8)
            bars2 = ax.bar(x + width/2, success_by_vague_round['Series B'], width,
                           label='Series B', color='coral', alpha=0.8)

            ax.set_xlabel('Promise Type', fontsize=13, fontweight='bold')
            ax.set_ylabel('Funding Success Rate', fontsize=13, fontweight='bold')
            ax.set_title('Funding Success Reversal', fontsize=14, fontweight='bold')
            ax.set_xticks(x)
            ax.set_xticklabels(success_by_vague_round.index)
            ax.legend(fontsize=11)
            ax.set_ylim(0, 1.1)
            ax.grid(axis='y', alpha=0.3)

            for bars in [bars1, bars2]:
                for bar in bars:
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height,
                            f'{height:.1%}', ha='center', va='bottom', fontsize=10)

            plt.tight_layout()
            plt.savefig(self.output_dir / 'figure1_reversal_bars.png', dpi=300)
            plt.close()
            print(f"    ✅ Saved figure1_reversal_bars.png")
        else:
            print(f"    ⚠️  Skipped figure1 (missing required columns)")

        # Figure 2: Vagueness curves
        print("\n  Creating Figure 2: Vagueness curves")
        if all(col in panel_df.columns for col in ['vagueness', 'round', 'funding_success']):
            fig, ax = plt.subplots(figsize=(12, 7))

            panel_df['vagueness_bin'] = pd.cut(panel_df['vagueness'], bins=[0, 30, 50, 70, 100],
                                                 labels=['0-30', '30-50', '50-70', '70-100'])
            vague_curves = panel_df.groupby(['vagueness_bin', 'round'])['funding_success'].mean().unstack()

            for col in vague_curves.columns:
                ax.plot(range(len(vague_curves.index)), vague_curves[col],
                        marker='o', linewidth=2.5, markersize=8, label=col, alpha=0.8)

            ax.set_xlabel('Vagueness Level', fontsize=13, fontweight='bold')
            ax.set_ylabel('Funding Success Rate', fontsize=13, fontweight='bold')
            ax.set_title('How Vagueness Affects Funding Success', fontsize=14, fontweight='bold')
            ax.set_xticks(range(len(vague_curves.index)))
            ax.set_xticklabels(vague_curves.index)
            ax.legend(fontsize=11, title='Round')
            ax.grid(alpha=0.3)
            ax.set_ylim(0, 1.1)

            plt.tight_layout()
            plt.savefig(self.output_dir / 'figure2_vagueness_curves.png', dpi=300)
            plt.close()
            print(f"    ✅ Saved figure2_vagueness_curves.png")
        else:
            print(f"    ⚠️  Skipped figure2 (missing required columns)")

        self.ds.attrs['deliverables_created'] = 1  # Use int instead of bool for NetCDF compatibility
        self.ds.attrs['deliverables_path'] = str(self.output_dir)

        print(f"\n  ✅ All deliverables created")
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
    parser.add_argument('--sample', type=int, default=None,
                        help='POC mode: Use only first N rows of data (e.g., --sample 1000)')

    args = parser.parse_args()

    # Initialize pipeline with sample_size
    pipeline = PitchbookPipeline(sample_size=args.sample)

    if args.summary:
        pipeline.get_summary()
    else:
        pipeline.run_pipeline(start_from=args.start_from, force_rerun=args.force)
