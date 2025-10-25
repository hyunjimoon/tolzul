---
성장:
  - 2025-10-23T23:33:06-04:00
  - 2025-10-24T13:38:48-04:00
URL: https://claude.ai/share/a427a92e-ab66-4e6e-ae3d-60fedc16c28d
---
# 14.282 Fall 2025 중간고사 정리 / Midterm Summary

## 문제 1: 경력 관리 (Career Concerns Model)

### 핵심 아이디어 / Core Intuition

**한글:**
직장인이 일을 열심히 하는 이유는 두 가지입니다:
1. 지금 당장 받는 월급 (명시적 보상)
2. 미래 고용주들에게 "나는 능력있는 사람"이라고 보이기 위해 (암묵적 보상)

이 문제는 두 번째 동기, 즉 "평판을 쌓으려는 노력"이 어떻게 작동하는지 보여줍니다.

**English:**
People work hard for two reasons:
1. Current salary (explicit incentives)
2. To signal "I'm talented" to future employers (implicit incentives)

This problem shows how the second motivation - "reputation building" - actually works.

---

### 문제 1(a): 성과가 관찰되지만 계약할 수 없을 때

**상황 설정 / Setup:**
- 2년 계약을 생각해보세요
- 매년 여러 회사가 당신을 고용하려고 경쟁합니다
- 당신의 "타고난 능력" η는 아무도 모릅니다 (당신도!)
- 당신이 일한 결과물 y는 회사만 보지만, 성과지표 p는 모두가 봅니다

**핵심 질문 / Key Questions:**
1. 왜 1년차에 노력 (a₁₁, a₂₁) ≠ (0, 0)인가?
2. cos(θ)가 노력에 어떤 영향을 주나?
3. φ = h_ϕ/(h+h_ϕ)가 노력에 어떤 영향을 주나?

**직관적 설명 / Intuitive Explanation:**

**한글:**
- **1년차:** 당신은 열심히 일합니다. 왜? 성과지표 p₁이 좋으면 사람들이 "이 사람은 능력이 있구나"라고 생각하고, 2년차 연봉이 올라가기 때문입니다.
- **2년차:** 더 이상 미래가 없으니 노력할 이유가 없습니다. a₁₂ = a₂₂ = 0

**왜 1년차에 일을 하나?**
- 성과 p₁ = g₁a₁₁ + g₂a₂₁ + η + φ₁
- 사람들은 p₁을 보고 η를 추측합니다 (베이지안 업데이트)
- p₁이 높으면 → 사람들이 "η가 높구나" 생각 → w₂가 올라감
- 그래서 1년차에 노력해서 p₁을 높입니다

**cos(θ)의 역할:**
- cos(θ)는 "성과지표 방향"과 "결과물 방향"이 얼마나 일치하는지를 나타냅니다
- 만약 성과지표가 실제 회사 성과와 잘 맞으면 (cos(θ) 크면), 노력이 합리적으로 배분됩니다
- 만약 불일치하면 (cos(θ) 작으면), "보여주기식" 노력이 많아집니다

**φ의 역할 (신호의 정확도):**
- φ가 크다 = 성과지표 p₁이 진짜 능력 η를 잘 반영한다
- φ가 크면 → 1년차 노력이 미래 연봉에 더 큰 영향 → 더 열심히 일함
- φ가 작으면 → "어차피 운빨이네" → 덜 노력함

**English:**
- **Year 1:** You work hard. Why? Good performance p₁ makes people think "this person is talented," raising your Year 2 salary.
- **Year 2:** No future left, no reason to work hard. a₁₂ = a₂₂ = 0

**Why work in Year 1?**
- Performance p₁ = g₁a₁₁ + g₂a₁₁ + η + φ₁
- People observe p₁ and infer η (Bayesian updating)
- High p₁ → people think "high η" → w₂ increases
- So you work hard in Year 1 to boost p₁

**Role of cos(θ):**
- cos(θ) measures alignment between "what looks good (p)" and "what's actually valuable (y)"
- High cos(θ) → performance metric aligns with real value → effort is well-directed
- Low cos(θ) → creates "window dressing" behavior

**Role of φ (signal precision):**
- Large φ = performance p₁ accurately reflects true ability η
- Large φ → Year 1 effort matters more for future salary → work harder
- Small φ → "it's all luck anyway" → work less

---

### 문제 1(b): 성과로 계약할 수 있을 때

**새로운 상황 / New Setup:**
이제 회사가 "기본급 + 성과급×성과지표" 계약을 제시할 수 있습니다: w_t = s_t + b_t·p_t

**핵심 질문 / Key Questions:**
1. b₁* ≠ b₂*인 이유는?
2. a₁* ≠ a₂*인 이유는?
3. 계약 내용이 공개되는 게 왜 중요한가?

**직관적 설명 / Intuitive Explanation:**

**한글:**

**왜 b₁* < b₂*인가?**
- **2년차 (b₂*):** 순수 "돈 주면 일하기" 문제입니다. 미래가 없으니 성과급만이 유일한 동기입니다.
- **1년차 (b₁*):** 이미 "평판 쌓기"라는 암묵적 동기가 있습니다. 회사는 "어차피 얘가 알아서 일할 거야"라고 생각하고 성과급을 덜 줍니다.
- **결과:** 명시적 인센티브(b₁)와 암묵적 인센티브(평판)가 **대체재** 관계입니다.

**생각해보기:** 
당신이 좋은 대학원에 가려고 1학년 때 이미 열심히 공부하고 있다면, 교수님이 굳이 "A+ 주겠다"고 약속할 필요가 없는 것과 같습니다.

**계약 내용 공개가 중요한 이유:**
시나리오를 상상해봅시다:
- 당신이 1년차에 성과 p₁ = 10을 달성했습니다
- 만약 계약이 비밀이라면: 사람들이 "이게 능력인가 노력인가?"를 구분 못합니다
- 만약 계약이 공개라면: "아, 성과급이 b₁=0.3이었구나. 그럼 저 정도 노력은 합리적이고, 나머지는 능력이겠네"라고 추론할 수 있습니다

**핵심:** 계약 공개 → 시장이 성과를 "능력"과 "노력" 으로 분해 가능 → 능력 평가 정확 → 평판 시스템 작동

**English:**

**Why b₁* < b₂*?**
- **Year 2 (b₂*):** Pure "pay for performance" problem. No future, so explicit incentives are the only motivation.
- **Year 1 (b₁*):** Implicit "reputation building" motive already exists. Firms think "they'll work hard anyway" and offer lower explicit incentives.
- **Result:** Explicit incentives (b₁) and implicit incentives (reputation) are **substitutes**.

**Analogy:**
If you're already studying hard in freshman year to get into a good grad school, your professor doesn't need to promise you an A+ as extra motivation.

**Why public observability of contracts matters:**
Imagine this scenario:
- You achieve performance p₁ = 10 in Year 1
- If contract is secret: People can't tell "was this ability or effort?"
- If contract is public: "Oh, bonus rate was b₁=0.3. Given that incentive, that effort level makes sense, so the rest must be ability"

**Key point:** Public contracts → market can decompose performance into "ability" and "effort" → accurate ability assessment → reputation system works

---

## 문제 2: 평판과 정보 전달 (Cheap Talk with Reputation)

### 핵심 아이디어 / Core Intuition

**한글:**
조언자가 "믿을 만한 사람"으로 보이고 싶어할 때, 오히려 정직한 조언을 못하게 되는 역설을 보여줍니다.

**상황:** 
- 컨설턴트(agent)가 상황 s ∈ {0,1}을 알고 있습니다
- CEO(principal)에게 조언 m ∈ {0,1}을 해야 합니다
- 컨설턴트에는 두 종류가 있습니다:
  - **편향된 컨설턴트:** 무조건 "높은 결정"을 선호 (자기 이익)
  - **공정한 컨설턴트:** CEO와 같은 선호 (진짜 도움)
- 모든 컨설턴트는 "공정한 사람"으로 보이고 싶어합니다 (평판 가치 λ)

**English:**
Shows the paradox: when advisors care about appearing "trustworthy," they actually become unable to give honest advice.

**Setup:**
- Consultant (agent) privately observes state s ∈ {0,1}
- Must advise CEO (principal) with message m ∈ {0,1}
- Two types of consultants:
  - **Biased:** always prefer "high decision" (self-interest)
  - **Unbiased:** same preferences as CEO (truly helpful)
- All consultants want to appear "unbiased" (reputation value λ)

---

### 문제 2(a): 왜 완전한 정보 전달이 불가능한가?

**한글:**
**목표:** 양쪽 타입 모두 진실을 말하는 균형이 있는가? (m = s)

**증명 (모순법):**
1. 만약 그런 균형이 있다고 가정해봅시다
2. 공정한 컨설턴트: s=0일 때 m=0, s=1일 때 m=1 (진실 말함)
3. 편향된 컨설턴트: s=1일 때는 m=1이라고 할 겁니다 (어차피 높은 결정 원하니까)
4. **문제:** s=0일 때 편향된 컨설턴트는 어떻게 하나?
   - 진실(m=0) 말하면 → CEO가 낮은 결정 → 싫음
   - 거짓(m=1) 말하면 → CEO가 높은 결정 + "공정한 척" 가능 → 이득!
5. **결론:** 편향된 컨설턴트가 s=0일 때 m=1으로 눕니다 → 균형 붕괴

**왜 이렇게 되나?**
거짓말의 비용이 없습니다 (cheap talk). 편향된 사람은 공정한 사람을 흉내내서 이득만 봅니다.

**English:**
**Goal:** Can both types truthfully reveal s? (m = s)

**Proof (by contradiction):**
1. Suppose such equilibrium exists
2. Unbiased: reports m=0 when s=0, m=1 when s=1 (truth-telling)
3. Biased: when s=1, will report m=1 (wants high decision anyway)
4. **Problem:** When s=0, what does biased type do?
   - Tell truth (m=0) → CEO makes low decision → dislikes it
   - Lie (m=1) → CEO makes high decision + looks "unbiased" → benefits!
5. **Conclusion:** Biased type deviates to m=1 when s=0 → equilibrium breaks

**Why?**
No cost to lying (cheap talk). Biased type can mimic unbiased and only benefit.

---

### 문제 2(b-c): 부분 분리 균형도 불가능

**한글:**
"공정한 사람은 가끔 진실을, 편향된 사람은 항상 거짓을" 같은 중간 균형도 안 됩니다.

**이유:** 평판 인센티브가 너무 강해서, 누구든 "좋은 평판 받는 메시지"로 몰립니다.

**English:**
Partial separation (like "unbiased sometimes tells truth, biased always lies") also impossible.

**Reason:** Reputation incentives are so strong that everyone pools on "good reputation message."

---

### 문제 2(d): 모두 "1"이라고 말하는 균형

**한글:**
**균형:** m^u = m^b = 1 (모두가 1이라고 말함)

**언제 가능한가?**
공정한 컨설턴트가 s=0을 봤을 때도 m=1이라고 말하려면:
- "진실(m=0) 말하면 → 편향된 사람으로 오해받음 → 평판 0"
- "거짓(m=1) 말하면 → 평균 평판 유지 → 평판 q"
- **조건:** λq ≥ y(1 - d₀²)
  - 왼쪽: 평판을 지키는 가치
  - 오른쪽: 정직하게 조언해서 얻는 가치

**의미:** 평판이 너무 중요하면, 공정한 사람도 거짓말을 합니다!

**실제 예시:**
- 투자은행 애널리스트들이 "매도" 추천을 거의 안 하는 이유
- 정치 컨설턴트들이 "위험한 진실"보다 "안전한 거짓"을 선택하는 이유

**English:**
**Equilibrium:** m^u = m^b = 1 (everyone says 1)

**When possible?**
For unbiased consultant who sees s=0 to still say m=1:
- "Tell truth (m=0) → perceived as biased → reputation 0"
- "Lie (m=1) → maintain average reputation → reputation q"
- **Condition:** λq ≥ y(1 - d₀²)
  - Left side: value of maintaining reputation
  - Right side: value of giving accurate advice

**Meaning:** If reputation matters too much, even honest people lie!

**Real examples:**
- 🙋‍♀️Why investment bank analysts rarely give "sell" recommendations
- Why political consultants choose "safe lies" over "dangerous truths"

---

### 문제 2(e): 모두 "0"이라고 말하는 균형

**한글:**
**균형:** m^u = m^b = 0 (모두가 0이라고 말함)

(d)의 조건이 성립 안 하면 이쪽 균형이 존재합니다. 대칭적 논리입니다.

**핵심 통찰:**
- 평판 관리가 정보 전달을 **파괴**합니다
- 모두가 같은 말을 하면 (pooling) → CEO는 아무것도 배우지 못함
- 하지만 아무도 "이상한 사람"으로 보이기 싫어서 정보를 숨김

**English:**
**Equilibrium:** m^u = m^b = 0 (everyone says 0)

When condition (d) fails, this equilibrium exists. Symmetric logic.

**Key insight:**
- Reputation concerns **destroy** information transmission
- Everyone says same thing (pooling) → CEO learns nothing
- But no one wants to look "weird," so they hide information

---

## 전체 교훈 / Overall Lessons

### 문제 1: 암묵적 vs 명시적 인센티브

**한글:**
- 미래를 생각하는 사람은 현재 계약 없이도 일합니다 (경력 관리)
- 명시적 보상과 암묵적 보상은 대체재입니다
- 정보 투명성이 평판 시스템을 작동시킵니다

**English:**
- People thinking about future work hard even without current contracts (career concerns)
- Explicit and implicit incentives are substitutes
- Information transparency enables reputation systems

### 문제 2: 평판과 정보 전달의 긴장

**한글:**
- 평판을 너무 중요하게 생각하면 → 정직한 소통 불가능
- "좋은 사람으로 보이기" vs "진실 말하기" 사이 트레이드오프
- 현실적 함의: 조언 시장에서 정보가 왜 왜곡되는가

**English:**
- Care too much about reputation → honest communication impossible
- Trade-off between "looking good" vs "telling truth"
- Real implication: why advice markets produce distorted information

---

## 연결: Strategic Ambiguity와의 관계

**한글:**
이 두 문제는 당신의 "strategic ambiguity" 연구와 깊은 관련이 있습니다:

**문제 1:**
- 기업가가 "precision"을 선택하는 문제
- 너무 정확한 약속 → 미래 적응력 상실
- 너무 애매한 약속 → 자원 동원 실패
- **연결:** Career concerns model에서 어떤 performance measure를 공개할지 선택하는 것과 유사

**문제 2:**
- 메시지의 모호성이 평판과 정보 전달에 미치는 영향
- 🙋‍♀️"풀링 균형"이 strategic ambiguity의 한 형태🙋‍♀️
- **연결:** 기업가가 의도적으로 모호하게 말해서 다양한 해석을 가능하게 하는 것

**English:**
These two problems deeply connect to your "strategic ambiguity" research:

**Problem 1:**
- Entrepreneurs choosing "precision" level
- Too precise promise → lose future adaptability
- Too vague promise → fail to mobilize resources
- **Connection:** Like choosing which performance measures to reveal in career concerns model

**Problem 2:**
- How message ambiguity affects reputation and information transmission
- "Pooling equilibrium" as form of strategic ambiguity
- **Connection:** Entrepreneurs deliberately speak vaguely to allow multiple interpretations

**당신의 OIL 프레임워크:** τ* = max{0, √(V/4i) - 1}
- 이 문제들은 정밀도(precision)를 선택할 때 reputation concerns와 information revelation의 트레이드오프를 보여줍니다
- Career concerns = implicit value of ambiguity
- Cheap talk equilibria = strategic use of ambiguity for reputation

**Your OIL framework:** τ* = max{0, √(V/4i) - 1}
- These problems show reputation concerns and information revelation trade-offs when choosing precision
- Career concerns = implicit value of ambiguity  
- Cheap talk equilibria = strategic use of ambiguity for reputation
