tags: #decision #calibration`

[[mike_betancourt]]
Goal: Apply Bayesian calibration to Bayesian decision theory and to find its application
# Introduction to Bayesian calibration
## 1. Inference
### 1.1 Previous <s>calibration</s> inference
$$
\text{Given the observation model}  \;p_1(y|\theta),\\
$$

$$
\underset{\theta} {min} \; div(p_1(\tilde{y}|\theta), p(y_{obs}))\
$$
*$divg()$ : divergence

Disadvantage
i) structural inability to separate epistemic (E) uncertainty form aleatoric (A) during calibratiton as it assumes no uncertainty exists in real world data; excluding modeling errors could make conventional calibration methods amplify model output uncertainty if data is biased (Muehleisen)

ii) inseparable contribution of each parameter on failed test 

iii) can overfit

### 1.2. Bayesian <s>calibration</s> inference
$$\text{Given the observation model and prior}  \;p_1(y|\theta), p(\theta)(=\pi)$$
Bayesian update's loss function is $L(\nu; \pi, y) = \int l(\theta,y)$ $\nu (d \theta)$ + $d_{KL}(\nu, \pi)$ with  $l(\theta ; y_1, \ldots, y_n)=-\sum_{i=1}^n \log \{p_1(y_i |\theta)\}$

which returns
$$\begin{aligned} \hat{\nu}(\theta) &=\arg \min _{\nu} L(\nu ; \pi, y) \\ &=\frac{\exp \{-l(\theta, y)\} \pi(\theta)}{\int \exp \{-l(\theta, y)\} \pi(\mathrm{d} \theta)} \end{aligned}$$

- Bayesian update corresponds to minimizing the KL-regularized total-log loss over all distribution from [Bissiri13](https://rss.onlinelibrary.wiley.com/doi/full/10.1111/rssb.12158) which introduces general, axiomatic treatment that shows to extend the idea to other losses
- Along with the likelihood conditional on certain distribution over $\theta$, a term that measures the distance between assumed distribution and a given prior is required. This explains why formulations such as the following which lacks its distance from the prior are incorrect. 
$\underset{p(\theta)} {max} \; \int \; p_1(y_{test}|\theta)p(\theta)d\theta \text{   or  }\underset{p(\theta)} {min} \; \int \; div(p_1(\tilde{y}|\theta), p(y_{test}))p(\theta)d\theta$
-  distribution over the parameter other than  need determine the most likely input parameter  **uncertainty** $p(\theta)$ that yield observed data's output, **uncertainty** $y_{test}$
- prior term acts as a regularizing term
- uncertainty is included in its result enabling further update: starting from a crude uniform or triangular prior, parameter distribution is iteratively updated to customized and empirical form
- different from popular optimization methods; (but interpretation of measure optimization could be possible)



## 2. Bayesian Calibration

 In Bayesian calibration, ground truth itself and the simulated results from it are compared for model diagnose and update.
 
$\tilde{\theta} \sim \pi_{S}(\theta)$
$\tilde{y} \sim \pi_{S}(y \mid \tilde{\theta})$
$\tilde{U}=U(a(\tilde{y}), \tilde{\theta})$
To be specific, repeatedly simulating model configurations from the prior distribution, observations from the corresponding data generating process, running our analysis to completion, and then scrutinizing the resulting likelihood functions, posterior distributions, and decision outcomes in the context of the simulated ground truth.

The compared results tell how decision making process is within the scope of the modeling assumptions. The utility $U(a(y), \theta)$ and action $a(y)$ are defined specific to diverse problems including prediction, posterior, computation algorithm etc  ([Betancourt, 2019](https://betanalpha.github.io/assets/case_studies/modeling_and_inference.html#33_bayesian_calibration)). This [newly](https://hackmd.io/HqHLMaGmQvOE0mQJ_5bcDw#Definition-Best-self-consistent-measure-SCM) proposed workflow uses this Bayesian calibration spirit as well.

- bootstrapping model development, since the improvement happens based on repeated fake-data simulation without the use of any real-data; initial crude model is calibrated by iterating simulate-then-compare. These calibrations can identify the limitations of that model and inform improvements such as more sophisticated observational models, more precise domain expertise, or even more robust methods for computing expectations.

- simulate-then-compare with $\bar U_{\mathrm{S}}=\int \mathrm{d} y \mathrm{~d} \theta \pi_{\mathrm{S}}(y, \theta) U(a(y), \theta)$ is the engine for calibration where the model configuration ($\pi_s(y, \theta)$) and $\theta$-divergence ($U$) need to be defined in advance

- one disadvantage is that improvement guidelines are not always clear, but [Yao18](https://arxiv.org/pdf/1802.02538.pdf) shows one example on improving approximate compuatation. This motivates [this](https://hackmd.io/HqHLMaGmQvOE0mQJ_5bcDw#Overview-and-example) research to substitute the original "iterating simulate-then-compare" with "calibrate-then-choose".

-   for simulation and utility is needed to measure the difference used to compare  the expected performance of the model we constructed; utility function U and model configuration are needed


- relate prior information with uncertainty to future information based on the likelihood of observed outptut
### 2.1  Kennedy [Bayesian calibration of computer models](https://rss.onlinelibrary.wiley.com/doi/10.1111/1467-9868.00294), [summary](http://www.mucm.ac.uk/Pages/Downloads/Presentations/RW%200608%20Hathersage.pdf)

- Take account of all sources of uncertainty:
Parameter uncertainty, Measurement error, Model discrepancy, Code uncertainty 
- Two information source:
-- Computer model $M(x, θ)$ 
-- Field data $D_{field}$: noisy measurement collection of reality at a variety of x values; compared with model outputs, $D_{sim} = {M(x_i, θ_i), i = 1..N}$.
-- discrepancy measure $\delta(x)$ and measurement error $\epsilon$ are used
-- $\mathcal{D}_{\text {field }}(x)=M(x, \hat{\theta})+\delta(x)+\epsilon$

### 2.2 Muehleisen [Bayesian Calibration - What, Why And How](https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1166&context=ihpbc)
- example of misuse of the term Bayesian calibration as the concept introduce here is Bayesian inference; all the same it explains great qualities of Bayesian inference including how it avoids overfitting
- "Bayesian calibration is a method of calibration that is fundamentally different than conventional calibration methods. Bayesian calibration has a long history within computer modeling in general (Dunsmore, 1968; RacinePoon, 1988; Kennedy and O’Hagan, 2001)" 
  

### 2.3 Betancourt 2019 [Calibrating Model-Based Inferences and Decisions](https://arxiv.org/abs/1803.08393)
**Bayesian inference** doesn’t say anything about what decisions to make, it just provides information to make decisions.
**Bayesian decision theory** combines a posterior distribution with a utility function to make a decision based on the information contained within that posterior distribution.  The decision analysis in the manual is an example of this.

**Bayesian calibration** considers how effective any decision making process might be within the scope of the modeling assumptions.  


![](https://i.imgur.com/tVfVIyu.png)



### 2.4 Dawid, 1982 The Well-Calibrated Bayesian

Well-Calibration:= relative frequency of an actual event is similar to forecast the probability of the event
Theorem 1: admissible selection process' empirical probability converges to average probability with probability 1 (proved with Martingale convergence theorem).

### 2.5 Oakes, 1985 Self-Calibrating Priors Do Not Exist

Nonexistence of self-calibrating prior is shown with a counterexample: one P for which calibration property (i.e. limiting relative frequency of actual event equals forecast probability of the event) does not hold

### 2.6 Dawid, 1985 The Impossibility of Inductive Inference (Dawid's comment for 2)
the implication of 2 is explained as "no statistical analysis of sequential data can be guaranteed to provide asymptotically valid forecasts for every possible set of outcomes"
### 2.7 Dawid, 2015 [THE GEOMETRY OF DECISION THEORY](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.106.7396&rep=rep1&type=pdf)

### 2.8 Calibration in NN, RL, Finance
1. NN 
[Revisiting the Calibration of Modern Neural Networks](https://arxiv.org/abs/2106.07998)
- a model f is **well-calibrated** if its output truthfully quantifies the predictive uncertainty.
For example, if we take all data points x for which the model predicts [f(x)]y = 0.3, we expect 30% of them to indeed take on the label y. Formally, the model f is said to be calibrated if (Bröcker, 2009)
$∀p ∈ ∆: P(Y = y | f(X) = p) = p_y$ (1)
- slightly weaker, but more practical condition, called top-label or argmax calibration (Kumar et al., 2019; Guo et al., 2017). This requires that the above holds only for the most likely $∀p^{*} ∈ [0, 1]$ $P\left(Y \in \arg \max p \mid \max f(X)=p^{*}\right)=p^{*}$

3. RL
4. Finance [Copula function calibration](https://www.frontiersin.org/articles/10.3389/fams.2021.642210/full)


# 3. Bayesian calibration meets decison
Iterative model validation including [simulation-based calibration (SBC)](https://mc-stan.org/docs/2_26/stan-users-guide/simulation-based-calibration.html) and predictive checks are needed as introduced in [Bayesian workflow](https://arxiv.org/abs/2011.01808). The aim of this writing is to show the importance of SBC for decision analysis with a thorough anatomy of compoenets that affect the final decision. The motivation was that in most business settings, calibration is focused on predictive rather than posterior. In short, SBC and predictive checks differ in the recovery test target -- parameter vs data. SBC uses the self-consistency principle to argue the need for symmetry in $p(\theta|\tilde{\theta})$ while predictive check uses conformity to real data, $p(y|\tilde{y})$. Let us begin!

There are three sequential propagation steps: posterior, predictive, and decision. $p(\theta), p(y), p(\theta_{D})$ are the end goal, for two reasons we would be more interested in $p(\theta | \tilde{y}), p(y|\tilde{y}),p(\theta_{D}|\tilde{y})$. First, we don't know the underlying true distribution. One approach is investigating investigate the convergence of $p(\theta|\tilde{y})$.   way would be to track the   but tracking their dynamical update could be more realistic in realand there ideal  as we are also interested in their dynamic update, rather than the ideal form, conditional on the observed data, our aim is $p(\theta|\tilde{y}), p(y|\tilde{y}), p(\theta_{D}|\tilde{y})$.

---
1. $p(\theta|\tilde{y})$

2. $p(y|\tilde{y}) =  \int d\theta p(y|\theta)p(\theta|\tilde{y})$
3. $p(\theta_{D}|\tilde{y}, \tilde{\theta_{D}})$
$= P(I_{\underset{\theta_D}{\operatorname{argmax}}E_{p(y| \theta_D, \tilde{y}, \tilde{\theta}_D)}[U(y|\theta_D)]})$ 
$=\int \mathbb{I}\left[E_{p(y| \theta_D, \tilde{y}, \tilde{\theta}_D)}[U(y|\theta_D)]=\underset{\theta_D'}\max\mathbb{E}_{p(y| \theta_D', \tilde{y}, \tilde{\theta}_D)}[U(y|\theta_D')]\right] P(\theta \mid \tilde{y}, \tilde{\theta_D}) d \theta$

$p(d|x^{obs}, d^{obs})$
$=\int \mathbb{I}\left (\mathbb{E}_{p(x| d, x^{obs}, d^{obs})}[U(x|d)]=\underset{d'}\max \mathbb{E}_{p(x| d', x^{obs}, d^{obs})}[U(x|d')]\right) P(\theta \mid x^{obs}, d^{obs}) d \theta$
 
cf. thompson sampling: ![](https://i.imgur.com/hfsueLQ.png)

decision parameter $\theta_D: (D,\mathcal{D}) \rightarrow(R, \mathcal{R})$. Decision type could be either discrete or continuous; its form could be single or set. model index for a model selection,  binary for hypothesis testing, integer for Interger programming etc. 
observation space $y \in Y$
observation $\tilde{y}, \tilde{\theta}_D$ 

---
Refer to [this](https://mc-stan.org/docs/2_26/stan-users-guide/ppcs-chapter.html) for more information on posterior and predictive checks.

Decision needs further explanation. [This](https://mc-stan.org/docs/2_26/stan-users-guide/example-decision-analysis.html) example from Stan manual consists of the choice of commute mode and the outcome is a time ($y$). The utility is the function of time which has different distributional parameter ($\theta$) that depends on the commute mode. The parameter does not appear in the final form as it is marginalized in the predictive distribution.

$p(y | \theta_D, \tilde{y}, \tilde{\theta}_D)=\int d\theta  p(y| \tilde{\theta}_D, \theta) \cdot p(\theta| \tilde{y})$


The existence of $\tilde{\theta}_D$ should be noted. It is highly likely that past observations are the outcome of the decisions made. For example, for inventory optimization, past observed demands are the censored value of the real demand because of the inventory level constraint -- past decision. 

Viewing the decision as another parameter increases the complexity but allows us to model its role in data generation. This provides advantage over models where decisions are passively optimized given the previous data; the structure of prior and posterior helps online update through $p(\theta_D|\tilde{\theta}_D, \tilde{y})$ and add prior knowledge or reflect preference  with $p(\theta_D)$ . 

---
## Need for SBC

Refer to Modrák, M., Moon, A. H., Kim, S., Bürkner, P., Huurre, N., Faltejsková, K., ... & Vehtari, A. (2023). Simulation-based calibration checking for Bayesian computation: The choice of test quantities shapes sensitivity. Bayesian Analysis, 1(1), 1-28.

----
SBC has largely two usecases as explained in Appendix. For 2, the advantage of SBC is clear as it is one of the few tools for evaluating the critical but frequently unexamined choice of computational method. [This](https://github.com/hyunjimoon/SBC#references) list shows its wide application. However, this writing focuses on 1. We investigate its usefulness in decision making context by suggesting the case where posterior, which are marginalized out for predictive, holds importance in decisions. My approach is to view decision as another model parameter.

Here are specific questions to develop this approach:

1.	Example situations where self-inconsistent model that false positively give decent predictive results can be a problem?

2.	For cases where only good predictive inference is needed, what could go wrong if the model is self-inconsistent?

3. Could the term $p(\theta_D|\tilde{\theta}_D, \tilde{y})$ be the basis for the need of SBC in decision making?


5. Validity condition: I claim A $\implies$ B $\implies$ C for infinite smaple
A. $p(\theta, \tilde{y}, \theta')$is symmetric (sym. joint)
B. prior samples = recovered posterior samples (set equivalence)
C. SBC rank $\sum_{m=1}^{m=M} I\left\{\tilde{{\theta}_n}<{\theta}_{nm}^{\prime}\right\}$ is N-uniform (statistics uniformity)

note)
- no equality in finite sample setting for B, C. threshold condition needed
- A to B asymptotic: closeness of $P_{S_{1..n}}$and $P_{S'_{1..n}}$ becomes reliable if $P_{S_{1..n}}$ and $P_\theta$ becomes close enough. ie.$||P_{emp}- P_{prior}||_{TV} <\epsilon \implies 
||P_{emp} - P_{posterior}||_{TV} < f(\epsilon)$
- $p(\theta) = p(\theta') \forall \tilde{y} \implies$ A?
- $p(\theta|y):p(\theta, y)=1:n$
- implication of identifiable ($p(x|\theta) = p(x|\theta') \forall x \implies \theta = \theta' \;(x \in R^N, \theta \in R^d)$ ):?
- counterexample for 3 $\implies$ 1: algorithm gives always returns sample frprior. B,C holds but A does not.

<SBC process> ![](https://i.imgur.com/IRKMaRo.png)

For 1 or 2, understanding the following two papers which has high focus on predictive beharviors of the model could be helpful.
[Projection Predictive Inference for Generalized Linear and Additive Multilevel Models](https://arxiv.org/pdf/2010.06994.pdf) 
[A Decision-Theoretic Approach for Model Interpretability in Bayesian Framework](https://arxiv.org/pdf/1910.09358.pdf) 

Note) a validation methodology comparison concentrates on parameter distribution in [Yao, 2018](https://arxiv.org/pdf/1802.02538.pdf). It explains VSBC diagnostics could complement PSIS diagnostic when VI posterior produce good point estimates even though the underlying distribution has stark difference with the true posterior. 

## Appendix. SBC use case
1. Test prior and likelihood on the basis of computational consistency
Any canonical Bayesian Model has the self recovering property, in which averaging over posterior distributions fitted with samples from the prior predictive distribution will always be equal to the prior distribution. SBC uses the above principle and evaluates the combination of the prior and likelihood model under a fixed computation algorithm. Users should choose one computation algorithm in advance, such as full HMC, ADVI, Laplace approximation.

2. Test approximation algorithms
Approximation based Bayesian computation is very promising but one limitation is that it can be hard to diagnose its reliability. For example, full HMC benchmark is needed to measure its error. SBC which evaluates how well an algorithm samples from the posterior distribution, given a model and a prior could be an alternative tool for measuring reliability.
$\pi(\theta) \simeq \int \mathrm{d} \tilde{y} \mathrm{~d} \tilde{\theta} \pi_{\text {approx }}(\theta \mid \tilde{y}) \pi(\tilde{y} \mid \tilde{\theta}) \pi(\tilde{\theta})$ 
Inconsistency is observed when approximate  joint or conditional distribution of computation algorithm is not close enough to that of original model ie. $\pi(\theta |y)$ and $\pi_{approx}(\theta ,y)$ are largely different. However, the identity holds true for any $\pi(\tilde{y} \mid \tilde{\theta}) \pi(\tilde{\theta})$. 

## replacement for SBC
- predictive validation for Generalized additive model (GAM) on every compoent could replace posterior validation
![](https://i.imgur.com/M8XD6PN.png)
