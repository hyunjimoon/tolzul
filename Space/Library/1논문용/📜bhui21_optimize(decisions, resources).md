---
collection:
  - "[[Space/Lab/Papers]]"
author_ids:
field:
  - 🐙ops
  - 👾cog
year: 2021
created: 2024-11-05
---

![[Pasted image 20250409071201.png|300]]
abstract: Across many domains of decision making, people seem both rational and irrational. We review recent work that aims to reconcile these apparently contradictory views by modeling human decisions as optimal under a set of cognitive resource constraints. This “resource-rational” analysis connects psychology and neuroscience to ideas from engineering, economics, and machine learning. Here, we focus on an information-theoretic formalization of cognitive resources, highlighting its implications for understanding three important and widespread phenomena: reference dependence, stochastic choice, and perseveration. While these phenomena have traditionally been viewed as irrational biases or errors, we suggest that they may arise from a rational solution to the problem of resource-limited decision making.

[📚contents cld](https://claude.ai/chat/f25601fe-e04c-41a7-869a-09c40c76d57c)

mentioned [[📜ullman20_conceptualdev]] as great connection to [[josh_tenanbaum]], [[📜Tenenbaum11_growmind]]

## 🗄️1: Table of Contents (Question-Answer Format)

|Section/Subsection|Question|Answer|🧱Literature Brick|
|---|---|---|---|
|Introduction|How can we reconcile human rationality and irrationality?|🧍‍♀️ Resource-rational analysis views human decisions as optimal under cognitive resource constraints, explaining both adaptive behavior and systematic limitations. This approach bridges psychology and neuroscience with concepts from engineering, economics, and information theory.|• Bounded rationality (Simon 1956)<br>• Ecological rationality (Todd & Gigerenzer 2003)<br>• Computational rationality (Gershman et al. 2015)|
|Formalizing Efficiency|How can we mathematically model cognitive limitations?|🧭 Cognition can be modeled as information transmission through a capacity-limited channel where efficiency emerges when representation fidelity is optimized given constraints. Three key objectives are: maximizing mutual information, minimizing squared loss, and maximizing reward, all subject to information capacity constraints.|• Information theory (Cover & Thomas)<br>• Rate-distortion theory<br>• Capacity-limited decision making (Sims 2003)|
|Reference Dependence|Why do our judgments depend on context?|🌏 Efficient coding requires neural resources to adapt to environmental statistics, making representations more sensitive to frequent values. The optimal representation with fixed output range follows the cumulative distribution function (CDF) of the stimulus distribution, explaining context effects in valuation and choice.|• Efficient coding (Barlow 1961)<br>• Decision by sampling (Stewart et al. 2006)<br>• Range and rank normalization (Parducci 1995)|
|Stochastic Choice|Why are our choices sometimes inconsistent?|🧍‍♀️ Stochasticity reflects an optimal trade-off between representational complexity and reward. When information is costly, choices become probabilistic, following a softmax distribution with bias toward frequently chosen actions, optimally balancing precision and cognitive cost.|• Softmax/multinomial logit models<br>• Sequential sampling models<br>• Information-theoretic decision theory (Tishby & Polani 2011)|
|Perseveration|Why do we tend to repeat previous choices?|🧍‍♀️ Under limited information capacity, choices become biased toward frequently selected actions across states. In dynamic settings, this manifests as perseveration—an adaptive behavior that optimizes the trade-off between exploring new information and exploiting existing knowledge.|• Dynamic rational inattention (Steiner et al. 2017)<br>• State abstraction in reinforcement learning<br>• Noisy deliberation models|
|Conclusions|What are the broader implications of resource rationality?|🗺️ Resource-rational analysis provides a unifying framework for understanding both rational and seemingly irrational behaviors. Rather than viewing biases as strange defects, they can be understood as sensible adaptations to cognitive constraints—connecting judgment and decision-making with other core cognitive functions.|• Information-theoretic cognitive science<br>• Normative approaches to cognition<br>• Rational analysis tradition|

## 🗄️2: Comparison with Existing Theories

|Aspect|Traditional Rational Choice|Heuristics & Biases|Ecological Rationality|Resource Rationality|
|---|---|---|---|---|
|**Core Assumption**|Humans maximize utility with perfect information processing|Human cognition is fundamentally flawed and error-prone|Cognition is adapted to specific environmental structures|Cognition optimally balances accuracy and computational costs|
|**View of "Errors"**|Deviations from normative standards indicate irrationality|Evidence of fundamental cognitive limitations|Adaptive responses to environmental regularities|Rational adaptations to resource constraints|
|**Theoretical Status**|Normative benchmark for decision-making|Descriptive catalog of deviations from rationality|Descriptive account of environment-mind fit|Integration of normative and descriptive approaches|
|**Explanation of Context Effects**|Treated as inconsistencies or preference reversals|Framing effects and reference-dependent preferences|Adaptations to statistical structures in environment|Efficient coding of information given capacity constraints|
|**View of Stochasticity**|Explained by random utility or unmodeled factors|Result of noise or processing errors|Adaptive exploration strategy|Optimal balance between precision and information costs|
|**Mathematical Foundation**|Utility maximization|Not formally unified|Adaptation algorithms|Information theory and constrained optimization|
|**Predictions for Interventions**|Removing biases improves decisions|Debiasing techniques needed to overcome limitations|Restructuring environment more effective than changing mind|Trade-offs are fundamental; interventions should target resource allocation|

## 🗄️3: Practical Implications

|Domain|Implication|Example Application|
|---|---|---|
|**Behavioral Economics**|Context effects in valuation are rational adaptations to information constraints|Redesigning price displays to account for reference-dependent perception, helping consumers make more consistent judgments|
|**Decision Support Systems**|Tools should optimize the allocation of limited cognitive resources|Medical diagnosis systems that highlight the most informative features while filtering less relevant information based on prevalence statistics|
|**User Interface Design**|Interfaces should adapt to users' limited information processing|Adaptive menu systems that emphasize frequently used options while making rarely used options progressively harder to access|
|**Educational Technology**|Learning systems should account for efficient coding of information|Personalized learning platforms that adjust difficulty based on the statistics of recently encountered problems to maximize information gain|
|**Artificial Intelligence**|AI systems can be designed with human-like resource constraints|Developing more human-like AI by incorporating information costs and context-dependent representations into decision algorithms|
|**Clinical Applications**|Some pathologies may reflect dysfunctional resource allocation|Therapeutic approaches for conditions like OCD or addiction that target the balance between exploration and exploitation|
|**Economic Policy**|Market interventions should account for information processing constraints|Financial disclosure regulations that prioritize making the most relevant information salient rather than providing exhaustive details|
