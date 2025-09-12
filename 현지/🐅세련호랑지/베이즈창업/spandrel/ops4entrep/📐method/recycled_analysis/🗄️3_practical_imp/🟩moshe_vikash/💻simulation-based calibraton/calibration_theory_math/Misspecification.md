#calibration #misspecification

# Misspecification
posterior 

1. misspecification

- [Misspecified Linear Bandits,  Ghosh17](https://arxiv.org/pdf/1704.06880.pdf) address misspeciﬁed (stochastic) linear bandits with a ﬁxed action set. In misspeciﬁed linear bandits, the reward is nearly a linear function of the feature vectors associated with the actions. - 
-- choose btw linear bandit or a ﬁnite-armed bandit based on the outcome when linearity test is cheap
-- ( √ k ∧ d) √ n regret up to log factors
-- MLB: Assume reward $X_t= 〈θ, A_t〉 + η_t + f(A_t)$, $η_t$ is 1-subgaussian noise, $∥f∥_∞ ≤ ε$, Algorithm 12's expected regret with δ = 1/n is $R_n= O dn log(nk) + nε √ d log(n)$
![](https://i.imgur.com/qoxCVGd.png)
Alg12 pf: eliminate low-rewarding arms with high-probability correctness of the conﬁdence intervals.

There are no studies that directly applied Bayesian calibration to RL as far as we know, but studies, but I have found studies dealing with in the context of misspecification and model selection. For example, [Ghosh, 2017                                                                                                                                                                                                                                                                                                                                                                               ](https://arxiv.org/abs/1704.06880), 2017 did not get much response, but it was introduced in Chapter 22.4 of the bandit algorithm textbook, and recently, there is a trend of active research under the names of AISTATS Takemura, 2021 NeurIPS Foster, 2020, misspecified linear contextual bandit, etc. Correspondence model assumption model After the class hypothesis test, it is assumed that "f exists with f(x, a) = E[l_t(a)|x_t = x]" in the previous study by selecting one of the two special/general algorithms (OFUL, UCB) and using it. It is developing into an online oracle concept that has been modified.

From the point of view of fake data introduced earlier, Professor Min Seung-gi's information relaxation thesis, which selects an action based on the future reward sample to prevent overexploration, is also highly relevant. Personally, I am very interested in the bandit algorithm.

- [A Parameter-Free Algorithm for Misspecified Linear Contextual Bandits](http://proceedings.mlr.press/v130/takemura21a/takemura21a.pdf)


3. Is posterior simulator fixed? Is this the same question as "would simulated set \theta always be the same if p(\theta|y) and y are fixed?" For deterministic approximators such as variational inference, where every update is deterministic, it could be fixed. However, for stochastic approximators where hyperparameters like metric M and leapfrog step L described here evolve, I think static form might not be possible.

2. (If answer for Q1.is No) For evolving posterior simulators, how could we formulate this update and where do you think is a nice starting point for this inquiry? Have you seen cases where the (monotone) operator which defines the fixed point also evolves? We could think of a family of operators which share the fixed point; operators are updated within to convergence guarantee or speed accelaration.

3. Could posterior simulator viewed as a policy? From Seungki's paper, A_t = \pi_t(H_{t-1}, \epsilon_t) policy maps history (H_t := (A_s, R_{{A_s},s}) s \in [t]) to action with additional randomness. In SBC context, if we think sample support as arms, what posterior sampler would choose next is determined by 
- A_s past action: which sample it has chosen as it adapts its hyperparameter (metric and leapfrog L) based on its past trajectory.
- R_{{A_s},s} reward: maybe the acceptance ratio of past proposals?
- \epsilon_s randomness: added via sampling procedure.

# Calibration in Thompson sampling
So, I read this and wondered whether we could discuss about the need for predictive distribution instead of posterior distribution
The article's message is to understand interpretability as an object of perception rahter than a design. In this sense, interpretable loss function that could help find the model that has smallest predictive distribution distance between the best model is suggested.

$\pi(\theta) \simeq \int \mathrm{d} \tilde{y} \mathrm{~d} \tilde{\theta} \pi_{\text {approx }}(\theta \mid \tilde{y}) \pi(\tilde{y} \mid \tilde{\theta}) \pi(\tilde{\theta})$ 



The calibration from other fields include:

Calibration uses common sense as an additional information source to test and improve model. The form of common sense could be:
- interval: conﬁdence aligns well with its expected accuracy (eg. sex ratio at birth is around 0.5)
- comparison: error and uncertainty should be higher for out of distribution (OOD) than in distribution data
- self-consistency:
DL: $p\left(\mathbf{y}=k \mid \phi^{\boldsymbol{W}}(\mathbf{x})=\boldsymbol{p}\right)=\boldsymbol{p}_{\boldsymbol{k}}$
Bayesian: $\pi(\theta) = \int \mathrm{d} \tilde{y} \mathrm{~d} \tilde{\theta} \pi(\theta \mid \tilde{y}) \pi(\tilde{y} \mid \tilde{\theta}) \pi(\tilde{\theta})$ 

# recom. ref
[Thompson Sampling with Information Rlaxation Penalties](https://arxiv.org/pdf/1902.04251.pdf)
[An Empirical Evaluation of Thompson Sampling](https://proceedings.neurips.cc/paper/2011/file/e53a0a2978c28872a4505bdb51db06dc-Paper.pdf)
[A Tutorial on Thompson Sampling](https://web.stanford.edu/~bvr/pubs/TS_Tutorial.pdf)
[Text:Bandit Algorithms](https://tor-lattimore.com/downloads/book/book.pdf)
[Meta-Learning Bandit Policies by Gradient Ascent](https://arxiv.org/pdf/2006.05094.pdf)
[Policy Gradient Optimization of Thompson Sampling Policies](https://arxiv.org/abs/2006.16507)
