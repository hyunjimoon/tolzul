Topology starts with divergence i.e. $d(model_1, model_2)$.

## What 
is model divergence? It is categorized as:

| -       | y                             | $\theta$                                        |
| ------- | ----------------------------- | ----------------------------------------------- |
| preFit  | 1. prior predictive check     | 2. model distance, simulation-based calibration |
| postFit | 3. posterior predictive check |                                                 |


## How 
to compute model divergence? For each 1, 2, 3 above,

1: $d(y, \hat{y_1}), d(y, \hat{y_2})$
- prior predictive check

2: $d(module_1, module_2)$

- structure of parameter
- measurement model
- e.g. module structure which is similar to network architecture in graphcial neural network. They determine basis function space.

3: $d(\tilde{y_1}, \tilde{y_2})$
- posterior predictive check
- $\theta$-based distance: simulation-based distance between edges and vertices (marginalize out y)
- $y$-based distance: expected log pointwise predictive density (marginalize out theta)

The three category correspond to three types of criticism recommended [this](https://arxiv.org/pdf/2006.02985.pdf) workflow paper for disease transmission.

![[Pasted image 20220622054150.png|800]]

## Why
is model divergence needed? This forms model topology which makes "familes of model", "model network" more concrete.

Predictions $\tilde{y}$ depend heavily on the model structure (e.g. model 1~ 8 in Birthday problem) and based on this, we assume the existence of `module tree` whose divergence on this [hyperbolic topology](https://en.wikipedia.org/wiki/Hyperbolic_tree) can be the proxy for model divergence. Just as [decision tree is an universal approximator](https://dbertsim.mit.edu/pdfs/papers/2018-sobiesk-optimal-classification-and-regression-trees.pdf), module tree is expressive and forms large enough basis function space. Hence, this structure is eligible to measure model divergence.