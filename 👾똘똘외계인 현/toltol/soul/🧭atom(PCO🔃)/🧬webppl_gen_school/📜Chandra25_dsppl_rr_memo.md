# memo: A Domain-Specific PPL for Reasoning about Reasoning (QA🗄️3🖼️2)

![[📜Chandra25_dsppl_rr_memo 2025-04-13-15.svg]]
%%[[📜Chandra25_dsppl_rr_memo 2025-04-13-15|🖋 Edit in Excalidraw]]%%

## 🗄️1: Table of Contents (Question-Answer Format)

|Section/Subsection|Question|Answer|Literature Brick|
|---|---|---|---|
|Introduction|Why is implementing theory of mind models challenging?|🧍‍♀️ Correctness: PPLs lack agency abstractions, leading to bugs like "perpetration confusion" where agents inadvertently control or read minds<br>🌏 Efficiency: Combinatorial explosion of possible worlds leads to slow inference|• Nested inference research<br>• Perceptual confusion in automatic differentiation<br>• Grid search parameter fitting limitations|
|Design & Implementation|How does memo address these challenges?|🧭 Syntax/Semantics: Explicit agency attribution for choices and observations, enforcing a "metatheory of mind"<br>🗺️ Compilation: Models compile to efficient array programs, enabling exact enumeration, parallelization, and differentiation|• Epistemic logic<br>• Bayesian recursive reasoning<br>• Array programming<br>• JAX ecosystem|
|Applications & Evaluation|What are the real-world benefits of memo?|🧠 Shorter code: 2-4× less code than implementations in existing PPLs<br>🤜 Dramatic speedups: 30-2,000,000× faster inference depending on model complexity<br>👓 New capabilities: Models that reason about thinking cost or integrate with neural networks|• RSA models in linguistics<br>• Schelling coordination games<br>• MDP planning models<br>• Resource-rationality modeling|
|Case Studies|How well does memo work on classic theory of mind models?|📊 Memo implementations are consistently shorter and faster than expert implementations in traditional PPLs, while being more modular and extensible|• Rational Speech Acts (RSA)<br>• Schelling coordination games<br>• Markov Decision Processes<br>• POMDP belief-space planning|
|Real-world Use|How are researchers adopting memo?|💸 Researchers are using memo for advanced models of lying, social relationships, empathetic explanation, and caregiving, achieving dramatic speedups that enable more ambitious models|• Lie production/detection<br>• Saliva sharing as social signal<br>• Empathetic explanation<br>• Parental intervention models|

## 🗄️2: Comparison with Existing Approaches (📐 Productizing)

|Aspect|General-Purpose PPLs|Hand-Coded Solutions|memo|
|---|---|---|---|
|Agency Modeling|Implicit, error-prone|Manual, ad-hoc|Explicit, principled|
|Programming Model|Samples, conditions, infers|Custom implementations|Agents choose, observe, think|
|Inference Method|Sampling, slow|Bespoke, efficient|Array-based, parallelized|
|Parameter Fitting|Grid search, no gradients|Custom optimization|Automatic differentiation|
|Code Reusability|Poor modularity|Language-specific|Domain-abstracted, reusable|
|Hardware Acceleration|Limited|Manual implementation|Native GPU support|
|Neural Network Integration|Complex, inefficient|Custom bridges|Seamless (via JAX)|
|Thinking Cost Modeling|Not supported|Manually implemented|First-class language construct|

## 🗄️3: Practical Applications (💸 Evaluating)

|Domain|Implication|Example Application|
|---|---|---|
|Cognitive Science|Enables more complex theory of mind models with recursive reasoning|Modeling how people detect lies by inferring over a model of how people produce lies (achieving 2,000,000× speedup)|
|Linguistics|Simplifies pragmatic communication models with efficient inference|Modeling scalar implicature (how "some" implies "not all") with 40× speedup and 2× less code|
|Decision Theory|Makes planning models faster and more extensible|Solving grid-mazes and optimal policies with 30× speedup and native GPU support|
|Uncertainty Reasoning|Enables belief-space planning with principled agency|Modeling POMDP problems with clear agent/world separation|
|Human-Computer Interaction|Creates user models that reason about thinking cost|Font design for seven-segment displays using pragmatic reasoning|

## 🖼️1: Need-Solution Mapping

![Need-Solution Mapping](https://i.imgur.com/need_solution.png)

- **Problem (💜)**: Implementing Theory of Mind models in general-purpose PPLs is:
    
    - Error-prone: Subtle agency-related bugs like perpetration confusion
    - Slow: Nested inference causes combinatorial explosion
    - Time-consuming: Parameter fitting takes days of computation
- **Solution (💚)**: A domain-specific language that provides:
    
    - Syntax that respects theory of mind principles with explicit agency
    - Compilation to efficient array programs with parallelization
    - End-to-end differentiation for parameter fitting via gradient descent

## 🖼️2: Methodology Visualization

![Methodology Visualization](https://i.imgur.com/methodology.png)

- **Static Semantics: Frames of Mind**
    
    - Tracks nested "frames of mind" for each agent
    - Enforces 4 agency principles:
        1. No mind reading
        2. False beliefs possible
        3. Referential opacity
        4. No mind control
- **Dynamic Semantics: Array Compilation**
    
    - Maintains array for each agent's beliefs
    - chooses: Adds dimension, updates with likelihood
    - observes: Normalizes along dimension
    - E[e]: Computes via tensor contraction
- **Design Tradeoffs**
    
    - 💜 Domain restrictions: Discrete variables only
    - 💜 Static structure: Fixed sequence of choices
    - 💚 Massive efficiency: 30-2,000,000× speedups
    - 💚 Deep learning integration: Neural networks in loop

## Key Resources

The paper presents memo, a domain-specific PPL for theory of mind modeling that offers dramatic speedups (up to 2,000,000×) and code simplification (2-4×) compared to traditional approaches. It achieves this by providing explicit agency syntax that prevents common bugs and compiling to efficient array programs. The system has already been adopted by several research groups working on cognitive science problems, enabling models that were previously computationally infeasible.