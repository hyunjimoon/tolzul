
| 🧊margine note (polyhedron) |                                                             |
| --------------------------- | ----------------------------------------------------------- |
| 🕸️vensim (graph)           |                                                             |
| 👫github (matrix)           |                                                             |
| 📚language model            | https://claude.ai/chat/79acbe33-faab-4154-a7f8-c13a99abf045 |
 
- goal is not failing
- reward: 1 if not fail, -1 if fail

code: https://github.com/Data4DM/Ops4Entrep-backend/tree/main/simulation
# Transportation Algorithms and Innovation

## Abstract
This report examines how transportation algorithms can provide valuable insights for innovation in the electric vehicle (EV) startup space. Using the fictional EV startup Starling as a case study, it explores four key algorithms: 1) Time-space diagrams for business planning, 2) Markov chains for static analysis of revenue and cost components of profit, 3) Decision rules for experimentation to find product market fit, 4) The relationship between startup pivots and the Simplex algorithm. While simplified, these examples illustrate the potential for cross-pollination between transportation optimization methods and emerging field of entrepreneurial strategy.
### 1. Introduction
The transportation sector faces significant challenges, from congestion to sustainability. At the same time, innovation in transportation, especially in the EV startup space, can benefit from applying algorithms and frameworks originally developed to solve transportation problems. This report presents four examples of transportation algorithms and their applicability to guiding the strategic decisions of the fictional EV startup Starling as it searches for product-market fit.

###  2. Time-space Diagrams for Dynamic Business Planning 
#### 2.1 Problem Statement
Effectively planning an EV startup (named starling)'s journey from early stage to product-market fit requires mapping business activities across both temporal and functional dimensions. This presents a complex, high-dimensional optimization challenge.

#### 2.2 Methods
Time-space diagrams, commonly used in transit planning, provide a framework for this task. For Starling, time is represented by 15 startup stages from goal-setting to hiring (Autlet, 2019; Cheek, 2024). The spatial axis captures 9 key business components, from partners to customer segments. By plotting activity sequence on this spatial canvas, a navigable "dynamic business canvas" emerges. While not a formal mathematical optimization, the time-space approach helps render an otherwise intractable 40+ dimensional planning space into an intuitive visual format. Potential inconsistencies, bottlenecks and synchronization issues in the startup's plans can be identified. Dynamic adjustments can be made as time unfolds and uncertainties are resolved.

![[Pasted image 20240514182227.png|800]]
#### 2.3 Conclusions
Time-space diagrams are a practical, communicable way to grapple with the "curses of dimensionality" that arise in holistic startup planning. More formal mathematical representations (e.g. tensor notation) may prove fruitful extensions.

### 3. Markov Chains and Heuristic Experimentation
#### 3.1 Problem Statement 
Faced with market uncertainties, Starling must decide which target markets and product configurations to experiment with in sequence. It needs a principled approach to incorporate market signals and update its product-market fit hypotheses.

#### 3.2 Methods
Startup first goes through static analysis of its profit.
![[Pasted image 20240514191541.png|800]]
A 3x3 Markov chain is proposed to model Starling's "state" as a combination of 3 potential markets (urban, suburban, rural) and 3 product types (300, 350, 400 mile range). Four "actions" are defined: pivot product, pivot market, scale, and fail. Transitions depend on a heuristic decision rule based on EV sales relative to two thresholds. 
Starling's belief in market acceptance for each state is modeled as a normal distribution with mean mu (optimism) and standard deviation sigma (confidence). Bayesian updating is used to modify beliefs after each experiment.

![[Pasted image 20240514190809.png|700]]
figures explain how startup pivot can be modeled in markov decision process framework. States are agent's belief, market, product , action is pivot product and pivot market. Scale and Fail is included in transition probability determined by whether observed signal is located with respect to low and high bar of startup. Low and high bar is predicted range of evaluation. Parameter of belief udpate model is as below.

1. Optimism `a`: The startup's belief about how well its average product will be accepted by the average market, standardized by the uncertainty of the product. Mathematically, it is represented as $\frac{𝜇_𝑝 - 𝜇_𝑚}{𝜎_𝑝}$, where $𝜇_𝑝$ is the mean belief about product acceptance, $𝜇_𝑚$ is the mean belief about market acceptance, and $𝜎_𝑝$ is the uncertainty of the product.

2. Uncertainty on market over uncertainty on product ($\frac{𝜎_𝑚}{𝜎_𝑝}$): The ratio of uncertainty of market acceptance ($𝜎_𝑚$) to uncertainty of product feasibility ($𝜎_𝑝$). This ratio is used to update the startup's belief based on the gap between the predicted and actual market evaluation.

The market's evaluation is generated based on distributions of:

- Dynamic market: This component represents the dynamic nature of the market, which evolves over time. It is characterized by the mean market acceptance ($𝜇_𝑚$).

- Uncertainty of product feasibility ($𝜎_𝑝$): This represents the startup's uncertainty about the performance and feasibility of its product in the market.

Appendix Stan code of this belief update (from prior distribution of market acceptance to posterior distribution given real market signal).

#### 3.3 Conclusions
Simulation of the Markov chain (not shown) illustrates how Starling can sequentially refine its product-market focus based on sales results. The importance of initial belief parameterization is noted - high initial optimism and confidence help abandon false leads faster. While stylized, the Markov framework effectively captures the dynamics of heuristic search and learning. Potential enhancements include increasing the state and action spaces, and exploring policies based on Markov decision processes.
### 4. Geometry of Startup Pivots
#### 4.1 Problem Statement
Startups must often "pivot" their business models in response to new information about what is feasible and desirable. A unifying mathematical lens for considering such pivots is sought.

#### 4.2 Methods
Startup business model components and their connections can be represented as a network/graph. Each vertex of the graph corresponds to a specific business configuration or state.

The startup's state can also be viewed as a vertex of a polyhedron in multi-dimensional space whose shape is defined by the edges between states. The polyhedron's faces represent feasibility constraints. Pivot direction is guided by an objective function informed by market demand.

This framework is analogous to the Simplex algorithm in linear optimization, where movement occurs between corner points of a geometrically-defined solution space. Updates to constraints (feasibility) or the objective (desirability) alter the solution.
![[Pasted image 20240514191510.png]]
#### 4.3 Results
A toy demonstration shows how Starling's business model network can be mapped to a low-dimensional polyhedron. Hypothetical pivots are visualized as movements across the polyhedron's surface. Changes in market demand shift the orientation of the pivot trajectory. While a simplified representation, the geometric view of startup pivots provides useful metaphors for considering the connectivity between business model options and the directionality of changes. More realistic representations would involve higher dimensions and topological complications.

### 5. Future Work
The four examples presented illustrate how concepts from transportation —time-space diagrams, Markov chains, Markov decision process, and startup pivot — can shed light on strategic choices in innovation contexts like EV startups. While simplified for illustration, they demonstrate the potential for cross-domain pollination. 
Future work could develop more realistic specifications tailored to specific startup use cases. Empirical calibration through entrepreneur interviews or case studies could enhance decision support. Interactive visualizations could aid practitioner communication.

### References
Aulet, B. (2024). _Disciplined Entrepreneurship Expanded & Updated: 24 Steps to a Successful Startup_. John Wiley & Sons.
Agrawal, A., Camuffo, A., Gambardella, A., Gas, J., Scott, E., & Stern, S. (2024). Bayesian Entrepreneurship. Working Paper.

### Appendix
I recommend https://betanalpha.github.io/assets/case_studies/stan_intro.html for further detail in Stan syntax.

```
data {
	int<lower=0, upper=1> E; // good evaluation (1) or bad evaluation (0)
	
	real a_mean_b; // optimism 😄 startup's belief on its average product accepted by average market, standardized by uncertainty of product
	
	real<lower=0> U; // uncertainty 🤔 startup's uncertainty on market over uncertainty on product 
}

parameters {
	vector[E] a; // optimism on product in chosen market
	
	real<lower=0> sigma; 
}

model {
	// Priors
	sigma ~ exponential(U); 
	
	a ~ normal(a_mean_b, sigma); // optimism (a_mean_b) + uncertatinty on chosen market 
		
	// Likelihood
	vector p;
	
	p = inv_logit(a); // translate optimism and confidence to expected probability of getting good evaluation
	
	E ~ bernoulli(p); // observing good evaluation given expected probability of getting good evaluation
}
```

not included: a_mean_b ~ exponential(1)
#### Data Block
- **`int<lower=0, upper=1> E;`**  
  Represents a binary outcome of product evaluation—either good (`1`) or bad (`0`). This parameter directly corresponds to "sampled evaluation" in your framework, capturing the binary outcome of market acceptance.

- **`real a_mean_b;`**  
  Signifies the average baseline optimism about a product receiving good evaluations. This parameter can be associated with "O: Optimism," reflecting the startup's confidence in the product's success across the average market, adjusted for product and market variability.

- **`real<lower=0> U;`**  
    Measures the startup's uncertainty about the market relative to the uncertainty about the product. This directly ties to "U: Uncertainty ratio," quantifying the relationship between market and product uncertainties.
#### Parameters Block
- **`vector[N] a;`**  
  This array represents the optimism levels for each evaluation, catering to market-specific conditions. It aligns with the "D: Dynamic Market," where market dynamics influence individual perceptions about the product's success.

- **`real<lower=0> sigma;`**  
  Defines the standard deviation for optimism across evaluations, reflecting market stability or instability. This relates to "E: Experiment opportunity" as it models the extent of variability that can be tolerated or explored during market testing.

#### Model Block
- **`sigma ~ exponential(U);`**  
  The distribution of `sigma` suggests that higher confidence (lower uncertainty about the market) leads to less variability in optimism, which is consistent with a stable market environment (lower "U: Uncertainty ratio").

- **`a ~ normal(a_mean_b, sigma);`**  
  The optimism for each product is modeled to follow a normal distribution centered around the baseline optimism, adjusted for the standard deviation dictated by market confidence. This captures the essence of "R: Risk-cash Tolerance" by quantifying how risk tolerance affects optimism variance.

- **`p = inv_logit(a);`**  
  Translates the adjusted optimism into a probability metric (`p`), which predicts the likelihood of receiving good evaluations. This is a critical step linking theoretical predictions to practical outcomes.

- **`E ~ bernoulli(p);`**  
  Models the observed evaluations as a Bernoulli process, influenced by the computed probabilities. This directly demonstrates how internal optimism and external market dynamics converge to shape real-world product evaluations.



-----

# previous
pivot: new basic feasible solution (retain (pivoting is a basic mechansim to retain feasibility and enhance desirability)
new basic feasible solution where (x1, x3, x4)=0, 


| simplex method pivot                                                 | startup pivot |
| -------------------------------------------------------------------- | ------------- |
| find direction of enhancing optimality while maintaining feasibility |               |
| ratio test                                                           |               |
| positive coefficient (possible direction of objective increase)      |               |
| simplex: optimality given feasibility                                | push          |
| dual simplex: feasibility given optimality                           | pull          |

how is infeasibility detected in simplex?

Here's the simplified table focusing on feasibility and desirability:

| Simplex Method Pivot                                                                    | Startup Pivot                                                                                          |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Move between corners of a shape (feasibility) to find the best solution (desirability). | Change business plans or products (feasibility) to find the best setup for the startup (desirability). |
| Updated constraints change the shape of possible solutions (feasibility).               | New tech (e.g., battery) updates what's possible for the startup (feasibility).                        |
| Updated objective function changes the direction of improvement (desirability).         | New market (e.g., eco-friendly car demand) updates what's desirable for the startup (desirability).    |

This concise table should help your YouTube audience understand the idea of moving through vertices (corners) during a simplex pivot and how it relates to startup pivots. Your animation comparing the pivot trajectories of `updated_product` (feasibility) and `updated_market` (desirability) will further clarify the concept.

| **Simplex Method Pivot** | **Startup Pivot** |
| --- | --- |
| Explore different solutions within the feasible space defined by rules to maximize outcomes. | Adjust products or business strategies within feasible changes to maximize startup's success in the desired market. |
| Test the boundaries of feasibility to identify potential improvements, while adhering to established guidelines. | Evaluate the extent of change the startup can incorporate without compromising stability, aiming to enhance market desirability. |
| Use indicators of feasibility to guide decisions towards the most effective solutions. | Utilize customer feedback and market trends to steer the startup towards areas with maximum desirability within feasible adjustments. |
| Persistently navigate through feasible options until the optimal solution is found or identified as unachievable. | Continuously adapt by integrating new technologies or market insights to find the best fit within the range of what’s feasible and desirable. |

This version integrates the concepts of feasibility and desirability, which should align well with your planned animation about how new technologies update the feasibility space (`updated_product`) and new market demands update the desirability space (`updated_market`).

| Simplex Method Pivot                                                                                                                     | Startup Pivot                                                                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Traverse across vertices (extreme points) of a polyhedron to find the optimal solution while maintaining feasibility.                    | Navigate through different business models, strategies, or product features to find the optimal configuration for the startup while ensuring viability and growth potential.                                              |
| Find the direction of enhancing optimality (improving the objective function) while maintaining feasibility (satisfying constraints).    | Identify the direction of enhancing the startup's value proposition, market fit, or growth potential while maintaining the core vision and mission.                                                                       |
| Ratio test is used to determine the step size to move along the improving direction without violating constraints. (FALSE)               | Assess the extent of change that can be made to the business model or strategy without compromising the startup's resources, stakeholder relationships, or legitimacy.                                                    |
| Positive reduced cost coefficients indicate possible directions of objective function increase.                                          | Positive feedback from customers, market trends, or metrics indicate potential areas for improvement or growth.                                                                                                           |
| Simplex: Maintain optimality given feasibility. Push the solution towards optimality while ensuring feasibility is not violated.         | Push: Proactively seek opportunities to enhance the startup's value proposition, market position, or growth potential while ensuring the changes are feasible and sustainable.                                            |
| Dual simplex: Maintain feasibility given optimality. Pull the solution towards feasibility while ensuring optimality is not compromised. | Pull: Reactively adapt the startup's business model or strategy in response to market demands, customer needs, or competitive pressures while striving to maintain the startup's competitive advantage and profitability. |
| Iterative process of moving from one vertex to another until the optimal solution is found or infeasibility is detected.                 | Iterative process of experimenting, learning, and adapting the startup's business model or strategy until product-market fit is achieved, sustainable growth is realized                                                  |
| detecting infeasibility                                                                                                                  | need for more fundamental pivot is recognized (how?)                                                                                                                                                                      |
| Efficient method to solve linear optimization problems by exploiting the structure of the feasible region (polyhedron).                  | Efficient approach to navigate the complex and uncertain landscape of entrepreneurship by leveraging the startup's agility, experimentation, and adaptability.                                                            |

The concept of pivot in the startup world shares similarities with the simplex method pivot in linear optimization. Both involve navigating through a complex landscape (polyhedron or business environment) to find the optimal configuration (solution or business model) while maintaining certain constraints (feasibility or viability). The process is iterative, with each pivot building upon the learning and insights gained from the previous steps.

Startups can draw inspiration from the simplex method pivot to embrace a more structured and systematic approach to pivoting:
1. Continuously assess the current position and identify potential directions for improvement.
2. Evaluate the feasibility and potential impact of each pivot option.
3. Select the most promising direction and determine the appropriate extent of change.
4. Execute the pivot and monitor the results closely.
5. Iterate the process based on the new learning and insights.

By understanding the parallels between the simplex method pivot and startup pivot, entrepreneurs can approach pivoting as a strategic tool for optimizing their ventures in the face of uncertainty and dinamically evolving the best path in the complex landscape of business opportunities, rather than as a reactive measure to be taken only when faced with challenges or setbacks.

----

1. pomdp formulation of early stage startup experiment to learn product-market fit
2. how different business strategies on early stage startup can be transfer-learned

| Parameter                                                 | Hypothesis on Time to Change Market over Change product (T2CMP) w.r.t. Parameter                                                                                                                      | early stage EV startup experiment                                                                                                                                                                                                                          | early stage AV startup experiment                                                                                                                                                                                                      |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C: Confidence on market acceptance                        | The more confident a startup is about the market acceptance (compared to production feasibility), the less it updates its belief about market, hence longer it takes to pivot the market.             | An EV startup highly confident in the demand for a specific battery chemistry may stick with it longer before considering pivoting to a different technology or market segment.                                                                            | An AV startup with strong conviction about the market acceptance of a particular use case, like autonomous shuttles, may persist longer before entertaining a pivot to another application.                                            |
| S: Stability of market                                    | The more dynamic market (low S) is, the less it updates its belief about market acceptance, hence longer it takes to pivot the market.                                                                | An EV startup operating in a highly dynamic market with rapidly evolving customer preferences and competitor moves may take longer to pivot, as the changing conditions make it harder to draw firm conclusions about market fit.                          | An AV startup in a market with frequent regulatory shifts and public perception changes may require more time to pivot, as the unstable environment complicates assessing the true state of market acceptance.                         |
| O: Optimism (gap of belief and real on market acceptance) | The more optimistic a startup is about market acceptance, the less it updates its belief about market, hence longer it takes to pivot the market.                                                     | An EV startup that is highly optimistic about the market potential for a new battery technology may continue pursuing it longer before considering a pivot, as the positive outlook reduces the perceived need to update beliefs based on market feedback. | An AV startup with a very optimistic view of the readiness of its technology for a specific use case may persist longer before pivoting, as the belief gap makes it less responsive to signals challenging its assumptions.            |
| E: Experiment opportunity                                 | The more experiment opportunity a startup has, the more scientific experiments can be done (e.g., in parallel), hence it can pivot to a more precise market, if needed.                               | An EV startup with ample resources to conduct multiple market validation tests simultaneously can more quickly zero in on the most promising segments and pivot accordingly.                                                                               | A well-funded AV startup that can afford to test various use cases and market segments in parallel will be able to more swiftly identify the optimal pivot direction based on comprehensive data.                                      |
| R: Risk endurance                                         | The more risk endurance a startup has (higher explore/exploit in cash term), the more scientific experiments can be done (e.g., in parallel), hence it can pivot to a more precise market, if needed. | An EV startup with high risk tolerance can conduct bolder experiments testing novel battery chemistries and market applications, enabling a more informed and targeted pivot if required.                                                                  | An AV startup with significant risk appetite may pursue more ambitious testing across a wider range of operating environments and use cases, allowing it to pivot more effectively to the best-fit market based on the data collected. |


|                      | 2-POMDPs.jl                                                                                                                                                                                                                                                                                                                                          | fit_product_market.py                                                                                                                                                                                                                                                                                                                                                                                                                 | bayesDB |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| summary of situation | parent agent feeding or ignoring baby who is observed to be crying or being quiet based on its latent state hungry or full                                                                                                                                                                                                                           | startup agent pivoting market or product of its business model which is observed to get good or bad review based on its fit or unfit product-market.                                                                                                                                                                                                                                                                                  |         |
| 👀state              | [hungry, full]                                                                                                                                                                                                                                                                                                                                       | [unfit, fit, capital]                                                                                                                                                                                                                                                                                                                                                                                                                 |         |
| 🤜action             | [feed, ignore]                                                                                                                                                                                                                                                                                                                                       | [pivoting_product, pivoting_market]                                                                                                                                                                                                                                                                                                                                                                                                   |         |
| 👀👀observation      | [crying, quiet]                                                                                                                                                                                                                                                                                                                                      | [bad, good]<br>observation = function O(s, a, s′)<br>    if s′ == fit<br>        return SparseCat([bad, good], [0.2, 0.8])<br>    elseif s′ == unfit<br>        return SparseCat([bad, good], [0.8, 0.2])<br>    end<br>end                                                                                                                                                                                                           |         |
| transition           | transition = function T(s, a)<br>        if a == feed<br>            return SparseCat([hungry, full], [0, 1])<br>        elseif s == hungry && a == ignore<br>            return SparseCat([hungry, full], [1, 0])<br>        elseif s == full && a == ignore<br>            return SparseCat([hungry, full], [0.1, 0.9])<br>        end<br>    end, | T(s, a) from business actions<br><br>transition = function T(s, a)<br>    if a == pivoting_product<br>        return SparseCat([unfit, fit, capital], [0.1, 0.8, 0.1])<br>    elseif s == unfit && a == pivoting_market<br>        return SparseCat([unfit, fit, capital], [0.5, 0.4, 0.1])<br>    elseif s == fit && a == pivoting_market<br>        return SparseCat([unfit, fit, capital], [0.1, 0.8, 0.1])<br>    end<br>end,<br> |         |
| 💰reward             | reward = (s,a)->(s == hungry ? -10 : 0) + (a == feed ? -5 : 0)                                                                                                                                                                                                                                                                                       | Based on business outcomes<br>reward = (s, a) -> <br>    (s == unfit ? -5 : 5) + <br>    (a == pivoting_product ? -2 : -3)<br>                                                                                                                                                                                                                                                                                                        |         |
| o\|o                 | observation = function O(s, a, s′)<br>        if s′ == hungry<br>            return SparseCat([crying, quiet], [0.8, 0.2])<br>        elseif s′ == full<br>            return SparseCat([crying, quiet], [0.1, 0.9])<br>        end<br>    end,                                                                                                      | Observations from market response<br>observation = function O(s, a, s′)<br>  if s′ == fit<br>    return SparseCat([bad, good], [0.2, 0.8])<br>  elseif s′ == unfit<br>     return SparseCat([bad, good], [0.8, 0.2])<br>   end<br> end,                                                                                                                                                                                               |         |

| 2-POMDPs.jl                                                                                                                                                                                                                                                                                                                                          |                      | fit_product_market.py                                                                                                                                                                                                                                                                                                                                                                                                                 | [[🏀basketball_pivot_example.pdf]]                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| parent agent feeding or ignoring baby who is observed to be crying or being quiet based on its latent state hungry or full                                                                                                                                                                                                                           | summary of situation | startup agent pivoting market or product of its business model which is observed to get good or bad review based on its fit or unfit product-market.                                                                                                                                                                                                                                                                                  |                                                                                                    |
| [hungry, full]                                                                                                                                                                                                                                                                                                                                       | 👀state              | [unfit, fit, capital]                                                                                                                                                                                                                                                                                                                                                                                                                 | [Executing, Versioning, Redirecting, Abandoning]                                                   |
| [feed, ignore]                                                                                                                                                                                                                                                                                                                                       | 🤜action             | [pivoting_product, pivoting_market]                                                                                                                                                                                                                                                                                                                                                                                                   | [Shoot, Dribble, Pass, Fail]                                                                       |
| [crying, quiet]                                                                                                                                                                                                                                                                                                                                      | 👀👀observation      | [bad, good]<br>observation = function O(s, a, s′)<br>    if s′ == fit<br>        return SparseCat([bad, good], [0.2, 0.8])<br>    elseif s′ == unfit<br>        return SparseCat([bad, good], [0.8, 0.2])<br>    end<br>end                                                                                                                                                                                                           | [Market feedback negative, Market feedback positive]                                               |
| transition = function T(s, a)<br>        if a == feed<br>            return SparseCat([hungry, full], [0, 1])<br>        elseif s == hungry && a == ignore<br>            return SparseCat([hungry, full], [1, 0])<br>        elseif s == full && a == ignore<br>            return SparseCat([hungry, full], [0.1, 0.9])<br>        end<br>    end, | transition           | T(s, a) from business actions<br><br>transition = function T(s, a)<br>    if a == pivoting_product<br>        return SparseCat([unfit, fit, capital], [0.1, 0.8, 0.1])<br>    elseif s == unfit && a == pivoting_market<br>        return SparseCat([unfit, fit, capital], [0.5, 0.4, 0.1])<br>    elseif s == fit && a == pivoting_market<br>        return SparseCat([unfit, fit, capital], [0.1, 0.8, 0.1])<br>    end<br>end,<br> | Transition based on market response and internal decision-making influenced by real options theory |
| reward = (s,a)->(s == hungry ? -10 : 0) + (a == feed ? -5 : 0)                                                                                                                                                                                                                                                                                       | 💰reward             | Based on business outcomes<br>reward = (s, a) -> <br>    (s == unfit ? -5 : 5) + <br>    (a == pivoting_product ? -2 : -3)<br>                                                                                                                                                                                                                                                                                                        | Rewards based on market share acquisition and revenue growth                                       |
| .9                                                                                                                                                                                                                                                                                                                                                   | discount             | .9                                                                                                                                                                                                                                                                                                                                                                                                                                    | .9 (Assuming long-term strategic thinking)                                                         |
| observation = function O(s, a, s′)<br>        if s′ == hungry<br>            return SparseCat([crying, quiet], [0.8, 0.2])<br>        elseif s′ == full<br>            return SparseCat([crying, quiet], [0.1, 0.9])<br>        end<br>    end,                                                                                                      | o\|o                 | Observations from market response<br>observation = function O(s, a, s′)<br>  if s′ == fit<br>    return SparseCat([bad, good], [0.2, 0.8])<br>  elseif s′ == unfit<br>     return SparseCat([bad, good], [0.8, 0.2])<br>   end<br> end,                                                                                                                                                                                               | Observational probabilities based on market dynamics and competitive response                      |
### 1. Critique of the Model and Case Study

The "Green Wheels" case study provides a practical application of a POMDP framework, depicting a startup's decision-making process concerning product and market adaptation based on observed market responses. However, there are areas that could be enhanced for realism and depth:

- **State Granularity**: The model could include more nuanced states within each market-product combination, such as "Early Adoption," "Growth," "Maturity," and "Decline," which would allow for a more dynamic and realistic representation of market evolution.
- **Complexity in Actions**: The actions of "pivoting product" and "pivoting market" could be expanded to include "introducing a new feature," "rebranding," or even "technology upgrades" which are common in product lifecycle management.
- **Feedback Loops**: The observation states (good and bad reviews) are simplistic. It could be beneficial to incorporate a broader range of customer feedback metrics such as Net Promoter Score (NPS), customer retention rates, and qualitative feedback.
- **Economic and Competitive Environment**: The model could also consider external factors such as changes in consumer preferences, economic downturns, or actions by competitors which significantly affect startup strategies.

### 2. Adding to the Table from "pivot_example.pdf"

From the document, let's extract the concepts corresponding to each state, action, observation, reward, discount, and observation transition that would apply in a POMDP context:

In the "pivot_example.pdf", the states, actions, and observations are conceptualized around the real options theory, where actions such as "Shoot," "Dribble," and "Pass" represent different strategic approaches a company can take based on their market positioning and internal capabilities . The rewards are not explicitly quantified in the document but are implied to relate to achieving better market fit and financial performance through adaptive strategies . Observations in this model would likely include direct market feedback, competitor actions, and internal performance metrics, informing further pivots and investment decisions.
state (market_belief, product, market_real, c, scale-pre_scale)
if c =0: absorb
action = m_p, p_p 
Q1.can i find parameterization where `product_pivot1`, `product_pivot2` be collapsed product_pivot actions?
- if utility is `market acceptance` and `production feasibility` - separable.

Q2. is parameterization (market_belief, product, ) reasonable?                                  
	- scale: `market_acceptance_belief_mu` +`market_acceptance_belief_sd` < `market_desirability_real` 
	- market_pivot: `market_acceptance_belief_mu` +`market_acceptance_belief_sd` < `market_desirability_real` 
	- fail: capital_state = 0 
![[Pasted image 20240424153445.png|800]]

Q3. transfer learning only apply to MDP? decision rules are sumo (learning rewards)
## Case Study: Early Stage Startup Pivoting through Market and Product Combinations

Consider an early stage startup that pivots through candidate market and product combinations. For simplicity, let's assume two markets ($m_1$: urban, $m_2$: rural) and two products ($p_1$: EV car, $p_2$: Hybrid car). The startup has an initial prior belief that the urban market prefers EV cars, while the rural market prefers Hybrid cars. We can formulate this problem using the Reinforcement Learning (RL) framework as follows:
#### 👀 State Set
![[Pasted image 20240424151610.png|400]]
$S = \{(m, p, b, c) | m \in \{m_1, m_2\}, p \in \{p_1, p_2\}, b \in \mathbb{R}, c \in \mathbb{R}^+\}$

The state is represented by a tuple $(m, p, b, c)$ where:
- $m$: current market (urban or rural)
- $p$: current product (EV car or Hybrid car)
- $\mu_b, \sigma_b$: belief about the market acceptance of the current market and product
- $c$: current cash state

#### 🤜 Action Set
$A = \{market\_pivot, product\_pivot\}$


- $market\_pivot$: pivot to a new market
- $product\_pivot$: pivot to a new product within the current market

#### 🗄️ Transition Matrix
The state transition is deterministic and depends on the current state and the chosen action. The transition matrices for each action are as follows:

##### 🗄️|🤜 action `market_pivot`
|                | $(m', p', b', c-cost)$ |
| -------------- | ---------------------- |
| $(m, p, b, c)$ | 1                      |
state 2, action 2, 

(market1, product1, mu1, sigma1, c) - (review)- [product_pivot] - (market1, product2, mu2, sigma2, c-1) -

reward: review (MPN['x_r'][m, p] = np.random.binomial(MPN['SR'], expit(MPN['a_r'][m,p]))[0])

1. better than baseline (cost 0이 돼 fail decision하기 전까지 cost minimize; shortest time to scale); 
2. oracle: 정확히 리뷰 알때 (바로 fail, scale) 


- sumo: real world (based on literature)
heuristic (RL) - 예측값이 낮아도 투자 (x가 실제와 다를수 있음 - 왜 rl??)
![[Pasted image 20240424153445.png|1000]]



- Market pivoting changes the market $m$ to the alternate market $m'$, resets the product $p$ to $p_1$, updates the belief $b$ to $b'$ based on the feedback, and reduces the cash $c$ by the pivoting cost.

##### 🗄️|🤜 action `product_pivot`
P(s,a,s') simulator

pi(s) -> a

- Product pivoting changes the product $p$ to the alternate product $p'$ within the current market $m$, updates the belief $b$ to $b'$ based on the feedback, and reduces the cash $c$ by the pivoting cost.

#### 💰 Rewards
The rewards in this model are implicit and tied to the ultimate success or failure of the startup. The objective is to find the optimal sequence of actions that maximizes the probability of scaling (success) while minimizing the probability of failure.

The rewards can be formulated as:
- $r(m, p, b, c, scale) = 1$ (if scaling is successful)
- $r(m, p, b, c, fail) = -1$ (if failure occurs)
- $r(m, p, b, c, market\_pivot) = 0$ (no immediate reward for market pivoting)
- $r(m, p, b, c, product\_pivot) = 0$ (no immediate reward for product pivoting)

The startup's goal is to find the optimal policy that maximizes the expected cumulative reward over the pivoting process. By exploring different market and product combinations, updating beliefs based on feedback, and managing cash resources, the startup aims to identify the most promising market-product fit that leads to successful scaling.
## forward
Viewing the value of an opportunity belief as scaled by its fit to the market is aligned with cognitive sciences and lens models of human judgment, which denote the fit of a judgment as the extent to which the mental representation matches the environment (Brunswik, 1956; Csaszar & LaureiroMartınez, 2018; Kozyreva & Hertwig, 2021; Shepherd & Zacharakis, 2002). This view of belief fit is aligned with Todd and Gigerenzer’s (2012) idea of ecological rationality, defined as the fit between a cognitive tool and the environment (Hertwig et al., 2019). Relative to this work, our notion of fit is more problem or belief specific—how well hypothesized solutions solve specific market problems. We thus view product–market fit as the correlation between (a) the entrepreneur’s own projections about the value-creation capacity of assumed needs and associated product features, and (b) the revealed value-creation capacity of these needs and features in the market. We call the former the belief model (Figure 2, left) and the latter the market model of the belief (Figure 2, right).

![[Pasted image 20240424105224.png]]