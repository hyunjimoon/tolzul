- [[#Core Strategic Concepts|Core Strategic Concepts]]
- [[#Cost Structure|Cost Structure]]
- [[#Stakeholder Dynamics|Stakeholder Dynamics]]
- [[#Mathematical Framework|Mathematical Framework]]
- [[#Entrepreneurial Context|Entrepreneurial Context]]
- [[#Dimensional Framework|Dimensional Framework]]
- [[#Units|Units]]

## Core Strategic Concepts

- **Push strategy**: Act first, learn second - make quality investment decisions (q*) then update understanding of stakeholder responsiveness (βc, βr) based on outcomes
- **Pull strategy**: Learn first, act second - extensively research stakeholder responsiveness (βc, βr) before committing to quality investment decisions (q*)
- **Integrated Push-Pull**: Simultaneous action and learning through controlled experimentation and rapid iteration
- *_Quality investment (q_)**: The optimal level of "fitness of use" - encompassing all non-monetary aspects of product/service refinement including performance, reliability, aesthetics, user experience, and manufacturability
- **Quality**: "Fitness of use" - everything about the product/service excluding price; the non-monetary dimensions that stakeholders evaluate
- **Robustness**: High probability of reaching optimal solution within practical time constraints
- **Efficiency**: Speed of convergence to optimal solution in competitive environments

## Cost Structure

- **Overage cost (Co)**: Cost to the organization of making product that wouldn't be sold (e.g., inventory, committed capacity, specialized components); 
- **Underage cost (Cu)**: Cost to organization of not being able to deliver the promise (e.g., lost sales, reputation damage, customer defection); disappointing real customers who wanted what you promised
- **Critical ratio (CR)**: Cu/(Co + Cu) - threshold that determines optimal resource allocation priority

## Stakeholder Dynamics

- **Stakeholder clockspeeds**: The different rates at which various stakeholders (e.g., customers, partners, investors) update their beliefs, make decisions, and require action. This temporal misalignment can amplify the complexity of degenerate decision problems.
- **Stakeholder responsiveness (β)**: Sensitivity parameter measuring how stakeholder commitment probability changes with quality improvements (dimensionless)
- **Commitment probability**: Likelihood that a stakeholder (customer or partner) will fulfill their role in value creation
- **Joint optimization**: Decision-making framework that considers multiple stakeholder quality responses simultaneously
- **Asymmetric sensitivity**: Stakeholders exhibiting different responsiveness patterns to the same quality investments (not conflicting preferences, but different quality sensitivity)


## Mathematical Framework

- **Newsvendor logic**: Operations research framework for optimizing decisions under demand uncertainty, adapted for stakeholder coordination
- **Sigmoid response function**: S-shaped curve modeling realistic stakeholder behavior (slow initial response, rapid middle response, diminishing returns)
- **Bayesian updating**: Method for continuously refining beliefs about stakeholder responsiveness based on new evidence
- **Linear vs nonlinear models**: Progression from simple threshold-based decisions to sophisticated optimization frameworks

## Entrepreneurial Context

- **Exploitation vs Exploration duality**: Fundamental tension between leveraging current capabilities and discovering new opportunities
- **Clockspeed pressure**: Time constraints that make decision speed critical for competitive advantage
- **Venture mortality risk**: Binary success/failure stakes that make robustness essential for survival
- **Dynamic capability**: Organizational ability to sense opportunities, seize them, and reconfigure resources accordingly

## Dimensional Framework

- **Quality dimension**: Non-monetary "fitness of use" characteristics (performance, reliability, aesthetics, manufacturability)
- **Cost dimension**: Pure monetary impacts (overage costs, underage costs, component expenses)
- **Responsiveness dimension**: Stakeholder sensitivity to quality improvements (β parameters, commitment probabilities)

# Performance metric
- prescription effectiveness
- prescription profitability
- prediction accuracy
- prediction effectiveness
- updated efficiency

## Units

|Variable|Unit|Tesla Roadster Example|Definition|
|---|---|---|---|
|**T**|months|24 months|Total development time available|
|**r**|dimensionless|0.2|Fraction of time spent on learning vs building|
|**q**|dimensionless [0,1]|0.85|Quality level achieved (fitness for use)|
|**β_r**|dimensionless|0.3|Resource partner responsiveness to quality|
|**β_c**|dimensionless|0.8|Customer responsiveness to quality|
|**P_r**|probability [0,1]|0.745|Resource partner commitment probability|
|**P_c**|probability [0,1]|0.68|Customer commitment probability|
|**C_o**|$|$50M|Overage cost (unsold inventory, excess capacity)|
|**C_u**|$|$200M|Underage cost (lost sales, reputation damage)|
|**V**|$|$300M|Value when both stakeholders commit|
|**L**|$|$85M|Expected loss from mismatches|


### The Degeneracy Canon (A0 → C0 → A0')

|Analogy (The LEGO Pile)|Paper Construct & Key Objects|
|---|---|
|**The Problem:** A giant, messy pile of LEGOs that is confusing and overwhelming.|**The Degenerate Problem (`A0`):** A decision space where variables vastly outnumber constraints.|
|**The "Seed":** The hidden insight that some pieces, like the big flat baseplates, are more important for starting a strong structure.|**The Economic Seed:** The underlying economic structure of `A0`, specifically the inherent existence of asymmetric mismatch costs: Underage Cost (`Cu`) and Overage Cost (`Co`).|
|**The Solution:** Learning the "rules" of building—like starting with a strong base—that allow you to turn the mess into something cool.|**The Solution Framework (`C0`):** The integrated approach that uses Newsvendor logic to transform the `Cu`/`Co` seed into a navigational guide: the **optimality surface**.|
|**Masterful Application:** You now want an even _bigger_ pile of LEGOs because you see the "mess" as pure opportunity for creating amazing things.|**Purposeful Degeneracy (`A0'`):** The entrepreneur now intentionally increases degeneracy (e.g., adds stakeholders or product features), using the `C0` framework to confidently manage the complexity and generate new opportunities.|