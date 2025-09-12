
from hyunjimoon on 2024-09-01T17:57:37Z
![[Pasted image 20241123161619.png]]

effect of three axes are summarized from 
### Performance Metric (Online to Offline)

min_π E[R_T(π)] → max_i P(i = i* | D_N)

This axis represents a shift from online performance (minimizing expected regret over T rounds) to offline identification (maximizing the probability of correctly identifying the best option after N samples). The left side represents the online setting where we minimize the expected regret R_T(π) of a policy π over T rounds. The right side represents the offline setting where we maximize the probability of correctly identifying the best option i* given a fixed dataset D_N.

### Modeling Technique (Frequentist to Bayesian):

θ̂ = argmax_θ L(θ; D) → p(θ | D) ∝ L(θ; D) p(θ)

This axis represents a transition from frequentist point estimates to Bayesian posterior distributions. The left side shows the frequentist approach, where we find the point estimate θ̂ that maximizes the likelihood L(θ; D) given the data D. The right side shows the Bayesian approach, where we compute the posterior distribution p(θ | D) proportional to the product of the likelihood L(θ; D) and the prior p(θ).

### Interaction (Independent to Correlated):

p(x_1, ..., x_n) = ∏_i p(x_i) → p(x_1, ..., x_n) = p(x_1) ∏_i p(x_i | x_1, ..., x_{i-1})

This axis represents a shift from independent to correlated models. The left side shows the independence assumption, where the joint probability of variables x_1 to x_n is the product of their individual probabilities. The right side shows a correlated model, where each variable depends on all previous variables, expressed as a product of conditional probabilities. This progression often involves moving from simple independent models to more complex models that capture correlations, such as Gaussian Processes or graphical models.



| Axis                                                       | Simplest → Complex (Mathematical Change)                                | Symbol Definitions                                                                                                                                                                                                                                                                                                                                          |   |  
| ---------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| Performance Metric (Online to Offline)                     |                                                                         |                                                                                                                                                                                                                                                                                                                                                             |     |
| 1. Thompson → Best arm id. in Beta-Bernoulli bandits       | argmax_t E[r_t\|H_t] → argmax_i P(μ_i = max_j μ_j \| D_N)               | In Thompson Sampling, we select the arm t that maximizes the expected reward r_t given the history H_t at each step. In Best Arm Identification, we identify the arm i that has the highest probability of being the best after N fixed samples, where μ_i is the true mean of arm i and D_N is the collected data.                                         |     |
| 2. Bandits → Best arm id.                                  | min_π E[∑_t=1^T (μ* - μ_π(t))] → max_i P(i = argmax_j μ_j \| D_N)       | In the bandit setting, we minimize the expected regret over T rounds, where π is the policy, μ* is the optimal arm's mean, and μ_π(t) is the mean of the chosen arm at time t. In Best Arm Identification, we maximize the probability of correctly identifying the best arm i after N samples, where μ_j are the true means and D_N is the collected data. |     |
| 3. X-armed linear bandits → Best arm id. in linear bandits | argmax_x∈X θ^T x → argmax_i∈{1,...,K} P(θ^T x_i = max_j θ^T x_j \| D_N) | In X-armed linear bandits, we choose x from a continuous set X to maximize the linear reward θ^T x. In linear best arm identification, we find the arm i among K discrete arms with the highest probability of having the maximum reward, given the data D_N. θ is the unknown parameter vector, and x_i are the feature vectors of the arms.               |     |
| 4. BO analysis → BayesOpt                                  | E[f(x)\|D_n] → argmax_x α(x\|D_n)                                       | In Bayesian Optimization analysis, we compute the expected value of f(x) given data D_n. In BayesOpt, we actively seek the x that maximizes the acquisition function α(x\|D_n), which balances exploration and exploitation based on the posterior distribution.                                                                                            |     |
| Modeling Technique (Frequentist to Bayesian)               |                                                                         |                                                                                                                                                                                                                                                                                                                                                             |     |
| 1. Bandits → Thompson                                      | argmax_i μ̂_i → argmax_i θ_i, where θ_i ~ p(θ_i\|D_t)                   | In frequentist bandits, we choose the arm i with the highest estimated mean μ̂_i. In Thompson Sampling, we sample θ_i from the posterior distribution p(θ_i\|D_t) given data D_t, and choose the arm with the highest sampled value.                                                                                                                        |     |
| 2. X-armed linear bandits → BO analysis                    | y = θ^T x + ε → f(x) ~ GP(m(x), k(x,x'))                                | X-armed linear bandits model the reward y as a linear function of x with parameters θ and noise ε. BO analysis models the function f(x) as a Gaussian Process with mean function m(x) and covariance function k(x,x').                                                                                                                                      |     |
| 3. Best arm id. → Best arm id. in Beta-Bernoulli bandits   | [μ̂_i - ε, μ̂_i + ε] → Beta(α_i, β_i)                                   | Frequentist approach uses confidence intervals [μ̂_i - ε, μ̂_i + ε] for each arm's mean. Bayesian approach models each arm's mean with a Beta distribution with parameters α_i and β_i.                                                                                                                                                                     |     |
| 4. Best arm id. in linear bandits → BayesOpt               | argmax_i x_i^T θ̂ → argmax_x [μ(x) + β σ(x)]                            | In linear bandits, we choose the arm i with the highest estimated reward x_i^T θ̂. In BayesOpt, we maximize the acquisition function, typically of the form μ(x) + β σ(x), where μ(x) is the posterior mean, σ(x) is the posterior standard deviation, and β is an exploration parameter.                                                                   |     |
| Interaction (Independent to Correlated)                    |                                                                         |                                                                                                                                                                                                                                                                                                                                                             |     |
| 1. Bandits → X-armed linear                                | r_i ~ P(r\|i) → r(x) = θ^T x + ε                                        | In classic bandits, rewards r_i for each arm i are drawn independently. In X-armed linear bandits, the reward r(x) is a linear function of the arm's features x, with unknown parameters θ and noise ε.                                                                                                                                                     |     |
| 2. Thompson → BO analysis                                  | p(θ_i) = Beta(α_i, β_i) → f(x) ~ GP(m(x), k(x,x'))                      | Thompson Sampling uses independent Beta distributions for each arm's parameter θ_i. BO analysis uses a Gaussian Process to model the function f(x), introducing correlations via the kernel k(x,x').                                                                                                                                                        |     |
| 3. Best arm id. → Best arm id. in linear bandits           | ∏_i P(μ_i ∈ [μ̂_i - ε_i, μ̂_i + ε_i]) → P(θ ∈ C_δ) ≥ 1 - δ              | In classic best arm id., we use independent confidence intervals for each arm's mean μ_i. In linear bandits, we use a confidence ellipsoid C_δ for the parameter vector θ, with confidence level 1 - δ.                                                                                                                                                     |     |
| 4. Best arm id. in Beta-Bernoulli bandits → BayesOpt       | p(μ_1,...,μ_K) = ∏_i Beta(α_i, β_i) → f(x) ~ GP(m(x), k(x,x'))          | Beta-Bernoulli bandits use independent Beta distributions for each arm's mean μ_i. BayesOpt uses a Gaussian Process to model the function f(x), introducing spatial correlation via the kernel k(x,x').                                                                                                                                                     |     |

---

## Reply from hyunjimoon on 2024-09-01T17:59:12Z

@jeanbaptiste you might be interested in the above - could you explain more on your discovery of different tribes/origin/user group of optimization and bayesian?

---


[Discussion link](https://github.com/Data4DM/BayesSD/discussions/248)
