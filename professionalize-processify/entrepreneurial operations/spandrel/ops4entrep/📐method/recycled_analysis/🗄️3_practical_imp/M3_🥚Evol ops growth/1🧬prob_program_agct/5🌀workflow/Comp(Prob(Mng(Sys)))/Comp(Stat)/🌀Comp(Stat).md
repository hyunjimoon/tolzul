## what
- solution of differential/integral equation
- [[prior(Sense)]], [[prior(Science)]], [[prior(Program)]]. As introduced in [[prior(Sense)]], prior serves the role of uncertainty representation and branching in hierarchical structure. The branching or mixture viewpoint are foundation for multiverse view introduced in Bayesian workflow [paper](https://arxiv.org/pdf/2011.01808.pdf).
- 
## how
- [Prior knowledge elicitation: the past, present, and future](https://arxiv.org/pdf/2112.01380.pdf)
- [Stan Prior Choice Recommendations](https://github.com/stan-dev/stan/wiki/Prior-Choice-Recommendations)

Our goal is prior calibration balancing the tradeoff of two priors
1. [[prior(Science)]]
- [Bayesian duality](https://bayesduality.github.io/#publications) and knowledge prior which use the dual representation of knowledge representation, transfer, collection as exaplained in [this](https://slideslive.com/38959794/kpriors-a-general-principle-of-adaptation?ref=speaker-17205-latest) ICML 2021 lecutre.
- Geometic prior using the symmetry of data structure based on Thm.1 in [[Dual and Twin]]

2. [[prior(Program)]]
- symmetry in simulation-based calibration using Thm2 in [[Dual and Twin]].


## why
1. to **embed** prior knowledge 
2. to allow **exchangeability** (de Finetti theorem)
3. to be open to **extremity**
4. to [**resolve** non-identifiability](https://mc-stan.org/docs/2_29/stan-users-guide/priors-for-identification.html)
5. to **remove** bias
	1. first order correction: bias removal
- Firth (1993) introduced "penalized likelihood" which adds the fisher information term to the likelihood to remove bias. Removing bias and stabilizing is different.
	2. second order correction
6. to regularize i.e. stabilize


References   
- above two Andrew's writing
- Mike's [writing](https://betanalpha.github.io/assets/case_studies/hierarchical_modeling.html) on HM titled "modeling heterogeneity"
- over twenty years of Andrew's quest for "[Prior distributions for variance parameters in hierarchical models](https://streaklinks.com/BJxvGzHqKupVlYdV3A76ScVX/http%3A%2F%2Fwww.stat.columbia.edu%2F~gelman%2Fresearch%2Fpublished%2Ftaumain.pdf?email=hyunji.moonb%40gmail.com)"

