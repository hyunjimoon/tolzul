# uncertainty making under promise, promise making under uncertainty

## Abstract

How should entrepreneurs calibrate their promises to maximize success? This paper develops a "promise vendor" model that prescribes optimal promise levels by adapting the newsvendor framework to entrepreneurial contexts. Unlike inventory decisions facing exogenous demand, entrepreneurial promises create the market conditions they must satisfy. We formalize two key costs: the failure cost of ambitious promises (sold but undelivered) and the opportunity cost of modest promises (deliverable but unsold). The model shows how promise level φ affects market response through P(Sell|φ) = φ and delivery capability through P(Deliver|φ) = 1-φ. Using Tesla's choice between promising 150-mile versus 300-mile range in 2008, we derive conditions for optimal promises: ambitious when opportunity costs exceed failure costs (Cu > Co), modest when reversed (Co > Cu), and moderate when balanced (Cu ≈ Co). The promise vendor framework provides entrepreneurs quantitative guidance for this fundamental strategic choice.

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

Asymmetric consequences of modest versus ambitious promises arrive at different times with different magnitudes. Consider Tesla in 2008 choosing between a 150-mile range (φ = 0.3) and 300-mile range (φ = 0.7) promise:

**Modest promise (150 miles)**: Few customers find this compelling for a $100,000 sports car. The venture dies immediately from lack of market interest. Underpromise cost Cu equals the entire venture value lost when sellable technology goes unfunded.

**Ambitious promise (300 miles)**: Many customers want this breakthrough capability. Capital flows in, development proceeds, but technical challenges mount. If delivery fails after years of effort, overpromise cost Co includes reputation damage, lawsuits, and refunds.

Acute timing differences emerge: Cu strikes immediately at t=0 when customers ignore modest promises. Co arrives later at t=T when ambitious promises fail delivery, discounted by factor δ^T. This temporal structure systematically favors ambition. Even with equal nominal costs, time value makes Cu > Co·δ^T, tilting optimal promises toward boldness.

### 1.4 Toward a Quantitative Framework

Addressing these tradeoffs, we develop the promise vendor model for quantification. By adapting newsvendor logic to entrepreneurial contexts, we derive closed-form solutions for optimal promise levels. The framework reveals when entrepreneurs should promise boldly (high Cu/Co), modestly (high Co/Cu), or moderately (balanced costs).

The model contributes to three literatures. First, it extends operations research by analyzing decisions that create rather than match uncertainty. Second, it provides entrepreneurship research with quantitative tools for strategic promise decisions. Third, it bridges behavioral and rational perspectives by showing how apparent overconfidence emerges from optimal responses to asymmetric costs.

## 2. Literature Review

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Promise Vendor: Dual Perspectives</title>
    <style>
        body {
            font-family: 'Courier New', monospace;
            background: white;
            padding: 40px;
            max-width: 700px;
            margin: 0 auto;
            line-height: 1.8;
        }
        .perspective {
            margin: 30px 0;
            padding: 25px;
            border-radius: 8px;
        }
        .founder-view {
            background: #e3f2fd;
            border: 2px solid #2196f3;
        }
        .society-view {
            background: #e8f5e9;
            border: 2px solid #4caf50;
        }
        h3 {
            margin-top: 0;
            font-size: 1.1em;
        }
        pre {
            font-size: 14px;
            margin: 15px 0;
        }
        .insight {
            font-style: italic;
            color: #555;
            margin-top: 10px;
        }
    </style>
</head>
<body>

<h2 style="text-align: center;">Promise Vendor: Two Views of Ps and Pd</h2>

<div class="perspective founder-view">
<h3>Founder's Perspective</h3>
<pre>
         ┌──── 1-Ps ───→ Not Sold
         │
   φ ────┤
         │         ┌───── Pd ────→ Delivered
         └─── Ps ──┤
                   └──── 1-Pd ───→ Not Delivered
</pre>
<div class="insight">
"Ps and Pd are market response functions I must navigate"
</div>
</div>

<div class="perspective society-view">
<h3>Society's Perspective</h3>
<pre>
         ┌──── 1-Ps ───→ Not Sold → Future Ps↓
         │
   φ ────┤
         │         ┌───── Pd ────→ Delivered → Future Pd↑
         └─── Ps ──┤
                   └──── 1-Pd ───→ Not Delivered → Future Pd↓
</pre>
<div class="insight">
"Today's promises and outcomes determine tomorrow's Ps and Pd"
</div>
</div>

</body>
</html>

### 2.1 Time: From Inventory-Then-Sell to Promise-Then-Deliver

Developing from classical newsvendor theory, the model anchors stochastic inventory decisions (Scarf, 1958; Porteus, 2002). A vendor observes historical demand patterns, forecasts future demand, then stocks inventory before demand realizes. Information flows from past to present to future. Decisions respond to but do not influence uncertainty.

Dramatically, entrepreneurial ventures invert this temporal sequence. Promises precede capability development. Tesla announced 300-mile range before securing battery technology. Apple promised 1,000 songs before miniaturizing storage. Amazon promised one-day delivery before building fulfillment infrastructure. The promise attracts resources that enable delivery, reversing causality from observe-then-act to promise-then-create.

Documented throughout entrepreneurship literature, this temporal inversion transforms decision-making. Sarasvathy (2001) contrasts predictive (causal) with creative (effectual) logics. Baker and Nelson (2005) document how entrepreneurs create resources through bricolage. Our model formalizes this insight: promises at t=0 determine probabilities that realize across time.

### 2.2 Cost Parameters: Asymmetric Penalties Transform Optimization

Distinguishing from newsvendor's balanced structure, entrepreneurial costs exhibit fundamental asymmetry. Overage cost co equals unit cost minus salvage value when inventory exceeds demand. Underage cost cu equals price minus cost when demand exceeds inventory. Both represent marginal economic losses realized simultaneously when demand arrives.

Diverging fundamentally in magnitude and timing, promise vendor costs create new dynamics:

**Underpromise cost Cu**: The entire venture value vanishes when modest promises fail to attract customers. This existential cost hits immediately at t=0. No customers means no funding, no development, no future. The venture dies unknown.

**Overpromise cost Co**: Reputation damage and financial penalties when ambitious promises fail delivery. These costs arrive at t=T after development attempts, discounted by δ^T. The venture dies known, but only after existing.

Driving systematic patterns, this asymmetry shapes venture evolution. Early-stage ventures face extreme Cu (huge opportunities foregone) and modest Co (limited assets at risk), making Cu/Co >> 1. The mathematics then prescribe bold promises (high φ*). As ventures mature, accumulated assets increase Co while proven models reduce Cu, shifting Cu/Co toward 1 and moderating optimal promises.

### 2.3 Uncertainty: Endogenous Variables Violate Classical Assumptions

Departing from traditional stochastic optimization's independence assumption, promise vendors face endogenous uncertainty. Newsvendor inventory q does not affect demand distribution D. This separation enables elegant mathematical analysis through critical fractile formulas (Arrow et al., 1951).

Decisions about promises fundamentally violate this independence. Promise level φ determines both sellability P(Sell=1|φ) = φ and deliverability P(Deliver=1|φ) = 1-φ. The decision variable parameterizes the uncertainty space. This endogeneity creates mathematical complexity but also strategic opportunity.

Directly challenging finance theory, this violation undermines classical assumptions. Modigliani and Miller (1958) proved capital structure irrelevance under perfect markets, assuming operational and financial decisions separate. Promise vendors integrate these realms: promises attract funding that enables operations. The promise mechanism makes operations and finance inseparable, explaining why entrepreneurial finance differs qualitatively from corporate finance.

### 2.4 Capital-Capability Endogeneity: What We Exclude but Matters

Deliberately, our model assumes conditional independence P(Sell|φ) ⊥ P(Deliver|φ) given promise level φ, though reality violates this through capital-mediated effects. When sellability generates funding that enhances deliverability, the true relationship becomes P(Deliver|φ) = ∫ P(Deliver|Fund,φ) × P(Fund|φ) dFund, where P(Fund|φ) increases with φ through investor attraction.

Demonstrating self-fulfilling dynamics, this endogeneity can drive unbounded promise escalation. Entrepreneurs recognizing that bold promises attract capital which improves delivery capability face incentives to continuously increase φ. Without natural bounds, this positive feedback loop pushes promises toward infinity—explaining phenomena like theranos's ever-expanding claims or crypto projects' astronomical projections.

Deep pocket effects compound this unfairness systematically. When P(Deliver|Fund,φ) increases with funding level, wealthy entrepreneurs enjoy a "cash shield" against technological uncertainty. Tesla's survival through production delays exemplifies this: Musk's personal wealth and funding access transformed a 1-φ delivery probability into near-certainty through capital infusion. This violates both Arrow et al.'s (1951) newsvendor independence and Modigliani-Miller's (1958) separation theorem.

Declining to model these dynamics preserves analytical tractability while acknowledging their importance. Our static framework cannot capture how funding flows evolve delivery capabilities over time. Section 6 discusses implications of this simplification, particularly regarding entrepreneurial inequality and policy interventions. For now, we maintain P(Sell|φ) ⊥ P(Deliver|φ) to derive baseline insights about promise optimization.

## 3. Model Development

### 3.1 From Newsvendor to Promise Vendor

Generalizing from newsvendor's inventory optimization given uncertain demand D:

**Minimize**: E[Cost] = co·E[(q-D)⁺] + cu·E[(D-q)⁺]

Where (x)⁺ = max(0,x). The optimal quantity q* satisfies:

P(D ≤ q*) = cu/(cu + co)

This critical fractile formula balances marginal overage against underage costs.

Given endogenous uncertainties, the promise vendor optimizes promise level φ ∈ [0,1]:

**Minimize**: E[Cost] = Co·P(Sell=1|φ)·P(Deliver=0|φ) + Cu·P(Sell=0|φ)

Where:
- P(Sell=1|φ) = φ (sellability increases with promise ambition)
- P(Deliver=1|φ) = 1-φ (deliverability decreases with promise ambition)

Substituting these probability functions:

E[Cost] = Co·φ·φ + Cu·(1-φ) = Co·φ² + Cu·(1-φ)

### 3.2 Linear Model with Match Value

Generating insights through first-order conditions:

dE[Cost]/dφ = 2Co·φ - Cu = 0

Therefore: φ* = Cu/(2Co)

Gaining realism by incorporating value V when promises successfully match delivery transforms the analysis. The complete objective function becomes:

E[Net Cost] = Co·φ² + Cu·(1-φ) - V·φ·(1-φ) (1)

The third term captures match value: revenue earned when customer buys (probability φ) AND partner delivers (probability 1-φ).

Taking the first-order condition:

dE[Net Cost]/dφ = 2Co·φ - Cu - V(1-2φ) = 0

Solving for optimal promise level:

φ* = (Cu + V)/(2Co + 2V)

Governing entrepreneurial behavior, this closed-form solution reveals the cost-priority principle: optimal promise level increases with underpromise cost Cu while decreases with overpromise cost Co. When match value is large V >> Co, Cu, optimal promise level φ* converge to .5 implying a balance between selling and delivering. In fact this can be derived without solving for φ* as the probability for matching and selling the promise is maximized when φ = .5 (see φ·(1-φ) from (1)).

### 3.3 Sigmoid Response Functions (need recalculation)

Generalizing beyond linear probability functions P(Sell|φ) = φ captures realistic stakeholder psychology. Real customers exhibit threshold effects: indifference below φ₀, enthusiasm above φ₁. Similarly, partners show commitment cliffs when promises exceed capabilities.

We generalize to sigmoid response functions:

P(Sell|φ) = 1/(1 + e^(-βc(φ-0.5)))
P(Deliver|φ) = 1/(1 + e^(βr(φ-0.5)))

Where βc and βr control response steepness. Larger β creates sharper transitions between rejection and acceptance.

Gauging different quality sensitivities reveals stakeholder heterogeneity. Tech-savvy early adopters (large βc) react dramatically to feature improvements. Conservative partners (small βr) change gradually. This asymmetry can override cost considerations.

### 3.4 Temporal Dynamics and Strategic Implications

Governing temporal effects, differential cost timing creates systematic biases. Underpromise cost Cu strikes immediately when customers ignore modest promises. Overpromise cost Co arrives later when delivery fails, discounted by factor δ^T:

φ*(t) = Cu/(2Co·δ^T)

As time horizon T increases, δ^T decreases, raising φ*. Longer development timelines systematically favor bolder promises—a mathematical explanation for why breakthrough innovations require patient capital.

Guiding strategic decisions, the model prescribes context-specific promise levels:

**Case 1: Early-stage ventures (Cu >> Co)**
Underpromise cost dominates when unfunded ideas represent massive foregone opportunities. With Cu = $10M potential and Co = $100K reputation risk, φ* ≈ 1 prescribes maximum ambition.

**Case 2: Mature ventures (Co >> Cu)**  
Overpromise cost dominates when established firms risk accumulated brand value. With Co = $1B reputation and Cu = $10M opportunity, φ* ≈ 0 prescribes conservative promises.

**Case 3: Balanced ventures (Cu ≈ Co)**
Equal costs yield φ* = 0.5, prescribing moderate promises that balance market excitement against delivery risk.

## 4. Discussion and Implications

### 4.1 Temporal Reversal: When Capability Precedes Customers

Challenging our promise-then-deliver framework, certain contexts exhibit "deliver-then-sell" dynamics where capability development precedes market creation. Deep tech ventures developing fundamental technologies (quantum computing, fusion energy, CRISPR) often achieve technical breakthroughs before identifying commercial applications. Here, the optimization inverts: minimize the salvage cost of unutilized capability while searching for market fit.

Consider pharmaceutical development where compounds exist before diseases are targetable, or Bell Labs' transistor invention preceding its market applications by decades. These scenarios require a dual-phase model: Phase 1 optimizes capability development under technical uncertainty, Phase 2 optimizes promise calibration given existing capabilities. The salvage cost of "delivered but unsold" capability—unutilized patents, idle manufacturing capacity, stranded R&D investments—becomes the primary loss function.

Critical insight: The promise vendor framework assumes customer pull dominates technology push. When reversed, entrepreneurs face a fundamentally different optimization—not "what should we promise?" but "what can we promise given what we've built?" This capability-first pathway explains why technical founders often struggle with commercialization: they optimize for deliverability (1-φ) rather than sellability (φ), systematically under-promising relative to their capabilities. Future work should develop a unified framework encompassing both promise-first and capability-first innovation pathways.

### 4.2 Cost Architecture: Who Sets Parameters and Why

Constructing entrepreneurial ecosystems requires understanding how society shapes the cost parameters (Cu, Co, V) that drive promise decisions. These parameters emerge from multiple actors with conflicting objectives: entrepreneurs maximize personal returns, investors seek portfolio performance, regulators protect consumers, and society desires innovation with minimal negative externalities.

Consider how different institutional designs create distinct parameter regimes. Silicon Valley's ecosystem minimizes Co through forgiving bankruptcy laws, normalized failure narratives, and rapid re-employment opportunities—enabling bold promises. Conversely, German Mittelstand culture amplifies Co through reputational permanence and community accountability, favoring incremental innovation. Singapore manipulates V through generous R&D tax credits and innovation prizes, while maintaining moderate Co through efficient courts that swiftly resolve commercial disputes.

Critical design principles emerge: (1) **Asymmetry preservation**—maintaining Cu > Co ensures entrepreneurial dynamism; (2) **Dynamic calibration**—parameters should evolve with venture maturity to prevent excessive risk-taking by established firms; (3) **Stakeholder alignment**—V should incorporate social returns beyond private gains. Society faces a fundamental tradeoff: lower Co encourages breakthrough innovation but enables fraud (Theranos), while higher Co ensures accountability but stifles transformation. Optimal parameter design likely requires sector-specific calibration—low Co for software where failure costs are contained, high Co for biotech where lives are at stake.

### 4.3 Catastrophic Uncertainty: When Promise Spaces Collapse

Catastrophic events—COVID-19, financial crises, wars, AI breakthroughs—fundamentally redefine the promise landscape by simultaneously shifting customer needs and delivery capabilities. Our model assumes stable probability functions P(Sell|φ) and P(Deliver|φ), but catastrophes create discontinuous jumps where entire promise categories become obsolete (travel during COVID) or suddenly viable (remote work technologies).

Consider three catastrophe types and their effects on promise optimization. **Demand shocks** (COVID lockdowns) instantly reset P(Sell|φ) functions—promises of "premium dining experiences" became unsellable overnight while "contactless delivery" surged. **Supply shocks** (chip shortages, war disruptions) collapse P(Deliver|φ) across entire sectors, forcing mass promise recalibration. **Paradigm shifts** (ChatGPT's emergence) create new promise dimensions previously unconsidered—suddenly every software company could promise "AI-powered" features.

Critical modeling challenges emerge: (1) **Non-stationarity**—parameters Cu, Co, V become time-varying stochastic processes rather than constants; (2) **Correlation breakdown**—previously independent stakeholder responses become highly correlated during crises; (3) **Option value**—maintaining promise flexibility gains importance relative to optimization. Catastrophic uncertainty suggests entrepreneurs should optimize for adaptability rather than specific promise levels. Future work must develop robust optimization techniques that perform well across multiple regime shifts, potentially using scenario planning or real options frameworks to value promise flexibility during turbulent periods.

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
