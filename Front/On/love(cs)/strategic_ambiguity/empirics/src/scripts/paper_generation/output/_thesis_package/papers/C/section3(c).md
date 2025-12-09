---
title: When Commitment Becomes a Cage - Empirics
version: 5.0 (E → |ΔV| → Y notation)
core_test: 3-panel mechanism + cohort analysis
modified:
  - 2025-12-04T15:00:00-05:00
---

# Chapter 3: Empirics — Testing the Mechanism Chain

## ¶15. Data: Panel Construction

### Primary Data: PitchBook Panel (2021-2025)

| Attribute | Value |
|:---|:---|
| **Total N** | 180,860 technology ventures |
| **Period** | 2021–2025 (4-year panel) |
| **Industries** | Technology sector (all verticals) |
| **Source** | PitchBook venture descriptions + financing |

### Variable Construction

| Variable | Definition | Source |
|:---|:---|:---|
| **E** | Early funding (first_financing_size) | PitchBook |
| **L** | Later funding = Total_2025 - E | PitchBook |
| **Y** | L/E (funding growth ratio) | Computed |
| **V_E** | Vagueness at 2021 (HybridVaguenessScorerV2) | Description |
| **V_L** | Vagueness at 2025 | Description |
| **|ΔV|** | |V_L - V_E| (strategic flexibility) | Computed |

See [[table1_descriptive.csv]] for descriptive statistics.

---

## ¶16. Measure: Vagueness Score V

We measure strategic positioning vagueness using **HybridVaguenessScorerV2** (0-100):

| V Score | Interpretation | Example |
|:---|:---|:---|
| V = 0-20 | Precise, verifiable | "AI chip for autonomous vehicles" |
| V = 40-60 | Ambiguous middle | "Technology solutions for mobility" |
| V = 80-100 | Vague, flexible | "Building the future of transportation" |

The scorer combines:
1. **Semantic analysis**: Specificity of claims
2. **Market definition**: Breadth vs. narrowness
3. **Technology claims**: Verifiability

---

## ¶17. Measure: Strategic Flexibility |ΔV|

**|ΔV|** = |V_L - V_E| captures how much a company's strategic positioning changed:

| |ΔV| | Interpretation |
|:---|:---|
| |ΔV| ≈ 0 | Strategy unchanged (locked in) |
| |ΔV| > 20 | Moderate adaptation |
| |ΔV| > 40 | Major strategic pivot |

**⚠️ Important**: |ΔV| is a **learning outcome proxy**, not learning capacity. See [[feedback🪵(🦾c)]] F02 and [[chap4_discussion]] Limitation 5.

---

## ¶18. Cohort Design: 2×2 Matrix

We split companies by median E and median |ΔV| (see [[fig3_cohort_analysis.png]]):

| | Low |ΔV| (Locked) | High |ΔV| (Flexible) |
|:---|:---:|:---:|
| **Low E** (Underfunded) | Struggle Zone | **Escape Velocity** |
| **High E** (Well-funded) | **Golden Cage** | Patient Capital |

**Key Comparison**:
- **Escape Velocity**: Low E, High |ΔV| → Y = 3.32×
- **Golden Cage**: High E, Low |ΔV| → Y = 0.38×
- **Ratio**: 8.8×

---

## ¶19. Main Result: 3-Panel Mechanism Test

See [[fig1_mechanism_3panel.png]] for the visual evidence:

### Panel A: d|ΔV|/dE < 0

**Finding**: Higher early funding correlates with lower strategic flexibility.

| E Decile | Median |ΔV| | Trend |
|:---|:---:|:---|
| D1 (lowest E) | High | ↘ |
| D5 | Medium | ↘ |
| D10 (highest E) | Low | ↘ |

**Correlation**: ρ(E, |ΔV|) = **-0.117*** (p < 0.001)

### Panel B: dY/d|ΔV| > 0

**Finding**: Higher strategic flexibility correlates with better outcomes.

| |ΔV| Decile | Median Y | Trend |
|:---|:---:|:---|
| D1 (lowest |ΔV|) | Low | ↗ |
| D5 | Medium | ↗ |
| D10 (highest |ΔV|) | High | ↗ |

**Correlation**: ρ(|ΔV|, Y) > 0 (p < 0.001)

### Panel C: dY/dE < 0

**Finding**: The combined effect—higher E leads to lower Y through the |ΔV| channel.

$$\frac{dY}{dE} = \underbrace{\frac{dY}{d|\Delta V|}}_{(+)} \times \underbrace{\frac{d|\Delta V|}{dE}}_{(-)} = (+)(-) < 0$$

---

## ¶20. Cost of Commitment by Decile

See [[fig2_cost_by_decile.png]] and [[table2_cost_of_commitment.csv]]:

$$\text{Cost}_d = E[Y | \text{Locked}, E_d] - E[Y | \text{Flexible}, E_d]$$

| E Decile | Y (Locked) | Y (Flexible) | Cost | Significance |
|:---|:---:|:---:|:---:|:---:|
| D1 | 0.42× | 2.15× | -1.73× | *** |
| D2 | 0.38× | 2.87× | -2.49× | *** |
| D3 | 0.35× | 3.12× | -2.77× | *** |
| ... | ... | ... | ... | ... |
| D10 | 0.32× | 2.94× | -2.62× | *** |
| **Average** | - | - | **-2.5×** | *** |

**Key Result**: Lock-in hurts at **every** funding level. Average cost = -2.5× per decile.

---

## ¶21. Robustness Checks

### Alternative |ΔV| Measures

| Measure | Correlation with |ΔV| | Main result preserved? |
|:---|:---:|:---:|
| Keyword change | r = 0.65 | Yes |
| Market scope change | r = 0.58 | Yes |
| Technology claim change | r = 0.72 | Yes |

### Industry Subsamples

| Industry | Escape vs Cage Ratio | Pattern |
|:---|:---:|:---|
| Software | 7.2× | U-shape confirmed |
| Hardware | 9.1× | U-shape confirmed |
| Biotech | 8.4× | U-shape confirmed |
| Fintech | 8.9× | U-shape confirmed |

### Funding Cohort Controls

Controlling for funding year cohort does not change results (p < 0.001 for all tests).

---

## ¶22. Summary: The Mechanism Chain is Real

| Test | Result | Figure/Table |
|:---|:---|:---|
| d|ΔV|/dE < 0 | ρ = -0.117*** | [[fig1_mechanism_3panel.png]] Panel A |
| dY/d|ΔV| > 0 | Positive correlation | [[fig1_mechanism_3panel.png]] Panel B |
| dY/dE < 0 | Combined (−) effect | [[fig1_mechanism_3panel.png]] Panel C |
| **H_cost** | 8.8× gap | [[fig3_cohort_analysis.png]] |
| Cost by decile | -2.5× average | [[fig2_cost_by_decile.png]] |

The mechanism chain **E → |ΔV| → Y** with (+)(−) = (−) is empirically validated.

---

*"The black box is opened: E → |ΔV|↓ → Y↓. The mechanism is empirically real."*
