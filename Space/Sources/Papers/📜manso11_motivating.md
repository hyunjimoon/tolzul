---
collection:
  - "[[Papers]]"
author_ids:
  - Gustavo Manso
field: 🐢inv
year: 2011
module: "8. Incentives for Innovators: Contracts and Control Rights"
url: "marginnote3app://note/[TO-BE-FILLED]"
tags:
  - exploration
  - exploitation
  - incentive-design
created: 2025-01-09
성장:
  - 2025-01-09T00:00:00-05:00
---

# Motivating Innovation

## Summary
Develops theoretical model showing optimal contracts for exploration must tolerate early failure and reward long-term success. Standard incentive contracts that reward immediate success lead agents to exploit known solutions rather than explore risky alternatives with higher expected social value.

## Research Question
How should principals design incentive contracts to encourage exploration of risky, uncertain innovations rather than exploitation of known solutions?

## Key Concepts

### Exploration vs Exploitation
Agent chooses between known solution (probability p₁) and unknown solution (expected probability E[p₂] < p₁, but E[p₂|S,2] > p₁ given first-period success).

### Optimal Contract for Exploration
- wF > 0: Payment for first-period failure (tolerance)
- wS = 0: No reward for first-period success alone
- wSS >> 0: "Bonanza" for success in both periods
- wFS = c₁/(p₁-p₀): Maintains effort incentives

### Optimal Contract for Exploitation  
- wF = wSF = wFF = 0: No payment for any failure
- wSS = wFS = c₁/(p₁-p₀): Reward all success equally
- wS = c₁/(p₁-p₀) + δ: Premium for immediate success

## Main Results

### Theoretical Prediction
Contracts rewarding immediate success discourage exploration even when exploration has higher expected value.

### Contract Structure Matters
The timing and conditionality of rewards fundamentally shapes whether agents explore or exploit.

## Critical Insights

From [[scott23🛠️_econ_idea_innov_ent]]:

> **Critical**: Standard pay-for-performance systems designed for routine work actively harm innovation by punishing the failures inherent in exploration.

### Policy Implication
Research funding mechanisms should explicitly incorporate failure tolerance and long-horizon evaluation.

## Methodology

**Approach**: Two-period theoretical model  
**Data**: N/A (pure theory)
**Analysis**: 
- Agent chooses exploration vs exploitation plan
- Principal designs contract to maximize expected value
- Comparative statics on contract parameters

## Connections

**Builds on**:
- [[📜holmstrom89_agency]] - Multi-period incentives
- March (1991) - Exploration/exploitation trade-off

**Relates to**:
- [[📜azoulay11_incentives(creativity)]] - Empirical test of theory
- [[📜aghion94_management(innovation)]] - Control rights for innovation

**Influences**:
- Design of HHMI investigator program
- Venture capital contract structure
- Academic tenure systems

## Class Discussion

### Key Points
- Exploration requires fundamentally different incentive design
- Short-term performance metrics kill innovation
- Failure must be actively rewarded, not just tolerated

### Open Questions
1. How to implement in settings with multiple projects?
2. What if agent's type (explorer vs exploiter) is unknown?
3. How do team dynamics affect optimal contract design?

## Application to Course

Connects to [[🗺️(15357)]] framework:
- Ideas production function: A' = f(L_A, K_A, A; Z_A, δ)
- Z_A: Contract design is key institutional parameter
- Shows why δ (form of production function) varies with incentive structure

Related themes from [[1 Innovation]]:
- Risk-taking in innovation
- Time horizons and research strategy
- Design of innovation institutions

---

*"Tolerance of early failure and reward for long-term success motivate innovation."*
