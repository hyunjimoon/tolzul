---
이름: Addressing degeneracy
출생: 2022-01-21
언어교환:
  - bayesian
  - blog
  - stan
---

Loosely speaking, the followings are all related

- Fisher information matrix (FIM) is not positive deﬁnite
- nonidentiﬁable/singularities of a statistical model
- algebraically: map from a parameter (theta) to a statistical model (p(.|theta)) is not one-to-one
- geometrically (sometimes called degeneracy): not a concentrated ball-shape inverse image of outcomes
- code-based degeneracy models can be viewed [here](https://betanalpha.github.io/assets/case_studies/identifiability.html#5_Don't_Do_Me_Like_That).

Practical solutions are the combination of  
S1. add more data  
S2. reparameterize to ensure independence  
S3. tighten the prior

For S2, naturally arising question is: how does the reparameterization affect the metric? Equation in Sec.3.2. of [this](https://arxiv.org/pdf/1910.09407.pdf) paper shows one-to-one equivalence between incomplete reparameterizations and the choice of metric. Given the equivalence, strategies are set: if you are designing an inference engine from scratch maybe you can interact with metric (e.g. algebraically etc) but in most cases focus more on an easy fix (S1~3) after fixing the tricky metric which leads to equivalent results in most cases (hence, incomplete reparameterizations).

"Geometric algorithm is implemented with coordinates, components, and probability densities. Typically, however, only the target probability density is exposed to the modeler. Conditional probability density functions on the tangent or cotangent bundle, or components of the metric that define those conditional densities, are set to default values not exposed to the user or exposed but significantly limited in flexibility. For example, the default configuration of Stan forces a metric with constant, diagonal components."

For S1, I don't know the specific mechanism but would be interested to understand.

As there are many combinations, "principled workflow" which is a guide for the recommended action (S1~3) for a given diagnosis is active research.

For models with typical degeneracy, a combination of the above solutions are "modularized" e.g. normal hierarchical models can be resolved using adaptive parameterization where different parameterization (centered vs noncentered) is dispatched according to the susceptibility of a parameter w.r.t. outcome. Susceptibility is characterized by the calibration coefficient. This approach is elaborated in [this](https://betanalpha.github.io/assets/case_studies/hierarchical_modeling.html) Betancourt’s writing on hierarchical modeling.
