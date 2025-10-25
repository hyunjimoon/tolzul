###### tags: `calibration`, `hierarchical`, `decision`, `reliability`
#reliability #calibration #verification #convergence 
# Hierarchical model
Bayesian calibration on hierarchical model with Navy data
Contribution: 
- Applying Bayesian calibration could improve our model in the [previous paper](https://onlinelibrary.wiley.com/doi/10.1002/ail2.22) 
- Applying the new workflow [Bayesian workflow(2020)](https://arxiv.org/abs/2011.01808) and its revision (progressing by Moon) is needed in failure prediction, reliability engineering domain especially in hierarchical model perspective where prior and calibration needs extra care due to highly correlated parameters

## 1. Inference
### 1.1 Previous <s>calibration</s> inference
$$
\text{Given the observation model}  \;p_1(Y|\Theta),\\
$$

$$
\underset{\theta} {min} \; divg(p_1(\tilde{y}|\theta), p(y_{obs}))\
$$

Disadvantage
i) structural inability to separate epistemic (E) uncertainty form aleatoric (A) during calibratiton as it assumes no uncertainty exists in real world data; excluding modeling errors could make conventional calibration methods amplify model output uncertainty if data is biased (Muehleisen)

ii) inseparable contribution of each parameter on failed test 

iii) can overfit

## 1.2. Bayesian <s>calibration</s> inference
$$
\text{Given the observation model} \;p_1(Y|\Theta),
$$
$$
\underset{p(\theta)} {min} \; \int d\theta  \;divg(p_1(\tilde{y}|\theta), p(y_{obs})) p(\theta)\\
$$
The objective function of Bayesian cannot be the sole function of $y$ as then overfitting cannot be avoided. Instead, $y$ replaces $y_{obs}$ leading to

$$
\underset{p(\theta)} {max} \; \int d\theta \; p_1(y_{test}|\theta)p(\theta)\\
$$
The prior term acts as a regularizing term; 
regularized risk functional is deﬁned by

R reg [f] := R emp [f] + λΩ[f]

and the regularized risk in RKHS is deﬁned by

λ R reg [f] := R emp [f] + f || 2 H 2 ||

Note that minimizing R reg [f] is equivalent to minimize R emp [f] subject to Ω[f] ≤ t. (Use the KKT condition.)


$$
\text{Given the observation model}  \;p_1(y|\theta),
$$

$$
\underset{p(\theta)} {max} \; \int d\theta \; p_1(y_{obs}|\theta)p(\theta)\\
$$
$$
\underset{\mu_\theta} {max} \; \int d\theta \; p_1(y_{obs}|\theta)\mu_{0_{\theta}}\mu_\theta\\
$$
or
$$
\underset{p(\theta)} {min} \; \int d\theta  \;divg(p(\tilde{y}|\theta), p(y_{obs})) p(\theta)\\
$$
- can reduce overfitting by not trying to minimize the difference between the model output and the measured data but rather maximize the likelihood (from Muehleisen but unclear) that the model output is statistically consistent with the measured data
- uncertainty is included in its result enabling further update: starting from a crude uniform or tiragular prior, parameter distribution is iteratively updated to customized and empirical form
- different from popular optimization methods; (but interpretation of measure optmization could be possible)

The core idea was compared to other fitting framework where the returned value is q(z)
- determine the most likely input parameter  **uncertainty** that yield observed data's output  **uncertainty** 

## 2. Bayesian Calibration

 In Bayesian calibration, ground truth itself and the simulated results from it are compared for model diagnose and update.
 
$\tilde{\theta} \sim \pi_{S}(\theta)$
$\tilde{y} \sim \pi_{S}(y \mid \tilde{\theta})$
$\tilde{U}=U(a(\tilde{y}), \tilde{\theta}]$
To be specific, repeatedly simulating model configurations from the prior distribution, observations from the corresponding data generating process, running our analysis to completion, and then scrutinizing the resulting likelihood functions, posterior distributions, and decision outcomes in the context of the simulated ground truth.

The compared results tell how decision making process is within the scope of the modeling assumptions. The utility $U(a(y), \theta)$ and action $a(y)$ are defined specific to diverse problems including prediction, posterior, computation algorithm etc  ([Betancourt, 2019](https://betanalpha.github.io/assets/case_studies/modeling_and_inference.html#33_bayesian_calibration)). This [newly](https://hackmd.io/HqHLMaGmQvOE0mQJ_5bcDw#Definition-Best-self-consistent-measure-SCM) proposed workflow uses this Bayesian calibration spirit as well.



--

1. Purpose
In practical aspect, hierarchical Bayesian model and tool are created for engine failure prediction. Our model could reflect the hierarchical structure of the system and also proved to outperform traditional timeseries methods. Moreover, it could address the underlying problem which is large portion of missing data.

Another contribution of this research is to provide Bayesian model validation workflow. The validation is even more important in a small data setting and we illustrate how SBC could mitigate the missing data effect through data simulation.


2. Motivation 

Current equipment failure prediction model for Korean army lacks systemical and dynamical feature. Moreover, immature information system resulted in unfavorable data state with majority of them missing and imbalanced.

Hierarchical model has an edge in representing the features of Navy data: imbalanced category and sharing structure, by information pooling. Hierarchical models are highly predictive because of pooling (Gelman et al., 2013). When a hierarchical model is used, there is almost always an improvement, but to different degrees that depends on the heterogeneity of the observed data (Gelman, 2006). When updating the model parameters, such as prior parameters, the relationship between the part of the data being used and the whole population should always be considered. Pooled effects between subclusters are partial as they are implemented through shared hyperparameters, not parameters.

As there are not much data, validation is even more important. For this, we show how simulation-based calibration (SBC) could be applied for diagnosis and calibration. SBC (Talts et al, 2018) is a relatively new but popular validation method in Bayesian field and are being widely applied in diverse domains including cognitive science (Chure et al., 2019), bioinformatics (Hartmann, Johannsen, and Klauer, 2020), and image processing (Moores et al., 2020). It tests the combination of mathematical model and computational algorithm through calculating prior sample rank among data-averaged posterior samples. Remember that pure mathematical model itself does automatically provide the output we need for further inference and decision making. Ideological models are transformed into specific codes with which computer helps compute the specific values as it name suggests. These values include conditional probability, likelihood, or pushforward value of our quantities of interest. However, the middle man is known for its lost of precision, namely numerical error, which is why not only model but the combination of model and its computation tool should be validated as one set. In Bayesian context, the combination of model and tool could be specified further. Both observational p(y | Θ) and prior p(Θ) should be determined, once combined become posterior p(y | Θ). Computation tool investigates this posterior and returns a single (optimizing) or set of values (samling) that best represents it. In this sense, SBC tests the combination of three components, prior, observation model, and computational tool that summarizes posterior. By observing SBC result and its changes while varying only one component, each three components could be validated. In this study, we use SBC along with traditional validation methods such as cross validation.



3. Current situation

Software "Oasis" provides repair parts predictions to Republic of Korea Navy. However according to the interview, its features only include moving average and exponential smoothing. Also, the tool that validate their prediction outputs proves that current system is not robust and even dangerous.

4. Outline
![](https://i.imgur.com/0XClW1d.png)

Figure 1 shows the annual failure count of each ship by its age. Data are hierarchically structure but imbalnced with 80% of them missing. Engine archetype in the figure highlights the existence of shared characteristics between different types of engines. Engine types are categorized into five types. Most missingness is due to the absence of ROK record system.

Time series of the failure rate of Naval ships (and Airplane, if time permits) are modeled hierarchically, where each layer corresponds to ship engine, engine type, and engine archetype (figure 2). As a result of the analysis, the suggested model aim to predict the failure rate of an entire lifetime accurately in multiple situational conditions, such as prior knowledge of the engine.



6. Expected effect

Practically, the result of the reseach, once applied to military system could achieve a large budget savings and increased level of security. Theoretically, the validation workflow on Bayesian model and its computation tool with real-world data could be a groundwork for further Bayesian research in OR field. Above all, this research would be a clear illustration of how sampled result of the model could be processed to produce useful results on both inference and decision of the system.

7. Reference

Afenyo, M., Khan, F., Veitch, B., & Yang, M. (2017). Arctic shipping accident scenario analysis using Bayesian Network approach. Ocean Engineering, 133, 224-230. Barragan, J. F., Fontes, C. H., & Embiruçu, M. (2016). A wavelet-based clustering of multivariate time series using a multiscale SPCA approach. Computers & Industrial Engineering, 95, 144-155. Betancourt, M., & Girolami, M. (2015). Hamiltonian Monte Carlo for hierarchical models. Current trends in Bayesian methodology with applications, 79(30), 2-4.

Chure, G., Razo-Mejia, M., Belliveau, N. M., Einav, T., Kaczmarek, Z. A., Barnes, S. L., ... & Phillips, R. (2019). Predictive shifts in free energy couple mutations to their phenotypic consequences. Proceedings of the National Academy of Sciences, 116(37), 18275-18284. Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2013). Bayesian data analysis. Chapman and Hall/CRC. Gelman, A. (2006). Multilevel (hierarchical) modeling: what it can and cannot do. Technometrics, 48(3), 432-435. Hartmann, R., Johannsen, L., & Klauer, K. C. (2020). rtmpt: An R

package for fitting response-time extended multinomial processing tree models. Behavior research methods, 52, 1313-1338. Moores, M., Nicholls, G., Pettitt, A., & Mengersen, K. (2020). Scalable

Bayesian inference for the inverse temperature of a hidden Potts model. Bayesian Analysis, 15(1), 1-27. Schad, D. J., Nicenboim, B., Bürkner, P. C., Betancourt, M., & Vasishth,

S. (2021). Workflow Techniques for the Robust Use of Bayes

Factors. arXiv preprint arXiv:2103.08744