a.k.a. Mangage

What: System-Bayes-Couple
How: Simulation-based Calibration 

## object of SBC
- prior:  `demand_prior` (policy), `relational_prior` (architecture), `variational_prior`(model parameter)
- likelihood: 
- posterior_approximator: [[5 Merging Algorithm Tribes]]

 ## Three steps of replacing epistemic with aleatoric uncertainty system construction

How epistemic uncertainty transforms to aleatoric can be seen as the following:

| step | <span style="color:green">operator</span> | <span style="color:red">operand</span> | result | e.g.                               | job    | 
| ---- | ----------------------------------------- | -------------------------------------- | --------------------------------------- | ---------------------------------- | --- |
|      |                                           |                                        | reality                                 | sun                                |     |
| 1    | 👁 sense                               | reality                                | perceived reality                       | 🔴🟠 1e^6km, 2e^30kg, G2V Star                   | fact based on sensor    |
| 2    | 🧠 hierarchize                          | perceived reality                      | scientific model                    | ⏳🌲 time-spatial process i.e. tree (generating process) of sun  | represent with math-stat model    |
| 3    | 🏭 program                              | scientific model                       | simulation   | 🌅                                 | computer-engineer, implement then verify   |


Experiments can be used to weakly support or strongly negate (i.e.falsifying theory1 (theory1 -> theory2).


| -           | strong yes | weak (yes, no) | strong no | type                     | _             |     |
| ----------- | ---------- | -------------- | --------- | ------------------------ | ------------- | --- |
| theory      | o          | x              | o         | induction                |               |     |
| experiment  |            | o              |           | deduction, falsification | finite sample |     |
| computation |            |                |           | deduction                |               |     |
|             |            |                |           |                          |               |     |

deductively connect weak -> strong [yes, no]
experiment is proving by deduction

experiment (saying "strong yes is wrong", can't)
computation is (saying "weak yes is right")

Based on the [[Three Axioms]]:

Three modelers each go through 1, 2, 3 with sense (), hierarchize (), program().
- 1: **sense y**.  `Eval()`
- 2: **reasons generating structure** i.e. data generating process
- 3: **guess and check weak sol**. They combine 2's result with the solution of inverse problem (Bayesian deconvolution) i.e. `Decide()`: $Y \times Y \rightarrow 0 or 1$

Statistical error is the first step (as we perceive the world) and 
We structure how a simulation will be constructed from testing our assumptions against reality. The simulation is now used to rigorously specify the "coin", so that we have complete information on how our aleatoric device is constructed. The final step is to translate our abstract, mathematical aleatoric device into a probabilistic program, on which computation is performed.


Transforming intractable epistemic uncertainty into tractable aleatoric uncertainty through workflow.  `Operator(operand)`

We use tools of aleatoric uncertainty to model epistemic uncertainty. For example, a logistic regression is an aleatory system to model events such as COVID infections. Or an event which its rate is unknown may be modeled through a Poisson-Gamma model.

Aleatoric probabilistic models are used to represent epistemic uncertainty about an event.

Unless the probabilistic model is perfectly, perfectly tractable, how can we guarantee that "this model and its computation suite correctly and faithfully computes the aleatoric uncertainty of interest"?

Diagnostic tools, such as SBC, an aleatoric "model" of epistemic uncertainty within model computation. [[_ref/QnA]]


## Introduction
We write many models that represent various portions of reality. What is our goal with writing such models? How effective are such models in describing systems of interest? Very much often reality is laced with uncertainty, acting as a veil that hinders our ability to observe the direct mechanisms of reality. In this post, we will explore what creating a model means, and how we create one.

## Coin
A model, by definition, is some represention of a system that helps to know, understand, or simulate underlying mechanisms in 
the system. In other words, we aim to reduce the uncertainty that's present from the lack of knowledge of a system. This uncertainty is called *epistemic uncertainty*. 

Think of a coinflip. Even with the most sophisticated model of the laws of physics, we can't predict what the outcome will be with complete certainty. This is epistemic uncertainty.

Imagine we are flipping this coin many times, resulting in a stream of outcomes: `0, 1, 1, 0, 1, 0, 0, ...`. We don't know what the next outcome will be, but after observing the data, we realize that ptentially there's a 50-50 chance for either side. How can we be so sure? We can construct a model of the coin to figure out. For example, a bernoulli model with an unknown parameter $p$. As we observe more and more outcomes of the result, we can be more certain in identifying whether the coin will be biased or not.

Strange. We can't pedict individual outcomes of the coin, but we were able to come up with a model that tries to explain the outcome generating process. The uncertainty that was present in the coin itself, was relocated into uncertainty that's now present in the value of a parameter. The latter form of uncertainty, uncertainty that's present about some incomplete knowledge about a well-defined model(process), is called *aleatoric uncertainty*. And from the coin example, this uncertainty can be overcome with sufficient amount data.

Like a coin, there are two sides of uncertainty. Epistemic uncertainty is uncertainty that can't be overcome, bar a god. To create a model is to create a smaller, well-understood replica that correctly "moves" the epistemic uncertainty to aleatoric uncertainty about parameters(information) in the replica.

## Example
Suppose you're in charge of managing logistics of goods. Your job is to identify how much goods needs to be moved every day, and supplying sufficient transportation so that the entire logistic chain doesn't suffer from a halt. You're not a god, so there's no way to exactly identify the process that generates the amount of goods per day.

Your first job is to first identify what the generating process is, and other factors involved. For example, you might know that some factors such as weather or the number of orders handled by a nearby Amazon warehouse, etc. might have an effect on the outcome. Using this information you may come up with a model, say a poisson regression, that may or may not explain the generating process. Remember that epistemic uncertainty means you can't be certain about it.

Once you have a model in mind, you begin to specify the details so that your model is well-understood. You choose reasonable priors and a likelihood that encapsulates your assumptions a bout the generating process. This is the "aleatoric device". Now the epistemic uncertainty regarding how the number of goods are generated is now translated into aleatoric uncertainty about estimating parameters in your model.

But the model can't run by itself. You need a way to realize your model into some computable form, a program. And as such, you need to use a probabilistic programming language such as Stan, that can perform inference for your model. Only then is reducing the aleatoric uncertainty possible.

Computation has completed and you know have more than enough confidene and certainty about the parameters. Does this mean you now understand the goods-generating process? The answer is "it depends". If the model you have devised, that links epistemic uncertainty to aleatoric uncertainty is reasonable enough and due to keen observations of reality was sufficient in containing some epistemic uncertainty, then the reduced aleatoric uncertainty will also contribute in reducing some epistemic uncertainty. However, the model being a bad analogy of the generating process means you only reduced aleatoric uncertainty irrelevant to the generating process.

Defining a model that captures sufficient portions of epistemic uncertainty is the first step of the entire modeling process, and arguably the most fundamental and crucial step. As with the phrase "a chain is as strong as its weakest link", even with perfect computation tools and data that eliminates aleatoric uncertainty, a model that cannot explain epistemic uncertainty results in faluty conclusions.

## Probabilistic Programs

Segment the big subject of PPLs into: 
- a model descriptive language (PL)
- inference algorithm(s) (computation)

From Ryan's definition of aleatoric uncertainty:

> Aleatoric uncertainty is incomplete knowledge of **well-defined states of a carefully constructed** gambling device

`PL assures this property when we work with realized gambling devices.`

A program is concrete - there are no uncertainties involved in what a program represents. Coinflips can't be involved in the specification of programs.

Maybe this is an example of reducing a coinflip? Because we have complete certainty about what model a program represents.

## samples
2,000 samples are drawn with MCMC algorithm but the first 1,000 and the last 1,000 have different meanings: the first is learning process while the second is the answer itself.

### E to A journey: learning
In the journey of replacing `E` with `A`, several "plausible" pairs of (prior, likelihood, algorithm) is generated. 

### E : target distribution
---

Ref: #RG 's writings 1.[What is statistics (statistical analogy)](https://rgiordan.github.io/philosophy/2021/08/22/what_is_statistics.html)  2.[Gambling device that build statistics](https://rgiordan.github.io/philosophy/2021/08/22/what_is_statistics.html)
