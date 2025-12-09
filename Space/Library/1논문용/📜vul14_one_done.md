---
collection:
  - "[[Space/Lab/Papers]]"
author_ids:
field:
  - 👾cog
year: 2014
created: 2025-09-12
---

[[09-12|25-09-12]]

### 핵심 통찰: "One and Done"의 최적성

Vul의 주장과 우리 이론의 연결:

```
Vul: 적은 샘플로 빠른 결정 = 전역 최적
우리: 낮은 τ로 빠른 피벗 = 생존 전략
```

### Precision과 τ의 관계

Vul의 continuous decision framework:

- σP = posterior 불확실성 (우리의 1/τ)
- σU = utility function 너비 (시장 tolerance)
- 최적 샘플 수 ∝ σU/σP

우리 모델로 번역:

```
τ* = V/(C×n) ≈ (σU/σP) × (V/C)

- σU 크면 (시장이 관대) → τ 낮춰도 됨
- σP 크면 (불확실성 높음) → τ 낮춰야 함
```

### Strategic Adjustment 증거

Vul이 보인 것:

- Stakes 높을 때 → 더 많은 samples
- 우리 모델: V 높을 때 → τ 증가

이것이 Better Place의 실패 설명:

- 높은 stakes ($850M) → 높은 τ 선택
- But 높은 n (복잡) → 낮은 τ 필요
- Mismatch → 실패