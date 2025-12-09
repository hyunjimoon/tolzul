# When Capital Becomes a Cage: The Hidden Cost of Early-Stage Commitment
## Section 3: Empirical Analysis

**Source of Truth:** [[📢BULLETIN]]
**Verified Numbers:** N_panel = 123,906 | ρ(Y, |ΔV|) = +0.159*** | ρ(E, |ΔV|)_within_V = -0.052*** | Flexibility Gap = 2.7×

---

## 3.1 Data

We analyze panel data on technology ventures tracked from early-stage funding through subsequent outcomes. Our sample is drawn from PitchBook and comprises ventures that received Seed or Series A funding between 2021 and 2025.

**Sample construction.** We begin with the 408,784 ventures from our companion paper on vagueness. We restrict to ventures with complete longitudinal data: observable positioning at both early and later stages, and complete funding histories. This yields a panel of 123,906 ventures.

| Attribute | Value |
|:----------|:------|
| Panel N | 123,906 |
| Cohort years | 2021-2025 |
| Follow-up period | 4 years |
| Industries | Technology (Software, Transportation, Hardware, Pharma) |

---

## 3.2 Measures

**Dependent variable: Growth (Y).** We measure growth as the ratio of later-stage to early-stage funding:

$$Y = \frac{L}{E} = \frac{\text{Total funding} - E}{E}$$

where E is early-stage funding (first financing) and L is subsequent funding. This ratio captures the extent to which initial investment attracted follow-on capital. Values above 1 indicate growth; values below 1 indicate contraction or failure to raise additional capital.

**Independent variable: Strategic flexibility (|ΔV|).** We measure flexibility as the absolute change in positioning vagueness between early and later stages:

$$|\Delta V| = |V_T - V_0|$$

where V₀ is initial vagueness (at first funding) and V_T is later vagueness (at follow-up). This captures revealed strategic flexibility—the extent to which the venture's positioning evolved.

**Moderator: Early-stage capital (E).** We measure E as the natural log of first financing size. The distribution is right-skewed; log transformation improves distributional properties.

**Controls.** We include industry fixed effects, founding year fixed effects, geographic region, initial vagueness (V₀), and investor quality indicators.

---

## 3.3 Identification Strategy

A key challenge is endogeneity. Capital allocation is not random—ventures with certain characteristics attract more funding. To isolate the effect of capital on flexibility, we employ within-V₀ analysis: we compare ventures with similar initial positioning but different funding levels.

**Procedure:**
1. Divide ventures into deciles by initial vagueness (V₀)
2. Within each V₀ decile, compute the correlation between E and |ΔV|
3. Average across deciles to obtain ρ(E, |ΔV|)_within_V

This approach controls for selection on initial positioning. Ventures that chose similar initial vagueness levels are compared; differences in funding within these groups identify the E → |ΔV| relationship.

---

## 3.4 Results: H1 (Flexibility → Growth)

We first test whether strategic flexibility predicts growth.

**Table 1: Flexibility and Growth**

| Specification | ρ(Y, |ΔV|) | p-value |
|:--------------|:----------:|:-------:|
| Unconditional | +0.159 | <0.001 |
| Controlling for E | +0.158 | <0.001 |
| By industry (range) | +0.14 to +0.18 | All <0.001 |

**Result:** H1 is supported. Ventures that demonstrated greater strategic flexibility achieved significantly higher growth (ρ = +0.159, p < 0.001). The relationship is robust to controlling for early-stage funding and holds across all industries.

---

## 3.5 Results: H2 (Capital → Rigidity)

We next test whether capital reduces flexibility.

**Table 2: Capital and Flexibility (Within-V₀)**

| V₀ Decile | ρ(E, |ΔV|) | p-value |
|:----------|:----------:|:-------:|
| D1 (Most precise) | -0.058 | <0.001 |
| D2 | -0.054 | <0.001 |
| D3 | -0.051 | <0.001 |
| D4 | -0.052 | <0.001 |
| D5 | -0.053 | <0.001 |
| D6 | -0.050 | <0.001 |
| D7 | -0.052 | <0.001 |
| D8 | -0.051 | <0.001 |
| D9 | -0.054 | <0.001 |
| D10 (Most vague) | -0.049 | <0.001 |
| **Average** | **-0.052** | **<0.001** |

**Result:** H2 is supported. Within each vagueness decile, more capital is associated with less subsequent flexibility (ρ = -0.052, p < 0.001). This effect is remarkably consistent across deciles, suggesting that the capital-rigidity relationship is not driven by selection into particular positioning strategies.

---

## 3.6 Results: H3 (Heterogeneous Effects)

We test whether capital's effect on growth varies by initial positioning.

**Table 3: Capital-Growth Relationship by Positioning**

| V₀ Level | ρ(Y, E) | Interpretation |
|:---------|:-------:|:---------------|
| Low V (Analyst channel) | -0.05 | Capital hurts |
| High V (Believer channel) | +0.08 | Capital helps |
| Difference | 0.13 | Significant (p < 0.001) |

**Result:** H3 is supported. For ventures with precise initial positioning (low V), capital is negatively associated with growth (ρ = -0.05). For ventures with vague initial positioning (high V), capital is positively associated with growth (ρ = +0.08). The difference is statistically significant.

**Interpretation:** Precise positioning creates stronger commitment pressure; capital amplifies the rigidity trap. Vague positioning preserves flexibility; capital enables resource deployment without lock-in.

---

## 3.7 The Flexibility Gap

We quantify the performance difference between flexible and rigid ventures.

**Table 4: Growth by Flexibility Quartile**

| |ΔV| Quartile | Median Y | Relative to Q1 |
|:-------------|:--------:|:--------------:|
| Q1 (Rigid) | 1.00 | 1.00× |
| Q2 | 1.57 | 1.57× |
| Q3 | 2.02 | 2.02× |
| Q4 (Flexible) | **2.71** | **2.71×** |

**Result:** The most flexible quartile (Q4) achieved 2.7× higher growth than the most rigid quartile (Q1). This "Flexibility Gap" represents the cost of commitment: ventures that maintained strategic flexibility dramatically outperformed those that remained locked in.

---

## 3.8 Robustness

**Alternative flexibility measures.** We replicate results using directional change (ΔV without absolute value), keyword-based measures, and market scope changes. Results are consistent.

**Alternative growth measures.** We replicate using total funding raised, survival to Series B+, and acquisition outcomes. The flexibility-growth relationship holds across specifications.

**Subsample analysis.** Results hold for US-only ventures and ventures with first financing above $500K.

**Mediation analysis.** Formal mediation tests (Baron and Kenny 1986) confirm that |ΔV| partially mediates the E → Y relationship. The direct effect of E on Y is attenuated when |ΔV| is included.

---

## 3.9 Summary

The empirical evidence supports all three hypotheses:

| Hypothesis | Prediction | Result | Evidence |
|:-----------|:-----------|:-------|:---------|
| H1 | |ΔV| → Y (+) | Supported | ρ = +0.159*** |
| H2 | E → |ΔV| (−) within V₀ | Supported | ρ = -0.052*** |
| H3 | E × V interaction | Supported | Low V: -0.05; High V: +0.08 |

The mechanism chain is confirmed: capital reduces flexibility (H2), flexibility drives growth (H1), and the combined effect varies by positioning (H3). The Flexibility Gap of 2.7× quantifies the cost of commitment.
