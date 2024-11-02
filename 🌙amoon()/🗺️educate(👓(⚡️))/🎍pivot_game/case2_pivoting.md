theory behind [[🌙amoon()/🧭apply(🗺️(👓(⚡️))))/case2_pivoting|case2_pivoting]]
### 1. intro and literature review (1page)
separating inference (sigma) and decision (k) uncertainty; react differently to same signal - pivot market vs product (depending on `k_sigma`, `mu, sigma` of predicted_profitability)

- #todo connect six sigma with k_sigma (should it decrease or increase k_sd)

#### 1.1 ground truth (observed profitability boost) 
The literature shows that rising expectations about future demand for new technologies increase the incentives for investments in innovation by enlarging payoffs to successful innovations​​.
[[📜Nemeta09_Demand-pull, technology-push, and government-led incentives for non-incremental technical change]]

#### 1.2 belief on how noisy learning is
Beliefs about the noisy nature of learning environments significantly influence the strategic orientations of startups, shaping their responses to market and technological signals​​.

#### 1.3 setting k

### 2. model (1page)
The belief-action dynamics for startup experimentation can be illustrated with the interaction belief, profitability, action, environment. 
![[Pasted image 20240616224039.png]]
#### 2.1 agent
1. **Expectation**: Initial belief (B1) about the environment (E1) determines the expected profit (P1). The observed profit may differ from the expected profit.
2. **Action**: Action (A1) is determined based on the comparison of expected and observed profit. #todo explanation on decide_action lowbar and highbar framework. add why static low and highbar over different cells is unrealistic. endogenizing low and highbar setting rules allows one to add generalizability to the model

3. **Update Environment**: Action updates the environment from E1 to E2.
4. **Update Belief**: Belief is updated from B1 to B2 based on the observed profit and initial belief.
   
detail in [[Belief-Action Dynamics for Startup Experimentation]] with [[🗄️BPAE.png]] on belief, profitability, action, environment interaction and five plots on   [[🗄️BTS_plot]]

#### 2.2 environment
from figure which has three different ground truth 
- **Initial Belief and Real (First Plot)**: The initial belief shows uniform expectations, whereas the real outcome indicates discrepancies, highlighting the need for adaptive strategies in belief updating.
- **Change Speed (Second Plot)**: An increase in speed from 2 to 4 shows the rapid adjustments needed in response to market changes, impacting both the pivot product and market ratios.
- **Change Angle (Third Plot)**: The change in angle from 2/2 to 3/1 illustrates how directional shifts in strategy must be managed, affecting the pivot decisions and overall market approach.

![[Pasted image 20240616223536.png]]

#### 2.3 agent x environment
how pivot ratio is affected
1. when playground's gradient as a whole changes 
2. when playground's angle changes

### 3. analysis (2page)

| Plot Type                              | mu_p2m (product-market ratio)    | mu_sum (sum of all mus)          | sigma (variance)                | k (decision variable)       |
| -------------------------------------- | -------------------------------- | -------------------------------- | ------------------------------- | --------------------------- |
| E![[Pasted image 20240616224921.png]]  | If mu_p2m increases, R increases | If mu_sum increases, R increases | If sigma increases, R increases | If k increases, R decreases |
| P![[Pasted image 20240616224927.png]]  | If mu_p2m increases, R increases | If mu_sum increases, R decreases | If sigma increases, R increases | If k increases, R decreases |
| B ![[Pasted image 20240616224933.png]] | If mu_p2m increases, R decreases | If mu_sum increases, R increases | If sigma increases, R increases | If k increases, R increases |
out or in X us or china (OIUC)
- **sigma (variance):** In all contexts (E, P, B), higher variance generally implies more uncertainty, prompting more pivots to explore different strategies and reduce risk.
- **k (decision variable):** Higher precision in decision-making usually reduces the need for frequent pivots in the environment and profitability contexts, but may increase pivots in the belief context to maintain updated and accurate beliefs.
- 
#### 3.1 ground truth (observed profitability boost) 
- fig1: decrease as mu_bc- increase
The impact on mu_p and mu_m from observing a significant deviation such as -2 in the first cell indicates a need to reassess the expected profitability and its variance in response to real-world outcomes

#### 3.2 belief on how noisy learning is
- fig2: viscous prior with belief on noisy environment
A more viscous prior belief on a noisy environment suggests that startups need to account for higher variability and uncertainty in their market and product strategies
#### 3.3 setting k
- (size of org -> cost ratio of pivot ->) 1/k -> 1/R
Setting the decision variable kkk involves understanding the cost ratio of pivots and how it impacts organizational size and resource allocation. This ratio influences whether a firm should pivot the product or market based on observed profitability and strategic objectives

### 4. further (1page)
capturing "size of org -> cost ratio of pivot "; size of org -> how R is mediated by cost ratio of pivot and k
- Big pharma with established distribution channel fix disease and change molecule. Tech push biotech fix molecule and change disease. I’d love to express nail to scale phase transition as crossing red line!
more flexible format of decide_action. currently, it maps profit value input (profit_obs and low_profit_b, high_profit_b) to action output (scale, pivot product, pivot market, pivot market and product).

however, based on the observation where big pharam has higher cost of pivot market than cost of pivot product compared to biotech startup whose cost of pivot product is larger than the cost of pivot market, i'd like to add cost component. i.e. depending on whether CR = pivot_product cost /pivot_market cost> 1 or not,

when CR > 1, input (value of profit_obs and low_profit_b, high_profit_b) can be mapped to action [scale, pivot market, pivot product, pivot market and product]

when CR < 1, input (value of profit_obs and low_profit_b, high_profit_b) can be mapped to action [scale, pivot product, pivot market, pivot market and product]

fig4🐣2🦖 [[🐣2🦖.png|300]]


- cost of pivot VS experiment