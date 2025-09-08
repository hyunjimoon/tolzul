- [[#input|input]]
		- [[#continuous, objective|continuous, objective]]
		- [[#discrete, subjective (customized)|discrete, subjective (customized)]]
	- [[#input#belief state|belief state]]
- [[#output|output]]
	- [[#output#consistency testing service|consistency testing service]]
	- [[#output#operation prescription service|operation prescription service]]
- [[#hypothesis|hypothesis]]
- [[#appendix|appendix]]
- [[#blitzscaling:|blitzscaling:]]


1. 스타트업 운영목표는 성공적인 exit이 목표인만큼,  인수/투자 주체인 established기업입장에서 생각해야한다.
2. 1을 위해, 하드웨어, 소프트웨어가 핵심역량인 스타트업은 risk, pivot 면에서 차이가 있으므로 (image recognition; acqhire)
tps도 방직기의 자동오류교정시스템을 자동차생산에 적용한것. product-process-organization으

research question: how to design a function $f()$ that maps 1. assessed physical state of an agent (=organization) 2. assessed physical state of environment 3. belief state of an  agent (business strategy) to actionable operational decisions like make/buy, push/pull (decoupling point), offensive/defensive, partner contract, rhythm of the release. That is to say, how to automate consulting that prescribes operations for entrepreneurs.

Denoting agent's internal state (e.g. organization's capability to decide make/buy, quality of conformity) as $\theta$ and external state as $y$ (e.g. customer needs, market size, entrant barrier) and its observed state as $\tilde{y}$, state of agent and environment are represented as $p(\theta, y)$. Strategy or guiding policy is a belief state of how an agent desire to respond to the environment it believes underlies beneath the observed state and noted as $p_A(\theta|y)$. When $p_A(\theta|y)= \frac{ p(\theta,y) }{p(y)}$ for every $y$, this is a optimal strategy meaning this strategy guides the agent through a path that's perfectly in sync with true demand which is not possible in reality. Instead we assume ‘‘two strategies $p_{A1}(\theta|y), p_{A2}(\theta|y)$ to show how strategies are chosen in different settings[^1]. `A` stands for approximation, and A1 vs A2 denote two structurally different response for given environment. For instance, meta's quest pro and apple's vision pro have very different strategy[^2] (let A1, A2) which is affected by and affects the internal and external states. Ultimately, our goal is a concurrent engineering workflow of organization, process, and product. 

Among agent's internal state, strategy is longer term and we treat it separately as hyperparameter $\phi$ which is fixed while coordinating other parameters according to true demand. Repeating the above, internal state is $(\theta, \phi)$, external state (true demand) and its observed state are $y$ and $\tilde{y}$, and $p(\phi, \theta, y)$ represents distribution function for strategy, agent, environment. Starting from the demand, designing organization and strategy according to its posterior $p(\phi, \theta|\tilde{y})$ is an approach closer to pull, whereas looking for customers with marginalized $p(y) = \int p_A(\phi, \theta, y) d\phi d\theta$ 
$p(\phi , θ) = p( \phi )p(θ |\phi )$ fully describes agent's state and how an agent adjust its strategy and organization is as follows:

function $f()$  provides:
1. consistency testing 
	- verify $p(\theta, y)$: organization and strategy fits (e.g. apple which has both hard and software capability choose architectural and leader rather than agile follower strategy)
	- validate $p(\theta, \tilde{y}, \tilde{\theta})$ 
	- math in appendix 

application: interoperability website where entrepreneurs can log their physical and belief state and be informed of their operational decision, at each time. 

ii) consistency testing between states (validate $p(\theta, y)$,  i.e. between physical and belief states within agent, between belief(internal_physical) states with outer_physical states 
ii) get aid in operational decisions (mid-term)
![[interoperability.png|100]]
- equation: strategy(organization(.)) = demand(.)
- object:
	- organization(.)
	- strategy(organization(.)) = product
	
## input 
1. assessed present state (agent)
	1. temporal: age of startup, employee number (family(<10), tribe(10s), village(100s), city(1000s), nation (10000s))
2. assessed present state (environment)
	1. domain discretized with atom/(bit+atom)
		1. high: advanced_manufacturing, advanced_materials, semiconductors
		2. mid: biotech_lifesci, food_agriculture, space, robotics
		3. low: energy, ai, quantum computing, iot
3. strategy (guiding policy to future state of agent)
	1. ([collaborate/compete, control/execute] (Scott, 2021) or [cost leadership/differentiation] (Porter))
	2. 
- age of startup should be scaled for each domain, as 1 yr IT startup would have hedged more risk compared to 1 yr bio or energy startup.

#### continuous, objective
#### discrete, subjective (customized)
Entry barriers protect an industry from newcomers who would add new capacity


## output

### consistency testing service
- e.g. identifying some statistics are not fine enough (truck statistics especially were too aggregated) to use, in the attempt to verify initial value of ev or ice users

### operation prescription service
1. make/buy
2. push/pull (decoupling point)
3. offensive/defensive
4. partner contract
5. rhythm of the release
It is not only established company that can have product/service platform. Having a regular rhythm of releasing new updates keeps demand and supply in sync. However this rhythm is the function of inputs. Software has faster release rhythm e.g. open-source library versions (month) are much finer scale than automobile (year).

--- 
## hypothesis
1. strategy to start from atom then pivoting to bit increase endurance and capability as organization can learn faster and more accurately from palpable atom-based feedback 
	1. aws: Amazon’s retail business is heavily based in atoms; originally outsourced its logistics to Ingram Book Company, but its heavy investment in inventory management systems and warehouses as it grew turned infrastructure limitations from a growth limiter to a growth factor. On the retail side, merchants pay Amazon to manage their inventories and logistics for them, while the massive computer systems that Amazon built to operate its retail business gave it the capabilities to launch its AWS business (which is a high-margin, bits-based business)
	2. better to write in paper before trying to build software line by line

- q:  defining `bits2atoms transformation cost` as turning bits (belief) into atoms (physical), for instance making mockup business moe

information, unlike material flows, is not conserved, a different structure is needed to capture information delays 

One may say, creation and destruction process for atom (e.g. radioactive waste, car, nation) is physical and therefore known better. [Nuclear reactor byproduct, low concentration] for radioactive waste, [assembly line, change of ownership or scrapping in a junkyard] for a car, [formation or revolution, perish or revolution] for nation. However, considering prescription-centered definition of our model, knowledge can't justify model inclusion.

Another explanation that fits our action-centered model is, different mechanism of in and outflow connects to different strategies. If our goal is to keep our bathtub (with source and sink) level stable, largely three actions exists: increase/keep/decrease the source-inflow and sink-outflow by the same amount. However if our goal is to 

prop 1. Comparative advantage in bit management is more focused on stock whereas comparative advantage in atom management is more focused on flow
- hard to measure bit
- hard to debug bit
- better to collaborate (every bug is detectable with many eyeballs (Von Hippel, 2020))
- faster diffusion
 For instance, if our goal is to keep radioactive waste low we can think of either decreasing the inflow rate or increasing the outflow rate. Also, to supply cars faster we can not only think of building more assembly lines, but also reuse used cars. For those aiming to become a king can either explore for ungoverned land or subvert. Which strategy to choose depends on the state of organization. Business strategy explains this as diagnosis of my state leads to several guiding policy which should executed coherently. To 

prop 2. use of defensive and offensive strategy differs
- [[MoonVolve🌀/sail🌕/comp(mng(bea))/_def(comp(mng(bea)))/off_def(bea)]] 
- [[amoon(world)/jungle🌳/comp(mng(bea))/offense_defense()/off_def(bea)|off_def(bea)]] which maps example with classifications
- [[amoon(world)/jungle🌳/comp(mng(bea))/_def(comp(mng(bea)))/off_def(bea)|off_def(bea)]] shows table for offensive and defensive startegy

prop3. easier knowledge transfer for bit
- there is less confusion of correlation/causation in atoms
- multi person decision theory: military ethics class vs harvard undergraduate ethics class (N person vs M person decision) - atom is N, but is M

prop4. risk: bit-based < atom-based, 
- can't pivot (aws)
how much i know: 

Information delays cannot be modeled with the same structure used for material delays because there is
- no physical inflow to a stock of material in transit. 
- inputs and outputs of material delays are conserved; for example, a strike at the post office lengthens the delay in delivering mail, reducing the delivery rate and causing the stock of mail in transit to build up. In contrast, information such as perceptions and beliefs is not conserved. 
- Consider a firm’s forecast of the order rate for its products. The expected order rate responds with a delay to changes in actual market conditions. 
physical order rate does not flow into the delay; rather information about the order rate enters the delay. Because information, unlike material flows, is not conserved, a different structure is needed to capture information delays

don't let customer choose you, you choose customer
prop 5. during scale up period of established company, contract type should differ for 
Second, stock variable of atom  Also, other model variables have different relationship with inflow and outflow variables. On the other hand, 



## appendix
Throughout this paper we assume an implicit and fixed statistical model (strategy) $\pi$ with data (environment)space $Y$ and parameter (agent) space $\Theta$. For $y \in Y, \theta \in \Theta$ the model implies the following joint, marginal, and posterior distributions:
$$
\begin{gathered}
\pi_{\text {joint }}(y, \theta)=\pi_{\text {obs }}(y \mid \theta) \pi_{\text {prior }}(\theta) \\
\pi_{\text {marg }}(y)=\int_{\Theta} \mathrm{d} \theta \pi_{\text {obs }}(y \mid \theta) \pi_{\text {prior }}(\theta) \\
\pi_{\text {post }}(\theta \mid y)=\frac{\pi_{\text {obs }}(y \mid \theta) \pi_{\text {prior }}(\theta)}{\pi_{\text {marg }}(y)}
\end{gathered}
$$
$\pi_{joint}(y, \theta)$ means how 
Typically, the posterior distribution $\pi_{\text {post }}$ is the target of inference but is impossible to evaluate directly. While many computational approaches exist for sampling from the posterior or its approximations, they may fail to provide a correct answer. Problems can arise from errors in how the algorithm or the statistical model are encoded or from inherent inability of the computational method to correctly handle a given model with a given dataset.

Self-consistency properties of statistical models. One such property concerns the data-averaged posterior (Geweke, 2004):
$$
\pi_{\text {prior }}(\theta)=\int_Y \mathrm{~d} y \int_{\Theta} \mathrm{d} \tilde{\theta} \pi_{\text {post }}(\theta \mid y) \pi_{\text {obs }}(y \mid \tilde{\theta}) \pi_{\text {prior }}(\tilde{\theta})
$$
SBC relies on a different property that involves the joint distribution of prior and posterior samples from the same model (Cook et al., 2006):
$$
\pi_{\mathrm{SBC}}(y, \theta, \tilde{\theta})=\pi_{\mathrm{prior}}(\tilde{\theta}) \pi_{\mathrm{obs}}(y \mid \tilde{\theta}) \pi_{\mathrm{post}}(\theta \mid y)
$$
Since $\pi_{\mathrm{obs}}(y \mid \tilde{\theta}) \pi_{\text {prior }}(\tilde{\theta})=\pi_{\text {marg }}(y) \pi_{\text {post }}(\tilde{\theta} \mid y)$, this implies
$$
\pi_{\mathrm{SBC}}(y, \theta, \tilde{\theta})=\pi_{\operatorname{marg}}(y) \pi_{\mathrm{post}}(\theta \mid y) \pi_{\mathrm{post}}(\tilde{\theta} \mid y)
$$

---- 
1. Write the joint posterior density, p(θ, φ| y), in unnormalized form as a product of the hyperprior distribution p( φ ), the population distribution p(θ |φ ), and the likelihood p(y | θ):
    $$p( \phi , θ | y) \propto p( \phi) p(θ |\phi) p(y | θ)$$ 
2. Determine conditional posterior density of θ given the hyperparameters φ ; for ﬁxed observed y, this is a function of φ , 
   $$p(θ |\phi, y)$$

3. Estimate φ using the Bayesian paradigm; that is, obtain its marginal posterior distribution, p( φ| y)
$$p(\phi \mid y)=\int p(\theta, \phi \mid y) d \theta$$


$p( \phi , θ | y) \propto p( \phi , θ)p(y |\phi , θ) = p( \phi, θ)p(y | θ)$ denotes how star
---- 




how scale strategy differs for bits and atoms:
- automation (agility hard to get for hardware; jucerio)
- "easier for tech firm to make cars than a caremaker to become a tech company" (economist)

## blitzscaling:
“software is eating the world.” What he means is that even industries that focus on physical products (atoms) are integrating with software (bits). Tesla makes cars (atoms), but a software update (bits) can upgrade the acceleration of those cars and add an autopilot overnight.

- PROVEN PATTERN #1: bits rather than atoms
Bits-based businesses
- e.g. Google and Facebook 
- focus on electronic bits rather than material atoms
- much easier to serve a global market, which in turn makes it easier to achieve a large market size
- easier tap into distribution techniques like virality, and their ability to be highly networked provides more opportunities to leverage network effects as bits are far easier to move around than atoms
- high-gross-margin businesses because they have fewer variable costs.
- easier to design around growth limiters. 
- iterate more quickly on software products (many Internet companies release new software daily) than on physical products, making it faster and cheaper to achieve product/market fit. 
- can get away with far fewer employees than most of their atom-based counterparts (e.g. WhatsApp)
- power of software has also made it easier to scale up atom-based businesses as well, despite—or perhaps because of—the growing dominance of bits. 


test hypothesis and test. possible explanation and constantly update

outside, learn from other's failure, inside view

[^1]: We can treat $p_A(\theta|y)$ as hyperparater $\phi$ = $p_A(\theta|y)$ and analyze continuous update of strategy in a longer term, but let's assume it to be fixed and with only two candidates.
[^2]: bit (metaverse)-driven meta pro vs atom-driven vision pro: Aim for Meta quest pro development is full VR experience in metaverse roadmap. On the other hand, 
Cook has been vocally against the concept of metaverse, now proven by Vision Pro being a MR-first device. Throughout the keynote, not only you don’t hear the word metaverse, but also no VR, very little gaming. https://www.cnbc.com/2022/10/03/apple-ceo-tim-cook-doesnt-like-metaverse-prefers-augmented-reality.html

