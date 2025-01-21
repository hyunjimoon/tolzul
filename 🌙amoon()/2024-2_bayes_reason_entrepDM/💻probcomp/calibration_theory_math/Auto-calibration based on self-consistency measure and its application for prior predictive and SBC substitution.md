tags: `calibration`

please cite  Modrák, M., Moon, A. H., Kim, S., Bürkner, P., Huurre, N., Faltejsková, K., ... & Vehtari, A. (2023). Simulation-based calibration checking for Bayesian computation: The choice of test quantities shapes sensitivity. _Bayesian Analysis_, _1_(1), 1-28. which supersedes below.

----


_Hyunji Moon. June.2021. Please do not distribute._

![](https://i.imgur.com/dkGdOje.png)

*Fig.1 Comparison of the original and revised workflow: decreased required input (shaded), the order of using data (simulated then real), automated calibration using $MCMC_{\mu_\theta}$, and the result type are different in the proposed flow. $\mu_\theta, \mu_y$ each refers to measure on parameter and data space.*
## Abstract
Contrary to the workflow suggested in [Talts20](https://arxiv.org/abs/2011.01808), where SBC is proceeded with a given prior $\mu_\theta$, data simulator $p_1(Y|\Theta)$, posterior simulator $p_2(\Theta|Y)$ and returns a hypothesis test, this paper proposes a procedure that returns a calibrated inference region for every given data and posterior simulator. This inference region, namely self-consistent measure ($SCM_{\theta}$), can then be used to measure how bespoke the two simulators are to the modeler's setting in two aspects: prior knowledge compatibility and data representability. In a Bayesian point of view, the prior knowledge on the inference range (e.g., probability of girl birth lower than 0.5) is directly compared with SCM. Then, fake data are simulated from $SCM_{\theta}$ with data simulator then compared with modeler's real data. 

This reverses the original workflow which includes predictive checks and SBC. With the prior which is pre-calibrated with prior predictive checks, data and posterior (the combination of three components) are tested with SBC. This had the following problems.
1) Modelers were overloaded with the choice of prior distribution and its parameters. Moreover, prescribing strong priors just to avoid computational problems confused the philosophy of prior.
2) Even with the right prior, the computation was heavy as it required thousands of posterior simulations.
3) Test type results did not include quantifiable information on posterior sampler. 

In a revised workflow, each is addressed with:
1. $MCMC_{\mu_{\theta}}$ automatically finds the calibrated inference region: $SCM_{\theta}$.  Priors are not what modelers can manipulate anymore. The flow of 'choose among infinite then test' is replaced with 'calibrate then choose among the finite'.
2. Guaranteed convergence of ${\mu_{\theta}}$-Markov chain allows one heavy data and posterior simulation with a repeated lighter version.
3. SCM inspection with knowledge and data are quantitatively measured with $p(\tilde{y}|y)$ and the overlap ratio of $\theta$ range.

Viewing the workflow in the perspective of verification and validation in simulation literature, we claim prior and posterior equivalence as the ideal condition for verification contrary to large difference (i.e. identified) for validation. Based on this concept, pre-data design of data collection and measurement for decision making is discussed as an extension of the revised workflow.


## Methodology
### Defintion. Self-consistent prior (SCP)
$P(\theta)$ is a self-consistent prior (SCP) when  $\int_{\theta}\left(\int_{y} p_{2}\left(\theta^{\prime} \mid y\right) p_{1}(y \mid \theta) d y\right) P(\theta) d \theta = P(\theta)$

### Definition1. Self-consistent prior set (SCS)
: set of priors that are preserved for given $A$
$$
AP(\theta) := \int_{\theta}\left(\int_{y} p_{2}\left(\theta^{\prime} \mid y\right) p_{1}(y \mid \theta) d y\right) P(\theta) d \theta \\
 SCS(A):=\{P(\theta)|AP(\theta) =P(\theta) \} 
$$
$A$ represents combination of $p1$ and $p2$. $\theta'$ is the result of inference, meaning that it is the result of fitting the generated data $y$ with $p_2(\Theta|Y)$. Data $y$ are generated with $p_1(Y|\Theta)$ with the ground truth $\theta$.

#### Observation
- $A$ preserve average operation on $\mu$ (homomorphism?) i.e. $A(1/2 (P_1 + P_2)) = 1/2(A(P_1) + A(P_2))$
- SCS is closed under convex combination. i.e. $1/2(P_1 +P_2) \in SCS \; \; \text{if} \; P_1, P_2 \in SCS$
-  If two dirac measures are included in SCS, then $\sum_{i=1}^{n} p_{i} \delta_i  \in$ SCS
- SCS is not topologically closed i.e. repeated average would give near-zero density, but $\mu$ space does not include 0
- $supp(\mu) \subset supp(p_1)$ is necessity condition for $\mu \in$ SCS
-- e.g. for Poisson model, measures defined only on $\lambda >0$ are included in SCS as $supp(p_1) = \lambda >0$ 


#### Examples
$SCS(A)$ expands as $A$ becomes regularized. For instance, $SCS(A)$ for $A$ with $p_2(\theta|y) = \delta(1)$ would only have $\delta(1)$ but with perfect posterior sampler $p_2$, every possible measure are in $SCS(A)$. While these examples show how SCS depends on $p_2$, dependence on $p_1$ could be illustrated with a funnel's neck where HMC sampler $p_2$ suffers. Compared to noncentered-parameterization (ncp) hierarchical model $p_1$, $SCS(A)$ of centered version (cp) would have narrower range of measure for population scale, $\tau$. This is because cp induces bad geometry for HMC sampler and near-zero region of $\tau$ would be excluded from $SCS$. For discussion on the relationship between SCS and automorphism group $Aut(\mathcal{W}_{p}(\mathcal{\Theta}))$, see [Appendix B](https://hackmd.io/HqHLMaGmQvOE0mQJ_5bcDw?both#B-Automorphism).

Note) Metastability excluded.

The following some another invariants that can be characterized for A, SCS, p1, p2:
- $p_2$ is X-invariant with respect to $p_1$ iff $SCS(A)$ is closed under X-transformations of the parameter space (i.e. closed under certain kinds of reparamerizations)
- A is $\theta$-invariant with respect to $\mu_{\theta}$ iff  $SCS(A)$ is closed under $\theta$-transformations of the parameter space
### Definition2. $\mu_\theta$ scale invariant
A is $\theta$ scale-invariant: existence of shared $SCS(A)$ member among $A$s with the same $p_1$ structure but with different scale. 

$$
\mu_{\theta} \in SCS(A_1) \leftrightarrow \mu_{\theta/c} \in SCS(A_2) \\ \forall A_1 \; \text{with}\; p_1(y; \theta_1, ..., \theta_p), A_2 \; \text{with} \; \; p_1(y; c * \theta_1, ..., \theta_p)
$$ 

#### Observation
- for $\theta$ scale-invariant A, constraint $\theta \in [0,1]$ can be given without affecting $SCS(A)$ i.e.$SCS(A)$ on $\theta \in [0,1]$ gives us enough information on measures with self-consistency as SCS is closed under convex combination
- e.g. Poisson. 
 -- $p_1=f(y ; \lambda)=\lambda e^{-\lambda y},  p_1'=f(y ; c*\lambda)=c*\lambda e^{-c*\lambda y}$ 
 -- if $\delta_3$ is included in SCS for $\lambda$, $\delta_k \forall k>0$ and its convex combination would also be included allowing measures with support $\{\lambda > 0\}$ to be included in SCS. This example shows SCS's inclusion of point mass is a sufficient condition for $\sum_{i=1}^{n} p_{i} \delta_i  \in SCS$ 
- e.g. Normal. 
-- fixed scale $p_1 = N(\theta, \sigma = \sigma_0 ) = \frac{1}{\sigma_0 \sqrt{2 \pi}} e^{-\frac{1}{2}\left(\frac{y-\theta}{\sigma_0}\right)^{2}}, p_1' = N(c * \theta, \sigma = \sigma_0 ) = \frac{1}{\sigma_0 \sqrt{2 \pi}} e^{-\frac{1}{2}\left(\frac{y-c * \theta}{\sigma_0}\right)^{2}}$
-- fixed location 
 $p_1 = N(\mu = \mu_0, \theta)e^{-\frac{1}{2}\left(\frac{y-\mu_0}{\sigma}\right)^{2}}, p_1' = N(\mu = \mu_0, c * \theta) = \frac{1}{c * \theta \sqrt{2 \pi}} e^{-\frac{1}{2}\left(\frac{y-\mu_0}{c * \theta}\right)^{2}}$
- e.g. Mixture normal.
-- $w*N(\mu_1,\sigma_1) + (1-w)*N(\mu_2,\sigma_2)$?
-- Could we find any $w, \mu, \sigma$ invariant relation for mixture normal? One observation is that the mixture of mixture normal is within the set of a repeated mixture of the normal.

When N prior samples and NM posterior samples generated with the following steps have the same distribution (or distance less than $\epsilon$), we call $\mu$ self-consistent. 
> 1) N prior samples are drawn from measure $\mu$
> 2) N pairs of dataset are generated 
> 3) M posterior samples are inferenced from each dataset 

In this sense, $\delta_c$ being included in SCS is a rather strong condition as it would require all posterior samples to  be c, even if data generated from c (prior sample) would include some variation. With posterior simulator that underestimates for every dataset generated from initial distribution $\delta_c$, SCS would be empty. However, if posterior simulators have a tendency to underestimate and overestimate for different value of $theta$ region, balanced mixture of them could recover the self-consistency. For instance, if $A\delta_0 = A\delta_1 =\frac{1}{2}(\delta_0+\delta_1)$ then $\frac{1}{2}(\delta_0+\delta_1)$ is included in $SCS(A)$. This could be specified with the following claim. 

### Proposition1. Symmetry-based validity exploiting Bayesian joint distribution
$A1 \leftrightarrow A2 \rightarrow B \rightarrow  C \rightarrow D$ if N, M $\rightarrow \infty$

A1. (joint) $\pi(\theta', y, \theta)$ is $\theta', \theta$ - symmetric (symmetric joint probability)
A2. (joint) $p(\theta'|\theta = c, y = d) \stackrel{D}{=} p(\theta|\theta' = c, y = d) \; \forall c, d \in R$
B. (marginalize y) $p(\theta'|\theta = c) \stackrel{D}{=} p(\theta|\theta' = c) \; \forall c$
C. (marginalize $y,\theta'$ or $y, \theta$) $p(\theta) \stackrel{D}{=} p(\theta')$
D. (statistics uniformity) SBC rank $\sum_{m=1}^{m=M} I\left\{{\theta}_n<{\theta'}_{nm}\right\}$ is uniform on $n = {1,..,N}$ 

Self-consistent measure lies between B and C in that its member satisfy $p(\theta'|\theta \sim \mu) \stackrel{D}{=} p(\theta|\theta'\sim \mu)$. Fig. illustrates B from the claim as posterior distribution on red and blue line are identical for every value of prior sample, c. This prompts the following proposition.
![](https://i.imgur.com/2bdtzDL.png)
*Fig. Symmetry-based validity exploiting Bayesian joint distribution*

### Proposition2. SCS and symmetric distribution
$$
SCS(A) := \{\mu|\int_{\theta}\left(\int_{y} p_{2}\left(\theta^{\prime} \mid y\right) p_{1}(y \mid \theta) d y\right) \mu d \theta =\mu \}\\
= \{\frac{1}{N}\Sigma_{i=1}^{N}\delta_{\theta_{i}} |\frac{1}{N}\Sigma_{i=1}^{N} [\frac{1}{M}\Sigma_{j=1}^{M}p_2(\theta'|y=j)p_1(y=j|\theta = \theta_i)]\delta_{\theta_i} = \frac{1}{N}\Sigma_{i=1}^{N}\delta_{\theta_{i}} \} \\
= \{\frac{1}{N}\Sigma_{i=1}^{N}\delta_{\theta_{i}} |\frac{1}{N}\Sigma_{i=1}^{N} p(\theta', y, \theta = \theta_{i})  = \frac{1}{N}\Sigma_{i=1}^{N} p(\theta=\theta_{i}, y, \theta') \; \forall y\} \text{(from A.1)}\\
\subset \{\frac{1}{N}\Sigma_{i=1}^{N}\delta_{\theta_{i}} |\frac{1}{N}\Sigma_{i=1}^{N} p(\theta'|\theta = \theta_i)  = \frac{1}{N}\Sigma_{i=1}^{N} p(\theta|\theta'=\theta_i) \} \text{(from B)} \\
\subset \text{prior that passes SBC test (from D)}
$$
The proposition2 follows from proposition1. Sample pair $(\theta', y,\theta)$ sequentially drawn as follows are samples from joint space which helps understanding. 

> $\theta \sim p(\theta)$ (prior)
> $y \sim p_1(y|\theta)$ (generate data)
> $\theta' \sim p_2(\theta'|y)$ (run program to get a bunch of draws)


### Definition3. Near self-consistent set

$$
 SCS_{\epsilon}(A):=\{\mu_\theta| |A\mu_\theta -\mu_\theta| <\epsilon \} 
$$
### Proposition3. SCM Getter
: Self-consistent measure is obtained from $A^n$.
$$A^n\mu_0 \in SCS_{\epsilon}(A)$$

For practical use, With finite number of samples that represent a measure, practical revise for SCS is $SCS_{\epsilon}$. The tool that could deliver the initial prior $\mu_0$ to a member of $SCS$ is repeated application of  $A$. Given a smooth and wide enough initial prior $\mu_0$ on compact parameter region, $A^n\mu_0$ would converge if they are equicontinuous from Arzelà–Ascoli theorem (The set of measures sharing the compact support is compact by 2.2.5 [here](https://link.springer.com/chapter/10.1007/978-3-030-38438-8_2)). In terms of computation, this convergence gurantee is crucial as then integral in $A$ can be approximated with moderate scale of N and M (the number of samples). Instead of using large (at least thousand) number of N prior samples, lower N can be used with increased iteration.


Once its convergence is guaranteed, $A^n\mu_0$ for large enough n becomes a member of SCS which prompts the next definition.

$$
 \mu
 := \Sigma_{k=1}^{k=|SCS|}\lambda_k\mu_k\\s.t \;
 |A\mu_k -\mu_k|<\epsilon, \\ \Sigma_{k=1}^{k=|SCS|}\lambda_k  = 1
$$

### Proposition4. $\mu_\theta$-Markov chain Monte Carlo
SCM is the expectation of measures which is approximated by averaging the set of samples that corresponds to each step of $MCMC_{\mu_\theta}$ after converge. Based on this,  $\mu_{\theta}^{MC}$
$$
 \mu^{MC}
 := \frac{1}{N}\Sigma_{k=L+1}^{k=L+N}A^k\mu_0\\s.t \;
|A\mu_L -\mu_L|<\epsilon
$$
Averaging the results shares its philosophy with             Dawid's Probability calibration where $p_i$ is averaged over only those times i when $p_i$ is close to π: $\bar{x_n}' − π → 0$ for fixed $\pi \in [0,1]$
While construcnting this markov chain, summary function which maps NM samples to N samples while preserving distribution could be composited after $p_1, p_2$ in operation $A$ as below. This is due to first, computation and memory. Exponentially growing number of samples cannot be kept. Another need for this summary function is the limited range of prior specification offered by probablistic progarms'. Prior can only have analytic form and sometimes posterior samples are refit with known distributions such as normal, gamma, and t.


![](https://i.imgur.com/4BJTfnu.png)

### Definition4. Widest self-consistent prior

$$P_{WS}(\theta) :=\min_{p(\theta)} \{ \text{div}(Ap(\theta),p(\theta)) - \lambda |\text{supp}(p(\theta))|\}$$

The first term measures the divergence between $p(\theta)$ and the posterior obtained by one iteration through the A operator representing the self-consistenty constriat while the second term incentives this prior to be as weak as possible. The second term can be substituted with entropy of $p(\theta)$.

#### Connection with regularization 

- Regularization theory: 

$$\underset{f}{\min} R_{\text {reg }}[f]:=R_{\text {emp }}[f]+\lambda \Omega[f]$$
$$\leftrightarrow \underset{f}{\min} R_{\text {emp }}[f] \text{  s.t  } \Omega[f] \leq t$$

$|supp(p(\theta))|$ term is related to  the penalty term (function's norm) in regularized risk functional. While the second term in regularized risk incentives the solution to shrink  towards zero-value, the second term in weakest self-consistent prior encourages the solution to have wider support. This seeming opposing force, shrinking (regularization) and widening (self-consistent prior) results from the fact that two problems are in a dual relationship.

1. Given a prior as regularizing factor, find the best parameter that explains data (min |y-Xbeta| + beta_norm) 

2. Given a range of parameter value from the modeler, find the best prior that are self-consistent (min |Ap - p| - entropy)

Though 1 is limited to regression, we tend to penalize complexity (diversity, high entropy). Also, it is usual that sharp (i.e. low entropy) posterior is encouraged from [here](https://statmodeling.stat.columbia.edu/2019/09/05/gneiting-on-calibration-and-sharpness/) and reference therein. I wish come up with a nice connection with existing methods as to why complexity is not penalized but encouraged. The point is extending the calibration concept from "point (ground truth parameter value) to set" to "set to set" comparison i.e. as we cannot test "E[QI|#] = # for all values of #" where # is E[QI|y]), find P(#) s.t. E[QI|P(#)] = P(#). This is also related to Andrew's concern (practical consideration) [here](https://discourse.mc-stan.org/t/need-help-on-sbc-uniform-proof/17777/13?u=hyunji.moon) that most modelers just test one or two ground truth when doing fake data simulation. The above calibration is Bayesian calibration (conditional on data) and the other types of calibrations (unconditional, conditional on parameter) are exaplained [here](https://github.com/hyunjimoon/SBC#method).

#### Connection with variational free energy maximization
The second component, $|supp(P(\theta))|$ can be replaced with entorpy of either $P(\theta)$ or $AP(\theta)$. The combination of the first term $D_{\mathrm{KL}}(Q(\theta, z)\| P(\theta|\beta,\mathbf{J}))$ in equation (3) below and the second term $\sum_{\mathbf{\theta}} Q(\mathbf{\theta} ; \boldsymbol{z}) \ln \frac{1}{Q(\mathbf{\theta} ; \boldsymbol{z})}$ in equation (2) seems to be related to the above formulation: $\min_{p(\theta)} \{ \text{div}(Ap(\theta),p(\theta)) - \Omega |\text{supp}(p(\theta))|\}$. Based on the philosophy that we target for $AP(\theta)$ that is closest to $P(\theta)$ discussed in [same prior and posterior in simulated data verification](https://hackmd.io/HqHLMaGmQvOE0mQJ_5bcDw?both#Verificate-with-simulated-data-and-validate-with-real-data), it would be interesting to formulate $P(\theta)$ and $AP(\theta)$ each playing the role of $P(\theta|\beta, J)$ and $Q(\theta; z)$ from below. 

_From [Mackay05, ch.33](http://www.inference.org.uk/itprnn/book.pdf), variational free energy $\beta \tilde{F}(z)$ measures approximation quality. Complex distribution $P(\theta|\beta, J)$ is approximated by a simpler ensemble $Q(\theta; z)$ whose parameter $z$ is adjusted to get the best approximate of P. A by-product of this approximation is a lower bound on partition function $Z( β , J)$ which is desirable because all the thermodynamic properties of the system can be derived from partition function. Finding the best latent parameter $z$ that minimize this objective function is the goal whose formulation have two interpretations.
\begin{aligned}
\beta \tilde{F}(z)\\
&:= \sum_{\mathbf{\theta}} Q(\mathbf{\theta} ; \boldsymbol{z}) \ln \frac{Q(\mathbf{\theta} ; \boldsymbol{z})}{\exp [-\beta E(\mathbf{\theta} ; \mathbf{J})]} - (1)\\
&=\beta \sum_{\mathbf{\theta}} Q(\mathbf{\theta} ; \boldsymbol{z}) E(\mathbf{\theta} ; \mathbf{J})-\sum_{\mathbf{\theta}} Q(\mathbf{\theta} ; \boldsymbol{z}) \ln \frac{1}{Q(\mathbf{\theta} ; \boldsymbol{z})}- (2)\\
& = \beta\langle E(\mathbf{\theta} ; \mathbf{J})\rangle_{Q}-S_{Q} - (2)\\
&=\sum_{\mathbf{\theta}} Q(\mathbf{\theta} ; \boldsymbol{z}) \ln \frac{Q(\mathbf{\theta} ; \boldsymbol{z})}{P(\mathbf{\theta} \mid \beta, \mathbf{J})}-\ln Z(\beta, \mathbf{J})- (3)\\
&=D_{\mathrm{KL}}(Q(\theta, z)\| P(\theta|\beta,\mathbf{J}))+\beta F(z)- (3)
\end{aligned}
Interpretation of (2) is the average of the energy function under the distribution $Q(\theta; z)$ plus the entropy of the distribution $Q(\theta; z)$ (Energy $Eg(\theta, J)=-\frac{1}{2} \sum_{m, n} J_{m n} x_{m} x_{n}-\sum_{n} h_{n} x_{n}$).
Interpretation of (3) a relative entropy between the approximating distribution $Q(\theta; z)$ and the true distribution $P(\theta | β , J)$ plus the true free energy._ 

#### Connection with robustness
In the Bayesian workflow, the only fixed thing is Bayes formula (update) and sometimes the need for robustness as a resort. The rest, prior, likelihood, and posterior computation are all susceptible to chage. In this sense, connecting self-consistency with robustness seems promising. Let Q := AP i.e. $Q = \int_{\theta}\left(\int_{y} p_{2}\left(\theta^{\prime} \mid y\right) p_{1}(y \mid \theta) d y\right) P(\theta) d \theta$. Connection between the two formulation $\min \frac{\|\nabla_\theta Q\|}{\|\nabla_\theta P\|}= \frac{\frac{dg_{\theta}(x)}{d\theta}d\theta}{\frac{d f_\theta(x)}{d\theta}d\theta}$ (this is wrong!!) (robustness) and $\min \{\operatorname{div}(Q, P)-\Omega|\operatorname{supp}(P)|\}$ (widest self-consistent prior) can be made. The second term is the scaling factor and can be replaced with entropy:

$$
D_{KL}(P||Q) - S_P\;(S:\text{entropy})\\ = \int ln(\frac{dP}{dQ})dP + \int ln(dP)dP\\
= \int_{x \in R} ln(\frac{f(x)^2}{g(x)})f(x)dx \\
= \int_{w\in\Omega} ln(\frac{f(X(w))^2}{g(X(w))})dP(X(w))
$$
![](https://i.imgur.com/gCNefAS.png)


$f(x) = f(\theta; x),  f_\theta(x)$ integrate w.r.t x, differentiate w.r.t $\theta$
[Fractional programming techinques](https://en.wikipedia.org/wiki/Fractional_programming) where $min \frac{f(x)}{g(x)}$ is equivalent to $min \; tf(\frac{x}{t})$ s.t $tg(\frac{x}{t}) \leq 1$ could be applied to make the connection between robustness and widest self-consistency.

#### Connection with Bayesian calibration
The followings are stronger formulations assuming that the corresponding posterior samples would be close to prior sample for every data $y$. 
$$ \mu_1^{\text{best}} := \underset{\mu}{argmin} \int_{\theta} (\int_y I_{div(\delta_{\theta(\theta')}, p_2(\theta'|y)) < \epsilon} \;p_1(y|\theta) dy)  \mu d\theta - \Omega|supp(\mu)|$$
or
$$ \mu_2^{\text{best}} := \underset{\mu}{argmin} \int_{\theta} (\int_y div(\mu, p_2(\theta'|y))  \;p_1(y|\theta) dy)  \mu d\theta - \Omega |supp(\mu)|$$
The motivation for this formulation is that application of Bayesian calibration with the utility $U(a(y), \theta)$ set as  $I_{divg(\mu, p_2(\theta'|y)) < \epsilon}$ or $divg(\mu, p_2(\theta'|y))$ which is averaged over data, parameter joint space. The first component of $\mu_1^{\text{best}}$ measures the average instance of posterior samples being too far from each prior sample pointwisely. $\mu_2^{\text{best}}$ is an averaged divergence of a measure to simulated measure. The second component is an incentive for $\mu^{\text{best}}$ to have the largest support (within [0,1] if $\theta$ scale-invariant). In Bayesian calibration, simulated and ground truth are compared with $\bar{U}_{S}=\int \mathrm{d} y \mathrm{~d} \theta \pi_{S}(y, \theta) U(a(y), \theta)$ to measures how decision making process is within the scope of the modeling assumptions ([Betancourt, 2019](https://betanalpha.github.io/assets/case_studies/modeling_and_inference.html#33_bayesian_calibration)).  

#### Algorithm 1.
> 1. Prespecify finite number of data simulators ($G_{1..a}$)and posterior simulators ($I_{1..b}$). 
> 2. Calculate SCS for each combination of data and posterior simulator.
> 3. Eliminate $SCM$ that overlaps little with modeler's domain knowledge from $\{SCM\}_{1..ab}$.
> 4. Eliminate $SCM$ whose simulated $\tilde{y}$ overlaps little with modeler's observed data from $\{SCM\}_{1..c}$.
> 5. if the remaining $\{SCM\}_{1,..d} = \emptyset$: 
     -> Go to 1 with extended range of prespecification.
   else: 
>   -> se the combination with the least computation time.

In steps 4 and 5, “c” and “d” are indicating the subset of SCMs that are kept in the previous step. Here SCM is $\mu^{\text{best}}$.

#### Example
Here is an example that accompanies the algorithm. [The NYC cockroaches problem](https://github.com/jgabry/lander-stan-2020-public/blob/master/main.html) aims to optimize the number of traps; it starts with the prediction model where the response variable is the number of constraints and the predictor is the number of trap. Data simulators are the Poisson and negative binomial models ([stan code](https://github.com/jgabry/lander-stan-2020-public/blob/master/stan_programs/simple_poisson_regression.stan)) and posterior simulators are HMC and ADVI.
> $\begin{aligned} \text { complaints }_{b, t} & \sim \text { Poisson}\left(\lambda_{b, t}\right) \text{ or} \; \text{Neg-Binomial}\left(\lambda_{b, t}, \phi\right) \\ \lambda_{b, t} &=\exp \left(\eta_{b, t}\right) \\ \eta_{b, t} &=\alpha+\beta \text { traps }_{b, t} \end{aligned}$

From the prespecification, joint parameter space of $\alpha, \beta, \phi$ are domain of $SCM_\theta$. If the posterior simulator recovers the posterior space constructed by the data simulator perfectly, $SCM_\theta$ should be the entire joint space: $\forall (\alpha,\beta), \phi=0$ for Poisson and $\forall(\alpha, \beta, \phi)$ for NB. However, depending on the approximation assumption or posterior geometry, only part of them would be self-consistent. For instance, for centered parameterization hierarchical model with HMC, near-zero region of population scale parameter would be excluded from SCM due to funnel problem (this can be included in the extended prespecified combination after step5-i). $SCM_{1..4}$ are calculated from the procedure described in the next section. 

Between the two criteria to judge the SCM's fit with the modeler, which take place in parameter and data space respectively, as domain knowledge does not require additional computation it precedes the predictive check. As complaints would decrease with increased number of traps, SCS with nonnegative $\beta$ should be eliminated. Contrary to choosing the predictor that is well-identified by the real data, nonidentifiability suits the definition of SCM as this implies simulated data holds no additional information and therefore is well calibrated with parameters. 

For step 5, if no SCM remains, i.e. discrepancy between the observed data and the model predictions from even the best-fitting parameter values is unacceptably large ([Kennedy and O'Hagan, 2001)](https://rss.onlinelibrary.wiley.com/doi/pdf/10.1111/1467-9868.00294), the modeler extend the prespecified data and posterior simulator. Hierarchical models can be added for example. If multiple SCMs that fit modeler's belief and data are left, the one with cheaper computation is chosen. As long as the data and posterior sampler are on SCM and therefore self-consistent, different combinations function the same. The original SBC paper suggests ADVI could fail simple linear regression, but as long as the modeler's intended use is within or close to SCM, it could replace HMC perfectly. This provides a clear guideline on when modelers could use the approximate algorithm.


### Markov chain construction and its stationary measure $SCM$
Stationary measure $\mu$ defined as $\mu(y) = \sum_{x} \mu(x) p(x, y)$ is another interpretation of self-consistency in Simulation-based calibration (SBC): $p(\theta)= \int dyd\theta p(\theta|y) p(y|\theta)p(\theta)$. In fact ${\{\theta}\}_{1..N}$ constructed from description in Fig.2 is a Markov chain with transition probability $P(\theta, \theta') := \int dy p'(\theta'|y)p(y|\theta)$, namely $MC_{\mu_\theta}$. The sketch of proof for its convergence to stationary measure is given in [Appendix](##Appendix). The **self-consistency measure ($SCM_{\theta}$)** is defined as stationary measure $\mu_{\theta}$ of $MC_{\mu_\theta}$. Imagining a parameter region exclued from $SCM$ helps intuitive understanding; for centered parameterization hierarchical model with HMC, near-zero region of population scale parameter is transient in that once the chain starts from near-zero region, the probability of returning to the initial state infinitely often is less than 1. Markov Chain Monte Carlo $MCMC_{\mu_\theta}$ is used to get samples from $SCM$.

![](https://i.imgur.com/9cYTO7L.png)


*Fig.2 One data and posterior simulation constructs $\mu_\theta$ - Markov chain which converges to a stationary measure $\mu_{\theta}$.*


$MCMC_{\mu_\theta}$ is different from MCMC ($MCMC_\theta$) used for posterior sampler; although both are chains on $\theta$ space, $MCMC_{\mu_{\theta}}$ targets self-consistent measures while $MCMC_{\theta}$ samples represent typical measure. The two measures differ in that the former is a calibrated inference over a wide variety of possible future datasets while the latter is the output of a specific dataset.

Multiple methods as follows have been developed to accelerate and diagnose $MCMC_\theta$ as well as to transform for favorable estimation. This could be equally appled to $MCMC_{\mu_{\theta}}$ and left for further study. This is possible by designing a well-behaving kernel $p(\theta, \theta')$.
-- accelerate: parallel, coupling
-- diagnose: Rhat
-- variance reduction
-- bias correction: coupled kernel [Xu2021](http://proceedings.mlr.press/v130/xu21i/xu21i.pdf)

### Verificate with simulated data and validate with real data: 
![](https://i.imgur.com/viXS2BP.png)
*Fig.3 Canonical verification and validation process in simulation literature.*

Verification measures how well the model represents modeler's mental map. Once the modeler is confident the model could operate in an intended manner, it is validated under the real world setting (Fig.3). Given the modeler's intention is well-represented by the model, the validation is necessarily the test on the modeler's intetntion. 

In Algorithm 1, verification corresponds to step 2 while validation is step 3, 4, and 5-ii). From the view of prior and posterior differences, i.e. how well data informs the parameter, contrary to validation where large difference is recommended, verification requires minute differences - even identical. This results from the inherent difference between real and simulated data; the former which is an external test should ideally inform the model while this gap of information implies that the model is under-calibrated. Shrinkage observed in Fig.4 shows $\alpha, \beta$ is well-identified by the real data for simple Poisson regression example.
![](https://i.imgur.com/U5nNjZl.png)
*Fig.4 Using intercept and the number of trap as predictors is justified by the large shrinkage between the prior and posterior of $\alpha, \beta$ in simple Poisson regression model.*


However, when calibrating with fake simulated data, the state where data and parameters could fully explain each other (i.e. information is balanced) is desirable. Starting from the wide prior, one data-posterior simulation would show great shrinkage (left in Fig.5) at first but after several iterations, it would start to show less shrinkage (right) before converging to SCM where prior and posterior distribution are equal i.e. self-consistent. This coincides with our understanding of stationary and even reversible.
![](https://i.imgur.com/PFyYx1q.png)
*Fig.5 Decreasing prior to posterior shrinkage as we iterate fake data simulation.*

Data encode manipulation for decision models will be further covered in Discussion.

### Convergence diagnostics

![](https://i.imgur.com/CnpINvd.png)

*Fig.6 Comparison of a posterior distribution to the assumed true parameter value and expected symmetry of self-consistent set*

Calculating SCM needs convergence diagnostics which measure the closeness of $\tilde{\theta}$ and $\tilde{\theta'}$ set in Fig. 2. The two distribution being equal, $\mu_\theta = \mu_{\theta'}$, is a necessary condition for perfect convergence. SBC rank histogram and ECDF ([Säilynoja21](https://arxiv.org/abs/2103.10522)) are ways to empirically compare the two distributions. In the experiment, the variance ratio of every parameter within the range of 0.8 to 1.2 was used. Advantage of guaranteed convergence is that now the quality of one data-posterior simulator is allowed to be degraded to a computationally reasonable level; original heavy computation required at least a thousand prior samples. Instead cheaper simulation could be repeated. Deciding the number of $\tilde{\theta}$ samples and thereby tuning the approximation quality of the kernel $P(\theta, \theta')$ for the fastest convergence is left as future research.
Viewing $\theta'$ and $\theta$ on the same joint $\theta, y, \theta'$ space, a new random variable $\theta'- \theta$ could be inspected based on the defintion of symmetric random variable which is the signed random variable having the same distribution ($X\stackrel{D}{=}-X$). Distribution of ${\theta'_{nm} -\theta_{n}}$ and ${\theta_{n} - \theta'_{nm}}$ can be compared as an extension of SBC rank statistics: $\sum_{m=1}^{m=M} I({{\theta'}_{nm} < {\theta}_n})$. Fig.5 shows problems with checking model with a few true prior samples pointwise ([Gelman20](https://arxiv.org/abs/2011.01808)).  Expected symmetry, $p(\theta,\theta') = p(\theta', \theta)$, (proof in Appendix) at stationary measure could provide insight to further diagnostic design.
The speed of convergence could be quantified by counting the frequency of instances where two independent chains $X_n, Y_n$ hit the same binned region based on the following equation from MCMC convergence proof using coupling theory:
$\sum_{y}\left|P\left(X_{n}=y\right)-P\left(Y_{n}=y\right)\right| \leq 2 P(T>n)$ 

## Experiment
#### linear regression $y = \alpha + \beta * X$ 
```
$X
[1] -4.191990  4.911008 -4.143202 -4.128198 -5.908929
```
With the given predictor data above, Markov chain is constructed with data and posterior simulator following the steps in Fig.2.
![](https://i.imgur.com/Dz4ABtn.png)


1. Start with N samples $\tilde{\theta}$ from wide enough prior distribution, $N(0,10^2)$ from below. 

```{stan}
generated quantities {
  real beta;
  real alpha;
  beta = normal_rng(0, 10);
  alpha = normal_rng(0, 10);
}
```
2. Data simulator: generate sample $\tilde{y}$ from each simulated parameter in 1.

```{stan}
generated quantities {
  vector[N] y;
  y ~ normal(alpha + beta * X, 1.2);
}
```
3. Posterior simulator: infer parameter samples that best explain $\tilde{y}$ in 2.
```{stan}
model {
  beta ~ normal(0,10);
  alpha ~ normal(0,10);
  y ~ normal(alpha + beta * X, 1.2);
}
```
4. Start step1 with samples that approximate the previous $\tilde{\theta'}$ set. Normal distribution with same location and scale with the previous $\tilde{\theta'}$ is used as empirical distribution encode is not possible in model block (need improvement). Due to posterior summary, the exact format would be as follows:
![](https://i.imgur.com/sciRvVg.png)

``` {stan}
data { 
  real alpha_loc;
  real alpha_scale;
  real beta_loc;
  real beta_scale;
 }
```

5. Data and posterior simulator
```{stan}
generated quantities {
  alpha = normal_rng(alpha_loc, alpha_scale);
  beta = normal_rng(beta_loc, beta_scale);
  y = normal_rng(alpha + beta * X, 1.2);
}
```
then
```{stan}
model {
  alpha = normal_rng(alpha_loc, alpha_scale);
  beta = normal_rng(beta_loc, beta_scale); 
  y ~ normal(alpha + beta * X, 1.2);
}
```
7. Iterate 4, 5 until convergence with convergence measure: $\operatorname{Var}(\theta_{post})/\operatorname{Var}(\theta_{prior}) \in [0.8,1.2] \; \forall$ parameters 

- summarizing the posterior as median is not good as it would limit its exploration property.
- starting from the narrow prior should (driving force to outside)
- 
![](https://i.imgur.com/JLdFpgR.png)
*Fig.7 Comparing the first shrinkage to the last shrinkage of prior to posterior samples in linear regression + HMC.*

The linear regression converged after 7th iteration and the range has shrinked from [-5,20] to around [0,10] from Fig.7.

#### Normal conjugate test
X-axis is the number of iteration (for loop in [this](https://gist.github.com/hyunjimoon/6881d4d1e4c07b9867a8c908b5efc29d#file-sbc_mc-L33) code) and Y-axis is the quantile(.25, .75) of the resulting distribution of each step. Little distributional change before and after the iteration implies it has reached the self-consistent region but as you can see from Fig.8, the converged distribution all have different quantile value. 
![](https://i.imgur.com/1geXVLy.png)
*Fig.8 Quantile of the iterated measure $A^n\mu_0$.*

Even with the same number of prior samples (N), they converged to different distributions (different mean but same sd (=0) from Fig.9; contrary to the Fig.8 figure, plots are mean and sd). 

![](https://i.imgur.com/4wQN2Mk.png)
*Fig.9 Sample number of prior samples but different converging region.*

(will be added)
#### Poisson $P_1(Y|\Theta)$with laplace approximation $P_2(\Theta|Y)$

![](https://i.imgur.com/9NsUROs.png)

## Discussion
### Data encode for decision model

If the data gives information on the parameters' sign but not its scale, which is called latent data, this encoding could be improved. Data space should evolve toward the decision space.

> Arsenic example
 
Constructive choice models explain that with direct data manipulation, decision function that maps data to action could be learned; this is different from the a_D$, is the decision parameter on which the number of complaints depend. First, the complaints prediction model with  with predictors such as traps, building id etc are built. The last cost optimization is performed by $\underset{\theta_D}{argmax} \; p(\theta_{D}|\tilde{y}, \tilde{\theta}_{D})$.

```
(In progress)
However, this rests on the assumption that past decisions are reliable in that each decision maker has chose the option with best utility based on their unknown utility coefficient, (a,b,c). 

where $p(\theta_{D}|\tilde{y}, \tilde{\theta_{D}})$= P(I_{\underset{\theta_D }{\operatorname{argmax}}E_{p(y| \theta_D, \tilde{y}, \tilde{\theta}_D)}[U(y|\theta_D)]})$ 
Decisions are encoded as response variables and  while we see are the decisions (y i= 0 or 1) for households, given their arsenic levels As i and distances x i to the nearest safe well.
• $a_i$ is the beneﬁt of switching from an unsafe to a safe well, while $$
• b i + c i x i : the cost of switching to a new well a distance x i away.
the best is an understand the relation between distance, arsenic level, and the decision to switch

just as prediction function that minimizes the loss  decisions , model a decision outcome as a balancing of goals or utilities.
```

### Representation update

### Intention, encode update

### Predictor dependent VS independent SCM in practice

## Future research

Long term goal:
Stochasticity is introduced either to express additional uncertainty or to substitute the original solution with cheap iterations; Bayesian and stochastic optimization are examples for each purpose. Validation is defined as “the process of determining the degree to which a model is an accurate representation of the real world from the perspective of the intended uses of the model.” (National Academy of Sciences report). However, due to the uncertainty underlying the intention and difficulty in finding the correct representation, stochasticity could be wisely included in the data exploration workflow from which the modeler's intention and model's representation could both evolve. Modelers can calibrate their goal based on simulated decisions and model can improve its ability to sample decisions based on the provided feedback from modelers. This is based on three observations: i) what we call "model" is actually the composition of multiple components such as model space specification, density, and approximate computation, ii) every unnecessary layer of composition leads to information loss, and iii) users are uncertain about their interests. An additional update algorithm that is paired with Algorithm 1 is required for encode update. Fig.8 and 9 suggest two views on this paired update of model and modeler.

2025-01-04 
![[Pasted image 20250104192009.png|100]]
in the context of A2E and E2K from [[🗺️abD.agent's belief and desire to equity valuation]], I returned to this detailed balance idea after three years. i summarized chat with this gpt which includes above balance between society's symbolic level and individual's algorithmic in one paragraph as follows. **Detailed balance** ensures that exploration and exploitation remain in “dynamic equilibrium” by maintaining equal “flow” in each direction. Concretely, if you switch from exploring new possibilities (A2E) to refining a known path (E2K) at a certain rate, then you allow a symmetric path back from E2K to A2E. This balancing act helps a modeler (and their model) avoid getting stuck in one mode or discarding prior gains; any time you invest in exploitation remains valid if you later decide to reopen the search. Mathematically, this is captured by saying the probability of being in A2E times the chance of moving to E2K equals the probability of being in E2K times the chance of moving back to A2E. By regulating how often (and how easily) you pivot between modes, detailed balance keeps the entire process “least‐irreversible”—no knowledge or flexibility is lost, even as you iterate, validate, and evolve both your intentions and your model’s representation.

![](https://i.imgur.com/WK6jzFH.png)

*Fig.8 Bottomup view: Evolving parameter, measure, and replicated data with MCMC.*

![](https://i.imgur.com/rE1Mag0.png)

*Fig.9 TopBottom view: how $t$ is selected and how replication systems are constructed.*

### Hierarchical model
> “Theorem” 2. Suppose we have a hierarchical model so that the parameter vector theta can be divided into a long vector of local or latent parameters, xi, and a short vector of hyperparameters, phi, so that the full prior is p(theta) = p(phi)p(xi|phi). Now suppose we start by drawing phi_tilde from some alternative distribution, g(phi), then draw xi_tilde from p(xi|phi_tilde) and y_tilde from p(y|phi_tilde, xi_tilde). The theorem is that the posterior simulations will still be approximately calibrated for the parameters in xi in the limit as the dimension of xi increases. Here the idea is that we could have weaker conditions on g(phi), compared to theorem 1.

The parameters could be views as $\theta$ as a whole but, structural condition such as conditional exchangability could be used to modify $MCMC_{\mu_\theta}$. This could have a connection with Theorem 2 suggested by Andrew.

![](https://i.imgur.com/R1kx11I.png)
*Fig.10 Detailed balance $p(\phi)p(\phi|\theta) = p(\theta|\phi)p(\phi)$ could be used to extend the Markov chain further.*



## Appendix 
### $MCMC_{\mu_{\theta}}$ Convergence
Update of $\theta$ could be described as a discrete-time Markov chain on a compact set $\Theta$ with its transition probability defined from the generate-inference process: $y_{n} \sim p\left(y \mid \theta_{n}\right), \theta_{n+1} \sim \alpha\left(\theta \mid y_{n}\right)$ 
Inference step with Markov kernel, ie.$p(\theta, \theta')=\left(\int_{y} \alpha(\theta' \mid y) p(y \mid \theta) d y\right)$ defines a probability density for all $\theta$ which leads to the existence of invariant measure $\mu(\Theta)$ and stationary distribution, $p(\theta)$. Condition for changing the stationary measure to distribution and the level of requirement for convergence between stationary and reversible remains to be decided.

$$\sum_{\theta} \mu(\theta) p(\theta, \theta')=\mu(\theta') - \text{stationary} \\
\mu(\theta) p(\theta, \theta')=\mu(\theta') p(\theta', \theta) \quad \text { for all } \theta, \theta' - \text{reversible}
$$
--

### Does it converge? Feedback

$K(\theta’, \theta) = \int dy p_{1}(\theta’ |  y) p_{2} (y | \theta)$ can be considered a Markov kernel (assuming that the densities are nice enough).  If $p_{1}$ and $p_{2}$ are related by Bayes’ Theorem then the unique stationary distribution of this kernel is the prior model.

you want to define some effective prior as the stationary distribution of $K(\theta’, \theta)$ when $p_{1}$ and $p_{2}$ are not related by Bayes’ Theorem, in particular when $p_{1}$ is defined implicitly by some computational method capable of generating samples.

There are a few technical issues with this approach:

1. Even if you can define a Markov kernel there’s no guarantee that the kernel supports _any_ stationary distribution, let alone an invariant one.  To ensure that a stationary distribution exists and is unique one has to verify a few technical conditions (irreducibility, aperiodicity, and ideally some minorization result to get Harris recurrence).  This is straightforward when engineering explicit Markov kernels, but it become much more challenging if even possible when the kernel is defined implicitly.

2.  Even if a unique stationary distribution exists running Markov chains to explore that distribution is no easy task.  Again there are various technical conditions that need to hold in order to ensure that the Markov chains characterize the stationary distribution reasonable well in finite time; you can always run Markov chains, but the finite-iteration behavior is not always a useful characterization of the stationary distribution.  These are really hard even when the kernel and the target density are known explicitly.  Moreover, even if everything works the stationary distribution will be characterized only through samples, and trying to convert those samples into some explicit prior model representation like a density function is really, really hard especially in more than a few dimensions.

3. My biggest hesitation, however, is in the relationship between $p_{1}$ and the stationary distribution.  In the standard Bayes case $p_{1}$ and $p_{2}$ are related to each other _and the stationary distribution_ by the prior model.  In other words $p_{1}$ can’t be defined without knowing the stationary distribution already.  In your proposed method this will no longer be the case.  
> strategy could be to show continuous property of $p_1$ (06.03)
 
In particular say that $p_{1}(\theta | y)$ is defined as approximate posterior computation for the observational model $p_{2}(y | \theta)$ and some default prior $p_{0}(theta)$, and you find a stationary distribution $p_{3}(\theta)$.  If you then use $p_{3}$ as the prior model in an analysis then the posterior distribution you need to compute will be

$posterior(\theta | y) = p_{2}(y | \theta) p_{3}(\theta) / normalization != p_{1}(\theta | y) = p_{2}(y | \theta) pi_{0}(\theta) / normalization$.

Said differently the “consistency” defined by the stationary distribution doesn’t actually say anything useful about how that stationary distribution would be useful as a prior model.

#### B. Automorphism
Finding measures preserved by a given operator can be better understood by observing its somewhat dual: measure-preserving function group on $\mathcal{W}_{p}(\mathcal{\Theta})$ (space of measures on $\Theta$)

$$
Aut(\mathcal{W}_{p}, msr):=\{A|A\mu = \mu \;\; \forall \mu \in \mathcal{W}_{p}\}\\
\mathcal{W}_{p}(\mathcal{\Theta})=\left\{\mu \in P(\mathcal{\theta}): \int_{\mathcal{\Theta}}\|\theta\|^{p} \mathrm{~d} \mu(\theta)<\infty\right\}
$$
$Aut(X)$ is larger than $Aut(X, |.|):= \{f|f:\text{bijective}, |f(x)| = |x| \; \;\forall x \in X \}$. $Aut(\mathcal{W}_{p}(\mathcal{\Theta}))$ shrinks if preservation of $X$'s structure is required e.g. norm-preserving $Aut(\mathcal{W}_{p}(\mathcal{\Theta}))$. $SCS(A)$ expands as $A$ becomes regularized; regularization meaning bounded and smooth engouth to guantee the convergence of $A^n\mu$.