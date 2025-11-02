---
collection:
- '[[People]]'
field:
- 🐅cba
- 👾cog
atom: 🧭atom(PCO🔃)
created: '2022-09-26'
---

## 0926
q. full flow info ~ full stock info?? (no; stock involve accumulation)
do we need to care whether the variance increase or decrease? (lognormal likelihood)
- homogeneous with purely synthetic data (dgp1, dgp2, ... -> "Y" -> estimated parameter (lambda, alpha) mea)
- bias or large interval
- f(x)
- generate with: RANDOM NORMAL( 0, 2, 1, Prod Start Measurement Noise Scale , Noise Seed )*Production Start Rate
- estimating: (Production Start Rate Measured Data-Production Start Rate)^2/MAX(Min Err,Production Start Measurement Noise Scale
*Production Start Rate Measured Data)^2
- ![[Pasted image 20220926084045.png]]

- gamma vs exp
![[Pasted image 20220926102557.png]]

1. stocks as lognormal is too fat-tailed, changing to neg_binom?
- [difference btw neg-binom and lognormal](https://stats.stackexchange.com/questions/233881/how-is-a-negative-binomial-regression-model-different-from-ols-with-a-logged-out) (floor,)
- related to exp_brownian motion and conditional poisson process ()
- process version of mixture distribution in this general setting (Poisson and Gamma distributions) is always a Negative Binomial random variable with parameters given by r = α and β = θ.


```- e1, e2 추정 
- s1, s2 관찰 
- subscript firm: f1, f2 
- 30days
4 time series vector, estimate 4 (two for each e1[firm], e2[firm] firm = f1, f2) (scalar)

1. _gen model and _est model

2. _gen model s1[firm], s2[firm] -> 30*4 shape df_obs

3. measurement
_est model vesim_ode_func, `df_gen` mean, dispersion α
target += negbinom2_lpdf (df_obs|df_gen, α) 

4. prior regularization 
target += negbinom2_lpdf(α| log(.1), .1)

target += normal_lpdf(e1| e1_mean, e1_sd) 

target += normal_lpdf(e1_mean| 2, .1) 

target += lognormal_lpdf(e1_sd| log(2), .01) 

```

2. hierarchical, between aggregation and disaggregation
- estimation of hierarchical model 

"[what we learned from hierarchical model 'estimator' can be of help in the designing step. For instance, imagine a framework where the outcome of estimation informs whether which out of 30 local parameter can be moved to G (Global: 46 + Local:30).](https://github.com/hyunjimoon/DataInDM/commit/97197bde56b6fe19e358fd64b3a8198e33de7715#r78780350)"

- between agent-based and compartment model (Nathaniel agreed, checking with Andrew)

- could this affect sampling methods? (gibbs sampling?)
- conditional poisson process (non-indep) and negative binomial (mixture) recitation slide comparing [[TA-StochasticModeling_Yao]]
- 

3. SIR model
- constant value performs well (bc Re ~ 1)? 
- acuity?
- 

bm, martingale, variance grows over time

random draw from beta then run stella with fixed beta value

time variant, normal distribution

process noise

constant demand + step function can create osciltion
 