
The purpose of this writing is to introduce the theory and application for the title. This is based on the discussion with my advisors Garud Iyengar and Andrew Gelman. Also, comments from SBC inventor/enthusiast,  Aki Vehtari, Bob Carpenter, Michael Betancourt, Daniel Simpson were a great help whom I wish to collaborate further to contribute to Bayesian workflow and Stan.

## Example of workfield is as follows:

1. Given a DS operator and initial prior $\mu_0|t_o$, use second MCMC to get the first self-consistent set

> Predictive check: Apply DS operator to self-consistent set which would give ${t_1,..,t_b}$. Compare this with known p(t). If $d(p(t),{t_1,..,t_N}) > t$ proceed:

2. Given $\mu_0$ and $p(\theta'|\theta)$, update DS operator as follows (not limited to):
-- sampling density (add predictor, poisson to NB likelihood)
-- posterior density (MCMC to ADVI or Laplace)
-- hyperparameter (adapt metric or leapfrog step)
- information bottleneck iteration: 

3. Given DS operator, update $(\mu, t)$
1 ) update $(\mu_0, y) \rightarrow  (\mu_1, t_1)$: heuristic or apply IBT with $(X,T,Y) \leftarrow (\theta, t, \theta)$ for most efficient encoding (dimension reduction from $y$ to $t_1$ is expected)
2 ) update ($\mu_0, t_1) \rightarrow  (\mu_1, t_1)$: SBC iteration


Summary:

1. SBC Markov chain convergence
claim) given a density and approximate computation on $p(t|\theta), p'(\theta|t)$, iterately updating $p(\theta'|\theta), p(\theta)$ would reach an stationary distribution
 
 - convergence for 2 is decided by its necessity condition, [symmetry](https://hackmd.io/b4vPQgRORPmjv1ZU57CRig?both#Experiment) of $p(\theta, \theta')$. 
 - resulting $p(\theta)$ is interpretated as a region to use safely use the model+algorithm (density+sampler), namely self-consistent region (SCR).
 - instead of pointwise validity check, suggest the valid boundary for a given model+algorithm pair.    "prior variability" "no gurantee" problem , but there are no guarantees that these decisions will achieve any desired performance for any possible observation
 - OCR is included in SCR.
 - and posteriordb had a problem of having suggesting a best 
iterate two steps until we get $\theta_{1..N}$ from $\Theta_k$ s.t. $t|\theta \sim t$
1) given $p(t|\theta), p(\theta|t)$, update $p(\theta'|\theta), p(\theta)$ until convergence
2) given $p(\theta'|\theta), p(\theta)$ update $p(t|\theta), p(\theta|t)$ until convergence
- we want $p(t|\theta)$ to be $p(t)$. modeler selects model+algorithm and SBC iteration brings to the best prior and is suggested by Information bottelneck [paper](https://arxiv.org/abs/physics/0004057) section 3.3, 2 is EM pair of 1.
- convergence for 2 is decided by its necessity condition, [symmetry](https://hackmd.io/b4vPQgRORPmjv1ZU57CRig?both#Experiment) of $p(\theta, \theta')$. 
- t is a random variable of interest, eg.variance of the optimal decision when robustness is required
- $p(t)$ is given, which highlights the need to encode the data in the form of your quantity of interest

Motivation
1. Optimal exploration of model+algorithm space.
Which model + algorithm (density + sampler) to use is an online decision problem. However, this update from one pair of model + algorithm to the next is rather random, lacking guideline except for a few heuristic advise such as folk theorem of statistical computing, simple to complex, or fail fast. Geometric interpretation on probability measure space led to concepts as information geometry, optimal transport, and Timeseries filter that boost the exploration efficiency. Likewise systemic search is needed for exploratory data analysis and mathematical formulation of this sequential update in model+algorithm space would be the starting point. My writing [Structure-based Transport](https://www.hyunjimoon.com/blog/structure-based-transport-how-bayes-meets-geometry/) explains this further. The name work'flow' pleas for the quest for field.

2. Modeler assigns, 
2.  Connection to information bottle neck theory 
- Higher level: After some point of your exploration, consistent decisional results are expected:
![](https://i.imgur.com/4aPmi3u.png)
Information bottle neck theory aims to find the optimal encoding of X that balances the efficiency and representability of our quantity of interest, Y. Think of X, T, Y as data, model+algorithm, decision; this would guide us to a reasonable model+algorithm. My writing [gradient descent to outcome consistent region](https://www.hyunjimoon.com/blog/structure-based-transport-how-bayes-meets-geometry/#outcome-consistent%20model%20region%20gradient%20descent) suggests another approach.

 ![](https://i.imgur.com/X1Acqfb.png)

- Lower level: EM update of DS operator and joint model space measure under self-consistenty constraint:
$p(t)= \Sigma_{\theta} p(\theta)p(t|\theta)$
$p(\theta|t)= \Sigma_{\theta'|\theta} p(\theta'|t)$

## Symmetry of $p(\theta, \theta')$
Using the SBC assumption $p(\theta) = p(\theta')$ which states perfect generate-inference steps would lead to same distribution for prior and posterior samples, the following holds.
$$
\begin{array}{l}
p\left(\theta^{\prime}, \theta\right) \\
=p(\theta) \int \mathrm{d} y p\left(\theta^{\prime} \mid y\right) p(y \mid \theta) \\
=p\left(\theta^{\prime}\right) \int \mathrm{d} y p\left(\theta^{\prime} \mid y\right) p(y \mid \theta) \\
=p\left(\theta, \theta^{\prime}\right)
\end{array}
$$
Conditional distribution $\theta_{n+1}|\theta_{n}$ specifies transition probabilities of a Markov chain. The symmetry leads to p($\theta_{n+1}|\theta_{n}$)


- Connection with stationary or reversible Markov chain
When would the repeated $p(\theta), p(\theta'|\theta)$ update given $p(\theta|t), p(t|\theta)$ along with symmetry inspection guarantee a convergence, ie stationary distrubtion? Update of $\theta$ could be described as a discrete-time Markov chain on a compact set $\Theta$ with its transition probability defined from the generate-inference process: $y_{n} \sim p\left(y \mid \theta_{n}\right), \theta_{n+1} \sim \alpha\left(\theta \mid y_{n}\right)$ 
Inference step with Markov kernel, ie.$p(\theta, \theta')=\left(\int_{y} \alpha(\theta' \mid y) p(y \mid \theta) d y\right)$ defines a probability density for all $\theta$ which guarantees the existence of invariant measure and hopefully the fixed point. Between stationary and reversible measure, 
$$\sum_{\theta} \mu(\theta) p(\theta, \theta')=\mu(\theta')\\
\mu(\theta) p(\theta, \theta')=\mu(\theta') p(\theta', \theta) \quad \text { for all } \theta, \theta'
$$
The first 
we would know th which can be done using results in general theory of Markov chains. $p(\theta',\theta) = p(\theta|\theta')$ would $p(\theta')$

![](https://i.imgur.com/I4reWsp.png)
- Setwise instead of pointwise inspection is needed; which rank comparison aims for, but I used variance comparison for the experiment.
## Modeler assigns then DS operator updates: EM algorithm in exploratory data analysis
Two steps of Expectation-Maximization algorithm have another name: assignement-update. Modeler at n-step _assign_ prior to model space $\Theta_n$. Within fixed model space, algorithm suggested in information bottleneck could be used to update DS and reach its convergence. Resulting DS operator could be described as a best posterior samples that explain $t$ within the flexibility of given model space $\Theta_n$. Beneath the layer lie $Density$ and $Sampler$ whose composition explains the nonunique relation between model configuration and posterior sample.  $(\Theta, t) -Density\rightarrow p(\theta, t, \theta') -Sampler\rightarrow \theta_{1..a},t_{1..b}, \theta'_{1..c}$

## Joint measure on model configuration space: $\mu_1\times .. \times \mu_N(\Theta_1 \times .. \times \Theta_N)$
- Prior $p(\Theta)$ is assigned on model configuration space which takes the form of a measure on joint space: product space of every possible model combination. 
- examples of product space axis are: type of predictors and form of density.
- different points of the model configuration space could be mapped to the same Y.
- form of distribution eg. 
-  measure formeach decision step, you are given a  has different model space: model averaging

fix the model scope: assign the measure on 
given a data and a fixed model configuration, we find the best parameter set that explains the data.
## DS operator: $DS: (\Theta, t) \rightarrow \theta_{1..a}, \theta'_{1..c}$
- $\Theta$ is a assigned parameter space. $t$ is suffient statistics that include all information from data.
- full: $(\Theta, t) -Density\rightarrow p(\theta, t, \theta') -Sampler\rightarrow \theta_{1..a},t_{1..b}, \theta'_{1..c}$
- $var(\theta') = 0$ when using deterministic method
- prior, sampling, approximate posterior density constitue $p(\theta, t, \theta')$ 
- practical use: $[\theta_{1..a},t_{1..b}]$ for predictive check, $[\theta_{1..a}, \theta'_{1..c}]$ for simulation-based calibration. 


## DS operator  update $DS_n \rightarrow DS_{n+1}$
- examples of DS update:
-- sampling density (add predictor, poisson to NB likelihood)
-- posterior density (MCMC to ADVI or Laplace)
-- hyperparameter (adapt metric or leapfrog step)
- updates are based on how modeler or adaptive algorithm respond to the given data. Extreme update is expected after spectacular misfit.



## SBC operator
Given a model and posterior, it finds the best _assignment_ $p(\theta)$ by iteratively upating $p(\theta)$ until $p(\theta'|\theta)$ satisfies certain condition: symmetry based on self-consistent equation.


When DS is fixed, prior could be updated and converge:

This is similar to how IBT proved its converge of DS with fixed $p(\theta)$ and $p(\theta'|\theta)$ $p(\Theta)$. This is due to their dual relationship:

$[p(t|\theta), p(\theta|t), p(t)]$ and $[p(\theta), p(\theta'|\theta)]$ are in a dual relationship under self-consistent equation in that convergent dynamic update are possible by fixing the other component. Given  $t$, we could design two types of convergence that could to achieve the result's convergence to $t \in R^n$.
i) $<g , f>_{n} \rightarrow t$ : update $<>_n$ with fixed $f$
ii) $<g , f_{n}> \rightarrow t$ : update $f_n$ with fixed $<>$
This fact uses the dual relationship between f and < ,f> which correspnd to joint measure and DS operator from below.

IBT suggests DS operator update and prove its convergence with fixed $p(\theta)$ and $p(\theta'|\theta)$.
$$
p_{n}(t \mid \theta)=\frac{p_{n}(t)}{Z_{n}(\theta, \beta)} \exp (-\beta d(\theta, t)) \\
p_{n+1}(t)= \Sigma_{\theta} p(\theta) p_{n}(t|\theta) \\
p_{n+1}(\theta|t)= \Sigma_{\theta}p(\theta'|\theta) p_{n}(\theta|t)
$$

Q. data ~ t?
Q. meaning of $p(\theta'|\theta)$?
- fixed?
- p(theta'|theta) = 1 means there is no additional knowledge to be learned from data.

Likewise, joint model space measure $p(\theta), p(\theta'|\theta)$ could be designed with fixed $p(t|\theta), p(\theta|t), p(t)$.
$$
p(t \mid \theta)=\frac{p_{n}(t)}{Z_{n}(\theta, \beta)} \exp (-\beta d(\theta, t)) \\
p(t)= \Sigma_{\theta} p_n(\theta) p(t|\theta) \\
p(\theta|t)= \Sigma_{\theta}p_n(\theta'|\theta) p(\theta|t)
$$



1) 
2) ie. find the best $p(t|\theta), p(\theta|t), p(t)$ and its sample. However, if the modeler decides to change the model,     I mean as an attempt to learn high dimensional in a subcomponent-fixed iteration way. p(y,theta) connects parameter and sampler given the data and either p() or theta_family should be fixed to learn the other. This shares its vain with self-consistency field approximation in quantum chemisty.

The latter update could be applied to find the prior given a data and posterior sampler. This is the extension of Simulation-based calibration: a tool that checks the validity of posterior sampler given a model by checking the uniformity of rank between prior and its posterior samples.


joint measure update: $(\mu_1\times ... \times \mu_N)_n\ \rightarrow (\mu_1\times ... \times \mu_N)_{n+1}$
- structure and cardinality need not be reserved.
- This affects the DS operatorf








## Experiment 
https://hackmd.io/tZPcC4MAR8Wr8Gd32cwc3Q
- convergence measure: $\operatorname{Var}(\theta_{post})/\operatorname{Var}(\theta_{prior}) \in [0.8,1.2] \; \forall$ parameters using $\operatorname{Var}(\theta_{post})=\mathrm{E}[\operatorname{Var}(\theta_{post} \mid \theta_{prior})]+\operatorname{Var}(\mathrm{E}[\theta_{post}\mid \theta_{prior}])$
- convergence of linear regression from different initial priors $p_0(\theta)$
-- tighter prior = faster convergence
- hierarchical model (eight school) with centered/noncentered parameterization (cp results only 0513)

## Further development
Optimization and bayesian computation are two required theoretical fields. 
- interpreting this with online decision theory lens and information-bottleneck theory. 
- connection with Bayesian workflow and prior proposal mechanism on the established framework of Stan and posteriordb.
- user defined $t$ 
- symmetry inspection of $\theta, \theta'$: think of new variable $\theta - \theta'$ and use the definition "symmetric r.v when X and -X has same distribtion"  compare the distribution of prior that led to the same posterior with our NM matrix. or comparison of prior-posterior with posterior-prior. connect with coupling theory. need to make the two independent

- understand IBT's succesful application to deep learning
https://www.quantamagazine.org/new-theory-cracks-open-the-black-box-of-deep-learning-20170921/#comments
- connection withSelf-Consistent Field (SCF) Method in quantum chemistry which has the following explanation:
- write the equation solutionas with fixed basis function: $\psi$ as $c_1\phi_1 +  ... + c_n\phi_n$. Then for each component, iterate expectation then substitution
$f_1(c_1,..,c_n) = E_1[c_1]$
$f_2(c_1,..,c_n)) = E_2[c_2]$


> Generally, the real wavefunction of a system is too complex to be found directly, but can be approximated by a simpler wavefunction. This then enables the electronic Schrödinger equation to be solved numerically. The self-consistent field method is an iterative method that involves selecting an approximate Hamiltonian, solving the Schrödinger equation to obtain a more accurate set of orbitals, and then solving the Schrödinger equation again with theses until the results converge.


Further reading
[Opening the black box of Deep Neural Networks via Information](https://arxiv.org/pdf/1703.00810.pdf)
[Machine learning and the physical sciences](https://journals.aps.org/rmp/pdf/10.1103/RevModPhys.91.045002?casa_token=7KGU-JUuvp0AAAAA%3AcKcJozhrYKv-L5N3u34F7I2ibfsSw6N3OgKZ8hbtkbpjHp__QOF1qgedwwqY5FVUbWOp599-uTi3Ce8u)


## Q

Q1. meaning of $p(\theta'|\theta)$?
- fixed?
- p(theta'|theta) = 1 means there is no additional knowledge to be learned from data.

Q2. related to ADMM method?
Constraint is self-consistency equation. What would be the objective function? 
$min_x f(x)+g(z)$
$s.t. Ax+Bz=c$

Q3. notation
- $t$: suffient statistics VS general coded information

Q4. implementation issues:
1. How to weight each parameter for standard for convergence? NMP vs NM 
2. How to design additional convergence measure regarding mean? Same variance does not guarantee equivalence of two sample sets.

Q5. interpretation of $min_{p(\tilde{x})}$?
![](https://i.imgur.com/5FM2klr.png)

![](https://i.imgur.com/iWgzOcR.png)
![](https://i.imgur.com/q8biToX.png)
