### 1. model abstract
Prior research on experimentation strategies has focused on maximizing reward per decision, overlooking the critical dimension of time. Additionally, the bandit literature assumes <span style="color:green">perceiving</span> and <span style="color:red">planning</span> occur simultaneously, contrary to computational rationality theory which suggests organizations face cognitive constraints forcing a <span style="color:green">perceiving</span>-or-<span style="color:red">planning</span> tradeoff. By analyzing reward flow, defined as reward per <span style="color:red">planning</span> event divided by the event's time cost, we treat <span style="color:green">perceiving</span> (updating belief) from perceiving, sampling, experimenting AND <span style="color:red">planning</span> (acting, implementing, deciding) as separate events.

**V1 (prescribing operational pivot):**  
This research suggests how an organization with a certain <span style="color:red">planning</span> to <span style="color:green">perceiving</span> ratio (e.g., 2:1 for perceiving-perceiving-<span style="color:red">planning</span> <span style="color:green">SSA</span>) adapts to an evolving world state by adjusting its decision cycle (e.g., from SSA to SASA or SSSA). We first show how optimal <span style="color:green">perceiving</span> per <span style="color:red">planning</span> is proportional to the ratio of <span style="color:red">planning</span> to <span style="color:green">perceiving</span> time costs. This rationalizes an organization's operational pivots on how many <span style="color:green">perceiving</span> "events" happen before a <span style="color:red">planning</span> event and argues the ratio of <span style="color:red">planning</span> to <span style="color:green">perceiving</span> time costs fundamentally determines this behavior. When <span style="color:red">planning</span> time costs are reduced—such as: 1. By moving <span style="color:green">perceiving</span> facilities closer to operational hubs, or 2. Standardizing <span style="color:green">perceiving</span> processes—organizations are recommended to <span style="color:green">perceive</span> more to maximize reward flow. Conversely, when <span style="color:red">planning</span> time costs are increased—such as: 1. When <span style="color:red">planning</span> innovations require major production changes or external supplier adjustments, or 2. The organization’s decision structure becomes rigid— dedicating more to <span style="color:red">planning</span> events is beneficial to avoid costly mistakes.  

**V2 (explaining behaviors on heterogeneous event ratio resolving contradictory findings):**  
When <span style="color:red">planning</span> time costs are high relative to <span style="color:green">perceiving</span> time costs—such as when <span style="color:red">planning</span> innovations require lengthy production changes—organizations benefit from dedicating more periods to <span style="color:green">perceiving</span> upfront, increasing the number of <span style="color:green">perceiving</span> events per <span style="color:red">planning</span> event to avoid costly errors.  Conversely, when <span style="color:red">planning</span> is a relatively quick and inexpensive event compared to <span style="color:green">perceiving</span>, alternating between <span style="color:green">perceiving</span> and <span style="color:red">planning</span> maximizes reward flow. This temporal perspective reconciles seemingly contradictory findings: In environments with low <span style="color:red">planning</span> time costs, frequent alternation between <span style="color:green">perceiving</span> and <span style="color:red">planning</span> is optimal.  In environments with high <span style="color:red">planning</span> time costs, extensive upfront <span style="color:green">perceiving</span> is preferred.  By explicitly modeling <span style="color:green">perceiving</span> and <span style="color:red">planning</span> as distinct components and introducing their time costs, this framework provides a computationally realistic approach to reward-driven <span style="color:green">perceiving</span> and <span style="color:red">planning</span>, addressing the limitations of bandit models that oversimplify the temporal dynamics of organizational decision-making.

![[Pasted image 20241123164853.png|200]]

The 🧠perceiving time-cost represents the time resource required for experimentation and testing. When Tesla's engineers evaluate battery specifications, interview potential suppliers, conduct engineering assessments, or test prototypes, they are incurring 📍planning costs. The efficiency of these  🧠perceiving activities determines how quickly Tesla can gather meaningful information before making implementation decisions. 

The 📍planning time-cost captures the time resource needed for implementation and execution. When Tesla commits to a specific battery design, they must invest substantial time in building supply chain relationships, 📍planning engineering characteristics, adjusting form factors, integrating cooling systems, and setting up production lines. 

These execution activities represent long-term commitments that are often difficult to reverse. Reward represents the degree of success in achieving goals. We use 1 to 5 scoring system with 5 being higher reward than 1. Scores like 445 represent satisfaction ratings from multiple customers/trials - e.g., 4,4,5 means three customers gave ratings of 4,4,5 out of 5. For Tesla's battery situation, reward measures both technical performance (meeting specifications) and market performance (customer willingness to pay). When batteries meet design specs and customers validate this through purchases at target price points, the reward is high.

The ratio of 📍planning time-cost to  🧠perceiving time-cost (r) serves as a critical decision metric for Tesla's battery development strategy. When this ratio is high, indicating that implementation requires substantially more time resources than perceiving, Tesla benefits from conducting more thorough evaluations before commitment. Conversely, when the ratio is low, suggesting that implementation can be accomplished relatively quickly compared to perceiving, a faster implementation approach with fewer 🧠perceiving iterations maximizes reward flow. The model optimizes decision-making by balancing reward per unit time instead of just reward per decision. For each decision, $\color{orange}{k}$ exchangeable 📍plannings events happens before decision is made (action) to 📍planning reward. The quality of our decision improves with more 📍plannings but faces diminishing returns, captured by the decision quality function $Q(\color{orange}{k}, \color{skyblue}{p}\color{white}{)} = \color{skyblue}{p} \color{white}{\cdot (1 - B(}\color{orange}{\frac{k}{2}}, \color{orange}{k}, \color{skyblue}{p} \color{white}{))} + (1-\color{skyblue}{p}\color{white}{)} \color{white}{\cdot B(}\color{orange}{\frac{k}{2}}, \color{orange}{k}, \color{skyblue}{p} \color{white}{)}$, where $\color{skyblue}{p}$ represents the true probability of success and $B$ is the binomial CDF. The total time cost $T$ combines both  🧠perceiving time and 📍planning time: $T(\color{orange}{k}, \color{green}{r}\color{white}{)} = \color{green}{r} \color{white}{+} \color{orange}{k}$, where $\color{green}{r}$ represents the ratio of 📍planning time-cost to 🧠perceiving time-cost. Unit of T is event (not time), meaning r is (📍planning time cost/ 🧠perceiving time cost) x (one 📍planning event) and k is (k  🧠perceiving events). The optimal strategy maximizes the reward rate $R(\color{orange}{k}, \color{green}{r}\color{white}{)} = \frac{Q(\color{orange}{k}, \color{skyblue}{p}\color{white}{)}}{T(\color{orange}{k}, \color{green}{r}\color{white}{)}}$. The decision-making process balances reward per 📍planning decision event against time costs of event. Like the sampling model in [[📜tenanbaum14_1sample(1decide)]], each 📍planning event provides information but faces diminishing returns. The quality function $Q(\color{orange}{k}, \color{skyblue}{p}\color{white}{)}$ resembles the Bayesian posterior estimation process, where more samples ( 🧠perceiving events) improve decision quality but with decreasing marginal benefit. The time cost $T(\color{orange}{k}, \color{green}{r}\color{white}{)}$ reflects both 🧠perceiving and 📍planning event sequences, similar to how sampling and action costs are balanced in [[📜tenanbaum14_1sample(1decide)]]'s decision-making framework. 

Difference between decision quality $Q(\color{orange}{k}, \color{skyblue}{p}\color{white}{)}$ and reward rate $R(\color{orange}{k}, \color{green}{r}\color{white}{)}$ is,  🧠perceiving-📍planning- 🧠perceiving-📍planning can have higher reward rate compared to that of  🧠perceiving- 🧠perceiving- 🧠perceiving-📍planning, even though its decision quality is lower. Assuming 🧠perceiving and 📍planning takes equal amount of time, 🧠📍🧠📍's reward per 📍planning event is lower (2 vs 3), but as two 📍planning event can happen in the same duration of time, 🧠📍🧠📍 claims victory in reward flow realm.

| Variable                                                  | Definition (unit)                                          | Tesla Example                                                                                                                                       |
| --------------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| $\color{orange}{k}$                                       | 🧠perceiving per 📍planning                                | Number of battery designs/specifications tested before committing to production                                                                     |
| $\color{skyblue}{p}$                                      | True success probability                                   | Underlying probability that a given battery design will meet performance requirements                                                               |
| $\color{green}{r}$                                        | 📍planning/🧠perceiving time cost ratio                    | Time needed to retool production line and establish supplier relationships divided by time needed to test one battery design (request for proposal) |
| $Q(\color{orange}{k}, \color{skyblue}{p}\color{white}{)}$ | Decision quality (reward / 📍planning event)               | How well the chosen battery design performs in actual production/market                                                                             |
| $T(\color{orange}{k}, \color{green}{r}\color{white}{)}$   | Total time cost (📍planning and 🧠perceiving event / time) | Total time from start of 🧠perceiving to full production implementation                                                                             |
| $R(\color{orange}{k}, \color{green}{r}\color{white}{)}$   | reward rate (reward / time)                                |                                                                                                                                                     |

# EOD

---

###  🚨todo
 - 🚨todo4: 
	 1. explain the table below in one paragraph.
	 2. make sure to specify "This rationalizes organization's operational pivots on how many 📍planning "event" happens before 📍planning event and we argue ratio of 📍planning to 📍planning time costs fundamentally determines this behavior. When 📍planning time costs are reduced—such as 1) by moving 🧠perceiving facilities closer to operational hubs or 2) standardizing 🧠perceiving processes—organizations are recommended to 🧠perceiving more to maximize reward flow. Conversely, when 📍planning time costs are increased —such as when 1) 📍planning innovations requires major production changes or external supplier adjustments or 2) organization decision structure becomes rigid— dedicating more on 📍planning event is beneficial to avoid costly mistakes." from ### 1. model abstract.
	 3. based on 1, fill in "**Outside Tesla:** 🚨" from 🔺 📍planning Time Cost ↑ row of table.
 - 🚨todo5: 
		1.  understand two tables in ## 4. extending to two dimensions section which compares exploiting vs exploring 📍planning choices in market and product domain. make sure you understand the mechanism behind tesla and rapidSoS.
		2. make sure you have one paragraph each for each table. make sure this table conveys how exploitive vs explorative 📍planning in product choice and market choice are exemplified.
		3. fill in your expectation of reward in four different situations. i denoted it as 🚨 (customer willingness to pay * total addressable market), given the score is from 1 to 5. be sure to remember exploitive has larger mean but smaller standard deviation compared to explorative.

## 3. tesla example

![[Pasted image 20241122160433.png|1000]]

![[🗄️🪶1d]]



- Phase1-2: **📍planning Time Costs Reduction:** The reduction in 🧠 📍planning time costs between Phase 1 (8 weeks) and Phase 2 (2 weeks) demonstrates the benefit of moving 🧠perceiving facilities closer to operational hubs (Fremont) and standardizing processes for rapid iterations. This aligns with the claim that organizations should increase 📍planning when 📍planning time costs are reduced to ensure efficient decision-making.

- Phase2-3: **📍planning Time Costs Increase:** The sharp rise in 📍 📍planning time costs from 10 weeks in Phase 2 to 72 weeks in Phase 3 (to implement the 4680 cells) reflects the increased complexity and retooling required for innovation. This supports the idea that dedicating more to 📍planning events is necessary when 📍planning time costs rise, as mistakes at this stage could be extremely costly.

Tesla's supply chain evolution demonstrates two distinct shifts in 📍planning-to-📍planning time ratios. For the Roadster, initial 📍planning cycles took 8 weeks due to distributed 🧠perceiving across three continents, while 📍planning (implementation) time was relatively quick at 4 weeks since changes only required coordinating with outsourced suppliers. Tesla pivoted to an integrated Fremont facility, cutting 📍planning time to 2 weeks while accepting longer 10-week implementation cycles - recognizing rapid 📍planning was crucial for developing a novel product. Later, when developing 4680 cells, Tesla faced much higher 📍planning costs of 18 months for production changes due to complex retooling requirements and supplier adjustments. Given these extended implementation timelines, Tesla adapted by conducting more thorough upfront 🧠perceiving and validation to minimize costly implementation mistakes. These examples show how Tesla optimized its development approach based on the ratio between 📍planning and 📍planning time costs - first by reducing 📍planning time through integration, then by increasing 📍planning iterations when faced with high 📍planning costs.


The Tesla Roadster was Tesla’s ﬁrst car sold to the public. The company designed an initial supply chain that spanned three continents and resulted in very long prototyping cycles. In that initial model, the design and engineering of the key electronics and battery modules were performed in California, along with the ﬁnal vehicle test and tuning. The manufacturing and supply chain team lacked professionals from the automotive industry, and with a focus on low labor costs outsourced the manufacture of key modules to multiple sites in Asia. Further, due to capability requirements, vehicle assembly was located in Europe. The footprint of this outsourcing model yielded very long design-manufacturetest cycles—from California to Asia to Europe and back to California. Such long debugging cycles, especially for a ﬁrst-of-its-kind product, were not sustainable, and the company went through a major re-capitalization and a radical organizational change to restructure and redesign its operations toward more a more insourced and geographically compact manufacturing footprint, which enabled it to then debug and deliver the Roadster vehicles. The initial concept of minimizing costs by outsourcing manufacturing to low-cost geographies was supplanted by the insight that supply chain speed can often save more money than low-cost labor. The extreme operations pivot that Tesla was forced to undergo under duress, is often not possible for a company that does not have backers with deep pockets. The lesson that Tesla drew from the Roadster experience was how short supply chains can increase development speed, which encouraged it to invest in a large, much more integrated facility (in Fremont California) for its next product generation, the Model S.

🚨todo4: 
1. explain the table below in one paragraph.
2. make sure to specify "This rationalizes organization's operational pivots on how many 📍planning "event" happens before 📍planning event and we argue ratio of 📍planning to 📍planning time costs fundamentally determines this behavior. When 📍planning time costs are reduced—such as 1) by moving 🧠perceiving facilities closer to operational hubs or 2) standardizing 🧠perceiving processes—organizations are recommended to 🧠perceiving more to maximize reward flow. Conversely, when 📍planning time costs are increased —such as when 1) 📍planning innovations requires major production changes or external supplier adjustments or 2) organization decision structure becomes rigid— dedicating more on 📍planning event is beneficial to avoid costly mistakes." from ### 1. model abstract.
3. based on 1, fill in "**Outside Tesla:** 🚨" from 🔺 📍planning Time Cost ↑ row of table.

| Cause | Factor & Tesla Battery Example                                                                                                                                                                                                                                             |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|       | **Inside Tesla:** Engineers got really good at battery 🧠perceiving through experience (professionalize)<br>**Outside Tesla:** Moving 🧠perceiving facilities closer to main office<br>**Example:**                                                                                  |
|       | **Inside Tesla:** New battery designs required completely changing how cars were built<br>**Outside Tesla:** 🚨<br>**Example:** When Tesla introduced their new 4680 battery, it took 18 months to set up production because both Tesla and suppliers needed major changes |

## 4. extending to two dimensions

🚨todo5: 
	1.  understand two tables in ## 4. extending to two dimensions section which compares exploiting vs exploring 📍planning choices in market and product domain. make sure you understand the mechanism behind tesla and rapidSoS.
	2. make sure you have one paragraph each for each table. make sure this table conveyes how exploitive vs explorative 📍planning in product choice and market choice are exemplified.
	3. fill in your expectation of reward in four different situations. i denoted it as 🚨 (customer willingness to pay * total addressable market), given the score is from 1 to 5. be sure to remember exploitive has larger mean but smaller standard deviation compared to explorative.



Suppose we're selling Japanese batteries to Texas, and Texas only wants Made in America, right? Yeah, yeah. Right Track is yeah, so. So we expect this is a really tough test. It. It's going to have to be extremely high performing to give satisfaction to these Texans for them to accept. I'm going to take these foreigner batteries in my car. Is that right? Do I have the right intuition? Yes, yes. So I'm so I'm I'm creating a very difficult test now. But why is it one? Okay, so it's three customers, yeah, three Texans gave us a one, one. She gave us a three one. Gave us a phone. Yeah. And so there are two dimensions here. One is the customer expectations. Are they Texans or are they Californians, right? Yeah. What's the other and the other dimension is the product? Is it a Japanese car, American, Made in America, made in Japan or something?

![[🗄️🪶2d]]
- Top Left = Easiest path (known Japanese tech + accepting market)
- Bottom Right = Most challenging path (new US tech + demanding market)
- Bottom Left  = Mixed (new US battery + accepting market)
- Top Right = Mixed (known Japanese battery + demanding market)

The reward (445, 222, 135, 345) represent customer satisfaction ratings from three different customers on a 1-5 scale, where higher numbers indicate greater satisfaction.

- Top Left =  Easiest path (Simple consumer app)
- Bottom Right = Most challenging path  (Full emergency response system, what they became)
- Bottom Left  = Mixed ( Basic medical/NGO tracking (what they tested; "If they don't like it, we should quit"))
- Top Right = Mixed (Basic medical/NGO tracking (what they tested))

RapidSOS chose to test with high bar market (medical/NGO) first using relatively low bar operations, then built up to high bar operations to serve the entire emergency response market.

---
## future work
- "The concept of exaptation (the repurposing of existing resources for new uses), offers two key strategies for structured experimentation."
- explain the difference with test 2 choose 1 which is sequential 📍planning i.e. second test builds on the first test. but we are multiverse situation where each 📍plannings are exchangeable. increased 📍planning increase precision of world representation of the world i.e. P(State|Data). One 📍planning decision is made based in majority voting way by choosing action that gained more than k/2 votes among k multi-verse.
- word choice between "reward" flow VS "utility" flow
- analyze variance?

| 🔻 📍planning Cost Variance (σ²ₛ↓)<br>*Making 📍planning time more predictable*       | **Inside Tesla:** Created standard 🧠perceiving procedures (processify)<br>**Outside Tesla:** Set up reliable 🧠perceiving labs<br>**Example:** At first, 🧠perceiving time varied between 1-4 weeks. After creating standard procedures, it consistently took about a week                                               |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🔺 📍planning Cost Variance (σ²ₐ↑)<br>*Making implementation time less predictable* | **Inside Tesla:** Some changes needed just software updates, others needed complete car redesign<br>**Outside Tesla:** Suppliers took unpredictable time to get ready<br>**Example:** Early Roadster battery implementation could take anywhere from 6-18 months depending on how complex the changes were |

----

| Company | Evolutionary Concept       | 🧠perceiving Strategy                                                                                                               | Market/Product Example                                                                            |
| ------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| Tesla   | Exaptation                 | Battery tech evolved from EV performance → home energy storage (Powerwall)                                                     | Sequential: First tested batteries for EVs, then expanded to home storage                         |
| Porsche | Spandrel                   | "Turbo" branding: byproduct of ICE heritage → EV performance signal                                                            | Parallel: Tested multiple brand positions simultaneously across markets                           |
| BYD     | Dual Exaptation & Spandrel | Blade Battery: Safety feature → marketing differentiator (exaptation) + modular design as unintended cost advantage (spandrel) | Sequential then Parallel: Started with safety perceiving, then explored multiple market applications |

| Topic | Discussion Insight | Mathematical Implication |
|-------|-------------------|------------------------|
| Parallel vs Sequential | High correlation between market/operations favors parallel perceiving, as choices in one domain constrain options in another | Model should incorporate correlation parameter between test domains |
| Exploration Cost | Low 🧠perceiving cost + high uncertainty favors parallel/spandrel approach with wide exploration | Optimal number of parallel tests (k) increases as ratio of implementation to 🧠perceiving cost (r) increases |
| 📍planning Structure | Sequential 📍planning builds on previous tests while parallel 📍planning treats samples as exchangeable | Quality function Q(k,p) uses majority voting for parallel tests vs conditional updating for sequential |

thinking = constructing programs that represent probability world models, performing inference in theses models to predict and plan, explain and evaluate, learn and teach, condited on goals, observations, and background knowledge.

understanding language (constructing meaning) = inferring (probability distributions over) expressions in internal programming languages of thought, conditioned on a communicative context.















