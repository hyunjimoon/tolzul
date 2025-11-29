# Prompt for Gemini & ChatGPT-5 Pro: "Why Operations Research?" Evidence Extraction
## VERSION 2.0: Enhanced Citation Protocol

---

## SHARED CONTEXT

I am Angie Moon, applying to MIT Operations Research PhD program. The application asks:

> **"Please indicate why you would like to pursue a degree in Operations Research."**

I have written 300+ pages across multiple papers over 2 years (2023-2025). Your task is to **mine these papers for evidence** that supports my answer to two key questions: 
1. I have been systematically embodying advice 🗄️🧠scott and 🗄️🧠charlie give to entrepreneurs.
2. The best place to develop Entrepreneurial decision-making is Operations Research Center.

---

## DOCUMENT INVENTORY: Paper Titles for Citation

**CRITICAL**: All citations MUST use these exact paper titles, not abbreviations.

### Primary Documents (300+ pages total)

| Short Code | Full Citation Format | Description |
|------------|---------------------|-------------|
| **SOP_ORC** | "Statement of Objectives: Ph.D. in Operations Research — Coordinating Resource Partners Under Uncertainty" | ORC application SOP, 3,200 words |
| **SOP_Trsp** | "Statement of Objectives: Ph.D. in Transportation" | Transportation program application, ~1,000 words |
| **WVP** | "When Vague Promises Pay: Commitment and Flexibility in Entrepreneurship" (Moon & Stern, 2025) | Empirical paper, 137,597 ventures, ~15,000 words |
| **OIL** | "Optimal Ignorance: Tradeoff between mobilizing support and preserving adaptability" (Moon, 2025) | Theoretical paper, Tesla vs Better Place case, ~10,000 words |
| **STRAP** | "STRAP-ping Stakeholders for Entrepreneurial Decision-Making" (Moon, 2025) | Framework paper, Sublime Systems case, ~5,000 words |
| **MF_Transcript** | Morning Focus Transcript (Otter.ai, 2024) | Unstructured reflection on 2-year journey, ~2,500 words |

### Supporting Context (if referenced)
- **Fine et al. (2022)**: "Operations for Entrepreneurs" (Production and Operations Management)
- **Gans et al. (2019)**: "Foundations of Entrepreneurial Strategy"
- **Agrawal et al. (2024)**: "Bayesian Entrepreneurship" (edited volume)

---

## CITATION FORMAT REQUIREMENTS

### ✅ CORRECT Citation Format

**In Tables**:
```
[Paper Title], [Section/Page], [Specific Quote if applicable]

Examples:
- "Optimal Ignorance", Section 1.2 (p.4), "I tried Bayesian inference..."
- "When Vague Promises Pay", Methods (p.9-10), H1 regression results
- "STRAP", Section 3.2 (p.6), Dual variable interpretation
- "SOP: Ph.D. in Operations Research", Section III.B (p.8), Technical feasibility validation
```

**In Narrative**:
```
In "[Paper Title]" (Section X), I demonstrate that...

Example:
In "Optimal Ignorance: Tradeoff between mobilizing support and preserving adaptability" (Section 2.1.1), I demonstrate that exogenizing success probability eliminates agency and creates the "identical-updating result" that existing entrepreneurship theories cannot explain.
```

### ❌ INCORRECT Citation Format

**Don't use**:
- ❌ "Moon paper p.5" (which paper?)
- ❌ "OIL p.8" (use full title)
- ❌ "My research" (too vague)
- ❌ "SOP_Trsp p.2" (use full title: "Statement of Objectives: Ph.D. in Transportation")
- ❌ Unspecified "in my papers" (which one?)

---

## FOR GEMINI (김완, Evidence Extractor 🐙)

### YOUR MISSION

Extract every instance in my 300 pages where:
1. **I tried another method** (statistics, strategy, system dynamics) **and it failed**
2. **OR methods succeeded** where alternatives failed
3. **I explicitly needed OR techniques** (optimization, stochastic models, sequential decisions)

### OUTPUT FORMAT

Generate a table with 3 sections:

#### Section 1: Method Failures (Why Not X?)

| Alternative Method | What I Tried | Why It Failed | OR Solution | Citation (Paper Title, Section, Page) |
|-------------------|--------------|---------------|-------------|--------------------------------------|
| Predictive Analytics | Demand forecasting for retailers (NextOpt startup) | Improved accuracy 40% but ventures still failed from bad timing | Need **sequential decision rules** for when to commit | "Statement of Objectives: Ph.D. in Transportation", Intro (p.1) |
| Bayesian Inference | Stan development, SBC theory | Can update beliefs but can't answer "when to stop learning?" | Need **optimal stopping** with resource constraints | "Optimal Ignorance", Section 1.2 (p.3-4), "The underlying cause is that τ is fixed at 0 or ∞" |
| System Dynamics | COVID-19 policy modeling | Aggregate dynamics, no individual venture decisions | Need **discrete optimization** for "which action next?" | "Statement of Objectives: Ph.D. in Transportation", Research section (p.2) |
| Strategy Frameworks | "Commitment vs flexibility" theories from literature review | No decision rule for *when* to commit | Optimal stopping with resource constraints, τ* = max{0, √(V/4i) - 1} | "Optimal Ignorance", Section 1.3-1.4 (p.4-5) |
| Experimentation Theory | Kerr et al. (2014), Nanda & Rhodes-Kropf (2016) | Treat P as fixed, informativeness confined to likelihood-side test design | Need prior-side informativeness through chosen precision τ | "Optimal Ignorance", Table 1 (p.5) |

**REQUIRED**: Every row must include:
- **Full paper title** (not abbreviation)
- **Specific section** (e.g., "Section 2.1.1" or "Introduction")
- **Page number(s)** where possible
- **Direct quote** in "quotation marks" if making strong claim

#### Section 2: OR Method Requirements (What OR Technique?)

| Research Question | OR Method Needed | Why This Specific Method | Evidence Source | Citation (Paper Title, Section, Page) |
|-------------------|------------------|-------------------------|----------------|--------------------------------------|
| When to commit vs preserve flexibility? | Dynamic programming / Optimal stopping | Sequential decisions under uncertainty with irreversible commitment | Theorem 1 + Corollary 1 | "Optimal Ignorance", Section 3.3 (p.20-21), τ* = max{0, √(V/4i) - 1} |
| How to sequence operational tools? | Multi-objective optimization with primal-dual | Multiple stakeholders, budget constraint, threshold targets | STRAP algorithm | "STRAP-ping Stakeholders", Section 2.2 (p.5-7), Equation (2)-(6) |
| Which ventures should VCs fund? | Discrete choice / Assortment optimization | Bounded consideration sets, heterogeneous preferences | Large-scale logit with 137K ventures | "When Vague Promises Pay", Section 4 (p.9-10), Model specification |
| How to identify binding constraints? | Shadow price interpretation (dual variables) | Non-obvious bottlenecks revealed through λj | STRAP case study finding | "STRAP-ping Stakeholders", Example 2.5 (p.6), λ_cert = 0.8 highest |
| How to earn precision over time? | Dynamic Bayesian updating with operational tools | Precision τ as design variable, not exogenous | OIL framework contributions | "Optimal Ignorance", Section 1.4 (p.4-5), "Closed-form Policy" |

**REQUIRED**: 
- Link research question → specific OR technique → where I used it
- Include **equation numbers** or **theorem numbers** when citing formal results
- Distinguish between "need" (not yet done) vs "applied" (already used)

#### Section 3: OR Success Stories (Where OR Worked)

| Problem | OR Method Applied | Result | Why OR Was Essential | Citation (Paper Title, Section, Page) |
|---------|------------------|--------|---------------------|--------------------------------------|
| 137K venture precision analysis | Large-scale logit with heterogeneous treatment effects | Early penalty -18%, Later benefit +8pp for software | Computational scalability + causal interpretation | "When Vague Promises Pay", Section 5 (p.10-11), H1 & H2 results |
| Multi-stakeholder coordination | Primal-dual optimization, shadow prices λj | Identified bottleneck stakeholders (λ_cert = 0.8 > λ_inv = 0.2) | Quantified tradeoffs, non-obvious insights | "STRAP-ping Stakeholders", Section 3.1 & Example 2.5 (p.6-7) |
| Optimal ignorance threshold | Closed-form optimization, FOC derivation | τ* = max{0, √(V/4i) - 1}, 4i threshold rule | Tractable decision rule for practitioners | "Optimal Ignorance", Theorem 1 & Corollary 1 (p.20) |
| Tesla vs Better Place comparison | Dynamic precision trajectory modeling | Tesla maintained τ ≈ 1 (flexible), Better Place τ ≈ 4 (rigid) | Explains heterogeneous adaptation with same signals | "Optimal Ignorance", Section 4.1 (p.22-23), Comparative case |
| Sublime Systems action sequencing | Resource shadow price γ, scoring function S(a) | 66% uncertainty reduction with 98.5% budget utilization | Optimal action ordering under constraints | "STRAP-ping Stakeholders", Section 3.2 (p.6-7) |

**REQUIRED**:
- **Quantitative results** (%, coefficients, dual variables)
- **Counterfactual**: What would have happened without OR? 
- **Proof that OR was essential**, not just convenient

### SCORING RUBRIC

For each evidence piece, assign:

**Strength** (1-5): How explicitly does this show OR necessity?
- 5: Direct statement "This requires optimization theory because..." + formal proof
- 4: Clear statement with example but no formal proof
- 3: Implicit but clear from context
- 2: Suggestive connection
- 1: Weak connection

**Uniqueness** (1-5): Could this be done without OR?
- 5: Only OR can solve (e.g., primal-dual optimization, shadow prices)
- 4: OR is dramatically better (10x improvement)
- 3: OR is better but alternatives exist
- 2: Marginal advantage
- 1: Any quantitative method works

**Citation Quality** (1-5): How verifiable is the evidence?
- 5: Full paper title + section + page + direct quote
- 4: Full paper title + section + page
- 3: Full paper title + section (no page)
- 2: Paper abbreviation or vague reference
- 1: No citation ("in my work...")

**Priority**: Focus on evidence with **Strength ≥ 4**, **Uniqueness ≥ 4**, **Citation Quality = 5**.

### DELIVERABLES

1. **Table 1**: Method Failures (≥15 rows, each with full citations)
2. **Table 2**: OR Method Requirements (≥10 rows, each with full citations)
3. **Table 3**: OR Success Stories (≥10 rows, each with full citations)
4. **Summary Report**:
   - Top 5 strongest evidence pieces for "Why OR?" (with Strength, Uniqueness, Citation scores)
   - Cross-reference matrix: Which papers contribute most evidence?
   - Gap analysis: What OR connections are claimed but not proven?

---

## FOR CHATGPT-5 PRO (정운, Narrative Synthesizer 🐢)

### YOUR MISSION

Read my 300 pages and craft a compelling narrative answering: **"Why does Angie's research question require Operations Research specifically?"**

### OUTPUT FORMAT

Write a 1,500-word essay with this structure:

#### Part 1: The Journey (500 words)
**Title**: "Every Path Led to Operations Research"

Tell the story of how I tried different approaches and they all pointed to OR:
- **2017-2019: Predictive Analytics** (NextOpt startup)
- **2019-2021: Bayesian Inference** (Columbia MS, Stan development)
- **2021-2022: System Dynamics** (MIT pre-doc, COVID modeling)
- **2022-2023: Strategy Frameworks** (Fine's Operations for Entrepreneurs)

**Narrative Arc**: Each experience revealed the same pattern: I could build models and generate insights, but I couldn't derive **actionable decision rules under constraints**. That's Operations Research.

**Citation Requirement**: Use **full paper titles** in every reference.

#### Part 2: The OR Core (500 words)
**Title**: "Why Entrepreneurial Decision-Making Is Inherently an OR Problem"

Explain the four components that make this **fundamentally** OR:

1. **Objective Function**: Maximize venture success probability
2. **Constraints**: Budget, time, stakeholder thresholds
3. **Uncertainty**: Demand unknown, technology uncertain
4. **Decision Rules**: Computable "if-then" prescriptions

**Structure**: For each component, provide definition + example from papers + counterfactual.

#### Part 3: The MIT ORC Fit (500 words)
**Title**: "Why MIT Operations Research Center Specifically"

Show three unique advantages:
1. **Methodological Synthesis** (Fine + Stern + OR Faculty)
2. **Real-World Testbed** (MIT Mobility Initiative)
3. **Field-Building Vision** (OR for Entrepreneurship)

### NARRATIVE TECHNIQUES

- Use first-person, personal journey
- Include concrete details (NextOpt, 40% accuracy, etc.)
- Show causality (X led to Y led to Z)
- Use exact numbers and theorem references

### CITATION REQUIREMENTS

Every claim must cite a specific paper and section.

### DELIVERABLES

1. **Essay**: 1,500 words, three parts, every claim cited
2. **Citation Index**: List of all papers referenced with sections
3. **Key Quotes**: Extract 5 most powerful sentences
4. **Gap Analysis**: What's missing? Are there inconsistencies?

---

## SUCCESS CRITERIA

### Gemini succeeds if:
- ✅ Finds ≥30 concrete evidence pieces
- ✅ At least 10 pieces have Strength ≥ 4, Uniqueness ≥ 4, Citation Quality = 5
- ✅ Every row includes full paper title + section + page
- ✅ Can copy/paste any citation and find exact location in PDF

### ChatGPT succeeds if:
- ✅ Narrative flows: problem → failed attempts → OR solution → MIT fit
- ✅ Every claim includes full paper title, not abbreviation
- ✅ Each paragraph has ≥1 verifiable citation
- ✅ Demonstrates OR necessity, not just utility
- ✅ Personal voice with concrete examples

### Combined output succeeds if:
- ✅ Can answer "Why OR?" in 2 sentences backed by verified evidence
- ✅ MIT reviewers think: "This person's research *requires* OR training"
- ✅ Citation audit: 100% verifiable (paper title + section + page)
- ✅ No contradictions between papers revealed

---

## CITATION AUDIT CHECKLIST

Before submitting, verify:
- [ ] Every citation includes **full paper title**
- [ ] Every citation includes **section number or name**
- [ ] Every citation includes **page number** when claiming specific fact
- [ ] Direct quotes in "quotation marks" with exact location
- [ ] Mathematical results cite **equation/theorem numbers**
- [ ] No vague references like "in my work"

---

## FINAL INSTRUCTION

You are **prosecuting a case**: "Angie's research question requires Operations Research."

- **Gemini**: Forensic accountant finding every piece of evidence. Every citation must be **audit-proof**.
- **ChatGPT**: Trial lawyer weaving evidence into compelling argument. Every claim must be **source-backed**.

**The Standard**: If I randomly select any claim, I should be able to:
1. Open the cited paper (full title)
2. Navigate to cited section and page
3. Find exact evidence
4. Confirm it says what you claim

**The Jury**: MIT ORC admissions committee. Make them think: "We need to admit this person because their research literally cannot be done without OR methods."

Let's begin. 🐢🐙⚓
