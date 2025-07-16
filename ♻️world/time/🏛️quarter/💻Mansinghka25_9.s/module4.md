---
date: 2025-03-18
---
### digesting
2025-04-24
discussed with [[katie_collins]]

[[cul_collab_cap_seg_eval]]
And the basic way we do that in policy programming is we make latent variables by writing a generative process, example for the noise, and then we write a little recursion called generate random DSL program, which chooses which structure of node we're going to have, like a constant or a sum or change point or other primitive types, and then generates the parameters, and if needed, recurses to generate the remainder of the structure.  

if we just look at a sequence of successive samples from these probabilistic programs, what we see are periodic, smooth, linear and other. So realizations the stochastic process, really broad space. So he has a very small, compact symbolic object on the right that's parameterizing a very broad ignorance prior an enormous space of model structures, and then also even more enormous space of realizations of models, because the structure doesn't say, oh, there's like periodic doesn't mean simulated. Periodic means some latent function whose structure itself repeats. There's really just an enormously broad space of possible law enforcement, concise symbolic description. 

Another way to look at it is to actually evaluate the prior probability for program sorted by length, which is one heuristic measure of complexity. So it's kind of fun to see that and to try to get some intuition for it. for people here who are interested in some of the really fundamental questions of learning with probabilistic programs, this really needs a lot more study. So one thing I'll just note,⭐️ we don't know what happens to this model class as you truncate the prior, you limit to depth one, def two, def three. Probabilistic programs where you limit the precision and the priors on the parameters. ⭐️

So basically, as you limit the information content in the model itself, what does that do to the posterior over parameter? I think if we were to try to get a deeper understanding of sort of so this is what they think theoretically interesting, but in my mind, it's related to a very important practical topic, which is, you know, ⭐️this class of models is syntactically very, very simple, but it's semantically very expressive. You know, one way we could try to make an intelligent system learn to generate time series, to generate deterministic programs that might be very complex and sometimes make choices and if we wanted to give causal mechanisms for processes that generate time series data, those might be extremely complex, but that's not What we're doing. 

Instead, we're ⭐️generating generative programs that are highly stochastic⭐️, vastly oversimplified surrogates for whatever was really happening. That's to say they're ⭐️not causal⭐️. I mean, they may have some elements of causality, like the change point, might accurately capture just a very limited, basic fact that at some point, the future is independent of the past. Is something exogenous change, but I think ⭐️they're completely non causal, but they're pretty phenomenological⭐️. I guess they don't have much in the way of mechanism, certainly not explicit mechanism. I think there's something quite interesting here about probabilistic models that are semantically very expressive, but syntactically, very simple. 

This will come back a couple more times in the seminar, especially people who are interested in engineering learning systems that are very general, or understanding how the mind can get so much from so little and so many domains. 

### digested
generate (not information is data; )
synthetic proxy that has all the information during some definition of all it contains the real data, even though it's a synthetic proxy. So we'd like representations that we can modularly edit and censor to control the information volume and still generate accurate synthetic data.

random variable ; time series structure (GP) better than transformer and lstm (intuitive calibraed error bar)

e.g. DSL linear covariance function with parameter value 1.0; 
input time points, time series structure, noise level, time series values 
x[i], x[j]

execution trace (inofmation of xi cocme from xi-1) 

sigma - 

visualize on execution 

### periodic
periodic (product of periodic kernel

change points (costt, linear)

sauared expoinentioal
x = vector {float64} (undef, length(t))
 repeat
how do we fill in the hole in the data

linear, period, 
online inference alg. fill in the hole, 

average the predcitionto account for un ()
smoother, more graded transitions between models that are clearly unstructured to models that impose kind of greater, successively greater degrees of structure.

🙋‍♀️hypothesis on additive vs multiplicative (prohet vs neural prophet)
🙋‍♀️ CP vs NCP: frequency of models (e.g. out of 100 program how many of them include cp?)

fit to data and model complexity (sine wave vs linear); 

posterior infernc based on marginal likelihood

why sfin
posteiror inference is helpful (betting process 

language L,  structure S, theta DSL program paraemters, latent variables z, observed varaibles 

sufficient condition 

probabilistic program synthesis largely possibl e in general setting
 take data and synthesis and see halut
 efficient noise possible in 
 can't have arbitrarily deterministic; prior halts with probability 1. 
parameter is usually higher and initie dimension so we need stutruect tob e first set then parameter dimension can be set within that

learning of libraries not only program, 
🙋‍♀️ rationality doesn't apply to dreacoder

exploiting sparsity to be efficient
Bayesian sampling over model structure and parameters.
modle selection for rich class of structure (low performance and high complexity)
automation we can discover (program synthesis)

automatic differentiation, and really how that enabled easy exploration of deep learning methods

what's DSL and EPSILON?
generate _random_dsl program

limit information of poetioer (effective) - as you sort of limit the information content in the model itself, what does that do to the posterior over parameter?

some elements of causality (might accurately capture just a very limited, basic fact that at some point, the future is independent of the past. Is something endogenous change)

semantic: universal approximator; syntax: stan has five types of block (data, transfomed parameter parameter, model, generative)

computational: sampling
tractable learning: language flexible levels of detail approriate to their domain (cover different range of model; architecture of)

syntaxically 
smen

"joint posterior over model structures and parameters. Does not concentrate on the high on the model, but assign the highest likelihood to data."

uniformity

broad coverage prior 
when desinign DSL, how did you observe  human behavior? e.g. over time human may have converged to good  much of -  time serise, 3d perception, relational data)

🙋‍♀️🙋‍♀️🙋‍♀️
1. when your team developed DSL for time series, 3d perception, relational data, how much did you observe  human behavior (time series modelers, robotics, )? 
2. is starting from observing human's use case/behvior helpful for designing DSL? bitter lesson?
burtler ramsey: modularity, prolog
## sol1: automation via program tracing AD
reversible jump mcmc 
hard to compute and takes many iteration to converage

walk tree, gernate sub expression + subtree involution (reads from one model and compy data into auxilabry model)

efficient implemenation 
use cases - 
## sol2: exploit spasitiy

## sol3: scaling smc (mcm rejuvanation)

prediction errror 1, 10, 30 mcmcm

initina  in the model ; load x and y + do smc + loop (effective sample size, resamble )
inference time compute graph (smc + rj-mcmc + hmc)

only smc -> collapses 

two versions in parallel : cheap and cheerful (e.g gpt 3) and deep and rational (gpt 4.5)

gen sp (estiamtor of ratio) - class of approximation; unbiased estiamtor is still sound (don't reduce convergence rate but improve it)

learning desing tricks for gen sp


+ simulation based calibraion + dependency dependent back tracking (contradiction) - which variables are relevant to that contradiction (some variable that can resolve the problem)
- dependence structure of the trace and then information flow the distributions, because the prompt is a really interesting firm I think trial would be a different person in particular.

josh's question on smc + rejuvanation weird as they are correlated and vkm's emphasis on joint inference on (epsilon, structure 

suggestion on using statistican's residual

- it'd be too hard to get to distinguish between idiosyncrasies of the implementation or conceptual fashion

other domains where ppl might be helpful

ChiExpert: augmenting every database with trustworthy ai expert system
oncology, board software develoer survey

large population - IPUMS

🙋‍♀️🙋‍♀️🙋‍♀️🙋‍♀️ how dose synthetic data be differentiated from imputation?
