###### tags: `risk measure`, `counterfactual`, `coupling`, `verification`, `calibration` `decision` `gametheory`


# Calibrating system
Every proposal is approximation to the unkown which needs to be `measured` `improved` `traded-off` 

efficient = lifting to time axis then marginalized out time = plug Ez to z
without external force (guide) it could take much longer to reach optimal
### recap from the paper

### 1.information balance btw latent-nonlatent 

- Static self-consistency as no **information is lost in its marginalization to p(θ, y)**, just as no information is lost by **saving the upper half of a symmetric matrix**.

- counterfactual $\in\sigma(parameter) = \sigma(observable) =  \sigma(observable, paramter)$ 

- learning from generated data until information is balanced with full data


#### Q
- test for the system optimal?
    - all the counterfactuals are adapted to $\theta_{opt}$
    - Self-Consistent Field (SCF) Method 
    - ![](https://i.imgur.com/KIgz8K8.png)
![](https://i.imgur.com/a0yF7N0.png)
![](https://i.imgur.com/s8aoO4P.png)

![](https://i.imgur.com/yAiPGsG.png)

![](https://i.imgur.com/dI7H7aW.jpg)

    - Hartree required final field computed from the charge distribution to be "self-consistent" with the assumed initial field.
    - wave function too complex to be found directly, but can be approximated by a simpler wave function. This then enables the electronic Schrödinger equation to be solved numerically. The self-consistent field method is an iterative method that involves selecting an approximate Hamiltonian, solving the Schrödinger equation to obtain a more accurate set of orbitals, and then solving the Schrödinger equation again until the results converge.
    - goal: converge to Schrödinger equation solution through
     i) specify class 
    ii) optimize (allocate, parameter estimation) 
    iii) compare iteration (project to $\sigma(T)$) $T$ is quantities of interest.
    iteration as joint is too complex 
     - convergence: E_t[f(y, theta, t)] = f(y, theta)

    - same value on measurable sets 
        $f(\theta_1, ., \theta_k, ., \theta_n) = f(\theta_1,.,  \theta'_k,., \theta_n)$ E_{}\theta_k/\theta_k' := E_{p(\{\theta)\}\theta_k}\theta_1, \theta_2, ..., \theta_n)$ 

## optimal verification 
algorithm to test/bring to the system optimal
    - what is the state of a ruined gambler? Send N gamblers and average their state indexed at their ruined time ($\alpha_1..N$) i.e. E[state[$\alpha_i$]]
    - ergodic:  time average on the orbit of x converges to the space average of f: $\lim _{k \rightarrow+\infty}\left(\frac{1}{k+1} \sum_{i=0}^{k} f\left(T^{i}(x)\right)\right)=\int_{X} f d \mu$
    - while($f(\theta_1,..,\theta_p)$ converge) 
        - repeat $\theta_i$ with $E[\theta_i]$
        - i <- i + 1(mod p) 
    - convr's invisible hand (Adam smith) failed..
    - with the help of`time` or`random` as the n+1th player which gives the effect of substituting z with Ez, can the system refine itself with iterated update and converge to system optimal?
    - genetic algorithm, multiverse, digital twin, 
    - EM algorithm: 

generated data holds information of the model which is constructed with real data and intention. Iterated refinement the system would reach the 

2. definition of robust prior
I am trying to argue that widest self-consistent prior is robust; 
Is robust having a unique solution under variances given certain axioms (from your paper online advertising)? What 
self-consistency axiom: unique solution under symmetry, loc-scale-invariant (efficiency and linearity? - computation)

The relative entropy D_KL (p || q) measures <font color ="blue"> how many bits per symbol are wasted </font> by using a code whose implicit probabilities are q, when the ensemble’s true probability distribution is p.


![](https://i.imgur.com/KYhkgKd.png)

3. relation with variational free energy


3 agents with 2 dms
- motivation for change (adopt block chain)
![](https://i.imgur.com/5WDu8I4.png)
transfer welfare from the third to two dms
- (bidding - dist.robust mechanism design)

would transfer happen as a result of iterated update (not overseeing force but from local entity)

counterfactual data holds info.
- game theory

### 3. model network navigator

- gradient calculation: `simple` model (4 noeds)
![](https://i.imgur.com/hoaE5uj.png)

- multi-chain exploration: `golf` model (12 nodes)
![](https://i.imgur.com/HOWS2r4.png)

where really needed
![](https://i.imgur.com/y408uFR.png)

- not all edges are created equal: depending on the bifurcation node's characteristic (say distribution lognormal vs std) edge and gradient calculation should be different

