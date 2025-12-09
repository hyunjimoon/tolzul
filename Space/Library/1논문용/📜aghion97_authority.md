---
collection:
  - "[[Space/Lab/Papers]]"
author_ids:
  - Philippe Aghion
  - Jean Tirole
field: 👾cog
year: 1997
rank: 5
module: M3. Delegation & Communication
course: "[[14.282 Organizational Economics]]"
tags:
  - authority
  - delegation
  - decision-rights
  - information-asymmetry
created: 2025-10-20
modified:
  - 2025-10-20T00:00:00-05:00
---

# Formal and Real Authority in Organizations

## Summary
Distinguishes between **formal authority** (right to decide) and **real authority** (effective control). Shows that informed subordinates can have real authority even without formal authority, through strategic information transmission. Provides micro-foundations for delegation and authority allocation.

## Key Concepts

### Two Types of Authority

#### Formal Authority
- **Definition**: Contractual right to make decisions
- **Example**: CEO's legal authority over firm decisions
- **Characteristic**: Ex ante allocation, legally enforceable

#### Real Authority  
- **Definition**: Effective control over decisions
- **Example**: Expert subordinate who controls information
- **Characteristic**: Ex post, depends on information structure

### The Core Trade-off
**Principal's dilemma**:
- Retain formal authority → better aligned decisions when informed
- Delegate formal authority → agent overrules less, stronger initiative incentives

### Three Decision Structures

| Structure | Formal Authority | Real Authority | When Optimal |
|-----------|------------------|----------------|--------------|
| **Centralization** | Principal | Principal | High alignment, low initiative value |
| **Delegation** | Agent | Agent | Low alignment, high initiative value |
| **Formal Centralization, Real Delegation** | Principal | Agent | Medium alignment |

## Critical Insights

> **Why this matters**: Explains why organizational charts don't always reflect who really makes decisions. Information is power—whoever has superior information has real authority.

### Four Key Results

#### 1. **Informed Subordinates Have Real Authority**
Even with centralization (formal authority), if agent has private information:
- Agent can manipulate information
- Principal rubber-stamps agent's recommendation
- **Real authority** rests with agent

#### 2. **Initiative and Authority**
- Agent's initiative (effort to find projects) depends on control
- Delegation → high initiative (agent expects to implement)
- Centralization → low initiative (principal may overrule)

#### 3. **Loss of Control**
Principal delegates when:
$$\text{Cost of Loss of Control} < \text{Benefit of Initiative}$$

Where:
- Loss of control = probability of misaligned projects × misalignment cost
- Benefit of initiative = probability of finding good project × project value

#### 4. **Intermediate Cases**
Most interesting: **formal centralization but real delegation**
- Principal keeps formal authority (option to overrule)
- Agent knows principal is uninformed
- Agent has real authority in practice
- Better than pure delegation (preserves option value)

## Mathematical Framework

### Game Structure
1. **Agent** exerts initiative $e$ (finds project with probability $p(e)$)
2. Agent observes project quality $\theta$
3. Agent sends message $m$ to Principal  
4. Principal decides: implement project or status quo
5. Payoffs realized

### Payoff Structure
- **Principal**: $\theta$ (if project implemented)
- **Agent**: $\theta + B$ (if project implemented)
  - $B$: agent's private benefit (congruence parameter)

### Equilibrium Characterization
- If $B$ is small (high congruence): Delegation optimal
- If $B$ is large (low congruence): Centralization optimal
- If $B$ is medium: Formal centralization, real delegation optimal

## Connections

**Extends**:
- Incomplete contracts literature (Hart, Grossman)
- Information economics (cheap talk)

**Applied in**:
- [[📜bgm99_informal]] - Informal authority in relational contracts
- [[📜bandiera21_delegation]] - RCT on delegation effects
- [[📜kala24_autonomy]] - Autonomy and firm outcomes

**Related to**:
- M4: Authority and ownership (property rights theory)
- M1: Authority as implicit incentive mechanism
- M6: Organizational capacity and delegation

## Classic Examples

### 1. **CEO and Division Manager**
- **Formal**: CEO has authority
- **Real**: Manager knows local market
- **Solution**: Give manager authority unless clear misalignment

### 2. **Headquarters and Subsidiaries**
- **Formal**: HQ controls major decisions
- **Real**: Subsidiary knows local conditions
- **Tension**: HQ may overrule profitable local initiatives

### 3. **Academic Departments and Deans**
- **Formal**: Dean controls hiring
- **Real**: Department knows candidates
- **Practice**: Dean rarely overrules department recommendations

## Discussion Notes

From [[14.282 Organizational Economics]]:

**Key Insight**: 
> Delegation is not just about efficiency—it's about incentives for initiative.

**Empirical Predictions**:
- More delegation when:
  - Lower stakes (smaller $B$)
  - Higher initiative value
  - Better measurement of outcomes (accountability)
  
**Design Implications**:
- Don't just look at org chart
- Understand information flows
- Consider: Can principal verify ex post?

**Connection to M1 (Incentives)**:
- Authority allocation is an incentive device
- Affects initiative, not just decisions
- Complements other incentives (pay, career concerns)

## Questions for Further Research
1. How to measure real vs. formal authority empirically?
2. What determines congruence parameter $B$?
3. How does real authority evolve over time in organizations?
4. Can organizations design information systems to affect real authority?
5. How does this interact with relational contracts? (→ BGM 1999)

---

*"Authority is not what's written in contracts, but who controls information"* - Aghion & Tirole (1997)
