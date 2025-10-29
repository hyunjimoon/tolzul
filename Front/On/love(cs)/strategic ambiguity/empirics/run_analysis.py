# run_analysis.py
#!/usr/bin/env python3
"""
W1 Pipeline: H1 + H2 (minimal outputs)

Outputs:
  outputs/
    - h1_coefficients.csv
    - h2_main_coefficients.csv
    - h2_analysis_dataset.csv
"""

import pandas as pd
from pathlib import Path
import argparse, sys, warnings
warnings.filterwarnings('ignore')

# dual import (modules.* or local *)
sys.path.insert(0, str(Path(__file__).parent))
try:
    from modules.features import (
        engineer_features, compute_founder_credibility, extract_sector_fe,
        create_survival_seriesb_progression, preprocess_for_w1
    )
    from modules.models import (
        test_h1_early_funding, test_h2_main_survival
    )
except Exception:
    from features import (
        engineer_features, compute_founder_credibility, extract_sector_fe,
        create_survival_seriesb_progression, preprocess_for_w1
    )
    from models import (
        test_h1_early_funding, test_h2_main_survival
    )

def read_snapshot(path: Path, encoding='utf-8') -> pd.DataFrame:
    try:
        return pd.read_csv(path, sep='|', encoding=encoding, low_memory=False)
    except UnicodeDecodeError:
        return pd.read_csv(path, sep='|', encoding='latin-1', low_memory=False)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', type=str, default='outputs')
    args = ap.parse_args()
    out = Path(args.output); out.mkdir(parents=True, exist_ok=True)

    print("="*80); print("W1: Load snapshots"); print("="*80)
    data_dir = Path("data/raw")
    snaps = {
        't0':  data_dir / "Company20211201.dat",
        'tm1': data_dir / "Company20220101.dat",
        'tm2': data_dir / "Company20220501.dat",
        't1':  data_dir / "Company20230501.dat"
    }
    dfs = {k: read_snapshot(v) for k, v in snaps.items()}

    print("\n"+"="*80); print("Step 1: DV(growth) — Series B+ progression"); print("="*80)
    dv = create_survival_seriesb_progression(dfs['t0'], dfs['tm1'], dfs['tm2'], dfs['t1'])
    dv.rename(columns={'Y_primary':'growth'}, inplace=True)

    print("\n"+"="*80); print("Step 2: Features @ baseline"); print("="*80)
    base = engineer_features(dfs['t0'])
    base['founder_credibility'] = compute_founder_credibility(base)
    if 'sector_fe' not in base: base['sector_fe'] = extract_sector_fe(base.get('keywords', pd.Series([""]*len(base))))

    print("\n"+"="*80); print("Step 3: Merge + preprocess"); print("="*80)
    id_col = 'CompanyID' if 'CompanyID' in base.columns else 'company_id'
    ana = base.merge(dv.rename(columns={'company_id': id_col}), on=id_col, how='inner')
    ana = preprocess_for_w1(ana)
    # back-compat alias
    if 'survival' not in ana.columns: ana['survival'] = ana['growth']
    ana.to_csv(out / "h2_analysis_dataset.csv", index=False)
    print(f"✓ Saved: {out / 'h2_analysis_dataset.csv'}")

    print("\n"+"="*80); print("Step 4: H1 (OLS)"); print("="*80)
    h1 = test_h1_early_funding(ana)
    pd.DataFrame({
        'variable': h1.params.index,
        'coefficient': h1.params.values,
        'std_err': h1.bse.values,
        't': h1.tvalues.values,
        'p_value': h1.pvalues.values,
        'ci_lower': h1.conf_int()[0].values,
        'ci_upper': h1.conf_int()[1].values
    }).to_csv(out / "h1_coefficients.csv", index=False)
    print(f"✓ Saved: {out / 'h1_coefficients.csv'}")

    print("\n"+"="*80); print("Step 5: H2 Main (Logit)"); print("="*80)
    h2 = test_h2_main_survival(ana)  # wrapper → growth 사용
    pd.DataFrame({
        'variable': h2.params.index,
        'coefficient': h2.params.values,
        'std_err': h2.bse.values,
        'z': h2.tvalues.values,
        'p_value': h2.pvalues.values,
        'ci_lower': h2.conf_int()[0].values,
        'ci_upper': h2.conf_int()[1].values
    }).to_csv(out / "h2_main_coefficients.csv", index=False)
    print(f"✓ Saved: {out / 'h2_main_coefficients.csv'}")

    print("\n"+"="*80); print("✓ DONE (W1 minimal outputs)"); print("="*80)
    print(f"Outputs → {out}")

if __name__ == "__main__":
    main()
