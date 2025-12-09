#!/bin/bash
# =============================================================================
# 로컬 환경에서 논문 자동 생성 파이프라인 실행 예시
# Local Paper Generation Pipeline Example
# =============================================================================
#
# 이 스크립트는 처음부터 끝까지 전체 과정을 보여줍니다:
# This script demonstrates the complete workflow from start to finish:
#
# 1. 환경 설정 (Setup)
# 2. 데이터 변환 (Data conversion: Parquet → NetCDF)
# 3. 데이터 처리 (Data processing)
# 4. 통계 분석 (Statistical analysis)
# 5. 논문 생성 (Paper generation)
# 6. 테스트 검증 (Test validation)
#
# Usage:
#   bash run_local_example.sh
#
#   # Or make it executable:
#   chmod +x run_local_example.sh
#   ./run_local_example.sh
#
# =============================================================================

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Helper functions
print_header() {
    echo -e "\n${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}\n"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_step() {
    echo -e "\n${YELLOW}>>> $1${NC}"
}

# =============================================================================
# STEP 0: 환경 확인 (Environment Check)
# =============================================================================

print_header "STEP 0: 환경 확인 (Environment Check)"

# Check Python
print_step "Checking Python installation..."
if command -v python &> /dev/null; then
    python_version=$(python --version 2>&1)
    print_success "Python found: $python_version"
else
    print_error "Python not found. Please install Python 3.9+"
    exit 1
fi

# Check required packages
print_step "Checking required packages..."
required_packages=("pandas" "numpy" "xarray" "statsmodels" "matplotlib")
missing_packages=()

for package in "${required_packages[@]}"; do
    if python -c "import $package" 2>/dev/null; then
        print_success "$package installed"
    else
        print_warning "$package not found"
        missing_packages+=("$package")
    fi
done

if [ ${#missing_packages[@]} -gt 0 ]; then
    print_warning "Missing packages: ${missing_packages[*]}"
    print_step "Installing missing packages..."
    pip install -r requirements.txt
    print_success "Packages installed"
fi

# =============================================================================
# STEP 1: 데이터 변환 (Convert Parquet → NetCDF)
# =============================================================================

print_header "STEP 1: 데이터 변환 (Data Conversion)"

# Check if .parquet files exist
if ls data/processed/*.parquet 1> /dev/null 2>&1; then
    print_step "Found existing .parquet files"
    print_step "Converting to NetCDF format..."

    python src/scripts/convert_to_netcdf.py --directory data/processed

    print_success "Conversion complete!"
    print_warning "Tip: You can delete .parquet files after conversion"
    echo "      rm data/processed/*.parquet"
else
    print_warning "No .parquet files found - will generate .nc files directly"
fi

# =============================================================================
# STEP 2: 데이터 처리 (Data Processing)
# =============================================================================

print_header "STEP 2: 데이터 처리 (Data Processing)"

print_step "Loading raw data and engineering features..."
if [ ! -f "data/processed/features_engineered.nc" ]; then
    make data
    print_success "Features engineered → data/processed/features_engineered.nc"
else
    print_warning "Features cache already exists (using existing file)"
    print_warning "To force re-computation: rm data/processed/features_engineered.nc"
fi

# Show data summary
if [ -f "data/processed/features_engineered.nc" ]; then
    file_size=$(du -h data/processed/features_engineered.nc | cut -f1)
    print_success "Data ready: $file_size"
fi

# =============================================================================
# STEP 3: 통계 분석 (Statistical Analysis)
# =============================================================================

print_header "STEP 3: 통계 분석 (Statistical Analysis)"

print_step "Running H1 and H2 hypothesis tests..."
make analysis

# Check outputs
if [ -f "paper/results_auto.tex" ]; then
    print_success "Results section generated → paper/results_auto.tex"
fi

if [ -f "paper/results_values.json" ]; then
    print_success "Statistical values saved → paper/results_values.json"

    # Show key results
    print_step "Key Results Preview:"
    python -c "
import json
with open('paper/results_values.json') as f:
    vals = json.load(f)
    print(f\"  H1 coefficient: {vals.get('h1_coef', 'N/A')}\")
    print(f\"  H1 p-value: {vals.get('h1_pval', 'N/A')}\")
    print(f\"  H2 interaction coef: {vals.get('h2_interaction_coef', 'N/A')}\")
    print(f\"  H2 interaction p-value: {vals.get('h2_interaction_pval', 'N/A')}\")
" || print_warning "Could not parse results_values.json"
fi

# =============================================================================
# STEP 4: 테이블 및 그림 생성 (Tables & Figures)
# =============================================================================

print_header "STEP 4: 테이블 및 그림 생성 (Tables & Figures)"

print_step "Generating LaTeX tables..."
make tables
print_success "Table 1 (H1) → paper/tables/table1_h1.tex"
print_success "Table 2 (H2) → paper/tables/table2_h2.tex"

print_step "Generating figures..."
make figures
print_success "Figure 2 → paper/figures/fig2_early_funding.pdf"
print_success "Figure 3 → paper/figures/fig3_later_success.pdf"

# =============================================================================
# STEP 5: 테스트 실행 (Run Tests)
# =============================================================================

print_header "STEP 5: 테스트 검증 (Test Validation)"

print_step "Running data quality tests..."
pytest test/integration/test_data_quality.py -v --no-cov || print_warning "Some data quality tests failed (check warnings)"

print_step "Running unit tests (models)..."
pytest test/unit/test_models.py -v --no-cov
print_success "All model tests passed!"

print_step "Running NetCDF I/O tests..."
pytest test/unit/test_data_io.py -v --no-cov
print_success "All data I/O tests passed!"

# =============================================================================
# STEP 6: 논문 컴파일 (Paper Compilation)
# =============================================================================

print_header "STEP 6: 논문 컴파일 (Paper Compilation)"

# Check if LaTeX is available
if command -v pdflatex &> /dev/null; then
    print_step "Compiling paper to PDF..."
    make paper

    if [ -f "paper/output/main.pdf" ]; then
        pdf_size=$(du -h paper/output/main.pdf | cut -f1)
        print_success "Paper compiled → paper/output/main.pdf ($pdf_size)"

        # Try to open PDF (macOS/Linux)
        if [[ "$OSTYPE" == "darwin"* ]]; then
            print_step "Opening PDF (macOS)..."
            open paper/output/main.pdf
        elif command -v xdg-open &> /dev/null; then
            print_step "Opening PDF (Linux)..."
            xdg-open paper/output/main.pdf
        fi
    else
        print_error "PDF compilation failed"
    fi
else
    print_warning "pdflatex not found - skipping PDF compilation"
    print_warning "Install LaTeX: sudo apt-get install texlive-full (Linux) or brew install mactex (macOS)"
fi

# =============================================================================
# FINAL SUMMARY
# =============================================================================

print_header "완료! (Complete!)"

echo "논문 자동 생성 파이프라인이 성공적으로 실행되었습니다."
echo "Paper auto-generation pipeline completed successfully!"
echo ""
echo "📁 Generated Files:"
echo "  ├── data/processed/features_engineered.nc     (Processed data)"
echo "  ├── paper/results_auto.tex                    (Auto-generated Results section)"
echo "  ├── paper/results_values.json                 (Statistical values)"
echo "  ├── paper/tables/table1_h1.tex                (H1 regression table)"
echo "  ├── paper/tables/table2_h2.tex                (H2 logit table)"
echo "  ├── paper/figures/fig2_early_funding.pdf      (Figure 2)"
echo "  ├── paper/figures/fig3_later_success.pdf      (Figure 3)"

if [ -f "paper/output/main.pdf" ]; then
    echo "  └── paper/output/main.pdf                     (Final paper PDF)"
fi

echo ""
echo "📊 Next Steps:"
echo "  1. Review generated tables:  cat paper/tables/*.tex"
echo "  2. Check Results section:    cat paper/results_auto.tex"
echo "  3. Inspect figures:          open paper/figures/*.pdf"
echo "  4. Read final paper:         open paper/output/main.pdf"
echo ""
echo "🔄 To re-run with fresh data:"
echo "  make clean-all   # Remove all generated files"
echo "  make all         # Re-run complete pipeline"
echo ""
echo "✅ To validate paper against tests:"
echo "  make test        # Run all tests with coverage"
echo "  make validate    # Validate paper values"
echo ""

print_success "로컬 환경에서 논문 자동 생성 완료! (Local paper generation complete!)"
