#!/bin/bash
# Quick Start Script - One-touch execution test

set -e  # Exit on error

echo "=================================="
echo "🚀 Quick Start - One-Touch Test"
echo "=================================="
echo ""

# 1. Check Python
echo "1️⃣ Checking Python..."
if ! command -v python &> /dev/null; then
    echo "❌ Python not found. Please install Python 3.7+"
    exit 1
fi
python --version
echo ""

# 2. Check required packages
echo "2️⃣ Checking packages..."
required_packages="pandas numpy matplotlib statsmodels scikit-learn seaborn scipy"
missing=""
for pkg in $required_packages; do
    if ! python -c "import $pkg" 2>/dev/null; then
        missing="$missing $pkg"
    fi
done

if [ -n "$missing" ]; then
    echo "⚠️  Missing packages:$missing"
    echo "Installing..."
    pip install $missing
fi
echo "✅ All packages installed"
echo ""

# 3. Check data
echo "3️⃣ Checking dataset..."
if [ ! -f "outputs/h2_analysis_dataset.csv" ]; then
    echo "⚠️  Dataset not found. Generating synthetic data..."
    python generate_synthetic_data.py
fi
echo "✅ Dataset ready"
echo ""

# 4. Run test
echo "4️⃣ Running one-touch test..."
echo ""
python test_one_touch.py

# 5. Show results
echo ""
echo "=================================="
echo "✅ Test Complete!"
echo "=================================="
echo ""
echo "📊 Generated files:"
echo ""
ls -lh outputs/h*.csv 2>/dev/null || echo "  (no CSV files)"
echo ""
ls -lh outputs/figures/*.png 2>/dev/null || echo "  (no figures)"
echo ""
echo "To view figures:"
echo "  macOS:  open outputs/figures/Figure_1_Reversal.png"
echo "  Linux:  xdg-open outputs/figures/Figure_1_Reversal.png"
echo "  Windows: start outputs/figures/Figure_1_Reversal.png"
echo ""
