---
modified:
  - 2025-12-04T07:15:00-05:00
version: 2.1-draft
status: J부대 검토용 초안
---
# Chapter 1: Introduction — The Commitment Trap

**Version:** 2.1 Draft (for J-Agent Review)
**Variable Convention:** V only (Low V = High Commitment, High V = High Flexibility)

---

## Abstract

When should entrepreneurs commit to a strategic path? Real options theory suggests deferring commitment preserves flexibility, yet securing funding often requires concrete promises. Among **488,381 technology ventures** across four industries, we observe a robust U-shaped pattern: both highly committed (Low V) and highly flexible (High V) ventures succeed, while intermediate strategies fail. We propose **Endogenous Appropriability** (Gans & Stern, 2017) as the structural mechanism: choosing a Control strategy (IP, technology moat) forecloses Execution options (pivot, adaptation). This is not merely belief lock-in but **stopped optionality** — strategy choice structurally eliminates alternatives. The "murky middle" (moderate V) commits enough to attract scrutiny but not enough to satisfy it, while preserving too little flexibility to pivot. The strategic implication: commitment is not a dial to tune but a **strategy to choose**.

---

## ¶1 📿 Gospel: The Commitment Premium

Entrepreneurship folklore celebrates bold commitment. Steve Jobs bet Apple on the iPhone. Elon Musk committed Tesla to vertical integration before the first Roadster shipped. Venture capitalists reward founders who "burn the boats" — eliminating retreat options to signal conviction.

This gospel aligns with signaling theory: concrete commitments reduce information asymmetry, enabling investors to verify claims and separate capable founders from pretenders. The prescription is clear: **commit early, commit hard**.

We formalize this conventional wisdom:

> **H₀ (Commitment Null):** Lower promise vagueness (Low V) monotonically increases venture growth.

---

## ¶2 🧩 Puzzle: When Commitment Becomes a Trap

Yet among 488,381 technology ventures in our PitchBook dataset spanning 2005–2023, we observe a pattern that defies this prediction. Survival to late-stage funding is **U-shaped** in vagueness.

| Case | V Score | Strategy | Outcome |
|:---|:---:|:---|:---|
| **Mobileye** | V ≈ 10 | Specific specs ("77GHz radar") | $15.3B acquisition |
| **Better Place** | V ≈ 50 | Vision + rigid specs | Bankruptcy ($850M lost) |
| **Tesla** | V ≈ 90 | Pure mission ("sustainable transport") | $800B valuation |

Both extremes succeed; the middle fails. Why?

**The puzzle deepens in autonomous vehicles:**
- **Waymo** (Low V): Committed to LiDAR, HD maps, L4 → geofenced, limited scale
- **Cruise** (Low V): $10B+ invested → 50% layoffs, operations paused
- **Argo AI** (Low V): Ford + VW backing → complete shutdown
- **Comma.ai** (High V): Vision-only, flexible → wide deployment
- **Tesla FSD** (High V): "Sustainable transport" mission → continuous adaptation

The most committed ventures, with the most resources, failed to pivot when paradigm shifts occurred.

---

## ¶3 😮 RQ: When Does Commitment Become a Trap?

When does strategic commitment help versus hurt venture growth? If both highly committed and highly flexible ventures succeed, what explains the failure of the middle ground?

More fundamentally: **Why can't well-funded, committed ventures pivot when they need to?**

---

## ¶4 🔎 Lens: Endogenous Appropriability and Stopped Optionality

We propose two complementary mechanisms:

### Mechanism 1: Endogenous Appropriability (Gans & Stern, 2017)

Appropriability strategy is a **choice**, not an endowment. Entrepreneurs choose between:
- **Control strategy** (Low V): Invest in IP, technology moats, specific claims
- **Execution strategy** (High V): Invest in speed, flexibility, broad positioning

**Critical insight**: These are **strategic substitutes**. Choosing Control forecloses Execution options — not because of psychology but because of **structure**.

| Strategy | V Level | Investment | Forecloses |
|:---|:---:|:---|:---|
| Control | Low V | IP, specific tech, verifiable claims | Pivot options |
| Execution | High V | Speed, flexibility, broad vision | IP protection |

Waymo chose LiDAR (Control) → invested billions in LiDAR-specific assets → vision-based pivot became **structurally impossible**, not just psychologically difficult.

### Mechanism 2: Investor Sorting and Belief Lock-in

Low V ventures attract Analyst investors who:
- Demand verifiable milestones
- Evaluate concrete technical claims
- **Reinforce the existing path** (τ ↑, σ² ↓)

When investor beliefs align with founder beliefs, new signals are interpreted through the existing frame. The pivot threshold rises:

$$\text{Pivot threshold} = \mu + k\sigma$$

As σ → 0 (belief homogeneity), even strong disconfirming evidence is dismissed as noise.

### The Murky Middle Trap

| V Level | Strategy | Outcome |
|:---|:---|:---|
| Low V | Control: verifiable, falsifiable → can be proven wrong → pivot or validated | **Success** |
| High V | Execution: flexible, adaptable → can pivot freely | **Success** |
| Middle V | Neither: too vague to verify, too committed to pivot | **Trapped** |

---

## ¶5 😆 Solution: Confirmed U-Shape Across All Industries

Our empirical analysis yields two main findings:

**First, we reject H₀.** The monotonic positive effect of commitment (Low V) on growth does not hold.

**Second, we confirm the U-shape (H₁).** Using non-parametric quartile analysis with χ² tests:

| Industry | N | Q1 (Low V) | Q2 | Q3 | Q4 (High V) | Murky Middle Δ | χ² | p |
|:---|---:|---:|---:|---:|---:|---:|---:|:---:|
| Transportation | 154,148 | 5.7% | 2.9% | 4.0% | 8.6% | **+3.7pp** | 1430.9 | <0.001 |
| Software | 226,896 | 7.8% | 4.8% | 6.8% | 8.0% | **+2.1pp** | 564.8 | <0.001 |
| Hardware | 50,390 | 6.0% | 3.7% | 3.9% | 8.7% | **+3.6pp** | 398.6 | <0.001 |
| Pharma | 56,947 | 8.8% | 5.7% | 6.2% | 10.6% | **+3.7pp** | 305.7 | <0.001 |

**Note:** Murky Middle Penalty = [(Q1+Q4)/2] − [(Q2+Q3)/2]

### Additional Evidence: ΔV and Early Funding

We further test whether early funding **locks in** vagueness level. If Endogenous Appropriability operates, ventures with more early funding should show **less change in V** over time (stopped optionality).

Preliminary finding: ΔV ∝ 1/(Early Funding) — more early funding → less strategic flexibility.

---

## ¶6 🗺️ Closest Papers

This paper contributes to literatures on commitment, flexibility, and appropriability:

- **Gans & Stern (2017):** Endogenous appropriability — Control and Execution as strategic substitutes. We extend: these strategies map onto vagueness (V).
- **Kogut & Kulatilaka (2001):** Capabilities as real options. We extend: options require not just resources but **structural capacity** to exercise.
- **Leonard-Barton (1992):** Core rigidity. We provide the mechanism: strategy choice forecloses alternatives.
- **Gans, Stern & Wu (2019):** Entrepreneurial strategy as experimentation. We show: vagueness level determines *what kind* of experiments are possible.

---

## ¶7 🗄️ Organization

- **Section 2 (Theory):** Endogenous Appropriability + Bayesian belief lock-in
- **Section 3 (Empirics):** 488K PitchBook ventures + AV case triangulation + ΔV analysis
- **Section 4 (Discussion):** "Stopped Optionality" as structural trap, managerial implications

---

## Key Theoretical Contributions

1. **Structural, not psychological**: The trap is about strategy choice foreclosing options, not cognitive bias.

2. **Endogenous Appropriability mapping**: Control ↔ Low V, Execution ↔ High V — connects appropriability theory to vagueness measurement.

3. **Stopped Optionality**: Early funding + low V = reduced ΔV = structurally eliminated pivot options.

4. **Murky Middle as strategic failure**: Neither verifiable enough for Control nor flexible enough for Execution.

---

## Connection to ✌️U

This paper uses the **same V variable** as ✌️U but with different framing:

| ✌️U | 🦾C |
|:---|:---|
| V = communication strategy | V = appropriability strategy |
| Low V = Analyst audience | Low V = Control strategy |
| High V = Believer audience | High V = Execution strategy |
| "Playbook to choose" | "Stopped optionality" |

The U-shape is identical; the mechanism interpretation differs.

---

**Punchline:** *"The trap is structural, not psychological. Strategy choice forecloses options — choose wisely."*

---

*Ready for J-Agent (11_JI🟢, 12_JT🟢, 13_JE🟢, 14_JD🟢) review.*
