---
title: "Approximate Bayesian Inference"
date: "2020-11-15"
categories: 
  - "bayesian"
  - "blog"
  - "optimization"
  - "stan"
---

Computing the posterior

![](images/image-12-1024x64.png)

is our target. Expectation to get the marginal as we might not know the exact data distribution. Even if we do, computation is burdensome in high dimension. Approximations around the equation 1 have been attempted in terms of modeling and computation.

1\. Modeling  

![](images/image-10-1024x72.png)

By replacing the negative loglik with Taylor loss function, we could get a classifier without having to know full data distribution. Example is PAC-Bayes.

2\. Computation

2.1 non exact monte carlo methods

Metropolis-Hastings algorithm that compute the likelihood ratio. It is known that , if each likelihood is computed by an unbiased Monte Carlo estimator, the algorithm remains exact. Approximate Bayesian Computation could be applied to models where likelihood is too complex to be computed, but sampling is relatively easy.

2.2 asymptotic approximation

Gaussian, or Laplace, approximation of the posterior centered on MLE and covariance as inverse of Fisher information. Bernstein-von Mises theorem justifies the approximation for parametric models under certain regularity conditions; but there are some extensions to non-parametric as well.

2.3 approximation via optimization

![](images/image-9-1024x120.png)

Best approximation of $latex \\pi (- | x )$, or$latex \\tilde{\\pi}(- \\mid x)$ among the set of prespecified probability distributions Q. Different metric that measures the distribution distance include Kullback–Leibler divergence as in equation 3 and 4. Computation is tractable when using KLD. To extend the concept, we could either replace KL with other divergence measures or optimize different objection function under KLD.

For the first approach, non-KLD measures could be found in divergence measures in information geometry and include Renyi, chisquared divergence. Wasserstein distance is another choice whose theoretical guarantees has been provided by [Huggins et al (2020)](https://www.hyunjimoon.com/blog/validated-variational-inference-via-practical-posterior-error-bounds/).

The second measures KL distance from the posterior to approximate distribution instead of the other way around. The concept has further extension such as power EP, $latex \\alpha$-divergences.

To solve the optimization problems, stochastic optimization methods including conjugate gradient, coordinate-wise optimization, gradient and stochastic gradient, natural gradient methods have been applied. Convexity and smoothness, theoretical justification for algorithm are analyzed ([Domke, 2019](https://www.hyunjimoon.com/blog/provable-smoothness-guarantees-for-black-box-variational-inference/)). for convergence of algorithm intruwhich aid of the minimization problem.

* * *

Related ways for Stan to achieve efficiency with modeling, computation approximation and its diagnosis.  

1\. Modeling  
\- reparameterization: model implementation can achieve the same performance as playing around with the algorithm. Betancourt's [post](https://discourse.mc-stan.org/t/riemann-manifold-hmc-in-stan/19466/5?u=hyunji.moon) and [Incomplete Reparameterizations and Equivalent Metrics paper](https://arxiv.org/abs/1910.09407). Simple tricks on modeling the difference instead of the cumulated for HMM could be another example.

2\. Computation  
\- brute force computation: Multiprocessing, parallel computing (within-chain paralleization), precomputing X^tX, faster adaptation, improved mass matrix  
\- enhance initial point quality with theoretical support (e.g. convex optimization)  
\- approximate computation in each iteration: laplace, gmo, advi, ep \[note\]to validate bayesian approximation computation, accuracy (compare with full HMC, simulation based calibration), asymptotic results (convergence) is needed. I assume [PAC-Bayes](https://bguedj.github.io/icml2019/material/main.pdf) (Probably Approximately Correct) is related to this. \[/note\]I would address validation in another post.
