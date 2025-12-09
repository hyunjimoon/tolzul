---
modified:
  - 2025-11-10T15:19:21-05:00
---


[[2025-11-10]]
![[michael_cusumano 2025_11_10.excalidraw]]
_Which verticals best match to maximize identification power for our step‑up test? 

**What an ideal vertical looks like (selection filter):**

1. **Era of ferment** with ≥20–30 competing firms and **distinct architectural plays** (modular vs integrated), so F varies.
    
2. **Founding‑moment text** is recoverable (pitch decks, accelerator blurbs, press at T1) to measure **promise vagueness**.
    
3. **Observable step‑ups** from A→B within 24–35 months (2021–22 A; outcomes by 2024–25).
    
4. **Low policy confounds** (market learning > regulation), minimizing exogenous shocks.
    
5. **Integration‑cost heterogeneity** (hardware↔software) to test moderation by option exercisability.


| **Component**               |   | **Example (your project: Strategic Ambiguity in Founders’ Promises)**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------- | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1. Research Question**    |   | • **When does strategic ambiguity in founders’ early promises help or hurt fundraising?**<br>• **Does ambiguity impose an early penalty (Series A amount) but yield a later benefit via larger valuation step‑ups and Series B+ progression—especially where pivot costs are high (hardware/complex architectures)?** <br>• **How do investor priors and cost‑of‑experimentation environments shape these effects?** (Bayesian staged‑financing lens).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **2. Conceptual Framework** |   | • **Bayesian learning via staged financing:** investors update beliefs round‑to‑round; value inflection occurs when milestones resolve uncertainty. Ambiguity = lower precision signal; optimal precision trades off **mobilization** vs **adaptability**. <br>• **Real‑options logic for venture finance:** lower probability of interim success (long‑shot bets) → **larger step‑ups conditional on success**; step‑up is inversely related to the probability of passing the first gate. (Ewens–Nanda–Rhodes‑Kropf model; see Table 9 for bigger step‑ups in treated sectors). <br>• **Moderator—Integration/architecture rigidity:** ambiguity should help more where **option exercisability** matters (hardware; quantum architectures) and less where switching is cheap (pure software). <br>• **Upper bound (“too vague is bad”):** expect an inverted‑U in later outcomes → include **Vagueness²**.                                                                                                                                                                                                                                                                                                                                                                                          |
| **3. Data**                 |   | • **Domains:** **Quantum** & **AI hardware** as principal settings (era of ferment; heterogeneous architectures; lower regulation confounds than AV/EV). <br>• **Sources:** PitchBook/Crunchbase funding histories (2019–2025), plus T=1 “founding promises” (pitch decks, accelerator pages, web archives) for textual vagueness (LIWC certitude → **Vagueness = 100 − Certitude**; validate with embeddings). <br>• **Panels & windows:** Cohorts with **as‑of capping** to avoid leakage, e.g., **2022‑12→2024‑12 (24 m)**; **2022‑12→2025‑11 (35 m)**; robustness **2021‑12→2023‑12 (24 m)**. <br>• **Implementation:** xarray‑based **multiverse engine** (spec grid over windows, moderators, controls) and evidence heatmaps (green/gray/red) for sign/strength.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **4. Research Design**      |   | **Outcomes (DVs)**<br>• **Early**: log(Series A amount) — test **H1 (mobilization penalty)**: *Vagueness ↓ Series A*. <br>• **Later**: (i) **log Step‑up** = log(PreMoney_{t+1}/PostMoney_t); (ii) **Series B+ indicator** within window — test **H2 (adaptability benefit)**: *Vagueness × IntegrationCost* **> 0**, conditional on being funded at t. (Motivated by step‑up logic and “long‑shot bet” inference). <br>**Key specs**<br>• **Model A (H1):**  E ~ Vagueness + controls + industry FE + cohort FE.<br>• **Model B (H2‑step‑up):**  StepUp ~ Vagueness × IntegrationCost + log(SeriesA$) + controls + industry FE + cohort FE; add **Vagueness²** for inverted‑U.<br>• **Model C (H2‑progression):**  Pr(B+) ~ Vagueness × IntegrationCost + log(SeriesA$) + controls (log employees, founder credibility, region FE); treat M&A as censored in primary; upper/lower‑bound robustness. <br>**Identification & QA**<br>• **As‑of capping** to kill future‑date leakage in funding fields; **VC‑backed at baseline**; **time‑to‑gate** calibration (A→B base rate ~12–15% at ~17 m). <br>• **Why step‑up?** Theory predicts bigger posterior jumps for low‑p₁ ventures; empirically, treated sectors show **15–23% higher step‑ups** conditional on continuation (Ewens et al., Table 9).  |
| **5. Results**              |   | **Status & priors‑consistent expectations**<br>**A. Early mobilization (H1):** preliminary runs show a small **negative** coefficient of vagueness on Series A (unit‑scaling under review). <br>**B. Later outcomes (H2):** expect **positive** effect of vagueness on **step‑ups** and **B+**, **amplified** by high integration cost (hardware; non‑modular architectures), consistent with “long‑shot bet” logic and staged‑learning (larger value inflection when ambiguous ventures pass milestones). <br>**C. Upper bound:** anticipate **inverted‑U**—excessive vagueness undermines credibility; test via **Vagueness²** and by comparing success‑firm vagueness percentiles. <br>**Deliverables:** direction‑aware multiverse heatmaps; Figures for H1/H2; Tables 1–3 with windows/moderators/robustness.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

**Notes on empirical/theory linkages (evidence you are leveraging):**

* Falling experimentation costs shifted VC behavior to **spray‑and‑pray**, more abandonment, **smaller initial rounds**, but **larger step‑ups** conditional on success—formal model & estimates in **Ewens–Nanda–Rhodes‑Kropf (JFE 2018)** (e.g., **−15% to −27%** initial round size; **higher step‑ups** and exit value/capital; see Table 3 and Table 9). 
* **Bayesian staged‑financing** perspective: value inflection arises when milestones reduce uncertainty; design experiments with high sensitivity/specificity to shift investor priors; figure‑based evidence on valuation progression across rounds. 
* Your **W2/W3 architecture** (domains, windows, multiverse engine, evidence map) operationalizes these ideas with clean **as‑of** panels and architecture‑level moderators. 
* Log details on **DV re‑definition** (from survival to **Series B+ / step‑up**), leakage fixes, base‑rate calibration, and spec grid appear in your **전투일지**. 

**Why this matters for your 15‑min adviser conversations:**

* The **core message** is theoretically sharp and empirically testable: *Ambiguous early promises can buy valuable option value—visible later as larger step‑ups and B+ progression—especially where pivoting is costly; but ambiguity has an upper bound.* This frames your domain ask and design choices in a way that is aligned with both **learning‑through‑experimentation** and **commitment–flexibility** trade‑offs.



----

## 1) One‑page summary slide — for Prof. Michael Cusumano

**Title:** _When do founders’ strategically ambiguous promises pay off?_  
**Subtitle:** A Bayesian test using funding **step‑ups** and architectural flexibility

**Why this matters (one‑liner):** If ambiguity preserves option value, ventures with lower prior success probability should show **larger valuation step‑ups** when evidence turns positive (Bayesian update) — especially where architectural **flexibility** makes options exercisable.

**What we already built (proof of execution):**

- Prototype pipeline + toy analysis demonstrating the test logic, variable schema (Vagueness **V**, Flexibility level **F**, funding) and diagnostics; pivot toward quantum as a tractable pilot vertical.
    
- Process architecture + multiverse spec (288 specs; windows anchored at 2022‑12) to run the full test on PitchBook/Crunchbase text + funding panels.
    

**Ask to Michael:** _Which verticals best match a “Cusumano-style” architecture and platform lens_ **and** maximize identification power for our step‑up test? (Characteristics below.)

**What an ideal vertical looks like (selection filter):**

1. **Era of ferment** with ≥20–30 competing firms and **distinct architectural plays** (modular vs integrated), so F varies.
    
2. **Founding‑moment text** is recoverable (pitch decks, accelerator blurbs, press at T1) to measure **promise vagueness**.
    
3. **Observable step‑ups** from A→B within 24–35 months (2021–22 A; outcomes by 2024–25).
    
4. **Low policy confounds** (market learning > regulation), minimizing exogenous shocks.
    
5. **Integration‑cost heterogeneity** (hardware↔software) to test moderation by option exercisability.
    

**Why step‑up as the DV (Michael‑ready logic):**

- In staged finance, conditional valuation **step‑ups** are **inversely proportional** to the prior success probability (p_1); bigger step‑ups signal “long‑shot” posteriors flipping after informative experiments.
    
- Empirically, step‑ups rose 15–20% in settings where **early experiments became cheaper/more informative** (cloud shock).
    
- A learning perspective: value inflection = information resolved; experiment **specificity/sensitivity** and **architecture** determine how persuasive evidence is to later‑stage investors.
    

**Shortlist you could react to (illustrative, not limiting):**

- **Quantum & AI hardware** (heterogeneous architectures; platform complements) — our current pilot.
    
- **Gen‑AI tooling stacks** (foundation‑model infra vs application bundles) — strong modular/integrated contrasts.
    
- **Robotics/automation** (AMRs vs integrated systems) — mixed hardware/software option exercisability.  
    _(Seeking your guidance on 2–3 additional, Cusumano‑style platform arenas.)_
    

**Outcome of your suggestions:** We’ll lock 2–3 verticals → harvest T1 texts → run multiverse (step‑up ~ Vagueness × Flexibility) → produce evidence heatmaps + calibration checks.

_(Slide sources: prototype results & pivot notes; pipeline & quantum focus; W2 process and windows.)_

---

## 2) What to deliver in the meeting + extraction spec + Scott’s guidance + your progress

**Core idea to deliver (10‑second version):**

> _“We can read entrepreneurial promises as priors. Ambiguity can preserve real options. The clean test is whether later **valuation step‑ups** are larger when early promises were more ambiguous — particularly in verticals where architectural **flexibility** makes options exercisable.”_  
> Theoretical anchor: step‑up is the revealed Bayesian update; informativeness and cost of experiments drive it.

**Key features to extract from any candidate vertical (data spec):**

1. **Founding‑moment text (T1)**: deck blurbs, demo‑day descriptions, early press, archived sites — to score **vagueness** (LIWC certitude + embedding‑specificity).
    
2. **Architecture labels (F)**: modular vs integrated (and levels), mapping option exercisability; hardware intensity as integration‑cost proxy.
    
3. **Funding panel**: A round in **2021–22**, follow‑on rounds through **2024–25**, with **A→B step‑up** (preB / postA).
    
4. **Confound controls**: regulation shocks; team quality; accelerator effects; market cycle windowing (unified 2022‑12 baseline).
    
5. **Heterogeneity**: hardware vs software, platform vs product, ecosystem role (complementors vs integrators). (Cusumano relevance.)
    

**What Scott suggested (to cite crisply):**

- Find a **boom/era of ferment** with **20–30+ comparables**, **founding decks**, and **observable A→B** outcomes (examples he gave: clean energy mid‑2000s, AI drug discovery, YC cohorts, CDL).
    

**What you’ve tried so far (your choices, documented):**

- **Built** a working demo + pipeline (V, F, funding), ran prototype regressions, and documented next‑step diagnostics.
    
- **Pivoted** main inference from EV/AV (policy‑confounded) to **Quantum & AI hardware** (market learning, architecture heterogeneity); EV/AV kept as governance case.
    
- **Locked W2 process:** xarray multiverse (≈288 specs), unified windows (post‑correction baseline 2022‑12), direction‑aware evidence heatmaps.
    
- **Data operations:** PitchBook raw ingest, company master built; identified need for **T1 original texts** (not current descriptions); set heuristics to fix A/B labeling.
    
- **Three flexibility tiers** (rigid/modular/flexible) for quantum (SC / ion‑photon / software‑SDK) to operationalize F.
    

---

## 3) Two things that surprised you and changed your thinking (very crisp)

1. **DV switch to step‑up (not “got B or not”).**
    
    - Theory: step‑up is **inversely proportional to the prior** (p_1) — the exact Bayesian signature of a long‑shot that clears a milestone.
        
    - Evidence: after AWS lowered early experimentation costs, **conditional step‑ups rose ~15–20%**, while failures also rose — precisely what the “long‑shot bets” mechanism predicts.  
        **Implication:** Model _ambiguity → later step‑up_ as the primary DV; treat “got B” only as a by‑product.
        
2. **Vertical choice must follow “informativeness × exercisability,” not topic fashion.**
    
    - Learning lens: Experiments create value only if they **change decisions**; informativeness depends on test design (specificity/sensitivity) **and** the architecture’s option exercisability.
        
    - Industry pattern: software > hardware on **value inflection per dollar**; heterogeneous step‑ups across sectors reflect experiment cost and information yield.  
        **Implication:** Prioritize verticals with measurable A→B step‑ups and clear architectural contrasts; avoid domains where regulation, not learning, drives outcomes — consistent with your W2 pivot.
        

---

### (Optional) 6‑line outreach note to Michael

> _Subject:_ Which verticals would best reveal option value in founders’ promises?  
> _Hi Michael—_ I’m testing when **strategically ambiguous** founder promises yield larger **valuation step‑ups** at A→B, especially where **architectural flexibility** makes options exercisable. I’m piloting **Quantum & AI hardware** and need **2–3 additional verticals** that fit your architecture/platform lens **and** give (i) founding‑moment texts and (ii) observable step‑ups within 24–35 months. Which platform arenas would you pick? Happy to share the pipeline & early diagnostics if useful.

---

### Quick intent tags

- **#goal:** Lock 2–3 data‑rich verticals (architecture contrasts, observable A→B step‑ups) to test _Ambiguity × Flexibility → Step‑up_.
    
- **#action:** Harvest T1 texts, label architectures, run multiverse, deliver heatmaps and calibration plots.
    
- **#belief:** Step‑ups operationalize Bayesian updating; ambiguity helps when **options are exercisable** and experiments are **informative**.
    

---

**Notes & sources used above:** prototype results & pivot notes from _founders use strategic ambiguity.pdf_ (model results; quantum pivot; pipeline) ; W2 process and windows (multiverse, baseline, low‑regulation rationale) ; Scott’s domain guidance (era of ferment; decks; observable A→B) ; JFE 2018 step‑up mechanism & estimates (Ewens–Nanda–Rhodes‑Kropf) ; Nanda (2024) Bayesian learning & value‑inflection/experiment design by sector ; operational progress logs for data/pipeline .

---

2025-06-20

with [[charlie_fine]]
[[miscrosoft_sceret]], [[strategy rules]], [[staying power]]

![[michael_cusumano 2025-06-20-5.svg]]
%%[[michael_cusumano 2025-06-20-5|🖋 Edit in Excalidraw]]%%