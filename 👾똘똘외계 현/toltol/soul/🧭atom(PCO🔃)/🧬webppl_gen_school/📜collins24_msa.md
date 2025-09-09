---
tags:
  - josh
---

![[📜collins24_msa 2025-04-13-6]]
using [[qa🗄️3🖼️2]], [cld](https://claude.ai/chat/e0672b42-c330-41b4-b89a-243326c6a859)
## 🗄️1: Table of Contents (Question-Answer Format)

| Section/Subsection                          | Question                                                                                      | Answer                                                                                                                                                                                                                                                                                                                                                                            | 🧱Literature Brick                                                                                                                                                                                                 |
| ------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Introduction                                | How do people reason flexibly across diverse domains despite the Frame Problem?               | 🧍‍♀️ People use a combination of 🧭 distributed and structured symbolic knowledge to construct 🗺️ bespoke mental models tailored to novel situations. This "Model Synthesis Architecture" (MSA) reconciles mental model theories with the Frame Problem by using distributional knowledge to identify relevant variables.                                                       | • Craik (1943), Minsky (1974), Johnson-Laird (1980) on mental models<br>• Dennett (1978), Fodor (2000) on the Frame Problem<br>• Brooke-Wilson (2023) on normatively rational reasoning                            |
| Model Synthesis Architecture                | How does the proposed MSA work computationally?                                               | 🧍‍♀️ People first use a 🧭 learned relevance model to identify what aspects of background belief are relevant to a task, then 🗺️ construct ad-hoc symbolic mental models supporting normatively rational reasoning. The implementation uses large language models (LLMs) for relevance determination and probabilistic programming languages (PPLs) for symbolic models.        | • Dubey et al. (2024), Lewis et al. (2020) on distributional models<br>• Cusumano-Towner et al. (2019), Goodman et al. (2014) on PPLs<br>• Vafa et al. (2024), Zhu & Griffiths (2024) on LLM limitations           |
| Related Work                                | How does MSA relate to prior approaches to the Frame Problem?                                 | MSA extends prior work by: (1) addressing not just whether small models can approximate reasoning in larger models, but 🧭 how we arrive at these small models; (2) generalizing LLM model synthesis to open-ended settings with arbitrary inputs; (3) applying hybrid approaches to the Frame Problem specifically.                                                              | • Icard & Goodman (2015), Ho et al. (2022) on small model approximations<br>• Li et al. (2024), Castro et al. (2025) on LLM model discovery<br>• Wong et al. (2023), Zhang et al. (2023) on hybrid language models |
| Implementation                              | How is the MSA computationally implemented?                                                   | The MSA implementation uses: (1) LLMs to parse natural language inputs into probabilistic program expressions; (2) LLMs to propose relevant background variables and relations in natural language; (3) LLMs to create dependency graphs; (4) LLMs to synthesize formal probabilistic programs; (5) semantic validity checks; and (6) inference algorithms to compute posteriors. | • WebPPL as the probabilistic programming language<br>• Llama-3.1-70B as the base LLM<br>• Few-shot prompting with hand-coded examples<br>• Rejection sampling for inference                                       |
| Model Olympics Domain                       | What experimental domain tests the MSA's ability to solve the Frame Problem?                  | The 🌏 "Model Olympics" domain consists of vignettes about three sports (tug-of-war, canoe-racing, biathlon) with distinct causal structures and variables. It requires: (1) reasoning about multiple causal structures; (2) filling in gaps with background knowledge; and (3) updating beliefs from novel information in language.                                              | • Goodman et al. (2014), Gerstenberg & Goodman (2012) on tug-of-war<br>• Multi-sample judgment paradigm from Gerstenberg et al.<br>• 7 vignette templates × 3 sports = 21 vignettes                                |
| Experiment 1: Detailed Background           | How well does MSA capture human probabilistic judgments with detailed background information? | The MSA synthesizes probabilistic models that correlate as well with human judgments as hand-crafted models, approaching the estimated noise ceiling from human-human correlations. MSA also outperforms LLM-only baselines in distributional similarity measures.                                                                                                                | • 78 human subjects on Prolific<br>• Multi-click judgment interface<br>• Comparisons to gold models and LLM baselines<br>• R² and Wasserstein distance metrics                                                     |
| Experiment 2: Underspecified Background     | How well does MSA perform with underspecified background information?                         | MSA maintains performance even with limited background information, demonstrating ability to retrieve relevant details and fill in likely causal dependencies. This captures a core aspect of the Frame Problem involved in everyday reasoning.                                                                                                                                   | • 80 human subjects on Prolific<br>• Same methodology as Experiment 1<br>• Focus on background knowledge retrieval                                                                                                 |
| Experiment 3: Participant-Generated Details | Can MSA handle arbitrary, open-world evidence in natural language?                            | In a preliminary study, MSA successfully synthesized probabilistic models incorporating a wide range of arbitrary evidence from human-generated "sports commentaries," showing promising performance on open-world reasoning.                                                                                                                                                     | • 20 human subjects eliciting commentaries<br>• 20 additional subjects providing judgments<br>• 9 extended vignettes<br>• Example commentaries about injuries, experience levels, etc.                             |

## 🗄️2: Comparison with Existing Theories

|Aspect|Pure Language Models|Hand-Crafted Probabilistic Models|Model Synthesis Architecture|
|---|---|---|---|
|**Core Approach**|Use large neural networks trained on text to directly answer queries through implicit world knowledge|Use hand-designed probabilistic programs with explicit variables and dependencies|Use language models to identify relevant variables and construct ad-hoc probabilistic programs|
|**Knowledge Representation**|Distributed, implicit knowledge in neural network weights|Explicit symbolic variables and probabilistic relationships|Hybrid: uses distributed knowledge to construct explicit symbolic representations|
|**Handling Novel Situations**|Strong at recognizing patterns from training data, weaker for novel compositions|Accurate for situations specifically modeled, but requires manual engineering for each domain|Can dynamically construct appropriate models for novel situations by drawing on distributional knowledge|
|**Reasoning Coherence**|May lack internal coherence and make contradictory judgments|Provides coherent probabilistic reasoning within modeled domain|Maintains probabilistic coherence through explicit symbolic models while leveraging broad knowledge|
|**Explanation of Human Cognition**|Suggests humans reason through pattern recognition and association|Suggests humans reason with explicit symbolic mental models|Suggests humans use both distributional knowledge and symbolic models, resolving the Frame Problem|
|**Frame Problem Solution**|Sidesteps by using associations without explicit variable selection|Doesn't address how humans determine relevant variables|Explicitly addresses by using distributional knowledge to determine relevant variables|
|**Response to Arbitrary Evidence**|Can incorporate arbitrary linguistic input but may lack coherence|Difficult to update with arbitrary linguistic input unless pre-engineered|Can incorporate arbitrary linguistic input with probabilistic coherence|

## 🗄️3: Practical Implications

|Domain|Implication|Example Application|
|---|---|---|
|**Cognitive Science**|Provides a computational account of how humans solve the Frame Problem|Models explaining how people flexibly reason about novel situations while maintaining coherence|
|**Artificial Intelligence**|Suggests a hybrid architecture combining strengths of neural and symbolic approaches|AI systems that maintain coherence when reasoning about novel situations while drawing on broad knowledge|
|**Education**|Offers insights into how humans transfer knowledge across domains|Educational tools that help students construct appropriate mental models for new domains|
|**Human-AI Collaboration**|Enables more interpretable AI systems that reason in ways humans understand|Collaborative systems where humans can inspect and refine AI-constructed models|
|**Healthcare Decision Support**|Models how clinicians draw on relevant background knowledge for diagnosis|Clinical decision support systems that construct case-specific probabilistic models|
|**Natural Language Understanding**|Provides mechanisms for grounding language in structured world models|Systems that translate natural language into probabilistic programs for reasoning|
|**Robotics and Planning**|Addresses how to reason with limited computational resources in complex environments|Robots that construct situation-specific models rather than reasoning with complete world models|

## Additional Key Resources

### 🗄️💭 Theoretical Foundations

- The paper builds on longstanding theories of mental models (Craik, Johnson-Laird) while addressing the Frame Problem raised by philosophers like Dennett and Fodor
- Positions mental model construction as a solution to the apparent intractability of reasoning with complete world knowledge
- Connects to debates about hybrid symbolic-neural architectures and bounded rationality

### 🗄️📐 Model Components and Architecture

- Sequential pipeline for model synthesis: parsing inputs → proposing relevant variables → conceptual dependency modeling → formal probabilistic program construction
- Uses LLMs to implement the "relevance model" that determines what aspects of background knowledge are pertinent
- Employs probabilistic programming (WebPPL) to represent and reason with structured causal models
- Includes semantic validity checks and inference algorithms

### 🗄️💸 Evaluation Results

- MSA performs comparably to hand-crafted models on human judgment prediction
- Shows advantages over pure LLM approaches, particularly in distributional similarity measures
- Pure LLMs appear less robust to surface variations in problems with similar underlying structure
- MSA successfully incorporates diverse forms of evidence (e.g., athlete injuries, experience levels)