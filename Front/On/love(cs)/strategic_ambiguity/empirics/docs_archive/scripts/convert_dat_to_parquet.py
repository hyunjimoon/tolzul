"""
Convert .dat files to .parquet format

Usage: python scripts/convert_dat_to_parquet.py
"""

import pandas as pd
from pathlib import Path

# Files to convert
FILES_TO_CONVERT = [
    "Company20231201.dat",
    "Company20241201.dat",
    "Company20251101.dat"
]

RAW_DIR = Path("data/raw")

print("="*80)
print("DAT → PARQUET CONVERSION")
print("="*80)

for filename in FILES_TO_CONVERT:
    dat_path = RAW_DIR / filename
    parquet_path = RAW_DIR / filename.replace('.dat', '.parquet')

    print(f"\n{filename}:")

    if not dat_path.exists():
        print(f"   ✗ File not found, skipping")
        continue

    if parquet_path.exists():
        print(f"   ⚠️  Parquet already exists, skipping")
        continue

    try:
        # Read DAT file (pipe-delimited)
        df = pd.read_csv(dat_path, sep='|', low_memory=False)
        print(f"   ✓ Loaded: {len(df):,} rows, {len(df.columns)} columns")

        # Save as parquet
        df.to_parquet(parquet_path, index=False)
        print(f"   ✓ Saved: {parquet_path}")

        # Check size reduction
        dat_size = dat_path.stat().st_size / (1024**2)  # MB
        parquet_size = parquet_path.stat().st_size / (1024**2)  # MB
        print(f"   Size: {dat_size:.1f}MB → {parquet_size:.1f}MB ({parquet_size/dat_size*100:.1f}%)")

    except Exception as e:
        print(f"   ✗ Error: {e}")

print("\n" + "="*80)
print("CONVERSION COMPLETE")
print("="*80)
