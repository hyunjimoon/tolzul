---
tags:
  - vikash
---
 
## 🗄️vikash1. Four Reasonings and Six Steps (REVED)

| | Probabilistic Reasoning | Relational Reasoning | Social Reasoning |
|---------------------------|------------------------|----------------------|-------------------|
| Knowledge about the world | The winner of a match is whichever team is stronger. | A grandfather is the father of one's parent. | Depending on whether they have a bike, people can bike or walk. |
| Generative world models | (define won-against (team-1 team-2) (> (team-strength team-1) (team-strength team-2))) | (define grandfather-of? (name_a name_b) (exists (lambda (x) (and (father-of? name_a x) (parent-of? x name_b))))) | (define actions (agent-id) (if (has_bike? agent-id) (list 'is_walking 'is_biking) (list 'is_walking))) |
| Observations about the world | John and Mary faced off against Tom and Sue and won. | Charlie is Dana's grandfather. | Alex loves sushi but hates pizza; and he brought his bike to work today. |
| Condition statements | (condition (won-against '(john mary) '(tom sue))) | (condition (grandfather-of? 'charlie 'dana)) | (condition (and (loves? 'alex 'sushi) (hates? 'alex 'pizza) (has-bike? 'alex))) |
| Questions about the world | Is Mary stronger than Tom? | Which of Charlie's kids is Dana's parent? | What do you think Alex will do? |
| Query statements | (query (> (strength 'mary) (strength 'tom))) | (query (filter-tree (lambda (x) (and (child-of? x 'charlie) (parent-of? x 'dana))))) | (query (get_actions 'alex)) |
## 🗄️vikash2. rule vs similarity 

| Aspect | Rule-based / Bayesian | Similarity-based / Evolutionary |
|--------|------------------------|----------------------------------|
| Focus | Optimization, precise solutions | Adaptation, flexible solutions |
| Decision-making | Careful analysis, planning | Experimentation, action-oriented |
| Uncertainty handling | Probabilistic inference | Trial and error, learning from experience |
| Generalization | Narrow, specific | Broad, flexible |
| Learning process | Convergence to optimal solution | Exploration of multiple possibilities |
| Strength in entrepreneurship | Detailed analysis, risk assessment | Quick adaptation, innovation in dynamic environments |
| Example algorithm | MIN algorithm | Weak Bayes |
| Computational approach | Bayesian inference | Evolutionary algorithms |


## 🗄️vikash3. bayes rule (prior, likelihood, posterior)+ (example, hypothesis )

eight concepts on hypothesis, observation/example of concept, prior of hypothesis, likelihood of observations given hypothesis, posterior, size principle of likelihood (smaller hypothesis receives greater likelihood, more so as n increases), choice principle (natural over logic) of principle, hypothesis averaging for new observation (averaging prediction over all hypothesis weighted by posterior)

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

## 🗄️vikash3. marr's three level

| Level | Name                         | Description                                                                                                                     |
| ----- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Computational theory         | - What are the inputs and outputs to the computation?<br>- What is its goal?<br>- What is the logic by which it is carried out? |
| 2     | Representation and algorithm | - How is information represented?<br>- How is information processed to achieve the computational goal?                          |
| 3     | Hardware implementation      | - How is the computation realized in physical or biological hardware?                                                           |

## 🗄️vikash4. seminar modules

|     | Name                                         | paper (vikash pick)           | notes                                                            |
| --- | -------------------------------------------- | ----------------------------- | ---------------------------------------------------------------- |
| 1   |                                              |                               | [[module1 scaling behavior of intelligence vs machine learning]] |
| 2   |                                              |                               | [[module2]]                                                      |
| 3   | ![[Vikash Seminar Modeling Inference 1.txt]] |                               | [[module3-modeling and inference]]                               |
| 4   | ![[vikash seminar_alex_automate_math.txt]]   |                               | [[Space/Sources/Lab/🐅CompBayes/💻Mansinghka25_9.s/module4]]                                                      |
| 5   |                                              |                               | [[module5 automating math]]                                      |
| 6   | ![[vikash seminar learning probprog.txt]]    |                               | [[module6]]                                                      |
| 7   | language                                     | [[📜syn_sem_ctrl_llm_smc]]    |                                                                  |
|     | image perception as inverse graph            | [[📜vikash13_appx_bayes_img]] |                                                                  |


