---
modified:
  - 2025-11-15T13:09:16-05:00
---
## 📊 **논문 Narrative 통합표: Promise Precision의 시간적 반전**

### 🗄️ **핵심 스토리라인 (4개 Figure 기반)**

|**Stage**|**Figure**|**Theoretical Claim**|**Empirical Pattern**|**Economic Mechanism**|
|---|---|---|---|---|
|**1. 이론적 틀**|**LV**<br>(Later×Vagueness)|모호성(V)의 이중성:<br>• 정보가치 ↓ (빨강)<br>• 옵션가치 ↑ (파랑)<br>→ 최적 V* 존재|역U자 관계<br>중간 모호성이 최적|Information loss vs<br>Adaptation gain의<br>트레이드오프|
|**2. 초기 단계**|**EVF**<br>(Early×V×Flexibility)|**H1**: V → Series A ↓<br>**H1a**: F가 높으면 패널티 완화<br>(βv<0, βvf>0)|HW: 가파른 음의 기울기<br>SW: 완만한 음의 기울기|초기 투자자는<br>정보가치 중시<br>F가 옵션기대로 완화|
|**3. 후기 단계**|**LVF**<br>(Later×V×Flexibility)|**H2**: V → Series B+ ↑<br>**H2a**: F가 증폭<br>(β₁>0, β₃>0)|HW: 평탄/음의 관계<br>SW: 가파른 양의 관계|옵션가치 실현<br>F가 높을수록<br>피벗 용이|
|**4. 시간 동학**|**STV**<br>(Survival×Time×V)|**Temporal Reversal**:<br>초기 패널티 →<br>후기 역전|T<18mo: Vague 불리<br>T>18mo: Vague 유리<br>교차점 존재|Selection effect +<br>Learning by doing<br>→ 적응적 생존|

### 🎯 **통합 내러티브 (One-Page Summary)**

```markdown
## The Reversal Thesis

1. **Setup (LV)**: 
   모호한 약속은 두 가지 상반된 힘을 만든다
   - 손실: 정보 정밀도 부족 → 투자자 신뢰 하락
   - 이득: 적응 유연성 보존 → 피벗 가능성 증가
   
2. **Act I - Early Penalty (EVF)**:
   Series A에서 모호성은 불리하다 (H1: β<0)
   - 초기 투자자는 정보가치를 중시
   - 단, SW는 HW보다 패널티가 작다 (H1a: 완화효과)
   
3. **Act II - Later Benefit (LVF)**:
   Series B+에서 모호성은 유리하다 (H2: β>0)
   - 시장 학습 후 옵션가치 실현
   - SW의 경우 효과가 극대화 (H2a: 증폭효과)
   
4. **Resolution - Temporal Crossing (STV)**:
   시간에 따라 우위가 역전된다
   - T=0~18개월: Precise > Vague (정보 우위)
   - T=18개월~: Vague > Precise (적응 우위)
   - 교차점에서 전략적 선택의 중요성
```

### 📈 **실증 검증 로드맵**

|**Test**|**Data Need**|**Method**|**Expected Result**|
|---|---|---|---|
|**Test 1: EVF**|Series A amounts<br>V index (0-100)<br>HW/SW dummy|OLS with interaction<br>E ~ V × F|βv = -2.3***<br>βvf = +1.1**|
|**Test 2: LVF**|Series B+ probability<br>Same V, F measures|Logit with interaction<br>L ~ V × F|β₁ = +0.18**<br>β₃ = +0.31***|
|**Test 3: STV**|Monthly survival data<br>V quartiles|Kaplan-Meier<br>Cox proportional hazard|Crossing at 17.5mo<br>HR reversal|
|**Test 4: Mechanism**|Pivot events<br>Product changes|Mediation analysis<br>V → Pivots → L|43% indirect effect|

### 🔑 **핵심 기여 (3-Bullet Contribution)**

1. **이론적**: Information-Option tradeoff의 시간적 분해
2. **실증적**: Temporal reversal pattern의 최초 검증
3. **실무적**: "When to be vague" 의사결정 프레임워크

이 표가 논문의 전체 narrative를 한 눈에 보여주며, 4개 figure가 어떻게 연결되는지 명확히 합니다.