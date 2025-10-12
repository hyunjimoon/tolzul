## 1. What
Iterative calibrating the chosen generative model system with self-organization which passes predictive checks, SBC, and return satisfactory diagnostics . Chosen  model consists of both mathematical and programic conveyor for {prior, Likelihood, computational algorithm}.

## 2. How
### prior
- Customized verison (probability invese tranform) is possible but choosing among [[Math-Family of distribution]] is conventional.
- SD의 prior설정: 다음 영상의 06:17에 실제 data피팅전, synthetic data를 생성해 reality check을 하는 구조가 소개됩니다. Stan+SD논문에서도 prior로 priorSim데이터를 먼저 생성하고 이에 피팅합니다.

<iframe title="vimeo-player" src="https://player.vimeo.com/video/206297867?h=1d77447143" width="640" height="360" frameborder="0" allowfullscreen></iframe>
 
### likelihood
The two representative likelihood pairs are: (`poisson`, `negative binomial`) for non-negative or integer type data and (`normal`, `t`) for data without any range or type contraint. Each of them form a pair as the latter is mixture version of the former meaning the latter is a more robust (a.k.a. added layer of parameter via hyperprior) version. Notice using the mixture version of likelihood, we can have the same effect as giving the prior for the parameter.

#### `poisson` $\rightarrow$ `negative binomial`
Mixture of poisson with common rate that follows a gamma distribution becomes negative binomal mixture:

$\operatorname{NegBin}\left(t \mid n, \frac{1}{\theta+1}\right)=\int_{0}^{\infty} \operatorname{Pois}(t \mid \lambda) \operatorname{Gamma}(\lambda \mid n, \theta) d \lambda$

#### `normal` $\rightarrow$  `t`
Mixture of normals with common mean and variances that follow an inverse-gamma distribution. Formally, let X | W be normal with mean 0 and variance W. Let W ∼ inverse gamma(ν/2, ν/2). Then the marginal distribution on X is Student-t with ν degrees of freedom.

$\begin{aligned} f_{X}(x) &=\int_{0}^{\infty} f_{X \mid w}(x) f_{W}(w) d w \propto \int_{0}^{\infty} \frac{1}{\sqrt{w}} \exp \left(-\frac{x^{2}}{2 w}\right) w^{-\frac{v}{2}-1} \exp \left(-\frac{v}{2 w}\right) d w \\ &=\int_{0}^{\infty} w^{-\frac{v+1}{2}-1} \exp \left(-\frac{x^{2}+v}{2 w}\right) d w =\Gamma\left(\frac{v+1}{2}\right)\left(\frac{x^{2}+v}{2}\right)-\frac{v+1}{2} \end{aligned}$

Interesting extension on variance decomposition [here](https://www.johndcook.com/t_normal_mixture.pdf).

### computational method
HMC, default stan estimator, is believed to fully recover the samples that represent the typical set of posterior space. However, due to feasibility issues such as [`L-BFGS` algorithm for opitimization](https://mc-stan.org/docs/2_29/reference-manual/bfgs-and-l-bfgs-configuration.html) or [`ADVI` algorithm for variational inference.](https://mc-stan.org/docs/2_29/reference-manual/vi-algorithms.html) 

## 3. Why

The roles of prior is summarized in [[🌀Comp(Stat)]]. Prior constructed purely from our knowledge may not be its optimal form as the computational aspect is not relfected yet.                  
- one shot vs iterative of setting prior can be found in [this](https://arxiv.org/pdf/2112.01380.pdf) paper p.10 D5. 


For more detail on history of Bayesian calibration refer to [1. Intro ](https://www.hyunjimoon.com/blog/bayesian-calibration-1-introduction/) and SBC's role to [2.SBC as navigator](https://www.hyunjimoon.com/blog/bayesian-calibration-2-sbc-as-a-navigator/).

---

Specific question as below motivated this writing.

> SD에 포함된 변수들의 모수를, 시스템 전체 관점에서 최적의 모수를 찾는건가요? 

$\lambda$ ~ `gamma(1,1)` -Vensim SD generator-> $\tilde{y}$ - Stan HMC estimator -> $\lambda$ ~ ??

If ?? is close enough to `gamma(1,1)`. 그 후 실제 데이터를 위 $\tilde{y}$에 대입.

> 그러면 결국 통계모델에 데이터를 기반으로 업데이트하는 과정이 시스템 관점에서 최적화되는게 캘리브레이션이 되는건가요? 

calibration용어가 혼용되고 있어요. estimator로 쓰일수도 있고, iterative update를 통한 수리이론적+컴퓨팅계산적 모델의 합치로 쓰일수도 있습니다. 1. 수리적모델과 컴퓨터모델을 구별하지 못하거나 2. 컴퓨터모델이 완벽히 수리적모델을 완벽히 재현해낼때 두 의미가 같아지는데요. pre-asymptotic한 상황에서는 구별하는걸 추천드립니다. 

> 시스템 전체 관점에서 캘리브레이션되면 기존의 통계모델과는 얼마나 차이가 나나요? 원래 통계모델 자체가 시스템의 작동 현상들이 반영된 데이터로 추정하는 것인데 둘의 차이가 있나요?

"기존의 통계모델"상의 추론이 SD calibariton을 포함합니다. ODE system이라하고 stan에서 이를 지원하고 있어요.