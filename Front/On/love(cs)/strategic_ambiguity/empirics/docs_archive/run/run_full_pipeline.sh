#!/bin/bash
################################################################################
# COMPLETE MULTIVERSE ANALYSIS PIPELINE
# Executes 5-stage pipeline + multiverse analysis
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
    echo -e "${YELLOW}Please install Python 3.9 or higher${NC}"
    exit 1
fi

echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║        COMPLETE MULTIVERSE ANALYSIS PIPELINE                  ║${NC}"
echo -e "${BLUE}║        必死則生 🐢🐅                                            ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Show Python version
PYTHON_VERSION=$($PYTHON --version 2>&1)
echo -e "${GREEN}✓${NC} Using: ${PYTHON_VERSION}"
echo ""

# Parse arguments with defaults
DATA_DIR="${1:-data/raw}"
OUTPUT_DIR="${2:-results}"
MULTIVERSE_DIR="${3:-multiverse_results}"
YEARS="${4:-2022 2024 2025}"  # Default years to load

echo -e "${CYAN}📂 Configuration:${NC}"
echo -e "   Data directory:       ${DATA_DIR}"
echo -e "   Results directory:    ${OUTPUT_DIR}"
echo -e "   Multiverse directory: ${MULTIVERSE_DIR}"
echo -e "   Years to load:        ${YEARS}"
echo ""

# Check if data directory exists
if [ ! -d "$DATA_DIR" ]; then
    echo -e "${RED}❌ ERROR: Data directory not found: ${DATA_DIR}${NC}"
    echo -e "${YELLOW}💡 Usage: $0 [DATA_DIR] [OUTPUT_DIR] [MULTIVERSE_DIR] [YEARS]${NC}"
    echo -e "${YELLOW}   Example: $0 data/raw results multiverse_results \"2022 2024 2025\"${NC}"
    exit 1
fi

# Count .dat files
DAT_COUNT=$(find "$DATA_DIR" -name "Company*.dat" -type f 2>/dev/null | wc -l | tr -d ' ')
echo -e "${GREEN}✓${NC} Found ${DAT_COUNT} .dat files in data directory"

if [ "$DAT_COUNT" -eq 0 ]; then
    echo -e "${RED}❌ ERROR: No Company*.dat files found in ${DATA_DIR}${NC}"
    exit 1
fi
echo ""

################################################################################
# STEP 1: 5-Stage Pipeline (main.py)
################################################################################

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}STEP 1/2: 5-Stage Pipeline (BUILD → DEFINE → PLOT1 → TEST → PLOT2)${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${CYAN}Pipeline Stages:${NC}"
echo -e "   1🏗️  BUILD:  Load and consolidate .dat files"
echo -e "   2🧠 DEFINE: Engineer core variables (E, L, V, F, S)"
echo -e "   3📊 PLOT1:  Variable distributions"
echo -e "   4⚖️  TEST:   Hypothesis testing (H1, H2)"
echo -e "   5📈 PLOT2:  Multiverse visualization (if results exist)"
echo ""

START_STEP1=$(date +%s)

echo -e "${YELLOW}Running main pipeline...${NC}"
echo ""

# Convert YEARS string to array for --years flag
YEARS_ARRAY=($YEARS)

if $PYTHON main.py --data-dir "$DATA_DIR" --output-dir "$OUTPUT_DIR" --years "${YEARS_ARRAY[@]}" 2>&1 | tee /tmp/main_pipeline.log; then
    END_STEP1=$(date +%s)
    DURATION_STEP1=$((END_STEP1 - START_STEP1))
    echo -e "\n${GREEN}✅ STEP 1 COMPLETE${NC} (${DURATION_STEP1}s)"
else
    echo -e "\n${RED}❌ ERROR: Main pipeline failed${NC}"
    echo -e "${YELLOW}See log: /tmp/main_pipeline.log${NC}"
    exit 1
fi
echo ""

# Check if parquet cache was created
PARQUET_CACHE=$(find "data/processed" -name "consolidated_companies_*.parquet" -o -name "consolidated_companies_*.pkl" 2>/dev/null | head -1)
if [ -n "$PARQUET_CACHE" ]; then
    CACHE_SIZE=$(ls -lh "$PARQUET_CACHE" | awk '{print $5}')
    echo -e "${GREEN}✓${NC} Parquet cache created: $(basename $PARQUET_CACHE) (${CACHE_SIZE})"
    echo -e "${CYAN}💡${NC} Future runs will be 20x faster!"
    echo ""
fi

################################################################################
# STEP 2: Multiverse Analysis (run_multiverse.py)
################################################################################

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}STEP 2/2: Multiverse Analysis (288 specifications)${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Check if analysis dataset exists
ANALYSIS_FILE="data/processed/analysis_panel.csv"

if [ ! -f "$ANALYSIS_FILE" ]; then
    echo -e "${YELLOW}⚠️  Analysis dataset not found: ${ANALYSIS_FILE}${NC}"
    echo -e "${YELLOW}   Skipping multiverse analysis${NC}"
    echo -e "${YELLOW}   To run multiverse analysis, ensure data/processed/analysis_panel.csv exists${NC}"
else
    echo -e "${CYAN}Specification Grid:${NC}"
    echo -e "   • 3 stages (E, L1, L2)"
    echo -e "   • 3 time windows"
    echo -e "   • 2 scaling methods (zscore, winsor99_z)"
    echo -e "   • 1 moderator (isSoftware)"
    echo -e "   • 2⁴ = 16 control combinations"
    echo -e "   • Total: 3×3×2×1×16 = 288 specifications"
    echo ""

    # Show dataset info
    ROW_COUNT=$(tail -n +2 "$ANALYSIS_FILE" | wc -l | tr -d ' ')
    COL_COUNT=$(head -n 1 "$ANALYSIS_FILE" | tr ',' '\n' | wc -l | tr -d ' ')
    FILE_SIZE=$(ls -lh "$ANALYSIS_FILE" | awk '{print $5}')

    echo -e "${GREEN}✓${NC} Analysis dataset: ${ANALYSIS_FILE}"
    echo -e "${GREEN}✓${NC} Dimensions: ${ROW_COUNT} rows × ${COL_COUNT} columns (${FILE_SIZE})"
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
        echo -e "${YELLOW}Continuing anyway...${NC}"
    fi
    echo ""

    # Display summary statistics
    if [ -f "${MULTIVERSE_DIR}/summary_stats.txt" ]; then
        echo -e "${CYAN}📊 SUMMARY STATISTICS:${NC}"
        echo -e "${BLUE}───────────────────────────────────────────────────────────────${NC}"
        cat "${MULTIVERSE_DIR}/summary_stats.txt"
        echo -e "${BLUE}───────────────────────────────────────────────────────────────${NC}"
        echo ""
    fi
fi

################################################################################
# RESULTS SUMMARY
################################################################################

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}RESULTS SUMMARY${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# List output files
echo -e "${CYAN}📁 OUTPUT FILES:${NC}"
echo ""

echo -e "${YELLOW}Pipeline Results (${OUTPUT_DIR}):${NC}"
if [ -d "$OUTPUT_DIR" ]; then
    find "$OUTPUT_DIR" -maxdepth 1 -type f \( -name "*.csv" -o -name "*.png" -o -name "*.txt" \) 2>/dev/null | sort | while read file; do
        SIZE=$(ls -lh "$file" | awk '{print $5}')
        BASENAME=$(basename "$file")
        echo -e "   ${GREEN}✓${NC} ${BASENAME} (${SIZE})"
    done
else
    echo -e "   ${YELLOW}(no results directory)${NC}"
fi
echo ""

if [ -d "$MULTIVERSE_DIR" ]; then
    echo -e "${YELLOW}Multiverse Results (${MULTIVERSE_DIR}):${NC}"
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
    echo ""
fi

################################################################################
# DONE
################################################################################

TOTAL_DURATION=$(($(date +%s) - START_STEP1))

echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                    ✅ PIPELINE COMPLETE                        ║${NC}"
echo -e "${BLUE}║                Total Runtime: ${TOTAL_DURATION}s                           ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${GREEN}🎉 SUCCESS! All analyses complete.${NC}"
echo ""
echo -e "${CYAN}📂 Quick Access to Results:${NC}"
echo ""
echo -e "${YELLOW}1. View hypothesis test results:${NC}"
echo -e "   cat ${OUTPUT_DIR}/hypothesis_results.txt"
echo ""
echo -e "${YELLOW}2. Browse variable distributions:${NC}"
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo -e "   open ${OUTPUT_DIR}/variable_distributions.png"
else
    echo -e "   xdg-open ${OUTPUT_DIR}/variable_distributions.png"
fi
echo ""

if [ -f "${MULTIVERSE_DIR}/spec_table.csv" ]; then
    echo -e "${YELLOW}3. Browse multiverse results:${NC}"
    echo -e "   head -20 ${MULTIVERSE_DIR}/spec_table.csv"
    echo ""
    echo -e "${YELLOW}4. View multiverse visualizations:${NC}"
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo -e "   open ${MULTIVERSE_DIR}/*.png"
    else
        echo -e "   xdg-open ${MULTIVERSE_DIR}/*.png"
    fi
    echo ""
fi

echo -e "${GREEN}必死則生 🐢🐅${NC}"
echo ""
