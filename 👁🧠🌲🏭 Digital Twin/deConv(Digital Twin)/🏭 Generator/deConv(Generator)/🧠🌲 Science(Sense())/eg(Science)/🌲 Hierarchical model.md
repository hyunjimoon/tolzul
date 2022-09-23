The following is the basic three-layer structure of hierarchical model.

1. The observational model for the data.
$$
\left(Y_{i} \mid \theta\right) \sim f\left(y_{i} \mid \theta\right), \quad i=1, \ldots, k
$$
2. The structural model for the parameters of the likelihood.
$$
(\theta \mid \alpha) \sim g(\theta \mid \alpha)
$$
3. The hyperparameter model for the parameters of the structural model.
$$
\alpha \sim h(\alpha)
$$

Compared to normal-normal hierarchical model (where all f, g, h distribution is normal), the structure of Poisson model is worth memorizing as non-negativity constraint only admits certain family of distribution.
- f: Poisson
- g: Gamma
- h: Uniform(0,.5), Gamma(.1, 1)

![[Pasted image 20220622044013.png]]