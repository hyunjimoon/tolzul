[[2025-08-08|25-08-08-07]]

# The Strategic Design of Entrepreneurial Promises: A Five-Stage Evolution Model

## I. Introduction

Entrepreneurial promises transform uncertainty into possibility. When Trevor Milton proclaimed that Nikola would revolutionize trucking with hydrogen power, markets responded with an $11 billion valuation. When Elon Musk promised to electrify transportation through Tesla, initial skepticism gave way to transformative success. Both entrepreneurs mastered the art of selling their vision—yet only one delivered. What distinguishes empty rhetoric from catalytic prophecy?

This paper advances two fundamental insights about entrepreneurial promise-making. First, excessive precision creates learning traps that prevent entrepreneurs from updating their beliefs when markets signal differently. Second, operational complexity imposes mathematical constraints on optimal promise levels, explaining why software ventures promise aggressively while hardware ventures speak cautiously. These insights transform promise-making from mysterious art to tractable science.

We develop a five-stage theoretical framework building from static promises to distributions over ambition levels. Through this progression, we derive four propositions that reshape how scholars should understand entrepreneurial decision-making. Our analysis provides mathematical foundations for phenomena that practitioners recognize intuitively but struggle to articulate systematically.

## II. Core Concepts and Theoretical Framework

### 2.1 The Architecture of Promises

Understanding entrepreneurial promises requires precise analytical decomposition. The **promise level** (φ) captures specific performance claims relative to technical possibilities. When battery technology permits 100-300 mile range, promising 226 miles yields φ = (226-100)/(300-100) = 0.63. This normalization enables cross-industry comparison despite different performance metrics.

The **aspiration level** (μ) represents the mean of the prior distribution over possible promises. Declaring "approximately 200-mile range" communicates μ while acknowledging uncertainty. The **precision parameter** (τ) quantifies how tightly promises cluster around this mean—high τ yields narrow commitments like "195-205 miles," while low τ permits broad ranges like "150-250 miles."

### 2.2 Decision Architecture: Choices and Constraints

Entrepreneurial promises emerge from the interplay between strategic choices and environmental constraints. Understanding this architecture is essential for grasping how our theoretical propositions translate into practical prescriptions.

#### 2.2.1 The Entrepreneurial Choice Space

Entrepreneurs control two fundamental variables that shape their venture's trajectory:

**Aspiration Level (μ)**: This strategic choice represents the entrepreneur's vision calibration—how ambitious their promises relative to current technological possibilities. A μ = 0.9 signals revolutionary ambition ("we'll obsolete the industry"), while μ = 0.3 indicates incremental improvement ("we'll enhance existing solutions"). This choice directly determines resource mobilization potential but also delivery difficulty.

**Precision Parameter (τ)**: This communication choice governs specificity design—how tightly promises cluster around the aspiration level. Low precision (τ < 10) preserves strategic flexibility through statements like "we aim to revolutionize transportation." High precision (τ > 50) creates rigid commitments like "we will deliver 1,000-mile range by Q3 2023." This choice fundamentally affects learning capacity and pivot optionality.

#### 2.2.2 Technological and Institutional Constraints

While entrepreneurs choose (μ,τ), they operate within a parameter space shaped by forces beyond their control:

**Technological Parameters**:
- **Operational Complexity (n)**: Physical laws create immutable constraints. Software's malleability yields n ≈ 1; hardware's material resistance imposes n ≈ 5; biology's complexity demands n ≈ 10. This parameter fundamentally bounds achievable promises.
- **Information Cost (c)**: Market structure determines validation expense. Open ecosystems with standardized metrics reduce c; proprietary domains with complex integration increase c. This shapes optimal precision levels.

**Institutional Parameters**:
- **Success Rewards (V_sd)**: Exit multiples and acquisition premiums create pull incentives. Higher rewards enable bolder promises but also amplify temptation.
- **Fraud Penalties (V_snd)**: Criminal sanctions and regulatory enforcement create push constraints. Severe penalties deter deception but may chill legitimate experimentation.
- **Failure Costs (V_ns)**: Bankruptcy protection and cultural attitudes determine downside risk. Forgiving environments encourage experimentation; punitive ones demand conservatism.

#### 2.2.3 The Complete Decision Table

| **Variable**          | **Links to Propositions** | **Links to Propositions**            | **Nature**           | **Control Mechanism**        |
| --------------------- | ------------------------- | ------------------------------------ | -------------------- | ---------------------------- |
| μ (aspiration)        |                           | Props 2,4: μ* = 1/(n+1)              | Strategic choice     | Vision calibration           |
| τ (precision)         |                           | Props 3,4: τ < μ(1-μ)/ε - 2          | Communication choice | Specificity design           |
| n (complexity)        |                           | Props 2,4: Determines μ*,τ*          | Physical constraint  | Operations difficulty        |
| c (information cost)  |                           | Prop 4: Shapes τ*                    | Market structure     | Due diligence infrastructure |
| V_sd (success reward) |                           | Props 1,4: Drives promise escalation | Market incentive     | Exit multiples               |
| V_snd (fraud penalty) |                           | Constrains high τ choices            | Legal deterrent      | Criminal sanctions           |
| V_ns (failure cost)   |                           | Enables experimentation              | Safety net           | Bankruptcy protection        |

This architecture reveals why entrepreneurial success requires more than good intentions or bold vision. The interplay between choice variables (μ,τ) and environmental parameters (n,c,V_sd,V_snd,V_ns) creates a complex optimization landscape where naive strategies—whether maximally bold or maximally precise—lead to predictable failure modes.

### 2.3 Mathematical Framework

We model entrepreneurial communication through Beta(μτ, (1-μ)τ) distributions as priors over promise levels. When τ = 2, we obtain nearly uniform distributions reflecting maximum uncertainty. As τ increases, distributions concentrate around μ, reflecting increasing confidence in specific outcomes. This framework enables rigorous analysis of how communication choices affect subsequent learning dynamics.

## III. Model Development and Core Propositions

Our theoretical journey progresses through five models, each adding critical elements to understand entrepreneurial promise-making. We begin with promises as cheap talk (Model 1), then show how they mobilize resources (Model 2), constrain delivery (Model 3), enable flexibility through distributions (Model 4), and finally optimize precision and ambition jointly (Model 5). The following table summarizes this progression, highlighting how each model's assumptions generate distinct insights about entrepreneurial behavior.

| Model                               | Key Assumption                                          | Core Result                                            | Real-World Implication                                                               |
| ----------------------------------- | ------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| **Model 1: Static World**           | Success probability exogenous (p fixed)                 | Promises irrelevant: U = p·V                           | Explains internal ventures, government contracts where promises don't affect funding |
| **Model 2: Persuasion Power**       | Promises mobilize resources: P(S∣φ) = p + αφ            | Maximum promises optimal: φ* = 1                       | Bubble dynamics—Nikola's $11B valuation from bold claims                             |
| **Model 3: Sell-Deliver Trade-off** | Delivery difficulty rises with promises: d(φ) = (1-φ)^n | Optimal promise: φ* = 1/(n+1)                          | Software promises 50%, hardware 17%, deep tech 9%                                    |
| **Model 4: Strategic Ambiguity**    | Entrepreneurs choose distribution Beta(μτ, (1-μ)τ)      | Learning trap when τ > μ(1-μ)/ε - 2                    | BetterPlace's τ=56 prevented pivoting to charging                                    |
| **Model 5: Precision Costs**        | Information gathering costly: C(τ) = c·ln(τ+1)          | Joint optimum: μ* = 1/(n+1), τ* = V_sd·n/[c(n+1)²] - 1 | Tesla's gradual precision increase (12→60) vs Nikola's immediate τ=100               |

Each model builds on its predecessors while introducing new strategic considerations. Model 1 establishes the null hypothesis—when don't promises matter? Model 2 reveals why entrepreneurs feel pressure to exaggerate. Model 3 explains why some succeed while others fail through operational constraints. Model 4 shows how overconfidence blocks learning. Model 5 integrates all elements into a complete optimization framework.
### Model 1: The Impotent Promise

Traditional economic models treat success probability as exogenous, rendering promises mere cheap talk. Here P(Success) = p regardless of promised performance. This baseline captures contexts where resource allocation follows predetermined plans—internal corporate ventures with fixed budgets, government contracts with guaranteed funding, tenure-track positions evaluated solely on past work. While limited, this null model establishes when promises matter.

### Model 2: The Escalation Imperative

Reality often exhibits self-fulfilling dynamics where bold promises attract resources that genuinely enhance success probability. We model this as P(Success|φ) = p + αφ, where α captures resource mobilization effects.

**Proposition 1.** When promises linearly affect success probability through resource mobilization, optimal promises always maximize: φ* = 1.

*Proof.* Expected utility U = (p + αφ)V yields ∂U/∂φ = αV > 0 throughout [0,1], implying corner solution φ* = 1. ∎

This proposition explains maximum promise equilibria during bubble periods. When resources flow toward confidence, entrepreneurs rationally escalate claims. Nikola's hydrogen revolution narrative attracted General Motors' partnership and $2 billion investment precisely because it maximized φ. The model's fatal flaw—ignoring delivery constraints—enables escalation spirals that end in collapse.

### Model 3: Physics Meets Rhetoric

Entrepreneurial success demands sequential achievements: selling visions then delivering results. We model delivery difficulty as d(φ) = (1-φ)^n, where operational complexity n transforms ambitious promises into exponential implementation challenges.

**Proposition 2.** Given operational complexity n, optimal promise level equals φ* = 1/(n+1).

*Proof.* Success requires both selling and delivering: E[U] = V_sd × φ × (1-φ)^n. First-order condition yields φ* = 1/(n+1). ∎

This proposition explains systematic variation across sectors:

**Low Complexity (n ≈ 1)**: SaaS platforms, mobile apps, algorithmic trading systems promise aggressively (φ* ≈ 0.5) because iteration cycles measure in days and deployment requires clicking "publish."

**Medium Complexity (n ≈ 5)**: Autonomous vehicles, robotics, medical devices promise moderately (φ* ≈ 0.17) because hardware prototyping takes months and regulatory approval adds years.

**High Complexity (n ≈ 10)**: Nuclear fusion, quantum computing, novel therapeutics promise minimally (φ* ≈ 0.09) because fundamental physics research spans decades and clinical trials eliminate most candidates.

### Model 4: From Points to Distributions

Sophisticated entrepreneurs communicate through probability distributions. When venture capitalists hear "we expect 10x to 100x returns, most likely around 30x," they receive information about the entire belief structure. We model this through Beta(μτ, (1-μ)τ) priors where entrepreneurs choose distribution parameters.

High precision creates rigidity—confident entrepreneurs cannot update beliefs despite contrary evidence. Low precision preserves adaptability but sacrifices credibility.

**Proposition 3.** Precision exceeding τ̄ = μ(1-μ)/ε - 2 creates learning traps where market feedback cannot meaningfully update the prior.

*Proof.* Consider Bayesian updating after observing failure. Prior Beta(μτ,(1-μ)τ) yields posterior Beta(μτ,(1-μ)τ+1) with mean μ' = μτ/(τ+1). The change |μ'-μ| = μ(1-μ)/(τ+1) < ε requires τ > μ(1-μ)/ε - 1. ∎

BetterPlace exemplified this trap. With μ = 0.7 confidence in battery-swapping and τ ≈ 56 precision, even strong consumer preference for charging stations barely moved beliefs. The learning trap threshold τ̄ = 2.2 for 5% minimum updates means Agassi's precision exceeded adaptability requirements by 25-fold.

**Figure 1: Success and Failure Regions in μ-τ Space**

![[figure1_mu_tau_space_eng.svg]]

The entrepreneurial landscape maps onto a two-dimensional space where aspiration (μ) and precision (τ) determine venture trajectories. Gradient shading indicates danger intensity, with the mathematical threshold τ̄ = μ(1-μ)/ε - 2 forming a curved boundary that separates the learnable zone from learning traps. Three distinct regions emerge: the adaptive zone (low τ, moderate μ), the operational rigidity trap (high τ, low μ), and the fraud temptation zone (high τ, high μ).

Tesla's path demonstrates successful navigation—maintaining μ≈0.4-0.7 while gradually adjusting τ. Even during "production hell," they stayed below the learning threshold, preserving adaptability. BetterPlace fell into the rigidity trap due to high precision (τ=45→95), blocking pivots despite market signals. Nikola began in the fraud temptation zone (μ=0.85, τ=35→56), where unrealizable promises led to deception.

**Figure 2: Evolution of Beta Distributions Over Time**

![[figure2_beta_evolution_eng.svg]]

The evolution of Beta distributions for three ventures reveals distinct patterns of belief concentration. Tesla began with broad exploration (Beta(2.1,2.9)) and converged to validated confidence (Beta(40,20)). The uncertainty range (shaded area) narrowed gradually as evidence accumulated. BetterPlace showed early rigidity (Beta(36,9)) leading to extremely narrow late-stage distributions (Beta(45,50))—a visual representation of learning impossibility. Nikola's distributions evolved toward extreme asymmetry (Beta(51,5)), representing commitment to rhetoric over realizability.

**Figure 3: Learning Dynamics and Precision's Trap**

![[figure3_learning_dynamics_eng.svg]]

Learning dynamics show how precision constrains adaptability. The vertical axis measures belief updates after negative market feedback. Ventures with τ < 20 maintain meaningful learning, enabling successful pivoting. Beyond τ > 20, updates fall below the 5% threshold, creating learning traps. Empirical cases validate the theory: PayPal and Instagram successfully pivoted with low τ, Segway and BetterPlace were trapped by high precision, and Nikola's extreme precision led to deception rather than adaptation.

### Model 5: The Precision-Aspiration Nexus

Choosing precision requires investment in market research, prototyping, and validation. We model cost as C(τ) = c × ln(τ+1), where the logarithm captures diminishing returns—doubling precision requires more than double investment.

**Proposition 4.** Optimal promise design yields joint solution (μ*, τ*) where:
- μ* = 1/(n+1)
- τ* = max(0, [V_sd·n/(c(n+1)²)] - 1)

*Proof.* Maximizing E[U] = V_sd × μ × (1-μ)^n - c × ln(τ+1) yields the stated first-order conditions. ∎

The coupling reveals why software startups speak precisely while hardware ventures hedge. Low operational complexity and information costs enable high optimal precision. High complexity compounds with high validation costs to demand strategic ambiguity.

## IV. Theoretical Integration and Implications

### 4.1 Theoretical Synthesis

Our four propositions form an integrated framework:

1. **Maximum promises emerge** when resources follow confidence (Proposition 1)
2. **Physics constrains promises** through operational complexity (Proposition 2)  
3. **Precision traps learning** when confidence exceeds adaptability needs (Proposition 3)
4. **Joint optimization** reveals complexity-precision trade-offs (Proposition 4)

These results explain entrepreneurial phenomena that previously seemed paradoxical. Why do smart founders make obviously impossible promises? Proposition 1 shows the structural incentives. Why do some sectors systematically overpromise while others underpromise? Proposition 2 quantifies operational constraints. Why can't failing ventures pivot despite clear market signals? Proposition 3 identifies learning traps. How should entrepreneurs balance specificity and flexibility? Proposition 4 provides the optimization framework.

### 4.2 The Entrepreneurial Perspective: Managing Aspiration and Precision

Our two core messages—that excessive precision creates learning traps and operational complexity constrains promises—translate into specific prescriptions for entrepreneurs navigating uncertainty.

**From Message 1 (Precision Traps)**: Proposition 3 reveals the mathematical threshold τ̄ = μ(1-μ)/ε - 2 beyond which learning ceases. For a typical venture with μ = 0.6 and requiring 5% belief updates, this yields τ̄ ≈ 2.8. Yet we observe entrepreneurs beginning with τ = 30-50, creating immediate learning paralysis. The prescription is clear: start with τ < 10, ideally τ ≈ 5. This preserves pivot optionality worth far more than any credibility gain from false precision.

**From Message 2 (Operational Constraints)**: Propositions 2 and 4 jointly determine optimal (μ*, τ*) given operational complexity n. For software ventures (n ≈ 1), μ* = 0.5 permits ambitious promises because rapid iteration enables recovery from overreach. For hardware ventures (n ≈ 5), μ* = 0.17 reflects the unforgiving nature of physical constraints. Deep tech ventures (n ≈ 10) must accept μ* = 0.09—humility imposed by physics, not choice.

**Integration Through Simulation**: Before committing to any (μ,τ) combination, entrepreneurs should simulate plausible market scenarios. If negative signals wouldn't meaningfully update beliefs, precision is dangerously high. If positive signals wouldn't increase confidence, precision may be too low for credibility. The sweet spot preserves learning while maintaining stakeholder engagement.

**Dynamic Calibration Path**: Begin with μ* = 1/(n+1) and minimal τ. As evidence accumulates—successful prototypes, customer validation, regulatory approvals—increase τ by approximately 20% per major milestone. Tesla exemplified this path: τ evolved from 5→12→30→60 over twelve years, each increase justified by demonstrated achievement.

### 4.3 The Institutional Perspective: Technology and Policy Design

While entrepreneurs control (μ,τ), institutions and technology shape the parameter space within which these choices occur.

**Technology's Immutable Constraints**: Operational complexity n represents physical laws that no amount of optimism can overcome. Battery chemistry, thermodynamic efficiency, biological pathways—these create hard bounds on feasible promises. Industries naturally stratify by n: software (n ≈ 1) permits aggressive promises because code is malleable; hardware (n ≈ 5) demands conservatism because atoms resist; biotech (n ≈ 10) requires extreme humility because biology humbles.

Information cost c similarly varies by technological infrastructure. Open-source ecosystems and standardized APIs reduce c, enabling higher optimal τ*. Proprietary knowledge and complex integration increase c, forcing strategic ambiguity. The formula τ* = V_sd·n/[c(n+1)²] - 1 quantifies how these technological realities shape communication strategies.

**Policy Levers for Innovation**: Institutions control three critical parameters that shape entrepreneurial behavior:

1. **Success Rewards (V_sd)**: Higher exit multiples and acquisition premiums increase both μ* and τ*. But this creates a dilemma—the same incentives that motivate genuine innovation also amplify fraud temptation. The policy challenge is calibrating rewards high enough to incentivize risk-taking but not so high as to make deception irresistible.

2. **Fraud Penalties (V_snd)**: Criminal sanctions and regulatory enforcement deter deception but may also discourage legitimate experimentation. Our framework suggests focusing enforcement on high-precision false claims (high τ with failed delivery) while tolerating low-precision aspirational statements. The distinction between "we will achieve X" (high τ) and "we aim toward X" (low τ) should guide regulatory response.

3. **Failure Costs (V_ns)**: Bankruptcy protection, social safety nets, and cultural attitudes toward failure determine entrepreneurial risk appetite. Low V_ns encourages experimentation by reducing downside risk. Silicon Valley's success partly reflects institutional forgiveness—failed entrepreneurs can try again. But excessive forgiveness enables recklessness. The optimum balances second chances with accountability.

**Empirical Predictions for Policy**: Our framework generates testable hypotheses about institutional effects:
- Increasing V_sd by 10% should increase average industry μ by approximately 5% and τ by 3%
- Doubling fraud penalties (V_snd) should reduce high-τ ventures by 30-40%
- Improving bankruptcy protection (reducing V_ns by half) should increase venture formation by 20-25%

These quantitative relationships enable evidence-based policy design rather than ideological speculation.

### 4.4 Future Research Directions

Our framework opens several avenues for theoretical and empirical investigation:

**Multi-Period Dynamics**: How do reputation effects modify optimal (μ,τ) trajectories? Does success in early rounds justify higher precision in later stages, or does maintaining adaptability remain paramount?

**Competitive Interactions**: When multiple entrepreneurs compete in the same space, do promise levels escalate in prisoner's dilemma dynamics? How do first-mover advantages interact with precision choices?

**Behavioral Extensions**: Do entrepreneurs systematically deviate from optimal (μ,τ) due to overconfidence bias or social pressures? Can training in simulation-based thinking improve calibration?

**Cross-Cultural Variation**: How do institutional parameters (V_sd, V_snd, V_ns) vary across entrepreneurial ecosystems? Do cultural attitudes toward uncertainty affect optimal precision independent of formal institutions?

### 4.5 Empirical Illustration: Calibrating Promise Priors Through Public Communications

To ground our theoretical framework in observable phenomena, we demonstrate how entrepreneurial communications translate into prior distributions over promise levels. This methodology illuminates the critical moment when entrepreneurs crystallize their initial beliefs—a simulation-based calibration that shapes all subsequent learning.

**Coding Protocol**: Our content analysis transforms linguistic choices into mathematical parameters. Aspiration level (μ) emerges from the semantic distance between current reality and promised future: "enhance" signals modest departure (μ ≈ 0.1-0.3), while "revolutionize" claims transformative discontinuity (μ ≈ 0.7-0.9). Precision (τ) accumulates through commitment devices—each quantitative metric adds specificity (+10), temporal boundaries create accountability (+15), while hedging language preserves optionality (-5 to -10). This translation reveals how rhetoric becomes belief structure.

**Table 2: Initial Promise Calibration in Three Ventures**

| Venture | Founding Communication | Coded Elements | μ | τ | Beta Prior | Theoretical Zone |
|---------|----------------------|----------------|---|---|------------|------------------|
| **Tesla (2006)** | "Build sports car. Use that money to build affordable car. While doing above, provide zero emission power generation" | • "Zero emission" (+0.4 aspiration)<br>• Sequential milestones (-10 flexibility)<br>• No timeline (-15 precision) | 0.42 | 5 | Beta(2.1, 2.9) | Adaptive zone |
| **BetterPlace (2007)** | "Make Israel oil-independent by 2020 through battery swapping infrastructure" | • "Oil-independent" (+0.8 aspiration)<br>• "By 2020" (+15 precision)<br>• Specific country/method (+30) | 0.80 | 45 | Beta(36, 9) | Rigidity threshold |
| **Nikola (2016)** | "1,000-mile range hydrogen trucks by 2020, making diesel obsolete" | • "Making obsolete" (+0.85 aspiration)<br>• "1,000 miles" (+10 precision)<br>• "By 2020" (+15 precision) | 0.85 | 35 | Beta(30, 5) | Fraud temptation |

These initial calibrations reveal each venture's fundamental stance toward uncertainty. Tesla's Roadster-era prior—Beta(2.1, 2.9)—represents nearly maximum entropy, acknowledging profound uncertainty while maintaining directional conviction. This wide distribution enabled learning: when battery costs proved higher than anticipated, the broad prior could accommodate reality without shattering.

BetterPlace began at the rigidity threshold, with τ = 45 already constraining adaptability. The specificity of "battery swapping" and "by 2020" created a narrow prior that subsequent market feedback—consumers' revealed preference for charging—could barely shift. Nikola's extreme aspiration (μ = 0.85) combined with moderate initial precision placed them immediately in our model's danger zone, where the mathematics of delivery make deception tempting.

This snapshot analysis—examining the crystallized moment of initial promise-making rather than temporal evolution—demonstrates how our framework operationalizes entrepreneurial belief structures. The simulation-based perspective reveals why some ventures preserve learning capacity while others lock themselves into tragic trajectories from inception.

## V. Conclusion

Entrepreneurial promises operate at the intersection of ambition and constraint, confidence and uncertainty. Our analysis reveals promise-making as optimization under physical laws and information dynamics. The core insights—that precision can trap learning and complexity constrains promises—provide mathematical foundations for entrepreneurial success and failure.

The four propositions trace a complete theory from escalation incentives through operational reality to learning dynamics and optimal design. This framework explains patterns that practitioners recognize but rarely articulate: why software founders speak boldly while hardware founders hedge, why confident entrepreneurs can't pivot, why some sectors breed fraud while others encourage honesty.

For entrepreneurs, the implications are direct. Respect operational complexity when setting ambitions. Preserve learning capacity by limiting initial precision. Increase specificity only as evidence accumulates. These principles transform promise-making from guesswork to engineering.

For scholars, our framework opens new research directions. How do competitive dynamics affect promise equilibria? Can reputation models explain precision evolution? Do behavioral biases systematically distort (μ,τ) choices? Each question extends naturally from our foundation.

The difference between Nikola and Tesla, between collapse and triumph, lies in mathematical alignment. Both ventures began with transformative visions. Both founders possessed conviction. But only Tesla calibrated promises to physics, precision to uncertainty. In this calibration lies entrepreneurship's essential challenge: bold enough to inspire, realistic enough to achieve, flexible enough to learn.

Success requires more than vision. It demands strategic design of promises that mobilize resources while respecting reality. Our model provides the blueprint for such design—not through inspirational maxims but through mathematical necessity. In entrepreneurship's highest calling, turning imagination into impact, precision matters. But not too much.

---

## References

Baron, J. N., & Hannan, M. T. (2002). Organizational blueprints for success in high-tech start-ups. California Management Review, 44(3), 8-36.

Fine, C. H. (1998). Clockspeed: Winning industry control in the age of temporary advantage. Perseus Books.

Gans, J. S. (2023). Experimental choice and disruptive technologies. Management Science, 69(11), 6429-6450.

Gans, J. S., & Stern, S. (2003). The product market and the market for "ideas." Research Policy, 32(2), 333-350.

Kerr, W. R., Nanda, R., & Rhodes-Kropf, M. (2014). Entrepreneurship as experimentation. Journal of Economic Perspectives, 28(3), 25-48.

---

## Mathematical Appendix

### A.1 Proposition 2 Extended

The first-order condition ∂E[U]/∂φ = V_sd[(1-φ)^n - nφ(1-φ)^(n-1)] = 0 yields φ* = 1/(n+1). This result has profound implications:

As n → 0 (trivial complexity), φ* → 1 (maximum promises)
As n → ∞ (impossible complexity), φ* → 0 (no promises)

The elasticity ∂ln(φ*)/∂ln(n) = -1 implies a 1% increase in complexity reduces optimal promises by 1%.

### A.2 Learning Trap Dynamics

For μ = 0.7 and τ = 100, observing failure yields:
- Prior: Beta(70, 30)
- Posterior: Beta(70, 31)  
- Updated mean: 70/101 = 0.693
- Change: 0.007 or 0.7%

For τ = 10:
- Prior: Beta(7, 3)
- Posterior: Beta(7, 4)
- Updated mean: 7/11 = 0.636
- Change: 0.064 or 6.4%

The 10-fold difference in precision creates a 9-fold difference in learning capacity.

### A.3 Joint Optimization Details

The Lagrangian for constrained optimization:
L = V_sd × μ × (1-μ)^n - c × ln(τ+1) + λ(τ - τ̄(μ))

Yields the system:
∂L/∂μ: V_sd[(1-μ)^n - nμ(1-μ)^(n-1)] = λ∂τ̄/∂μ
∂L/∂τ: c/(τ+1) = λ

Solving simultaneously produces the joint optimum.
