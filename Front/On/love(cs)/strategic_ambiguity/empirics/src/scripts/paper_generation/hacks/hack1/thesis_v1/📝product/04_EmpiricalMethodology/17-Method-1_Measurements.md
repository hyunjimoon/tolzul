---
modified:
  - 2025-11-16T16:31:41-05:00
---
# 04-Method-1_Measurements

(이 문단의 역할: 실증 방법(측정·식별·사양·로버스트·스케일링))

• 텍스트 파이프라인: 문장 토큰화 → S_cat(모호어 사전) + S_concdef(숫자/스펙/기한 부재 패널티).
• 결합식: `V_raw = 0.5·max(S_cat,S_concdef) + 0.5·mean(S_cat,S_concdef)` → [0,1] 스케일.
• `V_pct`: 표본 경험적 CDF 매핑. *Lexical uncertainty* 컴포넌트 제거(연구사양).
• F: HW/SW 및 옵션레벨(1–3) 분류 개요. E/L/S: 정의·변환·윈도우.
---

Prev: [[16-DataOverview-3_Variables_Overview]]  
Next: [[18-Method-2_DescriptiveStats]]


> 자동 생성: 2025-11-16T07:55:35

**Role**: 측정 구성과 통제/고정효과를 명시한다.

## Vagueness (V) Measurement

**Text Processing**:
1. **Tokenization**: 공개 약속 문서를 문장 단위로 분할
2. **Dictionary Matching**: 
   - (i) 모호어 사전 기반 빈도 (vague category terms)
   - (ii) 구체성 결핍 탐지 (absence of: numbers/specs/deadlines)
3. **Normalization**: 문장 수·문서 길이로 정규화
4. **Composite Index**: (i) + (ii) 가중 합성 → 0-100 스케일 → 0-1 정규화

**Validation**:
- Inter-rater reliability (전문가 이중 코딩, κ > 0.75)
- Convergent validity (대체 지표와 상관 r > 0.6)

We adopt the Hybrid scorer combining linguistic vagueness features with inverse concrete feature counts, which provides superior discriminatory power (IQR=8.97) and avoids score concentration while maintaining theoretical grounding in both rhetorical patterns and substantive content. [pr](https://github.com/hyunjimoon/empirics_ent_strat_ops/pull/6)
## Flexibility (F) Measurement

**Classification**:
- **Text-based**: HW/SW 키워드 분류
- **Architecture-based**: QC 전문가 3-level coding
  - **F=1** (Rigid HW): Superconducting, trapped ion
  - **F=2** (Modular HW): Photonic, topological
  - **F=3** (Software): Algorithms, simulators

or

| Original Sector | → | Binary Category | Rationale |
|----------------|---|-----------------|-----------|
| **Hardware/Robotics** | → | **HW (1)** | Physical products, high integration cost |
| **Biotech/Healthcare** | → | **HW (1)** | Lab equipment, clinical trials, FDA approval |
| **AI/ML Software** | → | **SW (0)** | Algorithms, cloud deployment |
| **FinTech** | → | **SW (0)** | APIs, payment processing |
| **Data/Analytics** | → | **SW (0)** | Software platforms |
| **Enterprise Software** | → | **SW (0)** | SaaS, B2B tools |
| **Consumer Software** | → | **SW (0)** | Apps, gaming, social |

**Robustness**:
- Binary HW/SW (F=1,2 vs F=3)
- Alternative weighting schemes

## Outcome Measurements

### E (Early Funding)
- **Source**: PitchBook Series A amount (USD)
- **Transformation**: log(E), base year 2020 CPI adjustment
- **Winsorization**: 1st/99th percentile to handle outliers

### L (Later Success)
- **Definition**: Binary indicator (Series B+ within t months)
- **Windows**: t ∈ {24, 36, 48}
- **Modeling**: Logit (cohort-level fixed effects)

### S (Step-up Ratio)
- **Definition**: PreMoney_{t+1} / PostMoney_t
- **Restriction**: **Survivors only** (conditional on Series B+)
- **Use**: Auxiliary analysis only (no causal claims)

## Control Variables & Fixed Effects

**Fixed Effects**:
- **연도 FE**: Year of Series A (2019-2024)
- **국가 FE**: HQ country (US/EU/Asia/Other)
- **세부분야 FE**: QC sub-sector (annealing/gate/measurement)
- **A-라운드 월 FE**: Month of Series A (seasonal effects)

**Continuous Controls**:
- Founder history (serial/exit experience)
- Investor composition (VC tier, strategic/corporate presence)
- Team size at Series A
- Patent count at baseline

**Standard Errors**:
- **Firm × Year** double clustering (primary specification)
- Alternative: Firm-level clustering
