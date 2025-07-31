# Lecture 7: Inventory Control 2 - Advanced Topics and Risk Pooling

**Date:** July 31  
**Duration:** 1.5 hours  
**Instructor:** Prof. Vivek Farias

---
## manual notes
not loosing customer but item, but moving onto next item

- underage cost is not $60, as customer profile is 
- 1 product match with each customer (different size)

same thing in the positive direction ()

compelling assortment so you'll buy another, if you don't see compelling one, 

👗60$ multiplied by probability of you won't buy anything from me (due to repeated visit and assortment)

virtuous cycle: rapid rotation, 

⭐️formula modularize thoughts

portfolio existis in particular point of time, 

long term value thinking (opportunity to calibrate numbers)

🔄rapid rotation -(reason to revisit)-> revisits  -(lower u, lower safety stock)-> understock   -()->

being exposed to supply risk is esp. bad fast turning business models
질문할때 짧고 핵심을.

I HAVE QUESTION AND OBSERVATION.

long term customer behavior (substitue over time), tractically important



---

## Learning Objectives
- Master advanced inventory models under uncertainty
- Understand risk pooling concepts and benefits
- Analyze multi-location inventory systems
- Apply service level optimization techniques

## Key Concepts

### Stochastic Inventory Models
- **Demand Uncertainty:** Random variables and distributions
- **Lead Time Variability:** Supply uncertainty effects
- **Service Level Constraints:** Probability-based targets
- **Safety Stock Optimization:** Balancing cost and service

### (R,Q) Inventory Policy
- **Reorder Point (R):** Inventory level triggering new order
- **Order Quantity (Q):** Fixed amount ordered each time
- **Policy Logic:** Order Q units when inventory hits R
- **Continuous Review:** Monitor inventory continuously

### (R,Q) Model Parameters
**Reorder Point Calculation:**
- R = μL + zα × σL
- Where:
  - μL = Expected demand during lead time
  - σL = Standard deviation of demand during lead time
  - zα = Safety factor for service level α

**Order Quantity:**
- Use EOQ formula: Q* = √(2DK/h)
- Or modified EOQ for uncertain demand

**Safety Stock:**
- SS = zα × σL
- Higher service levels require more safety stock
- Cost increases exponentially with service level

### Service Level Types Revisited

#### Type I Service Level (Cycle Service Level)
- **Definition:** Probability of not stocking out during lead time
- **Formula:** P(DL ≤ R) = α
- **Application:** Appropriate when stockout cost is very high
- **Calculation:** R = F^(-1)(α) where F is CDF of lead time demand

#### Type II Service Level (Fill Rate)
- **Definition:** Fraction of demand satisfied from stock
- **Formula:** β = 1 - E[Shortage]/Q
- **Application:** More relevant for ongoing operations
- **Calculation:** More complex, involves expected shortage function

## Risk Pooling Fundamentals

### Definition and Concept
- **Risk Pooling:** Combining uncertain demands to reduce total variability
- **Mathematical Basis:** Variance of sum < Sum of variances (when demands not perfectly correlated)
- **Central Limit Theorem:** Aggregated demand becomes more predictable

### Types of Risk Pooling

#### Location Pooling
- **Centralization:** Consolidate inventory at fewer locations
- **Benefit:** √n reduction in safety stock (for n identical locations)
- **Trade-off:** Response time vs. inventory cost

#### Product Pooling
- **Generic Products:** Design for late customization
- **Common Components:** Share parts across products
- **Postponement:** Delay differentiation until demand known

#### Time Pooling
- **Shorter Review Periods:** More frequent ordering
- **Cross-docking:** Reduce storage time
- **Just-in-Time:** Minimize time in system

#### Supplier Pooling
- **Multiple Sources:** Reduce supply risk
- **Flexible Contracts:** Option to source from different suppliers
- **Supply Diversification:** Geographic and capacity spreading

### Quantitative Risk Pooling Analysis

#### Single Location Model
- **Demand:** D ~ N(μ, σ²)
- **Safety Stock:** SS = zα × σ
- **Total Inventory:** μ + zα × σ

#### Pooled Model (n identical locations)
- **Aggregate Demand:** nD ~ N(nμ, nσ²)
- **Aggregate Std Dev:** √n × σ
- **Safety Stock:** SS_pooled = zα × √n × σ
- **Reduction Factor:** √n (significant for large n)

#### Correlation Effects
- **Perfect Correlation (ρ = 1):** No pooling benefit
- **Zero Correlation (ρ = 0):** Maximum pooling benefit
- **Negative Correlation (ρ < 0):** Even greater benefits
- **Real World:** Usually positive but less than perfect correlation

### Advanced Inventory Topics

#### Multi-Echelon Systems
- **Supply Chain Structure:** Multiple levels of inventory
- **Coordination:** Upstream-downstream interactions
- **Bullwhip Effect:** Demand amplification up supply chain
- **Information Sharing:** Reduce distortion through transparency

#### Substitution and Commonality
- **Product Substitution:** Use similar products when stockout
- **Component Commonality:** Share parts across products
- **Design Strategy:** Build flexibility into product architecture
- **Inventory Benefits:** Reduce total safety stock requirements

#### Capacity Constraints
- **Storage Limitations:** Physical or financial constraints
- **Optimal Allocation:** Distribute limited capacity across items
- **Lagrange Multipliers:** Mathematical optimization approach
- **ABC Analysis:** Focus resources on high-value items

## Performance Measurement

### Inventory Metrics
- **Inventory Turnover:** COGS / Average Inventory
- **Days Sales Outstanding:** Average Inventory / Daily Sales
- **Fill Rate:** Orders Filled Complete / Total Orders
- **Service Level:** Various measures of stockout avoidance

### Cost Analysis
- **Total Inventory Cost:** Ordering + Holding + Shortage costs
- **Trade-off Optimization:** Balance competing objectives
- **Sensitivity Analysis:** How parameters affect optimal policies
- **What-if Scenarios:** Compare alternative strategies

## Strategic Inventory Decisions

### Centralization vs. Decentralization
**Centralization Benefits:**
- Risk pooling advantages
- Economies of scale in purchasing
- Better demand visibility
- Reduced total safety stock

**Decentralization Benefits:**
- Faster response time
- Lower transportation costs
- Local market responsiveness
- Reduced complexity

**Hybrid Approaches:**
- Regional distribution centers
- Cross-docking facilities
- Virtual centralization through information sharing

### Postponement Strategies
- **Manufacturing Postponement:** Delay final assembly
- **Logistics Postponement:** Delay shipment until orders received
- **Product Postponement:** Design for late customization
- **Time Postponement:** Delay commitment decisions

## Discussion Questions for Class

1. **Risk Pooling Applications:** In what situations is risk pooling most beneficial? When might it not work well?

2. **Centralization Trade-offs:** How should a company decide between centralized vs. decentralized inventory?

3. **Service Level Setting:** How should service level targets be set? Should they be the same for all products?

4. **Technology Impact:** How do modern information systems change inventory management strategies?

## Real-World Applications

### E-commerce
- **Amazon:** Risk pooling through fulfillment centers
- **Drop-shipping:** Virtual inventory pooling
- **Prime delivery:** Service level differentiation

### Automotive Industry
- **Component commonality:** Share parts across models
- **Dealer networks:** Multi-echelon inventory
- **Just-in-time:** Minimize inventory investment

### Healthcare
- **Blood banks:** Perishable inventory pooling
- **Hospital networks:** Equipment sharing
- **Pharmaceutical distribution:** Service level requirements

## Key Takeaways
- **Risk Pooling Power:** Combining uncertain demands can dramatically reduce inventory requirements
- **Strategic Design:** Inventory systems should be designed to enable pooling benefits
- **Service Trade-offs:** Higher service levels come at increasing inventory costs
- **System Thinking:** Inventory decisions affect entire supply chain performance

## Preparation for Next Class
- Read [[Assignment_Yedioth_Case]]
- **Focus:** Newsvendor model application and risk pooling analysis
- **Graded Assignment:** Team case write-up due August 1
- Review quantitative techniques for pooling calculations

## Teaching Notes
- Build on inventory fundamentals from previous lecture
- Use mathematical examples to demonstrate pooling benefits
- Connect theoretical concepts to Zara case insights
- Prepare students for quantitative analysis in Yedioth case
- Emphasize strategic implications of inventory design decisions
