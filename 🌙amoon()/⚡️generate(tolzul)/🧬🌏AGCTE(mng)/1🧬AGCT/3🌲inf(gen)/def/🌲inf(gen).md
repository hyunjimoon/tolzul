(tbc)
goal:
- view generator and estimator from joint function space of simulate and infer a.k.a discriminator
- to argue Hierarchical draws2data causes data2draw uncertainty 

- find data with symmetry, hierarchy, by time and space based on [[daily_diary]] , [[forming_data_agency]]

#### Recovery quality under uncertainty
parameter retrieval quality (RQ) is a measure of model trustability defined with sbc metric

##### syntax: 
- numerically as sbc distance from uniformity metric, predictive quantities    
- visually as no divergence, pair plot simulate the model with some samples from the posterior and compare them against the data. This gives me a visual check of a "good fit".Pair Plot to evaluate the shape of the joint posterior distribution. Add correlations for more information. Lots of correlations indicate a difficult parameter space. Trace plots. For marginal distributions, I found it useful to overlap prior & posterior histograms. This plot tells how much information we gained from the inference process for a particular parameter.

##### semantic:

-   [Effect of process noise and hierarchy measured by parameter retrieval quality (RQ)](https://github.com/Data4DM/BayesSD/discussions/118)

#### Draws2data, data2draws uncertainty and noise

-   process and measurement noise during draws2data and data2draws

![](https://lh5.googleusercontent.com/igNWrpYtlFJWw1goCpC4oCvTm5wNTq8WeXTjnpT_zaNDhxOsOBlnBdjoerQvagE7i-B4G9rzjp5Mfk7TkfqPOKv-s4-uXVhyDGutntp8XPj-ibVpRTYghDujZaN8_aGD8d_LlHEqvaI2-2rdeeRab5AUl5TVX9PV38OnXgv_mFs0s4sANSGDLfu8wChNAw)

  

soft and hard constraint

-   how to decide giving prior or range
    
-   how user-defined constraints are encoded under the hood 
    

-   given the first two moments (mean and sd) PERT prior
    
-   given only the first moment (mean) -> normal( mean, .1 of mean)
    

#### Role of hierarchy 

-   experiment tool for heterogeneity (homogeneous treatment of heterogeneous unit VS heterogeneous treatment of homogeneous unit)
-   a.k.a process noise

We have orange (e.g. shorter delay, functional, make to stock, explicit, opt-in, reward function, efficiency, revenue of supply chain, strong ) and purple (e.g. longer delay, innovative, make to order, implicit, opt-out, satisfaction, effectiveness, innovation yes or no) types of test functions.

Detailed classification can be found in table from [[amoon(world)/jungle🌳/comp(mng(bea))/_def(comp(mng(bea)))/off_def(bea)|off_def(bea)]]. This is closely connected to _strong calibration_ which corresponds to passing SBC for every measurable functions (purple) and _weak calibration_ which corresponds to having a correct data-averaged posterior (orange) as introduced in [[Modrak22_SBCTest.pdf]] .

- [[table(inf(gen))]]
outer join instruction
	- exhausively cover: argue three template dynamic models from the system dynamics domain (two stock negative loop oscillators (prey-predator), growth generated by contacts between two groups (SIR, SEIR), and stock management structure (inventory) models)can be building blocks of sd models
	- concept that  [reflections on time step (as one of precision hyperparameter)](https://github.com/Data4DM/BayesSD/discussions?discussions_q=label%3A%223+tuning+time+step%22) 


- [[2_workflow]]

---
## What

Verification, Estimation on bounded range with ϵ- optimality/feasibility (based on weak optimization = weak separation)

Among inductive bias, this address [#statistical_error](https://publish.obsidian.md/#statistical_error), related to the hypothesis function expressed with given number of samples.

## How

## Why

#### Introducing CAT, reliability verification probablistic programming language

[#operator](https://publish.obsidian.md/#operator), [#hiearchize](https://publish.obsidian.md/#hiearchize) [#regression](https://publish.obsidian.md/#regression)

-   what: computationally efficient reliability verification of hierarchical model inference
    
-   how: operator-based probabilistic programming language PPL [[Computer-PPL History and Trend]]
    
-   why: simulation is a weak solution of equations which generated reality and "what" above is needed to verify the closeness of simulation and reality. With "online" flavor added to simulation for digital twins as [this](https://www.ibm.com/topics/what-is-a-digital-twin) IBM report shows, computational efficiency is the key for CAT. By weak solution, I mean just as SDE's weak solution is constructed on a new setting (probability space, sigma algebra, measure, and filtration) and weakly equal to the strong solution, twin is a newly constructed object that is weakly equal to reality. With this view, CAT's main job in catching RAT (:= generative regression modeling languages) becomes searching for counterexamples i.e. a member of determining class ϕ breaching the (in)equality. Digitizing this falsifying logic is its aim. An example is finding an counterexample for inequality using a increasing function δ1∈ϕ (determining class for ≥st, and n = 2. 1n∑l=1nXi≥st1n+1∑i=1n+1Xi (further check needed!)
    

Consistency Ability Test, Consistency Analyzing Test, Calibrate and Test are current candidates for the name CAT. Filtering models that are [Accurate, yet inconsistent](https://arxiv.org/pdf/2108.06665.pdf) is CAT's goal based on their potential danger.

List of verification-type approaches are:

-   [Abstract Interpretation in a Nutshell](https://www.di.ens.fr/~cousot/AI/IntroAbsInt.html)
-   [An importance sampling approach for reliable and efficient inference in Bayesian ordinary differential equation models](https://arxiv.org/pdf/2205.09059.pdf)
    
    > "validate the efficiency and reliability of our workflow in experiments using simulated and real data, and different ODE solvers"
    
-   [Detecting Model Misspecification in Amortized Bayesian Inference with Neural Networks](https://arxiv.org/pdf/2112.08866.pd)