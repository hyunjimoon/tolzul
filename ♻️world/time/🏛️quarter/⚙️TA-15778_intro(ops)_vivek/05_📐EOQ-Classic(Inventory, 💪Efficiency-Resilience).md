# Lecture 5: Inventory Control 1 - Fundamentals and Models

**Date:** July 28  
**Duration:** 1.5 hours  
**Instructor:** Prof. Vivek Farias

communicate with [[coTA-adam_jozefiak]]




---
tldr
- **Pros and Cons:** The primary pros of carrying inventory are ensuring customer access, hedging against supply risk, and achieving economies of scale, while the cons include significant financing costs, the risk of obsolescence, and expenses from storage and shrinkage.
- **CCC's Main Message:** The Cash Conversion Cycle is a critical indicator of a company's financial performance that directly impacts its stock price, not just a minor operational metric.
- **Amazon's Mention:** Amazon was mentioned as an extreme case because it claims a negative Cash Conversion Cycle by collecting payment from customers before paying suppliers, illustrating ultimate operational efficiency.
- 
---

- science of coordinating goals and capabilites to offer your customer a compelling offering
- nonlinearity of utilization and variability, MD+RN (taking lots of time from spread; no consistency) , efficacious system in country (per capita; MGH vs intermoutain; 1/5 - readmission is better for interMT)


🚨todo1 from [[prep(recitation)]] 
- financing cost (lending machines to produce), buy inventory hedge you 
- supply risk 
- auto industry hit from supply stuff from electronics
- economics of scale, shrinkage, increase 

contrarian deliberate scarcity are good; 💎i'm rich


•⁠  ⁠total assets=current assets (cash, cash equivalents, receivables, inventory, prepaid assets, total non-current assets) 
•⁠  ⁠total liabilities net minority
•⁠  ⁠total equity gross minority
total capitalization

L and lambda, inventory turnover time = inventory value (balance sheet) / cogs (earnings or P&L)

WMT = 56435 (L)/514625 (lambda) = 5.75 weeks
TGT = 12740 (L)/76159 (lambda) = 8.68 weeks

cost scale with time

why this matters? wait time macrofinance (cash conversion cycle CCC - start with dollars back plus margine; higher returns on underlying stock; zero-investment portfolio that buys the lowest); 

- first order mover (stock prices)
- 🙋‍♀️ppl pay merchant business (amazon example)

instant pod, fisher sandal, aldo shoes

margin structure + how confident are we on this forecast (variability)

median was 35k before knowing the margina structure and normal variation

portfolio management expected profit maximizing 
- risk
marginal cost = marginal revenue

as the tree increase, the probability of selling tree lowers

----


## Learning Objectives
- Understand the fundamental role of inventory in operations
- Learn basic inventory models and optimization techniques
- Analyze trade-offs between holding costs and stockout costs
- Apply Economic Order Quantity (EOQ) and newsvendor models

## Key Concepts

### Why Hold Inventory?
1. **Demand-Supply Mismatch:** Bridge timing differences
2. **Uncertainty Management:** Buffer against demand/supply variability  
3. **Economies of Scale:** Batch production and purchasing
4. **Service Level:** Maintain product availability
5. **Speculation:** Take advantage of price fluctuations

### Types of Inventory
- **Raw Materials:** Inputs to production process
- **Work-in-Process (WIP):** Partially completed products
- **Finished Goods:** Completed products ready for sale
- **Safety Stock:** Buffer against uncertainty
- **Cycle Stock:** Normal inventory for operations

### Inventory Costs
1. **Holding Costs (h):**
   - Capital cost (opportunity cost of money)
   - Storage costs (warehouse, handling)
   - Obsolescence and deterioration
   - Insurance and taxes
   - Typical range: 20-30% of item value annually

2. **Ordering Costs (K):**
   - Administrative costs of placing orders
   - Setup costs for production runs
   - Transportation costs
   - Fixed costs independent of order size

3. **Shortage Costs:**
   - Lost sales and profits
   - Customer dissatisfaction
   - Expediting costs
   - Stockout penalties

## Fundamental Inventory Models

### Economic Order Quantity (EOQ)
**Assumptions:**
- Deterministic demand (D units per time period)
- Constant lead time
- No stockouts allowed
- Fixed ordering cost (K) and holding cost (h)

**Model:**
- **Total Cost:** TC = (D/Q)K + (Q/2)h
- **Optimal Order Quantity:** Q* = √(2DK/h)
- **Optimal Total Cost:** TC* = √(2DKh)
- **Reorder Point:** R = dL (demand rate × lead time)

**Key Insights:**
- Order quantity independent of demand rate
- Square root relationship (doubling demand increases Q* by √2)
- Balance between ordering and holding costs

### EOQ Extensions
1. **Quantity Discounts:** Price breaks for larger orders
2. **Finite Production Rate:** Production while consuming
3. **Planned Shortages:** Allowing backorders when economical
4. **Multi-item Constraints:** Resource limitations

### Newsvendor Model (Single-Period)
**Setting:** One-time ordering decision for perishable/seasonal product

**Parameters:**
- **Demand (D):** Random variable with known distribution
- **Unit Cost (c):** Purchase/production cost
- **Selling Price (p):** Revenue per unit sold
- **Salvage Value (s):** Recovery value for unsold units

**Cost Structure:**
- **Overage Cost (Co):** c - s (cost of ordering too much)
- **Underage Cost (Cu):** p - c (cost of ordering too little)

**Optimal Solution:**
- **Critical Ratio:** CR = Cu/(Cu + Co) = (p-c)/(p-s)
- **Optimal Quantity:** Q* such that F(Q*) = CR
- Where F(Q) is cumulative distribution function of demand

## Service Level Concepts

### Type I Service Level (Fill Rate)
- Probability of not stocking out during lead time
- **Formula:** P(Demand ≤ Safety Stock + Expected Demand)

### Type II Service Level (Fill Rate)
- Fraction of demand satisfied from stock
- More relevant for operational performance

### Safety Stock Calculation
- **Safety Stock:** ss = z × σL
- Where z is safety factor for desired service level
- σL is standard deviation of demand during lead time

## Inventory Performance Metrics

### Inventory Turnover
- **Formula:** Turnover = COGS / Average Inventory
- **Interpretation:** How many times inventory is sold per year
- Higher turnover generally indicates better performance

### Days of Supply
- **Formula:** DOS = Average Inventory / Daily Demand
- **Interpretation:** How many days current inventory will last
- Lower DOS indicates more efficient inventory management

### Fill Rate
- **Formula:** Fill Rate = Units Satisfied / Units Demanded
- Measures customer service level

## Strategic Inventory Considerations

### ABC Analysis
- **Category A:** High-value items (tight control)
- **Category B:** Medium-value items (moderate control)  
- **Category C:** Low-value items (simple control)
- Based on Pareto principle (80/20 rule)

### Push vs. Pull Systems
- **Push:** Production based on forecasts
- **Pull:** Production triggered by actual demand
- **Hybrid:** Combination strategies

### Centralization vs. Decentralization
- **Benefits of Centralization:**
  - Risk pooling effects
  - Economies of scale
  - Better demand visibility
- **Benefits of Decentralization:**
  - Faster response time
  - Lower transportation costs
  - Local market responsiveness

## Discussion Questions for Class

1. **Inventory Trade-offs:** What are the fundamental trade-offs in inventory management? How do these vary by industry?

2. **EOQ Applications:** When is the EOQ model most applicable? What happens when assumptions are violated?

3. **Newsvendor Insights:** How does demand uncertainty affect optimal ordering policies? What role does the profit margin play?

4. **Service Levels:** How should companies set service level targets? What factors influence this decision?

## Real-World Applications

### Retail Industry
- Seasonal products (newsvendor model)
- Fast fashion (short life cycles)
- Perishable goods (time constraints)

### Manufacturing
- Component inventory (multiple items)
- Production planning (batch sizes)
- Supply chain coordination

### Healthcare
- Drug inventory (expiration dates)
- Emergency supplies (high shortage costs)
- Equipment maintenance parts

## Key Takeaways
- **Economic Principle:** Inventory decisions involve balancing competing costs
- **Model Selection:** Different models apply to different operational contexts
- **Uncertainty Impact:** Demand variability significantly affects optimal policies
- **Service Trade-offs:** Higher service levels require more inventory investment

## Preparation for Next Class
- Read [[Lec6_Zara__Staying_Fast_and_Fresh]]
- Consider how Zara's business model addresses inventory challenges
- Think about fashion industry characteristics and inventory implications

## Recitation Support
- **Next Session:** July 29 - Inventory concepts and Yedioth case preparation
- **Focus:** Quantitative inventory models and calculations
- **Office Hours:** Available for individual and team questions

## Teaching Notes
- Start with intuitive explanation before mathematical models
- Use concrete examples to illustrate concepts
- Emphasize the strategic importance of inventory decisions
- Connect models to real-world applications
- Prepare students for more complex scenarios in upcoming cases
