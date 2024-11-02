[[ceo(bsem)]]
growing entrepreneurial mind from bayesian brain

- [[cto1(eq(rational_agent))]] explains strategy formulation under uncertainty leveraging rational agency equation. this optimal decision-making equation for entrepreneurs translates inflow of complex business environments into outflow of decisions.
- [[coo(alg(eq(rational_agent)))]]
- [[Bayesian calibrated decision_ bootstrap toward the decision-consistent region]] explains bayesian inference and calibration for decision making, recalibration of prior 

```
use weaker prior if I sense increase of heterogeneity in data generating process (DGP). Two examples: first is when DGP is expected to be vertically differentiated. For instance, if you’re a marketing firm segmenting customers, knowing the fact that GPT diversifies customer desires (I don’t know this is true) and not updating your model would make you feel uncomfortable. However, you’re not ready to add one more layer. In this case, you can have the effect of injecting heterogeneity by widening your prior, until you finally commit to one more layer.Second is when DGP is expected to be differentiated horizontally. Keeping track of transmission rate and recovery rate of pandemic may be hard due to virus mutation and different biological and behavioral response across countries. In both cases, the more is at stake in failing to capture these dynamics, the wider prior should be. Marketing firm in luxury brand industry would use wider prior than that in commodity industry. Transmission rate of a Covid model that kills people is more likely to have wider prior than that of chronic wasting disease that harms deer. If you flip this, if the object you’re trying to model evolves slowly or you have strong control over it, it’s safer to use sharper prior. Andrew may have better suggestion but you may want to skim BDA chp.17. Further thoughts on dynamic model in the context of SBC is in https://discourse.mc-stan.org/t/could-sbc-rank-uniformity-be-attacked-by-unstable-equilibrium-point-in-generator/29960
```

---


table1: quadrant
fig1: ai rational agency (cooperate for survival - share world model due to limited s to a; inf_{p(t|x)} I(y|x)-beta I(t|x))
fig2: strategy comparison



### 1. meaning of "entrepreneurial" strategy and operation 

- This theory assumes that the brain encodes beliefs (probabilistic states) to generate predictions about sensory input, then uses prediction errors to update its beliefs. (Bottemanne H, Longuet Y, Gauld C. L’esprit predictif : introduction à la théorie du cerveau bayésien [The predictive mind: An introduction to Bayesian Brain Theory]. Encephale. 2022 Aug;48(4):436-444. French. doi: 10.1016/j.encep.2021.09.011. Epub 2022 Jan 7. PMID: 35012898.)
- how mindset relates with computation (theory-of-mind)
- mindset : heart, head, hand, home + solution oriented, adaptable
- science (fourth quadrant; prediction accuracy under intervention in yet unseen situation) that's different from strategy and operation. 
- axiom for strategy
1. lower variance on p(c,t,c,o|s) due to freedom (wider feasibility space)
2. need to focus on one strategy due to constraint 
3. need for pivot (change strategy) due to uncertainty (of feasibility and desirability world model)
4. need to update utility of non-chosen options due to noisy learning 

### 2. 
coherence among c, t, c, o and 

we argue two features of bayesian software can help address the problem. first feature is hierarhcial bayesian. it can solve 1 and 4. second feature is simulation. this extends "test two and choose one" framework with simulation and calibration using bayesian software. which can solve 2 and 3. when combined, hierarchical model of operations given startegy and strategy given operations can be alternatively simulated to test coherence.

contribution of this paper is to parameterize rational agency equation which maps utility, environment, perceived state, action to the next action in a form suitable for entrepreneurial strategy and operation. 

problem to solve: business theories are not implemented to support probabilistic reasoning for entrepreneurial decision making

implementing
knowledge 
