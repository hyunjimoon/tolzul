### Final Grade & Feedback

Q1: 15/15
Q2: 15/15
Q3: 15/15
Q4: 10/15 [No quantitative example provided]
Q5: 10/10
Bonus: 0/10 [Only censoring mentioned, no distribution assumption]

**Total: 65/80**

---

Section B
Pat Ovando Roche
Makeda Mekonnen
Ricardo Suarez Heredia
Shiva Mehrotra
Wee Hao Ng

THE YEDIOTH GROUP: CASE STUDY REPORT
Question 1. In the current distribution model, where each retailer is supplied once a week
independently of all other retailers, what would be a good method to compute the quantity
shipped to each retailer to guarantee that 99% of customers will be served? Apply your
approach to compute recommended quantities to the 50 retailers.
Method A: Estimating Demand based on Observed Sales (i.e. sales = demand)
Let

•
•
•

𝑖 ∈ {1,2, … , 𝑁} be the index for retailers (N=50)
𝑡 ∈ {1,2, … , 𝑇} be the index for distribution weeks (2008-2009)
𝑆𝑖,𝑡 be the observed sales for retailer 𝑖 in week 𝑡

Step 1: Estimate Mean (μ) of Observed Sales (Demand)
For each retailer, estimate the mean weekly demand (μ) (i.e., average of weekly sales):
𝑻

𝟏
𝝁 = ∑ 𝑺𝒊,𝒕
𝑻
𝒕=𝟏

Step 2: Estimate Standard Deviation (σ) of Observed Sales (Demand)
For each retailer 𝑖,estimate the standard deviation of weekly sales:
𝑻

𝟏
𝝈𝒊 = √
∑(𝑺𝒊,𝒕 − 𝝁𝒊 )𝟐
𝑻−𝟏
𝒕=𝟏

Step 3: Compute quantity to ship (Q) for 99% service level
Assuming demand follows a normal distribution, the quantity to ship to retailer 𝑖 is:
𝑸𝒊 = 𝝁𝒊 + 𝒌𝝈𝒊
Where:
• 𝑘 = 2.3326 is the Z-score for a 99% service level.
Step 4: Estimate total quantity to distribute (Q)

𝒏

𝑸∗ = ∑ 𝑸𝒊
𝑰=𝟏
Total Q (𝑸∗𝑨 ) = 393.5 → 394 units

Refer to the Appendix for full computation details
Method Limitation: This method assumes observed sales is equal to demand, which is
only true when there are no stockouts. In reality, censored demand exists. If a retailer
sells out, true demand may be higher than observed sales.

Method B: Estimating Demand with Censored Sales (Stockouts) (i.e. demand ≠ sales)
Let
• 𝑖 ∈ {1,2, … , 𝑁} be the index for retailers (N=50)
• 𝑡 ∈ {1,2, … , 𝑇} be the index for distribution weeks (2008-2009)
• 𝑆𝑖,𝑡 be the observed sales for retailer 𝑖 in week 𝑡
• 𝑄𝑖,𝑡 be the total quantity available to retailer 𝑖 in week 𝑡 (i.e., distributed + added)
• 𝑆𝑒𝑙𝑙𝑇ℎ𝑟𝑜𝑢𝑔ℎ𝑖,𝑡 = 1 if all inventory was sold (i.e, stockout), 0 otherwise
Step 1: Calculate the Stockout Rate (𝑃)
We calculate the stockout rate for each retailer 𝑖 across all weeks 𝑇
𝑻

𝟏
𝑷𝒊 = ∑ 𝑺𝒆𝒍𝒍𝑻𝒉𝒓𝒐𝒖𝒈𝒉𝒊,𝒕 = 𝟏
𝑻
𝒕=𝟏

Step 2: Calculating Demand Standard Deviation (σ)
We take the standard deviation σ of weekly sales for each retailer.
𝑻

𝟏
𝝈𝒊 = √
∑(𝑺𝒊,𝒕 − ̅
𝑺𝒊 )𝟐
𝑻−𝟏
𝒕=𝟏

Where:
• 𝑆𝑖̅ is the average of observed sales for retailer 𝑖
Step 3: Estimating Mean Demand (μ)
To estimate demand 𝐷𝑖 , we consider the total quantity available for retailer (distributed and
added) as Q. Assuming demand follows a normal distribution 𝐷𝑖 ~𝒩(𝜇𝑖 , 𝜎𝑖2 ), the stockout rate
represents the probability of a stockout (i.e. demand exceeds available inventory):
ℙ(𝑫𝒊 > 𝑸𝒊 ) = 𝑷𝒊
𝑸𝒊 − 𝝁𝒊
𝑸𝒊 − 𝝁𝒊
𝑷𝒊 = 𝟏 − ℙ(𝐙 <
) = 𝟏 − 𝚽(
)
𝝈𝒊
𝝈𝒊
We can then calculate 𝜇𝑖 which would be the estimated demand for newspaper sales for each
retailer.
Step 4: Compute Weekly Shipment Quantity for 99% service levels (Q)
Having estimated both σ and μ, we estimate Q for 99% service level for each retailer using:
𝑸𝒊 = 𝝁𝒊 + 𝒌𝝈𝒊
Where:
• 𝑘 = 2.3326 is the Z-score for a 99% service level.
Step 5: Estimate total quantity to distribute (Q)

𝒏

𝑸∗ = ∑ 𝑸𝒊
𝑰=𝟏
Total Q (𝑸∗𝑩 ) = 421.8 → 422 units
Refer to the Appendix for full computation details
Conclusion: We recommend Method B as it accounts for censored demand caused by
stockouts. By adjusting for weeks where demand likely exceeded available inventory,
Method B provides a more accurate estimate of true customer demand and a better basis
for service-level-aligned inventory policy.

2

Question 2. If Yedioth could implement full pooling among all of the 50 retailers what would
be the estimated benefit in terms of total production levels and returns if the required
service level is 99%? (Note: Full pooling means that somehow all of the retailers could be
supplied in-real-time from the same pool of inventory.)
Method C: Estimating Aggregate Weekly Demand across Retailers
Let
• 𝑖 ∈ {1,2, … , 𝑁} be the index for retailers (N=50)
• 𝑡 ∈ {1,2, … , 𝑇} be the index for distribution weeks (2008-2009)
• 𝑆𝑖,𝑡 be the observed sales for retailer 𝑖 in week 𝑡
Step 1: Estimate Total Weekly Sales
Assuming that demand is equal to observed sales, for each of the weeks 𝑡, compute the total
sales across all 50 retailers:
𝑵

𝑫𝒕 = ∑ 𝑺𝒊,𝒕
𝒊=𝟏

This provides a time series {𝐷1 , 𝐷2 , … , 𝐷𝑇 } representing total weekly demand.
Step 2: Estimate Mean and Standard Deviation of Weekly Sales
Let

•
•

𝜇𝐷 be the mean of total weekly demand
𝜎𝐷 be the standard deviation of total weekly demand
𝑻

𝟏
𝝁𝑫 = ∑ 𝑫 𝒕
𝑻
𝒕=𝟏

𝑻

𝟏
𝝈𝑫 = √
∑(𝑫𝒕 − 𝝁𝑫 )𝟐
𝑻−𝟏
𝒕=𝟏

Step 3: Compute quantity to ship at 99% service level
𝑸𝑫 = 𝝁𝑫 + 𝒌𝝈𝑫
Where:
• 𝑘 = 2.3326 is the Z-score for a 99% service level.
Refer to the Appendix for full computation details
Standard
Mean Demand (𝝁𝑫 ) Deviation of
Demand (𝝈𝑫 )
189.6
20.0

Q* at 99%
236 units

3

Step 4: Compare total quantity to distribute between Method B (Question 1) and Method C
(Question 2)
Current Distribution Model
(Method B)
Total Quantity to Distribute (Q*)
𝑸∗𝑩 = 422 units

Full Pooling
(Method C)
𝑸∗𝑪 = 236 units

Then the benefit from full pooling is the reduction in total quantity required:
𝚫𝑸 = 𝑸∗𝑩 − 𝑸𝑪∗
𝚫𝑸 = 𝟒𝟐𝟐 − 𝟐𝟑𝟔 = 𝟏𝟖𝟔 𝒖𝒏𝒊𝒕𝒔
Question 3. Suppose that one could implement full pooling only among retailers that are
treated by the same sales agent. What would be the potential benefit in terms of production
levels and returns, assuming 99% service level. Compare to your #2 answer.
Method D: Estimating Weekly Demand by Sales Agent
Let
•
•
•

Α be the set of sales agents with 𝑗 ∈ 𝐴
𝑡 ∈ {1,2, … , 𝑇} be the index for distribution weeks (2008-2009)
𝑆𝑗,𝑡 be the total number of copies sold by agent 𝑗 in week 𝑡

Step 1: Aggregate weekly sales per agent
Assuming that demand is equal to observed sales, for each of the weeks 𝑡, compute the

total sales across all 10 agents:

𝑨

𝑫𝒕 = ∑ 𝑺𝒋,𝒕
𝒋=𝟏

This provides a time series {𝐷1 , 𝐷2 , … , 𝐷𝑇 } representing total weekly demand across agents.
Step 2: Estimate Mean and Standard Deviation of Weekly Sales
Let

•
•

𝜇𝐷 be the mean of total weekly demand
𝜎𝐷 be the standard deviation of total weekly demand
𝟏

𝝁𝑫 = 𝑻 ∑𝑻𝒕=𝟏 𝑫𝒕

𝟏

𝝈𝑫 = √𝑻−𝟏 ∑𝑻𝒕=𝟏(𝑫𝒕 − 𝝁𝑫 )𝟐

Step 3: Compute quantity to ship at 99% service level
𝑸𝑫 = 𝝁𝑫 + 𝒌𝝈𝑫
Where:
• 𝑘 = 2.3326 is the Z-score for a 99% service level.

4

Refer to the Appendix for full computation details

Total Quantity to
Distribute (Q*)

Current Distribution
Model (Method B)

Full Pooling
(Method C)

Partial Pooling –
Sales Agents
(Method D)

𝑸∗𝑩 = 𝟒𝟐𝟐 𝒖𝒏𝒊𝒕𝒔

𝑸∗𝑪 = 𝟐𝟑𝟔 𝒖𝒏𝒊𝒕𝒔

𝑸∗𝑫 = 𝟐𝟖𝟕 𝒖𝒏𝒊𝒕𝒔

Question 4. Propose more realistic processes/strategies that leverage the fact that
the sales agent visits each retailer in the middle of the week. What would the benefit
be of these processes/strategies?
Proposal A. Mid-Week Inventory Replenishment ("Two-Shipment Model")
• Deliver a base quantity on Sunday (e.g., 60–70% of expected demand).
• Use the Wednesday visit to collect early-week sales data and replenish
stock for high-performing retailers.
Benefits:
• Reduces initial overproduction and overstocking at the start of the week.
• Maintains service levels by correcting early underestimates (i.e. captures
missed demand due to early stockouts).
• Reduces unpredictable demand variability by splitting the fulfilment
into two phases, allowing mid-week corrections based on actual trends.
• Improves predictable variability, making weekly planning more datadriven and reducing reliance on pure forecasts.
Requirements:
• Method could requires basic IT (best-case scenario) or manual reporting
(worst-case scenario).
• Method required logistic support and additional costs for mid-week
deliveries.
Proposal B. Early-Week Sales-Based Forecast Adjustment (Predictive
Replenishment)
• Use early-week sales (e.g., Sun–Tues) to update full-week demand
forecasts.
• Sales agents can manually report sales or estimate remaining inventory.
Benefits:
• Enables proactive adjustments in future print runs.
• Builds a feedback loop between the field and the supply and operations
team.
• Helps reduce unpredictable demand variability through near-real-time
sales data-informed planning (smart inventory decision making).
• Improves service level without full pooling.
Requirements:
• Method required historical data analysis (data collection devices) and
training/validation of forecasting models.
5

Proposal C. Localised Redistribution Among Retailers (Intra-Agent Pooling)
• Agents identify overstocked and understocked retailers on Wednesday.
• Transfer magazines within their cluster to better match supply with
demand (i.e. move unsold inventory from overstocked retailers to those
experiencing stockouts).
Benefits:
• Simulates pooling without systemic changes (i.e. centralized inventory).
• Reduces variability across the network by reallocating excess inventory
to high-demand locations.
• Increases overall sales and customer satisfaction with minimal cost.
• Reduces waste and lost sales.
Requirements:
• Method requires agent training, incentives as well as coordination and
tracking tools for stock movement.
Proposal D. Use of smart stands or RFID for real-time tracking
User RFID enabled stands to track inventory levels automatically upon
unit movement.
• RFID tags on magazines are read by smart stand scanners, updating the
inventory level to the central database.
•

Benefits:
Automation of inventory tracking increases accuracy and requires
minimal manual intervention.
• Enable real-time pooling and forecasting (Proposal B).
Requirements:
• Considerable investment and development time for RFID infrastructure
and suitable integration of tags into magazines at a sustainable cost.
• Experimentation through pilot studies with larger, medium and small
retailers (small subset) for advantages and disadvantages.
•

6

Question 5. What do you think are the organizational challenges that Assaf will have
to address?
A. Cultural Resistance:
• Sales agents are incentivised on sales volume, not efficiency.
• Staff may resist changes that reduce shipments or increase workload
(e.g. data collection).
B. IT Limitations:
• Most kiosks lack EDI or digital sales systems.
• Requires investment in tech infrastructure (e.g. RFID, mobile apps, or
smart stands).
• Build internal capabilities for statistical and analytical methods.
C. Interdepartmental Alignment:
• Research, Distribution, and Sales must coordinate on forecasting and
inventory.
• Requires training, role realignment, and perhaps changes in incentive
structures.
D. Trust and Change Management:
• Fear of stockouts and lost revenue is entrenched.
• New systems must demonstrate reliability and win buy-in gradually.
E. Operational Coordination:
• Adapt current logistics to support additional deliveries.
• Coordination among agents for additional stock delivery and/or inventory
transfer across retailers.
F. New Inventory proposals aligned to strategy
• Changes in inventory and supply have to align with strategic goals and
constraints: (1) free up printing capacity that can be monetized for external
customers (growth target); (2)reduce costs while maintaining advertising
revenue (profitability target); (3) balance efficiency with retailer satisfaction
(brand management target);

7

