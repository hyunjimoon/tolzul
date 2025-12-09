---
collection:
  - "[[Space/Lab/Papers]]"
author_ids:
field:
  - 🐢inv
year: 2024
created: 2025-02-02
---

abstract: The distributional impacts of congestion pricing have been widely discussed in the literature and the evidence on this is mixed. Some studies find that pricing is regressive whereas others suggest that it can be progressive or neutral depending on the specific spatial characteristics of the urban region, existing activity and travel patterns, and the design of the pricing scheme. Moreover, the welfare and distributional impacts of pricing have largely been studied in the context of passenger travel whereas freight has received relatively less attention. In this paper, we examine the impacts of several congestion pricing schemes on both passenger transport and freight in an integrated manner using a large-scale microsimulator (SimMobility) that explicitly simulates the behavioral decisions of the entire population of individuals and business establishments, dynamic multimodal network performance, and their interactions. Through simulations of a prototypical North American city, we find that a distance-based pricing scheme yields larger welfare gains than an area-based scheme, although the gains are a modest fraction of toll revenues (around 30%). In the absence of revenue recycling or redistribution, distancebased and cordon-based schemes are found to be particularly regressive. On average, lower income individuals lose as a result of the scheme, whereas higher income individuals gain. A similar trend is observed in the context of shippers — small establishments having lower shipment values lose on average whereas larger establishments with higher shipment values gain. We perform a detailed spatial analysis of distributional outcomes, and examine the impacts on network performance, activity generation, mode and departure time choices, and logistics operations.

| Section/Subsection | 🔐Research Question | 🧱Literature Brick | 🔑Key Message | Figure |
|-------------------|---------------------|-------------------|---------------|---------|
| 1. Introduction | What are distributional impacts of congestion pricing on both passenger and freight transport? | • De Palma & Lindsey (2011): Pricing taxonomy<br>• Santos & Verhoef (2011): Reviews<br>• King et al (2007): Political aspects | Equity issues are key barrier to congestion pricing - need integrated passenger/freight analysis | Fig 1: SimMobility framework showing multi-level agent interactions |
| 2. Literature Review | How have others evaluated pricing schemes and impacts? | • Arnott et al (1990): Bottleneck models<br>• MATSim studies<br>• Freight pricing literature | While welfare gains expected, distributional impacts vary by city structure and design | None |
| 3. Agent-based Model | How to model complex pricing impacts with heterogeneous agents? | • Activity-based models<br>• SimMobility architecture<br>• Behavioral choice models | SimMobility integrates passenger and freight behavior across three time scales | Fig 2: Price sensitive models in freight simulation |
| 4. Prototype City | How to create realistic test environment? | • Auto-Innovative city typology<br>• Boston calibration data<br>• Freight surveys | Generated synthetic city with 4.6M individuals and 130K establishments | Maps and network diagrams |
| 5. Pricing Schemes | What pricing structures to evaluate? | • Distance-based<br>• Cordon-based<br>• Area-based<br>• Time-varying rates | Design considers location, time period, and vehicle type specifics | Fig 3-4: Framework and trip patterns<br>Fig 5: Toll area map |
| 6. Results - Welfare | What are overall economic impacts? | • Consumer surplus models<br>• Producer surplus models<br>• Social welfare metrics | Distance-based yields highest welfare gains (2.27M USD/day) but all schemes regressive | Tables showing welfare changes |
| 7. Results - Distribution | Who wins and loses under different schemes? | • Equity analysis methods<br>• Spatial analysis tools | Higher income groups gain while lower income lose; smaller businesses disadvantaged | Fig 8-9: Spatial distribution maps |
| 8. Results - Operations | How do schemes affect system performance? | • Network metrics<br>• Activity patterns<br>• Logistics operations | Distance-based reduces VKT most; Area scheme shifts activity timing | Tables showing operational metrics |
| 9. Conclusions | What are policy implications? | • Pricing design literature<br>• Revenue recycling research | Need careful design and revenue redistribution to address equity concerns | Summary diagrams |

Key Methodological Components:
- Multi-agent simulation platform (SimMobility)
- Integrated passenger and freight modeling
- Detailed behavioral choice frameworks
- Prototype city generation process
- Three pricing scheme designs

Major Findings:
1. Distance-based pricing most effective but regressive
2. All schemes show modest welfare gains relative to toll revenue
3. Significant distributional impacts need policy attention
4. Freight carriers show strategic operational adaptations
5. Revenue recycling critical for equity outcomes

---
comparing estimating and calibrating

1. Based on the chat, here's the key point - the paper "Evaluating congestion pricing schemes using agent-based passenger and freight microsimulation" appears to discuss both estimation and calibration in transportation modeling. The key distinction discussed in the chat was:

- Estimation: Fitting an initial model to raw data, specifically getting values for betas/parameters
- Calibration: Taking estimated models and adjusting them for new contexts (e.g., taking models estimated for Boston and adjusting them for Toronto)

| Aspect | Estimation | Calibration |
|--------|------------|-------------|
| **Purpose** | Fitting initial model parameters to raw data | Adjusting existing models for new contexts |
| **Input Data** | Raw survey/empirical data | Aggregate validation data from new context |
| **Output** | Model parameters (e.g., betas) | Adjusted parameters for new context |
| **When Used** | Initial model development | Model transfer to new locations/times |
| **Example from Paper** | Original activity-based models estimated from 2010 Massachusetts Travel Survey data | Adjusting Boston parameters for Toronto: "they're in a different city, or they're in a different time period... if they were estimated for a Boston population, but now you have Toronto, and you don't actually, you don't want to recollect all of these, all these, this data" |
| **Process Type** | Statistical fitting | Iterative adjustment |
| **Data Requirements** | Detailed individual-level data | Aggregate data for validation |
| **Example Metrics** | Log-likelihood maximization | Matching traffic counts, trip distributions |

The discussion highlights a practical consideration in transportation modeling - while full estimation requires extensive data collection, calibration allows models to be adapted to new contexts more efficiently. However, this is always a balance between accuracy and practicality, as noted in the discussion about being unable to "recollect all these dozens of study, all of this, all of these travel surveys, every single time we want to apply a model to a different place."

---
using [organizing congestion pricing paper analysis cld](https://claude.ai/chat/9361c90d-c94a-4c55-99c3-c96442fa301c)