#mds #metric, #diagnostic, #summary

1.  How to sample well from a given space. Metric.
2.  How to know we sampled well. Diagnostic. 
3.  How to present the sample well. Summary.

## Metric

Space metric
change gradient and hessian (laplace operator)
Three spaces with different intrinsic geometry (S^n, E^n, H^n)

**

Space metric
-   change gradient and hessian (laplace operator)
Three spaces with different intrinsic geometry (S^n, E^n, [H^n](https://docs.google.com/presentation/d/1cvg6cSSEBIiQ4F3txFDy3Su3fTHpfhgMvTw_8VtpZQA/edit?usp=sharing))  
**



## Diagnostic

1.  Diagnose models with/without asymptotic bias or stochastic/deterministic approximation (eg. embedded laplace, variational inference) 

2.  Simulation-based calibration: comparing the prior samples with data-averaged posterior samples. github repo [issues](https://github.com/hyunjimoon/SBC/issues)

3.  Pareto-smoothing Importance sampling: fit generalized-pareto to likelihood ratios (q/p) and replace the values over threshold (biggest M ratios) for robustness

## Summary

-   Dynamic BayesFactor threshold that maximizes simulated utility [paper](https://arxiv.org/pdf/2103.08744.pdf), [slide](https://docs.google.com/presentation/d/1OxtIcKztjoDLnAxTN8-UPcd3Ja8qpzdsnidcuW1Si5Y/edit?usp=sharing)
    
-   [shortest posterior interval](https://discourse.mc-stan.org/t/shortest-posterior-intervals/16281) problem
    
-   Visualization in Bayesian workflow [paper](https://arxiv.org/abs/1709.01449)
![](Pasted%20image%2020210718091544.png)

Uniformity graphical test for fit and multiple sample comparison [paper](https://arxiv.org/abs/2103.10522)                                                     