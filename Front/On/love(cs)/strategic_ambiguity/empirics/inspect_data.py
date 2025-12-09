import pandas as pd
import xarray as xr

try:
    # Try loading as xarray first (since it's .nc)
    ds = xr.open_dataset('data/processed/features_all.nc')
    df = ds.to_dataframe()
    print("Loaded via xarray")
except Exception as e:
    print(f"Xarray load failed: {e}")
    # Try loading via pandas (if it's just a pickled dataframe saved with .nc extension, which is unlikely but possible given the code)
    # Actually the cli.py said "Loaded DataFrame from ...", so it might be using xarray or custom loader.
    # Let's check src/data_io.py if possible, but for now assume xarray or pandas read_hdf/parquet?
    # The Makefile said DATA_FORMAT := nc.
    pass

# If xarray worked
if 'df' in locals():
    print(f"Columns ({len(df.columns)}):")
    for col in sorted(df.columns):
        print(f" - {col}")
    
    # Check for vagueness
    print("\nVagueness related columns:")
    for col in df.columns:
        if 'vague' in col.lower():
            print(f" - {col}")
            
else:
    print("Could not load dataframe.")
