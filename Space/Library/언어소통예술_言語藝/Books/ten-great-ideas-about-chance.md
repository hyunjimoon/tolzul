---
이름: Ten great ideas about chance
출생: 2021-06-04
언어교환:
  - bayesian
  - math
  - persons
---
2025-01-27
excerpts
- kolmogorov ext: a theorem that guarantees that a suitably "consistent" collection of finite-dimensional distributions will define a stochastic process.

- komolgorov shows conflicting intuitions in borel paradox are from different choice of sigma algebra (subset of objects that are closed under 1.complement 2.countably infinite conjunctions and 3.disjunctions)
##### UNIFICATION
- differences wash out in the integral
- symmetry conditions on degrees of belief
- can be approximated on finite sequences
- exchangeable probabilities that makes the tosses independent are gotten from the surface of independence (wright manifold in population genetics) within the plane of exchangeability. points on the plane and beneast are ebl probabilities that can be represnted as averages over un

2024-12-29
sampling with vs without uncertainty

> Suppose that there are M red balls and L black balls in an urn. Sampling without replacement must give a sequence M red balls and L black balls in some order. All these outcome sequences have the same probability, so the probability is exchangeable. Sampling without replacement gives exchangeability. Call the exchangeable probability just gotten e, and suppose for reductio that it is a nontrivial mixture of two other probabilities, a and b. Both a and b must give probability 0 to outcome sequences with other than M red and L black balls. But a and b must give each outcome sequence with M red and L black balls the same probability because they are exchangeable. So a = b = e. It is not a nontrivial average. It is a vertex of the exchangeable simplex.
> Now, what if you think that there might be another trial—there might be another ball in the urn? And what if you maintain your belief that order doesn’t matter under that supposition? That is to say that your beliefs should be extendable to exchangeable beliefs on three trials. Then the point (0, 1 , 1 , 0) at the top vertex of our triangle is no longer 2 2 an option. [Why? It gives probability 0 to HH and to TT. Then its extension to three trials must give probability 0 to HHH, HHT, TTH, and TTT. If it were exchangeable, it would have to give probability 0 to any sequence with 2 heads or 2 tails in any position. But how am I to preserve probability of HT being 1 , when both its extensions, HTH 2 and HTT must have probability zero?] extendability to an exchangeable probability on 3 tosses cuts off nonindependent probabilities near the top vertex of the triangle, as shown in figure 7.3.
> extendability to more tosses further constrains the exchangeable probabilities, with them approximating the mixtures of independent ones, just as sampling without replacement from a large urn approximates sampling with replacement. The appendix to this chapter gives a careful statement (with an error term) for this finite version of the theorem.
> 

for finite setting which [[andrew_gelman]] says doesn't hold ([[📜bayesian data analysis]] chp.5.1,2,4 exercise)
##### UNIFICATION

In (9),
> μ(u) is the chance that P assigns to sequences resulting in u. (10)

The proof is precisely as in the binary case, using the law of total probability. Technically, the sum should be replaced by an integral, if X is infinite. Again we suppress such niceties; see Diaconis and Freedman* for more details.

These theorems give unique representations à la de Finetti: the most general exchangeable probability is a mixture of simple sampling distributions. Because samples with and without replacement are close, this will lead to exchangeable probabilities being close to a mixture of multinomials. We turn to making this precise.

#### EXPLICIT BOUNDS IN FINITE THEOREMS

Let X be any set and P the set of all probabilities on X (for measure-theoretic details, see Diaconis and Freedman). For F ∈ P, let F<sub>k</sub> be the independent probability on sequences of length k, so F<sub>k</sub>(A₁, ..., A<sub>k</sub>) = F(A₁)F(A₂)···F(A<sub>k</sub>) for A<sub>i</sub> subsets of X. If μ is a probability on P, let

P<sub>μk</sub>(A) = ∫ F<sub>k</sub>(A) μ(dF). (11)

Let P be an exchangeable probability on sequences of length n. For 1 ≤ k ≤ n, let P<sub>k</sub> be the marginal distribution on the first k coordinates. Thus

P<sub>k</sub>(A₁, ..., A<sub>n</sub>) = P(A₁, ..., A<sub>k</sub>, X, ..., X).

**Theorem:** Let X be a set and P an exchangeable probability on sequences of length n. Then there exists a probability μ on P such that for all k ≤ n and any set A,

|P<sub>k</sub>(A) - P<sub>μk</sub>(A)| ≤ k(k-1)/2n.

\* P. Diaconis and D. Freedman, "Finite Exchangeable Sequences," Annals of Probability 8 (1980): 45-64.

Thus, if n is large with respect to k², the first k coordinates of an exchangeable probability are uniformly well approximated by a mixture of independent identically distributed probabilities. De Finetti's theorem holds approximately! The result is often used in reverse: suppose P is an exchangeable probability on sequences of length k that can be extended to an exchangeable probability on sequences of length n (we can imagine getting more, similar data). Then P is almost a mixture of independent identically distributed probabilities.

The proof is easy and instinctive. Recall the multinomial and hypergeometric probabilities M<sub>u</sub> and H<sub>u</sub> generated by drawing with or without replacement from an urn u containing n balls labeled with various elements of X (repeats allowed). For 1 ≤ k ≤ n, let M<sub>uk</sub>, H<sub>uk</sub> be the probabilities induced on sequences of length k.

**Lemma:** For any set A and any urn u,
|M<sub>uk</sub>(A) - H<sub>uk</sub>(A)| ≤ k(k-1)/2n.

**Proof:** It is without loss of generality to take X = {1, 2, ..., n} and u = {1, 2, ..., n}. Then for any sequence x = (x₁, ..., x<sub>k</sub>) in X,

M<sub>uk</sub>(x) = 1/n<sup>k</sup>,

H<sub>uk</sub>(x) = {
  1/(n(n-1)···(n-k+1)) if all x<sub>i</sub> distinct
  0 otherwise.
}

It follows that the worst case for A is A = {x: all x<sub>i</sub> distinct}. Since H<sub>uk</sub>(A) = 1 and M<sub>uk</sub>(A) = n(n-1)...(n-k+1)/n<sup>k</sup>. For this A, direct computation shows

|M<sub>uk</sub>(A) - H<sub>uk</sub>(A)| = 1 - n(n-1)···(n-k+1)/n<sup>k</sup>.

Using (1-x)(1-y) = 1-x-y+xy ≥ 1-x-y (if x,y > 0), we see

n(n-1)...(n-k+1)/n<sup>k</sup> = (1-1/n)(1-2/n)···(1-(k-1)/n) ≥ 1-(1+···+(k-1))/n = 1-k(k-1)/2n.

Thus, for any A,
|M<sub>uk</sub>(A) - H<sub>uk</sub>(A)| ≤ k(k-1)/2n. QED

**Remark:** Note that the preceding calculations simply involve calculating the chance that a sample of size k from {1, 2, ..., n} with replacement yields all distinct elements. This is just the birthday problem of chapter 1. It is straightforward to show that for the chosen A, |M<sub>uk</sub>(A) - H<sub>uk</sub>(A)| ≥ 1-e<sup>-k(k-1)/2n</sup>. Thus our analysis is sharp; k²/n must be small to have the two distributions close.

To conclude, let P be an exchangeable probability on sequences of length n. We saw that P can be exactly represented as a mixture of urn measures H<sub>u</sub>. The mixing measure μ is simply induced by P: pick from P, what's the chance that the induced sample gives the urn u? Now,

|P<sub>k</sub>(A) - M<sub>μk</sub>(A)| = |∫ H<sub>uk</sub>(A) μ(du) - ∫ M<sub>uk</sub>(A) μ(du)| ≤ ∫ |H<sub>uk</sub>(A) - M<sub>uk</sub>(A)| μ(du) ≤ k(k-1)/2n.

This concludes the proof of the general de Finetti theorem.

**Remark:** Of course, the version of de Finetti's theorem for arbitrary X yields a theorem when X = {0, 1}. For this case, something sharper can be said. By using a sharper bound for sampling with and without replacement for urns with only two kinds of balls, Diaconis and Freedman proved the following theorem.

**Theorem:** Let P be an exchangeable probability on binary sequences of length n. Then there exists a probability μ on [0, 1] such that |P<sub>k</sub>(A) - P<sub>μk</sub>(A)| ≤ 4k/n for any set A.

Thus only k/n needs to be small (rather than k²/n being small).


2024-12-06
using https://xianblog.wordpress.com/2017/11/13/10-great-ideas-about-chance-book-preview/

| Chapter Number | Chapter Title          | Key Message Summary                                                                                                                                                                                    | Key Concepts & Technical Details                                                                                                                   | Historical Significance                                      |                                                                                                 |
| -------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| 1              | Measurement            | • Chance can be measured analogously to physical quantities like length<br>• The concept of equiprobability is fundamentally challenging to teach and understand                                       | • Historical development of probability measurement<br>• Cardano's contributions beyond cubic equations<br>• Conceptual foundations of probability | First systematic attempts to quantify chance and probability |                                                                                                 |
| 2              | Ramsey's Legacy        | • Probability can be derived from expectations rather than vice versa<br>• Joins probability and utility theory<br>• Dutch book arguments have limitations                                             | • Dutch book theorem<br>• Betting frameworks<br>• Utility theory foundations                                                                       | Ramsey's work bridges probability theory and decision-making |                                                                                                 |
| 3              | Psychology             | • Human decision-making often deviates from rational probability theory<br>• Distinction between risk (quantifiable) and uncertainty (non-quantifiable)<br>• Framing effects impact decision-making    | • Allais paradox<br>• Ellsberg's distinction<br>• Tversky and Kahneman's heuristics<br>• Framing effects                                           | Shows gap between theoretical probability and human behavior |                                                                                                 |
| 4              | Frequency              | • Explores tension between frequency-based and theoretical probability<br>• Introduces "Bernoulli's swindle" - limitations of frequency interpretation<br>• Addresses fundamental nature of randomness | • Law of Large Numbers<br>• Von Mises' Kollectiven<br>• Wald's contributions<br>• Randomness definitions                                           | Foundational for understanding stochastic processes          |                                                                                                 |
| 5              | Mathematics            | • Necessity of measure theory for advanced probability<br>• Kolmogorov's axiomatization<br>• Proper definition of conditional probability                                                              | • Measure theory foundations<br>• Kolmogorov's axioms<br>• Conditional probability as random variable                                              | Establishes mathematical rigor in probability theory         |                                                                                                 |
| 6              | Inverse Inference      | • Bayes' theorem and its historical context<br>• Laplace's contributions<br>• Role of prior distributions in binomial settings                                                                         | • Bayesian inference<br>• Prior selection<br>• Historical development of statistical thinking                                                      | Links probability theory to statistical inference            |                                                                                                 |
| ⭐️7            | De Finetti             | • Exchangeability as foundation for statistical inference<br>• Connection between exchangeability and sufficiency (🚨)<br>• Representation theorem for exchangeable sequences                          | • Exchangeability<br>• Partial exchangeability<br>• Markov exchangeability<br>• Sufficiency                                                        | Provides theoretical foundation for Bayesian statistics      | [[🌏(🧭)E(bp).environment affecting belief and prior]]<br><br>product<br>jobs to be done (signal from air, elec) |
| 8              | Algorithmic Randomness | • Computational approaches to defining randomness<br>• Martin-Löf's test for randomness<br>• Kolmogorov complexity                                                                                     | • Turing machines<br>• Computability theory<br>• Random number generators<br>• Complexity measures                                                 | Connects probability to computer science                     |                                                                                                 |
| 9              | Physical Chance        | • Statistical mechanics and probability<br>• Quantum mechanics and probability interpretations<br>• Ergodicity in physical systems                                                                     | • Thermodynamic probability<br>• Quantum probability<br>• Ergodic theory<br>• Bell's theorem                                                       | Links probability theory to physical sciences                |                                                                                                 |
| 10             | Induction              | • Hume's problem of induction<br>• Role of skeptical priors<br>• De Finetti's theorem as solution to inductive skepticism                                                                              | • Philosophical foundations<br>• Prior probability theory<br>• Skeptical priors<br>• Meta-probability                                              | Connects probability to philosophy of science                |                                                                                                 |

**Key Themes Across Chapters:**
1. **Mathematical Foundations:**
   - Evolution from informal to rigorous mathematical treatment
   - Role of measure theory
   - Importance of proper axiomatization

2. **Philosophical Challenges:**
   - Nature of probability itself
   - Relationship between frequency and theoretical probability
   - Problem of induction
   - Role of subjectivity

3. **Practical Applications:**
   - Decision theory
   - Statistical mechanics
   - Quantum mechanics
   - Computational randomness

4. **Historical Development:**
   - From gambling problems to modern theory
   - Key contributors across centuries
   - Evolution of different interpretations

5. **Interdisciplinary Connections:**
   - Physics
   - Psychology
   - Computer Science
   - Philosophy
   - Statistics


2021-06-04

\- How chance is solidified as probability and applied to mathematics, statistics, economics, and finance to physics and computer science

\- Starting from Cardano and Ramsey who thought chance and judgement could be measured it extends to how frequency is related to chance, and how chance, judgment, and frequency could be unified. Bayes laid the foundation of modern statistics, Hume explored the problem of induction, Kolmogorov laid general mathematical framework for probability. Application of computability to chance, why chance is essential to modern physics, and lastly we are psychologically predisposed to error when judging chance (Kahneman, Tversky) are introduced.

---

# CHP5. MATHEMATICS
- Borel paradox and shows that conflicting intuitions are merely the reflection of the choice of different sigma algebras.
# CHP10. UNIFICATION

### Introduction

Cardano introduced inferences from chance to frequencies. Bayes and Laplace extended this to infer frequencies to chance within probabilistic degrees of belief. But, fundamentally, **what is chance?**

- Bruno de Finetti argued: **Chance does not exist.**
- His position was that we can operate "as if" chance exists, even if it doesn’t.

This view challenges the notion of probability as a physical property (objective chance) and offers an alternative grounded in **exchangeable degrees of belief.**

---

### Exchangeability

- **Definition:** Order doesn't matter. The probability of sequences with the same relative frequency of events (e.g., heads and tails) remains the same.
- **Example:** A coin flip with an unknown bias, under Laplace's rule of succession, produces probabilities invariant under permutations.

#### Key Insight:
- Exchangeability replaces independence when modeling degrees of belief.
- De Finetti's theorem states that any exchangeable sequence can be treated **as if** derived from a model with independent trials and uncertain bias (subjective Bayesian probability).

---

### Finite Exchangeable Sequences

- Exchangeability can be approximated in finite cases.
- Example: Two coin flips, probabilities lie in a tetrahedron of possible outcomes. Constraints emerge from properties like symmetry and transition probabilities.

#### Geometry of Exchangeability:
- **Extreme Points:** Represent urn models with fixed compositions (e.g., red and black balls sampled without replacement).
- **Simplicity:** Order invariance restricts the probability space, creating a "simplex."

---

### Generalization to Arbitrary Observables

- De Finetti's theorem extends beyond binary outcomes (e.g., heads/tails) to arbitrary observables:
  - Example: Weather patterns, color classifications, numerical measurements.
- **Mathematical Formulation:** P(A1, A2, ..., An) = ∫ F(A1)F(A2)...F(An) µ(dF)
- - Where `µ` represents a distribution over all possible probabilities.

---

### Partial Exchangeability and Markov Chains

1. **Partial Exchangeability:**
 - Allows analogies between events without requiring full symmetry.
 - Example: Comparing results from trials involving two different coins.

2. **Markov Exchangeability:**
 - Sequences depend on prior outcomes, capturing patterns in dependencies (e.g., Markov chains).
 - Representation: Mixtures of stationary Markov processes.

---

### Practical Implications

De Finetti's theorem bridges **subjective beliefs** and **statistical models**:
- **Bayesian Perspective:** Inference relies on symmetry and exchangeability, not the existence of physical chance.
- **Finite Approximations:** Useful in practical contexts where infinite sequences are unrealistic.

---

### Applications

#### Normal Distribution
- A special case for exchangeable sequences under specific constraints.
- Challenges include finding natural symmetry characterizations.

#### Ergodic Theory
- Extends De Finetti’s ideas to time-invariant (stationary) processes, connecting probability and frequency.

---

### Summing Up

Bayes and de Finetti both provided foundational insights:
- **Bayes:** Parameterized chance models using priors.
- **De Finetti:** Reframed these models through symmetry in beliefs, showing chance as a "placeholder" for symmetry conditions.

---

### Appendices

1. **Ergodic Theory:** Links probability measures to stationary processes and expands De Finetti's framework.
2. **De Finetti’s Theorem (Detailed):** Covers both binary and general cases, offering finite-to-infinite extensions.

