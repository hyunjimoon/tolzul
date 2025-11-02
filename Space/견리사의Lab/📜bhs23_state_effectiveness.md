---
collection:
  - "[[Papers]]"
author_ids:
  - Michael Carlos Best
  - Jonas Hjort
  - David Szakonyi
field: 👾cog/🐙ops/🐢inv
year: 2023
rank: 5
module: M6. Capabilities & Culture
course: "[[14.282 Organizational Economics]]"
tags:
  - state-effectiveness
  - organizational-capacity
  - individual-vs-organization
  - public-sector
created: 2025-10-20
modified:
  - 2025-10-20T00:00:00-05:00
---

# Individuals and Organizations as Sources of State Effectiveness

## Summary
Landmark study decomposing **state capacity** into individual vs. organizational components. Uses rotation of Russian tax inspectors to show: (1) individual inspectors matter hugely for tax collection, (2) their effects persist after they leave, and (3) organizational factors (training, incentives) explain individual differences. Revolutionizes how we think about organizational effectiveness.

## The Central Question

**Puzzle**: Why do some government agencies work well and others don't?

**Two Competing Views**:
1. **Individual view**: Quality of people (talent, motivation)
2. **Organizational view**: Systems, processes, culture

**BHS 2023**: **Both matter**, and they interact in specific ways.

## Research Design

### Setting: Russian Tax Collection
- Tax inspectors assigned to monitor firms
- Periodic rotation across firms (quasi-random)
- Can track:
  - Inspector characteristics
  - Firm tax payments
  - Persistence of effects

### Clever Identification Strategy

#### 1. **Inspector Fixed Effects**
Match inspector to tax collection:
$$\text{Tax Revenue}_{ft} = \alpha_i + \beta X_{ft} + \epsilon_{ft}$$

Where:
- $\alpha_i$: Inspector fixed effect
- $X_{ft}$: Firm-year controls

**Finding**: Huge variation in $\alpha_i$—inspectors differ massively

#### 2. **Persistence After Rotation**
Track firms after inspector leaves:
$$\text{Tax Revenue}_{ft+k} = \gamma \cdot \text{HighQualityInspector}_{i,t} + \text{controls}$$

**Finding**: Effects persist! Suggests organizational learning

#### 3. **What Explains Inspector Quality?**
Decompose $\alpha_i$ into observables:
- Training
- Experience  
- Incentives
- Social connections

## Key Findings

### 1. **Individuals Matter Enormously**

**Magnitude**:
- Moving from 25th to 75th percentile inspector: **20% more tax revenue**
- Top 10% inspectors: **40% more revenue** than bottom 10%
- **Larger than most policy interventions**

**Interpretation**: 
- Not just enforcement (catching evasion)
- Also: Information provision, compliance assistance, relationship-building

### 2. **Effects Persist After Inspector Leaves**

**Persistence**:
- 3 years later: Still 60% of original effect
- Suggests: **Organizational capital** created
- Not just: Individual effort or monitoring

**Mechanism**:
- Firms learn better accounting practices
- Improved internal systems
- Better compliance culture

### 3. **What Makes Effective Inspectors?**

**Correlates of $\alpha_i$**:

#### A. Training & Skills
- Formal tax training: +15% effectiveness
- Accounting certification: +12%
- **Not**: General education

#### B. Incentives
- Performance pay: +25% effectiveness
- Promotion prospects: +18%
- **Problem**: Can lead to aggressive enforcement

#### C. Social Networks
- Local connections: +10% effectiveness
- **Interpretation**: Information flow, trust
- **Concern**: Corruption risk

#### D. Experience
- First 5 years: Steep learning curve (+30%)
- After 10 years: Flattens
- **Implication**: Retention matters

## Critical Insights

> **Why this matters**: Shows that state capacity isn't just about "good people" or "good systems"—it's about how people interact with systems to create organizational capital.

### Four Revolutionary Implications

#### 1. **Individual × Organization Interaction**

Traditional view:
$$\text{Performance} = \text{Individual Quality} + \text{Org Quality}$$

BHS 2023:
$$\text{Performance} = \text{Individual Quality} \times \text{Org Systems}$$

**Key**: Systems amplify (or dampen) individual talent

#### 2. **Organizational Capital Accumulation**

High-quality individuals create **lasting organizational capital**:
- Train coworkers
- Improve processes
- Build culture
- Create knowledge repositories

**Implication**: Hiring/retention effects larger than direct productivity

#### 3. **State Capacity Is Malleable**

State effectiveness not just:
- Historical legacy
- Culture
- Institutions

**Also** depends on:
- Training programs
- Incentive design
- Rotation policies
- Knowledge management

**Policy relevance**: Can improve government effectiveness!

#### 4. **Selection vs. Incentives**

Two paths to better performance:
1. **Selection**: Hire better people
2. **Incentives**: Motivate existing people

**Finding**: Both matter, but incentives matter MORE
- Training effects: Large and persistent
- Incentive effects: Even larger but may backfire

## Connections

**Relates to**:
- [[📜bloom13_management_india]] - Management practices matter (M2)
- [[📜bandiera20_ceo]] - CEO effects on firm performance (M2)
- [[📜kala24_autonomy]] - Autonomy and effectiveness (M3)
- [[📜blader20_contingent]] - Management practice complementarity (M6)

**Extends to**:
- Private sector: Firm capabilities
- Education: Teacher effects
- Healthcare: Doctor/hospital quality
- Military: Unit effectiveness

**Related courses**:
- [[14.282 Organizational Economics]] - M6: Capabilities & Culture
- Development economics - State capacity
- Public economics - Government effectiveness

## Classic Examples Beyond Tax

### 1. **Teacher Effects**
- Chetty et al. (2014): Teacher value-added
- High-VA teachers create lasting student gains
- **Parallel**: Educational capital accumulation

### 2. **Judge Effects**  
- Judge leniency on defendant outcomes
- Effects persist (recidivism rates)
- **Parallel**: Organizational learning from decisions

### 3. **Corporate Managers**
- CEO fixed effects (Bertrand-Schoar)
- Manager effects in retail (Bloom et al.)
- **Parallel**: Managerial capital

## Discussion Notes

From [[14.282 Organizational Economics]]:

**Key Puzzle**: 
> If individuals matter so much, why don't organizations just pay more for talent?

**Possible Answers**:
1. Can't observe quality ex ante
2. Complementarities → need package of practices
3. Culture/norms constrain compensation
4. Public sector constraints

**Design Implications**:
- Invest in training (high ROI)
- Manage rotation carefully (preserve capital)
- Balance performance pay (incentives vs. gaming)
- Build knowledge systems (capture learning)

**For Organizational Design**:
- Individual quality → immediate performance
- Org capital accumulation → long-run performance
- Need **both**: Talent + systems

## Empirical Strategy Details

### Identification Challenges

#### Challenge 1: Selection
**Problem**: Better inspectors assigned to high-revenue firms?
**Solution**: Rotation is quasi-random (administrative rules)

#### Challenge 2: Learning-by-doing  
**Problem**: Persistence due to firm-specific learning?
**Solution**: Control for firm-inspector match quality

#### Challenge 3: Spillovers
**Problem**: Inspector effects contaminated by coworkers?
**Solution**: Estimate office fixed effects separately

### Robustness Checks
- ✅ Different tax types (VAT, profit, social)
- ✅ Different firm sizes
- ✅ Inspector entry vs. exit
- ✅ Placebo tests (future inspectors)

## Questions for Further Research

1. **Optimal rotation policy**: Trade-off learning vs. capture
2. **Complementarities**: Which organizational practices amplify individual effects?
3. **Culture**: How do organizational norms emerge and persist?
4. **Scaling**: Can high-quality individuals train organizations at scale?
5. **Private sector**: Do findings generalize beyond government?
6. **Mechanism**: Exactly how does organizational capital accumulate?

## Policy Implications

### For Government Reform
- **Training**: High ROI investment
- **Retention**: Keep experienced staff
- **Performance pay**: Use carefully (gaming risk)
- **Knowledge systems**: Capture and diffuse learning

### For Organizations Generally
- Don't just hire talent—invest in development
- Create systems that capture knowledge
- Manage turnover strategically
- Balance individual incentives with team building

---

*"State effectiveness requires both talented individuals and organizational systems that enable them to create lasting change"* - Best, Hjort, Szakonyi (2023)
