# Growing Success through Precision

## Abstract

Prior research in entrepreneurship and strategy often treats either venture success probability (P) or the informativeness of evidence as exogenous. I develop an endogenous mechanism for both. I reparameterize P as an aspiration–precision prior, where aspiration is passively constrained by subsystem complexity, while precision (τ) is the founder’s design lever. Choosing τ determines how strongly evidence updates the prior distribution of P, thereby endogenizing **prior-driven informativeness**.This mechanism closes the gap between **micro experimentation and macro selection**. At the micro level, ventures differ in how much they allow evidence to move them; at the macro level, markets select across these trajectories. Ventures that assume high τ prematurely resist adaptation and collapse (Better Place), while staged low→high τ trajectories absorb evidence and survive (Tesla).Theoretically, τ has **three nested meanings**: as a concentration parameter (probability level), a pseudo–sample size (sampling level), and a variation–selection balance (evolutionary level). Linking these levels shows that ventures mirror natural selection: they begin with variation (low τ) and move toward selection (high τ). I define **growth** as this increase in τ, achieved not automatically but through deliberate actions—lowering information-integration cost (i) and raising venture value (V). The contribution is both conceptual and prescriptive: success probability and informativeness are **designed, not given**. Founders are not merely quixotic opportunity pursuer but **uncertainty engineer** who manage τ dynamically, earning precision through culture and capital.

Keyword: Bayesian and Evolutionary Entrepreneurship

*It appears to be a general principle that, whenever there is a randomized way of doing something, then there is a nonrandomized way that delivers better performance but requires more thought. \- E.T. Jaynes.*

# 1. Introduction 

Prior research in entrepreneurship and strategy has treated either **venture success probability (P)** or the **informativeness of evidence** as exogenous. This leaves a central puzzle unresolved: why do ventures facing the same environment and signals diverge so sharply in outcomes? If P is fixed, all ventures share the same odds, reducing differences in survival to luck or innate talent. If informativeness is fixed, all ventures learn at the same rate from the same signals, leaving no explanation for heterogeneous adaptation. What is missing is a mechanism by which founders _design their own capacity to learn_.

Consider Tesla and Better Place. Both confronted failures early in their journeys. Tesla’s Roadster suffered production delays and recalls; Better Place faced sluggish sales and uncertain charging standards. Yet Tesla pivoted and survived, while Better Place collapsed. Why did the same type of negative evidence trigger adaptation in one case but rigidity in the other? The answer lies in how each venture set its prior beliefs.

A simple Beta–Binomial model illustrates this mechanism. Let ϕ denote the probability that a promise succeeds. The prior is parameterized as ϕ∼Beta(μτ,(1−μ)τ) where μ is the prior mean (**aspiration**) and τ is its precision. After observing n trials with xx successes, the posterior becomes Beta(μτ+x,(1−μ)τ+n−x). When a single failure is observed (x=0,n=1), the posterior mean updates to: E[ϕ∣x=0,n=1]=μτ / (τ+1)

This expression makes informativeness concrete: with **low τ**, beliefs fall sharply after failure, reflecting high responsiveness to evidence; with **high τ**, beliefs barely move, reflecting rigidity.

**Figure Phenomena** visualizes this logic. The top panel shows a loose prior (τ=1) that shifts nearly 50% after one failure—precisely the responsiveness that enabled Tesla’s rapid pivots. The bottom panel shows a tight prior (τ=4) that shifts only 20% after the same failure—an update too small to change course, locking ventures into rigid commitments as in Better Place. Precision τ thus determines whether failure becomes a catalyst for adaptation or a trigger for collapse.
![[fig(phenomena).png]]

This mechanism closes the gap between **micro experimentation and macro selection**. At the micro level, ventures differ in how much evidence can move them; at the macro level, markets select across these trajectories. Better Place exemplified premature high τ, collapsing in rigidity. Tesla exemplified staged low→high τ, beginning with variation, gradually raising fidelity as information-integration cost fell and venture value increased, ultimately achieving scale.

Theoretically, τ has **three nested meanings**. At the probability level, τ is a concentration parameter. At the sampling level, τ is a pseudo–sample size approximating bounded rationality. At the evolutionary level, τ represents a **variation–selection balance**: ventures begin with variation (low τ) and evolve toward replication fidelity (high τ). Linking these levels shows that ventures mirror natural selection. Growth is defined as this staged increase in τ, achieved not automatically but through deliberate organizational design: lowering **information-integration cost (i)**—the inverse of organizational clockspeed—and raising venture value (V).

**Core contribution.** This paper shows that venture success probability and informativeness are not exogenous givens but are deliberately designed by founders. By reparameterizing success probability as an aspiration–precision prior, I demonstrate that **precision (τ)** is the founder’s design lever: it determines how much evidence can move beliefs, and thereby translates micro-level experimentation into macro-level selection. τ has three nested meanings—as concentration, as pseudo–sample size, and as variation–selection balance—linking Bayesian statistics, bounded rational cognition, and evolutionary dynamics in a single mechanism. Growth is defined as the staged increase of τ, but precision is never assumed; it must be earned. This framing dissolves the long-standing planning–action dichotomy: ventures must begin with low τ and raise it only as complexity (c) and information-integration cost (i) decline. In short, founders are **uncertainty engineers**, designing their own capacity to learn.

 The paper is engineered as follows. **Section 2 develops the theoretical framework (what)** by reparameterizing venture success probability as an aspiration–precision prior and showing why τ endogenizes informativeness. It explains why existing accounts are incomplete and how τ connects micro experimentation to macro selection. **Section 3 applies the framework (how)** through the contrasting cases of Tesla and Better Place, distilling a single prescription—_acculturate to concentrate_—and advancing a testable _Staged Precision Hypothesis_ that links τ trajectories to venture survival. **Section 4 concludes (so what)** by outlining implications for theory, practice, and future research, reframing founders not as passive or quixotic pursuers of opportunity (Stevenson, 1983) but as **uncertainty engineers** who deliberately design their learning capacity.

# 2. Theory and Model

## 2.1 Anatomy of Success Probability and Informativeness

Research in entrepreneurship, finance, and operations has each provided critical insights into uncertainty, but none offer a unified **endogenous mechanism for how success probability (P) and informativeness are designed.**

**Bayesian Entrepreneurship.** Recent work emphasizes the role of subjective priors and theory-driven experimentation (Agrawal, Gans, & Stern, 2024; Camuffo et al., 2024). Camuffo and colleagues show how disciplined, scientific approaches improve founder decision-making. Gambardella, Gius, and Stern introduce _Homo Entrepreneuricus_, highlighting subjective priors that allow entrepreneurs to “agree to disagree” and still experiment. These accounts are powerful in breaking with the common prior assumption. Yet they leave no handle for the _magnitude_ of updating—how strongly the same signal should move beliefs.

**Experimentation and Finance.** Kerr, Nanda, and Rhodes-Kropf (2014) frame entrepreneurship as experimentation, distinguishing macro Darwinian selection from micro staged financing. Nanda and Rhodes-Kropf (2016) extend this view to financing structures, while Bolton et al. (2024) formalize moral hazard in experiment design. These works are valuable in showing how capital and contracts shape tests, but they treat informativeness almost entirely on the **likelihood side** (test sensitivity/specificity), with **P exogenous and priors public.**

**Operations and Learning.** Fine (1986) formally linked learning curves and quality improvement, showing how higher quality accelerates cost reduction with experience. This implied that experience embeds information, making outcomes progressively more predictable—an **implicit treatment of informativeness.** Thomke (2003) further demonstrated how iterative experimentation accelerates innovation learning. Later work on clockspeed (Fine, 1998; Fine et al., 2002; Fine, 2022) distinguished product, process, and organizational rhythms, showing that fast-clockspeed firms absorb signals more quickly. These studies highlight the operational value of learning, but still treat P and informativeness as technological artifacts rather than design levers.

**Summary.** Across these streams, we inherit critical strengths—subjective priors, staged experimentation, and organizational learning—but all lack a unified endogenous mechanism. **Informativeness**, as I define it, is the **update potential**: the degree to which new evidence shifts the prior distribution of P. Prior work leaves this implicit or partial. **Table 1** summarizes these strengths and limitations.

| Stream / Representative Work                                                                                      | Strengths (what they captured well)                                                                                                                                                                            | Limitations (what they left missing)                                                           | Our Contribution (what we fill with τ)                                                      |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Bayesian Entrepreneurship** (Agrawal, Gans & Stern, 2024; Camuffo et al., 2024; Gambardella, Gius, Stern, 2024) | Camuffo et al. (2024): theory-driven decision-making discipline; Gambardella, Gius, Stern (2024): subjective priors + theory-based experimentation (Homo Entrepreneuricus)                                     | No mechanism for _update magnitude_—how strongly evidence shifts priors                        | τ formalizes **prior-driven informativeness**, endogenizing update capacity                 |
| **Experimentation / Finance** (Kerr et al., 2014; Nanda & Rhodes-Kropf, 2016; Bolton et al., 2024)                | Kerr et al. (2014): experimentation as macro vs. micro logic; Nanda & Rhodes-Kropf (2016): staged financing under uncertainty; Bolton et al. (2024): moral hazard in experiment design                         | P fixed; informativeness confined to **likelihood-side** test design                           | τ provides **prior-side informativeness**, bridging micro updates to macro selection        |
| **Operations / Learning** (Fine, 1986; Thomke, 2003; Fine 1998, 2002, 2022)                                       | Fine (1986): quality-based learning curves formalize implicit informativeness; Thomke (2003): experimentation accelerates innovation; Fine (2000) clockspeed work shows organization's signal absorption speed | Treat success probability and informativeness as technological artifacts, not strategic levers | Define i = (organizational clockspeed)⁻¹. **Earned precision**: only after i↓ can τ↑ safely |

[[🗄️🧠charlie]]
## 2.2 τ as the Missing Mechanism and Its Three Levels

Section 2.2 first dissolves the action/planning dichotomy on a τ continuum (2.2.1), then stacking τ’s nested meanings into a hierarchical loop that links Bayesian statistics, computation, and evolution (2.2.2).

#### 2.2.1 τ Spectrum: Integrating Schools with Different Epistemological logic

Epistemological logic is often contrasted between **action-oriented** school with **planning-oriented** school. Effectuation and causation, scientific experimentation, and design thinking can all be located on the τ continuum, which measures how concentrated or diffuse prior beliefs are. Mapping them onto this spectrum clarifies both their insights and their limitations, and shows how τ provides the missing mechanism that unifies them.

**Effectual logic (Sarasvathy, 2001).** At the action extreme, effectuation corresponds to **τ → 0**. Founders start with flexible, loosely held priors and experiment through small, adaptive steps. The strength of this approach is responsiveness: every piece of evidence shifts beliefs substantially. But the weakness is noise: overreaction and local optimization risks.

**Causal logic (Kirzner, 1997; Shane, 2003).** At the planning extreme, causal reasoning corresponds to **τ → ∞**. Opportunities are assumed to exist objectively, and founders engage in structured discovery and analysis. The strength here is reliability and coherence, but the cost is rigidity: with priors so tight, even strong counterevidence barely moves beliefs, trapping oneself in small hypothesis space (like Betterplace case).

**Scientific logic (Camuffo et al., 2020; Felin et al., 2020; Zellweger & Zenger, 2022; Camuffo et al., 2024).** Situated closer to the planning side but not at its extreme, scientific entrepreneurship emphasizes systematic hypothesis testing under uncertainty. Implicitly, it supports **earned precision**: starting from moderate τ and raising it as evidence accumulates. Its contribution is discipline and transparency, but its mechanism for how much to raise τ, and when, has remained implicit until now.

**Design logic (Dimov, 2016; Berglund et al., 2020; Mansoori and Dimov, 2025).** Design thinking bridges action and planning. Like effectuation, it treats opportunities as constructed, not discovered. Dimov (2016) product or service that is desirable in the market, technically and operationally feasible, and financially viable But like planning, it is deliberate and goal-oriented. In τ terms, design logic corresponds to **transition zones** where founders begin with low τ but intentionally reframe states and goals to create the organizational and cognitive foundations for raising τ later.

**Integrating the spectrum.** Seen this way, effectual–design–scientific–causal logics fall naturally along a **τ spectrum**: from low precision and high adaptability, to high precision and stability. Each logic captures a valuable piece of entrepreneurial behavior, but each taken in isolation risks either overreaction (τ too low) or rigidity (τ too high). The key argument of this paper is, ventures should keep moving. They must move along the spectrum of τ, converging to new equilibrium with its yet unseen environment. Thus, planning and action schools are not competing worldviews but sequential positions on a single τ continuum.

#### 2.2.2 τ Hierarchy: Three Nested Meanings
Beyond its role as a continuum that integrates action and planning logics, τ also operates **hierarchically** at three nested levels. Each level captures a different interpretation of how beliefs are formed and updated, and together they link Bayesian statistics, cognitive psychology, and evolutionary theory into a unified mechanism.

**Probability level.** At the most basic level, τ is a **concentration parameter.** A high τ prior is sharp and confident, leading to small posterior shifts; a low τ prior is diffuse, leading to large shifts from the same evidence. Prior work in Bayesian management research (Mackey & Dotson, 2024) recognizes the importance of priors but largely treats their shape as given, not as something founders design.

**Sampling level.** At the next level, τ can be understood as a **pseudo–sample size.** Sanborn and Chater (2016) show that the brain often approximates probabilities by drawing a finite number of samples rather than calculating exact probabilities. With few samples, inferences are noisy but highly responsive; with many samples, they are stable but sluggish. Ventures behave the same way: low-τ ventures look like small-sample samplers—quick to adapt but prone to error—while high-τ ventures look like large-sample samplers—robust but rigid.

**Evolutionary level.** At the highest level, τ encodes the **balance between variation and replication fidelity.** Ventures begin with low τ to preserve variation and adaptability, then raise τ to enforce fidelity and scale. This parallels Campbell’s (1960) variation–selection–retention model, Gould and Vrba’s (1982) concept of exaptation, and which show how institutions can steer ventures along this trajectory. This evolutionary culture is embodied in Moderna's mindset "pursue options in parallel, pivot fearlessly" () and Flagship pioneering "selection pressure and variation" ()on pivot 

**The hierarchy.** These three interpretations are not separate but **stacked.** At the bottom lies Bayesian probability, in the middle bounded-rational sampling, and at the top evolutionary dynamics. Together they highlight why τ is a uniquely unifying parameter. They also show why ventures cannot remain fixed at either extreme of the planning–action spectrum: τ must increase in stages, moving upward through the hierarchy, so that micro-level belief updates aggregate into macro-level evolutionary selection.

**Table 2** summarizes how τ integrates Bayesian and evolutionary perspectives across three nested levels.

| Level            | Meaning of τ                                                                  | Strengths in Prior Literature                                                                                | Limitations                                               | Our Contribution (what τ adds)                                                              |
| ---------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Probability**  | Concentration parameter: tighter priors reduce posterior updates              | Bayesian stats in management (Mackey & Dotson, 2024) stress priors shape inference                           | Priors treated as given; no founder design                | τ as **design lever**: endogenize informativeness by setting concentration                  |
| **Sampling**     | Pseudo–sample size: τ ≈ effective prior n                                     | Sanborn & Chater (2016): cognition as sampling; finite samples → systematic biases                           | Not applied to ventures; no link to survival              | τ interprets update capacity as sample size: low τ agile but noisy, high τ stable but rigid |
| **Evolutionary** | Variation–selection balance: low τ = variation, high τ = replication fidelity | Andrew & Josh (Bayes_evol): accelerators/regulators shape τ trajectory; Campbell (1960); Gould & Vrba (1982) | Evolutionary metaphor strong, but operationalization weak | τ as **evolutionary lever**: growth = staged τ↑, conditional on i ↓ (clockspeed↑) and V ↑   |
## 2.3 Growth as Earned Precision

At the evolutionary level, **growth is defined as the staged increase in τ.** Ventures cannot start with high τ—premature precision locks them into rigidity, a “worse posterior place.” Nor can they remain permanently low—failure to concentrate prevents scale. Instead, ventures must _earn_ precision by deliberately lowering information-integration costs and raising value before increasing τ.

**Stage-based growth.** Fine (2022) describes the entrepreneurial journey as _nail it, scale it, sail it_. In the _nail it_ stage, ventures operate with low τ, exploring variation and absorbing evidence with high informativeness. In the _scale it_ stage, τ rises as ventures systematize, processify, and replicate with increasing fidelity, turning learning into disciplined execution. In the _sail it_ stage, τ is high and growth depends on continuous improvement but also risks sclerosis. This stage logic maps directly onto τ as an evolutionary lever: **growth = staged τ↑**.

**Evolutionary logic.** This staged account echoes long-standing evolutionary theories. Campbell (1960) articulated adaptation as variation, selection, and retention; Gould and Vrba (1982) introduced exaptation to describe how traits repurposed by chance become core features. Andrew and Josh’s Bayesian evolution synthesis similarly shows how policy instruments such as accelerators and regulation shape venture τ trajectories, steering them from exploration toward replication. Together, these perspectives frame τ as the formal parameter that encodes the **variation–selection–replication fidelity balance.**

**Operational conditions.** Precision cannot be assumed—it must be earned. Fine (1986) demonstrated that higher quality accelerates learning curves, implying that informativeness is embedded in accumulated experience. Later clockspeed research (Fine, 1998; Fine et al., 2002) revealed how fast- versus slow-clockspeed firms differ in translating signals into coordinated action. I formalize this as **information-integration cost (i)**, defined as the inverse of organizational clockspeed. A low-i organization digests selected signals quickly, enabling τ to rise; a high-i organization struggles, making premature τ dangerous.

**Ecosystem dynamics.** Piepenbrock and Fine (2009) extend this logic to business ecosystems. Their research shows that industries oscillate between **modular and integral architectures**, reflecting systemic cycles of variation, integration, and dominant design. In modular epochs, low-τ variation is rewarded; in integral epochs, high-τ replication fidelity dominates. This demonstrates that τ not only evolves within ventures but also co-evolves with the architectures of their environments.

**Prescription.** Thus, τ is not just a statistical parameter but also an **evolutionary and operational prescription**. Founders must _acculturate to concentrate_: lowering i through organizational design and raising V before raising τ. Growth is therefore earned—by navigating variation and replication inside the venture, and by adapting to oscillations between modular and integral architectures in the broader ecosystem.

To close Section 2, I emphasize replication fidelity of the framework's recursive (Dimov and Pistrui, 2019) logic. The model shows that micro experimentation shapes macro selection: ventures differ in τ, which defines their learning capacity, and this propagates into divergent survival outcomes. I then reinterpret τ through its three nested meanings—as a concentration parameter (probability), as a pseudo–sample size (sampling), and as a variation–selection balance (evolutionary). This layering allows me to return from mechanism back to theory: ventures live under the same evolutionary constraint as natural selection, where variation, selection, and replication unfold over time, and the amount of absorbed information grows monotonically with τ. Thus, growth can be defined as the staged increase of τ. In the modeling section that follows, I will show formally the conditions under which this increase of τ is optimal, which, on the flip side, characterize conditions under which ignorance is optimal.

## 2.4 Modeling “Fake It Till Approximate It”

Table 3\. Key Model Variables

| Variable | Definition | Interpretation | Example (Tesla vs. Better Place) |
| ----- | ----- | ----- | ----- |
| μ | Aspiration (mean of belief distribution) | Boldness of the promise | Tesla (μ≈0.3): “200+ miles.” Better Place (μ≈0.9): “Infinite range.” |
| τ | Precision  | Specificity/rigidity of the promise | Tesla (τ≈1): “\~200 miles (±40).” Better Place (τ≈4): “Exactly 3 minutes.” |
| C | Operational complexity | \# of independent, critical components | Tesla (n≈5): pack, motor, software. Better Place (n≈10): robotics, real estate, standards, OEMs. |
| I | Information-integration cost | Marginal cost to raise τ by one | Tesla: prototype iteration. Better Place: nationwide swap network. |
| V | Venture value | Value upon successful delivery | E.g., market cap or TAM. |

​​# 2.4 Model: From “Fake It Till Make It” to “Approximate It”
![[fig(model).png]]

**Figure Model.** This figure makes transparent how an founder’s epistemology matures: In M1, the promise φ is monotonically linked to success probability; in M1′, nature’s complexity c bends that monotonicity into a concave shape, so the same promise has different effective impact. By M2, I treat promises as a distribution by reparameterizing venture's promise with founder's aspiration μ; in M2′, the founder chooses the design variable τ to approximate that distribution, adopting rational ignorance as a strategy by balancing it against the meaning-construction cost i. Ultimately, it offers a grammar for deciding scientifically not “to know more,” but “when and what to leave unknown,” and that grammar is the bridge that reunifies the planning school and the action school along a single continuum.


Table. Comparative schematic of four Bayesian decision models (with generative notation)

|                        | M1                                | M1′                                                | M2 (→ Proposition 1)                                                          | M2′ (→ Proposition 2)                                                                       |
| ---------------------- | --------------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Generative process** | $S \sim \text{Bern}(\phi)$        | $S\land D \sim \text{Bern}(\phi(1-\phi)^c)$        | $S\land D \sim \text{Bern}(\phi(1-\phi)^c)$<br>$\phi \sim \text{Beta}(\mu,1)$ | $S\land D \sim \text{Bern}(\phi(1-\phi)^c)$<br>$\phi \sim \text{Beta}(\mu\tau,(1-\mu)\tau)$ |
| **Objective**          | $\max_{\phi} P(S \mid \phi)=\phi$ | $\max_{\phi} P(S\land D \mid \phi)=\phi(1-\phi)^c$ | $\max_{\mu} P(S\land D) = \int P(S\land D\mid  \phi)p(\phi\mid \mu) d\phi$    | $\max_{\mu,\tau} P(S\land D) V - i \cdot \tau$                                              |
| **Optimal solution**   | $\phi^\star=1$                    | $\phi^\star=1/(c+1)$                               | $\mu^\star\approx 1/(\log c+\gamma)$                                          | $c=1$: $\mu^\star=1/2$, $\tau^\star=\max\{\sqrt{V/(4i)}-1,0\}$                              |
| **Interpretation**     | Pure MLE (prediction)             | MLE with complexity drag $c$ (prediction)          | Empirical-Bayes calibration of aspiration (Prop.1)                            | Information's value and integration cost tradeoff (Prop.2)                                  |

**M1: Naive Commitment.** The founder maximizes $P(S|\phi)=\phi$, yielding $\phi^\star=1$. This trivial solution embodies the naive “fake it till you make it” mentality: always promise the maximum. It ignores complexity and is unrealistic.

**M1′: Complexity as Constraint.** With operational complexity $c$, success requires delivering through $c$ interdependent tasks: $P(S\land D|\phi)=\phi(1-\phi)^c$. Reliability engineering interprets $(1-\phi)^c$ as the chance all $c$ subsystems succeed; Bayesian inference interprets it as the likelihood of one success after $c$ failures. Either way, the optimum shifts to $\phi^\star=1/(c+1)$. Complexity tempers ambition.

**M2: Empirical-Bayes Calibration of Aspiration.** Rather than choose a fixed $\phi$, the founder sets a prior mean $\mu$ with $\tau=1$. The objective is

$$\max_{\mu}\; \int_0^1 \phi(1-\phi)^c\,p(\phi|\mu,1)\,d\phi = \max_{\mu}\;\frac{B(1+\mu,1+c-\mu)}{B(\mu,1-\mu)}.$$

This is empirical-Bayes calibration (Gelman et al., 2015).

**Proposition 1 (Aspiration Calibration under Complexity).** When promises face complexity $c$, optimal aspiration is calibrated downward: $\phi^\star=1/(c+1)$; equivalently, the optimal prior mean $\mu$ satisfies $\tfrac{1}{\mu}=\sum_{k=1}^c 1/(k-\mu)$ and approximates $1/(\log c+\gamma)$.

All proofs are in appendix.
_Implication._ Aspiration falls with complexity. Better Place who had higher complexity c than Tesla could have reduced $\mu$ but did not.

**M2′: Aspiration Plus Optimal Ignorance.** Now both $\mu$ and precision $\tau$ are chosen:

$$\max_{\mu,\tau}\; V\int_0^1 \phi(1-\phi)^c\,p(\phi|\mu,\tau)\,d\phi-\tau i.$$

Another name of precision parameter $\tau$ is pseudo-sample size (Gelman et al, 2015), yet another name is pseudo counts (McElreath, 2022). Deeper knowledge is expected from precise priors hence they require  more surprising data to start shifting.The first-order condition $V\frac{\partial}{\partial \tau}\,\mathbb{E}[\phi(1-\phi)^c] = i$ means marginal value equals cost, leading to Proposition 2a.

**Proposition 2a (General principle).** The optimum $(\mu^\star,\tau^\star)$ equates the marginal value of additional precision with its marginal cost.

**Proposition 2b (Special cases).**
- If $i=0$: then $\tau^\star\to\infty$ and $\mu^\star=1/(c+2)$.
- If $c=1$: then $\mu^\star=1/2$ and $\tau^\star=\max{(\sqrt{V/(4i)}-1,0)}$.

**Proposition 2c (Fixed aspiration).** For fixed $\mu$, 
$$
\tau^*\;\approx\;\sqrt{\frac{V}{i}\cdot \frac{c}{2}\,\mu\,(1-\mu)^{\,c-1}\,\big(2-(c+1)\mu\big)},\quad 0<\mu<\frac{2}{c+1}.
$$

**Interpretation** are as follows. $\tau^\star$ increases in proportion to venture value $V$ (high-value ventures justify more precision). $\tau^\star$ decreases as information-integration cost $i$ rises (higher costs discourage paying for precision). $\tau^\star$ also decreases as complexity $c$ rises, because each additional subsystem multiplies the downside of bold promises, so the marginal payoff from further precision is diluted.

# 3. Practice: Case, Prescription, Prediction

This section validates the theory developed in Section 2 across three layers: **Figure of Theory** develops the logic (τ as endogenous lever), **Table of Practice** distills it into managerial guidance, and **Figure of Prediction** illustrates survival consequences.

## 3.1 Case: Better Place vs. Tesla

Tesla and Better Place provide a natural experiment showing how precision (τ) design shapes venture trajectories. Better Place assumed high τ from the outset—rigid promises about swap times, sales targets, and infrastructure—despite high complexity (c) and high information-integration cost (i). This deterministic posture created a **learning trap**: new evidence could not shift commitments, leading to collapse.

Tesla, by contrast, began with low τ—broad but legitimate promises (“200+ miles”)—and used staged products as sequential experiments. Each launch generated evidence, lowered i through tighter organizational routines, and raised V by proving demand. Only then did Tesla raise τ, gradually tightening commitments. In Bayesian terms, Tesla preserved the ability to learn before concentrating promises, whereas Better Place foreclosed learning by committing too tightly too early.

In sum, Better place's initial choice of high τ was a deterministic and all-in approach straight-jacket. On the other hand, Tesla outsourced its computation to the environment though its probable and adaptive approach. This contrast epitomize how M1 vs M2 model family differ in Sec.2. Separating founder from venture business model created hierarchical Bayesian principal agent relationship (Gelman, 2013) and improved the model quality.

Panels (a–c) of Figure of Theory formalize this contrast: μ falls with complexity c (control variable), while τ rises only as i falls and V rises (design lever). Tesla managed τ dynamically; Better Place assumed it.

![[fig(theory).png]]
**Figure of Theory. Bayesian foundations of entrepreneurial adaptation.**  
Panel (a) shows aspiration μ is passively constrained by complexity c; (b) shows precision τ∗ rises only as information-integration cost i falls and value V increases; (c) shows posterior updating depends on τ—low τ allows learning, high τ blocks it. **Together these panels illustrate that aspiration is limited by environment, but precision is actively earned—τ is the founder’s design lever for turning evidence into adaptation.

## 3.2 Prescription: Acculturate to Concentrate

The central prescription is straightforward:

> **Acculturate to concentrate.** Precision of venture's promise must be earned by lowering information-integration cost (i) and raising venture value (V).

Tesla reduced i and increased V before raising τ; Better Place did the opposite. This checklist helps investors and educators diagnose whether founders are **earning precision** or prematurely locking it in.

Table of Practice translates these principles into a practitioner’s checklist. Each row links a diagnostic question to methods for reducing either complexity or integration cost, and illustrates success through Tesla’s trajectory and failure through Better Place’s. Tesla consistently simplified and lowered integration cost before raising the specificity of its commitments, thereby earning precision. Better Place, by contrast, began with precise promises despite high complexity and high integration cost, locking itself into rigidity.

**Table of Practice. Precision Management Checklist**

| Lever                                | Diagnostic Question                                                                               | How to Reduce                                                         | Success (Tesla)                                                                                                                                          | Failure (Better Place)                                          | Other examples                                        |
| ------------------------------------ | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------- |
| **Information-integration cost (i)** | _When the organization chooses to absorb new information, how quickly can it coordinate and act?_ | Flatten structures; unify vocabulary; codify heuristics for iteration | During “production hell,” Tesla emphasized speed over perfection, kept gates open, corrected errors quickly, and created a shared language across teams. | Fragmented teams and inconsistent vocabularies slowed response. | Nvidia leadership  structure retaining its early form |
| **Precision (τ)**                    | Is specificity matched to earned reductions in i and increases in V?                              | Stage commitments; raise τ only after organizational readiness        | Tesla staged promises: broad → “200+ miles” → Model 3 forecasts, increasing τ only after i↓ and V↑.                                                      | Better Place launched with rigid swaps unsupported by i or V.   |                                                       |
### 3.3 Prediction: Staged Precision Hypothesis

From cases and theory emerges a simple, testable hypothesis:

> **Ventures that start with low precision τ and raise it only after lowering information integration cost i will outperform those that assume high τ prematurely.**

Founder language offers a proxy—rigid, quantified promises reveal high τ, while broad, flexible claims reveal low τ. Using hierarchical Bayesian and dynamic models developed to capture latent parameters (Bell & Dotson, 2022; Mackey, Barney, & Dotson, 2017; Wibbens, 2021), τ trajectories can be estimated from pitch decks, crowdfunding date, and communications and linked to outcomes such as survival, pivots, and funding.

**Figure of Prediction** shows the implication: Tesla-like “earned precision” trajectories sustain higher survival probabilities, while Better Place–like “premature precision” paths collapse quickly.

![[fig(pred)_tau.png]]

## 4\. Conclusion and Vision

**Conclusion**. Venture's success probability is anatomized (sec.2.1), unified (sec.2.2), reasoned, programmed, and implemented around the relationship between founder and its venture's probabilistic adaptation. I reframe promises as an aspiration–precision prior, with aspiration (μ) constrained by complexity (c) and precision (τ) earned only as integration costs (iii) fall. The central prescription is simple but powerful: **simplify to aspire, acculturate to concentrate.** This unifies the long-standing **action school** (which tends to remain at low τ) and the **planning school** (which assumes high τ ex ante) by showing how ventures can move from low to high precision gradually, through deliberate simplification and acculturation. Therefore, I translate one layer of founder's nature into nurture i.e. into principles to manage complexity, information, and precision over time.

**Vision.** This framework speaks to multiple audiences. For theorists, it unifies Bayesian and evolutionary perspectives by showing how aspiration (μ) and precision (τ) jointly structure adaptation, while raising open questions about irreversibility, path dependence, and whether firm “aging” is a choice—positioning startups as useful “fruit fly” models. For empiricists, it offers founder language as a measurable proxy for τ and highlights hierarchical Bayesian methods to estimate heterogeneous trajectories of aspiration and precision beyond average-effect approaches. For founders, it delivers a simple prescription: precision must be earned—simplify models, reduce integration costs, and stage commitments so that τ rises only as the venture learns, making the deliberate management of ignorance a central capability. And for educators, investors, and policymakers, it reframes evaluation criteria: look not only at aspiration (μ) but at calibrated realism (dynamic τ), teaching and rewarding the ability to balance flexibility and efficiency in relation to measurable complexity (c) and integration cost (i), rather than slogans.

## 5\. References

- Agrawal, A., Gans, J., & Stern, S. (Eds.). (2024). _Bayesian entrepreneurship_. MIT Press.
    
- An, K., Hwang, M., Kim, Y., Lee, H., Park, J., Hong, H., Sol, H., Moon, H., & Han, S. (2025). _AI insiders: Future report by global top-tier experts_. Smartbooks.
    
- Bell, J. J., & Dotson, J. P. (2022). Phantom attributes: Unpacking product perceptions. _Available at SSRN 4109569_.
    
- Berglund, H., Bousfiha, M., & Mansoori, Y. (2020). Opportunities as artifacts and entrepreneurship as design. _Academy of Management Review_, _45_(4), 825-846.
    
- Bolton, P., Liu, S., Nanda, R., & Sunderesan, S. (2024). _Moral hazard in experiment design: Implications for financing innovation_. Working Paper.
    
- Camuffo, A., Cordova, A., Gambardella, A., & Spina, C. (2020). A scientific approach to entrepreneurial decision making: Evidence from a randomized control trial. _Management Science, 66_(2), 564-586.
    
- Camuffo, A., Gambardella, A., Messinese, D., Novelli, E., Paolucci, E., & Spina, C. (2024). A scientific approach to entrepreneurial decision making: Large scale replication and extension. _Strategic Management Journal.
- 
- Camuffo, A., Gambardella, A., & Pignataro, A. (2024). Theory-driven strategic management decisions. _Strategy science_, _9_(4), 382-396.
    
- Campbell, D. T. (1960). Blind variation and selective retentions in creative thought as in other knowledge processes. _Psychological review_, _67_(6), 380.

- Dimov, D. (2016). Toward a design science of entrepreneurship. In A. C. Corbett, & J. A. Katz (Eds.), Models of start-up thinking and action: Theoretical, empirical, and pedagogical approaches (Vol. 18, pp. 1–31). Emerald Group Publishing Limited.

- Dimov, D., & Pistrui, J. (2020). Recursive and discursive model of and for entrepreneurial action. _European Management Review, 17_(1), 267-277.
    
- Felin, T., Gambardella, A., Stern, S., & Zenger, T. (2020). Lean startup and the business model: Experimentation revisited. _Long Range Planning_, _53_(4), 101889.
    
- Fine, C. H. (1986). Quality improvement and learning in productive systems. _Management Science, 32_(10), 1301-1315.
    
- Fine, C. H. (1998). _Clockspeed: Winning industry control in the age of temporary advantage_. Perseus Books.
    
- Fine, C. H. (2000). Clockspeed‐Based Strategies for Supply Chain Design 1. _Production and operations management_, _9_(3), 213-221.
    
- Fine, C. H., Padurean, L., & Naumov, S. (2022). Operations for entrepreneurs: Can Operations Management make a difference in entrepreneurial theory and practice?. _Production and Operations Management, 31_(12), 4599-4615.
    
- Fine, C. H., Vardan, R., Pethick, R., & El-Hout, J. (2002). Rapid-response capability in value-chain design. _MIT Sloan Management Review, 43_(2), 69-75.
- 
- Gelman, A., Carlin, J. B., Stern, H. S., & Rubin, D. B. (1995). _Bayesian data analysis_. Chapman and Hall/CRC.
- 
- Gelman, A., & Shalizi, C. R. (2013). Philosophy and the practice of Bayesian statistics. _British Journal of Mathematical and Statistical Psychology_, _66_(1), 8-38.
- 
    
- Gould, S. J., & Vrba, E. S. (1982). Exaptation--a missing term in the science of form. _Paleobiology, 8_(1), 4-15.
    
- Kerr, W. R., Nanda, R., & Rhodes-Kropf, M. (2014). Entrepreneurship as experimentation. _Journal of Economic Perspectives_, _28_(3), 25-48.
    
- Kirzner, I. M. (1997). Entrepreneurial discovery and the competitive market process: An Austrian approach. _Journal of economic Literature_, _35_(1), 60-85.
- Luo, H., Pisano, G., & Yu, H. (2018). Institutionalized entrepreneurship: Flagship pioneering. _HBS Case_, 718-484.
- Mackey, T., & Dotson, J. (2024). Bayesian Statistics in Management Research: Theory, Applications, and Opportunities. _Oxford Research Encyclopedia of Business and Management_.
    
- Mackey, T. B., Barney, J. B., & Dotson, J. P. (2017). Corporate diversification and the value of individual firms: A Bayesian approach. _Strategic Management Journal, 38_(3), 322–341.

- Mansoori, Y., & Dimov, D. (2025). Entrepreneurs as architects: Design (ing) focus in entrepreneurship education. _Entrepreneurship education and pedagogy_, _8_(3), 452-484.
- McElreath, R. (2018). _Statistical rethinking: A Bayesian course with examples in R and Stan_. Chapman and Hall/CRC.
- Moderna, Inc. (2025). _Moderna’s mindsets_. Moderna. Retrieved September 21, 2025, from [https://www.modernatx.com/en-US/about-us/our-mission/modernas-mindsets](https://www.modernatx.com/en-US/about-us/our-mission/modernas-mindsets)
    
- Nanda, R., & Rhodes-Kropf, M. (2016). Financing entrepreneurial experimentation. _Innovation Policy and the Economy_, _16_(1), 1-23.
    
- Piepenbrock, T. F. (2009). _Toward a theory of the evolution of business ecosystems: Enterprise architectures, competitive dynamics, firm performance & industrial co-evolution_ (Doctoral dissertation, Massachusetts Institute of Technology).
    
- Sanborn, A. N., & Chater, N. (2016). Bayesian brains without probabilities. _Trends in cognitive sciences, 20_(12), 883-893.
    
- Sarasvathy, S. D. (2001). Causation and effectuation: Toward a theoretical shift from founderial contingency. _Academy of Management Review, 26_(2), 243-263.
    
- Shane, S. (2003). A general theory of entrepreneurship: The individual-opportunity nexus. In _A General theory of entrepreneurship_. Edward Elgar Publishing.
    
- Stevenson, H. H. (1983). A perspective on entrepreneurship. KAO, John J. The.
    
- Thomke, S. H. (2003). _Experimentation matters: unlocking the potential of new technologies for innovation_. Harvard Business Press.
    
- Wibbens, P. D. (2021). A formal framework for the RBV: Resource dynamics as a Markov process. _Strategic Management Journal, 42_(1), 3–29.
    
- Zellweger, T., & Zenger, T. (2023). founders as scientists: A pragmatist approach to producing value out of uncertainty. _Academy of Management Review, 48_(3), 379-408.

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

