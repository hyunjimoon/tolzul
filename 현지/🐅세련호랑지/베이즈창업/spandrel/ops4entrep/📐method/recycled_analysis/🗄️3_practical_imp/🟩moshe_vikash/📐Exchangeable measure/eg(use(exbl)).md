
## (B) Simple Examples from Textbooks

🗣️REQUEST2: Several simple, clearly explained examples of how exchangeability has been used or explained in textbooks. 

----
### 1. 🟩 Statistics

-  Characterized by _explicit objective functions and constraints_
-  Exemplified by operations research methods, discrete-choice modeling, or linear programming
-  Focus is on finding an _optimal policy/decision_ given a deterministic or stochastic model

🟩  Moshe's deterministic utility-based discrete-choice
🟩 🟩  does MWG has this?? micro-econ + linear programming texts

De Finetti's representation theorem provides a fundamental characterization of exchangeable sequences - sequences whose probability distribution is invariant under permutation. Mathematically, for a sequence X₁, X₂, ..., Xₙ, exchangeability means p(x₁,...,xₙ) = p(xπ(1),...,xπ(n)) for any permutation π. The theorem states that for an infinite exchangeable sequence of binary random variables, there exists a generating function g(z) ≥ 0 such that p(r|n) = ∫₀¹(n,r)z^r(1-z)^(n-r)g(z)dz, where p(r|n) is the probability of r successes in n trials. This representation has profound implications: it shows that exchangeable sequences are equivalent to mixtures of independent, identically distributed sequences. Jaynes (1982) [[📜Jaynes82_appl_ext_definetti]]  extended this by showing that the representation holds for finite sequences if we drop the non-negativity constraint on g(z), demonstrating how apparently simple symmetry assumptions lead to powerful mathematical structures. This is exemplified in applications like modeling bank deposits (where account sizes are exchangeable) or particle systems in physics (where particle positions are exchangeable), making it a cornerstone of both theoretical statistics and applied probability. 

**Bayesian inference (updating) itself can be framed as an optimization over distributions**—minimizing a cumulative loss that balances data-fit against prior beliefs

[[📜mcerleath_rethinking]]
### 2. 🔵Simulation                                                             

- Encompasses both **agent-based** (micro-level entities with behavioral rules) and **compartment-based** (aggregate stock-and-flow) methods
- Highlights _emergent behavior_ from interacting components, feedback loops, or population-level processes
- More flexible at capturing **nonlinear, dynamic** phenomena but can be more complex

once choices are discretized, it becomes nonlinear (output variables (probability) are bounded but input variables are non-bounded)


🔵Business Dynamics: **Urn Models (Berger, _Statistical Decision Theory & Bayesian Analysis_).Classic Polya’s Urn Example:_ If you draw colored balls from an urn without replacement, the draws can be exchangeable over short horizons. A re-labeling of the draw order does not change how the color counts evolve from the prior perspective.
### 3. 🔴 Modeling Workflow 
    
- Rooted in **probabilistic/Bayesian** reasoning
- Focus is on _learning unknown parameters_ from data, updating priors to posteriors
- Good for **quantifying uncertainty** and “borrowing strength” across partially exchangeable groups

🔴 Mosche's random utility based discrete choice model - $P(U_1 > U_j ;\ \forall j)$ + model selection problem
🔴🔴 Gelman’s _Bayesian Data Analysis_ chp.5 (5.3,4), chp.7, model checking, 9

---

- 🚨🚨todo2: cite chung textbook

