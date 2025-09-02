
## 3. Foundations of modeling and inference

### rational ai principle3
 🪒auto occam's razor: hierarchical model encodes uncertain beliefs and sampling navigates that uncertainty representation. together, they form consistent algorithm for probabilistic inference which behaves rationally compared to those violating consistency hence making predictably irrational decisions.

### applying principle 1,2,3

| Module | Topic                                                | Rational AI Principle | How                                                                                                                        | Contrast                                                                                                                             | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------ | ---------------------------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3      | Foundations of modeling and inference                | 🪒Auto Occam's Razor  | Sample from hierarchical models with latent hyperparameters rather than optimize fixed models                              | Explicit regularization requires manual tuning; sampling naturally favors typical solutions                                          | **Polynomial regression with outlier detection**. Assign a prior over both the degree of the polynomial and outlier/noise parameters; then use posterior _sampling_ to infer model complexity. A naive optimizer might pick a high-degree polynomial that overfits, whereas the Bayesian sampler automatically leans toward simpler polynomials unless evidence strongly demands complexity, thus embodying “Occam’s razor” without manually fiddling with penalty terms.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

- 🗣️[vikash seminar modeling inference.txt](https://github.com/user-attachments/files/18985826/vikash.seminar.modeling.inference.txt)

### Table 1: Shallow summary
Model Aspect | Description
-- | --
🎯 Big Idea | Probabilistic modeling allows us to represent uncertainty about both parameters and model structure itself, enabling rational inference from limited data.
⭐️ Key Principles | • Bayesian Occam's Razor: Models of appropriate complexity emerge naturally through marginal likelihood<br>• Model Complexity: How falsifiable a model is relative to how well it fits data - not just parameter count<br>• Hierarchical Bayesian Modeling: Replace fixed parameters with latent variables to be inferred<br>• Marginal Likelihood (p(D\|m)): Integrates over all possible parameter values; automatically balances complexity and fit
🔍 Model Selection | • Too Simple Models: Can only generate a narrow range of datasets, unlikely to fit observed data<br>• Too Complex Models: Can generate many possible datasets, so assign low probability to any specific one<br>• "Just Right" Models: Balance specificity and flexibility, maximizing p(D\|m)
🌲 Hierarchical vs. Fixed | • Fixed Models: Manual parameter setting, brittle to misspecification<br>• Hierarchical Models: Parameters themselves have distributions, allowing automatic adaptation<br>• Example: Fixed outlier probability vs. inferring outlier probability from data


### Table 2: Deep dichotomy

| Inference Aspect | 🧮 Optimization-Based | 🪙 Sampling-Based |
|------------------|----------------------|-------------------|
| **Goal** | Find single best solution (MAP) | Represent entire distribution of solutions |
| **Mathematical Expression** | argmax<sub>θ</sub> p(θ\|D) | Draw samples from p(θ\|D) |
| **Typical Behavior** | Finds mode of distribution | Samples from typical set (often far from mode) |
| **Relationship to p(D\|m)** | Does not naturally compute marginal likelihood | Naturally approximates marginal likelihood via samples |
| **High-Dimensional Behavior** | Focuses on unlikely region (mode) | Focuses on probable regions (typical set) |
| **Computational Properties** | • Often gets stuck in local maxima<br>• Can be inefficient in non-convex settings | • Often more efficient than optimization in non-convex settings<br>• Equivalent to optimization in convex settings |
| **Engineering Simplification** | Model collapse to single point estimate | Approximation of full distribution via finite samples |
| **Impact on Rationality** | Sacrifices uncertainty representation | Maintains rational uncertainty management |
| **Cautionary Note** | "Building AI systems without understanding how optimization shortcuts relate to proper probability theory is like building bridges without understanding how engineering simplifications affect structural integrity." | Must still understand sampling approximation quality |

<h3>Integrated Paragraph Summary</h3>
<p>The foundations of modeling and inference rest on two complementary dimensions: how we represent uncertainty in model space and how we compute with that uncertainty. Table 1 explores the model space, highlighting how hierarchical Bayesian models naturally implement Occam's Razor through the marginal likelihood p(D|m), which integrates over all parameter values p(θ|m) to evaluate how well a model class explains data p(D|θ,m). This integration naturally penalizes overly complex models without requiring explicit regularization. Vikash didn't cover it but I especially liked the log2(1/p(D|m)) as "number of bits of surprise at observing data D under model m" interpretation as a recent study in my field showed decision makers should experiment with more “surprising” theories because in this case experiments are more informative and enable more learning (Camuffo et al., Theory-Driven Strategic Management Decisions).

Table 2 then examines how we navigate this model space, contrasting optimization (which finds single solutions often in improbable regions) with sampling (which represents typical behavior under the model). Together, these approaches create a synergy: hierarchical models provide the structure for encoding appropriate uncertainty, while sampling provides the computational mechanism for navigating that uncertainty, maintaining rational behavior even as problem complexity grows. I dubbed this as "🪒auto occam's razor" hierarchical model encodes uncertain beliefs and sampling navigates that uncertainty representation. together, they form consistent algorithm for probabilistic inference which behaves rationally compared to those violating consistency hence making predictably irrational decisions. (rational ai principle3)</p>

- --
RAW
example from home field - apply to get intuition
compute energy robustness 
(learning) inferring; 3d scence percepton, common sense data cleasng, automated data modelng (samplng over structure); choosng complexty model (number of parameter beng ) - complexity of model (not optmzng ftn but samplng)
SAMPILNG VS OPTIMZING; meaning of inferrng to (by construction ratonal)
percepton and navagon demo (GCP; google ; jax cpu mode; jax + cuda)
bayes occam's razor (conquene of probability theory; none of this would work f ths s not operative - depends on samplng; not the only reason to sample; norms of ratonalty from asymptoticity)
curve fitting with model selation 
parameter with outlier ()
< fixed hyperparameter
shared among instatiation
with flexible hyperparmeter - you have more flexibility partial trace filling in execution (output is full trace with weight = mc measure of )

trace, weight = query(program, args, observatons)
alpha =. args = prior

approximaiton to posterior (no obserafvtion = prior)

sgma would be higher (for those with may outlier, posteior of p would be higher and sigma)

approximate posterior samples

nferrng the # of parameter to explan the data (varying # of parmeters)

why unfiform = cover up possible cases

narrow prior 

🙋‍♀️even if you give uniform prior on the degree, is there incentive from code to prefer lower dmension? (shorter program doesn't help)

google bran (zelmany - 2014; make this with genjax and teachng notebook)

among the larger model space, the metric (distance between the ); best fit model

bayesian occam's razon; norms of probabilty

p(m|D) = p(D|m) * p(m), p(D|m) = integ dtheta p(D|theat, m) p(theta|m)

p(m) is constant - p(D|m) = marginal likelihood - joint probability ; randomly 

randomly selectly given data
-log2(p(D|m)): number of bts of supse at boserng D under model m

larger surprse for 

conservaton law

p(D|M) for vaying M (p = 2)

posterior gven the model class (from the quadratic; model s concentrated near the dat)

optmzaton doesn't tell prob.model is (unstable, arbitrary soluton)

typical set of sample=  

dicstionary order (sort all the gird order sell; see the smooth)

p(D|M) should be integrated to 1 for integrating on all D; 🙋‍♀️only visualize locally

p(D|m) small = less surprise = too complex

dop(d)

P of D given M, that key term determining p m, given D is highest for models whose complexity is a good match to the data, whereby , I mean something like how 

⭐️complexity: how falsifiable the model is relative to how well it fits the data for typical settings of the world

posterior inference (P(D|m)) over degree of polymonoimal (green plots; jointly green and blue; contrast with blue curvese)
it's local

expressiveness ; flattens (if you have model representive; scaling property; won't be used unless theiy are ned; trade; 🙋‍♀️you can choose your truncation factor to trade off the computational effects, with how much expressivsity You think you'll need) 

if we have good approximating engine (inference programming) we can 

typical set of saampling

from some distribution; 

⭐️can't sampling from the typical set be framed as an optimization on a measure space. But I'm saying in the space defined by the probability distribution, sampling versus sampling from the distribution, versus trying to optimize in that space. It is also true that computationally, you can define sampling methods in some cases, in or you can derive sampling methods using optimization objectives. But that's a very different optimization problem than finding a high probability value under the distribution. So another way to put as I'm talking about sampling versus optimizing from some distribution


diffculty of sampolng is easer (samplng s global - ); MC 

rationalty computationaly feasible; evaluating a problablity (findng the single most probable distribution)

efficient reducton: reducing samplng to optimzaton  on a noisy nstance

1. computing probability
2. optmizng MAP
3. sampoling

not nonconvex problem 

mixture model problems (EM scales much words than samplng )

easer vs faster
is samplng 

# Norms of rationalty 

probaility as a extenson of boolean algebra; 
consstent (several ways; all relevant evidences; ); belef function satsfyng ; numercal recalng

jaynes prbability of scence

make assumpton on model

dutch book theorem; gamblng games (ppl can cheat you)

🙋‍♀️dutch book - 1.evolutionary perspective (you mnght not want to get fooled) 2. doesn't consder computatnoal cost of belef update

posetror on concentrates near the ; f you world s wthng the hypothesis , the posterior concentrates to true data

whose predcton best approxmates  (concentrate; best ones you can hope to fnd)

 you concentrate on equivalently good wrong answers that are the best ones you could possibly hope to find. 
converste to best possble famly

quartocos loops (genearl  for shts properly l; bdd and low varance)

what if you have two Bayesians that have different priors, but they see the same data? Well, it turns out that as long as they agree on the sets of possible and impossible values, then again, in general, as they see more and more data, their posteriors will convert. 
So now again, obviously questions of rates and compute resources matter. 

regmes of ratonal ntelgence (compuaton model of when and how that breakes out); 

indespensible (send to vikash, andrew's paper.  )


exact vs approximate sampler - (runtime and memory ); rollng dce wth differnt dimension; provably optimal exact sampler and approximate sampler (h

Exact sampling (perfect sampling) produces samples that follow the true target distribution precisely. Every sample is guaranteed to come from the correct probability distribution.

Approximate sampling produces samples that are close to, but not exactly from, the target distribution. These methods typically converge to the true distribution as the number of iterations increases. Examples include Markov Chain Monte Carlo (MCMC) methods.

probabilitc and global s more ratonal )

meta learning (learng makes the next learning easier)
1. general game playing (woudl you expect meta learnng to work in general) - share primtive (how does that relate with infernce; inference algorithm can learn across game; those parameter mediate so that information flow from the game1 to game2; data to behavior; what are properties of the world that is constant or change)
2. embodied intellgence


| Module | Topic                                                | rational ai principle | how                                                       | contrast | example |
| ------ | ---------------------------------------------------- | --------------------- | --------------------------------------------------------- | -------- | ------- |
| 1      | Scaling behavior of intelligence vs machine learning | 📐shallow to deep     | explore broad prior with structured parallelism           |          |         |
| 2      | Perception and navigation                            | 👁️see flowing mass   | visualize probability dbn. through entire parameter space |          |         |
| 3      | Foundations of modeling and inference                | 🪒auto occam's razor  | sampling from hierarchical model                          |          |         |
| 4      | Automatic integration of probabilistic programs      |                       |                                                           |          |         |
| 5      | Neural network models of visual perception           |                       |                                                           |          |         |
| 6      | Learning probabilistic programs                      |                       |                                                           |          |         |
| 7      | Theory-of-mind via inference                         |                       |                                                           |          |         |
| 8      | Language model probabilistic programming             |                       |                                                           |          |         |
| 9      | Neurally mappable implementations                    |                       |                                                           |          |         |
| 10     | Research methods                                     |                       |                                                           |          |         |
| 11-12  | Research frontiers                                   |                       |                                                           |          |         |
| 13     | Project CHI                                          |                       |                                                           |          |         |



| Module | Topic                                                | Rational AI Principle | How                                                               | Contrast                                                                                                                             | Example                                                                                                                                                                                               | transcript                                     |
| ------ | ---------------------------------------------------- | --------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| 1      | Scaling behavior of intelligence vs machine learning | 📐Shallow to Deep     | Explore broad prior with structured parallelism                   | Traditional ML fixes model architecture and optimizes parameters; shallow-to-deep allows structure itself to adapt based on evidence | Time series analysis starting with broad model space (linear, periodic, change point) that captures COVID airline traffic drop, versus LSTM/transformer models that fail to adapt to dramatic changes | [[vikash seminar.txt]]                         |
| 2      | Perception and navigation                            | 👁️See Flowing Mass   | Visualize probability distribution through entire parameter space | Deep learning provides point estimates without uncertainty; flowing mass reveals full distribution of possibilities                  | Robot localization showing all possible positions when uncertain, versus Tesla autopilot that fails catastrophically when its single-point estimate is wrong                                          | [[vikash seminar - perception_navigation.txt]] |
| 3      | Foundations of modeling and inference                | 🪒Auto Occam's Razor  | Sampling from hierarchical model                                  | Explicit regularization requires manual tuning; sampling naturally favors typical solutions                                          | DSL program inference for time series automatically favoring simpler syntax trees until evidence justifies complexity, versus overfitted models that require manual regularization                    | [[vikash seminar modeling inference.txt]]      |
| 4      | Automatic integration of probabilistic programs      |                       |                                                                   |                                                                                                                                      |                                                                                                                                                                                                       |                                                |
| 5      | Neural network models of visual perception           |                       |                                                                   |                                                                                                                                      |                                                                                                                                                                                                       |                                                |
| 6      | Learning probabilistic programs                      |                       |                                                                   |                                                                                                                                      |                                                                                                                                                                                                       |                                                |
| 7      | Theory-of-mind via inference                         |                       |                                                                   |                                                                                                                                      |                                                                                                                                                                                                       |                                                |
| 8      | Language model probabilistic programming             |                       |                                                                   |                                                                                                                                      |                                                                                                                                                                                                       |                                                |
| 9      | Neurally mappable implementations                    |                       |                                                                   |                                                                                                                                      |                                                                                                                                                                                                       |                                                |
| 10     | Research methods                                     |                       |                                                                   |                                                                                                                                      |                                                                                                                                                                                                       |                                                |
| 11-12  | Research frontiers                                   |                       |                                                                   |                                                                                                                                      |                                                                                                                                                                                                       |                                                |
| 13     | Project CHI                                          |                       |                                                                   |                                                                                                                                      |                                                                                                                                                                                                       |                                                |

| Module | Topic                                                | Rational AI Principle | How                                                                                                                        | Contrast                                                                                                                             | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------ | ---------------------------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1      | Scaling behavior of intelligence vs machine learning | 📐Shallow to Deep     | Define broad model space with structured ignorance priors, allowing models to evolve incrementally as evidence accumulates | Traditional ML fixes model architecture and optimizes parameters; shallow-to-deep allows structure itself to adapt based on evidence | **Time-series forecasting with a dynamic DSL**. We specify a generative model (e.g. linear trend, seasonal/periodic components, change-point jumps) with latent hyperparameters for amplitudes, frequencies, etc. The system samples _which_ model components to include, plus their parameters, instead of committing to a single fixed architecture. Then, using particle-based sampling (e.g. SMC), it _automatically_ refines and prunes these structural choices as new observations arrive. In **airline-traffic demo**, this approach successfully adapts to the sudden COVID drop, while a transformer or LSTM—pre-trained on stationary patterns—fails to track the abrupt change. The code can be implemented in Gen/GenJAX by writing a short “kernel DSL” for time-series structure, assigning a broad prior over kernels, and applying sequential Monte Carlo so that the model _grows in complexity only if/when the data demand it_. |
| 2      | Perception and navigation                            | 👁️See Flowing Mass   | Visualize probability distribution through entire parameter space using particle-based methods with adaptive computation   | Deep learning provides point estimates without uncertainty; flowing mass reveals full distribution of possibilities                  | **2D Robot Localization with noisy sensors**. Gen/GenJAX _generative model_ of a robot’s motion (uncertain rotation & translation) and sensor (noisy distance readings to walls). Instead of a single “best guess,” it **maintains a _distribution_ of possible poses** using Sequential Monte Carlo. The “mass” of particles _flows_ from one area of the map to another when sensor data contradict the current pose. A single-point estimate (like Tesla’s autopilot) can fail catastrophically if, e.g., the map alignment is off by one room; but a particle-based inference method _automatically_ _rejuvenates_ proposals and corrects itself when local mismatches accumulate. The code is straightforward: define a pose+motion generative function, a sensor-likelihood function, then run “resample‐move” SMC so multiple pose hypotheses are re-weighted each step, bridging _uncertainty_ in real time.                                |
| 3      | Foundations of modeling and inference                | 🪒Auto Occam's Razor  | Sample from hierarchical models with latent hyperparameters rather than optimize fixed models                              | Explicit regularization requires manual tuning; sampling naturally favors typical solutions                                          | **Polynomial regression with outlier detection**. Assign a prior over both the degree of the polynomial and outlier/noise parameters; then use posterior _sampling_ to infer model complexity. A naive optimizer might pick a high-degree polynomial that overfits, whereas the Bayesian sampler automatically leans toward simpler polynomials unless evidence strongly demands complexity, thus embodying “Occam’s razor” without manually fiddling with penalty terms.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 4      | Automatic integration of probabilistic programs      |                       |                                                                                                                            |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 5      | Neural network models of visual perception           |                       |                                                                                                                            |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 6      | Learning probabilistic programs                      |                       |                                                                                                                            |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 7      | Theory-of-mind via inference                         |                       |                                                                                                                            |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 8      | Language model probabilistic programming             |                       |                                                                                                                            |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 9      | Neurally mappable implementations                    |                       |                                                                                                                            |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 10     | Research methods                                     |                       |                                                                                                                            |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 11-12  | Research frontiers                                   |                       |                                                                                                                            |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 13     | Project CHI                                          |                       |                                                                                                                            |                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

📐shallow to deep: structured ignorance priors enable robust inference by starting deliberately broad and refining incrementally as evidence accumulates. this approach maintains flexibility against unexpected cases while leveraging structure when appropriate, yielding systems that scale better than those with premature specificity.

👁️see flowing mass: probabilistic programming visualization reveals how probability distributes across hypothesis space rather than fixating on point estimates. this perceptual skill transforms inference from opaque guesswork to transparent reasoning, allowing rational uncertainty quantification that drives adaptive computation and robust decision-making.

🪒auto occam's razor: hierarchical model encodes uncertain beliefs and sampling navigates that uncertainty representation. together, they form consistent algorithm for probabilistic inference which behaves rationally compared to those violating consistency hence making predictably irrational decisions.



 marriage of hierarchical modeling and sampling-based inference to balance model complexity with data fit. 

📐shallow-to-deep approach provides the pathway for progressively refining models from uncertainty to specificity, while 🪒automatic Occam's razor through hierarchical sampling guides this journey by naturally favoring simpler explanations until evidence justifies added complexity.