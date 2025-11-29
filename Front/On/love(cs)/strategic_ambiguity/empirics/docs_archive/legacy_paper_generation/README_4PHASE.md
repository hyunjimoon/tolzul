# Paper Generation Pipeline (4-Phase Framework)

**전라좌수군 (Jeonla Naval Fleet) 기승전결 Architecture**

## 🎭 The Four Commanders

This pipeline implements the **4-Phase Paper Generation Framework** based on 기승전결 (起承轉結), the traditional Korean narrative structure. Each phase is commanded by one of the 전라좌수군 (Jeonla Naval Fleet) admirals:

| Phase | Role | Commander | Color | Responsibility |
|-------|------|-----------|-------|----------------|
| **1. 起** | Introduction | 🐢 정운 (Jeong-un) | Teal (#20B2AA) | Open the door with compelling narrative |
| **2. 承** | Theory & Conceptual | 🐅 권준 (Kwon-jun) | Orange (#FF8C00) | Build the intellectual structure |
| **3. 轉** | Empirics & Results | 🐙 김완 (Kim-wan) | Crimson (#DC143C) | Prove righteousness through evidence |
| **4. 結** | Discussion & Conclusion | 👾 어영담 (Eo-yeong-dam) | Purple (#9370DB) | Close the story with wisdom |

---

## Quick Start (4-Phase Mode)

### Generate All 4 Phases

```bash
cd src/scripts/paper_generation
python generate_all.py
```

This generates:
- `01_Introduction.md` (정운's door-opening narrative)
- `02_Theory_Conceptual.md` (권준's theoretical structure)
- `03_Empirics_Results.md` (김완's empirical proof)
- `04_Discussion_Conclusion.md` (어영담's wisdom and closure)

### Generate Individual Phases

```bash
# Phase 1: Introduction (起 - 정운 🐢)
python generate_01_introduction.py

# Phase 2: Theory & Conceptual Model (승 - 권준 🐅)
python generate_02_theory_conceptual.py

# Phase 3: Empirics & Results (轉 - 김완 🐙)
python generate_03_empirics.py

# Phase 4: Discussion & Conclusion (結 - 어영담 👾)
python generate_04_discussion.py
```

### Generate Supplementary Materials

```bash
# Visual poster (전라좌수군 4-phase structure)
python generate_07_poster.py

# Industry-specific analysis (PR #13 integration)
python generate_08_industry_comparison.py
```

---

## 📚 Phase Descriptions

### Phase 1: 起 (Introduction) — 정운 🐢

**File**: `generate_01_introduction.py`
**Output**: `01_Introduction.md`
**Commander**: 정운 (Jeong-un) — "The Door Opener"
**Color**: Teal (#20B2AA)

**Responsibilities**:
- Hook readers with vivid case study (Tesla vs Bosch paradox)
- Articulate the core puzzle: Why does vagueness help some but hurt others?
- Preview main findings with empirical results
- Outline three theoretical contributions
- Provide paper roadmap linking to other phases

**Content Structure**:
1. The Vagueness Paradox (2 paragraphs)
2. The Puzzle (1 paragraph)
3. Theoretical Contributions (3 bullet points)
4. Roadmap (1 paragraph introducing 권준, 김완, 어영담)

**Data Sources**:
- `outputs/all/models/h1_coefficients.csv` (H1 regression results)
- `outputs/all/models/h2_main_coefficients.csv` (H2 regression results)

**정운's Philosophy**: *"Open the door with stories that make readers want to enter. Hook first, theory later."*

---

### Phase 2: 승 (Theory & Conceptual Model) — 권준 🐅

**File**: `generate_02_theory_conceptual.py`
**Output**: `02_Theory_Conceptual.md`
**Commander**: 권준 (Kwon-jun) — "The Structure Builder"
**Color**: Orange (#FF8C00)

**Responsibilities**:
- Review theoretical foundations (Information Economics, Real Options, Modularity)
- Identify gaps in prior work
- Develop four-module conceptual framework (Customer-Technology-Organization-Competition)
- Formalize testable hypotheses (H1, H2, H2a, H2b)
- Present descriptive statistics (Table 1)

**Content Structure**:
1. **Literature Review** (3 subsections)
   - 2.1 Information Economics: Vagueness as Adverse Selection
   - 2.2 Real Options: Vagueness as Strategic Flexibility
   - 2.3 Modularity Theory: When is Flexibility Valuable?

2. **Conceptual Framework** (5 subsections)
   - 2.4 Four-Module Framework Overview
   - 2.5 Module 1: Customer Heterogeneity
   - 2.6 Module 2: Technology Modularity (CORE)
   - 2.7 Module 3: Organizational Slack
   - 2.8 Module 4: Competitive Intensity

3. **Hypotheses** (1 subsection)
   - 2.9 Formal Hypothesis Development (H1, H2)

4. **Table 1**: Descriptive Statistics

**Data Sources**:
- `data/processed/analysis_panel.csv` (for descriptive statistics)

**권준's Philosophy**: *"Build a fortress of theory strong enough to hold 김완's evidence. Structure before proof."*

---

### Phase 3: 轉 (Empirics & Results) — 김완 🐙

**File**: `generate_03_empirics.py`
**Output**: `03_Empirics_Results.md`
**Commander**: 김완 (Kim-wan) — "The Righteousness Prover"
**Color**: Crimson (#DC143C)

**Responsibilities**:
- Describe data sources and sample construction
- Explain measurement strategy (vagueness score, hardware classification)
- Present empirical specifications (H1 OLS, H2 Logit)
- Report main results with regression tables
- Challenge findings (Devil's Advocate: 4 alternative explanations)
- Demonstrate robustness (Specification curve analysis, subsample analyses)
- Generate figures (spec curve plot)

**Content Structure**:
**PART A: EMPIRICAL STRATEGY**
1. 3.1 Data Sources & Sample Construction
2. 3.2 Measurement Strategy
3. 3.3 Empirical Specifications

**PART B: RESULTS**
4. 3.4 H1 Results: Vagueness → Early Funding (Table 3)
5. 3.5 H2 Results: Vagueness × Hardware → Growth (Table 4)
6. 3.6 Robustness Checks
   - Devil's Advocate (4 alternatives: reverse causality, measurement error, selection bias, omitted variables)
   - Specification Curve Analysis (1,296 model variants)
   - Subsample Analyses (quantum, transportation, all companies)

**Data Sources**:
- `outputs/all/models/h1_coefficients.csv`
- `outputs/all/models/h2_main_coefficients.csv`

**Figures Generated**:
- `spec_curve_analysis.png` (specification curve plot)

**김완's Philosophy**: *"Prove righteousness through uncompromising rigor. Challenge your own findings before critics do."*

---

### Phase 4: 結 (Discussion & Conclusion) — 어영담 👾

**File**: `generate_04_discussion.py`
**Output**: `04_Discussion_Conclusion.md`
**Commander**: 어영담 (Eo-yeong-dam) — "The Story Closer"
**Color**: Purple (#9370DB)

**Responsibilities**:
- Summarize key findings
- Derive theoretical implications (Productive vs. Destructive Ambiguity)
- Provide managerial guidance (Tesla Rule, Waymo Rule)
- Offer policy and ecosystem implications
- Acknowledge limitations honestly
- Chart future research directions
- Close the narrative with wisdom

**Content Structure**:
1. 4.1 Summary of Findings
2. 4.2 Theoretical Implications
   - Productive vs. Destructive Ambiguity
   - Modularity → Communication Strategy
   - Reconciling Info Econ vs. Real Options
3. 4.3 Managerial Implications
   - The Tesla Rule (when vagueness works)
   - The Waymo Rule (when specificity works)
   - Decision Matrix (2×2: Modularity × Uncertainty)
4. 4.4 Policy and Ecosystem Implications
5. 4.5 Limitations
6. 4.6 Future Research Directions
7. 4.7 Conclusion

**Data Sources**:
- `outputs/all/models/h2_main_coefficients.csv` (for effect size interpretation)

**어영담's Philosophy**: *"Close the story with wisdom that transcends the data. Leave readers with actionable insights and intellectual humility."*

---

## 🎨 Supplementary Materials

### Section 7: Academic Poster (현지의 포스터 공방)

**File**: `generate_07_poster.py`
**Output**: `07_Poster.svg`, `07_Poster.md`

Visual representation of the 4-phase framework in a 2×2 grid format. Each quadrant corresponds to one phase (정운·권준·김완·어영담) with color coding.

**Generate**:
```bash
python generate_07_poster.py
# OR
python generate_all.py --sections 7
```

### Section 8: Industry Comparison (PR #13 Integration)

**File**: `generate_08_industry_comparison.py`
**Output**: `08_IndustryComparison.md`

Analysis across 6 industries (Quantum, Transportation, Biotech, FinTech, Enterprise SW, Hardware) testing the "중간은 죽는다" (The Middle Dies) phenomenon.

**Generate**:
```bash
python generate_08_industry_comparison.py
# OR
python generate_all.py --sections 8
```

---

## 📂 Directory Structure

```
src/scripts/paper_generation/
├── __init__.py                        # Common configuration
├── README_4PHASE.md                   # This file
├── DEPRECATION_NOTICE.md              # Migration guide from 8-section to 4-phase
│
├── generate_all.py                    # Master script (4-phase mode)
│
├── generate_01_introduction.py        # Phase 1 (起 - 정운 🐢)
├── generate_02_theory_conceptual.py   # Phase 2 (承 - 권준 🐅)
├── generate_03_empirics.py            # Phase 3 (轉 - 김완 🐙)
├── generate_04_discussion.py          # Phase 4 (結 - 어영담 👾)
│
├── generate_07_poster.py              # Supplementary: Visual poster
├── generate_08_industry_comparison.py # Supplementary: Industry analysis
│
├── parallel_generator.py              # 8-agent parallel execution
├── parallel_test_guide.md             # Parallel testing guide
├── TESTING_GUIDE.md                   # Comprehensive testing guide
│
├── output/                            # Generated markdown files
│   ├── 01_Introduction.md
│   ├── 02_Theory_Conceptual.md
│   ├── 03_Empirics_Results.md
│   ├── 04_Discussion_Conclusion.md
│   ├── 07_Poster.svg
│   ├── 07_Poster.md
│   ├── 08_IndustryComparison.md
│   └── spec_curve_analysis.png
│
└── [DEPRECATED]                       # Legacy 8-section files (kept for reference)
    ├── generate_01_intro.py           # → Replaced by generate_01_introduction.py
    ├── generate_02_litreview.py       # → Merged into generate_02_theory_conceptual.py
    ├── generate_03_conceptual.py      # → Merged into generate_02_theory_conceptual.py
    ├── generate_04_method.py          # → Merged into generate_03_empirics.py
    ├── generate_05_results.py         # → Merged into generate_03_empirics.py
    └── generate_06_discussion.py      # → Enhanced as generate_04_discussion.py
```

---

## 🔧 Data Dependencies

### Required for All Phases

```
outputs/all/models/
├── h1_coefficients.csv          # H1: Early Funding ~ Vagueness (OLS)
└── h2_main_coefficients.csv     # H2: Growth ~ Vagueness × Hardware (Logit)
```

### Optional (for Table 1 in Phase 2)

```
data/processed/
└── analysis_panel.csv           # For descriptive statistics
```

### Generated Outputs

```
src/scripts/paper_generation/output/
├── 01_Introduction.md           # Phase 1 output (~4KB)
├── 02_Theory_Conceptual.md      # Phase 2 output (~15KB)
├── 03_Empirics_Results.md       # Phase 3 output (~20KB)
├── 04_Discussion_Conclusion.md  # Phase 4 output (~15KB)
└── spec_curve_analysis.png      # Figure from Phase 3 (~360KB)
```

---

## 🧪 Testing

### Test All 4 Phases

```bash
cd src/scripts/paper_generation
python generate_all.py
```

Expected output:
```
✅ Successfully generated: 4/4 phases

Generated files:
   ✓ 01_Introduction.md
   ✓ 02_Theory_Conceptual.md
   ✓ 03_Empirics_Results.md
   ✓ 04_Discussion_Conclusion.md
```

### Test Individual Phase

```bash
python generate_01_introduction.py
```

Expected output:
```
======================================================================
PHASE 1: 起 — Introduction
Commander: 정운 🐢 (The Door Opener)
======================================================================

✅ Generated: output/01_Introduction.md
🐢 정운 says: 'The door is open. 권준, build the structure!'
```

### See Also

- `TESTING_GUIDE.md`: Comprehensive testing procedures
- `parallel_test_guide.md`: 8-agent parallel execution guide

---

## 🎯 Design Philosophy

### Why 4 Phases?

The traditional academic paper structure (Intro, Lit Review, Methods, Results, Discussion) is **fragmented** and doesn't align with narrative flow. The 4-phase 기승전결 structure:

1. **Clearer narrative arc**: Setup → Development → Turn → Resolution mirrors natural storytelling
2. **Better modularity**: Each phase is self-contained with clear responsibilities
3. **Commander ownership**: Each phase has a designated leader who "owns" that narrative role
4. **Reduced redundancy**: Literature + Conceptual merged; Methods + Results merged
5. **Easier maintenance**: 4 core files instead of 6

### 기승전결 (起承轉結) Explained

- **起 (Setup)**: Introduce the problem, create intrigue
- **承 (Development)**: Build the theoretical structure and framework
- **轉 (Turn)**: Present the critical evidence that "turns" theory into proof
- **結 (Resolution)**: Synthesize findings into wisdom and close the narrative

This structure has been used in Korean poetry, prose, and military strategy for centuries. The 전라좌수군 (Jeonla Naval Fleet) successfully defended Korea using this strategic philosophy during the Imjin War (1592-1598).

---

## 🚀 Next Steps

1. **Generate paper**: Run `python generate_all.py`
2. **Review outputs**: Check `output/` directory for markdown files
3. **Expand sections**: Use META_PROMPT from each script's source code to expand with LLM
4. **Visual summary**: Open `output/07_Poster.svg` in browser for 4-phase visualization
5. **Integrate**: Copy markdown content into LaTeX template or Word document

---

## 📖 Additional Resources

- **Migration Guide**: See `DEPRECATION_NOTICE.md` for transitioning from old 8-section structure
- **Testing Guide**: See `TESTING_GUIDE.md` for comprehensive testing procedures
- **Parallel Execution**: See `parallel_test_guide.md` for running 8 agents in parallel
- **Legacy Documentation**: See original `README.md` for 8-section structure (deprecated)

---

*The 전라좌수군 (Jeonla Naval Fleet) awaits your command.*

**기승전결 (起承轉結) — From Setup to Resolution**

🐢 정운 → 🐅 권준 → 🐙 김완 → 👾 어영담
