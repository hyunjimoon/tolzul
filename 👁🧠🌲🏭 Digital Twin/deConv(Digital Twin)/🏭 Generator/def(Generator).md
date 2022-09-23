
## What
`Generator` is dual of [[def(Discriminator)]] which is the same logic as `simulation` is dual of reality. Refer to [[Dual and Twin]] for further discussion on how twins are created.

Compared to famous Harry Potter quote, neither can live while the other survives, twin relation is much symbiotic in that "neither can be defined without the other".

## How
### Explicit and Implicit Generators
A Generative *Adversarial* Network defines a generator network. In our context, the generator is defined by the Stan model and/or the System Dynamic model. 

### Loss function and training

Generator decodes convoluted `Discriminator` which decides authenticity. This explains the inverse of convolution i.e. deconvolution operation that `Generator` need to master.

Loss function encouraging constant contest between the generator and  can ensure convergence to optimal point. minimax is representedConversely, we may potentially use the  as an objective function to train our parameterized generator, in the sense of bayesian optimization.

## Why