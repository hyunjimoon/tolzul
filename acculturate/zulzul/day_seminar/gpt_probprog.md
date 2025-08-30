![[Pasted image 20230810121423.png]]
![[Pasted image 20230810121430.png]]

given the previous (xb[b,t]  65) - categorical_logit_lpmf: cross-entrophy loss (log loss)
![[Pasted image 20230810121525.png]] 
 replace (urng through language modeling head - butn in to bigger [vocab_size] - mixing up); not putting prior; still doesn't look back although have some mixing up
![[Pasted image 20230810121708.png]]
x[b] is using position embedding (not using much history, but only position)
![[Pasted image 20230810121950.png]]
key, query, value (function `self_attention`)
![[Pasted image 20230810122124.png]]
key is what it refers to, mix them up (what does "it" related to? in query? -- > "animal" among key)
![[Pasted image 20230810122201.png]]
input is key, query and scaled dot product self-attention (q x k' - single number); encoder: lower triangular matrix; key is batch_size, query is block_size; 
![[Pasted image 20230810122319.png]]
![[Pasted image 20230810122620.png]]
each of the are different keys ("it" was related to animal, didn't, cross - ; have mutiple keys)
![[Pasted image 20230810122647.png]]
skip connection (computation tricks) ![[Pasted image 20230810122842.png]]

data X (all sorts of shape and dimension), parameter also multidimensional
statistical model links data and parameter (higher is better ; log_loss; logit)

![[Pasted image 20230810123023.png]]

inference is separate
![[Pasted image 20230810123119.png]]

update subset of parameters -> stochastic optimization (practical concern - fit data is too large); for hierarchical model, hyper variance component (pptimality happens in the region that violates modeling assumption) goes to zero
- sometimes you know how good your approximate algorithm
![[Pasted image 20230810123551.png]]

![[Pasted image 20230810123834.png]]
> How do you know the approximate inference algorithm is good and matches reality? - tamara broderick (quantify ) - advi approximate (unconstrained scale - multivariate normal; both advi and hmc perform well under the same condition)

 > hi Dan, great talk, wondering if you could speak more to the "batching" of the data when using L-BFGS, how small are you making it, and what's the rationale based on the iterative parameter updating. Seems like that would be a real challenge to get to work properly and quickly at the same time.

> Bruno Pajusco: Another potential issue is heteroscedasticity in the data. Grammar doesn’t change over the years that swiftly but other datasets are non stationary
1. theses thoughts are on priors (hierarchical models) two moon (subnetworks that work on different dataset) - rotate -> hierarchical model (structured prior that we can learn; hallucination) https://twiecki.io/blog/2016/07/05/bayesian-deep-learning/
2. classification changes overtime - rotating ; model update; https://twiecki.io/blog/2017/03/14/random-walk-deep-net/

gpt with probprog
probprog with gpt: causally reason about
