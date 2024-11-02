#finance #calibration #copula #verification

# Finance Calibration


[Calibrating and Simulating Copula Functions in Financial Applications](https://www.frontiersin.org/articles/10.3389/fams.2021.642210/full)
[Extending approximate Bayesian computation methods to high dimensions via a Gaussian copula model](https://econpapers.repec.org/article/eeecsdana/v_3a106_3ay_3a2017_3ai_3ac_3ap_3a77-89.htm)

high dim: 
- marginal adjustment
- extended using Gaussian copula approximation. 
- 1) estimates bivariate posterior for each pair of parameters separately using a 2-dimensional Gaussian copula
- 2) combines these estimates together to estimate the joint posterior
- separately matching many low-dimensional vectors to form the copula approximation instead of simultaneously matching high-dimensional vector
- :( non-linear dependencies, complex higher-order relationships between 3 parameters in the full posterior π(θ | s obs ) will not be accurately captured
- :) accurately fitted Gaussian copula approximation to a highly complex posterior is useful than a poor standard ABC approximation to the joint model
### [An Introduction to Copulas](http://www.columbia.edu/~mh2078/QRM/Copulas.pdf)

- isolate dependency structure in a multivariate distribution
- Sklar’s Theorem and the Frechet-Hoeffding bounds
- important topic of model risk
- #q correlation between two neighboring model
	- dependency structure
	- what information does highly related models give us?
	- 
- ![[Pasted image 20210729171240.png]]
- ecdf()

![](https://i.imgur.com/6D5R7MO.png)
Among the risk measures defined above, the following two are widely used. Percentaile and the conditional expectation are concepts well-respresented with samples and monte-carlo sampling.

$VaR_\alpha (X) = -inf {\{ x \in R| F_x(x) > \alpha} = F_X(x) > \alpha \} = F_Y^{-1}(\alpha)$
$CVaR_\alpha(X) = E[-X| -X > VaR_\alpha (X)]$. 

![](https://i.imgur.com/MqzSRiF.png)
![](https://i.imgur.com/O19jXse.png)



time horizon, credible level, 
```{python}
def mcVaR(return, alpha = 5):
    return np.percentile(returns, alpha)
def mcCVaR(returns, alpha = 5):
    belowVar = returns <= mcVaR(return, alpha)
    return returns[belowVar].mean()
```
Calculation mtds:

#cbs
## Bayes Finance textbook
- 리스크모형은 리스크사 상의 발생과 손실액을 확률변수들로 간주하고 그 확률분포들을 기술


#cvar #aumentation
## Risk-sensitive Optimal Execution via a Conditional Value-at-Risk Objective
- form closed form dp sol and compare w/ static
- state-space augmentation
- trading algorithm provides the best allocation of trading effort to minimize the cost of traidng give a liquidation task/ mean-variance tradeoff
- optimal action at some point in time may not be completely determined by the current state of the MDP, but may depend on the entire history
- two types of augmentation: extra state variable for running cost and quantile value

- CVaR MDP uses #MRT of CVaR objective + game-theory #representation + Markov policies on augmented state space

## Statistical models and stochastic optimization in ﬁnancial technology and investment science
- cloud computing, blockchain, #fintech
- high freq. trading, latency of a strategy.
- ﬁnancial systems have long operated on the basis of trust, for which banks and governments have served to provide #topdown control of monetary value. #bottomup “trust machines” emerging through blockchain
- #eg why verification is important in finance: 
- duplicate checks
```
As trading decisions are made at split-second intervals, the task of ensuring that the algorithm and the infrastructure are error-free in a HFT ﬁrm pertains to both software engineering and LOB analytics. Trading algorithms are required to undergo multiple stages of testing and certiﬁcation, with duplicate checks in place. Seemingly inconspicuous bugs such as integer overﬂow or underﬂow could have a signiﬁcant impact on the strategy. Operational risk in this context mainly refers to the risk stemming from infrastructure disruptions and software bugs. A case in point was the 2012 software error of the Knight Capital Group that deployed on August 1 untested software, which contained an obsolete function because a technician forgot to copy the new code to one of its servers for automated routing of equity orders. This caused major disruption in stock prices within 45 minutes and a pre-tax cost of $440 million and subsequent drop of over 70% of the company’s stock price. On August 5, 2012, Knight Capital raised about $400 million from several major investors to stay in business. It was subsequently acquired by the Global Electronic Trading Company (Getco LLC).
```
- Blockchain: real-time gross settlement, or ﬁnancial transactions veriﬁcation: probablistic outperform deterministic
- Cryptosystems: stream + block cipher
#finance #calibration #copula #verification


--
alias: 
--

# Finance Calibration
- equilibrium checker. blockchain, copula



[Calibrating and Simulating Copula Functions in Financial Applications](https://www.frontiersin.org/articles/10.3389/fams.2021.642210/full)
[Extending approximate Bayesian computation methods to high dimensions via a Gaussian copula model](https://econpapers.repec.org/article/eeecsdana/v_3a106_3ay_3a2017_3ai_3ac_3ap_3a77-89.htm)

high dim: 
- marginal adjustment
- extended using Gaussian copula approximation. 
- 1) estimates bivariate posterior for each pair of parameters separately using a 2-dimensional Gaussian copula
- 2) combines these estimates together to estimate the joint posterior
- separately matching many low-dimensional vectors to form the copula approximation instead of simultaneously matching high-dimensional vector
- :( non-linear dependencies, complex higher-order relationships between 3 parameters in the full posterior π(θ | s obs ) will not be accurately captured
- :) accurately fitted Gaussian copula approximation to a highly complex posterior is useful than a poor standard ABC approximation to the joint model
### [An Introduction to Copulas](http://www.columbia.edu/~mh2078/QRM/Copulas.pdf)

- isolate dependency structure in a multivariate distribution
- Sklar’s Theorem and the Frechet-Hoeffding bounds
- important topic of model risk
- #q correlation between two neighboring model
	- dependency structure
	- what information does highly related models give us?
	- 
- ![[Pasted image 20210729171240.png]]
- ecdf()

![](https://i.imgur.com/6D5R7MO.png)
Among the risk measures defined above, the following two are widely used. Percentaile and the conditional expectation are concepts well-respresented with samples and monte-carlo sampling.

$VaR_\alpha (X) = -inf {\{ x \in R| F_x(x) > \alpha} = F_X(x) > \alpha \} = F_Y^{-1}(\alpha)$
$CVaR_\alpha(X) = E[-X| -X > VaR_\alpha (X)]$. 

![](https://i.imgur.com/MqzSRiF.png)
![](https://i.imgur.com/O19jXse.png)



time horizon, credible level, 
```{python}
def mcVaR(return, alpha = 5):
    return np.percentile(returns, alpha)
def mcCVaR(returns, alpha = 5):
    belowVar = returns <= mcVaR(return, alpha)
    return returns[belowVar].mean()
```
Calculation mtds:

#cbs
## Bayes Finance textbook
- 리스크모형은 리스크사 상의 발생과 손실액을 확률변수들로 간주하고 그 확률분포들을 기술


#cvar #aumentation
## Risk-sensitive Optimal Execution via a Conditional Value-at-Risk Objective
- form closed form dp sol and compare w/ static
- state-space augmentation
- trading algorithm provides the best allocation of trading effort to minimize the cost of traidng give a liquidation task/ mean-variance tradeoff
- optimal action at some point in time may not be completely determined by the current state of the MDP, but may depend on the entire history
- two types of augmentation: extra state variable for running cost and quantile value

- CVaR MDP uses #MRT of CVaR objective + game-theory #representation + Markov policies on augmented state space

## Statistical models and stochastic optimization in ﬁnancial technology and investment science
- cloud computing, blockchain, #fintech
- high freq. trading, latency of a strategy.
- ﬁnancial systems have long operated on the basis of trust, for which banks and governments have served to provide #topdown control of monetary value. #bottomup “trust machines” emerging through blockchain
- #eg why verification is important in finance: 
- duplicate checks
```
As trading decisions are made at split-second intervals, the task of ensuring that the algorithm and the infrastructure are error-free in a HFT ﬁrm pertains to both software engineering and LOB analytics. Trading algorithms are required to undergo multiple stages of testing and certiﬁcation, with duplicate checks in place. Seemingly inconspicuous bugs such as integer overﬂow or underﬂow could have a signiﬁcant impact on the strategy. Operational risk in this context mainly refers to the risk stemming from infrastructure disruptions and software bugs. A case in point was the 2012 software error of the Knight Capital Group that deployed on August 1 untested software, which contained an obsolete function because a technician forgot to copy the new code to one of its servers for automated routing of equity orders. This caused major disruption in stock prices within 45 minutes and a pre-tax cost of $440 million and subsequent drop of over 70% of the company’s stock price. On August 5, 2012, Knight Capital raised about $400 million from several major investors to stay in business. It was subsequently acquired by the Global Electronic Trading Company (Getco LLC).
```
- Blockchain: real-time gross settlement, or ﬁnancial transactions veriﬁcation: probablistic outperform deterministic
- Cryptosystems: stream + block cipher

![[Pasted image 20210918154638.png]]