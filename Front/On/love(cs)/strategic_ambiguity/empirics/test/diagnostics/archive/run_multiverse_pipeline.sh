#!/bin/bash

################################################################################
# MULTIVERSE ANALYSIS - ONE-TOUCH PIPELINE
# Data prep → Parquet cache → Multiverse analysis → Results
# 必死則生 🐢🐅
################################################################################

set -e  # Exit on error

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Detect Python command
if command -v python3 &> /dev/null; then
    PYTHON="python3"
elif command -v python &> /dev/null; then
    PYTHON="python"
else
    echo -e "${RED}❌ ERROR: Python not found${NC}"
    echo -e "${YELLOW}Please install Python 3.7 or higher${NC}"
    exit 1
fi

echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║     MULTIVERSE ANALYSIS PIPELINE - ONE-TOUCH EXECUTION        ║${NC}"
echo -e "${BLUE}║     必死則生 🐢🐅                                               ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Show Python version
PYTHON_VERSION=$($PYTHON --version 2>&1)
echo -e "${GREEN}✓${NC} Using: ${PYTHON_VERSION}"
echo ""

# Parse arguments with defaults
DATA_DIR="${1:-data/raw}"
OUTPUT_DIR="${2:-outputs}"
MULTIVERSE_DIR="${3:-multiverse_results}"

echo -e "${CYAN}📂 Configuration:${NC}"
echo -e "   Data directory:       ${DATA_DIR}"
echo -e "   Analysis outputs:     ${OUTPUT_DIR}"
echo -e "   Multiverse outputs:   ${MULTIVERSE_DIR}"
echo ""

# Check if data directory exists
if [ ! -d "$DATA_DIR" ]; then
    echo -e "${RED}❌ ERROR: Data directory not found: ${DATA_DIR}${NC}"
    echo -e "${YELLOW}💡 Usage: $0 [DATA_DIR] [OUTPUT_DIR] [MULTIVERSE_DIR]${NC}"
    echo -e "${YELLOW}   Example: $0 /Users/hyunjimoon/tolzul/Front/On/love\\(cs\\)/strategic_ambiguity/empirics/data/raw${NC}"
    exit 1
fi

# Count .dat files
DAT_COUNT=$(find "$DATA_DIR" -name "*.dat" -type f 2>/dev/null | wc -l | tr -d ' ')
echo -e "${GREEN}✓${NC} Found ${DAT_COUNT} .dat files in data directory"

if [ "$DAT_COUNT" -eq 0 ]; then
    echo -e "${RED}❌ ERROR: No .dat files found in ${DATA_DIR}${NC}"
    exit 1
fi

# Check for existing parquet files
PARQUET_COUNT=$(find "$DATA_DIR" -name "*.parquet" -type f 2>/dev/null | wc -l | tr -d ' ')
if [ "$PARQUET_COUNT" -gt 0 ]; then
    echo -e "${GREEN}✓${NC} Found ${PARQUET_COUNT} cached .parquet files (fast mode!)"
else
    echo -e "${YELLOW}⏳${NC} No parquet cache found - first run will create cache"
fi
echo ""

################################################################################
# STEP 1: Data Preparation & Feature Engineering
################################################################################

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}STEP 1/3: Data Preparation & Parquet Cache Generation${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

START_STEP1=$(date +%s)

echo -e "${YELLOW}Running data preparation pipeline...${NC}"
echo -e "   • Reading .dat files"
echo -e "   • Creating .parquet cache (for future speedup)"
echo -e "   • Engineering features"
echo -e "   • Building analysis dataset"
echo ""

if $PYTHON run_analysis.py --output "$OUTPUT_DIR" 2>&1 | tee /tmp/run_analysis.log; then
    END_STEP1=$(date +%s)
    DURATION_STEP1=$((END_STEP1 - START_STEP1))
    echo -e "\n${GREEN}✅ STEP 1 COMPLETE${NC} (${DURATION_STEP1}s)"
else
    echo -e "\n${RED}❌ ERROR: Data preparation failed${NC}"
    echo -e "${YELLOW}See log: /tmp/run_analysis.log${NC}"
    exit 1
fi

# Verify analysis dataset was created
ANALYSIS_FILE="${OUTPUT_DIR}/h2_analysis_dataset.csv"
if [ ! -f "$ANALYSIS_FILE" ]; then
    echo -e "${RED}❌ ERROR: Analysis dataset not created: ${ANALYSIS_FILE}${NC}"
    exit 1
fi

# Show dataset info
ROW_COUNT=$(tail -n +2 "$ANALYSIS_FILE" | wc -l | tr -d ' ')
COL_COUNT=$(head -n 1 "$ANALYSIS_FILE" | tr ',' '\n' | wc -l | tr -d ' ')
FILE_SIZE=$(ls -lh "$ANALYSIS_FILE" | awk '{print $5}')

echo -e "${GREEN}✓${NC} Analysis dataset: ${ANALYSIS_FILE}"
echo -e "${GREEN}✓${NC} Dimensions: ${ROW_COUNT} rows × ${COL_COUNT} columns (${FILE_SIZE})"
echo ""

# Show parquet cache status
PARQUET_AFTER=$(find "$DATA_DIR" -name "*.parquet" -type f 2>/dev/null | wc -l | tr -d ' ')
if [ "$PARQUET_AFTER" -gt "$PARQUET_COUNT" ]; then
    NEW_PARQUET=$((PARQUET_AFTER - PARQUET_COUNT))
    echo -e "${GREEN}✓${NC} Created ${NEW_PARQUET} new .parquet cache files"
    echo -e "${CYAN}💡${NC} Future runs will be 10-50x faster!"
fi
echo ""

################################################################################
# STEP 2: Multiverse Analysis
################################################################################

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}STEP 2/3: Multiverse Analysis (384 specifications)${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${CYAN}Specification Grid:${NC}"
echo -e "   • 3 stages (E, L1, L2)"
echo -e "   • 3 time windows"
echo -e "   • 2 scaling methods (zscore, winsor99_z)"
echo -e "   • 2 moderators (option_level, isSoftware)"
echo -e "   • 2⁴ = 16 control combinations"
echo -e "   • Total: 3×3×2×2×16 = 384 specifications"
echo ""

START_STEP2=$(date +%s)

echo -e "${YELLOW}Running multiverse analysis...${NC}"
echo -e "   Input:  ${ANALYSIS_FILE}"
echo -e "   Output: ${MULTIVERSE_DIR}/"
echo ""

if $PYTHON run_multiverse.py --input "$ANALYSIS_FILE" --outdir "$MULTIVERSE_DIR" 2>&1 | tee /tmp/run_multiverse.log; then
    END_STEP2=$(date +%s)
    DURATION_STEP2=$((END_STEP2 - START_STEP2))
    echo -e "\n${GREEN}✅ STEP 2 COMPLETE${NC} (${DURATION_STEP2}s)"
else
    echo -e "\n${RED}❌ ERROR: Multiverse analysis failed${NC}"
    echo -e "${YELLOW}See log: /tmp/run_multiverse.log${NC}"
    exit 1
fi
echo ""

################################################################################
# STEP 3: Results Summary
################################################################################

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}STEP 3/3: Results Summary${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Display summary statistics
if [ -f "${MULTIVERSE_DIR}/summary_stats.txt" ]; then
    echo -e "${CYAN}📊 SUMMARY STATISTICS:${NC}"
    echo -e "${BLUE}───────────────────────────────────────────────────────────────${NC}"
    cat "${MULTIVERSE_DIR}/summary_stats.txt"
    echo -e "${BLUE}───────────────────────────────────────────────────────────────${NC}"
    echo ""
fi

# List output files
echo -e "${CYAN}📁 OUTPUT FILES:${NC}"
echo ""

echo -e "${YELLOW}Analysis Outputs (${OUTPUT_DIR}):${NC}"
if [ -d "$OUTPUT_DIR" ]; then
    find "$OUTPUT_DIR" -maxdepth 1 -type f \( -name "*.csv" -o -name "*.png" \) 2>/dev/null | sort | while read file; do
        SIZE=$(ls -lh "$file" | awk '{print $5}')
        BASENAME=$(basename "$file")
        echo -e "   ${GREEN}✓${NC} ${BASENAME} (${SIZE})"
    done
else
    echo -e "   ${YELLOW}(no outputs directory)${NC}"
fi
echo ""

echo -e "${YELLOW}Multiverse Outputs (${MULTIVERSE_DIR}):${NC}"
if [ -d "$MULTIVERSE_DIR" ]; then
    find "$MULTIVERSE_DIR" -type f 2>/dev/null | sort | while read file; do
        SIZE=$(ls -lh "$file" | awk '{print $5}')
        BASENAME=$(basename "$file")
        EXT="${BASENAME##*.}"

        case "$EXT" in
            nc)   ICON="📦" ;;
            csv)  ICON="📊" ;;
            png)  ICON="📈" ;;
            txt)  ICON="📝" ;;
            *)    ICON="📄" ;;
        esac

        echo -e "   ${GREEN}✓${NC} ${ICON} ${BASENAME} (${SIZE})"
    done
else
    echo -e "   ${YELLOW}(no multiverse directory)${NC}"
fi
echo ""

# Count visualizations
PNG_COUNT=$(find "$MULTIVERSE_DIR" -name "*.png" 2>/dev/null | wc -l | tr -d ' ')
if [ "$PNG_COUNT" -gt 0 ]; then
    echo -e "${GREEN}✓${NC} Generated ${PNG_COUNT} visualization plots"
    echo ""
fi

################################################################################
# DONE
################################################################################

TOTAL_DURATION=$((END_STEP2 - START_STEP1 + DURATION_STEP1))

echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                    ✅ PIPELINE COMPLETE                        ║${NC}"
echo -e "${BLUE}║                Total Runtime: ${TOTAL_DURATION}s                           ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${GREEN}🎉 SUCCESS! All analyses complete.${NC}"
echo ""
echo -e "${CYAN}📂 Quick Access to Results:${NC}"
echo ""
echo -e "${YELLOW}1. Summary Statistics:${NC}"
echo -e "   cat ${MULTIVERSE_DIR}/summary_stats.txt"
echo ""
echo -e "${YELLOW}2. Browse Results Table:${NC}"
echo -e "   head -20 ${MULTIVERSE_DIR}/spec_table.csv"
echo ""
echo -e "${YELLOW}3. View Visualizations:${NC}"
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo -e "   open ${MULTIVERSE_DIR}/*.png"
else
    echo -e "   xdg-open ${MULTIVERSE_DIR}/*.png"
fi
echo ""
echo -e "${YELLOW}4. Load in Python:${NC}"
echo -e "   ${BLUE}import xarray as xr${NC}"
echo -e "   ${BLUE}ds = xr.open_dataset('${MULTIVERSE_DIR}/multiverse_results.nc')${NC}"
echo -e "   ${BLUE}# Slice by specification:${NC}"
echo -e "   ${BLUE}ds.sel(stage='E', moderator='option_level')${NC}"
echo ""
echo -e "${YELLOW}5. Generate Custom Plots:${NC}"
echo -e "   ${BLUE}import pandas as pd${NC}"
echo -e "   ${BLUE}df = pd.read_csv('${MULTIVERSE_DIR}/spec_table.csv')${NC}"
echo -e "   ${BLUE}df[df['is_consistent_vag_main']==1].shape  # Count consistent specs${NC}"
echo ""
echo -e "${GREEN}必死則生 🐢🐅${NC}"
echo ""

# Optional: Open results directory (macOS/Linux)
if [ -d "$MULTIVERSE_DIR" ]; then
    read -p "Open results folder? [y/N] " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        if [[ "$OSTYPE" == "darwin"* ]]; then
            open "$MULTIVERSE_DIR"
        elif command -v xdg-open &> /dev/null; then
            xdg-open "$MULTIVERSE_DIR"
        else
            echo -e "${YELLOW}Results directory: ${MULTIVERSE_DIR}${NC}"
        fi
    fi
fi
