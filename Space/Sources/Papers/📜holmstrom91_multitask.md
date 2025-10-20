---
collection:
  - "[[Papers]]"
author_ids:
  - Bengt Holmstrom
  - Paul Milgrom
field: 🐙ops
year: 1991
rank: 5
module: "M1. Pay for Performance"
course: "[[14.282 Organizational Economics]]"
tags:
  - multitask
  - incentive-design
  - task-allocation
  - organizational-design
created: 2025-10-20
성장:
  - 2025-10-20T00:00:00-05:00
---

# Multitask Principal-Agent Analyses

## Summary
Revolutionary extension of single-task moral hazard to **multi-dimensional effort**. Shows that strong incentives on one measurable task distort effort away from other important but harder-to-measure tasks. Explains low-powered incentives and organizational design choices.

## Key Concepts

### The Multi-Task Problem
Agent allocates effort across **multiple tasks**:
- Some tasks: Easy to measure (e.g., quantity)
- Other tasks: Hard to measure (e.g., quality, cooperation)

**Core tension**: Paying for what's measurable crowds out what's not.

### Task Balance Condition
$$\frac{\beta_i}{\beta_j} = \frac{MPP_i}{MPP_j}$$

Where:
- $\beta_i$: incentive weight on task $i$
- $MPP_i$: marginal product of performance measure $i$

**Implication**: Incentive weights should match productivity ratios, NOT measurability.

### The Multitasking Distortion
If Task A is measurable but Task B is not:
- Naive solution: High $\beta_A$, $\beta_B = 0$
- **Problem**: Agent over-allocates effort to Task A
- **Better solution**: Reduce $\beta_A$ to balance effort allocation

## Critical Insights

> **Why this matters**: Explains why organizations often use weak incentives (salaries) instead of strong pay-for-performance. Not because they don't care about performance, but because they care about balance.

### Three Revolutionary Implications

#### 1. **Low-Powered Incentives Can Be Optimal**
When tasks are hard to measure completely:
- Fixed wages > piece rates
- Discretionary bonuses > formulaic pay
- Example: University professors on salary (teaching + research + service)

#### 2. **Complementarity in Organizational Design**
- Job design affects optimal incentives
- Narrow jobs → can use strong incentives
- Broad jobs → need weak incentives
- Example: Assembly line (narrow) vs. consulting (broad)

#### 3. **Asset Ownership and Incentives**
Ownership gives residual control rights:
- Owner: High-powered incentives (keeps residual)
- Employee: Low-powered incentives (doesn't keep residual)
- Explains franchise (owner-operator) vs. company stores

## Mathematical Framework

### Agent's Multi-Task Problem
$$\max_{a_1, a_2} \sum_i \beta_i \cdot p_i(a_1, a_2) - c(a_1, a_2)$$

Where:
- $a_i$: effort on task $i$
- $p_i$: performance measure for task $i$
- $c(\cdot)$: cost function (often separable: $c_1(a_1) + c_2(a_2)$)

### Optimal Incentive Intensity
With task complementarity or substitutability:
- **Substitutes**: Measuring one task reduces incentive on other
- **Complements**: Measuring one task increases incentive on other

## Connections

**Extends**:
- [[📜holmstrom79_moral_hazard]] - From single to multiple tasks

**Applied in**:
- [[📜bloom13_management_india]] - Management practices as multi-task
- [[📜bgm02_relational]] - Relational contracts for multi-task settings
- [[📜bandiera20_ceo]] - CEO multi-tasking (time allocation)

**Related to organizational design**:
- Job design (narrow vs. broad roles)
- Make-or-buy decisions (M4)
- Authority allocation (M3)

## Classic Examples

### 1. **Teachers**
Tasks: Teaching quality + test prep + mentoring + admin
- Strong incentive on test scores → neglect other tasks
- Solution: Weak incentives, peer monitoring, mission alignment

### 2. **Salespeople**
Tasks: Current sales + customer relationship + market intel
- Pure commission → overselling, churning customers
- Solution: Salary + bonus, or make them franchisees

### 3. **R&D Scientists**
Tasks: Breakthrough innovation + incremental improvements + knowledge sharing
- Pay per patent → focus on patentable (not impactful) work
- Solution: Fixed pay + promotion based on peer review

## Discussion Notes

From [[14.282 Organizational Economics]]:

**Puzzle**: Why don't we see more piece-rate systems?
- **Answer**: Multi-tasking! Most jobs have multiple dimensions

**Design Principle**: 
- Narrow the job → strengthen incentives
- Broaden the job → weaken incentives
- Or: Change organizational form (ownership)

**Empirical prediction**:
- Franchises (owner-operators) vs. company stores
- Stronger incentives when tasks are substitutes
- Asset ownership screens for agents who can handle multi-task

## Questions for Further Research
1. How to empirically measure task substitutability/complementarity?
2. Can we design better performance metrics that capture multiple dimensions?
3. What role does intrinsic motivation play in multi-task settings?
4. How do relational contracts help with multi-tasking?

---

*"The problem with paying for what you measure is that you get what you pay for, not what you want"* - Holmstrom & Milgrom (1991)
