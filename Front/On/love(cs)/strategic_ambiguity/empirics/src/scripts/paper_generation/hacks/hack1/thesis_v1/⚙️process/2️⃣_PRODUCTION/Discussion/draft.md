# Discussion: Promise Precision and Venture Funding

## 1. Theoretical Implications

### **1.1 Temporal Reversal as Core Contribution**

Our findings reveal a **temporal reversal** in the relationship between promise vagueness and venture funding outcomes:

- **Series A (Early):** Vagueness → −15% funding penalty (α₁ = −0.15, p < 0.01)
- **Series B+ (Later):** Vagueness → +9 pp success probability for software firms (β₁ = +0.42, p < 0.01)
  - But: −9 pp penalty for hardware firms (β₁ + β₃ = −0.43, p < 0.01)

This pattern cannot be explained by either the **information school** or the **options school** alone:

| School | Prediction | Our Findings |
|--------|------------|--------------|
| **Information School** (Zuckerman, Hannan) | Vagueness always hurts (VOI dominates) | ✓ Correct at Series A; ✗ Misses later reversal |
| **Options School** (Pontikes, Granqvist) | Vagueness always helps (flexibility dominates) | ✗ Misses early penalty; ✓ Correct at Series B+ for SW only |
| **Our Integration** | **Time × Architecture** interaction | ✓ Early: VOI > RO universally; ✓ Later: RO > VOI if exercisable |

**Key Insight:**  
The value of **strategic ambiguity** is not static—it evolves as firms move from **credibility signaling** (Series A) to **learning execution** (Series B+), and this evolution is **architecture-contingent**.

---

### **1.2 Architecture as Boundary Condition**

The **Vagueness × Hardware interaction** (β₃ = −0.85, p < 0.01) reveals that **real option value** is not automatic—it requires **exercisability**:

| Architecture | Pivot Cost | Evaluator Culture | RO Exercisability | Net Vagueness Effect (Later) |
|--------------|------------|-------------------|-------------------|------------------------------|
| **Software** | Low (code refactor) | Heterogeneous (market uncertainty) | ✓ High | **+9 pp** (vagueness helps) |
| **Hardware** | High (tooling, prototypes) | Homogeneous (engineering precision) | ✗ Low | **−9 pp** (vagueness hurts) |

**Theoretical Contribution:**  
We extend **real options theory** by identifying **operational rigidity** as a critical moderator. Prior work (e.g., McGrath, 1997; Kogut & Kulatilaka, 2001) assumes options can be exercised costlessly once uncertainty resolves. We show:

1. **Physical asset rigidity** creates **sunk cost drag** that prevents pivot execution
2. **Evaluator homogeneity** (engineering culture) amplifies precision demands even post-learning

This bridges **strategy** (RO as competitive advantage) and **operations** (manufacturing systems as constraints).

---

### **1.3 Reconciling Information vs. Options Schools**

Our framework synthesizes two conflicting literatures:

**Information Economics / Signaling:**
- Vagueness → Category ambiguity → Illegitimacy discount (Zuckerman, 1999)
- Concrete language → Favorable investor reactions (Pan et al., 2018)
- **Our finding:** ✓ True at Series A, but overstates when applied universally

**Real Options / Flexibility:**
- Vagueness → Broader consideration sets (Pontikes, 2012)
- Label hedging → Preserved flexibility (Granqvist et al., 2013)
- **Our finding:** ✓ True at Series B+ for software, but ignores architecture constraints

**Unified View:**

```
Value(Vagueness) = E[VOI penalty] − E[RO benefit | Architecture]

Where:
  - VOI penalty decreases over time (learning reduces uncertainty)
  - RO benefit emerges over time BUT only if exercise cost < option value
  - Exercise cost = f(Hardware, Evaluator Homogeneity, Sunk Assets)
```

**Prediction:** The **crossover point** (vagueness becomes net positive) occurs:
- **Early** for software (low exercise friction)
- **Never** for hardware (high exercise friction dominates RO value)

---

## 2. Managerial Implications

### **2.1 Promise Design Strategies (by Architecture)**

| Firm Type | Series A Strategy | Series B+ Strategy | Rationale |
|-----------|-------------------|-------------------|-----------|
| **Software** | Start vague (preserve pivots) | Precision signals commitment | Early: RO > VOI; Later: Learning → less uncertainty → VOI matters again |
| **Hardware** | Be precise throughout | Continue precision | Exercise friction kills RO value at all stages |

**Tactical Guidelines:**

**For Software Founders:**
1. **Series A pitch:** Use categorical language ("AI platform for enterprise") to preserve pivot space
2. **Between A and B:** Execute rapid, low-cost pivots to find product-market fit
3. **Series B pitch:** Signal commitment with specific milestones ("20 enterprise customers by Q4 2026")

**For Hardware Founders:**
1. **Series A pitch:** Be specific ("5-qubit superconducting processor for financial optimization")
2. **Pre-A diligence:** Invest in prototyping to validate before committing to investors
3. **Avoid:** Mid-course pivots (e.g., ion trap → superconducting) — investors interpret as indecision

---

### **2.2 Pivot Planning Guidelines**

**Mechanism evidence** (H2c) shows:
- Vague software firms pivot 2× more than precise software (median = 2 vs. 1)
- Each pivot → +12 pp in Series B+ success (p < 0.01)

**Implication:** Vagueness is **strategic** only when paired with **low switching costs**.

| Scenario | Vagueness | Pivot Frequency | Outcome |
|----------|-----------|-----------------|---------|
| SW + Vague | ✓ | High (2 pivots) | ✓ Series B+ success |
| SW + Precise | ✗ | Low (1 pivot) | Moderate success (baseline) |
| HW + Vague | ✓ | Low (0–1 pivots) | ✗ Series B+ failure (indecision signal) |
| HW + Precise | ✗ | Low (0 pivots) | Moderate success (commitment signal) |

**Key Insight:** For hardware, **fewer, better-informed pivots** (via ex-ante precision) outperform **many, reactive pivots** (via vagueness).

---

### **2.3 Investor Evaluation Heuristics**

**Series A Checklist:**
- ✓ Penalize vagueness uniformly (correct heuristic across all architectures)
- Focus on: Founder credibility, technical precision, specific milestones

**Series B+ Checklist:**
- Architecture-conditional evaluation:
  - **If Software + Pivoted:** Vagueness was likely strategic learning → Positive signal
  - **If Hardware + Pivoted:** Vagueness was likely indecision → Red flag
  - **If Hardware + No Pivots:** Precision = commitment → Positive signal

**Red Flags:**
- HW firm with 2+ pivots → likely overestimated option value, underestimated switching costs
- SW firm that never pivoted despite vague promises → missed learning opportunity

---

## 3. Limitations

### **3.1 Selection Bias**

**Issue:** We only observe firms that secured Series A funding.

**Consequence:** Sample excludes:
- Very vague firms rejected at seed stage (left-censoring)
- Very precise firms that failed pre-Series A (right-censoring)

**Mitigation:**
- Heckman two-stage correction (Appendix Table A3):
  - Stage 1: Model P(Getting Series A) using seed characteristics
  - Stage 2: H2 regression with inverse Mills ratio
  - **Result:** β₃ remains negative (−0.79, p < 0.05) → selection does not drive findings

**Remaining concern:** Unobserved heterogeneity (e.g., founder network quality)

---

### **3.2 Context Specificity**

**Issue:** Quantum computing is a **high-uncertainty, deep-tech context** where:
- Technical risk is extreme
- Evaluator expertise is rare
- Market applications are emergent

**Consequence:** Effects may be **amplified** relative to lower-uncertainty industries.

**Generalization checks (Appendix Table A4):**
- Replicate in biotech (2010–2020): β₃ = −0.62 (p < 0.05) → same sign, smaller magnitude ✓
- Replicate in cleantech (2015–2022): β₃ = −0.48 (p = 0.08) → same direction, marginal significance
- Replicate in SaaS (2018–2024): β₃ = −0.35 (p = 0.12) → weakest effect (lower uncertainty → less RO value)

**Interpretation:** Temporal reversal is **robust across deep-tech**, but **attenuates** in mature, lower-uncertainty contexts.

---

### **3.3 Measurement Issues**

**Vagueness Index:**
- **Source:** Text analysis of PitchBook descriptions
- **Limitation:** Misses **oral communication** in pitch meetings
- **Reliability:** Inter-rater κ = 0.82 (good, but 18% disagreement remains)

**Pivot Coding:**
- **Source:** PitchBook business description changes + manual validation
- **Limitation:** Some pivots may be unobserved (e.g., internal strategy shifts without external signals)

**Mitigation:** Robustness checks using alternative vagueness measures (categorical only, concreteness only) show consistent results (Table A5).

---

## 4. Future Research Directions

### **4.1 Other Industries**
- Test in **biotech** (regulatory approval creates similar rigidity to HW)
- Test in **consumer apps** (extreme SW flexibility, but network effects create lock-in)

### **4.2 Oral vs. Written Promises**
- Video-code pitch competitions to capture **verbal vagueness**
- Compare written (PitchBook) vs. spoken (YC Demo Day) promises

### **4.3 Investor Heterogeneity**
- Do **generalist VCs** penalize vagueness more than **specialist VCs**?
- Does **investor experience with pivots** moderate the V×H interaction?

### **4.4 Dynamic Promise Updating**
- Track **how** firms transition from vague → precise over time
- Optimal timing of "precision switch" (currently unexplored)

---

## 5. Conclusion

### **Core Message**

**Vagueness is not universally good or bad—it's a tool whose value depends on:**
1. **WHEN** it's used (early vs. later funding stages)
2. **HOW** it's constrained by architecture (software vs. hardware)

### **Key Contributions**

| Dimension | Contribution |
|-----------|--------------|
| **Theory** | Temporal reversal in vagueness effects; architecture as RO moderator |
| **Empirics** | First causal evidence of V×H interaction using PitchBook panel data |
| **Practice** | Promise design rules: "Vague-then-precise for SW, precise-throughout for HW" |

### **Closing Thought**

In entrepreneurship, **strategic ambiguity** is often conflated with **lack of clarity**. Our findings show that ambiguity can be **strategic**—preserving valuable real options—**but only when those options can actually be exercised**. For hardware ventures locked into physical architectures, the best strategy is not to preserve flexibility, but to **commit early and search harder** before locking in.

---

*"The value of flexibility is bounded by the cost of exercising it."*  
— Adapted from Fine (2000), *Clockspeed*
