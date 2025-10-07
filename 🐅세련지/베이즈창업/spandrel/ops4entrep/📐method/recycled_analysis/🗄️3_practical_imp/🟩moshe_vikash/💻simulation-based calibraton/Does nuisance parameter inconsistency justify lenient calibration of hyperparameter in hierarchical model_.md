###### tags: `consistency`, `marginal`, `hierarchical`, `calibration`
# Does nuisance parameter inconsistency justify lenient calibration of hyperparameter in hierarchical model?

Goal: 
1. Can nuisance parameter viewed as hyperparameter? 
2. If so, does the former's inconsistency explain the weak calibration condition for hyperprior from Andrew's [observation](https://statmodeling.stat.columbia.edu/2021/01/18/simulation-based-calibration-two-theorems/):

> Thm.2. Suppose we have a hierarchical model so that the parameter vector $\theta$ can be divided into a long vector of latent parameters, $\xi$, and a short vector of hyperparameters, $\phi$, so that the full prior is $p(\theta) = p(\xi|\phi)p(\phi)$. 
>
> 1.  $\tilde{\phi} \sim g(\phi)$ (alternative distribution) 
> 2. $\tilde{\xi} \sim p(\xi|\tilde{\phi})$
> 3. $\tilde{y} \sim p(y|\tilde{\phi}, \tilde{\xi})$.
> 
>  The theorem is that the posterior simulations will still be approximately calibrated for the parameters in $\xi$ in the limit as the dimension of $\xi$ increases. Here the idea is that we could have weaker conditions on $g(\phi)$, compared to theorem 1.

 3. Can this be exaplained with identifiability: $p(\xi|\phi)$ is much identifiable than $p(\phi|\xi)$?
### Marginalize joint via channels with different identifiability
Two marginalizations exist starting from $\xi, \phi$ joint distribution. Let's denote $\phi$ as nuisance parameter. Nuisance parameter is a parameter needed for model construction but as we are not interested in its inference, it is integrated out (BDA Ch.4). If its inference is of interest, framing the two $\xi, \phi$ as major and minor parameters might be safer. The first marginalization is $p\left(\xi \mid y\right)=\int p\left(\xi \mid \phi, y\right) p\left(\phi\mid y\right) d \phi$. LHS $p(\xi| y)$ can be interpretated as a mixture of the conditional posterior distributions given the nuisance parameter, $\phi$, where $p(\phi| y)$ is a weighting function for the different possible values of $\phi$.

Likewise, the joint can be integrated out along the axis of main parameter: $p\left(\phi \mid y\right)=\int p\left(\phi\mid \xi, y\right) p\left(\xi \mid y\right) d \xi$.

Compared to $p\left(\xi \mid \phi, y\right)$, channel for the first marginalization, let's say the second channel $p\left(\phi\mid \xi, y\right)$ is noisier and less identified (observational model π(y;θ) with observations y∈Y and model configurations θ∈Θ is _identified_ when the two distinct model configurations θ1≠θ2 implies π(y;θ1)≠π(y;θ2)) and degenerated. This could lead to the effect of posterior concentration as data increases much stronger for $p(\xi|y)$ compared to $p(\phi|y)$. For identifiability and degeneracy, refer to Mike's [ writing](https://betanalpha.github.io/assets/case_studies/identifiability.html).

Similar argument could be made in $p(\phi|\hat{\xi}, y)$ which has MLE-MAP relation with $p(\phi|y)$.

### Relation between Generate and Inference 

Proposition: $p(\xi|\phi)$ is better than $p(\phi|\xi)$ for both generate and inference steps, i.e.$p(\xi|\phi, y), p(\xi, y|\phi)$ are more identifiable than their counterparts $p(\phi|\xi, y), p(\phi, y|\xi)$ 

- From inference step, $\int p(\theta|y) p(y) dy = p(\theta)$, information encoded in data cannot be efficiently delivered to specify (i.e. tighten) the targeted posterior $p(\phi|\xi, y)$ due to its unidentifiable density (~ non-independent setting) leading to inconsistent $\phi$.
- From generate step, $\int p(y|\theta) p(\theta) d\theta = p(y)$, $\phi$ is slippery and therefore, downstread data ($\xi, y$) can equally well-explained by different distributions of $\phi$. This could explain the weak calibration conditions for hyperprior.

Connection between the two is not clear for now whose plan is described in [todo](https://hackmd.io/Od4SXN9-TEyfdB6fwskbEA?both#TODO-Hyunji) below.
### Questions (to Ryan):
- How would you define the difference between latent and nuisance parameter? Would the amount of interest in their inferece be the main difference? e.g. we are interested in latent parameter inference such as logit Bernoulli latent gaussian process where latent parameters are personal cancer contraction risks (prostate cancer dataset from [here](https://arxiv.org/abs/2004.12550)). 

- Is g from your nuisance parameter problem, group index? Are you using hiearchical model?
 ![](https://i.imgur.com/TvmEHtN.png)
(z is a random effect such as day, pollster)

- Do you think identifiability/degeneracy is related to inconsistency?
- If so, is the following arguement valid? 
> Similar argument could be made in $p(\theta_2|\hat{\theta_1}, y)$ which has MLE-MAP relation with $p(\theta|y)$. 

### Some references
- (You may already know but) Ch.15 (Hierarchical linear model) of Bayesian data analysis (Gelman et.al.) textbook includes election modeling. It also discusses exchangability in greater depth - somewhat related to the discussion of your talk.

- I think connection between inconsistency and identifiability can be found from Thm2 of [Inconsistent Estimation and Asymptotically Equal Interpolations in Model-Based Geostatistics](https://www.tandfonline.com/doi/abs/10.1198/016214504000000241) 

![](https://i.imgur.com/3cRf9t5.png)


### TODO (Hyunji) 

- interpretation from two coding schemes:
-- source coding (learn P given $X_{1..N}$, how much information does a signal contain?)
 ![](https://i.imgur.com/e9ByOHp.png) 
 -- channel coding (learn f given $X_{1..N}$, how much information can a noisy channel reliably transmit)
 
![](https://i.imgur.com/2g8QeVr.png)

- connect the two failures:
1) inconsistent and unidentifiable channel $p(\phi|\xi)$ 
2) non-iid & conditional independent structure of $p\left(\phi\mid \xi, y\right) p\left(\xi \mid y\right)$ from $p\left(\phi \mid y\right)=\int p\left(\phi\mid \xi, y\right) p\left(\xi \mid y\right) d \xi$.

- related keywords:
-- unidentifiable mixture and hierarchical model 

EOD

![](https://i.imgur.com/1TB8SXd.png)
Would searching for papers that uses latent variables and proves asymptotic unbiased work?

My closest experience on nuisance/latent parameters was latent gaussian process (with poisson or bernouli likelihood with inverse log and logit link).
F(x) is marginal over z, not condition given the random effect.

![](https://i.imgur.com/YWTKywf.png)