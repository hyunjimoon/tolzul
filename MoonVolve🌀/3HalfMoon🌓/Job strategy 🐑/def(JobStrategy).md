## Demand
- satisfying job for everyone

## Decision
- External intervention in the parameter space (policy parameter e.g. task richness) level is possible (Yes / No).

## Draws
- hierarchical factor analysis model with 200 subgroups, 40 local + 60 global coefficient (`est_param`)
	- U3_specify_projection: 
		- the number of bookstore etc
	- U4_specify_regularize (by adding to `targe`): 
		- difference of latent variable and observed data is added to `target` according to `family` distirbution function (negative binomial)
		- parameter is added to `target` accroding to prior distribution (e.g. `lognormal_lpdf()` )

- middle size (around 5 stocks) generator
- bimodal parameter geometry and its mapping with tipping point boundary in phase space
Examples each by Tom, Hazhir, Jeorun, David is documented in [[tipping points and bimodality]]