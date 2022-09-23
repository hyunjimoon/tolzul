- Added random variable in each layer of the tree is modeled as convolution; i.e. the following four are equivalent.  From [[Efron computer age stat inf]] Chp.21, Bayesian deconvolution. $f$ is a distribution function on $Y$ and $g$ is distribution function on $\Theta$.

$f=g * \mathcal{N}(0, \sigma^{2})$
$f_{i}(Y_{i})=\int_{\mathcal{T}} p_{i}(Y_{i} \mid \theta_{i}) g(\theta_{i}) d \theta_{i}$
$Y_{i}=\Theta_{i}+Z_{i}$
$\phi_{f}(t)=\phi_{g}(t) e^{-t^{2} / 2}$

![[Pasted image 20220605181013.png]]
- convolution and deconvolution are the machinery underlying generative adversarial network (GAN). For the constant contest between actor (`generator` which generates new data) and critic (`discriminator` which evaluates them for authenticity), the two components of GAN adopt inverse structure of the network. `generator` is inverse convolution network whereas `discriminator` is convolution network.
- [transpose](https://www.engineering.iastate.edu/~julied/classes/CE570/Notes/strangpaper.pdf) is the underlying principle for inverse (recalling singular value decomposition, operator `A`and `A^{t}` have opposite direction (base to singular vector and its reverse) but the same scaling.

