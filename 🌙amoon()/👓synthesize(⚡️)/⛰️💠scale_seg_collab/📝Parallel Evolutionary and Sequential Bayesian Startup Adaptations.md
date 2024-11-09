- 
- 
	- [[#2. Model#2.1 🧠/📍 low cost ratio of sampling to action|2.1 🧠/📍 low cost ratio of sampling to action]]
	- [[#2. Model#2.2 🎲 high Uncertainty|2.2 🎲 high Uncertainty]]
	- [[#2. Model#2.3🧩 low correlation|2.3🧩 low correlation]]
- [[#3. Meaning with examples|3. Meaning with examples]]
- 
- [[#Notes:|Notes:]]
- [[#Notes:#Comparison of Three Strategies:|Comparison of Three Strategies:]]
- [[#Notes:#Assignment of Key Insights to Chapters:|Assignment of Key Insights to Chapters:]]
- [[#Incorporating JB's and Charlie's Papers:|Incorporating JB's and Charlie's Papers:]]
- [[#Incorporating JB's and Charlie's Papers:#JB's Papers:|JB's Papers:]]
- [[#Incorporating JB's and Charlie's Papers:#Charlie's Papers:|Charlie's Papers:]]
- [[#Next Steps:|Next Steps:]]
- [[#Next Steps:#Abstract|Abstract]]
- [[#Next Steps:#**Introduction: Strategic Experimentation and Pivots in Uncertain Markets**|**Introduction: Strategic Experimentation and Pivots in Uncertain Markets**]]
- [[#Next Steps:#**Parallel and Sequential Search in Experimentation**|**Parallel and Sequential Search in Experimentation**]]
	- [[#**Parallel and Sequential Search in Experimentation**#**Parallel Search: Rapid Innovation through Broad Exploration**|**Parallel Search: Rapid Innovation through Broad Exploration**]]
	- [[#**Parallel and Sequential Search in Experimentation**#**Sequential Search: Methodical Learning through Stepwise Exploration**|**Sequential Search: Methodical Learning through Stepwise Exploration**]]
- [[#Next Steps:#**The “Test Two, Choose One” Rule and Pivot Thresholds**|**The “Test Two, Choose One” Rule and Pivot Thresholds**]]
- [[#Next Steps:#**Behavioral Biases and Entrepreneurial Decision-Making**|**Behavioral Biases and Entrepreneurial Decision-Making**]]
- [[#Next Steps:#**Exaptation and the Adjacent Possible**|**Exaptation and the Adjacent Possible**]]
- 
- [[#Next Steps:#**Conclusion: Leveraging Exaptive Strategies for Startup Success**|**Conclusion: Leveraging Exaptive Strategies for Startup Success**]]
- [[#Next Steps:#**References**|**References**]]

[[eval(recovering rationality of venture's adaptation)]]


T2C1: test two choose one
- 🧱https://github.com/Data4DM/BayesSD/discussions/246#discussioncomment-10852783 
> 1. angie's prep for abstract submission [Navigating Exploration and Commitment in Uncertain Markets cld](https://claude.ai/chat/29824b40-5872-4b34-a5ac-98ba0760a83d)
>    2. summary of yichen's feedback  
    • 🔄 Comparability of test-two-choose-one-twice vs. test-four-choose-one: Angie suggests lowered cost of partial-commitment learning and faster testing clockspeed (e.g., GPT) may make the two scenarios more comparable  
    • 🧠 Learning and development between stages in sequential search: Angie proposes increasing individual heterogeneity to reduce the impact of learning between stages  
    • 💰 Need for additional costs in parallel search (segmentation costs): Angie agrees to add segmentation costs to the model for parallel search  
    • 🌀 Circularity in the argument about exaptation and parallel search: Angie explains that parallel search creates a larger "spandrel" or free space early on, facilitating exaptation  
    • 🏭 Clarity needed on industry-specific factors and company-level characteristics: Angie confirms this part is based on simulation using empirical research on industry clock speed

| Section                                                   |                                                                                                              | Research Question (🔐)                                                                                                                                                                                                                                                                                                                 | Literature Brick (🧱)                                                                                                                                                                                                                                                                                                                                                             | Key Message (🔑)                                                                                                                                                                                                                                                                                                                                         | Bridge (🌉)                                                    | fig                                       |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ----------------------------------------- |
| [[#1. Theoretical Background\|1. Theoretical Background]] |                                                                                                              | What conditions make parallel search more effective than sequential?                                                                                                                                                                                                                                                                   | **JB**: [[📜Andriani17_msr_exaptation_pharma]] on pharma exaptation frequency<br>[[📜Andriani16_ExaptationCreativity]] on innovation sources<br><br>**Charlie**: [[📜Agrawal21_ebl_choice]] on choice architecture<br>[[📜gans23_expchoice]] on technology disruption<br><br>[[📜DOW10_parallel_prototyping]] supports parallel, [[📜Ott18_decision_weaving]] is against parallel | Three key mechanisms affect search strategy:<br>- Testing cost ratio<br>- Outcome uncertainty<br>- Up/downstream correlation                                                                                                                                                                                                                             | These mechanisms lead us to examine each factor individually → | ![[Pasted image 20241108180209.png\|100]] |
| [[#2. Model\|2. Model]]                                   |                                                                                                              |                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                   | We compare the three strategies:<br>T2C1_PM (Product then Market): 🧠2️⃣ → 📍1️⃣ → 🧠2️⃣ → 📍1️⃣ <br>**T2C1_MP** (Market then Product): 🧠2️⃣ → 📍1️⃣ → 🧠2️⃣ → 📍1️⃣ <br>**T4C1**  (Test all four; Testing all combinations simultaneously.): 🧠4️⃣ → 📍1️⃣<br>We analyze how each strategy affects sampling ratios, decision steps, and search spaces. |                                                                |                                           |
|                                                           | [[#2. Model#2.1 🧠/📍 low cost ratio of sampling to action\|2.1 🧠/📍 low cost ratio of sampling to action]] | How does low sample-to-action cost ratio affect search strategy?                                                                                                                                                                                                                                                                       | **JB**: [[📜Cattani21_BusinessModelInnovation]] on SME innovation<br><br>                                                                                                                                                                                                                                                                                                         | When testing cost is low relative to implementation, parallel search becomes more viable                                                                                                                                                                                                                                                                 | Cost analysis raises questions about uncertainty's role →      |                                           |
|                                                           | [[#2. Model#2.2 🎲 high Uncertainty\|2.2 🎲 high Uncertainty]]                                               | How do different types of uncertainty (fixed vs increasing σ) affect strategy?                                                                                                                                                                                                                                                         | **JB**: [[📜Haselton82_Spandrels]] on adaptations and spandrels<br><br>**Charlie**: [[📜nasa_parallel]] on parallel development                                                                                                                                                                                                                                                   | Higher uncertainty favors parallel search, especially with non-stationary variance                                                                                                                                                                                                                                                                       | Uncertainty analysis leads to correlation questions →          |                                           |
|                                                           | [[#2. Model#2.3🧩 low correlation\|2.3🧩 low correlation]]<br>                                               | How does correlation between upstream and downstream activities affect choice?                                                                                                                                                                                                                                                         | **JB**:<br>[[📜Mastrogiorgio22_thumbs_rules_rational_exapt]]<br>on rule adaptation<br>**Charlie**<br>-  [[📜Phadnis17_e2e]] on supply chain strategy<br>- [[📜Sculley15_hidden_tech_debt]] on hidden feedback loops                                                                                                                                                               | Lower correlation between activities makes parallel search more effective                                                                                                                                                                                                                                                                                | Correlation insights point to integration questions →          |                                           |
| [[#3. Meaning with examples\|3. Meaning with examples]]   |                                                                                                              | 🎲Moderna's parallel entrepreneurship<br><br><br>🧩correlation lowering strategy between sourcing and sales? (todo: can we think of example in Tesla)                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                          |                                                                |                                           |
| [[#4. TODO/Future Work\|4. TODO/Future Work]]             |                                                                                                              | 1. How do these insights apply to modular vs integral systems? Semiconductor (TMSC-Nvidia VS IDM (Samsung Intel)) (@Charlie)<br><br>2. systemic analysis of type1,2 error (@JB)<br><br>[[#Next Steps:#**Visualization of Pivot Dynamics and Exaptive Opportunities**\|**Visualization of Pivot Dynamics and Exaptive Opportunities**]] | **Charlie**: [[📜integrated_vs_modular]] on semiconductor industry<br><br>2. [[📜Heimann93_challenger_org]]                                                                                                                                                                                                                                                                       | Framework for analyzing search strategies in different system architectures                                                                                                                                                                                                                                                                              | Opens new research directions on system design and search      |                                           |



### 1. Theoretical Background

### 2. Model


| Model Type     | Sample-Action Ratio | Decision Steps | Search Space |
| -------------- | ------------------- | -------------- | ------------ |
| Product→Market | 2:1 (twice)         | 2 sequential   | 2+2 options  |
| Market→Product | 2:1 (twice)         | 2 sequential   | 2+2 options  |
| Full Search    | 4:1                 | 1 combined     | 4 options    |
#### 2.1 🧠/📍 low cost ratio of sampling to action
#### 2.2 🎲 high Uncertainty
#### 2.3🧩 low correlation

##### 🗄️2.3 example of correlation

| Interaction Direction                                                                                         | Operational Dynamics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Case Evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **How <font color = "#C0A0C0">Segmentation</font> Enable/Constrain <font color = "Red">Collaboration</font>** | 1. **Supply Chain Complexity:**<br>- Each new <font color = "#C0A0C0">segment</font> requires different <font color = "Red">supplier</font> capabilities<br>- Geographic expansion strains <font color = "Red">collaborator</font> partner relationships<br>- Volume/variety trade-offs affect <font color = "Red">collaborator</font> selection<br><br>2. **Capability Requirements:**<br>- Different <font color = "#C0A0C0">segments</font> need different technical expertise<br>- Partners must scale capabilities across <font color = "#C0A0C0">segments</font><br>- Quality standards vary by <font color = "#C0A0C0">segment</font><br><br>3. **Control Challenges:**<br>- Multiple <font color = "#C0A0C0">segments</font> increase coordination complexity<br>- <font color = "Red">Collaborator</font> capabilities may not span all segments<br>- Risk of losing control over quality/delivery | **Tesla:**<br>- Initial Roadster <font color = "#C0A0C0">segment</font> required specific <font color = "Red">suppliers</font> (Lotus for chassis, Asian suppliers for batteries/electronics)<br>- 8-week design-manufacture-test cycles and $29k/car air freight costs due to dispersed <font color = "Red">collaboration</font><br>- Forced to restructure entire supply chain for Model S<br><br>**BGI, Micrometal:**<br>- Each new <font color = "#C0A0C0">segment</font> required different <font color = "Red">collaborator</font> expertise<br>- Quality certifications varied across industry <font color = "#C0A0C0">segments</font><br>- Had to build new <font color = "Red">collaboration</font> models per segment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **How <font color = "Red">Collaboration</font> Enable/Constrain <font color = "#C0A0C0">Segmentation</font>** | 1. **Market Access:**<br>- Partner capabilities limit serviceable segments<br>- <font color = "Red">Collaboration</font> network affects geographic reach<br>- Partner relationships open new segments<br><br>2. **Technical Limitations:**<br>- Partner expertise constrains <font color = "#C0A0C0">segment</font> choices<br>- Joint learning enables <font color = "#C0A0C0">segment</font> expansion<br>- Innovation depends on collaborative capability<br><br>3. **Operational Constraints:**<br>- Partner scale limits <font color = "#C0A0C0">segment</font> growth<br>- Geographic footprint affects <font color = "#C0A0C0">segment</font> choices<br>- <font color = "Red">Collaboration</font> quality impacts <font color = "#C0A0C0">segment</font> viability                                                                                                                                | **Tesla:**<br>- Initial <font color = "Red">supplier</font> choices led to unsustainable prototype cycles<br>- Geography-driven <font color = "Red">collaboration</font> model prevented efficient <font color = "#C0A0C0">segment</font> expansion<br>- Fremont consolidation enabled better control over new <font color = "#C0A0C0">segments</font><br><br>**Angularity:**<br>- Started as equipment manufacturer for electronics <font color = "#C0A0C0">segment</font><br>- Used manufacturing expertise from initial <font color = "Red">partnerships</font> to pivot into component markets<br>- Successfully competed with former customers in new <font color = "#C0A0C0">segments</font><br><br>**MediTech (Failure Case):**<br>- Chose <font color = "Red">suppliers</font> solely for technical superiority<br>- Large <font color = "Red">suppliers</font> didn't prioritize small-lot prototypes<br>- Ran out of cash before proven viable in medical imaging <font color = "#C0A0C0">segment</font><br><br>**SkinnyGirl (Failure Case):**<br>- Initial <font color = "Red">fulfillment partner</font> couldn't scale with demand<br>- Lost control of brand value in spirits <font color = "#C0A0C0">segment</font><br>- Sold to large beverage company but lost market momentum |


### 3. Meaning with examples

### 4. TODO/Future Work

##### **Visualization of Pivot Dynamics and Exaptive Opportunities**

Visualization tools can play a crucial role in tracking how exaptive processes drive entrepreneurial pivots. By visualizing the **adjacent possible**, entrepreneurs can identify emerging opportunities and make informed decisions about how to reconfigure their existing resources. **Mansinghka (2021)** and **Chen et al. (2020)** recommend using dynamic visualizations to track the emergence of exaptive opportunities during parallel and sequential search strategies.

**Monika Blattmeier (2023)** delves deeper into the aestheticization of business processes, emphasizing how visualizing their **Gestalt** can enhance collective decision-making. This visualization approach helps entrepreneurs see the holistic potential of their business models and innovation pathways. Such tools foster collective thinking in startups, helping teams make more informed decisions when navigating pivot dynamics.


---
[Test-Four-Choose-One 💠 (Parallel Search) vs Test-Two-Choose-One Twice 🔷-💠 (Sequential Search)](https://github.com/Data4DM/BayesSD/discussions/246#discussioncomment-10852672)


| Section                              | Research Question (🔐)                                                                                                     | Literature Brick (🧱)                                                                                                                                                                                                                                                                                                                                   | Key Message (🔑)                                                                                                                                                                                                        | Bridge to Next Section (🌉)                                                                                    |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **1. Theoretical Foundation**        | How do startups rationally allocate resources between parallel vs sequential search strategies under bounded rationality?  | [[📜Gans19_EntrepreneurialStrategy]]: T2C1 framework shows how entrepreneurs sequence product-market fit experiments<br><br>[[📜Felin21_ResourceOriginsSearch]]: Explains when parallel search becomes optimal for resource discovery<br><br>[[📜Haselton82_Spandrels]]: Demonstrates how evolutionary systems handle parallel vs sequential adaptation | Search strategy choice can be modeled as resource allocation problem:<br>- Sequential = depth-first exploration<br>- Parallel = breadth-first exploration<br>- Both can be optimal depending on environment constraints | This resource allocation framing leads us to examine specific factors that determine optimal strategy choice → |
| **2. Strategy Selection Mechanisms** | What environmental and organizational factors determine optimal sampling ratio between parallel vs sequential experiments? | [[📜Eisenmann12_HypothesisDrivenEntrepreneurship]]: Lower sampling ratios enable faster learning cycles<br><br>[[📜Thomke98_ManagingExperimentation]]: Higher variance in parallel experiments improves selection<br><br>[[📜Gould82_Spandrels]]: Low correlation between options makes parallel search more effective                                  | Optimal strategy depends on three key factors:<br>- Sampling ratio (cost per experiment)<br>- Variance (σ) in outcomes<br>- Correlation between options                                                                 | Understanding these mechanisms raises question of how to measure and model them →                              |
| **3. Measurement Model**             | How can we quantify and predict optimal search strategy given specific context?                                            | [[📜Gelman13_BayesianDataAnalysis]]: Hierarchical Bayesian modeling framework<br><br>[[📜Bell22_PhantomAttributes]]: Models unobservable strategic attributes<br><br>[[📜Kauffman95_AdjacentPossible]]: Maps exploration space in evolutionary systems                                                                                                  | Develop measurement model that:<br>- Uses hierarchical Bayes<br>- Incorporates evolutionary concepts<br>- Accounts for unobservable attributes                                                                          | This model enables practical recommendations for entrepreneurs and investors                                   |

Role Integration:
- **Scientist** (Angie): Formalizes resource allocation model and develops measurement framework
- **Artist** (JB): Maps evolutionary concepts to search strategies
- **Judge** (Charlie): Evaluates practical implications and strategic recommendations
- 

| Section                       | 🔐 Lock and Key                                                                                                                                   | 🧱 Brick                                                                                                                                                                                                                                | 🔑 Our Key                                                                                                                                                                 | 👥 Role Assignments                                                                                                            |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **1. Theoretical Foundation** | How do startups decide between parallel and sequential search strategies? What are the differences between T2C1_PM, T2C1_MP, and T4C1 strategies? | - [[📜Gans19_EntrepreneurialStrategy]] explains T2C1 framework<br>- [[📜Felin21_ResourceOriginsSearch]] <br>- [[📜Haselton82_Spandrels]] on evolutionary concepts<br>- [[📜Andriani17_msr_exaptation_pharma]] on empirical evidence          | We analyze how evolutionary concepts inform startup search strategies, comparing:<br>- T2C1_PM (Product→Market)<br>- T2C1_MP (Market→Product)<br>- T4C1 (All combinations) | **Scientist**: Model framework<br><br>**Artist**: Map evolutionary concepts<br><br>**Judge**: Evaluate strategic implications  |
| **2. Model**                  | How do sample-action ratio, variance, and correlation affect decision-making efficiency?                                                          | - [[📜Eisenmann12_HypothesisDrivenEntrepreneurship]] on sampling efficiency<br>- [[📜Thomke98_ManagingExperimentation]] on variance<br>- [[📜Gould82_Spandrels]] on correlation effects<br>- [[📜Bell22_PhantomAttributes]] on modeling | We develop a hierarchical Bayesian model incorporating:<br>- Sampling ratio impacts<br>- Variance effects<br>- Correlation influence                                       | **Scientist**: Develop Bayesian model<br><br>**Artist**: Envision evolutionary mechanisms<br><br>**Judge**: Assess feasibility |
| **3. Vision & Impact**        | How does our research contribute to entrepreneurial strategy and innovation?                                                                      | - Integration of evolutionary concepts<br>- Synthesis of Bayesian modeling<br>- Practical applications for startups                                                                                                                     | We provide:<br>- Theoretical synthesis<br>- Practical frameworks<br>- Strategic insights                                                                                   | **Scientist**: Analyze implications<br>**Artist**: Explore future adaptations<br>**Judge**: Evaluate utility                   |

Notes: 
- Scientist (Angie) focuses on programmable inference and meta-cognition
- Artist (JB) imagines evolutionary synthesis with Bayesian approaches
- Judge (Charlie) evaluates operationalization and practical implications


**Role Synthesis Framework:**
- **Scientist × Artist**: Discovery through synthesis of Bayesian and evolutionary approaches
- **Scientist × Judge**: Skill development in understanding pivoting and strategic adaptation
- **Collective Goal**: 
  - Scientist (Angie): Understanding what will happen
  - Artist (JB): Imagining what might happen
  - Judge (Charlie): Evaluating utility of what happens


| 🔑 Our Key                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| We set the stage by introducing the challenge startups face in selecting search strategies and how evolutionary concepts can inform this decision-making process.                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                        |
| We explore how a lower ratio between sampling and action points leads to more efficient decision-making, particularly in the context of the three search strategies.                                                                                                                                                                                                                                                   |
| We analyze how higher variance (sigma) in the sampling process results in more reliable final selections, emphasizing the benefits of embracing uncertainty in experimentation.                                                                                                                                                                                                                                        |
| We examine how lower correlation between options enables better discrimination between choices, aiding startups in selecting optimal paths during experimentation.                                                                                                                                                                                                                                                     |
| We synthesize insights from JB's and Charlie's recommended papers, integrating evolutionary concepts and strategic management theories to enrich our analysis of startup adaptation strategies.                                                                                                                                                                                                                        |
| We propose developing a hierarchical Bayesian model to compare the three strategies, incorporating evolutionary concepts like exaptation and spandrels, and accounting for factors such as sampling ratio, variance, and correlation.                                                                                                                                                                                  |
| - **Chapter 3**: Assigned to **Lower Ratio of Sampling and Action**.<br>- **Chapter 4**: Assigned to **Higher Sigma (Variance)**.<br>- **Chapter 5**: Assigned to **Lower Correlation**.<br>This organization helps focus each chapter on analyzing how these specific factors influence the effectiveness of the search strategies.                                                                                   |
| - **Scientist (Angie):** Develop the hierarchical Bayesian model and analyze the impact of sampling ratio, variance, and correlation.<br>- **Artist (JB):** Imagine how evolutionary concepts like exaptation and spandrels can be modeled within the agent-environment belief framework.<br>- **Judge (Charlie):** Evaluate the operationalization of evolutionary concepts and assess their utility and feasibility. |
| - **Review Literature:** Deep dive into the selected papers, focusing on how they inform our model.<br>- **Model Refinement:** Incorporate evolutionary concepts into the Bayesian model.<br>- **Simulation:** Compare T2C1_PM, T2C1_MP, and T4C1 strategies under varying conditions.<br>- **Meeting:** Schedule collaborative sessions to share insights and integrate feedback.                                     |
| We conclude by summarizing how our collaborative effort enhances understanding of startup adaptation strategies, providing both theoretical contributions and practical implications for entrepreneurs and investors.                                                                                                                                                                                                  |

[[👻phantom rationalize meaning]]

---

## Notes:

### Comparison of Three Strategies:

- **T2C1_PM (Test Two, Choose One - Product then Market):**

  - **Sample-Action Ratio:** 2:1 (twice)

  - **Decision Steps:** 2 sequential decisions

  - **Search Space:** 2 products tested, choose one; then test 2 markets, choose one.

- **T2C1_MP (Test Two, Choose One - Market then Product):**

  - **Sample-Action Ratio:** 2:1 (twice)

  - **Decision Steps:** 2 sequential decisions

  - **Search Space:** 2 markets tested, choose one; then test 2 products, choose one.

- **T4C1 (Test Four, Choose One):**

  - **Sample-Action Ratio:** 4:1

  - **Decision Steps:** 1 combined decision

  - **Search Space:** All 4 product-market combinations tested simultaneously.

### Assignment of Key Insights to Chapters:

- **Chapter 3:** Impact of Sampling Ratio – Focuses on how lower ratios between sampling and action points lead to more efficient decision-making.

- **Chapter 4:** Effect of Variance (Sigma) – Discusses how higher variance in the sampling process results in more reliable final selections.

- **Chapter 5:** Role of Correlation – Examines how lower correlation between options enables better discrimination between choices.

---
- 📜 **Andriani, P., & Cattani, G.** (2016). *Exaptation as Source of Creativity, Innovation, and Diversity*. *Industrial and Corporate Change*, 25(1), 115–131.
- 📜 **Andriani, P., & Cattani, G.** (2017). *Functional Diversification and Exaptation: The Emergence of New Drug Uses in the Pharmaceutical Industry*. *Organization Science*, 28(1), 30–47.
- 📜 **Cattani, G., & Ferriani, S.** (2021). *Business Model Innovation and Exaptation: A New Way of Innovating in SMEs*. *European Management Journal*, 39(5), 521–529.
📜 **Felin, T., Kauffman, S., & Mastrogiorgio, A.** (2021). *Resource Origins and Search: Property Rights, Innovation, and Value Creation*. *Strategic Management Journal*, 42(1), 7–24.
📜 **Gould, S. J., & Vrba, E. S.** (1982). *Exaptation—a Missing Term in the Science of Form*. *Paleobiology*, 8(1), 4–15.
📜 **Kauffman, S. A.** (1995). *At Home in the Universe: The Search for the Laws of Self-Organization and Complexity*. Oxford University Press.
 📜 **Haselton, M. G., & Nettle, D.** (2006). *The Paranoid Optimist: An Integrative Evolutionary Model of Cognitive Biases*. *Personality and Social Psychology Review*, 10(1), 47–66.
### Charlie's Papers:

- 📜 **Gans, J.** (2015). *The Disruption Dilemma*. *MIT Sloan Management Review*, 57(1), 31–34.
- 📜 **Krishnan, S., et al.** (2014). *Technical Debt in Large Systems: Understanding the Cost of Software Evolution*. *Communications of the ACM*, 57(9), 50–57.
- 📜 **Gans, J., Stern, S., & Wu, J.** (2019). *Foundations of Entrepreneurial Strategy*. *Strategic Management Journal*, 40(5), 736–756.
- 📜 **Eisenmann, T., Ries, E., & Dillard, S.** (2012). *Hypothesis-Driven Entrepreneurship: The Lean Startup*. *Harvard Business School Background Note*, 812-095.
- 📜 **Thomke, S.** (1998). *Managing Experimentation in the Design of New Products*. *Management Science*, 44(6), 743–762



---


even with agent with joint resource and business choice capability (established by [[📝Recovering Cost and Revenue Reasoning Rationality with Environments]] and [[📝Conversational Inference of Equity Valuation Agreement]]), we need world model. this paper and [[📝Startup Lifecycle World modeling with Program Synthesis]] are two sides of one coin as the former assumes world model clockspeed is faster than the latter whereas this (repurposing of existing resources for new uses) introduces the concept of world modeling in operations.  
[[📝Recovering Cost and Revenue Reasoning Rationality with Environments]]

- below table belongs here compared to [[📝Recovering Cost and Revenue Reasoning Rationality with Environments]]: 🗄️table5. further work on interrelated segmentation and collaboration
- feedback loop between <font color  = "Red">operation cost</font> and <font color  = "#C0A0C0">customer acquisition cost</font> (the more customer you get e.g. government - reference, you need less operations cost to diversify; vice versa, if you cut operations cost, the longer your runway becomes so you can endure till you find good enough customer group)


🧱Bricks:
- [🧭🗺️selling entrepreneurial compass/map as Bayesian Entrepreneurship](https://github.com/Data4DM/BayesSD/discussions/234)
- [⛓️⚙️ 🧬selling value chain tools as evolutionary entrepreneurship](https://github.com/Data4DM/BayesSD/discussions/100)(esp. on [evolutionary as frequentist and crossfit](https://github.com/Data4DM/BayesSD/discussions/100#discussioncomment-10738412))
- [🛠️selling probabilistic program to implement Entrepreneurship](https://github.com/Data4DM/BayesSD/discussions/224)
- [parallel ent: insight from moderna, kwldg transfer from ML](https://github.com/Data4DM/BayesSD/discussions/246)
- [[comp(🏳️‍🌈)]]

---
alternative title: Sequential and Parallel Pivots: Two Exaptive Strategies for Entrepreneurial Innovation

2024-10-26
connecting conditions for spandrel with 'low test cost, low variance within supply and demand, low correlation between supply and demand' being the condition for parallel search, I'd highly recommend [felin_kauffman_zenger21-resource_origins_search.pdf](https://github.com/user-attachments/files/17530303/Strategic.Management.Journal.-.2021.-.Felin.-.Resource.origins.and.search.pdf) on 'Resource Origins and Search.' Their concept of 'search images' - firm-specific ways of seeing and identifying valuable resources that others might miss - offers valuable insights for our work. Rather than conducting exhaustive search or relying solely on existing endowments, they argue firms can search more effectively by starting with a functional need or problem they aim to solve. This framework could enhance our understanding of when parallel search is optimal, particularly in situations with low test costs (when the search image clearly guides what to look for), low variance (when the search image helps identify specific resource properties), and low correlation (when the search image enables recognition of novel resource combinations). Their perspective on how firms recognize dormant value in resources could help us better formalize the conditions under which parallel search strategies outperform sequential approaches, especially in evolving market environments.
[[JB __ Angie_cheap test, hetero, less correlation_otter_ai.txt]]

---
### Abstract
Research Summary: This study investigates the efficacy of parallel versus sequential search strategies in testing value creation hypotheses for entrepreneurial ventures. We develop a Bayesian model using probabilistic programming to compare parallel "test-four-choose-one" and sequential "test-two-choose-one-twice" approaches across various contexts. Our analysis focuses on two key dimensions: technological innovation (component vs. system innovations) and customer segments (existing vs. new users). The study reveals that parallel search tends to outperform sequential search under specific conditions: (1) when the cost of each test is low relative to pivoting costs💸, (2) when uncertainty in technological innovations and customer segments is high🎲, and (3) when the true values of technological innovations and customer segments have low correlation🧩. We also examine industry-specific factors and company-level characteristics that influence the optimal search strategy, providing insights into when entrepreneurs should adopt broad, simultaneous exploration versus more focused, step-by-step approaches. 

Managerial Summary: In entrepreneurial ventures, the choice between parallel and sequential search strategies for testing value creation hypotheses depends on industry characteristics and company-specific factors. Parallel search excels in industries with fast clockspeeds, low test costs, high uncertainty, and low correlation between technological innovations and customer segments. For instance, personal computers, toys, and semiconductors benefit from parallel approaches due to their low test costs 💸, high uncertainty 🎲, and potentially low correlation 🧩. Conversely, industries like shipbuilding, petrochemicals, and commercial aircraft favor sequential strategies due to slow clockspeeds and high development costs. However, company-specific factors can override industry norms, as exemplified by Moderna's successful parallel search in the typically sequential pharmaceutical industry. Moderna's mRNA platform enables faster, cheaper development 💸, operates in a novel, uncertain space 🎲, and has potential applications across various diseases 🧩, making parallel search advantageous. This nuanced approach to search strategies enables entrepreneurs to optimize their exploration of technological innovations and customer segments based on their unique context and uncertainties.   
keywords: entrepreneurial strategy, parallel search, sequential search, value creation hypotheses, technological innovation, customer segments, industry clockspeed, uncertainty, Bayesian modeling, probabilistic programming

### **Introduction: Strategic Experimentation and Pivots in Uncertain Markets**

Entrepreneurs in dynamic markets face the ongoing challenge of balancing exploration with commitment. Key decisions revolve around how much to experiment and when to **pivot** in response to new information, which is often complicated by cognitive biases such as overconfidence. Structured experimentation programs—those that carefully manage how many experiments to run and the timing of strategic shifts—are critical for entrepreneurial success.

Pivots are strategic shifts that startups make when they discover new information or insights, usually in response to market feedback, technological advancements, or internal challenges. A pivot involves changing the business model, product offering, target market, or approach, while retaining the startup’s core vision or goals. Successful pivots allow startups to avoid stagnation and seize emerging opportunities.

Recent studies (Gans et al., 2019; Stern, 2019) emphasize that while frequent experimentation can spur innovation, excessive pivoting can disrupt learning and harm long-term performance. The Lean Startup model popularized by Eric Ries stresses iterative learning while cautioning against over-pivoting. In light of this, a well-structured experimentation framework mitigates such risks, enabling better-informed decisions.

Central to this framework is the concept of **exaptation**, borrowed from evolutionary biology. Exaptation describes how existing features, originally developed for one function, are repurposed for new, often unanticipated uses (Gould & Vrba, 1982). In the context of entrepreneurial innovation, two types of exaptation emerge: one where a feature previously shaped by selection is co-opted for a new use (adaptation), and another where features not initially shaped by selection are co-opted (nonaptation). These represent **sequential pivots** and **parallel pivots**, respectively. Both are crucial for understanding how startups navigate uncertainty and explore innovation.

---

### **Parallel and Sequential Search in Experimentation**

Startups typically adopt either **parallel** or **sequential search** strategies in experimentation, each suited to different industry contexts and conducive to distinct exaptive opportunities.

---

#### **Parallel Search: Rapid Innovation through Broad Exploration**

In parallel search, startups run multiple experiments simultaneously, a strategy well-suited for industries characterized by fast-paced development and low testing costs, such as biotechnology, software, and semiconductors. This approach facilitates broad exploration, increasing the likelihood of discovering novel applications for technologies that may not have been originally designed for a particular purpose.

For instance, **Moderna** applied parallel search effectively during its early development of mRNA vaccines. By pursuing several mRNA programs concurrently, Moderna rapidly identified new applications for its platform. This process exemplifies **nonaptation exaptation**, where resources not previously optimized for a specific function are repurposed to meet emerging market needs. Such strategies expand the "adjacent possible" (Kauffman, 1995), enabling startups to discover opportunities quickly and increase entrepreneurial agility.

In high-uncertainty environments, especially for early-stage biotech startups, rapid experimentation facilitates the discovery of exaptive opportunities. This is particularly relevant in sectors where technological breakthroughs and market needs evolve rapidly, making parallel search essential for long-term survival and success.

---

#### **Sequential Search: Methodical Learning through Stepwise Exploration**

Conversely, sequential search follows a linear, methodical approach, where each experiment informs the next step. This approach works best in industries where failure is costly or where each test requires significant investment, such as aerospace and automotive engineering. Startups adopting sequential search can more deeply analyze results from each experiment, gaining greater understanding of their assets before moving forward.

**Tesla** provides a notable example of sequential search. In its early stages, the company focused heavily on refining its battery technology. Each iteration in its electric powertrain design built upon the previous results, eventually expanding into related areas such as home energy storage (Powerwall). Tesla’s deliberate expansion demonstrates **adaptation exaptation**, where technology optimized for one use (electric vehicles) is adapted to serve broader applications like home energy systems. Sequential pivots allow startups to mitigate risk, ensuring that each strategic shift is based on solid evidence.

While sequential search fosters slower innovation, it enables more informed decisions by allowing startups to carefully evaluate the results of each experiment, reducing uncertainty and facilitating more deliberate pivots.

---

### **The “Test Two, Choose One” Rule and Pivot Thresholds**

The "Test Two, Choose One" rule (Gans et al., 2019) offers a practical framework for balancing exploration with decision-making in uncertain environments. This rule encourages entrepreneurs to test two equally viable alternatives simultaneously and select the more promising path based on data. Such structured experimentation reduces the risk of premature commitment to a single strategy and encourages adaptability to emerging opportunities.

In **parallel search**, this rule supports faster pivoting, as new applications of technologies or resources can emerge from simultaneous experiments. For example, **Uber** initially tested both black-car services and peer-to-peer ride-sharing models in parallel. After evaluating customer demand and operational feasibility, the company chose the more scalable peer-to-peer model, which ultimately transformed Uber into a dominant player in the transportation industry.

In **sequential search**, the "Test Two, Choose One" rule encourages more deliberate decision-making. By limiting the number of simultaneous experiments, startups can focus their efforts on one solidified experiment before moving on to the next. Setting clear **pivot thresholds**—specific points in an experimental program where decisions must be made based on results—helps entrepreneurs avoid the dangers of over-pivoting and ensure that each pivot is grounded in data rather than intuition.

---

### **Behavioral Biases and Entrepreneurial Decision-Making**

Entrepreneurs are often vulnerable to cognitive biases such as **overconfidence** and the **sunk cost fallacy**, which can lead to either excessive experimentation or reluctance to pivot. A structured experimentation program, supported by clear pivot thresholds, can mitigate these biases by enforcing data-driven decision-making processes.

Structured experimentation forces entrepreneurs to rely on empirical evidence rather than gut feeling, helping to avoid emotional attachment to failing strategies. For example, startups in sectors like healthcare or fintech often face these dilemmas, where early indicators may suggest promising avenues that turn out to be dead ends. Establishing clear pivot thresholds helps mitigate the risk of overcommitting to a strategy or technology that is unlikely to succeed.

By incorporating explicit pivot thresholds into both **parallel** and **sequential search** strategies, entrepreneurs can optimize their decision-making process, reducing the likelihood of failure due to cognitive traps and increasing the probability of long-term success.

---

### **Exaptation and the Adjacent Possible**

Exaptation plays a critical role in expanding the **adjacent possible**—the set of all future innovations that become accessible based on current conditions (Kauffman, 1995). By repurposing existing resources or technologies, startups can unlock previously unforeseen opportunities and strategically pivot into new markets.

In **parallel search**, startups running multiple experiments simultaneously are more likely to encounter exaptive opportunities, especially for resources or technologies that were not originally designed for their current use. For instance, **CRISPR Therapeutics** began as a tool for bacterial immune systems but was rapidly exapted for use in human gene-editing therapies, enabling the startup to address a variety of diseases from cancer to genetic disorders. This broad exploration uncovers hidden possibilities and allows startups to pivot in response to new market data.

In **sequential search**, exaptive opportunities emerge more gradually, often following a deeper understanding of the technology being repurposed. **Waymo**, Google’s autonomous vehicle project, initially focused on self-driving technology for ride-hailing services. Over time, as the technology evolved, Waymo incrementally expanded into autonomous delivery, reflecting how sequential pivots uncover new applications over time, grounded in methodical learning.

---


---

### **Conclusion: Leveraging Exaptive Strategies for Startup Success**

The ability to pivot effectively is crucial for startups navigating uncertain markets. Both **parallel** and **sequential search** strategies, informed by exaptation, offer valuable frameworks for experimentation and innovation. Parallel search enables rapid discovery of new opportunities, while sequential search fosters deeper, more deliberate learning, reducing the risk associated with each pivot.

By incorporating structured experimentation programs, clear pivot thresholds, and an understanding of the dynamics of exaptation, startups can enhance their ability to innovate and expand their **adjacent possible**. Startups that master these methods are better equipped to discover novel applications for their existing technologies and achieve sustained innovation in dynamic markets.

---

### **References**

1. Gould, S. J., & Vrba, E. S. (1982). Adaptation and Exaptation: A Critique of Some Current Evolutionary Thought. _Proceedings of the Royal Society_.
    
2. Fine, C. H. (1998). Clockspeed: Winning Industry Control in the Age of Temporary Advantage. Harvard Business School Press.
    
3. Kauffman, S. (1995). At Home in the Universe: The Search for the Laws of Self-Organization and Complexity. Oxford University Press.
    
4. Kahneman, D., & Tversky, A. (1979). Prospect Theory: An Analysis of Decision Under Risk. _Econometrica_, 47(2), 263-291.
    
5. Chen, J., Wu, S., & Lee, Y. (2020). Simulation and Visualization for Entrepreneurial Pivots. _Journal of Business Research_.
    
6. Blattmeier, M. (2023). The Aestheticization of Business Processes: Visualizing Their Gestalt for Collective Thinking. _Journal of Information Technology_. [https://journals.sagepub.com/doi/epub/10.1177/02683962231166438](https://journals.sagepub.com/doi/epub/10.1177/02683962231166438)
    
7. Gans, J., Stern, S., & Wu, J. (2019). Foundations of entrepreneurial strategy. Strategic Management Journal, 40(5), 736-756. [DOI: 10.1002/smj.3010](https://doi.org/10.1002/smj.3010) ￼ ￼

---
todo: 

| Concept            | Test Two Choose One (T2C1)                       | Marr's Three Levels                                                                      | Information Relaxation                                                                 |
| ------------------ | ------------------------------------------------ | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Purpose            | Guide entrepreneurial decision-making            | Analyze cognitive and information processing systems                                     | Optimize decision-making under uncertainty                                             |
| Structure          | 1. Test two strategies<br>2. Choose one          | 1. Computational theory<br>2. Representation and algorithm<br>3. Hardware implementation | 1. Relax information constraints<br>2. Introduce penalties<br>3. Solve relaxed problem |
| Key Benefit        | Reduces uncertainty through comparison           | Provides comprehensive view of system functioning                                        | Yields performance bounds and simplifies complex problems                              |
| Decision Mechanism | Comparative analysis and choice                  | Hierarchical analysis from abstract to concrete                                          | Mathematical optimization with relaxed constraints                                     |
| Information Use    | Creates information through internal consistency | Describes how information is processed at each level                                     | Allows access to future information (hypothetically)                                   |
| Application        | Entrepreneurship and strategy                    | Cognitive science and AI                                                                 | Operations research and finance                                                        |
