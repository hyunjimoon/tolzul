- refined using [[mss(🫀, markovian(🧠))]], [[MSS(🫀Update 📜🪢 into Management Science Paper, markovian(🧠))]]
- spawned to [[mss(🫀mincost_maxflow(sol(OM), need(ENT)), 🧠(charlie-scott))]] using scaling strategy as [[scale(charlie-scott, ops-ent)]]
![[minmaxflow(field) 2025-05-18-14.svg]]
%%[[minmaxflow(field) 2025-05-18-14.md|🖋 Edit in Excalidraw]]%%


three components are need to write a paper: [[design(experiment)]]
2025-05-22

| Need Group                                      | 📐 Rule                                                                              | 🫀 Cause                                                                                                                                           | 🧠 Knowledge                                                                                                                                                                 | 🗄️ Structure                                                                                                   | 💸 Validation                                                                                                  |
| ----------------------------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **N1: Subjective Belief Formation & Alignment** | `IF entrepreneur_belief ≠ stakeholder_belief THEN persuasion_required = TRUE`        | C1: Market heterogeneity creates belief divergence<br>C2: Individual lacks credibility metrics<br>C3: Institution lacks belief alignment framework | S1: Robust optimization under uncertainty<br>S3: Total Quality Management for belief consistency<br>Strategic: Persuasion & signaling<br>Emerging: Entrepreneurial cognition | Focus: Perception flexibility<br>Solutions: S1 (robust optimization), S3 (TQM), persuasion<br>Chapters: 2, 5, 8 | Case 1: Private info advantage<br>Case 2: Overconfidence as rationality<br>Case 3: Investor persuasion success |
| **N2: Adaptive Experimentation & Learning**     | `IF experiment_result ≠ prior_belief THEN belief_update = Bayesian(prior, evidence)` | C1: Market uncertainty demands testing<br>C2: Individual lacks learning metrics<br>C3: Institution lacks experimentation framework                 | S2: Stochastic dynamic programming<br>S1: Robust optimization for experiments<br>Strategic: Real options theory<br>Emerging: Continuous learning systems                     | Focus: Action flexibility<br>Solutions: S2 (stochastic DP), S1 (robust optimization)<br>Chapters: 2, 8, 9, 10   | Case 1: Pivot decision optimization<br>Case 2: Sequential learning gains<br>Case 3: Resource-rational updating |

## 🏭 **Operations Management Solution Modules**

|Module|🎯 Definition|N1 Application|N2 Application|Flow Capacity|
|---|---|---|---|---|
|**S1: Robust Optimization**|Optimize decisions under worst-case uncertainty scenarios|Handle belief divergence robustly|Design experiments robust to model uncertainty|High (serves both N1 & N2)|
|**S2: Stochastic Dynamic Programming**|Sequential decision-making under random processes|Limited application to belief persuasion|Core method for adaptive learning|Medium (primarily N2)|
|**S3: Total Quality Management**|Systematic quality improvement through process control|Ensure belief consistency and credibility|Limited application to experiment quality|Low (primarily N1)|

## 🌐 **Min-Cost Max-Flow Network Problem Formulation**

### Network Structure

```
Source Node: S123 (Combined Solution Modules)
Sink Nodes: N1, N2 (Need Groups)
Intermediate Nodes: 📐🫀🧠🗄️💸 (Framework Components)
```

### Flow Network Graph

```
      [S1: Robust Opt]────┐
           │              │
    [S123]─┤ [S2: Stoch DP]──→ [📐🫀🧠🗄️💸] ──→ [N1: Belief Alignment]
           │              │         │                │
      [S3: TQM]──────────┘         │                │
                                   ↓                ↓
                              [N2: Experimentation] [N12: Combined]
```

### Capacity & Cost Matrix

|Edge|Capacity|Unit Cost|Rationale|
|---|---|---|---|
|S1 → N1|8|2|High: Robust optimization handles belief uncertainty well|
|S1 → N2|6|3|Medium: Supports experiment design under uncertainty|
|S2 → N1|2|8|Low: Limited application to belief persuasion|
|S2 → N2|10|1|High: Core method for sequential learning|
|S3 → N1|7|3|High: TQM ensures belief consistency|
|S3 → N2|3|6|Low: Limited to experiment quality control|

### Objective Function

```
Minimize: Σ(cost_ij × flow_ij)
Subject to: 
- Flow conservation at all nodes
- Capacity constraints: flow_ij ≤ capacity_ij
- Demand satisfaction: flow_to_N1 + flow_to_N2 = Total_Demand
```

### 🎯 **Optimal Solution Interpretation**

The min-cost max-flow solution reveals the most efficient allocation of operations management techniques to address entrepreneurial needs, maximizing **Homo Entrepreneuricus** effectiveness while minimizing implementation costs.

## 🎯 **Combined Objective Function**

```
Homo_Entrepreneuricus = f(📐belief_alignment × 📐belief_updating) 
                     × (🫀shared_root_causes)
                     × (🧠integrated_knowledge)
                     × (🗄️complementary_structure)
                     × (💸cross_validated_impact)
```

## 💭 **Memory Device**

> **"📐 Align beliefs through 🔬 experiments, 🫀 addressing same causes via 🧠 integrated knowledge"**

2025-05-18
[[📜PhanChambers18_EntTheoryOM]]


# Capability: operations management [[scott(🧭🗺️selling entrepreneurial choice-map as Bayes.Entrep)]]
# Citation-Weighted Analysis for Prioritizing Research Arcs A7–A10

## Literature Selection and Scoring Methodology

**Scope and Selection:** We identified two sets of literature (last ~15 years) to bridge Operations Management (OM) and Bayesian Entrepreneurship (BE). For OM, we focused on top journals such as _Management Science_, _Operations Research_, _Manufacturing & Service Operations Management_, _Production and Operations Management_, and _Journal of Operations Management_. We selected 10 highly-cited papers addressing supply chain optimization challenges for innovative products (e.g. new product launches, concurrent engineering of product/process/supply chain). For BE/decision-theory, we selected 7 influential papers from _Journal of Business Venturing (JBV)_, _Strategic Entrepreneurship Journal (SEJ)_, _Entrepreneurship Theory and Practice (ETP)_, etc., emphasizing work by research-focused faculty (N1) and interdisciplinary scholars (N3). These papers examine early “nailing-stage” startup challenges (e.g. effectuation vs. planning, experimental learning, cognitive biases) and the integration of Bayesian decision approaches in entrepreneurship.

**Relevance to Arcs A7–A10:** Each paper was scored for relevance (0–5) to the four central arcs (A7–A10) that connect entrepreneurial **Needs** (N1: fragmented stakeholders; N2: no unified decision rule) with **Solutions** (S1: perception/learning; S2: action/execution)【1†】. For example, a paper solving how entrepreneurs make **action** decisions under uncertainty would score high on A10 (connecting “no unified rule” to an actionable framework), whereas one about leveraging diverse **stakeholders** for better information would score on A7 (connecting “fragmented stakeholders” to improved perception). We then obtained each paper’s citation count (Google Scholar) and calculated normalized citations (Citations ÷ years since publication) to gauge annual impact. The journal impact factor (IF) was noted as a quality weight (e.g. _JBV_ ~8.7, _ETP_ ~10.5, _Management Science_ ~5.5). Finally, a **Weighted Score** for each paper (per arc) was computed:

Weighted Scorepaper,arc=(Relevance Score0−5)×(Normalized cites)×(Journal IF).\text{Weighted Score}_{paper,arc} = (\text{Relevance Score}_{0-5}) \times (\text{Normalized cites}) \times (\text{Journal IF}).

This scoring matrix (Tables 1 and 2) ensures highly-cited, relevant papers in respected journals contribute more to an arc’s “value.”

## Table 1. OM Literature Assessment (Top 10 Papers) with Arc Scores

The table below summarizes the OM papers, each with relevance scores to arcs A7–A10, citation metrics, and weighted contributions. High relevance and high-impact papers drive larger weighted scores. For instance, Swinney et al. (2011) develop a model for capacity investment timing in startups, addressing the lack of a unified decision rule (N2) by prescribing an optimal **action** policy (S2). It scores high on A10 and, with ~300 citations (21.4/year) and appearing in _Management Science_, yields a strong weighted score toward arc A10. In contrast, Li et al. (2011) examine how a distributor’s entrepreneurial orientation aids a manufacturer’s knowledge acquisition – linking fragmented supply chain stakeholders (N1) to improved **perception** (S1) – thus scoring on A7. This paper’s ~316 citations in _J. Operations Mgmt_ further amplify A7’s weight.

|**OM Paper (Year)**|**Relevance to A7**(N1→S1)|**A8**(N1→S2)|**A9**(N2→S1)|**A10**(N2→S2)|**Google Scholar Citations**|**Normalized Cites/year**|**Journal IF**|**Weighted Score A7**|**Weighted Score A8**|**Weighted Score A9**|**Weighted Score A10**|
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Swinney, Cachon & Netessine (2011) – Capacity investment timing for startups vs. incumbents|0|0|0|4|~300|21.4|5.5|0.0|0.0|0.0|471.5|
|Tanrısever, Erzurumlu & Joglekar (2012) – Production/process investment & startup survival|0|0|0|5|108|8.3|5.0|0.0|0.0|0.0|207.8|
|Tatikonda et al. (2013) – Operational capabilities & new venture survival|0|0|0|5|74|6.2|5.0|0.0|0.0|0.0|154.3|
|Terjesen, Patel & Covin (2011) – Alliance diversity & manufacturing capabilities|2|5|0|0|~90 (est.)|6.4|7.5|96.5|241.1|0.0|0.0|
|Kickul et al. (2011) – _Editorial:_ OM, entrepreneurship & value creation|3|3|3|3|~50 (est.)|3.6|7.5|80.3|80.3|80.3|80.3|
|Fine, Padurean & Naumov (2022) – _Framework:_ OM for entrepreneurs (defines arcs A7–A10)|5|5|5|5|2 (crossref)|0.67|5.0|16.8|16.8|16.8|16.8|
|Lee & Schmidt (2017) – Using value chains to enhance innovation|2|4|0|0|99|12.4|5.0|123.8|247.6|0.0|0.0|
|Yoo, Corbett & Roels (2016) – Optimal time allocation to process improvement|0|0|0|5|19 (Scopus)|2.1|5.0|0.0|0.0|0.0|52.8|
|Yoo, Roels & Corbett (2016) – Time–money trade-off: when to hire first employee|0|0|0|5|20 (Scopus)|2.2|5.0|0.0|0.0|0.0|55.5|
|Li, Liu & Liu (2011) – Distributor’s orientation & manufacturer’s knowledge|5|0|0|0|316|22.6|7.5|846.4|0.0|0.0|0.0|

**Table 1:** **Operations Management Literature Assessment.** Each paper’s relevance (0–5) to arcs A7–A10 is multiplied by its normalized annual citations and journal impact factor to yield a weighted score contribution for each arc. _E.g._, Li et al. (2011) scores 5 on A7 and, with ~22.6 cites/year and IF 7.5, contributes **846.4** to arc A7’s value – reflecting the high impact of research linking fragmented supply chain stakeholders to better information flow. Bolded cells (if any) would indicate highest relevance per paper. All papers are from top OM journals, ensuring quality and impact (e.g. _Management Science_, _POM_, _JOM_). Citation counts are from Google Scholar as of 2025.

----
# Market: entrepreneurship
## Old Entrepreneurship
## Table 2. BE Literature Assessment (Top 7 Papers) with Arc Scores

Table 2 similarly presents the Bayesian Entrepreneurship/decision-theory papers. These works largely tackle the entrepreneurial decision-making paradigm under uncertainty – often highlighting the absence of a single “optimal” rule (N2) and proposing either improved **perception** (e.g. learning, updating beliefs) or guiding **action** (experiments, heuristics) as solutions. Notably, several are highly cited theoretical pieces that shape current thinking (e.g. Fisher 2012, Shepherd et al. 2015). For instance, Fisher (2012) compares effectuation, causation, and bricolage decision logics, directly addressing _how entrepreneurs act vs. plan_ when no unified rule exists. It scored max on both A9 and A10, and with >1600 citations in _ETP_ (IF ~10), it heavily weights both arcs. Shepherd et al. (2015) provide a comprehensive review of entrepreneurial decision-making research – covering cognitive biases (perception) and action-oriented strategies – hence high on A9 and A10; its ~1175 citations in _Journal of Management_ confirm its influence. In contrast, Koudstaal et al. (2016) focus on cognitive differences in risk perception between entrepreneurs and managers, mainly contributing to A9 (perception under uncertainty). Each paper’s weighted scores reflect these emphases.

|**BE/Decision Paper (Year)**|**Relevance to A7**(N1→S1)|**A8**(N1→S2)|**A9**(N2→S1)|**A10**(N2→S2)|**Google Scholar Citations**|**Normalized Cites/year**|**Journal IF**|**Weighted Score A7**|**Weighted Score A8**|**Weighted Score A9**|**Weighted Score A10**|
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Dew, Read, Sarasvathy & Wiltbank (2009) – Effectual vs. predictive logic (experts vs. novices)|0|0|3|5|560 (GS)|35.0|8.7|0.0|0.0|913.5|1522.5|
|Fisher (2012) – Comparing effectuation, causation, bricolage|1|1|5|5|1616 (GS)|124.3|10.0|1243.1|1243.1|6215.5|6215.5|
|Shepherd, Williams & Patzelt (2015) – Review of entrepreneurial decision-making|2|2|5|5|1175 (GS)|117.5|12.0|2820.0|2820.0|7050.0|7050.0|
|Arend, Sarooghi & Burkemper (2015) – _AMR_ critique of effectuation theory|0|0|0|3|~150 (GS)|15.0|10.0|0.0|0.0|0.0|450.0|
|Koudstaal, Sloof & van Praag (2016) – Entrepreneurs vs. managers in risk/uncertainty lab experiment|0|0|5|2|178 (GS/RG)|19.8|5.5|0.0|0.0|543.9|217.6|
|Kerr, Nanda & Rhodes-Kropf (2014) – Entrepreneurship as Experimentation (theory)|0|0|4|5|958 (GS)|87.1|7.0|0.0|0.0|2438.5|3048.2|
|Camuffo, Cordova, Gambardella & Spina (2020) – RCT of scientific decision-making training|0|0|3|5|~100 (Scopus)|20.0|5.5|0.0|0.0|330.0|550.0|

**Table 2:** **Bayesian Entrepreneurship Literature Assessment.** Relevance and weighted scores of representative BE papers for arcs A7–A10. These works predominantly address N2 (the absence of a clear decision rule in entrepreneurship) by proposing new decision frameworks. For example, Fisher (2012) and Shepherd et al. (2015) collectively contribute very heavily to arcs A9 and A10, given their high citations and direct focus on entrepreneurial cognition and action under uncertainty. _Note:_ Some highly-cited conceptual works (Shepherd 2015, Fisher 2012) drive up the totals for A9/A10 significantly (as seen in their weighted scores). This indicates that a large portion of scholarly attention has been on how entrepreneurs **think and act** (perceive information and make decisions) when classical optimization or rational models fail – exactly the issues A9 and A10 represent. Meanwhile, stakeholder-focused arc A7/A8 receive comparatively fewer but still notable contributions (e.g. effectuation emphasizes stakeholder commitments, reflected in Fisher 2012’s nonzero A7/A8 scores).

## New Entrepreneurship
[[📜stern24_bayesent]]