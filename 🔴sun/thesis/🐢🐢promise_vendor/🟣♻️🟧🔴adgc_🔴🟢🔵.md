# uncertainty making under promise

## Abstract
Business Model Prior Calibration: A Theoretical Framework for Action-Oriented Belief Encoding Paradigmatic Innovation in Bayesian Decision Theory The proposed framework of "Business Model Prior Calibration" represents a fundamental reconceptualization of Bayesian inference in entrepreneurial contexts. By treating prior distributions as action-oriented encodings rather than epistemic states, this approach resolves the theoretical tension between optimization and belief formation while maintaining mathematical coherence."

AS-IS: $\underset{ϕ}{min} E[Cost] = g(ϕ)=C⋅P(S=1,D=0∣ϕ)−V⋅P(S=1,D=1∣ϕ)=Cϕ2−Vϕ(1−ϕ)$
 founder knows exactly what one should promise $\phi$ which implies founder isn't learning anything from the experiment which beats the purpose of experiment in most cases

TO-BE:
$\underset{a,b}{min} E[Cost] = \int g(ϕ) P(ϕ) dϕ$ where $ϕ \sim Beta(a,b)$

founder minimize expected cost given one's prior of promise level. prior becomes decision variable, meaning founder choose what and how one should be uncertain about, rather than optimizing given exogenous uncertainty. main goal is to separate existing confusion on prior and belief. As such, we define prior as action-oriented encoding of belief and show how environment's cost parameter of action to sell then deliver promise affects the optimal prior on promise level. Using our framework, founder can calibrate prior distribution on their promise level before promising. This calibration is formulated as optimization problem where the founder minimize the expected cost using marginalized likelihood of sell or buy event which is environment's reaction to one's promise. This process of calibrating one's prior using simulated prior update helps founder become more flexible in their business modeling. 



this means the EVENT PROBABILITY P(S=1, D=0) is marginalized likelihood which is calculated by founder as weighted average of P(S=1, D=0|phi) using one's prior p(phi). likewise, from founder's perspective, event probability P(S=1, D=1) is marginalizing P(S=1, D=0|phi) over the weight p(phi) as founder will choose this promise level distribution to create uncertainty which its environment will react to. we derive P(S=1, D=0) = Beta(a+2, b)/Beta(a, b) and P(S=1, D=1) = Beta(a+1, b+1)/Beta(a, b). Note Beta(a, b+1) + Beta(a+2, b) + Beta(a+1, b+1) = Beta(a, b), proving the probability of three events adds up to one.


How should entrepreneurs calibrate their promises to maximize success? This paper develops a "promise vendor" model that prescribes optimal promise levels by adapting the newsvendor framework to entrepreneurial contexts. Unlike inventory decisions facing exogenous demand, entrepreneurial promises create the market conditions they must satisfy. We formalize three key outcomes: not sold (cost C_ns), sold but not delivered (cost C_snd), and sold and delivered (value V_sd). The model shows how promise level φ affects market response through P(Sell|φ) = φ and delivery capability through P(Deliver|φ) = 1-φ. Using Tesla's choice between promising 150-mile versus 300-mile range in 2008, we derive conditions for optimal promises: ambitious when not-sold costs exceed sold-not-delivered costs (C_ns > C_snd), modest when reversed (C_snd > C_ns), and moderate when balanced (C_ns ≈ C_snd). The promise vendor framework provides entrepreneurs quantitative guidance for this fundamental strategic choice.

## 1. Introduction

### 1.1 Promises to Prison or Power

Ambitious promises create surprising outcomes: spectacular success or spectacular failure. Elon Musk promised 300-mile range electric vehicles when battery costs exceeded $1,000/kWh; Tesla now commands an $800 billion valuation. Elizabeth Holmes promised instant blood diagnostics from a single drop; she serves an eleven-year sentence. Steve Jobs promised 1,000 songs in your pocket when flash memory cost $400 per gigabyte; Apple became history's most valuable company. Billy McFarland promised luxury festival experiences on a Bahamian island; he entered federal prison for fraud.

Analyzing broader patterns reveals consistent dynamics. Jeff Bezos promised one-hour delivery when logistics networks could barely support two-day shipping; Amazon revolutionized commerce. Sam Bankman-Fried promised revolutionary trading infrastructure; FTX collapsed in spectacular fashion. Each entrepreneur made ambitious promises that strained contemporary technological capabilities. Success and failure diverged not in promise boldness but in navigating the consequences of those promises.

Assessing these observations raises a fundamental question: What determines the optimal level of entrepreneurial promises? Promise too modestly and fail to attract customers or investors. Promise too ambitiously and risk catastrophic delivery failure. Between these extremes lies an optimal promise level that maximizes expected success.

### 1.2 Promises Create What They Must Satisfy

Analyzing traditional operations research reveals how firms match supply to demand. A newspaper vendor observes market signals, forecasts demand, then stocks inventory accordingly. Demand exists independently; the vendor's decision affects only how well supply matches it. This separation between decision and uncertainty enables classical optimization techniques.

Alternatively, entrepreneurs face a fundamentally different problem. Before Tesla's promise of a luxury electric vehicle, no such market existed. The promise itself created customer interest, attracted investor capital, and motivated supplier partnerships. Abstracting secondary effects such as decreasing marginal return and stationary customer and capabilities, bolder promise has higher market potential and is more challenging to deliver compared to modest promise. Example of bold promises are: flying car, 300 mile range electric vehicle (EV), $2 cost per mile autonomous truck; as opposed to modest promises, electric golf cart, 150 mile range EV, $10 cost per mile autonomous truck. We capture this tradeoff on promise level to formulate optimization problem.

Accordingly, this endogeneity transforms the optimization landscape. A newsvendor chooses inventory quantity q to match exogenous demand D. An entrepreneur chooses promise level φ that generates both market demand and delivery challenge. The decision variable constructs the probability space within which success or failure occurs.

### 1.3 Asymmetric Costs Drive Bold Promises

Asymmetric consequences of modest versus ambitious promises create different strategic incentives. Consider Tesla in 2008 choosing between a 150-mile range (φ = 0.3) and 300-mile range (φ = 0.7) promise:

**Modest promise (150 miles)**: Few customers find this compelling for a $100,000 sports car. The venture dies from lack of market interest. Not-sold cost C_ns equals the entire venture value lost when sellable technology goes unfunded.

**Ambitious promise (300 miles)**: Many customers want this breakthrough capability. Capital flows in, development proceeds, but technical challenges mount. If delivery fails, sold-not-delivered cost C_snd includes reputation damage, lawsuits, and refunds.

Asymmetric magnitudes emerge: C_ns represents total opportunity loss when ventures fail to launch, while C_snd represents manageable penalties after attempting delivery. Early-stage ventures typically face C_ns >> C_snd because they have minimal assets at risk but massive potential upside. This asymmetry systematically favors ambition, explaining why rational entrepreneurs make seemingly overconfident promises.

### 1.4 Toward a Quantitative Framework

Addressing these tradeoffs, we develop the promise vendor model for quantification. By adapting newsvendor logic to entrepreneurial contexts, we derive closed-form solutions for optimal promise levels. The framework reveals when entrepreneurs should promise boldly (high C_ns/C_snd), modestly (high C_snd/C_ns), or moderately (balanced costs).

The model contributes to three literatures. First, it extends operations research by analyzing decisions that create rather than react to uncertainty. Second, it provides entrepreneurship research with quantitative tools for strategic promise decisions. Third, it bridges behavioral and rational perspectives by showing how apparent overconfidence emerges from optimal responses to asymmetric costs.

## 2. The Promise Vendor Framework

### 2.1 GAME: Entrepreneurs Generate Their Own Playing Field

Entrepreneurs generate their own game by choosing promise level φ, creating a tree where bold promises attract customers but challenge delivery while modest promises ensure delivery but fail to excite markets. Unlike newsvendors who stock inventory against exogenous demand patterns, promise vendors construct the decision tree their venture must navigate. The promise φ branches into sell-or-not based on market response, which further branches into deliver-or-not based on capability realization.

This game generation inverts classical decision theory. Newsvendors observe historical data, forecast demand distribution D, then choose inventory q to match it. Promise vendors choose φ first, which then determines the probabilities P(Sell|φ) and P(Deliver|φ) they face. The decision variable creates the stochastic space rather than responding to it. Tesla's 2008 choice between promising 150-mile range (modest but stress-free) versus 300-mile range (bold but stressful) exemplified this game construction—the promise itself determined which market they would compete in.

The promise vendor tree admits dual interpretations:

**Founder's View**: "I must navigate given market response functions"
```
      ┌─── (1-Ps) ──→ Not Sold
      │
φ ────┤
      │      ┌─── Pd ────→ Delivered  
      └─ Ps ─┤
             └─── (1-Pd) ─→ Not Delivered
```

**Society's View**: "Today's outcomes shape tomorrow's response functions"
```
      ┌─── (1-Ps) ──→ Not Sold → Future Ps↓
      │
φ ────┤
      │      ┌─── Pd ────→ Delivered → Future Pd↑  
      └─ Ps ─┤
             └─── (1-Pd) ─→ Not Delivered → Future Pd↓
```

Committee perspective (Mansinghka): This generative view aligns with probabilistic programming where entrepreneurs write the stochastic program that reality executes. The promise level φ serves as the key parameter that shapes all downstream randomness.

### 2.2 COST: Asymmetric Penalties Shape Strategic Choices

Cost asymmetry affects outcomes. The venture dies unknown from not selling (C_ns) versus dies known from selling but not delivering (C_snd), while successful delivery generates value (V_sd). This structure fundamentally differs from newsvendor's symmetric overage and underage costs that balance marginal losses.

Cost C_ns strikes with existential force: modest promises fail to attract customers, no customers means no funding, no funding means no venture. The entire potential value vanishes when the market ignores underwhelming promises. A promise of "electric golf cart" for urban transport might work technically but dies commercially from lack of interest. Cost C_snd arrives after ambitious promises attract resources but fail delivery, incurring reputation damage, refunds, and legal penalties. Meanwhile, successful matching—selling and delivering—generates value V_sd that justifies the risk.

The three terminal states create an optimization landscape: not sold incurs C_ns, sold-but-not-delivered incurs C_snd, while sold-and-delivered earns V_sd. This asymmetric structure explains entrepreneurial behavior—when C_ns (opportunity cost of being ignored) exceeds C_snd (failure cost after trying), rational entrepreneurs choose ambitious promises. Early-stage ventures typically face C_ns >> C_snd because they have little to lose but everything to gain.

Committee perspective (Stern): This cost alienation represents entrepreneurial experimentation where founders rationally accept the risk of public failure (C_snd) to avoid the certainty of obscure death (C_ns), 🚨treating promises as real options on future capability.🚨

### 2.3 PROBABILITY: Response Functions Create the Fundamental Tradeoff

Markets distribute outcomes through response functions where sellability increases with promise ambition while deliverability decreases, forcing entrepreneurs to balance excitement against feasibility. In the baseline formulation, Sell|φ ~ Bernoulli(φ) captures how bolder promises attract more customers, while Deliver|φ ~ Bernoulli(1-φ) reflects increasing technical difficulty.

The hierarchical structure reveals how promises propagate through the system:

P(Deliver = 1) = P(Deliver|Sell=0)·P(Sell=0) + P(Deliver|Sell=1)·P(Sell=1)

where P(Sell=1|φ) increases and P(Deliver=1|φ) decrease as φ increases. This decomposition shows that delivery probability depends on whether selling occurs, though our baseline model assumes conditional independence given φ.

This creates the promise vendor's central tension: the very ambition that attracts customers challenges delivery. A φ=0.9 promise of "fully autonomous driving by next year" maximizes sellability but minimizes deliverability. A φ=0.1 promise of "lane keeping assistance" ensures delivery but attracts few buyers. The entrepreneur must navigate this probability landscape where moving along φ shifts odds in opposite directions.

Real response functions exhibit more complexity through sigmoid shapes that capture threshold effects. Customers show little interest until promises exceed some minimum ambition φ₀, then enthusiasm saturates above φ₁. Similarly, delivery probability may remain high until promises exceed capability limits, then drop sharply. These nonlinearities create sweet spots where marginal increases in φ yield maximum benefit. 🚨cite Ben-Akiva's literature to explain how he motivates random utility model in discrete choice analysis🚨 

Committee perspective (Ben-Akiva): Promise calibration represents choice architecture where entrepreneurs design the choice set that stakeholders face, with response functions emerging from how different segments value ambition versus reliability.

### 2.4 DECISION: Optimizing Promise Level Through Feedback

#### Founder's Perspective: Promise Making Under Uncertainty
Entrepreneurs calibrate optimal promises by minimizing expected cost E[C] = C_snd·φ² + C_ns·(1-φ) - V_sd·φ(1-φ), where the three terms capture not selling, selling-but-not-delivering, and successful matching respectively. The first-order condition yields φ* that reveals when to promise boldly (high C_ns/C_snd), modestly (low C_ns/C_snd), or moderately (balanced costs). From this view, uncertainty exists independently—the founder's job is making the best promise given fixed probabilities.

#### Society's Perspective: Uncertainty Making Under Promise
The market maintains Beta priors about each entrepreneur's type θ (tendency to choose high or low φ), updating these beliefs through sequential promise-outcome observations:

Starting from θ ~ Beta(1,1) (unknown type), the first outcome branches:
- Not sold → θ ~ Beta(1,2): Conservative type who under-promises
- Sold → θ ~ Beta(2,1): Bold type who can excite markets

Among those who sold, delivery outcomes further refine beliefs:
- Delivered → θ ~ Beta(2,2): Calibrated visionary who balances ambition with execution  
- Not delivered → θ ~ Beta(3,1): Chronic over-promiser who sells dreams but delivers nightmares

From society's view, today's promises create tomorrow's uncertainty. Tesla's repeated delivery of "impossible" promises shifted Musk's type toward high α in Beta(α,β), enabling increasingly bold promises to be taken seriously. Conversely, Theranos contaminated Holmes's type toward high β, making future biotech promises harder to sell. The market has a memory—each venture's promise-outcome pair becomes data that calibrates collective beliefs about entrepreneur types.

#### The Fundamental Duality
What appears as exogenous uncertainty to individual founders emerges from endogenous learning at the population level. Founders optimize against perceived constraints while simultaneously creating those constraints for future entrepreneurs through type revelation. This duality explains why promise vendor equilibria can shift dramatically—a few spectacular successes or failures can recalibrate entire sectors' beliefs about what type of entrepreneur succeeds. The model deliberately brackets certain endogeneities like capital-capability spirals, acknowledging these create additional feedback loops beyond pure type learning.

Committee perspective (Fine): Promise decisions cannot be separated from capability evolution—the very act of making bold promises can catalyze organizational capabilities while Beta-binomial type learning ensures today's entrepreneurs shape tomorrow's funding landscape.

## 3. Model Development

### 3.1 Linear Promise Vendor Model

Generalizing from newsvendor's inventory optimization given uncertain demand D:

**Minimize**: E[Cost] = co·E[(q-D)⁺] + cu·E[(D-q)⁺]

Where (x)⁺ = max(0,x). The optimal quantity q* satisfies:

P(D ≤ q*) = cu/(cu + co)

This critical fractile formula balances marginal overage against underage costs.

Given endogenous uncertainties, the promise vendor optimizes promise level φ ∈ [0,1]:

**Minimize**: E[Cost] = C_snd·P(Sell=1|φ)·P(Deliver=0|φ) + C_ns·P(Sell=0|φ) - V_sd·P(Sell=1|φ)·P(Deliver=1|φ)

Where:
- P(Sell=1|φ) = φ (sellability increases with promise ambition)
- P(Deliver=1|φ) = 1-φ (deliverability decreases with promise ambition)

Substituting these probability functions:

E[Cost] = C_snd·φ·φ + C_ns·(1-φ) - V_sd·φ·(1-φ) = C_snd·φ² + C_ns·(1-φ) - V_sd·φ(1-φ)

Generating insights through first-order conditions:

dE[Cost]/dφ = 2C_snd·φ - C_ns - V_sd(1-2φ) = 0

Rearranging:

2C_snd·φ + 2V_sd·φ = C_ns + V_sd

Therefore: φ* = (C_ns + V_sd)/(2C_snd + 2V_sd)

![[🖼️promise_performance_tradeoff.svg]]

*Figure 1: Fundamental trade-off embedded in the linear probability model. The intersection at φ = 0.5 represents the point where sale and delivery probabilities equalize, corresponding to the maximum joint probability φ(1-φ). This visual representation clarifies why V_sd >> C_snd, C_ns drives φ* toward 0.5—the matching value dominates cost considerations, pulling the optimal promise toward maximum joint success probability.*

Governing entrepreneurial behavior, this closed-form solution reveals the cost-priority principle: optimal promise level increases with not-sold cost C_ns while decreases with sold-not-delivered cost C_snd. When match value is large V_sd >> C_snd, C_ns, optimal promise level φ* converges to 0.5, implying a balance between selling and delivering. This result emerges naturally since the matching probability φ(1-φ) achieves its maximum at φ = 0.5.

### 3.2 Sigmoid Response Functions (need recalculation)

Generalizing beyond linear probability functions P(Sell|φ) = φ captures realistic stakeholder psychology. Real customers exhibit threshold effects: indifference below φ₀, enthusiasm above φ₁. Similarly, partners show commitment cliffs when promises exceed capabilities.

We generalize to sigmoid response functions:

P(Sell|φ) = 1/(1 + e^(-βc(φ-0.5)))
P(Deliver|φ) = 1/(1 + e^(βr(φ-0.5)))

Where βc and βr control response steepness. Larger β creates sharper transitions between rejection and acceptance.

Gauging different quality sensitivities reveals stakeholder heterogeneity. Tech-savvy early adopters (large βc) react dramatically to feature improvements. Conservative partners (small βr) change gradually. This asymmetry can override cost considerations.

### 3.3 Strategic Implications and Contextual Applications

Guiding strategic decisions, the model prescribes context-specific promise levels based on the ratio C_ns/C_snd:

**Case 1: Early-stage ventures (C_ns >> C_snd)**
Not-sold cost dominates when unfunded ideas represent massive foregone opportunities. With C_ns = $10M potential value lost and C_snd = $100K reputation risk, φ* → 1 prescribes maximum ambition. The venture has little to lose from failure but everything to gain from market excitement.

**Case 2: Mature ventures (C_snd >> C_ns)**  
Sold-not-delivered cost dominates when established firms risk accumulated brand value. With C_snd = $1B reputation damage and C_ns = $10M opportunity cost, φ* → 0 prescribes conservative promises. The firm protects existing assets rather than pursuing speculative gains.

**Case 3: Balanced ventures (C_ns ≈ C_snd)**
Equal costs yield φ* = 0.5 (when V_sd is moderate), prescribing moderate promises that balance market excitement against delivery risk. This equilibrium emerges in competitive markets where neither playing it safe nor going all-out provides decisive advantage.

The framework extends naturally to dynamic settings where costs evolve with venture maturity, market conditions change response functions, and feedback loops create path dependencies. Section 4 explores these extensions in detail.

## 4. Discussion and Implications

### 4.1 Temporal Reversal: When Capability Precedes Customers

Challenging our promise-then-deliver framework, certain contexts exhibit "deliver-then-sell" dynamics where capability development precedes market creation. Deep tech ventures developing fundamental technologies (quantum computing, fusion energy, CRISPR) often achieve technical breakthroughs before identifying commercial applications. Here, the optimization inverts: minimize the salvage cost of unutilized capability while searching for market fit.

Consider pharmaceutical development where compounds exist before diseases are targetable, or Bell Labs' transistor invention preceding its market applications by decades. These scenarios require a dual-phase model: Phase 1 optimizes capability development under technical uncertainty, Phase 2 optimizes promise calibration given existing capabilities. The salvage cost of "delivered but unsold" capability—unutilized patents, idle manufacturing capacity, stranded R&D investments—becomes the primary loss function.

Critical insight: The promise vendor framework assumes customer pull dominates technology push. When reversed, entrepreneurs face a fundamentally different optimization—not "what should we promise?" but "what can we promise given what we've built?" This capability-first pathway explains why technical founders often struggle with commercialization: they optimize for deliverability (1-φ) rather than sellability (φ), systematically under-promising relative to their capabilities. Future work should develop a unified framework encompassing both promise-first and capability-first innovation pathways.

### 4.2 Cost Architecture: Who Sets Parameters and Why

Constructing entrepreneurial ecosystems requires understanding how society shapes the cost parameters (C_ns, C_snd, V_sd) that drive promise decisions. These parameters emerge from multiple actors with conflicting objectives: entrepreneurs maximize personal returns, investors seek portfolio performance, regulators protect consumers, and society desires innovation with minimal negative externalities.

Consider how different institutional designs create distinct parameter regimes. Silicon Valley's ecosystem minimizes C_snd through forgiving bankruptcy laws, normalized failure narratives, and rapid re-employment opportunities—enabling bold promises. Conversely, German Mittelstand culture amplifies C_snd through reputational permanence and community accountability, favoring incremental innovation. Singapore manipulates V_sd through generous R&D tax credits and innovation prizes, while maintaining moderate C_snd through efficient courts that swiftly resolve commercial disputes.

Critical design principles emerge: (1) **Asymmetry preservation**—maintaining C_ns > C_snd ensures entrepreneurial dynamism; (2) **Dynamic calibration**—parameters should evolve with venture maturity to prevent excessive risk-taking by established firms; (3) **Stakeholder alignment**—V_sd should incorporate social returns beyond private gains. Society faces a fundamental tradeoff: lower C_snd encourages breakthrough innovation but enables fraud (Theranos), while higher C_snd ensures accountability but stifles transformation. Optimal parameter design likely requires sector-specific calibration—low C_snd for software where failure costs are contained, high C_snd for biotech where lives are at stake.

### 4.3 Catastrophic Uncertainty: When Promise Spaces Collapse

Catastrophic events—COVID-19, financial crises, wars, AI breakthroughs—fundamentally redefine the promise landscape by simultaneously shifting customer needs and delivery capabilities. Our model assumes stable probability functions P(Sell|φ) and P(Deliver|φ), but catastrophes create discontinuous jumps where entire promise categories become obsolete (travel during COVID) or suddenly viable (remote work technologies).

Consider three catastrophe types and their effects on promise optimization. **Demand shocks** (COVID lockdowns) instantly reset P(Sell|φ) functions—promises of "premium dining experiences" became unsellable overnight while "contactless delivery" surged. **Supply shocks** (chip shortages, war disruptions) collapse P(Deliver|φ) across entire sectors, forcing mass promise recalibration. **Paradigm shifts** (ChatGPT's emergence) create new promise dimensions previously unconsidered—suddenly every software company could promise "AI-powered" features.

Critical modeling challenges emerge: (1) **Non-stationarity**—parameters C_ns, C_snd, V_sd become time-varying stochastic processes rather than constants; (2) **Correlation breakdown**—previously independent stakeholder responses become highly correlated during crises; (3) **Option value**—maintaining promise flexibility gains importance relative to optimization. Catastrophic uncertainty suggests entrepreneurs should optimize for adaptability rather than specific promise levels. Future work must develop robust optimization techniques that perform well across multiple regime shifts, potentially using scenario planning or real options frameworks to value promise flexibility during turbulent periods.

### 4.4 Capital-Capability Spiral: Self-Fulfilling Promises and Deep Pockets

Capital-capability endogeneity—where funding directly improves delivery probability—creates self-fulfilling dynamics that fundamentally alter promise optimization. When P(Deliver|φ) = ∫ P(Deliver|Fund,φ) × P(Fund|φ) dFund with P(Deliver|Fund,φ) increasing in Fund, bold promises attract capital that enables their own fulfillment. This positive feedback can drive unbounded promise escalation, as entrepreneurs rationally increase φ knowing that the promise itself generates resources for delivery.

Consider the deep pocket effect exemplified by Elon Musk's ventures. Tesla's survival through "production hell" depended critically on Musk's ability to inject personal capital during crisis moments—transforming P(Deliver|Fund=∞,φ=0.7) ≈ 1 despite P(Deliver|Fund=0,φ=0.7) ≈ 0.1. This cash shield against technological uncertainty creates profound unfairness: identical promises carry different failure probabilities depending on founder wealth. The poor entrepreneur's bold promise remains genuinely risky; the wealthy entrepreneur's identical promise becomes self-fulfilling prophecy.

Critical modeling requirements for capturing these dynamics include: (1) **Stochastic differential equations** tracking how capital accumulation affects capability evolution d(Capability) = α(Fund)dt + σdW; (2) **Fixed point analysis** identifying stable promise equilibria where φ* = f(φ*) through funding feedback; (3) **Inequality measures** quantifying how initial wealth W₀ affects terminal success probability P(Success|W₀). Without modeling this endogeneity, we systematically underestimate optimal promises for wealthy entrepreneurs and overestimate them for resource-constrained founders. Future work must develop dynamic models where promises, funding, and capabilities co-evolve, potentially revealing multiple equilibria—virtuous cycles for the wealthy, vicious cycles for the poor—that explain persistent inequality in entrepreneurial outcomes despite equal talent and effort.

## References

Arrow, K., Harris, T., & Marschak, J. (1951). Optimal inventory policy. Econometrica, 19(3), 250-272.

Baker, T., & Nelson, R. E. (2005). Creating something from nothing: Resource construction through entrepreneurial bricolage. Administrative Science Quarterly, 50(3), 329-366.

Modigliani, F., & Miller, M. H. (1958). The cost of capital, corporation finance and the theory of investment. American Economic Review, 48(3), 261-297.

Porteus, E. L. (2002). Foundations of stochastic inventory theory. Stanford University Press.

Sarasvathy, S. D. (2001). Causation and effectuation: Toward a theoretical shift from economic inevitability to entrepreneurial contingency. Academy of Management Review, 26(2), 243-263.

Scarf, H. (1958). A min-max solution of an inventory problem. Studies in the Mathematical Theory of Inventory and Production, 201-209.
