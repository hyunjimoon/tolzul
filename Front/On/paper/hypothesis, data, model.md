---
성장:
  - 2025-10-21T23:03:49-04:00
---
# Promise Precision and Venture Funding

## 0. Hypothesis 
**"Vagueness at Series A lowers initial funding chances but increases Series B success (because no rigid expectations to disappoint)"**

## 1. Data 
**Primary**: Pitchbook + TechCrunch/accelerator pitch materials
**Domain**: AI/ML infrastructure startups (2021-22 Series A → 2025 Series B outcomes)
**Sample size**: 60-80 firms

## 2. Model

### Dependent Variable
`Funding_Success_it` (binary): 1 if round successfully raised, 0 otherwise

### Key Independent Variables
- `Vagueness_i` (0-100): Coded from Series A pitch, using 100 - [[2metric_LIWC]] (El-Zayaty et al. 2025)
  - Low vagueness (70-100): "10ms inference on A100 GPUs"
  - High vagueness (0-30): "Enterprise-ready AI infrastructure"
- `SeriesB_it` (binary): 1 if Series B attempt, 0 if Series A
- `Vagueness_i × SeriesB_it` (interaction): Tests reversal hypothesis

### Control Variables
From Pitchbook:
- `log(SeriesA_Amount)`
- `Team_Size`
- `Founder_Prior_Exit` (binary)
- `High_Integration_Cost` (binary): Hardware/distributed systems (=1) vs API/software (=0)

### Regression Equation1
```
Logit(Funding_Success_it) = β₀ + β₁·Vagueness_i + β₂·SeriesB_it 
                          + β₃·(Vagueness_i × SeriesB_it) 
                          + β₄·log(SeriesA_Amount) + β₅·Team_Size
                          + β₆·Founder_Prior_Exit + ε_it
```

### Hypothesis Tests
- **H1**: β₁ < 0 (vagueness hurts at Series A)
- **H2**: β₃ > 0 (interaction positive: vagueness effect reverses at Series B)
- **H3**: β₁ + β₃ > 0 (net effect: vagueness helps at Series B)

### Regression Equation2

```
Funding_Success = β₀ + β₁·Vagueness + β₂·SeriesB + β₃·(Vagueness × SeriesB) + ε

**Where:**
- `Funding_Success` = 1 if raised round, 0 if failed
- `Vagueness` = language vagueness score (e.g., El-Zayaty's LIWC certitude measure)
- `SeriesB` = 1 if Series B attempt, 0 if Series A (reference)
- `Vagueness × SeriesB` = interaction term

**Your hypothesis predicts:**
- β₁ > 0 (vagueness helps at Series A)
- β₃ < 0 and significant (effect flips at Series B)
- β₁ + β₃ < 0 (net effect: vagueness hurts at Series B)

**Test:** Is β₃ significantly negative?

**With controls:**
Funding_Success = β₀ + β₁·Vagueness + β₂·SeriesB + β₃·(Vagueness × SeriesB)
                + β₄·Founder_Experience + β₅·Team_Size + β₆·Industry_FE 
                + β₇·Year_FE + ε
```


----

## Workflow 

### Hour 1-3: Data Collection
- Pull 70-80 AI infrastructure Series A deals (2021-22) from Pitchbook
- Download pitch materials from TechCrunch, company blogs, accelerator archives
- Record Series B outcomes through Q3 2025

### Hour 4-6: Variable Coding
**Vagueness Coding Rubric**:
| Score Range | Description | Example |
|------------|-------------|---------|
| 0-33 | High precision | "Sub-3s inference at 99.9% uptime" |
| 34-67 | Medium precision | "Production-ready with enterprise features" |
| 68-100 | High vagueness | "Seamless AI integration" |

**Integration Cost** (binary):
- High (=1): Custom hardware, distributed training, edge deployment
- Low (=0): API wrappers, fine-tuning SaaS, prompt tools

### Hour 7-8: Analysis
```python
# Base model
m1 = glm(Funding_Success ~ Vagueness + controls, family=binomial)

# Interaction model (key test)
m2 = glm(Funding_Success ~ Vagueness * SeriesB + controls, family=binomial)

# Subsample by integration cost (mechanism test)
m3_low_i = glm(Funding_Success ~ Vagueness * SeriesB + controls, 
               data=subset(High_Integration_Cost==0))
m4_high_i = glm(Funding_Success ~ Vagueness * SeriesB + controls,
                data=subset(High_Integration_Cost==1))
```

### Hour 9: Visualization
1. **Main result**: 2×2 bar chart (Vagueness × Stage)
2. **Predicted probabilities**: Crossing curves showing reversal
3. **Descriptive stats**: Sample composition table

## Deliverables
1. **Table 1**: Descriptive statistics by stage and integration cost
2. **Table 2**: Regression results (Models 1-4)
3. **Figure 1**: Success rates by vagueness level and stage
4. **Figure 2**: Predicted probability curves (low-i vs high-i sectors)

## Key Insight from Jeff
Vagueness is strategic when founders have credibility signals (prior exits, team pedigree). This:
1. Forces investors to bet on the team (not rigid promises)
2. Preserves flexibility to pivot without "disappointing" early commitments
3. Creates selection: only credible founders can afford vagueness at Series A

## Alternative Specifications (if time permits)
- **Selection model**: Heckman correction for who attempts Series B
- **Temporal dynamics**: Days_to_SeriesB_Attempt as moderator
- **Rhetorical capital**: Interaction with Founder_Prior_Exit
