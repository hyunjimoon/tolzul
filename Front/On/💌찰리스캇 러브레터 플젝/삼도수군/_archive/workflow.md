---
updated: 2025-10-25
전투계획: 명량해전 3주 프로젝트
---

# Promise Precision and Venture Funding

## 1. Hypotheses

**H1 (Early Stage - Short-term Cost):** α₁ < 0  
😵‍💫 Vague promises hurt at first → Lower initial funding

**H2 (Later Stage - Long-term Benefit):** β₁ > 0  
😵‍💫 Vague promises benefit later → Higher survival probability

---

## 2. Data

### Source
Longitudinal data with company descriptions and funding data at early and later stages from venture databases (e.g., Pitchbook, Crunchbase, or similar sources).

### Sample Structure
* **Temporal span**: Early-stage investments → Later-stage outcomes
* **Cross-section**: Technology ventures with detailed descriptions
* **Panel structure**: Same firms tracked across funding rounds

### Key Variables

| Variable | Measurement | Role |
|----------|-------------|------|
| 😵‍💫 Vagueness | Inverse of linguistic certitude in company descriptions | Independent |
| 💰 Early_Funding | Funding amount at early stage | Dependent (Model 1) / Control (Model 2) |
| 🎯 Later_Success | Binary indicator of later-stage funding success | Dependent (Model 2) |
| Controls | Firm characteristics (e.g., team, prior experience, sector) | Control variables |

---

## 3. Models

### Model 1: Early-Stage Funding Amount
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
Funding Amount ↑
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
Success Rate ↑
      |        ____/
      |      /
      |    /
      |  /
      |/____________ 😵‍💫 Vagueness →
    Precise      Vague
```
**Interpretation:** Vague descriptions → higher later-stage success (conditional on early funding)

---

## 5. Analysis Pipeline

1. **Data Preparation**: Extract funding records, compute vagueness scores
2. **Model 1**: OLS regression (early funding ~ vagueness)
3. **Model 2**: Logistic regression (later success ~ vagueness + early funding)
4. **Visualization**: Recreate patterns with actual data
5. **Robustness**: Industry/sector effects, alternative measures

---

## 6. Deliverables

| Item | Description |
|------|-------------|
| **Table 1** | Descriptive statistics |
| **Table 2** | Model 1 results (early stage) |
| **Table 3** | Model 2 results (later stage) |
| **Figure 1** | Vagueness → Early-stage funding |
| **Figure 2** | Vagueness → Later-stage success |

---

## 🔄 見利思義 순환 전투 계획

### Week 1: Data + Model 1
```
見 → 利(ChatGPT: data extraction) 
   → 思(Claude: data pipeline) 
   → 義(Gemini: validation)
```
**산출**: Table 1, Table 2

---

### Week 2: Model 2 + Visualization
```
見 → 利(ChatGPT: logistic prototype) 
   → 思(Claude: refinement) 
   → 義(Gemini: robustness)
```
**산출**: Table 3, Figure 1, Figure 2

---

### Week 3: Paper
```
見 → 利(ChatGPT: draft sections) 
   → 思(Claude: structure) 
   → 義(Gemini: logic check)
```
**산출**: Complete manuscript

---

## 📊 Measurement Notes

### Vagueness Proxy
Options for operationalization:
- Linguistic certitude (LIWC)
- Readability/fog index
- Specificity of claims
- Inverse of concrete language

### Temporal Windows
- **Early stage**: Initial external funding round
- **Later stage**: Subsequent funding or exit within observation period

### Control Strategy
- Firm-level: Team size, founder experience
- Context-level: Industry, geography, cohort
- Process-level: Time between rounds, market conditions

---

## 🎯 연결 to Broader Theory

### Theoretical Positioning
This empirical test connects to:
- **Optimal Ignorance Level (OIL)**: τ* = max{0, √(V/4i) - 1}
- **Strategic ambiguity literature**: When should ventures be vague?
- **Signaling theory**: What do vague promises signal?

### Expected Contribution
Empirical evidence that promise precision has **non-monotonic effects**:
- Short-term: Precision helps (credibility)
- Long-term: Vagueness helps (flexibility)

---

**이 파일은 전투의 지도입니다** 🗺️  
**막힐 때마다 이 workflow로 돌아오세요**
