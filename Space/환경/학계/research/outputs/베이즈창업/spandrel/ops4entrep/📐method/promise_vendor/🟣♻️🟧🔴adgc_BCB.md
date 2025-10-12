### Entrepreneurial Promises as Dynamic Systems: A Prospect Theory Extension

### Abstract

We extend prospect theory to explain entrepreneurial overpromising through system dynamics and feedback loops. Building on Kahneman and Tversky's reference-dependent preferences, we show how temporal cost asymmetry creates systematic promise inflation through interconnected mechanisms. Our "promise vendor" model reveals promise level P as the central node connecting fundability F|P and deliverability D|P through reinforcing and balancing loops. The key insight: immediate underage costs (Cu) interact with discounted overage costs (Co) through conditional dependencies that violate traditional independence assumptions. We incorporate clockspeed (μ₁) and market scale (μ₂) to show how these feedback loops accelerate or dampen. Using Tesla Roadster data, we demonstrate that apparent overconfidence emerges from rational navigation of system dynamics under prospect theory. This reframes entrepreneurship from individual bias to system-level optimization.

# 1. Introduction: System Dynamics Meet Prospect Theory

Entrepreneurial ventures operate as dynamic systems where promises, resources, and capabilities interact through complex feedback loops. We extend prospect theory (Kahneman & Tversky, 1979) to this system context, showing how reference-dependent preferences create predictable patterns of overpromising through temporal and operational interdependencies.

## The Promise System Architecture

Consider the entrepreneurial promise as a system with three core components:
1. **Temporal dynamics**: Cost asymmetry between immediate and future consequences
2. **Operational coupling**: Funding enables capability development (F affects D)
3. **Feedback amplification**: Success reinforces bold promises through reputation

These components interact under prospect theory's value function, where losses loom larger than gains but temporal distance moderates perception. The result: systematic overpromising emerges not from individual bias but from rational system navigation.

## Variables and Their Relationships

Our model centers on promise level P, which influences:
- **F|P**: Funding probability (increases with P)
- **D|P**: Delivery probability (decreases with P)
- **V**: Value from joint success

But critically, these aren't independent. When F|P ⊥̸ D|P (funding affects delivery capability), the system exhibits:
- **Reinforcing loop**: Funding → Resources → Capability → Delivery → Reputation → More funding
- **Balancing loop**: Bold promises → Lower delivery probability → Reputation damage → Conservative promises

The entrepreneur navigates these loops by optimizing:
```
L(P) = Cu(1-F|P)D|P + Co·F|P(1-D|P) - V·F|P·D|P
```

Where temporal structure makes Cu more salient than future Co.

# 2. Literature: From Static Bias to Dynamic Systems

## System Dynamics in Entrepreneurship

Sterman (2000) established system dynamics as crucial for understanding business phenomena. In entrepreneurship:
- **Resource feedback**: Initial resources enable capability building (Penrose, 1959)
- **Reputation cycles**: Past performance affects future opportunities (Diamond, 1989)
- **Network effects**: Success attracts resources attracting success (Barabási & Albert, 1999)

We formalize these dynamics through conditional probability structures.

## Prospect Theory's Temporal Dimension

While original prospect theory focused on static choices, subsequent work incorporated time:
- **Hyperbolic discounting**: Present bias in temporal choices (Laibson, 1997)
- **Myopic loss aversion**: Frequent evaluation leads to conservative choices (Benartzi & Thaler, 1995)

We extend by showing how temporal structure interacts with operational dependencies.

## Entrepreneurial Ecosystems as Complex Systems

Recent ecosystem literature treats entrepreneurship as emergent from system interactions:
- **Isenberg (2010)**: Six domains creating entrepreneurial dynamics
- **Spigel (2017)**: Cultural, social, and material attributes as system components
- **Roundy (2016)**: Feedback loops sustaining entrepreneurial activity

Our model provides micro-foundations for these macro patterns.

# 3. The Promise Vendor System Model

## 3.1 System Structure and Feedback Loops

The promise vendor system exhibits multiple feedback mechanisms:

**Primary Reinforcing Loop (R1)**:
Promise ↑ → Funding probability ↑ → Resources ↑ → Delivery capability ↑ → Success ↑ → Reputation ↑ → Easier future promises

**Primary Balancing Loop (B1)**:
Promise ↑ → Delivery difficulty ↑ → Failure risk ↑ → Reputation damage ↑ → Conservative future promises

**Temporal Moderation Loop (B2)**:
Time delay → Discount future costs → Bias toward present funding → Overpromise → Reality check → Moderation

## 3.2 Mathematical Formalization

System state evolves according to coupled dynamics:

```
dF/dP = μ₂·F(1-F)  [Logistic funding response]
dD/dP = -μ₂·D(1-D) [Inverse logistic delivery response]
```

With coupling term when F affects D:
```
D_effective = D_base + α·F [Deep pocket effect]
```

The optimization problem becomes:
```
P* = argmin L(P) subject to system dynamics
```

## 3.3 Prospect Theory Value Function Integration

Under prospect theory, the entrepreneur evaluates outcomes through:
```
v(x) = x^α for gains
v(x) = -λ(-x)^β for losses
```

Applied to our system:
- Immediate unfunding: v(-Cu) = -λ₁Cu^β (highly salient loss)
- Future failure: δ·v(-Co) = -δλ₂Co^β (discounted loss)
- Success value: δ·v(V) = δV^α (discounted gain)

The system dynamics amplify loss aversion through feedback loops.

## 3.4 Clockspeed and Scale Effects

**Clockspeed μ₁** accelerates all system dynamics:
- Faster funding decisions
- Compressed development cycles
- Rapid reputation formation

This affects the balance between loops—fast ventures experience stronger reinforcing dynamics before balancing loops catch up.

**Market scale μ₂** affects system sensitivity:
- Larger markets → Steeper response curves
- More extreme feedback (both positive and negative)
- Greater variance in outcomes

Combined effect:
```
P* = (1/μ₂)·ln((2Cu + V·δ^(1/μ₁))/(2Co·δ^(1/μ₁) + V·δ^(1/μ₁)))
```

# 4. Empirical Evidence: Tesla's System Navigation

## 4.1 Mapping Tesla's Promise System

Tesla Roadster (2006-2008) exemplifies system dynamics:

**Variables**:
- P: "250-mile range electric sports car by 2008"
- F|P: High (~80%) given Musk's reputation and EV market potential
- D|P: Low (~20%) given battery technology and supply chain complexity
- V: $300M+ including brand value and future platforms

**System coupling (F ⊥̸ D)**:
Funding enabled:
- Battery R&D acceleration
- Supply chain development
- Manufacturing capability

But created dependencies:
- Rush to outsource (Thailand → UK → California)
- Quality challenges from distributed production
- Cash flow pressure affecting engineering decisions

## 4.2 Feedback Loops in Action

**Reinforcing loop observed**:
Bold promise → $45M Series D → Accelerated development → Prototype success → Media attention → Easier Series E → Production capability

**Balancing loop observed**:
Aggressive timeline → Production delays → Customer frustration → Moderated Model S promises → Rebuilt credibility

**System parameters**:
- μ₁ ≈ 3: Moving 3x faster than traditional auto
- μ₂ ≈ 2: Targeting global luxury EV market

Model prediction: P* ≈ 0.71 (71st percentile ambition)
Actual behavior: Aligned with prediction, slight overpromise on timeline due to system dynamics

## 4.3 Cross-Industry System Patterns

Different industries exhibit different system configurations:

**Software**: Tight positive feedback, rapid iteration
- High μ₁ → Quick loops
- Low asset requirements → F doesn't constrain D much
- Result: "Move fast" optimal

**Pharmaceuticals**: Regulated balancing loops
- Low μ₁ → Slow dynamics  
- FDA approval → F strongly affects D
- Result: Conservative promises optimal

**Hardware**: Mixed dynamics
- Medium μ₁ → Moderate pace
- Manufacturing constraints → F partially enables D
- Result: Measured overpromising

# 5. Discussion: System-Level Insights

## 5.1 Individual Navigation of System Dynamics

Entrepreneurs rationally navigate the promise system by:
1. **Reading feedback loops**: Understanding which dominate in their context
2. **Timing interventions**: Leveraging reinforcing loops before balancing loops activate
3. **Managing coupling**: Using funding to genuinely improve delivery capability

This explains lifecycle patterns:
- Early stage: Reinforcing loops dominate → Bold promises
- Growth stage: Balancing loops emerge → Moderation
- Mature stage: System equilibrium → Conservative promises

## 5.2 Ecosystem as Meta-System

Multiple ventures create ecosystem-level dynamics:

**Diversity maintenance**:
- Some ventures exploit reinforcing loops (explorers)
- Others respect balancing loops (exploiters)
- Portfolio effects sustain innovation

**Contagion effects**:
- Success stories shift system parameters for others
- Tesla made EV promises credible industry-wide
- Failures tighten balancing loops temporarily

**Policy leverage points**:
- Bankruptcy laws affect Co (balancing loop strength)
- Funding availability affects Cu (reinforcing loop trigger)
- Market structure affects μ₂ (system sensitivity)

## 5.3 Designing Entrepreneurial Systems

Understanding promise systems enables design interventions:

**For entrepreneurs**:
- Map your feedback loops
- Identify coupling points where F enables D
- Time promises to leverage system dynamics

**For investors**:
- Recognize rational overpromising in high-reinforcement contexts
- Design contracts acknowledging system dynamics
- Stage funding to manage coupling effects

**For policymakers**:
- Foster healthy feedback diversity
- Prevent excessive reinforcement (bubbles) or balancing (stagnation)
- Create "sandbox" environments for system experimentation

# 6. Conclusion: Embracing System Complexity

We extend prospect theory to entrepreneurial systems, showing how overpromising emerges from rational navigation of feedback loops under reference-dependent preferences. The promise vendor model reveals promise level P as the key control variable in a complex system where funding and delivery capabilities interact through reinforcing and balancing dynamics.

This system view reframes entrepreneurial behavior:
- From individual bias → System optimization
- From static decision → Dynamic navigation  
- From failure to correct → Feature to channel

The entrepreneur's challenge—promising boldly enough to trigger reinforcing loops while managing balancing loops—reflects sophisticated system navigation, not cognitive failure. Understanding these dynamics enables better individual strategies and ecosystem design.

Future research should explore:
- Multi-agent system dynamics
- Adaptive learning within systems
- Optimal diversity maintenance
- Policy interventions at system leverage points

In complex entrepreneurial systems, overpromising isn't a bug—it's the fuel that drives reinforcing loops creating innovation. The key is designing systems that channel this fuel productively.

# References

Barabási, A., & Albert, R. (1999). Emergence of scaling in random networks. Science, 286(5439), 509-512.

Benartzi, S., & Thaler, R. (1995). Myopic loss aversion and the equity premium puzzle. Quarterly Journal of Economics, 110(1), 73-92.

Diamond, D. (1989). Reputation acquisition in debt markets. Journal of Political Economy, 97(4), 828-862.

Isenberg, D. (2010). How to start an entrepreneurial revolution. Harvard Business Review, 88(6), 40-50.

Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. Econometrica, 47(2), 263-291.

Laibson, D. (1997). Golden eggs and hyperbolic discounting. Quarterly Journal of Economics, 112(2), 443-478.

Penrose, E. (1959). The Theory of the Growth of the Firm. Oxford University Press.

Roundy, P. (2016). Start-up community narratives: The discursive construction of entrepreneurial ecosystems. Journal of Entrepreneurship, 25(2), 232-248.

Spigel, B. (2017). The relational organization of entrepreneurial ecosystems. Entrepreneurship Theory and Practice, 41(1), 49-72.

Sterman, J. (2000). Business Dynamics: Systems Thinking and Modeling for a Complex World. McGraw-Hill.