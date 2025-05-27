#### Introduction  
Entrepreneurial decision-making under uncertainty involves not only choosing which opportunity to pursue but also how much time and effort to invest in testing before committing. Traditional models in entrepreneurship and innovation—many inspired by Weitzman-style search, optimal stopping rules, and lean experimentation—often rely on simplified assumptions. They frequently treat the decision to stop sampling information as a rule triggered by a threshold value. While elegant, such frameworks tend to overlook three crucial factors:

1. The Time Opportunity Cost: Standard stopping rules ignore the direct time cost of delaying action.
    
2. The Commitment to the Idea: The evolution of an idea from conception to impact is cumulative and can affect how we view the cost of switching or discarding an approach.
    
3. The Aleatoric/Epistemic (A/E) Uncertainty Ratio: Not all uncertainties are created equal. Distinguishing between inherent randomness (aleatoric uncertainty) and ignorance or knowledge gaps (epistemic uncertainty) matters for how we approach parallel vs. sequential strategies.

This paper presents three critiques of the existing entrepreneurship and strategy literature and proposes corresponding prescriptions. By linking these critiques to influential works in cognitive science and product development—particularly the ideas in How to Think What Not to Think ([[📜Phillips19_How We Know What Not To Think]], One and Done, Computational rationality ([[📜Gershman15_comp_rationality]]), and Product design frameworks ([[📜Ulrich20_pd_des_dev]])—we build a richer framework that transcends classic stopping rules and reorients them as “stopping times,” integrates idea commitment dynamics, and incorporates nuanced uncertainty structures.

---

#### Section 1: Time Opportunity Cost – From Stopping Rule to Stopping Time  

[[📜RyanLippman05_opt_exit_deterpj]]
Critique: The first shortcoming is that standard entrepreneurial decision models often emphasize a “stopping rule” perspective, deciding when to halt information collection based on a static threshold. Such approaches neglect the critical fact that time is not free. Delays in implementation impose opportunity costs—markets shift, competitors move, and resources depreciate in value over time. The existing literature’s focus on a stopping rule (e.g., “test until you find an outcome above x-star”) overlooks that each test consumes time and thus reduces net present value (NPV).

Solution: We must move from treating the decision as a mere stopping rule to a “stopping time” problem. Drawing on cognitive science insights, humans often employ limited sampling when under severe time constraints—what the One and Done literature ([[📜tenanbaum14_1sample(1decide)]]) reveals is that individuals rarely integrate over large hypothesis spaces exhaustively. Instead, they rely on a few samples. How to Think What Not to Think (Phillips, Morris & Cushman, 2019) shows we focus on valuable and probable possibilities quickly, consistent with a time-sensitive approach. Likewise, computational rationality suggests that bounded agents adapt strategies to constraints, including time.

By incorporating time-based discounting into search models, we see that waiting for perfect information is suboptimal if the opportunity erodes with delay. Instead of “stop if payoff > x,” the entrepreneur should solve:  
Maximize p(K)Vδ^(Kt) - (Kc),  
where K is the number of tests, δ < 1 is a discount factor capturing time costs, and c is testing cost. The optimal K*—the “stopping time”—explicitly considers that each additional test reduces future payoff via elapsed time. Thus, fewer tests and more rapid decisions become justifiable, explaining “one-shot” experiments and minimal viable product tests.

Prescription (Parallel vs. Sequential):

- Parallel approach: When time costs are high and you want to quickly learn from multiple options, consider testing several ideas simultaneously in a shallow manner. This reduces the calendar time per idea and leverages cross-learning.
    
- Sequential approach: If time is less pressing or each test is cheap, you might afford sequential deep dives. But the more time-sensitive the market, the more you tilt toward parallel exploration to shorten waiting times.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeyOT2Oe4nTx-eCmySTVE-_x1LAI-vrsZBeuhT1--wcEL5zrpi-zcqdaKzslAtLg2QQwc6i30XPmzsuQDDXkudPJtTenP3C0DIT9C3BD9Dfor7KHpWB9YJKxHYZnlZMsFEZuzes?key=S5O2yAlRp2GCpf0U0Ci34u2I)

---

#### Section 2_v1: Commitment to the Idea – Modularity, Quality, and Evolving Hierarchies  
Critique: The literature often assumes ideas as static entities with simple yes/no decisions. In reality, entrepreneurs form commitments over time. An idea evolves through phases: inception, testing, refinement, and impact. Current models rarely capture that an entrepreneur might partially commit to an idea, invest in building specialized capabilities around it, or reconfigure it into a new variant (“Idea 1 prime”). Such incremental commitment creates a hierarchy of idea components and paths. Ignoring this structure oversimplifies the switching cost and fails to model how entrepreneurs’ evolving belief in their idea’s quality affects their strategy.

Solution: We must recognize that ideas are cumulative: knowledge gained can be reused or reassembled. The value of partial experiments is not only in weeding out duds but also in building a platform of capabilities. For instance, How to Think What Not to Think highlights how we focus on actions that have general practical utility. As entrepreneurs test their idea’s core assumptions, they gain modular pieces of know-how. If the initial sub-idea fails, they may pivot, reusing components learned.

Additionally, commitment dynamics relate to uncertainty about execution quality. If entrepreneurs suspect they are not adept at exploring multiple novel directions (poor “jockey” skills), they might deepen commitment to the one “horse” (idea) that seems promising. The idea’s cumulative nature means prior investment constrains future adaptation—akin to path dependencies in strategy (Sydow, Schreyögg & Koch, 2009).

Prescription (Parallel vs. Sequential):

- High Idea Reusability (Parallel): If capabilities and knowledge gained are modular and can be redeployed, a more parallel approach to experimentation can pay off. You invest in many small bets, building a portfolio of partial insights.
    
- Low Idea Reusability (Sequential): If each idea’s test is highly specialized and non-redeployable, sequential deep focus makes more sense. Committing deeply reduces overhead from switching and leverages cumulative understanding of one trajectory.
    

Below is a revised version of the "Commitment to the Idea" section that incorporates the notion of option structures discussed with John, including the idea of exaptative parallel experiments (like Moderna’s approach) and modification as adaptive sequential moves. The changes are highlighted in the context of the existing five-page framework.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcuPvM7JsvYmbXvjjEl725X2vnkv9LBDJdERsGiy-IkpcWlEMdO8TK-TMKj-ZxdDEwiMyuy2_lnzF760xyd4KBufuuC94nlgKS7iZH6zKcxrImpeoH-5Qg-ci2kkayl84f4GBKf?key=S5O2yAlRp2GCpf0U0Ci34u2I)
#### Section 2_v2: Commitment to the Idea – Integrating Option Structures and Cumulative Evolution  
Critique: The literature often treats entrepreneurial ideas as static entities with binary outcomes: either you pursue them fully or discard them entirely. In practice, entrepreneurs manage evolving portfolios of ideas, where partial commitments accumulate, capabilities build up incrementally, and decision paths branch into “option structures.” Ideas are not merely yes/no choices; they represent real options that can be created, expanded, deferred, or abandoned as market signals and internal competencies evolve. Traditional models overlook how the entrepreneur’s increasing commitment to an idea shapes not just the cost of switching but also the value of having the option to pivot later.

Incorporating Option Structures:  
A rich perspective emerges when we view ideas as options within a portfolio. Consider two contrasting archetypes:

1. Exaptative Parallel Approach (Option Creation and Abandonment):  
    Inspired by examples like Moderna’s mRNA vaccine development approach, entrepreneurs may advance multiple independent initiatives in parallel. Each initiative’s partial progress generates modular insights (technological capabilities, market intel) that have value beyond the primary application. Even if a particular idea is never exercised (fully implemented), holding it as an option can be beneficial. By testing multiple variants, entrepreneurs gain the flexibility to abandon underperforming paths without losing all informational value. This is analogous to a “parallel” strategy where each line of R&D is treated as a call option on future success—exercised if conditions warrant, abandoned if not, but always yielding some residual knowledge.  
      
    
2. Adaptive Sequential Approach (Modification and Deepening):  
    Conversely, when switching costs are high or idea-specific assets accumulate (specialized knowledge or capabilities locked into one trajectory), an “adaptive sequential” model emerges. Here, entrepreneurs invest deeply in one promising path and continually refine it. Instead of creating numerous parallel options, they focus on modifying and improving a single approach over time. Commitment intensifies, as the entrepreneur’s cumulative learning and resource investments make pivoting costly. However, this deepened commitment can pay off if the initial path turns out to be correct, leveraging path-dependent learning and minimizing the overhead of managing multiple options in parallel.  
      
    

Rationale and Cognitive Insights:  
From a cognitive standpoint, How to Think What Not to Think suggests that humans focus initially on likely and valuable actions. By maintaining multiple promising ideas as options, entrepreneurs can quickly zero in on the most fruitful paths. Over time, the evolving “option structure” means they either deepen their bet sequentially (adaptation) or shift their bets across previously established alternatives (exaptation). Additionally, the “one and done” principle, where minimal sampling suffices to narrow down choices, supports the exaptative parallel model: entrepreneurs gain just enough evidence to preserve options rather than fully commit to one prematurely.

Prescription (Parallel vs. Sequential):

- Option-Rich, Exaptative Parallel: When individual ideas are modular and their partial outcomes have value that can transfer to other projects, maintaining multiple options in parallel makes sense. Entrepreneurs can afford quick tests, preserve valuable fallback options, and abandon unpromising routes with minimal regret.
    
- Option-Narrowing, Adaptive Sequential: If knowledge and capabilities are highly specific and non-transferrable, it may be more efficient to commit sequentially, deepening investment in one path. Over time, iterative modification refines the single chosen trajectory, converting uncertainty into cumulative learning while minimizing the complexity of managing multiple unused options.
    

  

---

#### Section 3: The A/E Uncertainty Ratio – Differentiating Aleatoric from Epistemic Unknowns  
Critique: Entrepreneurship scholarship often conflates all uncertainty into a single dimension. Yet, there is a meaningful difference between aleatoric (inherent, random) and epistemic (ignorance-based) uncertainty. Epistemic uncertainty can be reduced through learning, while aleatoric uncertainty is irreducible risk. Current strategy models don’t explicitly incorporate the ratio of A/E uncertainty. This matters because product development and market strategies differ depending on whether we face unknown-but-knowable information (epistemic) or fundamental randomness (aleatoric).

Drawing from product design frameworks (Ulrich & Eppinger, 2016), we consider opportunities along two axes: knowledge of user needs and knowledge of solutions (methods, technologies). Regions in this space differ in how uncertainty is structured. For instance, a startup that knows the user need well but must invent novel technology faces mostly epistemic uncertainty about a solution—trial and error reduces ignorance. Conversely, a venture gambling in a completely new domain with unknown users and unknown technologies might face more aleatoric elements.

One and Done logic applies here too: when facing high epistemic uncertainty, sampling few data points may suffice to gain insight. Reducing epistemic uncertainty allows more confident choice. But if the uncertainty is primarily aleatoric, further sampling adds little predictive power. Instead of infinite tests, entrepreneurs must accept the dice roll and commit based on their best guess.

Solution: By formalizing uncertainty types, entrepreneurs can choose strategies aligned with the ratio of A/E uncertainty. High epistemic uncertainty supports parallel experiments that quickly map out unknown territory, while high aleatoric uncertainty favors learning to accept risk or mitigating it through contracts, hedging, or staged commitments.

Prescription (Parallel vs. Sequential):

- High Epistemic Uncertainty → Parallel Learning: When ignorance dominates, run multiple small tests in parallel. For example, a product design team might quickly prototype multiple concepts (Ulrich & Eppinger, 2016) to reveal where knowledge gaps lie and to reduce epistemic uncertainty efficiently.
    
- High Aleatoric Uncertainty → More Cautious and Possibly Sequential Steps: If randomness can’t be easily reduced, it might make sense to proceed sequentially, extracting partial information from each step and adapting slowly. Or commit sooner once you realize additional tests won’t help.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcN3e5iwKImFdPP4YRPofCvmEK86jOorgmyDXCeTH_o3NvW8zCVHjGgQcG5kxmLBCX8797c_5HyAkkHMBXhzGvkh21FRSEGw-MnhbNJ_G5aqmYDCtwfIYVww_hsiYPFn_DGAsKU?key=S5O2yAlRp2GCpf0U0Ci34u2I)

---

#### Integrating the Three Critiques  
While each critique stands alone, together they reveal a richer picture:

1. Time Costs force us to think in stopping times, not rules. The entrepreneur’s clock is ticking; a delay in committing erodes value.
    
2. Idea Commitment acknowledges that opportunities evolve and capabilities accumulate. This dynamic shapes whether breadth (parallel) or depth (sequential) is optimal.
    
3. A/E Uncertainty Ratio clarifies what kind of uncertainty we’re facing. Reducing epistemic uncertainty justifies more parallel experimentation, while confronted by irreducible aleatoric uncertainty, entrepreneurs might stop testing sooner.
    

Combining these insights yields a conceptual map:

- When time pressure is severe, and uncertainty is largely epistemic, parallel rapid tests (“one and done” style) maximize learning per unit time.
    
- When you have strong cumulative capability in one direction, and the cost of switching is high, a more sequential, committed path may dominate.
    
- If much uncertainty is aleatoric, no amount of waiting will help—thus time cost considerations push you to commit earlier rather than continually sampling.
    

---

#### Conclusion  
Classic entrepreneurial search models often present decisions as neat stopping rules and ignore the nuanced interplay of time costs, idea commitment structures, and differences in uncertainty types. By introducing time opportunity costs, we convert stopping rules into dynamic stopping times. By modeling idea commitment and modularity, we appreciate how entrepreneurial portfolios evolve rather than just pivot. By distinguishing aleatoric from epistemic uncertainty, we guide parallel versus sequential strategies with a more principled rationale.

References in cognitive science and product development—How to Think What Not to Think, One and Done, computational rationality, and Ulrich & Eppinger’s product design frameworks—underscore that real-world entrepreneurs operate under tight deadlines, partial commitments, and complex uncertainty structures. Embracing these three critiques enriches our theoretical models, aligning them more closely with entrepreneurial reality. The result is a set of refined prescriptions on how and when to run tests in parallel or sequentially, how to leverage evolving idea hierarchies, and how to tailor strategies to the type of uncertainty faced.

In sum, the next generation of entrepreneurship models must move beyond simplistic stopping thresholds, integrating time, cumulative idea development, and nuanced uncertainty to generate more credible guidance for practice and richer insights for research.

---

References

- Phillips, J., Morris, A., & Cushman, F. (2019). How to Think What Not to Think. Trends in Cognitive Sciences.
    
- Vul, E., Goodman, N., Griffiths, T. L., & Tenenbaum, J. B. (2014). One and done? Optimal decisions from very few samples. Cognitive Science.
    
- Gershman, S. J., Horvath, J. C., & Tenenbaum, J. B. (2015). Computational rationality: A converging paradigm for intelligence in brains, minds, and machines. Science.
    
- Sydow, J., Schreyögg, G., & Koch, J. (2009). Organizational path dependence: Opening the black box. Academy of Management Review.
    
- Ulrich, K. T., & Eppinger, S. D. (2016). Product Design and Development. 6th ed. McGraw-Hill.
    

**