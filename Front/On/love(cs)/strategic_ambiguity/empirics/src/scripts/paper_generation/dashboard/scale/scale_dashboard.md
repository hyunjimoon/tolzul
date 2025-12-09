---
modified:
  - 2025-12-09T07:48:08-05:00
---
# The Promise Vendor
## Strategic Ambiguity and the Capital-Flexibility Paradox in Deep-Tech Ventures

> **Dissertation Dashboard** | MIT PhD  
> **Advisors**: Charlie Fine (Operations) · Scott Stern (Strategy)  
> **Candidate**: Angie H. Moon  
> **Shared Folder**: `_thesis_package/`

---

# PART I: STATIC REFERENCE (Literature & Foundations)

## 📚 Core Literature Map

```dataview
TABLE thesisPaper as "Paper", thesisChapter as "Ch", rank as "⭐"
FROM "Space/Library/1논문용"
WHERE file.name.startsWith("📜") AND thesisPaper
SORT thesisPaper DESC, rank DESC
LIMIT 30
```

### Primary Theoretical Foundations

| Paper                | Core Idea                                                             | Thesis Application                           |
| :------------------- | :-------------------------------------------------------------------- | :------------------------------------------- |
| **Ghemawat (1991)**  | Strategy = commitment via sticky assets; flexibility has option value | Golden Cage mechanism; AOC formalization     |
| **Spence (1973)**    | Signaling under asymmetric information                                | Precision prescription (null hypothesis)     |
| **Eisenberg (1984)** | Strategic ambiguity enables projection                                | Believer investor mechanism                  |
| **Bolton (2002)**    | Product differentiation under uncertainty (?)                         | S₂ parameter mapping to V                    |
| **Barney (1991)**    | Resources create competitive advantage                                | Boundary condition: when resources constrain |

### Ghemawat (1991): Commitment as Dynamic Constraint

**Book**: *Commitment: The Dynamic of Strategy*

**Central Thesis**: Strategy is about commitment—costly, hard-to-reverse choices that create persistent differences via lock-in, lock-out, lags, and inertia.

**Three-Layer Value Architecture**:

| Layer          | Function              | Mapping to thesis     |
| :------------- | :-------------------- | :-------------------- |
| Positioning    | Static value creation | Promise precision V   |
| Sustainability | Defending value       | Stakeholder alignment |
| Flexibility    | Value of revisability | k* = F⁻¹(CR)          |

**Type I vs Type II Organizations** (Ch.7):

| Type | Error Bias | Structure | Thesis Mapping |
|:---|:---|:---|:---|
| Type I | Omission errors | Hierarchical, serial | **Analyst**: demand precision |
| Type II | Commission errors | Horizontal, parallel | **Believer**: accept ambiguity |

**Key Quote**: "Flexibility isn't synonymous with safety... it is an abundant store of potentially valuable revision possibilities."

**Direct Applications**:
1. **AOC** = Ghemawat's lock-in via sticky assets = "capital becomes concrete"
2. **CR** = commitment-intensive choice threshold
3. **k*** = flexibility chapter: "capital as options vs capital as concrete"

---

### Eisenberg (1984): Strategic Ambiguity

**Paper**: "Ambiguity as Strategy in Organizational Communication"

**Core Insight**: "The more ambiguous the message, the greater the room for projection."

**Functions of Ambiguity**:
1. **Unified diversity**: Diverse stakeholders coalesce around shared language
2. **Preserving options**: Vague commitments avoid premature lock-in
3. **Enabling deniability**: Abstract promises allow flexible interpretation

**Thesis Application**: Explains why Believer investors prefer vague promises—they project their own vision onto abstract positioning.

---

### Signaling Theory: The Precision Prescription

**Spence (1973)**: High-quality actors distinguish themselves via costly, verifiable signals.

**Connelly et al. (2011)**: Applied to entrepreneurship—precise promises reduce information asymmetry.

**Camuffo et al. (2020)**: "Scientific approach" to entrepreneurship emphasizes falsifiable hypotheses.

**Our Contribution**: Precision prescription holds only for verification-oriented (Analyst) audiences. For projection-oriented (Believer) audiences, vagueness dominates.

---

### Real Options in Strategy

| Paper | Contribution | Thesis Connection |
|:---|:---|:---|
| Kogut & Kulatilaka (2001) | Capabilities as options | Flexibility value formalization |
| Huchzermeier & Loch (2001) | R&D project flexibility | Staged commitment logic |
| McGrath (1999) | Failing forward | Learning from abandoned options |

---

## 📖 Paper-Specific Citations

### Paper U: Vague Promise

| Citation | Use |
|:---|:---|
| Eisenberg (1984) | Strategic ambiguity theory |
| Spence (1973) | Signaling null hypothesis |
| Sillince et al. (2012) | Rhetoric and ambiguity |
| Guzman & Stern (2020) | Observable founding choices |

### Paper C: Commitment Trap

| Citation | Use |
|:---|:---|
| Ghemawat (1991) | Commitment mechanisms |
| Barney (1991) | Resource-based theory |
| Leonard-Barton (1992) | Core rigidities |
| Levinthal & March (1993) | Success trap |

### Paper N: Promise Vendor

| Citation | Use |
|:---|:---|
| Arrow (1951) | Newsvendor foundation |
| Dixit & Pindyck (1994) | Investment under uncertainty |
| Bolton et al. (2002) | Differentiation parameter S₂ |

---

# PART II: DYNAMIC DASHBOARD (Live Status)

## 🖥️ Live Dashboard

<div><iframe src="https://html-preview.github.io/?url=https://github.com/hyunjimoon/tolzul/blob/master/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/dashboard/scale/scale_dashboard.html" width="100%" height="1000" frameborder="0"></iframe></div>

🔗 [**Open Full Screen**](https://html-preview.github.io/?url=https://github.com/hyunjimoon/tolzul/blob/master/Front/On/love(cs)/strategic_ambiguity/empirics/src/scripts/paper_generation/dashboard/scale/scale_dashboard.html)

---

## 1. Core Thesis

**Research Question**: When do the commitments that secure early resources become constraints on long-term success?

**Central Finding**: Promise precision and venture growth exhibit a U-shaped relationship. Both highly precise and highly vague positioning outperform intermediate positioning, where 25.6% of ventures become trapped.

**Mechanism**: Audience segmentation. Precise promises attract Analyst investors who verify specific claims. Vague promises attract Believer investors who project their own vision. Intermediate positioning activates neither evaluation mode.

**Paradox**: Early capital reduces strategic flexibility (ρ = -0.052), yet flexibility predicts growth (ρ = +0.159). Flexible ventures achieve 2.7× higher growth than rigid ventures.

---

## 2. Three Papers

### Paper U: Vague Promise and Venture Growth

**RQ**: When is vagueness valuable despite signaling theory's precision prescription?

| Hypothesis | Statement | Result |
|:---|:---|:---|
| **H0** | Vagueness monotonically reduces growth | Rejected |
| **H1** | Both extremes outperform intermediate | Supported |

**Sample**: N = 408,784 ventures across 4 industries

| Quartile | Survival |
|:---:|:---:|
| Q1 (Precise) | 5.7% |
| Q2 | 2.9% |
| Q3 | 4.0% |
| Q4 (Vague) | 8.6% |

**Murky Middle Penalty**: Δ = +2.1pp to +3.7pp across industries

---

### Paper C: The Commitment Trap

**RQ**: When does early capital constrain rather than enable growth?

| Hypothesis | Evidence |
|:---|:---|
| H1: Flexibility → Growth | ρ = +0.159*** |
| H2: Capital → Rigidity | ρ = -0.052*** |
| H3: E × V interaction | Low V: -0.05; High V: +0.08 |

**Sample**: N = 123,906 ventures (panel)

**Flexibility Gap**: Top quartile achieves 2.7× median growth of bottom quartile

**Golden Cage Mechanism**:
1. Capital requires specific promises
2. Promises attract aligned stakeholders
3. Alignment compresses belief variance (σ² → 0)
4. Compressed variance blocks adaptation

---

### Paper N: The Promise Vendor

**RQ**: How should founders choose the optimal number of strategic options?

**Core Model**:
```
CR = Cu / (Cu + Co)
k* = F⁻¹(CR)
```

Where:
- Cu = cost of under-commitment (lock-in to wrong path)
- Co = cost of over-commitment (diluted execution)
- k* = optimal number of strategic options

**Investor Heterogeneity**:

| Type | Error Sensitivity | k* |
|:---|:---|:---:|
| Analyst | High Co (waste) | ≈1 |
| Believer | High Cu (miss) | >1 |

---

## 3. Strategic Prescription

**The choice is structural, not preferential.**

Founders must select a coherent channel based on their environment's cost structure:

**Analyst Channel** (Low CR):
- When: Technology risk is low; execution is the challenge
- Action: Precise promises, verifiable milestones, k* ≈ 1
- Example: Software/SaaS ventures

**Believer Channel** (High CR):
- When: Uncertainty is high; adaptation is paramount
- Action: Abstract vision, strategic ambiguity, k* > 1
- Example: Deep-tech/AV ventures

**Critical Insight**: Intermediate positioning satisfies neither audience. Analysts cannot verify claims that are too vague. Believers cannot project onto promises that are too specific. The survival penalty for intermediate positioning ranges from 2.1 to 3.7 percentage points.

---

## 4. Evidence Summary

### Industry Heterogeneity (Paper U)

| Industry | Q1 | Q2 | Q3 | Q4 | Δ | χ² |
|:---|:---:|:---:|:---:|:---:|:---:|---:|
| Transportation | 5.66% | 2.89% | 4.02% | 8.63% | +3.69pp | 1430.9*** |
| Software | 7.77% | 4.80% | 6.76% | 7.98% | +2.10pp | 564.8*** |
| Hardware | 5.95% | 3.71% | 3.85% | 8.74% | +3.57pp | 398.6*** |
| Pharma | 8.79% | 5.73% | 6.20% | 10.56% | +3.72pp | 305.7*** |

### Causal Chain (Paper C)

```
Capital (E)  ──(-0.052)──▶  Flexibility (|ΔV|)  ──(+0.159)──▶  Growth (Y)

Combined: dY/dE = ∂Y/∂|ΔV| × ∂|ΔV|/∂E = (+)(−) < 0
```

### Strategic Cohorts

| Cohort | E (Median) | |ΔV| | Y |
|:---|---:|:---:|:---:|
| Escape Velocity | $257K | 40.2 | 3.01 |
| Golden Cage | $5.4M | 19.1 | 1.95 |

---

## 5. Theoretical Contributions

| Literature | Conventional View | Our Boundary Condition |
|:---|:---|:---|
| **Signaling** | Precision reduces asymmetry | Only for Analyst audiences |
| **RBV** | Resources enable advantage | Resources can create rigidity |
| **Real Options** | Options have value | Capital destroys options via AOC |
| **Lean Startup** | k=1 and iterate | k* varies with CR |

---

## 6. Practical Implications

**For Founders**:
1. Diagnose industry CR (Cu/Co ratio)
2. If CR < 0.5: Analyst channel (precise, k ≈ 1)
3. If CR > 0.5: Believer channel (vague, k > 1)
4. Avoid intermediate positioning

**For Investors**:
1. Belief homogeneity = risk factor
2. Maintain skeptics among stakeholders
3. Stage capital to preserve flexibility

**For Policymakers**:
1. "Pick-the-winner" destroys adaptive capacity
2. Reward optionality preservation
3. Penalizing pivots harms deep-tech

---

## 7. File Registry

| Document | Location |
|:---|:---|
| **Thesis Draft** | `_thesis_package/angie_thesis_draft_v0.pdf` |
| **Figures** | `_thesis_package/figures/` |
| **Paper Sections** | `_thesis_package/papers/U,C,N/` |
| **Slides** | `_thesis_package/thesis_slides.md` |
| **BULLETIN** | `_thesis_package/📢BULLETIN.md` |
| **REGISTRY** | `_thesis_package/🗄️REGISTRY.md` |

---

**Last Updated**: 2025-12-09
