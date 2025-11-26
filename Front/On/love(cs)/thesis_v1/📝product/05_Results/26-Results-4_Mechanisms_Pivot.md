---
modified:
  - 2025-11-16T08:17:36-05:00
---
# 05-Results-4_Mechanisms_Pivot

**Prev:** [[25-Results-3_VxF_Interaction]]  
**Next:** [[27-Results-5_Robustness_SpecCurve]]
**Role**: 피벗·재구성 메커니즘의 보조 증거를 제시한다.

텍스트/깃허브/특허/채용 전환 등 **재구성 신호**를 결합하면 `V` 고분위 기업에서 **피벗 빈도**가 더 높고, `L`과 **부분 매개**한다. `V`가 **옵션 보전→실행** 경로로 후기 성과에 연결됨을 시사.

*(Figure 4 참조: 시간 추이 생존율 역전은 적응/피벗 메커니즘과 일관)*

![[T_Mech]]

---



## Pivot/Reconfiguration Signals

promise text의 변화폭 측정. 텍스트/깃허브 릴리즈/특허·채용 전환 등 **재구성 신호**를 결합하면:

### High-V Firms Show More Pivots
- **Pivot frequency** (텍스트 기반 전략변화 탐지): 
  - High V (Q4): [X]% pivot rate
  - Low V (Q1): [Y]% pivot rate
  - Difference: [X-Y]%p, p < 0.05

### Pivot Mediates V→L Relationship
- **Indirect effect** (Baron-Kenny mediation):
  - Direct V→L: β = [PLACEHOLDER: +0.XXX]
  - V→Pivot: β = [PLACEHOLDER: +0.XXX]
  - Pivot→L: β = [PLACEHOLDER: +0.XXX]
  - **Mediation**: ~[XX]% of V→L effect via pivot pathway

### Heterogeneity by F
- **SW firms**: Pivot signal stronger (easier to detect/execute)
- **HW firms**: Pivot signal weaker or absent (higher reconfiguration costs)

## Interpretation

이는 `V`가 **옵션 보전→실행**의 경로를 통해 후기 성과로 연결됨을 시사한다. 

다만 측정 잡음/이질적 공개 관행으로 인해 메커니즘 추정은 **정성+정량 혼합**으로 보고한다:
- **Quantitative**: 텍스트/GitHub 기반 전환 빈도
- **Qualitative**: 케이스 스터디 (예: Zapata Computing, Rigetti pivot paths)

## Limitations

- **Selection bias**: 공개하지 않은 피벗 누락
- **Measurement error**: 텍스트 기반 피벗 정의의 타당성
- **Reverse causality**: 성공→회고적 피벗 서술 가능성

→ 결과 해석에서 **보조 증거**로만 활용 (인과 주장 제한)

## Tables

🗄️ **Table 6.4**: Mechanism Regression Summary (Mediation/Moderation)

| Path | β | SE | p | 95% CI |
|------|---|----|----|--------|
| V → L (direct) | [β] | [SE] | [p] | [[CI]] |
| V → Pivot | [β] | [SE] | [p] | [[CI]] |
| Pivot → L | [β] | [SE] | [p] | [[CI]] |
| V → L (indirect via Pivot) | [β] | [SE] | [p] | [[CI]] |
| Mediation % | [X%] | - | - | [[CI]] |

*Note: Sobel test for indirect effect; bootstrapped CI (1000 iterations)*
