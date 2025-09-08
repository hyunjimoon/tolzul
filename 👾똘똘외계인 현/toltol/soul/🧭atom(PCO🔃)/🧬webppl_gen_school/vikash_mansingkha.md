2025-06-03
- detail of math equation interpretation : economics > computational statistics > computational cognitive science
- math to code/figure ratio:   economics > computational statistics > computational cognitive science
- need to infer which phase (state) i'm in and since risk is a variable, progression of phase is not monotonic
- 


2025-05-16
Request: May I share biweekly progress updates with you as I rebuild my research approach? No feedback expected, though occasional guidance would be valuable.  
  
Thank you for your precise feedback during yesterday's qualification exam. Three insights:  
  
1. Structure before detail  
  * You emphasized defining formal objects and motivating them before diving into formalism.  
  * My error: I focused on advancing research rather than demonstrating researcher capability. This misalignment won't recur.  
  
2. Teaching as validation  
  * Your suggestion to explain "as if to an undergraduate" provides a concrete test of understanding.  
  * I've favored comprehensive teaching approaches (showing all concepts together then refining) over sequential ones, but recognize academic writing requires foundation-first structures. My coarse-to-fine learning style might need restructuring when writing.  
  
3. Disciplinary clarity  
  * You noted uncertainty about whether I've "done substantial work but can't communicate it" or "haven't made sufficient progress."  
  * This ambiguity itself indicates presentation failure. While simulating the two mode's separability from each committee member's perspective is challenging, I'll learn how to make technical depth unambiguous.  
  * Context: I'm navigating transition from engineering to business, managing family expectations (my mother has pre-thyroid cancer condition and worries about my progress), and balancing high ambitions with practical constraints. These factors don't excuse communication requirements but add complexity.  
  
Based on your insight, I'm executing two bottleneck actions 1) Restructure paper following Bolton et al., 2) Develop concrete examples demonstrating formal concepts. Hopefully my algorithm STRAP's predicted committee's acceptance uncertainty decrease (.62 and .48 bits) is not too off...  
  
Also, as you emphasized alignment with Charlie, I will put this as my top priority.



2024-11-19
2nd class on programmable inference [[🧠9.66 Vikash - comp.cog.sci_otter_ai.txt]]

"from the first lecture, I did understand your explanation about robustness and generality. Trade off. Oh, I thought like perhaps the example that you just illustrated. I understand what generality comes from, but I don't know where the robustness comes from. Oh, that's interesting. Well, I can say, for this example, I will point out that this whole symbolic method, right, discretizing the domain, training an approximation, and then doing exact inference has much more easy to understand error properties than training in your own right. You know, if you want arbitrary accuracy in the circuit and add more samples to calculate the conditional probability, which will converge essentially by Monte Carlo execution. Carlo. And the exact inference process is exact. So this is sort of one way to get a much more robust inference algorithm because, and in fact, you can, even if you want to, you can remove the Monte Carlo sampling by systematically enumerating current start and destination cells. So there's all kinds of ways that you can basically use this type of architecture to make an inference engine that has founded failure problems with you, rather than just hoping for cover things by"

- [[VKM CoCoSci Fall 2024 Lecture 2 Inference meta-programming 11.07.24.pdf]]
- [[VKM CoCoSci 2024 ProbComp Lecture 1 --- Big Picture.pdf]]

---
 - bridge mapped brain with mapped world
- evaluated by [[vikash🧠(🌏,🗺️))]]
- comparing statistical equity valuation to conversational inference language-based equity valuation

---

2024-10-28
- gave feedback on [[TwoSigma_proposal 1.pdf]]: the design of 1) evaluation, ?,3)natural language interface


---

2023 summer
[[🗺️abD_mon]], [[🌏abE_tues]], [[🌏abdE_thurs]], [[🌏🗺️aE_fri]], 
### Rational AI foundation models via probabilistic programming

| Feature                    | Transformers                         | Databases, Graphics Engines, Parsers (e.g., C++) | Generative Databases, Graphics Engines, Semantic Parsers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------- | ------------------------------------ | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Effort Type**            | "best effort"                        | "strict & safe"                                  | probabilistic best-effort                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Learnability**           | Learned weights, fixed structure     | Not learnable                                    | Learned model structure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Scaling Approach**       | Empirical app-level scaling          | Back-of-envelope app-level scaling               | Back-of-envelope app-level scaling                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Implementation Tools**   | JAX                                  | C++                                              | Embedded in C++ and JAX                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Key Features/Tradeoffs** | Focused on generality and automation | Focused on robustness                            | Rational risk & reward tradeoffs in user space between robustness and generality<br><br>probabilistic programming as a unifying framework for building AI systems, emphasizing its ability to balance robustness and generality. It explains how symbolic methods, like discretizing domains and exact inference, offer robust error properties compared to neural networks, while Monte Carlo sampling enables scalable, adaptive solutions. The trade-offs between robustness, generality, and automation are highlighted as critical to rational AI design.<br> |



| Aspect                    | Computer Systems                              | Market Strategy                         | Example: Tesla Battery Market                                  |
| ------------------------- | --------------------------------------------- | --------------------------------------- | -------------------------------------------------------------- |
| **Conservative Approach** | Symbolic Methods (C++)                        | Sequential Testing                      | Test in California First                                       |
| • *Strategy*              | Exact inference, discretization               | Test one market/feature at a time       | Launch with proven Japanese batteries                          |
| • *Benefits*              | Clear error bounds, guaranteed performance    | Predictable outcomes, clear feedback    | Consistent satisfaction, reliable adoption                     |
| • *Limitations*           | Limited scalability, rigid                    | Slower learning, missed interactions    | May miss breakthrough opportunities                            |
| • *When to Use*           | Safety-critical systems, small problem spaces | High-stakes decisions, known markets    | Luxury segment, reliability-focused customers                  |
| **Exploratory Approach**  | Monte Carlo Sampling                          | Parallel Testing                        | Test in Multiple Markets                                       |
| • *Strategy*              | Probabilistic sampling, adaptive precision    | Test multiple features simultaneously   | Launch US & Japanese batteries together                        |
| • *Benefits*              | Scalable, handles complexity                  | Rapid learning, discovers interactions  | Find unexpected market opportunities                           |
| • *Limitations*           | Probabilistic guarantees only                 | Higher uncertainty, resource intensive  | Risk of market confusion/rejection                             |
| • *When to Use*           | Complex problems, approximate solutions ok    | Uncertain markets, need rapid learning  | Performance segments, early adopters                           |
| **Rational Tradeoff**     | Let users choose precision vs. speed          | Market-specific risk tolerance          | Geographic/demographic segmentation                            |
| • *Example*               | Add more samples as needed                    | Adjust testing based on market feedback | CA: Japanese batteries (safe)<br>TX: US batteries (innovative) |
| • *Key Factor*            | Resource constraints                          | Market uncertainty                      | Cultural/economic factors                                      |
| • *Success Metric*        | Computational efficiency vs. accuracy         | Learning speed vs. confidence           | Customer satisfaction vs. innovation                           |
| • *Optimization Goal*     | Balance robustness and generality             | Balance risk and market potential       | Balance reliability and performance                            |