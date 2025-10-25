---
성장:
  - 2025-10-22T04:57:29-04:00
previous: "[[workflow(hypothesis, data, model)]]"
---

# jeff

## 1. control for team!
**Current H3 (β₇):** `Vagueness × SeriesB × High_Integration_Cost` — tests if reversal is stronger in hardware vs software.
**Jeff's alternative (not in your model):** `Vagueness × SeriesB × Founder_Credibility` — tests if reversal only works for credible founders.

These are **different mechanisms**:

- **Your H3**: Reversal depends on technical uncertainty (hardware = high discovery cost)
- **Jeff's idea**: Reversal depends on social capital (prior exits = trust to be vague)

Your file already has `Founder_Prior_Exit` as a **control**, not a **moderator**. Jeff suggests it should be tested as a moderator instead of (or in addition to) integration cost.

You could test both:

- Model 2A: `× High_Integration_Cost` (your current H3)
- Model 2B: `× Founder_Prior_Exit` (Jeff's suggestion)![[Jeff empirical guru guidance on hidden commitment cost_otter_ai (1).txt]]


**Core Guidance:**
- **Mechanism**: Vagueness = flexibility (no rigid expectations). Founders with **credibility signals** can be strategically vague, forcing investors to bet on the team, not the idea.
- **Data**: Use existing certitude score from org science paper. Pitchbook fine.
- **Model**: Simple logistic regression:
  - DV: `Funding_Success` (0/1)
  - IV: `Vagueness` (100 - certitude)
  - Interaction: `Vagueness × SeriesB`
  - Controls: founder experience, team size, industry FE
- **Tables**: Show progression (vagueness-only → + controls) to prove robustness

**Implemented:**
- ✅ Logistic framework
- ✅ Panel structure (A → B)
- ✅ Interaction term
- ✅ Pitchbook data

**Not Yet Addressed:**
- ⚠️ Certitude measure (need to verify org science paper = LIWC)
- ❌ Credibility as mechanism (Jeff emphasizes this; we test integration cost instead)
- ❌ Table progression (only final models, not intermediate)
- ❌ Endogeneity ("why choose vagueness?" - selection bias unaddressed)

**Key Quote:**
> "Strategic mechanism in being vague...force investors to invest in the team, not the idea. Lowers likelihood of getting funded, but conditional on funding, increases likelihood of delivery."

**Actions:**
1. Check org science vagueness measure vs our LIWC
2. Add: `Vagueness × SeriesB × Founder_Track_Record`
3. Build: Model 1 (vagueness) → Model 2 (+ controls) → Model 3 (+ interaction)

---

## #scott (Hart Posen - Paper Structure Advisor)

**Implemented:**
- ✅ Formatting (no subsections in intro)
- ✅ Simplified game (2-player: entrepreneur + customer)
- ✅ One idea focus (strategic ambiguity)
- ✅ Mean/variance separation

**Not Yet Addressed:**
- ⚠️ "Explain to your mom" simplicity (still technical)
- ⚠️ Remove exogenous probability critique (deleted Section 1.2 but philosophy persists)
- ❌ Actual intro (hypothesis.md ≠ paper intro)

**Quote:**
> "A paper is an argument for ONE thing, not 10."

**Action:** Lead intro with "vague promises paradox", not Bayesian machinery.

---

## #unknown_speaker (from document 8 - YC/CDL pitch deck mining suggestion)

**Core Guidance:**
- Sample 20-30 firms from one domain (clean energy, AI drug discovery)
- Mine pitch decks, code vagueness via LLM
- Track Series A → B with CrunchBase
- Model: Strip to 1/3 symbols, derive optimum, explain deviations (agency/bounded rationality)

**Status:** Partially implemented (Pitchbook replaces YC/CDL, but same logic)

---

## Combined Gaps

**Critical:**
1. Jeff + Unknown both want **credibility** tested, not just integration cost
2. Model too complex (9 variables) - contradicts "proof of concept" guidance
3. No table progression (vagueness → + controls → + interaction)

**MVP Priority:**
1. Verify vagueness measure consistency
2. Test credibility alongside integration cost
3. Simplify variable count (drop less critical controls)
