participants: Hazhir, Jason, Angie

## 0607
maf cycle : lead time

수요발생되면 백록으로 들어감

show all 6, analytic 

X is not always there; 
inventory, demand, shipment
pink : ,mean, var, corr
y: shipment, inventory

use pink noise delivery, 


Decision
- Is it a correct understanding you wish to (first) focus on the chp.1 of Analytic method textbook?
- 
- You have went to the level of decision; were you able to find the reviewer?
## 0606
- bimodal in 07 paper is from purely theoretical
- empirical + many firms. wish to pool datas
- policy prior will loose the reviewer and readers

### leadtime is not random variable by convention
details in [[👁🧠🌲🏭 Digital Twin/deConv(Digital Twin)/🏭 Generator/eg(Generator)/Forrestor meets Bayes/Matching SD-Bayes/Process noise and Feature noise]]

###  estimation helps policy design
![[Pasted image 20220706033653.png]]
- given the shipping, inventory, demand data, we estimate parameters 
- 879 students will select the model, differentiate which to put as variable, and which to estimate (which process, measurement noise)
- read covid paper, estimation for chp.1, 
- there are sometimes choices of policy (vensim + python)
- modularizing demand forecast - put outside python ok!
- 
CMIN, IMAX is a strategy (includes exogenout)
decision rule is 
### difference btw policy, strategy, decision rule
- policy: e.g. order the difference btw (SS, current)
- strategy (function): "N" days of (SS(N), current) 
	- control theory, exogeneous (not endog.to dynamics of design; existence of free parameter = performance, task richness), 
- decision rule: 
	- heuristic, actor transforms the  endogenous (all dictated)

## 06.21
todo: 
- Angie: 
	- confirm autodiff for implicit function and preferable its implementation in Stan: [Efficient Automatic Differentiation of Implicit Functions paper](https://arxiv.org/pdf/2112.14217.pdf).
	- getting advice from Jim on his choice for [`SDR_Bayes`](https://github.com/jandraor/SDR_Bayes) which seems to be neither 1 or 2 but somewher in between. For "hierarchical bayesian estimation approaches into SD modeling", I believe his choice to be optimal from its notorious posterior geometry which necessitates both reparamterization (e.g. parameter transformation) and sampler diagnostics (e.g. pair/trace plots + predictive checks + SBC).
	- prior (below)
- Jason: 
	- construct synthetic data and parameter estimation pipeline. 
	-  (Jason, if you mail me your goal + summary, I will be happy to add!).
	
### Prior distribution for $\sigma$
Currently, penalty regarding prior (PriorErrs) is $\frac{1}{2}(\frac{ActiveAve[Priors]-RegionalInputs[Priors,Sims]}{AbsStd[Priors]*StdScale})^2$  where 
- ActiveAve: `InputAve[Priors]*(1-SW EndoAve)+SW EndoAve*CalcAve[Priors]`


- AbsStd[Priors]: `30000, 0.5, 50000, 0.3, 3, 0.05, 3, 2, 0.5, 500, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 1, 0.05, 10, 0.01, 0.01, 0.01, 0.01, 0.01`
- StdScale: `1`
### Explore three alternatives 
R/Matlab may substitute Python and PyStan/PyMc may substitute RStan. If full Bayesian on hierarchical ODE is the goal, I carefully suggest 1-2 mix. This is what Jim did using [`SDR_Bayes`](https://github.com/jandraor/SDR_Bayes)  which translate vensim `model.xmile`, list of DE equation, to `model.stan` i.e. Stan model block (data, parameter, model).

1) Conducting simulations in a general programming language
pros: 
    - flexible control
    - easier to implement prior and synthetic data 

cons: 
    -  a) for computationally intensive project, compiled Vensim is relatively efficient (C++ engine)
    -  b) some Vensim functions (e.g. Find Zero and Allocate By Priority) doesn't have Python translation
    -  c) extra cost to find certified estimating engies (e.g. Kalman filtering, MCMC) 
	- e.g. [Andrade and Duggin 2021](https://onlinelibrary.wiley.com/doi/full/10.1002/sdr.1693)
2) Connecting Vensim with a general programming language in a dynamic fashion, so that Vensim is controlled with the programming language
    - flexible control
    - fast speed and direct access to Vensim’s capabilities 
    - lower learning cost and than 1)
    -  
<iframe title="vimeo-player" src="https://player.vimeo.com/video/206297867?h=1d77447143" width="640" height="360" frameborder="0" allowfullscreen></iframe> 

3) Connecting Vensim with a general programming language in a static fashion using Vensim’s command scripts.
- pros: easiest to implement with reasonable flexibility
- cons: unknown quailty of parameter estimates without diagnostics. Diagnostic includes which summarizes parameter's state without diagnostics as plots (trace, pair, predictive-retrodictive on parameter and observation level) or metrics (potential reduction factor $\hat{R}$, [Pareto-$\hat{k}$](https://avehtari.github.io/modelselection/CV-FAQ.html), effective sample size ESS)




## 06.13
- Synthetic data generation


## 06.06


## 06.01
- Good job model overview (model, control panel, kalman, metric, optimParam)
- payoff function which uses computes likelihood with the following assumption:
    - normal distrituion noise
    - no prcess noise
![[Pasted image 20220622041152.png]]