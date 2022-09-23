
Vignette [[self_calib(dap).pdf]] includes:
-   plots that compare HMC (red) vs laplace approximation (blue) (what Andrew called weather map)
-   definition and illustration of metric what I defined as `computational bias and sd` which can have mathematical background using pythagorean (bias-variance) decomposition
-   tweak application on binomial and eight school model (the latter aiming for joint calibration)

Paper draft exists which includes:

-   definition of SBC objective function `SBC_obj`
-   attempts to prove the convergence of its update based on convexity

Pull request documentation which includes  

-   code implementation (including Gaussian mixture) within SBC package
-   plot code for  `SBC_obj` geometry where we discussed can be benefitted from kernel approximation with grid-based computation of `SBC_obj`,