---
collection:
  - "[[Space/Lab/Papers]]"
author_ids:
field:
  - 🐢inv
year: 2020
created: 2025-04-09
---

![[Pasted image 20250409070824.png|300]]
## 🗄️1: Table of Contents (Question-Answer Format)

|Section/Subsection|Question|Answer|🧱Literature Brick|
|---|---|---|---|
|1. Introduction|What is the central cognitive task of early childhood?|🧍‍♀️ Building a model of the world is the central cognitive task of early childhood. 🧭 Computational approaches to cognitive development aim to build models of this task and of children's minds as they solve it.|• Bayesian cognitive models showing humans can approximate optimal inference<br>• Hierarchical Bayesian models for learning abstract knowledge|
|2. Model Building as Bayesian Inference|How can Bayesian inference frame model building?|🗺️ Bayesian inference provides the mathematics linking models of the world to evidence that supports them, with posterior probability being determined by both prior probability and likelihood of evidence. 🌏 Hierarchical Bayesian models extend this to nested inferences, capturing abstract knowledge that organizes domains.|• Hierarchical Bayesian models (HBMs)<br>• Bayesian overhypothesis learning<br>• Dirichlet-multinomial models<br>• Graph grammars|
|3. Probabilistic Generative Programs|What representations capture people's mental models?|🧭 Probabilistic generative programs combine abstract causal knowledge with simulation-based reasoning, providing a universal language for representing models. 🧍‍♀️ These programs can be used for prediction, inference, and generalization in domains like intuitive physics and psychology.|• Probabilistic programming<br>• Mental simulation<br>• Game engine models of intuitive physics<br>• Planning models of intuitive psychology|
|4. Core Knowledge as Start-up Software|What initial knowledge enables model building?|🌏 Core knowledge constitutes a start-up library of domain-specific generative programs built by evolution, providing abstract expectations about objects, agents, space, and time. 🧭 Core principles like solidity and permanence can be implemented as constraints in probabilistic simulators.|• Core knowledge theory<br>• Minimal nativism<br>• Domain-specific principles<br>• Game physics engine models|
|5. Child as Scientist, Child as Program Learner|How do children learn beyond core knowledge?|🧍‍♀️ Children build intuitive theories through resource-rational hierarchical Bayesian inference over generative programs. 🧭 This search can be understood as goal-directed programming or "hacking" - constructing or modifying programs to better explain observations.|• Theory theory<br>• Stochastic search algorithms<br>• Program synthesis<br>• Resource-rational approach|
|6. From Intuitive Theories to Scientific Theories|Why is science hard if cognitive development is like science?|🧭 The same cognitive processes operate in both domains but face different challenges: Scientific theories address domains outside everyday experience where evolution-provided inductive biases don't apply, requiring cultural transmission of conceptual tools. 🌏 Scientific theories often rely on intuitive theories as initial scaffolding.|• Dynamics of scientific theory change<br>• Cultural evolution of scientific concepts<br>• Relationship between informal and formal theories|

## 🗄️2: Comparison with Existing Theories

|Aspect|Traditional Nativism|Traditional Empiricism|Resource-Rational Bayesian Program Learning|
|---|---|---|---|
|**Initial Knowledge**|Extensive domain-specific knowledge innately specified|Minimal general-purpose learning mechanisms|Minimal but structured domain-specific generative programs as "start-up software"|
|**Learning Mechanism**|Parameter setting within fixed structures|General-purpose association or reinforcement learning|Hierarchical Bayesian inference over generative programs|
|**Knowledge Representation**|Rule-based systems or modular processors|Connectionist networks or statistical associations|Probabilistic generative programs that can simulate and predict|
|**Knowledge Development**|Maturation of innate modules with limited genuine conceptual change|Bottom-up accumulation of associations, with conceptual change emerging from statistical learning|Iterative model building through theory search, with genuinely new concepts constructed through program learning|
|**Explanation for Early Competence**|Direct expression of innate knowledge|Fast statistical learning from rich environmental input|Core knowledge as evolution-provided generative models|
|**Explanation for Later Development**|Limited account beyond maturation|Gradual accumulation without clear mechanism for theory formation|Goal-directed search through program space guided by Bayesian inference|
|**View of Children's Learning**|Passive unfolding of innate potential|Passive accumulation of statistical patterns|Active model-building through theory search and "hacking"|
|**Relationship to Evolution**|Innate modules directly selected for|Selection for general learning mechanisms only|Selection for useful inductive biases and generative models in common domains|

## 🗄️3: Practical Implications

|Domain|Implication|Example Application|
|---|---|---|
|**Cognitive Science**|Provides computational precision to intuitive theories and theory change|Modeling specific conceptual developments like false belief understanding or intuitive physics using hierarchical Bayesian inference over programs|
|**Artificial Intelligence**|Suggests architecture for human-like learning systems|Building AI systems with core knowledge primitives and program induction capabilities for more human-like learning from minimal examples|
|**Education**|Suggests ways to scaffold learning by leveraging existing mental models|Designing curricula that build on children's intuitive theories rather than starting from formal scientific definitions|
|**Developmental Robotics**|Provides framework for embodied learning systems|Creating robots with built-in physics and psychology engines that can learn through interaction|
|**Developmental Disorders**|Offers computational perspective on atypical development|Modeling autism or ADHD as differences in prior distributions or search algorithms over program space|
|**Human-Computer Interaction**|Informs design of interfaces aligned with human mental models|Creating visualizations that map to intuitive physics or psychology representations|
|**Cognitive Architecture**|Unifies perception, action, and reasoning through generative models|Implementing systems that integrate simulation-based reasoning with Bayesian inference|

## Key Visual Elements

### 🖼️1: Need-Solution Mapping

The **Problem (💜)** in cognitive development is understanding how children build rich, abstract, and causal models of the world from limited experience. Traditional approaches either assume too much innate knowledge (classical nativism) or too little structure to explain rapid learning (classical empiricism).

The **Solution (💚)** is hierarchical Bayesian inference over probabilistic generative programs. This framework explains how children can start with core knowledge "start-up software" built by evolution and then search through program space to construct increasingly sophisticated models, guided by both structured prior knowledge and evidence from experience.

### 🖼️2: Methodology Visualization

The framework balances several key **Tradeoffs (🔴)** in modeling cognitive development:

- **Nativism vs. Empiricism**: Evolution provides minimal domain-specific generative programs as core knowledge, while learning mechanisms construct new theories through program induction.
    
- **Ideal vs. Resource-Rational**: The ideal computational-level theory (hierarchical Bayesian inference) is approximated by resource-bounded algorithms like stochastic search or goal-directed programming.
    
- **Simulation vs. Recognition**: Generative programs support both forward simulation (prediction) and inverse inference (learning from observation), allowing mental models to be both used and updated.
    
- **Domain-General vs. Domain-Specific**: Domain-general learning mechanisms operate over domain-specific representations, with different core knowledge systems providing distinct starting points for learning in different domains.
    

This integrated framework connects the "child as scientist" metaphor with concrete computational mechanisms, showing how children's intuitive theories can be understood as probabilistic programs discovered through a form of "hacking" - active, goal-directed programming that builds on existing mental software.