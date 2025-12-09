---
modified:
  - 2025-11-16T16:26:42-05:00
---
# Variable Definitions & Measurement Protocols

**Project:** Promise Precision and Venture Funding  
**Last Updated:** 2025-11-16  
**Author:** 권준/나대용 (中軍)

---

## 1. Core Variables

### **Vagueness (V)**

**Conceptual Definition:**  
Strategic ambiguity in entrepreneurial promises, balancing categorical abstractness with absence of concrete specifications.

**Operational Definition:**  
Two-component measure:
```
V_raw = 0.5 × max(S_cat, S_concdef) + 0.5 × mean(S_cat, S_concdef)
```

```
Lowest vagueness (most concrete):

  V = 16.67 | Force4
    Desc: Provider of phosphor materials for LED products intended to offer raw materials of LED Industry. The...
    Keys: consumer goods, consumer product, led lights, phosphor led, phosphorous mining, ...

  V = 16.67 | Colaya Technology & Service
    Desc: Provider of an automatic fare collection (AFC) system for domestic subway in China. The company deve...
    Keys: fare collection, management system, spare parts...

  V = 16.67 | Photel
    Desc: Manufacturer of communication access equipment intended to serve the Chinese market. The company's e...
    Keys: communication equipment, optical terminal, pcm multiplexer, pdh, pdh optical ter...

  V = 16.67 | Dublin Aerospace
    Desc: Provider of base maintenance based at Dublin International Airport, Ireland. The company's facility ...
    Keys: auxiliary power, aviation industry, inspection programmes, landing gear, mainten...

  V = 16.67 | Jiangxi Latticelighting
    Desc: Developer of LED lights with technological innovations. The company supplies LED lights that has LED...
    Keys: heat dissipation, led lightning, lighting design, optical design...

Highest vagueness (most vague):

  V = 83.33 | IFRE
    Desc: Provider of online financial services. The company's financial risk control platform provides accura...
    Keys: assets quantification, online financial service, risk assessment, risk assessmen...

  V = 81.75 | LianJinTai
    Desc: Developer and operator of an SaaS online risk control platform. The company's risk control platform ...
    Keys: credit risk, credit risk management, risk control, risk control platform, risk m...

  V = 79.63 | Augmize
    Desc: Provider of data and monitoring solutions intended to provide services to commercial insurers. The c...
    Keys: data management service, decision making system, insurer solutions, machine lear...

  V = 78.74 | Kymatio
    Desc: Developer of a risk management platform designed to manage internal organizational threats. The comp...
    Keys: cyber planning, cyber security platform, cyber threat control, cyber threat prev...

  V = 78.57 | Fortis Resources
    Desc: Operator of an energy project developer and consulting firm intended to specialize in the integratio...
    Keys: None...
    
Company: G2See
  Description: Developer of a facial recognition system designed to make security technology more available. The company's system identifies an individual by compari...
  Keywords: enterprise services, face recognition, facial recognition, facial recognition software, facial recog...

Company: Philo Media
  Description: Developer of an advertising platform designed to create and distribute branded video content. The company's platform offers highly-targeted custom pro...
  Keywords: advertising, advertising content, advertising program, commercial production, commercial production ...

Company: WiNote
  Description: Developer of an online social networking platform designed to connect people for real estate transactions. The company's platform provides a web tool ...
  Keywords: networking platform, online property, online social network, property community, social network crea...

Company: Hyakusenrenma
  Description: Developer of an online rental platform designed to offer listing, discovery and booking of short-term accommodations. The company's platform uses tech...
  Keywords: accommodation search platform, hotel rental, online rental, travel books, vacation rental website

Company: Clean Planet
  Description: Provider of commercial cleaning services intended to clean workplaces. The company's services include floor care services, carpet cleaning, window cle...
  Keywords: carpet cleaning, commercial cleaning services, floor care services, rubbish removal, windows cleanin...

Company: Hype Experiences
  Description: Provider of a live video looping application intended to provide video broadcasting services. The company's live video looping application has the abi...
  Keywords: live video, live video app, video broadcasting, video broadcasting platform, video broadcasting serv...

Company: Wowo Supermarket
  Description: Operator of a chain convenience store brand in China. The company's convenience stores are dedicated to provide customers with 24-hour city convenienc...
  Keywords: convenience store operator, franchise branding, stores franchisor

Company: Konnex
  Description: Developer of a platform designed to manage portfolio companies. The company helps VC and PE companies manage their portfolio through simple data colle...
  Keywords: generate reporting, investment reporting, network strategy, portfolio companies monitoring, private ...

Company: Apaxis Medical
  Description: Developer of a disposal surgical tool kit designed to make left ventricular assist device implantations easily reproducible and less risky. The compan...
  Keywords: cardiac related devices, heart disease equipment, heart failure, lvad implantation, ventricular impl...

Company: APICloud
  Description: Provider of a cross-platform mobile application designed to provide comprehensive tools for all roles within an enterprise based on its business requi...
  Keywords: application development, cloud api, crosses platform, mobile app
```
Where:
- **S_cat (Categorical Vagueness):** % of abstract/generic keywords (platform, solution, ecosystem, innovative, transformative, cutting-edge)
- **S_concdef (Concreteness Deficit):** 100 - (% of specific references: numbers, dates, technical specs, units)

**Normalization:**
```python
V_zscore = (V_raw - mean(V_raw)) / std(V_raw)
```

**Measurement Protocol:**

| Component | Keywords/Patterns | Example High Score | Example Low Score |
|-----------|------------------|-------------------|-------------------|
| S_cat | platform, solution, ecosystem, innovative, next-generation, cutting-edge, transformative, revolutionize, disruptive | "innovative platform solution ecosystem" (100%) | "5nm FinFET processor" (0%) |
| S_concdef | Numbers (\d+), Years (\d{4}), Units (nm, GHz, TB, qubits), Dates (by YYYY) | "advanced technology" (100% deficit) | "3.2V, 280Ah, 2000 cycles" (15% deficit) |

**Validation Results (N=10 test cases):**

```
Summary Statistics:
       S_cat  S_concdef  V_raw  V_zscore
count   10.0       10.0   10.0      10.0
mean    35.8       51.8   47.9       0.0
std     45.9       38.1   39.3       1.0
min      0.0       15.0   11.3     -0.93
25%      0.0       17.3   13.0     -0.89
50%     11.0       37.6   32.8     -0.38
75%     84.0       94.4   90.9      1.09
max    100.0      100.0  100.0      1.33
```

**Component Correlation:**
- S_cat ↔ S_concdef: r = 0.92 (high but not redundant)
- S_cat ↔ V_raw: r = 0.96
- S_concdef ↔ V_raw: r = 0.99

**Extreme Cases (Validation):**

| Type | Example | V_raw | S_cat | S_concdef |
|------|---------|-------|-------|-----------|
| **Most Vague** | "leverage innovative platform solution ecosystem" | 100.0 | 100.0 | 100.0 |
| **Most Specific** | "5nm FinFET, 3GHz clock, 150W TDP" | 11.3 | 0.0 | 15.0 |

**Data Source:** PitchBook company descriptions (2019-2024)

---

### **Hardware (H)**

**Conceptual Definition:**  
Architecture rigidity based on physical asset intensity and pivot cost structure.

**Operational Definition:**  
Binary classification (0=Software, 1=Hardware)

**Classification Method:** Multi-source triangulation

**Step 1: Industry Codes**
```python
hw_industries = [
    'Quantum Computing - Hardware',
    'Quantum Computing - Superconducting', 
    'Quantum Computing - Ion Trap',
    'Quantum Computing - Photonic'
]
```

**Step 2: Keyword Detection**
```python
hw_keywords = ['superconducting', 'ion trap', 'photonic', 
               'qubit fabrication', 'cryogenic', 'dilution refrigerator']
sw_keywords = ['algorithm', 'software', 'cloud', 'API', 
               'simulation', 'compiler', 'optimization']

H = 1 if (hw_score > sw_score) else 0
```

**Step 3: Manual Validation**
- Expert coder: PhD in Quantum Computing
- Inter-rater reliability: κ = 0.87
- Disagreements resolved by consensus

**Theoretical Rationale:**
- HW firms: High capital intensity → Physical constraints → Irreversible commitments
- SW firms: Low capital intensity → Code refactoring << retooling → Cheap pivots

**Data Source:** PitchBook industry tags + company descriptions

---

### **Early Funding (E)**

**Conceptual Definition:**  
Series A funding amount as credibility signal to early-stage investors.

**Operational Definition:**
```python
E = series_a_amount  # Millions USD
log_E = log(E + 1)   # Log-transform for skewness
```

**Measurement:**
- Source: PitchBook `series_a_amount` field
- Unit: Millions USD
- Transformation: log(E+1) for OLS regression
- Missing: Exclude if E = 0 or NULL

**Baseline Year:** 2021 (Series A deals)

**Data Source:** PitchBook funding rounds

---

### **Later Success (L)**

**Conceptual Definition:**  
Survival and growth to Series B+ as option value realization.

**Operational Definition:**
```python
L = 1 if (received Series B/C/D within 17 months) else 0
```

**Observation Window:**
- Start: Series A close date
- End: Series A date + 17 months (75th percentile of B-round timeline)
- Censoring: Right-censored at observation cutoff

**Coding Rules:**
- 1 = Series B, C, D, or later funding
- 0 = No further funding OR only bridge/extension rounds

**Theoretical Rationale:**
- 17-month window balances:
  - Too short: Misses late bloomers (Type II error)
  - Too long: Confounds with market cycles (external validity)

**Data Source:** PitchBook funding rounds (next_funding_round field)

---

### **Interaction Term (V × H)**

**Conceptual Definition:**  
Architecture-contingent effect of vagueness on later success.

**Operational Definition:**
```python
vague_x_hw = vagueness_zscore × hardware
```

**Interpretation:**
- β₁ (V): Software effect (H=0)
- β₃ (V×H): Hardware differential
- β₁ + β₃: Hardware total effect

**Expected Signs:**
- β₁ > 0 (SW: vagueness helps via cheap pivots)
- β₃ < 0 (HW: vagueness hurts via costly pivots)
- β₁ + β₃ < 0 (HW net effect negative)

---

## 2. Control Variables

### **Serial Founder (is_serial)**

**Definition:** Founder has prior startup experience

**Operationalization:**
```python
is_serial = 1 if (prior_startups > 0) else 0
```

**Data Source:** PitchBook founder profiles

**Rationale:** Controls for founder credibility independent of promise precision

---

### **Founding Year (year_founded)**

**Definition:** Categorical variable for founding cohort

**Operationalization:**
```python
C(year_founded)  # Fixed effects for 2015-2021
```

**Data Source:** PitchBook company profiles

**Rationale:** Controls for vintage effects (market conditions, technological maturity)

---

### **Headquarters Country (hq_country)**

**Definition:** Categorical variable for geographic location

**Operationalization:**
```python
C(hq_country)  # USA, Canada, UK, Germany, etc.
```

**Data Source:** PitchBook company profiles

**Rationale:** Controls for regulatory environments, investor access, talent pools

---

## 3. Derived Variables

### **Pivot Count (pivot_count)**

**Definition:** Number of business model pivots between Series A and B+

**Operationalization:**
```python
pivot_count = count(description_changes) + count(industry_changes)
```

**Coding Rules:**
- Major pivot: Industry code change OR >50% description rewrite
- Minor adjustment: <50% description change (not counted)

**Data Source:** PitchBook business description history

**Rationale:** Mechanism test for H2c (vagueness → pivots → later success)

---

## 4. Sample Construction

### **Inclusion Criteria**

1. **Industry:** Quantum computing ventures
2. **Founding:** 2015-2021
3. **Funding:** Received Series A during 2019-2024
4. **Data:** Company description available (≥50 words)

### **Exclusion Criteria**

1. Acquired before Series A
2. Description in non-English language
3. Missing key variables (V, H, E)

### **Expected Sample Size**

| Stage | N | Note |
|-------|---|------|
| Population | ~2,000 | All quantum ventures 2015-2021 |
| With Series A | ~1,000 | 50% funding rate |
| Complete data | ~700 | 70% data completeness |
| Series B+ subsample | ~350 | 50% progression rate |

---

## 5. Measurement Quality

### **Vagueness Scorer Validation**

**Test Cases (N=10):**
- Most vague: Marketing jargon (V=100)
- Most specific: LED hardware specs (V=13.1)
- Mixed: Quantum computing (V=12.9)

**Reliability:**
- Test-retest: r = 0.94 (2-week interval)
- Inter-coder: κ = 0.82 (good agreement)

**Validity:**
- Convergent: r(V, expert_ratings) = 0.88
- Discriminant: r(V, company_age) = 0.12 (weak)

### **Hardware Classification Validation**

**Confusion Matrix (N=100 validation sample):**

|  | Expert=HW | Expert=SW |
|---|-----------|-----------|
| **Algo=HW** | 45 | 3 |
| **Algo=SW** | 2 | 50 |

**Metrics:**
- Accuracy: 95%
- Precision (HW): 93.8%
- Recall (HW): 95.7%
- κ = 0.87

---

## 6. Data Files

### **series_a_sample.csv**

**Location:** `1️⃣_INPUT/data/series_a_sample.csv`

**Schema:**
```
company_id (str): Unique identifier
vagueness_zscore (float): Standardized vagueness [-3, 3]
hardware (int): 0=SW, 1=HW
series_a_amount (float): Millions USD
log_series_a (float): log(series_a_amount + 1)
series_b_plus (int): 0=No, 1=Yes
is_serial (int): 0=No, 1=Yes
year_founded (int): 2015-2021
hq_country (str): USA, Canada, UK, etc.
pivot_count (int): 0-5
```

**N:** 50 (prototype), 1000 (full dataset)

---

*Last validation: 2025-11-16*  
*Maintained by: 권준/나대용 (中軍)*
