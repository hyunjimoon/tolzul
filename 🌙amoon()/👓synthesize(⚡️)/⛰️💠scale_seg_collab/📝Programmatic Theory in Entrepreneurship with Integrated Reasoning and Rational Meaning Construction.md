🧱Bricks: [[Cronin24_the_enterprise.pdf]], [Moon et al (2024)'s integrating bayesian inference and system dynamics](https://docs.google.com/presentation/d/19aQe6h7lz70h5427cArytNUJXqx0ndNKziyIVmUKtZs/edit#slide=id.g2ff515a62c6_0_115)

---

## Abstract
This paper addresses the low adoption of Bayesian reasoning in entrepreneurial decision-making despite its proven optimality.

### 1. Introduction
Entrepreneurial decision-making faces high uncertainty in both demand and supply, increasing the value of strategic thinking. This paper advocates for Bayesian reasoning in entrepreneurial strategy, addressing root causes of its low adoption (sec.2) and proposing solutions through integration of inference and decision processes (sec.3.1), and different types of reasoning (sec.3.2).

### 2. Obstacles to Bayesian Reasoning Adoption in Entrepreneurial Decision Making
Despite its proven optimality (Bissiri et. al., 2016), Bayesian reasoning is rarely used in practice due to:

1. Lack of clear value chain mapping for individual modelers
2. Fragmented ecosystem of Bayesian tools and frameworks
3. Misconceptions about Bayesian methods among potential users

Three causes are all under the umbrella of process management. Section2.1 suggests lack of framework on model building process management for individual model builders. Section2.2 discusses value chain road mapping of Bayesian ecosystem, mostly based on [[📜past, present, future of bayes software]], which encouraged continued development of algorithms and software in multiple research fields, such as probabilistic programming, likelihood-free inference, and Bayesian neural networks, to expand Bayesian paradigm applications. I predict this expansion will be limited without quality control of new algorithms and software. As a stepping stone to section3 which suggests solution to each in segmented market, Section2.3 introduces misunderstanding of Bayesian reasoning in entrepreneurship field.

[[ber_3cause.png]]
Fig.1 the most left figure shows evolving bayesian reasoning that is affected by evolving observation in different applications/markets and technologies (sec.2.1). The middle figure shows flood of bayesian inference tools and workflows that makes users confused (sec.2.2). The most right figure describes upsides and downsides of bayesian thinking perceived by consumers in entrepreneurship scholars (sec.2.3).

#### 2.1 (Supply) Lack of Value Chain Road Mapping for Individuals
Clear value chain road mapping for individual Bayesian modelers is absent. Gelman et al. (2020) proposes a Bayesian Workflow which is a principled and systematic way of model building, but it has limitations in terms of complexity which Stan team is working on to make it more interactive. (todo1??connect 3d concurrent engineering, design thinking etc with workflow??)

I think the greatest challenge may be a slow iteration between policy use case feedback (stakeholders: model builders, policy designers, stakeholders) and software use case feedback (algorithm builders, tool builders, model builders). One example is, a large gap between inference-based (parameter estimation, calibration) research and policy research based on inferred parameter in epidemiology field. Even if inference and decision are naturally connected actions in real life, gap of clockspeed (Fine, 2000) between inference (optimization, inverse problem) and simulation (projection, evaluation, forward problem) disconnects the value chain of Bayesian prodcuts. This is illustrated in fig.2 where the upstream (red) and downstream (blue) are disconnected. To worsen this compartmentalization, tools that require significant effort to be compatible to each other are flooding. One example of this significant effort is, it took six months for a Stan develop with diverse Vensim modeling experience to make Vensim (main language/software of System dynamics community) compatible with Stan (main language/software of Bayesian computation) (Moon and Kim, 2023). 

![[ber_2integ.png|400]]
Fig.2 [
#### 2.2 (Supply) Lack of Value Chain Road Mapping for Ecosystem (Flooding Software and Frameworks)
The proliferation of Bayesian tools and frameworks has led to a fragmented ecosystem, reminiscent of the "toothbrush problem" in psychology (Mischel, 2008; Rocca and Yarkoni, 2021). This fragmentation impedes cumulative development and adoption. 
#### 2.3 (Demand) Potential Customers' Misconception
Subjectivity of priors and the inability to update zero-probability events are main criticism of Bayesian (todo2??reference??). However, some areas where Bayesian thinking has intruded are marketing and entrepreneurship. This is where there's not enough data so that elicitation of prior matter greatly for   create barriers to adoption. However,  an emerging field, Bayesian Entrepreneurship which synthesizes different domains (todo3??from economy, industry, in??)
### 3. Enabling Bayesian Reasoning in Business with Two Integrations
####  3.1 Integrating Inference and Decision
To address the fragmentation in Bayesian tools and frameworks, we propose integrating inference structures with decision-making frameworks. This integration can provide a unified platform for entrepreneurial decision-making. By combining Bayesian inference methods (e.g., Hamiltonian Monte Carlo using Stan) with decision heuristics (e.g., low and high bar heuristics) on top of entrepreneurial strategy axioms. This inference based decision brings interpretability hence consistency, which is the core of strategic thinking.

##### 3.1.1 Unifying Inference with Decision For Entrepreneurial Strategy
simulation model is designed so that each axiom from Gans16 can be pointed to its specific component. entrepreneurial strategy's axiom1 freedom: different pivoting paths, axiom2 constraint: cannot diverge has to choose either to pivot product or market, axiom3 uncertainty is represented as mu_p and mu_m which are parameter to be inferred. axiom4 noisy learning is finding out more about one route leads to reassessment of other alternatives (update expectation of all four quadrants). 

inference structure
![[ber_diamond.png]]

decision structure
![[ber_decision.png]]

experiment process
 ![[ber_inference.png]]


##### 3.1.2 Case Study: Entrepreneurial Decision-Making Tool
![[ber_2experiment.png]]
We present a case study of an simulation tool that integrates Bayesian inference with decision-making processes, demonstrating how this integration can enhance marketing and sourcing decisions. This integration will be reintroduced, but expressed in a more general language, in sec.3.2.1 as probabilistic reasoning. This re expression contributes to integration of different reasoning types (between probabilistic, relational, social).

On the left of the figure is marketing experiment illustrating EV startup's experiment and learning with chosen product and market segment’s feedback. EV Startup choosing between developing an electric vehicle with a 300-mile range versus a 350-mile range, and targeting either urban or rural markets. The performance measure is Market Adoption and Revenue Potential, illustrating how entrepreneurs must balance product capabilities with market needs.

On the right of the figure is sourcing experiment. Based on the case study of Tesla (Fine, et. al., 2014), it shows experiments in supply chain sourcing strategy. Two main decisions are between in-house vs. outsourced production and between local vs. global manufacturing. The performance measure is the probability of scaling before running out of funds, highlighting the critical balance between speed, cost, and quality in product development.

#### 3.2 Integrating Three Types of Bayesian Reasoning
Wong et al. (2023) proposes integrating probabilistic, relational, and social reasoning to create a more comprehensive framework for decision-making. This integration can address the complexity of entrepreneurial decision-making. Table below explains how the process of bayesian reasoning in entrepreneurship "starting from the prior, updating prior with experiments, persuading stakeholders, training knowhow of bayesian reasoning".

| reasoning type                       | goal                                                                                                                                                                                         | 🧠belief                                                                                                                                                                         | 🧪learn experiment                                                                                                                                                                                                                                                                                    | 🗣️persuade                                                                                                                                                                                                                                              | 🏋🏼train                                                                                                                                                                                                                                                                         |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| probabilistic<br>![[ber_p.png\|100]] | Marketing<br><br>Find product-market fit <br><br>e.g. EV range [300 vs 350 miles] x market [urban vs rural])                                                                                 | Believed there was growing demand for long-range electric vehicles, particularly among urban early adopters. Assumed high-performance EVs could compete with luxury sports cars. | Developed Roadster prototypes with different ranges. Later expanded to multiple models (S, 3, X, Y) targeting various market segments. Conducted extensive market testing and collected data on customer preferences and adoption rates.                                                              | Created data-driven presentations for investors, showing the potential of high-performance EVs. Used sales data (e.g., Model Y becoming 4th best-selling passenger vehicle globally) to demonstrate market acceptance.                                   | Trained team to use data-driven models for assessing risks and potential returns of different vehicle options. Developed capability to rapidly adjust pricing strategies based on market response.                                                                                |
| relational<br>![[ber_r.png\|100]]    | Supply Chain<br><br>Find end-to-end supply chain strategy <br><br>e.g., source in [outsource vs. inhouse] x supply at [global vs. local supplier] x distribute in [online vs. brick-mortar]) | Initially believed outsourcing manufacturing to Asia, following Silicon Valley's typical approach, would be key to achieving ambitious cost and speed targets.                   | Established partnerships with Lotus (UK) for vehicle assembly, Xcellent (Thailand) for battery assembly, and Chroma (Taiwan) for PEM manufacturing. Experimented with long-distance, complex supply chain. Later, moved towards vertical integration, building Gigafactories for in-house production. | Used data from initial outsourcing experiments to demonstrate the need for more control over the supply chain. Later, used successful vertical integration results to justify increased capital expenditures (e.g., $9B forecast for 2023) to investors. | Developed internal capabilities in manufacturing and supply chain management. Trained teams to balance the trade-offs between outsourcing and vertical integration, considering factors like quality control, speed to market, and cost-effectiveness.                            |
| social<br>![[ber_s.png\|100]]<br>    | Social Impact<br><br>Develop a business model with positive social impact (value proposition)<br><br>e.g. promote sustainable transportation                                                 | Assumed that innovative electric vehicles would have a positive social impact by reducing carbon emissions and promoting sustainable transportation.                             | Conducted surveys and focus groups to understand customer perceptions of EVs' social impact. Experimented with different vehicle models and price points to increase EV adoption. Tested impact of Supercharger network on EV adoption.                                                               | Crafted a compelling vision of sustainable transportation to inspire team and stakeholders. Used data on EV adoption rates and environmental impact to demonstrate Tesla's contribution to reducing urban air pollution and combating climate change.    | Developed training programs focused on social reasoning, helping the team understand the broader implications of decisions on various stakeholders. Trained employees to anticipate and address social and environmental concerns in product development and business strategies. |
Table1. probabilistic, relational, social reasoning type applied to bayesian entrepreneurship's process of prior to learn-experiment to persuade to train.
##### 3.2.1 Probabilistic Reasoning in Marketing Strategy

**Goal**: Our objective was to develop a probabilistic model to optimize Tesla's product-market fit strategy. This model aims to determine the ideal configurations for Tesla's vehicle lineup (Roadster, Model S, Model 3, and Model Y) across different market segments (urban and rural), considering factors such as range and price.

**Belief**: The model incorporates Tesla's initial beliefs about the electric vehicle market. We assumed a growing demand for long-range electric vehicles, particularly among urban early adopters. The prior also reflected the assumption that high-performance EVs could compete effectively with luxury sports cars. These beliefs were encoded into the model through probability distributions for vehicle ranges and prices, as well as market-specific demand functions.

**Learn Experiment**: To simulate Tesla's market testing and data collection process, we designed an experiment function within our model. This function takes a vehicle configuration (defined by model, range, and price) and a market type (urban or rural) as inputs. It then calculates the expected demand, adoption rate, and revenue for that specific combination. By running this experiment across various vehicle configurations and market types, the model mimics Tesla's real-world process of developing multiple prototypes and expanding its product line to target different market segments.

**Persuade**: The model generates data-driven insights that could be used to create compelling presentations for investors. It calculates the total expected revenue across all vehicle models and market types, demonstrating the potential of Tesla's high-performance EV strategy. The output includes optimal configurations for each vehicle model, showing how different range and price points can be tailored to maximize market acceptance and revenue. This aligns with Tesla's real-world use of sales data, such as the Model Y becoming the 4th best-selling passenger vehicle globally, to demonstrate market acceptance.

**Train**: Our probabilistic model serves as a framework for training Tesla's team in data-driven decision making. By allowing rapid iteration and adjustment of model parameters, it simulates the company's capability to adapt pricing and product strategies based on market response. The model can be continually updated with new data, enabling the team to refine their understanding of market dynamics and improve their ability to assess risks and potential returns for different vehicle options. This approach fosters a culture of data-driven decision making and strategic flexibility within the organization.

##### 3.2.2 Relational Reasoning in Supply Chain Strategy

**Goal**: Our objective was to model Tesla's approach to developing an end-to-end supply chain strategy. This model aims to optimize decisions across three key dimensions: sourcing (outsource vs. in-house), supply (global vs. local suppliers), and distribution (online vs. brick-and-mortar).

**Belief**: Initially, Tesla believed that outsourcing manufacturing to Asia, following the typical Silicon Valley approach, would be key to achieving their ambitious cost and speed targets. This belief was encoded into our model as a prior favoring outsourcing and global suppliers, reflecting Tesla's early strategy.

**Learn Experiment**: To simulate Tesla's learning process, we designed experiments that modeled their partnerships with various suppliers: Lotus in the UK for vehicle assembly, Xcellent in Thailand for battery assembly, and Chroma in Taiwan for PEM manufacturing. The model also incorporates Tesla's later shift towards vertical integration, including the construction of Gigafactories for in-house production. These experiments calculate metrics such as production speed, quality control, and overall costs for different supply chain configurations.

**Persuade**: The model generates insights that mirror Tesla's real-world data-driven approach to persuasion. It compares the outcomes of initial outsourcing experiments with later vertical integration results, demonstrating the need for greater supply chain control. This aligns with Tesla's use of such data to justify increased capital expenditures to investors, such as the $9 billion forecast for 2023.

**Train**: Our relational reasoning model serves as a framework for developing internal capabilities in manufacturing and supply chain management. It allows for the exploration of trade-offs between outsourcing and vertical integration, considering factors like quality control, speed to market, and cost-effectiveness. This approach simulates Tesla's real-world training of teams to balance these complex factors in supply chain decision-making.

##### 3.2.3 Social Reasoning for Social Impact Strategy
**Goal**: Our objective was to model Tesla's approach to developing a business model with positive social impact, focusing on the promotion of sustainable transportation. This model aims to balance environmental benefits, customer perceptions, and business viability.

**Belief**: The model incorporates Tesla's initial assumption that innovative electric vehicles would have a positive social impact by reducing carbon emissions and promoting sustainable transportation. This belief is encoded as a prior that links EV adoption rates to positive environmental outcomes.

**Learn Experiment**: To simulate Tesla's learning process, we designed experiments that model their surveys and focus groups on customer perceptions of EVs' social impact. The model also incorporates experiments with different vehicle models and price points to increase EV adoption, as well as tests on the impact of the Supercharger network on EV adoption rates. These experiments calculate metrics such as perceived environmental benefit, customer satisfaction, and overall EV adoption rates.

**Persuade**: The model generates insights that mirror Tesla's real-world approach to crafting a compelling vision of sustainable transportation. It quantifies the environmental impact of increased EV adoption, simulating Tesla's use of such data to demonstrate their contribution to reducing urban air pollution and combating climate change. This aligns with Tesla's strategy of inspiring team members, stakeholders, and potential customers with a vision of a sustainable future.

**Train**: Our social reasoning model serves as a framework for developing training programs focused on understanding the broader implications of business decisions on various stakeholders. It allows for the exploration of how different product development and business strategies might impact customers, employees, investors, and the environment. This approach simulates Tesla's real-world training of employees to anticipate and address social and environmental concerns in their decision-making processes.

##### 3.2.4 Integrated Evaluation
###### 3.2.4.1 Comparing Individual and Integrated Reasoning 
To illustrate an integrated evaluation of Tesla's marketing, sourcing, and social impact strategy using probabilistic, relational, and social reasoning, we can create a model that considers the interdependencies between these aspects. This approach aligns with the spirit of the Phadnis and Fine (2017), which emphasizes that locally optimal (sourcing and distribution) strategy may not be globally optimal when considering the end-to-end supply chain. Let's consider a decision about whether to source batteries locally or globally:

Probabilistic reasoning for Marketing strategy: 
- Local sourcing might allow for faster product iterations, potentially increasing demand by 10% due to more frequent updates.
- However, it might also increase costs by 15%, potentially reducing demand by 5%.

Relational reasoning for Sourcing strategy:
- Local sourcing could reduce lead times by 30% and increase supply chain flexibility.
- It could enhance Tesla's ability to innovate and implement the latest battery technology more quickly, potentially improving performance by 5-10%.

Social reasoning for Social Impact strategy:
- Local sourcing could reduce carbon footprint of production by 20%.
- It might also create local jobs, improving public perception and potentially increasing demand by 3%.

Integrated Evaluation:
- Traditional supply chain thinking might favor global sourcing due to potentially lower costs.
- However, an integrated evaluation shows that local sourcing could be superior:
  1. The demand increase from faster iterations, improved performance, and improved public perception (18-23%) significantly outweighs the decrease from higher costs (5%).
  2. The supply chain flexibility from local sourcing allows Tesla to better match supply with the more volatile demand of an innovative product.
  3. The environmental benefits align with Tesla's brand image, potentially creating a virtuous cycle of increased demand and positive social impact.
  4. Faster innovation cycles in battery technology could lead to a competitive advantage, further boosting demand and potentially offsetting higher production costs through premium pricing.
  5. The improved performance from quicker implementation of battery innovations could enhance Tesla's reputation as a technology leader, reinforcing brand value and potentially justifying higher prices.

This integrated approach reveals that local sourcing, despite higher upfront costs, could be the optimal end-to-end strategy when considering marketing, sourcing, and social impact together. It demonstrates how a seemingly cost-inefficient choice can lead to superior overall performance by leveraging synergies across different aspects of the business. This aligns with the paper's insight about how responsive components in a supply chain strategy can outperform cost-efficient ones, even for what might be considered more "functional" products like car batteries.

###### 3.2.4.2 Comparison of Individual and Integrative Evaluation
- Synergies and Trade-offs:
    - Individual: Might overlook how strengths in one area can compensate for weaknesses in another.
    - Integrated: Recognizes how, for instance, the Supercharger network addresses multiple concerns simultaneously (range anxiety, user experience, EV adoption), creating synergies across marketing, product, and social impact.
- Long-term Strategy Alignment:
    - Individual: Might focus on short-term optimizations within each domain.
    - Integrated: Considers long-term strategic alignment. For example, Gigafactories are evaluated not just on production efficiency, but on how they contribute to brand image and environmental goals.
- Risk Assessment:
    - Individual: Might identify risks within each domain separately.
    - Integrated: Considers interconnected risks. For instance, how ambitious marketing promises might strain production capabilities and potentially impact brand reputation.
- Innovation Drivers:
    - Individual: Might focus on innovation within specific areas (e.g., battery technology, manufacturing processes).
    - Integrated: Sees how innovations in one area drive changes in others. For example, how battery technology improvements affect pricing strategies, market positioning, and environmental impact.
- Stakeholder Value:
    - Individual: Might prioritize certain stakeholders relevant to each domain.
    - Integrated: Balances value creation for multiple stakeholders simultaneously. For instance, considering how pricing strategies affect not just profitability but also market adoption rates and the broader goal of accelerating sustainable transportation.
### 4. Conclusion and Future Directions

The integration of inference and decision along with the combination of different reasoning types, offers a promising path to overcoming barriers to Bayesian reasoning adoption in entrepreneurship. 

Future research should focus on
- developing user-friendly tools that implement these integrated approaches and empirically testing their effectiveness in entrepreneurial decision-making. 
- add more clockspeed based strategy (Fine, 2000)

### Reference
#### Bayesian Entrepreneurship
Fine, C. et al (2022), “Operations for Entrepreneurs: Can OM make a difference in Entrepreneurial Theory and Practice?”, Production & Operations Management, 31(12), 4599-4615, 2022. 
Fine, C. H. (2000). Clockspeed‐based strategies for supply chain design 1. _Production and operations management_, _9_(3), 213-221.
Phadnis, S, and C. Fine, “End-to-end Supply Chain Strategies: Parametric Study of the Apparel Industry,” Production and Operations Management, 26(12), 2305-2322. ,2017. 
Agarwal, et al, “Bayesian Entrepreneurship,” MIT working paper, 2024, at https://www.dropbox.com/scl/fi/kzlamnq9nx9qkh274e40f/0-Bayesian_Entrepreneurship-WP-Updated.pdf?rlkey=cmx6arg7x821fzyvzevapc30z&dl=0
Gans, J., Scott, E.L., & Stern, S. (2025). Entrepreneurship: Choice and Strategy. W.W. Norton, Incorporated.
#### Bayesian reasoning
Andrade, J., & Duggan, J. (2020). An evaluation of Hamiltonian Monte Carlo performance to calibrate age-structured compartmental SEIR models to incidence data. _Epidemics_, _33_, 100415.
Andrade, J., & Duggan, J. (2021). A Bayesian approach to calibrate system dynamics models using Hamiltonian Monte Carlo. _System Dynamics Review_, _37_(4), 283-309.
Andrade, J., & Duggan, J. (2022). Inferring the effective reproductive number from deterministic and semi-deterministic compartmental models using incidence and mobility data. _PLOS Computational Biology_, _18_(6), e1010206.
Andrade, J., Beishuizen, B., Stein, M., Connolly, M., & Duggan, J. (2024). Preparing for pandemic response in the context of limited resources. _System Dynamics Review_.
Bissiri, P. G., Holmes, C. C., & Walker, S. G. (2016). A general framework for updating belief distributions. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 78(5), 1103-1130.
Becker, M. R., Lew, A. K., Wang, X., Ghavami, M., Huot, M., Rinard, M. C., & Mansinghka, V. K. (2024). Probabilistic Programming with Programmable Variational Inference. _Proceedings of the ACM on Programming Languages_, _8_(PLDI), 2123-2147.
Gelman, A., Vehtari, A., Simpson, D., Margossian, C. C., Carpenter, B., Yao, Y., ... & Modrák, M. (2020). Bayesian workflow. arXiv preprint arXiv:2011.01808.
Moon, A., Kim, S., Stanify - Bridging System dynamics tool (Vensim) and Bayesian computation tool (Stan) https://github.com/Data4DM/stanify
Thomke, Stefan. "Building A Culture of Experimentation." Harvard Business Review 98, no. 2 (March–April 2020): 40–48.
Štrumbelj, E., Bouchard-Côté, A., Corander, J., Gelman, A., Rue, H., Murray, L., ... & Vehtari, A. (2024). Past, Present and Future of Software for Bayesian Inference. Statistical Science, 39(1), 46-61.
Wong, L., Grand, G., Lew, A. K., Goodman, N. D., Mansinghka, V. K., Andreas, J., & Tenenbaum, J. B. (2023). From word models to world models: Translating from natural language to the probabilistic language of thought. arXiv preprint arXiv:2306.12672.

### Appendix
##### code for 3.2.1 Probabilistic Reasoning in Marketing Strategy
```scheme
;; Define the generative model
(define (vehicle range)
  (list (pair 'range range)))

(define (market-demand range urban?)
  (if urban?
      (gaussian (+ 50 (* 0.2 range)) 10)
      (gaussian (+ 30 (* 0.3 range)) 15)))

(define (adoption-rate demand price)
  (min 1 (max 0 (- 1 (/ price demand)))))

(define (revenue vehicles-sold price)
  (* vehicles-sold price))

;; Define the experiment
(define (run-experiment range urban? price)
  (let* ((demand (market-demand range urban?))
         (rate (adoption-rate demand price))
         (vehicles-sold (* rate 1000))  ; assume market size of 1000
         (rev (revenue vehicles-sold price)))
    (list (pair 'demand demand)
          (pair 'adoption-rate rate)
          (pair 'revenue rev))))

;; Language model translation (simplified)
(define (translate-to-condition statement)
  (case statement
    (("The 350-mile range vehicle has higher adoption")
     (lambda (result)
       (> (cadr (assoc 'adoption-rate result)) 0.5)))
    (else (lambda (result) #t))))

;; Probabilistic inference
(define (infer-adoption range urban? price condition-statement)
  (rejection-query
   (define experiment-result (run-experiment range urban? price))
   experiment-result
   ((translate-to-condition condition-statement) experiment-result)))

;; Example usage
(define urban-350-result 
  (infer-adoption 350 #t 45000 "The 350-mile range vehicle has higher adoption"))

(define rural-350-result
  (infer-adoption 350 #f 45000 "The 350-mile range vehicle has higher adoption"))

(define urban-300-result
  (infer-adoption 300 #t 40000 "The 350-mile range vehicle has higher adoption"))

(define rural-300-result
  (infer-adoption 300 #f 40000 "The 350-mile range vehicle has higher adoption"))

;; Compare results
(display "350-mile range adoption in urban areas: ")
(display (cadr (assoc 'adoption-rate urban-350-result)))
(newline)

(display "350-mile range adoption in rural areas: ")
(display (cadr (assoc 'adoption-rate rural-350-result)))
(newline)

(display "300-mile range adoption in urban areas: ")
(display (cadr (assoc 'adoption-rate urban-300-result)))
(newline)

(display "300-mile range adoption in rural areas: ")
(display (cadr (assoc 'adoption-rate rural-300-result)))
(newline)
```
##### code for 3.2.2 Relational Reasoning in Supply Chain Strategy
```scheme
;; Define the manufacturing entities
(define (manufacturer id name labor-cost iteration-speed quality-control logistics-cost)
  (list
    (pair 'id id)
    (pair 'name name)
    (pair 'labor-cost labor-cost)
    (pair 'iteration-speed iteration-speed)
    (pair 'quality-control quality-control)
    (pair 'logistics-cost logistics-cost)))

;; Define relationships between entities
(define (partnership partner1 partner2 strength)
  (list partner1 partner2 strength))

;; Generate the initial supply chain
(define (generate-initial-supply-chain)
  (let ((tesla (manufacturer 'tesla "Tesla" 9 5 8 2))
        (lotus (manufacturer 'lotus "Lotus" 7 6 7 5))
        (xcellent (manufacturer 'xcellent "Xcellent" 3 2 5 8))
        (chroma (manufacturer 'chroma "Chroma" 4 3 6 7)))
    (list
      tesla lotus xcellent chroma
      (partnership 'tesla 'lotus 0.9)
      (partnership 'tesla 'xcellent 0.7)
      (partnership 'tesla 'chroma 0.8))))

;; Initial (flawed) strategy evaluation function
(define (initial-strategy-score manufacturer-id)
  (let ((labor-cost (get-attribute manufacturer-id 'labor-cost))
        (iteration-speed (get-attribute manufacturer-id 'iteration-speed))
        (quality-control (get-attribute manufacturer-id 'quality-control))
        (logistics-cost (get-attribute manufacturer-id 'logistics-cost)))
    (+ (* 0.5 (- 10 labor-cost))  ; Overemphasis on labor cost
       (* 0.2 iteration-speed)
       (* 0.2 quality-control)
       (* 0.1 (- 10 logistics-cost)))))  ; Underemphasis on logistics cost

;; Updated strategy evaluation function
(define (updated-strategy-score manufacturer-id)
  (let ((labor-cost (get-attribute manufacturer-id 'labor-cost))
        (iteration-speed (get-attribute manufacturer-id 'iteration-speed))
        (quality-control (get-attribute manufacturer-id 'quality-control))
        (logistics-cost (get-attribute manufacturer-id 'logistics-cost)))
    (+ (* 0.1 (- 10 labor-cost))  ; Reduced emphasis on labor cost
       (* 0.4 iteration-speed)    ; Increased emphasis on iteration speed
       (* 0.3 quality-control)    ; Increased emphasis on quality control
       (* 0.2 (- 10 logistics-cost)))))  ; Increased emphasis on logistics cost

;; Query functions (as before)
(define (get-attribute manufacturer-id attribute)
  (let ((manufacturer (find (lambda (m) (equal? (cadr (assoc 'id m)) manufacturer-id)) (generate-initial-supply-chain))))
    (cadr (assoc attribute manufacturer))))

;; Relational reasoning functions
(define (initial-best-strategy)
  (let ((partners '(lotus xcellent chroma)))
    (argmax initial-strategy-score partners)))

(define (updated-best-strategy)
  (let ((partners '(lotus xcellent chroma)))
    (argmax updated-strategy-score partners)))

;; Example queries
(query (initial-best-strategy))
(query (updated-best-strategy))
```
##### code for 3.2.3 Social Reasoning for Social Impact Strategy 
```scheme
;; Define the generative model
(define (ev-model range price emissions)
  (list (pair 'range range)
        (pair 'price price)
        (pair 'emissions emissions)))

(define (customer-utility range price emissions)
  (+ (* 0.5 range) (* -0.3 price) (* -0.2 emissions)))

(define (social-impact emissions)
  (- 0 emissions))

(define (company-utility sales social-impact)
  (+ (* 0.7 sales) (* 0.3 social-impact)))

;; Define the experiment
(define (run-experiment range price emissions)
  (let* ((model (ev-model range price emissions))
         (cust-util (customer-utility range price emissions))
         (soc-impact (social-impact emissions))
         (sales (min 1000 (* 10 (max 0 cust-util))))
         (comp-util (company-utility sales soc-impact)))
    (list (pair 'customer-utility cust-util)
          (pair 'social-impact soc-impact)
          (pair 'sales sales)
          (pair 'company-utility comp-util))))

;; Language model translation (simplified)
(define (translate-to-condition statement)
  (case statement
    (("The EV has a positive social impact")
     (lambda (result)
       (> (cadr (assoc 'social-impact result)) 0)))
    (else (lambda (result) #t))))

;; Probabilistic inference
(define (infer-impact range price emissions condition-statement)
  (rejection-query
   (define experiment-result (run-experiment range price emissions))
   experiment-result
   ((translate-to-condition condition-statement) experiment-result)))

;; Example usage
(define model-s-result 
  (infer-impact 400 80000 20 "The EV has a positive social impact"))

(define model-3-result
  (infer-impact 250 35000 18 "The EV has a positive social impact"))

;; Compare results
(display "Model S social impact: ")
(display (cadr (assoc 'social-impact model-s-result)))
(newline)

(display "Model 3 social impact: ")
(display (cadr (assoc 'social-impact model-3-result)))
(newline)

(display "Model S sales: ")
(display (cadr (assoc 'sales model-s-result)))
(newline)

(display "Model 3 sales: ")
(display (cadr (assoc 'sales model-3-result)))
(newline)
```


| Operational Consideration                      | Probabilistic Reasoning                           | Relational Reasoning                                | Social Reasoning                                  |
| ---------------------------------------------- | ------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------- |
| **Facilities**                                 |                                                   |                                                     |                                                   |
| - Size                                         | Capacity modeling, demand forecasting             | Supply chain logistics, transportation costs        | Workforce needs, community impact                 |
| - Location                                     | Geographic factors, transportation infrastructure | Proximity to markets, supply chain efficiency       | Regulations, labor availability                   |
| - Focus                                        | Production efficiency, market access              | Integration with supply chain                       | Community impact, workforce utilization           |
| **Capacity**                                   |                                                   |                                                     |                                                   |
| - Amount                                       | Demand forecasting, production planning           | Supplier capabilities, production scheduling        | Workforce flexibility, overtime potential         |
| - Timing                                       | Lead times, demand fluctuations                   | Customer fulfillment, supplier delivery             | Workforce availability, schedule adjustments      |
| **Vertical Integration & Supplier Management** |                                                   |                                                     |                                                   |
| - Direction                                    | Supplier reliability, risk assessment             | Upstream/downstream relationships, collaboration    | Trust building, contract negotiation              |
| - Extent                                       | Market volatility, technological changes          | Control over production, cost savings               | Workforce, community, external partnerships       |
| **Production Technologies & Processes**        |                                                   |                                                     |                                                   |
| - Equipment                                    | Reliability, failure rates, maintenance costs     | Automation potential, system-level interactions     | Workforce training, safety, job displacement      |
| - Interconnectedness                           | Process bottlenecks, efficiency optimization      | Dependencies between processes                      | Communication, collaboration                      |
| **Workforce & Management**                     |                                                   |                                                     |                                                   |
| - Policies                                     | Financial impact, turnover, litigation risks      | Employee morale, productivity, conflict             | Fair wages, safe conditions, talent attraction    |
| - Skill Levels                                 | Training program effectiveness                    | Team performance, production efficiency             | Continuous learning, upskilling opportunities     |
| **Information Technologies**                   |                                                   |                                                     |                                                   |
| - Use and Investment                           | Efficiency, productivity, ROI                     | System integration, data sharing                    | User adoption, change management                  |
| **Supply Chain & Materials**                   |                                                   |                                                     |                                                   |
| - Logistics                                    | Inventory levels, transportation times            | Provider relationships, transportation optimization | Delivery performance, partner collaboration       |
| - Vendor Relations                             | Supplier reliability, disruption risks            | Contract negotiation, capabilities matching         | Trust building, conflict resolution               |
| **Organization & Incentives**                  |                                                   |                                                     |                                                   |
| - Structure                                    | Decision-making, accountability, performance      | Collaboration, communication                        | Employee morale, motivation, conflict             |
| - Incentives                                   | Cost, complexity, unintended consequences         | Impact on employee behavior                         | Alignment with goals, promotion of teamwork       |
| **Business Processes**                         |                                                   |                                                     |                                                   |
| - Product Generation                           | Process bottlenecks, efficiency optimization      | Cross-functional dependencies                       | Roles, responsibilities, collaboration            |
| - Interfaces                                   | Impact on efficiency, data accuracy               | Workflow integration, information exchange          | User experience, training                         |
| - Vendor Development                           | Supplier reliability, disruption risks            | Relationship management, delivery performance       | Collaboration culture, problem resolution         |
| - Order Fulfillment                            | Delivery times, customer satisfaction             | Customer relationships, service quality             | Customer service, issue resolution                |
| - Other Capabilities                           | Impact of cross-functional collaboration          | Departmental dependencies, potential synergies      | Innovation, communication, continuous improvement |


----
# todo
- review [[Kuljanin et al (in press) - Computational Process Theory.pdf]]
-  - key literature/module:  [[Cronin24_the_enterprise.pdf]], [Moon et al (2024)'s integrating bayesian inference and system dynamics](https://docs.google.com/presentation/d/19aQe6h7lz70h5427cArytNUJXqx0ndNKziyIVmUKtZs/edit#slide=id.g2ff515a62c6_0_115),   [[1🧬🌏AGCTE(mng)]], [[ns(operations and innovation management for early-stage social scientists)]]

Integrated Reasoning: combining multiple types of reasoning - probabilistic, relational, and social - to develop a more comprehensive and coherent approach to understanding language and constructing meaning. This integration aims to address the challenges of fragmentation and limited practical applicability in current language understanding and reasoning systems. The key components are:
1. Probabilistic reasoning: Using Bayesian methods and probabilistic programming to model uncertainty and update beliefs based on evidence.
2. Relational reasoning: Understanding the relationships and dependencies between different components of a system or domain.
3. Social reasoning: Modeling the knowledge production chain and how different agents (e.g., researchers, educators, practitioners) interact and contribute to understanding.

| Section                   | Relevant Quotes from "Word to World models"                                                                                                                                                                                                                                                                                                                                        | Relation to Integrated Reasoning                                                                                                   |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Introduction              | "Language expresses the vast internal landscape of our thoughts. We use language to convey what we believe, what we are uncertain about, and what we do not know."                                                                                                                                                                                                                 | Highlights the need for integrating different types of reasoning to capture the full range of human thought expressed in language. |
| Introduction              | "Theories of cognition have long considered human language and thinking to be deeply related, but fundamentally distinct."                                                                                                                                                                                                                                                         | Suggests the need for an integrated approach that combines language understanding with cognitive reasoning.                        |
| Introduction              | "Large language models (LLMs) use a new generation of attention-based deep neural networks to learn the probabilistic distributions of words from vast datasets of human language"                                                                                                                                                                                                 | Introduces the potential of using LLMs as a component in integrated reasoning systems.                                             |
| Introduction              | "We propose a framework for rational meaning construction in which linguistic meaning is formalized as a context-sensitive mapping from natural language to a distribution over expressions in a probabilistic language of thought (PLoT) for rational world modeling and inference."                                                                                              | Outlines the core idea of the integrated reasoning approach, combining probabilistic, relational, and linguistic components.       |
| Overview of the Key Ideas | "We view the world models that support biological intelligence as structured and probabilistic, designed to integrate the noisy evidence an agent receives into causal, explanatory models that allow them to maintain coherent beliefs about the world and generalizably infer consistent, useful predictions and plans."                                                         | Emphasizes the importance of probabilistic reasoning in the integrated approach.                                                   |
| Overview of the Key Ideas | "We frame the problem of deriving meaning as inferring the mappings between a language's system of external communicative signals into the representations of rational thought."                                                                                                                                                                                                   | Highlights the relational aspect of reasoning, connecting language to internal representations.                                    |
| Overview of the Key Ideas | "We propose that probabilistic programs can formally instantiate the first component. They offer a structured representation for expressing novel situations and arbitrary problems with respect to a meaningful model over possible world states, a coherent notion of conditional belief updating, and a systematic framework for inferences with respect to queries and goals." | Describes how probabilistic programming can serve as a foundation for integrated reasoning.                                        |
| Overview of the Key Ideas | "We propose, in turn, that meaning construction can be modeled as translation from utterances in language to expressions in a general probabilistic programming language."                                                                                                                                                                                                         | Outlines how language understanding can be integrated with probabilistic reasoning.                                                |
