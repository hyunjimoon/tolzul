# Theoretical background of SBC

## Two interpretation of self-consistency

$p(\theta) = \int \mathrm{d} \tilde{y} \mathrm{~d} \tilde{\theta} p(\theta \mid \tilde{y}) p(\tilde{y} \mid \tilde{\theta}) p(\tilde{\theta})$ 

i) integrate out data then parameter
$p(\theta'|\theta) = \int \mathrm{d} y p(\theta' \mid y) p(y \mid \theta)$ 
$p(\theta') =\int d\theta p(\theta'|\theta)p(\theta)$

ii) integrate out parameter then data
$p(y) = \int  \mathrm{~d}\theta p(y \mid \theta) p(\theta)$ 
$p(\theta') = \int dy p(\theta' \mid y)$ 


## SBC basic concepts
Q1. relation to qqplot?
$F\left(F^{-1}(u)\right)=u$![](https://i.imgur.com/IBRh91j.png)
![](https://i.imgur.com/pz4Ytur.png)

Q2. Could we relate sample-based variation to its continuous counterpart? Each set of $\{\tilde{\theta_n}, \tilde{y},\hat{\theta}_{1..M}\}_{1..N}$ is approximation of $\pi(\hat{\theta}|\theta = \theta_n)$. M = 25, N = 100000

$\operatorname{Var}(\hat{\theta}-\theta)=\mathrm{E}[\operatorname{Var}(\hat{\theta} \mid \theta)]+\operatorname{Var}(\mathrm{E}[\hat{\theta} \mid \theta])$


### Correct vs Incorrect SBC
Based on the [proof](https://hackmd.io/9dAhuKpwQZyM4OgujggPrQ#SBC-proof),
Correct
\begin{aligned} \tilde{\theta} & \sim \pi(\theta) \\ \tilde{y} & \sim \pi(y \mid \tilde{\theta}) \\ \tilde{\theta}_{m}^{\prime} & \sim \pi\left(\theta \mid \tilde{y}\right) \\ r &=\#\left[\tilde{\theta}<\hat{\theta}_{m}\right] \end{aligned}
Incorrect
\begin{aligned} \tilde{\theta} & \sim \pi(\theta) \\ \tilde{y}_{m} & \sim \pi(y \mid \tilde{\theta}) \\ \tilde{\theta}_{m}^{\prime} & \sim \pi\left(\theta \mid \tilde{y}_{m}\right) \\ r &=\#\left[\tilde{\theta}<\hat{\theta}_{m}\right] \end{aligned}
![](https://i.imgur.com/gfLc7EM.png)

## SBC usecase: Measuring approximate eg. embedded laplace for LGM (latednt gaussian)
Any discrepancy of its inference would affect the rank ($\int \mathrm{d} u(y)[u(y)]^{r}[1-u(y)]^{L-r}$ term from the proof) with the manifestation of its type, such as the direction of bias and dispersion. 

### Generating vs Recovered
![](https://i.imgur.com/qMw4SRY.png)

went deeper!
![](https://i.imgur.com/LmIcc8w.png)


## 1. Contsturction of joint space given $\pi(\theta,y)$ and $\hat{\pi}(\theta | y)$
### Claim) Valid algorithm induce symmetric joint distribution w.r.t parameter and its recovered counterpart
Closeness of ${\pi}(\theta | y), \hat{\pi}(\theta | y)$ is usually assessed to test approximate algorithm. Viewing this in a joint $\pi(\hat{\theta},y,\theta)$ space is helpful. Instead of testing the likeness of data-conditioned distribution, we could test how symmetric the joint distribution is with regard to the original and recovered parameter. One advantage that comes with this is that data y can be marginalized out leading to $\pi(\hat{\theta}, \theta)$; whose symmetry we could test with the symmetry of $\pi(\hat{\theta}|\theta)$ for fixed $\theta$.

However, as this symmetry concept is abstract, an explicit symmetry-based measure that could replace or complement the rank statistics could be helpful. Which example model would you think is appropriate to start this probe? We would need a formulation on 1.combining $\pi(\theta,y)$ and $\hat{\pi}(\theta | y)$ to get the whole joint then 2. marginalize out y.


Based on this, any distribution should be recovered, not only prior which was used to construct the joint $\pi(y|\theta)$. The reason we are using prior is that we know $\pi(\hat{\theta}|\theta)$ is asymmetric for some $\theta$ and wish to measure the average degree of asymmetry on the parameter region we would most likely to encounter when using the model.

$\pi(\hat{\theta},\theta)$ is symmetric -(A)
$\pi(\hat{\theta}|\theta) = \int \mathrm{d} y \; \pi(\hat{\theta} \mid y) \pi(y \mid \theta)$ is centered on $\theta$ - (B)
$g(\hat{\theta}) = \int \mathrm{~d} \theta \pi(\hat{\theta}|\theta) g(\theta)$ - ( C)

more on [Talts, 2018](https://arxiv.org/abs/1804.06788) section 3. Existing validation methods exploiting Bayesian joint distribution
## 2. Specification of symmetry-based validity 
### Claim) A $\implies$ B $\implies$ C if N, M $\rightarrow \infty$
Q1. Can you imagine the full joint space?
Q2. what level of symmetry would hold from below? [q. on symmetry w.o. y and marginalize out y](https://discourse.mc-stan.org/t/need-help-on-sbc-uniform-proof/17777/12?u=hyunji.moon)
A. $\pi(\hat{\theta}, y, \theta)$ is $\hat{\theta}, \theta$ - symmetric (symmetric joint probability)
B1. recovered posterior samples is centered around their corresponding prior value $\forall \theta \in\Theta$
B2. recovered posterior samples is centered around corresponding $N$ prior samples $\tilde{\theta},\forall \tilde{\theta} \in\theta$
C. SBC rank $\sum_{m=1}^{m=M} I({\hat{\theta}_{nm} < {\tilde{\theta}}_n})$ is N-uniform (statistics uniformity)



Validating A is hard so we specify it to its sample-based condition B and C. I am interested in the non-asymptotic case which is why decomposing SBC failure cause is needed:


- For finite samples, B, C does not hold exactly. Given that A holds, the discrepency results form the difference btween $P_{emp}$ (discrete sample distribution) and $P_{true}$. 

- A to B asymptotic: closeness of $P_{\tilde{\theta}_{1..n}}$and $P_{\hat{\theta}_{1..n}}$ becomes reliable if $P_{emp} =(P_{\tilde{\theta}_{1..n}})$ and $P_{g(\theta)}$ becomes close enough (simliar to X $\rightarrow$ Y  if $||X_{n} - Y_{n}||_{\infty} <  \epsilon$ and $||X- X_{n}||_{\infty}  <  \epsilon$). 
The compuatation is accurate if 
1.  $||P_{emp-prior}- P_{emp-posterior}||_{TV} <\epsilon$ (distance between original and approximation measured with samples)
2.  $||P_{emp-prior} - P_{prior}||_{TV} < \epsilon$ (distance between continous and discrete)


- counterexample for 3 $\implies$ 1: algorithm which always returns sample from prior. B,C holds but A does not.
![](https://i.imgur.com/IRKMaRo.png)
Fig.1 Two steps of SBC: generate then inference



## 3. Perfect recovery after dual's dual
### claim) $\tilde{\theta} \equiv \hat{\theta}$ same set (or $P_{\theta} \equiv P_{\theta'})$ if $\hat{\pi(\theta|y)}$ satisfies conditions

Q1. Which to target: set equivalence (finite) or measure equivalence(cont)?
Set should work with $p(y|\theta)$ while measure with $p(y|\tilde{\theta})$

Q2. Is sufficient statistics needed when SBC is based on one pair of data?
![](https://i.imgur.com/NgD9A9q.png)



Doesn't $\theta$ and $y$ in $p(\theta, y)= p(\theta|y)p(y) = p(y|\theta)p(\theta)$ seem to have dual relation similar to what $(a,b)$ and $(x,y)$ in $ax + by = <(a,b), (x,y)> = <(x,y),(a,b)>$ (vector and linear function)? For exact formulation, y might be substituted to T(y), but as we are only sampling one y, I am not sure whether T(y) is needed.
- parameter $\eta$ and data $T(y)$ space in $exp(<\eta,T(y)>)$ form of exponential family 
- exponential family $(Y, \nu, T)$is probability statistical manifold. Dual cone exists [exp.varieties](https://arxiv.org/abs/1412.6185):

![](https://i.imgur.com/Hgi6Fu8.png)
Fig.2 Parameter and data space dual cone

- Considering -1 and +1 geometry of affine statistical manifold in [informatinal geometry](http://stats-www.open.ac.uk/TechnicalReports/space-aism.pdf), different SBC could be desinged depending on the distribution (normal and multinomial: -1)

related concepts
(Banach space) f = f'' reflexive iff weak = weak* top. on X*
(legendre conjugate) f = f'' iff f is convex, lower semi-continuous 
(dual cone) K = K'' if closed, convex cone


## SBC proof

The probability of the rank, $r,$ of a prior sample, $\theta_{0},$ relative to $L$ posterior samples $\left\{\tilde{\theta}_{1}, \ldots, \tilde{\theta}_{L}\right\},$ conditioned on an intermediate data simulation, $\tilde{y}$

$$
\begin{aligned}
\tilde{\theta}_{0} & \sim \pi(\theta) \\
\tilde{y} & \sim \pi\left(y \mid \tilde{\theta}_{0}\right) \\
\left\{\tilde{\theta}_{1}, \ldots, \tilde{\theta}_{L}\right\} & \sim \pi(\theta \mid \tilde{y})
\end{aligned}
$$
is given by
$\begin{aligned} \pi(r) &=\int \mathrm{d} \theta_{0} \mathrm{d} y \pi\left(y, \theta_{0}\right) \frac{L !}{r !(L-r) !} \mathbb{P}\left[\theta_{l}<\theta_{0}\right] \cdot \mathbb{P}\left[\theta_{l} \geq \theta_{0}\right] \\ &=\frac{L !}{r !(L-r) !} \int \mathrm{d} \theta_{0} \mathrm{d} y \pi\left(y, \theta_{0}\right) \mathbb{P}\left[\theta_{l}<\theta_{0}\right] \cdot \mathbb{P}\left[\theta_{l} \geq \theta_{0}\right] \\ &=\frac{L !}{r !(L-r) !} \int \mathrm{d} \theta_{0} \mathrm{d} y \pi\left(y, \theta_{0}\right)\left[\prod_{l=1}^{r} \int_{-\infty}^{\theta_{0}} \mathrm{d} \theta_{l} \pi\left(\theta_{l} \mid \theta_{0}, y\right)\right]\left[\prod_{l=r+1}^{L} \int_{\theta_{0}}^{\infty} \mathrm{d} \theta_{l} \pi\left(\theta_{l} \mid \theta_{0}, y\right)\right] \\ &=\frac{L !}{r !(L-r) !} \int \mathrm{d} \theta_{0} \mathrm{d} y \pi\left(y, \theta_{0}\right)\left[\int_{-\infty}^{\theta_{0}} \mathrm{d} \theta_{l} \pi\left(\theta_{l} \mid \theta_{0}, y\right)\right]^{r}\left[\int_{\theta_{0}}^{\infty} \mathrm{d} \theta_{l} \pi\left(\theta_{l} \mid \theta_{0}, y\right)\right]^{L-r} \\ &=\frac{L !}{r !(L-r) !} \int \mathrm{d} \theta_{0} \mathrm{d} y \pi\left(y, \theta_{0}\right)\left[\int_{-\infty}^{\theta_{0}} \mathrm{d} \theta_{l} \pi\left(\theta_{l} \mid \theta_{0}, y\right)\right]^{r}\left[1-\int_{0}^{\theta_{0}} \mathrm{d} \theta_{l} \pi\left(\theta_{l} \mid \theta_{0}, y\right)\right]^{L-r} \end{aligned}$

Because the posterior samples are independent of the prior sample conditioned on the data we have 

$$
\pi\left(\theta_{l} \mid \theta_{0}, y\right)=\pi\left(\theta_{l} \mid y\right)
$$

$$
\begin{aligned}
\pi(r) &=\frac{L !}{r !(L-r) !} \int \mathrm{d} \theta_{0} \mathrm{d} y \pi\left(y, \theta_{0}\right)\left[\int_{-\infty}^{\theta_{0}} \mathrm{d} \theta_{l} \pi\left(\theta_{l} \mid y\right)\right]^{r}\left[1-\int_{0}^{\theta_{0}} \mathrm{d} \theta_{l} \pi\left(\theta_{l} \mid y\right)\right]^{L-r} \\
&=\frac{L !}{r !(L-r) !} \int \mathrm{d} \theta_{0} \mathrm{d} y \pi\left(\theta_{0} \mid y\right) \pi(y)\left[\int_{-\infty}^{\theta_{0}} \mathrm{d} \theta_{l} \pi\left(\theta_{l} \mid y\right)\right]^{r}\left[1-\int_{0}^{\theta_{0}} \mathrm{d} \theta_{l} \pi\left(\theta_{l} \mid y\right)\right]^{L-r} \\
&=\frac{L !}{r !(L-r) !} \int \mathrm{d} y \pi(y) \int \mathrm{d} \theta_{0} \pi\left(\theta_{0} \mid y\right)\left[\int_{-\infty}^{\theta_{0}} \mathrm{d} \theta_{l} \pi\left(\theta_{l} \mid y\right)\right]^{r}\left[1-\int_{0}^{\theta_{0}} \mathrm{d} \theta_{l} \pi\left(\theta_{l} \mid y\right)\right]^{L-r}
\end{aligned}
$$

Because we’re simulating model conﬁgurations and observations from the same model from which our posterior is constructed

$$
\pi\left(\theta_{l} \mid y\right)=\pi\left(\theta_{0} \mid y\right)
$$

In particular we can consider the change of variables
$$
u(y)=\int_{-\infty}^{\theta_{0}} \mathrm{d} \theta \pi(\theta \mid y)
$$
which gives
$$
\begin{aligned}
\pi(r) &=\frac{L !}{r !(L-r) !} \int \mathrm{d} y \pi(y) \int \mathrm{d} u(y)[u(y)]^{r}[1-u(y)]^{L-r} \\
&=\frac{L !}{r !(L-r) !} \int \mathrm{d} y \pi(y) \frac{r !(L-r) !}{(L+1) !} \\
&=\frac{1}{L+1} \int \mathrm{d} y \pi(y) \\
&=\frac{1}{L+1}
\end{aligned}
$$
## EOD The rest is not done yet.
## 3. Information Geometry SBC 
### claim) Inference step of SBC should be designed based on model's distribution (statistical manifold)

Doesn't $\theta$ and $y$ in $p(\theta, y)= p(\theta|y)p(y) = p(y|\theta)p(\theta)$ seem to have dual relation similar to what $(a,b)$ and $(x,y)$ in $ax + by = <(a,b), (x,y)> = <(x,y),(a,b)>$ (vector and linear function)? For exact formulation, y might be substituted to T(x).
- parameter $\eta$ and data $T(y)$ space in $exp(<\eta,T(y)>)$ form of exponential family 
- exponential family $(Y, \nu, T)$is probability statistical manifold. Dual cone exists [exp.varieties](https://arxiv.org/abs/1412.6185):

![](https://i.imgur.com/Hgi6Fu8.png)
Fig.2 Parameter and data space dual cone

- Considering -1 and +1 geometry of affine statistical manifold in [informatinal geometry](http://stats-www.open.ac.uk/TechnicalReports/space-aism.pdf), different SBC could be desinged depending on the distribution (normal and multinomial: -1)

## 4. Desiging symmetry-based measure
From [your post](https://discourse.mc-stan.org/t/need-help-on-sbc-uniform-proof/17777/5?u=hyunji.moon)

How to summarize the symmetry 
For this, I think the follwoing is needed (which I am having difficulty):

1. With a simple approximate algorithm with distribution pˆ (gaussian approximation?), first combine p(x,y) and pˆ(x | y) then to marginalize out y 
2. 



it measures how the approximation recovers the posterior 


it is a weighted test -- test the quality of the recovery skill of approximation algorithm at each given posterior $p(\theta|y) from p(y|\tilde{\theta}) then average the quality based on how often that particular parameters are likely to realized. SBC need not exact prior because if the sampler is perfect, it would return the perfect score whatever weights we give. 



$$
\tilde{\theta} \sim N(0,1^2)
y \sim N(|\tilde{\theta},1^2)
p(\theta)
p(y_tilde, theta_tilde, theta)존재가능?
$$
1. data generating process. 
model block is coded as normal (sample update is programmed by the gradient of lp value eg. $-\frac{1}{2}\left(\frac{y-\mu}{\sigma}\right)^{2}$ for $N(y|\mu, \sigma)$ with `normal_lpdf` whose gradient is calculated at each point, $\{\theta_1, .., \theta_M\}$.
However, the data does not live in a space 

2. computation is samplers' inability to follow the flow encoded within model block. When using dynamic HMC, the factor could be sampler's divergence from the hamiltoninan flow (eg. offtracks the vector field $X_{H}$'s flow $dH(.) = w(X_{H}, .)$ due to discretizing approximation, NUTS misimplementation?..)


![](https://i.imgur.com/16uE1Um.png)


3. Discrete vs Continous (finite vs infinite)

To validate the approximation computation algorithm, samples from an reference distribution or resulting samples from ideal sampler should be first established. 
Note that the ideal sample set is not unique unlike distributionl
samples are our basic unit, which is in most cases, comparison between two distribution should we need 
reference distribution is represented only by a ﬁnite sample



- $p(\theta) = p(\theta') \forall \tilde{y} \implies$ A?
- $p(\theta|y):p(\theta, y)=1:n$
- implication of identifiable ($p(x|\theta) = p(x|\theta') \forall x \implies \theta = \theta' \;(x \in R^N, \theta \in R^d)$ ):?

