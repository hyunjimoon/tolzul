---
collection:
  - "[[Papers]]"
author_ids:
  - Sanford J. Grossman
  - Oliver D. Hart
field: 🐢inv/🐅cba
year: 1986
rank: 5
module: M4. Boundary of the Firm
course: "[[14.282 Organizational Economics]]"
tags:
  - property-rights
  - firm-boundaries
  - incomplete-contracts
  - residual-control
created: 2025-10-20
modified:
  - 2025-10-20T00:00:00-05:00
---

# The Costs and Benefits of Ownership: A Theory of Vertical and Lateral Integration

## Summary
Nobel Prize-winning paper (Hart, 2016) that revolutionized theory of the firm. Shows that **ownership = residual rights of control** over non-contractible decisions. Integration changes ex ante investment incentives by allocating these control rights. Provides micro-foundations for when firms should integrate vs. outsource, based on which party's investment is more important.

## The Central Question

**Puzzle (after Coase)**:
- Coase (1937): Firms exist to minimize transaction costs
- Williamson (1971): Integration solves hold-up problem
- **But**: What exactly IS ownership? How does it affect behavior?

**GH Answer**: 
> Ownership is residual control rights. It affects ex ante investment incentives by determining who controls non-contractible decisions.

## Key Concepts

### Residual Rights of Control

**Definition**: The right to decide anything not specified in contract

**Example**: 
- Owner of building can:
  - Change use (if not restricted)
  - Modify structure
  - Exclude others
  - Sell asset

**Key insight**: Contracts incomplete → some decisions non-contractible → owner decides

### Property Rights Theory (PRT)

**Three elements**:

#### 1. **Incomplete Contracts**
Cannot specify all contingencies ex ante:
- Too costly to write
- Unforeseen circumstances
- Non-verifiable actions

#### 2. **Residual Control**
For non-contractible decisions, owner decides:
- What to produce
- How to produce  
- Who has access
- When to shut down

#### 3. **Investment Incentives**
Anticipating who controls ex post:
- Affects ex ante relationship-specific investments
- **This** determines optimal ownership structure

## The Model

### Setup: Two Parties, One Asset

**Players**:
- **Party 1**: Supplier (e.g., component manufacturer)
- **Party 2**: Buyer (e.g., final assembler)

**Asset**: Production equipment (e.g., specialized machine)

**Timeline**:
1. **t=0**: Ownership structure chosen, investments made
2. **t=1**: Uncertainty resolved, trade occurs
3. Parties bargain over surplus (Nash bargaining)

### Investment Decisions

Each party invests $a_i$ in relationship-specific capital:
- Cost: $c_i(a_i)$
- Increases joint surplus $v(a_1, a_2)$
- **Problem**: Non-contractible, so hold-up possible

### Ownership Structures

Three options:

| Structure | Who Owns Asset | Outside Options | Notation |
|-----------|---------------|-----------------|----------|
| **Non-Integration** | Party 1 (Supplier) | $\bar{v}_1(a_1), \bar{v}_2(a_2)$ | NI |
| **Integration** | Party 2 (Buyer) | $\bar{v}_1(a_1 \| 2), \bar{v}_2(a_2 \| 2)$ | I |
| **Reverse Integration** | Party 1 (Supplier) | ... | RI |

**Key**: Ownership affects **outside options** (what each party gets if trade breaks down)

### The Trade-Off

**Owner's investment**:
- Gets higher share of surplus (stronger bargaining position)
- **Better** incentive to invest

**Non-owner's investment**:
- Gets lower share (weaker bargaining position)
- **Worse** incentive to invest

**Optimal ownership**: Allocate to party whose investment is more important

## Critical Insights

> **Why this matters**: First formal theory explaining WHY ownership matters and WHEN to integrate. Bridges Coase (why firms exist) with Williamson (hold-up problem) with mechanism design (optimal contracts).

### Four Revolutionary Implications

#### 1. **Ownership Is About Control, Not Just Returns**

**Traditional view**: Owner gets residual income (profits)

**GH view**: Owner gets **residual control rights**
- Income rights can be contracted
- Control rights cannot (by definition of residual)
- **Control** is what matters for investment incentives

**Example**: 
- Franchisee owns restaurant (control)
- But franchisor gets share of revenues (income)
- Why? Franchisee's local effort more important than franchisor's brand investment

#### 2. **Integration Has Costs and Benefits**

**Benefit**: Stronger incentive for buyer's investment
**Cost**: Weaker incentive for supplier's investment

**When to integrate**:
$$\text{Benefit}(\uparrow \text{buyer investment}) > \text{Cost}(\downarrow \text{supplier investment})$$

**Not** about eliminating transaction costs—about **balancing** investment incentives

#### 3. **Complementarity Matters**

**Supermodularity**: If investments are complementary
$$\frac{\partial^2 v}{\partial a_1 \partial a_2} > 0$$

Then:
- One party's investment increases return to other's investment
- Stronger reason to allocate control efficiently
- May favor joint ownership or profit-sharing

#### 4. **Asset Specificity Is Key**

**When is ownership important?**
- High asset specificity → large holdup problem → ownership matters more
- Low asset specificity → small holdup → ownership matters less

**Prediction**: See integration when:
- Relationship-specific investments large
- Complementarity between investments
- One party's investment clearly more important

## Connections

**Builds on**:
- [[Space/Sources/Lab/📜coase37_nature]] - Why firms exist (transaction costs)
- [[📜williamson71_integration]] - Hold-up problem
- [[📜williamson79_tce]] - Asset specificity and governance

**Extended by**:
- [[📜hm90_property]] - Multiple assets, formal model
- [[📜bgm02_relational]] - Adding relational contracts
- [[📜atalay14_vertical]] - Empirical evidence

**Related to**:
- M1: Incentives and investment (career concerns)
- M3: Authority and control (formal vs. real)
- M5: Non-integration with relational contracts

**Related courses**:
- [[14.282 Organizational Economics]] - M4: Boundary of the Firm
- [[14.281 Contract Theory]] - Incomplete contracts

## Classic Examples

### 1. **GM and Fisher Body (Revisited)**

**GH interpretation**:
- Fisher owns specialized dies (non-integration)
- Fisher's investment: Production efficiency
- GM's investment: Design, integration with other parts
- **Problem**: GM's investment more important → should integrate
- **History**: GM did integrate in 1926

### 2. **Hollywood Studios and Theater Chains**

**Before 1948** (Vertical integration):
- Studios owned theaters
- Studio investment: Film quality
- Theater investment: Location, customer service
- **Held**: Film quality more important → integration

**After 1948** (Paramount Decree):
- Forced separation
- Result: Some inefficiency, but more competition

### 3. **Outsourcing in Tech**

**Apple and Foxconn**:
- Foxconn owns factories (non-integration)
- Apple investment: Design, IP
- Foxconn investment: Manufacturing efficiency
- **Optimal**: Non-integration because Apple's design investment most critical
- But: Apple monitors closely, quasi-integration

## Mathematical Framework

### Party $i$'s Payoff Under Ownership Structure $k$

Ex ante investment decision:
$$\max_{a_i} \frac{1}{2}[v(a_1, a_2) - \bar{v}_{-i}(a_{-i}|k)] + \bar{v}_i(a_i|k) - c_i(a_i)$$

Where:
- First term: Share of joint surplus (Nash bargaining, 50-50 split)
- $\bar{v}_i(a_i|k)$: Outside option under ownership $k$
- $c_i(a_i)$: Investment cost

### First-Order Condition

$$\frac{1}{2}\frac{\partial v}{\partial a_i} + \frac{\partial \bar{v}_i}{\partial a_i} = c_i'(a_i)$$

**Key**: Ownership $k$ affects $\frac{\partial \bar{v}_i}{\partial a_i}$ (marginal return to investment)

### Optimal Ownership

Choose $k^*$ to maximize:
$$W(k) = v(a_1^*(k), a_2^*(k)) - c_1(a_1^*(k)) - c_2(a_2^*(k))$$

Where $a_i^*(k)$ solves FOC under ownership $k$

## Discussion Notes

From [[14.282 Organizational Economics]]:

**Why Nobel Prize?** (Hart, 2016)
- Formalized "ownership" concept
- Provided testable predictions
- Unified transaction cost, property rights literatures
- Influenced antitrust, privatization policy

**Limitations**:
- Assumes all parties invest (symmetric model)
- Nash bargaining (50-50 split)
- Two parties, one asset (simple case)
- **Extensions** needed: Multiple assets (HM 1990), relational contracts (BGM 2002)

**Empirical Challenges**:
- Hard to measure "outside options"
- Investment often unobservable
- Ownership changes infrequent
- **But**: Can test predictions about integration patterns

**GHM Message**: 
> Integration is not free. It helps some investments, hurts others. Design ownership to maximize total investment incentives.

## Questions for Further Research

1. **Multiple assets**: How to allocate when many complementary assets? (→ HM 1990)
2. **Bargaining power**: What if not 50-50? Does ownership still matter?
3. **Measurement**: How to empirically identify investment importance?
4. **Dynamics**: How does ownership evolve as relationships mature?
5. **Relational contracts**: Do relationships substitute for ownership? (→ BGM 2002)
6. **Public goods**: Does PRT apply to public sector? (privatization debate)

## Empirical Implications

**Testable predictions**:
1. Integration more likely when buyer investment critical (✓ partial evidence)
2. Asset specificity → integration (✓ confirmed, Baker-Hubbard 2003)
3. Complementary investments → joint ownership (mixed evidence)
4. Integration increases buyer investment, decreases supplier investment (hard to test)

**Policy implications**:
- Antitrust: Not all vertical integration anti-competitive (may be efficient)
- Regulation: Forcing separation may reduce investment incentives
- Privatization: Ownership assignment affects service quality

---

*"Ownership matters not because it determines who gets the income, but because it determines who gets to decide"* - Grossman & Hart (1986)
