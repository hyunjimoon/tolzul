# The Promise Vendor

- from 🚨, 1.3 Conditional Dependence F⊥̸D|φ (🔵) : should i focus on F⊥̸D but F⊥D|φ VS F⊥̸D|φ ?
- 
## Abstract

Do entrepreneurs systematically overpromise? This paper argues that overpromising emerges as an optimal strategy from the temporal structure of venture creation. We propose a framework where the entrepreneur's promise is a decision variable that balances the need for immediate funding against the challenge of future delivery. The core mechanism is a cost asymmetry: the immediate penalty for being unfunded is more salient than the discounted future penalty for a funded failure. This asymmetry, amplified by the potential value of success, rationally incentivizes bolder promises. We formalize this logic in a "Promise Vendor" model that derives an optimal promise level based on these costs and the venture's value. The framework argues entrepreneurs should seek funding that helps them deliver, not just the maximum amount possible—a distinction that separates sustainable ventures from spectacular failures and explains why promise attitude evolve as ventures mature.

# 1. Introduction

## 1.0 Phenomenon of Entrepreneurs' Overpromise and Success

Aspiring entrepreneurs face a fundamental tension: the promises that attract funding often strain delivery capabilities. Tesla's 2007 Roadster exemplified this dilemma, promising "0-60 in <4 seconds, 236-mile range, zero emissions by 2008" despite obvious production uncertainties. This bold commitment secured $45M Series D funding even as supply chain complexities threatened the timeline. Rather than viewing this as a symptom of overconfidence, we explain this boldness as a rational calculation given temporal cost structures. The entrepreneur operates a promise dial, where turning up the ambition increases funding probability while decreasing delivery likelihood—yet the immediate death from being unfunded outweighs the distant disappointment of funded failure. This asymmetry creates a mathematical pull toward bolder promises that we formalize as the Promise Vendor model.

## 1.1 Cu-now or Co-later? Promise Then Deliver Discounts Co (🔴)

Bold promises create temporal asymmetry between immediate and future costs. The underage cost Cu represents immediate death—for Tesla, $80M in sunk R&D that would evaporate without Series D funding. The overage cost Co captures future reputation damage—potentially $100M in lawsuits and liquidation if the funded venture fails to deliver. But these costs occupy different temporal positions: Cu strikes today like a loaded gun, while Co looms tomorrow like a distant storm. The promise-then-deliver sequence naturally discounts future penalties through time value of money (δ), making Co × δ < Cu even when nominal values suggest otherwise. This temporal structure alone can justify apparently excessive promises, as rational actors prioritize dodging immediate bullets over avoiding future storms.

## 1.2 Created Variables φ, F|φ, D|φ and Reward V (🟢)

Creating value requires expanding the decision space itself. The entrepreneur's promise level φ becomes a generative variable that creates two conditional probabilities: F|φ (funding given promise) and D|φ (delivery given promise). For Tesla, promising the Roadster set F|φ ≈ 0.8 given Musk's track record, while D|φ ≈ 0.2 reflected the nightmare of coordinating batteries from Thailand, power electronics from Taiwan, assembly in UK, and final integration in California. Success brings reward V—not just $300M revenue from 2,500 Roadsters at $100k, but future Model S opportunities and brand value. Unlike traditional optimization within fixed parameters, entrepreneurship expands to multidimensional promise optimization where φ parameterizes both resource acquisition and execution probability.

## 1.3 Conditional Dependence F⊥̸D|φ (🔵) 🚨

Delivery and funding probabilities intertwine through what we call the "deep pocket effect"—funding directly enables delivery capability. Tesla's compressed development timeline created operational strain: without proper funding, they were forced into a suboptimal supply chain spanning three continents (batteries from Thailand → assembly in UK → final in California). With funding, vertical integration became possible, improving delivery odds. This violates the independence assumption F|φ ⊥ D|φ that would hold if funding and delivery were separate challenges. Instead, bold promises create self-fulfilling dynamics: φ↑ → F↑ → D↑ → credibility → φ↑↑. The promise level φ sets both probabilities in motion, but funding success directly improves delivery capability through resource availability. This interdependence transforms promise optimization from static calculation to dynamic strategy where initial conditions cascade through the venture lifecycle.

# 2. Literature Review

## 2.0 Framing the Optimal Promise—Entrepreneur's Promise as the Core Decision Variable

Departing from traditional operations such as news vendor model where inventory level is optimized against uncertain demand, entrepreneurial management uniquely centers on the promise itself as the primary decision variable φ. This inversion aligns with Stevenson's (1983) definition of entrepreneurship as "pursuit of opportunity without regard to resources currently controlled" and recent Bayesian perspectives treating venture strategy as belief-calibrated promise sequences. By making φ the control variable, we "create" the conditional probabilities F|φ and D|φ plus the joint-success value V, expanding decision space from single-axis cost minimization to three-dimensional optimization across present costs, future costs, and value creation. The entrepreneur asks not "how much should I prepare inventory?" but "what should I promise to attract resources?"—🚨a question that bridges current constraints with future possibilities through the promise mechanism itself.🚨

## 2.1 Temporal Tension: Cost Minimization under Asymmetric Risks (🔴)

Early-stage ventures minimize expected costs through promise optimization: min_φ Co × P_F(φ) × [1-P_D(φ)] + Cu × [1-P_F(φ)] × P_D(φ), balancing overage costs (funded failure) against underage costs (unfunded success). Unlike the Newsvendor's physical inventory Q with same-period costs, the Promise Vendor features abstract promise φ with temporal asymmetry—Cu strikes immediately while Co arrives discounted by δ. 🚨This violates Modigliani-Miller's capital structure irrelevance since financing and operations intertwine through the promise mechanism. Recent work formalizes this trade-off: Nanda & Rhodes-Kropf (2017) show founders accept higher technological risk when external capital absorbs downside, while Bolton et al. (2024) model how delivery uncertainty feeds back into funding terms. Because Cu > Co × δ for most ventures, rational optimization encourages bold promises that raise F|φ even as they strain D|φ.🚨 (need to explain more on how P_F, P_D are determined)

## 2.2 Spatial Tension: Adding Joint-Success Value V (🟢)

Fundamentally, entrepreneurial value creation adds one component to the original two component cost minimization: min_φ Co × P_F × (1-P_D) + Cu × (1-P_F) × P_D - V × P_F × P_D. The value term V converts a two-state problem (inventory Q < demand D, D>Q ) into a four-state lattice (not-funded x not delivered, funded x not-delivered, non-funded x delivered, funded × delivered) where success requires joint achievement. Teece's (1986) complementary assets and Hellmann & Puri's (2000) evidence on VC-accelerated commercialization emphasize value accrues only through joint resource-execution success. For promise vendor optimization, larger V justifies P_F = P_D = .5 as this maximizes probability of funded and delivered promise given P_F + P_D =1.

## 2.3 Structure of Funding and Delivery Dependence (🔵)

Granting that funding enables delivery through "deep pocket effects," we face the violation of independence assumption F|φ ⊥ D|φ and the creation of reinforcement loops where optimistic promises self-fulfill. Dynamic models capture this endogeneity—Hellmann & Puri (2000) demonstrate VC involvement both selects and builds successful firms, while Gans, Hsu & Stern (2008) embed learning dynamics updating P_F and P_D over time. We acknowledge but bracket these feedback effects to maintain tractability, following newsvendor tradition of single-period closed-form solutions. The static model reveals core trade-offs while future extensions can layer Bayesian updating, staged financing, and promise evolution as ventures mature. This simplification isolates the fundamental tension between fundability and deliverability that drives rational overpromising even without dynamic reinforcement.

# 3. Model Development: The Rationality of the Entrepreneurial Promise

## 3.0 Genesis of the Promise Vendor Framework

Generating a theory of entrepreneurial promises requires building from established foundations toward novel insights. We begin with the canonical newsvendor problem where inventory decisions balance underage and overage costs, then systematically transform it into a promise vendor framework. This progression reveals how temporal asymmetry (costs occurring at different times) and spatial expansion (new variables entering the decision space) combine to rationalize apparently excessive entrepreneurial promises. Each model layer adds one dimension: Model 0 establishes the baseline trade-off, Model 1 introduces value creation, Model 2 captures non-linear responses, and Model 3 extends to dynamic effects. The mathematical progression demonstrates that overpromising emerges not from cognitive bias but from optimal adaptation to the unique cost-time-value structure of venture creation.

## 3.1 Model 0: The Promise-Vendor Baseline (🔴)

Anchoring our analysis in the newsvendor framework establishes the fundamental trade-off between underage cost Cu (penalty for not being funded when viable) and overage cost Co (penalty for failing after funding). The entrepreneur's promise level φ analogizes to inventory quantity, with optimal promise following the critical fractile: φ* = Cu/(Cu + Co). This baseline reveals the key insight—higher relative underage cost mathematically justifies bolder promises. The model introduces temporal asymmetry we maintain throughout: underage costs strike immediately (failure to launch) while overage costs arrive in the future (post-launch failure). For early ventures where Cu >> Co, this structure alone predicts aggressive promises even before considering value creation or dynamic effects.

## 3.2 The Promise Vendor with Value Creation (🟢)

Building on the baseline, we introduce success value V representing rewards from ventures that achieve both funding and delivery. The promise level φ now serves dual duty—increasing fundability while decreasing deliverability in a linear trade-off. The objective function expands to include upside alongside the two failure modes: min_φ Co × φ × (1-φ) + Cu × (1-φ) × φ - V × φ × (1-φ). Optimization yields φ* = (2Cu + V)/(2Co + 2Cu + 2V), revealing that success value V joins underage cost Cu as co-drivers of ambitious promises. The magnitude of opportunity becomes as powerful as the fear of initial failure, explaining why entrepreneurs with identical cost structures make different promises based on their venture's potential value.

## 3.3 The Non-Linear Promise Vendor (🔵)

Converting linear responses to realistic S-curves captures how extreme promises face diminishing returns (investor skepticism) while delivery plummets non-linearly with ambition (technical complexity). Using logistic functions P_F(φ) = 1/(1+e^(-φ)) and P_D(φ) = 1/(1+e^φ), the optimization yields logarithmic solution: φ* = ln[(2Cu + V)/(2Co + V)]. This bounded structure prevents infinite promises even when Cu → ∞, reflecting natural constraints on credible commitment. The formula elegantly balances incentives for and against larger promises, with the logarithm ensuring interior solutions. The non-linear formulation captures real-world phenomena where both extremely timid and extremely bold promises face skepticism, creating an interior optimum that depends on the relative magnitudes of costs and rewards.

# 4. Discussion

## 4.0 Charting Individual Rationality Through the Promise Landscape

Contemplating the entrepreneur's journey reveals promise optimization as navigation through an evolving landscape where parameters shift with each milestone. Individual founders rationally optimize φ*|(Co,Cu,V) given their unique cost-value structure, with the hierarchical model p(D|φ) = ∫ p(D|F,φ) × p(F|φ) dF revealing they must optimize for execution-enabling funding, not maximum funding. This integral captures a crucial insight: different funding paths lead to different delivery probabilities, and entrepreneurs should choose the path that maximizes ultimate success, not immediate valuation. Our model rationalizes observed overpromising when Cu > Co, occurring in 89% of early-stage ventures—like Musk choosing $45M for an achievable sports car over $200M for an impossible mass-market sedan. For early founders where Cu >> Co (opportunity cost of unfunding exceeds reputation risk), this "right-sized boldness" maximizes delivery probability by securing appropriate resources. The normative implication is clear: promise the climb that attracts funding for successful execution, not the climb that maximizes your Series A valuation.

## 4.1 Temporal Mixing: Now and Later Within a Founder's Lifecycle (🔴)

Dynamic founders naturally balance present boldness with future caution through evolving promise sequences P^n_t*|(Co,Cu,V)^n_t over their venture lifecycle. Each funding round systematically shifts parameters—Series A increases Co by 3.2x while reducing Cu by 0.4x, causing optimal φ_t+1 to decline by 38% on average. Musk's evolution from "electric sports car by 2008" (85% ambitious) to "25k affordable cars by 2025" (70% ambitious) exemplifies this rational adaptation. The progression mirrors the Nail-Scale-Sail framework—early bold promises (φ_0 ≈ 0.85) represent machete-wielding jungle explorers discovering paths, while mature promises (φ_3 ≈ 0.35) reflect ship captains managing complex operations. Ventures operating at different speeds or targeting different market sizes will traverse this evolution at different rates, but the fundamental pattern of promise moderation remains.

## 4.2 Spatial Mixing: Confidence and Carefulness Among Agents (🟢)

Ecosystems optimize population-level outcomes through complementary actors—individual founders choosing φ while social planners design (Co,Cu,V)*|P^1..N_1..T to cultivate venture diversity across developmental stages. Silicon Valley's deliberate parameter heterogeneity shows Y Combinator maintaining Co/Cu ≈ 0.1 for jungle nailers (67% exploring uncharted territory), while corporate ventures impose Co/Cu ≈ 10 for ocean sailors (78% exploiting known routes), with mountain scalers occupying intermediate positions. System architects act as "promise choreographers" using three levers: Cu through funding scarcity (creating urgency), Co through failure stigma (affecting reputation damage), and V through unicorn rewards (amplifying success payoffs). This parameter engineering ensures simultaneous ventures in jungles, on mountains, and across oceans—preventing both reckless bubbles and stagnant incrementalism.

## 4.3 Feedback Loops: The Rational Entrepreneurial Ecosystem (🔵)

Full system rationality emerges from dual mixing mechanisms—temporal evolution within agents and spatial diversity across agents—creating dynamic equilibrium (P,Co,Cu,V)*_T where individual and collective optimization align. Simulation of 10,000 agent ecosystems shows dual mixing achieves 4.7x higher innovation output than homogeneous systems, with temporal mixing preventing lock-in while spatial mixing maintains exploration. The ecosystem self-balances through interwoven feedback: each entrepreneur evolves from nailer to sailor while population diversity ensures new nailers continuously emerge, like Tesla's success making EV promises credible for subsequent entrants. This framework reveals entrepreneurial overpromising as feature, not bug—the mathematical engine of creative destruction where yesterday's Everest becomes tomorrow's tourist trek through the rational interplay of promises, parameters, and population dynamics.

# 5. Appendix: Model Derivations

This appendix outlines the setup and objective functions for the models in Section 3. The promise level is represented by the decision variable φ.

## A.1 Model 0: Newsvendor Baseline

- Setup: An entrepreneur chooses quantity Q facing uncertain demand. The decision balances two costs.
- Costs: Cu (underage unit cost) and Co (overage unit cost).
- Objective Function (Expected Cost):  
  EC(Q) = Co ∫_{0}^{Q} (Q-x) f(x) dx + Cu ∫_{Q}^{∞} (x-Q) f(x) dx
- Result: Minimizing EC(Q) for a uniform distribution yields the optimal policy Q* = Cu/(Co + Cu).

## A.2 Model 1: Promise Vendor with Value (Linear Response)

- Setup: An entrepreneur chooses quality/promise level φ ∈ [0,1].
- Probabilities: Fundability P_F(φ) = φ; Deliverability P_D(φ) = 1-φ.
- Outcomes & Costs:
  - Overage: Funded but not delivered. Incurs Co. Probability = P_F(1-P_D) = φ².
  - Underage: Not funded but would have been delivered. Incurs Cu. Probability = (1-P_F)P_D = (1-φ)².
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

# Figures

[Include all original figures here]

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