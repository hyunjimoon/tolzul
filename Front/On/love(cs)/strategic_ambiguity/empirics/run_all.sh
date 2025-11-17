#!/bin/bash
################################################################################
# Promise Precision Thesis - Complete Analysis Pipeline
# ======================================================
# Executes full analysis for three dataset variants:
#   1. All companies
#   2. Quantum computing companies
#   3. Transportation & mobility companies
#
# Pipeline Steps:
#   01. Load and cache raw .dat files (parquet speedup)
#   02. Engineer features with StrategicVaguenessScorerV2
#   03. Filter datasets into three variants
#   04. Run H1/H2 models for each dataset
#   05. Generate F3a interaction plots for each dataset
#
# Usage:
#   ./run_all.sh              # Run full pipeline for all datasets
#   ./run_all.sh --quick      # Skip data loading (use cache)
#   ./run_all.sh --dataset quantum   # Run only for quantum dataset
#
# Output Structure:
#   outputs/all/              # All companies results
#   outputs/quantum/          # Quantum-only results
#   outputs/transportation/   # Transportation-only results
################################################################################

set -e  # Exit on error
set -u  # Exit on undefined variable

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Parse arguments
QUICK_MODE=false
DATASET_FILTER="all"

while [[ $# -gt 0 ]]; do
    case $1 in
        --quick)
            QUICK_MODE=true
            shift
            ;;
        --dataset)
            DATASET_FILTER="$2"
            shift 2
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            echo "Usage: $0 [--quick] [--dataset {all|quantum|transportation}]"
            exit 1
            ;;
    esac
done

# Validate dataset filter
if [[ ! "$DATASET_FILTER" =~ ^(all|quantum|transportation)$ ]]; then
    echo -e "${RED}Invalid dataset: $DATASET_FILTER${NC}"
    echo "Valid options: all, quantum, transportation"
    exit 1
fi

# Header
echo -e "${BLUE}═══════════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}     Promise Precision Thesis - Full Analysis Pipeline${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "Dataset filter: ${GREEN}$DATASET_FILTER${NC}"
echo -e "Quick mode: ${GREEN}$QUICK_MODE${NC}"
echo ""

# Start timer
START_TIME=$(date +%s)

# ============================================================================
# STEP 1: Load Data
# ============================================================================
if [ "$QUICK_MODE" = false ]; then
    echo -e "${YELLOW}▶ STEP 1: Load Data${NC}"
    echo "────────────────────────────────────────────────────────────────────"
    python3 pipeline/01_load_data.py
    echo ""
else
    echo -e "${YELLOW}⏭  STEP 1: Skipped (quick mode)${NC}"
    echo ""
fi

# ============================================================================
# STEP 2: Engineer Features
# ============================================================================
echo -e "${YELLOW}▶ STEP 2: Engineer Features${NC}"
echo "────────────────────────────────────────────────────────────────────"
python3 pipeline/02_engineer_features.py
echo ""

# ============================================================================
# STEP 3: Filter Datasets
# ============================================================================
echo -e "${YELLOW}▶ STEP 3: Filter Datasets${NC}"
echo "────────────────────────────────────────────────────────────────────"
python3 pipeline/03_filter_datasets.py
echo ""

# ============================================================================
# STEP 4: Run Models
# ============================================================================
echo -e "${YELLOW}▶ STEP 4: Run Models${NC}"
echo "────────────────────────────────────────────────────────────────────"

if [ "$DATASET_FILTER" = "all" ]; then
    # Run for all three datasets
    echo -e "${BLUE}Running models for all datasets...${NC}"
    python3 pipeline/04_run_models.py all
    python3 pipeline/04_run_models.py quantum
    python3 pipeline/04_run_models.py transportation
else
    # Run for specified dataset only
    echo -e "${BLUE}Running models for $DATASET_FILTER dataset...${NC}"
    python3 pipeline/04_run_models.py "$DATASET_FILTER"
fi
echo ""

# ============================================================================
# STEP 5: Generate Plots
# ============================================================================
echo -e "${YELLOW}▶ STEP 5: Generate Plots${NC}"
echo "────────────────────────────────────────────────────────────────────"

if [ "$DATASET_FILTER" = "all" ]; then
    # Generate for all three datasets
    echo -e "${BLUE}Generating plots for all datasets...${NC}"
    python3 pipeline/05_generate_plots.py all
    python3 pipeline/05_generate_plots.py quantum
    python3 pipeline/05_generate_plots.py transportation
else
    # Generate for specified dataset only
    echo -e "${BLUE}Generating plots for $DATASET_FILTER dataset...${NC}"
    python3 pipeline/05_generate_plots.py "$DATASET_FILTER"
fi
echo ""

# ============================================================================
# Summary
# ============================================================================
END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))
MINUTES=$((ELAPSED / 60))
SECONDS=$((ELAPSED % 60))

echo -e "${GREEN}═══════════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✓ PIPELINE COMPLETE${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "Total time: ${GREEN}${MINUTES}m ${SECONDS}s${NC}"
echo ""
echo -e "${BLUE}Output directories:${NC}"

if [ "$DATASET_FILTER" = "all" ]; then
    echo "  📁 outputs/all/models/           - All companies results"
    echo "  📁 outputs/all/figures/          - All companies plots"
    echo "  📁 outputs/quantum/models/       - Quantum companies results"
    echo "  📁 outputs/quantum/figures/      - Quantum companies plots"
    echo "  📁 outputs/transportation/models/ - Transportation companies results"
    echo "  📁 outputs/transportation/figures/ - Transportation companies plots"
else
    echo "  📁 outputs/$DATASET_FILTER/models/   - Model results"
    echo "  📁 outputs/$DATASET_FILTER/figures/  - Plots"
fi

echo ""
echo -e "${BLUE}Key outputs:${NC}"
echo "  📊 h1_coefficients.csv       - Early funding ~ vagueness"
echo "  📊 h2_main_coefficients.csv  - Growth ~ vagueness × hardware"
echo "  📈 F3a_interaction.png       - THE MONEY PLOT (scissors pattern)"
echo ""
echo -e "${GREEN}Ready for advisor presentation! 🎉${NC}"
echo ""
