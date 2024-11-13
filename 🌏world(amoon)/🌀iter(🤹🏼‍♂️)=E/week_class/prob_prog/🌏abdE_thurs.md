Maria Cracium, Youness Kaddar, Matt Bowers, Wendy Sun, Francisco Marchi, Sid Cox, Yudi Xie, James Sum

🎯: learning pp structure from data, dsl with fast, exact inference, automated modeling of multivariate and db

[[abe()

----

both encouraging and 
labor of love - teaching material 
invite the slack channel (comment)
![[Pasted image 20230824131210.png]]

- how to scale up
- we can have ppl that captures both symbolict and diff model including key maths 
- single particle do 
litttle bit of generative and inference program (user supplied)

![[Pasted image 20230824131435.png]]
- less clear to write programs (start from dsl, then move on to less contraints)
- fast, exact (if you domain knowledge falls within certain region)
- make meta program which cooperatively infer from structured data (time series, panel, cross-sectional, relational; how many different panel datas (individual - longitude - Roge chetty's tax return, macro econ, core financial report, sec companies, lab values for clinical trial))
- flexibility of human thought vs wide spread (econ, bio-statistc - flexible), oncology, economic policy (prospect of grounded model is good), 
- scaling up to common sense
- if we could go from data to probprog, symbolically analyze (how2quantify - calc rare events)
- 
- ![[Pasted image 20230824131552.png]]
scale the method - m3 database - 10times faster (temp fusion) - self-tuned arima models, 
- statistical model hard to beat (7yrs ago on google health)
- in the supplement (logistic regression is within) - illusion of progress / random forest
- empircal support from accuracy 
![[Pasted image 20230824132058.png]]

- 3d (shapes are arbirary for box-sized model) - don't need to 
- probablistic + nonparameteric (1. model for shape voxal grid - 2. mixture model - mixture model)
- vm prefers to can empirical model (memorize data - ) rather than semi-parateric
- run time and accuracy (whiskers - confidnec) 
- smc converge smoothly - gradient had problem with local min, sgd converged better (wrong cuz part of the data)
- MCMC: SMC = gd:sgd (likelihood data)
- pure jacob has done some work  (short parallel chain) - what more (speed and mind  - adaptive biological perspective should matter e.g. selection)
- dsl (domain specific language) - linear(1.0), 
- matrix (sigma, noise level, series of )
- ![[Pasted image 20230824133028.png]]
- ![[Pasted image 20230824133734.png]]
- ![[Pasted image 20230824133802.png]]
- noise level and 0 to N
- ![[Pasted image 20230824133814.png]]
- ![[Pasted image 20230824133947.png]]
- variation
- periodic covariance
- high covariance or length scale covariance ![[Pasted image 20230824134001.png]]
- sin squared (general length scale where covariance is low) 
- warped by the (covariance is also periodic)
- far apart 
- combine (symbolic - linear trend over lay / memorize data within the structure)
- whole field that can be mapped to gen
- this to next (change dsl and change expressiveness)
- 
- ![[Pasted image 20230824134512.png]]
- sketching (filling in wholes of deterministic program)
- ![[Pasted image 20230824134538.png]]
- schedule (enough compute)  
- lean and get better anything (takes work to remain flexible) - pl is studying (expressiveness and specialization) - tradeoff is essential (compilers show - express formalism - automate specialization - sufficiently good without penalty)
- for intelligence, core q is ppl question + new domain specific (learned collaboratively)
- arc of this field first principled reasons (type of theory how the tradeoff playoff)
- didn't expect to learn gpu programming  (need to understand system and architecture - ppl has one more area"codesign of dsl")
- changepoints - robustness
- ![[Pasted image 20230824135309.png]]
- ![[Pasted image 20230824135328.png]]
- ![[Pasted image 20230824135336.png]]
- ![[Pasted image 20230824135345.png]]
- some change![[Pasted image 20230824135412.png]]
- bayes structural (neural variant failed) ![[Pasted image 20230824135426.png]]
- why ml can fail
- ![[Pasted image 20230824135459.png]]
- flexible of new data,  (gambling - hedge your bets)
- single program is totally crazy
- dsl_program doesn't include unkown unkowns
- ![[Pasted image 20230824135828.png]]
- google deepmind teeunecities![[Pasted image 20230824140351.png]]
- ![[Pasted image 20230824140635.png]] (sampled prior)
- when you're not interpolating, posterior doesn't capture
- posterior are far apart
- space around the actual (area around the actual mode)
- ![[Pasted image 20230824141521.png]]- spread mass to too many (assign low likelihood to all dataset) too simple - assing to much likelihood to 
- uniform model  (failfied ability bias) - more falsified model gain more evidence
- compared to model that can't falsify (optimize no luck)
- monk (optimization - electric monastry - trick into believeing sth and having no flexiblity left)
- ![[Pasted image 20230824141936.png]]
- ![[Pasted image 20230824142017.png]]
- ![[Pasted image 20230824142027.png]]
- ![[Pasted image 20230824142034.png]]
- ![[Pasted image 20230824142044.png]]
- prob.programming made it too tempting not to try
- ![[Pasted image 20230824142204.png]]
- choose type of code - parameterize and  (fills in dsl)
- ![[Pasted image 20230824142239.png]]
- infiintely branching time series tree  - short symbolic (Q. why thought is even possible) - what dsl capture (infernce process is much fater)
- ![[Pasted image 20230824142244.png]]
- not simplistic prior but ignorance (run time would grow too much - ) ; 
- foundation for induction under computational constraint (eliia - inductive bias = computational bias - learning over circuits under - not a norm but smooth - circuts quickly)
- what's the compute cost for prior and likelihood - don't need probablity mass concentrate
- ![[Pasted image 20230824142341.png]]
- ![[Pasted image 20230824142531.png]]
- ![[Pasted image 20230824142601.png]]
- resample move smc
- ![[Pasted image 20230824142651.png]]
- gen's radom nickodym (jacobian - normal ad and treat it as part of nd)
- ![[Pasted image 20230824142713.png]]
- incremental computation - re-excuate local parts of the trace) 
- ![[Pasted image 20230824142750.png]]
- need too many iteration (smc - resample ![[Pasted image 20230824142819.png]]
- ![[Pasted image 20230824142833.png]]
- drops much faster ![[Pasted image 20230824142845.png]]
- resample mode smc 
- hmc for re - multi-threaded![[Pasted image 20230824142900.png]]
- how to make; modern cpu is powerful than gpu (esp. for prob syntehsis)  genjax (other parallel)
- ![[Pasted image 20230824143011.png]]
- the right (everything is underfit) - robust model + fast to converge infence alg![[Pasted image 20230824143020.png]]
- how this might scale for brain-level