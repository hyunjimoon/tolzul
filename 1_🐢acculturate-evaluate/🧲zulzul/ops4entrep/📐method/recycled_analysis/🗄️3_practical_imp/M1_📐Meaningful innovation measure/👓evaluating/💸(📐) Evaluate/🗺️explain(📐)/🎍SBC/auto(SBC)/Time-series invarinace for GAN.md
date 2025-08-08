### Finding metric in seasonality coefficient space that corresponds to `E_z[1-D2(G(z))]`

$$
\begin{align}
y = X \beta \\
\beta_{prior} \sim N(0, \lambda) \\
\beta_{posterior} \sim X(X'X + \lambda I)^{-1} y
\end{align}
$$
cannot summarize as 1D (e.g. season(X) -> 10/10+1 , season(X_tilde) -> 6/(5+6)) due to a.

> dist(beta_vec, beta_tilde_vec) 

* difference between image and time series data:
a. contrary to score function of connectedness, ratio of the main cannot differentiate 10/11 W and M i.e. $\beta_{w}/(\beta_{w} + \beta_{m})$ vs $\beta_{m}/(\beta_{w} + \beta_{m})$
- which prior could be given 
tuning parameter (=prior parameter) = lambda
beta_posterior
beta_tilde_posterior



Part 1
MLE의 점근적 성질
empirical Bayes estimator 장점소개 (Jame-Stein, shrikage)
1. MLE보다 항상 더 적은 MSE
2. 베이즈 해석을 가진 estimator를 plug-in방식으로 활용가능 

덧) shrikage는 partial pooling으로 no-pooling과 complete pooling의 가중

Part 2
- Random effects model 
- application: smoothing spline
