---
alias: coupling
tags: coupling, or
---
# Coupling

1.[mathematical benefit] coupling enables 
- geometry classification (e.g. markovian maximal coupling's infimum is attained only in one of the three: Euclidean, sphere, or hyperbolic; 
- [stochastic rigidity](https://www.researchgate.net/publication/269334770_Rigidity_for_Markovian_Maximal_Couplings_of_Elliptic_Diffusions)) 
-  guarantees a.s. convergence of stochastic process like markov chain
1. [application e.g.] verify necessary relational conditions of probablistic program
- coupling functions play important roles in the phenomena and the qualitative states resulting from the interactions (e.g. synchronization, amplitude and oscillation death, low-dimensional dynamics of ensembles)

## Related concepts
- coupling from the past:
	- sampling from stationary distribution of Markov chain
	- unlike other MC, perfect sample from the [stationary distribution](https://en.wikipedia.org/wiki/Stationary_distribution "Stationary distribution")
- I wish to design an optimality verification (i.e. intenal test such as self-consistency) test with coupling on the assumption that optimal state would have the shortest meeting time for coupled processes. Optimal states' robustness to perturbation and recurrence as well as methodoloties (e.g. simulated annealing) that rest upon this assumption could support this view.


4. I am trying to find computable prior $p_c(\theta)$. Could coupling applied to both increase efficiency (e.g. faster convergence) and effectiveness (e.g. accurate multimodal estimation)? Computable prior is defined as prior samples that satisfy the following constraint given a data simulator $p_d(y|\theta)$, and posterior simulator $p_p(\theta|y)$:
 ![](https://i.imgur.com/3rqYuI1.png)
This prior is found by iterating the two steps until convergence: 1) generate y with $\theta$ drawn from $p_{k}(\theta)$, 2) infer $\theta$ from generated y which becomes $p_{k+1}(\theta)$, the pricr onlnext setpsprior. i.e. $lim_{k}p_k(\theta) = p(\theta)$

p.s. For 1.4 and 5, compared to multiple chains where random sampling $\omega$ of two chains are separate, coupled chains share this random sampling. So I don't think coupling could be of much help for multimodal problems.

시계열 분석 - hmc (cotangent bundle을 symplectic manifold) 
coupling을 kahler에서 처음 적용
ode, pde:소수 classification, graph laplacian (time t, t+1)=0




---
I am summarizing relevant facts:


## Coupling Theory
- Coupling joins the two independent process along the randomness axis. Instead of having separate random sampling process, two stochastic process are foreced to share the randomness. This is implemented by building a single process on the joint space of the two original two chains with two constraints: having the same distribution with the two once marginalized to original space.
-   try to force them to be together in a certain way have single process in the bigger space which will emulate the behavior of the two
- started from infinite particle system where synthetic (constrcution) solution outwithed the benefits of analytical solution

### vs Splitting
[splitting integrator by Sam power](https://hackmd.io/@sp-monte-carlo)
### vs Chaining
![](https://i.imgur.com/AVldoJe.png)
$\mathbb{E} \sup _{t \in T} X_{t} \leq C K \sum_{k \in \mathbb{Z}} 2^{-k} \sqrt{\log \mathcal{N}\left(T, d, 2^{-k}\right)}$
$X_{t}-X_{t_{0}}=\left(X_{\pi_{\kappa}(t)}-X_{t_{0}}\right)+\left(X_{\pi_{\kappa+1}(t)}-X_{\pi_{\kappa}(t)}\right)+\cdots+\left(X_{t}-X_{\pi_{K}(t)}\right)$
purpose: uniform bound for random process
1. Chaining set-up: nets, 
2. Controlling the increments, 
3. Summing up the increments

### vs Lifting
- $\mu_1, \mu_2$ are related by the lifting of R iff there exists the distribution $\nu$ where $\nu$ is a coupling of $\mu_1. \mu_2$ and support of $\nu$ is included in R.
- "different couplings yield liftings for different relations"
- useful becaue if two distributions are related by a lifted relation R† , we can treat two samples from the distribution as if they were related by R, i.e. the lifting machinery gives a powerful way to translate between information about distributions and samples.

## Coupling Math Application 
- used to prove equivalence, convergence (Markovian property), stochastic domination of probabilistic processes. Also it could help debias estimation by viewing coupling as parallel process and using telescope sum
$$H_{k}(X, Y)=h\left(X_{k}\right)+\sum_{n=k+1}^{\tau-1}\left\{h\left(X_{n}\right)-h\left(Y_{n-1}\right)\right\}$$

- interacting particle system, randomized algorithms, harmonic functions ( #gradient estimation)random walks, card shuﬄing, Poisson approximation, Markov chains, correlation inequalities, percolation, 
## Coupling outside Math Application
- interacting particle systems
- verifying compositional relationality conditions of probablistic program (map back)
- easy with  and reduced to proving non-relational non
- meeting time shortening strategies for faster convergence 

## Coupling Application in OR
- verify the three necessary conditions for differential privacy: monotonicity, stabilty, non-interference
- instead of analyzing a single probabilistic computation, need to deal with two.

- Probabilistic (bi)simulation can be characterized logically, i.e., two systems are (bi)similar if and only if they satisfy the same formulas in some modal logic
- bound the probability of speciﬁc events in the coupling distribution to prove quantitative probabilistic relational properties.
- couple the samplings to guide the two states towards one another, especially if the states are many transitions apart. path coupling method, a powerful tool to construct
- Liftings were originally introduced in research on probabilistic bisimulation, a technique for verifying equivalence of two probabilistic transition systems. By viewing liftings as a particular kind of coupling, we can repurpose veriﬁcation tools to prove new properties by constructing couplings, while leveraging ideas from the coupling literature to enrich existing systems.

- coupling is running a multiple chain (thinking in a joint probability) for efficiently learn the geometry to boost the convergence to optimum (meeting) 

- when exploring the model network, the following multiple thread approach would be efficient
-![](https://i.imgur.com/j1he43s.png)


Reference
[Probabilistic Coupling, Kendall](https://warwick.ac.uk/fac/sci/statistics/staff/academic-research/kendall/personal/talks/CouplingReview-handout-2x2.pdf)
[Relational Program Verification and Probabilistic Couplings - Gilles Barthe](https://www.youtube.com/watch?v=pae2t5lPupk&t=713s&ab_channel=ETHWSCR)