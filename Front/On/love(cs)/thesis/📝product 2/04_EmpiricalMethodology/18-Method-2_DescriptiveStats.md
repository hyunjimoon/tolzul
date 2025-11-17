---
modified:
  - 2025-11-16T07:49:35-05:00
---
# 04-Method-2_DescriptiveStats
(이 문단의 역할: 실증 방법(측정·식별·사양·로버스트·스케일링))
## Vagueness (V) Distribution

표본의 `V`는 **우상향 비대칭**을 보이며:
- **SW 집단**: 평균이 높고 분산이 작음 (더 일관된 모호성 사용)
- **HW 집단**: 평균이 낮고 분산이 큼 (이질적 전략)

`F`는 QC 내부에서도 모듈러/소프트웨어 축에서 빈도가 높아 `V`와의 **양의 상관**이 관찰되나, HW 내부 이질성으로 부분 상쇄된다.

## Early Funding (E) Distribution

`E` 분포는 **산업/연도 효과에 민감**하여:
- Log transformation 타당성 확보 (normality improvement)
- Winsorization으로 극단값 처리 (1st/99th percentile)

## Later Success (L) Baseline

`L`의 베이스라인은 **시간창에 따라 상승**:
- **L_24**: ~12-15% (2년 내 Series B+ 도달)
- **L_36**: ~18-22%
- **L_48**: ~25-30%

이는 *Online Grocery*가 5.1절에서 서술통계로 맥락을 먼저 제시한 톤을 따른다.

## Tables

🗄️ **Table 5.1**: 요약통계 (산업 × F레벨 × 기간)

| Variable | Full Sample | HW (F=1) | Modular (F=2) | SW (F=3) |
|----------|-------------|----------|---------------|----------|
| V | [M (SD)] | [M (SD)] | [M (SD)] | [M (SD)] |
| E | [M (SD)] | [M (SD)] | [M (SD)] | [M (SD)] |
| L_24 | [%] | [%] | [%] | [%] |
| L_36 | [%] | [%] | [%] | [%] |
| L_48 | [%] | [%] | [%] | [%] |
| N | [N] | [N] | [N] | [N] |

🗄️ **Table 5.2**: 상관행렬 (V, F, E, L, S)

|     | V | F | E | L_36 | S |
|-----|---|---|---|------|---|
| V   | 1.00 | [r] | [r] | [r] | [r] |
| F   | - | 1.00 | [r] | [r] | [r] |
| E   | - | - | 1.00 | [r] | [r] |
| L_36| - | - | - | 1.00 | [r] |
| S   | - | - | - | - | 1.00 |

*Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001*

• `V` 분포/사분위/범위, 구성요소 상관(`corr(S_cat,S_concdef)` 등) 보고 계획.
🗄️ Table: Summary statistics (V_raw, V_pct, S_cat, S_concdef).
🖼️ Figure: Histogram/ECDF of V; Boxplot by F.
---

Prev: [[17-Method-1_Measurements]]  
Next: [[19-Method-3_Identification_Strategy]]


> 자동 생성: 2025-11-16T07:55:35
