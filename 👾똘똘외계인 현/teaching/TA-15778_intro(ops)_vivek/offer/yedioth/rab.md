### Final Grade & Feedback

Q1: 15/15
Q2: 10/15 [Calculated 252, outside ±5% range of 236]
Q3: 10/15 [Calculated 308, outside ±5% range of 287]
Q4: 10/15 [No quantitative example provided]
Q5: 10/10
Bonus: 0/10 [Only censoring mentioned, no distribution assumption]

**Total: 55/80**

---

15.778 - Homework 2 - Yedioth Case
Team Rabbits - (Section B)
Ryosuke Kobayashi, Arjun Banerjee, Paul Guiloff, Vivek Mehta, Talha Rehmani
1. In the current distribution model, where each retailer is supplied once, independently of all
other retailers. What would be a good method to compute the quantity shipped to each
retailer if one wishes to guarantee that 99% of customers will be served? Apply your
approach to compute recommended quantities to the 50 retailers (explain the methodology
in the body of the report and provide the results in the appendix).
In our report, we define “uncensored demand” as demand data that includes not only actual
sales but also potential lost sales due to stockouts. Under Yedioth’s standard operations, it
was difficult to distinguish whether a sellout reflected fulfilled demand or missed
opportunities—this is referred to as “censored demand.” By contrast, in Assaf’s
experiment, sales agents visited stores daily to record actual customer demand throughout
the week. This allowed us to observe uncensored demand, providing a more accurate basis
for setting shipment levels. 🚨uncensored demand awareness🚨
In order to guarantee that 99% of the customers' demands are met, we are going to use the
99th percentile of historical weekly sales for each retailer. The following steps outline the
methodology used to compute the recommended shipment quantity:
Step 1: Calculate the Mean (μ)
For the expected value, we have taken the average weekly demand for each retailer. This
is highlighted in columns D4 to D53, in the Question 1 tab of the attached Excel file.
For Example, for Customer 1, the number of observation weeks is 45
Mean
(μ)
=
4.27
This is the average number of magazines sold per week over 45 weeks
(See Column D, rows 4 to 53 in the "Question 1" tab)
Step 2: Calculate Variability (σ)
For each retailer, the standard deviation of weekly sales has been calculated to capture the
variability
in
demand.
For
Customer
1,
the
standard
deviation
is
1.76
(See Column E, rows 4 to 53 in the "Question 1" tab)
Step 3: Calculate Recommended Quantity q*
We apply the newsvendor formula to determine the quantity needed to satisfy 99% of
demand
q* = μ + k . σ
We know that for a 99% service level, k corresponds to 2.33

Therefore,

q*

=

μ

+

2.33

.

σ

This means we recommend shipping 9 (8.38 is rounded off to 9) magazines to customer 1
per week.
Overall
Summary:
Column F in Question 1 tab, shows the recommended number of magazines to be shipped
per week to each retailer to meet the 99% service level.
If we sum the demand of all 50 customers with variability, the total number of magazines
Yedith should print and ship weekly is
Total Weekly Production Quantity = 394 (approx)
However, this quantity involves partial (decimal place) magazine allocation to stores. We
would have to round up to the nearest integer for each store
Total Weekly Production Quantity when rounded = 419 🚨correct ~419🚨
This guarantees that Yedioth can serve 99% of its customers across all 50 retailers without
pooling and under the current distribution model, where each retailer is served
independently.
2. If Yedioth could implement full pooling among all of the 50 retailers what would be the
estimated benefit in terms of total production levels and returns (assume that the required
service level is 99%). Note: Full pooling means that somehow all of the retailers could be
supplied in real time from the same pool of inventory.
To estimate the benefit of full pooling among all 50 retailers at a 99% service level, we
treat the entire network as if it were a single, centralized system. In this case, inventory can
be flexibly shared across all locations in real time, allowing demand variability to be
smoothed out through aggregation.
To simulate this, we calculate the total weekly sales across all 50 retailers. However, due
to missing data for some retailers, simply summing observed values would result in
inconsistencies across weeks and introduce noise into the average and standard deviation.
To address this, we first compute the average weekly sales per retailer (excluding missing
data), then multiply by 50 to estimate the weekly total sales as if all 50 retailers reported
data.
Based on this approach, the estimated weekly demand has:
● Mean = 206.88
● Standard deviation = 19.18
Using a 99% service level (z ≈ 2.33), the required inventory level
is:

● 206.88 + 2.33 × 19.18=251.56
This suggests that by implementing full pooling, the total
inventory required to meet demand with 99% certainty can be
significantly reduced—demonstrating the efficiency and riskpooling benefits of centralized inventory management. In
practice, since the number of copies must be an integer, the
required inventory would be rounded up to 252 copies. 🚨calculated 252, outside range🚨 This means
fewer copies are needed than in the current system (Question 1),
while still meeting the 99% service level. Furthermore, pooling
reduces the risk of overstocking at individual retailers, which in
turn lowers the likelihood of returns.
For detailed calculations, please refer to Question 2 in the attached file.
3. Suppose that one could implement full pooling only among retailers that are treated by the
same sales agent, what would be the potential benefit in terms of production levels and
returns (assume 99% service level). Compare to 2) above.
This approach is similar to Question 2, but instead of pooling all 50 retailers together, we
assume each sales agent manages a pool of 5 retailers. So there are 10 separate pools.
For each week, we estimate the total sales for each sales agent by adjusting for missing
data. We take the average sales per available retailer, then multiply by 5 to simulate
complete data.
Next, we calculate the average and standard deviation of weekly demand for each sales
agent, and apply the 99% service level formula:
● μ + 2.33 × σμ + 2.33 × σ
We sum these 10 inventory levels to get the total required inventory across all 50 retailers:
302.48 units. After rounding up each sales agent’s inventory to the nearest integer, the total
required inventory increases slightly to 308 units. 🚨calculated 308, outside range🚨
This is lower than in Question 1 (no pooling), but higher than in Question 2, where all
retailers were fully pooled together. So partial pooling gives a moderate benefit.
For detailed calculations, please refer to Question 3 in the attached file.
4. Propose more realistic policies that leverage the fact that the sales agent visits each retailer
in the middle of the week. What would the benefit be of these policies?
A more realistic policy would be that each store would have its static inventory level set
using the methodology above. The agent would leverage micropooling to manage his risk
of sell-through. As an agent gauges orders partway through the week, they are authorized
the ability to re-allocate inventory, or order more if needed, based on demand within stores

in the agent’s scope. This would partially yield the benefits of the results of pooling by
agent, with some loss due to the more realistic model of a weekly check-in.
Another policy would be to make partial shipments on Sunday, and plan a 2nd partial
delivery on Wednesday for each store; therefore, if a store or set of stores is
underperforming that week, we could potentially avoid some returns while still planning
for the higher end of variability. We would experiment with this policy by starting at a
90% initial partial shipment and reducing that percentage value week-over-week until an
optimal operating stock is achieved. The agent would make the decision of how much of
the remaining allocation to deliver during the mid-week check-in based on actual vs
expected performance numbers of each seller. 🚨specific mechanisms🚨
As an additional need, sellers must document on sell-through days how many times
customers request a magazine after it's gone to document demand. This would enable us
to better predict demand instead of sell-through functioning as partial/incomplete data.
To attack the information flow problems, agents would be equipped with an RFID tracker
or inventory scanner to scan inventory and digitally transmit the inventory values at midweek check-in. This would enable the production and delivery teams to respond
immediately on Wednesday without delay.
To protect against potential overestimation or overallocation pressure from the retailers,
we would institute a per-unit return charge policy for any returned stock above our 99%
calculated allocation for each retailer.
5. What do you think are the organizational challenges that Assaf will have to address?
The biggest challenge will be getting the retailers to align with stock reallocations 🚨multiple stakeholders🚨 because
they work independently and do not care if other retailers run out.
The next big challenge would be the coordination aspect of both the check-in and the stock
reallocation mid-week. This requires good information flow and cooperation of multiple
parties (retailer, agent, and delivery).
These policy changes will require training for the agents, and potentially some training or
standardization for the retailers.
These policies of changing allocation may be met by resistance from the retailers because
they are already used to full allocation at the beginning of every week
Another big challenge will be collecting sell-through demand data beyond stock running
out, because a customer may not voice their demand/discontent, and a retailer may not be
motivated to document even though it's in their best interest from a stock allocation
standpoint. Alternatively, the retailer may overestimate their sell-through demand because
they are trying to get protection stock.

