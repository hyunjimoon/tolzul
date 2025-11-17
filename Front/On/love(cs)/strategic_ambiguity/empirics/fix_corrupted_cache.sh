#!/bin/bash
################################################################################
# Fix Corrupted Parquet Cache Files
# ==================================
# Use this if you encounter parquet corruption errors:
#   "Parquet magic bytes not found in footer"
#
# This script safely removes corrupted cache files and re-runs feature engineering.
################################################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}     Fix Corrupted Parquet Cache${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════${NC}"
echo ""

# Check if features_all.parquet exists
FEATURES_FILE="data/processed/features_all.parquet"

if [ ! -f "$FEATURES_FILE" ]; then
    echo -e "${YELLOW}⚠️  File not found: $FEATURES_FILE${NC}"
    echo -e "This is fine - it will be created when you run Step 2."
    echo ""
    echo -e "${GREEN}Run: python3 pipeline/02_engineer_features.py${NC}"
    exit 0
fi

# File exists - check if it's corrupted
echo -e "${YELLOW}Checking if $FEATURES_FILE is corrupted...${NC}"

# Try to read the file
if python3 -c "import pandas as pd; pd.read_parquet('$FEATURES_FILE', nrows=1)" 2>/dev/null; then
    echo -e "${GREEN}✓ File is valid!${NC}"
    echo ""
    echo -e "The parquet file is NOT corrupted. The error may have been transient."
    echo -e "Try running the pipeline again: ${GREEN}./run_all.sh${NC}"
    exit 0
fi

# File is corrupted - offer to delete
echo -e "${RED}✗ File is corrupted!${NC}"
echo ""
echo -e "File: $FEATURES_FILE"
echo -e "Size: $(du -h $FEATURES_FILE | cut -f1)"
echo ""
echo -e "${YELLOW}This script will:${NC}"
echo -e "  1. Delete the corrupted file"
echo -e "  2. Re-run Step 2 (feature engineering)"
echo ""

# Ask for confirmation
read -p "Do you want to proceed? (y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}Aborted.${NC}"
    echo ""
    echo -e "To fix manually, run:"
    echo -e "  ${GREEN}rm $FEATURES_FILE${NC}"
    echo -e "  ${GREEN}python3 pipeline/02_engineer_features.py${NC}"
    exit 1
fi

# Delete corrupted file
echo -e "${YELLOW}Deleting corrupted file...${NC}"
rm -f "$FEATURES_FILE"
echo -e "${GREEN}✓ Deleted${NC}"
echo ""

# Re-run feature engineering
echo -e "${YELLOW}Re-running Step 2: Feature Engineering...${NC}"
echo ""
python3 pipeline/02_engineer_features.py

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}✓ SUCCESS${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "Features file has been regenerated successfully!"
    echo -e "You can now resume the pipeline:"
    echo -e "  ${GREEN}./run_all.sh --quick${NC}  (skip Step 1, use existing cache)"
    echo ""
else
    echo ""
    echo -e "${RED}═══════════════════════════════════════════════════════════════════${NC}"
    echo -e "${RED}✗ FAILED${NC}"
    echo -e "${RED}═══════════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "Feature engineering failed. Check the error messages above."
    exit 1
fi
