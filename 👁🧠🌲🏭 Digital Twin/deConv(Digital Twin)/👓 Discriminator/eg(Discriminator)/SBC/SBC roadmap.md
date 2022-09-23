Main message of SBC extention
#### practical value
1. use data as well as parameter 
2. randomized ties
3. rejection sampling
4. empirical coverage plot
5. how to summarize joint well (constructing test function space): correlation, ordering, combination of parameters (incorrect posteriors), monotonous transformation

#### theoretical contribution


| -    | practical value | theoretical contribution  | IF = $\phi(p, t)$ | 
| ---- | --------------- | ------------------------- | ---------------- |
| near/completed | 1>2>3>4            | 5 (surprising)> 1,3 > 2,4 |                  |
| far  |              | 5          |                  |


Goal: Trust-building for Approximation
First is to develop statistical theory that justifies approximation. Credible interval as a function of sample size and the simulator is the outcome. Based on the interval, graphical test that verifies miscalibration is provided through SBC, an opensource package for simulation-based calibration. [[package](https://github.com/hyunjimoon/SBC/)][[vignettes](https://hyunjimoon.github.io/SBC/articles/index.html)]
   
- Characterizing transforms which is reliable given the SBC procedure function, $\phi$ with two comments on composition^[Procedurally, y is dependent on prior and likelihood hence $p(y, \theta) = Prior_{\theta} * Lik(y|\theta)$ so I am hoping for two-step notation in the future. Our focus is first set on identifying set of transform given the joint space, so I think $\phi$ might be a good start.] and convolution.^[I found Bayesian deconvolution part of [this](https://hastie.su.domains/CASI_files/PDF/casi.pdf) Efron's book chp.21 relevant: $f(y) = g(\theta) *N(0,1)$ especially considering our proposal of rejection sampling based on y, $\theta$-marginalized notation can be of help.]
- `theory`, `experiment` (counter-example), and `computation` are three pillars of the scientific method, `theory` being induction and the rest deduction. Experiment is strong proof of nonexistence "strong yes is wrong", can't) while computation is weak proof of existence "weak yes is right" through enumeration.

I was approaching SBC in three steps.
1. **Justify** with `theory` and `experiment` (strong existence)

- a. Identify diagnostics hierachy of the following conditions: 
$p(\theta, y, \theta')$ is $\theta, \theta'$ - exchangeable $\rightarrow$  $p(\theta, \theta'|y)$ is $\theta,\theta'$ - exchangeable $\rightarrow$   self-consistent integral equation $\rightarrow$  uniform rank. The relationship can equivalently viewed from  $S_f$ for each diagnostics condition are not  

- b. For each level of the hierarchy, set a diagnostic benchmark using the oracle (no bug in dgp and perfect computation). 

2. **Verify** with `computation` :  (weak existence)
- define diagnostics that determines certain configuration that are "not calibrated badly". 

3. **Solve** ^[this is what I was working on with @paul.buerkner; finding a weak solution (prior) that passes the diagnostics]

---
1. $\phi$ should be a map from joint $Y, \Theta \rightarrow Z$ where Z is a distribution (i.e. measure). I believe borrowing notations in [Proposition 2.16(The random-variable Bellman equation](https://www.distributional-rl.org/contents/chapter2.html) might be efficient. I would be happy to chat further on how the reference can be applied in our setting.

2. f is the test function. It is a transformation fishing for vanilla-SBC failure given $\phi$. SBC diagnostics verifies  aims to SBC aims to carve out weak yes out from the union of weak yes and strong yes. From the three types, strong-yes, weak-yes, and strong-no where the definition of weak-yes is there exists at least a function that makes `f`

3. Induction bias
is about trade-off in statistical, approximation, and optimization error. Statistical error increases as `hypothesis class` size increases while approximation error decrease as `function class` size increases. From definition 5, a set of function approach triggers defining a test-function class (perhaps dual-cone). This  which is what Thm3 is planning 

Type and We will first focus on mapping that are **continuous** between $Y, \Theta$. This assumes two things: continuous type variable and **infinite** samples, as opposed to discrete and finite samples. For practical reasons that every downstream operation is with a finite number of samples regardless of the type, I prefer viewing continuous and infinite as the limit of the discrete and finite rather than the approximation view.

|type \ sample   | finite  | infinite   | 
|---|---|---|
| disc.   |   |   |  
| cont.  |   | o  |   

2. Test function view. two mappings f, g that are in order-unpreserving transform relation has $S_f \setminus S_g \neq \emptyset, S_g \setminus S_f \neq \emptyset$ 
1. Three main objects: 
- $\phi$ function from thec
- $f$ function from the joint distribution of data and parameters to 
2. Thms:


## Trust building approximations.
: #indicator

There is no formal attempt to define `simulation-based calibation` which cause users confusions on when and why to use this or how to interpret its visual results. Starting by setting its purpose as turst-building approximations, we classify the Two types of approximations happen from scientific result to happen we define based on the type of the output,  which give measure provide software which generates certificate for and aim to develop software that aids 

easi  in which diagnostics to use ad big picture for axioms, assumptions, theorems in using ^{TM} is  diagnostic of three things make 
Three diagnostic classification: strong yes != weak yes
strong yes (exists no fail condition)  
weak yes (inside oval but \exists other fail condition) 
strong no (outside oval)

### Two workflows with the same goal, different order
optimizing set of qoi vs finding set of prior
find (conditions for) f s.t. SBC(theta) iff SBC(f(theta)) conditioned on prior
Martin's approach
find prior s.t. prior = dap conditioned on f  + workflow where f is learned (red in the diagram attached)
Angie and Shin's approach self-calib() operator

### Two workflows with different verification object
Binary decision for dgp vs algorithm
verify dgp (Martin's tutorial last year) 
 detect error in models (can work, nonidentifiable), two prior (in the model >> belief - Bayesian cringe)
detect error in model implementation (classic SBC; software, data)
verify algorithm (VI vignette)
not a test but discrepancy (interval)

prior draw are not bijection with real use hence posterior draw can be

Minor q. > In particular this precludes use of any automatic method that turns
a model in a PPL into a simulator. Why so?

