#RB 
network application paper
 * Model search: Greedy graph search  
 * Model search: Projection prediction ([https://arxiv.org/abs/2010.06994](https://arxiv.org/abs/2010.06994))  
 * Model search: Genetic algorithms (on module selection vectors)  
 * Model search: Many-armed bandit. Metric (like ELPD) sampling time is the resources; Bayesian model of module contribution  
 * Model search: "Symbolic regression" (meaningfully different or not?)  
 * Sensitivity analysis: do neighbors of a model share its results?  
 * Edges (posterior in data space/"fit"): absolute (e.g. ELPD (requires likelihood augmentation)) or comparative (bayes factor, marginal likelihood)  
 * Edges (prior in data space): mutual SBC (requires generative model augmentation)  
 * Edges (posterior in data space): basic data stats  
 * Edges (posterior in parameter space): distribution distance (KL?); custom metrics (effect size)  
 * Edges (prior in parameter space): "difference between priors"  
 * Visualizations: Edges weights as distances, embed into 2D continuous space  
 * Visualizations: Scatter plots of models, e.g. complexity/p-loo vs. ELPD or estimated effect size  
 * Multiverse methods  
 * Stacking methods  
 * Module validation/effect isolation  
 * Counterfactual models as nodes  
 * Counterfactuals: estimated effect size as embedding dimension for visualization  
 * Stan module libraries  
 * Stan multi-model compilation  
 * Module code generation  
 * Module signatures ~ modeling assumptions (advanced module signature type system; Curry-Howard esque)  
  
I think the order I'd pursue these in might be:  
  
 1. Model search: Greedy graph search (pretty much done)  
 2. Sensitivity analysis: do neighbors of a model share its results?  
 3. Stacking methods  
 4. Model search: Many-armed bandit. Sampling time of the metric (like ELPD) is the resources; Bayesian model of module contribution  
 5. Model search: Projection prediction ([https://arxiv.org/abs/2010.06994](https://arxiv.org/abs/2010.06994))  
 6. Multiverse methods  
 7. Edges (posterior in data space/"fit"): absolute (e.g. ELPD (requires likelihood augmentation)) or comparative (bayes factor, marginal likelihood)  
 8. Edges (prior in data space): mutual SBC (requires generative model augmentation)  
 9. Visualizations: Scatter plots of models, e.g. complexity/p-loo vs. ELPD or estimated effect size  
 10. Visualizations: Edges weights as distances, embed into 2D continuous space