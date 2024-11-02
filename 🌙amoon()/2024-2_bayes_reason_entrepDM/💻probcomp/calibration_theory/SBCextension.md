---
tags: henry, sensitivity
---



- SBC can be used on the given model,
i) when MCMC is possible: demonstrate calibrated inference for model over a wide variety of possible future datasets.
ii) when MCMC is too slow: test whether the best possible algorithm with feasible computation time is sufficiently accurate.

- Each set of $\{\tilde{\theta_n}, \tilde{y},\hat{\theta}_{1..M}\}_{1..N}$ is approximation of $\pi(\hat{\theta}|\theta = \theta_n)$. M = 25, N = 100000

### 1. Sensitivity 
### Q. Between fixing VS not fixing the other variables, what is the usual protocol for sensitivity analysis of one variable $\theta_1$? I was wondering what effect the high correlation between $\theta_1, \theta_2$ would have on the SBC outcome of one variable, $\theta_1$.

When computing the influence function from your [paper](http://simulation.su/uploads/files/default/2018-lam-qian.pdf), $\frac{\partial E[f(\theta_1, \theta_2)]}{\partial \theta_1 }|_{\theta_{1}=a}$ does $\theta2$ change or fixed?
### 2. computation scale down 

- Do fewer draws from the prior and lots of draws from $\tilde{y}$ for each. sensitivity around a particular $\tilde{\theta}$, while keeping $\tilde{y}$ close to its base value.
- instead of drawing a new $\tilde{y}$ from each $\tilde{\theta}$, draw one, draw an MCMC sample for $\tilde{\theta}$, and then bootstrap or do the IJ. 


![](https://i.imgur.com/y6Uezif.png)

### Q. How could we use this? $\operatorname{Var}(\hat{\theta})=\mathrm{E}[\operatorname{Var}(\hat{\theta} \mid \theta)]+\operatorname{Var}(\mathrm{E}[\hat{\theta} \mid \theta])$

### Q. Does this clash with the fact that y should be simulated once for each rank calculation based on [SBC rank uniformity proof](https://hackmd.io/9dAhuKpwQZyM4OgujggPrQ#SBC-proof)? From the experiment, many pairs of y does not affect beta_binomial but affect normal-normal.

Correct
\begin{aligned} \tilde{\theta} & \sim \pi(\theta) \\ \tilde{y} & \sim \pi(y \mid \tilde{\theta}) \\ \tilde{\theta}_{m}^{\prime} & \sim \pi\left(\theta \mid \tilde{y}\right) \\ r &=\#\left[\tilde{\theta}<\hat{\theta}_{m}\right] \end{aligned}
Incorrect
\begin{aligned} \tilde{\theta} & \sim \pi(\theta) \\ \tilde{y}_{m} & \sim \pi(y \mid \tilde{\theta}) \\ \tilde{\theta}_{m}^{\prime} & \sim \pi\left(\theta \mid \tilde{y}_{m}\right) \\ r &=\#\left[\tilde{\theta}<\hat{\theta}_{m}\right] \end{aligned}
![](https://i.imgur.com/gfLc7EM.png)



Share simulated dataset if every parameter needs 

```{r cars}
# Correct normal_normal
name <- "Correct normal_normal"
ranks <- rep(0, 100)
for (n in 1:N) {
  theta <- rnorm(1, m, s)
  y <- rnorm(1, theta, sigma)
  post_m <- (y * s2 + m * sigma2) / (s2 + sigma2)
  post_s <- sqrt( s2 * sigma2 / (s2 + sigma2) )
  post_theta <- rnorm(M, post_m, post_s)
  ranks[n] <- sum(post_theta < theta)
}
plot_sbc(name, ranks)
print_summary(matrix(ranks))
# Inorrect normal_normal
name <- "Inorrect normal_normal"
ranks <- rep(0, 100)
for (n in 1:N) {
  theta <- rnorm(1, m, s)
  y <- rnorm(M, theta, sigma)
  post_m <- (y * s2 + m * sigma2) / (s2 + sigma2)
  post_s <- sqrt( s2 * sigma2 / (s2 + sigma2) )
  post_theta <- rnorm(M, post_m, post_s)
  ranks[n] <- sum(post_theta < theta)
}
plot_sbc(name, ranks)
print_summary(matrix(ranks))
# Improve inorrect normal_normal
name <- "Improve Inorrect normal_normal"
ranks <- rep(0, 100)
for (n in 1:N) {
  theta <- rnorm(1, m, s)
  y <- rnorm(M, theta, sigma)
  post_m <- (mean(y) * s2 + m * sigma2) / (s2 + sigma2)
  post_s <- sqrt(s2 * sigma2 / (s2 + sigma2) )
  post_theta <- rnorm(M, post_m, post_s)
  ranks[n] <- sum(post_theta < theta)
}
plot_sbc(name, ranks)
print_summary(matrix(ranks))
#rank <- calculate_rank(p, post_p)
#plot_ecdf(ranks, "p")
```
![](https://i.imgur.com/E8TghtG.png)
```{r, echo=FALSE}
# Correct beta_bern
name <- "Correct beta_bern"
a = b = 1
ranks <- rep(0, 100)
for (n in 1:N) {
  p <- rbeta(1, a, b)
  y <- rbernoulli(1, p)
  post_a <- a + sum(y)
  post_b <- b + 1 - sum(y)
  post_p <- rbeta(M, post_a, post_b)
  ranks[n] <- sum(post_p < p)
}

name <- "Incorrect beta_bern"
ranks <- rep(0, 100)
for (n in 1:N) {
  p <- rbeta(1, a, b)
  y <- rbernoulli(M, p)
  post_a <- a + sum(y)
  post_b <- b + M - sum(y)
  post_p <- rbeta(M, post_a, post_b)
  ranks[n] <- sum(post_p < p)
}
plot_sbc(name, ranks)
print_summary(matrix(ranks))

# Correct beta_binom
name <- "Correct beta_binom"
NB <- 10
ranks <- rep(0, 100)
for (n in 1:N) {
  p <- rbeta(1, a, b)
  y <- rbinom(1, NB, p)
  post_a <- a + sum(y)
  post_b <- b + NB - sum(y)
  post_p <- rbeta(M, post_a, post_b)
  ranks[n] <- sum(post_p < p)
}
plot_sbc(name, ranks)

# Incorrect beta_binom
name <- "Incorrect beta_binom"
ranks <- rep(0, 100)
for (n in 1:N) {
  p <- rbeta(1, a, b)
  y <- rbinom(M, NB, p)
  post_a <- a + sum(y)
  post_b <- b + NB * M - sum(y)
  post_p <- rbeta(M, post_a, post_b)
  ranks[n] <- sum(post_p < p)
}
plot_sbc(name, ranks)
```
![](https://i.imgur.com/zIVIHIo.png)

![](https://i.imgur.com/KPguSnE.png)

### Q. which is correct IJ? building on Bayes.IJ from Giordano [repo](https://github.com/rgiordan/StanSensitivity#infinitesimal-jackknife). His [blog](https://rgiordan.github.io/bayes/2020/08/09/bayes_ij.html) states:

1. empirical influence function of a Bayesian posterior expectation can be computed easily from a single run of MCMC samples. 

2. variance is taken over the data
$\operatorname{Var}_{y}(\mathbb{E}[\theta \mid y]) \approx \frac{1}{N} \sum_{n=1}^{N} \psi_{n}^{2}-\left(\frac{1}{N} \sum_{n=1}^{N} \psi_{n}\right)^{2}$

$\psi_{n}:=\left.N \frac{d \mathbb{E}[\theta \mid y, w]}{d w_{n}}\right|_{w_{n}=1}=N \operatorname{Cov}\left(\theta, \ell\left(y_{n} \mid \theta\right)\right)$

IJ1: assume theta ~ N_data * cov(loglik_draws, param_draws) [guess not]
- IJ1.1:  IJ approx in N_theta for loop
- IJ1.2:  IJ approx in N_theta and N_y for loop
IJ2: assume known mean, estimate var with ij_cov 


 
```{r}
N_data = 1 #? (30)
N = 100 prior sample
M = 25 posterior samples per each prior
  
for (n in 1:N) {
  lambda <- rgamma(1, shape, rate)
  y <- rpois(N_data, lambda) 
  y_BS <- sample(y, replace=TRUE, size=N_data)
  sf_IJ <- s_fit(modelName, approxName, data = list(N =N_data, y = y_BS), S = n) # "IJ var captures BS var better"
  loglik_draws <-  select(as_draws_df(sf_IJ$draws(variables = "log_lik")), contains("log_lik"))
  param_draws <- as_draws_df(sf_IJ$draws(variables ="lambda"))$lambda 
  infl_draws_mat <- N_data * cov(loglik_draws, param_draws) #infl_draws_mat scale is  much smaller comparable to lambda
  post_lambda <- infl_draws_mat[,1]
  ranks[n] <- sum(post_lambda< lambda)
}   

# IJ approx in N and M for loop
approxAlg = "IJ1_2"
approxName  = paste0(approxAlg, "_", N,"_", M, "_",N_data)
ranks <- rep(NA, N)
for (n in 1:N) {
  lambda <- rgamma(1, shape, rate)
  y <- rpois(N_data, lambda) 
  for (m in 1:M){
    y_BS <- sample(y, replace=TRUE, size=N_data)
    sf_IJ <- s_fit(modelName, approxName, data = list(N =N_data, y = y_BS), S = n*M + m) # "IJ var captures BS var"
    loglik_draws <-  select(as_draws_df(sf_IJ$draws(variables = "log_lik")), contains("log_lik"))
    param_draws <- as_draws_df(sf_IJ$draws(variables ="lambda"))$lambda
    infl_draws_mat <- N_data * cov(loglik_draws, param_draws) #infl_draws_mat scale is  much smaller comparable to lambda
    post_lambda <- infl_draws_mat[,1]
  }
}   


# IJ assume known mean, estimate var with ij_cov 
approxAlg = "IJ2"
N = 30
M = 20
approxName  = paste0(approxAlg, "_", N,"_", M, "_",N_data)
ranks <- matrix(, nrow = M, ncol = N)

for (n in 1:N) {
  lambda <- rgamma(1, shape, rate)
  y <- rpois(N_data, lambda) 
  for (m in 1:M){
    y_BS <- sample(y, replace=TRUE, size=N_data)
    sf_IJ <- s_fit(modelName, approxName, data = list(N =N_data, y = y_BS), S = n*M + m) # IJ var captures BS var well.
    loglik_draws <- as_draws_df(sf_IJ$draws(variables = "log_lik"))%>%select(1:N_data)
    param_draws <- as_draws_df(sf_IJ$draws(variables ="lambda"))$lambda
    infl_draws_mat <- N_data * cov(loglik_draws, param_draws)
    ij_cov <- cov(infl_draws_mat, infl_draws_mat)
    #assume known mean 
    post_mean = post_shape/post_rate
    post_var = ij_cov
    post_shape_IJ = post_mean^2/post_var
    post_scale_IJ = post_mean/post_var
    post_lambda <- rgamma(L, post_shape_IJ, post_scale_IJ)
    ranks[m, n] <- sum(post_lambda < lambda)
  }
}
```
### 3. multidimensional SBC (if correlation btw parameter matters)
- How to extend 1D SBC to 2D? How can we modify the 1d rank computation?
SBC rank $\sum_{m=1}^{m=M} I({{\theta}_{nm}^{\prime} < \tilde{{\theta}_n}})$ is N-uniform 

 With the given marginal distribution for theta_1 and theta_2, there exist nonunique joint. 


### 4. uniformity measure
R-hat which has a direct interpretation in terms of scale reduction, rather than to frame as a hypothesis test (uniform/nonuniform)

scale reduction statistic which test MCMC convergence:
$\hat{R}[f]=\sqrt{\frac{N-1}{N}+\frac{1}{N} \frac{\hat{B}[f]}{\hat{W}[f]}}$
$\hat{W}[f]=\frac{1}{C} \sum_{c=1}^{C}\left(\mathrm{SE_{MCMC}}_{c}[f]\right)^{2}$
$\hat{B}[f]=\frac{N}{C-1} \sum_{c=1}^{C}\left(\hat{f}_{c, N}^{\mathrm{MCMC}}-\hat{f}\right)^{2}$

