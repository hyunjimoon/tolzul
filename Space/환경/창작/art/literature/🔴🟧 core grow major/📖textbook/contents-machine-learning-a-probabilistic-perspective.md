---
이름: "[contents] Machine Learning A Probabilistic Perspective"
출생: 2019-02-20
언어교환:
  - bayesian
---

1. Introduction
2. Probability
3. Generative models for discrete data
4. Gaussian models
5. Bayesian statistics
6. Frequentist statistics
7. Linear regression
8. Logistic regression
9. Generalized linear models and the exponential family
10. Directed graphical models (Bayes nets)
11. Mixture models and the EM algorithm
12. Latent linear models
13. Sparse linear models
14. Kernels
15. Gaussian processes
16. Adaptive basis function models
17. Markov and hidden Markov models
18. State space models
19. Undirected graphical models (Markov random fields)
20. Exact inference for graphical models
21. Variational inference
22. More variational inference
23. Monte Carlo inference
24. Markov chain Monte Carlo (MCMC) inference
25. Clustering
26. Graphical model structure learning
27. Latent variable models for discrete data
28. Deep learning

 

1. Introduction
    1. Machine Learning: what and why?
    2. Supervised learning
    3. Unsupervised learning
    4. Some basic concepts in machine learning
2. Probability
    1. Introduction
    2. A brief review of probability theory
    3. Some common discrete distributions
    4. Some common continuous distributions
    5. Joint probability distributions
    6. Transformation of random variables
    7. Monte Carlo approximation
    8. Information theory
3. Generative models for discrete data
    1. Introduction
    2. Bayesian concept learning
    3. The beta-binomial model
    4. The Dirichlet-multinomial model
    5. Naive Bayes classifier
4. Gaussian models
    1. Introduction
    2. Gaussian discriminant analysis
    3. Inference in jointly Gaussian distributions
    4. Linear Gaussian systems
    5. Digression: The Wishart distribution
    6. Inferring the parameters of MVN
5. Bayesian statistics
    1. Introduction
    2. Summarizing posterior distributions
    3. Bayesian model selection
    4. Priors
    5. Hierachical Bayes
    6. Empirical Bayes
    7. Baeysian decision theory
6. Frequentist statistics
    1. Introduction
    2. Sampling distribution of an estimator
    3. Frequentist decision theory
    4. Desirable properties of estimators
    5. Empirical risk minimization
    6. Pathologies of frequentist statistics
7. Linear regression
    1. Introduction
    2. Model specification
    3. Maximum likelihood estimation (least squares)
    4. Robust linear regression
    5. Ridge regression
    6. Bayesian linear regression
8. Logistic regression
    1. Introductions
    2. Model specification
    3. Model fitting
    4. Bayesian logistic regression
    5. Online learning and stochasitc optimization
    6. Generative vs discriminative classifiers
9. Generalized linear models and the exponential family
    1. Introduction
    2. The exponential families
    3. Generalized linear models (GLMs)
    4. Probit regression
    5. Multi-task learning
    6. Generalized linear mixed models
    7. Learning to rank
10. Directed graphical models (Bayes nets)
    1. Introduction
    2. Exmples
    3. Inference
    4. Learning
    5. Conditional indepence properties of DGMs
11. Mixture models and the EM algorithm
    1. Latent variable models
    2. Mixture models
    3. Parameter estimation for mixture models
    4. The EM algorithm
    5. Model selection for latent variable models
    6. Fitting models with missing data
12. Latent linear models
    1. Factor analysis
    2. Principal components analysis (PCA)
    3. Choosing the umber of latent dimensions
    4. PCA for categorical data
    5. PCA for paired and multi-view data
    6. Independent Component Analysis (ICA)
13. Sparse linear models
    1. Introduction
    2. Bayesian variable selection
    3. L1 regularization: basics
    4. L1 regularization: algorithms
    5. L1 regularization: extensions
    6. Non-convex regularizers
    7. Automatic relevance determination (ARD)/sparse Bayesian learning (SBL)
    8. Sparse coding
14. Kernels
    1. Introduction
    2. Kernel functions
    3. Using kernels inside GLMs
    4. The kernel trick
    5. Support vector machines (SVMs)
    6. Comparison of discriminative kernel methods
    7. Kernels for building generative models
15. Gaussian processes
    1. Introduction
    2. GPs for regression
    3. **GPs meet GLMs**
    4. Connection with other methods
    5. GP latent variable model
    6. Approximation methods for large datasets
16. Adaptive basis function models
    1. Introduction
    2. Classification and regression trees (CART)
    3. Generalized additive models
    4. Boosting
    5. Feedforward neural networks (multilayer perceptrons)
    6. Ensemble learning
    7. Experimental comparison
    8. Interperting black-box models
17. Markov and hidden Markov models
    1. Introduction
    2. Markov models
    3. Hidden Markov models
    4. Inference in HMMs
    5. Learning for HMMs
    6. Generalizations of HMMs
18. State space models
    1. Introduction
    2. Application of SSMs
    3. Inference in LG-SSM
    4. Learning for LG-SSM
    5. Approximate online infernce for non-linear, non-Gaussian SSMs
    6. Hybrid discrete/continuous SSMs
19. Undirected graphical models (Markov random fields)
    1. Introduction
    2. Conditional independence properties of UGMs
    3. Parameterization of MRFs
    4. Examples of MRFs
    5. Learning
    6. Conditional random fields (CRFs)
    7. Structural SVMs
20. Exact inference for graphical models
    1. Introduction
    2. Belief propagation for trees
    3. The variable elimination algorithm
    4. The junction tree algorithm
    5. Computational intractability of exact inference in the worst case
21. Variational inference
    1. Introduction
    2. Variational inference
    3. The mean field method
    4. Structured mean field
    5. Variational Bayes
    6. Variational Bayes EM
    7. Variational message passing and VIBES
    8. Local variational bounds
22. More variational inference
    1. Introduction
    2. Loopy belief propagation: algorithmic issues
    3. Loopy belief propagationl: theoretical issues
    4. Extensions of belief propagation
    5. Expectation propagation
    6. MAP state estimation
23. Monte Carlo inference
    1. Introduction
    2. Sampling from standard distributions
    3. Rejection sampling
    4. Importance sampling
    5. Particle filtering
    6. Rao-Blackwellised particle filtering (RBPF)
24. Markov chain Monte Carlo (MCMC) inference
    1. Introduction
    2. Gibbs sampling
    3. Metroplis Hastings algorithm
    4. Speed and accuracy of MCMC
    5. Auxiliary variable MCMC
    6. Annealing methods
    7. Approximationg the marginal likelihood
25. Clustering
    1. Introduction
    2. Dirichlet process mixture models
    3. Affinity propagation
    4. Spectral clustering
    5. Hierarchical clustering
    6. Clustering datapoints and features
26. Graphical model structure learning
    1. Introduction
    2. Structure learning for knowledge discovery
    3. Learning tree structures
    4. Learning DAG structures
    5. Learning DAG structure with latent variables
    6. Learning causal DAGs
    7. Learning undirected Gaussian graphical models
    8. Learning undirected discrete graphical models
27. Latent variable models for discrete data
    1. Introduction
    2. Distributed state LVMs for discrete data
    3. Latent Dirichlet allocation (LDA)
    4. Extensions of LDA
    5. LVMs for graph-sructured data
    6. LVMs for relational data
    7. Restricted Boltxmann machines (RBMs)
28. Deep learning
    1. Introduction
    2. Deep generative models
    3. Deep neural networks
    4. Application of deep networks
    5. Discussion
