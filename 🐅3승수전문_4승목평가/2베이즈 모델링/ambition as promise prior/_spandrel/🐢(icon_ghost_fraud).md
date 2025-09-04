## 문단별 요약

### **서두**

- 창업의 핵심 역설은 “벤처가 자신이 속한 현실을 어떻게 만들어내는가”라는 문제.
- 네 가지 지적 전통이 이를 다루었으나 각자 일부만 포착.

---

### **# charlie**

- 전통적 운영관리는 안정적 조건에서 효율을 극대화하는 데 최적화됨.
- 그러나 창업은 기존 현실에 맞추는 것이 아니라, 조정이 가능하도록 불확실성 구조를 설계하는 과정.
- 질문은 “효율적으로 생산하는 방법”에서 “집단 행동을 이끌 신념 분포 설계”로 전환.

---

### **# moshe**

- 통계·의사결정과학은 위험과 불확실성을 구분하고, 기대효용 극대화를 제시했으나 이는 안정된 확률/선호를 전제로 함.
- 행동의사결정이론은 선호가 맥락에 따라 변하고, 창업에서는 신념과 효용이 동시에 변하는 ‘공진화’ 현상이 나타남.
- 창업 현실을 설명하려면 이 공진화를 수학적으로 포착할 새로운 틀이 필요.

---

### **# vikash**

- 창업과 인지과학을 베이즈 관점에서 통합.
- 창업자의 약속을 ‘행동을 고취하고 신뢰성을 유지하는 불확실성 구조’로 모델링.
- Beta(μ, τ) 분포를 활용해 창업자가 새로운 세계를 설계하는 과정을 설명.
- 자원-합리성 관점에서, 실패 원인은 종종 ‘조기 정밀화’에 있으며, 성공은 정밀도 조율 능력에 달림.
- 창업 성공은 신념과 가치의 공진화를 조율하는 데 있음.

---

### **# scott**

- 창업 이론은 ‘기회 발견’ → ‘기회 창출’ → ‘약속 설계’로 진화.
- Stern은 창업자가 다양한 이해관계자에게 작동할 수 있는 신념 분포를 설계한다고 주장.
- 이는 전략경영의 ‘계획’ → ‘의미형성’ 전환과 연결됨.
- Beta(μ, τ) 분포는 대담한 약속(μ)과 전략적 모호성(τ)을 동시에 설명하는 수학적 도구로 기능.


Four intellectual traditions have grappled with entrepreneurship's fundamental paradox—how ventures create the realities they inhabit—yet each captures only fragments of this phenomenon. 
# charlie
Operations management, from Taylor's (1911) scientific management to the Toyota Production System (Womack, Jones, & Roos, 1990), perfected coordination within stable constraints, achieving remarkable efficiency when inputs and outputs are well-defined. Yet as Skinner (1969) presaged, strategic alignment assumes an existing reality to align with; entrepreneurship inverts this logic, requiring founders to architect the uncertainty structures that make coordination possible. The operational question transforms from "how do we efficiently produce X?" to "what belief distribution about X enables the collective action necessary to manifest X?"

# moshe
Statistics and decision science promised rigor under uncertainty, beginning with Knight's (1921) distinction between measurable risk and unmeasurable uncertainty. Savage's (1954) axiomatization offered entrepreneurs the apparent comfort of expected utility maximization, assuming stable probability distributions and fixed preference orderings. Yet behavioral decision theory shattered these foundations; Kahneman and Tversky (1979) demonstrated that human valuation dynamically reframes with context, making preferences endogenous to choice architecture. Entrepreneurs face an even more radical entanglement: the act of articulating new possibilities simultaneously transforms both probability assessments and utility functions, requiring mathematics that captures this co-evolution.

detail in [[🐢stats]] as **의사결정의 4단계** 고전적 결정분석이 신념 도출과 효용 명세를 깔끔하게 분리하지만, 창업 현실은 이보다 복잡—신념과 욕망이 공진화 (p(x|d)와 U(x)는 독립적이지 않음)
# vikash
This paper bridges entrepreneurship and cognitive science through a shared Bayesian lens, revealing how the mathematics of belief formation under uncertainty unifies two seemingly disparate fields. Drawing on Josh Tenenbaum's probabilistic language of thought framework—where human cognition constructs and updates structured world models from sparse data—we formalize entrepreneurial promises as designed uncertainty structures that must simultaneously inspire action and maintain credibility. This synthesis extends Scott Stern's evolution from market dynamics (how environments shape innovation) to strategic choice (how entrepreneurs navigate uncertainty), providing the mathematical machinery his recent Bayesian entrepreneurship framework requires. The convergence is not coincidental but necessary: both fields grapple with how agents make consequential decisions under radical uncertainty with limited computational resources. Where Tenenbaum et al. (2020) model children as building probabilistic programs to understand their world, we model entrepreneurs as designing Beta(μ, τ) distributions to create new worlds; where Wong et al. (2023) show how language translates into probabilistic mental models, we show how entrepreneurial promises function as "executable code" that different stakeholders run to generate predictions about venture futures. The resource-rational perspective from Gershman et al. (2015)—that intelligence emerges from optimizing decisions under computational constraints—directly informs our Model 4, where precision becomes a scarce resource requiring investment. This theoretical synthesis yields practical insights: entrepreneurial failure often stems not from insufficient boldness but from premature precision, with Tesla's survival tracing to maintaining τ ≈ 5 while competitors locked into τ > 45, a pattern predicted by the same mathematics governing one-shot learning (Vul et al., 2014) and causal induction (Griffiths & Tenenbaum, 2007). The framework thus positions entrepreneurship within the broader computational rationality paradigm, where success requires not maximizing any single parameter but orchestrating the co-evolution of belief and value—precisely the challenge both cognitive science and entrepreneurship confront at their respective frontiers.
# scott
Entrepreneurship theory evolved from opportunity discovery to opportunity creation, yet Scott Stern's work reveals a deeper evolution: from static choice to dynamic promise design. While Shane and Venkataraman (2000) framed entrepreneurship as recognizing pre-existing opportunities, and Alvarez and Barney (2007) distinguished creation from discovery, Stern's progression from market dynamics (Gans & Stern, 2003) to endogenous appropriability (Gans & Stern, 2018) to entrepreneurial strategy foundations (Gans et al., 2019) traces how entrepreneurs shape not just opportunities but the uncertainty structures surrounding them. His recent Bayesian entrepreneurship framework (Agrawal et al., 2024; Stern et al., 2024) crystallizes this evolution: entrepreneurs don't merely choose strategies, they design belief distributions that must function across heterogeneous stakeholders with divergent priors. Where Sarasvathy's (2001) effectuation showed entrepreneurs begin with means rather than ends, Stern shows they begin with designed ambiguity—carefully calibrated promises that preserve optionality while attracting resources. This connects directly to strategic management's shift from planning to sensemaking: where Cyert and March (1963) recognized firms as coalitions requiring convergent interpretation, and Weick (1995) formalized sensemaking as creating order from ambiguity, Stern's work operationalizes how entrepreneurs architect that ambiguity from the start. Our contribution formalizes this through Beta(μ, τ) distributions—mathematical objects that capture both the persuasion power of bold promises (high μ) and the operational flexibility of strategic ambiguity (low τ), unifying Stern's insights about endogenous choice with the cognitive science of belief formation under uncertainty.