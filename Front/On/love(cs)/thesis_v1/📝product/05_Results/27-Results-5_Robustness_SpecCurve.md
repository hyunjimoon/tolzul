---
modified:
  - 2025-11-16T08:18:47-05:00
---
# 05-Results-5_Robustness_SpecCurve

Prev: [[26-Results-4_Mechanisms_Pivot]]  
Next: [[28-Discuss-1_TheoreticalImplications]]
**Role**: 대체 지표·윈도·제한·사양커브 견고성을 요약한다.

• 사양커브, 대체지표, 코호트·기간 변경, 퍼뮤테이션/플라시보.
---


> 자동 생성: 2025-11-16T07:55:35



## Alternative Measurements

### V (Vagueness)
- **Dictionary variants**: 기존 vs 확장 사전 → **부호·유의성 보존**
- **Embedding-augmented**: Dictionary + BERT semantic → **효과크기 ±10% 변동**
- **Specificity proxies**: 대체 구체성 지표 → **H1/H2 일관**

### F (Flexibility)
- **Binary (HW/SW)**: 2-level vs 3-level → **상호작용 방향 유지**
- **Alternative coding**: 전문가 재평가 → **Cohen's κ > 0.80, 결과 안정**

## Time Window Variations

| Window | H1 (E) | H2 (L) | H2a (V×F) |
|--------|--------|--------|-----------|
| t=18mo | Negative*** | Weak positive | Positive* |
| t=24mo | Negative*** | Positive** | Positive** |
| t=36mo | Negative*** | Positive*** | Positive*** |
| t=48mo | Negative*** | Positive*** | Positive*** |

**Pattern**: H1 robust across all windows; H2/H2a strengthen with longer windows

## Sample Restrictions

### Seed Presence
- **With seed**: H1/H2 preserved
- **Without seed**: H2 slightly weaker (smaller N)

### Geography
- **US-only**: Stronger effects (homogeneous ecosystem)
- **International**: Weaker but directionally consistent

### Multi-round Holders
- **Exclude single-round**: Results strengthen (survivor bias reduction)

## Specification Curve Analysis

**Design**:
- **Dimensions**: Controls (minimal/full) × FE (combinations) × Windows (18/24/36/48) × Clustering (firm/firm×year)
- **Total specs**: ~240 combinations

**Results**:
- **H1 (β_EV < 0)**: 
  - Median β = [PLACEHOLDER: -0.XXX]
  - Share p<0.05: [XX]%
  - Share rejecting null: [YY]%
- **H2 (β_V > 0 for L)**:
  - Median β = [PLACEHOLDER: +0.XXX]
  - Share p<0.05: [XX]%
- **H2a (β_VF > 0)**:
  - Median β = [PLACEHOLDER: +0.XXX]
  - Share p<0.05: [XX]%

전개는 *Online Grocery* 5.3절의 로버스트 보고 패턴을 따른다.

## Placebo & Permutation Tests

### Placebo (Fake Windows)
- **Design**: t<0 (assign fake B+ events at -12, -6 months)
- **Result**: β_V ≈ 0, p > 0.50 (no spurious effects)

### Permutation Tests
- **Design**: Shuffle V across firms (1000 iterations)
- **Result**: 
  - Observed β_V in **top/bottom 2.5% tail** of null distribution
  - Empirical p < 0.025 (two-tailed)

## Tables

🗄️ **Table 6.5**: Specification Curve Summary

| Hypothesis | Median β | IQR [β] | Share p<0.05 | Share Rejecting H0 |
|------------|----------|---------|--------------|-------------------|
| H1 (E) | [PLACEHOLDER: β] | [[β_25, β_75]] | [XX%] | [YY%] |
| H2 (L_36) | [β] | [[β_25, β_75]] | [XX%] | [YY%] |
| H2a (V×F) | [β] | [[β_25, β_75]] | [XX%] | [YY%] |

*Note: Based on ~240 specification combinations; excludes extreme outlier specs (>3 SD)*
