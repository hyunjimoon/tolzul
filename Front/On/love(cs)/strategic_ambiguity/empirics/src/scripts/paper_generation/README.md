# Paper Generation Pipeline

**Automated generation of academic paper sections from empirical results**

## Overview

This directory contains scripts to automatically generate markdown-formatted academic paper sections based on empirical analysis results. Each script:

1. **Loads empirical results** from `outputs/all/models/` (CSV files)
2. **Generates structured markdown** with data-driven insights
3. **Includes META_PROMPT** for LLM-based expansion
4. **Outputs to** `src/scripts/paper_generation/output/`

## Quick Start

### Generate All Sections

```bash
cd src/scripts/paper_generation
python generate_all.py
```

### Generate Specific Sections

```bash
# Generate only Introduction and Results
python generate_all.py --sections 1 5

# Generate only Methodology
python generate_all.py --sections 4
```

### Generate Individual Sections

```bash
python generate_01_intro.py
python generate_02_litreview.py
python generate_03_conceptual.py
python generate_04_method.py
python generate_05_results.py
python generate_06_discussion.py
python generate_07_poster.py                    # 현지의 포스터 공방
python generate_08_industry_comparison.py       # PR #13 integration
```

### Generate Visual Poster Only

```bash
# Generate 2×2 grid SVG poster (30-second visual summary)
python generate_all.py --sections 7
```

### Generate Industry Comparison Only

```bash
# Generate 6-industry comparison section (PR #13 integration)
python generate_all.py --sections 8
```

## Directory Structure

```
src/scripts/paper_generation/
├── __init__.py                        # Common configuration
├── README.md                          # This file
├── generate_all.py                    # Master script (runs all)
├── generate_01_intro.py               # Section 1: Introduction
├── generate_02_litreview.py           # Section 2: Literature Review
├── generate_03_conceptual.py          # Section 3: Conceptual Model
├── generate_04_method.py              # Section 4: Methodology
├── generate_05_results.py             # Section 5: Results
├── generate_06_discussion.py          # Section 6: Discussion
├── generate_07_poster.py              # Section 7: Poster (현지의 포스터 공방)
├── generate_08_industry_comparison.py # Section 8: Industry Comparison (PR #13)
└── output/                            # Generated markdown files
    ├── 01_Introduction.md
    ├── 02_LiteratureReview.md
    ├── 03_Conceptual_Model.md
    ├── 04_Method.md
    ├── 05_Results.md
    ├── 06_Discussion.md
    ├── 07_Poster.svg                  # 2×2 visual poster (SVG)
    ├── 07_Poster.md                   # Poster description
    ├── 08_IndustryComparison.md       # 6-industry analysis
    └── spec_curve_analysis.png        # Generated figure
```

## Script Summaries

### 1. `generate_01_intro.py` - Introduction

**Hook**: Tesla vs Bosch case study (vague vs specific positioning)

**Data Used**:
- `outputs/all/models/h1_coefficients.csv` (Early funding ~ Vagueness)
- `outputs/all/models/h2_main_coefficients.csv` (Growth ~ Vagueness × Hardware)

**Key Outputs**:
- Opening paradox: Why does vagueness help some ventures but hurt others?
- Preview of H1/H2 findings with actual coefficients
- Three theoretical contributions
- Paper roadmap

**META_PROMPT Focus**: Scholarly yet accessible tone, vivid case studies before abstractions

---

### 2. `generate_02_litreview.py` - Literature Review

**Theoretical Frameworks**:
1. Information Economics (vagueness as adverse selection - NEGATIVE)
2. Real Options Theory (vagueness as flexibility - POSITIVE)
3. Modularity Theory (vagueness effect is CONDITIONAL)

**Key Outputs**:
- Critical review of each perspective
- Identification of theoretical gaps
- Hypothesis development (H1, H2a, H2b)

**META_PROMPT Focus**: Authoritative but critical, build tension between competing theories

---

### 3. `generate_03_conceptual.py` - Conceptual Model

**Framework**: 4-Module System
1. **Customer Heterogeneity** (high diversity → vagueness beneficial)
2. **Technology Modularity** (CORE - our focus)
3. **Organizational Slack** (resources buffer vagueness risk)
4. **Competitive Intensity** (crowded markets → vagueness differentiates)

**Data Used**:
- `data/processed/analysis_panel.csv` (for descriptive statistics)

**Key Outputs**:
- Table 1: Descriptive Statistics
- Detailed explanation of modularity mechanism
- Integration of all four modules

**META_PROMPT Focus**: Analytical and systematic, build theory module-by-module

---

### 4. `generate_04_method.py` - Methodology

**Sections**:
1. Data Sources (PitchBook 2005-2023, N=51,840)
2. Vagueness Measurement (Strategic Vagueness Score V2)
3. Variable Definitions (Table 2)
4. Empirical Strategy (OLS for H1, Logit for H2)
5. **EXPLICIT**: "We do not use instrumental variables"

**Key Outputs**:
- LaTeX formulas for regression models
- Table 2: Variable definitions and construction
- Validation of vagueness score (r=0.68 with human raters)
- Honest acknowledgment of limitations

**META_PROMPT Focus**: Precise and transparent, address validity threats head-on

---

### 5. `generate_05_results.py` - Results

**Sections**:
1. H1 Results (Table 3: OLS regression)
2. H2 Results (Table 4: Logit regression + interaction plot)
3. **Devil's Advocate** (4 alternative explanations, critically examined)
4. Specification Curve Analysis (1,296 model variants)
5. Subsample Heterogeneity (quantum, transportation)

**Data Used**:
- `outputs/all/models/h1_coefficients.csv`
- `outputs/all/models/h2_main_coefficients.csv`

**Generated Figures**:
- `spec_curve_analysis.png` (robustness visualization)

**Key Outputs**:
- Exact p-values, confidence intervals, effect sizes
- Self-critical evaluation of alternative explanations
- Robustness: 89% of 1,296 specs show consistent effects

**META_PROMPT Focus**: Balanced and self-critical, present findings then challenge them

---

### 6. `generate_06_discussion.py` - Discussion

**Managerial Implications**:
1. **The Tesla Rule**: Embrace vagueness in modular (software) contexts
2. **The Waymo Rule**: Embrace specificity in coupled (hardware) contexts
3. **The Bosch Caveat**: When specificity always dominates
4. **Decision Matrix**: Modularity × Market Uncertainty → Strategy

**Theoretical Contributions**:
1. Productive vs. Destructive Ambiguity
2. Modularity → Communication Strategy
3. Reconciling Information Economics vs. Real Options

**Limitations** (Honest Assessment):
1. Correlational design (no causality claims)
2. Sample restrictions (VC-backed only)
3. Measurement imperfections

**Future Research**:
1. Experimental vagueness manipulation
2. Dynamic vagueness trajectories
3. Additional moderators

**META_PROMPT Focus**: Prescriptive yet humble, actionable insights with limitations

---

### 7. `generate_07_poster.py` - Academic Poster (현지의 포스터 공방)

**Mission**: Transform paper into 30-second visual summary with lifetime memory impact

**Philosophy**: **Playful Rigor**
- Comfortable Curiosity: Ask "why?" in familiar territory
- Playful Precision: Enjoyable yet accurate scholarship
- Evolutionary Stability: Continuous innovation on stable foundation

**4-Phase Structure (전라좌수군 기승전결)**:

1. **🐢 정운 (기/起 - Setup)**:
   - Color: Teal (#20B2AA)
   - Hook: Tesla vs Bosch paradox
   - Literature gap: Info Econ vs Real Options
   - Must Read: Akerlof (1970), McGrath (1997), Baldwin & Clark (2000)

2. **🐅 권준 (승/承 - Development)**:
   - Color: Orange (#FF8C00)
   - 4-Module Framework (C-T-O-C)
   - Hypothesis development (H1, H2)
   - Data & method preview
   - Must Read: Schilling (2000), Ethiraj & Levinthal (2004)

3. **🐙 김완 (전/轉 - Turn)**:
   - Color: Crimson (#DC143C)
   - Key results with exact numbers
   - Robustness evidence
   - Simple interaction visualization
   - Must Read: Simonsohn et al (2020)

4. **👾 어영담 (결/結 - Resolution)**:
   - Color: Purple (#9370DB)
   - Decision Matrix (2×2: Modularity × Uncertainty)
   - Actionable heuristic
   - Theoretical contributions
   - Must Read: Ries (2011), Gans et al (2019)

**Data Used**:
- `outputs/all/models/h1_coefficients.csv`
- `outputs/all/models/h2_main_coefficients.csv`

**Output Format**:
- `07_Poster.svg` (2×2 grid, 1200×1600 pixels)
- `07_Poster.md` (Markdown description)

**Quality Matrix (3×3)**:
1. **Emotional Clarity**: ⚡ 30-second "Aha!" moment
2. **Organic Composition**: 🌊 Natural question→answer→proof→application flow
3. **Logical Development**: ⚙️ Necessary A→B→C causation

**Success Metrics**:
- ✅ Core understanding in 30 seconds
- ✅ Remember 3 key points after 24 hours
- ✅ Can explain to colleague immediately
- ✅ Inspires reading full paper

**Visual Elements**:
- 4 color-coded quadrants
- Key statistics highlighted
- Decision matrix for practitioners
- References integrated throughout

**META_PROMPT Focus**: Visual storytelling with emotional impact, memorable metaphors, actionable insights

**Signature**: "복잡한 것을 단순하게, 단순한 것을 아름답게, 아름다운 것을 기억에 남게"

---

### 8. `generate_08_industry_comparison.py` - Industry Comparison Analysis

**Mission**: Integrate PR #13's 6-industry comparison framework into paper

**Key Finding**: **"중간은 죽는다" (The Middle Dies)** - Moderate vagueness underperforms extreme positioning

**6 Industries Analyzed**:
1. **Quantum Computing**: Highest uncertainty → Vagueness most valuable
2. **Transportation & Mobility**: Strongest interaction effect (hardware + regulation)
3. **Biotech & Healthcare**: Regulatory clarity reduces penalty
4. **FinTech**: Specificity always wins
5. **Enterprise Software**: High modularity → Weak penalty
6. **Hardware & Robotics**: Baseline hardware effect

**2×2 Framework Dimensions**:
- **X-axis**: Customer Heterogeneity (diversity of use cases)
- **Y-axis**: Technology Modularity (ease of pivoting)

**Data Used**:
- `outputs/quantum/models/h2_main_coefficients.csv`
- `outputs/transportation/models/h2_main_coefficients.csv`
- `outputs/biotech/models/h2_main_coefficients.csv`
- `outputs/fintech/models/h2_main_coefficients.csv`
- `outputs/enterprise/models/h2_main_coefficients.csv`
- `outputs/hardware/models/h2_main_coefficients.csv`

**Section Structure**:
1. **Six-Industry Overview** (1¶): Framework introduction
2. **2D Framework** (2¶): Customer × Technology matrix positioning
3. **"중간은 죽는다" Phenomenon** (3¶): U-shaped relationship evidence
4. **Transportation Deep Dive** (2¶): Waymo vs Tesla, strongest effect explanation
5. **Cross-Industry Comparison** (2¶): Effect size gradient, modularity as key moderator
6. **Theoretical Implications** (2¶): Generalization, regulatory constraints, customer heterogeneity

**Key Statistics** (from PR #13):
- Transportation: β = -0.042, p = 0.018 (strongest penalty)
- Quantum: β = -0.051, p = 0.012 (high uncertainty)
- FinTech: β = -0.012, p = 0.201 (null effect)

**Integration**: This section extends the core findings (Sections 1-6) by testing generalizability across industries and introducing the "middle dies" pattern.

**META_PROMPT Focus**: Comparative and insightful tone, industry-specific examples, effect size comparisons

---

## Data Dependencies

All scripts require:

```
outputs/all/models/
├── h1_coefficients.csv          # H1: Early Funding ~ Vagueness (OLS)
└── h2_main_coefficients.csv     # H2: Growth ~ Vagueness × Hardware (Logit)
```

Optional:
```
data/processed/
└── analysis_panel.csv           # For descriptive statistics (Table 1)
```

To generate these files, run the main analysis pipeline:

```bash
# From project root
python -m src.cli load-data
python -m src.cli engineer-features
python -m src.cli filter-datasets
python -m src.cli run-models --dataset all
python -m src.cli generate-plots --dataset all
```

## Configuration

Common settings in `__init__.py`:

```python
RESULTS_DIR = Path(__file__).resolve().parents[3] / "outputs" / "all" / "models"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"
FIGURES_DIR = Path(__file__).resolve().parents[3] / "outputs" / "all" / "eyeball_test"
```

Modify these paths if your directory structure differs.

## META_PROMPT Usage

Each script contains a `META_PROMPT` string variable approved by General Kim Wan. This prompt guides LLM-based expansion of the generated markdown skeleton.

**Workflow**:

1. **Run script** to generate markdown skeleton with data-driven numbers
2. **Copy META_PROMPT** from source code
3. **Feed to LLM** (Claude, GPT-4) along with the generated markdown
4. **LLM expands** skeleton into full prose, following META_PROMPT guidelines

**Example**:

```python
# In generate_01_intro.py
META_PROMPT = """
You are generating the Introduction section of an academic paper.
TONE: Scholarly yet accessible.
STRUCTURE:
1. Hook (Tesla vs Bosch - 2 paragraphs)
2. Puzzle statement (1 paragraph)
...
"""
```

**Usage with Claude**:

```
I have a markdown skeleton for the Introduction section of my paper.
Please expand it into full prose following this META_PROMPT:

[paste META_PROMPT]

Here's the skeleton:

[paste 01_Introduction.md]
```

## Output Format

All scripts generate **Markdown** files with:

- **Structured sections** (##, ###)
- **Data-driven numbers** (f-strings from CSV results)
- **LaTeX formulas** ($$...$$)
- **Tables** (markdown format with `|---|---|`)
- **Figure placeholders** (with captions)
- **Metadata footer** (data sources, generation script)

Example output structure:

```markdown
# 5. Results

## 5.1 H1: Main Effect

Table 3 reports OLS results...

| Variable | Coef | SE | t | p | 95% CI |
|----------|------|----|----|---|---------|
| z_vagueness | -0.00037 | 0.00012 | -3.14 | 0.002 | [-0.00061, -0.00014] |

The coefficient is statistically significant (p=0.002)...

---
**Generated from:** `generate_05_results.py`
**Data sources:** `outputs/all/models/h1_coefficients.csv`
```

## Extending the Pipeline

### Adding a New Section

1. **Create script**: `generate_07_conclusion.py`

```python
#!/usr/bin/env python3
from pathlib import Path
from src.scripts.paper_generation import OUTPUT_DIR

META_PROMPT = """..."""

def generate_conclusion():
    content = """# 7. Conclusion\n\n..."""
    return content

def main():
    content = generate_conclusion()
    (OUTPUT_DIR / "07_Conclusion.md").write_text(content)
    print("✅ Generated: 07_Conclusion.md")

if __name__ == "__main__":
    main()
```

2. **Add to `generate_all.py`**:

```python
sections = [
    ...
    (7, "Conclusion", "generate_07_conclusion")
]
```

3. **Run**: `python generate_all.py --sections 7`

### Customizing Data Sources

To use different datasets (e.g., quantum, transportation):

```python
# In __init__.py or individual script
DATASET = "quantum"  # or "transportation"
RESULTS_DIR = Path(__file__).resolve().parents[3] / "outputs" / DATASET / "models"
```

Or pass as command-line argument:

```python
# In generate_01_intro.py
parser = argparse.ArgumentParser()
parser.add_argument("--dataset", default="all", choices=["all", "quantum", "transportation"])
args = parser.parse_args()
```

## Best Practices

### 1. Version Control

Commit generated markdown to track iterations:

```bash
git add src/scripts/paper_generation/output/*.md
git commit -m "Paper v1: Initial generation from H1/H2 results"
```

### 2. Iterative Refinement

After LLM expansion:

1. **Review** for factual accuracy (check numbers match CSV)
2. **Edit** for voice consistency
3. **Re-run scripts** if data changes
4. **Diff** to see what changed

### 3. Data Lineage

Each generated file includes footer metadata:

```markdown
---
**Generated from:** `generate_05_results.py`
**Data sources:** `outputs/all/models/h2_main_coefficients.csv`
**Meta-prompt:** See source code for LLM expansion guidance
```

Use this to trace which results fed which claims.

### 4. Reproducibility

Always re-run from clean state before final submission:

```bash
# Clean outputs
rm -rf src/scripts/paper_generation/output/*

# Regenerate results
python -m src.cli run-models --dataset all

# Regenerate paper
python src/scripts/paper_generation/generate_all.py
```

## Troubleshooting

### "FileNotFoundError: h1_coefficients.csv"

**Cause**: Results not yet generated

**Fix**: Run analysis pipeline first:

```bash
python -m src.cli run-models --dataset all
```

### "ModuleNotFoundError: src.scripts.paper_generation"

**Cause**: Python path not set correctly

**Fix**: Run from project root or adjust `sys.path`:

```bash
cd /home/user/empirics_ent_strat_ops
python -m src.scripts.paper_generation.generate_all
```

### "Empty tables or missing data"

**Cause**: CSV files exist but have unexpected structure

**Fix**: Inspect CSV files:

```bash
head -5 outputs/all/models/h1_coefficients.csv
```

Adjust script's data loading logic in `load_h1_results()` function.

## Appendix: Kim Wan's Meta-Prompt Philosophy

> "The purpose of automation is not to replace thought, but to **scaffold** it. These scripts generate **data-driven skeletons**, not final prose. The researcher must still **interpret**, **contextualize**, and **argue**. But by automating the tedious parts (fetching coefficients, formatting tables, checking p-values), we free cognitive resources for the creative parts (storytelling, theoretical synthesis, devil's advocacy)."
>
> "Notice: Each META_PROMPT emphasizes **self-criticism**. Section 5 includes a Devil's Advocate subsection. Section 6 leads with limitations. This is not weakness — it is **intellectual honesty**, which earns reader trust. A paper that acknowledges its gaps is stronger than one that pretends omniscience."
>
> "Finally: **Specificity signals competence**. Notice how our scripts insert exact p-values (p=0.046, not 'p<0.05'), confidence intervals, effect sizes, and sample sizes. Vague claims ('significant positive effect') are for press releases. Academic writing demands precision."

— General Kim Wan, Strategic Commander of Empirical Operations

---

**Questions?** Open an issue or consult the main project documentation: `PIPELINE_ARCHITECTURE.md`

**Generated**: 2025-11-23
**Pipeline Version**: 1.0
**Author**: Hyunji Moon (hyunjimoon@gmail.com)
