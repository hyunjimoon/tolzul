# The Promise Vendor: Finding the Optimal Level of Entrepreneurial Promises

## Abstract

How should entrepreneurs calibrate their promises to maximize success? This paper develops a "promise vendor" model that prescribes optimal promise levels by adapting the newsvendor framework to entrepreneurial contexts. Unlike inventory decisions facing exogenous demand, entrepreneurial promises endogenously create the deliverability they must satisfy through the funding mechanism. We formalize two key costs: the failure cost of bold promises (funded but undelivered) and the opportunity cost of timid promises (deliverable but unfunded). The model shows how promise level φ affects deliverability through P(D|φ) = ∫ P(D|F,φ) × P(F|φ) dF, violating Modigliani-Miller by making operations inseparable from finance. Using Tesla's choice between promising 150-mile (timid) versus 300-mile (bold) range in 2008, we derive conditions for optimal promises: bold when opportunity costs exceed failure costs (Cu > Co), timid when reversed (Co > Cu), and moderate when balanced (Cu ≈ Co). The promise vendor framework provides entrepreneurs quantitative guidance for this fundamental strategic choice.

**Keywords:** entrepreneurship, newsvendor model, promise optimization, venture funding, strategic decision-making

# 1. Introduction

## 1.1 The Puzzle of Finding Optimal Promise Levels

Entrepreneurs face a fundamental calibration challenge. Elon Musk promised 300-mile range electric vehicles when battery costs exceeded $1000/kWh. Steve Jobs promised "1000 songs in your pocket" when flash memory cost $8/MB. Jeff Bezos promised one-day delivery when logistics networks couldn't support it. Each succeeded spectacularly. Yet Elizabeth Holmes promised instant blood diagnostics that sent her to prison. Billy McFarland promised luxury festival experiences that ended in fraud charges. Sam Bankman-Fried promised revolutionary trading that collapsed in scandal.

This pattern reveals a critical puzzle: **How do we find the optimal level of entrepreneurial promises?** As my advisor noted, "We can find examples of very bold promises that have proven to be successful, and some examples of bold promises that ended up in jail. This suggests that an infinitely bold promise is not appropriate for every entrepreneur."

The answer matters. Promise too boldly and risk Theranos-style failure after burning investor capital. Promise too timidly and risk never getting funded despite viable technology. Somewhere between these extremes lies an optimal promise level that maximizes the probability of entrepreneurial success.

This paper provides a quantitative framework for finding that optimum. By adapting the newsvendor model to entrepreneurial contexts, we show how to balance the failure cost of overly bold promises against the opportunity cost of overly timid ones. The resulting "promise vendor" model prescribes optimal promise levels based on specific cost structures, offering entrepreneurs a decision tool for this critical strategic choice.

## 1.2 From Newsvendor to Promise Vendor

The newsvendor model provides our analytical foundation. A newspaper vendor must decide how many papers to stock before knowing demand. Order too many and unsold papers become waste (overage cost). Order too few and miss profitable sales (underage cost). The optimal order quantity balances these opposing costs.

Entrepreneurs face an analogous but distinct problem. Before knowing their true delivery capability, they must promise a performance level to attract funding. Promise too boldly and risk failing after securing investment (failure cost). Promise too timidly and risk not getting funded despite having viable technology (opportunity cost).

The key difference: **promises create the uncertainty they must satisfy**. While newspaper inventory doesn't affect customer demand, entrepreneurial promises directly influence both funding probability and delivery difficulty. This endogeneity transforms the optimization problem and violates traditional finance assumptions about the separation of financing and operations.

## 1.3 The Promise Vendor Framework

We model the entrepreneur's choice of promise level φ ∈ [0,1], where 0 represents a timid promise and 1 represents a bold promise. For Tesla in 2008:
- φ = 0: Promise 150-mile range (easily achievable with existing battery technology)
- φ = 1: Promise 300-mile range (requires breakthrough in battery cost and density)

The promise level generates two stochastic outcomes:
1. **Funding outcome F ∈ {0,1}**: Whether the venture secures investment
2. **Delivery outcome D ∈ {0,1}**: Whether the venture successfully delivers on its promise

These create four possible states with associated payoffs:
- (F=1, D=1): Funded and delivered → Payoff = V (success value)
- (F=1, D=0): Funded but failed → Payoff = -L (liability/reputation loss)  
- (F=0, D=1): Unfunded but viable → Payoff = 0 (missed opportunity)
- (F=0, D=0): Unfunded and unviable → Payoff = 0 (no loss)

This payoff structure defines our two key costs:
- **Cost of too bold promise (Co)**: V - (-L) = V + L (failure cost)
- **Cost of too timid promise (Cu)**: V - 0 = V (opportunity cost)

# 2. Model Development

## 2.1 Building Intuition: From Newsvendor Basics

We begin with the canonical newsvendor problem to establish baseline intuition. A vendor faces uncertain demand D and chooses order quantity Q to minimize expected mismatch costs:

**Step 1: Define the costs**
- Overage cost co: Loss per unit of unsold inventory
- Underage cost cu: Lost profit per unit of unmet demand

**Step 2: Set up the trade-off**
The vendor increases Q until marginal expected revenue equals marginal cost:
- Marginal revenue = cu × P(D > Q)
- Marginal cost = co × P(D ≤ Q)

**Step 3: Find the optimal quantity**
At optimum: cu × P(D > Q*) = co × P(D ≤ Q*)

Rearranging: P(D ≤ Q*) = cu/(cu + co)

This critical fractile formula shows that optimal inventory increases with underage cost and decreases with overage cost.

## 2.2 The Promise Vendor Model

Now we transform this framework for entrepreneurial promises using a hierarchical formulation (see Figure 1).

**[Figure 1 about here: Promise Vendor Model - Final Formulation]**

### Hierarchical Structure

**Hyperparameter Level**: φ ~ Beta(α, β)
- φ ∈ [0,1] represents promise boldness (0=timid, 1=bold)
- For Tesla: φ=0.3 means promising 150-mile range, φ=0.7 means 250-mile range

**Observable Level**: Y|φ ~ Categorical(π₀(φ), π₁(φ), π₂(φ))

Where Y represents the venture outcome:
- Y=0: Funded failure (F=1, D=0) - secured funding but couldn't deliver
- Y=1: Missed opportunity (F=0, D=1) - could deliver but didn't get funded
- Y=2: Funded success (F=1, D=1) - got funded and delivered

### Conditional Independence Property of Deliverability     

The key structural assumption is conditional independence:

**P(D|F,φ) = P(D|φ) = 1 - φ**

This equation means delivery capability is inherent to the promise level, not dependent on funding. Ambitious promises are inherently harder to deliver regardless of resources.

### Probability Structure

Given conditional independence:
- π₀(φ) = P(F=1|φ) × P(D=0|φ) = φ × φ = φ²
- π₁(φ) = P(F=0|φ) × P(D=1|φ) = (1-φ) × (1-φ) = (1-φ)²
- π₂(φ) = P(F=1|φ) × P(D=1|φ) = φ × (1-φ)

Figure 2 shows how these probabilities vary with promise level.

**[Figure 2 about here: Promise Vendor - Probability Trade-offs]**

### Cost Structure and Optimization

Define payoffs V₀, V₁, V₂ for outcomes Y=0, Y=1, Y=2:
- Overage cost: Co = V₂ - V₀ (failure cost)
- Underage cost: Cu = V₂ - V₁ (opportunity cost)

Expected cost: EC(φ) = Co × φ² + Cu × (1-φ)²

Taking the derivative and solving:
**φ* = Cu/(Cu + Co)**

Remarkably, this recovers the newsvendor critical fractile formula!

## 2.3 Three Illustrative Cases

### Case 1: Balanced Costs (Co = Cu)
**Example**: Early-stage biotech with high success value
- Co = $400M (large liability if drug fails after funding)
- Cu = $400M (large market opportunity if viable)
- φ* = 400/(400+400) = 0.5 (moderate promise)

**Prescription**: Promise in the middle range - ambitious enough to attract funding but achievable enough to deliver.

### Case 2: High Opportunity Cost (Co << Cu)  
**Example**: Software platform with network effects
- Co = $100M (limited liability, "fail fast" culture)
- Cu = $900M (winner-take-all market)
- φ* = 900/(900+100) = 0.9 (bold promise)

**Prescription**: Promise aggressively - the opportunity cost of missing the market window far exceeds failure costs.

### Case 3: High Failure Cost (Co >> Cu)
**Example**: Medical device in regulated market
- Co = $900M (regulatory penalties, lawsuits)
- Cu = $100M (moderate market, many competitors)
- φ* = 100/(100+900) = 0.1 (timid promise)

**Prescription**: Promise conservatively - the failure costs from overpromising exceed the opportunity costs of modest targets.

## 2.4 Violation of Modigliani-Miller

The condition P(D|F,φ) ≠ P(D|φ) reveals a fundamental violation of Modigliani-Miller's capital structure irrelevance theorem. In our model, funding affects operational outcomes - ventures with funding have different delivery probabilities than those without, even conditional on promise level.

This interdependence reflects entrepreneurial reality:
- Funded ventures access resources, expertise, and networks that improve delivery odds
- The promise level that attracts funding also determines the technical challenge
- Operations and finance become inseparable through the promise mechanism

For Tesla, securing funding didn't just provide capital - it enabled battery partnerships, manufacturing expertise, and market credibility that made 300-mile range achievable. The promise vendor model captures this operations-finance nexus that Modigliani-Miller assumes away.

# 3. Practical Application: Tesla's Promise Decision

## 3.1 Setting Up Tesla's Choice (2008)

Tesla faced a critical promise decision for the Roadster:
- **Timid promise (φ=0.3)**: 150-mile range using proven battery technology
- **Bold promise (φ=0.8)**: 300-mile range requiring battery cost breakthroughs

**Cost parameters**:
- Success value V = $300M (market opportunity for luxury electric sports car)
- Liability L = $100M (reputation damage, lawsuits if funded venture fails)
- Co = V + L = $400M (failure cost)
- Cu = V = $300M (opportunity cost)

**Optimal promise**: φ* = 300/(300+400) = 0.43

This suggests a moderate promise around 220-mile range would optimize Tesla's expected outcome.

## 3.2 Why Tesla Promised Boldly

Tesla actually promised 244-mile range (later achieving 245 miles), slightly above our model's prescription. Several factors may explain this:

1. **Elon Musk's track record** reduced effective failure costs through reputation insurance
2. **Electric vehicle market dynamics** increased opportunity costs of conservative promises
3. **Technical confidence** from early prototypes shifted delivery probability estimates

The framework still provided valuable guidance - Tesla avoided both extremes of 150-mile (too timid) and 300-mile (too bold) promises.

# 4. Managerial Implications

## 4.1 A Decision Tool for Entrepreneurs

The promise vendor model provides a quantitative framework for promise calibration:

**Step 1**: Estimate your parameters
- What's your venture's success value (V)?
- What's your liability if you fail after funding (L)?
- Calculate Co = V + L and Cu = V

**Step 2**: Apply the formula
- Optimal promise level: φ* = Cu/(Cu + Co) = V/(V + V + L) = V/(2V + L)

**Step 3**: Interpret the prescription
- φ* > 0.7: Make bold promises (high opportunity cost environment)
- 0.3 < φ* < 0.7: Make moderate promises (balanced cost environment)
- φ* < 0.3: Make conservative promises (high failure cost environment)

## 4.2 Sector-Specific Guidance

**Software/Platform Ventures**: Generally face Cu > Co due to network effects and winner-take-all dynamics. Prescription: Promise boldly to capture market position.

**Healthcare/Regulated Ventures**: Generally face Co > Cu due to regulatory penalties and patient safety. Prescription: Promise conservatively to avoid catastrophic failures.

**Hardware/Manufacturing Ventures**: Often face Cu ≈ Co with balanced opportunities and liabilities. Prescription: Promise moderately, calibrating to specific market conditions.

# 5. Conclusion

The promise vendor framework transforms entrepreneurial promise decisions from gut feelings to quantitative optimization. By adapting the newsvendor model's cost-balancing logic to entrepreneurial contexts, we provide a practical tool for finding optimal promise levels.

The key insight: promises create the uncertainty they must satisfy. This endogeneity makes entrepreneurial decisions fundamentally different from inventory optimization, violating Modigliani-Miller and creating an operations-finance nexus unique to new ventures.

For practitioners, the message is clear. Don't promise blindly - calculate. Estimate your failure costs and opportunity costs, apply the critical fractile formula, and calibrate your promises accordingly. In a world where the difference between Musk and Holmes often comes down to promise calibration, this framework provides essential guidance for entrepreneurial success.

# References

Cachon, G., & Terwiesch, C. (2013). Matching supply with demand: An introduction to operations management. McGraw-Hill.

Modigliani, F., & Miller, M. H. (1958). The cost of capital, corporation finance and the theory of investment. American Economic Review, 48(3), 261-297.

Porteus, E. L. (2002). Foundations of stochastic inventory theory. Stanford University Press.

Silver, E. A., Pyke, D. F., & Peterson, R. (1998). Inventory management and production planning and scheduling. John Wiley & Sons.

Zipkin, P. H. (2000). Foundations of inventory management. McGraw-Hill.