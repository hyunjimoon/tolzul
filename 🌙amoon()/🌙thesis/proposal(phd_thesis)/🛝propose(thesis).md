
## Overview

On Thursday, I'll analyze three phrases from Joni Mitchell's "Both Sides Now" to compare Bolton et al.'s moral hazard framework with Moon's STRAP model. Using the primal-dual foundation from Moon, we'll explore how entrepreneurs and social planners can navigate uncertainty through three key processes.

---

## Three Perspectives: From Both Sides Now

| Bolton et al.                                                                                                    | Moon (STRAP)                                                                                        |
| ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Binary experiment outcomes<br>False positives/false negatives<br>Private benefit Z                               | Multiple stakeholder states<br>Entropy-based uncertainty<br>Multi-stakeholder preferences           |
| Investor-entrepreneur contract<br>Limited to two parties<br>Market failure or inefficient funding                | Stakeholder coordination<br>Multiple stakeholders with thresholds<br>Weighted uncertainty reduction |
| Moral hazard in experiment design<br>Ventures failing post-experiment<br>University validation, proof-of-failure | Strategic experiment selection<br>Bottleneck uncertainties<br>Dual variable optimization            |


| Bolton et al.                                                                                                    | Moon (STRAP)                                                                                        | Keywords                                           | Section                                   |
| ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ----------------------------------------- |
| Binary experiment outcomes<br>False positives/false negatives<br>Private benefit Z                               | Multiple stakeholder states<br>Entropy-based uncertainty<br>Multi-stakeholder preferences           | Perspective<br>Illusion<br>Motivation<br>Tradeoffs | **I. 🧭 Agents Perceive to Act**          |
| Investor-entrepreneur contract<br>Limited to two parties<br>Market failure or inefficient funding                | Stakeholder coordination<br>Multiple stakeholders with thresholds<br>Weighted uncertainty reduction | Exchange<br>Complexity<br>Outcomes                 | **II. 🗺️ Society Dualize to Distribute** |
| Moral hazard in experiment design<br>Ventures failing post-experiment<br>University validation, proof-of-failure | Strategic experiment selection<br>Bottleneck uncertainties<br>Dual variable optimization            | Concealment<br>Failure<br>Solutions                | **III. 🧬 Agents Act to Perceive**        |

[[📜Bolton24]]
# Variable Mapping Between Papers

| Bolton et al. Concept           | Bolton Variable | Moon Concept                | Moon Variable                                                                                     |
| ------------------------------- | --------------- | --------------------------- | ------------------------------------------------------------------------------------------------- |
| Venture value if successful     | $V$             | Venture value               | <span style="color:orange">$f_{js}$</span> (stakeholder state values)                             |
| Prior probability of success    | $p_0$           | Prior probability           | <span style="color:blue">$\vec{p}_j = (p_{j1}(x),\ldots,p_{jS}(x))$</span> (choice probabilities) |
| Cost of experiment              | $C$             | Cost coefficient            | <span style="color:cyan">$c_j$</span>                                                             |
| Cost of full development        | $K$             | Budget constraint           | <span style="color:cyan">$R$</span> (total budget)                                                |
| Experiment specificity          | $s_1$           | Venture attributes          | <span style="color:gray">$x$</span> (affects choice probabilities)                                |
| Experiment sensitivity          | $s_2$           | Stakeholder preferences     | <span style="color:gray">$\beta_{js}$</span> (affects choice probabilities)                       |
| Entrepreneur's private benefit  | $Z$             | Not explicitly modeled      | N/A                                                                                               |
| Investor ownership stake        | $\alpha$        | Not explicitly modeled      | N/A                                                                                               |
| Expected payoff from experiment | $\pi_{s_1,s_2}$ | Uncertainty                 | <span style="color:blue">$H(\vec{p}_j)$</span>                                                    |
| Proof-of-failure payment        | $X$             | Not explicitly modeled      | N/A                                                                                               |
| Not explicitly modeled          | N/A             | Actions                     | <span style="color:red">$a_j$</span> (weeks)                                                      |
| Not explicitly modeled          | N/A             | Optimal decision            | <span style="color:red">$a^*_j$</span> (weeks)                                                    |
| Not explicitly modeled          | N/A             | Threshold targets           | <span style="color:orange">$\mu_j$</span>                                                         |
| Not explicitly modeled          | N/A             | Dual variable for threshold | <span style="color:orange">$\lambda_j$</span>                                                     |
| Not explicitly modeled          | N/A             | Dual variable for resource  | <span style="color:cyan">$\gamma$</span>                                                          |

Based on the color scheme in the image:

- <span style="color:blue">Blue</span>: Choice probabilities and uncertainty metrics
- <span style="color:red">Red</span>: Actions and decisions
- <span style="color:orange">Orange</span>: Threshold targets, state values, and threshold dual variables
- <span style="color:cyan">Cyan</span>: Budget, cost coefficients, and resource dual variables
- <span style="color:gray">Gray</span>: Entrepreneur's attributes and stakeholder preferences



| Variable group           | Variable                                                                                             | Description                                                                 | Unit           | Category                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------- |
| **State Variables**      |                                                                                                      |                                                                             |                |                                                                                         |
|                          | <span style="color:skyblue">$\vec{p}_j = (p_{j1}(x),\ldots,p_{jS}(x))$</span> (choice probabilities) | Probability that stakeholder j assigns to outcome state s                   | Unitless (0-1) | <span style="color:green">Effective</span>                                              |
|                          | <span style="color:orange">$f_{js}$</span> (stakeholder state values)                                | Value associated with stakeholder j choosing state s                        | $              | <span style="color:green">Effective</span>                                              |
|                          | <span style="color:orange">$\mu_j$</span>                                                            | Threshold target value for stakeholder j                                    | $              | <span style="color:purple">Satisfactory</span>                                          |
|                          | <span style="color:cyan">$c_j$</span>                                                                | Cost of action j                                                            | $              | <span style="color:red">Efficient</span>                                                |
|                          | <span style="color:cyan">$R$</span> (total budget)                                                   | Budget/resources available                                                  | $              | <span style="color:red">Efficient</span>                                                |
| **Action Variables**     |                                                                                                      |                                                                             |                |                                                                                         |
|                          | <span style="color:red">$a_j$</span>                                                                 | Binary decision variable indicating whether action j is taken               | Unitless (0/1) | <span style="color:red">Efficient</span>                                                |
| **Diagnostic Variables** |                                                                                                      |                                                                             |                |                                                                                         |
|                          | $H(p_j)$                                                                                             | Entropy measuring uncertainty in stakeholder j's choice distribution        | bits           | <span style="color:green">Effective</span>                                              |
|                          | <span style="color:orange">$\lambda_j$</span>                                                        | Dual variable for threshold constraint - shadow price of relaxing threshold | bits/$         | <span style="color:purple">Satisfactory</span>                                          |
|                          | <span style="color:cyan">$\gamma$</span>                                                             | Dual variable for resource constraint - shadow price of additional resource | bits/$         | <span style="color:red">Efficient</span>                                                |
|                          | Primal-dual gap                                                                                      | Convergence measure quantifying distance from optimality                    | bits           | <span style="color:purple">Satisfactory</span>                                          |
| **Key Trends**           |                                                                                                      |                                                                             |                |                                                                                         |
|                          | $H(p_j)$                                                                                             | Decreases as ventures mature                                                | bits ↓         | <span style="color:green">Effective</span>                                              |
|                          | Dual variable                                                                                        | Decrease as ventures gains feasibility                                      | bits/$ ↓       | <span style="color:red">Efficient</span>/<span style="color:purple">Satisfactory</span> |
|                          | Primal-dual gap                                                                                      | Converges to zero indicating stakeholder alignment                          | bits → 0       | <span style="color:purple">Satisfactory</span>                                          |

Note: Colors represent categories from the framework:

- <span style="color:red">Red</span>: Efficient (resource utilization)
- <span style="color:green">Green</span>: Effective (goal achievement)
- <span style="color:purple">Purple</span>: Satisfactory (convergence diagnostics)
- 
---

## I. 🧭 Agents Perceive to Act: "Cloud Illusions"

> _"I've looked at clouds from both sides now<br>From up and down and still somehow<br>It's cloud illusions I recall"_

### Bolton et al.:

- **Perspective**: Binary experiment outcomes (Pass/Fail)
- **Illusion**: Experiments with false positives create illusion of progress
- **Key Equation**: $P(s = P|v = V) = s_1$ (specificity)

---

### Moon (STRAP):

- **Perspective**: Multiple stakeholder states (Reject, Consider, Accept)
- **Illusion**: Entropy as measure of true uncertainty
- **Key Equation**: $H(\vec{p}_j) = -\sum_s p_{js} \log p_{js}$

---

### Action Proposal 1:

Entrepreneurs should quantify uncertainty as entropy rather than probability, acknowledging the multi-state nature of stakeholder decisions to avoid the illusion of binary outcomes.

---

## II. 🗺️ Society Dualize to Distribute: "Something's Lost, Something's Gained"

> _"Well, something's lost, but something's gained<br>In living every day"_

---

### Bolton et al.:

- **Exchange**: Investor-entrepreneur contract (α)
- **Complexity**: Limited to two stakeholders
- **Outcomes**: Market failure or inefficient funding

---

### Moon (STRAP):

- **Exchange**: Coordination across multiple stakeholders
- **Complexity**: Multiple thresholds μⱼ with dual variables λⱼ
- **Outcomes**: Optimized uncertainty reduction across stakeholders

---
### Action Proposal 2:

Social planners should adopt dual-variable frameworks to identify which stakeholder constraints are truly binding (highest λⱼ), as these may not be the ones that appear unsatisfied in a binary framework.

---

## III. 🧬 Agents Act to Perceive: "From Give and Take"

> _"I've looked at love from both sides now<br>From give and take and still somehow"_

---

### Bolton et al.:

- **Concealment**: Moral hazard in experiment design
- **Failure**: Failed ventures after passing misleading experiments
- **Solutions**: Paying for proof of failure (X ≥ Z)
---

### Moon (STRAP):

- **Concealment**: Strategic selection of which uncertainty to reduce first
- **Failure**: Unidentified bottleneck uncertainties
- **Solutions**: Primal-dual optimization of experiment selection

---
### Action Proposal 3:

Entrepreneurs should design experiments that explicitly target the highest-weighted uncertainties (by λⱼ) rather than maximizing pass probability, while investors should reward information gain rather than just success.

---

## Synthesis: Both Sides Now

The STRAP framework helps mitigate moral hazard by:

1. **Quantifying the true value of uncertainty reduction** rather than binary success/failure
2. **Identifying non-obvious bottlenecks** through dual variables
3. **Aligning incentives around information gain** rather than experiment outcomes

---

By integrating insights from both models, we can create a more robust approach to entrepreneurial decision-making under uncertainty.

_"I've looked at life from both sides now<br>From win and lose and still somehow<br>It's life's illusions I recall<br>I really don't know life at all"_

---


I'm reaching out to introduce my favorite english song: from both sides now
On thursday, I will sample three phrases from this song and use these to scaffold comparing the assigned paper (Bolton) with mine (Moon25). 
using the primal dual model from moon25, i will walk you though how  [[I.🧭Agents Perceive to Act]], [[II.🗺️Society Dualize to Distribute]], [[III.🧬Agents Act to Perceive]] to suggest three action proposals for entrepreneurs and social planners. 

# entreperneur
To be specific, entrepreneurs should model their value system by choosing $w_{j}, f_{jk}, c$, 

## social planner
![[🗄️table_of_contents]]
## social planner

and social planner should lower $c, \mu, $ from [[2.2📐Produce solution(🗺️)]]framing (rows of 

Society should report $\bar{p},$ f, mu, c so

i'll solve posed questions by contrasting bolton's research with mine.
- binary vs K-bucket
- single stakeholder (entrepreneur and investor) vs multi stakeholder
- investor-centered vs founder-centered (bumble)

cause of moral hazard (dating app)? information asymmetry (unavoidable) implemented as , judged by god who can see both side
only woman can choose

[[Both sides now]]
solving four questions on 


introduce research on 

# 4. 
# 5. future work 
JK value system cld

| Section                                         | fig./interactive. |
| ----------------------------------------------- | ----------------- |
| [[I.🧭Agents Perceive to Act]]               |                   |
| [[II.🗺️Society Dualize to Distribute]]        |                   |
| [[III.🧬Agents Act to Perceive]] |                   |


| Section                                         | fig./interactive.                                                                                                                                             | Decision Variable                                                                                                                                                                    |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [[I.🧭Agents Perceive to Act]]               | Bayesian decision tool for entrepreneurs to model stakeholder uncertainties and generate actionable strategies from abstracted representations                | ~a_j = perception decisions to process stakeholder uncertainties through entropy H(~p_j) and Bayesian logit models mapping venture attributes to stakeholder choice probabilities    |
| [[II.🗺️Society Dualize to Distribute]]        | Optimization mechanism using dual variables to dynamically distribute resources across stakeholders with competing needs while satisfying thresholds          | λ_j, γ = threshold and resource dual variables representing shadow prices that guide fair resource allocation by balancing threshold satisfaction (λ_j) with resource efficiency (γ) |
| [[III.🧬Agents Act to Perceive]] | Sequential learning framework where individual entrepreneurial experiments provide data to update global strategies and improve collective ecosystem outcomes | a__j = optimal action selection that maximizes information gain per resource unit by solving the primal-dual optimization: a__j = arg max_aj (ΔH + Σ_j λ_j Δ(f_j·p_j))/c_j           |

### 2.1 Perception

| Inputs                                          | Outputs                                                            |
| ----------------------------------------------- | ------------------------------------------------------------------ |
| Entrepreneur's Attributes: $x \in \mathbb{R}^n$ | Choice probabilities: $\vec{p}_j = (p_{j1}(x), \ldots, p_{jS}(x))$ |
| Stakeholder preferences: $\beta_{js}$           | Uncertainty: $H(\vec{p}_j) = -\sum_s p_{js} \log_2 p_{js}$         |
|                                                 |                                                                    |

### 2.2 Action

| Inputs | Outputs |
|--------|---------|
| Actions: $a_j \in \{0,1\}$ (weeks) | Decision: $a_j^* = \arg\max_{a_j} \frac{\Delta H_j + \sum_j \lambda_j \Delta(f_j \cdot p_j)}{c_j}$ (weeks) |
| Threshold targets, State values: $\mu_j, f_{js}$ | Dual variable for threshold: $\lambda_j = \max\{0, w_j(µ_j - \sum_s f_{js}p_{js})/µ_j\}$ |
| Budget & cost coefficient: $R, c_j$ | Dual variable for resource: $\gamma = S(a^*)$ |

$\simeq$ attributes, preferences coefficient (various); $\simeq$ probabilities (unitless) $\simeq$ uncertainty (bits); $\simeq$ actions (weeks);
$\simeq$ thresholds (\$), values(\$), dual var. (bits/$); $\simeq$ budget (\$), cost coefficient (\$/week), resource dual var. (bits/$);

The STRAP framework integrates these three components through:

1. Perception (Agents Abstract) - Models stakeholder uncertainties using Bayesian methods
2. Distribution (Society Dualizes) - Uses dual variables to coordinate resource allocation
3. Optimization (Agent Samples) - Selects experiments that maximize information gain per resource unit
