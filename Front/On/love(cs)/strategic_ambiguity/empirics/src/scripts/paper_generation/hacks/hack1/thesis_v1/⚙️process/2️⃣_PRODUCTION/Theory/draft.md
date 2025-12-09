# Theory Section: Promise Precision and Venture Funding

## 1. Core Puzzle

**Research Question:**  
When does vagueness in entrepreneurial promises help or hurt venture funding outcomes?

---

## 2. Theoretical Framework

### 2.1 Two Forces in Entrepreneurial Signaling

#### 🔴 **Value of Information (VOI)** - Early Stage Dominance
- **Mechanism:** Investors need precise signals to reduce uncertainty
- **Effect:** Vague promises → Lower Series A funding
- **Literature Base:**
  - Zuckerman (1999): Category ambiguity → illegitimacy discount
  - Pan et al. (2018): Concrete language → favorable investor reactions
  - Hannan et al. (2007): Fuzzy signals raise cognitive costs

#### 🔵 **Real Option (RO)** - Later Stage Emergence  
- **Mechanism:** Flexibility to pivot preserves option value under uncertainty
- **Effect:** Vague promises → Higher Series B+ success (when exercisable)
- **Literature Base:**
  - Pontikes (2012): Ambiguous positions broaden consideration sets
  - Granqvist et al. (2013): Label hedging preserves flexibility
  - Wry et al. (2014): Hybrid categories attract capital in nascent fields

---

## 3. Hypotheses

### **H1: Vagueness → Early Funding (−)**
```
Early Stage Funding = α₀ + α₁(Vagueness) + ε
Prediction: α₁ < 0
```

**Logic:** At Series A, VOI dominates. Clear promises reduce investor uncertainty.

---

### **H2a: Vagueness × Hardware → Later Success (−)**
```
P(Series B+) = β₀ + β₁(Vagueness) + β₂(Hardware) + β₃(Vagueness×Hardware)
Prediction: β₃ < 0
```

**Logic:** Hardware firms face:
1. **RO Exercise Friction:** Physical pivots require scrapping tooling, re-testing, inventory write-offs
2. **Evaluation Homogeneity:** Engineering culture values precision (Scott et al., 2019)

---

### **H2b: Vagueness → Later Success (+) for Software**
```
P(Series B+) = β₀ + β₁(Vagueness) when Hardware = 0
Prediction: β₁ > 0
```

**Logic:** Software firms can:
1. **Exercise Options Cheaply:** Code rewrites << physical retooling
2. **Exploit Evaluator Heterogeneity:** Market uncertainty → diverse evaluations

---

## 4. Trade-off Formalization

**Decision Variable:** V ∈ [0,1] (Promise Vagueness)

**Objective Function:**
```
max E[FA(V)] + E[FB+(V|A)]
 V
```

Where:
- FA = Series A funding amount
- FB+ = Series B+ funding amount (conditional on getting A)

**Comparative Statics:**
- Early: ∂E[FA]/∂V < 0  (VOI dominates)
- Later: ∂E[FB+]/∂V > 0 when options exercisable (RO > VOI)
         ∂E[FB+]/∂V < 0 when options rigid (VOI still dominates)

---

## 5. Key Constructs

| Construct | Operationalization | Source |
|-----------|-------------------|---------|
| **Vagueness (V)** | Composite index: Categorical abstractness + Concreteness deficit | Pontikes (2012); Pan et al. (2018) |
| **Early Funding (E)** | Series A amount ($M) | PitchBook |
| **Later Success (L)** | P(Series B+ within 17 months) | PitchBook |
| **Hardware (H)** | Industry classification + keyword detection | Fine (2000); own coding |

---

## 6. Contribution

**Bridging Two Schools:**
1. **Information School (Economics/Strategy):** Vagueness as credibility cost
2. **Options School (Operations):** Vagueness as flexibility preservation

**Novel Insight:**  
The **temporal reversal** (early penalty → later benefit) is **architecture-contingent** (hardware vs. software).

---

## Next: Empirical Tests

See `TO_EMPIRICS.txt` for variable specifications and expected outputs.
