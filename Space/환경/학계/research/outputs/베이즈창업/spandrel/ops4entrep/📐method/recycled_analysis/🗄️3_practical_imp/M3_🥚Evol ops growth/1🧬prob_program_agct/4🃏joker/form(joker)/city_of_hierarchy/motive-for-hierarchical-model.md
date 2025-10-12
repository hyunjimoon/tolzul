---
이름: Hierarchical model and priors
출생: 2021-02-18
언어교환:
  - bayesian
---

Justifications and recommendations

complete pooling

- discarding a variance component or setting the variance to zero understates the uncertainty
- standard errors for coefﬁcients of covariates that vary between groups will be too low

no pooling

- ﬁt a regression with indicators for groups (a ﬁxed-effects model)
- overcorrect for group effects (it is mathematically equivalent to a mixed-effects model with variance set to inﬁnity)
- does not allow predictions for new groups

Monte carlo estimation

- estimating equations involve the empirical version of the infinite-dimensional parameter in the semiparametric model (Jin15, MCVarSmoothing)

Prior choice

- log-normal and inverse-gamma can only be used when there is real prior information to guide the choices of their two parameters; prevents nonzero variances (Chung et al., 2013)
- multiple priors could be used during the sampling similar to mixing RK45 and BDF ODE integrators (natural interpretation of a posterior mode is as a starting point for full Bayes inference, in which priors are speciﬁed for all parameters in the model and Metropolis or Gibbs jumping is used to capture uncertainty in the coefﬁcients and the variance parameters (Dorie, Liu, & Gelman, 2013). For reasons discussed above, it can make sense to switch to a different class of priors when moving to full Bayes: once modal estimation is abandoned, there is no general reason to work with priors that go to zero at the boundary.)

![](images/image-1024x828.png)

- correspondence between prior and penalty  
    1\. exponential of penalty = prior (eg uniform prior = marginal logpost with varying intercept integrated out)  
    2\. log-gamma(α,λ) penalty on σ θ = log gamma(2α − 1,λ) penalty on σ θ

References

A NONDEGENERATE PENALIZED LIKELIHOOD ESTIMATOR FOR VARIANCE PARAMETERS IN MULTILEVEL MODELS provides insightful relation between prior and penalty as well as their recommendation and connections.
