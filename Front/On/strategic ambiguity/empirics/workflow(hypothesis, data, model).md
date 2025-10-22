---
성장:
  - 2025-10-21T23:08:50-04:00
  - 2025-10-22T10:30:45-04:00
updated:
  - 2025-10-22T04:45:00-04:00
next: "[[revisit]]"
---

# Promise Precision and Venture Funding

## 1. Hypotheses

* **Hypothesis 1:** Vagueness at Series A lowers initial funding chances but increases Series B success (because no rigid expectations to disappoint).
- **Hypothesis 2:** High integration cost firms (hardware, distributed systems) benefit more from initial ambiguity than low integration cost firms (software, APIs).
---

## 2. [[Data]] and [[Context]]

This study will merge time-stamped promissory texts, sourced from public venture archives, with firm-level funding and valuation data from a comprehensive private capital database. This hybrid-archival approach links founder language to subsequent, objective financing outcomes.

### Data Source

* **Primary Sources:** Pitchbook Company + Deal data
* **Domain with era of ferment:** one of the three
	* 1: AI/ML infrastructure startups (2021–2022 Series A → 2025 Series B outcomes)
	* 
* **Sample Size:** 60–80 firms observed twice (Series A attempt, Series B attempt)

sample data at 
- /Users/hyunjimoon/Dropbox (MIT)/tolzul/Front/On/strategic ambiguity/empirics/data/raw/deal2023.dat
- /Users/hyunjimoon/Dropbox (MIT)/tolzul/Front/On/strategic ambiguity/empirics/data/raw/company2021.dat
### **Data Integration Strategy:**

**Company Data (Pitchbook) - 핵심 컬럼:**
1. **Description** → LIWC certitude 분석으로 `Vagueness_i` 생성
2. **Keywords** → Integration cost 분류 (hardware: chip, ASIC, distributed, robotics)
3. **TotalRaised** → 초기 트랙션 통제변수
4. **Employees** → `Team_Size`
5. **YearFounded** → 창업 연수

**Deal Data (Pitchbook) - 핵심 컬럼 + Mitigation:**
1. **VCRound + DealType** → Series A/B 식별 (**UPDATED**)
   - **Problem**: VCRound often missing or vague ("Early Stage VC")
   - **Solution (4-step heuristic)**:
     1. Filter: `DealType IN ("Early Stage VC", "Later Stage VC")` (exclude Grants, SAFE, Accelerator)
     2. Sequence: First qualifying deal = Series A, second = Series B
     3. Size thresholds: Series A $2M-$15M, Series B $10M+
     4. Date filter: Series A 2021-2022, Series B 2023-2025
   - **Validation**: Manual review of 20% random sample, exclude ambiguous edge cases
2. **DealDate** → 시간축
3. **DealSize** → `Funding_Success_it` (>$0 = 1)
4. **Investors** → Tier-1 VC proxy
5. **PostValuation** → Robustness

**데이터 조리 (5 steps)**:
1. Company filter: AI/ML keywords in Description or Primary Industry
2. Deal join: Extract qualifying equity rounds per CompanyID
3. Panel construct: Each firm × 2 observations (A, B)
4. LIWC scoring: `Vagueness = 100 - certitude`
5. Final: 150 obs (75 firms × 2 stages)

---

### Key Variables

#### Dependent Variable

* **Funding_Success_it (binary):** 1 if DealSize > $0

#### Independent Variables

* **Vagueness_i:** 100 - LIWC Certitude (0-100 scale)
* **SeriesB_it:** 1=Series B, 0=Series A
* **High_Integration_Cost_i:** 1=hardware, 0=software

#### Controls

* **log(SeriesA_Amount)**, 
* **Team_Size**, 
* **Founder_Prior_Exit**: Founders with **credibility signals** can be strategically vague, forcing investors to bet on the team, not the idea.

---

### Variable Description Table

| Variable | Source | Type | Role | Example |
|----------|--------|------|------|---------|
| firm_id | CompanyID | String | Panel key | "100001-08" |
| Vagueness_i | Description | 0-100 | IV | 68.4 |
| SeriesB_it | DealType+heuristic | Binary | IV | 0 |
| High_Integration_Cost_i | Keywords | Binary | Moderator | 1 |
| Funding_Success_it | DealSize | Binary | DV | 1 |

---

### Sample Database Snippet

| firm_id | stage | vagueness | high_int | success | deal_$m |
|---------|-------|-----------|----------|---------|---------|
| 001 | A | 42.3 | 1 | 1 | 8.0 |
| 001 | B | 42.3 | 1 | 0 | 0.0 |
| 002 | A | 68.7 | 0 | 1 | 5.2 |
| 002 | B | 68.7 | 0 | 1 | 18.0 |

---

## 3. Model

**Model 1 (H1, H2)**:
```
logit(Funding_Success_it) = β₀ + β₁·Vagueness + β₂·SeriesB 
                          + β₃·(Vagueness × SeriesB) + Controls
```

**Model 2 (H3)**:
```
+ β₇·(Vagueness × SeriesB × High_Int_Cost)
```

---

## 4-6. Analysis, Results, Robustness

* Expected: β₁ < 0, β₃ > 0, β₇ > 0
* Robustness: Winsorize, alternative vagueness measures

---

# Workflow

## Deliverables (8 items)

| Item | Summary |
|------|---------|
| Table 1 | Descriptive stats |
| Table 2 | Model 1 regression |
| Figure 1-2 | Bar + curves (reversal) |
| Table 3-4 | Sector rates + 3-way |
| Figure 3-4 | 4 lines + magnitude bars |

---

### **(🚨11) Data Challenges**

1. **VCRound Ambiguity**: Solved via 4-step heuristic (DealType + size + sequence + date)
2. **Description Quality**: Exclude <50 words
3. **Series B Censoring**: Restrict to pre-2023 Series A cohort
4. **Integration Cost**: Binary classification via hardware keywords
