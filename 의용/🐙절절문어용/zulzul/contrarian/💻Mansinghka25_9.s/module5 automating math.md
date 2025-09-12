---
date:
---

to productize theories from [lew25_auto(math(integ, diff)).pdf](https://github.com/user-attachments/files/19142533/mit-vkm-class-lecture-3-4-25.pdf), [🗣️: vikash seminar_alex_automate_math.txt](https://github.com/user-attachments/files/19142536/vikash.seminar_alex_automate_math.txt), angie mapped selling strategy of probabilistic program:

![[Pasted image 20250330115139.png]]

to test my mental model, i asked feedback to friends in prob.comp:

matin gave feedback:
> It is a little tough to decode for me, but here is a paragraph-by-paragraph breakdown.1. I generally agree with the first paragraph.2. I don't probcomp follows a specific strategy that is outlined in the entrepreneurial strategy course at MIT. I think it is a research lab. More importantly, I "quality of users" is never a consideration in probcomp (or at all in PL) in my experience.3. I mostly agree with the "responsible deployment" angle. One thing that is missing is extending LLMs with capabilities they currently don't have, for example formal reasoning. Another thing to note is that probcomp is not an LLM lab.4. I don't immediately see how automation incentivizes vertical integration. This might be because I just don't know enough about economics. Please let me know if there is a standard reason why.5. I generally agree with the last paragraph, although presenting a general-purpose language to users is in principle more attractive than presenting a set of DSLs, but pragmatically no general-purpose language works well enough for general AI engineering via probabilistic programming.

hopefully i can get additional feedback from alex and nishad (tbc)

---
class notes


math operations automation

prob.comp is increasingly common
provably prove that resulat (lunar - 80: kalman filter; 00: draw inference from imperfect data; prediction word type; 20: 3D geometry)

tensorflow, pytorch, jax (optimzing compilers, autodiff, gpu/tpu support; probability theory (prob.distr hard to see (thining is pen and paper)))

gernal purpose tools and applied 

prob. as first class object

1. composable transformation of prob programs
represent probdistribution as programs
P(thetta):  b = flip(theta)

condition dist (real number igven the); random choices

prob distr action on prob distr; 

basis set (combination class of algorithm)

1. gradient, expected value, radon
	1. F: gradient(function), distr; how much more likeliy one distribution relative to onotherf 
	2. D: 
	3. DD: density ratio (individual don't have density distribution)
2. gradients of KL divg (grad log density ratio)
3. SMC: 
4. stochastic varianctional infrec 

theoretical guranctiees fast unbiased aproximatios are ogten preferable to ; slow, exact derivatives
many batches, unbiased
composable program trnaformation
probabilisti progrmming with composing gradient of expected values

stochastically approximate function (input theta; dots for executaion of program)
L(theta) = E_x~p(theta)[x], 
math is the same for qualitatively (stochastic branch inside)
value of theta doesn't control how hight the theta is

proportion of samples
blue program is unbiased estimator of the dots and one program's mean was increasing and the other program's varince wsas increasing

don't know blue; some way of estimating

gradient estimator in yellow (estimate of green line; as long as estimate is unbiased)
derive an expressed (expected value of sth else); sample that expression ; take as a input thetat (every theta, you have cloud of gradient estiamte)

decision theoretica optimization 
z~simultate (theta), x = U(z), return x

stochastic objective

sampling process is not differentiable - discrete varialbes

gradient estimates are biased - why?
quick urundown of forward mode AD 

(x, dx/dtheta) ; value,  (all real number); dual number vresion of a function f(x), f_D(x, dx/dtheta) = f(x)

change input time (primiteve to dual number versions); my dual version is 0

dual number version fo the whole program

the derivte of my program is let (y, dy/dtheta) = myprogr(theta, 1) in dy/dtehta

🔑1:
sampling 
p: X-> PY -> expectation 

sampling primitive (flip, normal) into a program (expected value assuming expectation operator for primite)

direct form and continuation passion form (compilation step) - augments everything with  *Y->R* is called continuation

law of iterated

avg of (average val 

turn all the program into expected value 

🙋‍♀️1: stochatic in high dim = determinsitc?

🔑2:
expected value of f under flip

expectation -> cps trnaofrm -> ad (dual number version) are not E_flp and E_normal D 
sin' = cosin
how show flip expected value of f
expected vlaue of (f is can't compute but estimate; av)

🙋‍♀️2: probabilistic progrmaE[X]= E[E[X|Y]] expectation operator

overhead of automtaion decreases as problem becomes lareger

stochastic monte carlo (slow exact densitfy function)

blue (smc; automatically derived) vs orange (hancoded) vs green (slow exact)

for every step of mcmc - proposal (whether it should jump there is density ratio; computing to jumpt there)

to exactly (integrate over all path ) propose

rejecting more than how can you be converging (accidentally rejecting are borderline moves; clear wins are still accept them)

deep learning for AD ~ ADEV

tensorflow and pytorch AD and  (alexnet moment); 

---

language model prob prog

some architecture may not be accurate enough

probabilistic reasoning about relational data

rows
growing hypothesis on what database might be (new objects; attribute, )

accuracy jumps when changing from smc to mcmc rejuvanation (percentage of jumpts after rrecorrected)
of all the cellls pclean was confidencet about (40%), 40% are correct

domain specific probabilistic systems
- scalable probabilitreasonign about relation data (uncertainty esatimage; uncertainty comes from 10 samples)
- language model probabilistic programing

https://github.com/stanfordnlp/dspy is starting at mit 

lm output distribution over answers (after); filtering , reranking; creative generation

primitive distriuion parmetrized by language models
ctx = lmcontext(after a), ctx.next_

describe task as bayesian inference
- soft constraints (sparks of ai); write a first line for a peom that would still make sense if read with the words reversed
- infiling ; 1,2,3, her 5,6,7, down 9, 10, the 12, 13

concentrated selection (rejection sample)- when unconstratinted more natural
SMC (But targeting the same distribution regjection would target)

different from another but is natural
prior - first line (probability of th reverse; prolduct of the two; ) ; rejction sampling ; separate

overindexing on the probmpt 

which token woud; greedier (token masking and logit biasing)


