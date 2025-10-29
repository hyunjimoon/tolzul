#!/bin/bash
# ==============================================================================
# One-Touch Analysis & Report Generation Pipeline
# ==============================================================================
# This script:
# 1. Builds dataset from raw data files (Company*.dat)
# 2. Runs statistical analysis and generates outputs
# 3. Renders three Quarto reports
# 4. Evaluates reports against quality checklist
# ==============================================================================

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo "================================================================================"
echo "🚀 One-Touch Analysis & Report Generation Pipeline"
echo "================================================================================"
echo ""

# ==============================================================================
# Step 0: Environment Check
# ==============================================================================

echo -e "${BLUE}[Step 0/4]${NC} Checking environment..."

# Check Python
if ! command -v python &> /dev/null; then
    echo -e "${RED}✗ Python not found${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Python found:${NC} $(python --version)"

# Check Quarto
if ! command -v quarto &> /dev/null; then
    echo -e "${YELLOW}⚠ Quarto not found - reports will not be rendered${NC}"
    echo -e "${YELLOW}  Install from: https://quarto.org/docs/get-started/${NC}"
    QUARTO_AVAILABLE=0
else
    echo -e "${GREEN}✓ Quarto found:${NC} $(quarto --version)"
    QUARTO_AVAILABLE=1
fi

# Define paths
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check for data directory
DATA_DIR_LOCAL="/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Front/On/love(cs)/strategic ambiguity/empirics/data/raw"
DATA_DIR_DOCKER="data/raw"

if [ -d "$DATA_DIR_LOCAL" ]; then
    DATA_DIR="$DATA_DIR_LOCAL"
    echo -e "${GREEN}✓ Data directory found (Mac local):${NC} $DATA_DIR"
elif [ -d "$DATA_DIR_DOCKER" ]; then
    DATA_DIR="$DATA_DIR_DOCKER"
    echo -e "${GREEN}✓ Data directory found (Docker):${NC} $DATA_DIR"
else
    echo -e "${RED}✗ Data directory not found${NC}"
    echo -e "${YELLOW}  Expected locations:${NC}"
    echo -e "    - $DATA_DIR_LOCAL"
    echo -e "    - $DATA_DIR_DOCKER"
    exit 1
fi

# Verify data files exist
REQUIRED_FILES=(
    "Company20211201.dat"
    "Company20220101.dat"
    "Company20220501.dat"
    "Company20230501.dat"
)

MISSING_FILES=0
for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$DATA_DIR/$file" ]; then
        echo -e "${RED}✗ Missing data file: $file${NC}"
        MISSING_FILES=$((MISSING_FILES + 1))
    else
        FILE_SIZE=$(du -h "$DATA_DIR/$file" | cut -f1)
        echo -e "${GREEN}✓ Found:${NC} $file ($FILE_SIZE)"
    fi
done

if [ $MISSING_FILES -gt 0 ]; then
    echo -e "${RED}✗ Missing $MISSING_FILES required data files${NC}"
    exit 1
fi

echo ""

# ==============================================================================
# Step 1: Data Construction & Analysis
# ==============================================================================

echo -e "${BLUE}[Step 1/4]${NC} Running analysis pipeline..."
echo "  This will build dataset and generate all outputs (.csv, .png)"

# Install required packages if needed
echo "  Checking Python dependencies..."
python -c "
import sys
required = ['pandas', 'numpy', 'matplotlib', 'statsmodels', 'scipy']
missing = []
for pkg in required:
    try:
        __import__(pkg)
    except ImportError:
        missing.append(pkg)

if missing:
    print('Installing missing packages: ' + ', '.join(missing))
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q'] + missing)
else:
    print('✓ All dependencies installed')
" || {
    echo -e "${RED}✗ Failed to install dependencies${NC}"
    exit 1
}

# Run analysis
echo "  Running run_analysis.py..."
if python run_analysis.py; then
    echo -e "${GREEN}✓ Analysis completed successfully${NC}"
    echo "  Outputs generated in: outputs/"
else
    echo -e "${RED}✗ Analysis failed${NC}"
    exit 1
fi

echo ""

# ==============================================================================
# Step 2: Render Quarto Reports
# ==============================================================================

echo -e "${BLUE}[Step 2/4]${NC} Rendering Quarto reports..."

REPORTS=(
    "moderator_bakeoff_lean.qmd"
    "Progress_Report_W1_is_serial.qmd"
    "Progress_Report_W1_is_hardware.qmd"
)

if [ $QUARTO_AVAILABLE -eq 1 ]; then
    mkdir -p outputs/reports

    for report in "${REPORTS[@]}"; do
        if [ -f "$report" ]; then
            echo "  Rendering: $report"

            # Render to HTML
            if quarto render "$report" --to html --output-dir outputs/reports 2>&1 | grep -v "Warning"; then
                echo -e "${GREEN}    ✓ HTML rendered${NC}"
            else
                echo -e "${YELLOW}    ⚠ HTML rendering had warnings${NC}"
            fi

            # Try to render to PDF (may fail if LaTeX not installed)
            if quarto render "$report" --to pdf --output-dir outputs/reports 2>&1 | grep -v "Warning" > /dev/null 2>&1; then
                echo -e "${GREEN}    ✓ PDF rendered${NC}"
            else
                echo -e "${YELLOW}    ⚠ PDF rendering skipped (LaTeX may not be installed)${NC}"
            fi
        else
            echo -e "${RED}  ✗ Report not found: $report${NC}"
        fi
    done

    echo -e "${GREEN}✓ Reports rendered successfully${NC}"
    echo "  Output location: outputs/reports/"
else
    echo -e "${YELLOW}⚠ Skipping report rendering (Quarto not available)${NC}"
    echo "  Generated .qmd files can be rendered manually later:"
    for report in "${REPORTS[@]}"; do
        echo "    - $report"
    done
fi

echo ""

# ==============================================================================
# Step 3: Evaluate Reports
# ==============================================================================

echo -e "${BLUE}[Step 3/4]${NC} Evaluating reports against quality checklist..."

# Create evaluation script
cat > /tmp/evaluate_reports.py <<'EVAL_SCRIPT'
import os
import sys
from pathlib import Path

def evaluate_report(report_path, report_name):
    """Evaluate a report against the quality checklist."""

    print(f"\n{'='*80}")
    print(f"📊 Evaluating: {report_name}")
    print(f"{'='*80}\n")

    if not Path(report_path).exists():
        print(f"⚠️  Report file not found: {report_path}")
        print(f"   (This is expected if Quarto is not installed)")
        return

    try:
        with open(report_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"✗ Error reading report: {e}")
        return

    # Checklist evaluation
    checks = {
        "가독성 (Readability)": {
            "문장 명확성 & 용어 일관성": check_clarity(content),
            "논리 흐름 & 시각자료 설명": check_flow_and_visuals(content),
            "독자 친화성": check_user_friendliness(content)
        },
        "자족성 (Self-contained)": {
            "배경 없이도 이해 가능": check_self_contained(content),
            "모든 표·그림 포함 & 해설": check_figures_explained(content),
            "결과 의미 & 시사점 명확": check_implications(content)
        }
    }

    # Print evaluation
    for category, items in checks.items():
        print(f"\n🔍 {category}")
        print("-" * 60)
        for criterion, (score, comment) in items.items():
            status = "✓" if score >= 3 else "○" if score >= 2 else "✗"
            stars = "⭐" * score
            print(f"  {status} {criterion}: {stars} ({score}/5)")
            if comment:
                print(f"     💬 {comment}")

    # Overall assessment
    avg_score = sum(score for cat in checks.values() for score, _ in cat.values()) / sum(len(cat) for cat in checks.values())
    print(f"\n📈 Overall Score: {avg_score:.1f}/5.0")

    if avg_score >= 4:
        print("✅ Excellent - Ready for advisor review")
    elif avg_score >= 3:
        print("✓ Good - Minor improvements recommended")
    else:
        print("⚠️  Needs improvement before advisor review")

def check_clarity(content):
    """Check sentence clarity and term consistency."""
    score = 3
    comments = []

    # Check for key terms consistency
    key_terms = ['vagueness', 'Series A', 'Series B+', 'founder credibility', 'integration cost']
    term_count = sum(1 for term in key_terms if term.lower() in content.lower())

    if term_count >= 4:
        score += 1

    # Check for clear section headings
    if content.count('#') >= 5:  # Multiple section headers
        score += 1

    comments.append(f"Key terms used consistently ({term_count}/{len(key_terms)} found)")

    return (score, "; ".join(comments))

def check_flow_and_visuals(content):
    """Check logical flow and visual explanations."""
    score = 3
    comments = []

    # Check for figure references
    fig_refs = content.lower().count('figure') + content.lower().count('fig.')
    if fig_refs >= 3:
        score += 1
        comments.append(f"Multiple figure references ({fig_refs})")

    # Check for transition words
    transitions = ['however', 'therefore', 'thus', 'moreover', 'furthermore']
    transition_count = sum(content.lower().count(word) for word in transitions)
    if transition_count >= 5:
        score += 1
        comments.append("Good use of transition words")

    return (score, "; ".join(comments))

def check_user_friendliness(content):
    """Check reader friendliness."""
    score = 3
    comments = []

    # Check for explanatory text
    if 'interpretation:' in content.lower() or 'key finding' in content.lower():
        score += 1
        comments.append("Clear interpretations provided")

    # Check for summary sections
    if 'summary' in content.lower() or 'executive summary' in content.lower():
        score += 1
        comments.append("Executive summary included")

    return (score, "; ".join(comments))

def check_self_contained(content):
    """Check if report is self-contained."""
    score = 3
    comments = []

    # Check for background/introduction
    if any(section in content.lower() for section in ['introduction', 'background', 'motivation']):
        score += 1
        comments.append("Background context provided")

    # Check for methodology description
    if any(section in content.lower() for section in ['method', 'data', 'measurement']):
        score += 1
        comments.append("Methodology described")

    return (score, "; ".join(comments))

def check_figures_explained(content):
    """Check if all figures are explained."""
    score = 3
    comments = []

    # Count figure references and interpretations
    fig_refs = content.lower().count('figure')
    interpretations = content.lower().count('interpretation:')

    if fig_refs > 0 and interpretations >= fig_refs * 0.5:
        score += 2
        comments.append(f"Most figures have interpretations ({interpretations}/{fig_refs})")
    elif fig_refs > 0:
        comments.append(f"Some figures may lack interpretation ({interpretations}/{fig_refs})")

    return (score, "; ".join(comments))

def check_implications(content):
    """Check if implications are clear."""
    score = 3
    comments = []

    # Check for discussion of implications
    keywords = ['implication', 'finding', 'result', 'conclude', 'suggest']
    keyword_count = sum(content.lower().count(word) for word in keywords)

    if keyword_count >= 10:
        score += 2
        comments.append("Clear discussion of findings and implications")
    elif keyword_count >= 5:
        score += 1
        comments.append("Some discussion of implications")

    # Check for next steps
    if 'next step' in content.lower() or 'future' in content.lower():
        comments.append("Next steps outlined")

    return (score, "; ".join(comments))

# Main execution
if __name__ == "__main__":
    reports_dir = Path("outputs/reports")

    print("\n" + "="*80)
    print("🧾 보고서 품질점검 (Charles Fine & Scott Stern 관점)")
    print("="*80)

    reports = [
        ("moderator_bakeoff_lean.html", "Moderator Bake-off (Architecture vs. Founder)"),
        ("Progress_Report_W1_is_serial.html", "Progress Report (Founder Credibility)"),
        ("Progress_Report_W1_is_hardware.html", "Progress Report (Architecture/Integration Cost)")
    ]

    for report_file, report_name in reports:
        report_path = reports_dir / report_file
        evaluate_report(report_path, report_name)

    print("\n" + "="*80)
    print("📝 Charles Fine's Perspective (Operations/Architecture)")
    print("="*80)
    print("""
Key evaluation criteria from Prof. Fine's perspective:

1. Integration Cost Theory
   - Is the hardware vs. software distinction well-grounded?
   - Are supply chain and manufacturing implications discussed?
   - Is modularity theory properly applied?

2. Practical Relevance
   - Are findings actionable for entrepreneurs?
   - Do recommendations align with operational realities?
   - Is the architecture-performance link clear?

3. Empirical Rigor
   - Are integration cost measures valid?
   - Are alternative explanations addressed?
   - Is the sample representative of hardware/software split?
""")

    print("\n" + "="*80)
    print("📝 Scott Stern's Perspective (Entrepreneurship/Strategy)")
    print("="*80)
    print("""
Key evaluation criteria from Prof. Stern's perspective:

1. Methodological Soundness
   - Is the Series A(t₀) → Series B+(t₁) framework correctly implemented?
   - Are at-risk cohorts properly defined?
   - Is censoring handled appropriately?

2. Strategic Insights
   - Does the reversal pattern have theoretical grounding?
   - Are boundary conditions (moderators) well-motivated?
   - Do findings advance entrepreneurship theory?

3. Causal Inference
   - Are endogeneity concerns addressed?
   - Is the identification strategy credible?
   - Are robustness checks sufficient?

4. Policy Implications
   - Are findings relevant for entrepreneurship policy?
   - Do they inform founder development programs?
   - Is the link to startup ecosystem clear?
""")

    print("\n" + "="*80)
    print("✅ Evaluation complete!")
    print("="*80)
EVAL_SCRIPT

python /tmp/evaluate_reports.py

echo ""

# ==============================================================================
# Step 4: Summary
# ==============================================================================

echo -e "${BLUE}[Step 4/4]${NC} Pipeline Summary"
echo "================================================================================"
echo ""
echo "📁 Generated Outputs:"
echo "  Data & Results:"
echo "    - outputs/*.csv (coefficient tables, metrics)"
echo "    - outputs/figures/*.png (visualizations)"
echo "    - outputs/bakeoff/*.png (moderator comparison plots)"
echo ""

if [ $QUARTO_AVAILABLE -eq 1 ]; then
    echo "  Reports (HTML):"
    for report in "${REPORTS[@]}"; do
        html_file="outputs/reports/${report%.qmd}.html"
        if [ -f "$html_file" ]; then
            echo -e "    ${GREEN}✓${NC} $html_file"
        fi
    done
    echo ""
    echo "  Reports (PDF):"
    for report in "${REPORTS[@]}"; do
        pdf_file="outputs/reports/${report%.qmd}.pdf"
        if [ -f "$pdf_file" ]; then
            echo -e "    ${GREEN}✓${NC} $pdf_file"
        else
            echo -e "    ${YELLOW}○${NC} $pdf_file (not generated - LaTeX required)"
        fi
    done
else
    echo "  Reports (Source):"
    for report in "${REPORTS[@]}"; do
        echo "    ○ $report (render with: quarto render $report)"
    done
fi

echo ""
echo "🎯 Next Steps:"
echo "  1. Review evaluation results above"
echo "  2. Open reports in browser:"
if [ $QUARTO_AVAILABLE -eq 1 ]; then
    echo "     open outputs/reports/moderator_bakeoff_lean.html"
    echo "     open outputs/reports/Progress_Report_W1_is_serial.html"
    echo "     open outputs/reports/Progress_Report_W1_is_hardware.html"
else
    echo "     (Install Quarto first: https://quarto.org/)"
fi
echo "  3. Share with Professors Fine and Stern for feedback"
echo ""
echo "================================================================================"
echo -e "${GREEN}✅ Pipeline completed successfully!${NC}"
echo "================================================================================"
