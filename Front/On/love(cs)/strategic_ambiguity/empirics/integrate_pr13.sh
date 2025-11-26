#!/bin/bash
# Integration Plan: PR #13 + Paper Generation Pipeline
# ======================================================

set -e  # Exit on error

echo "🔄 Paper Pipeline Integration Strategy"
echo "======================================"
echo ""

# ============================================
# STEP 1: Merge PR #13 First
# ============================================
echo "📥 STEP 1: Merge PR #13"
echo "----------------------"
echo "Manual action required:"
echo "1. Go to https://github.com/hyunjimoon/empirics_ent_strat_ops/pull/13"
echo "2. Review changes (6개 산업비교, 2D framework, Makefile)"
echo "3. Click 'Squash and merge'"
echo "4. Wait for merge to complete"
echo ""
read -p "Press Enter when PR #13 is merged..."

# ============================================
# STEP 2: Update Current Branch
# ============================================
echo ""
echo "🔄 STEP 2: Rebase on Latest Main"
echo "--------------------------------"

# Fetch latest
git fetch origin

# Checkout main to get latest
git checkout main
git pull origin main

# Rebase paper generation branch
git checkout claude/refine-paper-generation-01X6QniGETpjbK8cxEpXwDVq
git rebase main

echo "✅ Rebase complete"

# ============================================
# STEP 3: Run PR #13 Pipeline
# ============================================
echo ""
echo "📊 STEP 3: Generate Latest Analysis Results"
echo "-------------------------------------------"

# Use Makefile from PR #13
if [ -f Makefile ]; then
    echo "Found Makefile, running analysis..."
    make data
    make analysis
    echo "✅ Analysis complete"
else
    echo "⚠️  No Makefile found, using CLI directly"
    python -m src.cli load-data
    python -m src.cli engineer-features
    python -m src.cli run-models --dataset all
fi

# ============================================
# STEP 4: Generate Paper Sections
# ============================================
echo ""
echo "📝 STEP 4: Generate Paper Sections + Poster"
echo "-------------------------------------------"

cd src/scripts/paper_generation
python generate_all.py

echo "✅ Paper generation complete"

# ============================================
# STEP 5: Verify Integration
# ============================================
echo ""
echo "🔍 STEP 5: Verify Output"
echo "------------------------"

# Check if results exist
if [ -f "outputs/all/models/h1_coefficients.csv" ]; then
    echo "✅ H1 results found"
else
    echo "❌ H1 results missing"
fi

if [ -f "outputs/all/models/h2_main_coefficients.csv" ]; then
    echo "✅ H2 results found"
else
    echo "❌ H2 results missing"
fi

# Check paper sections
if [ -f "src/scripts/paper_generation/output/01_Introduction.md" ]; then
    echo "✅ Paper sections generated"
else
    echo "❌ Paper sections missing"
fi

# Check poster
if [ -f "src/scripts/paper_generation/output/07_Poster.svg" ]; then
    echo "✅ Poster generated"
else
    echo "❌ Poster missing"
fi

# ============================================
# STEP 6: Test Industry-Specific Generation
# ============================================
echo ""
echo "🏭 STEP 6: Test Industry-Specific Paper"
echo "---------------------------------------"

# Generate for quantum industry
echo "Generating quantum industry paper..."
cd ../../..
python -m src.cli run-models --dataset quantum

cd src/scripts/paper_generation
python generate_all.py --dataset quantum 2>/dev/null || echo "Note: --dataset flag not yet implemented"

# ============================================
# DONE
# ============================================
echo ""
echo "🎉 Integration Complete!"
echo "======================="
echo ""
echo "Generated files:"
echo "├─ outputs/all/models/*.csv (from PR #13 analysis)"
echo "├─ src/scripts/paper_generation/output/*.md (paper sections)"
echo "└─ src/scripts/paper_generation/output/07_Poster.svg (poster)"
echo ""
echo "Next steps:"
echo "1. Review generated sections: cat src/scripts/paper_generation/output/01_Introduction.md"
echo "2. View poster: open src/scripts/paper_generation/output/07_Poster.svg"
echo "3. Push integrated branch"
echo "4. Create new PR for merged work"
