---
collection:
  - "[[Papers]]"
author_ids:
  - Bengt Holmstrom
field: 🐙ops/🐢inv
year: 1979
rank: 5
module: M1. Pay for Performance
course: "[[14.282 Organizational Economics]]"
tags:
  - moral-hazard
  - incentive-design
  - risk-sharing
  - principal-agent
created: 2025-10-20
modified:
  - 2025-10-20T00:00:00-05:00
---

# Moral Hazard and Observability

## Summary
Foundational principal-agent model establishing the **risk-incentive tradeoff**. When effort is unobservable and the agent is risk-averse, optimal contracts trade off insurance (fixed pay) against incentives (variable pay).

## Key Concepts

### The Principal-Agent Problem
- **Principal**: Risk-neutral employer
- **Agent**: Risk-averse employee
- **Asymmetry**: Principal observes output, not effort
- **Challenge**: Design contract that induces optimal effort

### Risk-Incentive Tradeoff
$$w(x) = \alpha + \beta \cdot x$$

Where:
- $w(x)$: wage as function of output $x$
- $\alpha$: fixed component (insurance)
- $\beta$: performance sensitivity (incentive)
- Higher $\beta$ → stronger incentives BUT more risk for agent

### First-Best vs. Second-Best
- **First-Best** (effort observable): Perfect risk-sharing, no distortion
- **Second-Best** (effort unobservable): Incentive cost + risk-bearing cost
- Optimal $\beta^*$ balances moral hazard vs. risk premium

## Critical Insights

> **Why this matters**: Explains why we can't have both perfect insurance AND perfect incentives. All real-world contracts reflect this tradeoff.

### Three Core Implications:
1. **No perfect contracts**: Can't achieve first-best with moral hazard
2. **Risk costs incentives**: Risk aversion → weaker incentives optimal
3. **Information matters**: Better signals → better contracts

### The Informativeness Principle
Any signal correlated with effort should be used in the contract, even if not perfectly correlated with output.

## Connections

**Builds foundation for**:
- [[📜holmstrom91_multitask]] - Multi-dimensional incentives
- [[📜holmstrom82_career]] - Implicit incentives via career concerns
- [[📜bgm94_subjective]] - Subjective performance evaluation

**Related courses**:
- [[14.282 Organizational Economics]] - M1: Pay for Performance
- [[14.281 Contract Theory]] - Moral hazard fundamentals

**Applications to research**:
- **Entrepreneurship**: How to pay founding teams? Equity vs. salary
- **Operations**: Production bonuses vs. quality metrics
- **Innovation**: R&D incentives - pay for patents or publications?

## Mathematical Framework

### Agent's Problem
$$\max_{a} \mathbb{E}[u(w(x))] - c(a)$$
Subject to: $x = f(a, \theta)$ where $\theta$ is noise

### Principal's Problem
$$\max_{w(\cdot)} \mathbb{E}[x - w(x)]$$
Subject to:
- IR: $\mathbb{E}[u(w(x))] - c(a) \geq \bar{u}$
- IC: $a \in \arg\max_{a'} \mathbb{E}[u(w(x))] - c(a')$

## Discussion Notes

From [[14.282 Organizational Economics]]:
- **Holmstrom's genius**: Showed why "pay for performance" can't be too strong
- **Real-world puzzle**: Why do CEOs have such high pay-performance sensitivity?
  - Maybe: Not risk-averse? Wealth effect? Selection?
- **Extension needed**: Multi-task settings (→ Holmstrom & Milgrom 1991)

## Questions for Further Research
1. How does risk aversion vary across individuals/contexts?
2. Can we measure the cost of moral hazard empirically?
3. What about behavioral biases (loss aversion, reference points)?
4. How do career concerns affect optimal $\beta$?

---

*"The optimal contract balances insurance and incentives—neither can be perfect"* - Holmstrom (1979)
