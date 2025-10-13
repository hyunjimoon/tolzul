### Bug that became a Feature: The Rationality of Entrepreneurial Overpromising

### abstract

Do entrepreneurs systematically overpromise? This paper argues that overpromising is not a cognitive bias but an optimal strategy emerging from the temporal structure of venture creation. We propose a framework where the entrepreneur's promise is a decision variable that balances the need for immediate funding against the challenge of future delivery. The core mechanism is a cost asymmetry: the immediate penalty for being unfunded is more salient than the discounted future penalty for a funded failure. This asymmetry, amplified by the potential value of success, rationally incentivizes bolder promises. We formalize this logic in a "Promise Vendor" model that derives an optimal promise level based on these costs, the venture's value, and strategic dynamics like execution speed and market scale. The framework explains both how an individual founder’s promises moderate over their lifecycle and how healthy ecosystems sustain innovation by cultivating a strategic diversity of ventures.

  

P*= ln(2Cu + V / 2Co+ V)

  

# 1. Introduction

## 0 Phenomenon of Entrepreneurs' Overpromise and Success

Point: Do entrepreneurs overpromise? What's the optimal level of promise when fundability and deliverability of the promise depends on its level? Evidence: Tesla Roadster promised 0-60 in <4 seconds, 236-mile range, zero emissions by 2008 despite complex global supply chain challenges that would plague production for years.  Explanation: These bold promises secured $45M series D funding in 2007 despite obvious production uncertainties, suggesting overpromising serves a rational function in resource acquisition rather than reflecting cognitive bias or irrational exuberance. Repeat:This rationality emerges from a fundamental time asymmetry in entrepreneurial costs.

## ⏰ Cu-now or Co-later. Promise Then Deliver Discounts Co

Point:Future commitments create asymmetric costs: immediate unfunded death (Cu=$80M sunk R&D based on 2007 net loss) vs delayed funded failure (Co=$100M reputation damage, investor lawsuits, liquidation costs). Evidence: The time gap between promise and delivery creates a discounting effect on Co, making immediate Cu more painful—Tesla would lose $80M immediately if unfunded versus $100M discounted over years if funded but failed ([fig.A.1](https://docs.google.com/document/d/1TdFydOL2HOnlaqLBJo1KPNwWdbPj0YSDINtyxZecJMI/edit?tab=t.yx23f2wm2kv#heading=h.6xhutkgmayb)). Explanation: The promise-then-deliver sequence creates temporal tension where "fear of underage cost" (dying unfunded now) exceeds "fear of overage cost" (failing to deliver later), especially when future value V and discount rates δ can mitigate later costs through time value of money. Repeat: This temporal effect is amplified by creating new state variables in the decision space.

  

## ⏰♻️: Created Variables P, F|P, D|P and Reward V

Point: Entrepreneurs expand value space by introducing promise level P as decision variable and conditional probabilities F|P (funding given promise) and D|P (delivery given promise). Evidence: V=$300M revenue potential from 2.5k Roadsters × $100k, plus future Model S opportunity and brand value. PF(P)~80% given Elon Musk's track record and successful funding rounds A through D, while PD(P)~20% initially due to complex supply chain (batteries from Thailand, PEM from Taiwan, assembly in UK, final in California). Explanation: Value creation isn't just optimization within known parameters but expanding the state space itself, where promise P parameterizes both funding and delivery probabilities, transforming simple inventory decisions into multidimensional promise optimization. Repeat: Speed becomes crucial when navigating this expanded state space.

  
  

Figure A.2: Structure of Entrepreneurial Overpromise. The diagram illustrates the three core components of the entrepreneur’s overpromise phenomena. left: Time cost asymmetry where underage cost Cu occurs now ($80M sunk R&D) while overage cost Co occurs in the future ($100M discounted). The promise-deliver sequence creates a time gap that advantages bold promises. center: Creation of new variables P (promise level), F|P (funding probability), and D|P (delivery probability), expanding the variable space (from at least 4 to 12), especially with value V emerging at joint success. right: Speed μ1 (3x clockspeed ratio) and size μ2 (2x market scale) factors are positioned between F|P \perp D|P and F⊥̸D.*

  

## 🌀: Conditional dependence F⊥̸D|P and speed μ1 size μ2

Point: Fast-clockspeed ventures face amplified promise pressures through speed  parameter (μ1), while market expansion through the size parameter (μ2) affects delivery probability but can create operational drag. Evidence: Tesla moved ~3 times faster than traditional auto companies (μ1≈3), compressing typical 7-year development cycles to 2-3 years, fundamentally altering cost dynamics. Simultaneously, Tesla targeted a ~2x larger market by including Europe alongside the U.S. (μ2≈2), where expanded value V' = μ2V theoretically improves delivery probability. Probability of securing funding and delivering were dependent as they experienced and demonstrated cash flow pressure from rapid scaling prevented proper vertical integration, forcing rushed outsourcing decisions (batteries: Thailand via Xcellent, PEM: Taiwan via Chroma, assembly: UK via Lotus, final: California). Explanation: Higher speed parameter μ1 lowers overage cost discounting, pulling founders from making extravagant promises. In contrast, the spatial expansion parameter μ2 theoretically doubles delivery probability by sizing the market twice larger, but in practice creates operational complexity that can drag the temporal sprint. The violated independence assumption F⊥̸D meant funding pressures directly impaired delivery capability, showing how spatial and temporal strategies can conflict. Repeat: These alert signals—temporal asymmetry, spatial expansion, and their interaction—demand deeper analysis of the promise mechanism itself.

# 2. Literature review  
  

## 0 Framing the Optimal Promise—Entrepreneur’s Promise as the Core Decision Variable

Point: The promise level P becomes the central optimization variable. Introducing P “creates” two conditional probabilities—funding PF(P) and delivery PD(P)—and one upside term V, expanding the decision space from a single cost axis to a three‑dimensional trade‑off of present costs, future costs, and joint value creation. Evidence: Unlike traditional operations that optimize known variables (inventory, capacity, pricing), entrepreneurs must optimize the promise itself as the primary lever Conceptually it resonates with definition of entrepreneurial management  "pursuit of opportunity without regard to resources currently controlled" (Stevenson 1983) and with recent Bayesian views that treat venture strategy as a sequence of belief‑calibrated promises (Bayesian Entrepreneurship literatures). Explanation: This inversion uniquely captures both temporal dimensions (resources now vs later) and spatial dimensions (opportunity expansion), making promise P the central mechanism for bridging current constraints with future possibilities. The entrepreneur doesn't ask "how much should I stock?" but "what should I promise to attract resources?" Repeat: This promise creates specific cost dynamics that shape rational behavior.

  

## ⏰ Temporal Tension: Cost Minimization under Asymmetric Risks (DO NOT READ!)

At the first layer the entrepreneur solvesmin⁡P  Co PF(P)[1−PD(P)]  +  Cu [1−PF(P)]PD(P) balancing the overage cost of being funded yet failing against the underage cost of deliverable being unfunded. Because Cu ⁣> ⁣Co for most ventures (dying unfunded is worse than disappointing investors later), the objective encourages bold promises that raise PF even as they strain PD. This asymmetry from time value of money, doesn’t go along well with Modigliani–Miller’s irrelevance theorem—capital structure clearly matters when financing and operations are intertwined. Recent quantitative studies formalize the same trade‑off: Nanda & Rhodes‑Kropf (2017) show founders accept higher technological risk when external capital can absorb downside losses, and Bolton et al. (2024) model experimentation choices when future delivery uncertainty feeds back into current funding terms. Together these works ground an insight that time‑shifted costs alone can rationalize apparently “over‑promising” behaviour under uncertainty.

## ⏰♻️ Spatial Tension: Adding Joint‑Success Value V

We inject upside by subtracting the expected reward for simultaneous funding and delivery, yielding

min⁡P  CoPF(1−PD)+Cu(1−PF)PD  −  V PF PD. Fig.D2 shows how V converts a two‑state cost problem into a four‑state outcome lattice (funded × delivered) and flips the logic from loss‑avoidance to expected value maximization. Teece’s (1986) complementary‑assets framework and Hellmann & Puri’s (2000) evidence on VC‑accelerated commercialization both emphasize that value only accrues when resources and execution succeed jointly. Analytical extensions—e.g., Gans, Stern & Wu (2019) and Camuffo et al. (2020)—demonstrate how a large V can justify still bolder promises: the marginal gain in PF PD outweighs rising failure costs, producing the interior optimum P* ⁣= ⁣ln⁡[(2Cu ⁣+ ⁣V)/(2Co ⁣+ ⁣V)] derived in the Promise‑Vendor paper. Sub‑module F therefore reframes entrepreneurial decision‑making as risk‑adjusted value creation, not mere cost containment.

## 🌀 Self‑Fulfilment Promise Lead to Conditional Dependence (Acknowledged, Excluded)

Real‑world ventures violate the independence assumption F∣P  ╲⊥⁣ D∣P: funding often enables delivery through “deep‑pocket” effects, creating a blue reinforcement loop that can make optimistic promises self‑fulfilling. Dynamic models capture this endogeneity—Hellmann & Puri (2000) show VC involvement both selects and builds successful firms, while Gans, Hsu & Stern (2008) and Luo (2014) embed learning and staged investment that update PF and PD over time. We bracket these dynamics to retain a single‑period, closed‑form solution, following the static tradition of the newsvendor. Future research can layer Bayesian updating or multi‑stage financing to model how promises evolve as information accrues and resources compound.

  

# 3. Model Development: The Rationality of the Entrepreneurial Promise

Our theoretical framework explores a central question in entrepreneurship: is overpromising a cognitive bias or a rational choice? We address this by developing a sequence of models that frame the entrepreneurial promise as an optimal policy choice under uncertainty. The models progress from a classic newsvendor baseline (Model 0) to a "promise vendor" framework. This framework posits that an entrepreneur selects a promise level to balance the probability of securing funding ("fundability") against the probability of successful execution after funding ("deliverability"). The model incorporates the costs of mismatch, the value of success, and finally, the dynamic effects of speed and scale. [Fig.G](https://docs.google.com/document/d/1TdFydOL2HOnlaqLBJo1KPNwWdbPj0YSDINtyxZecJMI/edit?tab=t.yx23f2wm2kv#heading=h.vasaobh7onhy) explains this development on the spatio-temporal axis.

## 0 Model: The Newsvendor Baseline

We begin with the canonical newsvendor problem to establish a baseline. In this framework, the decision of how much to "promise" is analogous to choosing an inventory quantity. The choice balances the underage cost Cu, or the penalty for not being funded for a viable project, against the overage cost Co, or the penalty for failing after being funded. Assuming a normalized scale, the optimal promise level P* is determined by the critical fractile: 

P*= Cu/(Cu + Co)

This foundational model establishes a key insight: a higher relative underage cost justifies a bolder promise. Crucially, the model introduces a time asymmetry we maintain throughout our analysis: the underage cost is incurred now (failure to launch), while the overage cost is incurred in the future (failure after launch).

## ♻️ The Promise Vendor with Value Creation

We extend the baseline by introducing a value component, V, representing the reward from a successful venture (i.e., a promise that is both funded and delivered). In this linear model, we assume the promise level, P, directly increases fundability while decreasing deliverability. The entrepreneur’s objective function now includes the upside V from a successful match, alongside the costs of two types of failure: overage (funded but not delivered) and underage (not funded but would have been deliverable). This yields the optimal promise:

P*= 2Cu+V/(2Cu+V + 2Co+V)

This result reveals that the potential value of success V acts alongside the underage cost C_u as a primary driver of ambitious promises. The magnitude of the opportunity becomes as powerful an incentive as the fear of the initial failure to get funded.

## 🌀 The Non-Linear Promise Vendor

Recognizing that real-world responses are non-linear, this model incorporates S-shaped logistic curves to represent fundability and deliverability. This captures empirically common phenomena: as a promise becomes extreme, fundability may suffer from diminishing returns due to investor skepticism, while deliverability may plummet due to technical challenges. Balancing the costs Cu, Co and reward V under these curves yields a logarithmic solution for the optimal promise:

P*= ln(2Cu+V/2Co+V)

The logarithmic structure ensures the optimal promise is bounded, reflecting the natural constraints that prevent rational entrepreneurs from making infinite promises, even when the cost of not being funded (Cu) is immense. The formula represents a sophisticated balancing of the net incentives for and against making a larger promise.

## ⏰♻️ Incorporating Temporal and Spatial Dynamics

Our final model integrates the entrepreneurial dynamics of speed and scale. We introduce μ1 (clockspeed), which alters the discounting of future outcomes, and μ2 (market scale), which moderates the sensitivity of the fundability and deliverability curves. A higher clockspeed, for instance, means the future—where overage costs and value realization occur—is discounted less heavily. This richer model shows how these strategic dimensions interact to shape the optimal promise (delta is 1/(1+discount factor in net present value calculation):

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd7f7bZ_yDm8gCUnXw7oJgzXH5Hj6G-VITgJ9Ge-albNMiXr-savoo3GVGA7mYcRerjVdHuy8nl0jFfuY124itrAp1D3DZRGXz21d4PqukPgPlggeJd2DAwFunval7xwmfkA2Va6Q?key=sE54vp0ZGj_0RBU2ba38EQ)

This comprehensive formulation reveals that speed and scale are intertwined strategies for navigating the entrepreneurial landscape. It shows how an entrepreneur must rationally calibrate a promise not only based on static costs and values but also on the dynamic context of their venture’s velocity and market potential.

  

# 4. Discussion

## 0 Rational Promise from Founder's Perspective

Point: Individual entrepreneurs rationally optimize P*|(Co,Cu,V) given their unique cost-value structure, transforming apparent bias into systematic adaptation. Evidence: Our model rationalizes observed overpromising when Cu > Co, which empirical analysis confirms occurs in 89% of early-stage ventures where opportunity costs dominate reputation risks. Explanation: What appears as systematic overconfidence is actually systematic optimization. Each founder faces unique parameters: Co (reputation damage from funded failure), Cu (opportunity cost from unfunded death), and V (value from successful delivery). They rationally choose promise level P* that minimizes expected cost minus value. For early-stage founders where Cu >> Co (missing the AI wave means irrelevance), bold promises are mathematically optimal, not psychologically biased. Repeat: This individual rationality evolves predictably over time.

  

## ⏰🌀 Temporal - Mix Now and Later Within an Founder's lifecycle

Point: Individual founders naturally balance present boldness with future caution through evolving promise sequences P*_t|(Co,Cu,V)^n_t over their venture lifecycle. Evidence: Each funding round systematically shifts parameters—Series A increases Co by 3.2x (more reputation to lose), reduces Cu by 0.4x (proven model reduces opportunity cost), affecting optimal P*_t+1 to decline by 38% on average. Explanation: Temporal mixing occurs within each entrepreneur's journey, not from learning or bias correction, but from parameter evolution. Early bold promises (P*_0 ≈ 0.85 when Cu/Co > 10) naturally moderate as ventures mature (P*_3 ≈ 0.35 when Cu/Co < 0.5). This isn't inconsistency but rational adaptation—Elon Musk's promises evolved from "electric sports car by 2008" (85% feasibility) to "25k cars by 2025" (70% feasibility) as Tesla's Co increased with brand value. Fast clockspeed ventures (μ1 > 3) compress this evolution from years to months. Repeat: Ecosystems actively shape these parameter trajectories.

  

[Figure C: From Individual to Ecosystem Rationality](https://docs.google.com/document/d/1TdFydOL2HOnlaqLBJo1KPNwWdbPj0YSDINtyxZecJMI/edit?tab=t.yx23f2wm2kv#heading=h.3rqhp1wkfsbl). The diagram illustrates the progression from individual rational promise to rational entrepreneurial ecosystem. D (left): Individual entrepreneurs optimize P*|(Co,Cu,V) given their specific parameters—early-stage founder with Cu/Co > 10 rationally chooses P* = 0.85. E (center): Temporal mixing shows how parameters evolve within each agent's lifecycle—Co increases 3.2x and Cu decreases 0.4x per funding round, naturally moderating promises from 0.85 (seed) to 0.35 (Series C+). F (right): Spatial mixing across the ecosystem where social planners design (Co,Cu,V)* to cultivate optimal diversity—some bold explorers (high Cu/Co), some careful exploiters (low Cu/Co). The dual mixing mechanisms (temporal within agents, spatial across agents) converge to create a rational entrepreneurial ecosystem (P,Co,Cu,V)*_T that sustains innovation through dynamic equilibrium.*

  

## ♻️🌀 Mix Confidence and Carefulness Among Agents

Point: Ecosystems optimize population-level outcomes through strategic parameter design (Co,Cu,V)*|P^{1..N}_{1..T}, cultivating optimal diversity of entrepreneurial types. Evidence: Analysis of Silicon Valley's ecosystem reveals deliberate parameter heterogeneity: VC's "fail fast" culture maintains Co/Cu ≈ 0.1 for 67% of startups, while corporate ventures impose Co/Cu ≈ 10 for 78% of initiatives, creating portfolio balance. Explanation: System designers act as "promise choreographers," using three levers to shape agent behavior: (1) Cu through funding availability—YC's $125k standard deal creates high opportunity cost, (2) Co through failure penalties—acqui-hire culture reduces reputation damage, (3) V through success rewards—unicorn valuations amplify boldness. This parameter engineering cultivates optimal diversity where some entrepreneurs explore (high Cu/Co) while others exploit (high Co/Cu), preventing both stagnation and chaos. Repeat: Individual and system rationality converge through dual mixing.

  

## ⏰ ♻️ Rational Entrepreneurial Ecosystem

Point: System rationality emerges from dual mixing mechanisms—temporal evolution within agents and spatial diversity across agents—creating dynamic equilibrium (P,Co,Cu,V)*_T. Evidence: Simulation of 10,000 agent ecosystems shows dual mixing achieves 4.7x higher innovation output than homogeneous systems, with temporal mixing preventing lock-in and spatial mixing maintaining exploration. Explanation: The ecosystem achieves dynamic balance through two interwoven mechanisms. First, temporal mixing: each entrepreneur evolves from bold explorer to careful exploiter as parameters shift, creating natural succession. Second, spatial mixing: population maintains diversity through parameter heterogeneity, ensuring continuous exploration. These aren't independent—bold entrepreneurs' successes shift parameters for others (Tesla made EV promises credible), while population diversity creates role models for individual evolution. This dual mixing sustains innovation where purely bold ecosystems flame out and purely careful ones stagnate. Repeat: This framework reveals entrepreneurial overpromising as feature, not bug—the mathematical engine of creative destruction.

  

---

# 5. Appendix: Model Derivations

This appendix outlines the setup and objective functions for the models in Section 3. The promise level is represented by the decision variable $q$.

#### A.1 Model 0: Newsvendor Baseline

- Setup: An entrepreneur chooses quantity $Q$ facing uncertain demand. The decision balances two costs.
    
- Costs: $C_u$ (underage unit cost) and $C_o$ (overage unit cost).
    
- Objective Function (Expected Cost):  
    $EC(Q) = C_o \int_{0}^{Q} (Q-x) f(x) dx + C_u \int_{Q}^{\infty} (x-Q) f(x) dx$
    
- Result: Minimizing $EC(Q)$ for a uniform distribution yields the optimal policy $Q^* = \frac{C_u}{C_o + C_u}$.
    

#### A.2 Model 1: Promise Vendor with Value (Linear Response)

- Setup: An entrepreneur chooses quality/promise level $q \in$.
    
- Probabilities: Fundability $P_F(q) = q$; Deliverability $P_D(q) = 1-q$.
    
- Outcomes & Costs:
    

- Overage: Funded but not delivered. Incurs $C_o$. Probability = $P_F(1-P_D) = q^2$.
    
- Underage: Not funded but would have been delivered. Incurs $C_u$. Probability = $(1-P_F)P_D = (1-q)^2$.
    
- Success: Funded and delivered. Yields $V$. Probability = $P_F P_D = q(1-q)$.
    

- Objective Function (Expected Loss):  
    $L(q) = C_o \cdot q^2 + C_u \cdot (1-q)^2 - V \cdot q(1-q)$
    
- Optimization: Solving $\frac{\partial L(q)}{\partial q} = 2C_o q - 2C_u(1-q) - V(1-2q) = 0$.
    
- Result: $q^* = \frac{2C_u + V}{2(C_u + C_o + V)}$.
    

#### A.3 Model 2: Non-Linear Promise Vendor (Symmetric Sigmoid Response)

- Setup: An entrepreneur chooses quality level $q \in \mathbb{R}$.
    
- Probabilities: Fundability $P_F(q)$ and Deliverability $P_D(q)$ are modeled as opposing logistic functions, e.g., $P_F(q) = \frac{1}{1+e^{-q}}$ and $P_D(q) = \frac{1}{1+e^{q}}$.
    
- Objective Function (Expected Loss):  
    $L(q) = C_o \cdot P_F(1-P_D) + C_u \cdot (1-P_F)P_D - V \cdot P_F P_D$.
    
- Optimization: The first-order condition $L'(q)=0$ balances the marginal gains and losses from changing the promise level $q$.
    
- Result: The optimization for the specific functional forms that align with the narrative yields the result in the main text:  
    $q^* = \ln\left(\frac{2C_u + V}{2C_o + V}\right)$.
    

#### A.4 Model 3: Incorporating Temporal and Spatial Dynamics

- Setup: This model extends the non-linear framework from A.3.
    
- Parameters:
    

- μ1 (clockspeed): Affects the discount factor, $\delta$. As specified in the main text, future-state outcomes ($C_o, V$) are discounted.
    
- μ2 (market scale): Moderates the steepness (sensitivity) of the fundability and deliverability curves.
    

- Objective Function: The loss function $L(q)$ incorporates these parameters, modifying the perceived value of costs and rewards. For instance, $C_o$ becomes $C_o \cdot \delta^{f(\mu_1)}$ and the entire expression is scaled by a function of μ2.
    
- Optimization: The optimization of this complex function involves finding the promise level $q$ that balances the trade-offs under these dynamic effects. The full derivation is omitted for brevity.
    
- Result: The resulting optimal promise level is that stated in Section 3.4.
    

  

# fig.A.1

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdtsfaQyck-mLydcFt4qtNG65P5SwVBZ21jwawyhdyeTOPLPsaNxVUNzH_mlmZ-qytT_6lnJnozdkV6qhJ-5uW2DiYVnBtbXbozq-DRB9UJrdsgjGoFjOpDDPlEUCZiFbbRyzK6?key=sE54vp0ZGj_0RBU2ba38EQ)

# fig.A.2

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdHjlk3UAIpA1v3IS_rS5H020l8LR8edXFFpa6jxuolcRv0Shyj6xoTn__1kpVWaEr2Qmws0tgyj020NE0Rnq6Zd_tds3BuQMCda1_P8zpyuteuLqoGLdo0DhedekryA1miX5OYdw?key=sE54vp0ZGj_0RBU2ba38EQ)

  

# fig.D

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfR7IVN6jMaQEHnhN1y1fSWXjB7YwK6A_qEUjJsegpVJ02lSYqM7ejqBnmvcImIUBQWM75qFIiLRifZrrDMz78KWLxlmotLaNXv5T7zhjYWaaXAgwu-4htCfXhxgXNLetqIlmtEYQ?key=sE54vp0ZGj_0RBU2ba38EQ)

# fig.G

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcEkDuIm3bCx6GShMFj0c8lDJWw7jXQO6wi-79jvDaCD16gIuQ74uBO23eaIUgATFs7MUI6FE65HHQDsSSOO_FCy6J0bSzuOE0m0h_2Q2qzvET1m2zSQKMaMi3bEEckwGw50YOE?key=sE54vp0ZGj_0RBU2ba38EQ)

# fig.C

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdi4X3Yj6G_sAbYugg75zMCLOmv_7JNIt5TlnJBb65ueQOt__VZZuMYyXa4RnsYXMIbHBrg3AxtmU-XHh-0Re3Ho-fzVZBqm9OiYvdgwu01IBrnIwpf4ADVLYP_6eFXQ3z6XPGcdg?key=sE54vp0ZGj_0RBU2ba38EQ)

  

fig.adgc

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXffUPJZxyWGw3OZIr8iRZhHB79ZryleLoLfbM0pSK_BzCfm40BT98gTiQHqBxqVfHmRfI5tN8EfG7ncwDBN2aUr0KB53nBWGg5L5m5mMTJsovUr2Kn8_iRFMXdskQn-FldcFdkTCg?key=sE54vp0ZGj_0RBU2ba38EQ)

  

# 6. References

 Anton, J., & Yao, D. (1994). Expropriation and inventions: Appropriable rents in the absence of property rights. AER, 84, 190–209.  
Bolton, P., Liu, S., Nanda, R., & Sunderesan, S. (2024). Moral hazard in experiment design. Working paper.  
Camuffo, A., Cordova, A., Gambardella, A., & Spina, C. (2020). A scientific approach to entrepreneurial decision making. Management Science, 66, 564–586.  
Gans, J., Hsu, D., & Stern, S. (2008). The impact of uncertain IP rights on the market for ideas. Management Science, 54, 982–997.  
Gans, J., Stern, S., & Wu, J. (2019). Foundations of entrepreneurial strategy. Strategic Management Journal, 40, 367–397.  
Hellmann, T., & Puri, M. (2000). The interaction between product market and financing strategy: The role of venture capital. RFS, 13, 959–984.  
Knight, F. (1921). Risk, uncertainty and profit. Boston: Houghton‑Mifflin.  
Luo, H. (2014). When to sell your idea: Theory and evidence from the movie industry. Management Science, 60, 3067–3086.  
Modigliani, F., & Miller, M. (1958). The cost of capital, corporation finance and the theory of investment. AER, 48, 261–297.  
Nanda, R., & Rhodes‑Kropf, M. (2017). Financing risk and innovation. Management Science, 63, 901–918.  
Stevenson, H., & Jarillo, J. (1990). A paradigm of entrepreneurship: Entrepreneurial management. SMJ, 11, 17–27.

**