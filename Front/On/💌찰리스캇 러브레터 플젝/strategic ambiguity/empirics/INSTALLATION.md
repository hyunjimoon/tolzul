# Installation Instructions

## Python Requirements

The pipeline requires Python 3.9 or higher.

## Installing Required Packages

### Option 1: Using pip (Recommended)

```bash
# Navigate to the empirics directory
cd "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Front/On/💌찰리스캇 러브레터 플젝/strategic ambiguity/empirics"

# Install all required packages
pip install -r requirements.txt
```

Or if you're using Python 3 specifically:
```bash
pip3 install -r requirements.txt
```

### Option 2: Install Packages Individually

If you prefer to install packages one by one:

```bash
pip3 install pandas numpy xarray statsmodels scipy matplotlib seaborn
```

For Jupyter notebook support (optional):
```bash
pip3 install jupyter notebook ipykernel
```

### Option 3: Using Conda (Alternative)

If you're using Anaconda or Miniconda:

```bash
# Create a new environment (optional but recommended)
conda create -n strategic_ambiguity python=3.9
conda activate strategic_ambiguity

# Install packages
conda install pandas numpy xarray statsmodels scipy matplotlib seaborn
conda install jupyter notebook
```

## Verifying Installation

After installation, verify that the packages are installed correctly:

```bash
python3 -c "import pandas, numpy, xarray, statsmodels, matplotlib, seaborn; print('✅ All packages installed successfully!')"
```

If you see the success message, you're ready to run the pipeline!

## Running the Pipeline

Once packages are installed:

```bash
cd code
python3 pipeline_xarray.py
```

Or to start from a specific step:
```bash
python3 pipeline_xarray.py --from 2 --force
```

## Troubleshooting

### "command not found: pip3"

If `pip3` is not found, try:
- `pip install -r requirements.txt`
- Or install pip: https://pip.pypa.io/en/stable/installation/

### "Permission denied" errors

If you get permission errors, try:
```bash
pip3 install --user -r requirements.txt
```

### Using Virtual Environment (Recommended for Isolation)

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On macOS/Linux
# or
.\venv\Scripts\activate  # On Windows

# Install packages
pip install -r requirements.txt
```

## Package Versions

The pipeline has been tested with:
- Python 3.9+
- pandas 1.5+
- xarray 2023.1+
- statsmodels 0.14+

See `requirements.txt` for full version specifications.
