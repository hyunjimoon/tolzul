# Fake it Till you Approximate it: Hierarchical Bayesian Adaptation of Entrepreneurial Promises

## Abstract

Why do some ventures succeed while others fail, even when they share a similar vision? I argue that an under-theorized, core entrepreneurial capability lies in dynamically managing promise precision. This paper proposes a Bayesian framework that models an entrepreneurial promise as a distribution parameterized with aspiration and precision. The framework unifies the “planning school,” which favors high precision, and the “action school,” which favors low precision, as endpoints on a continuous spectrum of optimal ignorance. From this integration follows a prescription for optimal precision: I derive a policy function for founders given information-integration costs and environmental complexity. Conceptually, precision—also interpretable as a lever on the fundamental efficiency–flexibility trade-off—emerges from a structural innovation that separates the entrepreneur from the venture via a hierarchical Bayesian model. The precision parameter τ acquires three substantial meanings: the flexibility of the prior, the entrepreneur’s pseudo–sample size, and the breadth of the open space for adaptation. Building on these meanings, I explain how founders can learn efficiently through simulation and calibration. A contrast between Tesla and Better Place illustrates the theory: Tesla began with low precision and earned precision adaptively, while Better Place maintained a rigid high-precision promise and failed. The paper offers a new theoretical lens, empirical methodology, and actionable guidance to help entrepreneurs and investors navigate the efficiency–flexibility trade-off.

## ***Keywords**: Bayesian and Evolutionary entrepreneurship, Hierarchical Model, Calibration, Flexibility*

*It appears to be a general principle that, whenever there is a randomized way of doing something, then there is a nonrandomized way that delivers better performance but requires more thought. \- E.T. Jaynes.*

## 1\. Introduction

Tesla and Better Place shared a vision to electrify the automobile, yet their fates diverged dramatically because they managed promise precision differently. Both promised a sustainable transportation future, but their strategies sat at opposite poles of the confidence spectrum. Better Place committed to a tightly integrated, highly precise system of battery-swap stations—a high-τ promise requiring the entire ecosystem to conform at once. Tesla, by contrast, began with a low-τ promise—a premium sports car for a niche market—and increased precision gradually while learning from the market, expanding both its product line and charging infrastructure. I argue that the capability to dynamically manage promise precision explains this fork in outcomes.

### 1.2. Three Meanings of τ

In my model, precision τ carries three analytically grounded meanings:

1. Promise precision. High τ denotes a narrow, specific commitment; low τ denotes a broad, flexible commitment.

2. Pseudo–sample size. High τ behaves as if the founder holds substantial prior evidence.

3. Width of open adaptive space. Low τ preserves a set of latent functions not yet specified, maximizing the real option value of exaptation.

As organizations mature and face greater information-integration costs and environmental complexity, managing τ dynamically—by deliberately controlling i (information-integration cost) and c (complexity)—becomes a central task.

The structural metaphor of DNA helical tension and the strategic metaphor of firebreak width illuminate why flexibility (low τ) and efficiency (high τ) succeed under different conditions:

Table 1\. Bayesian–Entrepreneurial Metaphors for the Flexibility–Efficiency Tension

|  | Low τ (Flexibility) | High τ (Efficiency) |
| ----- | ----- | ----- |
| DNA tension | Loose | Tight |
| Firebreak width | Wide | Narrow |
| Best-fit environment | High complexity, high information cost | Low complexity, low information cost |

Tightly wound DNA strands (high τ) replicate with high fidelity and are efficient in stable environments, but they generate little variation and thus adapt poorly to shocks. Loosely wound strands (low τ) admit variation, enabling pivots essential for survival in changing conditions. Firebreak width reflects the founder’s prior quality: a founder with a very high-quality prior (e.g., Robert Langer at MIT) can set a narrow firebreak (high τ) and pursue maximum efficiency; a less certain founder exploring novel terrain should widen the firebreak (low τ) to preserve room and time to maneuver when reality defies the initial thesis.

### 1.4. Methodological Innovation: Separating Entrepreneur and Venture

I implement hierarchical Bayesian modeling to separate the entrepreneur (prior) from the venture (likelihood). This enables simulation and calibration of a business model to raise its success probability. The separation clarifies how environmental complexity c shapes the likelihood of success and how the strategic choice of ambiguity τ shapes the prior—allowing us to model learning as belief-updating in response to venture-generated evidence (Gelman et al., 2020).

### 1.5. Bridging Schools of Thought

The framework bridges the false dichotomy between the action school, which values flexibility and emergence, and the planning school, which values detailed prediction and commitment. In our model, the pure action school corresponds to the limit τ → 0 (maximal openness), and the pure planning school corresponds to τ → ∞ (absolute confidence in a single plan). These are endpoints of a continuum. Rather than “decision-making under uncertainty,” we model decision-making about uncertainty itself, offering a new perspective for strategy.

### 1.6. Roadmap

We proceed with a “what–why–how–so what” logic. Section 2 develops the theory of τ, its structural and strategic metaphors grounded in Bayesian and Evolutionary math. Section 3 applies the framework to Tesla and Better Place, showing how it explains real-world success and failure. Section 4 envisions future works in both theory and practice.

## 2\. Theory and Modeling

### 2.1 Theoretical Background

#### 2.1.1 Anatomy of Success Probability

The entrepreneurship literature has long been divided by a fundamental epistemological schism regarding the nature of opportunity and success probability. The planning school, exemplified by Porter’s (1980) competitive positioning framework and extended by Camuffo et al. (2020) through their scientific approach to entrepreneurial decision-making, posits that systematic analysis and hypothesis testing can reduce uncertainty to manageable proportions. This tradition, rooted in industrial organization economics (Bain, 1956; Mason, 1939), treats success probability as an exogenous market characteristic that entrepreneurs must discover through rigorous analytical processes. Conversely, the action school, pioneered by Sarasvathy’s (2001) effectuation theory and complemented by Baker and Nelson’s (2005) bricolage construct, argues that opportunities emerge through entrepreneurial action rather than analytical discovery. March’s (1991) exploration-exploitation framework provides the theoretical underpinning for this perspective, suggesting that under conditions of radical uncertainty, experimentation supersedes planning. Yet both schools share a critical limitation: they treat success probability as exogenous to entrepreneurial choice, differing only in their prescribed methods for navigating this given constraint. However, this is odd. If entrepreneur can't have any influence on one's venture success, what's the point of entrepreneurial education? Also, if venture success probability is exogenous, does it matter who founds the venture? Does this one core assumption in decision making model negate > 1000 entrepreneurhsip literature reporting "nature" aspect of entrepreneurship, finally terminating the greatest myth of entrepreneurship that entrepreneurs are born? (Agrawal, 2025)

Our theoretical contribution fundamentally reconceptualizes success probability through a double reparameterization that transforms it from an exogenous constraint to an endogenously designed variable. Building on recent advances in Bayesian decision theory (Gelman et al., 2020\) we decompose success probability P into promise level φ, which we further decompose into aspiration μ and precision τ. This decomposition reveals that entrepreneurs possess three strategic levers—φ\*, μ\*, and τ\*—through which they actively construct rather than merely respond to their probability landscape. The failure of Better Place, despite $850 million in funding and seemingly perfect planning (Etzion & Struben, 2023), versus Tesla’s trajectory from ambiguous promises to market dominance (Teece, 2018), cannot be explained by existing frameworks that treat success as exogenously determined. Our model demonstrates that Better Place’s high precision parameter (τ → ∞) created what we term a “learning trap,” (proposition1) while Tesla’s initially low τ preserved what Keats (1817) called “negative capability”—the capacity to remain comfortable with uncertainty. This reconceptualization transforms the entrepreneur from what Kirzner (1973) termed an “alert discoverer” to what we propose as an “uncertainty architect.”

#### 2.1.2 Tau Stitches False Dichotomies 

Table 2\. False Dichotomies Unified by the τ Framework

| Domain                                  | Low τ (Complex / High i)                | High τ (Simple / Low i)               | Unifying Principle                                            |
| --------------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------------------------------- |
| Strategy schools                        | Action school (“act then think”)        | Planning school (“think then act”)    | τ maps action–planning onto a continuum                       |
| Learning schools                        | Model-free (experience-driven)          | Model-based (theory-driven)           | τ weights prior knowledge                                     |
| DNA tension metaphor                    | Loose DNA (high variation, flexibility) | Tight DNA (low variation, efficiency) | τ tunes variation vs. replication fidelity                    |
| Sampling                                | Few samples (fast decisions)            | Many samples (precise estimates)      | τ ≈ pseudo–sample size                                        |
| Founder’s response to given uncertainty | Fight with self-imposed uncertainty     | Fight with knowledge                  | τ sets the explore–exploit balance                            |
| Venture cases                           | Tesla (flexible pivots)                 | Better Place (rigid strategy)         | τ\* decreases with higher complexity c and integration cost i |

Thus τ is not a binary choice but a continuous variable that should be tuned to environmental conditions (i: information-integration cost, normalized by venture value; c: environmental complexity). As c and i rise, the optimal τ decreases (choose flexibility); as they fall, the optimal τ increases (choose efficiency). Tesla’s trajectory (start low τ, then earn precision) and Better Place’s failure (rigid high τ amid high complexity) illustrate the point. 

![][image1]

#### 2.1.3 Tau Viewed from Bayesian Entrepreneurship Island

“Bayesian entrepreneurship” reconceives the founder’s cognition as a computational inference system, not merely the application of probabilistic language. Agrawal et al. (2024) articulate how founders possess heterogeneous, relatively strong priors and update them systematically via Bayes’ rule—casting founders as active theorists (Felin & Zenger, 2009; Zellweger & Zenger, 2023). RCT evidence (Camuffo et al., 2020, 2024\) shows scientific approaches improve termination, pivoting, and performance; Novelli & Spina (2024) highlight the role of causal reasoning, in line with hierarchical Bayesian cognitive models (Griffiths and Tenenbaum, 2017; Tenenbaum, 1998). Current frontiers integrate individual and population-level learning (Li et al., 2023), i.e., meta-learning across venture populations.

Two epistemic shifts follow. First, priors and likelihoods are not merely “what” but “how”—embodied process knowledge (Gelman et al., 2017). τ is thus a meta-parameter governing strategic flexibility and learning speed. Second, we separate modeler and model (entrepreneur vs. venture), adopting Bayes not only for inference but for model development as an iterative design process.

Technically, the beta–binomial conjugate structure with a precision parameterization places execution–planning and explore–exploit on a single mathematical spectrum. Venture outcomes are sequences of Bernoulli trials (e.g., conversions, test passes), giving a Binomial likelihood. The unknown success probability ϕ has a Beta prior with mean (aspiration) μ and precision τ. Conjugacy provides clean posterior updates and ties the abstract notions of strategic certainty and flexibility to a precise statistical quantity, τ.

DNA metaphor—separating prior and likelihood. DNA tension depicts the relation between the entrepreneur’s prior (τ) and environmental constraint (c). Sellability vs. deliverability is encoded in the likelihood: as c rises, deliverability of any promise ϕ drops steeply. τ, in turn, governs how strongly the prior weighs against new data. Low τ protects flexibility and learnability (more weight on data) but may hamper resource mobilization; high τ aids mobilization (more weight on prior) but risks rigidity when wrong.

![][image2]

Graphically, priors with different τ (e.g., Beta(0.5,0.5), Beta(1,1), Beta(2,2)) illustrate Ignore → Attention → Know stages; posterior dynamics visualize Contraction / Compromise / Containment under new data—showing that τ is the control knob for learning speed and pivot capacity.

#### 2.1.4 Tau Viewed from Evolutionary Entrepreneurship Island

Beyond biological analogy, evolutionary entrepreneurship fuses complex adaptive systems with operations science. 🚨Fine (1986; Fine & Li, 1988; Fine & Freund, 1990\) modeled learning and flexibility–efficiency trade-offs; Clockspeed (Fine, 1998\) formalized industry-specific evolutionary tempos; Fine et al. (2002) developed rapid-response capability across value chains; Operations for Entrepreneurs (Fine, 2022\) offers the Nail–Scale–Sail framework and ten scaling tools. Opportunities that form at the boundary of the value chain, and options values🚨

Felin & Kauffman (2021a; 2021b) extend this with the adjacent possible, explaining how opportunity arises from the current frontier of technology, markets, and resources. Functional excess and experimentation power disruptive evolution, dovetailing with exaptation (Gould & Vrba, 1982). With Bateson’s (1963) somatic flexibility, low τ preserves slack that can be repurposed. Slack’s pivot from gaming to enterprise communication exemplifies how low-τ assets enable exaptation.

Firebreak metaphor—strategic ambiguity as containment. A wide firebreak (low τ) is prudent where fire (market dynamics) behaves unpredictably: you concede uncertainty and create defendable space away from the fire’s edge. Low-τ founders adopt containment; high-τ founders adopt contraction—efficient when fires are small, catastrophic when they jump the line.

### 2.2 Model: From “Fake It Till Make IT” to “Approximate It”

Table 3\. Key Model Variables

| Variable | Definition | Interpretation | Example (Tesla vs. Better Place) |
| ----- | ----- | ----- | ----- |
| μ | Aspiration (mean of belief distribution) | Boldness of the promise | Tesla (μ≈0.3): “200+ miles.” Better Place (μ≈0.9): “Infinite range.” |
| τ | Precision  | Specificity/rigidity of the promise | Tesla (τ≈1): “\~200 miles (±40).” Better Place (τ≈4): “Exactly 3 minutes.” |
| C | Operational complexity | \# of independent, critical components | Tesla (n≈5): pack, motor, software. Better Place (n≈10): robotics, real estate, standards, OEMs. |
| I | Information-integration cost | Marginal cost to raise τ by one | Tesla: prototype iteration. Better Place: nationwide swap network. |
| V | Venture value | Value upon successful delivery | E.g., market cap or TAM. |

​​2.4 Model: From “Fake It Till Make It” to “Approximate It”

![][image3]

**Figure1.** This figure makes transparent, across four layers, how an entrepreneur’s epistemology matures: In M1, the promise φ is monotonically linked to success probability; in M1′, nature’s complexity c bends that monotonicity into a concave shape, so the same promise has different effective impact. By M2, we treat promises as a distribution and probabilistically design aspiration μ; in M2′, the entrepreneur chooses the design variable τ to approximate that distribution, adopting rational ignorance as a strategy by balancing it against the meaning-construction cost i. Ultimately, it offers a grammar for deciding scientifically not “to know more,” but “when and what to leave unknown,” and that grammar is the bridge that reunifies the planning school and the action school along a single continuum.

We formalize four decision-making models (M1 through M2′) that progressively incorporate complexity, founder-venture separation, and approximation. This progression mirrors a shift from the naive “fake it till you make it” approach (blindly promising the moon) to a more nuanced “approximate it” approach (managing and choosing uncertainty deliberately).

2.4.1. M  Naive Commitment (No Complexity). 

The founder directly chooses a target outcome φ  to maximize the probability of success P(S∣φ). In this simplest baseline, there are no penalties for over-promising. If success likelihood increases monotonically with the ambition level  (as implicitly assumed in many simplistic models), the trivial “solution” is to promise as much as possible (maximize φ). This corresponds to an extreme “fake it till you make it” mentality – the founder would always set to the highest conceivable value because nothing in the model discourages doing so. However, M1 is clearly unrealistic: it ignores the complexity of execution and the uncertainty in achieving φ. 

2.4.2 M1′ Incorporating Complexity C 

We introduce a complexity parameter  that captures the aggregate uncertainty from the environment and organization. In strategy terms,  combines external uncertainty (e.g. market volatility, economic crises, regulatory changes) and organizational uncertainty (e.g. internal coordination problems, many subsystems or layers) into a single Complexity measure. Complexity directly dampens the likelihood of success for any given promise φ. Specifically, suppose the joint probability of “success and delivering on the promise” given φ is:  
				P(S∧D∣φ)=φ (1-φ)^c

This functional form means that as the promised outcome  grows, it becomes exponentially harder to actually deliver success when complexity  is high (intuitively, higher goals incur greater penalty in a complex environment). The founder now chooses  to maximize P(S∧D∣φ)=φ(1-φ)^c. Unlike M1, this model yields a finite optimal promise: if c\>0, over-promising is self-defeating (e.g.  gives zero success probability because (1-1)^c=0). Adding complexity transforms “fake it” into a calibrated strategy: the founder must trade off ambition against the probability of delivery. In other words, M1′ captures the idea that the greater the combined external and internal uncertainty (higher c), the more a founder should temper their promises. For example, if a startup faces turbulent markets and a convoluted organizational design (high c), a bold claim like “we will achieve 100% of X” is very likely to fail; a more modest φ has higher chance of success. (Indeed, φ(1-φ)^c is φ-concave for c \>0 , so the optimal  will lie in (0,1) and decline as c increases.)

 2.4.3 M2: Bayesian Separation of Founder’s Belief and Reality

In this extension, the founder acknowledges that φ (the true achievable performance or probability of success) is uncertain. Instead of picking a fixed φ, the founder adopts a prior distribution over φ. Let that prior be parameterized by a mean  (and implicitly some precision, addressed later). The *founder’s decision* now is to choose the prior’s parameters (here, μ ) to maximize expected success. The success function remains the same likelihood from M1′. Mathematically, the founder solves:

max\_μ ∫\_0^1 P (S∧D∣φ) p(φ∣μ) dφ

where p(φ∣μ) is the prior density reflecting the founder’s initial belief about φ. This formulation introduces a principal–agent-like separation (Gelman and Shalizi, 2013): the *venture’s outcome*  is a random variable (driven by nature or underlying reality), while the *founder* can only influence it through her prior choice (beliefs/strategic posture). Importantly, the founder’s optimal strategy now involves “choosing her uncertainty” (via the prior) rather than assuming a known outcome. This model aligns with recent Bayesian entrepreneurship perspectives that highlight how founders’ subjective priors shape outcomes. By adding separation, M2 moves beyond “faking a specific outcome” – it recognizes the founder must prepare for an uncertain range of outcomes. The founder’s choice will balance optimism vs. caution: for instance, if the environment is likely harsh (high c), the founder might choose a relatively conservative prior  (lower expected φ) to avoid plans predicated on unrealistically high success chances. Conversely, in a benign context, a higher μ (more aggressive belief) might maximize expected payoff. The key insight is that the founder’s belief (prior) acts as a strategic decision lever separate from the environment’s complexity. Note that traditional operations (Phan and Chambers, 2013\) assumes “decision-making **under** uncertainty” where external uncertainty is given; here, we emphasize decision-making *on* uncertainty – the founder actively chooses a belief stance  under uncertainty.

**Proposition 1 (Learning Trap).**  
 A trap arises when μ(1−μ)\<ε(τ+1). High τ prevents revision, creating rigidity.

As will be explained with rich graphics in the 3\. Application section, high precision prevents belief updates, creating structural rigidity regardless of market evidence. Better Place's "exactly 3-minute battery swap" (τ≈30) reduced their learning capacity to 0.003—even a strong signal like BMW's refusal to participate couldn't change their strategy. 

2.4.4 M2′: Approximate Planning with Bounded Rationality

Finally, we account for the costs of reasoning and information. In reality, entrepreneurs cannot integrate over all possibilities perfectly (as in M2) because gathering and processing information is costly and time-consuming. Model M2′ introduces a *resource-rational* approach: the founder chooses not only a prior  but also a precision  τ, which determines how confident or narrow that prior is. Equivalently,  τ can be viewed as the number of samples or experiments the founder effectively uses in shaping her plan. Rather than compute the full integral, the founder considers a limited sample of τ hypothetical outcomes  drawn from the prior p(φ∣μ,τ). She then maximizes an *approximate expected success* minus a cost term:

	max\_(μ, τ)  {1/τ ∑\_(k=1)^τ P (S∧D∣φ\_k ) - i(τ)},

where i(τ) is an increasing cost function (the cost of drawing/analyzing more samples or the cost of delay/complexity in a more precise plan). This Monte Carlo–style objective approximates the true expectation in M2 when τ is large, but it allows the founder to economize on cognitive effort by using a smaller  if costs warrant. The inclusion of  explicitly as a decision variable captures the idea from cognitive science that sometimes “one or few shots” is optimal when deliberation is costly (Vul [et.al](http://et.al)., 2014). A founder with a low  is effectively sampling very little – perhaps making a quick gut decision or a rough plan after considering only a couple of scenarios. This corresponds to an “Approximate It” strategy: the founder chooses to remain flexible and *not* over-commit to a single precise prediction, which preserves adaptability and saves resources. On the other hand, a higher τ means the founder conducts more analysis or experimentation (approaching the full Bayesian ideal of M2), which can improve the plan’s accuracy but at an escalating cost i(τ) . The optimal τ\* balances these: it will be lower when complexity is high or quick adaptation is needed (favoring exploration and learning), and higher when the environment is more stable or the cost of being wrong is very high (favoring thorough planning and exploitation of the prior). In sum, M2′ adds approximate inference to the model, showing how a founder *rationally limits the scope of their planning* under resource constraints – a key difference between idealized decision-making and practical entrepreneurship.

***Proposition2 (Optimal precision/ignorance).***  
*Optimal aspiration and precision level maximizing expected payoff marginalized over posterior distribution is (μ∗,τ∗)=(1/(c+1),  max⁡{0, ((c/(c+1))^c/(2i))−1}). Optimal aspiration and precision both decrease with complexity; higher information-integration cost lowers optimal precision.* 

Proof is in the appendix

***Corollary.** Founders don’t “pick between think or act”; they pick τ appropriate to their context on complexity and information integration cost(c, i), and earn higher τ as n accumulates. Low τ → exploration (data-dominant updates); high τ → exploitation (prior-dominant execution).* 

Proposition2 shows both aspiration and precision can be optimized, justifying intentional ignorance of some information if that’s not worth the cost. This happens early stages ventures where it’s under high complexity and low integration cost.

### From Uncertainty As Constraint (M1, M1’) to Choice (M2, M2’)

In the above models, we have formally separated two roles of uncertainty in entrepreneurial strategy:

* **Complexity (c)** – the uncertainty exogenous to the founder, stemming from external and organizational sources. This appears in the likelihood P(S∧D∣φ) and *acts as a drag* on success probability. Higher  means the world is more unpredictable or complex; **any given bold plan is less likely to succeed**. This captures what strategy scholars call external vs. internal uncertainty: for instance, a severe economic recession or shifting regulations (external uncertainty) and a convoluted corporate structure with many interdependent subsystems (organizational uncertainty) both raise c. Our formulation **aggregates them** into one complexity term for analytical simplicity – effectively treating *external* and *internal* uncertainties as additive contributors to execution difficulty.  To clarify, strategy literature distinguishes between firm’s *external uncertainty* (e.g. 2008 economic crisis, covid) and internal *uncertainty* (e.g. organizational)*.* In my model both are nature’s uncertainty captured in the likelihood via c, which are different from uncertainty from tau (captured in the prior).  
* **Prior Precision (τ)** – the uncertainty **chosen by the founder**. This appears in the prior p(φ∣μ,τ)  and reflects how narrowly or broadly the founder defines the venture’s direction upfront. A low τ means a very broad prior (high uncertainty in belief, or an initially vague, flexible promise), whereas a high  means a tight prior (low uncertainty in belief, a specific and rigid commitment). Crucially, τ is under the founder’s control – it’s part of the *strategy*. In our framework, the founder decides how much uncertainty to embrace or avoid: this is the essence of **“decision-making on uncertainty.”** By setting τ, the founder is effectively tuning how much they **“fake” precision vs. leave room to adapt**.

This perspective is novel in that classic decision theory treats uncertainty as something to endure or mitigate, whereas here the founder actively **manages and allocates uncertainty**. The term **τ-spectrum** highlights that entrepreneurs can deliberately operate anywhere between high uncertainty (exploratory mode) and low uncertainty (exploitative, committed mode), depending on context. With illustrative examples on tesla and betterplace, we identify complexity and information integration cost to critique their τ management in the next section.

**In summary,** the evolution from M1 to M2′ captures a shift in entrepreneurial decision-making philosophy. Rather than **just “faking it” under uncertainty**, successful founders dynamically **approximate** solutions – they manage how much uncertainty to take on. By separating the world’s complexity (uncertainty-as-constraint,  ) from the founder’s strategic choice (uncertainty-as-choice,  ), we get a richer spectrum of behaviors. This helps explain why entrepreneurs like Tesla’s team thrive by embracing learning and adjustment (low τ when  is high), whereas those who lock in rigid plans in complex environments can fail spectacularly. Our model thus provides a language to discuss **when to flex versus when to fix** in startup strategy, contributing a novel perspective to the strategy literature’s longstanding discussion of exploitation vs. exploration under uncertainty. The next sections will build on this foundation to management policy of τ (and related decision variables) as ventures progress, and to derive testable implications for entrepreneurial performance.


## 3\. Application: Tesla vs. Better Place and Empirical Predictions

### ![][image4]

### 3.1 From M1′ to M2′: The Evolution of Probabilistic Thinking

Better Place remained trapped in a deterministic M1′ frame: precise sales targets (“100k in Israel by 2011”), exact swap times (“exactly 3 minutes,” later “59.1 seconds”), fixed station costs (“$0.5M,” actually \>$2M). Excess precision structurally blocked learning. Tesla implemented M2′: it reframed “250 miles” as “200+ miles,” preserving legitimacy while updating; used early Roadsters as paid experiments to probe price elasticity, feature preferences, and geographic demand; published independent validations and transparently revised targets. The low-τ start and sequential learning raised τ over time.

### 3.2 Contrasting Approximation Strategies: Sequential Sampling vs. One-Shot Bets

Musk’s 2006 “Secret Master Plan” explicitly staged learning: (1) sports car, (2) mid-price car, (3) mass-market car, (4) solar integration—each stage funding and informing the next. Production ramped 2.5k → 50k → 500k, with τ increasing stepwise. Better Place invested \~$850M up front in a single infrastructure bet, precommitting to large-scale deployment and narrowing posterior updates. Sales stalled (\~1,400), many internal or leased.

### 3.3 Managing Complexity: The Power of Ruthless Simplification

Tesla systematically reduced c: a single gear ratio, concentrated suppliers (e.g., pack with Panasonic), tighter vertical integration, and simple comparative metrics (e.g., g/km CO₂). Better Place faced sprawling complexity: robotics, standards, multi-party coordination (OEMs, utilities, governments, real estate), and simultaneous multi-country rollout—pushing n \> 15 and implying a very conservative μ\* that they ignored.

### 3.4 Information-Integration Costs: Organization Sets the Learning Rate

Tesla’s low i (fast dissemination, rapid iteration, public transparency, direct customer feedback) enabled quick adaptation. Better Place’s high i (slow message updates, delayed plan revisions, prolonged leadership changes) dampened learning, sustaining an over-precise prior.

A stylized formula (e.g., τ\* ≈ 1/12) captures why Tesla could afford to raise τ while Better Place could not—and why reversing these choices produced opposite outcomes.

### 3.5 Practical Prescription: Earn Your Precision

Actionable guidance:

* Manage I (information integration)  
   – Simplify evaluation metrics (focus on 2–3 KPIs; weekly single-metric review).  
   – Codify decision principles; measure information-sharing latency.  
   – Design staged experiments (e.g., 100 → 1,000 → 10,000 units); track per-stage learning cost.

* Manage C (complexity)  
   – Reduce independent subsystems to ≤10; apply first-principles simplification.  
   – Favor modular architectures to enable parallel innovation.

Monitor V/(I·C) continuously: if ≤1, lower τ immediately; raise τ only when \>2. Investors should assess founders’ predict-then-prescribe capability and probabilistic thinking; educators should teach how and when to choose flexibility vs. efficiency beyond generic “lean startup” advice.

### 3.6 Visualizing Bayesian Learning: Containment vs. Contraction

The 2008 crisis highlighted the contrast. Tesla adjusted prices and plans quickly—wide priors, fast posteriors. Better Place held to precise targets and sought more capital—narrow priors that structurally blocked updating. Learning capacity scales as μ(1−μ)/(τ+1); with very high τ, it can approach zero.

![][image5]

### 3.6 Evidence via Predict-Then-Prescribe: A Hierarchical Bayesian Analysis of Founder Language

We propose measuring cognitive τ from 10,000 VC pitch decks (tense, modals, numeric ranges) to infer founders’ τ choices. A hierarchical Bayesian model estimates founder-specific τ propensities and heterogeneous effects on outcomes, addressing essential heterogeneity (Mackey & Dotson, 2024\) beyond standard econometric measures like instrumental variables. We predict ventures that start with τ≈5 in the first six months and increase to τ≈20 over the next 18 months exhibit \~2.5× higher three-year survival, with larger effects in high-complexity (n\>10) industries.

## 4\. Conclusion and Vision

### 4.1 Formal (Form) and Functional (Function) Contributions

Form. (i) We separate entrepreneur (modeler) and venture (model) via a hierarchical Bayesian structure, explicitly distinguishing prior and likelihood (§1.4). (ii) We double reparameterize success probability → promise → (μ, τ), reducing promise design to choices over mean (aspiration) and precision (§2). (iii) We endow τ with three substantive meanings—prior breadth, pseudo–sample size, and option-space width—making it a single control knob linking strategic flexibility and learning speed (§1.2).

Function. We make two capabilities prescriptive: simulation (sampling from the belief distribution to front-load experiment design, M2′) and calibration (adjusting the weights on μ and τ in proportion to observed data—“earn your precision”). Together they power predict-then-prescribe in OM, providing explicit rules for when to choose (and transition between) low-τ flexibility and high-τ efficiency, thereby integrating “action vs. planning” as a choice of optimal τ along a spectrum.

| Axis | Contribution | Reader Benefit |
| ----- | ----- | ----- |
| Form | Founder–venture separation; τ’s three meanings | Identifiability, estimability, reproducibility |
| Function | Operating rules for simulation & calibration | Immediate use in experiment design, due diligence, and curricula |

### 4.2 Vision

#### 4.2.1 For Theorists: Integrating Schools and Opening Questions

We bridge Bayesian and evolutionary entrepreneurship, noting their distinct units of analysis: bits (information) vs. atoms (structures). Future work should model, via hierarchy, how abstract beliefs manifest as concrete actions, and how predictive–prescriptive agents choose and shape environments.

#### 4.2.2 For Empiricists: New Measures and Analyses

Language in pitch decks provides a window into cognitive τ. Hierarchical Bayesian designs can estimate unobserved founder traits and heterogeneous effects, advancing beyond IV-limited approaches to essential heterogeneity (Mackey and Dotson, 2024).

#### 4.2.3 For Founders: Dynamic Management of Optimal Ignorance

“Earn your precision.” Admit ignorance and manage it: simplify metrics, stage experiments, and counter rising i and c with deliberate controls to stay on the optimal τ path.

#### 4.2.4 For Educators, Investors, and Policymakers: Capability Building and Assessment

Evaluate not only vision (μ) but calibrated realism (dynamic τ management). Teach when and why flexibility vs. efficiency dominates, grounded in c and i, not slogans.

## 5\. References

*Agrawal, A., Gans, J., & Stern, S. (Eds.). (2024). Bayesian entrepreneurship. MIT Press.*

*Brinkerink, J. (2025). Negative Capability and Entrepreneurial Action. Strategic Change.Baker, C. L.,* 

*Saxe, R., & Tenenbaum, J. B. (2011). Bayesian theory of mind: Modeling joint belief-desire attribution. Proceedings of the Annual Meeting of the Cognitive Science Society, 33, 2469-2474.*

*Baker, C. L., Jara-Ettinger, J., Saxe, R., & Tenenbaum, J. B. (2017). Rational quantitative attribution of beliefs, desires and percepts in human mentalizing. Nature Human Behaviour, 1(4), 0064\.*

*Bateson, G. (2000). Steps to an ecology of mind: Collected essays in anthropology, psychiatry, evolution, and epistemology. University of Chicago press.*

*Camuffo, A., Cordova, A., Gambardella, A., & Spina, C. (2020). A scientific approach to entrepreneurial decision making: Evidence from a randomized control trial. Management Science, 66(2), 564-586.*

*Camuffo, A., Gambardella, A., Messinese, D., Novelli, E., Paolucci, E., & Spina, C. (2024). A scientific approach to entrepreneurial decision making: Large scale replication and extension. Strategic Management Journal, forthcoming.*

*Felin, T., & Kauffman, S. (2021a). Disruptive evolution: Harnessing functional excess, experimentation and science as tool. Industrial and Corporate Change, 30(2), 446-466.*

*Felin, T., & Kauffman, S. (2021b). The search function and evolutionary novelty. In S. Kauffman (Ed.), A world beyond physics (pp. 122-145). Oxford University Press.*

*Felin, T., & Zenger, T. R. (2009). Entrepreneurs as theorists: On the origins of collective beliefs and novel strategies. Strategic Entrepreneurship Journal, 3(2), 127-146.*

*Fine, C. H. (1986). Quality improvement and learning in productive systems. Management Science, 32(10), 1301-1315.*

*Fine, C. H. (1998). Clockspeed: Winning industry control in the age of temporary advantage. Perseus Books.*

*Fine, C. H. (2022). Operations for entrepreneurs. MIT Press.*

*Fine, C. H., & Freund, R. M. (1990). Optimal investment in product-flexible manufacturing capacity. Management Science, 36(4), 449-466.*

*Fine, C. H., & Li, L. (1988). Technology choice, product life cycles, and flexible automation. Journal of Manufacturing and Operations Management, 1(4), 372-399.*

*Fine, C. H., Vardan, R., Pethick, R., & El-Hout, J. (2002). Rapid-response capability in value-chain design. MIT Sloan Management Review, 43(2), 69-75.*

*Gelman, A., & Shalizi, C. R. (2013). Philosophy and the practice of Bayesian statistics. British Journal of Mathematical and Statistical Psychology, 66(1), 8-38.*

*Gelman, A., Simpson, D., & Betancourt, M. (2017). The prior can often only be understood in the context of the likelihood. Entropy, 19(10), 555\.*

*Gould, S. J., & Vrba, E. S. (1982). Exaptation--a missing term in the science of form. Paleobiology, 8(1), 4-15.*

*Griffiths, T. L., & Tenenbaum, J. B. (2009). Theory-based causal induction. Psychological review, 116(4), 661\.*

*Huh, W. T., Kim, M. J., & Lin, M. (2025). Uncertain search with knowledge transfer. Management Science.*

*Jara-Ettinger, J., Gweon, H., Schulz, L. E., & Tenenbaum, J. B. (2016). The naïve utility calculus: Computational principles underlying commonsense psychology. Trends in cognitive sciences, 20(8), 589-604.*

*Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. Econometrica, 47(2), 263-291.*

*Knight, F. H. (1921). Risk, uncertainty and profit. Houghton Mifflin.*

*Mackey, T., & Dotson, J. (2024). Bayesian Statistics in Management Research: Theory, Applications, and Opportunities. Oxford Research Encyclopedia of Business and Management.*

*Novelli, E., & Spina, C. (2024). Causal reasoning and the scientific entrepreneur. In A. Agrawal, J. Gans, & S. Stern (Eds.), Bayesian entrepreneurship (Chapter 6). MIT Press.*

*Phillips, J., Morris, A., & Cushman, F. (2019). How we know what not to think. Trends in Cognitive Sciences, 23(12), 1026-1040.*

*Sarasvathy, S. D. (2001). Causation and effectuation: Toward a theoretical shift from economic inevitability to entrepreneurial contingency. Academy of Management Review, 26(2), 243-263.*

*Skali Lami, O. (2022). Predictive and Prescriptive Analytics in Operations Management (Doctoral dissertation, Massachusetts Institute of Technology).*

*Tenenbaum, J. (1998). Bayesian modeling of human concept learning. Advances in neural information processing systems, 11\.*

*Zellweger, T., & Zenger, T. (2023). Entrepreneurs as scientists: A pragmatist approach to producing value out of uncertainty. Academy of Management Review, 48(3), 379-408.*

## 7\. Appendix: Proof Sketches

**Proposition 1 (Learning Trap).**  
 A trap arises when μ(1−μ)\<ε(τ+1). High τ prevents revision, creating rigidity.  
 *Proof.* After a failure, prior Beta(μτ,(1−μ)τ) updates to Beta(μτ,(1−μ)τ+1), with μ′=μτ/(τ+1). Then ∣μ′−μ∣=μ(1−μ)/(τ+1)\<ε ⇒ τ\>μ(1−μ)/ε−1.

**Proposition2 (Optimal precision/ignorance).**  
Optimal aspiration and precision level maximizing expected payoff marginalized over posterior distribution is (μ∗,τ∗)=(1/(c+1),  max⁡{0, ((c/(c+1))c/(2i))−1}). Optimal aspiration and precision both decrease with complexity; higher information-integration cost lowers optimal precision. 

 *Proof.* Maximize L(μ,τ)=E\[p(ϕ)\]−C(τ)  with expected reward ⋅E\[ϕ(1−ϕ)c\]  and linear precision cost i⋅τ. With ϕ∼Beta(μτ,(1−μ)τ) and μ∗=1/(c+1), approximate E\[h(ϕ)\] for h(ϕ)=ϕ(1−ϕ)^c using a second-order Taylor expansion around μ∗, noting Var(ϕ)=μ(1−μ)/(1+τ). Optimize the resulting expression in τ against the linear cost iτ , yielding the stated closed form after algebraic simplification and the nonnegativity constraint on τ.

![][image6]  

