# Lecture 13: Choice Modeling and Customer Centricity

**Date:** August 11  
**Duration:** 2.5 hours (2:30 PM - 4:00 PM Cohort A / 8:30 AM - 10:00 AM Cohort B)  
**Instructor:** Prof. Vivek Farias  
**Assignment:** VENTURE PITCH DUE (TEAM)

---
# manual note
guide inventory so that we sell out in the last week

---
if i had a crystal ball of demand, i could have (95%)

derek: could have run the last four weeks slower

optimization: principled discussion on objective and constraints
mike: 
- re-optimize at week 5, 10 (hit solver three times)
- two benefit of re-optimize (data source)
	- historical data from w1~5 (allows me to build better demand model)
	- actual inventory (unpredictable variability; i might have sold; account for natural variation)
	- hold on to that 80% longer
	- stick with 80% one week more (as demand is healthier)

🗣️ i'm beginning to think multiple period condition of 

updating demand model rather than using the original regression

redo the w5 solver, how does this change
- pricing at $80 (x_80, x_90 would disapper as we ); i
- x_80 + x_60 <=11 (week count), data from the first five weeks to update the 84, 111, 180
- you expected to solve 90, but you sold 95 - adjust 
- ![[12_🥗BlueApron-Lifecycle(Demand, 🎯Focus-Scale) 2025-08-11-8.svg]]
%%[[12_🥗BlueApron-Lifecycle(Demand, 🎯Focus-Scale) 2025-08-11-8.md|🖋 Edit in Excalidraw]]%%

using [llm](https://poe.com/s/YWZWU1fDoRUwDMuxoMG0), d is the output of updated demand prediction model which becomes coefficient that included in both objective (revenue =  price * count) and count constraint

|**Aspect**|**No Re-optimization**|**Re-optimization**|
|---|---|---|
|**Objective Function**|Fixed coefficients for revenue:|Coefficients updated based on observed sales data:|
||`Maximize: 100(64x₁₀₀) + 90(84x₉₀) + 80(111x₈₀) + 60(180x₆₀)`|`Maximize: 100(d₁₀₀x₁₀₀) + 90(d₉₀x₉₀) + 80(d₈₀x₈₀) + 60(d₆₀x₆₀)`|
||where `d₁₀₀ = 64`, `d₉₀ = 84`, etc.|where `d₁₀₀`, `d₉₀`, etc., are updated demand rates based on observed data.|
|**Time Constraint**|Static: `x₁₀₀ + x₉₀ + x₈₀ + x₆₀ ≤ 16`|Adjusted: Remaining weeks only: `x₈₀ + x₆₀ ≤ T_remaining`|
|**Inventory Constraint**|Static: `64x₁₀₀ + 84x₉₀ + 111x₈₀ + 180x₆₀ ≤ 2000`|Dynamic: Real-time inventory update: `d₁₀₀x₁₀₀ + d₉₀x₉₀ + d₈₀x₈₀ + d₆₀x₆₀ ≤ Inventory_remaining`|
|**Demand (Coefficients)**|Fixed: Assumes constant demand rates over time.|Dynamic: Updates demand coefficients (`d₁₀₀`, `d₉₀`, etc.) based on observed weekly sales.|
|**Solver Execution**|Single run at the start of the 16-week period.|Re-run periodically (e.g., every 5 weeks) using updated coefficients and constraints.|

---

### **Steps for Re-optimization in Gurobi**

1. **Initial Optimization (Week 0):**
    
    - Define the model with:
        - Objective: `Maximize: 100(64x₁₀₀) + 90(84x₉₀) + 80(111x₈₀) + 60(180x₆₀)`
        - Constraints:
            - Time: `x₁₀₀ + x₉₀ + x₈₀ + x₆₀ ≤ 16`
            - Inventory: `64x₁₀₀ + 84x₉₀ + 111x₈₀ + 180x₆₀ ≤ 2000`
2. **Observe Weekly Sales:**
    
    - After each week (or batch of weeks), collect:
        - **Units Sold**: Actual sales data for each

----

diff in diff design ()

profit logic (scott frank; sold oracle and first; partner in bain)

training customer to devalue your brand

owned ; overpriced jacket (patch); super short season - discount (brand losing its shine); tradeoff = short vs long run; 

even for bablan goods, we have sensitivity to price

if it's inventory issue, why don't we diminish inventor risk in the first place?? that more tightly (diminishing inventory risk); reason of pricing is 

price -> portfolio as a lever?

assortment
pool, customer experience more options (capture more market share)

reinforce zara's buy now 
(-) more cannibalization - eating away from each other (high correlation) -
SKU bloat

lots of choices is not good

[sheena iyengar](https://business.columbia.edu/faculty/people/sheena-iyengar); blind made her introspection - w1 (20 jams), w2 (4 jams) - cognitive overload (paradox of choice)
- expecting to get more market and at some point it's crap (just explanation)
- easier to add a product then subtracting a product

⭐️capture market, pooling from substitution, complementary drive cross shopping vs sku bloat and cann
managing product (entire discussion was on price (shirt, ?)) to managing pr

michael: TO SANDRA's point, 

⭐️portfolio is complicated as we have mix of substitution, cannibalation, pooling
this complexity on different effects lead to focus on one person profile
manage lifetime value

CAC: netflix's price to get customer (20yrs ago) was $100
how long she sticks around and how valuable she is  (retention drives how long she sticks around)

how did amazon figure out to (easy to use, broadest product assortments, fast and free shipping, great prices) via customer centricity logic?

⭐️amazon was focused on gathering data on affluent educated shoppers - price close to cost (understand what makes this folks tick)
get constant feedback

leaky bucket (filling in a bucket that's leaking)

CLV  to CAC ratio high loyalty 

⭐️hello fresh did (distinct needs) blue apron


----

## Learning Objectives
- Understand customer choice modeling and its operational implications
- Analyze subscription business models and unit economics
- Apply Customer Lifetime Value (CLV) analysis to operational decisions
- Evaluate product assortment optimization strategies

## Case Studies
- **Primary Cases:**
  - [[Lec13_Which_Products_Should_You_Stock_.pdf]]
  - [[Lec13_Blue_Apron__Turning_Around_the_Struggling_Meal_Kit_Market_Leader.pdf]]

## Required Readings
- **[SaaS Metrics 2.0: A Guide to Measuring and Improving What Matters](https://www.forentrepreneurs.com/saas-metrics-2/)**

### SaaS Metrics Article Key Insights:

**Core SaaS Principles:**
1. **Customer Acquisition:** Getting new customers
2. **Customer Retention:** Keeping customers engaged and subscribed
3. **Customer Monetization:** Increasing revenue per customer over time

**Critical Metrics:**
- **Customer Lifetime Value (LTV):** Total revenue from a customer over their entire relationship
- **Customer Acquisition Cost (CAC):** Total cost to acquire a new customer
- **LTV:CAC Ratio:** Should be >3:1 for healthy SaaS businesses
- **Months to Recover CAC:** Should be <12 months, ideally 5-7 months
- **Churn Rate:** Monthly customer/revenue loss rate
- **Net Negative Churn:** When expansion revenue exceeds churn losses

**Unit Economics Framework:**
Can you make more profit from customers than it costs to acquire them? This fundamental question drives all operational decisions in subscription businesses.

## Key Concepts

### Customer Choice Modeling
- **Discrete Choice Theory:** How customers select among alternatives
- **Utility Functions:** Mathematical representation of customer preferences
- **Price Sensitivity:** Elasticity of demand to price changes
- **Substitution Patterns:** How customers switch between products

### Product Assortment Optimization
- **Attribute-Based Approach:** Focus on product characteristics customers value
- **Sales Data Limitations:** Past performance doesn't predict future preferences
- **Cannibalization Effects:** How new products affect existing sales
- **Variety vs. Complexity:** Trade-off between choice and operational efficiency

### Subscription Business Models
- **Recurring Revenue:** Predictable income streams
- **Customer Lifetime Value:** Total revenue over customer relationship
- **Retention Focus:** Keeping customers is cheaper than acquiring new ones
- **Expansion Revenue:** Upselling and cross-selling to existing customers

## Blue Apron Case Analysis

### Business Model Overview
- **Meal Kit Delivery:** Pre-portioned ingredients with recipes
- **Subscription Model:** Weekly recurring deliveries
- **Customer Acquisition:** High marketing spend to acquire subscribers
- **Operational Challenges:** Complex supply chain and logistics

### Unit Economics Challenges
**High Customer Acquisition Costs:**
- **CAC Problem:** Very expensive to acquire customers through marketing
- **LTV Challenge:** Low customer lifetime value due to high churn
- **Unit Economics:** CAC often exceeded LTV, making business unsustainable

**Churn Issues:**
- **Novelty Factor:** Initial excitement wears off quickly
- **Convenience vs. Cost:** Customers find alternatives more convenient/cheaper
- **Product-Market Fit:** Unclear if there's sustainable long-term demand

### Operational Implications
**Supply Chain Complexity:**
- **Fresh Ingredients:** Short shelf life requires precise demand forecasting
- **Portion Control:** Exact quantities needed for each meal
- **Logistics:** Cold chain distribution with tight delivery windows
- **Waste Management:** High perishability leads to significant waste

**Customer Experience:**
- **Meal Variety:** Need to continuously innovate recipes
- **Dietary Preferences:** Customization adds operational complexity
- **Delivery Reliability:** Service quality affects retention

### Strategic Questions
1. **Unit Economics:** How can Blue Apron improve its LTV:CAC ratio?
2. **Retention Strategy:** What operational changes could reduce churn?
3. **Market Position:** Is the business model fundamentally viable?
4. **Competitive Advantage:** What sustainable differentiators exist?

## Product Assortment Case Analysis

### Traditional Approach Problems
- **Sales-Based Decisions:** Drop products with low sales volume
- **Ignores Customer Preferences:** Doesn't consider why products succeed/fail
- **Limited Innovation:** Conservative approach to new products
- **Competitive Vulnerability:** Predictable assortment decisions

### Attribute-Based Optimization
**Customer Preference Modeling:**
- **Conjoint Analysis:** Understand relative importance of product attributes
- **Choice Experiments:** Test customer preferences under controlled conditions
- **Market Research:** Direct feedback on desired product characteristics
- **Behavioral Data:** Actual purchase patterns and sequences

**Operational Benefits:**
- **Better Forecasting:** Predict demand for new products based on attributes
- **Strategic Assortment:** Design product mix to maximize customer satisfaction
- **Reduced Risk:** Data-driven decisions rather than intuition
- **Competitive Advantage:** Unique assortments competitors can't easily copy

## Customer Lifetime Value Analysis

### CLV Calculation Framework
**Basic Formula:**
- CLV = (Average Revenue per Customer) × (Gross Margin %) × (Customer Lifespan)

**Advanced DCF Approach:**
- Account for time value of money
- Include acquisition and retention costs
- Consider expansion revenue potential
- Factor in churn probability over time

### Operational Decision Making
**Investment Justification:**
- **Customer Service:** How much to invest in retention?
- **Product Development:** Which features drive long-term value?
- **Acquisition Channels:** Which sources provide highest-value customers?
- **Pricing Strategy:** How to maximize long-term customer value?

**Segmentation Strategy:**
- **High-Value Customers:** Provide premium service and retention focus
- **Growth Customers:** Invest in expansion and upselling
- **At-Risk Customers:** Targeted retention campaigns
- **Low-Value Customers:** Cost-efficient service models

## Choice Modeling Applications

### Revenue Management Extensions
- **Dynamic Pricing:** Adjust prices based on demand elasticity
- **Product Bundling:** Combine products to increase customer value
- **Personalization:** Customize offerings to individual preferences
- **Capacity Allocation:** Optimize inventory mix for customer choice

### Supply Chain Implications
- **Demand Forecasting:** Better predictions based on customer preferences
- **Inventory Planning:** Stock levels aligned with choice patterns
- **Product Lifecycle:** Understand when to introduce/discontinue products
- **Supplier Relationships:** Align sourcing with customer-driven demand

## Discussion Questions for Class

### Blue Apron Analysis
1. **Unit Economics:** What are the key drivers of Blue Apron's customer acquisition cost and lifetime value? How can they be improved?

2. **Operational Strategy:** What operational changes could Blue Apron make to improve customer retention and reduce churn?

3. **Business Model Viability:** Is the meal kit subscription model fundamentally sound, or are there structural issues that make it unsustainable?

4. **Competitive Positioning:** How should Blue Apron differentiate itself from competitors like HelloFresh and traditional grocery shopping?

### Product Assortment Optimization
1. **Method Comparison:** How does attribute-based assortment optimization compare to traditional sales-based approaches?

2. **Implementation Challenges:** What are the practical difficulties in implementing choice modeling for product assortment?

3. **Competitive Advantage:** How can companies use customer choice insights to create sustainable competitive advantages?

4. **Technology Role:** How do modern analytics and AI change product assortment strategies?

## Venture Pitch Assignment

### Assignment Overview
Teams present 10-slide pitch decks for operations-focused ventures, targeting venture investors for first-round funding.

**Due Date:** August 11  
**Presentation:** August 14 (top 3 teams present live)  
**Peer Review:** All students rank assigned decks by August 13

### Operations-Focused Sectors
- **Customer Service Automation:** AI-powered process automation
- **Sharing Economy:** Asset utilization platforms
- **Healthcare Operations:** Process optimization and automation
- **Food Service Technology:** Restaurant and delivery optimization
- **Supply Chain & Logistics:** Visibility and optimization platforms
- **GenAI Applications:** Automation across various sectors

### Evaluation Criteria
- **Market Opportunity:** Size and growth potential
- **Operational Innovation:** Unique process improvements
- **Business Model:** Revenue and unit economics
- **Competitive Advantage:** Sustainable differentiation
- **Implementation Feasibility:** Realistic execution plan

## Modern Customer Analytics

### Advanced Techniques
- **Machine Learning:** Predictive customer behavior models
- **Real-Time Analytics:** Dynamic response to customer actions
- **A/B Testing:** Continuous optimization of customer experience
- **Cohort Analysis:** Understanding customer behavior over time

### Privacy and Ethics
- **Data Protection:** GDPR and privacy regulations
- **Algorithmic Bias:** Ensuring fair treatment of all customers
- **Transparency:** Clear communication about data usage
- **Customer Control:** Opt-out and preference management

## Key Takeaways
- **Strategic Message:** For subscription models, Customer Lifetime Value (CLV) analysis is crucial for understanding unit economics. For retail, an attribute-based approach to assortment planning is superior to simple sales data analysis.

- **Customer Focus:** Operations should be designed around customer preferences and behavior patterns.

- **Data-Driven Decisions:** Modern choice modeling enables more sophisticated operational strategies.

- **Unit Economics:** Understanding the relationship between acquisition cost and lifetime value is critical for sustainable growth.

## Preparation for Next Class
- Review GenAI applications in operations management
- Consider how artificial intelligence changes traditional operational processes
- Think about automation opportunities in various industries

## Teaching Notes
- Emphasize the connection between customer insights and operational decisions
- Use Blue Apron as cautionary tale about unit economics
- Highlight the evolution from intuition-based to data-driven assortment decisions
- Connect customer choice modeling to earlier revenue management concepts
- Prepare students for discussions about technology's role in operations
