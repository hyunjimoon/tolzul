---
성장:
  - 2025-10-21T23:08:50-04:00
updated:
  - 2025-10-22T01:45:00-04:00
---
# Promise Precision and Venture Funding

## Hypothesis 
**"Vagueness at Series A lowers initial funding chances but increases Series B success (because no rigid expectations to disappoint)"**

**Mechanism**: Precision helps when execution is the bottleneck (low-i). Vagueness helps when discovery is the bottleneck (high-i).

## Data and Context

**Primary Sources**: Pitchbook + TechCrunch/accelerator pitch materials  
**Domain**: AI/ML infrastructure startups (2021-22 Series A → 2025 Series B outcomes)  
**Sample Size**: 60-80 firms  
**Panel Structure**: Each firm observed twice (Series A attempt, Series B attempt)

**Domain Selection** (choose 2 for high vs low integration cost):

| Integration Cost | Example Domains |
|-----------------|----------------|
| **High** (=1) | AI chip startups, robotics/edge AI, distributed training infrastructure |
| **Low** (=0) | LLM fine-tuning platforms, prompt engineering tools, vector database SaaS |

**Mechanism Table**:

| Dimension | Low Integration Cost (API/SaaS) | High Integration Cost (Hardware/Chips) |
|-----------|--------------------------------|---------------------------------------|
| **Example Promise** | "99.9% uptime, <100ms latency" | "AI accelerator chip for inference" |
| **Technical Uncertainty** | Low (standard stack) | High (novel architecture) |
| **Bottleneck** | **Execution** (can you deliver?) | **Discovery** (what should you build?) |
| **Precise Promise Effect** | ✅ Enables accountability → Trust | ❌ Creates rigidity → Straitjacket |
| **Vague Promise Effect** | ❌ Signals incompetence → Red flag | ✅ Preserves flexibility → Pivot option |
| **Series A Outcome** | Precision wins funding (shows competence) | Precision wins funding (shows ambition) |
| **Series B Outcome** | Precision still wins (delivered on metrics) | **Vagueness wins** (avoided failed commitments) |
| **Real Example** | Stripe: "7-line integration, 2.9% + 30¢" → delivered exactly that | Tesla: "250 mile range" → shipped 244 miles (close enough, adapted battery chemistry) |

## Model

### Dependent Variable
`Funding_Success_it` (binary): 1 if round successfully raised, 0 otherwise

### Independent Variables

**Core Variables**:
- `Vagueness_i` (continuous, 0-100): Coded from Series A pitch, measured once
  - Measurement: 100 - LIWC Certitude Score (El-Zayaty et al. 2025)
  - Alternative: Flesch-Kincaid grade level (free via Python textstat)
  - Interpretation: Higher score = vaguer language
  - Examples:
    - Low vagueness (0-30): "10ms inference on A100 GPUs at 99.9% uptime"
    - High vagueness (70-100): "Enterprise-ready AI infrastructure"
- `SeriesB_it` (binary): 1 if Series B attempt, 0 if Series A
- `High_Integration_Cost_i` (binary): 1 = hardware/distributed systems, 0 = API/software

**Control Variables** (from Pitchbook):
- `log(SeriesA_Amount)` - Initial traction signal
- `Team_Size` - Execution capacity
- `Founder_Prior_Exit` (binary) - Credibility/rhetorical capital

### Regression Equations

**Model 1: Base Reversal Effect**
```
logit(Funding_Success_it) = β₀ + β₁·Vagueness_i + β₂·SeriesB_it 
                          + β₃·(Vagueness_i × SeriesB_it) 
                          + β₄·log(SeriesA_Amount) + β₅·Team_Size
                          + β₆·Founder_Prior_Exit + ε_it
```

**Hypothesis Tests**:
- **H1**: β₁ < 0 (vagueness hurts at Series A overall)
- **H2**: β₃ > 0 (effect reverses at Series B)

**Model 2: Integration Cost Mechanism (Three-way Interaction)**
```
logit(Funding_Success_it) = β₀ + β₁·Vagueness_i + β₂·SeriesB_it 
                          + β₃·High_Integration_Cost_i
                          + β₄·(Vagueness_i × SeriesB_it)
                          + β₅·(Vagueness_i × High_Integration_Cost_i)
                          + β₆·(SeriesB_it × High_Integration_Cost_i)
                          + β₇·(Vagueness_i × SeriesB_it × High_Integration_Cost_i)
                          + β₄·log(SeriesA_Amount) + β₅·Team_Size
                          + β₆·Founder_Prior_Exit + ε_it
```

**Hypothesis Test**:
- **H3**: β₇ > 0 (reversal strongest in high-integration-cost sectors)

**Standard Errors**: Cluster by firm_id (each firm appears twice)

## Workflow

### Part 1: Testing Base Reversal Effect (H1, H2)

**Hour 1-3: Data Collection**
- Pull 70-80 AI infrastructure Series A deals (2021-22) from Pitchbook
- Download pitch materials from TechCrunch, company blogs, accelerator archives
- Record Series B outcomes through Q3 2025
- Create panel: each firm appears twice (A attempt, B attempt)

**Hour 4-6: Variable Coding**

*Vagueness Coding Rubric*:
| Score Range | Description | Example |
|------------|-------------|---------|
| 0-33 | High precision | "Sub-3s inference at 99.9% uptime" |
| 34-67 | Medium precision | "Production-ready with enterprise features" |
| 68-100 | High vagueness | "Seamless AI integration" |

*Methods*:
```python
# Option A: LIWC (if licensed)
import liwc
vagueness = 100 - certitude_score(pitch_texts)

# Option B: Readability proxy (free)
import textstat
vagueness = textstat.flesch_kincaid_grade(pitch_texts)
```

**Hour 7-8: Analysis**
```python
import statsmodels.formula.api as smf

# Model 1: Base reversal
m1 = smf.logit('funding_success ~ vagueness * series_b_dummy + np.log(series_a_amount) + team_size + founder_prior_exit',
               data=df_panel).fit(cov_type='cluster', cov_kwds={'groups': df_panel['firm_id']})

# Test H1: β₁ < 0
print(f"H1 (vagueness hurts at A): β₁ = {m1.params['vagueness']:.4f}, p = {m1.pvalues['vagueness']:.4f}")

# Test H2: β₃ > 0
interaction_coef = m1.params['vagueness:series_b_dummy']
print(f"H2 (effect reverses at B): β₃ = {interaction_coef:.4f}, p = {m1.pvalues['vagueness:series_b_dummy']:.4f}")
```

**Hour 9: Visualization for Part 1**
```python
# Figure 1: 2×2 success rates
pivot = df_panel.pivot_table('funding_success', 
                              index=pd.cut(df_panel['vagueness'], bins=2, labels=['Low', 'High']),
                              columns='series_b_dummy')
pivot.plot(kind='bar')

# Figure 2: Predicted probabilities showing crossover
vagueness_range = np.linspace(0, 100, 100)
# Plot lines for Series A vs B showing reversal
```

**Deliverables**:
- **Table 1**: Descriptive statistics (mean vagueness, success rates by stage)
- **Table 2**: Model 1 regression results
- **Figure 1**: Success rates by vagueness level × stage (bar chart)
- **Figure 2**: Predicted probability curves (crossing lines)

### Part 2: Testing Integration Cost Mechanism (H3)

**Hour 1-2: Integration Cost Coding**
```python
# Binary coding based on business model
hardware_keywords = ['chip', 'hardware', 'edge device', 'robotics', 'distributed', 'ASIC', 'GPU cluster']
software_keywords = ['API', 'SaaS', 'platform', 'wrapper', 'fine-tuning', 'prompt']

df['high_integration_cost'] = df['description'].str.contains('|'.join(hardware_keywords)).astype(int)

# Manual verification: review ambiguous cases
ambiguous = df[df['description'].str.contains('|'.join(hardware_keywords)) & 
                df['description'].str.contains('|'.join(software_keywords))]
```

**Domain Balance Check**:
- Target: ~30 high-i firms, ~30 low-i firms
- If unbalanced, adjust keyword list or expand data collection

**Hour 3-4: Three-way Interaction Analysis**
```python
# Model 2: Full mechanism
m2 = smf.logit('''funding_success ~ vagueness * series_b_dummy * high_integration_cost + 
                  np.log(series_a_amount) + team_size + founder_prior_exit''',
               data=df_panel).fit(cov_type='cluster', cov_kwds={'groups': df_panel['firm_id']})

# Test H3: β₇ > 0
three_way = m2.params['vagueness:series_b_dummy:high_integration_cost']
print(f"H3 (reversal stronger in high-i): β₇ = {three_way:.4f}, p = {m2.pvalues['vagueness:series_b_dummy:high_integration_cost']:.4f}")

# Marginal effects by integration cost
from statsmodels.discrete.discrete_model import Logit
margeff_low = m2.get_margeff(at={'high_integration_cost': 0, 'series_b_dummy': 1})
margeff_high = m2.get_margeff(at={'high_integration_cost': 1, 'series_b_dummy': 1})
```

**Hour 5: Visualization for Part 2**
```python
# Figure 3: 2×2×2 success rates (Vagueness × Stage × Integration Cost)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Panel A: Low integration cost
low_i = df_panel[df_panel['high_integration_cost'] == 0]
pivot_low = low_i.pivot_table('funding_success', index='vagueness_bin', columns='series_b_dummy')
pivot_low.plot(kind='bar', ax=ax1, title='Low Integration Cost (API/SaaS)')

# Panel B: High integration cost  
high_i = df_panel[df_panel['high_integration_cost'] == 1]
pivot_high = high_i.pivot_table('funding_success', index='vagueness_bin', columns='series_b_dummy')
pivot_high.plot(kind='bar', ax=ax2, title='High Integration Cost (Hardware)')

# Figure 4: Predicted probabilities (4 curves)
# Series A × Low-i, Series A × High-i, Series B × Low-i, Series B × High-i
```

**Deliverables**:
- **Table 3**: Descriptive statistics by integration cost
- **Table 4**: Model 2 regression results (three-way interaction)
- **Figure 3**: Success rates by vagueness × stage × integration cost (faceted bar charts)
- **Figure 4**: Predicted probability curves (4 lines showing differential reversal)

## Expected Results

**Model 1 (Base)**:
- β₁ ≈ -0.02 (p < 0.05): Vagueness hurts at Series A
- β₃ ≈ 0.03 (p < 0.05): Effect reverses at Series B

**Model 2 (Mechanism)**:
- β₇ ≈ 0.06 (p < 0.01): Reversal 2-3× stronger in high-integration-cost sectors
- Interpretation: In hardware/distributed systems, vagueness provides valuable flexibility. In API/SaaS, precision enables accountability.

## Key Insights

**From Jeff's Guidance**:
- Vagueness is strategic when founders have credibility signals (prior exits, team pedigree)
- Forces investors to bet on the team (not rigid promises)
- Preserves flexibility to pivot without "disappointing" early commitments
- Only credible founders can afford vagueness at Series A

**Endogeneity Handling**:
- Control for `Founder_Prior_Exit` as proxy for rhetorical human capital (El-Zayaty approach)
- Selection-on-observables assumption
- Acknowledge limitation: technical skill may still confound

## Alternative Specifications (Future Work)
- Heckman selection model for who attempts Series B
- `Days_to_SeriesB_Attempt` as moderator
- Interaction with `Founder_Prior_Exit` (rhetorical capital)
- Temporal fixed effects (year dummies for macro shocks)
