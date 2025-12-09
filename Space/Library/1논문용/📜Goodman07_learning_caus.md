---
collection:
  - "[[Space/Lab/Papers]]"
author_ids:
  - noah_goodman
field:
  - 👾cog
year: 2007
created: 2024-12-03
---

1. The Goodman et al. paper on "Learning Grounded Causal Models" is relevant because it shows how systems can learn multiple layers simultaneously:
- Observable variables (perceptual grounding)
- Causal structure between variables
- The relationship between perception and causation

world is causal, but our observation2theory2hypotheis is complex?
![[Pasted image 20241203145700.png]]

| Section/Subsection | 🔐Research Question                                                                                           | 🧱Literature Brick                                                                                                                                                            | 🔑Key Message                                                                                                                                                                     | Figure                                                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Introduction    | How do people learn causal variables and their relationships simultaneously when neither is known in advance? | • Traditional causal learning theories assume variables are predefined<br>• Gestalt grouping and perceptual learning literature<br>• Philosophy of science on paradigm shifts | Bottom-up perceptual clustering alone cannot explain how humans learn causally-relevant variables - need integrated learning of variables and causal structure                    | Fig 1: Hierarchical framework showing perceptual grounding and causal structure<br>![[Pasted image 20241203145328.png\|300]]            |
| 2. Modeling        | How can we formalize the joint learning of variables and causal structure in a Bayesian framework?            | • Bayesian networks literature<br>• Shepard's (1987) consequential regions<br>• Work on size principle in learning                                                            | • Variables defined by observation functions mapping percepts to states<br>• Causal structure links variables over time<br>• Size principle provides pressure to minimize regions | Fig 1: Diagram of grounded causal models showing perceptual grounding and causal structure<br>![[Pasted image 20241203145328.png\|300]] |
| 3. Experiment      | Can humans learn grounded causal models from perceptual evidence alone?                                       | • Work on perceptual causality<br>• Studies of causal learning<br>• Research on concept formation                                                                             | • Created paradigm with hidden "buttons" and causal effects<br>• Three conditions indistinguishable to bottom-up learner<br>• People successfully learned structure and variables | Fig 2: Experimental conditions and example responses<br>![[Pasted image 20241203145409.png]]                                            |
| 4. Results         | Do human inferences match predictions of the Bayesian model?                                                  | • Methods for analyzing causal learning<br>• Research on rational errors<br>• Work on geometric biases                                                                        | • People distinguished conditions impossible for bottom-up learner<br>• Model predicted both successes and "rational errors"<br>• Geometric inferences matched model predictions  | Fig 3: Comparison of human responses to model predictions<br>![[Pasted image 20241203145426.png]]                                       |
| 5. Discussion      | What are implications for theories of concept learning and causal understanding?                              | • Theory-theory approach<br>• Work on semantic grounding<br>• Research on conceptual development                                                                              | Framework shows how meaning can come from both perceptual grounding and causal relations, bridging empiricist and theory-theory approaches                                        | None                                                                                                                                    |
combining induction or transduction for abduction purpose


| Component | Details | Implementation Notes | Success Metrics |
|-----------|---------|---------------------|-----------------|
| **Web Interface Setup** | Interactive EV product development simulator<br>- 6x6 grid representing different market-feature combinations<br>- Hidden customer feedback until tested | • Each cell shows market response within 2s<br>• Color coding: Green (success), Red (failure), Gold (unexpected benefit)<br>• Click = market test ($100K virtual budget) | • Track test selections<br>• Record sequence<br>• Measure time between tests |
| **Condition A: Tesla Path** | Sequential Battery Development<br>- Region 1: Basic cell chemistry<br>- Region 2: Thermal management<br>- Must optimize both for success | • Start with basic cells<br>• Need thermal management for full success<br>• Hidden link: manufacturing efficiency<br>• Time: 5 mins<br>• Budget: 10 tests | Student should:<br>• Find basic-thermal link<br>• Discover production insights<br>• Map technology evolution |
| **Condition B: BYD Case** | Safety-Driven Innovation<br>- Primary goal: Battery safety<br>- Hidden benefits: cost & manufacturing<br>- Parallel discovery possible | • Testing safety reveals manufacturing benefits<br>• Cost advantages emerge from structural design<br>• Multiple feedback loops<br>• Time: 5 mins<br>• Budget: 10 tests | Student should:<br>• Find unexpected benefits<br>• Identify synergies<br>• Map parallel discoveries |
| **Condition C: Porsche Brand** | Brand Value Transfer<br>- Need to map performance metrics<br>- Multiple market segments<br>- Brand value testing | • Premium vs Mass market segments<br>• Performance definition evolution<br>• Heritage value testing<br>• Time: 5 mins<br>• Budget: 10 tests | Student should:<br>• Map segment differences<br>• Track value transfer<br>• Identify brand synergies |
| **Response Template** | Three structured tasks | 1. Draw discovery sequence diagram<br>2. Map feature-market relationships<br>3. Explain development strategy chosen | • Clear process maps<br>• Feature-market links<br>• Strategy rationale |
| **Measurement** | Key metrics | • Time between tests<br>• Test sequence patterns<br>• Budget efficiency<br>• Discovery completeness | • Parallel vs Sequential ratio<br>• Cost per insight<br>• Strategy adaptability |
| **Debrief Format** | 20-minute analysis | • Compare strategies across conditions<br>• Identify optimal patterns<br>• Link to actual company outcomes | • Pattern recognition<br>• Strategic insights<br>• Real-world application |

Specific Examples for Each Condition:

1. **Tesla Condition**
- Testing basic cell gives 70% performance
- Adding thermal gets 90%
- Manufacturing optimization reveals hidden 100%

2. **BYD Condition**
- Safety testing shows 80% cost
- Structural tests reveal 90% manufacturing
- Combined approach enables 100% optimization

3. **Porsche Condition**
- Premium segment accepts 70% traditional metrics
- Performance redefinition gets 90% acceptance
- Brand heritage integration achieves 100%

Experiment Setting:
"Students interact with a virtual product development simulator where they can 'test' different market-feature combinations by clicking cells in a grid, receiving feedback on each test's success while operating under time and budget constraints."

Mathematical Measure:
The key ratio being measured is:

$\text{Strategy Efficiency} = \frac{\text{Value Discovered}}{\text{(Test Cost)} \times \text{(Time Between Tests)}} = \frac{\sum_{i=1}^{n} V_i}{C \times \sum_{i=1}^{n-1} (t_{i+1} - t_i)}$

Where:
- $V_i$ = value discovered in test i (0-100%)
- $C$ = cost per test ($100K)
- $t_i$ = timestamp of test i
- $n$ = total number of tests conducted

This measures how effectively students balance exploration (finding new value) against exploitation (using known information) under resource constraints.

[[🗄️🗄️scott_charlie]] 

[[scott(🧭🗺️selling entrepreneurial choice-map as Bayes.Entrep)]]

Ah yes! Let me redesign the experiment following Goodman's "alien panel" paradigm but applied to automotive innovation:

| Testing Dimension | Grid Design | Mathematical Measure |
|------------------|-------------|---------------------|
| **Criticality** (Is this the right hypothesis to test?) | • 6x6 grid with hidden "innovation regions"<br>• Tesla Case: Two adjacent regions might be one large market (like Goodman's button experiment)<br>• Each click reveals if region is "active" with dot appearance | $\text{ValidApproxBiasCost}(\phi) = \frac{\text{Size of Active Region}}{\text{Total Grid Size}}$ |
| **Fidelity** (Is this test giving accurate signals?) | • BYD Case: Safety region activates manufacturing benefits<br>• Dots appear in specific patterns indicating causal relationships<br>• Hidden relationships between regions (like Goodman's causal structure) | $\text{VerifApproxBiasCost}(\theta\|\phi) = \frac{\text{Correct Causal Links Found}}{\text{Total Possible Links}}$ |
| **Opportunity Cost** (What resources are spent?) | • Each click costs virtual budget<br>• 5-minute time limit per condition<br>• Porsche Case: Premium vs Mass market regions with brand value transfer | $\text{OpportunityCost}(\theta,\phi,N,M) = \text{Clicks} \times \text{Time Between Clicks}$ |

Concrete Experiment Structure:
1. **Condition A (Tesla)**: 
   - Two adjacent regions that might be one market
   - Must discover if separate or unified market
   - Similar to Goodman's "are these separate buttons?"

2. **Condition B (BYD)**:
   - Safety testing reveals manufacturing benefits
   - Must discover causal relationships
   - Like Goodman's hidden causal structure

3. **Condition C (Porsche)**:
   - Brand value transfers across regions
   - Must map value flow patterns
   - Similar to Goodman's effect propagation

Success Metric:
$\text{Learning Efficiency} = \frac{\text{Correct Structure Identified}}{\text{Total Resources Used}} = \frac{\text{Causal Links Found}}{(\text{Clicks}) \times (\text{Time})}$

This design more closely follows Goodman's experimental paradigm while maintaining the automotive industry context. Would you like me to elaborate on any specific condition?