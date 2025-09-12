# three grading 🫀goals
1. clear grading to minimize re-grade request from students receiving the feedback
2. persuade those who had points off by explaining what they've missed and could prevent similar point loss during the final exam
3. rewarding those who thought deeply e.g. Quantitative censoring adjustment using sellthrough and Empirical vs normal distribution analysis 
# Yedioth Case Grading Rubric

**Instructions for Grading:** Grade each team's PDF submission using this rubric. Award points in 5-point increments only. Target class mean: 60-65/80.

## Q1: Individual Retailer Quantities (15 points)

**15/15 - Full Credit:**

- Uses newsvendor formula OR histogram method correctly
- Achieves total inventory ~457 (histogram) or ~489 (normal)
- **Acknowledges that historical sales underestimate true demand due to stockouts**

**10/15 - Partial Credit:**

- Correct calculations but treats sales = demand
- _Deduction rationale: "Lost 5 points because analysis assumes sales data perfectly reflects demand, ignoring lost sales from stockouts"_

**5/15 - Major Issues:**

- Calculation errors OR missing appendix with 50 retailers
- _Deduction rationale: State specific error_

## Q2: Full Pooling Benefits (15 points)

**15/15 - Full Credit:**

- Calculates ~319 (histogram) or ~333 (normal) units
- Shows variance pooling: σ_total = √Σσ_i²
- Explains risk pooling reduces safety stock needs

**10/15 - Partial Credit:**

- Correct answer but weak/missing risk pooling explanation
- _Deduction rationale: "Lost 5 points - need to explain WHY pooling reduces inventory"_

**5/15 - Major Issues:**

- Wrong pooling calculations
- _Deduction rationale: Show correct formula_

## Q3: Agent-Level Pooling (15 points)

**15/15 - Full Credit:**

- Calculates all 10 agents (~387-401 total)
- Compares to both no pooling AND full pooling
- Explains why partial pooling < full pooling benefits

**10/15 - Partial Credit:**

- Calculations done but missing comparative analysis
- _Deduction rationale: "Lost 5 points - must compare agent pooling to both extremes"_

**5/15 - Major Issues:**

- Incomplete agent calculations

## Q4: Realistic Mid-Week Policies (15 points)

**15/15 - Full Credit:**

- Proposes specific mechanism (e.g., two-stage delivery, rebalancing)
- Quantifies benefit (% reduction or units saved)
- Addresses case constraint: no mid-week production

**10/15 - Partial Credit:**

- Good idea but vague on benefits or implementation
- _Deduction rationale: "Lost 5 points - need specific benefit quantification"_

**5/15 - Major Issues:**

- Impractical proposal or ignores case constraints

## Q5: Organizational Challenges (10 points)

**10/10 - Full Credit:**

- Identifies multiple stakeholders (retailers, agents, management)
- Provides specific barriers (e.g., agent incentives, IT systems)

**5/10 - Partial Credit:**

- Generic discussion without specifics
- _Deduction rationale: "Lost 5 points - need specific stakeholder concerns"_

## Bonus Points (10 points) - Award if demonstrated AT LEAST ONCE in Q1-Q5:

**+5 Censoring/Sellthrough Analysis:** Award if student quantitatively adjusts for censored demand using sellthrough rates or discusses μ_latent > μ_observed

**+5 Distribution Choice Analysis:** Award if student thoughtfully compares empirical vs normal approaches, discussing when each is appropriate (e.g., fat tails for individuals, normal approximation improves with pooling)

## Final Feedback Template:

Q1: __/15 [If <15, explain using deduction rationale] Q2: __/15 [If <15, explain using deduction rationale] Q3: __/15 [If <15, explain using deduction rationale] Q4: __/15 [If <15, explain using deduction rationale] Q5: __/10 [If <10, explain using deduction rationale] Bonus: __/10 [Specify which bonus earned and where demonstrated]

**Total: __/80**

**Example Feedback:** "Q2: 10/15. Lost 5 points - while calculations are correct, you need to explain WHY risk pooling reduces total inventory. The key insight is that individual demand variations partially cancel out when pooled."