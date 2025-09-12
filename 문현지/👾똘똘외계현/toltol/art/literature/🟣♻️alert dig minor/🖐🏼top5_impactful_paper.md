[[09-11|25-09-11]]

물론입니다. 세 논문의 구조를 한눈에 비교하고 그 흐름을 직관적으로 파악할 수 있도록 다이어그램 형태의 표로 정리했습니다.

각 논문이 **문제 제기(🐢) → 이론 구축(🐅) → 적용 및 확장(🐙) → 마무리(👾)**라는 공통된 논리적 흐름을 따르면서도, 저자의 스타일에 따라 각 단계의 구성과 강조점이 어떻게 달라지는지 명확히 볼 수 있습니다.

---

### **세 논문 구조 비교: 🐢🐅🐙👾 프레임워크**
using [[🐢🐅🐙👾의용군현지스타일]]

|구조|역할|Gans et al. (Scott Stern) <br> **[이론 중심]**|Fine et al. (Charlie Fine) <br> **[실무 중심]**|Bolton et al. <br> **[모델 중심]**|
|---|---|---|---|---|
|**🐢<br>기(起)**|**문제 제기** <br> (Why this paper?)|**Sec 1. Introduction** <br> **Sec 2. The S-Curve Paradox** <br> S-커브의 이론적 패러독스를 제시하며 문제의 깊이를 더함|**Sec 1. Introduction** <br> **Sec 2. Literature Review** <br> 실무와 학계의 괴리(Gap)를 지적하며 연구의 필요성을 강조|**Sec 1. Introduction** <br> "실험 설계에서의 새로운 도덕적 해이"라는 핵심 문제를 간결하게 정의|
|**🐅<br>승(承)**|**이론 & 모델** <br> (What is the engine?)|**Sec 3. A Choice-Based Approach...** <br> **Sec 4. A Simple Model...** <br> 개념적 프레임워크를 먼저 제시하고, 수리 모델로 구체화|**Sec 3. Nailing, Scaling, and Sailing** <br> 현장 관찰을 바탕으로 한 실용적인 3단계 프레임워크를 제시|**Sec 2. Relation to Literature** <br> **Sec 3. The Model** <br> 문헌적 맥락을 짚은 후, 정교하고 상세한 수리 모델을 구축|
|**🐙<br>전(轉)**|**응용 & 함의** <br> (How does it work?)|**Sec 5. Industry-Level...** <br> **Sec 6. Implications for Strategy...** <br> 모델을 산업 수준으로 확장하고, 전략 및 정책적 함의를 도출|**Sec 4. Case Examples...** <br> 다양한 실제 사례에 프레임워크를 적용하여 타당성을 증명|**Sec 4. Policy Responses** <br> 모델의 결과를 바탕으로 현실에 적용 가능한 정책적 대안을 탐구|
|**👾<br>결(結)**|**결론** <br> (So what?)|(별도 결론 없음) <br> **Sec 6. Implications...** <br> 정책적 함의를 제시하며 자연스럽게 마무리|**Sec 5. Discussion, Conclusion...** <br> 연구를 요약하고 한계와 향후 연구 방향을 명시하는 전형적 구조|**Sec 5. Conclusion** <br> 연구의 핵심 발견과 이론적 기여를 간결하게 요약하며 마무리|


----


entrepreneur's innovation (idea to impact) should be designed as idea's implementation and adoption of that implementation. i'll analyze the five paper that i adopted and reverse engineer this.

[[💠integ(process-product)]]

[[moon24]]
## interesting

using Davis' Index of the Interesting. I'm aware of the [need for bridge from interesting to important](https://journals.aom.org/doi/10.5465/amj.2020.4002), but paper has interesting lowbar to pass to even be judged on its importance.

| Type of Interestingness                         | Why it's Interesting                                                                               |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Order from Chaos                                | What seems disorganized and unstructured is really organized and structured                        |
| Chaos from Order                                | What seems organized and structured is really unstructured and disorganized                        |
| Simplicity in the Complex (Invisible Structure) | What seems like heterogeneous phenomena are really a single phenomenon                             |
| Complexity in the Simple (False Structure)      | What seems like a single phenomenon is really heterogeneous phenomena                              |
| The Psychological is Social                     | What seems like an individual phenomenon is really holistic                                        |
| The Social is Psychological                     | What seems like a holistic phenomenon is really individual                                         |
| The Social-Psychological                        | What seems holistic or individual is really a property of the relation between the two             |
| Local is General                                | What seems like a local phenomenon is real generalizable                                           |
| General is Local or Contextual                  | What seems like a general phenomenon is really local or context-dependent                          |
| Unobserved Dynamism                             | What seems stable and unchanging is really unstable and changing                                   |
| Unobserved Regularity or Periodicity            | What seems unstable and changing is really regular and repeating                                   |
| Unobserved Functionality                        | What seems ineffective for achieving an end is really functional                                   |
| Unobserved Dysfunction                          | What seems functional for achieving an end is really ineffective                                   |
| Unobserved Good                                 | What seems like a bad phenomenon is really good                                                    |
| Unobserved Bad                                  | What seems like a good phenomenon is really bad                                                    |
| Unobserved Correlation                          | What seem like independent phenomena are really interrelated                                       |
| False Correlation                               | What seem like interrelated phenomena are really independent                                       |
| False Coexistence                               | What seem like phenomena that can exist together really cannot exist together                      |
| Surprise Coexistence                            | What seem like phenomena that cannot exist together can really exist together                      |
| False Positive                                  | What seems like positive covariation is really negative covariation                                |
| False Negative                                  | What seems like negative covariation is really positive covariation                                |
| Header (General)                                | Incremental is continuous, continuous is incremental, curvilinear is linear, linear is curvilinear |
| False Similarity                                | What seem like nearly similar phenomena are really opposite phenomena                              |
| False Difference                                | What seem like different phenomena are really the same                                             |
| Dependent Variable is Independent Variable      | What seems like the predictor is really the outcome                                                |
| Independent Variable is Dependent Variable      | What seems like the outcome is really the predictor                                                |
| One-Way relationship is Complex                 | What seems like a direct relationship is really a mutual or non-recursive relationship             |

## implementable

it should have a tool to implement what the audience learn. 
- how to resolve "resistance to change"
- if supplying the research for the audience with economics background, i should camouflage the language to what they can (and don't have uncomfortableness in) digesting. 

| Application of Research method (Bayesian Computation and Simulation                            | Bible (2020+)                                                                                                                   | Relevance to Angie's Problem                                                   | Seed paper for                                                                                                                                 | Limitation                                                                        | outside school but insightful  | Current Frontier                                          | interacting                                                                                                                                                      | honorable mention      |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------ | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Application1 <br>Modeling workflow<br>                                                         | Bayesian Workflow (statistics)<br><br>World to Word Model (cognition)<br><br>Analytical Methods for Dynamic Modelers (dynamics) | experiment choice (which data to collect)<br><br>rational meaning construction | 1️⃣Parameterization & Modeling<br>[[_ref/Gelman04_parameterizationBayes.pdf]] (Andrew Gelman's favorite)<br>[[📜gelman04]]                     | Holes in Bayesian Stats<br><br>data collection is not cast as resource allocation | Computational Rationality      | posterior SBC (statistics)<br><br>ADEV (computer science) | Andrew (statistics)<br><br>Vikash (computer science)<br><br>Tom (dynamics)                                                                                       | [[📜gans23_choose(ent, exp)]] |
| Application2<br>Operations and Innovation Management using Bayesian computation and simulation | Bayesian Entrepreneurship<br><br>Product development and opportunity tournament                                                 | <br><br><br>what to be uncertain about                                         | 4️⃣empirical approach recipe [[📜MackeyBarneyDotson15_CorpDiv]] [[_ref/MackeyBarneyDotson15_CorporateDiv.pdf]] (Jay Barney's favorite)<br><br> |                                                                                   | 3️⃣Operations for entrepreneur | Need Analysis capturing psychological inventory (Moshe)   | Moshe (choice analysis, demand modeling)<br><br>Scott (economics of idea, innovation, entrepreneurship)<br><br>Charlie (decision science, operations management) |                        |
| Counterfactual - Operations and Innovation Management without Bayesian Computation             |                                                                                                                                 |                                                                                | 2️⃣[[📜Meehl90_appraising_amend]]                                                                                                              | 2️⃣One and Done (Efficiency)                                                      |                                |                                                           |                                                                                                                                                                  |                        |



