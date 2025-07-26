###### tags: `calibration`
# Contraction experiment
0715
![](https://i.imgur.com/nJAZTVu.png)


non-sc
![](https://i.imgur.com/Fe534yW.png)
"pval: 0 max_diff: 1.77 wasserstein: 1.096"
max_diff: 1.775 wasserstein: 1.096"
sc

0606
![](https://i.imgur.com/ru6gfov.png)
*unstable with big sigma: converge to different invariant measure*



- When sd for noise and prior are similar in scale, no contraction; early convergence
![](https://i.imgur.com/PAJKxLB.png)

- $\mu_0 \sim N(0,.5^2)$
- $p_1: y|\mu_i \sim N(\mu_i ,1^2)$
- $p_2: \mu_{i+1} = \mu_i|y \sim N(a,b^2) \text{  perfect sampler with}$
$$
\\
a = (y * s^2 + m * \sigma^2) / (s^2 + \sigma^2)\\
b = \sqrt{s2 * \sigma2 / (s2 + \sigma2) }
$$
With multiple data simulations, exploration motivation could be low.



![](https://i.imgur.com/kUrsbHw.png)
- $\mu_0 \sim N(0,10^2)$

Converged after 17 iteration
![](https://i.imgur.com/89K8UBg.png)
With tighter prior sd from 5 to 1, 
- iteration: 17 -> 12
- 
![](https://i.imgur.com/UhKkhOa.png)



sequence of variance ratio
![](https://i.imgur.com/dm8aV0u.png)
![](https://i.imgur.com/VRRddgJ.png)

Same fixed point?
![](https://i.imgur.com/sW6yBPQ.png)

First contraction is large. Goes up and down for complex models.
![](https://i.imgur.com/kUsp8ES.png)
## hierarchical model (eight school) 
much harder to converge with greater number of parameter: took 222 
![](https://i.imgur.com/q3s3sqU.png)

![](https://i.imgur.com/O5qogob.png)


![](https://i.imgur.com/pQXPuNj.png)

![](https://i.imgur.com/mrxM6UN.png)
