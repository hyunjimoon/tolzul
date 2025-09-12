
for #apply  [[🧭predict(entrepreneuring)]]

from hyunjimoon on 2024-04-17T11:23:40Z

target audience: BE evaluators
for PC evaluators, i summarized bayes.entrep in sister thread https://github.com/Data4DM/BayesSD/discussions/234

this thread's purpose is two: 

1. to put scalable auto-modeling using Bayesian synthesis and domain specific language on my [Bayes in Business supporters](https://github.com/Data4DM/Bayes2Business/blob/main/README.md#list-of-supporters)' radar 📡

2. to share my willingness to bet to prob.comp with Vikash and seek path to officially join [prob.comp project](http://probcomp.csail.mit.edu/)

format: [Bob Horn's information mural](https://www.bobhorn.us/) with more structured as 𝌭`designing` and image sequence as 🎞️`filming`. collaborated output of designer-value (𝌭), artist-vision (🎞️), scientist-understand (🔭), engineer-solve (⚙️) is architecture🏛️.

keywords: domain specific language [claude](https://claude.ai/chat/0f6e416a-8904-4c58-a8ed-cdfc4b4bf6d6), inference controller, reverse engineering natural intelligence, population model, posterior sampling algorithms

![image](https://github.com/user-attachments/assets/eac0720f-8d85-411c-8aa1-342f51de09f7)

---
## contents

[Inference controller, SMC algorithms (a): How does abstract knowledge guide learning and inference from sparse data? (e): How can probabilistic inferences be used to drive action?](https://github.com/Data4DM/BayesSD/discussions/224#discussioncomment-9179329)

[Reverse engineering natural intelligence (b): What form does that knowledge take, across different domains and tasks?](https://github.com/Data4DM/BayesSD/discussions/224#discussioncomment-9927775)

[Larger population model (c): How is that knowledge itself constructed?](https://github.com/Data4DM/BayesSD/discussions/224#discussioncomment-9481249)

[Posterior space sampling algorithms (d): How can learning and inference proceed efficiently and accurately, even with very complex hypothesis spaces?](https://github.com/Data4DM/BayesSD/discussions/224#discussioncomment-10440118)


| Concept | Description | Emoji |
|---------|-------------|-------|
| Hypothesis space (H) | Space of possible concepts |⬛️ |
| Examples (X) | X = {x1, . . . , xn}: n examples of a concept C | ⚫️ |
| Prior | p(h): domain knowledge, pre-existing biases | 🟩 |
| Likelihood | p(X\|h): statistical information in examples | 🔴 |
| Posterior | p(h\|X): degree of belief that h is the true extension of C | 🟦 |
| Size principle | Smaller hypotheses receive greater likelihood, exponentially more so as n increases |📌 |
| Choice principle | Choice of hypothesis space embodies a strong prior, favoring natural over logical possibilities |🌲>🎄 |
| Hypothesis averaging | p(y ∈ C \| X): Probability that C applies to new object y, averaged over all h weighted by p(h\|X) | ⭐️|
| Conservation of belief | Total probability must sum to 1; increased belief in some hypotheses necessitates decreased belief in others | ⚖️ |


----

### papers
- [Bayesian Synthesis of Probabilistic Programs for Automatic Data Modeling](https://arxiv.org/abs/1907.06249) 
![🎞️filming automatic data modeling mural](https://github.com/Data4DM/BayesSD/assets/30194633/b8b218a7-a170-4336-8e76-aa32738bfbc3)

### [Gen Tutorial](https://www.gen.dev/tutorials/)

![🎞️filming gen](https://github.com/Data4DM/BayesSD/assets/30194633/5c8c7f3e-536f-434d-b93b-9d64da32fde7)

### angie's action
- show Vikash [this demo](https://github.com/Data4DM/Ops4Entrep-backend/blob/pivot/simulation/idea_exp.ipynb) which is `stan`-based startup pivot simulation that tests existing hypothesis in entrepreneurship literature and align with prob.comp's vision to seek path in proceeding the project to develop startup education and prediction tool under computer human interaction expert's umbrella

- plan developing education material with Academy of Management conference Professional Development Workshops team (led by Andreas Schwab) e.g. gen-finance https://github.com/Data4DM/BayesSD/discussions/177

- model entrepreneurial growth https://github.com/Data4DM/BayesSD/discussions/174#discussioncomment-7922743

![ 🎞️ filming entrepreneurial growth](https://github.com/Data4DM/BayesSD/assets/30194633/2d69ab1e-4b57-4220-afc0-ac6ddce54a18)

- https://github.com/Data4DM/BayesSD/discussions/200


---

## Reply from hyunjimoon on 2024-04-21T14:01:46Z

## 1. inference controller, path finding sequential MC algorithms

### Fact
- George shared challenges in inference controller
### Angie's Belief
- "Kidnap the robot" from my friend (George)'s [notebook](https://github.com/probcomp/tasks2D/blob/main/notebooks_clean/KidnappedRobot.ipynb) is the key to understand, explain, predict, synthesize startup pivot. 

### Angie's action
sharing modularized prior and simulated re-action, asking for verification + further action
#### modularized prior
![🎞️filming george's kidnapped robot](https://github.com/Data4DM/BayesSD/assets/30194633/4ead815c-9c77-4862-9415-aa9ee12a35d4)

#### simulate re-action to prompt
>  similar need-solution dynamics in punctured equilibrium from evolutionary psychology?

baseline controller might represent a standard approach to robot navigation, using observed data to infer the robot's position and move toward the goal. In contrast, the robust controller introduces particle filtering, a method that uses a set of "particles" to represent the distribution of possible states, to improve the agent's beliefs about its location, particularly when uncertainties or changes in the environment occur.

 concept of punctuated equilibrium from evolutionary biology—and by extension, evolutionary psychology—can offer intriguing insights into the processes of adaptation and innovation, such as those found in startup pivots or the development of robust controllers for localization algorithms.

Punctuated equilibrium posits that evolutionary development is characterized by long periods of stability (equilibrium) interrupted by short, sudden changes (punctuations). In the context of startups, this can parallel the periods of steady growth or consistent business models that are periodically disrupted by significant shifts or 'pivots' in response to market changes, technological advancements, or new information.

Applying this to your friend George's situation with his localization algorithm, the 'Kidnap the robot' animation might metaphorically represent a startup's unexpected shift in the market or a sudden realization that the current business model isn't viable—a 'kidnapping' of the startup's trajectory. George's difficulty with developing an inference controller could be akin to a startup struggling to find a new direction after such a disruption.

The process of developing a robust controller could benefit from evolutionary principles in the following ways:

1. **Adaptation:** Just as species must adapt to survive after a punctuation event, startups need to pivot effectively to adapt to new market conditions. A localization algorithm must similarly adjust to unexpected changes in the environment.

2. **Diversity of Approaches:** In evolutionary terms, genetic diversity can increase a species' resilience. For George, incorporating a variety of inference strategies could provide a robustness that a single approach lacks. A startup might explore different business models or product offerings to find the most viable path forward.

3. **Selective Retention:** Evolution operates on the principle that successful adaptations are retained over generations. Similarly, a robust localization algorithm should retain successful strategies (or 'particles' in a particle filter context) while discarding those that are less effective. For startups, this means learning from what works and what doesn't, maintaining flexibility without losing sight of the core vision.

4. **Rapid Iteration:** Punctuations in evolutionary terms are relatively rapid bursts of change. For George's algorithm, this suggests that rapid prototyping and iterative testing could quickly identify the most effective strategies post-'kidnap'. In the startup world, swift iteration allows for rapid learning and adjustment to the new market conditions.

By drawing parallels between these evolutionary mechanisms and the challenges George faces, one can suggest that a more dynamic, adaptive, and resilient approach to algorithm development may emerge. This perspective might not only aid in refining his inference controller but also serve as an inspiration for startups navigating their pivots.

---

### Reply from jeanbaptiste on 2024-04-21T14:37:34Z

> Punctuated equilibrium posits that evolutionary development is characterized by long periods of stability (equilibrium) interrupted by short, sudden changes (punctuations). In the context of startups, this can parallel the periods of steady growth or consistent business models that are periodically disrupted by significant shifts or 'pivots' in response to market changes, technological advancements, or new information.

Yes! Exactly, i think this is a good mapping of exaptation in the startup evolution world.

---

### Reply from jeanbaptiste on 2024-04-21T15:34:44Z

About Exaptation and Pivot, these two articles (on biotech/pharma innovation!) might interest you:

- https://pubsonline.informs.org/doi/10.1287/orsc.2017.1116 (. In this paper, we measure the frequency of exaptation in the pharmaceutical industry. We find that about 42% of new functions derived from existing drugs have an exaptive nature)
- https://www.semanticscholar.org/paper/Functional-diversification-and-exaptation%3A-the-of-Andriani-Cattani/b303cd47c9f7c19d8e83dc06f05e8f7df355b446 (Functional diversification and exaptation: the emergence of new drug uses in the pharma industry)

---

### Reply from hyunjimoon on 2024-08-08T19:54:03Z

for gpt input:
[tasks2D_notebooks_clean_KidnappedRobot.ipynb at main · probcomp_tasks2D.pdf](https://github.com/user-attachments/files/16552778/tasks2D_notebooks_clean_KidnappedRobot.ipynb.at.main.probcomp_tasks2D.pdf)
 summary of the key points:

1. The experiment simulates a robot navigating through a 2D environment resembling a hotel with multiple rooms and hallways.

2. The goal is for the robot to navigate to a specific target (represented by a green square) while maintaining an accurate belief about its location.

3. Three different controllers are implemented and compared:
   a. A baseline controller that re-localizes at every timestep
   b. A baseline particle filter controller
   c. A robust controller using particle filtering with a reset mechanism

4. The "kidnapping" scenario is introduced, where the robot is suddenly moved to a new location without being aware of the change.

5. The robust controller is designed to handle the kidnapping scenario by resetting its particle filter when the estimated likelihood of observations falls below a certain threshold.

6. The notebook includes visualizations of the robot's path, belief state, and performance metrics for each controller.

7. Performance comparisons are made between the controllers in both normal and kidnapping scenarios, measuring steps to reach the goal and computation time per step.

8. The robust controller demonstrates the ability to recover from the kidnapping scenario, while the baseline controllers struggle to re-localize after being moved.

9. The experiment showcases the importance of balancing computational efficiency with the ability to handle unexpected changes in the environment.

10. The code uses Julia programming language and various libraries for probabilistic programming, particle filtering, and visualization.

This notebook serves as an educational and research tool for exploring robot localization and navigation strategies, particularly in scenarios where the robot's belief about its location may become dramatically incorrect.

---

### Reply from hyunjimoon on 2024-10-06T00:04:45Z

[bayes, simulation, gradceful disintegration cld](https://claude.ai/chat/ffa31da6-8476-4bcf-b114-35adfb7c0906)
 table summarizing the key concepts from each chapter and how they could apply to Angie's situation of learning about the future of probabilistic programming based on data from nine particle filters:

| Chapter | Main Concept | Application to Angie's Situation |
|---------|--------------|----------------------------------|
| Importance Sampling to SMC | Using weighted samples to approximate target distributions, with resampling to address weight degeneracy in sequential settings | Angie could use SMC to track the evolution of ideas/approaches in probabilistic programming over time, using the nine experts as "particles" and resampling based on how influential their ideas become |
| Learning Proposals and Twisting Targets | Adapting proposal distributions and intermediate target distributions to improve SMC performance | Angie could learn proposal distributions for predicting each expert's next contribution based on their past work. She could also design intermediate targets that incorporate information about future developments to guide the sampling |
| Nested Monte Carlo | Using layers of Monte Carlo sampling to approximate intractable ideal algorithms | Angie could use nested MC to handle uncertainty at multiple levels - e.g. uncertainty in each expert's contributions nested within uncertainty about overall field directions |
| Conditional SMC | Conditioning SMC on a reference trajectory to construct MCMC algorithms targeting the original distribution | Angie could use conditional SMC to explore alternative histories of probabilistic programming development, conditioning on the actual observed trajectory but allowing variations to study counterfactuals |


---

### Reply from hyunjimoon on 2024-10-06T00:08:28Z

#261 

---

## Reply from hyunjimoon on 2024-05-18T17:50:05Z

## 1. population model

Jaao, Angie
Jaao's (5th year phd) thesis is three components as below:
[🎞️filming of probabilistic programs as multi-task learner, uncertainty aware parsing of natural language into domain specific language, system for learning models of relational database](https://github.com/Data4DM/BayesSD/assets/30194633/b2d87a2d-239d-4aad-9537-d6d7c2103f2a)

crosscat: https://jmlr.org/papers/volume17/11-392/11-392.pdf, http://probcomp.csail.mit.edu/software/crosscat/
he seems to be most actively working on the third project with google (large population model)


---

### Reply from hyunjimoon on 2024-05-26T17:05:56Z

| Project                                       | Application                                                                                  | Benefit                                                                                                        |
|-----------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Probabilistic Programs that are Multi-task Learners for Data Science** | Enhance data analysis and predictive modeling for entrepreneurship.                           | Efficient handling of large-scale, uncertain data, improving decision-making processes.                        |
| **Probabilistic Programming for Uncertainty-aware Parsing of Natural Language into Domain-specific Languages** | Improve parsing and understanding of natural language data relevant to entrepreneurship.       | Enhance the accuracy of data interpretation and hypothesis testing, aiding strategic decision-making.         |
| **Probabilistic Programming System for Learning Models of Relational Databases** | Develop relational data models to support complex entrepreneurial decisions.                   | Facilitate robust data management and analysis, enabling better resource allocation and risk management.       |

for relational db:
[cdl database by amir](https://github.com/Data4DM/BayesSD/assets/30194633/3f0609f5-4c79-43c3-bc1f-0119570ec1d4)


---

## Reply from hyunjimoon on 2024-05-29T16:54:40Z

to answer charlie's question in [halfway persuasion on PC(BE).txt](https://github.com/Data4DM/BayesSD/files/15487855/halfway.persuasion.on.PC.BE.txt), i prepared three summaries of vikash's talk:

### [ted talk on AI That Understands the World, Using Probabilistic Programming](https://www.youtube.com/watch?v=8j2S7BRRWus&ab_channel=TEDxTalks)

summary: Probabilistic programs provide a new symbolic language for expressing uncertain knowledge about possible worlds and the processes to infer them. It's a new medium for knowledge representation. Examples demonstrate probabilistic programming outperforming machine learning systems on tasks such as perceiving 3D structure, reducing errors in perception (compared to Tesla's neural networks), cleaning millions of database records from US Medicare, and forecasting econometric time series. These probabilistic programs seem to understand the world more like humans do, in terms of symbolic representations.

answer to your questions on its novelty + success case:
examples of AI domain experts using probabilistic programming in areas like cancer clinical trials, salary surveys, genetic engineering experiments, and US Census data. In each case, the probabilistic programs learned were able to generate synthetic data very similar to the real data, indicating they captured key patterns and relationships ([here](https://streaklinks.com/B_CEXDHTk9HbOmvGNQl748kH/https%3A%2F%2Fyoutu.be%2F8j2S7BRRWus%3Fsi%3DtzgJ6hzFYzcS-U22%26t%3D526)).
symbolic aspect of probabilistic programming that sets it apart from neural networks. Symbolic representations, dating back to ancient times, have been crucial for increasing individual and collective human intelligence. Probabilistic programming combines this symbolic approach with probability to handle uncertainty ([here](https://streaklinks.com/B_CEXC-dnQHihWCyYQKaO0-G/https%3A%2F%2Fyoutu.be%2F8j2S7BRRWus%3Fsi%3D0c5aV3ZusiE5FAIu%26t%3D158)).

### Probabilistic Programming Tutorial Part [1](https://www.youtube.com/watch?v=n08kGjReS74&ab_channel=NeurosymbolicProgrammingforScience), [2](https://www.youtube.com/watch?v=O9kBeXn1MbU&ab_channel=NeurosymbolicProgrammingforScience)
Part I
1. An MIT view on probabilistic programming and intelligent systems
2. Example probabilistic programs in Gen
- Online learning of probabilistic program structure from structured data
- Real-time inference of 3D scenes from video

Part II
3. Inference (meta-)programming in Gen
4. Automating and scaling inference
5. OpenGen: from Gen.jl to PyGen and the GenTL C++ Template Library
6. Implications for large-scale AI systems



---

## Reply from hyunjimoon on 2024-06-08T13:31:15Z

## 🙋‍♀️ query
Q1. among three query language `bayesianQL`, `inferenceQL`, `genSQL` which technology can best support startup pivoting decision? Maturity, Feature, support from developers affect my use. i'd expect older technology would have lower stability but higher versatility and support from developers.

Q2. what is the family tree of the three language? if it is BQL to IQL to GSQL what "need" for feature prompted birth of the latter ones? how would this be relevant to startup pivoting decisions?

## 👨🏽‍🏫 predicted answer
below is short comparison of three languages from supply and demand's side (historic order)

#### Supply Side Table
| Feature | Form                                                                                                                                                                                                                         | Function                                                                                                                                                                                                                                           | Goal                                                                                                                                                                                                                        |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Bayesian Query Language (BQL)** | - Extends SQL with probabilistic constructs<br>- `in`: SQL-like queries with probabilistic extensions<br>- `out`: Probabilistic estimates, synthetic data, posterior distributions, relevance scores                                   | - `ESTIMATE`: Estimate probabilistic expressions<br>- `SIMULATE`: Generate synthetic data<br>- `PREDICT`: Compute posterior distributions<br>- `INFER`: Perform inference over missing data<br>- `RELEVANCE PROBABILITY`: Compute relevance scores | - Democratize Bayesian data analysis<br>- Enhance decision-making with probabilistic reasoning<br>- Provide scalable and flexible probabilistic analysis<br>- Improve data quality through imputation and anomaly detection                                         |
| **Inference Query Language (IQL)** | - Extends SQL to support probabilistic models<br>- Specific input/output format not detailed                                                                                                                                              | - Automated Bayesian inference<br>- Generate synthetic data<br>- Compute probabilities and mutual information<br>- Override learned models with custom probabilistic programs                                                                      | - Make Bayesian data analysis accessible to broad audiences<br>- Assist experts in auditing and improving data, models, and inferences                                                                                      |
| **Gen Structured Query Language (GenSQL)** | - Declarative extension of SQL<br>- `in`: SQL queries augmented with primitives for querying probabilistic models<br>- `out`: Probabilities, synthetic data                                                                            | - `GENERATE UNDER`: Generate synthetic data<br>- `PROBABILITY OF`: Compute probabilities<br>- `GENERATIVE JOIN`: Join tables with synthetic rows generated from a probabilistic model<br>- Model conditioning with `GIVEN`                          | - Enable complex Bayesian inference workflows in SQL<br>- Provide a declarative query language for interleaving SQL with generative modeling and inference                                                                  |

#### Demand Side Table

| Feature                                    | User                                                                                                                      | Query Usecase                                                                                                             | Maturity                                                                                                                                                                                                                  | Features                                                                                                                                                                                                                  | Support from Developers                                                                                                                                                                                                | Suitability for Startup Pivoting                                                                                                                                                                                               |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Bayesian Query Language (BQL)**          | - Database users and administrators<br>- Data scientists and analysts<br>- Business analysts<br>- Researchers and academics<br>- Developers and engineers | <br>ESTIMATE PROBABILITY OF FDA_approval = 'Yes' GIVEN cash_needed = 5000000 AND scenario = 3;<br>                        | - Oldest and most mature technology among the three<br>- Well-documented features<br>- Robust community support                                                                  | - Comprehensive support for probabilistic constructs<br>- Powerful tools for predictive analytics and uncertainty modeling                                                           | - Strong community and developer support<br>- Extensive documentation<br>- Wide range of use cases                                                                           | - High suitability due to its maturity, extensive features, and strong support<br>- Capabilities in handling complex probabilistic queries and generating synthetic data are essential for making informed pivot decisions in a startup environment |
| **Inference Query Language (IQL)**          | - Typical SQL database users aiming to apply Bayesian inference and probabilistic programming                              | <br>GENERATE synthetic_results FROM meditech_model GIVEN cash_needed = 5000000 AND scenario = 3;<br>                      | - Newer than BQL<br>- Less documented<br>- May not have as wide adoption or support                                                                                             | - Focuses on automating Bayesian inference<br>- Capable of handling complex probabilistic models<br>- Customizable to fit specific analysis needs                                  | - Limited compared to BQL<br>- Potential challenges in adoption and troubleshooting                                                                                          | - Powerful in automating Bayesian inference, but the lack of maturity and comprehensive documentation could be a hindrance for startups needing immediate, reliable support for pivot decisions                                  |
| **Gen Structured Query Language (GenSQL)** | - Users familiar with SQL who want to leverage probabilistic models in data analysis workflows                            | <br>SELECT * FROM meditech_scenarios GENERATIVE JOIN meditech_model GIVEN cash_needed = 5000000 AND scenario = 3;<br>     | - Similar to IQL in terms of maturity<br>- Newer and less mature compared to BQL<br>- Community support and documentation might be limited                                        | - Integrates seamlessly with SQL<br>- Declarative approach simplifies complex Bayesian modeling<br>- Effective for interleaving SQL operations with generative modeling            | - Less comprehensive compared to BQL<br>- Limited documentation and examples available for advanced use cases                                                              | - Effective for users familiar with SQL<br>- Maturity level might be a concern for startups needing stable and well-supported technologies                                                                                   |

[process](https://chatgpt.com/share/b94cf7d2-0b7d-47a8-ae03-ca81efee511a)

---

### Reply from hyunjimoon on 2024-06-08T14:47:36Z

GenSQL represents a significant advancement in probabilistic programming systems for querying generative models of database tables. Unlike InferenceSQL, which focuses on specific inference tasks, GenSQL provides a more comprehensive and flexible approach to integrating probabilistic models with database queries. The key motivation for creating GenSQL appears to be the need for a system that can seamlessly combine traditional SQL operations with complex probabilistic queries while maintaining a familiar syntax for database users. GenSQL achieves this through its SQL-like language extensions and the Abstract Model Interface, which allows it to work with various probabilistic programming languages. The system's formal semantics and performance optimizations demonstrate a commitment to both theoretical soundness and practical efficiency. By offering a unified framework for tasks such as conditional synthetic data generation, anomaly detection, and imputation, GenSQL aims to make advanced probabilistic modeling techniques more accessible to data scientists and analysts who are already comfortable with SQL.

| Feature | InferenceSQL | GenSQL |
|---------|--------------|--------|
| Query Language | SQL-like language for probabilistic queries | SQL extension with probabilistic constructs (e.g., PROBABILITY OF, GENERATE UNDER) |
| Model Integration | Works with specific probabilistic models | Supports various probabilistic programming languages via Abstract Model Interface (AMI) |
| Inference Capabilities | Focuses on specific inference tasks | Broader range of probabilistic operations (e.g., conditioning, sampling, density estimation) |
| Formal Semantics | Not explicitly defined in the paper | Provides measure-theoretic denotational semantics |
| Performance Optimizations | Not discussed in detail | Includes caching and independence-based query simplifications |

[GenSQL.pdf](https://github.com/user-attachments/files/16816249/GenSQL.pdf)
[🎞️filming inferenceSQL and genSQL comparison](https://github.com/Data4DM/BayesSD/assets/30194633/c911846a-12cc-41a8-a5f7-721a53a15bdf)


---

## Reply from hyunjimoon on 2024-06-12T14:53:31Z

casestudy building with prob.comp(matin and mattieu) on medtech company (medical device with >10times accurate imaging) that aims to find win win strategy that satisfies both ceo, vc, employee


---

## Reply from hyunjimoon on 2024-07-01T16:41:57Z

## 2. reverse engineering natural intelligence
![image](https://github.com/Data4DM/BayesSD/assets/30194633/9b3aa8a8-06e3-4112-ad48-362f1a296e40)

![image](https://github.com/Data4DM/BayesSD/assets/30194633/f2aa2935-6aef-4c6d-a95b-74b2aa9409f6)
![image](https://github.com/Data4DM/BayesSD/assets/30194633/8d1075e1-887b-4192-a76b-c84abec542c5)
![image](https://github.com/Data4DM/BayesSD/assets/30194633/78856c26-e279-4d30-bbdd-3355b7ada69e)
![image](https://github.com/Data4DM/BayesSD/assets/30194633/107e5989-c971-416f-ae0d-ef114abbd295)
![image](https://github.com/Data4DM/BayesSD/assets/30194633/ee27710f-2adb-4a62-9361-948ddc10f2b3)

--
based on josh's slide above, i synthesized as below using v model / marr's level
![image](https://github.com/user-attachments/assets/cc8845f8-0e7f-4d23-b9a4-83439ea31686)


---

### Reply from hyunjimoon on 2024-08-02T15:39:42Z

Abstract of [from word to world model](https://arxiv.org/pdf/2306.12672):
> How does language inform our downstream thinking? In particular, how do humans make meaning from language—and how can we leverage a theory of linguistic meaning to build machines that think in more human-like ways? In this paper, we propose rational meaning construction, a computational framework for language-informed thinking that combines neural models of language with probabilistic models for rational inference. We frame linguistic meaning as a context-sensitive mapping from natural language into a probabilistic language of thought (PLoT)—a general-purpose symbolic substrate for probabilistic, generative world modeling. Our architecture integrates two powerful computational tools that have not previously come together: we model thinking with probabilistic programs, an expressive representation for flexible commonsense reasoning; and we model meaning construction with large language models (LLMs), which support broad-coverage translation from natural language utterances to code expressions in a probabilistic programming language. We illustrate our framework in action through examples covering four core domains from cognitive science: probabilistic reasoning, logical and relational reasoning, visual and physical reasoning, and social reasoning about agents and their plans. In each, we show that LLMs can generate context-sensitive translations that capture pragmatically-appropriate linguistic meanings, while Bayesian inference with the generated programs supports coherent and robust commonsense reasoning. We extend our framework to integrate cognitively-motivated symbolic modules (physics simulators, graphics engines, and goal-directed planning algorithms) to provide a unified commonsense thinking interface from language. Finally, we explore how language can drive the construction of world models themselves. We hope this work will help to situate contemporary developments in LLMs within a broader cognitive picture of human language and intelligence, providing a roadmap towards AI systems that synthesize the insights of both modern and classical computational perspectives.

one synthesis with john horton's [automated social science](https://arxiv.org/pdf/2306.12672) for entrepreneurial decision making tool i'm building is automating scientific entrepreneurial learning for entrepreneurial decision making. 

> How can we integrate structural causal models and probabilistic reasoning on "general-purpose symbolic substrate for probabilistic, generative world modeling framework" to create a decision support tool for entrepreneurs that captures the complex interplay between idea, experiment, strategy (value chain vs architectural), operation (buy vs make), while accounting for market uncertainties and technological evolution?

1. It builds on John's work on automated social science using language models and structural causal models.

2. It extends the application of these models to a specific, high-stakes domain (entrepreneurial decision-making).

3. It incorporates the idea of translating natural language into a probabilistic language of thought, which could be used to model and reason about complex business strategies.

4. It suggests the potential for creating a tool that can adapt and learn from new data and market conditions, similar to how the models in John's paper can be used for prediction and planning follow-on experiments.

5. It addresses the challenge of capturing both the logical structure of business strategies and the probabilistic nature of market outcomes, which aligns with the unification of logical and statistical AI discussed in Domingos [paper](https://homes.cs.washington.edu/~pedrod/papers/cacm19.pdf).

This research question could lead to the development of a tool that not only helps entrepreneurs make better decisions but also advances our understanding of how language models can be used to reason about complex, real-world scenarios in a way that combines human-like intuition with rigorous causal reasoning.

---

## Reply from hyunjimoon on 2024-07-10T22:39:36Z

meeting with zane. 
3yr (prob.comp) - paper -> prototype
working with digital garage (investing (VC), real estate)

planning business is hard to quantify (adjustment from engineering to business focused)

1. has been trying to turn quantitive data -> qualitative data
2. fund raising (detailed model of how world viewing go to market strategy, risk)
3.communicating value of equity grants to (cruiting process)-> bayesian method (specify belief up front)

presenting (prior beliefs on latent values; ability to input)
looking at public filings (ipo), sec website (former) https://news.crunchbase.com/public/how-to-read-an-s1/
business views it own financial aspect (good company to be interested)
investor purchasing stock (belief)
early stage (building a model) - prevent a risk
will think about direct collaboration and follow up 

---

## Reply from hyunjimoon on 2024-08-24T22:43:10Z

### 3. posterior space sampling algorithms
different sampling algorithms that has implications for entrepreneurial learning ([claude optimal learning modes](https://claude.ai/chat/b10efacb-b51f-45e7-9be2-3b8e5208ccfa))

| Algorithm 1 (Fast, Higher Rejection)          | Algorithm 2 (Slow, Lower Rejection) | Context                                   | Explanation                                                                                                                                                                                                        |
| --------------------------------------------- | ----------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Random Walk Metropolis-Hastings               | Hamiltonian Monte Carlo             | High-dimensional continuous distributions | RW-MH proposes quickly but struggles in high dimensions, leading to high rejection. HMC uses gradient information for more efficient proposals, reducing rejection rates.                                          |
| Gibbs Sampling                                | Metropolis-within-Gibbs             | Highly correlated variables               | Gibbs sampling can move quickly through dimensions but may mix poorly with strong correlations. Metropolis-within-Gibbs can make larger moves, improving mixing at the cost of speed.                              |
| Independence Sampler                          | Adaptive Metropolis                 | Complex, multimodal distributions         | Independence sampler proposes from a fixed distribution quickly but may have high rejection in complex spaces. Adaptive Metropolis learns the target structure, reducing rejections but requires more computation. |
| Metropolis-Adjusted Langevin Algorithm (MALA) | Riemann Manifold HMC                | Distributions with varying scales         | MALA uses first-order gradient information for quick proposals but can be inefficient. RMHMC incorporates second-order geometry, moving more slowly but more effectively.                                          |

1. understand how the two attached paper frames lean vs scientific (felin-et-al.pdf) and practice vs theoretical (theory-baed entrepreneurial search.pdf) and explain to me by making tables that compare the two. consider practice based similar to lean and theoretical similar to scientific.
2. understand the mechanism behind how slower but lower rejection samplers (Hamiltonian Monte Carlo, Metropolis-within-Gibbs, Adaptive Metropolis, Riemann Manifold HMC) can perform better in high dimension, correlated, multimodal, varying scale situations. using this and your answer from 1, could you elicit helpful insights for entrepreneurs when they think (theory driven) might be more helpful than doer? i'm not saying scientific/thinker approach is always better.

| Aspect | Lean / Practice-based | Scientific / Theory-based |
|--------|----------------------|---------------------------|
| Core premise | Rapidly test ideas with customers | Develop and test theories about value creation |
| Primary focus | Customer feedback and validation | Contrarian beliefs and problem solving |
| View of rationality | Bounded rationality | Generative rationality |
| Information emphasis | Information asymmetry between entrepreneur and customer | Belief asymmetry and theory-dependent information |
| Learning approach | Learn directly from environment/customers | Theory-laden observation and learning |
| Search strategy | Global or distant search | Targeted, theory-guided search |
| Experimentation | Primarily through customer interactions (e.g., MVPs) | Various methods depending on the theory (may include customer feedback) |
| Pivoting | Based on customer feedback | Based on theory validation/invalidation |
| Valuation of expert opinion | Limited | Highly valued for resolving theory uncertainty |
| Stopping rule in search | Fixed cut-off based on static distribution | Dynamic, based on evolving beliefs about distribution |
| Handling of unexpected outcomes | May overlook high-value outliers | Can lead to continued search or theory revision |
| Approach to novelty | May struggle with radically new ideas | Better equipped to pursue novel, contrarian ideas |
| Risk of premature invalidation | Higher, due to early customer feedback | Lower, due to theory-guided experimentation |

---

### Reply from hyunjimoon on 2024-09-01T18:01:36Z

🧊 of optimization https://github.com/Data4DM/BayesSD/discussions/248

---

## Reply from hyunjimoon on 2024-09-02T22:50:25Z

@chasfine asked definitions of three apis/architecture of vikash (prob.comp) so I guessed below to get @mugamma's verification

<img width="150" alt="image" src="https://github.com/user-attachments/assets/c58000f1-d69f-48e3-be5c-96d50be28d4e">

tl;dr
`Modular learning from human-scale data` breaks down complex problems into smaller components, learning from datasets comparable to human experience while incorporating prior knowledge and allowing for incremental adaptation. e.g. structural decomposition of time series into trend, seasonal, event components.

`AI-human comparisons in comparable worlds`creates simulated environments where both AI systems and humans can be evaluated on equal footing, allowing for fair comparisons (shared world model).

`World modeling and decision making` creates computational models of the world using probabilistic programming to capture causal structures and uncertainties, which are then used for decision-making through inference and prediction.

---

### 1. Modular learning from human-scale data:
This refers to a learning approach that breaks down complex problems into smaller, manageable components (modules) and learns from data that is comparable in scale to what humans typically encounter. In the context of probabilistic programming, this involves:

a) Creating modular probabilistic programs that can be combined and reused across different tasks.
b) Learning from relatively small datasets, similar to the amount of information a human might process when learning a new skill.
c) Incorporating prior knowledge and structure into the learning process, much like humans do when they learn.
d) Allowing for incremental learning and adaptation as new data becomes available.

This approach contrasts with traditional machine learning methods that often require massive datasets and monolithic models.

### 2. AI-human comparisons in comparable worlds:
This concept involves creating simulated environments or "worlds" where both AI systems and humans can be evaluated on equal footing. In these comparable worlds:

a) We define tasks and scenarios that are meaningful for both AI and humans.
b) We use probabilistic programs to model these worlds, capturing the uncertainty and complexity that humans naturally deal with.
c) We compare the performance, decision-making processes, and learning curves of AI systems and humans.
d) We aim to understand the strengths and limitations of both AI and human cognition in these controlled environments.

This approach allows us to make fair comparisons and gain insights into how AI systems can be designed to complement human intelligence.

### 3. World modeling and decision making:
This refers to the process of creating computational models of the world (or specific domains within it) and using these models to make decisions. In the context of probabilistic programming:

a) World modeling involves creating probabilistic programs that capture the causal structure, uncertainties, and dynamics of a given environment or problem domain.
b) These world models can be updated based on new observations, much like how humans update their mental models of the world.
c) Decision making is then framed as inference within these probabilistic world models. This might involve:
   - Predicting the outcomes of different actions
   - Inferring hidden states of the world based on partial observations
   - Choosing actions that maximize expected utility under uncertainty
   
d) The probabilistic nature of these models allows for reasoning about uncertainty in both the world state and the outcomes of actions.

This approach to world modeling and decision making aims to capture the richness and uncertainty of real-world scenarios, allowing for more robust and adaptable AI systems that can reason in ways more similar to human cognition.

[cld.Leveraging Probabilistic AI for Entrepreneurial Decision-Making](https://claude.ai/chat/fb58109a-a549-40ae-867b-845561073801)

---

### Reply from hyunjimoon on 2024-09-04T14:04:56Z

Mathieu introduced five papers related to world modeling and decision making with abstract each:
[From Word Models to World Models- Translating from Natural Language to the Probabilistic Language of Thought.pdf](https://github.com/user-attachments/files/16871759/From.Word.Models.to.World.Models-.Translating.from.Natural.Language.to.the.Probabilistic.Language.of.Thought.pdf)
How does language inform our downstream thinking? In particular, how do humans make meaning from language—and how can we leverage a theory of linguistic meaning to build machines that think in more human-like ways? In this paper, we propose rational meaning construction, a computational framework for language-informed thinking that combines neural models of language with probabilistic models for rational inference. We frame linguistic meaning as a context-sensitive mapping from natural language into a probabilistic language of thought (PLoT)—a general-purpose symbolic substrate for probabilistic, generative world modeling. Our architecture integrates two powerful computational tools that have not previously come together: we model thinking with probabilistic programs, an expressive representation for flexible commonsense reasoning; and we model meaning construction with large language models (LLMs), which support broad-coverage translation from natural language utterances to code expressions in a probabilistic programming language. We illustrate our framework in action through examples covering four core domains from cognitive science: probabilistic reasoning, logical and relational reasoning, visual and physical reasoning, and social reasoning about agents and their plans. In each, we show that LLMs can generate context-sensitive translations that capture pragmatically-appropriate linguistic meanings, while Bayesian inference with the generated programs supports coherent and robust commonsense reasoning. We extend our framework to integrate cognitively-motivated symbolic modules (physics simulators, graphics engines, and goal-directed planning algorithms) to provide a unified commonsense thinking interface from language. Finally, we explore how language can drive the construction of world models themselves. We hope this work will help to situate contemporary developments in LLMs within a broader cognitive picture of human language and intelligence, providing a roadmap towards AI systems that synthesize the insights of both modern and classical computational perspectives.

[Building Machines that Learn and Think with People.pdf](https://github.com/user-attachments/files/16871754/Building.Machines.that.Learn.and.Think.with.People.pdf)
What do we want from machine intelligence? We envision machines that are not just tools for thought, but partners in thought: reasonable, insightful, knowledgeable, reliable, and trustworthy systems that think with us. Current artificial intelligence (AI) systems satisfy some of these criteria, some of the time. In this Perspective, we show how the science of collaborative cognition can be put to work to engineer systems that really can be called “thought partners,” systems built to meet our expectations and complement our limitations. We lay out several modes of collaborative thought in which humans and AI thought partners can engage and propose desiderata for human-compatible thought partnerships. Drawing on motifs from computational cognitive science, we motivate an alternative scaling path for the design of thought partners and ecosystems around their use through a Bayesian lens, whereby the partners we construct actively build and reason over models of the human and world.

[Online Bayesian Goal Inference for Boundedly-Rational Planning Agents.pdf](https://github.com/user-attachments/files/16871755/Online.Bayesian.Goal.Inference.for.Boundedly-Rational.Planning.Agents.pdf)
People routinely infer the goals of others by observing their actions over time. Remarkably, we can do so even when those actions lead to failure, enabling us to assist others when we detect that they might not achieve their goals. How might we endow machines with similar capabilities? Here we present an architecture capable of inferring an agent’s goals online from both optimal and non-optimal sequences of actions. Our architecture models agents as boundedly-rational planners that interleave search with execution by replanning, thereby accounting for sub-optimal behavior. These models are speciﬁed as probabilistic programs, allowing us to represent and perform efﬁcient Bayesian inference over an agent’s goals and internal planning processes. To perform such inference, we develop Sequential Inverse Plan Search (SIPS), a sequential Monte Carlo algorithm that exploits the online replanning assumption of these models, limiting computation by incrementally extending inferred plans as new actions are observed. We present experiments showing that this modeling and inference architecture outperforms Bayesian inverse reinforcement learning baselines, accurately inferring goals from both optimal and non-optimal trajectories involving failure and back-tracking, while generalizing across domains with compositional structure and sparse rewards.

[Pragmatic Instruction Following and Goal Assistance via Cooperative Language-Guided Inverse Planning.pdf](https://github.com/user-attachments/files/16871757/Pragmatic.Instruction.Following.and.Goal.Assistance.via.Cooperative.Language-Guided.Inverse.Planning.pdf)
People often give instructions whose meaning is ambiguous without further context, expecting that their actions or goals will disambiguate their intentions. How can we build assistive agents that follow such instructions in a flexible, context-sensitive manner? This paper introduces cooperative language-guided inverse plan search (CLIPS), a Bayesian agent architecture for pragmatic instruction following and goal assistance. Our agent assists a human by modeling them as a cooperative planner who communicates joint plans to the assistant, then performs multimodal Bayesian inference over the human’s goal from actions and language, using large language models (LLMs) to evaluate the likelihood of an instruction given a hypothesized plan. Given this posterior, our assistant acts to minimize expected goal achievement cost, enabling it to pragmatically follow ambiguous instructions and provide effective assistance even when uncertain about the goal. We evaluate these capabilities in two cooperative planning domains (Doors, Keys & Gems and VirtualHome), finding that CLIPS significantly outperforms GPT-4V, LLM-based literal instruction following and unimodal inverse planning in both accuracy and helpfulness, while closely matching the inferences and assistive judgments provided by human raters.
[Towards Guaranteed Safe AI- A Framework for Ensuring Robust and Reliable AI Systems.pdf](https://github.com/user-attachments/files/16871758/Towards.Guaranteed.Safe.AI-.A.Framework.for.Ensuring.Robust.and.Reliable.AI.Systems.pdf)
Ensuring that AI systems reliably and robustly avoid harmful or dangerous behaviours is a crucial challenge, especially for AI systems with a high degree of autonomy and general intelligence, or systems used in safety-critical contexts. In this position paper, we will introduce and define a family of approaches to AI safety, which we will refer to as guaranteed safe (GS) AI. The core feature of these approaches is that they aim to produce AI systems which are equipped with highassurance quantitative safety guarantees. This is achieved by the interplay of three core components: a world model (which provides a mathematical description of how the AI system affects the outside world in a way that appropriately handles both Bayesian and Knighting uncertainty), a safety specification (which is a mathematical description of what effects are acceptable), and a verifier (which provides an auditable proof certificate that the AI satisfies the safety specification relative to the world model). We outline a number of approaches for creating each of these three core components, describe the main technical challenges, and suggest a number of potential solutions to them. We also argue for the necessity of this approach to AI safety, and for the inadequacy of the main alternative approaches.

---

## Reply from hyunjimoon on 2024-09-10T15:15:56Z

#249 
Josh Tenenbaum's approach to unifying statistical and pragmatic linguistic meaning involves:
[2407 josh_llmunderstanding.txt](https://github.com/user-attachments/files/16947035/2407.josh_llmunderstanding.txt)

1. Using probabilistic programs as a framework for world modeling
2. Implementing a "rational meaning construction" approach where language understanding involves translating natural language into a probabilistic language of thought
3. Utilizing large language models (LLMs) to perform this translation, capturing both statistical patterns in language use and pragmatic, contextual interpretations
4. Integrating this translated language with structured world models that can perform probabilistic inference and reasoning
5. Allowing for the construction of "bespoke" world models that are context-specific and can be updated based on new linguistic input

---

## Reply from hyunjimoon on 2024-10-04T20:22:12Z

#250 

---

## Reply from hyunjimoon on 2024-10-04T20:43:12Z

how gensql is framed
https://news.mit.edu/2024/mit-researchers-introduce-generative-ai-databases-0708
MIT researchers introduce generative AI for databases
This new tool offers an easier way for people to analyze complex tabular data.
Adam Zewe | MIT News

Stacked squares in techy space
Caption:A new tool enables someone to perform complicated statistical analyses on tabular data using just a few keystrokes.
Credits:Image: MIT News; iStock
A new tool makes it easier for database users to perform complicated statistical analyses of tabular data without the need to know what is going on behind the scenes.

GenSQL, a generative AI system for databases, could help users make predictions, detect anomalies, guess missing values, fix errors, or generate synthetic data with just a few keystrokes.

For instance, if the system were used to analyze medical data from a patient who has always had high blood pressure, it could catch a blood pressure reading that is low for that particular patient but would otherwise be in the normal range.

GenSQL automatically integrates a tabular dataset and a generative probabilistic AI model, which can account for uncertainty and adjust their decision-making based on new data.

Moreover, GenSQL can be used to produce and analyze synthetic data that mimic the real data in a database. This could be especially useful in situations where sensitive data cannot be shared, such as patient health records, or when real data are sparse.

This new tool is built on top of SQL, a programming language for database creation and manipulation that was introduced in the late 1970s and is used by millions of developers worldwide.

“Historically, SQL taught the business world what a computer could do. They didn’t have to write custom programs, they just had to ask questions of a database in high-level language. We think that, when we move from just querying data to asking questions of models and data, we are going to need an analogous language that teaches people the coherent questions you can ask a computer that has a probabilistic model of the data,” says Vikash Mansinghka ’05, MEng ’09, PhD ’09, senior author of a [paper introducing GenSQL](https://dl.acm.org/doi/10.1145/3656409) and a principal research scientist and leader of the Probabilistic Computing Project in the MIT Department of Brain and Cognitive Sciences.

When the researchers compared GenSQL to popular, AI-based approaches for data analysis, they found that it was not only faster but also produced more accurate results. Importantly, the probabilistic models used by GenSQL are explainable, so users can read and edit them.

“Looking at the data and trying to find some meaningful patterns by just using some simple statistical rules might miss important interactions. You really want to capture the correlations and the dependencies of the variables, which can be quite complicated, in a model. With GenSQL, we want to enable a large set of users to query their data and their model without having to know all the details,” adds lead author Mathieu Huot, a research scientist in the Department of Brain and Cognitive Sciences and member of the Probabilistic Computing Project.

They are joined on the paper by Matin Ghavami and Alexander Lew, MIT graduate students; Cameron Freer, a research scientist; Ulrich Schaechtle and Zane Shelby of Digital Garage; Martin Rinard, an MIT professor in the Department of Electrical Engineering and Computer Science and member of the Computer Science and Artificial Intelligence Laboratory (CSAIL); and Feras Saad ’15, MEng ’16, PhD ’22, an assistant professor at Carnegie Mellon University. The research was recently presented at the ACM Conference on Programming Language Design and Implementation.

Combining models and databases

SQL, which stands for structured query language, is a programming language for storing and manipulating information in a database. In SQL, people can ask questions about data using keywords, such as by summing, filtering, or grouping database records.

However, querying a model can provide deeper insights, since models can capture what data imply for an individual. For instance, a female developer who wonders if she is underpaid is likely more interested in what salary data mean for her individually than in trends from database records.

The researchers noticed that SQL didn’t provide an effective way to incorporate probabilistic AI models, but at the same time, approaches that use probabilistic models to make inferences didn’t support complex database queries.

They built GenSQL to fill this gap, enabling someone to query both a dataset and a probabilistic model using a straightforward yet powerful formal programming language.

A GenSQL user uploads their data and probabilistic model, which the system automatically integrates. Then, she can run queries on data that also get input from the probabilistic model running behind the scenes. This not only enables more complex queries but can also provide more accurate answers.

For instance, a query in GenSQL might be something like, “How likely is it that a developer from Seattle knows the programming language Rust?” Just looking at a correlation between columns in a database might miss subtle dependencies. Incorporating a probabilistic model can capture more complex interactions.   

Plus, the probabilistic models GenSQL utilizes are auditable, so people can see which data the model uses for decision-making. In addition, these models provide measures of calibrated uncertainty along with each answer.

For instance, with this calibrated uncertainty, if one queries the model for predicted outcomes of different cancer treatments for a patient from a minority group that is underrepresented in the dataset, GenSQL would tell the user that it is uncertain, and how uncertain it is, rather than overconfidently advocating for the wrong treatment.

Faster and more accurate results

To evaluate GenSQL, the researchers compared their system to popular baseline methods that use neural networks. GenSQL was between 1.7 and 6.8 times faster than these approaches, executing most queries in a few milliseconds while providing more accurate results.

They also applied GenSQL in two case studies: one in which the system identified mislabeled clinical trial data and the other in which it generated accurate synthetic data that captured complex relationships in genomics.

Next, the researchers want to apply GenSQL more broadly to conduct largescale modeling of human populations. With GenSQL, they can generate synthetic data to draw inferences about things like health and salary while controlling what information is used in the analysis.

They also want to make GenSQL easier to use and more powerful by adding new optimizations and automation to the system. In the long run, the researchers want to enable users to make natural language queries in GenSQL. Their goal is to eventually develop a ChatGPT-like AI expert one could talk to about any database, which grounds its answers using GenSQL queries.

----
https://www.techbriefs.com/component/content/article/51167-meet-gensql-generative-ai-for-databases
A new tool makes it easier for database users to perform complicated statistical analyses of tabular data without the need to know what is going on behind the scenes.

GenSQL, a generative AI system for databases, could help users make predictions, detect anomalies, guess missing values, fix errors, or generate synthetic data with just a few keystrokes.

For instance, if the system were used to analyze medical data from a patient who has always had high blood pressure, it could catch a blood pressure reading that is low for that particular patient but would otherwise be in the normal range.

GenSQL automatically integrates a tabular dataset and a generative probabilistic AI model, which can account for uncertainty and adjust their decision-making based on new data.

Moreover, GenSQL can be used to produce and analyze synthetic data that mimic the real data in a database. This could be especially useful in situations where sensitive data cannot be shared, such as patient health records, or when real data are sparse.

This new tool is built on top of SQL, a programming language for database creation and manipulation that was introduced in the late 1970s and is used by millions of developers worldwide.

“Historically, SQL taught the business world what a computer could do. They didn’t have to write custom programs, they just had to ask questions of a database in high-level language. We think that, when we move from just querying data to asking questions of models and data, we are going to need an analogous language that teaches people the coherent questions you can ask a computer that has a probabilistic model of the data,” said Senior Author Vikash Mansinghka, Ph.D., Principal Research Scientist and leader of the Probabilistic Computing Project in the MIT Department of Brain and Cognitive Sciences.

When the researchers compared GenSQL to popular AI-based approaches for data analysis, they found that it was not only faster but also produced more accurate results. Importantly, the probabilistic models used by GenSQL are explainable, so users can read and edit them.

“Looking at the data and trying to find some meaningful patterns by just using some simple statistical rules might miss important interactions. You really want to capture the correlations and the dependencies of the variables, which can be quite complicated, in a model. With GenSQL, we want to enable a large set of users to query their data and their model without having to know all the details,” said Lead Author Mathieu Huot, Research Scientist in the Department of Brain and Cognitive Sciences and member of the Probabilistic Computing Project.

Here is an exclusive Tech Briefs interview, edited for length and clarity, with Huot.

Tech Briefs: What was the biggest technical challenge you faced while developing Gen SQL?

Huot: I think being able to compactly represent a whole range of problems you want to solve in a way that's going to be accessible — how do you not develop 20 different tools and sets of ideas that people can reuse. The point was to be concise and accessible to a large audience. So, how do you make that possible and unify all these different kind of questions — that was definitely a challenge.

Tech Briefs: Can you explain in simple terms how it works?

Huot: You usually have a model; if not, you can have one automatically synthesized for you, given some data. And then given the data — which is either what you train your model on or a different set; but the data of interest that you want to analyze and your model — you can type questions in this formal language. But now we also have some prototype language integration where you can just write in English and it would translate to the formal language. Then, your query is run in the formal language, and you get specialized answers, which can be tables, numbers, etc.

Tech Briefs: How did this work come about? What was the catalyst for the project?

Huot: We've had, in our team, a history of looking at data science and statistics. So, people were aware of the different challenges in applying existing tools to certain problems. Either it was too specialized, or the automation wasn't good, or the model needed too much expertise. So, there was a growing desire in the team to produce something more accessible.

Maybe having a hybrid team of some people being more interested in applications and others thinking about language design was the key to utilizing this opportunity to create something new that can solve a problem by being more accessible to data scientists.

Related Articles
[How Is Generative AI Transforming Engineering?](https://www.techbriefs.com/component/content/article/50058-how-is-generative-ai-transforming-engineering)

[Tech Focus: Leveraging Generative AI for Industrial Environment](https://www.techbriefs.com/component/content/article/50706-tech-focus-leveraging-generative-ai-for-industrial-environment)

Tech Briefs: What are your next steps? Do you have plans for further research, work, etc. to accomplish these goals?

Huot: There are several technical challenges, which I won't go into the details of. But one challenge is how to scale these things up: how to build a better backend system that can create richer and faster models to query. That's one part.

Another is making it more accessible, for example, through language modeling. So, you speak or write in English, then we can convert it to a formal query. But in the process, sometimes you find ambiguities in the language. One example is, ‘Show me all the people, who are Democratic voters who voted one way in the U.S. in a certain year. But those voters might be registered in that party or just identify as being in that party. So, it can be ambiguous, depending on the dataset. And you may not know that up front.

Here, the system could show you two queries depending on which one you are actually asking for.

On a larger scale, we have some people looking at how to apply these tools to build models for prostate cancer data. Here the challenge is that many experiments are on a small scale, like a single hospital and they can't really share the data. So, if you train a model on that, it's not really telling you enough to make many predictions. But there are a lot of these experiments on the internet that are freely accessible. They're usually not super clean or they have different conventions; you can't really train a model by magic on all of these models and then solve all your problems.

But, these tools that we develop can help. We’re pushing to make the tools able to construct a model that's going to look at, for example, two different clinical trials where the roles don't exactly match. One may have people grouped by age, another by category, how do people get assigned to a group, they might have different labels. So, automating data harmonization.

Tech Briefs: Do you have any advice for researchers or engineers aiming to bring their ideas to fruition, broadly speaking?

Huot: I think it's great — if you want to create something to apply to a problem — to clearly know what the problem is. It may sound extremely simple, but it's really hard in research.

You have to spend, for example, six months in the mud to really get to know the problem and what people actually want instead of what you think they want. That can be really hard to do. Usually, it's going take way longer to solve that problem than you might think; creating these tools takes years. Start from the bottom, be humble.

---

[Discussion link](https://github.com/Data4DM/BayesSD/discussions/224)


[[tom_griffith]]