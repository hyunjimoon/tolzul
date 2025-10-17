---
이름: "[contents] BDA Ch. 14 Introduction to regression models"
출생: 2019-03-03
언어교환:
  - bayesian
---

1. Conditional modeling
    1. Notation
    2. Formal Bayesian justification of conditional modeling
2. Bayesian analysis of the classical regression model
    1. Notation and basic model
    2. The standard noninformative prior distribution
    3. The posterior distribution
    4. Conditional posterior distribution of β, given σ
    5. Marginal posterior distribution of σ^2
    6. Comparison to classical regression estimates
    7. Checking that the posterior distribution is proper
    8. Sampling from the posterior distribution
    9. The posterior predictive distribution for new data
    10. Posterior predictive simulation
    11. Analytic form of the posterior predictive distribution
    12. Prediction when X\_tilda is not completely observed
    13. Model checking and robustness
3. Regression for causal inference: incumbency in congressional elections
    1. Units of analysis, outcome, and treatment variables
    2. Setting up control variables so that data collection is approximately ignorable
    3. Implicit ignorability assumption
    4. Transformations
    5. Posterior inference
    6. Model checking and sensitivity analysis
    7. Search for outliers
    8. Posterior predictive checks
    9. Sensitivity of results to the normality assumption
4. Goals of regression analysis
    1. Predicting y from x for new observations
    2. **Causal inference**
    3. Do not control for post-treatment variables when estimating the causal effect
5. Assembling the matrix of explanatory variables
    1. Identifiability and colinearity
    2. Nonlinear relations
    3. Indicator variables
    4. Categorical and continuous variables
    5. Interatctions
    6. Controlling for irrelevant variables
    7. Selecting the explanatory variables
6. Regularization and dimension reduction for multiple predictors
    1. Lasso
7. Unequal variance and correlations
    1. Modeling unequal variances and correlated errors
    2. Bayesian regression with a known covariance matrix
    3. The posterior distribution
    4. Drawing posterior simulations
    5. Prediction
    6. Bayesian regression with unknown covariance matrix
    7. Variance matrix known up to a scalar factor
    8. Weighted linear regression
    9. Parametric models for unequal variances
    10. Drawing posterior simulations
    11. Estimating several unknown variance parameters
    12. Fitting the regression model with two variance parameters
    13. General models for unequal variances
8. Including numerical prior information
    1. Coding prior information on a regression parameter as an extra 'data point'
    2. Interpreting prior information on several coefficients as several additional 'data points'
    3. Prior information about variance parameters
    4. Prior information in the form of inequality constraints on parameters
9. Bibilographic note
10. Excercises

**Linear regression**

Bayesian linear regression, computations of linear regression, including QR decomposition, Bayesian graphical regression model

**Elections example**

can frame the problem using a hierarchical model

**Lasso regression**

Tibshirani (1996) as a way to estimate a large number of parameters so that, with sparse data, many of the coefficients will be estimated at zero

Bayesian lasso:

Park and Casella (2008) using MCMC computation

Seeger (2008) expectation propagation

Carvalho, Polson, and Scott (2010) horseshoe distribution, a continuous Cauchy mixture model of normal distributions, as a hierarchical prior distribtuion for regression coefficients

Polson and Scott (2012) shrinkage priors

Arminger (1998), Murray et al. (2013) and Hoﬀ and Niu (2012) consider models for latent structured covariance matrices that can be viewed as dimension-reduction techniques

**Parametric models for unequal variances**

Boscardin and Gelman (1996) present references and an example with forecasting Presidental elections

**Correlation models** 

Box and Jenkins (1976), Brillinger (1981), and Pole, West, and Harrison (1994) for time series analysis

Kunsch (1987) and Cressie (1993) for spatial statistics, and Mugglin, Carlin, and Gelfand (2000) and Banerjee, Carlin, and Gelfand (2004) for space-time models
