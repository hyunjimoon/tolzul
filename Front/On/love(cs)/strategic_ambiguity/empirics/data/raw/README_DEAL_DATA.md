# Deal Data Instructions

## You Have Deal Data Locally!

Your Deal data file should be named `Deal*.dat` and placed in this directory (`data/raw/`).

### Valid File Names:
- `Deal2023.dat` ✓
- `DealData.dat` ✓
- `Deal20230501.dat` ✓
- `Deal_pitchbook.dat` ✓

### Invalid File Names:
- `deal2023.dat` ✗ (must start with capital 'D')
- `company_deal.dat` ✗ (must start with 'Deal')
- `Company2021_deal2023.dat` ✗ (currently exists but doesn't match pattern)

## The File is Already in .gitignore

The Deal file won't be pushed to GitHub because it's listed in `.gitignore`:
```
Front/On/💌찰리스캇 러브레터 플젝/strategic ambiguity/empirics/data/raw/Deal20230501.dat
```

You can add your specific filename to `.gitignore` if it's different.

## What to Do

1. **If your Deal file has a different name**, rename it to match the pattern:
   ```bash
   # Example: rename your current file to Deal2023.dat
   mv your_deal_file.dat Deal2023.dat
   ```

2. **Verify the file is here**:
   ```bash
   ls -lh Deal*.dat
   ```

3. **Run the pipeline**:
   ```bash
   cd ../code
   python pipeline_xarray.py --from 2 --force
   ```

## Expected Output

Once the Deal file is properly named, you should see:
```
[Step 2] Processing deal data...
Found 1 Deal files: ['Deal2023.dat']
  - Deal2023.dat: NNNN rows, 95 columns
Total deals loaded: NNNN

✅ Processed NNNN deals
```

## File Format Verification

Your Deal file should be:
- **Delimiter**: Pipe (`|`) separated ✓
- **Encoding**: UTF-8 ✓
- **Header**: First row with column names ✓

Based on the sample you provided, your format looks perfect! Just need the right filename.
