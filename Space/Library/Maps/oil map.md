---
up:
  - - Home
출생: 2025-10-09
type: map
---

# 📊 베이지안 창업 지도

> **"불확실성은 적이 아니라 항해의 조건이다"**

---

## 🧭 핵심 개념

### 베이지안 사고의 본질
```
Prior (사전믿음) + Evidence (증거) → Posterior (사후믿음)
     ↓                  ↓                    ↓
  가정/이론        실험/데이터           업데이트된 전략
```

### 창업에의 적용
- **Prior**: 초기 비즈니스 가설
- **Evidence**: 고객 피드백, 시장 데이터
- **Posterior**: 업데이트된 전략, 피봇 결정

---

## 🌊 연구의 네 전장

### 🐢 사천: 문제 정의
**핵심 질문**: 
- 창업가들은 어떻게 불확실성 하에서 의사결정하는가?
- 베이지안 추론이 창업 의사결정을 설명할 수 있는가?

**관련 노트**:
```dataview
LIST
FROM "Atlas/1-사천-몰입"
WHERE contains(file.outlinks, [[베이지안]]) OR contains(file.outlinks, [[창업]])
```

---

### 🐅 한산: 모델 구축

**Oil Framework의 베이지안 해석**:
- **Precision (τ)**: Prior의 강도
- **Promise (ρ)**: Evidence의 방향
- **Value (V)**: Posterior의 가치

**진화창업 모델**:
- Variation (변이)
- Selection (선택)  
- Retention (보존)

**관련 노트**:
```dataview
LIST
FROM "Atlas/2-한산-전략"
WHERE contains(file.path, "베이즈창업") OR contains(file.path, "진화창업")
```

---

### 🐙 명량: 실증 연구

**데이터 수집**:
- 창업가 인터뷰
- 케이스 스터디
- 실험 설계

**협업자**:
- Charlie (advisor)
- Teja (paper 협업)
- Scott, Vikash (방법론)

**관련 노트**:
```dataview
LIST  
FROM "Atlas/3-명량-협업"
WHERE contains(file.content, "베이지안") OR contains(file.content, "창업")
```

---

### 👾 노량: 임팩트

**학술 기여**:
- Second paper 준비
- StanCon 발표
- 방법론 패키지 개발

**실무 기여**:
- 창업가를 위한 의사결정 도구
- 베이지안 교육 자료

---

## 🎯 주요 프레임워크

### 1. Oil Framework
```
Precision (τ) × Promise (ρ) = Venture Value (V)

저정밀-큰약속 → Nail stage (탐색)
고정밀-작은약속 → Scale stage (활용)
```

[[Atlas/2-한산-전략/Oil-Framework|→ Oil Framework 상세]]

### 2. 베이지안 의사결정
```
P(Strategy|Data) ∝ P(Data|Strategy) × P(Strategy)

Posterior       Likelihood      Prior
```

### 3. 진화적 창업
```
Variation → Selection → Retention
   ↓           ↓            ↓
 실험       피드백        학습
```

---

## 📚 핵심 문헌

### 베이지안 방법론
- [[Gelman]] - Bayesian Data Analysis
- [[McElreath]] - Statistical Rethinking
- [[Carpenter]] - Stan Development

### 창업 연구  
- [[Gans]] - Strategic Entrepreneurship
- [[Scott Stern]] - Innovation Strategy
- [[Charlie Fine]] - Clockspeed Theory

---

## 🔄 연구 진행 상태

```dataview
TABLE
  전장 as "Stage",
  상태 as "Status",
  다음단계 as "Next"
FROM "Efforts"
WHERE contains(file.content, "베이지안") OR contains(file.content, "창업")
```

---

## 💡 통찰 메모

### 최근 깨달음
- 정밀도와 약속의 tradeoff는 exploration-exploitation과 유사
- 베이지안 업데이트는 피봇의 수학적 표현
- Prior는 founder's conviction, Evidence는 market feedback

### 다음 탐구 질문
- [ ] 어떻게 prior를 quantify할 것인가?
- [ ] 피봇을 베이지안 업데이트로 모델링?
- [ ] 시계열 데이터로 precision trajectory 추적?

---

## 🔗 연결

**상위**:
- [[Home|전장 사령부]]
- [[4전장|전장 흐름]]

**관련 주제**:
- [[Atlas/2-한산-전략/베이즈창업|베이즈창업 폴더]]
- [[Atlas/2-한산-전략/진화창업|진화창업 폴더]]
- [[Efforts/Ongoing/베이지안-창업-연구|진행 중인 작업]]

**사람**:
- [[Charlie Fine|Charlie]] - Advisor
- [[Teja Prayaga|Teja]] - 공동연구
- [[Scott Stern|Scott]] - 창업 멘토
- [[Vikash Mansinghka|Vikash]] - 베이지안 멘토

---

*"사전믿음을 가지되, 증거에 겸손하라"*
