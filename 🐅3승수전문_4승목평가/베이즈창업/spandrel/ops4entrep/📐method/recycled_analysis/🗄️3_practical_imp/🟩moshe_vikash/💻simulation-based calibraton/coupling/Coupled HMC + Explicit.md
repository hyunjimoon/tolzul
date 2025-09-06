###### tags: `MCMC`, `coupling`
kernel은 각각 d공간에서 생성 후 2d공간에서 이동
advanced hmc overriding으로 인해 
kernel, hamiltonian, integrator, 첫 sample 

q. 
couplingdml init설정법?
mixture는 어디에?

3종류: ,
couplings.ji: couping관련함수제공

![[Pasted image 20210724111843.png]]
line2: advanced HMC (초기설정)

mixturekernel, maximumcoupled

![[Pasted image 20210724112032.png]]
## alg3.
![[Pasted image 20210724112556.png]]
![[Pasted image 20210724110706.png]]
![[Pasted image 20210724110805.png]]


![[Pasted image 20210724114424.png]]
![[Pasted image 20210724114730.png]]
![[Pasted image 20210724120805.png]]

mixture 중 advanced 돌아감

```
- change hamiltonian: H = V + K 
(flow is changed)
- change integrator($T_s$) according to the changed coupling

1. 현 rhmc이 생각보다 쓸모없다
2. coupling이 유용
3. explicit이 중요하다 (mass의미있음)

symplectic깨진다 + coupling을 합치자
- 어떤 coupling을 쓰느냐? 
- 알고리즘 2번 돌리는 걸 hamiltonian coupling

```
![](https://i.imgur.com/mMbiMnQ.png)
![[Pasted image 20210724113709.png]]


![](https://i.imgur.com/gEh4Y2V.png)
$T_s$, Hamiltonian

0717
차주 (8) 식 alg.8봐오기 왜 mixture kernel이용했는지
0710
hamiltonian을 바꾸자
1. rhmc이 생각보다 쓸모없다
2. coupling이 유용
3. explicit이 중요하다 (mass의미있음)

symplectic깨진다. + coupling을 합치자
어떤 coupling을 쓰느냐? 
알고리즘 2번 돌리는 걸 hamiltonian coupling

Multinomial hmc

probability α we use the coupled RWMH kernel and with probability 1−α we use the HMC kernel. Heng and Jacob (2019) proves that, under certain assumptions, if the relaxed meeting time

τ δ:= inf { n ≥ 0 : ∥ X n− Y n−1∥ ≤ δ }

### coupling관련 논문
- Can perfect synchrony emerge from a cacophony of thousands of mindless metronomes? yes. Not only can it work-it will alway work

system synchronizing itself
- [Solvable Model for Chimera States of Coupled Oscillators](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.101.084103?casa_token=-CHxHO1z9GIAAAAA%3A1qGA9fjMN6YCycXC4cQDFIAAOdjpQ1vGPcy4BjcZya9COkSYVsDhVBiTsi16_Vm-wy3G-guXhVeAIstE)
- Networks of Oscillators That Synchronise Themselves, 2020 [lecture](https://www.youtube.com/watch?v=e5xxdNeNkmE&ab_channel=TheArchimedeans)
![](https://i.imgur.com/BZ23xSl.png)
Global synchronize:= asymptotically all oscillators approaches in-phase state, starting from all almost all initial conditions (terrible initial conditions are measure zero as they are both expanding in volume but self-inclusive.)

[IMPLEMENTABLE COUPLING OF LEVY PROCESS AND BROWNIAN MOTION](https://arxiv.org/pdf/2103.11475.pdf)
### coupling관련 용어정리
Reordering of Brownian increments

- recursive manner
- upper bound on the mean squared maximal distance between the paths
- reduce comonotonic (perfect positive dependence between vector components; represented as increasing functions of a single random variable) coupling of increments

### Multilevel Monte Carlo simulation
- samples are taken on different levels of accuracy to compute expection of stoch. sim.
- cost-saving by taking many low accuracy and cost (lev 0) samples and very few with high acc (lev 2).
- telescope sum for $E[G]$, works if ${V} [G_{\ell }-G_{\ell -1}]\rightarrow 0$
$\mathrm{E}\left[G_{L}\right]=\mathrm{E}\left[G_{0}\right]+\sum_{\ell=1}^{L} \mathrm{E}\left[G_{\ell}-G_{\ell-1}\right]$
- recursive control variate strategy.
- ![](https://i.imgur.com/aCBzjd9.png)
- use an approximation to the sample path  X(t) with time step  <font color = "blue">$h_{l}=2^{-l}T$. </font>
- uncertainty quantification application (PDE with random coefficients)

![](https://i.imgur.com/yvL3Q0b.png)

### Talk: [Coupling of levy process and Brownian motion](https://arxiv.org/pdf/2103.11475.pdf)
 - Levy process X(t) ($t \in [0,1]$): continuous-time analog of a random walk. (e.g. Brownian motion process, )
![](https://i.imgur.com/rzaKR8Y.png)

Two asymp. equivalent alg for Brownian bridge construction: reordering Brownian increment, comontonic coupling of increments
![](https://i.imgur.com/bqQCLva.png)

![](https://i.imgur.com/bcZOurP.png)

- proof by Doob's maximal inequality, comonotonic coupling bound (last ineq.from E)
### Asymptotic equivalence of two coupling
- sequence of Levy process $X_n \rightarrow W$ and coupled Brownian motions $W_n, \hat{W_n}$
Assume $\mathbb{E} \sup _{t \in[0,1]}\left|X_{n}(t)-\widehat{W}_{n}(t)\right|^{2}=\mathrm{O}\left(\varepsilon_{n}\right)$ for some $\epsilon_n \rightarrow 0$. Then $\mathbb{E} \sup _{t \in[0,1]}\left|X_{n}(t)-{W}_{n}(t)\right|^{2}=\mathrm{O}\left(\varepsilon_{n}\right)$ given it is true for t = 1, $logk_n/k_n = O(\epsilon_n)$

$\mathbb{E} \max _{i \leqslant k_{n}}\left|X_{n}\left(i / k_{n}\right)-\widehat{W}_{n}\left(i / k_{n}\right)\right|^{2} \leqslant 4 \mathbb{E}\left|X_{n}(1)-\widehat{W}_{n}(1)\right|^{2}$
$=4 k_{n} \mathbb{E}\left|X_{n}\left(1 / k_{n}\right)-\widehat{W}_{n}\left(1 / k_{n}\right)\right|^{2} \leqslant 4 C k_{n} \mu_{4, n}$

### Proximity of two Brownian bridge
$\mathbb{E} \sup _{t \in[0,1]}|[W(t)-t W(1)]-[\hat{W}(t)-t \hat{W}(1)]|^{2}=\mathrm{O}(\log k / k)$ uniformly for all processes X
- Brownian bridge 용도?


### Optimal transport couplings
![](https://i.imgur.com/rqBIQu2.png)



![](https://i.imgur.com/FljUXHQ.png)
객체인 TS, alg
[coupled reflection](https://github.com/pierrejacob/statisfaction-code/blob/master/2019-09-stan-logistic.R)도 구현은 돼있음 
vectarget은 target dist의 logpdf정의된부분
# Coupled HMC + Explicit
0619
![](https://i.imgur.com/USMR2WS.png)
- coupling섞어 symplectic깨지는 문제를 해결하자
- sampling시간이 많이 걸림 but narrow한 부분탐색가능이 장점이었음 (김) - 소수의 횟수로 adaptation할 수 있느냐?
- 어려운 sampling가능

0626
특수상황에서 explicit form 있음
![](https://i.imgur.com/lukiikP.png)

![](https://i.imgur.com/2UdsJ2Q.png)
metric정함, hamiltonian 정의함, Integrator를 정의함 (flow의 이산화)

![](https://i.imgur.com/4QVtwNJ.png)

metric 이전에 hamiltonian 형태를 바꿈 H1 + H2 + / H1내의 (w,p)가 metric영향받음
[Multinomial](https://github.com/TuringLang/AdvancedHMC.jl/blob/c8feff3350e72cf0fcb2ebe1841c1a80ee0afe9a/src/trajectory.jl#L330) code from advancedHMC
0612
- hamiltonian 어떻게 바뀜?
- 1,4비교

0605

Our target is coupled Markov kernel with nonseparable(i.e.Riem) but symplectic integrator.
- integrator is a discrete approximation of the flow
- symplectic implies volume preserving
- explicit leapfrog integrator is nonseparable but symplectic and therefore volume preserving
- Riem. setting is nonseparable as the kinetic term is the function of $\theta$ (position)  $H(p,q) = U(p,q) + K(p)$ -> $K(p,q)$
- Understanding the implication of [this](https://www.jmlr.org/papers/volume6/lafferty05a/lafferty05a.pdf) paper which says "there is no need to introduce other structures such as a Riemannian metric, local coordinates, or a reference measure." @조건희 please? :)
- Experiment below @김민규, 문현지
```{python}
class Sampler(Enum):
    HMC = 1
    RMHMC = 2
    HMC_NUTS = 3
    # IMPORTANCE = 3
    # MH = 4

class Integrator(Enum):
    EXPLICIT       = 1
    IMPLICIT       = 2
    S3             = 3
    SPLITTING      = 4
    SPLITTING_RAND = 5
    SPLITTING_KMID = 6

class Metric(Enum):
    HESSIAN = 1
    SOFTABS = 2
    JACOBIAN_DIAG = 3
    HYPERELLIP = 4
```
link to [note](https://github.com/TuringLang/CoupledHMC.jl/blob/76ec0efc91121c53ce495ca0d0edd057613fd37a/research/notebooks/illustration.ipynb)
```{julia}
q₀ = [
    -2.0 1.0;
     0.0 0.5
]
metric = AdvancedHMC.UnitEuclideanMetric((dim, 2))
hamiltonian = AdvancedHMC.Hamiltonian(metric, target.logdensity, target.get_grad(q₀))
integrator = AdvancedHMC.Leapfrog(fill(0.3, 2))

p₀ = [-1, 1]
z = AdvancedHMC.phasepoint(hamiltonian, q₀, cat(p₀, p₀; dims=2))
zs = [z, AdvancedHMC.step(integrator, hamiltonian, z, 7; fwd=true, full_trajectory=Val(true))...]

ℓweights = -AdvancedHMC.energy.(zs)
ℓweights = cat(ℓweights...; dims=2)
unnorm_ℓprob = ℓweights
prob = exp.(unnorm_ℓprob .- AdvancedHMC.logsumexp(unnorm_ℓprob; dims=2))

τ¹ = cat(map(z -> z.θ[:,1], zs)...; dims=2)
τ² = cat(map(z -> z.θ[:,2], zs)...; dims=2)
p, q = prob[1,:], prob[2,:]
```

problem) Coupling paper does not include RMHMC setting i.e. K(p ) = 1/2p^tp. Integrator in [this](https://github.com/TuringLang/AdvancedHMC.jl/blob/master/src/integrator.jl) julia file does not include line3 from Alg.1 below. Could [this](https://github.com/TuringLang/CoupledHMC.jl/blob/9ce2a2a40123851ba4f1a795377f4f0438f65f84/src/couplings.jl#L59) euclidean distance part for optimal transport coupling be related?


> $W_p$-coupling due to the role it plays in the Wasserstein distance wrt. Euclidean metric. $W p ( µ , ν) = ( inf γ ∈ Γ( µ ,ν) \\E (X,Y )∼ γ ∥ x − y ∥ 2 p ) 1/p$. In this work we will consider two diﬀerent choices for the metric d: 1) Euclidean distance d 2 which gives rise to the W 2 -coupling, and 2) 0-1 distance $d_I$ which gives rise to the maximal coupling.
논문 다음부분해석법?
![](https://i.imgur.com/UDoJKal.png)




```{julia}
    for i = 1:n_steps
        # Tempering
        r = temper(lf, r, (i=i, is_half=true), n_steps)
        # Take a half leapfrog step for momentum variable
        r = r - ϵ / 2 .* gradient
        # Take a full leapfrog step for position variable
        ∇r = ∂H∂r(h, r)
        θ = θ + ϵ .* ∇r
        # Take a half leapfrog step for momentum variable
        @unpack value, gradient = ∂H∂θ(h, θ)
        r = r - ϵ / 2 .* gradient
        # Tempering
        r = temper(lf, r, (i=i, is_half=false), n_steps)
        # Create a new phase point by caching the logdensity and gradient
        z = phasepoint(h, θ, r; ℓπ=DualValue(value, gradient))
        # Update result
        if FullTraj
            res[i] = z
        else
            res = z
        end
```
## Experiment 
This means IMPLICIT.implicit, IMPLICIT.explicit in [this](https://github.com/hyunjimoon/hamiltorch/blob/4c5a11d0f23701517a19d1f3aeffb0839b4e41bb/hamiltorch/samplers.py#L379) file should be newly implemented in Julia.  main experiments will be revising [this]( https://github.com/TuringLang/CoupledHMC.jl/blob/master/research/notebooks/meeting-plot.ipynb) file on [this](https://colab.research.google.com/github/ageron/julia_notebooks/blob/master/Julia_Colab_Notebook_Template.ipynb#scrollTo=s5igIeDRp0_t) colab notebook.

![](https://i.imgur.com/ZyGfZ3U.png)


EOD------

Porting to python is [possible]( https://github.com/salilab/hmc/blob/master/examples/notebooks/basic_usage.ipynb), but simply changing [here](https://github.com/TuringLang/AdvancedHMC.jl/blob/cf3df9496fd2957f6d657df1c269737ae399731a/src/integrator.jl#L89) could be enough.

![](https://i.imgur.com/mt78SqJ.png)


![](https://i.imgur.com/aMKjA9a.png)

max coupling: transition함수만 변형상태

![](https://i.imgur.com/eyXrxZo.png)


![](https://i.imgur.com/qTOUEJc.png)


[link](https://github.com/TuringLang/CoupledHMC.jl/blob/9ce2a2a40123851ba4f1a795377f4f0438f65f84/src/couplings.jl#L30)
![](https://i.imgur.com/WUG1QHm.png)

https://github.com/TuringLang/CoupledHMC.jl/blob/9ce2a2a40123851ba4f1a795377f4f0438f65f84/src/trajectory_samplers.jl#L34
![](https://i.imgur.com/wVIUVEE.png)

![](https://i.imgur.com/2T4LcLU.png)

Heuristically picking `k` amd `m` from a sample set of meeting time (`τs`)

![](https://i.imgur.com/VtTo01c.png)
![](https://i.imgur.com/OnpS6hj.png)

필요사항: 
- 4.1 Geometric tails via local contractivity 리뷰
- 