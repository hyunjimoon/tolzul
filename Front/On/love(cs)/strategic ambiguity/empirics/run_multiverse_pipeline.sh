#!/bin/bash
# Multiverse Analysis Pipeline - One-Touch Execution
# 必死則生 🐢🐅

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║     MULTIVERSE ANALYSIS PIPELINE - ONE-TOUCH EXECUTION        ║"
echo "║     必死則生 🐢🐅                                               ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Get script directory (where this .sh file is located)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Define paths
VENV_DIR=".venv"
VENV_PYTHON="$VENV_DIR/bin/python3"
VENV_PIP="$VENV_DIR/bin/pip3"

# 1. Check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}⚠ Virtual environment not found. Creating .venv...${NC}"
    python3 -m venv "$VENV_DIR"
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${GREEN}✓ Virtual environment found: $VENV_DIR${NC}"
fi

# 2. Check if packages are installed
if ! "$VENV_PYTHON" -c "import pandas" 2>/dev/null; then
    echo -e "${YELLOW}⚠ Required packages not installed. Installing from requirements.txt...${NC}"
    "$VENV_PIP" install --upgrade pip
    "$VENV_PIP" install -r requirements.txt
    echo -e "${GREEN}✓ All packages installed${NC}"
else
    echo -e "${GREEN}✓ Required packages already installed${NC}"
fi

# 3. Display Python info
PYTHON_VERSION=$("$VENV_PYTHON" --version 2>&1)
echo -e "${BLUE}✓ Using: $PYTHON_VERSION (from $VENV_PYTHON)${NC}"
echo ""

# 4. Display configuration
echo "📂 Configuration:"
echo "   Data directory:       data/raw"
echo "   Analysis outputs:     outputs"
echo "   Multiverse outputs:   multiverse_results"
echo ""

# Check data files
DATA_FILES=$(find data/raw -name "*.dat" 2>/dev/null | wc -l)
PARQUET_CACHE=$(find data/cache -name "*.parquet" 2>/dev/null | wc -l)
echo -e "${GREEN}✓ Found $DATA_FILES .dat files in data directory${NC}"
if [ "$PARQUET_CACHE" -gt 0 ]; then
    echo -e "${GREEN}✓ Found $PARQUET_CACHE cached .parquet files (fast mode!)${NC}"
fi
echo ""

# 5. Run analysis pipeline
echo "═══════════════════════════════════════════════════════════════"
echo "STEP 1/3: Data Preparation & Parquet Cache Generation"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "Running data preparation pipeline..."
echo "   • Reading .dat files"
echo "   • Creating .parquet cache (for future speedup)"
echo "   • Engineering features"
echo "   • Building analysis dataset"
echo ""

START_TIME=$(date +%s)
"$VENV_PYTHON" run_analysis.py
END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

echo ""
echo -e "${GREEN}✅ STEP 1 COMPLETE (${ELAPSED}s)${NC}"
echo ""

# 6. Check outputs
if [ ! -f "outputs/h2_analysis_dataset.csv" ]; then
    echo -e "${RED}❌ ERROR: Analysis dataset not created: outputs/h2_analysis_dataset.csv${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Analysis dataset created: outputs/h2_analysis_dataset.csv${NC}"
echo ""

# 7. Run multiverse analysis (if script exists)
if [ -f "run_cohort_analysis.py" ]; then
    echo "═══════════════════════════════════════════════════════════════"
    echo "STEP 2/3: Multiverse Analysis (Cohort-based)"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""

    START_TIME=$(date +%s)
    "$VENV_PYTHON" run_cohort_analysis.py
    END_TIME=$(date +%s)
    ELAPSED=$((END_TIME - START_TIME))

    echo ""
    echo -e "${GREEN}✅ STEP 2 COMPLETE (${ELAPSED}s)${NC}"
    echo ""
fi

# 8. Summary
echo "═══════════════════════════════════════════════════════════════"
echo "PIPELINE COMPLETE! 🎉"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "📊 Results:"
echo "   • H1 coefficients:     outputs/h1_coefficients.csv"
echo "   • H2 coefficients:     outputs/h2_main_coefficients.csv"
echo "   • Analysis dataset:    outputs/h2_analysis_dataset.csv"
echo ""

if [ -d "multiverse_results" ]; then
    MULTIVERSE_FILES=$(find multiverse_results -name "*.csv" 2>/dev/null | wc -l)
    echo "   • Multiverse results:  $MULTIVERSE_FILES CSV files in multiverse_results/"
    echo ""
fi

echo "🎯 Next steps:"
echo "   1. Review outputs/ directory"
echo "   2. Check diagnostics/ for plots"
echo "   3. Open report_w1.qmd in RStudio/Quarto"
echo ""
echo -e "${GREEN}✅ All done! 必死則生${NC}"
