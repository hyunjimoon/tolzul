2025-02-06
Below is a three-paragraph summary of **Chapter 13: Models With Memory** (multilevel or hierarchical Bayesian models), followed by a comparative table that addresses how **Theory-Based Entrepreneurial Search** (which benefits from hierarchical Bayesian thinking) contrasts with **Practice-Based Entrepreneurial Search** in key dimensions.

---

[[📜chavda24_theoent]]
## **Three-Paragraph Summary of #13 Models With Memory**

**Paragraph 1.** Conventional statistical models often suffer from “anterograde amnesia,” meaning they treat each category or group in the data as if it has no relationship to any other. When modeling outcomes across multiple clusters—whether they are individuals, locations, or time periods—older approaches use either a single pooled average for all clusters or assign each cluster its own completely unpooled parameter. Both extremes can yield poor inference: pooling everything together can underfit by ignoring important differences, while treating every cluster in isolation can overfit and “forget” that clusters often share similarities. Chapter 13 introduces **multilevel (hierarchical) Bayesian models** to address this shortcoming, showing how they “remember” information from all clusters and pool that information adaptively.

**Paragraph 2.** The central idea is that each group-level parameter (like a café’s average waiting time, or an entrepreneur’s theory-based learning rate) is drawn from a population distribution that itself is estimated from the data. This allows **partial pooling**, shrinking extreme or data-scarce groups toward the overall mean, while leaving well-supported (data-rich) groups closer to their own local estimates. A classic illustration is the “coffee robot”: if it observes waiting times in one café, it updates its population-level beliefs about cafés in general. When it visits a new café, it starts from that overall belief—rather than forgetting what it learned—yet it still recognizes that each café has unique features. This “memory” boosts accuracy and guards against under- or overfitting.

**Paragraph 3.** Applied to **entrepreneurial search**, a hierarchical Bayesian model makes it possible for an entrepreneur to learn from multiple ventures, teams, or market niches simultaneously. Some ventures have scant data (small samples) and should borrow strength from the others, whereas well-tested ventures (large samples) remain closer to their own evidence. The model “remembers” the variation among clusters through a learned variance term, so it neither forces everyone into a single mean nor splits them into unrelated points. Overall, **Models With Memory** emphasize how such multilevel approaches harness the entire data set to inform each subgroup, yielding more robust and balanced inference for complex, structured problems.


2025-02-04
## exchangeability

compilation of exchangeability from [[eg(use(exbl))]],

- The point isn’t to say epistemology trumps reality, but rather that in ignorance of such correlations the most conservative distribution to use is i.i.d. 71 This issue will return in Chapter 10. Furthermore, there is a mathematical result known as de Finetti’s theorem that tells us that values which are exchangeable can be approximated by mixtures of i.i.d. distributions. Colloquially, exchangeable values can be reordered. The practical impact of this is that “i.i.d.” as an assumption cannot be read too literally, as different process models again correspond to the same statistical model (as argued in Chapter 1). Even furthermore, there are many types of correlation that do little or nothing to the overall shape of a distribution, but only affect the precise sequence in which values appear. For example, pairs of sisters have highly correlated heights. But the overall distribution of female height remains almost perfectly normal. In such cases, i.i.d. remains perfectly useful, despite ignoring the correlations. Consider for example that Markov chain Monte Carlo (Chapter 9) can use highly correlated sequential samples to estimate most any iid distribution we like.
- In a time series, a previous observation becomes a predictor variable for the next observation. So it’s not easy to think of each observation as independent of, or exchangeable with, the others
- The reason to use varying effects is because they provide better inferences. It doesn’t matter how the clusters arise. If the individual units are exchangablethe index values could be reassigned without changing the meaning of the model—then partial pooling could help.
- essence of the general varying effects strategy: Any batch of parameters with exchangeable index values can and probably should be pooled. Exchangeable just means the index values have no true ordering, because they are arbitrary labels. There’s nothing special about intercepts; slopes can also vary by unit in the data, and pooling information among them makes better use of the data. So our coffee robot should be programmed to model both the population of intercepts and the population of slopes. Then it can use pooling for both and squeeze more information out of the data.



----

## learning covariance


ex-aption ()
생존한게 적자
ex-aption (줄무늬; 인과 (시간축을 byproduct; 다국어))

다국어를 하는게 영향을 미친다. theory 
- test two choose one ()
rationality is ex-post, 사후적으로 구성된 지식은 쓸모가 없다 (인과적이라서가 아니라 다양성을 설명하기 때문에)

정보종결욕구

많은 정보를 받아들이는게 아니라 (데이터가 ); t-1 (머리가 아파서)

A, B, C, D (ambidexirty; 추출 (배터리 기술- 차 시장, 집 배터리 시장 ))
보검 (누구나 다 이길수 있다.) -> 다 잘 할수 있다. (10배는 잘 하는)

material (core competence) 확보 시 (resource-based view; 어디나 통할수 있는 핵심역량 - 살아남을 수 있을수 있다.)

power가 더 중요함 - 성숙단계 (규모가 있어야함; platform)

사후적으로는 비합리적

actor의 입장에서는 순서가 바뀜 (과거의 성공요소가 현재의 실패요소 (월마트 - cross docking는 amazon internet based 확장가능성 바뀜))

- optimal stopping rule: exchangeability (최적화되는 지점; marginal underage = overage cost); exchangeability 
- 계량화 (두가지 대안; 3가지 대안)
- max(shipment)

[[Aggregate and Marginalize]]

[[💠integ(process-product)]]