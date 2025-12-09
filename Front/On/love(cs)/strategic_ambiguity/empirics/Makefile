# Makefile for Paper Generation Pipeline
# =======================================
# From data → 32 paragraphs + tables + figures → final PDF

# Configuration
PYTHON := python
DATA_RAW := data/raw
# Support both .nc (NetCDF) and .parquet formats
# NetCDF is default (no pyarrow dependency required)
DATA_FORMAT := nc
DATA_PROCESSED := data/processed/features_all.$(DATA_FORMAT)
PAPER_DIR := paper
PAPER_OUTPUT := $(PAPER_DIR)/output
PAPER_MAIN := $(PAPER_OUTPUT)/main.pdf

# Intermediate files
RESULTS_AUTO := $(PAPER_DIR)/results_auto.tex
TABLES_DIR := $(PAPER_DIR)/tables
FIGURES_DIR := $(PAPER_DIR)/figures

.PHONY: all data analysis tables figures paper clean help

# ============================================
# Main Targets
# ============================================

## all: Complete pipeline from raw data to final PDF
all: data analysis paper

## help: Show this help message
help:
	@echo "Paper Generation Pipeline"
	@echo "========================="
	@echo ""
	@echo "Main targets:"
	@grep -E '^## ' Makefile | sed 's/## /  /'
	@echo ""
	@echo "Usage:"
	@echo "  make all        # Complete pipeline"
	@echo "  make data       # Process data"
	@echo "  make analysis   # Run statistical tests"
	@echo "  make paper      # Generate paper PDF"
	@echo "  make clean      # Remove generated files"

# ============================================
# Data Processing (Module #14-16)
# ============================================

## data: Process raw data and engineer features
data: $(DATA_PROCESSED)

$(DATA_PROCESSED): $(DATA_RAW)/*.dat
	@echo "=== Step 1: Data Processing ==="
	$(PYTHON) -m src.cli load-data
	$(PYTHON) -m src.cli engineer-features
	@echo "✓ Data processed: $(DATA_PROCESSED)"

# ============================================
# Statistical Analysis (Module #23-27)
# ============================================

## analysis: Run hypothesis tests and generate results
analysis: $(RESULTS_AUTO)

$(RESULTS_AUTO): $(DATA_PROCESSED)
	@echo "=== Step 2: Statistical Analysis ==="
	$(PYTHON) src/scripts/generate_paper_results_section.py \
		--data $(DATA_PROCESSED) \
		--output $(PAPER_DIR)
	@echo "✓ Results generated: $(RESULTS_AUTO)"

# ============================================
# Tables (Module #23-24)
# ============================================

## tables: Generate LaTeX tables
tables: $(TABLES_DIR)/table1_h1.tex $(TABLES_DIR)/table2_h2.tex

$(TABLES_DIR)/table1_h1.tex $(TABLES_DIR)/table2_h2.tex: $(DATA_PROCESSED)
	@echo "=== Step 3: Table Generation ==="
	$(PYTHON) src/scripts/generate_paper_tables.py \
		--data $(DATA_PROCESSED) \
		--output $(TABLES_DIR)
	@echo "✓ Tables generated: $(TABLES_DIR)/*.tex"

# ============================================
# Figures (Module #23-25)
# ============================================

## figures: Generate figures
figures: $(FIGURES_DIR)/fig2_early_funding.pdf $(FIGURES_DIR)/fig3_later_success.pdf

$(FIGURES_DIR)/fig2_early_funding.pdf $(FIGURES_DIR)/fig3_later_success.pdf: $(DATA_PROCESSED)
	@echo "=== Step 4: Figure Generation ==="
	$(PYTHON) -m src.cli generate-plots --dataset all --output $(FIGURES_DIR)
	@echo "✓ Figures generated: $(FIGURES_DIR)/*.pdf"

# ============================================
# Paper Compilation
# ============================================

## paper: Compile LaTeX to PDF
paper: $(PAPER_MAIN)

$(PAPER_MAIN): $(RESULTS_AUTO) $(TABLES_DIR)/*.tex $(FIGURES_DIR)/*.pdf
	@echo "=== Step 5: Paper Compilation ==="
	@echo "Compiling LaTeX..."
	cd $(PAPER_OUTPUT) && pdflatex main.tex
	cd $(PAPER_OUTPUT) && bibtex main
	cd $(PAPER_OUTPUT) && pdflatex main.tex
	cd $(PAPER_OUTPUT) && pdflatex main.tex
	@echo "✓ Paper compiled: $(PAPER_MAIN)"

# ============================================
# Testing
# ============================================

## test: Run tests to verify paper results
test:
	@echo "=== Running Tests ==="
	pytest test/integration/test_paper_results.py -v
	@echo "✓ All tests passed"

## test-quick: Run quick unit tests only
test-quick:
	pytest test/unit/test_models.py -v --no-cov

# ============================================
# Utilities
# ============================================

## clean: Remove generated files
clean:
	@echo "Cleaning generated files..."
	rm -rf $(PAPER_OUTPUT)/*.aux $(PAPER_OUTPUT)/*.log $(PAPER_OUTPUT)/*.bbl
	rm -rf $(PAPER_OUTPUT)/*.blg $(PAPER_OUTPUT)/*.out $(PAPER_OUTPUT)/*.toc
	rm -rf $(TABLES_DIR)/*.tex
	rm -rf $(FIGURES_DIR)/*.pdf $(FIGURES_DIR)/*.png
	rm -f $(RESULTS_AUTO)
	@echo "✓ Cleaned"

## clean-all: Remove all generated files including data
clean-all: clean
	rm -f $(DATA_PROCESSED)
	rm -rf data/cache/*
	@echo "✓ Deep clean complete"

## watch: Auto-rebuild paper on file changes (requires entr)
watch:
	@echo "Watching for changes... (Ctrl+C to stop)"
	ls $(PAPER_DIR)/*.tex $(TABLES_DIR)/*.tex | entr make paper

# ============================================
# Quick Commands
# ============================================

## quick: Quick rebuild (skip data processing)
quick: analysis paper

## results-only: Regenerate Results section only
results-only: analysis
	cd $(PAPER_OUTPUT) && pdflatex main.tex

## validate: Validate paper against tests
validate: test
	@echo "=== Validating Paper Results ==="
	$(PYTHON) src/scripts/validate_paper_values.py
	@echo "✓ Paper values match test expectations"

# ============================================
# CI/CD Integration
# ============================================

## ci: CI/CD pipeline (run on GitHub Actions)
ci: test data analysis tables figures
	@echo "✓ CI pipeline complete"

# ============================================
# Info
# ============================================

## info: Show pipeline status
info:
	@echo "Paper Generation Pipeline Status"
	@echo "================================"
	@echo ""
	@echo "Data:"
	@test -f $(DATA_PROCESSED) && echo "  ✓ $(DATA_PROCESSED)" || echo "  ✗ Data not processed"
	@echo ""
	@echo "Analysis:"
	@test -f $(RESULTS_AUTO) && echo "  ✓ $(RESULTS_AUTO)" || echo "  ✗ Results not generated"
	@echo ""
	@echo "Tables:"
	@test -f $(TABLES_DIR)/table1_h1.tex && echo "  ✓ Table 1" || echo "  ✗ Table 1 missing"
	@test -f $(TABLES_DIR)/table2_h2.tex && echo "  ✓ Table 2" || echo "  ✗ Table 2 missing"
	@echo ""
	@echo "Figures:"
	@test -f $(FIGURES_DIR)/fig2_early_funding.pdf && echo "  ✓ Figure 2" || echo "  ✗ Figure 2 missing"
	@test -f $(FIGURES_DIR)/fig3_later_success.pdf && echo "  ✓ Figure 3" || echo "  ✗ Figure 3 missing"
	@echo ""
	@echo "Paper:"
	@test -f $(PAPER_MAIN) && echo "  ✓ $(PAPER_MAIN)" || echo "  ✗ Paper not compiled"
