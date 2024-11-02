 0 ---- 
Goal of this paper:
  - deliver `educatable` knowledge to startup advisors (thinkers)
  - deliver `applicable` knowledge to startups (doers)
---- 
- [[#1. Introduction|1. Introduction]]
	- [[#1. Introduction#1.1  three root causes of P|1.1  three root causes of P]]
	- [[#1. Introduction#1.2 process of modularizing solution|1.2 process of modularizing solution]]
	- [[#1. Introduction#1.3 process of integrating modular solutions to solve problem P|1.3 process of integrating modular solutions to solve problem P]]
- [[#2. Cause of problem at different level|2. Cause of problem at different level]]
	- [[#2. Cause of problem at different level#PA Agent level problem|PA Agent level problem]]
	- [[#2. Cause of problem at different level#PI Institution level problem|PI Institution level problem]]
	- [[#2. Cause of problem at different level#PN Nature level problem|PN Nature level problem]]
- [[#3. Solution|3. Solution]]
	- [[#3. Solution#SA|SA]]
	- [[#3. Solution#SI|SI]]
	- [[#3. Solution#SN|SN]]
- [[#4. Productizing Solution|4. Productizing Solution]]
	- [[#4. Productizing Solution#PSA|PSA]]
	- [[#4. Productizing Solution#PSI|PSI]]
	- [[#4. Productizing Solution#PSN|PSN]]
- [[#5. Way forward|5. Way forward]]
- [[#6. Conclusion|6. Conclusion]]
- [[#References|References]]

#### 1. Introduction
Problem to intervene (P): Science of startup adaptation is not accumulative 
##### 1.1  three root causes of P
Agent level (PA): Cognitive limitation and necessity of simulation to frame as "choosing to adapt"
Institution level (PI): Non-cumulative learning from startup success and failure without shared taxonomy and dynamic decision model
Nature level (PN): Idiosyncratic signals from dynamic environments

how likely EV would be take 50% of the cars in the road in the 10yr.
##### 1.2 process of modularizing solution
$X_{1...1000}$: high dimension observable states (e.g. number of cofounders, objective, number of previous startup success, matched mentor) 
$A_{1..T} \in$ {scale, change-market, change-product, fail}
$B_{1..T} \in R$ belief of (market acceptance X production feasibility)
$H_{1..6}$: six latent hyper-parameters (market instability DR, market segment size SR, belief and real gap BR, diffuseness of belief DB, number of experiment opportunity ER, confidence ratio of market acceptance to production feasibility CT)

as-is: $[X_{1...1000}, B_1, B_T] \underset{f}{\rightarrow} [A_{1..T}]$
- input: startup feature $X_{1...1000}$, past belief ($B_1$), future goal ($B_T$), 
- infer function $f$ which maps  startup's action sequence with its past belief and future goal
- output: action sequence $A_{1..T}$

to-be:  $[X_{1...1000}] \underset{f_{1}}{\rightarrow} [H_{1..6}] \underset{f_{2}}{\rightarrow} [(A,B)_{1..T}$]
- input: startup feature $X_{1...1000}$,
- infer decomposed heterogenous ($f_1$) and homogenous ($f_2$) function by 1) adding hyper-parameters layer $H_{1..6}$, 2) lifting output space from action to action and belief 
	- $f_2$: more settled science (enough to be used for education purpose)
	- $f_1$: less settled science (too heterogeneous to generalize, but need inference for startup prediction )map with observed/descriptive characteristic of startup to $H_{1..6}$
- output: action and belief sequence $(A,B)_{1..T}$
##### 1.3 process of integrating modular solutions to solve problem P
Propose implementing simulation-based adaptive learning  (Solution) and map each section to problem and solution
- [[#2. Cause of problem at different level]] addresses the root causes of problems to intervene at the agent, institution, nature level.
- [[#3. Solution]] presents how sequential decision model addresses each of the root causes 2.1, 2, 3.
- [[#4. Productizing Solution]] demonstrates the mechanism of how solutions address the problem's root causes and solve the problem.
- [[#5. Way forward]] discusses use of productized solution 
- [[#6. Conclusion and further study]] summarizes the contribution and remaining problems

#### 2. Cause of problem at different level
##### PA Agent level problem
 impossible without tool
- cognitively limited in attention, decision, action space
- even for the person without any cognitive constraint, simulation tool is needed as change from the baseline should be computed for adaptation 
##### PI Institution level problem
 no incentive to develop programmatic theory (Cronin et al, 2019)
- conflicting literature on [[📜🗄️2_literature review on H1to6]] as evidence for P (problem to intervene): noncumulative science of startup adaptation
- pivoting has relative and absolute aspect; REL is direction of vector whereas ABS is size of the vector. if you're more confident on the market, you're less likely to pivot away from this market 
- [[table on pivot conflict with old hp names]]
- [[detail on simulation model]]

##### PN Nature level problem
Prediction is inherently hard
- idiosyncratic signals from dynamic environments, which can be decomposed to below based on [[📜life_origin]]'s framework
1. Irreducible error: Startups operate in highly dynamic and complex environments, with numerous factors influencing their outcomes. Even with perfect measurements and models, there will always be some inherent randomness and unpredictability in startup trajectories due to unforeseen events, market shifts, and complex interactions among variables. This irreducible error makes perfect prediction impossible.
2. Unmeasurable features: Many crucial aspects of startups, such as founder passion, team dynamics, and customer sentiment, are difficult or impossible to quantify precisely. These unmeasurable features can have significant impacts on startup success but are challenging to incorporate into predictive models, leading to increased uncertainty in predictions.
3. Imperfectly-measured features: Even for startup features that can be measured, such as financial metrics or user growth, the measurements may be noisy, incomplete, or collected at a coarse granularity. These imperfect measurements can obscure important nuances and lead to less accurate predictions.
4. Unmeasured features: Some key variables influencing startup success may be entirely unknown or unmeasured, such as undiscovered market opportunities, emerging competitor strategies, or unexpected regulatory changes. The absence of these variables in predictive models can lead to significant blind spots and prediction errors.
5. Non-zero irreducible error: The complex interplay of factors driving startup success means that even with extensive data and sophisticated models, there will always be some level of irreducible uncertainty in startup outcome prediction. Perfect prediction is likely impossible due to the inherent complexity and randomness of the startup ecosystem.
6. Intervening events: Unforeseen events can dramatically alter the trajectory of a startup, such as key personnel changes, technological breakthroughs, or global crises like the COVID-19 pandemic. These intervening events are difficult to anticipate and incorporate into predictive models, leading to unexpected outcomes and reduced predictive accuracy.
#### 3. Solution
##### SA 
Solution to [[#PA Agent level problem]] 
- Enhancing the decision-making process through integrative models
 - Dashboard 🖥️ that shows higher quality information to agents
- Interactive Simulation 🖱️ where agents can test their beliefs 
- Case studies of startups demonstrating the effectiveness of these solutions
##### SI 
Solution to [[#PI Institution level problem]]
 - Developing comprehensive platforms for iterative learning and adaptation
 - Case studies of startup educators illustrating the benefits of such platforms for startups and advisors
##### SN 
Solution to [[#PN Nature level problem]]
- being aware of inherent unpredictability
- may be improved with constraining prior. More in [[#PSN productizing SN Solution to PN Nature level problem]]
#### 4. Productizing Solution

##### PSA 
productizing [[#SA Solution to PA Agent level problem]]

To enhance the decision-making process for startups, they should be able to map their situated knowledge to the model's hyper-parameters. This helps them to update their belief on adaptation mechanism, which may further affect their action.

1. Customized mapping ($f_1$) from situated knowledge to hyper-parameters (S2H): This stage involves translating an entrepreneur's specific context, experiences, and knowledge into the six hyper-parameters identified in the model (market instability DR, market segment size SR, belief and real gap BR, diffuseness of belief DB, number of experiment opportunities ER, and confidence ratio of market acceptance to production feasibility CT).
2. Generic mapping  ($f_2$) from hyper-parameters to action and belief update  (H2AB): Once the hyper-parameters are determined, the model provides a standardized framework for updating beliefs and guiding decision-making based on the relationships between these parameters and the learning process (as in [[#1.2 process of modularizing solution]]).

##### PSI 
productizing [[#SI Solution to PI Institution level problem]]

To make this process more data-driven and actionable, we aim to address common myths and challenges faced by startups, from the book founders' dilemma and the unicorn's shadow. By incorporating empirical evidence and case studies, we can demonstrate the effectiveness of our integrative approach. For example, how the number of cofounders affect the time taken to change the market or product has infinite mechanism as below [[d(T2CM)-d(founders)]], but using the improved mapping which abstracts S2H as choice is free from  different combination of mechanisms.

| Parameter                            | More is less                                                                                                                                                                                                                               | More is More                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| DR (Market Stability)                | Duo may prefer a more stable market to reduce coordination costs and disagreements between founders. A stable market allows for more predictable decision making.                                                                          | Duo may be more willing to tackle dynamic markets because they can divide and conquer, with each founder focusing on different changing aspects. Duo has more total cognitive bandwidth to process a dynamic environment.<br><br>                                                                                                                                                                      |
| SR (Market Size)                     | Duo may prefer to target a smaller market initially to prove their business model with fewer resources. Starting small also reduces the risk of conflict between founders.                                                                 | Duo may target larger markets from the start because they have more combined resources, connections and credibility than a solo founder. Larger markets provide more opportunities for the founders to pursue different customer segments if needed.                                                                                                                                                   |
| BR (Optimism)                        | Duo may be less optimistic than a very confident solo founder because the duo has to constantly calibrate their expectations with each other, reducing individual over-optimism.                                                           | Duo may be more optimistic than a timid solo founder because the founders can reinforce each other's confidence.<br><br>Having a shared vision can increase the optimism beyond what either founder would have individually. It's unclear if duo would be consistently more or less optimistic than solo. It likely depends on the individual traits of the founders and their interpersonal dynamics. |
| OB (Market Acceptance info)          | Duo may have less information on market acceptance because each founder has limited bandwidth to gather external data while also coordinating internally. Some market information could get lost in the "telephone game" between founders. | Duo likely has more total information on market acceptance because they can tap into two separate networks and have two pairs of eyes and ears open to the market. They can cover more ground in customer discovery.                                                                                                                                                                                   |
| ER (Experiment Opportunity)          | Duo may have fewer experiment opportunities because some experiments could be vetoed by the other founder. With shared resources, each founder may be more conservative in deploying experiments.                                          | Duo can run more experiments in parallel by dividing and conquering. They also have a larger combined pool of resources and mental bandwidth to deploy a greater number and variety of experiments.                                                                                                                                                                                                    |
| CT (Market-Product Confidence Ratio) | Duo may have a lower ratio (relatively more confidence in product than market) because the founders reinforce each other's confidence in their own product. Overconfidence in one's own product is a common pitfall.                       | Duo may have a higher ratio (relatively more confidence in market than product) because they can do more market research and the Product Confidence gets divided across two founders' visions. Reaching agreement provides a check against Product overconfidence.                                                                                                                                     |

To facilitate the adoption and use of our model by entrepreneurs and startup advisors, we will integrate the mapping process described above into existing tools and platforms, such as the Martin Trust Center's Orbit platform. By providing a user-friendly interface and clear guidance on how to input situated knowledge and interpret the resulting hyper-parameters and learning outcomes, we can make the model more accessible and actionable for a wider audience. By offering training and educational resources, we aim to build a community of practice around data-driven entrepreneurship and foster a culture of continuous learning and adaptation. In specific, we will develop targeted training programs and educational resources to help entrepreneurs and advisors using the tool. These will address:
- Identifying and quantifying the six hyper-parameters based on a startup's specific context and knowledge
- Interpreting the relationships between hyper-parameters and the belief update process
- Using the interactive simulation tool like below  to test different scenarios and adaptation strategies
 ![[sim_tool.png|300]]

##### PSN 
productizing [[#SN Solution to PN Nature level problem]]
Constraining priors by incorporating domain-specific knowledge can enhance the predictive accuracy of the model. For example, in the biotech industry, startups often face longer development cycles and higher regulatory barriers compared to the IT sector. By incorporating these industry-specific factors into the model's priors, we can generate more accurate predictions and tailor the guidance provided to entrepreneurs.

To demonstrate the effectiveness of this approach, we will conduct case studies and hypothesis testing using the interactive simulation tool. These case studies will focus on improved decision-making in the biotech and semiconductor industries, showcasing how the model can adapt to different industry dynamics.

Furthermore, we will perform systematic parameter space inspections using the `plot_hypo_test` function to iteratively test the model over a range of identified parameter values. This process will help us understand the sensitivity of the model to different inputs and identify the most influential factors driving startup success.

Based on these tests, we will generate summary statistics on final pivot actions and decision rules. For instance, our preliminary results indicate that startups are more likely to change their target market rather than their product when:
- The market size (SR) is larger (0.30 > 0.27)
- The number of experiment opportunities (ER) is lower due to cash constraints (0.32 > 0.27)
- The confidence ratio of market acceptance to production feasibility (CT) is lower, indicating less commitment to a single market (0.36 > 0.24)

These findings provide valuable insights into the factors influencing startup decision-making and adaptation strategies. By refining the model's priors based on industry-specific knowledge and conducting rigorous testing, we can improve its predictive accuracy and offer more targeted guidance to entrepreneurs.

simulating [[collaborate(Amir_Sariri, Jeff_Dotson)]], on projects like "Activity Sequencing in Startups" and "Learning vs. Doing: The Effect of Business Uncertainty on Entrepreneurial Activities" can improve the model's performance by controlling for industry heterogeneity. Specifically, we propose a novel approach adapting the multi-state Markov model from [Moon et al. (2022)](https://arxiv.org/pdf/2111.14368.pdf) to model startup activity sequencing using longitudinal data from the Creative Destruction Labs (CDL) program, which can uncover common activity patterns and their relationship to startup success.

#### 5. Way forward
The way forward for this research involves exploring how prior knowledge can be incorporated into the model to increase the homogeneity of the startup adaptation process. For example, by considering industry-specific factors such as the distinction between deep tech and non-deep tech startups, we may be able to improve the model's predictive accuracy and provide more tailored guidance to entrepreneurs.

In line with the future research plan outlined in the attached document, the next steps could include:
- Connecting observations, such as the number of co-founders and industry characteristics, with the six hyper-parameters identified in the model
- Examining how founder team composition affects these parameters and, consequently, the belief update mechanisms and decision-making processes
- Developing and implementing a comprehensive platform that includes a real-time dashboard, targeted training programs, and interactive simulations to support startups in their decision-making processes
- Incorporating additional factors, such as founder characteristics and industry dynamics, to improve the model's explanatory power and predictive accuracy
- Validating the model's assumptions and outcomes through empirical studies and case analyses
- Expanding the scope of the model to encompass the entire startup life cycle, from ideation to scaling and beyond

This platform could be integrated with existing resources, such as the MIT Martin Trust Center's Orbit platform, to provide a seamless experience for entrepreneurs seeking guidance and support. By leveraging the insights gained from this research and collaborating with experts in Bayesian Entrepreneurship (BE) and Probabilistic Computing (PC), we can create a powerful tool that empowers startups to make data-driven decisions and adapt effectively to the challenges they face.

#### 6. Conclusion 
In conclusion, this paper presents an integrative simulation model that combines Bayesian Entrepreneurship (BE) and Probabilistic Computing (PC) to guide startup decision-making and adaptation. By addressing the root causes of problems at the agent, institution, and nature levels, the model offers a novel approach to understanding and supporting entrepreneurial success.

The key contributions of this work include:
- Identifying the challenges faced by startups in adapting to dynamic environments and the limitations of existing approaches
- Developing a sequential decision model that incorporates hyper-parameters to capture the heterogeneity and homogeneity of the startup adaptation process
- Demonstrating the potential of the model to provide valuable insights and guidance to entrepreneurs and startup advisors through interactive simulations and case studies

The implications of this research extend to both entrepreneurship education and practice. By providing startup advisors (thinkers) with an "educate" knowledge type and supporting startups (doers) with an "apply" knowledge type, the model bridges the gap between theory and application, fostering a more evidence-based approach to entrepreneurship. By collaborating with experts in BE and PC, as well as industry partners and entrepreneurship support organizations, we aim to create a powerful ecosystem that fosters innovation, learning, and success in the startup world. Through continued research, development, and engagement with the entrepreneurial community, we hope to contribute to a more vibrant, resilient, and impactful startup landscape.

#### References
Chen, J. S., Elfenbein, D. W., Posen, H. E., & Wang, M. Z. (2024). Programs of experimentation and pivoting for (overconfident) entrepreneurs. Academy of Management Review, 49(1), 80-106.