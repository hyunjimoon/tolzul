[[09-29|25-09-29]]
[[3.2 bayesian_calibration]]

abstract: Simulation-based calibration checking (SBC) is a practical method to validate computationally derived posterior distributions or their approximations. In this paper, we introduce a new variant of SBC to alleviate several known problems. Our variant allows the user to in principle detect any possible issue with the posterior, while previously reported implementations could never detect large classes of problems including when the posterior is equal to the prior. This is made possible by including additional data-dependent test quantities when running SBC. We argue and demonstrate that the joint likelihood of the data is an especially useful test quantity. Some other types of test quantities and their theoretical and practical benefits are also investigated. We support our recommendations with numerical case studies on a multivariate normal example and theoretical analysis of SBC, thereby providing a more complete understanding of the underlying statistical mechanisms. From the theoretical side, we also bring attention to a relatively common mistake in the literature and clarify the difference between SBC and checks based on the dataaveraged posterior. The SBC variant introduced in this paper is implemented in the SBC R package.

TEST QUANTITIES ARE DESIRE-DEPENDENT

This study addresses the critical founder-investor alignment challenge by advancing the theoretical framework from **BP|DE** to **BPD|E**. In this context, **BP|DE** represents a scenario where belief and prior functions are variable while desire and environment are fixed, reflecting the basic entrepreneurial state before integration with external stakeholders. Transitioning to **BPD|E**, we integrate desire alongside belief and prior while keeping the environment separate. This framework allows for modeling joint founder-investor preferences but does not yet account for full market dynamics. Through a comprehensive analysis of investor archetypes, we uncover heterogeneity in prior construction, which is the action-oriented encoding of belief. This foundational analysis facilitates the implementation of Bayesian calibration, enabling the modeling of the joint distribution of p(prior|investor_type). By elucidating how variations in investor interpretations influence entrepreneurial decision-making, our research bridges theoretical foundations and algorithmic modeling. The findings contribute to a nuanced understanding of how investor beliefs and actions shape entrepreneurial outcomes in dynamic market environments, offering valuable insights for both practitioners and scholars.

----
sbc citations

#### Aki cites 
- "Modrak proposed in the context of simulation-based calibration checking (SBC) to use non-monotone transformations to improve sensitivity." in [Nabiximols treatment efficiency]( https://users.aalto.fi/~ave/casestudies/Nabiximols/nabiximols.html#model-refinement)
- https://users.aalto.fi/~ave/casestudies/postsbc/postsbc.html#normalmu-1-model
-  However, with finite S this approach doesn’t correctly take into account the discreteness or the effect of correlated sample from Markov chain Gelman ([2017](https://users.aalto.fi/~ave/casestudies/postsbc/postsbc.html#ref-Gelman:correction)).
[[2025-08-01|25-08-01-07]]
