## (A) Mathematical Definition of Exchangeability

🗣️REQUEST1: Clear mathematical definition of exchangeability and a clear explanation of what the math is saying. 

---

**Definition.** A sequence of random variables $\{X_1, X_2, \dots\}$ is **exchangeable** if, for every finite subset and every permutation $\pi$ of indices, the joint probability of observing a particular outcome does not change when we permute the order of the variables. Formally,

$P(X_1 = x_1, \dots, X_n = x_n) \;=\; P\bigl(X_{\pi(1)} = x_1, \dots, X_{\pi(n)} = x_n \bigr)$

for all n and all permutations $\pi$.

**Interpretation.** Exchangeability says that the “labels” of the observations do not matter, only the values they take. De Finetti’s theorem states that **any** infinite exchangeable sequence can be viewed as a mixture of i.i.d. processes—intuitively, there is an unobserved parameter (“data-generating distribution”), and each observation is conditionally i.i.d. given that parameter. It is a conceptual tool from hierarchical Bayesian inference that allows us to treat outcomes or configurations as if their order does not influence their overall likelihood, focusing instead on their collective

**What the Math Is Saying.**

- **Symmetry assumption.** Observations are treated symmetrically with respect to their ordering.
- **Partial pooling.** Exchangeability often leads to “borrowing strength” across data points. In Bayesian hierarchical models, if we deem certain groups or time periods exchangeable, it implies they share common hyperparameters.
- **Subjective judgments.** In real-world settings—especially in entrepreneurship—one must decide which subsets of observations “should” be treated as exchangeable (e.g., are they from the same manufacturing process, or from the same market segment?).


next, [[eg(use(exbl))]] explains B. Simple Examples from Textbooks.

----

- 🚨 todo1: angie's intuition is, [[proof on EXPLICIT BOUNDS IN FINITE THEOREMS (from chp.7 of book ten-great-ideas-about-chance]]) is important due to the repeated theme of "conditions where with replacement from an urn can be approximated with without replacement", but lacks judgement on its priority.
