List of pure Bayes lexicon is in https://statmodeling.stat.columbia.edu/2009/05/24/handy_statistic/

2025-01-13

using [🤟lexicon cld](https://claude.ai/chat/d836138a-dfc8-42ed-9f83-d27344425245), 

| Topic                                                | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🤥 **Pinocchio**                                     | • Sin vs exponential growth<br>• Multimodality might be not relevant to your problem<br>• Differentiating stuck chain (adapt_delta .9 to .95) and actual multimodality in posterior<br>• Pinocchio enable "telling"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 🎯 **Dynamic tolerance**                             | • Dynamic aggregation: to prevent gardens of forking path in modeling heterogeneity                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 🔝 **Glass ceiling**                                 | • Wrongly set upper bound of parameter hampering the estimation by cutting off the head                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 🔄 **Loop2Table**                                    | • Using table function as loop's abstraction: functional mapping<br>• Tom is using "parameterize table functions for sensitivity testing" for deer chronic disease aging chain<br>• Relevant to Loop knockout, causal identification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 🌈 **Rainbow**                                       | • Somewhere in between                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 🌊 **Scale free**                                    | • Tom showed me the picture of waterfall<br>• Only nature can produce full fractal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 🦠 **Two ways to improve SIR**                       | • Coflow and SEIR<br>• Screen function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 👨‍🍳 **Cooking Time series for dynamic modeling**   | • 0_PA, 1_PAD, 2_PD, 3_Data4DM, 4_DM4Data<br>• Labeled then unlabeled<br><br>**Description: finding patterns:**<br>• Descriptive<br>• Visualization<br>• Clustering<br>• Latent variable identification & generative approaches<br>• Dimensionality reduction<br>• Causality detection (CCM)<br>• Density estimation<br><br>**Prediction: Identify systemic way to anticipate outcome:**<br>• Regression<br>• Classification<br>• Key: defining loss function and regularization<br><br>**Causal Prediction: Understanding counterfactuals and general behaviors:**<br>• Correlation doesn't imply causation<br>• Seeks to rigorously predict outcomes in accordance w/posited causal structure<br>• Heavy reliance upon postulated causal structure<br>• Can cross-check causal expectations using empirical data<br>• In temporal settings, causal hints can be suggested by empirical data (CCM) |
| [[🔄😲 Pre-Bayesian exchangeability-based surprise]] | • Unexpected discovery of two seemingly unrelated things working well together<br>• Suspicion of hidden/latent parameter connecting them<br>• Example: mRNA platform effectiveness across different domains<br>• Guides research to identify underlying principles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 🧠🤜clever brute force                               | [[CBF]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |


----


## Pinocchio
- sin vs exponential grwoth? 
- multimodality might be not relevant to your problem [image](https://user-images.githubusercontent.com/30194633/195950493-ed6dcc31-823d-4848-bba0-bcd8f55e727f.png)
- differentiating stuck chain (`adapt_delta` .9 to .95) and actual multimodality in posterior ("are you real","if you can't tell, does it matter?" - west world)
- pinocchio enable "telling"

## Dynamic tolerance
- dynamic aggregation: to prevent gardens of forking path in modeling hetereogenity (relevant to Best cluster may not come from clustering)

## Glass ceiling
- wrongly set upper bound of parameter hampering the estimation by cutting off the head

## Loop2Table
- Using table function as loop's abstraction: functional mapping (SW vs base point parameter  
- Tom is also using "parameterize table functions for sensitivity testing" for his deer chronic disease aging chain, but Tom is experiencing parameter's upper bound acting as a ceiling
- relevant to Loop knockout, causal identification as described in 

## Rainbow
- somewhere in between

## Scale free
- Tom showed me the picture of waterfall 
- only nature can produce full fractal

## Two ways to improve SIR: coflow and SEIR 
- screen function

## Cooking Time series for dynamic modeling
- 0_PA, 1_PAD, 2_PD, 3_Data4DM, 4_DM4Data
- labeled then unlabeled

### Description: finding patterns
- descriptive
- visualization
- clustering
- latent variable identification & generative approaches
  - Bayesian (theory-based): HMM, Particle filtering, PMCMC
  - Connectionist (less theory-based): Autoencoders, VAEs, GANs
- Dimensionality reduction (PCA/ICA, t-sne, SVC)
- Causality detection (CCM)
- Density estimation

### Prediction: Identify systemic way to anticipate outcome
- regression
- classification
key: defining loss function and regularization 

### Causal Prediction: Understanding counterfactuals and general behaviors
- correlation doesn't imply causation
- seeks to rigorusly predict outcomes in accordance w/posited causal structure
- advantage
  - capacity to reason about counterfactuals
  - strong generalizability across contexts
  - enhanced explainability
- heavy reliance upon postulated causal structure
- can cross-check causal expectations using empirical data via conditional independence, reverse dependence
- in temporal settings, causal hints can be suggested by empirical data (CCM)

Nathaniel [explains](https://youtu.be/bHzTFLRCMZo) the above as: Description (unsupervised), Prediction (supervised/semi-supervised), Causal prediction (both supervised & unsupervised).

# pre-Bayesian exchangeability-based surprise (methodic doubt)
This idea relates to the unexpected discovery that two seemingly unrelated things work well together, leading to the suspicion of a hidden or latent parameter connecting them. You used the mRNA platform as an example to illustrate this concept. In this context, you likely explained how researchers or companies might have been surprised to find that mRNA technology, initially developed for one purpose, proved effective in multiple, apparently unrelated applications. This surprising effectiveness across different domains led to the hypothesis that there might be an underlying, previously unrecognized parameter or principle (the latent parameter) that explains why the mRNA platform works so well in various contexts. Your comment seems to have been exploring how this type of unexpected discovery can lead to new insights and potentially reshape our understanding of a technology or scientific principle. It also touches on how such surprises can guide further research and development efforts, as investigators try to identify and understand the latent parameters that might explain the observed successes. This idea of "exchangeability-based surprise" appears to be a novel or less common concept that you were introducing or explaining in the context of hierarchical modeling and the development of platform technologies like mRNA.