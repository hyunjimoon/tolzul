There is no such thing as an optimal simulation method. - [Christian P. Robert](https://link.springer.com/book/10.1007/0-387-71599-1#author-0-0)the author of The Bayesian choice

However, we can categorize them into three families:

## 1. Accept-reject (AR) methods

AR methods are intended to provide an i.i.d. sample from f. To achieve this, one designs an algorithm that takes as input a random number of uniform variates 𝑢1,𝑢2,... and returns a value x that is a realisation from f. The _pros_ are that there is no approximation in the method: the outcome is truly an i.i.d. sample from f. The _cons_ are many: (i) designing the algorithm by finding an envelope of f that can be generated may be very costly in human time; (ii) the algorithm may be inefficient in computing time, i.e., requires many uniforms to produce a single 𝑥x; (iii) those performances are decreasing with the dimension of X. In short, such methods cannot be used for simulating one or a few simulations from f unless they are already available in a general computer language.

## 2. Markov chain Monte Carlo (MCMC) methods

 MCMC are extensions of i.i.d. simulations methods when i.i.d. simulation is too costly. They produce a sequence of simulations xt which limiting distribution is the distribution f. The _pros_ are that (i) less information about f is needed to implement the method; (ii) f may be only known up to a normalising constant or even as an integral and still be associated with an MCMC method; (iii) there exist generic MCMC algorithms to produce simulations (xt)t that require very little calibration; (iv) dimension is less of an issue as large dimension targets can be broken into conditionals of smaller dimension (as in Gibbs sampling) or HMC which allows smart update by iterating lifting and projecting between manifold and symplectic manifold (symplectic optimization).

   
The _cons_ are that (i) the simulations (xt)t are correlated, hence less informative than i.i.d. simulations; (ii) the validation of the method is only asymptotic, hence there is an approximation in considering $x_t$ for a fixed t as a realization of f; (iii) convergence to f (in t) may be so slow that for all practical purposes _the algorithm does not converge_; (iv) the universal validation of the method means there is an infinite number of potential implementations, with an equally infinite range of efficiencies.

## 3. **Importance sampling methods** 

are originally designed for integral approximations, namely generating from the wrong target g(x) and compensating by an importance weight

f(x)/g(x).

```
The resulting sample is thus weighted, which makes the comparison with the above awkward. However, importance sampling can be turned into importance sampling resampling by using an additional resampling step based on the weights. The _pros_ of importance sampling resampling are that (i) generation from an importance target 𝑔g can be cheap and recycled for different targets 𝑓f; (ii) the "right" choice of 𝑔g can lead to huge improvements compared with regular or MCMC sampling; (iii) importance sampling is more amenable to numerical integration improvement, like for instance quasi-Monte Carlo integration; (iv) it can be turn into adaptive versions like population Monte Carlo and sequential Monte Carlo. The _cons_ are that (i) resampling induces inefficiency (which can be partly corrected by reducing the noise as in systematic resampling or qMC); (ii) the "wrong" choice of 𝑔g can lead to huge losses in efficiency and even to infinite variance; (iii) importance has trouble facing large dimensions and its efficiency diminishes quickly with the dimension; (iv) the method may be as myopic as local MCMC methods in missing important regions of the support of 𝑓f; (v) resampling induces a bias due to the division by the sum of the weights.
```

Recalling the advise by Christian Robert, simulation should be chosen based on the demand. Dimension, type (continuous/discrete) of the parameter, and the need for explainability are main information modelers should base their choice of sampling methods.


Based on Christian Robert's work and the provided search results, I can infer some potential reasons why he might believe importance sampling could be the future of sampling methods. Here's a summary in table format:

using [smc perplexity]( https://www.perplexity.ai/search/please-find-me-a-post-where-ch-QWKGMEgFS8er2bg9A_emcg#1), below are some reasons why SMC is 

| Reason | Explanation |
|--------|-------------|
| Adaptability | Importance sampling can be adapted to complex and high-dimensional distributions, making it versatile for various applications[2][3].|
| Efficiency | Adaptive importance sampling methods can significantly improve accuracy with minimal additional computational cost[2].|
| Flexibility | It can be combined with other techniques, such as Stein variational gradient descent, to create more powerful sampling algorithms[3].|
| Applicability to real-world problems | Importance sampling has shown promise in addressing challenges in reinforcement learning and partially observable Markov decision processes[1].|
| Ongoing research and innovation | There's active research in developing new variants and improvements, such as implicitly adaptive and multiple importance sampling methods[2][3].|
| Theoretical foundations | Importance sampling has well-established theoretical properties, allowing for rigorous analysis and improvement of algorithms[1][3].|
| Potential for parallelization | Some importance sampling methods can be parallelized, potentially increasing computational efficiency[3].|
| Applicability to intractable problems | It can be used to estimate intractable normalization constants and handle complicated distributions not available in closed form[2][3].|

While Christian Robert hasn't explicitly stated that importance sampling is the future, his continued research and contributions to the field suggest he sees significant potential in these methods for addressing complex sampling challenges.

Citations:
[1] https://www.cs.ucr.edu/~cshelton/papers/docs/phd.pdf
[2] https://link.springer.com/article/10.1007/s11222-020-09982-2
[3] http://auai.org/uai2017/proceedings/papers/217.pdf
[4] https://www.researchgate.net/publication/318376952_Adaptive_Importance_Sampling_The_past_the_present_and_the_future
[5] https://www.youtube.com/watch?v=czFB8IAeFxw