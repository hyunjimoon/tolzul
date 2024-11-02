2. Simulation-based calibration checking

In this section, we introduce notation and describe simulation-based calibration checking [Cook et al., 2006, Talts et al., 2020, Modrák et al., 2024], which we extend in our recalibration procedures. We will use the notation $M$ for the model that we are trying to fit, $\theta$ for the parameters in the model, $y$ for the data, $M^{\prime}$ for the approximate computation, and $g(\theta)$ for a scalar quantity of interest. For simplicity, we take $g(\theta):=\theta$, though our methods are easily extensible to more general $g$.

A natural way to check if the posteriors are correct is through simulation-based calibration checking as follows:
```
Algorithm 0 Simulation-based calibration checking
    Requires Models $M, M^{\prime}$, constants $L, S$
    Obtain $L$ independent draws $\theta^1, \ldots, \theta^L$ of $\theta$ from its prior distribution in model $M$.
    for $l=\{1, \ldots, L\}$, in parallel do
        Take $\theta^l$, one of the draws of $\theta$ from step 1 .
        Draw $y^l \sim P\left(y \mid \theta^l\right)$ from the data model in $M$.
        Fit $M^{\prime}$ to $y^l$ to obtain $S$ independent approximate posterior samples, $\theta_{\text {post }}^{l, s}, s=1, \ldots, S$.
        Determine the quantile $q^l$ of $\theta^l$ in this distribution, that is, $q^l=\frac{1}{S} \sum_{s=1}^S 1_{\theta^l>\theta_{\text {post }}^{l, s}}$
    end for
    If the model is fit exactly (that is, if $M^{\prime} \equiv M$ ) and the simulation draws are independent, then
    $q^1, \ldots, q^L$ should be i.i.d. random draws from the uniform distribution on $[0,1]$.
    Compare $q^1, \ldots, q^L$ to the uniform distribution on $[0,1]$. A discrepancy indicates miscalibration.
```
Simulation-based calibration checking [Talts et al., 2020, Modrák et al., 2024] relies on the wellknown observation that the data-averaged posterior and the prior are self-consistent [Cook et al., 2006]: for the prior distribution $\pi(\theta)$ defined over parameters of interest $\theta$, and $\theta^l \sim \pi(\theta)$, and $y^l \sim \pi\left(y \mid \theta^l\right)$, then by construction $\left(\theta^l, y^l\right) \sim \pi(\theta, y)$ so that
$$
\theta^l \sim \pi\left(\theta \mid y^l\right) .
$$
In other words, the parameter $\theta^l$, which was drawn from $\pi(\theta)$, can also be thought of as being drawn from the posterior $\pi\left(\theta \mid y^l\right)$. Checking calibration is ultimately verifying that $\theta^l$ appears to be sampled from the posterior $\pi\left(\theta \mid y^l\right)$, which can be done by comparing $\theta^l$ with independently drawn samples from the actual posterior, $\theta_{\text {post }}^{l, s} \sim \pi\left(\theta \mid y^l\right)$. From this we obtain the condition used in SBC to check for calibration:
$$
\pi(\theta)=\iint \pi\left(\theta^l\right) \pi\left(y^l \mid \theta^l\right) \pi\left(\theta \mid y^l\right) d \theta^l d y^l
$$

In this paper, we go beyond the above SBC procedure. We don't want to just identify problems with calibration; we would also like to obtain roughly calibrated intervals.