# Fake It Till You Approximate It: Earn Your Precision 

## Abstract

[[evolutionary vs bayesian entrepreneurship]]
Bayesian entrepreneur's success stems not from innate traits but from how founders translate environmental challenges into adaptive capabilities. I develop a framework where entrepreneurs act as modelers who continuously update their venture designs based on environmental feedback. Two principles emerge: ventures must limit operational complexity to maintain bold aspirations, and must reduce information-integration costs to earn strategic precision. Simplify to aspire, acculturate to concentrate. These principles explain why some ventures adapt while others fail. Tesla succeeded by starting flexible and earning precision through systematic experimentation; Better Place failed by committing to rigid precision despite high complexity. Our model shows that success probability isn't given—it's constructed through deliberate choices about how much to know and when. This transforms entrepreneurship from a game of prediction to one of calibrated adaptation, where the ability to manage uncertainty becomes the core capability. 

***Keywords**: Bayesian and Evolutionary entrepreneurship, Hierarchical Model, Calibration, Flexibility*

*It appears to be a general principle that, whenever there is a randomized way of doing something, then there is a nonrandomized way that delivers better performance but requires more thought. \- E.T. Jaynes.*

So we beat on, boats against the current, borne back ceaselessly into the past.  -  The Great Gatsby

🚨todo1: imagine you're 공자 who knows english. translate 견리사의 in english so that its meaning is not lost in translation
🚨🚨todo2: lsyntax and semantics
🚨🚨🚨todo3: replace firebreak's width as openspace related with dna - 
🚨🚨🚨🚨todo4: extract from 🗣️chat with leke 🚨🚨🚨🚨
🚨🚨🚨🚨🚨todo5: after inferring the systematic design of the paper, update its roadmap. 유기적 구성과 논리적 전개에 특히 신경쓰라 🚨🚨🚨🚨🚨
✋🚨 todo6: motivate more connection on ✋🚨
✋🚨🚨 todo7: add full citation for An et.al., (2025) AI insiders, in # 5. References ✋🚨🚨
✋🚨🚨🚨  todo8: ✋🚨🚨🚨
# 1. Introduction

Tesla and Better Place shared a vision to electrify the automobile, yet their fates diverged dramatically because they differed in one initial choice: promise precision. Both promised a sustainable transportation future, but their strategies sat at opposite poles of the confidence spectrum. Better Place committed to a tightly integrated, highly precise system of battery-swap stations—a highly specific promise requiring the entire ecosystem to conform at once. Tesla, by contrast, began with a low-τ promise—a premium sports car for a niche market—and increased precision gradually while learning from the market, expanding both its product line and charging infrastructure. I argue that the capability to dynamically manage the level of aspiration and concentration explains this fork in outcomes.

[[📜gleick11_information]]
## 1.1 Three Meanings of τ

In my model, promise precision τ is defined as **a measure of the specificity and rigidity of a venture's promise, acting as a control knob for flexibility vs. efficiency.** Three meanings of this core decision variable carries are:
1. Promise precision. High τ denotes a narrow, specific commitment; low τ denotes a broad, flexible commitment.
2. Pseudo–sample size. High τ behaves as if the founder holds substantial prior evidence.
3. Width of open space. Low τ preserves a set of latent functions not yet specified, maximizing the real option value of exaptation.

As organizations mature and face greater information-integration costs and environmental complexity, managing τ dynamically—by deliberately controlling i (information-integration cost) and c (complexity)—becomes a central task.

The structural metaphor of DNA helical tension and the strategic metaphor of firebreak width illuminate why flexibility (low τ) and efficiency (high τ) succeed under different conditions:

Table 1. Bayesian–Evolutionary Metaphors for the Flexibility–Efficiency Tension

|  | Low τ (Flexibility) | High τ (Efficiency) |
| ----- | ----- | ----- |
| DNA tension | Loose | Tight |
| Firebreak width | Wide | Narrow |
| Best-fit environment | High complexity, high information cost | Low complexity, low information cost |


Tightly wound DNA strands (high τ) replicate with high fidelity and are efficient in stable environments, but they generate little variation and thus adapt poorly to shocks. Loosely wound strands (low τ) admit variation, enabling pivots essential for survival in changing conditions. Firebreak width reflects the founder’s prior quality: a founder with a very high-quality prior (e.g., Robert Langer at MIT) can set a narrow firebreak (high τ) and pursue maximum efficiency; a less certain founder exploring novel terrain should widen the firebreak (low τ) to preserve room and time to maneuver when reality defies the initial thesis.

## 1.2 Separating Founder and Venture

- Bayesian: empirical bayes overlaps with hierarchical bayesian (Gelman, 2015; )
- Evolutionary: 

🚨🚨🚨🚨As the environment becomes more complex, higher the founder's need to improve quality of one's venture model. Imagine how the tide of 2008 economic crisis and Covid has acted upon the founders simulating and calibrating different business models 🚨🚨🚨🚨 To capture the function of quality improvement, I use hierarchical Bayesian model where founder represented as prior  Bayesian principal agent (Gelman, 2013) relationship between the founder and one's venture, I implement hierarchical Bayesian modeling to separate the founder who learns and the venture,  [[founder learns and venture adapts]] "The venture is the manifestation of the founder's learning. It adapts structurally based on what the founder has learned cognitively. The venture doesn't have independent consciousness to "learn" - it changes through the founder's updated decisions.ada" This enables simulation and calibration of a business model to raise its success probability. The separation clarifies how environmental complexity c shapes the likelihood of success and how the strategic choice of ambiguity τ shapes the prior—allowing us to model learning as belief-updating in response to venture-generated evidence (Gelman et al., 2020).


## 1.3. Bridging Schools of Thought

The framework bridges the false dichotomy between the action school, which values flexibility and emergence, and the planning school, which values detailed prediction and commitment. In our model, the pure action school corresponds to the limit τ → 0 (maximal openness), and the pure planning school corresponds to τ → ∞ (absolute confidence in a single plan). Placing the two schools on the spectrum, I prescribe founders to grow from low to high τ to empirically calibrating their aspiration and venture's promise level against the environment's complexity one senses. This aligns with Bastone (2000)'s perspective where information is defined as difference that causes difference.  Venture' growth, as differentiation, can be view   reflects   against   my theory prescribes founders to gradually increase τ  venture should grow τ These are endpoints of a continuum. Rather than “decision-making under uncertainty,” I model decision-making on uncertainty itself, offering a new perspective for strategy.

simplify to aspire, sync to concentrate. mu propto 1/complexity, tau,  propto

## 1.4. Roadmap for the Paper

🚨🚨🚨🚨🚨I proceed with a “what–why–how–so what” logic. Section 2 develops the theory of τ, its structural and strategic metaphors grounded in Bayesian and Evolutionary math. Section 3 applies the framework to Tesla and Better Place, showing how it explains real-world success and failure. Section 4 envisions future works in both theory and practice.🚨🚨🚨🚨🚨

# 2. Theory and Model

### 2.1 Prior Bodies of Literature 

#### 2.1.1 Anatomy of Success Probability

The entrepreneurship literature has long been divided by a fundamental epistemological schism regarding the nature of opportunity and success probability. The planning school, exemplified by Porter’s (1980) competitive positioning framework and extended by Camuffo et al. (2020) through their scientific approach to founderial decision-making, posits that systematic analysis and hypothesis testing can reduce uncertainty to manageable proportions. This tradition, rooted in industrial organization economics (Bain, 1956; Mason, 1939), treats success probability as an exogenous market characteristic that founders must discover through rigorous analytical processes. Conversely, the action school, pioneered by Sarasvathy’s (2001) effectuation theory and complemented by Baker and Nelson’s (2005) bricolage construct, argues that opportunities emerge through founderial action rather than analytical discovery. March’s (1991) exploration-exploitation framework provides the theoretical underpinning for this perspective, suggesting that under conditions of radical uncertainty, experimentation supersedes planning. Yet both schools share a critical limitation: they treat success probability as exogenous to founderial choice, differing only in their prescribed methods for navigating this given constraint. However, this is odd. If founder can't have any influence on one's venture success, what's the point of founderial education? Also, if venture success probability is exogenous, does it matter who founds the venture? Does this one core assumption in decision making model negate > 1000 founderhsip literature reporting "nature" aspect of entrepreneurship, finally terminating the greatest myth of entrepreneurship that founders are born? (Agrawal, 2025)

Our theoretical contribution fundamentally reconceptualizes success probability through a double reparameterization that transforms it from an exogenous constraint to an endogenously designed variable. Building on recent advances in Bayesian decision theory (Gelman et al., 2020\) I decompose success probability P into promise level φ, which I further decompose into aspiration μ and precision τ. This decomposition reveals that founders possess three strategic levers—φ\*, μ\*, and τ\*—through which they actively construct rather than merely respond to their probability landscape. The failure of Better Place, despite $850 million in funding and seemingly perfect planning (Etzion & Struben, 2023), versus Tesla’s trajectory from ambiguous promises to market dominance (Teece, 2018), cannot be explained by existing frameworks that treat success as exogenously determined. Our model demonstrates that Better Place’s high precision parameter (τ → ∞) created what I term a “learning trap,” (proposition1) while Tesla’s initially low τ preserved what Keats (1817) called “negative capability”—the capacity to remain comfortable with uncertainty. This reconceptualization transforms the founder from what Kirzner (1973) termed an “alert discoverer” to what I propose as an “uncertainty architect.”

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

#### 2.1.3 Tau Counts Bayesian Heads
##### 2.1.3.1 Bayesian entrepreneurship

“Bayesian entrepreneurship” reconceives the founder’s cognition as a computational inference system, not merely the application of probabilistic language. Agrawal et al. (2024) articulate how founders possess heterogeneous, relatively strong priors and update them systematically via Bayes’ rule—casting founders as active theorists (Felin & Zenger, 2009; Zellweger & Zenger, 2023). RCT evidence (Camuffo et al., 2020, 2024\) shows model-based hypothesis testing approaches improve termination, pivoting, and performance; Novelli & Spina (2024) highlight the role of causal reasoning, in line with hierarchical Bayesian cognitive models (Griffiths and Tenenbaum, 2017; Tenenbaum, 1998). Current frontiers integrate individual and population-level learning (Li et al., 2023), i.e., meta-learning across venture populations.

summarize 
1. among what [[Infer Josh and Scott's Mind and Market.pdf]] saying is missing and suggesting for the next step in current bayesian entrepreneurship literature 
	1. sample-based approach that enables resource rational reasoning
	2. hierarchical bayesian model, which is closely related with empirical bayes

> bayesian brains without probabilities (cite Sanborn et.al., 2016)
Bayesian explanations have swept through cognitive science over the past two decades, from intuitive physics and causal learning, to perception, motor control and language. Yet people flounder with even the simplest probability questions. What explains this apparent paradox? How can a supposedly Bayesian brain reason so poorly with probabilities? In this paper, we propose a direct and perhaps unexpected answer: that Bayesian brains need not represent or calculate probabilities at all and are, indeed, poorly adapted to do so. Instead, the brain is a Bayesian sampler. Only with infinite samples does a Bayesian sampler conform to the laws of probability; with finite samples it systematically generates classic probabilistic reasoning errors, including the unpacking effect, base-rate neglect, and the conjunction fallacy

Two epistemic shifts follow. First, priors and likelihoods are not merely “what” but “how”—embodied process knowledge (Gelman et al., 2017). τ is thus a meta-parameter governing strategic flexibility and learning speed. Second, I separate modeler and model (founder vs. venture), adopting Bayes not only for inference but for model development as an iterative design process.

Technically, the beta–binomial conjugate structure with a precision parameterization places execution–planning and explore–exploit on a single mathematical spectrum. Venture outcomes are sequences of Bernoulli trials (e.g., conversions, test passes), giving a Binomial likelihood. The unknown success probability ϕ has a Beta prior with mean (aspiration) μ and precision τ. Conjugacy provides clean posterior updates and ties the abstract notions of strategic certainty and flexibility to a precise statistical quantity, τ.

DNA metaphor—separating prior and likelihood. DNA tension depicts the relation between the founder’s prior (τ) and environmental constraint (c). Sellability vs. deliverability is encoded in the likelihood: as c rises, deliverability of any promise ϕ drops steeply. τ, in turn, governs how strongly the prior weighs against new data. Low τ protects flexibility and learnability (more weight on data) but may hamper resource mobilization; high τ aids mobilization (more weight on prior) but risks rigidity when wrong.

![][image2]

Graphically, priors with different τ (e.g., Beta(0.5,0.5), Beta(1,1), Beta(2,2)) illustrate Ignore → Attention → Know stages; posterior dynamics visualize Contraction / Compromise / Containment under new data—showing that τ is the control knob for learning speed and pivot capacity.

##### 2.1.3.2 Evolutionary entrepreneurship

- Fine, C. H., Padurean, L., & Naumov, S. (2022). _Operations for entrepreneurs: Can OM make a difference in entrepreneurial theory and practice?_ Production and Operations Management, 31(12), 4599–4615.  
    → 창업 맥락에서 **운영관리 도구와 클록스피드** 개념을 적용해야 한다는 논의[](https://www.dropbox.com/preview/Angie.H%20Moon/house%20in%20boston/ops4entrep_quality_stakeholder.pdf)
    
    [ops4entrep_quality_stakeholder](https://www.dropbox.com/preview/Angie.H%20Moon/house%20in%20boston/ops4entrep_quality_stakeholder.pdf)
    
    .
    
- Joglekar, N. R., & Lévesque, M. (2013). _The role of operations management across the entrepreneurial value chain._ Production and Operations Management, 22(6), 1321–1335.  
    → 신생기업이 성장 단계별로 **운영 설계, 실험, 스케일링**을 어떻게 다뤄야 하는지 분석[](https://www.dropbox.com/preview/Angie.H%20Moon/house%20in%20boston/ops4entrep_quality_stakeholder.pdf)
    
    [ops4entrep_quality_stakeholder](https://www.dropbox.com/preview/Angie.H%20Moon/house%20in%20boston/ops4entrep_quality_stakeholder.pdf)
    
    .
    
- Packard, M. D., Clark, B. B., & Klein, P. G. (2017). _Uncertainty types and transitions in the entrepreneurial process._ Organization Science, 28(5), 840–856.  
    → 창업자가 직면하는 **불확실성의 유형과 전환**을 정리, 왜 **정밀도를 서서히 획득**해야 하는지를 뒷받침[](https://www.dropbox.com/preview/Angie.H%20Moon/house%20in%20boston/ops4entrep_quality_stakeholder.pdf)
    
    [ops4entrep_quality_stakeholder](https://www.dropbox.com/preview/Angie.H%20Moon/house%20in%20boston/ops4entrep_quality_stakeholder.pdf)
    
    .
    
- Fisher, G., Kotha, S., & Lahiri, A. (2016). _Changing with the times: An integrated view of identity, legitimacy, and new venture life cycles._ Academy of Management Review, 41(3), 383–409.  
    → 신생기업이 **단계별로 정체성과 정당성을 조정**해야 함을 보여주며, τ를 한 번에 고정하는 것의 위험성을 설명[](https://www.dropbox.com/preview/Angie.H%20Moon/house%20in%20boston/ops4entrep_quality_stakeholder.pdf)
    
    [ops4entrep_quality_stakeholder](https://www.dropbox.com/preview/Angie.H%20Moon/house%20in%20boston/ops4entrep_quality_stakeholder.pdf)
    
    .
    
- Sarasvathy, S. D. (2001). _Causation and effectuation: Toward a theoretical shift from economic inevitability to entrepreneurial contingency._ Academy of Management Review, 26(2), 243–263.  
    → **플래닝 vs 액션(효과화)** 논쟁의 대표 논문. 본 논문은 이 둘을 **τ의 동적 관리**라는 틀로 통합.
    
Beyond biological analogy, evolutionary entrepreneurship fuses complex adaptive systems with operations science. 🚨Fine (1986; Fine & Li, 1988; Fine & Freund, 1990\) modeled learning and flexibility–efficiency trade-offs; Clockspeed (Fine, 1998\) formalized industry-specific evolutionary tempos; Fine et al. (2002) developed rapid-response capability across value chains; Operations for founders (Fine, 2022\) offers the Nail–Scale–Sail framework and ten scaling tools. Opportunities that form at the boundary of the value chain, and options values🚨 [[founder learns and venture adapts]]

- Integral needs multiple functions and the open space allows ambidextrity
- 3 dimensional concurrent engineering on the hierarchy of organizational, process, product and feedback within
Felin & Kauffman (2021a; 2021b) extend this with the adjacent possible, explaining how opportunity arises from the current frontier of technology, markets, and resources. Functional excess and experimentation power disruptive evolution, dovetailing with exaptation (Gould & Vrba, 1982). With Bateson’s (1963) somatic flexibility, low τ preserves slack that can be repurposed. BYD's battery Slack’s pivot from gaming to enterprise communication exemplifies how low-τ assets enable exaptation. ✋🚨
Using literature on exaptation in entrepreneruship [[📜Andriani_exaptation_creativity_source]] [[📜laporta20_understanding Innovation Through Exaptation]], [[🛠️exaptation_spandrel]], synthesize one paragraph that 
1. describes how i'm using wide definition of adaptation that includes direct adaptation (optimization of trait for its original function) and co-option (adding new functions while maintaining original), and co-opted adaptation (complete shift to new function from original).
2. prescribes acculturating permeable, porous, open space as implementation of tau knob 
3. analyze Moderna's culture of parallel entrepreneurship and active pivot that [[noubar_afeyan]]; "
- You explore a diverse set of opportunities (variation), select promising ventures that passed the test (selection), refine these ventures based on feedback (mutation and crossover). " genetic algorithm 
- leverage the evolutionary engine of co-opted adaptation, ✋🚨

| Aspect                  | Direct Adaptation (Narrow) 🎯                                                                                                                                           | 🟩Exaptation1 Co-option (sequential)🎨                                                                                                                                                                              | 🔴Exaptation2  Co-opted adaptation (parallel)🛠️                                                                                                                                                                                                      |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Definition**          | Optimization of trait for its original function                                                                                                                         | Adding new functions while maintaining original                                                                                                                                                                     | Complete shift to new function from original                                                                                                                                                                                                          |
| **Process**             | Continuous refinement through selection                                                                                                                                 | Accumulation of additional functions                                                                                                                                                                                | Transformation of functional role                                                                                                                                                                                                                     |
| **Selection Pattern**   | Single directional pressure                                                                                                                                             | Multiple simultaneous pressures                                                                                                                                                                                     | Shift in selective pressure                                                                                                                                                                                                                           |
| **Original Function**   | 💪 Enhanced and optimized                                                                                                                                               | 🤹Maintained at functional level                                                                                                                                                                                    | 👋 Left behind                                                                                                                                                                                                                                        |
| **Biological Examples** | • 🦒Giraffe neck length for reaching leaves<br>• 🐆Cheetah speed for hunting<br>• 🌵Cactus spines for water retention<br>• 🐻‍❄️Polar bear fur thickness for insulation | • 🪶Bird feathers: insulation → insulation + flight<br>• 🐧Penguin wings: flight → flight + swimming<br>• 🤲Human hands: climbing → climbing + tool use<br>• 🐢Turtle shell: mineral storage → protection + storage | • 🫁 Fish bladder → lungs<br>• 🦖Dinosaur scales → feathers<br>• 👂Jaw bones → ear bones<br>• Heat shock proteins → lens crystallins                                                                                                                  |
| **Business Examples**   | • 🚗Car engine efficiency improvements<br>• 🔋Battery life optimization<br>• 🔍Search algorithm refinement<br>• ⚙️ Manufacturing process optimization                   | • 📚Amazon: books → books + general retail<br>• 🎬Netflix: DVD rental → streaming + production<br>• 🔎 Google: search → search + advertising<br>• 📱Twitter: messaging → messaging + news                           | 📧email (ftp protocol)<br>🏎️speedbox (same engine, go faster)<br>• 🎨 Play-Doh: wallpaper cleaner → toy<br>• 💊Viagra: heart medicine → ED treatment<br>• 📸Instagram: check-in app → photo sharing<br>• 💬 Slack: game company tool → business chat |

🚨🚨🚨Firebreak metaphor—strategic ambiguity as containment. A wide firebreak (low τ) is prudent where fire (market dynamics) behaves unpredictably: you concede uncertainty and create defendable space away from the fire’s edge. Low-τ founders adopt containment; high-τ founders adopt contraction—efficient when fires are small, catastrophic when they jump the line.🚨🚨🚨

## 2.2 Modeling “Fake It Till Approximate It”

Table 3\. Key Model Variables

| Variable | Definition | Interpretation | Example (Tesla vs. Better Place) |
| ----- | ----- | ----- | ----- |
| μ | Aspiration (mean of belief distribution) | Boldness of the promise | Tesla (μ≈0.3): “200+ miles.” Better Place (μ≈0.9): “Infinite range.” |
| τ | Precision  | Specificity/rigidity of the promise | Tesla (τ≈1): “\~200 miles (±40).” Better Place (τ≈4): “Exactly 3 minutes.” |
| C | Operational complexity | \# of independent, critical components | Tesla (n≈5): pack, motor, software. Better Place (n≈10): robotics, real estate, standards, OEMs. |
| I | Information-integration cost | Marginal cost to raise τ by one | Tesla: prototype iteration. Better Place: nationwide swap network. |
| V | Venture value | Value upon successful delivery | E.g., market cap or TAM. |

​​2.4 Model: From “Fake It Till Make It” to “Approximate It”
![[🗄️🐅likelihood_updated.svg]]

**Figure1.** This figure makes transparent how an founder’s epistemology matures: In M1, the promise φ is monotonically linked to success probability; in M1′, nature’s complexity c bends that monotonicity into a concave shape, so the same promise has different effective impact. By M2, I treat promises as a distribution by reparameterizing venture's promise with founder's aspiration μ; in M2′, the founder chooses the design variable τ to approximate that distribution, adopting rational ignorance as a strategy by balancing it against the meaning-construction cost i. Ultimately, it offers a grammar for deciding scientifically not “to know more,” but “when and what to leave unknown,” and that grammar is the bridge that reunifies the planning school and the action school along a single continuum.


Table. Comparative schematic of four Bayesian decision models (with generative notation)

|                               | M1                            | M1′                                            | M2 (→ Proposition 1)                                                                                       | M2′ (→ Proposition 2)                                                                                                                    |
| ----------------------------- | ----------------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Generative process**        | $S \sim \text{Bern}(\phi)$    | $S\land D \sim \text{Bern}(\phi(1-\phi)^c)$    | $S\land D \sim \text{Bern}(\phi(1-\phi)^c)$<br>$\phi \sim \text{Beta}(\mu,1)$                              | $S\land D \sim \text{Bern}(\phi(1-\phi)^c)$<br>$\phi \sim \text{Beta}(\mu\tau,(1-\mu)\tau)$                                              |
| **Objective**                 | $\max_{\phi} P(S\|\phi)=\phi$ | $\max_{\phi} P(S\land D\|\phi)=\phi(1-\phi)^c$ | Same as M1′                                                                                                | Same as M1′                                                                                                                              |
| **Representative  optimizer** | $\phi^\star=1$                | $\phi^\star=1/(c+1)$                           | $\mu$ solves $\frac{1}{\mu}=\sum_{k=1}^c \frac{1}{k-\mu}$;<br>approx. $\mu^\star\approx 1/(\log c+\gamma)$ | $\frac{1}{\mu\tau}=\sum_{k=0}^c \frac{1}{(1-\mu)\tau+k}$;<br>special case $c=1$: $\mu^\star=1/2$, $\tau^\star=\max\{\sqrt{V/(4i)}-1,0\}$ |
| **Interpretation**            | Pure MLE (prediction)         | MLE with complexity drag $c$ (prediction)      | Empirical-Bayes calibration of aspiration (prediction-based prescription, Prop.1)                          | Aspiration + optimal ignorance tradeoff (expected payoff, Prop.2)                                                                        |

**M1: Naive Commitment.** The founder maximizes $P(S|\phi)=\phi$, yielding $\phi^\star=1$. This trivial solution embodies the naive “fake it till you make it” mentality: always promise the maximum. It ignores complexity and is unrealistic.

**M1′: Complexity as Constraint.** With operational complexity $c$, success requires delivering through $c$ interdependent tasks: $P(S\land D|\phi)=\phi(1-\phi)^c$. Reliability engineering interprets $(1-\phi)^c$ as the chance all $c$ subsystems succeed; Bayesian inference interprets it as the likelihood of one success after $c$ failures. Either way, the optimum shifts to $\phi^\star=1/(c+1)$. Complexity tempers ambition.

**M2: Empirical-Bayes Calibration of Aspiration.** Rather than choose a fixed $\phi$, the founder sets a prior mean $\mu$ with $\tau=1$. The objective is

$$\max_{\mu}\; \int_0^1 \phi(1-\phi)^c\,p(\phi|\mu,1)\,d\phi = \max_{\mu}\;\frac{B(1+\mu,1+c-\mu)}{B(\mu,1-\mu)}.$$

This is empirical-Bayes calibration (Gelman et al., _Bayesian Data Analysis_).

**Proposition 1 (Aspiration Calibration under Complexity).** When promises face complexity $c$, optimal aspiration is calibrated downward: $\phi^\star=1/(c+1)$; equivalently, the optimal prior mean $\mu$ satisfies $\tfrac{1}{\mu}=\sum_{k=1}^c 1/(k-\mu)$ and approximates $1/(\log c+\gamma)$.

_Implication._ Aspiration falls with complexity. Better Place who had higher complexity c than Tesla could have reduced $\mu$ but did not.

**M2′: Aspiration Plus Optimal Ignorance.** Now both $\mu$ and precision $\tau$ are chosen:

$$\max_{\mu,\tau}\; V\int_0^1 \phi(1-\phi)^c\,p(\phi|\mu,\tau)\,d\phi-\tau i.$$

Another name of precision parameter $\tau$ is concentration parameter. Yet another is pseudo-sample size (Gelman et al, 2015, pseudo counts in McElreath, 2022). Deeper knowledge is expected from precise priors hence they require  more surprising data to start shifting.The first-order condition $V\frac{\partial}{\partial \tau}\,\mathbb{E}[\phi(1-\phi)^c] = i$ means marginal value equals cost, leading to Proposition 2a.

**Proposition 2a (General principle).** The optimum $(\mu^\star,\tau^\star)$ equates the marginal value of additional precision with its marginal cost.

**Proposition 2b (Special cases).**
- If $i=0$: then $\tau^\star\to\infty$ and $\mu^\star=1/(c+2)$.
- If $c=1$: then $\mu^\star=1/2$ and $\tau^\star=\max{(\sqrt{V/(4i)}-1,0)}$.

**Proposition 2c (Fixed aspiration).** For fixed $\mu$, 
$$
\tau^*\;\approx\;\sqrt{\frac{V}{i}\cdot \frac{c}{2}\,\mu\,(1-\mu)^{\,c-1}\,\big(2-(c+1)\mu\big)},\quad 0<\mu<\frac{2}{c+1}.
$$

**Interpretation** 
- $\tau^\star$ increases in proportion to venture value $V$ (high-value ventures justify more precision).
- $\tau^\star$ decreases as information-integration cost $i$ rises (higher costs discourage paying for precision).
- $\tau^\star$ also decreases as complexity $c$ rises, because each additional subsystem multiplies the downside of bold promises, so the marginal payoff from further precision is diluted.


# 3. Practice: Case, Prescription, Prediction

Section 3 validates theory developed in sec.2. links our contribution across three layers: Figure of Theory develops the theory (μ vs. c, τ vs. i, deterministic vs. probabilistic, all-in vs. sequential), Table of Practice distills this into practice (a checklist of managerial actions), and Figure Y delivers prediction (ventures that manage τ as prescribed achieve higher survival probabilities). Analyzing cases correspond to Bayesian retrodictive check while making predictions under intervention in yet unseen situation (Hoffman )is predictive check predicting is predictive check, testing the prescription is 
## 3.1 Case: Better place vs. Tesla

Sec.3.1 validates theorized benefit of probabilistic reasoning and sequential execution using case analysis. Tesla illustrates sequential approximation, while Better Place illustrates the dangers of one-shot bets. This sets the stage for practical prescriptions on how founders can deliberately manage τ through c and i.
### 3.1.1 Contrasting Reasoning Capabilities: Deterministic vs. Probabilistic

Better Place remained trapped in a deterministic M1′ frame: precise sales targets (“100k in Israel by 2011”), exact swap times (“exactly 3 minutes,” later “59.1 seconds”), and fixed station costs (“$0.5M,” actually >$2M). Excess precision structurally blocked learning. Tesla, by contrast, operated in an M2′ mode: it reframed “250 miles” as “200+ miles,” preserving legitimacy while allowing updates. Early Roadsters were used as paid experiments to probe elasticity, preferences, and demand. Independent validations were published and targets revised transparently. Starting with low τ and gradually raising it through staged learning, Tesla treated aspiration and precision as design variables to be earned, not assumed.

Panels (a) and (b) of Figure of theory formalize this logic. Panel (a) shows how **aspiration ($\mu^*$) is constrained by complexity**: only by simplifying interdependencies could Tesla maintain ambitious goals. Panel (b) shows how **precision ($\tau^*$) depends on integration cost**: Tesla lowered ii to justify tighter commitments, while Better Place ignored its high ii and locked in rigid precision. These dynamics mark the transition from deterministic M1′ reasoning to probabilistic M2′ reasoning.

### 3.2.2 Contrasting Approximation Strategies: All-in vs. Sequential Sampling
Better Place exemplified a **one-shot bet** strategy. From inception it invested roughly $850M in a nationwide battery-swap infrastructure, precommitting to a single, rigid high-τ posterior. This strategy resembled deterministic reasoning: management assumed that a precise ex-ante plan could substitute for adaptation. As a result, when sales stalled (~1,400 units) and external signals pointed to shifting demand and standards, Better Place had locked itself into what I call a “worse posterior place.” Its prior was so tight that new evidence could not meaningfully shift its commitments.

Tesla, by contrast, approximated uncertainty through **sequential sampling**. Musk’s 2006 “Secret Master Plan” staged learning deliberately: (1) sports car, (2) mid-price car, (3) mass-market car, (4) solar integration. Each stage funded and informed the next, with production ramping 2.5k → 50k → 500k and τ increasing stepwise. Tesla treated each product launch as a posterior update, raising precision only after accumulating evidence that complexity (ccc) had been simplified and integration cost (iii) reduced.

Panel (c) of Figure of theory illustrates these dynamics. A high-τ prior, like Better Place’s, barely shifts after observing failure, leading to **containment and rigidity**. A low-τ prior, like Tesla’s, shifts substantially, allowing **contraction and adaptation**. This visualization clarifies why both extremes of the traditional schools are maladaptive: the **action school** risks remaining under-committed with perpetually low τ, while the **planning school** locks in prematurely with high τ. Our synthesis shows that τ should neither remain low nor be set high a priori, but should **grow only as ventures simplify complexity and acculturate integration.**

---
![[Pasted image 20250920090028.png]]

**Figure of Theory. Bayesian foundations of entrepreneurial adaptation.**  
Panel (a) shows that optimal aspiration $\mu^*$ declines with complexity (c): Tesla, with fewer subsystem interdependencies, could aspire higher than Better Place.  
Panel (b) shows that optimal precision $\tau^*$ rises as information-integration cost (i) falls: Tesla lowered ii during _production hell_, earning precision adaptively, while Better Place sustained high ii yet committed to high precision prematurely.  
Panel (c) shows how priors update into posteriors. A low-τ prior (Tesla) contracts significantly upon observing failure, enabling rapid pivots, whereas a high-τ prior (Better Place) barely shifts, leading to containment and rigidity.  
Together these panels illustrate our central argument: **aspiration must be simplified, and precision must be acculturated, or else evidence fails to translate into adaptation.**


## 3.2 Prescription: Simplify to Aspire, Sync to Concentrate

Panels (a) and (b) of Figure X provide the theoretical foundation for our prescriptions. Panel (a) shows that optimal aspiration μ∗ is inversely related to complexity c: unless ventures deliberately simplify, aspirations will collapse as interdependencies grow. Panel (b) shows that optimal precision τ∗ rises only when information-integration cost i is reduced: precision cannot be assumed; it must be earned through organizational design. Together, these panels formalize our two principles: **simplify to aspire** and **acculturate to concentrate**.

Table of Practice translates these principles into a practitioner’s checklist. Each row links a diagnostic question to methods for reducing either complexity or integration cost, and illustrates success through Tesla’s trajectory and failure through Better Place’s. Tesla consistently simplified and lowered integration cost before raising the specificity of its commitments, thereby earning precision. Better Place, by contrast, began with precise promises despite high complexity and high integration cost, locking itself into rigidity.

**Table of Practice. Precision Management Checklist with Illustrative Examples**

| Lever                    | Diagnostic Question                                                  | How to Reduce                                                                                                 | Success Example (Tesla)                                                                                                                                                                            | Failure Example (Better Place)                                                                        |
| ------------------------ | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Integration Cost (i)** | Are organizational _clockspeeds_ synchronized with external signals? | Acculturate (Fine, 2022); flatten structures; build shared vocabulary; codify heuristics for rapid iteration. | During its struggle to deliver roadster, Musk emphasized speed over perfection, kept “gates open” to release parts, corrected errors quickly, and unified teams with terms like “production hell.” | Fragmented teams and inconsistent vocabularies slowed adaptation and kept i high.                     |
| **Complexity (c)**       | How many subsystems must succeed simultaneously?                     | Challenge assumptions; focus on one dominant “physics”; serialize breakthroughs.                              | Tesla rejected the “battery swap” assumption and concentrated on battery packs, reducing subsystem interdependencies.                                                                              | Better Place pursued robotics, real estate, utilities, and OEM standards in parallel, raising c.      |
| **Precision (τ)**        | Is specificity matched to earned reductions in i and c?              | Link commitments to demonstrated progress; increase τ only after lowering i and c.                            | Tesla staged promises: broad vision → 200+ mile range → Model 3 at $35,000 → multi-million-unit forecasts.                                                                                         | Better Place launched with “3-minute swaps at 500,000 stations,” unsupported by reductions in i or c. |

This table conveys the essence of our prescription. Tesla reduced i and c before raising τ; Better Place did the opposite. Investors and educators can apply this framework to assess whether founders are earning precision or prematurely locking it in.

## 3.3 Prediction: A Hierarchical Bayesian Analysis of Founder Language

I move from cases to testable predictions by treating **founder language as a window into prior precision (τ) and aspiration (μ)**. Rigid, quantified, time-bound promises signal high τ; broader, more flexible claims signal low τ\tau. Using a hierarchical Bayesian model applied to pitch decks, investor updates, and public communications, I can estimate venture-specific trajectories of μ\mu and τ\tau, then link them to outcomes such as survival, funding, and pivots.

This approach builds on prior work showing that strategy must be studied at the firm-specific level rather than through average effects (Mackey, Barney, & Dotson, 2017). It resonates with evidence that decision-makers infer unobserved “phantom attributes” from observed signals (Bell & Dotson, 2022), suggesting that investors infer venture feasibility from the precision of founder communication. It also aligns with the resource-based view recast as a stochastic process (Wibbens, 2021), as I model aspiration and precision as dynamic latent states. 

From these foundations, our propositions yield straightforward hypotheses: ventures that start with low τ and raise it gradually as c and i decline will outperform those that begin with high τ despite high c and i. **Figure of Prediction** visualizes these predictions: Tesla-like “earned precision” trajectories sustain higher survival probabilities, while Better Place–like “premature precision” paths collapse quickly.

 Problem remains how to gather optimal entrepreneurs who behaves (1) **simplify to aspire**: aspiration falls as complexity (c) rises; (2) **acculturate to concentrate**: precision rises only as integration cost, acknowledged as "Bayesian Entrepreneurs are not commonly found in the wild" (Arora, 2025). 
![[Fig(predict).png]]

**Figure of Prediction. Predicted venture survival under different precision trajectories.**  
This figure visualizes our prediction: ventures that manage precision as prescribed—**simplifying to sustain aspiration and acculturating to earn concentration—exhibit higher survival probabilities** (red, Tesla-like trajectory). Ventures that assume high precision prematurely despite high complexity and integration cost collapse quickly (skyblue, Better Place-like trajectory). This completes the sequence: **Figure of Theory shows the theory, Table of Practice distills it into practice, and the Figure of Prediction demonstrates the expected performance consequences.**

## 4\. Conclusion and Vision

### 4.1 Conclusion
Venture's success probability is anatomized (sec.2.1), unified (sec.2.2), reasoned, programmed, and implemented around the relationship between founder and its venture's probabilistic adaptation. I reframe promises as an aspiration–precision prior, with aspiration (μ) constrained by complexity (c) and precision (τ) earned only as integration costs (iii) fall. The central prescription is simple but powerful: **simplify to aspire, acculturate to concentrate.** This unifies the long-standing **action school** (which tends to remain at low τ) and the **planning school** (which assumes high τ ex ante) by showing how ventures can move from low to high precision gradually, through deliberate simplification and acculturation. Therefore, I translate one layer of founder's nature into nurture i.e. into principles to manage complexity, information, and precision over time.

### 4.2 Vision by Target Users

- **For Theorists.** Building on Unifying Bayesian and evolutionary perspectives by implementing aspiration, concentration, promise (bits) with bodies of founder and venture and approximating the promise distribution with samples (atoms). Open questions remain on how founders capable of prediction-based prescription not only adapt to but also shape their environments. What implication does this have on irreversibility and path dependency? Just as aging is not an universal phenomenon (An et.al., 2025), can firm's aging also be understood as a choice? Whatever the answer is startups are great fruit fly model (Fine, 2000) to test anti-aging hypotheses.
    
- **For Empiricists.** Founder language offers a measurable proxy for τ. Hierarchical Bayesian methods enable estimation of heterogeneous trajectories of aspiration and precision, moving beyond average effects and IV-limited designs (Mackey et. al., 2015, Mackey and Dotson, 2024).
    
- **For Founders.** Precision must be earned. Simplify world model () which assumption matters, reduce integration costs, and stage commitments so that τ increases only as the venture learns. Managing ignorance deliberately becomes a central capability.
    
- **For Educators, Investors, and Policymakers.** Assess not just vision (μ) but calibrated realism (dynamic τ). Teach and evaluate when ventures should favor flexibility or efficiency, grounding these judgments in measurable c and i rather than slogans.

## 5\. References

An, K., Hwang, M., Kim, Y., Lee, H., Park, J., Hong, H., Sol, H., Moon, H., & Han, S. (2025). _AI insiders: Future report by global top-tier experts_. Smartbooks.

*Agrawal, A., Gans, J., & Stern, S. (Eds.). (2024). Bayesian entrepreneurship. MIT Press.*

*Brinkerink, J. (2025). Negative Capability and founderial Action. Strategic Change.Baker, C. L.,* 

*Saxe, R., & Tenenbaum, J. B. (2011). Bayesian theory of mind: Modeling joint belief-desire attribution. Proceedings of the Annual Meeting of the Cognitive Science Society, 33, 2469-2474.*

*Baker, C. L., Jara-Ettinger, J., Saxe, R., & Tenenbaum, J. B. (2017). Rational quantitative attribution of beliefs, desires and percepts in human mentalizing. Nature Human Behaviour, 1(4), 0064\.*

*Bateson, G. (2000). Steps to an ecology of mind: Collected essays in anthropology, psychiatry, evolution, and epistemology. University of Chicago press.*

Bell, J. J., & Dotson, J. P. (2022). Phantom attributes: Unpacking product perceptions. _Journal of Consumer Research, 49_(3), 523–546.

*Camuffo, A., Cordova, A., Gambardella, A., & Spina, C. (2020). A scientific approach to founderial decision making: Evidence from a randomized control trial. Management Science, 66(2), 564-586.*

*Camuffo, A., Gambardella, A., Messinese, D., Novelli, E., Paolucci, E., & Spina, C. (2024). A scientific approach to founderial decision making: Large scale replication and extension. Strategic Management Journal, forthcoming.*

Dotson, J. P. (2010). Strategic satisfaction and decision-making under uncertainty. _Strategic Management Journal, 31_(5), 457–477.

*Felin, T., & Kauffman, S. (2021a). Disruptive evolution: Harnessing functional excess, experimentation and science as tool. Industrial and Corporate Change, 30(2), 446-466.*

*Felin, T., & Kauffman, S. (2021b). The search function and evolutionary novelty. In S. Kauffman (Ed.), A world beyond physics (pp. 122-145). Oxford University Press.*

*Felin, T., & Zenger, T. R. (2009). founders as theorists: On the origins of collective beliefs and novel strategies. Strategic entrepreneurship Journal, 3(2), 127-146.*

*Fine, C. H. (1986). Quality improvement and learning in productive systems. Management Science, 32(10), 1301-1315.*

*Fine, C. H. (1998). Clockspeed: Winning industry control in the age of temporary advantage. Perseus Books.*

*Fine, C. H. (2022). Operations for founders. MIT Press.*

*Fine, C. H., & Freund, R. M. (1990). Optimal investment in product-flexible manufacturing capacity. Management Science, 36(4), 449-466.*

*Fine, C. H., & Li, L. (1988). Technology choice, product life cycles, and flexible automation. Journal of Manufacturing and Operations Management, 1(4), 372-399.*

*Fine, C. H., Vardan, R., Pethick, R., & El-Hout, J. (2002). Rapid-response capability in value-chain design. MIT Sloan Management Review, 43(2), 69-75.*

*Gelman, A., & Shalizi, C. R. (2013). Philosophy and the practice of Bayesian statistics. British Journal of Mathematical and Statistical Psychology, 66(1), 8-38.*

*Gelman, A., Simpson, D., & Betancourt, M. (2017). The prior can often only be understood in the context of the likelihood. Entropy, 19(10), 555\.*

*Gould, S. J., & Vrba, E. S. (1982). Exaptation--a missing term in the science of form. Paleobiology, 8(1), 4-15.*

*Griffiths, T. L., & Tenenbaum, J. B. (2009). Theory-based causal induction. Psychological review, 116(4), 661\.*

*Huh, W. T., Kim, M. J., & Lin, M. (2025). Uncertain search with knowledge transfer. Management Science.*

Jake M. Hofman 1,17 ✉ , Duncan J. Watts 2,3,4,17 ✉ , Susan Athey5 , Filiz Garip6 , Thomas L. Griffiths7,8 , Jon Kleinberg9,10 , Helen Margetts11,12 , Sendhil Mullainathan13 , Matthew J. Salganik6 , Simine Vazire14, Alessandro Vespignani 15& Tal Yarkoni16 Integrating explanation and prediction in computational social science

*Jara-Ettinger, J., Gweon, H., Schulz, L. E., & Tenenbaum, J. B. (2016). The naïve utility calculus: Computational principles underlying commonsense psychology. Trends in cognitive sciences, 20(8), 589-604.*

*Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. Econometrica, 47(2), 263-291.*

*Knight, F. H. (1921). Risk, uncertainty and profit. Houghton Mifflin.*

*Mackey, T., & Dotson, J. (2024). Bayesian Statistics in Management Research: Theory, Applications, and Opportunities. Oxford Research Encyclopedia of Business and Management.*

*Novelli, E., & Spina, C. (2024). Causal reasoning and the scientific founder. In A. Agrawal, J. Gans, & S. Stern (Eds.), Bayesian entrepreneurship (Chapter 6). MIT Press.*

*Phillips, J., Morris, A., & Cushman, F. (2019). How we know what not to think. Trends in Cognitive Sciences, 23(12), 1026-1040.*

*Sarasvathy, S. D. (2001). Causation and effectuation: Toward a theoretical shift from economic inevitability to founderial contingency. Academy of Management Review, 26(2), 243-263.*

*Skali Lami, O. (2022). Predictive and Prescriptive Analytics in Operations Management (Doctoral dissertation, Massachusetts Institute of Technology).*

*Tenenbaum, J. (1998). Bayesian modeling of human concept learning. Advances in neural information processing systems, 11\.*

*Zellweger, T., & Zenger, T. (2023). founders as scientists: A pragmatist approach to producing value out of uncertainty. Academy of Management Review, 48(3), 379-408.*


    
- Sanborn, A. N., & Chater, N. (2016). Bayesian brains without probabilities. _Trends in cognitive sciences_, _20_(12), 883-893.
    
- Mackey, T. B., Barney, J. B., & Dotson, J. P. (2017). Corporate diversification and the value of individual firms: A Bayesian approach. _Strategic Management Journal, 38_(3), 322–341.
    
- Wibbens, P. D. (2021). A formal framework for the RBV: Resource dynamics as a Markov process. _Strategic Management Journal, 42_(1), 3–29.
    

---

👉 Would you like me to also **sketch Figure Y** (the prediction figure) so that it mirrors Figures X and Table X — i.e., theory → practice → prediction — with Tesla-like and Better Place–like survival curves side by side?
# Appendix A. Dictionary of Key Terms

**Aspiration–precision prior.** A Beta distribution parameterized by mean $\mu$ (aspiration) and precision $\tau$. Encodes how bold ($\mu$) and how rigid ($\tau$) a founder’s promise is.

**Aspiration ($\mu$).** The mean of the prior distribution; represents the boldness of the promise.

**Precision ($\tau$).** The concentration of the prior distribution; interpretable as pseudo–sample size, the rigidity of the promise, or the degree of prior evidence.

**MLE (Maximum Likelihood Estimation).** A classical method that chooses parameter values to maximize the likelihood of observed data.

**Empirical Bayes.** A procedure that estimates prior parameters (like $\mu$ or $\tau$) by maximizing the marginal likelihood of the data 

**Hierarchical Bayes.** A Bayesian modeling strategy where parameters (such as $\phi$) themselves have distributions governed by hyperparameters (such as $\mu,\tau$). Integrating over these priors yields predictive distributions.

**Prior.** A probability distribution placed on a parameter before observing current data; represents prior knowledge (**not information**).

**Ignorance prior.** A deliberately vague or low-precision prior, chosen to reflect high flexibility and openness to evidence.

**Marginal likelihood.** The probability of data integrated over the prior distribution: $\int p(data|\phi)p(\phi|\mu,\tau)d\phi$. Used for model comparison and empirical Bayes calibration.

**Value of information (VOI).** The increase in expected payoff from gaining additional precision; in M2′ this trades off against the integration cost $i$.

**Optimal ignorance.** The principle that precision should only be raised until its marginal value equals its marginal cost; beyond that, it is optimal to remain ignorant (low $\tau$).


# Appendix B

### Proof of Proposition 1

Derivative of $\phi(1-\phi)^c$ gives condition $1/\phi-\sum_{k=1}^c 1/(k-\phi)=0$. Unique interior solution yields $\phi^\star=1/(c+1)$. In empirical-Bayes form, maximize $B(1+\mu,1+c-\mu)/B(\mu,1-\mu)$. Taking derivative yields $1/\mu=\sum_{k=1}^c 1/(k-\mu)$. For large $c$, harmonic approximation $H_c\sim \log c+\gamma$ gives $\mu^\star\approx1/(\log c+\gamma)$.

### Proof of Proposition 2a  (General principle)

Start with objective $g(\mu,\tau)=V\mathbb{E}[\phi(1-\phi)^c]-\tau i$ with $\phi\sim\text{Beta}(\mu\tau,(1-\mu)\tau)$. Differentiating with respect to $\tau$ and setting to zero gives marginal benefit = cost.

### Proof of Proposition 2b (Special cases)
- If $i=0$, $\tau^\star\to\infty$ and $\mu^\star=1/(c+2)$.
    
- If $c=1$, $\mathbb{E}[\phi(1-\phi)]=\mu(1-\mu)\tau/(\tau+1)$. Maximizing over $\mu$ gives $\mu^\star=1/2$. Then $g(1/2,\tau)=V(\tau/(\tau+1))(1/4)-\tau i$. Differentiating and solving yields $\tau^\star=\max{\sqrt{V/(4i)}-1,0}$.

We’re maximizing

$$g(\mu,\tau)=V\,\mathbb{E}[\phi(1-\phi)]-\tau i,\quad \phi\sim\mathrm{Beta}(\mu\tau,(1-\mu)\tau).$$

1. **Expectation.** For $c=1$,
    

$$\mathbb{E}[\phi(1-\phi)]=\frac{\alpha\beta}{(\alpha+\beta)(\alpha+\beta+1)}=\frac{\mu(1-\mu)\,\tau}{\tau+1},$$

with $\alpha=\mu\tau,\ \beta=(1-\mu)\tau$.

So

$$g(\mu,\tau)=V\,\frac{\tau}{\tau+1}\,\mu(1-\mu)-\tau i.$$

2. **Maximize w.r.t. $\mu$ (hold $\tau$ fixed).**
    

$$\frac{\partial}{\partial\mu}[\mu(1-\mu)]=1-2\mu.$$

Set to zero: $1-2\mu=0\Rightarrow \mu^\star=1/2$.

3. **Substitute $\mu^\star=1/2$.**
    

$$g(1/2,\tau)=V\,\frac{\tau}{\tau+1}\,\tfrac14-\tau i.$$

4. **Differentiate w.r.t. $\tau$.**
    

$$\frac{d}{d\tau}\left(\frac{\tau}{\tau+1}\right)=\frac{1}{(\tau+1)^2}.$$

So

$$\frac{\partial g}{\partial \tau}=V\cdot\tfrac14\cdot\tfrac{1}{(\tau+1)^2}-i.$$

5. **Solve.**
    

$$\frac{V}{4(\tau+1)^2}=i\Rightarrow (\tau+1)^2=V/(4i)\Rightarrow \tau^\star=\max\{\sqrt{V/(4i)}-1,0\}.$$

---

### Appendix C: Miscellaneous for future Angie 
#### Simple Rule for Optimal Precision $\tau^*(\mu,c)$

##### Level 1: Parsimonious Plug-in Formula

I derive a simple approximation for the optimal precision level that balances value creation against information costs. The optimal precision can be expressed as:

$$\boxed{\tau^*(\mu,c;V,i) \approx \sqrt{\frac{V}{i}} \cdot \underbrace{\sqrt{\frac{c}{2}\mu}(1-\mu)^{\frac{c-1}{2}}}_{\text{core shape in }(\mu,c)} \cdot \underbrace{\sqrt{\max\{0, 2-(c+1)\mu\}}}_{\text{feasibility cap}}}$$

This expression decomposes into three multiplicative components. First, the term $\sqrt{V/i}$ represents the value–cost lever that scales the entire precision surface upward or downward based on the ratio of value creation potential to information cost. Second, the core shape function $\sqrt{(c/2)\mu}(1-\mu)^{(c-1)/2}$ captures the fundamental relationship between aspiration level and complexity, exhibiting a single-peaked behavior in $\mu$. Notably, for practical aspiration levels, this component decreases in complexity $c$ after small values of $c$. Third, the feasibility cap $\sqrt{2-(c+1)\mu}$ enforces a boundary condition that drives $\tau^*$ toward zero as $\mu$ approaches $2/(c+1)$, ensuring that interior solutions require $\mu < 2/(c+1)$.

##### Level 2: One-Line Surrogate for Fast Calibration

When the feasibility constraint is not binding (specifically when $\mu \leq 1/(c+1)$), I can employ a simplified expression that omits the cap term:

$$\boxed{\tau^*(\mu,c;V,i) \approx \sqrt{\frac{V}{i}} \cdot \sqrt{\frac{c}{2}\mu}(1-\mu)^{\frac{c-1}{2}}}$$

The comparative statics of this surrogate formula reveal important managerial insights. The optimal precision increases with value potential ($\partial\tau^*/\partial V > 0$) and decreases with information cost ($\partial\tau^*/\partial i < 0$), as expected. More interestingly, for typical aspiration levels where $\mu \in (0,1/2]$, the optimal precision $\tau^*$ decreases as complexity $c$ increases. Furthermore, holding complexity fixed, $\tau^*$ exhibits single-peaked behavior in aspiration level $\mu$ over the feasible interval $(0, 2/(c+1))$.

