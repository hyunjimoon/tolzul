---
updated: 2025-10-25
프로젝트: 명량해전 (3주)
성장:
  - 2025-10-27T08:53:07-04:00
---

# Promise Precision and Venture Funding

**🔗 작전 지휘부**: `../../삼도수군/` (일일 순환 추적)  
**🏛️ 전투 본부**: 이 폴더 (최종 결과물)

---

## 1. Hypotheses

**H1 (Early Stage - Short-term Cost):** α₁ < 0  
😵‍💫 Vague promises hurt at first → Lower initial funding

**H2 (Later Stage - Long-term Benefit):** β₁ > 0  
😵‍💫 Vague promises benefit later → Higher survival probability

---

## 2. Data

### Source
Longitudinal data with company descriptions and funding data at early and later stages from venture databases (Pitchbook, Crunchbase, or similar).

### Sample Structure
* **Temporal**: Early-stage investments → Later-stage outcomes
* **Cross-section**: Technology ventures with detailed descriptions
* **Panel**: Same firms tracked across funding rounds
* **Target N**: ~30-75 firms with complete data

### Key Variables

| Variable | Measurement | Role |
|----------|-------------|------|
| 😵‍💫 Vagueness | Inverse of linguistic certitude (LIWC) in company description | Independent |
| 💰 Early_Funding | Funding amount at early stage ($ millions) | Dependent (Model 1) / Control (Model 2) |
| 🎯 Later_Success | Binary: 1 if raised later-stage funding, 0 otherwise | Dependent (Model 2) |
| Team_Size | Number of employees at early stage | Control |
| Prior_Exit | Founder has previous exit (binary) | Control |
| Sector | Industry category | Control |

---

## 3. Models

### Model 1: Early-Stage Funding Amount (OLS)
```
💰 Early_Funding_i = α₀ + α₁ · 😵‍💫Vagueness_i + Controls + ε_i
```
**Expected:** α₁ < 0 (vagueness → less initial funding)

### Model 2: Later-Stage Success (Logistic)
```
logit(🎯 Later_Success_i) = β₀ + β₁ · 😵‍💫Vagueness_i 
                            + β₂ · 💰Early_Funding_i + Controls + ε_i
```
**Expected:** β₁ > 0 (vagueness → better survival, controlling for early funding)

---

## 4. Expected Patterns

### Pattern A: Early Stage (Short-term Cost)
```
Funding ↑
      |
      |\
      | \
      |  \_____ 
      |____________ 😵‍💫 Vagueness →
   Precise      Vague
```
**Interpretation:** Vague descriptions → lower early-stage funding

### Pattern B: Later Stage (Long-term Benefit)  
```
Success ↑
      |        ____/
      |      /
      |    /
      |  /
      |/____________ 😵‍💫 Vagueness →
   Precise      Vague
```
**Interpretation:** Vague descriptions → higher later-stage success rate

---

## 5. Analysis Pipeline

### 파이프라인 위치
```
code/
├── 01_process_company_data.py    (데이터 추출 & 정제)
├── 02_process_deal_data.py       (펀딩 데이터 처리)
├── 03_create_panel.py            (패널 구성)
├── 04_run_analysis.py            (Model 1 & 2)
└── 05_create_deliverables.py    (Tables & Figures)
```

### 단계
1. **Data Prep**: Extract funding records, compute vagueness scores
2. **Model 1**: OLS regression (early funding ~ vagueness)
3. **Model 2**: Logistic regression (later success ~ vagueness + early funding)
4. **Visualization**: Create Pattern A & B with actual data
5. **Robustness**: Sector effects, alternative vagueness measures

---

## 6. Deliverables

| Item | 위치 | 설명 |
|------|------|------|
| **Table 1** | `output/table1_descriptive.csv` | Descriptive statistics |
| **Table 2** | `output/table2_model1.csv` | Model 1 results (early stage) |
| **Table 3** | `output/table3_model2.csv` | Model 2 results (later stage) |
| **Figure 1** | `output/figure1_early.png` | Vagueness → Early funding |
| **Figure 2** | `output/figure2_later.png` | Vagueness → Later success |

---

## 🔄 견리사의 순환 작업법

이 연구는 **삼도수군 폴더**에서 일일 순환으로 진행됩니다:

```
아침 (見)
  ↓
삼도수군/전투일지.md (계획)
  ↓
작업 (利 → 思 → 義)
  ↓
삼도수군/1_利/ (ChatGPT 프로토타입)
삼도수군/2_思/ (Claude 정교화)
삼도수군/3_義/ (Gemini 검증)
  ↓
✅ 검증 완료
  ↓
이 폴더 (empirics/)로 이동
  ↓
code/ (최종 코드)
output/ (최종 결과)
```

**일일 워크플로우**: `../../삼도수군/README.md` 참조

---

## 📅 3주 계획

### Week 1 (10.25-10.31): Data + Model 1
**목표**: Table 1, 2 완성
- Day 1-2: 데이터 파이프라인 구축
- Day 3-4: Model 1 구현
- Day 5-7: 검증 & Table 2

**산출**: `output/table1*.csv`, `output/table2*.csv`

---

### Week 2 (11.01-11.07): Model 2 + Visualization
**목표**: Table 3, Figure 1, 2 완성
- Day 8-10: Model 2 (Logistic)
- Day 11-12: 시각화
- Day 13-14: Robustness checks

**산출**: `output/table3*.csv`, `output/figure*.png`

---

### Week 3 (11.08-11.15): Paper
**목표**: 논문 초고
- Day 15-17: Introduction, Theory, Method
- Day 18-19: Results, Discussion
- Day 20-21: 최종 제출

**산출**: `../theory/paper_draft.md`

---

## 🎯 핵심 연결점

### 이론적 기반
- **OIL Framework**: τ* = max{0, √(V/4i) - 1}
- **Strategic Ambiguity**: When should ventures be vague?
- **Signaling Theory**: What do vague promises signal?

### Empirical Contribution
Promise precision has **non-monotonic effects**:
- **Short-term** (H1): Precision helps (credibility) → α₁ < 0
- **Long-term** (H2): Vagueness helps (flexibility) → β₁ > 0

---

## 🚨 막힐 때

### 연구 설계 질문
→ 이 파일 재독

### 일일 작업 막힘
→ `../../삼도수군/README.md`

### 코드 문제
→ `code/PIPELINE_GUIDE.md`

---

**"신에게는 아직 12척의 배가 있습니다"**

**이 workflow는 우리의 지도입니다** 🗺️
