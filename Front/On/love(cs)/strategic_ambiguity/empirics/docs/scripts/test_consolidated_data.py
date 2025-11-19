"""
Test consolidated 2021 cohort data quality

E Definition: Companies whose most recent financing was Early Stage VC (Series A)
              as of Dec 2021. NO Buyout/LBO, NO Merger/Acquisition.

Checks:
1. Files exist
2. Row/column counts
3. No duplicate CompanyIDs
4. DealType columns populated
5. E=1 cohort verification (CRITICAL: baseline must be Early Stage VC only)
6. Cross-year consistency
7. Sample data

Usage: python scripts/test_consolidated_data.py
"""

import pandas as pd
import re
from pathlib import Path

PROCESSED_DIR = Path("data/processed")

FILES_TO_TEST = [
    "companies_21_23-24-25.parquet",
    "companies_21_23-24-25_quantum.parquet",
    "companies_21_23-24-25_transportation.parquet"
]

# Pattern for Early Stage VC (Series A) - E=1
PAT_E = re.compile(r"(?:\bEarly\s*Stage\s*VC\b|\bSeries\s*A(?:\b|[\s\-]?\d*)\b)", re.I)

# Patterns for EXCLUDED deal types (should NOT appear in DealType_2021)
EXCLUDED_PATTERNS = [
    (r"\bBuyout/LBO\b", "Buyout/LBO"),
    (r"\bMerger[/\s]*Acquisition\b", "Merger/Acquisition"),
    (r"\bLater\s*Stage\s*VC\b", "Later Stage VC"),
    (r"\bSeries\s*[B-G]", "Series B+"),
    (r"\bAngel\b", "Angel"),
    (r"\bSeed\b", "Seed"),
]

print("="*80)
print("DATA QUALITY TESTS")
print("="*80)

all_passed = True

for filename in FILES_TO_TEST:
    filepath = PROCESSED_DIR / filename

    print(f"\n{'='*80}")
    print(f"Testing: {filename}")
    print(f"{'='*80}")

    # Test 1: File exists
    print(f"\n1. File exists...")
    if not filepath.exists():
        print(f"   ✗ FAIL: File not found")
        all_passed = False
        continue
    print(f"   ✓ PASS")

    # Load file
    try:
        df = pd.read_parquet(filepath)
    except Exception as e:
        print(f"   ✗ FAIL: Could not load file - {e}")
        all_passed = False
        continue

    # Test 2: Basic shape
    print(f"\n2. Basic shape...")
    print(f"   Rows: {len(df):,}")
    print(f"   Columns: {len(df.columns)}")
    print(f"   Column names: {list(df.columns)}")
    if len(df) == 0:
        print(f"   ✗ FAIL: Empty dataframe")
        all_passed = False
    else:
        print(f"   ✓ PASS")

    # Test 3: No duplicate CompanyIDs
    print(f"\n3. No duplicate CompanyIDs...")
    duplicates = df['CompanyID'].duplicated().sum()
    if duplicates > 0:
        print(f"   ✗ FAIL: {duplicates} duplicate CompanyIDs found")
        all_passed = False
    else:
        print(f"   ✓ PASS")

    # Test 4: DealType columns populated
    print(f"\n4. DealType columns populated...")
    dealtype_cols = [c for c in df.columns if 'DealType' in c]

    if len(dealtype_cols) == 0:
        print(f"   ✗ FAIL: No DealType columns found")
        all_passed = False
    else:
        print(f"   Found columns: {dealtype_cols}")
        for col in dealtype_cols:
            non_null = df[col].notna().sum()
            pct = non_null / len(df) * 100
            print(f"   {col}: {non_null:,} / {len(df):,} ({pct:.1f}%) populated")

            if pct < 50:
                print(f"      ⚠️  WARNING: Less than 50% populated")

        print(f"   ✓ PASS (columns exist)")

    # Test 5: E=1 cohort verification (CRITICAL)
    print(f"\n5. E=1 cohort verification (baseline must be Early Stage VC only)...")
    if 'DealType_2021' in df.columns:
        # Check: ALL companies should have Early Stage VC
        is_early_stage = df['DealType_2021'].fillna('').apply(
            lambda x: bool(PAT_E.search(str(x)))
        )

        early_count = is_early_stage.sum()
        total_count = len(df)

        print(f"   Early Stage VC (E=1): {early_count:,} / {total_count:,} ({early_count/total_count*100:.1f}%)")

        if early_count != total_count:
            non_early = df[~is_early_stage]
            print(f"   ✗ FAIL: Found {len(non_early):,} companies that are NOT Early Stage VC!")
            print(f"   First 5 non-Early Stage VC companies:")
            print(non_early[['CompanyID', 'CompanyName', 'DealType_2021']].head().to_string())
            all_passed = False
        else:
            print(f"   ✓ PASS: All companies are Early Stage VC (E=1)")

        # Check: NO excluded deal types (Buyout/LBO, M&A, etc.)
        print(f"\n   Checking for EXCLUDED deal types in DealType_2021...")
        found_excluded = False
        for pattern, label in EXCLUDED_PATTERNS:
            regex = re.compile(pattern, re.I)
            has_excluded = df['DealType_2021'].fillna('').apply(
                lambda x: bool(regex.search(str(x)))
            )
            excluded_count = has_excluded.sum()

            if excluded_count > 0:
                print(f"   ✗ FAIL: Found {excluded_count:,} companies with '{label}'")
                excluded_samples = df[has_excluded][['CompanyID', 'CompanyName', 'DealType_2021']].head(3)
                print(f"   Sample companies:")
                print(excluded_samples.to_string())
                all_passed = False
                found_excluded = True

        if not found_excluded:
            print(f"   ✓ PASS: No excluded deal types found (Buyout/LBO, M&A, etc.)")
    else:
        print(f"   ⚠️  SKIP: DealType_2021 not found")

    # Test 6: Cross-year consistency (progression logic)
    print(f"\n6. Cross-year consistency...")
    if 'DealType_2021' in df.columns:
        # Count Early Stage at baseline
        early_2021 = df['DealType_2021'].fillna('').str.contains('Early Stage VC', case=False, na=False).sum()
        print(f"   Early Stage VC (2021): {early_2021:,}")

        # Check progression to Later Stage
        if 'DealType_2023' in df.columns:
            later_2023 = df['DealType_2023'].fillna('').str.contains('Later Stage VC', case=False, na=False).sum()
            print(f"   Later Stage VC (2023): {later_2023:,}")

        if 'DealType_2024' in df.columns:
            later_2024 = df['DealType_2024'].fillna('').str.contains('Later Stage VC', case=False, na=False).sum()
            print(f"   Later Stage VC (2024): {later_2024:,}")

        if 'DealType_2025' in df.columns:
            later_2025 = df['DealType_2025'].fillna('').str.contains('Later Stage VC', case=False, na=False).sum()
            print(f"   Later Stage VC (2025): {later_2025:,}")

        print(f"   ✓ PASS (counts displayed)")
    else:
        print(f"   ⚠️  SKIP: DealType_2021 not found")

    # Test 7: Sample data
    print(f"\n7. Sample data (first 3 rows)...")
    print(df.head(3).to_string())
    print(f"   ✓ PASS")

print(f"\n{'='*80}")
print(f"FINAL RESULT")
print(f"{'='*80}")

if all_passed:
    print(f"\n✓ ALL TESTS PASSED!")
else:
    print(f"\n✗ SOME TESTS FAILED - Please review above")

print()
