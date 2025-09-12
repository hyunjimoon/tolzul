## Introduction
We write many models that represent various portions of reality. What is our goal with writing such models? How effective are such models in describing systems of interest? Very much often reality is laced with uncertainty, acting as a veil that hinders our ability to observe the direct mechanisms of reality. In this post, we will explore what creating a model means, and how we create one.

## Coin

A model, by definition, is some represention of a system that helps to know, understand, or simulate underlying mechanisms in 
the system. In other words, we aim to reduce the uncertainty that's present from the lack of knowledge of a system. This uncertainty is called *epistemic uncertainty*. 

Think of a coinflip. Even with the most sophisticated model of the laws of physics, we can't predict what the outcome will be with complete certainty. This is epistemic uncertainty.

Imagine we are flipping this coin many times, resulting in a stream of outcomes: `0, 1, 1, 0, 1, 0, 0, ...`. We don't know what the next outcome will be, but after observing the data, we realize that ptentially there's a 50-50 chance for either side. How can we be so sure? We can construct a model of the coin to figure out. For example, a bernoulli model with an unknown parameter $p$. As we observe more and more outcomes of the result, we can be more certain in identifying whether the coin will be biased or not.
