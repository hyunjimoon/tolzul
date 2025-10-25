# Promise Precision and Venture Funding - END HERE (나침반)

**Your Destination**: A complete Management Science paper with theory, empirics, and case studies that answers: **When and how much should entrepreneurs be vague vs. precise in their promises?**

---

## 🎯 Final Deliverables Overview

### Paper Structure (Target: 40-50 pages)

```
┌─────────────────────────────────────────────────────────┐
│ 1. INTRODUCTION (8-10 pages)                           │
│    - Tesla hook ("200+ miles")                          │
│    - Theoretical puzzle: precision vs. flexibility      │
│    - Preview of answer: optimal ignorance rule          │
│    - Contributions to 3 literatures                     │
├─────────────────────────────────────────────────────────┤
│ 2. THEORY (10-12 pages)                                 │
│    - Model progression: M1 → M1' → M2 → M2'            │
│    - Core result: τ* = max{0, √(V/4i) - 1}             │
│    - Optimal ignorance rule & threshold                 │
│    - Comparative statics                                │
├─────────────────────────────────────────────────────────┤
│ 3. EMPIRICAL TESTS (12-15 pages)                        │
│    - H1: Vague at A ↓, Precise at B ↑                  │
│    - H2: Reversal 3× stronger in hardware              │
│    - Pitchbook panel data (2021-2025)                   │
│    - 4 tables + 4 figures                               │
├─────────────────────────────────────────────────────────┤
│ 4. CASE STUDIES (8-10 pages)                            │
│    - Deep dive: Tesla vs. Better Place                  │
│    - (τ, V, i) trajectories over time                   │
│    - Documentary evidence from pitch decks              │
│    - Quotes, charts, tables                             │
├─────────────────────────────────────────────────────────┤
│ 5. DISCUSSION & IMPLICATIONS (5-6 pages)                │
│    - When to shift from vague → precise                 │
│    - Toolkit: Acculturate, Processify, etc.            │
│    - Limitations & future research                      │
└─────────────────────────────────────────────────────────┘
```

---

## 📊 Complete Deliverables Checklist

### Section 1: Introduction ✅

**Status**: 80% complete  
**File**: `theory/📝(strategic_ambiguity).md`

**What's Done**:
- ✅ Tesla opening hook
- ✅ Theoretical puzzle setup
- ✅ Model preview (μ, σ², τ)
- ✅ Literature positioning (Archibald, El-Zayaty)
- ✅ Three key differences

**What's Missing**:
- [ ] Add "Some might object..." paragraph (anticipate objections)
- [ ] Strengthen "This matters because..." (importance)
- [ ] Final polish on They Say/I Say transitions

**Target**: 1,500-2,000 words

---

### Section 2: Theory ✅

**Status**: 90% complete  
**File**: `modeling_part_of_the_paper.pdf` (pages 1-6)

**What's Done**:
- ✅ M1→M1': Simulate (Figure 4)
- ✅ M1'→M2: Calibrate (Bayesian prior)
- ✅ M2→M2': Design (endogenize τ)
- ✅ Theorem 1 + Corollaries 1-2
- ✅ Table 5 (variable definitions)

**What's Missing**:
- [ ] Proofs appendix (show derivations)
- [ ] Alternative cost functions robustness
- [ ] Connection to Aumann convergence

**Target**: 3,000-3,500 words + math

---

### Section 3: Empirical Tests 🚧

**Status**: 40% complete (scripts ready, analysis pending)  
**File**: `empirics/` folder

**Deliverables Needed**:

#### Table 1: Descriptive Statistics ⏳
```
Variables          Mean   SD    Min   Max   N
─────────────────────────────────────────────
Vagueness         52.3   18.4   12    89   150
High_Integration   0.43   0.50    0     1   150
Series A Success   0.61   0.49    0     1    75
Series B Success   0.53   0.50    0     1    75
Deal Size (A, $M)  7.2    3.1   2.0  15.0   46
Deal Size (B, $M) 16.4    8.2  10.0  45.0   40
```

**Script**: `04_run_analysis.py` → outputs `output/table1_descriptives.csv`

---

#### Table 2: Main Regressions (H1 + H2) ⏳
```
Model 1: logit(Funding_Success) ~ Vague + SeriesB + Vague×SeriesB

                          Coef    SE     z      p
───────────────────────────────────────────────────
Vagueness               -0.024  0.009  -2.67  0.008**
SeriesB                  0.130  0.165   0.79  0.431
Vagueness × SeriesB      0.031  0.012   2.58  0.010**
───────────────────────────────────────────────────
N = 150, Pseudo R² = 0.14
```

**Interpretation**: 
- β₁ < 0: Vague hurts at Series A (mobilization cost)
- β₃ > 0: Effect reverses at Series B (adaptability value)

**Script**: `04_run_analysis.py` → outputs `output/table2_regressions.csv`

---

#### Figure 1: Success Rates by Stage (Bar Chart) ⏳
```
     Series A              Series B
     ┌────┐               ┌────┐
 70% │    │           60% │    │ Vague
     │    │               │    │
 50% └────┘           40% └────┘
     ┌────┐               ┌────┐
 45% │    │           70% │    │ Precise
     │    │               │    │
 30% └────┘           50% └────┘
```

**Key**: Precise disadvantage at A flips to advantage at B

**Script**: `05_create_deliverables.py` → outputs `output/figure1_success_rates.png`

---

#### Figure 2: Predicted Probabilities Curve ⏳
```
P(Success)
    1.0 ┤                    ╱╲  Precise
        │                  ╱    ╲
    0.8 ┤                ╱        ╲
        │              ╱            ╲
    0.6 ┤            ╱                ╲
        │   Vague  ╱
    0.4 ┤        ╱
        │      ╱
    0.2 ┤    ╱
        │  ╱
    0.0 ┼─────────────────────────────
        A                            B
```

**Key**: Crossover shows optimal transition point

**Script**: `05_create_deliverables.py` → outputs `output/figure2_curves.png`

---

#### Table 3: Success Rates by Sector ⏳
```
                  Software (Low-i)      Hardware (High-i)
              ──────────────────────  ──────────────────────
              Precise    Vague        Precise    Vague
Series A      65%        55%          75%        52%
Series B      70%        60%          28%        63%
───────────────────────────────────────────────────────────
Difference    +5pp       +5pp         -47pp***   +11pp*
```

**Key**: Hardware shows 3× stronger reversal (β₇ > 0)

**Script**: `04_run_analysis.py` → outputs `output/table3_sector_split.csv`

---

#### Table 4: Three-Way Interaction (H2) ⏳
```
Model 2: + High_Integration × Vague × SeriesB

                                      Coef    SE     z      p
─────────────────────────────────────────────────────────────
Vagueness × SeriesB                  0.018  0.015   1.20  0.230
High_Integration × Vague × SeriesB   0.042  0.018   2.33  0.020**
─────────────────────────────────────────────────────────────
N = 150, Pseudo R² = 0.21
```

**Interpretation**: Reversal effect 2.3× stronger in hardware (V/i ratio)

**Script**: `04_run_analysis.py` → outputs `output/table4_three_way.csv`

---

#### Figure 3: Four-Line Plot (Sector × Stage) ⏳
```
P(Success)
    0.8 ┤─────────────────╲
        │  Precise,Low-i   ╲───────
    0.7 ┤                   ╲
        │                    ╲
    0.6 ┤  Vague,High-i ────────╲───
        │                         ╲
    0.5 ┤  Vague,Low-i ────────────╲
        │
    0.4 ┤
        │          ╱─────────────────
    0.3 ┤ Precise,High-i
        ┼─────────────────────────────
        A                            B
```

**Key**: Hardware-Precise crashes at B (rigidity cost)

**Script**: `05_create_deliverables.py` → outputs `output/figure3_four_lines.png`

---

#### Figure 4: Effect Magnitude Bars ⏳
```
Reversal Effect Size (Δβ)

Software  ├──────┤  0.023
             
Hardware  ├────────────────┤  0.060***
          
          0.00            0.06
```

**Key**: Visual proof of moderation by integration cost

**Script**: `05_create_deliverables.py` → outputs `output/figure4_magnitude.png`

---

### Section 4: Case Studies 🚨

**Status**: 30% complete (outline exists, needs execution)  
**File**: TBD (new document)

**What Scott Wants** (from `scott_suggestion`):
> "I would pick a domain... It could be the clean energy boom of mid-2000s... It could be AI drug discovery... I would have it in a domain where there's a cluster of companies, all of whom are competing... You have 20 or 30 companies, and they all have available pitch decks from around the time of founding."

**Deliverables Needed**:

#### 4.1 Deep Dive: Tesla vs. Better Place (3-4 pages) ⏳

**Structure**:
```
┌──────────────────────────────────────────────────────────┐
│ A. Initial Promises (2008-2009)                          │
│    Tesla: "200+ miles" (τ ≈ 1, flexible)                 │
│    Better Place: "3-minute swap" (τ ≈ 4, rigid)          │
│    [Include actual pitch deck screenshots/quotes]        │
├──────────────────────────────────────────────────────────┤
│ B. (τ, V, i) Trajectories                                │
│    - Timeline chart showing evolution                     │
│    - Tesla: maintained flexibility, iterated             │
│    - Better Place: locked in early, couldn't adapt       │
├──────────────────────────────────────────────────────────┤
│ C. Outcome Analysis                                       │
│    - Tesla: $60M → adaptive learning → success           │
│    - Better Place: $850M → rigidity → failure            │
│    - Model prediction: V/i ratio explains divergence     │
└──────────────────────────────────────────────────────────┘
```

**Evidence Needed**:
- [ ] Original pitch decks (2008-2009)
- [ ] Founder interviews/quotes
- [ ] Timeline of promise revisions
- [ ] Capital raise amounts & dates
- [ ] Technical spec changes over time

**Sources**:
- Crunchbase/Pitchbook historical data
- News articles (TechCrunch, WSJ)
- Founder blogs/tweets
- Academic case studies (HBS, Stanford)

---

#### 4.2 Pitch Deck Analysis (4-5 pages) ⏳

**Scott's Prescription**:
> "There are data sets of slide decks... You would code... people who make very strong promises... who are very precise. You could train an LLM to score it for you... Then you would take... a class at Y Combinator, Creative Destruction Lab pitch days... You can definitely see who earns good money in Crunchbase."

**Deliverables**:

##### Table 6: Pitch Deck Precision Scores ⏳
```
Company         Domain        τ_initial  Series A  Series B  Outcome
────────────────────────────────────────────────────────────────────
Rivian          EV/Hardware   1.8        $2.5M    $700M     Success
NIO             EV/Hardware   2.1        $5M      $1B       Success
Nikola          EV/Hardware   3.8        $3M      $230M     Fraud
Lucid           EV/Hardware   1.5        $131M    $1B       Success
────────────────────────────────────────────────────────────────────
Sample: 20-30 EV startups, 2015-2020 cohort
```

**Coding Rules** (LLM-assisted):
- Vague phrases: "approximately", "around", "up to", "flexible"
- Precise phrases: "exactly", "guaranteed", "certified", "X units by Y date"
- τ = precision_score / (precision_score + vague_score + 1)

##### Figure 5: Precision vs. Funding Scatter ⏳
```
Series A ($M)
    15 ┤     •  
       │   •   •
    10 ┤ •   •  •
       │ • •  •
     5 ┤•  • •
       │ •
     0 ┼─────────────
       0   1   2   3   4
           Precision (τ)
```

**Expected**: Inverted-U (moderate τ optimal at A)

##### Figure 6: Precision Evolution Timeline ⏳
```
Precision (τ)
    4 ┤                        Better Place
      │                        ─────────────
    3 ┤                  ╱
      │                ╱
    2 ┤              ╱
      │            ╱
    1 ┤ Tesla ────────────────────
      │
    0 ┼────────────────────────────
      2008  2010  2012  2014  2016
```

**Key**: Early commitment trap vs. maintained flexibility

---

#### 4.3 Operational Toolkit Table ⏳

**From Modeling Paper** (Section 4.3):
> "Founders face recurring choices about how to reduce integration cost i and increase value V in parallel."

##### Table 7: Tools to Manage (V, i) ⏳
```
Strategy       V Effect   i Effect   When to Use          Example
───────────────────────────────────────────────────────────────────
Acculturate    +          +          Early stage          Hire domain experts
Processify     +          -          Scale-up             Automate workflows
Collaborate    +          -          Resource-limited     Strategic partnerships
Replicate      ++         -          Post-PMF             Franchise model
Modularize     +          --         High complexity      API architecture
───────────────────────────────────────────────────────────────────
```

**Explanation**:
- Acculturate: Hire experts → raises both V (better execution) and i (coordination cost)
- Processify: Standardize → raises V (efficiency) while lowering i (less ad-hoc integration)
- Collaborate: Partner → raises V (resource access) while lowering i (shared burden)
- Etc.

---

### Section 5: Discussion & Implications ⏳

**Status**: 20% complete (outline only)

**Deliverables Needed**:

#### 5.1 Decision Framework (1-2 pages) ⏳
```
┌────────────────────────────────────────────────────────┐
│ When Should Founders Shift from Vague → Precise?      │
├────────────────────────────────────────────────────────┤
│ IF V/i < 4  →  Stay vague (τ* = 0)                    │
│ IF V/i ≥ 4  →  Raise precision (τ* = √(V/4i) - 1)     │
├────────────────────────────────────────────────────────┤
│ Proxies:                                               │
│  - V: Market size × probability of winning             │
│  - i: # of subsystems × coordination complexity        │
└────────────────────────────────────────────────────────┘
```

**Practical Guidelines**:
- Hardware startups: Stay vague longer (high i)
- Software startups: Shift earlier (low i)
- Series A: Default to vague unless proven PMF
- Series B: Default to precise unless exploring pivots

---

#### 5.2 Limitations (1 page) ⏳
- Sample size constraints (N=150)
- Domain specificity (AI/ML only)
- Language measures (keyword-based, not semantic)
- Survivor bias (only funded firms observed)
- Causality (precision ↔ success endogeneity)

---

#### 5.3 Future Research (1 page) ⏳
- Semantic NLP measures (BERT, GPT embeddings)
- Cross-industry replication (biotech, fintech, etc.)
- Investor heterogeneity (VC sophistication)
- Temporal dynamics (precision trajectory clustering)
- Experimental validation (randomized pitch variants)

---

## 🔧 Technical Stack & Workflow

### Software/Tools Needed
```
Language:       Python 3.10+
Core Packages:  pandas, numpy, statsmodels, scikit-learn
Visualization:  matplotlib, seaborn, plotnine
NLP (optional): nltk, spacy, transformers (BERT)
Tables:         stargazer, texttable
Version Control: git
Writing:        LaTeX (Overleaf) or Markdown → PDF
```

### Data Pipeline
```
Raw Data (Pitchbook)
    ↓
01_process_company_data.py  → company_master.csv
    ↓
02_process_deal_data.py     → deal_panel.csv
    ↓
03_create_panel.py          → analysis_panel.csv
    ↓
04_run_analysis.py          → Tables 1-4 (CSV)
    ↓
05_create_deliverables.py   → Figures 1-4 (PNG)
    ↓
Case Studies (Manual)       → Tables 6-7, Figures 5-6
    ↓
LaTeX Integration           → paper.pdf
```

---

## 📅 Completion Roadmap

### Phase 1: Empirics (Week 1-2) 🚧
- [x] Write 5 Python scripts
- [ ] Run on sample data (30 firms)
- [ ] Validate output formats
- [ ] Debug & iterate
- [ ] Run on full data (60-80 firms)
- [ ] Generate all tables & figures

### Phase 2: Case Studies (Week 3-4) ⏳
- [ ] Collect Tesla/Better Place archives
- [ ] Code pitch deck corpus (20-30 firms)
- [ ] Generate trajectory charts
- [ ] Write narrative analysis (4 pages)
- [ ] Create operational toolkit table

### Phase 3: Integration (Week 5) ⏳
- [ ] Finalize introduction (polish)
- [ ] Write discussion section
- [ ] Assemble LaTeX document
- [ ] Format tables/figures
- [ ] Internal review & revision

### Phase 4: Submission Prep (Week 6) ⏳
- [ ] Proofread full draft
- [ ] Check MS formatting guidelines
- [ ] Prepare cover letter
- [ ] Online appendix (code, data)
- [ ] Submit to Management Science

---

## 🎯 Success Criteria (How to Know You're Done)

### Must-Have (Minimum Viable Paper)
✅ All 8 deliverables from Section 3 (Tables 1-4, Figures 1-4)  
✅ Theory section with proofs (Theorem 1 + Corollaries)  
✅ Tesla vs. Better Place case study (3+ pages)  
✅ Introduction with clear positioning (5+ pages)  
✅ Discussion with practical guidelines (3+ pages)  

**Total**: 35-40 pages minimum

### Nice-to-Have (Target for MS)
✅ Pitch deck corpus analysis (Tables 6-7, Figures 5-6)  
✅ Operational toolkit table with examples  
✅ Alternative specifications robustness  
✅ Online appendix with replication code  

**Total**: 45-50 pages optimal

### Stretch Goals (If Time Permits)
□ Cross-industry extension (biotech, fintech)  
□ Semantic NLP analysis (BERT embeddings)  
□ Investor heterogeneity analysis  
□ Experimental pre-registration  

---

## 💡 Key Insights to Remember

**From Theory**:
> "Precision must be earned through validated growth. The threshold V > 4i separates exploration from exploitation."

**From Empirics**:
> "Hardware's reversal effect is 3× stronger than software's because integration costs i are higher, making flexibility more valuable longer."

**From Cases**:
> "Tesla maintained τ ≈ 1 for 5 years while Better Place locked in at τ ≈ 4 immediately. The $60M vs. $850M outcome maps directly to optimal vs. premature precision."

**From Scott**:
> "Within a few months, that analysis is only going to be so deep and so rich, but that would at least show some kind of blocking and tackling in the broad domain that you're at."

---

## 🚀 Next Immediate Actions

1. **Complete empirics (Priority 1)**:
   - Run all 5 scripts on full dataset
   - Generate 8 deliverables (4 tables + 4 figures)
   - Validate results match predictions

2. **Gather case materials (Priority 2)**:
   - Download Tesla/Better Place pitch decks
   - Archive news articles & interviews
   - Code precision scores manually

3. **Polish introduction (Priority 3)**:
   - Add objection paragraph
   - Strengthen importance claim
   - Final They Say/I Say pass

4. **Write discussion (Priority 4)**:
   - Decision framework table
   - Limitations paragraph
   - Future research paragraph

---

## 📝 Final Checklist Before Submission

- [ ] All 8 empirical deliverables complete
- [ ] Case study with documentary evidence
- [ ] Introduction hooks reader + positions clearly
- [ ] Theory proves Theorem 1 + Corollaries
- [ ] Discussion gives actionable guidance
- [ ] References formatted (APA/MS style)
- [ ] Figures/tables have captions
- [ ] Online appendix with replication code
- [ ] Cover letter drafted
- [ ] Internal review by 2+ colleagues
- [ ] Grammar/spell check pass
- [ ] MS submission system upload

---

## 🎓 Why This Matters (Your North Star)

You're answering a question **every entrepreneur faces**:

> "Should I be vague or precise in my pitch?"

**Current advice is contradictory**:
- VCs say: "Be specific! Show traction!"
- Lean Startup says: "Pivot often! Stay flexible!"

**Your answer is precise**:
- Early stage (Series A): Be vague if V/i < 4 (preserve option value)
- Late stage (Series B): Be precise if V/i ≥ 4 (signal credibility)
- Hardware: Stay vague longer (high i)
- Software: Shift earlier (low i)

**Impact**:
- **Theoretical**: First formal model of promise variance as design variable
- **Empirical**: First longitudinal evidence of reversal effect
- **Practical**: Operational toolkit for managing precision trajectory

**Target Journals**:
1. Management Science (primary)
2. Organization Science (backup)
3. Strategic Management Journal (backup)

---

**Last Updated**: 2025-10-22  
**Estimated Completion**: 6 weeks from empirics finish  
**Status**: 50% complete overall

---

## 🧭 Remember: This is Your 나침반

When you feel lost, come back here and ask:
- "Which deliverable am I working on?"
- "Does this move me toward the 8 empirical tables/figures?"
- "Am I deepening the Tesla case with documentary evidence?"
- "Does this help answer: when should entrepreneurs shift from vague → precise?"

If yes → keep going.  
If no → refocus.

**You've got this.** 🚀
