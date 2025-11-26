---
modified:
  - 2025-11-16T13:41:30-05:00
---

• 목적함수 스케치: `max_V  [Info(V)↓ + Opt(V;F)↑] − C(V)`.
• 예측: 초기엔 정밀성 선호, 후기엔 옵션가치 실현 가능(F↑) 시 모호성의 순효과 ↑.
---



# 03-Concept-2 FormalModel — Minimal Objective (loss form)

Prev: [[11-Concept-1_Framework_2x2]]  
Next: [[13-Concept-3_Hypotheses]]
**목표:** H1/H2/H2a의 **가장 단순하고 식별 친화적인** 목적함수.

## Minimal Objective (log-additive; loss sign)

\[
\max_{V\in(0,1)}\; J(V;F)
\;=\; \underbrace{F\,\log V}_{\text{옵션(유연성) — blue}}
\;-\; \underbrace{\mathrm{InfoLoss}(V)}_{\text{정보손실(평가패널티) — red}},
\qquad \mathrm{InfoLoss}(V)\equiv -\log(1-V).
\]

- **동치표현(단조변환):** 위 목적함수는 \(\max_V \log\big[(1-V)\,V^F\big]\)와 동치 ⇒ 곱형 \((1-V)\,V^F\)과 **같은 최적해**.  
- **일차조건(FOC):** \(\tfrac{F}{V}-\tfrac{1}{1-V}=0\Rightarrow V^*(F)=\tfrac{F}{F+1}\).  
- **이차조건:** \(-F/V^2-1/(1-V)^2<0\) ⇒ **단봉형**(내부 최대).  
- **비용항 \(C(V,F)\)**: **불포함**(상수로 흡수). 핵심 검정(H1/H2/H2a)엔 불필요.

## 두-청중(조직 vs. 시장) 분리

- **시장/평가자(초기)**: \(\mathrm{InfoLoss}(V)\) ↑ ⇒ **E↓ (red)**  
- **조직/운영(후기)**: \(F\log V\) ↑ ⇒ **L↑ (blue)**  
- **식별 원칙:** 정보항은 **F-비의존**, 교차효과는 **옵션항**에서만 발생.

![[12-Concept-2_FormalModel_Sketch 2025_11_16.excalidraw]]

- **Figure 1 (LV)**: red(정보가치), blue(옵션가치), green(\(V^*\)), skyblue(행사가능성 주석), pink(Angie’s doubt band).  
- **Figure 2 (EVF)**: red 곡선(초기펀딩) **F-비의존**. green: \(V^*\) 표식.  
- **Figure 3 (LVF)**: blue 곡선 2개(저/고 F), green: 각 \(V^*\), skyblue 주석.


창업팀의 선택은 다음과 같이 요약된다:

```
max_V { Opt(V;F) – InfoLoss(V) – C(V) }
```

여기서 `Opt(V;F)`는 `F`(행사가능성; 매칭/재구성/거버넌스/실험비용의 함수)가 높을수록 더 가파르게 증가하며, `InfoLoss(V)`는 `V`가 클수록 커져 초기 평가를 악화시킨다. 

두-청중 해석에서:
- **조직(적응/학습)**: `Opt(V;F)`를 중시 → 유연성 확보
- **시장/생태계(선택/옵션행사)**: `InfoLoss(V)` 축소를 중시 → 정밀성 요구

"항상 정밀/항상 모호" 전략은 `F`에 따라 지배열세가 발생하므로 배제된다. 

이 직관은 W2 정리 및 VOI 노트의 **행사가능성 기반 `V*` 존재**와 부합한다.

## Mathematical Representation

**Optimal Vagueness** (from VOI framework):
```
V* = F/(F+1)
```

Thm1. founder's choice of vagueness (`V`) as an optimization problem. It frames the objective as maximizing the joint probability of a successful information outcome (clarity for investors, modeled as `1-V`) and a successful option outcome (flexibility for the team, modeled as `V^F`). Solving this trade-off yields the optimal level of vagueness (`V*`) as a direct function of the option's exercisability (`F`), P(I=1, O=1|V)= P(I=1|V) P(O=1|V) = (1-V) V^F . V* = F/(F+1)

Where:
- `VOI` = Value of Information (learning benefit)
- `i` = Integration/Commitment cost
- Ratio `VOI/i` determines commitment timing
