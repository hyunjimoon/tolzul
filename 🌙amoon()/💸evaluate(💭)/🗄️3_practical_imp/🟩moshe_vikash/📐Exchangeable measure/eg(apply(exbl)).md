## (C) Simple Examples from Applied Research

🗣️REQUEST3: Several simple, clearly explained examples of how exchangeability has been used or explained in applied research papers. 
next is [[form(ent(exbl))]]
Rationality is ex-post and any knowledge derived from assuming other agent's rationality is useless to the


### 1. 🟩 Optimizing and Inferring 

Studies using utility maximization frameworks while accounting for real-world constraints and behavioral factors. Shows how classical optimization adapts to empirical challenges.

### 2. 🔵Simulating and Generating 
- **Behavioral Simulation**: Implementation of bounded rationality and heterogeneous agent models, demonstrating how theoretical simulations evolve when confronted with real-world complexity.

Barlas (1996) demonstrates exchangeability testing through the "Turing test" validation approach for system dynamics models. In this simple example, experts are shown a mixed collection of real data patterns and simulated output patterns from the model. If the experts cannot reliably distinguish between real and simulated patterns (i.e., the patterns are "exchangeable" in terms of expert judgment), this provides evidence for model validity. However, if experts can consistently tell which patterns came from the simulation versus reality, they are interviewed to understand what makes these patterns distinguishably different, helping identify where the model's assumption of exchangeability with the real system breaks down. The paper shows how this test was applied to fluid/electrolyte balance models in the human body, where experts evaluated whether simulated and actual patterns of variables like fluid levels were exchangeable in terms of their qualitative features (rises, falls, oscillations, etc.).

Companies face an interesting puzzle: they need to be excellent at their current business while also exploring new opportunities. O'Reilly and Tushman (2016) call this ambidexterity - like being good with both your left and right hands. Here's where exchangeability becomes valuable: when two situations are exchangeable, success in one tells us about likely success in the other. Mastrogiorgio and Marengo (2022) explain this through the lens of exaptation - how traits developed for one purpose can be repurposed for another. For example, Toyota first got really good at building reliable cars (their current business). When looking at making hybrid vehicles (their new opportunity), they realized something cool: their skills in quality control were exchangeable - meaning they could use the same careful testing methods for both regular and hybrid cars. By recognizing which skills are exchangeable across old and new businesses, companies can be better at this two-handed juggling act. It's like finding out your kitchen knife skills from cooking are surprisingly useful for gardening - the basic techniques transfer over. 

### 3. 🔴Approaching Complexity with Modeling Workflow 
- **Statistical Workflow**: Integration of optimization and simulation through data-driven inference, showing how real-world applications often require combining multiple approaches to handle partial exchangeability.

simulation-based calibration

uniformity testing,


- **In Optimization** (the classical model), humans are “perfect decision-makers” with consistent, utility-maximizing behavior. Because real individuals rely on heuristics, have limited information, and often behave inconsistently, behavioral research shows that purely rational optimization frameworks can overlook crucial complexities in human decision-making.

- **In Simulation**, we incorporate _bounded rationality_—heuristics, biases, or emergent phenomena. Even when modeling heuristics, a simulation can remain oversimplified if it ignores the wide range of cognitive biases and social factors, leading to an unrealistically uniform portrayal of ‘boundedly rational’ agents.

- **In Inference**, we **calibrate** (or “train”) these more realistic assumptions on actual data. By systematically collecting real-world observations and updating parameters to fit observed choices, the model can integrate genuine human behavior—including partial exchangeability—into its core assumptions. Here, instead of providing a set of answers, we provide modeling workflow of how to assemble tools (statistical theory, simulation, inference algorithm). Agents in the system use statistical theory to gain deeper understanding of a simulation which is a profitable abstraction of counterfactually repeated phenomena.


----

[[clever-lifting]]

[[🌙amoon()/💭 theorize/🌙thesis/M3_🥚Evol ops growth/T3_🔷resource_rationality/🧶atom_bit_supply/how-clever-is-random|how-clever-is-random]]

computational rationality cognitive science

random utility model

2. **Marketing Mix Models.**
    
    - Researchers often assume different consumer segments are partially exchangeable within a single region. This leads to hierarchical structures where brand-level parameters (like price elasticity) come from a shared hyper-distribution (e.g., Allenby & Rossi in Bayesian marketing).

3. **Manufacturing Process Control.**
    
    - In reliability engineering, one might assume all products from a particular assembly line are exchangeable _unless_ a known factor (such as operator shift or batch) breaks that assumption. This helps detect anomalies in the line (e.g., a subtle batch-level defect) when observed behavior deviates from the exchangeable baseline.
      
4. **Health Outcomes in Clinical Trials.**
    
    - In multi-site clinical trials, we often treat patients at different sites as exchangeable within each site, then impose partial exchangeability across sites. Unexpected non-exchangeability across sites can reveal unique demographic or procedural differences.

---

how exbl appeared in applied papers
- [[📜Vul14_onedone]]'s uses majority voting system to define decision quality in binary choice p * binominal_cdf(n, p) + (1-p) * (1- binominal_cdf(n, p)) and i disagree with treating n people's vote as exchangeable
- [[📜Gans19_EntrepreneurialStrategy]]'s test two choose one uses max(v1,v2) which assumes v1 and v2 are exchangeable (order doesn't matter testing v1 then v2 gives same result as testing v2 then v1)
- [[Aggregate and Marginalize]]'s manufacturing assumes independence across different SKUs ()which is unrealistic (ignoring shared political system)
