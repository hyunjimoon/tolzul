---
이름: Clever Lifting
출생: 2021-08-08
---

My question began from how and where could the idea of lifting or augmentation be used cleverly like HMC? Adding the momentum variable helps structured sampling in HMC. I listed concepts that I thought could connect; the first part of this post describes a static relationship created by lifting between the original (q) and its new coordinate (q,p). The second part lists how this relation could be developed into a converging process through "lift then project" iteration. The third part plans to present how the second strategy be used in optimization and verification. 

## 1. Relation created by lifting  

Origin X $\xrightarrow{Lift \;  f}$ Augmented (X, f(X))

- newly created structure as the following on augmented space prompts 2 below i.e. efficient update.
    - Convex structure through dual variable: Lagrangian-related
    - Vector flow structure through dual variable: HMC, Augmented neural ODE
    - Markov structure through extra state: CVaR MDP, Stopping time
    - Sampling structure through latent var: EM, Imputation
    - Efficiency and diversity through copy: Coupling, Splitting


| algorithm | Original, | Aug (=Ori., New), New | New | Effect | Constrain/Invariant/Conserve | Ref |
| --------- | --------- | --------------------- | --- | ------ | ---------------------------- | --- |
| SBC | $\theta, (\theta, y)$ | data | verification, calib. | $(\theta, \theta')$ symmetry |  |
| Coupling | $\theta(w), (\theta\_1(w), \theta\_2(w))$ | rng-share process | unbias, var. reduction |  | [Maximal Couplings of the Metropolis–Hastings Algorithm](http://proceedings.mlr.press/v130/wang21d/wang21d.pdf) |
| Splitting | $\theta(w), (\theta\_1(w), \theta\_2(w)?)$ | ? |  |  |  |
| Copula | $x\_a, (x\_a, x\_b)$ | param. with dependence | dependence inf, calib. | Uniform marginal |  |
| Info. bottleneck | $x, (x,\tilde{x})$ | encode of the source | $p(\tilde{x}/x)$ optimal assignment | self-consistent eq. for $X \rightarrow \tilde{X},\tilde{X} \rightarrow Y$ coding marginal for p$(y/\tilde{x}), p(\tilde{x})$ | [Tishby2000](https://arxiv.org/abs/physics/0004057)(Thm.4) |
| EM | $\theta, (\theta, z)$ | latent variable | sampling is easier for $p(\theta/z)$ than $p(\theta )$ | $p(\theta) =\int p(\theta/z)dz$ |  |
| Imputation | $\theta, (\theta, z)$ | data augmentation |  |  |  |
| CVaR MDP1 | $X, (X , C)$ | running cost state |  |  | Bäuerle(2011), Huang(2016), Miller(2017), Chow(2018), Backhoff-Veraguas(2020) from [Min20](http://www.mskyt.net/wp-content/uploads/2020/11/cvar-exec.pdf) |
| CVaR MDP2 | $X, (X , Q)$ | risk aversion quantile state | CVaR dual |  | Pflug(2016), [Chow et al. (2015)](https://papers.nips.cc/paper/2015/file/64223ccf70bbb65a3a4aceac37e21016-Paper.pdf), Chapman(2018), Li(2020), [Min20](http://www.mskyt.net/wp-content/uploads/2020/11/cvar-exec.pdf) |
| Lagrangian dual | $x, (x,\lambda)$ | coeff. dual variable | dual's convex strc. | dual ineq. infsup>=supinf |  |
| Aug. Lagrangian or ADMM | $x, (x, \lambda)$ or $x,z, (x,z, \lambda)$ | coeff. dual variable | convex strc.,better convergence | dual ineq. | [A generalized risk budgeting approach to portfolio construction](http://www.columbia.edu/~mh2078/A_generalized_risk_budgeting_approach.pdf) |
| Stopping time | $X, (\alpha,X\_\alpha)$ | stopping time | Markovian strc. |  | Chung, Intro to prob. Ch.9 |
| HMC | $q, (p,q)$ | momentum in phase space | Vector flow structure | Hamiltonian symplectic vol. |  |
| Augmented Neural ODE | $x, (x\_1, x\_2)$? | feature | flexible feature mapping |  | [Augmented Neural ODEs](https://arxiv.org/abs/1904.01681) |
| Augmented preference | ? | augmented preference | infer preference w.o. util. ftn. | partial order | Boyd, Convex Optimization Ch.6 |

## 2\. Lift then project iteration

Origin $X_t \underset{\text { Lift }}{\stackrel{f}{\longrightarrow}}$  Augmented $(X_t, f(X_t))$ $\underset{\text { Project }}{\stackrel{f^{-1}}{\longrightarrow}}$ $X_{t+1}$

- used for efficient update (~ calibration) or verification via model boostrap
- verification is my aim developing on attractor idea in [_coupling, copula, calibration_](https://hackmd.io/jYRJ0fBCQZOjhtPU5Pq65w#coupling-copula-calibration)
- similar to Source ($X_t, P$) $\rightarrow\[\\text{Compress}\]{f}$ Aug. $(X\_t, f(X\_t)) \\xrightarrow\[\\text{Decompress}\]{P(X\_{t+1}|f(X\_t))}$ Receiver $X\_{t+1}$?

Source ($X_t, P$) $\underset{\text { Compress }}{\stackrel{f}{\longrightarrow}}$ Aug(X_t, f(X_t)) $\underset{\text { Decompress }}{\stackrel{f}{\longrightarrow}}$ ${P(X_{t+1}|f(X_t))}$  Receiver $X_{t+1}$?

| algorithm | Update,  target | Lift f | Projection $f^{-1}$ |
| --- | --- | --- | --- |
| SBC | $\theta\_t \xrightarrow{(\theta\_t, y\_t)} \theta\_{t+1}$, |joint dist.simulator | $p(\theta/y)$ data simulator | $p(y/\theta)$ posterior simulator |
| Copula | $x^a\_t \xrightarrow{(x^a\_t, x^b\_t)} x^a\_{t+1},x^b\_t \xrightarrow{(x^a\_t, x^b\_t)} x^b\_{t+1}$,  
|copula ftn. $C(x\_a,x\_b)$ |  |  |
| Info. bottleneck | $x\_t \xrightarrow{(x\_t, \tilde{x}_t)} x_{t+1}$,  
|$p^{\*}(\tilde{x}/x)$ |  |  |
| EM | $\theta\_t/Y \xrightarrow{(\theta\_t, z\_t)/Y} \theta\_{t+1}/Y$,  
|$p(\theta/Y)$ | $p(\theta / z)$ |  |
| Imputation | $\theta\_t \xrightarrow{(\theta\_t, z\_t)} \theta\_{t+1}$,  
|$p(\theta)$ | $Z\_{t+1} \sim P (Z / Y, θ\_t)$ | $θ{t+1} \sim P (θ / Y, Z{t+1})$ |
| CVaR MDP1 | $X\_t \xrightarrow{(X\_t, C\_t)} X\_{t+1}$,  
|optimum |  |  |
| CVaR MDP2 | $X\_t \xrightarrow{(X\_t, Q\_t)} X\_{t+1}$,  
|optimum |  |  |
| Lagrangian dual | $x\_t \xrightarrow{(x\_t,\lambda\_t)} x\_{t+1}$,  
|optimum | $f(x) +\lambda g(x)$ |  |
| Aug. Lagrangian or ADMM | $x\_t \xrightarrow{(x\_t, \lambda\_t)} x\_{t+1}$ or $x\_t,z\_t \xrightarrow{(x\_t,z\_t, \lambda\_t)} x\_{t+1}, z\_{t+1}$,  
|optimum |  |  |
| HMC | $q\_t \xrightarrow{(p\_t,q\_t)} q\_{t+1}$,  
|typical set | $q \rightarrow \pi^{-1}(q)$ |  |
| Augmented Neural ODE | $x^a\_t \xrightarrow{(x^a\_t, x^b\_2)} x^a\_{t+1}$ (Incorrect),  ? |  |  |


## 3\. Verify or optimize via lift-then-project iteration

tbc.

\---

Quotes from papers

- combining the augmented Lagrangian approach with MCMC sampling to generate a point in the proximity of the global optimum of the GRB problem. sample points with a higher objective function value and simultaneously drive the sample path in the direction of the feasible region using the augmented Lagrangian terms. - [A generalized risk budgeting approach to portfolio construction](http://www.columbia.edu/~mh2078/A_generalized_risk_budgeting_approach.pdf)
- by introducing an extra state variable, an optimal policy can be sufficiently characterized as a Markov process defined on this augmented state space. - Min's [paper](http://www.mskyt.net/wp-content/uploads/2020/11/cvar-exec.pdf)
- augment the known preferences (6.22) with the inequality u(ak) ≤ u(al). If augmented set of preferences is infeasible, it means that any concave nondecreasing utility function that is consistent with the original given consumer preference data must also satisfy u(ak) > u(al); conclude that basket k is preferred to basket l, without knowing the underlying utility function. - Boyd's convex optimization textbook p.341

Q1. From the quote in Boyd's textbook, it seems the role of "Augmented preference" is feasibility certificate, but its role is tricky to understand. Especially does 'augment' mean sampling in this context?

Q2. Could there be any relationship between splitting and coupling? Do you agree they have similar flavor; the only difference being the direction of the bifurcation --= vs =--?

Here are some related references that I am going through:  

- [Projections Onto Convex Sets (POCS) Based Optimization by Lifting](http://repository.bilkent.edu.tr/bitstream/handle/11693/27908/Projections%20onto%20convex%20sets%20(POCS)%20based%20optimization%20by%20lifting.pdf;jsessionid=5E92DF0BFBD6BEDEC1239F6B27C881F0?sequence=1)

![[Pasted image 20220919185418.png|100]]
- [M](http://www.princeton.edu/~yc5/ele522_optimization/lectures/mirror_descent.pdf)[irror descent](http://www.princeton.edu/~yc5/ele522_optimization/lectures/mirror_descent.pdf)

- Geometry of regularized optimal transport from [here](https://arxiv.org/pdf/1610.06447.pdf)

![[Pasted image 20220919185340.png|100]]


- Information projection from Nielsen's [lecutre](https://youtu.be/X3cBhBA1nNw?t=5229)  
![[Pasted image 20220919185359.png|100]]


## 4. Information Relaxation (Brown, Smith and Sun, 2010)
What if we relax the “information constraint”?
• a.k.a. non-anticipativity constraint: DM can only use the information revealed so far
• allow DM to access some future information
• introduce penalties for violating the constraint
The relaxed DP problem
• yields a performance bound on the maximal achievable performance
• can be easier to solve than the original DP problem more future information
The idea has been studied in different contexts:
• Rockafellar and Wets (1991) – stochastic programming
• Davis and Karatzas (1994) – optimal stopping
• Rogers (2002), Haugh and Kogan (2004), Anderson and Broadie (2004), Chen and Glasserman (2004) – option pricing
• Brown, Smith and Sun (2010) – general framework formulated
Applications/extensions:
• Desai, Farias, and Moallemi (2012) – optimal stopping
• Desai at el. (2012), Haugh and Lim (2012) – linear-qaudratic and linear-convex control
• Haugh and Wang (2014) – dynamic portfolio execution
• Kim and Lim (2016) – robust MAB
• Brown and Haugh (2017) – inﬁnite horizon MDPs
• Haugh and Lacedelli (2019) – POMDPs

## 5. 
 "convexify operator via lifting"이 일차 탐구대상이고, 이것과 tractable (time-spatial process), 3차원기하 well-structured 등 [Link chavatal_loc_cut_tilt](marginnote3app://notebook/32A6CD72-6DBD-4780-828F-0A87714D0B7F) to mindmap.


## 6. [[Aggregate and Marginalize]]

## 7. [[inspection paradox]]
connection with transportation and entrepreneurship on [[🍪CHIP mobility]].
continue building thoughts on https://chatgpt.com/c/677677e2-9ca0-8002-809c-63bb388e2708 - on synthesizing lift with disaggregate, project with aggregate. 

