#!/usr/bin/env python3
"""
Diagnostic Checks for Data Quality

Combines all diagnostic scripts:
- Snapshot checks (files exist, readable)
- Series A detection (regex patterns work)
- Deal type patterns
- Founder columns availability
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys


def check_snapshots(data_dir="data/raw"):
    """Check if all required snapshot files exist and are readable."""
    print("="*80)
    print("SNAPSHOT FILES CHECK")
    print("="*80)

    snapshots = {
        'Baseline (2021-12-01)': Path(data_dir) / "Company20211201.dat",
        'Mid 1 (2022-01-01)': Path(data_dir) / "Company20220101.dat",
        'Mid 2 (2022-05-01)': Path(data_dir) / "Company20220501.dat",
        'Endpoint (2023-05-01)': Path(data_dir) / "Company20230501.dat"
    }

    all_ok = True
    for name, path in snapshots.items():
        if path.exists():
            try:
                df = pd.read_csv(path, sep='|', encoding='utf-8', nrows=10)
                print(f"  ✓ {name}: {path.name} ({df.shape[1]} columns)")
            except Exception as e:
                print(f"  ✗ {name}: {path.name} - ERROR: {e}")
                all_ok = False
        else:
            print(f"  ✗ {name}: {path.name} - NOT FOUND")
            all_ok = False

    return all_ok


def check_series_a_detection(data_file="data/raw/Company20211201.dat"):
    """Check if Series A regex patterns work."""
    print("\n" + "="*80)
    print("SERIES A DETECTION CHECK")
    print("="*80)

    try:
        df = pd.read_csv(data_file, sep='|', encoding='utf-8', low_memory=False)

        if 'LastFinancingDealType' not in df.columns:
            print("  ✗ LastFinancingDealType column not found")
            return False

        # Patterns
        A_STAGE_PAT = r"(?:\bSeries\s*A(?:[-\s]?\d+|[A-Z])?\b|\bEarly[-\s]*Stage\s*VC\b)"
        B_PLUS_PAT = r"(?:\bLater[-\s]*Stage\s*VC\b|\bSeries\s*[B-G](?:[-\s]?\d+|[A-Z])?\b)"

        import re
        series_a = df['LastFinancingDealType'].str.contains(A_STAGE_PAT, case=False, na=False, regex=True)
        series_b_plus = df['LastFinancingDealType'].str.contains(B_PLUS_PAT, case=False, na=False, regex=True)

        print(f"  ✓ Total companies: {len(df):,}")
        print(f"  ✓ Series A detected: {series_a.sum():,} ({series_a.mean():.1%})")
        print(f"  ✓ Series B+ detected: {series_b_plus.sum():,} ({series_b_plus.mean():.1%})")

        if series_a.sum() == 0:
            print("  ⚠️  WARNING: No Series A companies detected!")
            return False

        return True

    except Exception as e:
        print(f"  ✗ ERROR: {e}")
        return False


def check_deal_types(data_file="data/raw/Company20211201.dat", top_n=20):
    """Show most common deal types."""
    print("\n" + "="*80)
    print(f"DEAL TYPE PATTERNS (Top {top_n})")
    print("="*80)

    try:
        df = pd.read_csv(data_file, sep='|', encoding='utf-8', low_memory=False)

        if 'LastFinancingDealType' not in df.columns:
            print("  ✗ LastFinancingDealType column not found")
            return False

        deal_types = df['LastFinancingDealType'].value_counts().head(top_n)

        for deal_type, count in deal_types.items():
            pct = count / len(df) * 100
            print(f"  {deal_type:<40} {count:>8,} ({pct:>5.1f}%)")

        return True

    except Exception as e:
        print(f"  ✗ ERROR: {e}")
        return False


def check_founder_columns(data_file="data/raw/Company20211201.dat"):
    """Check availability of founder-related columns."""
    print("\n" + "="*80)
    print("FOUNDER COLUMNS CHECK")
    print("="*80)

    try:
        df = pd.read_csv(data_file, sep='|', encoding='utf-8', low_memory=False)

        founder_cols = [
            'PrimaryContactPBId',
            'PrimaryContactName',
            'PrimaryContactTitle',
            'TotalRaised',
            'YearFounded'
        ]

        print(f"  Total companies: {len(df):,}\n")

        for col in founder_cols:
            if col in df.columns:
                n_valid = df[col].notna().sum()
                pct = n_valid / len(df) * 100
                print(f"  ✓ {col:<25} {n_valid:>8,} ({pct:>5.1f}%)")
            else:
                print(f"  ✗ {col:<25} NOT FOUND")

        # Check if we can compute serial entrepreneurs
        if 'PrimaryContactPBId' in df.columns:
            contact_ids = df['PrimaryContactPBId'].dropna()
            founder_counts = df.groupby('PrimaryContactPBId')['CompanyID'].nunique()
            serial = (founder_counts >= 2).sum()
            serial_pct = serial / len(founder_counts) * 100

            print(f"\n  📊 Founder credibility potential:")
            print(f"     Unique founders: {len(founder_counts):,}")
            print(f"     Serial entrepreneurs: {serial:,} ({serial_pct:.1f}%)")

        return True

    except Exception as e:
        print(f"  ✗ ERROR: {e}")
        return False


def check_singular_matrix_risk(data_file="outputs/h2_analysis_dataset_17m.csv"):
    """Check for collinearity that could cause singular matrix."""
    print("\n" + "="*80)
    print("SINGULAR MATRIX RISK CHECK")
    print("="*80)

    try:
        df = pd.read_csv(data_file)

        # Check founding_cohort for empty categories
        if 'founding_cohort' in df.columns:
            cohort_counts = df['founding_cohort'].value_counts()
            print(f"\n  Founding Cohort Distribution:")
            for cohort, count in cohort_counts.sort_index().items():
                status = "⚠️" if count < 100 else "✓"
                print(f"    {status} {cohort:<15} {count:>8,}")

            empty_cats = cohort_counts[cohort_counts == 0]
            if len(empty_cats) > 0:
                print(f"\n  ⚠️  WARNING: {len(empty_cats)} empty categories (will cause singular matrix!)")

        # Check IC vs Sector collinearity
        if 'high_integration_cost' in df.columns and 'sector_fe' in df.columns:
            import statsmodels.api as sm

            # Compute R² of IC ~ Sector
            S = pd.get_dummies(df['sector_fe'], drop_first=True)
            r2 = sm.OLS(df['high_integration_cost'], sm.add_constant(S)).fit().rsquared

            print(f"\n  IC ~ Sector Collinearity:")
            print(f"    R² = {r2:.3f}")

            if r2 > 0.95:
                print(f"    ⚠️  WARNING: Nearly perfect collinearity!")
                print(f"    → IC is {r2:.1%} explained by sector")
                print(f"    → MUST use ic_within to identify within-sector effect")
            else:
                print(f"    ✓ OK: Sufficient within-sector variation")

        return True

    except FileNotFoundError:
        print(f"  ℹ️  Analysis dataset not found yet (run pipeline first)")
        return True
    except Exception as e:
        print(f"  ✗ ERROR: {e}")
        return False


def main():
    """Run all diagnostic checks."""
    print("\n" + "="*80)
    print("DATA QUALITY DIAGNOSTICS")
    print("="*80)
    print()

    results = {
        'Snapshots': check_snapshots(),
        'Series A Detection': check_series_a_detection(),
        'Deal Types': check_deal_types(),
        'Founder Columns': check_founder_columns(),
        'Singular Matrix Risk': check_singular_matrix_risk()
    }

    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)

    for check, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"  {status:<10} {check}")

    all_passed = all(results.values())

    if all_passed:
        print("\n✓ All checks passed! Ready to run analysis.")
        return 0
    else:
        print("\n⚠️  Some checks failed. Review issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
