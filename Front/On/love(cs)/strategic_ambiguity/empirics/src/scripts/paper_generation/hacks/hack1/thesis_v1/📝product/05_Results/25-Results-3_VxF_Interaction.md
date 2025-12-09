---
modified:
  - 2025-11-16T08:16:21-05:00
---
# 05-Results-3_VxF_Interaction

**Prev:** [[24-Results-2_LaterSuccessBenefit]]  
**Next:** [[26-Results-4_Mechanisms_Pivot]]
**Role**: H2 결과와 시간역전(LTV)을 요약한다.

`V×F` 상호작용은 **양(+)**이며 유의. SW에서 `V`의 기울기가 **음→양** 전환. 옵션 행사가능성 확보 시에만 모호성의 자산성이 실현됨을 시사.

![[Fig3_LVF_LaterSuccess_vs_V_by_Flex.png]]

**Figure 3 (재참조)**: SW(파란색)는 양의 기울기, HW(빨간색)는 음/평탄. H2a 핵심 증거.

---

## Main Finding

모형 B의 평균 마진에서 `V`는 후기성공 `L`에 **정(+)의 한계효과**를 보이며, 창(`t`)이 길수록 효과가 강화된다:

- **β_V (L_24)** = [PLACEHOLDER: +0.XXX] (SE = [0.XXX], p = [0.0XX])
- **β_V (L_36)** = [PLACEHOLDER: +0.XXX] (SE = [0.XXX], p < [0.0XX])
- **β_V (L_48)** = [PLACEHOLDER: +0.XXX] (SE = [0.XXX], p < [0.0XX])

## Time Reversal Pattern (LTV)

초기의 정보열세가 **학습·적응을 거치며 옵션가치 실현**로 전환되는 **시간 역전**을 시사:
- **t=24mo**: 효과 약함 또는 비유의 (학습기간 미흡)
- **t=36mo**: 효과 출현 (피벗/확장 실행 구간)
- **t=48mo**: 효과 강화 (옵션행사 완료)

## Economic Interpretation

**1 SD ↑ in V** →
- **L_36 예측확률**: [a–b]%p 증가
- **Baseline comparison**: [baseline %] → [new %]
- **Practical significance**: 
  - Top quartile V: [X]% survival to Series B+
  - Bottom quartile V: [Y]% survival
  - Difference: [X-Y]%p advantage

## Subgroup Analysis

본 패턴은 **SW/모듈러 집단에서 더 두드러짐**:
- **SW (F=3)**: β_V = [PLACEHOLDER: +0.XXX], p < 0.001
- **HW (F=1)**: β_V = [PLACEHOLDER: +0.XXX], p > 0.05 (non-sig or weaker)

## Figures

[[LVF_VTV_FLTV 2025_11_15.excalidraw]]
🖼️ **Figure 6.1**: LTV (Time Reversal Pattern)
- **X-axis**: Relative time since Series A (months)
- **Y-axis**: Predicted P(L=1) - Marginal effect of V
- **Color**: V quartiles (Q1-Q4)
- **Pattern**: Negative → Neutral → Positive trajectory

## Tables

🗄️ **Table 6.2**: Model B—Later Success (Logit) Regression Results

| Variable | L_24 | L_36 | L_48 |
|----------|------|------|------|
| V | [PLACEHOLDER: β] | [β] | [β] |
|  | [(SE)] | [(SE)] | [(SE)] |
| F | [β] | [β] | [β] |
|  | [(SE)] | [(SE)] | [(SE)] |
| V×F | [β] | [β] | [β] |
|  | [(SE)] | [(SE)] | [(SE)] |
| Controls | Yes | Yes | Yes |
| FE | Yes | Yes | Yes |
| N | [N] | [N] | [N] |
| Pseudo R² | [X.XX] | [X.XX] | [X.XX] |

*Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001. Odds ratios available in appendix.*

---

**Navigation**:
- [[이전: 01_EarlyPenalty.md]]
- [[다음: 03_VxF_Interaction.md]]
