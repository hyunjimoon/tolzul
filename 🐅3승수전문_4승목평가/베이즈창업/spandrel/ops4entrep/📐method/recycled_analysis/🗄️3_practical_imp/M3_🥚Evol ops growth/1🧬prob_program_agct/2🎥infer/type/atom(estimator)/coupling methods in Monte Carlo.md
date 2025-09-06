#coupling #sampling

- [[#What|What]]
- [[#How|How]]
- [[#Why|Why]]
- [[#Integration with Markov Chains|Integration with Markov Chains]]
- [[#Initialisation Bias in MCMC|Initialisation Bias in MCMC]]
- [[#Path Measure Representation of MCMC Estimators|Path Measure Representation of MCMC Estimators]]
- [[#Telescoping Representations of Expectations|Telescoping Representations of Expectations]]
- [[#Path Space Couplings|Path Space Couplings]]
- [[#Unbiased Estimation by Faithful Couplings|Unbiased Estimation by Faithful Couplings]]
- [[#Practical Construction of Couplings|Practical Construction of Couplings]]
	- [[#Practical Construction of Couplings#Simple Skeleton Strategy|Simple Skeleton Strategy]]
- [[#Conclusion|Conclusion]]


## What
Removing Initialisation Bias in MCMC

## How
- telescope

## Why
- unbiased coupling

**Overview**: Coupling techniques can be used to remove the initialisation bias which is common to methods of Markov Chain Monte Carlo.

## Integration with Markov Chains

The standard Monte Carlo method estimates the integral $I = \int f(x) p(dx)$ by drawing independent samples from $p$, computing the value of $f$ at those samples, and then averaging those values.


$$\hat{I}_N ^{\text{MC}}= \frac{1}{N} \sum_{i = 1}^N f(x^i)$$


The Markov Chain Monte Carlo method is designed for problems in which sampling directly from $p$ is challenging, and so instead focuses on generating a sequence of correlated points $\{ X_t \}_{t \geqslant 1}$ which converge in distribution to $p$. Provided that this convergence takes place rapidly enough, one can use these points 'as if' they were drawn from $p$, and still obtain consistent estimates of $I$:


$$\hat{I}_T ^{\text{MCMC}}= \frac{1}{T} \sum_{t = 1}^T f(X_t).$$


One typically incurs some additional variance as a price for the correlation between the points $X_t$, but the hope is that despite this additional variance, the situation is better than simply trying very hard to draw exact samples from $p$, the complexity of which can often scale exponentially unfavourably with the difficulty of the problem.

## Initialisation Bias in MCMC

Despite the rich theory associated with estimators derived in this way, there has been a persistent unease with the initialisation bias of these estimators. This is essentially a by-product of the fact that the chain $X_t$ typically starts off 'out of stationarity', i.e. $X_0$ may be very far from having the distribution of $p$. For $t_0$ sufficiently large, one expects that the chain with have 'reached stationarity', and so the estimator 
$$
\begin{align}
\hat{I}_{T;t_0}^{\text{MCMC}}= \frac{1}{T - t_0} \sum_{t > t_0}^T f(X_t)
\end{align}
$$
will have much more reasonable bias properties.

Of course, this is in some sense easier said than done. In some cases, it is reasonable to make a guess at a suitable $t_0$ by eye, and in other cases there are useful heuristics for estimating $t_0$ systematically. Nevertheless, while each of these strategies can mitigate the initialisation bias to some extent, they do not really get rid of it entirely. It is thus of interest to identify generic strategies which can resolve this problem.

It should perhaps be emphasised that the bias removal task is not about magically taking a bad set of samples and transforming them into great estimates. The ability of any Markov chain-based procedure to provide useful estimates will always be contingent on the ability of the chain to explore the state space efficiently. Bias removal should be thought of more as having quite a specific goal: many things can go wrong when computing estimates via MCMC, but we can try to ensure that initialisation bias is not the main thing which is going wrong.

## Path Measure Representation of MCMC Estimators

Write $p_0$ for the law of where our chain is born, and $K$ for the transition kernel which governs its evolution. I will occasionally use the following abstract notation
$$
\begin{align}
\mathbf{P}(dX) = p_0 (dX_0) \cdot \prod_{t \geqslant 1} K ( X_{t-1} \to dX_t )
\end{align}
$$
without really justifying its meaning. One should just think of it as the law of the particle's path, starting at birth, throughout its lifespan.

One can then write the conventional MCMC estimator as an unbiased estimate of
$$
\begin{align}
I_{1:T} ^{\text{MCMC}}= \mathbf{E}_\mathbf{P} \left[ \frac{1}{T} \sum_{t = 1}^T f(X_t) \right].
\end{align}
$$
Under suitable conditions, one can prove that $I_T ^{\text{MCMC}}$ (which is a deterministic quantity) converges to $I = \mathbf{E}_p [f]$, as we would hope. However, generally it will not be the case that $I_T ^{\text{MCMC}} = I$ at finite $T$, i.e. we have some bias in our estimator.

Equally, we could consider the single-term estimator
$$
\begin{align}
I_T ^{\text{MCMC}}= \mathbf{E}_\mathbf{P} \left[ f(X_T) \right],
\end{align}
$$
to which similar (but not identical) comments apply. For example, the bias of this estimator decreases more rapidly, but the variance remains of constant order in $T$.

## Telescoping Representations of Expectations

With our previous comments in mind, we can write
$$
\begin{align}
I &= \lim_{T \to \infty} \mathbf{E}_\mathbf{P} \left[ f(X_T) \right] \\
&= \lim_{T \to \infty} \left( \mathbf{E}_\mathbf{P} \left[ f(X_0) \right] + \sum_{1 \leqslant t \leqslant T} \mathbf{E}_\mathbf{P} \left[ f(X_t) \right] - \mathbf{E}_\mathbf{P} \left[ f(X_{t-1}) \right] \right) \\
&= \mathbf{E}_\mathbf{P} \left[ f(X_0) \right] + \sum_{t \geqslant 1} \left( \mathbf{E}_\mathbf{P} \left[ f(X_t) \right] - \mathbf{E}_\mathbf{P} \left[ f(X_{t-1}) \right] \right).
\end{align}
$$
Going forward, I will assume without a loss of generality that $\mathbf{E}_\mathbf{P} \left[ f(X_0) \right] = 0$.

Now, time to think about what can we do with this representation.

* The bad news: the sum is infinite, so we don't have time to evaluate it directly. Also, even if the sum were finite, its terms are expressed as expectations, so we would need to do some sampling to estimate each of the terms.
* Some good news: the telescoping terms $\left( \mathbf{E}_\mathbf{P} \left[ f(X_t) \right] - \mathbf{E}_\mathbf{P} \left[ f(X_{t-1}) \right] \right)$ decay as $t$ grows, and normally at an exponential rate (though not always a fast one).
* Some bad news: Despite this, we do not immediately have a low-variance estimator of these terms: if we estimate both terms using $(X_{t-1}, X_t)$ from the same Markov chain, we should expect the term to be of order $1$.
* Some good news: We know that we don't have to use the same Markov chain to estimate this difference unbiasedly, which means that there is some hope of finding an estimator of this difference whose variance vanishes as $t$ grows.

## Path Space Couplings

To this end, let $\mathsf{P}$ denote a coupling of two copies of $\mathbf{P}$, i.e. the law of two  infinite sequences, each of which marginally behaves according to the path measure $\mathbf{P}$. Calling the corresponding sequences $X_t^1, X_t^2$, we might now write
$$
\begin{align}
I &=  \sum_{t \geqslant 1} \left( \mathbf{E}_\mathbf{P} \left[ f(X_t) \right] - \mathbf{E}_\mathbf{P} \left[ f(X_{t-1}) \right] \right) \\
&=  \sum_{t \geqslant 1} \left( \mathbf{E}_\mathsf{P} \left[ f(X_t^1) \right] - \mathbf{E}_\mathsf{P} \left[ f(X_{t-1}^2) \right] \right) \\
&= \sum_{t \geqslant 1} \mathbf{E}_\mathsf{P} \left[ f(X_t^1) - f(X_{t-1}^2) \right] \\
&= \mathbf{E}_\mathsf{P} \left[ \sum_{t \geqslant 1} \left( f(X_t^1) - f(X_{t-1}^2)  \right) \right].
\end{align}
$$
Now, we are back in business! Some quick takeaways:

* If we want to estimate $I$ in the case where $f$ is Lipschitz, then it suffices for us to find a coupling $\mathsf{P}$ such that $\mathbf{E}_\mathsf{P} \left[ |X_t^1 - X_{t-1}^2| \right]$ decays quickly. 
* If $f$ is bounded, then it suffices for us to find a coupling $\mathsf{P}$ such that $\mathsf{P} \left( X_t^1 \neq X_{t-1}^2 \right)$ decays quickly.

Essentially, if we can couple the two chains to be close together, with high probability, then we have a reasonable hope of estimating some of the terms in this infinite sum with an acceptable variance.

Nevertheless, we still have an infinite sum facing us, which poses some problems. We could use an importance sampling trick to truncate the sum, but this may be undesirable.

## Unbiased Estimation by Faithful Couplings

A delightful solution to this problem is to have the sum truncate itself, by having its terms converge exactly to $0$. Recall our estimator
$$
\begin{align}
\hat{I}_\mathsf{P} &=\sum_{t \geqslant 1} \left( f(X_t^1) - f(X_{t-1}^2)  \right).
\end{align}
$$
Now, suppose that our coupling is structured such that, with probability $1$, there is a time $\tau$ such that $X_\tau^1 = X_{\tau - 1}^2$, and $X_t^1 = X_{t-1}^2$ for all $t \geqslant \tau$. That is, at the (random) time $\tau$, the two sequences meet one another, and they stay together thereafter. Such a coupling is called *faithful*.

In that case, one can write
$$
\begin{align}
\hat{I}_\mathsf{P} &=\sum_{t \geqslant 1} \left( f(X_t^1) - f(X_{t-1}^2)  \right) \\
&= \sum_{1 \leqslant t < \tau} \left( f(X_t^1) - f(X_{t-1}^2)  \right).
\end{align}
$$
In particular, the sum has *finitely-many terms*. Even though the estimator is constructed by considering an infinitely-long sequence, it can be computed in finite time. Thus, using a Markov chain whose state at time $t$ converges in law to $p$, we have constructed an unbiased estimator of expectations under $p$.

Two small comments are in order. Firstly, as should now be unsurprising, while the computational cost of the estimator is almost surely finite, it is both random, unbounded, and potentially heavy-tailed. Depending on how the coupling $\mathsf{P}$ is constructed, the distribution of $\tau$ may be favourable or disastrous. 

Secondly, the estimator can sacrifice structure, in the sense that e.g. even for nonnegative $f$, the corresponding estimator of $\mathbf{E}_p[f]$ may be negative. In some sense, this is also par for the course.

## Practical Construction of Couplings

As in our earlier encounters with couplings, we face a conceptually tough situation: there are optimal couplings in theory, implementable options in practice, and we want to find something roughly in their intersection. A reasonable ansatz to narrow the search space is the following: constrain the coupling to be Markovian with respect to the off-by-one pair $(X_t^1, X_{t-1}^2)$, i.e. so that it can be written as
$$
\begin{align}
\mathsf{P}(dX^1, dX^2) = &\ p_0 (dX_0^1) \cdot K_0 \left( dX_1^1, dX_0^2 | X_0^1 \right)\cdot \prod_{t > 1} K_t (dX_t^1, dX_{t-1}^2 | X_{t-1}^1, X_{t-2}^2), 
\end{align}
$$
i.e. one can sample from the coupling as 

1. Sample $X_0^1 \sim p_0$
2. Sample $(X_1^1, X_0^2) \sim K_0$, such that marginally (conditional on $X_0^1$), it holds that
$$
\begin{align}
X_1^1 &\sim K(X_0^1 \to dX_1^1)\\
X_0^2 &\sim p_0
\end{align}
$$
3. For $t > 1$, sample $(X_t^1, X_{t-1}^2) \sim K_t$, such that marginally (conditional on $X_{t-1}^1, X_{t-2}^2$), it holds that
$$
\begin{align}
X_t^1 &\sim K(X_{t-1}^1 \to dX_t^1)\\
X_{t-1}^2 &\sim K(X_{t-2}^2 \to dX_{t-1}^2).\\
\end{align}
$$
Additionally, it simplifies matters greatly to constrain the $K_t$ to be time-homogeneous. 

### Simple Skeleton Strategy

A basic coupling framework would be the following: to initialise, do

1. Draw $X_0^1 \sim p_0$.
2. Draw $X_1^1 \sim K (X_0^1 \to dX_1^1)$.
3. Draw $X_0^2 \sim p_0$.

Now, the challenging part: for $x', x'' \in \mathcal{X}$, let $\mathcal{K} ( (x', x'') \to (\cdot, \cdot))$ be a coupling of $\left( K(x' \to \cdot) , K(x'' \to \cdot) \right)$. Then, for $t > 1$, do

4. Draw $(X_t^1, X_{t-1}^2) \sim \mathcal{K} \left( (X_{t-1}^1, X_{t-2}^2) \to (dX_t^1, dX_{t-1}^2)\right)$

Most of the ingenuity in these methods is caught up in the construction of these $\mathcal{K}$ kernels. Here, I sketch (quite roughly) a couple of examples.

* For Gibbs-type updates, one can often draw from the kernel $K(x \to dy)$ by sampling $\xi \sim \rho$, where $\rho$ is some $x$-independent auxiliary distribution, and setting $y = \mathcal{G}(x, \xi)$. A natural coupling would then be to draw a single $\xi_t$, and set
$$
\begin{align}
X_t^1 &= \mathcal{G}( X_{t-1}^1, \xi_t) \\
X_{t-1}^2 &= \mathcal{G}( X_{t-2}^2, \xi_t).
\end{align}
$$
* For Metropolis-type updates, there are two challenges:
    * The proposal kernels should be well-coupled to one another, i.e. the proposed moves should ideally be close together. This is normally relatively straightforward, e.g. 
        * in Random Walk methods, couple the noises which are added to each chain
        * in Diffusion methods, couple the driving Brownian motions of each chain
        * in Hamiltonian dynamics, couple the momentum variables of each chain
    * The accept/reject decision should be made optimally, i.e. given the initial and proposed states of each chain, the coin flips in the accept-reject step should be coupled so as to minimise the expected distance between the resulting states of the chain.

It should be noted that for 'unadjusted' MCMC algorithms (e.g. ULA, uHMC), coupling is slightly more straightforward. There are tradeoffs here: this methodology still allows for the initialisation bias of these methods to be mitigated, but the asymptotic bias will remain. In this sense, the simplicity of coupling is paid for by the introduction of a new form of bias.

There are additional subtleties and difficulties which I will not cover here. For standard sampling algorithms, it seems that by now, there are some reasonably reliable strategies for coupling chains without too much pain. As ever, there will be counterexamples. One must also keep in mind that the difficulty of coupling is related to the ability of the underlying Markov chains to equilibrate quickly.


## Conclusion

In this note, I have outlined a recently-developed strategy which allows for the initialisation bias of MCMC methods to be removed, by use of coupling techniques. In keeping with other debiasing methods, the method has a random, finite run-time, and may inflate the variance relative to simple methods which retain a bias. 

There are a number of important aspects of this methodology which have been glossed over here. The ability to parallelise these methods at scale is particularly relevant from a practical perspective. The systematic construction of practical, efficient coupling kernels also deserves closer attention.
