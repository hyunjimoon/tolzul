"""
Hybrid Pipeline: xarray for checkpointing + parquet for data storage
Best of both worlds for real Pitchbook data (94+ columns)

Structure:
    checkpoint.nc (lightweight xarray)
        - Step completion status
        - Row counts
        - Timestamps
        - File paths

    data files (efficient formats)
        - company_master.parquet (94 columns, compressed)
        - deal_panel.parquet (97 columns, compressed)
        - analysis_panel.parquet (merged data)
"""

import xarray as xr
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime

class PitchbookPipelineHybrid:
    """
    Hybrid pipeline: xarray checkpoint + parquet data storage
    Optimized for real Pitchbook format (94+ columns)
    """

    def __init__(self, data_dir="data", output_dir="output"):
        self.data_dir = Path(data_dir)
        self.output_dir = Path(output_dir)
        self.processed_dir = self.data_dir / "processed"

        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)

        self.checkpoint_file = self.output_dir / "checkpoint.nc"

        # Load or create checkpoint
        if self.checkpoint_file.exists():
            print(f"📂 Loading checkpoint: {self.checkpoint_file}")
            self.checkpoint = xr.open_dataset(self.checkpoint_file)
        else:
            print("🆕 Creating new checkpoint")
            self.checkpoint = self._init_checkpoint()

    def _init_checkpoint(self):
        """Initialize lightweight checkpoint (no data, just status)"""
        return xr.Dataset(
            attrs={
                'pipeline_version': '2.0_hybrid',
                'created_at': datetime.now().isoformat(),
                'last_updated': datetime.now().isoformat(),
                'data_format': 'parquet',
                # Initialize all steps as pending (NetCDF doesn't support nested dicts)
                'step_01_status': 'pending',
                'step_02_status': 'pending',
                'step_03_status': 'pending',
                'step_04_status': 'pending',
                'step_05_status': 'pending',
            }
        )

    def _update_checkpoint(self, step_num, step_name, output_file, row_count):
        """Update checkpoint with step completion"""
        self.checkpoint.attrs['last_updated'] = datetime.now().isoformat()
        self.checkpoint.attrs[f'step_{step_num:02d}_status'] = 'completed'
        self.checkpoint.attrs[f'step_{step_num:02d}_output'] = str(output_file)
        self.checkpoint.attrs[f'step_{step_num:02d}_rows'] = int(row_count)
        self.checkpoint.attrs[f'step_{step_num:02d}_timestamp'] = datetime.now().isoformat()
        self.checkpoint.to_netcdf(self.checkpoint_file)
        print(f"💾 Checkpoint updated: {step_name}")

    def _is_step_completed(self, step_num):
        """Check if step is already completed"""
        key = f'step_{step_num:02d}_status'
        return self.checkpoint.attrs.get(key) == 'completed'

    def step_01_process_company_data(self, force=False):
        """
        Step 1: Process Company data (ALL 94 columns)
        Output: company_master.parquet
        """
        if not force and self._is_step_completed(1):
            print("⏭️  Step 1: Already completed (use --force to rerun)")
            return

        print("▶️  Step 1: Processing company data (94 columns)...")

        # Read ALL columns from raw data
        company_files = list((self.data_dir / "raw").glob("Company*.dat"))
        dfs = []
        for f in company_files:
            df = pd.read_csv(f, sep='|', low_memory=False, encoding='utf-8')
            dfs.append(df)
            print(f"  Read {f.name}: {len(df)} rows, {len(df.columns)} columns")

        company_df = pd.concat(dfs, ignore_index=True)
        print(f"  Total: {len(company_df)} companies, {len(company_df.columns)} columns")

        # Filter AI/ML firms
        ai_keywords = ['AI', 'ML', 'machine learning', 'artificial intelligence',
                       'neural', 'deep learning', 'NLP', 'GPT', 'language model']

        def is_ai_ml(row):
            text = f"{row.get('Description', '')} {row.get('Keywords', '')}".lower()
            return any(kw.lower() in text for kw in ai_keywords)

        company_df['is_ai_ml'] = company_df.apply(is_ai_ml, axis=1)
        ai_ml_df = company_df[company_df['is_ai_ml']].copy()
        print(f"  AI/ML firms: {len(ai_ml_df)}")

        # Calculate vagueness (add new column to existing 94)
        vague_kw = ['approximately', 'around', 'roughly', 'flexible', 'scalable',
                    'adaptive', 'designed to', 'enables']
        precise_kw = ['precisely', 'exactly', 'guaranteed', 'specific', 'certified',
                      'proprietary', 'advanced']

        def calc_vagueness(desc):
            if pd.isna(desc):
                return 50
            text = str(desc).lower()
            vague = sum(text.count(w) for w in vague_kw)
            precise = sum(text.count(w) for w in precise_kw)
            return max(0, min(100, 50 + 10 * (vague - precise)))

        ai_ml_df['vagueness'] = ai_ml_df['Description'].apply(calc_vagueness)

        # Calculate integration cost
        high_i_kw = ['chip', 'asic', 'robotics', 'gpu', 'hardware', 'semiconductor']
        low_i_kw = ['api', 'saas', 'software', 'cloud', 'platform']

        def calc_int_cost(row):
            text = f"{row.get('Keywords', '')} {row.get('Description', '')}".lower()
            high = any(w in text for w in high_i_kw)
            low = any(w in text for w in low_i_kw)
            return 1 if high and not low else 0

        ai_ml_df['high_integration_cost'] = ai_ml_df.apply(calc_int_cost, axis=1)

        # Save to parquet (efficient for 94+ columns)
        output_file = self.processed_dir / "company_master.parquet"
        ai_ml_df.to_parquet(output_file, compression='snappy', index=False)
        print(f"  ✅ Saved: {output_file} ({len(ai_ml_df)} rows)")

        # Update checkpoint
        self._update_checkpoint(1, 'process_company', output_file, len(ai_ml_df))

    def step_02_process_deal_data(self, force=False):
        """
        Step 2: Process Deal data (ALL 97 columns)
        Output: deal_panel.parquet
        """
        if not force and self._is_step_completed(2):
            print("⏭️  Step 2: Already completed")
            return

        print("▶️  Step 2: Processing deal data (97 columns)...")

        # Read ALL columns
        deal_files = list((self.data_dir / "raw").glob("Deal*.dat"))
        dfs = []
        for f in deal_files:
            df = pd.read_csv(f, sep='|', low_memory=False, encoding='utf-8')
            dfs.append(df)
            print(f"  Read {f.name}: {len(df)} rows, {len(df.columns)} columns")

        deal_df = pd.concat(dfs, ignore_index=True)
        print(f"  Total: {len(deal_df)} deals, {len(deal_df.columns)} columns")

        # Filter VC deals
        vc_deals = deal_df[deal_df['DealType'].isin(['Early Stage VC', 'Later Stage VC'])].copy()
        print(f"  VC deals: {len(vc_deals)}")

        # Identify Series A/B
        vc_deals['DealDate'] = pd.to_datetime(vc_deals['DealDate'], errors='coerce')

        series_a = vc_deals[vc_deals['VCRound'].str.contains('Series A', case=False, na=False)].copy()
        series_b = vc_deals[vc_deals['VCRound'].str.contains('Series B', case=False, na=False)].copy()

        series_a['round'] = 'Series A'
        series_b['round'] = 'Series B'

        # Funding success
        series_a['DealSize'] = pd.to_numeric(series_a['DealSize'], errors='coerce').fillna(0)
        series_b['DealSize'] = pd.to_numeric(series_b['DealSize'], errors='coerce').fillna(0)

        series_a['funding_success'] = (
            (series_a['DealSize'] > 0) &
            (series_a['DealStatus'].str.contains('Completed', case=False, na=False))
        ).astype(int)

        series_b['funding_success'] = (
            (series_b['DealSize'] > 0) &
            (series_b['DealStatus'].str.contains('Completed', case=False, na=False))
        ).astype(int)

        # Combine
        deal_panel = pd.concat([series_a, series_b], ignore_index=True)
        print(f"  Series A: {len(series_a)}, Series B: {len(series_b)}")

        # Save to parquet
        output_file = self.processed_dir / "deal_panel.parquet"
        deal_panel.to_parquet(output_file, compression='snappy', index=False)
        print(f"  ✅ Saved: {output_file} ({len(deal_panel)} rows)")

        self._update_checkpoint(2, 'process_deal', output_file, len(deal_panel))

    def step_03_create_panel(self, force=False):
        """
        Step 3: Create analysis panel
        Output: analysis_panel.parquet
        """
        if not force and self._is_step_completed(3):
            print("⏭️  Step 3: Already completed")
            return

        print("▶️  Step 3: Creating analysis panel...")

        # Load from parquet (fast!)
        company_df = pd.read_parquet(self.processed_dir / "company_master.parquet")
        deal_df = pd.read_parquet(self.processed_dir / "deal_panel.parquet")

        print(f"  Company: {len(company_df)} firms")
        print(f"  Deal: {len(deal_df)} deals")

        # Merge on CompanyID
        panel = deal_df.merge(
            company_df,
            on='CompanyID',
            how='inner',
            suffixes=('_deal', '_company')
        )

        print(f"  Merged: {len(panel)} observations")

        # Add derived variables
        panel['series_b_dummy'] = (panel['round'] == 'Series B').astype(int)

        # Save
        output_file = self.processed_dir / "analysis_panel.parquet"
        panel.to_parquet(output_file, compression='snappy', index=False)
        print(f"  ✅ Saved: {output_file}")

        self._update_checkpoint(3, 'create_panel', output_file, len(panel))

    def step_04_run_analysis(self, force=False):
        """
        Step 4: Run regression analysis
        Output: table2_model1.csv, table4_model2.csv
        """
        if not force and self._is_step_completed(4):
            print("⏭️  Step 4: Already completed")
            return

        print("▶️  Step 4: Running regression analysis...")

        # Load analysis panel
        panel = pd.read_parquet(self.processed_dir / "analysis_panel.parquet")
        print(f"  Loaded: {len(panel)} observations")

        # Import statsmodels
        import statsmodels.formula.api as smf

        # Prepare variables
        panel['vagueness_scaled'] = panel['vagueness'] / 100

        # Model 1: Vagueness × SeriesB interaction
        print("\n  Model 1: Vagueness × Series B interaction")
        model1_formula = """
            funding_success ~ vagueness_scaled + series_b_dummy +
                              vagueness_scaled:series_b_dummy +
                              log_series_a_amount + employees
        """

        try:
            model1 = smf.logit(model1_formula, data=panel).fit(disp=False)
            model1_results = pd.DataFrame({
                'Variable': model1.params.index,
                'Coefficient': model1.params.values,
                'Std Error': model1.bse.values,
                'z-value': model1.tvalues.values,
                'p-value': model1.pvalues.values,
            })
            output_file1 = self.output_dir / "table2_model1.csv"
            model1_results.to_csv(output_file1, index=False)
            print(f"    ✅ Saved: {output_file1}")
        except Exception as e:
            print(f"    ⚠️  Logit failed, using OLS: {e}")
            model1 = smf.ols(model1_formula, data=panel).fit()
            model1_results = pd.DataFrame({
                'Variable': model1.params.index,
                'Coefficient': model1.params.values,
                'Std Error': model1.bse.values,
                't-value': model1.tvalues.values,
                'p-value': model1.pvalues.values,
            })
            output_file1 = self.output_dir / "table2_model1.csv"
            model1_results.to_csv(output_file1, index=False)
            print(f"    ✅ Saved (OLS): {output_file1}")

        # Model 2: Three-way interaction
        print("\n  Model 2: Three-way interaction")
        model2_formula = """
            funding_success ~ vagueness_scaled + series_b_dummy + high_integration_cost +
                              vagueness_scaled:series_b_dummy +
                              vagueness_scaled:high_integration_cost +
                              series_b_dummy:high_integration_cost +
                              vagueness_scaled:series_b_dummy:high_integration_cost +
                              log_series_a_amount + employees
        """

        try:
            model2 = smf.logit(model2_formula, data=panel).fit(disp=False)
            model2_results = pd.DataFrame({
                'Variable': model2.params.index,
                'Coefficient': model2.params.values,
                'Std Error': model2.bse.values,
                'z-value': model2.tvalues.values,
                'p-value': model2.pvalues.values,
            })
            output_file2 = self.output_dir / "table4_model2.csv"
            model2_results.to_csv(output_file2, index=False)
            print(f"    ✅ Saved: {output_file2}")
        except Exception as e:
            print(f"    ⚠️  Logit failed, using OLS: {e}")
            model2 = smf.ols(model2_formula, data=panel).fit()
            model2_results = pd.DataFrame({
                'Variable': model2.params.index,
                'Coefficient': model2.params.values,
                'Std Error': model2.bse.values,
                't-value': model2.tvalues.values,
                'p-value': model2.pvalues.values,
            })
            output_file2 = self.output_dir / "table4_model2.csv"
            model2_results.to_csv(output_file2, index=False)
            print(f"    ✅ Saved (OLS): {output_file2}")

        self._update_checkpoint(4, 'run_analysis', output_file2, len(panel))

    def step_05_create_deliverables(self, force=False):
        """
        Step 5: Create deliverables (tables and figures)
        Output: table1_descriptives.csv, table3_success_rates.csv, 4 figures
        """
        if not force and self._is_step_completed(5):
            print("⏭️  Step 5: Already completed")
            return

        print("▶️  Step 5: Creating deliverables...")

        # Load analysis panel
        panel = pd.read_parquet(self.processed_dir / "analysis_panel.parquet")
        print(f"  Loaded: {len(panel)} observations")

        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import seaborn as sns

        sns.set_style("whitegrid")

        # Table 1: Descriptive statistics
        print("\n  Creating Table 1: Descriptive statistics")
        desc_vars = ['vagueness', 'high_integration_cost', 'funding_success',
                     'deal_size', 'employees', 'total_raised']
        desc_stats = panel[desc_vars].describe().T
        desc_stats['median'] = panel[desc_vars].median()
        desc_stats = desc_stats[['count', 'mean', 'median', 'std', 'min', 'max']]

        output_file1 = self.output_dir / "table1_descriptives.csv"
        desc_stats.to_csv(output_file1)
        print(f"    ✅ Saved: {output_file1}")

        # Table 3: Success rates
        print("\n  Creating Table 3: Success rates by sector")
        success_rates = panel.groupby(['vagueness_category', 'round', 'integration_cost_label']).agg({
            'funding_success': ['count', 'sum', 'mean']
        }).round(3)
        success_rates.columns = ['N', 'Successes', 'Success_Rate']
        success_rates = success_rates.reset_index()

        success_pivot = success_rates.pivot_table(
            index=['integration_cost_label', 'vagueness_category'],
            columns='round',
            values='Success_Rate'
        )

        output_file3 = self.output_dir / "table3_success_rates.csv"
        success_pivot.to_csv(output_file3)
        print(f"    ✅ Saved: {output_file3}")

        # Figure 1: Reversal bars
        print("\n  Creating Figure 1: Reversal pattern")
        fig, ax = plt.subplots(figsize=(12, 7))
        success_by_vague_round = panel.groupby(['vagueness_category', 'round'])['funding_success'].mean().unstack()

        x = np.arange(len(success_by_vague_round.index))
        width = 0.35

        bars1 = ax.bar(x - width/2, success_by_vague_round['Series A'], width,
                       label='Series A', color='steelblue', alpha=0.8)
        bars2 = ax.bar(x + width/2, success_by_vague_round['Series B'], width,
                       label='Series B', color='coral', alpha=0.8)

        ax.set_xlabel('Promise Type', fontsize=13, fontweight='bold')
        ax.set_ylabel('Funding Success Rate', fontsize=13, fontweight='bold')
        ax.set_title('Funding Success Reversal: Precise vs. Vague Promises',
                     fontsize=14, fontweight='bold')
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
        fig1_file = self.output_dir / "figure1_reversal_bars.png"
        plt.savefig(fig1_file, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"    ✅ Saved: {fig1_file}")

        # Figure 2: Vagueness curves
        print("\n  Creating Figure 2: Success curves by vagueness")
        fig, ax = plt.subplots(figsize=(12, 7))

        panel['vagueness_bin'] = pd.cut(panel['vagueness'], bins=[0, 30, 50, 70, 100],
                                         labels=['0-30', '30-50', '50-70', '70-100'])
        vague_curves = panel.groupby(['vagueness_bin', 'round'])['funding_success'].mean().unstack()

        for col in vague_curves.columns:
            ax.plot(range(len(vague_curves.index)), vague_curves[col],
                    marker='o', linewidth=2.5, markersize=8,
                    label=col, alpha=0.8)

        ax.set_xlabel('Vagueness Level', fontsize=13, fontweight='bold')
        ax.set_ylabel('Funding Success Rate', fontsize=13, fontweight='bold')
        ax.set_title('How Vagueness Affects Funding Success Across Rounds',
                     fontsize=14, fontweight='bold')
        ax.set_xticks(range(len(vague_curves.index)))
        ax.set_xticklabels(vague_curves.index)
        ax.legend(fontsize=11, title='Round')
        ax.grid(alpha=0.3)
        ax.set_ylim(0, 1.1)

        plt.tight_layout()
        fig2_file = self.output_dir / "figure2_vagueness_curves.png"
        plt.savefig(fig2_file, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"    ✅ Saved: {fig2_file}")

        print("\n  ✅ All deliverables created")
        self._update_checkpoint(5, 'create_deliverables', output_file3, len(panel))

    def get_summary(self):
        """Print pipeline status"""
        print("\n" + "=" * 80)
        print("PIPELINE STATUS (Hybrid: xarray checkpoint + parquet data)")
        print("=" * 80)
        print(f"\nCheckpoint: {self.checkpoint_file}")
        print(f"Data format: parquet (optimized for 94+ columns)")

        for i in range(1, 6):
            key = f'step_{i:02d}_status'
            status = self.checkpoint.attrs.get(key, 'pending')

            if status == 'completed':
                output_key = f'step_{i:02d}_output'
                rows_key = f'step_{i:02d}_rows'
                time_key = f'step_{i:02d}_timestamp'

                output = self.checkpoint.attrs.get(output_key, 'N/A')
                rows = self.checkpoint.attrs.get(rows_key, 'N/A')
                timestamp = self.checkpoint.attrs.get(time_key, 'N/A')

                print(f"\n✅ Step {i}: {status}")
                print(f"   Output: {output}")
                print(f"   Rows: {rows}")
                print(f"   Time: {timestamp}")
            else:
                print(f"\n⏸️  Step {i}: {status}")

    def run_pipeline(self, start_from=1, force=False):
        """Run pipeline from specific step"""
        steps = [
            self.step_01_process_company_data,
            self.step_02_process_deal_data,
            self.step_03_create_panel,
        ]

        print("=" * 80)
        print("PITCHBOOK PIPELINE (Hybrid: xarray + parquet)")
        print("=" * 80)

        for i, step_func in enumerate(steps, 1):
            if i < start_from:
                continue

            try:
                step_func(force=force)
            except Exception as e:
                print(f"\n❌ Error in step {i}")
                print(f"   {str(e)}")
                print(f"\n💡 Resume: python pipeline_hybrid.py --from {i}")
                import traceback
                traceback.print_exc()
                return False

        print("\n" + "=" * 80)
        print("🎉 PIPELINE COMPLETED")
        print("=" * 80)
        return True


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--from', dest='start_from', type=int, default=1)
    parser.add_argument('--force', action='store_true')
    parser.add_argument('--summary', action='store_true')

    args = parser.parse_args()

    pipeline = PitchbookPipelineHybrid()

    if args.summary:
        pipeline.get_summary()
    else:
        pipeline.run_pipeline(start_from=args.start_from, force=args.force)
