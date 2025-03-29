[[🛝eval(scott, angie)2]]
## Machine Partner for Decision-Making

 2024-10-14 with two evaluators: 
 - [[charlie24👓_nss🗣️]], [[charlie24🛠️_clockspeed🗣️]], [[🗄️charlie]]
 - [[scott24👓_Bayesian_Entrepreneurship.pdf]], [[scott23🛠️_econ_idea_innov_ent.pdf]], [[🗄️🧠scott]]
---
##### Plan for Today
1. Reflect on last meeting
2. Who, When, Why of Machine Partner in Decision-Making
3. 🧠 Probabilistic Reasoning and 📍Selecting Optimal Action in nail, scale, sail stages
4. Weaving decision functions for 🌳⛰️🌊 NSS on Probabilistic program
5. Angie's petition, persuading Charlie to apply for Bose grant

---
##### Reflect on last meeting
✅ agreed on optimal action sequence given different belief and utility
✅ ENT: "pursuit of opportunity beyond resources currently controlled" (Stevenson)
-> four types of opportunities and risks (Eisenmann) 

---
##### Narrowing the Scope (opportunity)
 1) ~~pioneering a truly innovative product~~
 2) ~~devising a new business model~~
 3) ~~creating a better or cheaper version of an existing product~~
 4) targeting an existing product to new sets of customers

---
##### Narrowing the Scope (risk)
- _Demand risk_: prospective customers’ are willing to adopt envisioned solution  
- ~~Technology risk: eng./sci. breakthroughs required to bring a solution to fruition~~
- _Execution risk_ : entrepreneur has ability to attract employees and partners to implement venture’s plans
- _Financing risk_ : external capital will be available on reasonable terms
---
##### 🌳⛰️🌊 Innovation Odyssey: Mapping Risks to Operational Contexts

1. 💰🌳 Nail: Financial risk (Capitalize)
2. 💠⛰️ Scale: Demand risk (Segment-Collaborate)
3. 🛫🌊 Sail: Execution risk (Evaluate)

---
##### Key Decision-Making Functions

1. 👁️ Choosing Relevant States
2. 🧠 Probabilistic Reasoning
3. 📍 Selecting Optimal Action
4. 🤝 Estimating Commitment Effect

---
##### Key Decision-Making Functions Diagram
![[theory2alg.png|500]]
fig.1

---

##### Key Decision-Making Functions Table


| Function                       | Input                                                                                                                             | Output                                                                                                                     | Why Machine Partner is Better                                                                                                                                                                                      |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 👁️Choosing Relevant States    | world model at time t $W_t$                                                                                                       | <font color  = "violet">- state of agent model at time t $w^a_t$<br>- state of environement model at time t $w^e_t$</font> | Machines can process diverse, high-dimensional data much faster and more accurately, capturing subtle patterns and relationships                                                                                   |
| 🧠Probabilistic Reasoning      | - <font color  = "violet">$w^a_t, w^e_t$</font><br>- <font color  = "green">state of agent's belief at time t-1 $b_{t-1}$ </font> | <font color  = "green">$b_t$</font>                                                                                        | Machines has better inference methods (Markov chain monte carlo, sequential monte carlo) on complex probability distributions, and has higher precision which prevents  human biases like probability shifting<br> |
| 📍Selecting Optimal Action     | - <font color  = "green">$b_t$</font><br>- <font color  = "#C0A0C0">utility</font>                                                | <font color  = "red">action at time t $a_t$</font>                                                                         | Machines can explore vast action spaces and optimize long-term strategies more effectively, considering numerous possibilities                                                                                     |
| 🤝Estimating Commitment Effect | - <font color  = "red">$a_t$</font><br>- $W_t$                                                                                    | $W_{t+1}$                                                                                                                  | Machines can consistently track and update complex state spaces, accurately modeling the long-term impacts of decisions                                                                                            |


---
##### 🧠 Probabilistic Reasoning: Machine Advantage

- Advanced inference methods (MCMC, SMC)
- High-precision probabilistic calculations
- Unbiased belief updating

---
##### 📍 Selecting Optimal Action: Machine Superiority

- Vast action space exploration
- Long-term strategy optimization
- Comprehensive possibility consideration

---

##### Two Key Decision-Making Functions in NSS examples

| 🧠Probabilistic Reasoning  | Input: Prior beliefs on valuation, new market data<br><br>Output: Updated probability distribution of future valuations              | Input: Prior beliefs on market adoption, new sales data<br>Output: Updated probability distribution of market success for each segment-product combination | Input: Prior beliefs on operational efficiency, new AV performance data<br><br>Output: Updated probability distribution of AV adoption success |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 📍Selecting Optimal Action | Input: Updated valuation beliefs, founder's utility function<br><br>Output: Optimal SAFE terms (investment amount and valuation cap) | Input: Updated market success beliefs, company's utility function<br><br>Output: Optimal market-product strategy and sourcing decisions                    | Input: Updated AV adoption beliefs, airport's utility function<br><br>Output: Decision on whether to adopt AV for baggage loading              |

---
##### 🧠🌳 Nail Stage: Financial Risk Management

```javascript
var probabilisticReasoning = function(priorBelief, newEvidence) {
  return Infer({method: 'MCMC', samples: 10000}, function() {
    var futureValuation = sample(priorBelief);
    observe(Gaussian({mu: futureValuation, sigma: 1000000}), newEvidence.observedValuation);
    return futureValuation;
  });
};
```

---
##### 📍🌳 Nail Stage: Optimal SAFE Terms Selection

```javascript
var selectOptimalAction = function(belief, utilityFunction) {
  return argMax(function(terms) {
    return expectation(Infer({method: 'forward', samples: 1000}, function() {
      var futureValuation = sample(belief);
      return utilityFunction(futureValuation, terms);
    }));
  }, safeTerms);
};
```

---
##### 🧠⛰️ Scale Stage: Revenue-Cost Reasoning
```javascript
var revReasoning = function(rev_prior, rev_obs) {
  return Infer({method: 'MCMC', samples: 10000⚡️⚡️⚡️}, function() {
    var rev = sample(rev_prior);
    observe(Gaussian({mu: rev, sigma: 0.1}), rev_obs); #🧠bayes_rule
    return rev_post;
  });
};

var costReasoning = function(cost_prior, cost_obs) {
  return Infer({method: 'MCMC', samples: 10000⚡️⚡️⚡️}, function() {
    var cost = sample(cost_prior);
    observe(Gaussian({mu: cost, sigma: 0.1}), cost_obs); #🧠bayes_rule
    return cost_post;
  });
};
```
##### 📍⛰️ Scale Stage: Segment-Collaborate Acting

```javascript
var acting = function(rev_post, cost_post, utility) {

  return argMax(function(action) { #📍
    return expectation(Infer({method: 'forward', samples: 1000⚡️⚡️}, function() {
      var seg_rev = sample(rev_post);
      var collab_cost = sample(cost_post);
      return utility(seg_rev, collab_cost, action);
    }));
  }
};
```

---
##### 🧠🌊 Sail Stage: Efficiency Gain Assessment

```javascript
var probabilisticReasoning = function(priorBelief, newEvidence) {
  return Infer({method: 'MCMC', samples: 10000}, function() {
    var efficiencyGain = sample(priorBelief);
    observe(Gaussian({mu: efficiencyGain, sigma: 0.1}), newEvidence.observedGain);
    return efficiencyGain;
  });
};
```

---
##### 📍🌊 Sail Stage: Technology Adoption Optimization

```javascript
var selectOptimalAction = function(belief, utilityFunction) {
  return argMax(function(action) {
    return expectation(Infer({method: 'forward', samples: 1000}, function() {
      var efficiencyGain = sample(belief);
      return utilityFunction(efficiencyGain, action);
    }));
  }, actions);
};
```

---
##### 🧠📍 Integrated Decision-Making across NSS 🌳⛰️🌊

- Combining key functions across innovation stages
- Tailored strategies for each odyssey phase

---
##### Future Work: Implementing Machine Partner 

- Enhance probabilistic programming models
- Integrate real-world data
- Validate with transportation sector cases: Mobility venture capitalization, Tesla's segmentation, Changi airport's evaluation for AV adoption