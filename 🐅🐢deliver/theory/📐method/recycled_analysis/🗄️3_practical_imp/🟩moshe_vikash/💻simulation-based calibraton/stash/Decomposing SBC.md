
## 1. Contsturction of joint space given $\pi(\theta,y)$ and $\hat{\pi}(\theta | y)$
### Claim) Valid algorithm induce symmetric joint distribution w.r.t parameter and its recovered counterpart
Closeness of ${\pi}(\theta | y), \hat{\pi}(\theta | y)$ is usually assessed to test approximate algorithm. Viewing this in a joint $\pi(\hat{\theta},y,\theta)$ space is helpful. Instead of testing the likeness of data-conditioned distribution, we could test how symmetric the joint distribution is with regard to the original and recovered parameter. One advantage that comes with this is that data y can be marginalized out leading to $\pi(\hat{\theta}, \theta)$; whose symmetry we could test with the symmetry of $\pi(\hat{\theta}|\theta)$ for fixed $\theta$.

However, as this symmetry concept is abstract, an explicit symmetry-based measure that could replace or complement the rank statistics could be helpful. Which example model would you think is appropriate to start this probe? We would need a formulation on 1.combining $\pi(\theta,y)$ and $\hat{\pi}(\theta | y)$ to get the whole joint then 2. marginalize out y.


Based on this, any distribution should be recovered, not only prior which was used to construct the joint $\pi(y|\theta)$. The reason we are using prior is that we know $\pi(\hat{\theta}|\theta)$ is asymmetric for some $\theta$ and wish to measure the average degree of asymmetry on the parameter region we would most likely to encounter when using the model.

$\pi(\hat{\theta},\theta)$ is symmetric -(A)
$\pi(\hat{\theta}|\theta) = \int \mathrm{d} y \; \pi(\hat{\theta} \mid y) \pi(y \mid \theta)$ is centered on $\theta$ - (B)
$g(\hat{\theta}) = \int \mathrm{~d} \theta \pi(\hat{\theta}|\theta) g(\theta)$ - (  C)


more on [Talts, 2018](https://arxiv.org/abs/1804.06788) section 3. Existing validation methods exploiting Bayesian joint distribution
## 2. Specification of symmetry-based validity 
### Claim) A $\implies$ B $\implies$ C if N, M $\rightarrow \infty$
A1. (joint) $\pi(\theta', y, \theta)$ is $\theta', \theta$ - symmetric (symmetric joint probability)
A2. (joint) $p(\theta'|\theta = c, y = d) \stackrel{D}{=} p(\theta|\theta' = c, y = d) \; \forall c, d \in R$
B. (marginalize y) $p(\theta'|\theta = c) \stackrel{D}{=} p(\theta|\theta' = c) \; \forall c$
C. (marginalize $\theta$ or $\theta'$) $p(\theta) \stackrel{D}{=} p(\theta')$
D. (statistics uniformity) SBC rank $\sum_{m=1}^{m=M} I\left\{{\tilde{\theta}}_n<\hat{\theta}_{nm}\right\}$ is uniform on n = {1,..,N} 

SCM lies between B and C in that its member satisfy $p(\theta'|\theta \sim \mu) \stackrel{D}{=} p(\theta|\theta'\sim \mu)$.


B1. recovered posterior samples are centered around their corresponding parameter value $\forall \theta \in\Theta$
B2. recovered posterior samples is centered around each of thier corresponding $N$ reasonable values sampled from SCM $\tilde{\theta},\forall \tilde{\theta} \in\theta$
A. means $\theta'|\theta = \theta|\theta' = c_1$
Any discrepancy of its inference would affect the rank ($\int \mathrm{d} u(y)[u(y)]^{r}[1-u(y)]^{L-r}$ term from the proof) with the manifestation of its type, such as the direction of bias and dispersion. 


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

Q1. set equivalence (finite) or measure equivalence(cont)?
Set should work with $p(y|\theta)$ while measure with $p(y|\tilde{\theta})$
![](https://i.imgur.com/NgD9A9q.png)

Q2. Is sufficient statistics needed for one pair of data?

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
