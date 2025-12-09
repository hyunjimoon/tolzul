# Vague Promise and Venture Growth
## Section 2: Theory

**Source of Truth:** [[📢BULLETIN]]

---

## 2.1 Signaling Theory and the Precision Prescription

Signaling theory originated with Spence's (1973) analysis of job market signaling, where education serves as a credible signal of worker productivity. The theory has since been applied extensively to entrepreneurial contexts (Connelly et al. 2011). The core insight is that when quality is unobservable, high-quality actors can distinguish themselves by sending signals that are (a) costly to produce and (b) differentially costly such that low-quality actors cannot profitably mimic them.

In entrepreneurship, this logic suggests that precise, verifiable promises function as effective signals. When a founder claims specific technical capabilities, measurable market traction, or concrete milestones, investors can verify these claims through due diligence. The verification process creates separation: founders who cannot deliver on precise promises face reputational costs, while those who can deliver benefit from reduced information asymmetry.

Recent work has operationalized this insight through the "scientific approach" to entrepreneurship. Camuffo et al. (2020) show that founders trained to formulate falsifiable hypotheses and test them systematically achieve better outcomes. The implication is that precision—in both thinking and communication—improves entrepreneurial performance.

We formalize the conventional wisdom as:

> **H₀ (Signaling Null):** Promise vagueness monotonically reduces venture growth.

Under H₀, we would expect survival rates to decline monotonically as vagueness increases: Q1 > Q2 > Q3 > Q4.

---

## 2.2 Strategic Ambiguity as Alternative

A contrasting perspective emerges from organizational communication research. Eisenberg (1984) argues that ambiguity is not merely failed clarity but can serve strategic functions:

1. **Promoting unified diversity.** Ambiguous goals allow diverse stakeholders to coalesce around shared language while maintaining different interpretations.
2. **Preserving future options.** Vague commitments avoid premature lock-in to specific courses of action.
3. **Enabling deniability.** Abstract promises provide flexibility in subsequent interpretation.

Sillince et al. (2012) extend this logic to show how organizations deploy ambiguity strategically to manage competing stakeholder demands. For entrepreneurs, vagueness can preserve flexibility during periods of high uncertainty, support identity formation in emerging markets, and avoid premature commitment to niches that may prove unviable.

This perspective suggests that the relationship between vagueness and outcomes may not be uniformly negative. Rather than universally degrading signal quality, strategic ambiguity may function as an instrument for maintaining degrees of freedom.

---

## 2.3 Heterogeneous Audiences and Evaluation Modes

We reconcile these perspectives by proposing that investor audiences differ systematically in their evaluation modes. This heterogeneity creates conditions under which both precision and vagueness can be optimal, depending on the target audience.

**Analyst Investors.** Some investors evaluate ventures through systematic due diligence. They analyze market size, assess technical feasibility, benchmark against comparables, and project financial returns. This evaluation mode requires verifiable inputs. Vague promises frustrate the process: without concrete claims, Analysts cannot distinguish genuine potential from wishful thinking. For Analyst investors, precision reduces uncertainty and enables informed decision-making.

**Believer Investors.** Other investors evaluate ventures through mission alignment and transformative potential. They seek founders with compelling visions, assess market-making opportunities, and project scenarios of dramatic success. This evaluation mode benefits from vagueness. Eisenberg (1984, p. 239) notes that "the more ambiguous the message, the greater the room for projection," where projection allows receivers to "fill in the meaning... in a way which is consistent with their own beliefs." For Believer investors, vagueness provides latitude to imagine favorable outcomes.

The distinction parallels Guzman and Stern's (2020) observation that observable founding choices predict growth outcomes. We extend their logic: not just the content of signals but their precision affects how investors process and respond to them.

---

## 2.4 The Mechanism: Audience Sorting

Promise precision functions as a sorting device. Founders who communicate with high precision attract Analyst investors who reward verifiability. Founders who communicate with high vagueness attract Believer investors who reward vision. In equilibrium, both strategies can succeed when matched appropriately.

The middle ground fails because it satisfies neither audience. Moderately vague promises are:
- Too vague for Analysts to verify → they discount or reject
- Too specific for Believers to project → they lose interest

This "murky middle" attracts weaker versions of both investor types rather than committed supporters from either channel.

We can represent the mechanism formally. Let the probability of attracting committed investment be:

$$P(\text{committed}) = \max[A(V), B(V)]$$

where A(V) is the Analyst channel activation (decreasing in V) and B(V) is the Believer channel activation (increasing in V). If A and B are both continuous and single-peaked at their respective optima, the overall probability function is U-shaped in V.

---

## 2.5 Hypotheses

From this framework, we derive:

> **H₁ (U-Shape):** Both low-vagueness and high-vagueness ventures outperform intermediate-vagueness ventures.

Under H₁, we expect: Q1 > Q2, Q4 > Q3, and (Q1 + Q4)/2 > (Q2 + Q3)/2.

The Analyst/Believer distinction serves as an interpretive mechanism rather than a directly tested moderator. We do not observe investor types in our data. Instead, we document the aggregate pattern and interpret it through the lens of audience segmentation.

---

## 2.6 Empirical Approach: Non-Parametric Specification

The U-shaped hypothesis requires an empirical approach that does not impose functional form assumptions. Standard polynomial regression would impose symmetry (the quadratic term forces equal curvature on both sides), but the pattern we hypothesize may be asymmetric.

We therefore employ non-parametric quartile analysis:

1. Rank ventures by vagueness within each industry
2. Divide into quartiles (Q1 = lowest vagueness, Q4 = highest)
3. Compute survival rates within each quartile
4. Test heterogeneity using χ² contingency tests (df = 3)
5. Measure U-shape strength as Δ = [(Q1 + Q4)/2] − [(Q2 + Q3)/2]

This approach makes minimal assumptions about the underlying relationship while providing clear, interpretable tests of the competing hypotheses.

---

## 2.7 Summary

Signaling theory predicts that precision improves outcomes (H₀: monotonic decline in survival as vagueness increases). Strategic ambiguity research suggests that vagueness can also be valuable. We propose audience segmentation as the mechanism that reconciles these views: precision attracts Analyst investors, vagueness attracts Believer investors, and the middle ground attracts neither effectively. This yields a U-shaped prediction (H₁) that we test using non-parametric methods.
