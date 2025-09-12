# Lecture 8: Yedioth Group Case - Newsvendor Model and Risk Pooling

**Date:** August 1  
**Duration:** 1.5 hours  
**Instructor:** Prof. Vivek Farias  
**Assignment:** GRADED CASE WRITE-UP DUE AT 8:30 AM (TEAM)

---
## manual notes
holding cost and inventory + fixed order cost

DCFH: demand rate (units per time), cost, f, h (olding cost)

q* = sqrt(2DF/CH)
 sqrt(2 D 20k, F 500/C 45, H .45)

changes the timing we place the order 

dollars, variability
place order five days in advance (R)

hate runout and hate inventory

u/u+o in this situtation (not being able to serve vs) ; target service level (95%), chance that i run out to be no larger than 5%

uncertainty in lead time (thogut 5 days)

⭐️joe's question: one can update q after the first triangle compared with online learning of D, but changing q can complicate policy making its use fragile

 ddlt is random variable, 
inventory rule: order Q whenever inventory reaches R

![[08_📰Yedioth-Unique(Inventory, 💪Efficiency-Resilience) 2025-08-01-8.svg]]
%%[[08_📰Yedioth-Unique(Inventory, 💪Efficiency-Resilience) 2025-08-01-8|🖋 Edit in Excalidraw]]%%
---

## Learning Objectives
- Apply newsvendor model to real-world distribution problem
- Quantify benefits of risk pooling in multi-location systems
- Analyze different pooling strategies and their implementation challenges
- Develop practical recommendations for organizational change

## Case Studies
- **Primary Case:** [[Assignment_Yedioth_Case.pdf]]

## Case Background

### Yedioth Group Overview
- **Business:** Major Israeli newspaper and magazine publisher
- **Product:** Weekly magazines with uncertain demand
- **Distribution:** Network of 50 retailers across Israel
- **Current System:** Independent supply to each retailer
- **Challenge:** High returns due to overproduction and demand uncertainty

### Current Distribution Model
- **Independent Supply:** Each retailer supplied separately
- **Forecast-Based:** Orders based on demand predictions
- **No Pooling:** Cannot transfer inventory between retailers
- **High Returns:** Significant unsold inventory returned to publisher
- **Service Target:** 99% customer service level required

### Sales Agent Structure
- **Regional Organization:** Sales agents cover geographic territories
- **Multiple Retailers:** Each agent visits several retailers
- **Weekly Schedule:** Mid-week visits to each retailer
- **Information Flow:** Agents observe demand patterns

## Key Concepts for Analysis

### Newsvendor Model Application
- **Single-Period Problem:** Weekly magazine with no carryover value
- **Uncertain Demand:** Stochastic demand at each retailer
- **Service Level Constraint:** 99% probability of meeting demand
- **Cost Structure:** 
  - Purchase cost (c)
  - Selling price (p)  
  - Return/disposal cost (salvage value s)

### Risk Pooling Scenarios
1. **Status Quo:** Independent supply to 50 retailers
2. **Full Pooling:** Complete inventory sharing across all retailers
3. **Agent-Level Pooling:** Pooling within each agent's territory
4. **Practical Alternatives:** Feasible mid-week redistribution policies

## Graded Assignment Questions

### Question 1: Current System Analysis
**Prompt:** In the current distribution model, where each retailer is supplied once, independently of all other retailers. What would be a good method to compute the quantity shipped to each retailer if one wishes to guarantee that 99% of customers will be served? Apply your approach to compute recommended quantities to the 50 retailers.

**Analysis Framework:**
- **Newsvendor Formula:** Q* such that F(Q*) = 0.99
- **Individual Optimization:** Calculate for each retailer separately
- **Service Level:** 99% probability of no stockout
- **Implementation:** Apply to all 50 retailers using demand distributions

**Methodology:**
1. Identify demand distribution for each retailer
2. Calculate 99th percentile of demand distribution
3. Determine optimal order quantity for each location
4. Provide results in appendix with clear explanation

### Question 2: Full Pooling Benefits
**Prompt:** If Yedioth could implement full pooling among all of the 50 retailers what would be the estimated benefit in terms of total production levels and returns (assume that the required service level is 99%)?

**Analysis Framework:**
- **Aggregate Demand:** Sum demands across all 50 retailers
- **Variance Reduction:** σ²_total = Σσ²_i + 2ΣΣcov(i,j)
- **Optimal Aggregate Quantity:** Based on total demand distribution
- **Comparison:** Total production with vs. without pooling

**Expected Benefits:**
- **Production Reduction:** Lower total quantity needed
- **Return Reduction:** Less overproduction
- **Service Maintenance:** Same 99% service level
- **Quantification:** Calculate percentage improvements

### Question 3: Agent-Level Pooling
**Prompt:** Suppose that one could implement full pooling only among retailers that are treated by the same sales agent, what would be the potential benefit in terms of production levels and returns (assume 99% service level). Compare to Question 2.

**Analysis Framework:**
- **Partial Pooling:** Group retailers by sales agent
- **Agent-Level Optimization:** Pool within groups, not between groups
- **Benefit Calculation:** Compare to both status quo and full pooling
- **Trade-off Analysis:** Feasibility vs. benefit magnitude

**Implementation:**
1. Identify retailer groups by sales agent
2. Calculate pooled demand for each group
3. Optimize quantities at group level
4. Compare total benefits to full pooling scenario

### Question 4: Practical Pooling Policies
**Prompt:** Propose more realistic policies that leverage the fact that the sales agent visits each retailer in the middle of the week. What would the benefit be of these policies?

**Strategic Considerations:**
- **Mid-Week Information:** Sales agents observe demand patterns
- **Redistribution Opportunity:** Move inventory between retailers
- **Implementation Constraints:** Transportation costs, timing limitations
- **Organizational Feasibility:** Agent capabilities and incentives

**Potential Policies:**
1. **Mid-Week Rebalancing:** Redistribute based on observed sales
2. **Dynamic Allocation:** Agents make reallocation decisions
3. **Emergency Pooling:** Share inventory only for stockouts
4. **Hub-and-Spoke:** Central depot for agent territories

### Question 5: Organizational Challenges
**Prompt:** What do you think are the organizational challenges that Assaf will have to address?

**Challenge Categories:**
- **Sales Agent Incentives:** Motivation to share vs. hoard inventory
- **Performance Measurement:** How to evaluate agent performance
- **Information Systems:** Data sharing and coordination mechanisms
- **Transportation Logistics:** Cost and complexity of redistribution
- **Retailer Relationships:** Managing conflicts over allocation

## Quantitative Analysis Framework

### Statistical Modeling
- **Demand Distributions:** Normal, Poisson, or empirical distributions
- **Correlation Analysis:** Demand relationships between retailers
- **Pooling Benefits:** √n rule approximation
- **Service Level Calculations:** Probability constraints

### Financial Analysis
- **Cost Components:**
  - Production costs
  - Return/disposal costs
  - Transportation costs
  - Administrative costs

- **Benefit Quantification:**
  - Production reduction
  - Return reduction
  - Service level maintenance
  - Implementation costs

### Sensitivity Analysis
- **Service Level Variations:** Impact of different targets
- **Correlation Assumptions:** Effect on pooling benefits
- **Cost Parameter Changes:** Sensitivity to cost assumptions
- **Demand Uncertainty:** Impact of forecast accuracy

## Strategic Implementation Considerations

### Technology Requirements
- **Information Systems:** Real-time inventory tracking
- **Communication Tools:** Agent-retailer coordination
- **Decision Support:** Optimization algorithms
- **Performance Monitoring:** KPI tracking systems

### Process Changes
- **Agent Training:** New responsibilities and procedures
- **Retailer Coordination:** Collaborative planning processes
- **Transportation Planning:** Redistribution logistics
- **Performance Management:** New metrics and incentives

### Change Management
- **Stakeholder Buy-in:** Agent and retailer acceptance
- **Pilot Testing:** Gradual implementation approach
- **Training Programs:** Skill development requirements
- **Success Metrics:** Clear performance indicators

## Key Takeaways
- **Strategic Message:** Demonstrates the classic "newsvendor" problem; highlights the significant inventory and cost benefits of risk pooling to better match uncertain demand with supply.

- **Quantitative Impact:** Risk pooling can provide substantial benefits even with partial implementation.

- **Implementation Reality:** Organizational and logistical constraints limit theoretical benefits.

- **Strategic Design:** Distribution systems should be designed to enable pooling opportunities.

## Assignment Submission Guidelines
- **Team Work:** Study groups of max 5 students
- **Due Date:** August 1 at 8:30 AM
- **Length:** Less than 4 pages (excluding appendices)
- **Format:** 12-point font minimum
- **Calculations:** Clear methodology explanations and detailed appendices

## Preparation for Next Class
- Review network design concepts
- Consider centralization vs. decentralization trade-offs
- Prepare for Amazon European distribution strategy discussion

## Recitation Support
- **Focus:** Yedioth debrief and Littlefield simulation introduction
- **Quantitative Review:** Newsvendor calculations and pooling benefits
- **Next Steps:** Simulation game strategy development

## Teaching Notes
- Emphasize practical application of newsvendor model
- Connect theoretical pooling benefits to implementation challenges
- Guide students through statistical calculations
- Highlight organizational change management aspects
- Prepare for transition to supply chain network design topics
