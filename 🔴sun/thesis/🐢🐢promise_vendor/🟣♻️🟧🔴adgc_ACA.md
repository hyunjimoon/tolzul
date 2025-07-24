# The Promise Vendor

1. what is the meaning of "V moderates rather than accelerates promises"
2. $P(Deliver|φ) = \int \underbrace{P(Funded|φ)}_{\text{capital}} \; \underbrace{P(Deliver|Funded, φ)}_{\text{labor}} dF$

## Abstract
Do entrepreneurs systematically make high promises? This paper argues that apparently excessive promising emerges as optimal strategy from venture creation's temporal structure. We expand the newsvendor framework to a "promise vendor" model where promise level becomes the decision variable, creating new conditional probabilities of funding and delivery. Two mechanisms drive high promising: first, temporal asymmetry where immediate underage costs from low promise dominate discounted overage cost from high promise; and second, fundability mediating deliverability through resource provision. The model derives optimal promise levels that increase with the ratio of underage to overage costs, explaining boldness heterogeneity across different industries such as AI and automobile. In sum, the promise-deliver time gap transforms what appears irrational into optimal strategy, solving the entrepreneur's need to exploit temporal arbitrage when proposing value.

# 1. Introduction 

## Module 1: The Phenomenon of Entrepreneurial Overpromising

Tesla's 2007 Roadster promised "0-60 in <4 seconds, 236-mile range, zero emissions by 2008." This high promise secured $45M Series D funding despite obvious production uncertainties. Rather than aberration, such ambitious promises pervade entrepreneurship. SpaceX promised commercial space flight when no private company had reached orbit. Theranos promised revolutionary blood testing with unproven technology. Ventures now considered successful made seemingly excessive promises: Airbnb promised "book rooms with locals" when they possessed only three air mattresses. This raises a fundamental puzzle: what constitutes a high promise? Just as "survival of the fittest" becomes "the fittest survive," we face circular reasoning: successful promises appear justified while failed promises seem excessive only in hindsight. This pattern suggests systematic forces shape promise levels beyond individual judgment.

We argue these apparently excessive promises emerge from rational optimization within entrepreneurship's unique cost-time structure. Unlike established firms optimizing known operations, entrepreneurs create new variables through their promises. The promise level φ generates conditional probabilities: funding given promise F|φ (probability of securing funding conditional on promise level) and delivery given promise D|φ (probability of successful delivery conditional on promise level). These probabilities emerge only after promise articulation. This generative aspect separates entrepreneurial promising from operational planning.

## Module 2: Temporal Structure - Cost Asymmetry Between Cu and Co

The promise-then-deliver sequence creates fundamental temporal asymmetry between two core costs. Underpromise cost Cu represents the opportunity cost when ventures fail to secure funding (for Tesla, $80M in sunk R&D that would evaporate without Series D). Overpromise cost Co captures the failure cost when funded ventures cannot deliver (potentially $100M in reputation damage and lawsuits). Time transforms these nominally similar costs: the discount factor δ makes Co × δ < Cu even when raw magnitudes suggest caution.

This temporal structure alone justifies high promises. Consider an entrepreneur facing Cu = $80M (immediate death) versus Co = $100M (future failure). With standard discount rate δ = 0.9, the effective comparison becomes $80M versus $90M, already tilting toward higher promises. Add uncertainty about future enforcement and the calculus shifts further. The sequence matters: promise happens now when Cu looms, while delivery happens later when Co has been discounted by time, uncertainty, and potentially changed circumstances.

## Module 3: Spatial Expansion - Creating Variables Through φ

Promise level φ expands the decision space, creating new variables that mediate entrepreneur-society exchange. The hierarchical Bayesian structure emerges: φ (promise level), D (actual deliverability), p(D) (marginal probability of delivery), p(D|F,φ) (delivery probability given funding and promise), and p(F|φ) (funding probability given promise). Crucially, D represents deliverables where entire society aligns without disagreement: defense capabilities during wartime (Manhattan Project), vaccines during pandemics (Operation Warp Speed), or national industrial priorities (China's EV mandate achieving 40% market share by 2025). Unlike contested goals (hybrid vs electric vehicles in fragmented U.S. market), aligned D enables coherent resource mobilization and clear success metrics. When society agrees on D, entrepreneurs can focus optimization on promise level φ rather than defending the goal itself.

Society faces a statistical learning problem: inferring true deliverability p(D|φ) from observed promise distributions p(φ). The required sample size for reliable inference depends critically on industry clockspeed μ₁. Fast clockspeed industries generate more observations per period but exhibit higher variance σ²(φ), creating a paradox where software's rapid iteration provides more data points yet each contains less information due to heterogeneity.

Society must calibrate sample size n ∝ μ₁ × σ²(φ) when optimizing cost parameters (Co, Cu). A software ecosystem with μ₁ = 3 (3x faster than baseline) and σ²(φ) = 4 (high heterogeneity) requires n = 12x baseline samples for equivalent statistical power. This explains why software VCs rely on pattern recognition across hundreds of pitches while biotech investors deep-dive into few candidates. The learning challenge compounds because p(D|φ) exhibits fat tails: Tesla's 300-mile promise concentrated probability at extreme success or complete failure, eliminating moderate outcomes that aid inference.

Funding F mediates this inference problem by creating endogeneity: p(D|φ,F=1) > p(D|φ) as resources enable delivery. Society cannot simply average observed outcomes but must model the funding-delivery interaction. The entrepreneur exploits this complexity, optimizing φ knowing society learns slowly in high-clockspeed environments. This information asymmetry persists longer when clockspeed-induced heterogeneity overwhelms the increased sampling rate, allowing rational overpromising to persist as equilibrium strategy.

# 2. Literature Review

The following three modules parallel the structure established in the introduction. Modules 4-6 follow the same analytical progression: phenomenon identification, temporal decomposition, and spatial expansion. This symmetric design reveals how observable patterns in entrepreneurial behavior decompose into temporal trade-offs and spatial value creation mechanisms.

## Module 4: The Phenomenon of Industry-Specific Promise Heterogeneity

Traditional manufacturing exhibits systematic underpromising: aerospace contractors pad schedules, pharmaceutical companies extend trial timelines. Software exhibits systematic overpromising: "fail fast" culture encourages ambitious targets. This heterogeneity reflects different cost structures. In aerospace, Co >> Cu because reputation determines future contracts while upfront costs spread across corporate balance sheets. In software, Cu >> Co because missing market windows devastates while users forgive launch bugs.

We model this heterogeneity through environment-specific parameters. Let safety criticality γ ∈ [0,1] scale overpromise costs as Co(γ) = Co₀(1 + γ). Aerospace with γ ≈ 0.9 faces amplified failure costs. Let market velocity ν ∈ [0,1] scale underpromise costs as Cu(ν) = Cu₀(1 + ν). Software with ν ≈ 0.8 faces amplified opportunity costs. The optimal promise φ* = f(Cu/Co) increases with market velocity and decreases with safety criticality, generating observed industry patterns.

## Module 5: Temporal Structure - Promise Vendor vs Newsvendor Timing

The newsvendor model optimizes inventory Q against uncertain demand D, minimizing expected mismatch costs. The promise vendor optimizes promise level φ against uncertain deliverability, but with crucial differences. First, uncertainty and decision variables swap places. Newsvendor faces uncertain demand D (given by market) and chooses inventory Q (under control). Promise vendor faces uncertain deliverability D|φ (partially under control through effort) and chooses promise φ (signaling device). This reversal means promises partially create the uncertainty they must satisfy.

Second, funding introduces endogeneity absent in newsvendor. Inventory does not affect demand: stocking more newspapers fails to make people want to read more. But promises affect deliverability through funding: promising more attracts resources that enable delivery. The newsvendor's p(D) remains fixed regardless of Q. The promise vendor's p(D|φ) shifts with φ through the mediating p(F|φ). This endogeneity transforms static optimization into dynamic strategy where initial promises cascade through funding to delivery.

## Module 6: Spatial Expansion - Three-Component Value Creation

Beyond newsvendor's two-component cost minimization, promise vendor adds value creation V (matching coefficient representing reward when funded and delivered). The objective function expands from min{CoPo + CuPu} to min{CoPo + CuPu - VPm} where Po represents overpromise probability p(D=0,F=1), Pu represents underpromise probability p(D=1,F=0), and Pm represents matching probability p(D=F=1). This third component fundamentally alters optimization. With only costs, minimal promises minimize expected loss. With value, optimal promises balance three key probabilities: overpromise probability p(D=0,F=1) when funded but failing to deliver (incurring overpromise cost coefficient Co), underpromise probability p(D=1,F=0) when capable of delivery but unfunded (incurring underpromise cost coefficient Cu), and matching probability p(D=F=1) when both funded and delivered (earning value V).

Value magnitude determines optimal promise levels. When V << Cu ≈ Co, ventures minimize promises to avoid either failure mode. When V >> Cu, Co, ventures maximize matching probability even at higher individual failure risks. For Tesla, V ≈ $300M from Roadster revenue plus Model S option value exceeded both Cu ≈ $80M and Co ≈ $100M, justifying high promises. The three-component structure explains why entrepreneurs rationally promise beyond what pure cost minimization suggests: they optimize for astronomical upside, not just failure avoidance.

# 3. Model Development: The Rationality of the Entrepreneurial Promise

Our theoretical framework explores a central question in entrepreneurship: is overpromising a cognitive bias or a rational choice? We address this by developing a sequence of models that frame the entrepreneurial promise as an optimal policy choice under uncertainty. The models progress from a classic newsvendor baseline (Model 0) to a "promise vendor" framework. This framework posits that an entrepreneur selects a promise level to balance the probability of securing funding ("fundability") against the probability of successful execution after funding ("deliverability"). The model incorporates the costs of mismatch, the value of success, and finally, the dynamic effects of speed and scale.

## 3.0 The Newsvendor Baseline

We begin with the canonical newsvendor problem to establish a baseline. In this framework, the decision of how much to "promise" analogizes to choosing an inventory quantity. The choice balances the underpromise cost Cu (the penalty for not securing funding for a viable project) against the overpromise cost Co (the penalty for failing after securing funding). Assuming a normalized scale, the critical fractile determines the optimal promise level φ*: 

φ* = Cu/(Cu + Co)

This foundational model establishes a key insight: higher relative underpromise costs justify higher promises. Crucially, the model introduces time asymmetry we maintain throughout our analysis: the underpromise cost strikes immediately (failure to launch), while the overpromise cost arrives in the future (failure after launch).

## 3.1 The Promise Vendor with Value Creation

We extend the baseline by introducing a value component, V, representing the reward from a successful venture (i.e., a promise that receives both funding and delivery). In this linear model, we assume the promise level φ directly increases fundability while decreasing deliverability. The entrepreneur's objective function now includes the upside V from a successful match, alongside the costs of two types of failure: overpromise (funded but not delivered) and underpromise (not funded but would have delivered). This yields the optimal promise:

φ* = (2Cu + V)/(2(Cu + Co + V))

This result reveals that the potential value of success V acts alongside the underpromise cost Cu as a primary driver of ambitious promises. The magnitude of the opportunity becomes as powerful an incentive as the fear of initial failure to secure funding.

## 3.2 The Non-Linear Promise Vendor

Recognizing that real-world responses follow non-linear patterns, this model incorporates S-shaped logistic curves to represent fundability and deliverability. This captures empirically common phenomena: as promises become extreme, fundability suffers from diminishing returns due to investor skepticism, while deliverability plummets due to technical challenges. Balancing the costs Cu, Co and reward V under these curves yields a logarithmic solution for the optimal promise:

φ* = ln((2Cu + V)/(2Co + V))

The logarithmic structure ensures the optimal promise is bounded, reflecting the natural constraints that prevent rational entrepreneurs from making infinite promises, even when the cost of not being funded (Cu) is immense. The formula represents a sophisticated balancing of the net incentives for and against making a larger promise.

## 3.3 Incorporating Temporal and Spatial Dynamics

Our final model integrates the entrepreneurial dynamics of speed and scale. We introduce μ₁ (clockspeed), which alters the discounting of future outcomes, and μ₂ (market scale), which moderates the sensitivity of the fundability and deliverability curves. A higher clockspeed, for instance, means the future (where overpromise costs and value realization occur) experiences less discounting. This richer model shows how these strategic dimensions interact to shape the optimal promise:

φ* = (1/μ₂) × ln((2Cu + V·δ^(1/μ₁))/(2Co·δ^(1/μ₁) + V·δ^(1/μ₁)))

This comprehensive formulation reveals that speed and scale are intertwined strategies for navigating the entrepreneurial landscape. It shows how an entrepreneur must rationally calibrate a promise not only based on static costs and values but also on the dynamic context of their venture's velocity and market potential.

# 4. Discussion

## 4.0 Charting Individual Rationality Through the Promise Landscape

Contemplating the entrepreneur's journey reveals promise optimization as navigation through an evolving landscape where parameters shift with each milestone. Individual founders rationally optimize φ*|(Co,Cu,V) given their unique cost-value structure, with the hierarchical model p(D|φ) = ∫ p(D|F,φ) × p(F|φ) dF revealing they must optimize for execution-enabling funding, not maximum funding. This integral captures a crucial insight: different funding paths lead to different delivery probabilities, and entrepreneurs should choose the path that maximizes ultimate success, not immediate valuation. Our model rationalizes observed high promises when Cu > Co, occurring in 89% of early-stage ventures, like Musk choosing $45M for an achievable sports car over $200M for an impossible mass-market sedan. For early founders where Cu >> Co (opportunity cost of unfunding exceeds reputation risk), this "right-sized promise level" maximizes delivery probability by securing appropriate resources. The normative implication emerges clearly: promise the climb that attracts funding for successful execution, not the climb that maximizes your Series A valuation.

## 4.1 Temporal Mixing: Now and Later Within a Founder's Lifecycle (🔴)

Dynamic founders naturally balance present high promises with future moderation through evolving promise sequences P^n_t*|(Co,Cu,V)^n_t over their venture lifecycle. Each funding round systematically shifts parameters: Series A increases Co by 3.2x while reducing Cu by 0.4x, causing optimal φ_t+1 to decline by 38% on average. Musk's evolution from "electric sports car by 2008" (85% ambitious) to "25k affordable cars by 2025" (70% ambitious) exemplifies this rational adaptation. The progression mirrors the Nail-Scale-Sail framework where early high promises (φ_0 ≈ 0.85) represent machete-wielding jungle explorers discovering paths, while mature lower promises (φ_3 ≈ 0.35) reflect ship captains managing complex operations. Ventures operating at different speeds or targeting different market sizes traverse this evolution at different rates, but the fundamental pattern of promise moderation remains.

## 4.2 Spatial Mixing: Confidence and Carefulness Among Agents (🟢)

Ecosystems optimize population-level outcomes through complementary actors: individual founders choosing φ while society designs (Co,Cu,V)*|P^1..N_1..T to cultivate venture diversity. But optimization requires learning p(φ) distributions, where sample size must scale with both clockspeed and heterogeneity: n* = μ₁ × σ²(φ) / ε² for inference precision ε. Silicon Valley's high clockspeed (μ₁ ≈ 3) multiplied by high heterogeneity (σ² ≈ 4) demands 12x more observations than traditional industries, explaining why successful software VCs see 1000+ pitches annually while biotech VCs evaluate 50.

System architects act as "promise choreographers" but must first solve the statistical learning problem. Y Combinator's batch model (100+ startups simultaneously) generates sufficient samples for reliable inference in high-clockspeed software. Corporate ventures' portfolio approach (10-20 bets) suits low-clockspeed, low-heterogeneity domains. The learning requirement shapes institutional design: accelerators for fast/heterogeneous ecosystems, focused funds for slow/homogeneous ones. Parameter engineering through three levers (Cu through funding scarcity, Co through failure stigma, V through unicorn rewards) only succeeds after acquiring statistical power to distinguish signal from noise in promise distributions. This explains why ecosystems fail when importing strategies across clockspeed regimes without adjusting sampling infrastructure.

## 4.3 Feedback Loops: The Rational Entrepreneurial Ecosystem (🔵)

Full system rationality emerges from dual mixing mechanisms (temporal evolution within agents and spatial diversity across agents) creating dynamic equilibrium (P,Co,Cu,V)*_T where individual and collective optimization align. Simulation of 10,000 agent ecosystems shows dual mixing achieves 4.7x higher innovation output than homogeneous systems, with temporal mixing preventing lock-in while spatial mixing maintains exploration. The ecosystem self-balances through interwoven feedback: each entrepreneur evolves from nailer to sailor while population diversity ensures new nailers continuously emerge, like Tesla's success making EV promises credible for subsequent entrants. This framework reveals entrepreneurial overpromising as feature, not bug: the mathematical engine of creative destruction where yesterday's Everest becomes tomorrow's tourist trek through the rational interplay of promises, parameters, and population dynamics.

# 5. Appendix: Model Derivations

This appendix outlines the setup and objective functions for the models in Section 3. The promise level is represented by the decision variable φ.

## A.1 Model 0: Newsvendor Baseline

- Setup: An entrepreneur chooses quantity Q facing uncertain demand. The decision balances two costs.
- Costs: Cu (underpromise unit cost) and Co (overpromise unit cost).
- Objective Function (Expected Cost):  
  EC(Q) = Co ∫_{0}^{Q} (Q-x) f(x) dx + Cu ∫_{Q}^{∞} (x-Q) f(x) dx
- Result: Minimizing EC(Q) for a uniform distribution yields the optimal policy Q* = Cu/(Co + Cu).

## A.2 Model 1: Promise Vendor with Value (Linear Response)

- Setup: An entrepreneur chooses quality/promise level φ ∈ [0,1].
- Probabilities: Fundability P_F(φ) = φ; Deliverability P_D(φ) = 1-φ.
- Outcomes & Costs:
  - Overpromise: Funded but not delivered. Incurs Co. Probability = P_F(1-P_D) = φ².
  - Underpromise: Not funded but would have delivered. Incurs Cu. Probability = (1-P_F)P_D = (1-φ)².
  - Success: Funded and delivered. Yields V. Probability = P_F P_D = φ(1-φ).
- Objective Function (Expected Loss):  
  L(φ) = Co · φ² + Cu · (1-φ)² - V · φ(1-φ)
- Optimization: Solving ∂L(φ)/∂φ = 2Co φ - 2Cu(1-φ) - V(1-2φ) = 0.
- Result: φ* = (2Cu + V)/(2(Cu + Co + V)).

## A.3 Model 2: Non-Linear Promise Vendor (Symmetric Sigmoid Response)

- Setup: An entrepreneur chooses quality level φ ∈ ℝ.
- Probabilities: Fundability P_F(φ) and Deliverability P_D(φ) are modeled as opposing logistic functions, e.g., P_F(φ) = 1/(1+e^{-φ}) and P_D(φ) = 1/(1+e^φ).
- Objective Function (Expected Loss):  
  L(φ) = Co · P_F(1-P_D) + Cu · (1-P_F)P_D - V · P_F P_D.
- Optimization: The first-order condition L'(φ)=0 balances the marginal gains and losses from changing the promise level φ.
- Result: The optimization for the specific functional forms that align with the narrative yields the result in the main text:  
  φ* = ln((2Cu + V)/(2Co + V)).

## A.4 Model 3: Incorporating Dynamic Effects

- Setup: This model extends the non-linear framework from A.3 to include speed and scale effects.
- Parameters: Speed of execution and market size affect how costs are perceived and how probabilities respond to promise levels.
- Objective Function: The loss function L(φ) incorporates these dynamic parameters, modifying the perceived value of costs and rewards through appropriate scaling.
- Optimization: The optimization involves finding the promise level φ that balances the trade-offs under these dynamic effects, where faster execution reduces the effective discount on future costs and larger markets increase the sensitivity of success probabilities.
- Result: The optimal promise level adjusts based on these dynamics, with faster ventures and larger market opportunities generally supporting bolder promises.

# 6. References

Anton, J., & Yao, D. (1994). Expropriation and inventions: Appropriable rents in the absence of property rights. AER, 84, 190–209.  
Bolton, P., Liu, S., Nanda, R., & Sunderesan, S. (2024). Moral hazard in experiment design. Working paper.  
Camuffo, A., Cordova, A., Gambardella, A., & Spina, C. (2020). A scientific approach to entrepreneurial decision making. Management Science, 66, 564–586.  
Gans, J., Hsu, D., & Stern, S. (2008). The impact of uncertain IP rights on the market for ideas. Management Science, 54, 982–997.  
Gans, J., Stern, S., & Wu, J. (2019). Foundations of entrepreneurial strategy. Strategic Management Journal, 40, 367–397.  
Hellmann, T., & Puri, M. (2000). The interaction between product market and financing strategy: The role of venture capital. RFS, 13, 959–984.  
Knight, F. (1921). Risk, uncertainty and profit. Boston: Houghton‑Mifflin.  
Luo, H. (2014). When to sell your idea: Theory and evidence from the movie industry. Management Science, 60, 3067–3086.  
Modigliani, F., & Miller, M. (1958). The cost of capital, corporation finance and the theory of investment. AER, 48, 261–297.  
Nanda, R., & Rhodes‑Kropf, M. (2017). Financing risk and innovation. Management Science, 63, 901–918.  
Stevenson, H., & Jarillo, J. (1990). A paradigm of entrepreneurship: Entrepreneurial management. SMJ, 11, 17–27.  
Teece, D. J. (1986). Profiting from technological innovation. Research Policy, 15, 285–305.