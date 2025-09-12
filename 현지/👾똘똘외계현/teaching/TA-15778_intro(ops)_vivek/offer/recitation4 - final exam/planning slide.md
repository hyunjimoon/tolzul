
## Today's Coverage

**Four Core Topics for Final Exam:**
1. Build-up Diagrams
2. Queueing Theory  
3. **EOQ & (R,Q) Policy** ← Today's focus
4. **Newsvendor Model** ← Today's focus

*Note: Adam will cover Build-up and Queueing on Friday*

**Why these two together?** Both address inventory decisions under different conditions:
- Newsvendor: Single-period decision with uncertain demand
- (R,Q): Multi-period decision combining certain and uncertain elements

----

## 1. Newsvendor Logic: The Foundation
### When Uncertainty Meets Inventory

**The Core Formula:**
$$q^* = \mu + k_\alpha \cdot \sigma$$

Where:
- $q^*$ = optimal order quantity
- $\mu$ = mean demand
- $\sigma$ = standard deviation of demand
- $k_\alpha$ = service level multiplier

**Key Insight:** We're adding a "safety cushion" (k·σ) to average demand

[DIAGRAM PLACEHOLDER: Visual showing normal distribution with μ and safety stock marked]

----

## 1.1 Finding Your Parameters
### From Data to Decision

**Two Paths to Parameters:**

**Path 1: Normal Distribution**
- Given: Mean (μ) and Standard Deviation (σ)
- Assumption: Demand ~ N(μ, σ²)

**Path 2: Empirical Distribution**
- Historical data: Actual demand observations
- No distribution assumption needed
- Find percentiles directly from data

**Example:** SportyBoston T-shirts
- Path 1: μ = 500, σ = 200 → Use normal tables
- Path 2: Historical sales data → Count up to desired percentile

----

## 1.2 The Critical Ratio
### Translating Costs to Service Level

**The Magic Formula:**
$$\alpha^* = \frac{u}{u + o} = \frac{r-c}{(r-c) + (c-s)}$$

Where:
- u = underage cost (lost profit from stockout)
- o = overage cost (loss from excess inventory)
- r = revenue per unit
- c = cost per unit
- s = salvage value per unit

[DIAGRAM PLACEHOLDER: Triangle diagram showing r, c, s relationships]

**Key Values to Remember:**
- k₈₀% = 0.84
- k₉₀% = 1.28
- k₉₅% = 1.64
- k₉₉% = 2.33

----

## 1.3 The Power of Pooling
### When 1 + 1 < 2

**Individual Locations:**
- Location 1: N(μ₁, σ₁²)
- Location 2: N(μ₂, σ₂²)

**Pooled System:**
- Combined: N(μ₁ + μ₂, σ₁² + σ₂²)
- Key insight: σ_pooled = √(σ₁² + σ₂²) < σ₁ + σ₂

**Coefficient of Variation Impact:**
- Individual CV: σ/μ
- Pooled CV: (1/√n) × Individual CV

[DIAGRAM PLACEHOLDER: Before/after pooling visualization with warehouses]

----

## 2. The (R,Q) Policy
### Continuous Review for Continuous Business

**Two Decisions:**
1. **Q: How much to order?** (Economic Order Quantity logic)
2. **R: When to reorder?** (Newsvendor logic)

**The System:**
- Monitor inventory continuously
- When inventory drops to R → Order Q units
- Balances multiple cost trade-offs

----

## 2.1 Finding Q: The Balancing Act
### Marginal Analysis of Ordering vs. Holding

**The Trade-off:**
- Order more → Higher holding costs
- Order less → Higher ordering costs

**Marginal Cost Analysis:**

When we increase Q by one unit:
- Marginal increase in holding cost = CH/2
- Marginal decrease in ordering cost = FD/Q²

**At optimum:** Marginal costs equal
$$\frac{CH}{2} = \frac{FD}{Q^2}$$

Solving: $$Q^* = \sqrt{\frac{2FD}{CH}}$$

[DIAGRAM PLACEHOLDER: Cost curves showing intersection point]

----

## 2.1 Deriving Q: Step by Step

**Total Cost Function:**
$$V(Q) = \frac{FD}{Q} + \frac{CHQ}{2}$$

**Taking derivative:**
$$\frac{dV}{dQ} = -\frac{FD}{Q^2} + \frac{CH}{2}$$

**Setting to zero:**
$$-\frac{FD}{Q^2} + \frac{CH}{2} = 0$$

**Rearranging:**
$$\frac{FD}{Q^2} = \frac{CH}{2}$$

**Final formula:**
$$Q^* = \sqrt{\frac{2FD}{CH}}$$

----

## 2.2 Finding R: When to Pull the Trigger
### Newsvendor Logic Meets Lead Time

**The Reorder Point Formula:**
$$R = E[DDLT] + k_\alpha \cdot \sigma_{DDLT}$$

Where:
- DDLT = Demand During Lead Time
- E[DDLT] = μ × L (if L is lead time in periods)
- σ_{DDLT} = σ × √L (for independent demand)

**Example:** 
- Daily demand: μ = 10, σ = 3
- Lead time: 3 days
- Service level: 95%
- R = 10×3 + 1.64×3×√3 = 30 + 8.5 = 38.5

----

## Newsvendor vs. (R,Q): A Comparison

**Newsvendor - Balancing Under/Over:**
- As q increases by 1:
  - Expected underage cost decreases by: P(D>q)×(r-c)
  - Expected overage cost increases by: P(D≤q)×(c-s)
- At optimum: These marginal changes equal

**(R,Q) - Balancing Order/Hold:**
- As Q increases by 1:
  - Ordering cost per unit decreases by: FD/Q²
  - Holding cost per unit increases by: CH/2
- At optimum: These marginal changes equal

----

## Key Takeaways for the Exam

1. **Newsvendor = Single Period Uncertainty**
   - Start with service level (α)
   - Add safety stock to mean demand

2. **(R,Q) = Continuous Multi-Period**
   - Q from EOQ (deterministic costs)
   - R from Newsvendor (uncertain demand)

3. **Pooling Always Helps**
   - Reduces relative variability
   - CV reduces by factor of 1/√n

4. **Watch Your Units!**
   - Time periods must match
   - Costs must be consistent

[DIAGRAM PLACEHOLDER: Summary flowchart connecting all concepts]
