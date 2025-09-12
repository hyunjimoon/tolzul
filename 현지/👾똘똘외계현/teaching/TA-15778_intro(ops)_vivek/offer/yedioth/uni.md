### Final Grade & Feedback
Q1: 10/15 [Q1 result 422 is outside 5% range of 419]
Q2: 15/15
Q3: 15/15
Q4: 15/15
Q5: 10/10
Bonus: 0/10
**Total: 65/80**

● Section A
● 15.778 Operations Management
● Yedioth Case Report
● Study group:
● Aimee Su
● Artur Martyniuk
● Myint Htay Win
● Omar Dominguez
● Sree Kolli

1

1. In the current distribution model, where each retailer is supplied once,
independently of all other retailers. What would be a good method to compute the
quantity shipped to each retailer if one wishes to guarantee that 99% of customers
will be served? Apply your approach to compute recommended quantities to the 50
retailers (explain the methodology in the body of the report and provide the results
in appendix.
Methodology: Independent method with 99% of service level)
Data Collection
Weekly sales data was collected per retailer over several weeks
Estimate Mean and Standard Deviation
For each retailer:
µ: average weekly sales
σ: standard deviation of weekly sales per customer
Set Service Level
A 99% service level corresponds to a z-score of 2.32, meaning we aim to meet or exceed
demand in 99% of the weeks.
Calculate Recommended Quantity
Using the standard safety stock formula:
Q*=⌈μ+z⋅σ⌉
Q*: weekly quantity to ship
z=2.32 for 99% coverage
This method is applied independently for each retailer.
Values are rounded up to the nearest whole number
The total Q* weekly magazines is 🚨422 units🚨.

2

2. If Yedioth could implement full pooling among all of the 50 retailers what would
be the estimated benefit in terms of total production levels and returns (assume that
the required service level is 99%). Note: Full pooling means that somehow all of the
retailers could be supplied in real time from the same pool of inventory.
In the full pooling model, all 50 retailers are served from a centralized inventory pool. Weekly
sales across retailers are aggregated, and the system is treated as one combined demand
stream.
Steps we followed:
1.- Aggregate weekly demand across all retailers.
2.- Calculate mean (µ) and standard deviation (σ) of total weekly demand.
3.- Apply 99% service level using formula
● Q pool=⌈μ aggregated weekly demand +z⋅σ of aggregated weekly demand⌉z @99%=
2.326
● Estimated savings pooling vs independent = 422 units (independent) - 236 units
(pooling) = 186 units weekly
Recommended demand with pooling = Q* = 🚨236 Units🚨 / week

3. Suppose that one could implement full pooling only among retailers that are
treated by the same sales agent, what would be the potential benefit in terms of
production levels and returns (assume 99% service level). Compare to 2) above.
Methodology for Partial pooling (293 units) vs. Full pooling (236 units):
●
●
●

Requires 57 more units/week
Full pooling still provides greater efficiency but is harder to implement
Pooling at the sales agent level offers a practical balance between cost savings and
implementation ease, capturing much of full pooling’s efficiency through existing visit
routines

Total Q* with pooling by agent = 🚨293 units🚨 / week

4. Propose more realistic policies that leverage the fact that the sales agent visits
each retailer in the middle of the
week. What would the benefit be of these policies?
Policy 1
We are deeply concerned about the 4,731 returned magazine units, which not only reflect
overproduction costs but also added expenses for collection and scrapping. While we
acknowledge that sales agents visit on Wednesdays, refilling distribution centers at this
return rate offers little value. However, agents’ input can help refine demand forecasts and
reduce variability. To address this, we propose 🚨lowering the service level to 90%🚨 to
significantly reduce returns

3

Policy 2
How to leverage mid-week agents visit

1. Mid-week sale agents visit allows the company to capture half a week sales data and
stock levels. This allows high-performing retailers to receive top-ups before the
weekend peak, while pooling stocks from low-performing retailers. It can reduce
overstock in low-demand stores and avoid lost sales in high-demand ones.
2. Adjusting forecasts through mid-week visits reduces the variability compared to the
weekly one, helping correct unexpected demand surges or poor-performing stores.
Theoretically, reducing variability narrows the spread of the distribution, ultimately
minimizing the stock returns.
3. Micro pooling among agent retailers allows reallocation of excess magazines to
nearby stores. Alternatively, micro pooling by locations (within 2-3km) offers more
efficient reallocation.

5. What do you think are the organizational challenges that Assaf will have to
address?
1. Cultural Friction: The organization has had a history of overstocking and the existing
infrastructure supports that type of behavior as well as the retailers’ mindsets.
However, in order to pivot this point of view, we can implement pilots to help get
people aligned with this new shift in behavior. This will take time but it will be a
critical component to getting buy in and having influence over the organization. The
framing could be “modernizing and optimizing for loyalty” versus “breaking tradition.”
(Less returns means more efficiency but positioning matters.)
2. 🚨Misaligned Sales Incentives: Sales agents are paid on volume🚨. If we reduce their
potential upside, the sales team will no longer be incentivized to perform in the same
way. Hence, we need to focus on revamping their sales compensation structure to
ensure that it aligns with the business goals around efficiency. This will be positively
accepted as long as they still have a path to getting their total OTE and compensation.
3. Technology + Coordination: We need to balance access to data with additional cost
investments. As we become more data centric in our decision making, we can be
better in terms of our capital allocation for new investments as well. In addition,
regional coordination requires more tooling.

4

