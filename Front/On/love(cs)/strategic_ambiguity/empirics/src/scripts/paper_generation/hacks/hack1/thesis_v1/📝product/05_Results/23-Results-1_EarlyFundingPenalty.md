---
modified:
  - 2025-11-16T08:14:40-05:00
---
# 05-Results-1_EarlyFundingPenalty

(이 문단의 역할: H1 메인 결과를 보고하고 경제적 크기를 해석한다.)

모형 A에서 `V`의 계수는 **음(-)**이며 통계적으로 유의하다. `V` 1 SD 증가 시 `E`가 **x–y% 감소(로그)**하며, HW 집단에서 기울기가 더 가파르다. 초기 투자자의 **정보가치** 중시와 정합적이다.

![[Fig2_EVF_EarlyFunding_vs_V_by_Flex.png]]

**Figure 2**: Series A 금액(로그)과 모호성의 관계. 유연성 낮을수록 음의 기울기 증폭.

![[T1_ModelA_EarlyFunding]]

---

**Prev:** [[22-Method-6_StatPower_Scaling]]  
**Next:** [[24-Results-2_LaterSuccessBenefit]]

## Main Finding

모형 A에서 `V`의 계수 β_EV는 **음(-)**이며 통계적으로 유의하다 (Table 6.1):
- **β_EV = [PLACEHOLDER: -0.XXX]** (SE = [0.XXX], p < [0.0XX])
- **95% CI**: [[PLACEHOLDER: -0.XXX, -0.XXX]]

## Economic Interpretation

**Effect Size**:
- **1 SD ↑ in V** → **[x–y]% 감소** in log(E)
- **Dollar terms**: 
  - Median Series A: $[X]M → $[Y]M
  - IQR range: $[A]M – $[B]M → $[C]M – $[D]M

**Practical Significance**:
- Equivalent to **[Z] months of runway** difference
- Comparable to **[W]% reduction** in investor confidence signal

## Heterogeneity by Flexibility (F)

**HW (F=1, low flexibility)** 하위집단:
- **β_EV = [PLACEHOLDER: -0.XXX]** (SE = [0.XXX], p < [0.0XX])
- 더 가파른 패널티 → **유연성 부족 시 정보 부족의 비용 확대**

**SW (F=3, high flexibility)** 하위집단:
- **β_EV = [PLACEHOLDER: -0.XXX]** (SE = [0.XXX], p < [0.0XX])
- 패널티 완화되나 여전히 음(-) → 초기에는 정보가치 우선

전개 톤은 *Online Grocery* 5.2절의 "계수→경제적 해석→이질성 암시" 구조를 따른다.

## Tables

🗄️ **Table 6.1**: Model A—Early Funding (Dependent) Regression Results

| Variable | (1) Baseline | (2) +Controls | (3) +FE | (4) Full |
|----------|--------------|---------------|---------|----------|
| V | [PLACEHOLDER: β] | [β] | [β] | [β] |
|  | [PLACEHOLDER: (SE)] | [(SE)] | [(SE)] | [(SE)] |
| Year FE | No | No | Yes | Yes |
| Country FE | No | No | Yes | Yes |
| Sector FE | No | No | Yes | Yes |
| Controls | No | Yes | Yes | Yes |
| N | [N] | [N] | [N] | [N] |
| R² | [X.XX] | [X.XX] | [X.XX] | [X.XX] |

*Note: \* p<0.05, \*\* p<0.01, \*\*\* p<0.001. Standard errors (Firm×Year clustered) in parentheses.*
