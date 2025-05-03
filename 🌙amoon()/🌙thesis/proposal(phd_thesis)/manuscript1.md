# 🕸️Introduction

# Abstract Versions

## 1. Supply-Development Focus (for Charlie Fine and Moshe Ben-Akiva)

**Abstract: Entrepreneurial Decision Model with Phase-Based Operational Uncertainty Reduction**

This thesis develops an operational framework for entrepreneurial decision-making that minimizes uncertainty rather than maximizing utility. We introduce a structured approach to sequence critical operational actions (Collaborate, Segment, Capitalize) based on their uncertainty reduction efficiency across venture development phases. Using state transition modeling, we demonstrate how different action sequences create distinct uncertainty reduction paths, allowing entrepreneurs to optimize resource allocation. Our model integrates operations management principles with discrete choice modeling to create actionable decision tools that adapt to different venture phases. Case studies in mobility ventures validate our approach, showing how entrepreneurs can systematically reduce operational uncertainties while respecting resource constraints. This work bridges the gap between theoretical models and practical implementation, providing entrepreneurs with structured methods to navigate complex decision environments.

## 2. Demand-Development Focus (for Scott Stern and Jinhua Zhao)

**Abstract: Bayesian Entrepreneurial Decision-Making Under Multi-Stakeholder Uncertainty**

This thesis develops a Bayesian approach to entrepreneurial decision-making under uncertainty, focusing on how entrepreneurs can systematically reduce demand-side uncertainty through strategic action sequencing. We formulate entrepreneurial decisions as uncertainty minimization problems where stakeholder preferences and initial venture states determine optimal action paths. The model accounts for how different actions (Collaborate, Segment, Capitalize) affect stakeholder uncertainties and demonstrates that market-focused actions early in the venture lifecycle can dramatically improve efficiency. Our empirical analysis of mobility ventures validates the model's predictive power for understanding entrepreneurial choices and outcomes. This work contributes to entrepreneurship theory by providing a mathematically rigorous framework for analyzing the previously tacit knowledge of uncertainty reduction, while offering practical guidance for entrepreneurs navigating complex market environments.

## 3. Technical Implementation Focus (for Vikash Mansinghka)

**Abstract: Probabilistic Programming for Entrepreneurial Decision Support Under Uncertainty**

This thesis develops a probabilistic programming approach to entrepreneurial decision-making under uncertainty. We formulate entrepreneurial choices as sequential decisions aimed at minimizing weighted uncertainties across demand, supply, and investor dimensions. Our model leverages advanced probabilistic programming techniques to represent the state transition dynamics between different uncertainty states based on entrepreneurial actions. We demonstrate how this approach enables entrepreneurs to reason systematically about complex decision spaces, accounting for resource constraints and stakeholder preferences. Implementation using probabilistic programming allows for efficient simulation of alternative action sequences and their uncertainty reduction effects. Case studies in mobility ventures showcase how different initial conditions and preference weights lead to distinct optimal action sequences. This work bridges theoretical entrepreneurship models with computational decision support tools, providing a foundation for AI-assisted entrepreneurial decision-making.

---

# 1.1😵‍💫Entrepreneurial Decision Models (EDM) are Unusable by Entrepreneurs

## The Fundamental Challenge

Entrepreneurial decision-making occurs in environments characterized by extreme uncertainty, multi-stakeholder interactions, and sequence-dependent outcomes. Despite decades of academic research developing entrepreneurial decision models (EDMs), practicing entrepreneurs rarely adopt these models in their actual decision processes. This creates a troubling gap between theory and practice that undermines both entrepreneurial success and scholarly advancement.

## Mathematical Formulation of the Problem

At its core, the Entrepreneurial Decision Model for Navigating Outcomes (EDMNO) can be mathematically represented as:

**Definition (EDMNO):** Given rational matrices $A_t$ ($N \times M$) and $R_t$ ($N \times P$), rational vectors $b_t$ ($M$) and $c_t$ ($P$) for $t \in 1, \ldots, T$, a set of opportunity states $\textcolor{blue}{\Omega} = {\textcolor{blue}{\omega_1}, \ldots, \textcolor{blue}{\omega_Q}}$, a non-additive uncertainty function $\textcolor{blue}{U}: \mathbb{R}^{P \times T} \times \textcolor{blue}{\Omega} \rightarrow \mathbb{R}$, and a rational number $L$, does there exist a sequence of integral vectors $x_1, \ldots, x_T$ (each of length $N$) such that $A_tx_t \leq b_t$ for all $t$, and $\textcolor{blue}{U}({R_tx_t - c_t}_{t=1}^T, \textcolor{blue}{\omega}) \leq L$ for some $\textcolor{blue}{\omega} \in \textcolor{blue}{\Omega}$, where $\textcolor{blue}{U}$ is non-additive in its first argument and represents uncertainty to be minimized?

	This can be simplified to our working notation:

$\arg\min_{\textcolor{red}{a} \in \textcolor{red}{A}} \textcolor{violet}{W_d} \textcolor{#3399FF}{U_d} + \textcolor{violet}{W_s} \textcolor{#3399FF}{U_s} + \textcolor{violet}{W_i} \textcolor{#3399FF}{U_i}$
s.t.
1. $B\textcolor{green}{S} = [\textcolor{#3399FF}{U_d}, \textcolor{#3399FF}{U_s}, \textcolor{#3399FF}{U_i}]$
2. $C\textcolor{red}{A} \leq \textcolor{#3399FF}R$
3. $\textcolor{blue}{D}(\textcolor{green}{S},\textcolor{red}{A}) = \textcolor{green}{S'}$

Where:

- $\textcolor{red}{A}$ represents the action space (entrepreneur's decisions)
- $\textcolor{green}{S}$ represents the state space (venture context)
- $\textcolor{violet}{W}$ represents stakeholder (on demand, supply, capital side - customer, operational resource partner, investor) preference weights
- $\textcolor{#3399FF}{U}$ represents uncertainty metrics to be minimized
- $B$ maps states to uncertainty measures
- $C$ maps actions to resource requirements
- $D$ is the state transition function

This formulation aligns with the "de-risking by milestones" mindset that entrepreneurs typically employ, where the goal is to minimize weighted uncertainties across different dimensions (development, stakeholder, institutional) rather than maximizing abstract utility.

**Theorem 1:** EDMNO is NP-complete, making it computationally intractable in its full form.

## The Usability Paradox

This mathematical formulation reveals the fundamental paradox: as EDMs increase in reality fit (capturing more of the complex multi-stakeholder, multi-period dynamics entrepreneurs actually face), they decrease in computational tractability. Entrepreneurs find themselves caught between models that are:

1. **Too simple**: Single-stakeholder, static models with high tractability but poor reality fit
2. **Too complex**: Multi-stakeholder with multiple operational variables that have high reality fit but intractable computation requirements

![[1.1😵‍💫Entrepreneurial Decision Models (EDM) are Unusable by Entrepreneurs 2025-04-28-10.svg]]
%%🖋 Edit in Excalidraw%%

This creates a "tractability-reality gap" in the middle where entrepreneurs abandon formal modeling altogether, reverting to intuition, imitation, or simplified heuristics that fail to capture critical decision dynamics instead of developing their own entrepreneurial style by experimenting with their unique operating environment. Without appropriate modeling tools, entrepreneurs cannot systematically learn from their context, preventing the emergence of personalized decision approaches adapted to their specific venture and market conditions.


---

# 1.2🏳️‍🌈Complexity Spectrum of Entrepreneurial Decision Models

## Progressive Spectrum of Model Complexity

The unusability of entrepreneurial decision models becomes evident when examining the progressive spectrum of model complexity:

|Model Type|Temporal Complexity|Spatial Complexity|Tractability|Reality Fit|Need for New Approach|
|---|---|---|---|---|---|
|**Strategy-Only, Single Stakeholder**|Low|Low|High|Poor|❌ No|
|**Strategy + Time Steps, Single Stakeholder**|Medium|Low|Medium-High|Moderate|⬇️ Low|
|**Strategy + Multi-Stakeholder (Static)**|Low|Medium|Medium|Moderate|⬆️ Medium|
|**Strategy + Operations + Multi-Stakeholder (Dynamic)**|High|High|Low|High|✅ Yes|
|**Full Operational Scaling + Multi-Stakeholder**|Very High|Very High|Very Low|Very High|🚨 Critical|

As temporal complexity (uncertainty unfolding over time) and spatial complexity (number of interacting stakeholders/variables) increase, the model better represents reality but becomes increasingly intractable. At the highest complexity levels—precisely where real entrepreneurial decisions exist—traditional models become unusable.
- **Temporal Complexity** = How much uncertainty unfolds over time.
- **Spatial Complexity** = How many stakeholders/variables interact.
- **Reality Fit** = How closely the model matches real entrepreneurial conditions.
- **Need for New Approach** for integrated phase-based learning + + calibrated federated learning


## Three-Dimensional Complexity Analysis

The unusability of entrepreneurial decision models stems from three interconnected dimensions of complexity:

1. **System Design Issues**: The fundamental tractability-reality tradeoff creates structural barriers to model adoption, as evidenced by the progression from strategy-only to operational-scaling EDMs.
    
2. **Individual Cognitive Barriers**: Entrepreneurs face overwhelming cognitive load attempting to infer both their own preferences and stakeholder responses, leading to ineffective causal reasoning about multi-dimensional decision spaces.
    
3. **Institutional Coordination Gaps**: Misalignment between entrepreneur pace and institutional/societal evolution creates temporal uncertainty that compounds with spatial complexity, particularly when ventures require coordination with broader ecosystem stakeholders.
    

## Toward Integrated Solutions

This thesis proposes that entrepreneurial decision models can become usable through three integrated solutions that address these complexity dimensions:

1. **Phase-based learning** to address temporal complexity through modularized approaches that adapt to different venture development stages
2. **Proactive hypothesis proposal** to address spatial complexity through probabilistic programming that navigates stakeholder interdependencies
3. **Calibrated federated learning** to address spatio-temporal complexity through entrepreneur-social planner coordination

The challenge of making entrepreneurial decision models usable isn't just academic—it directly impacts innovation capacity, resource efficiency, and entrepreneurial success rates across the economy. By developing frameworks that balance complexity and tractability while maintaining reality fit, we can bridge the theory-practice gap and empower entrepreneurs with decision tools that match the actual challenges they face.

### 🎯 Why this structure works:

- Quickly shows that as we move **right →**, reality fit increases but **tractability collapses**.
- Builds intuitive reason **why smart uncertainty minimization methods** are necessary.
- Shows **where** your methods kick in (middle-high complexity) without overwhelming readers.
    



The table below compares various entrepreneurial decision models, progressing from a simple single-stakeholder strategy to a highly detailed multi-stakeholder operational model. It shows how **temporal complexity** (time/horizon) and **spatial complexity** (breadth of stakeholders/variables) increase along this spectrum, leading to higher dimensionality, reduced tractability, and changes in phenomenological accuracy. At the extreme end, traditional optimization and heuristic methods become insufficient – underscoring the need for new approaches like **federated learning** (to manage temporal complexity) and **proactive proposal testing** (to manage spatial complexity).

| Model Type                                                         | Temporal Complexity                                   | Spatial Complexity                                         | Dimensionality                                                    | Tractability                                                                                                                                                                                                                                                                                                                                                                                                | Phenomenological Accuracy                                                                                                                                                                      | Typical Methods Used                                                                                                                                                                                                       | Need for New Approach                                                                                                                            |
| ------------------------------------------------------------------ | ----------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Basic Single-Stakeholder Strategy (Static)**                     | Low – static (single time-point decision)             | Low – single stakeholder (one perspective)                 | Low – very few variables                                          | High – highly tractable (simple; optimal solution easily found)                                                                                                                                                                                                                                                                                                                                             | Low – oversimplified (misses key dynamics and interactions) ([When models are wrong, but useful                                                                                                | Mathematical Institute](https://www.maths.ox.ac.uk/node/34245#:~:text=other%20hand%2C%20simple%20models%20are,So%20how | Intuition, basic ROI/cost-benefit analysis, simple spreadsheets                                                                                  |
| **Single-Stakeholder Dynamic Planning (Multi-period)**             | Moderate – incorporates a timeline or multiple stages | Low – single stakeholder focus (limited scope)             | Moderate – more variables introduced by time steps                | High – still tractable with standard methods (e.g. dynamic programming, scenario analysis)                                                                                                                                                                                                                                                                                                                  | Moderate – captures temporal changes, but still one perspective only                                                                                                                           | Scenario planning, forecasting models, dynamic programming                                                                                                                                                                 | Low – conventional methods handle moderate temporal complexity                                                                                   |
| **Multi-Stakeholder Strategic Model (Static Multi-criteria)**      | Low – static decision (single period)                 | Moderate – multiple stakeholders or criteria considered    | Moderate – higher dimensionality (several objectives/constraints) | Medium – must balance conflicting objectives; no single optimum (trade-offs via MCDA) (Introduction - Multicriteria Analysis for Environmental Decision-Making | Moderate – accounts for diverse perspectives at one time, but no dynamics                                                                                                                      | Multi-criteria analysis (AHP, weighted scoring), stakeholder negotiations                                                                                                                                                  | Medium – complexity grows with stakeholders; advanced support tools increasingly useful                                                          |
| **Integrated Multi-Stakeholder Dynamic Model (Moderate Detail)**   | High – multiple decision stages or time steps         | High – multiple stakeholders and functional areas included | High – many variables across time and subsystems                  | Low – computationally difficult; relies on heuristics or approximate optimization                                                                                                                                                                                                                                                                                                                           | High – captures dynamic interactions and stakeholder influences (more realistic)                                                                                                               | System dynamics models, agent-based simulations, heuristic optimization (e.g. genetic algorithms)                                                                                                                          | High – traditional methods strained; benefit from federated learning (to divide temporal scope) and proposal testing (to explore scenario space) |
| **Full High-Dimensional Multi-Stakeholder Model (Maximal Detail)** | Very High – fine-grained long-horizon dynamics        | Very High – many stakeholders & all operational variables  | Very High – extremely large state space (myriad variables)        | Very Low – intractable for exact optimization (combinatorial explosion); even simulation is hard ([When models are wrong, but useful                                                                                                                                                                                                                                                                        | Mathematical Institute](https://www.maths.ox.ac.uk/node/34245#:~:text=but%20some%20are%20useful,On%20the | Very High (in theory) – includes most real-world phenomena (highest fidelity) but nearly unmanageable due to complexity                                                                                                    | Massive-scale simulations (digital twins), exhaustive scenario exploration, AI-driven search (e.g. reinforcement learning)                       |


---

# 1.3🎞️Thesis Scope and Example Case

Three interrelated factors contribute to the unusability of current EDMs, each with significant consequences at a different level of analysis. At the fundamental **nature of the problem** level, the inherent trade-off between model tractability and reality-fit means that formal models tend to be either overly simplistic or overwhelmingly complex; consequently, entrepreneurs often **abandon formal modeling** in favor of intuition, imitation, or ad hoc heuristics. At the **individual** level, entrepreneurs’ idiosyncratic initial conditions and the cognitive difficulty of inferring both their own and others’ preferences render one-size-fits-all models ineffective – leading individuals to revert to copying others’ strategies and hindering the development of a personalized decision-making style. At the **institutional** level, insufficient modeling education for entrepreneurs and weak coordination between ventures and public stakeholders result in **fragmented, non-cumulative learning** and planning failures on a broader scale. Each of these problem dimensions is examined in depth in Section 2.Nature of problem, Section 4.Individual level of problem, and Section 6.Institutional level of problem, respectively, underscoring the need for new approaches to bridge this usability gap.

To address these challenges, this thesis proposes a three-pronged framework of solutions, summarized in the table below.

| Solution                                                                                             | Symbols                                                                                         | Complexity Addressed                           | As-is → To-be                                                                                                                                                                                          | How                                                                                        | Why                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **<span style="color:red">Phase-based learning by Entrepreneur</span>**                              | <span style="color:red">![wavy red line] D(a,s)=s'</span>                                       | <span style="color:red">Time</span>            | Too complex/too simple strategy only, one stakeholder model → Modularized, not too simple but not too complex, containing multiple operational variables with multiple stakeholders                    | Sub-path based formulation with simplex algorithm                                          | Entrepreneurs need phases to learn and change operational modes (experiment first); mobility ventures show D-shape differs between phases (from innovation/idea/value creation to value capturing with precision/operational efficiency) |
| **<span style="color:green">Proactive hypothesis proposal by Entrepreneur</span>**                   | <span style="color:green">UC/Cost = UC/State × State/Act × Act/Cost (B,D,C)</span>              | <span style="color:green">Space</span>         | Causal inference (inferring preference, initial state, and stakeholders' perception) → Synthesizing probabilistic programs (aligning explainability, participatory modeling of value creation/capture) | Multi-model probabilistic program and simplex algorithm                                    | Entrepreneurs need to understand boundaries of acceptable regions and find the fastest path toward those regions                                                                                                                         |
| **<span style="color:violet">Calibrated federated learning by Entrepreneur & Social Planner</span>** | <span style="color:violet">D mapped to D-bar interconnected equations, s'=E[s\|a], D-MDP</span> | <span style="color:violet">Time & Space</span> | City without vision or strategy → Bounded probability distribution on width and height of S-curve; dynamic consistency leading to tighter solution set                                                 | D-bar sharing through milestones (time and performance metrics in form of test quantities) | Need coordinated vision with milestones (e.g., "2030: 50% EV for California"); shift in performance measures (mile per intervention to cost per mile, range-based to efficiency-based)                                                   |
Table 1.3 A three-solution framework addressing temporal (<span style="color:red">red</span>), spatial (<span style="color:green">green</span>), and spatio-temporal (<span style="color:violet">violet</span>) complexities in entrepreneurial decision models through phase-based learning, proactive hypothesis testing, and calibrated federated learning approaches.

This table presents a comprehensive framework for addressing key complexities in entrepreneurial decision models through three integrated solutions. The <span style="color:red">red-coded phase-based learning approach</span> tackles temporal complexity by transforming overly simplistic or overly complex strategies into modularized operational models with sub-path formulations. The <span style="color:green">green-coded proactive hypothesis proposal methodology</span> addresses spatial complexity by evolving causal inference into participatory value modeling through probabilistic programming techniques. Finally, the <span style="color:violet">violet-coded calibrated federated learning system</span> combines both temporal and spatial dimensions by replacing unstructured approaches with bounded probability distributions that enable dynamic consistency through milestone-based coordination between entrepreneurs and social planners. Together, these color-coded solutions form a robust toolkit for enhancing model usability across the different complexity dimensions of entrepreneurial decision-making.


## NEED

# Markovian Entrepreneurial Decision Framework: Structured Database Table

|Concept|Mathematical Formulation|Phase Transition Bottleneck|Stakeholder Acceptance Bottleneck|Application to Sublime Systems|
|---|---|---|---|---|
|**State Vector (S)**|$S = [S_1, S_2, S_3]$ where $S_i \in {0,1}$|$S_{NAIL} \rightarrow S_{SCALE}$ transition occurs when $\sum_{i=1}^{3} S_i \geq 2$|Full acceptance requires $S = [1,1,1]$|$S_1$: Testing facility approval<br>$S_2$: Eco-builder adoption<br>$S_3$: Investor commitment|
|**Uncertainty Matrix (B)**|$B \cdot S = U$ where $B \in \mathbb{R}^{3 \times 3}$|Critical values of $B$ determine phase transition threshold: $\frac{\partial U}{\partial S}\big\vert_{S_{NAIL} \rightarrow S_{SCALE}}$|$B_{ij}$ coefficients reveal cross-stakeholder dependencies|$B = \begin{bmatrix} 0.8 & 0.6 & 0.4 \ 0.7 & 0.9 & 0.5 \ 0.3 & 0.6 & 0.8 \end{bmatrix}$ where $B_{21} = 0.7$ means testing approval reduces builder uncertainty by 70%|
|**Resource Constraints (C)**|$C \cdot A \leq R$ where $C \in \mathbb{R}^{3 \times 3}$|Resource allocation shifts at transition: $\frac{R_{SCALE}}{R_{NAIL}} > 1$|Resources must be strategically allocated to reach $S = [1,1,1]$|$C = \begin{bmatrix} 0.4 & 0.3 & 0.7 \ 0.5 & 0.6 & 0.4 \ 0.7 & 0.5 & 0.3 \end{bmatrix}$ mapping segment/collaborate/capitalize actions to resources|
|**State Transition (D)**|$D(S,A) = S'$|Transition rates increase exponentially after inflection: $\frac{dS}{dt}\big\vert_{SCALE} > \frac{dS}{dt}\big\vert_{NAIL}$|Optimal path to $[1,1,1]$ given by $\arg\max_A P(S' = [1,1,1] \| S,A)$|$D(S,A) = S + \begin{bmatrix} A_1 \cdot (1-S_1) \ A_2 \cdot (1-S_2) \ A_3 \cdot (1-S_3) \end{bmatrix} \cdot P_A$|
|**Optimization Objective**|$\min (W_1 \cdot U_1 + W_2 \cdot U_2 + W_3 \cdot U_3)$|At transition: $\frac{\Delta U}{\Delta C} = \frac{W_1 \cdot \Delta U_1 + W_2 \cdot \Delta U_2 + W_3 \cdot \Delta U_3}{\Delta C}$|Minimizing stakeholder-weighted uncertainty|For Sublime: $W = [0.3, 0.4, 0.3]$ balancing testing, builder, and investor concerns|
|**Proactive Testing**|$D_{proactive}(S, A_{multi}) = D(S, A_1) \cup D(S, A_2) \cup D(S, A_3)$|Accelerates transition by parallelizing validation: $T_{NAIL-SCALE}^{proactive} < T_{NAIL-SCALE}^{sequential}$|Enables simultaneous state changes across multiple stakeholders|Sublime can simultaneously validate with testing facilities while demonstrating to builders and investors|
|**Value Creation**|$V(S) = V_{innovation}(S) + V_{operation}(S)$|Phase transition occurs when $\frac{dV_{innovation}}{dS} = \frac{dV_{operation}}{dS}$|Total value maximized at $S = [1,1,1]$: $V([1,1,1]) > V(S)$ for all $S \neq [1,1,1]$|Sublime's value creation shifts from innovation (CO₂ reduction) to operational efficiency (cost parity)|
|**Decision Sequencing**|$\pi^*(S) = \arg\max_A \sum_{S'} P(S'|S,A) \cdot V(S')$|Optimal policy switches at transition: $\pi^__{NAIL} \neq \pi^__{SCALE}$|Sequence that maximizes probability of reaching $[1,1,1]$|

## SOL

## FULFILLMENT
from moshe_benAkiva
- you mentioned "1.Experimental (proactive)" is impractical or infeasible, but this is very usual in entrepreneurship where previous collected data hints the next experiment. I believe ultimate outcome of every model should be an action that triggers data based on which next action is chosen. Incidentally I don't trust any data collected by others (measurement issues) so my preference is experimental > hypothetical > observational