---
담당: 권준 (Gwon Jun) - 논리적 구조화와 모델 구축
역할: 승(承) - 이론 전개와 가설 도출
modified:
  - 2025-11-22T06:43:43-05:00
---

# Meta-Prompt for Conceptual Model & Data Overview Section

## Your Mission
이론적 프레임워크를 정교화하고, 검증 가능한 가설을 도출하며, 실증 분석을 위한 데이터 구조를 제시하세요. Scott Stern의 '수렴적 학습'과 Charlie Fine의 '측정 가능한 시스템'을 동시에 만족시켜야 합니다.

## Section 1: Conceptual Framework - The 2x2 Matrix

### Core Framework Visualization
```
         Low Flexibility (F=0)    High Flexibility (F=1)
         Hardware/Physical         Software/Digital
    ┌─────────────────────────┬─────────────────────────┐
    │  Quadrant 1: SIGNAL     │  Quadrant 2: HEDGE      │
Low │  전통 제조업 모델         │  하이브리드 전략         │
 V  │  (Bosch, Continental)   │  (Waymo, Cruise)        │
    │  E↑ L→                  │  E→ L↑                  │
    ├─────────────────────────┼─────────────────────────┤
    │  Quadrant 3: STRUGGLE   │  Quadrant 4: OPTION     │
High│  최악의 조합             │  전략적 모호성           │
 V  │  (Better Place, Fisker) │  (Tesla, Uber)          │
    │  E↓ L↓                  │  E↓ L↑↑                 │
    └─────────────────────────┴─────────────────────────┘
```

### Module-Specific Contingencies
각 모듈(Customer, Technology, Organization, Competition)이 V-F 관계를 어떻게 조절하는지 명시

## Section 2: Formal Model Sketch

### Setup
- 창업자 i는 약속 정밀도 τᵢ ∈ [0,1] 선택
- 투자자는 τᵢ 관찰 후 투자 결정
- 시장 불확실성 σ는 시간에 따라 변화

### Early Stage (t=0): Information Value
```
P(Funding|τ) = α₀ + α₁τ + α₂X + ε
where α₁ > 0 (specificity premium)
```

### Later Stage (t=1): Option Value  
```
P(Success|τ,σ) = β₀ + β₁(1-τ) + β₂σ + β₃(1-τ)×σ + ε
where β₃ > 0 (flexibility value under uncertainty)
```

### Key Mechanism: Learning & Pivoting
- High τ → Commitment → Limited learning
- Low τ → Flexibility → Pivot option → Better product-market fit

## Section 3: Hypothesis Development

### H1: Early Funding Penalty
**Statement**: "Ventures with vaguer value propositions receive less early-stage funding"
```
H1: α₁ < 0 in P(Series A) = α₀ + α₁×Vagueness + Controls
```
**Logic**: Information asymmetry → Investors prefer specificity as quality signal

### H2: Later Success Benefit
**Statement**: "Ventures with vaguer value propositions have higher later-stage success"
```
H2: β₁ > 0 in P(Series B+) = β₀ + β₁×Vagueness + Controls
```
**Logic**: Flexibility → Adaptation → Better survival

### H2a-d: Contingent Effects (4 Modules)
```
H2a (Customer): β₃ > 0 when Customer_Heterogeneity is high
H2b (Technology): β₃ > 0 when Tech_Uncertainty is high  
H2c (Organization): β₃ > 0 when Org_Ambidexterity is high
H2d (Competition): β₃ > 0 when Market_Dynamism is high
```

## Section 4: Data Context - Mobility/AV Industry

### Why Mobility? The Perfect Laboratory
1. **High uncertainty**: Regulatory, technology, business model all in flux
2. **Clear outcomes**: Funding rounds, exits, failures well-documented
3. **Rich variation**: Hardware (Waymo) vs Software (Mobileye)
4. **Recent history**: 2010-2024 complete cycle observable

### Industry Statistics
- Total ventures: ~450 mobility/AV startups
- Total funding: $120B+ (2010-2024)
- Success rate: 8% reach Series C+
- Key segments: Autonomous, Sharing, Electric, Logistics

## Section 5: Sample Construction

### Data Sources
1. **Primary**: Crunchbase (funding), PitchBook (exits)
2. **Secondary**: USPTO (patents), LinkedIn (teams)
3. **Text**: Pitch decks, websites, press releases

### Inclusion Criteria
- Founded 2010-2020 (complete observation window)
- Mobility/AV/Transportation primary sector
- Raised seed/Series A (active ventures only)
- English-language materials available

### Final Sample
- N = 326 ventures
- Software: 198 (61%)
- Hardware: 128 (39%)
- Mean funding: $47M
- Mean vagueness: 0.42 (SD=0.18)

## Section 6: Variable Definitions

### Dependent Variables
| Variable | Definition | Measurement | Mean(SD) |
|----------|-----------|-------------|----------|
| **E** (Early) | Series A success | Binary: 1 if raised | 0.34(0.47) |
| **L** (Later) | Series B+ or exit | Binary: 1 if achieved | 0.21(0.41) |

### Independent Variables  
| Variable | Definition | Measurement | Mean(SD) |
|----------|-----------|-------------|----------|
| **V** (Vagueness) | Promise ambiguity | NLP score [0,1] | 0.42(0.18) |
| **F** (Flexibility) | Adaptability | 1 - is_hardware | 0.61(0.49) |

### Control Variables
- Founder experience (serial entrepreneur)
- Team size (LinkedIn profiles)
- Patent count (USPTO)
- Market timing (founding year FE)
- Geographic location (Bay Area dummy)

## Output Requirements
- **Length**: 2000-2500 words total
- **Figures**: 
  - Fig 1: 2x2 conceptual framework
  - Fig 2: Timeline diagram (Early vs Later)
- **Tables**:
  - Table 1: Variable definitions
  - Table 2: Descriptive statistics
  - Table 3: Correlation matrix

## Key Mathematical Notation
- τ (tau): Promise precision [0,1]
- σ (sigma): Market uncertainty
- μ (mu): Entrepreneur's aspiration level
- θ (theta): True market state
- π (pi): Profit function

Charlie와 Scott이 모두 만족할 수 있도록, 엄밀한 논리와 측정 가능한 구조를 구축하세요!