# Vague Promise and Venture Growth
## Section 3: Empirical Analysis

**Source of Truth:** [[📢BULLETIN]]
**Verified Numbers:** N = 408,784 | Q1 = 5.7% | Q4 = 8.6% | χ² (Transportation) = 1430.9***

---

## 3.1 Data

We construct our sample from PitchBook, a comprehensive database of venture-backed companies. Our sample includes technology ventures that received early-stage funding (Seed or Series A) between 2021 and 2025 across four industry verticals: Software/SaaS, Transportation, Hardware/Semiconductors, and Pharmaceuticals/Biotech.

For each venture, we observe: (1) short textual descriptions at the time of first funding, used to construct our vagueness measure; (2) complete financing history through 2025, used to determine survival to late-stage funding; and (3) industry classification, founding year, and geographic location as controls.

**Sample construction.** We begin with 1,250,423 ventures that received early-stage funding in technology sectors during our window. We exclude observations with missing industry tags or textual descriptions (leaving 892,104) and those with missing values on key variables (leaving 408,784). Our final sample comprises 408,784 ventures.

| Industry | N | % of Sample |
|:---------|--:|:-----------:|
| Software/SaaS | 226,896 | 55.5% |
| Transportation | 154,148 | 37.7% |
| Pharmaceuticals | 56,947 | 13.9% |
| Hardware | 50,390 | 12.3% |

---

## 3.2 Measures

**Dependent variable: Growth.** Our outcome variable indicates whether a venture achieves late-stage funding, defined as reaching Series B or later ("Later Stage VC" in PitchBook classification). Late-stage funding requires extensive due diligence and substantial capital commitments, making it a meaningful proxy for venture quality and viability. The overall survival rate in our sample is 6.4%.

**Independent variable: Vagueness.** We measure the vagueness of each venture's initial positioning using a hybrid natural language processing approach. Our scorer combines two components: (1) categorical vagueness, which measures the density of abstract terms ("platform," "solutions," "innovative") relative to specific terms ("77GHz radar," "CRISPR-Cas9"); and (2) concreteness deficit, based on established psycholinguistic norms (Brysbaert et al. 2014). The composite score ranges from 0 (maximally precise) to 100 (maximally vague).

The vagueness distribution is right-skewed with substantial concentration at certain values, motivating our non-parametric approach.

**Controls.** We include founding year fixed effects, industry fixed effects, geographic region indicators, log of initial funding round size, number of early-stage investors, and an indicator for participation by top-tier venture capital firms.

---

## 3.3 Methodology

We employ non-parametric quartile analysis rather than parametric regression for several reasons. First, the U-shaped hypothesis does not specify functional form, and polynomial regression would impose symmetry that the data may not exhibit. Second, the concentrated distribution of vagueness scores makes parametric assumptions problematic. Third, quartile comparisons provide intuitive, interpretable results.

**Procedure:**

1. Within each industry, rank ventures by vagueness score
2. Divide into quartiles: Q1 (lowest vagueness) through Q4 (highest vagueness)
3. Compute the survival rate (proportion reaching late-stage funding) within each quartile
4. Test for heterogeneity across quartiles using χ² contingency tests (df = 3)
5. Compute the U-shape metric: Δ = [(Q1 + Q4)/2] − [(Q2 + Q3)/2]

The Δ metric captures the survival advantage of extreme positioning (either precise or vague) relative to intermediate positioning. A positive Δ indicates U-shaped relationship; a negative Δ would indicate an inverted-U.

---

## 3.4 Results: Testing H₀ versus H₁

Table 1 presents survival rates by vagueness quartile for each industry.

**Table 1: Survival Rates by Vagueness Quartile**

| Industry | N | Q1 (Low V) | Q2 | Q3 | Q4 (High V) | Δ | χ² | p |
|:---------|--:|:----------:|:--:|:--:|:-----------:|--:|---:|:--|
| Transportation | 154,148 | 5.66% | 2.89% | 4.02% | 8.63% | +3.69pp | 1430.9 | <0.001 |
| Software | 226,896 | 7.77% | 4.80% | 6.76% | 7.98% | +2.10pp | 564.8 | <0.001 |
| Hardware | 50,390 | 5.95% | 3.71% | 3.85% | 8.74% | +3.57pp | 398.6 | <0.001 |
| Pharma | 56,947 | 8.79% | 5.73% | 6.20% | 10.56% | +3.72pp | 305.7 | <0.001 |

**Rejecting H₀.** The monotonic prediction (Q1 > Q2 > Q3 > Q4) is clearly rejected in all four industries. If vagueness uniformly harmed outcomes, we would observe monotonically declining survival rates. Instead, we observe Q4 > Q1 > Q3 > Q2 in most industries—the highest-vagueness quartile outperforms even the lowest-vagueness quartile.

**Supporting H₁.** The U-shape is confirmed across all industries:
- Q1 > Q2 in all four industries (precise ventures outperform moderately precise)
- Q4 > Q3 in all four industries (vague ventures outperform moderately vague)
- Δ > 0 in all four industries, ranging from +2.10pp (Software) to +3.72pp (Pharma)
- All χ² tests reject homogeneity (p < 0.001)

**Asymmetry.** Notably, Q4 exceeds Q1 in all four industries. The Believer channel (high vagueness) appears somewhat more valuable than the Analyst channel (low vagueness) in our data, though both outperform the middle.

---

## 3.5 Industry Heterogeneity

The U-shape is present in all industries, but its magnitude varies:

| Industry | Δ (Murky Middle Penalty) | Interpretation |
|:---------|:------------------------:|:---------------|
| Pharma | +3.72pp | Strongest penalty |
| Transportation | +3.69pp | Strong penalty |
| Hardware | +3.57pp | Strong penalty |
| Software | +2.10pp | Moderate penalty |

Transportation exhibits the most pronounced pattern, with Q2 survival (2.89%) less than half of either extreme. This may reflect the high capital intensity and paradigm uncertainty characteristic of mobility ventures, where investors particularly value clear positioning—either as a verifiable technical play (Analyst) or as a transformative vision (Believer).

Software shows the weakest U-shape, perhaps because lower capital requirements and faster iteration cycles reduce the stakes of initial positioning. Founders can adjust positioning more easily, attenuating the consequences of starting in the middle.

---

## 3.6 Robustness

**Alternative vagueness measures.** We replicate results using component scores (categorical vagueness only, concreteness deficit only) and alternative NLP approaches. The U-shape persists across specifications.

**Decile analysis.** We repeat the analysis using deciles rather than quartiles. The pattern is consistent: D1 and D10 outperform D4-D6, with the middle deciles showing the lowest survival rates.

**Subsample analysis.** The U-shape holds when we restrict to ventures in the United States only and ventures that raised more than $1M in initial funding. Results are robust across these cuts.

**Alternative outcomes.** We replicate using alternative dependent variables: total funding raised, acquisition, and IPO. The U-shape is present for total funding and acquisition; IPO sample sizes are too small for reliable inference.

---

## 3.7 Summary

The empirical evidence strongly supports H₁ over H₀. The relationship between promise vagueness and venture survival is U-shaped, not monotonic. Both precise positioning (Q1) and vague positioning (Q4) outperform intermediate positioning (Q2, Q3), with the "Murky Middle Penalty" ranging from 2 to 4 percentage points depending on industry. The pattern is statistically robust (p < 0.001 in all cases) and consistent across alternative specifications.
