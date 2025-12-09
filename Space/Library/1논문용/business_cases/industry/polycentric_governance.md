---
modified:
  - 2025-11-07T18:06:45-05:00
---

## 🧭 목표

- 산업별로 **“공동 전환(governance of transition)”** 을 문서화할 수 있는 **Markdown 템플릿** 생성
    
- Claude or ChatGPT 등에게 “산업분석 인터뷰 요약을 이 구조로 정리해줘” 라고 요청할 프롬프트 작성
    
- Obsidian vault 나 Git repo 에서 산업별 폴더를 누적 가능하게 설계
    

---

## 🗂️ 디렉터리 구조 제안 (Obsidian-friendly)

```
/Polycentric-Industries/
│
├── EV-Transition/
│   ├── EV-Transition.md
│   ├── Interviews/
│   │   ├── Founder.md
│   │   ├── University.md
│   │   ├── VC.md
│   │   ├── Corporate.md
│   │   ├── Government.md
│   └── Synthesis.md
│
├── Quantum-Transition/
│   ├── Quantum-Transition.md
│   ├── Interviews/
│   │   ├── Founder.md
│   │   ├── University.md
│   │   ├── VC.md
│   │   ├── Corporate.md
│   │   ├── Government.md
│   └── Synthesis.md
│
└── _Template/
    └── Industry-Transition-Template.md
```

---

## 📘 `Industry-Transition-Template.md` (Markdown Base)

```markdown
# {{Industry}} Transition – Polycentric Governance Analysis

## 1️⃣ Overview
**Period:** {{StartYear}} – {{EndYear}}  
**Core Technology / System:** {{TechFocus}}  
**Transition Goal:** {{TransitionGoal}}  
**Bayesian Frame:**  
- How actors update shared beliefs (priors) as new evidence emerges  
- How “vagueness” or strategic ambiguity enables coordination under uncertainty  

---

## 2️⃣ Ecosystem Actors (Map)
| Actor Type | Key Stakeholders / Examples | Role in Transition | Coordination Mechanism |
|-------------|-----------------------------|--------------------|------------------------|
| Founder / Entrepreneur |  | Signaling + experimentation | Promise variance management |
| University / Research Lab |  | Knowledge production | Open benchmark / training |
| Venture / Risk Capital |  | Funding allocation under uncertainty | Bayesian filter on credibility |
| Corporate / OEM / Integrator |  | Scaling capabilities | Platform / standardization |
| Government / Regulator |  | Policy + grant coordination | Incentive alignment / rules |

---

## 3️⃣ Polycentric Dynamics (visible hands)
- **Coordination gaps:** {{e.g., no chief engineer, no standard metric}}  
- **Visible hands emerged as:** {{working groups / alliances / consortia}}  
- **Naming / Framing practices:** {{shared vocabulary that stabilized expectations}}  
- **Learning cycles:** {{hypothesis → experiment → belief update}}  

---

## 4️⃣ Evidence of Bayesian Learning
| Stage | Signal / Promise Made | Evidence Observed | Updated Interpretation |
|--------|----------------------|------------------|-----------------------|
| t₀ (Early hype) |   |   |   |
| t₁ (Correction) |   |   |   |
| t₂ (Refocus / Execution) |   |   |   |

---

## 5️⃣ Quantitative Hooks (if available)
- **Funding trajectories:** Series A → B+ → IPO progression (%).  
- **R&D Intensity Proxies:** Grants / Patents / Employees / Downround Share.  
- **Key windows:** {{2021-12 → 2023-12, 2022-12 → 2024-12, 2022-12 → 2025-11}}.  

---

## 6️⃣ Comparative Insight
- **Commitment vs Flexibility trade-off:** {{Observation}}  
- **Most salient coordination problem:** {{Observation}}  
- **Effective visible hand mechanism:** {{Observation}}  
- **Emergent norm / shared prior:** {{Observation}}  

---

## 7️⃣ References / Notes
- Interviews conducted: {{N}}  
- Data sources: {{PitchBook, policy reports, white papers …}}  
- Related files: [[{{Industry}}/Interviews/Founder]] [[{{Industry}}/Synthesis]]
```

---

## ✳️ Example 1 – EV Transition (Summary)

```markdown
# EV Transition – Polycentric Governance Analysis

## 1️⃣ Overview
**Period:** 2019–2023  
**Core System:** EV charging network  
**Transition Goal:** Accelerate adoption of EVs via reliable, coordinated infrastructure.  
**Bayesian Frame:** Stakeholders updated beliefs about EV feasibility as reliability evidence accumulated.

## 2️⃣ Ecosystem Actors (Map)
| Actor Type | Examples | Role | Coordination |
|-------------|-----------|------|--------------|
| Founder | EVgo, SparkCharge | Tech entrepreneurship & experimentation | Signal credibility through pilot data |
| University | MIT MMI, Fine, Womack | System design & lean heritage transfer | Convening platform |
| VC | Amazon Climate Pledge Fund | Capital allocation | Hype-to-evidence shift |
| Corporate | GM, Ford, Electrify America | Scaling infra & standardization | Joint working groups |
| Government | DoE, Mass DOT | Policy support & grants | NEVI fund & rule alignment |

## 3️⃣ Polycentric Dynamics
- Lack of chief engineer → MMI acts as “virtual chief engineer.”  
- Naming practice: “reliability rate,” “charger uptime.”  
- Shared metric creation reduced belief variance among stakeholders.

## 4️⃣ Evidence of Learning
| Stage | Promise | Evidence | Update |
|-------|----------|-----------|---------|
| t₀ | “Fast EV adoption possible” | Charger failures | Need for reliability focus |
| t₁ | “99% uptime” | Joint data collection | Alignment on common metric |
| t₂ | “Scalable business model” | Successful pilots | Shared confidence |

```

---

## ✳️ Example 2 – Quantum Transition (Summary)

```markdown
# Quantum Transition – Polycentric Governance Analysis

## 1️⃣ Overview
**Period:** 2021–2025  
**Core Technology:** Quantum computing hardware & software stack  
**Transition Goal:** Shift from NISQ experiments to error-corrected quantum (EQC) systems.  
**Bayesian Frame:** Actors update beliefs about feasibility and timing of EQC as benchmarks and roadmaps emerge.

## 2️⃣ Ecosystem Actors (Map)
| Actor Type | Examples | Role | Coordination |
|-------------|-----------|------|--------------|
| Founder | IonQ, QuEra, Rigetti | Signal technical milestones & raise capital | Promise variance management |
| University | MIT, Caltech, ETH | Fundamental research & standards | Benchmark consortia |
| VC | Andreessen Horowitz, Quantonation | Funding under uncertainty | Learning across portfolios |
| Corporate | IBM, Google, PsiQuantum | Scaling hardware ecosystems | Roadmap transparency |
| Government | DOE Quantum Initiative, EU Flagship | Policy & grant coordination | Consortium rules & shared metrics |

## 3️⃣ Polycentric Dynamics
- No single “chief engineer” → consortia serve as visible hands.  
- Naming practice: “logical qubit,” “quantum advantage.”  
- Shared definitions align priors and reduce interpretation variance.

## 4️⃣ Evidence of Learning
| Stage | Promise | Evidence | Update |
|-------|----------|-----------|---------|
| t₀ | “Full quantum advantage by 2023” | Tech delays | Expectations corrected |
| t₁ | “Error-corrected demo soon” | Google ‘Willow’ chip (105 qubits) | Belief in scaling path restored |
| t₂ | “Commercial use cases by 2025” | R&D grants + start-up funding uptick | Shared confidence in EQC trajectory |

```

---

## ✳️ Claude Extraction Prompt (to generate or populate these)

> **Prompt to Claude:**  
> “You are a research summarizer for polycentric industrial transitions.  
> Given interview transcripts or notes about an industry, extract and summarize them into the following markdown template:
> 
> - Identify 5 actor categories (Founder, University, Venture/Risk Capital, Corporate, Government).
>     
> - For each, list representative organizations, their role in the transition, and their coordination mechanisms.
>     
> - Capture evidence of Bayesian learning (what promises were made, what evidence appeared, how priors were updated).
>     
> - Fill out Sections 1–7 of the Industry-Transition-Template.md.  
>     Return valid Markdown ready for Obsidian.”
>     

---

이제 이 구조를 **EV**, **Quantum**, 그리고 향후 “AI Transition”, “Biotech Transition” 같은 산업에도 동일하게 복제할 수 있습니다.  
결과물은 Obsidian에서 폴더별로 쌓여 “polycentric industry atlas”처럼 관리됩니다.