---
collection:
  - "[[Papers]]"
author_ids:
  - Rocco Macchiavello
  - Ameet Morjaria
field: 🐢inv
year: 2015
rank: 5
module: M5. Governance of Non-Integration
course: "[[14.282 Organizational Economics]]"
tags:
  - relational-contracts
  - supply-chains
  - value-of-relationships
  - kenya
  - quasi-experiment
created: 2025-10-20
modified:
  - 2025-10-20T00:00:00-05:00
---

# The Value of Relationships: Evidence from a Supply Shock to Kenyan Rose Exports

## Summary
Landmark quasi-experimental study measuring the **value of relational contracts** in supply chains. Exploits 2008 post-election violence in Kenya that disrupted flower exports. Shows that established buyer-supplier relationships are **highly valuable** (~20% premium), sustained by relational contracts, and recover faster from shocks. First clean evidence quantifying relationship value.

## The Central Question

**Theory** (BGM 2002, Levin 2003):
- Relational contracts sustained by future rents
- Should be valuable in incomplete contract settings
- **But**: How valuable? Can we measure?

**Empirical challenge**:
- Relationships endogenous (good suppliers → relationships)
- Selection bias
- Hard to observe relationship quality

**MM solution**: 
> Use **exogenous supply shock** to test how relationships respond.

## Research Design

### Setting: Kenyan Cut-Flower Industry

**Why roses?**
- Perishable (3-5 day shelf life)
- Quality heterogeneity (color, stem length, bloom size)
- Complex supply chains (growers → exporters → EU buyers)
- **Incomplete contracts**: Can't contract on all quality dimensions

**Market structure**:
- ~120 Kenyan exporters (large and small)
- ~1,000 European buyers
- Long-term relationships common (but not universal)

### The Natural Experiment: 2008 Post-Election Violence

**Shock timeline**:
- **Dec 2007**: Presidential election, disputed results
- **Jan-Feb 2008**: Ethnic violence, road blockages
- **Impact on flowers**:
  - Transport disrupted (roads unsafe)
  - Workers flee (ethnic tensions)
  - Shipments delayed/canceled
  - **Exogenous supply shock**: ~30% production loss

**Key feature**: 
- Shock NOT correlated with relationship quality
- Affects all exporters similarly
- Creates **quasi-experiment** for studying relationships

### Identification Strategy

Compare buyer-exporter pairs:

| Group | Relationship Status | Pre-Shock | During Shock | Post-Shock |
|-------|---------------------|-----------|--------------|------------|
| **Treatment** | Established relationship | High trade | ? | ? |
| **Control** | New/arm's length | Low trade | ? | ? |

**Key prediction** (relational contract theory):
- Established relationships **should** be maintained during shock
- Arm's length relationships **should** break down
- Why? Value of future rents sustains cooperation

## Key Findings

### 1. **Relationships Are Highly Valuable**

**Relationship premium**:
- Established buyers pay **10-20% more** per stem
- Even after controlling for:
  - Quality
  - Shipment size
  - Timing
  - Buyer-exporter fixed effects

**Interpretation**: 
- Not just quality (already controlled)
- Premium reflects **relationship value**
- Buyers willing to pay for reliability, flexibility, trust

### 2. **Relationships Survive Shocks**

**During 2008 violence**:

**Established relationships**:
- Trade volume: -25% (less than aggregate shock)
- Price premium: Maintained (+15%)
- Buyer loyalty: 90% continued trading

**Arm's length relationships**:
- Trade volume: -45% (worse than shock)
- Price premium: Disappeared
- Buyer loyalty: 40% stopped trading

**Conclusion**: Relational contracts act as **insurance**

### 3. **Mechanisms: Quality and Flexibility**

**Why do relationships survive?**

#### A. **Quality Assurance**
- Relationship buyers get **better average quality**
- Even during shock (lower defect rates)
- Evidence: Established exporters prioritize relationship buyers

#### B. **Flexibility**
- Relationship buyers more likely to:
  - Accept delayed shipments
  - Modify orders
  - Share information about EU market conditions

#### C. **Communication**
- More frequent contact during crisis
- Problem-solving together
- Evidence: Email/phone records

### 4. **Recovery Pattern**

**Post-shock (Mar-Jun 2008)**:

**Established relationships**:
- Quick recovery (2 months to pre-shock levels)
- Maintained quality standards
- Some relationships strengthened

**New relationships**:
- Slow recovery (6+ months)
- Lower quality initially
- Many didn't recover

**Interpretation**: 
- Relationships have **option value**
- Can flex during bad times
- Resume quickly when shock ends

## Critical Insights

> **Why this matters**: First clean measurement of relational contract value in real supply chains. Shows relationships aren't just correlated with good outcomes—they CAUSE better outcomes, especially during crises.

### Four Revolutionary Implications

#### 1. **Relational Contracts Are Valuable Insurance**

**Insurance value**:
- Against supply shocks: ~15% trade volume
- Against quality variation: ~10% defect rate reduction  
- Against opportunism: Maintained during crisis

**Unlike formal contracts**:
- Can't write contract for "be flexible during crisis"
- Relational understanding: "We'll work it out"

#### 2. **Relationships Are Asymmetrically Valuable**

**More valuable when**:
- High uncertainty (shock periods)
- Quality hard to contract (perishables)
- Flexibility needed (variable demand)

**Less valuable when**:
- Standardized products
- Spot markets efficient
- Complete contracts possible

#### 3. **Competition Can Undermine Relationships**

**Follow-up**: MM 2021 (Rwanda coffee)
- Increased competition → relationships break down
- Why? Reduces future rents
- Trade-off: Competition efficiency vs. relationship stability

#### 4. **Development Implications**

**For developing country supply chains**:
- Building relationships takes time
- Shocks can destroy relationships
- Policy: Protect supply chains during crises
- Infrastructure: Reduce vulnerability to shocks

## Connections

**Tests theory from**:
- [[📜bgm02_relational]] - Relational contracts and firm boundaries
- Levin (2003) - Relational incentive contracts
- Klein (1996) - Hold-up and vertical integration

**Extended by**:
- [[📜mm21_rwanda_coffee]] - Competition and relational contracts
- [[📜blouin19_default]] - Strategic default in coffee markets
- [[📜boudreau24_osh]] - External enforcement and relationships

**Related to**:
- M4: Why not integrate? (Relationships substitute)
- M1: Relational incentive contracts
- M6: Organizational capital (relationships as capital)

**Related courses**:
- [[14.282 Organizational Economics]] - M5: Governance of Non-Integration
- Development economics - Supply chain development
- International trade - Trade relationships

## Methodology Details

### Data Sources

**Transaction-level data**:
- **Kenyan Flower Council**: All exports (2007-2009)
  - Exporter, buyer, quantity, price, date
  - Quality indicators (stem length, color)
- **Customs records**: Shipment details
- **Surveys**: Exporter-buyer relationship characteristics

**Relationship measures**:
- **Length**: Years of trading
- **Intensity**: Share of buyer's purchases from exporter
- **Exclusivity**: Whether buyer sources from multiple exporters

### Identification Challenges

#### Challenge 1: **Endogenous relationships**
**Problem**: Good exporters → relationships
**Solution**: 
- Exporter × buyer fixed effects
- Within-pair variation over time
- Shock exogenous to relationship quality

#### Challenge 2: **Quality unobservable**
**Problem**: Relationship premium = quality premium?
**Solution**:
- Control for observable quality
- Use within-buyer variation (same buyer, different exporters)
- Placebo: Non-relationship premium in non-shock periods

#### Challenge 3: **Selection into survival**
**Problem**: Only good relationships survive?
**Solution**:
- Heckman selection correction
- Inverse probability weighting
- Results robust

### Empirical Strategy

**Baseline regression**:
$$\ln(\text{Price}_{ijt}) = \beta \cdot \text{Relationship}_{ij} \times \text{Shock}_t + \alpha_{ij} + \delta_t + X_{ijt}'\gamma + \epsilon_{ijt}$$

Where:
- $\alpha_{ij}$: Exporter-buyer fixed effects
- $\delta_t$: Time fixed effects  
- $X_{ijt}$: Quality controls, shipment characteristics

**Key coefficient**: $\beta$ (relationship premium during shock)

## Classic Examples

### Example 1: **Large UK Supermarket + Small Kenyan Exporter**

**Pre-shock**:
- 5-year relationship
- Exporter ships 50% to this buyer
- Premium: +12% above spot price

**During shock** (Feb 2008):
- Transport delayed 3 days
- Quality slight decline
- **Buyer**: Accepted shipment, paid premium (+10%)
- **Alternative**: Spot buyer would reject

**Post-shock**:
- Relationship strengthened
- Buyer increased orders
- Premium increased to +15%

### Example 2: **Spot Market Transaction**

**Pre-shock**:
- One-off transaction
- No relationship history
- Price: Market rate

**During shock**:
- Transport delayed 2 days
- Quality slight decline
- **Buyer**: Rejected shipment
- **Exporter**: Lost ~$5,000

**Post-shock**:
- No resumption of trade
- Exporter shifted to relationship buyers

## Discussion Notes

From [[14.282 Organizational Economics]]:

**Key Insight**: 
> Relationships are like **organizational capital**—valuable, hard to build, but can be destroyed by shocks.

**Design Questions**:
1. **How to build relationships?**
   - Time + consistent quality
   - Investment in communication
   - Shared risk (flexibility)

2. **When to invest in relationships vs. spot market?**
   - High uncertainty → relationships
   - Standardized products → spot
   - Perishables, quality variation → relationships

3. **Competition effects**:
   - Some competition good (discipline)
   - Too much competition → relationships unsustainable
   - Trade-off for policy

**Empirical Lessons**:
- Natural experiments valuable for studying relationships
- Transaction-level data > aggregate data
- Need exogenous shock to identify causal effects

## Questions for Further Research

1. **Relationship formation**: How do relationships start? What's the courtship phase?
2. **Multiple relationships**: Can exporters maintain many relationships? Optimal portfolio?
3. **Reputation**: Do third-party reputations substitute for relationships?
4. **Dynamics**: How do relationships evolve over time? Learning? Trust accumulation?
5. **Other industries**: Do findings generalize beyond flowers? (Yes—see MM 2021 Rwanda coffee)
6. **Policy**: How to protect relationships during crises? Infrastructure investment? Insurance?

## Policy Implications

### For Developing Countries
- **Infrastructure**: Reduce shock vulnerability (roads, power)
- **Market design**: Don't over-promote competition (can hurt relationships)
- **Trade policy**: Maintain supply chains during crises (e.g., COVID-19)

### For Firms
- **Invest in relationships**: High return, especially in uncertain environments
- **Relationship portfolio**: Diversify but maintain depth
- **Crisis management**: Prioritize key relationships during shocks

### For Supply Chain Management
- **Relational capital**: Treat as strategic asset
- **Supplier development**: Invest in long-term relationships
- **Flexibility**: Build slack into relationships for crisis response

---

*"The value of a relationship is revealed not in good times, but in bad times"* - Macchiavello & Morjaria (2015)
