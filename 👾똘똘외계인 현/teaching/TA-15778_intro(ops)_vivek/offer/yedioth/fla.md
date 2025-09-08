### Final Grade & Feedback

Q1: 15/15
Q2: 15/15
Q3: 15/15
Q4: 15/15
Q5: 10/10
Bonus: 0/10

**Total: 70/80**

---

Yedioth Case Report
Section A, Flamingos:
Jay Kim

jaykim@mit.edu

John Law

john_law@mit.edu

Nicolas Melero

nmelero@mit.edu

Shuyan Feng

shuyanf@mit.edu

Vikram Siwach

vsiwach@mit.edu

1. In the current distribution model, where each retailer is supplied once a week independently of all other
retailers, what would be a good method to compute the quantity shipped to each retailer to guarantee
that 99% of customers will be served? Apply your approach to compute recommended quantities to the
50 retailers
(explain the methodology in the body of the report and provide the results in appendix).

Applying the Newsvendor formula to each of the 50 retailers:
qi = μi + k σi
•
•
•
•

qi
μi
k
σi

= optimized quantity to be sold at/ shipped to retailer i (each from 1 to 50) per week
= for retailer i, mean of quantity sold per week
= 2.32 (z-score per 99% service level)
= for retailer i, standard deviation of quantity sold per week

Key assumptions
1. Considered all data points provided (both sell-through and non-sell-through)
2. Assumed normal distribution across all retailers
3. All quantity numbers are rounded up to the nearest integer
Recommended quantities to the 50 retailers : 419
Please see the quantities for each of the 50 retailers in the appendix.(Appendix-Q1)
2.

If Yedioth could implement full pooling among all of the 50 retailers what would be the estimated
benefit in terms of total production levels and returns if the required service level is 99%?
(Note: Full pooling means that somehow all of the retailers could be supplied in-real-time from the same pool of inventory.)

1

The same Newsvendor formula can be applied, but this time with mean (μ) and standard deviation (σ)
calculated for all 50 retailers based on the sum of total sales each week. The formula will be tweaked as
follows:
q all retailers pooled = μ all retailers pooled + k σ all retailers pooled
•
•
•
•

q all retailers pooled
= optimized quantity to be shipped to all 50 retailers per week at 99% service
level
μ all retailers pooled
= mean of quantity sold by all 50 retailers per week
k
= 2.32 (z-score per 99% service level)
σ all retailers pooled
= standard deviation of quantity sold by all 50 retailers per week

Estimated benefit in total production levels and returns
Before Pooling = 419 magazines per week (rounded up to the nearest integer)
After Pooling
Δ

= 236 magazines per week (rounded up to the nearest integer)
= 183 magazines fewer per week

Please see the quantities for each of the 50 retailers in the appendix.(Appendix-Q2)
Compared to the #1 answer, the potential benefit in terms of production level and returns would
be increased by 183 (419 – 236 = 183).

3. Suppose that one could implement full pooling only among retailers that are treated by the same sales
agent. What would be the potential benefit in terms of production levels and returns, assuming 99%
service level. Compare to your #2 answer.
Calculated each retailer’s expected average demand (μ) and STD (𝜎) on a weekly basis.
Assumed the demand follows a normal distribution

•
•
•
•

Q𝑖 : Recommended quantity for agent 𝑖
𝜇𝑖 : Mean of weekly total sales for agent
K : 2.32 (z-score per 99% service level)𝜎𝑖: Standard deviation of weekly total sales for agent

2

The expected weekly total sales are 293
Please see the quantities for each of the 50 retailers in the appendix.(Appendix-Q3)
Compared to the #2 answer, the potential benefit in terms of production level and returns would
be increased by 57 (293 – 236 = 57).

Conclusion: Full pooling benefits > Partial pooling by sales agents > No pooling at all. The power
of pooling scales with the number of pooled units—larger pools reduce variability more
effectively.
4. Propose more realistic processes/strategies that leverage the fact that the sales agent visits each retailer
in the middle of the week. What would the benefit be of these processes/strategies?
Given that sales agents visit retailers midweek, we can design practical strategies that capture
partial benefits of pooling without requiring full real-time tracking systems.
Strategy 1: Hold off certain inventory for each retailer based on estimated weekly demand at the
beginning of the week and only deliver a smaller-than-expected batch every Sunday.
In the middle of the week, sales agents check inventory and sales. If understocked, deliver
additional units from a regional hub or other retailers. If overstocked, reallocate surplus to nearby
high-demand retailers, and re-shuffle supplies across nearby retailers if feasible, or through restocking from the central warehouse. As a result, production reduction and return rate are down
from pooling and inventory moves around among retailers.
Key benefits include:
• Reduces initial overstock and lowers the returns
• Prevents lost sales in high-demand weeks
• Simulates partial pooling without centralized inventory
Strategy 2: Assume sales agent shifts out all the forecast demands, and shift among them in the
mid-week, maintaining barely a tiny buffer stock at agent-level hubs. Only high-variability or highsales retailers are eligible for a midweek top-up to count for sales volatility.
Key benefits include:
• Low implementation cost

3

•
•

High ROI on inventory reduction as most of the stocks have shipped out
Scalable to many retailers

Strategy 3: Dynamic forecast update using midweek sales. Use Wednesday sales to forecast the
second half of the week’s demand. Fit a regression to predict the 2nd half sales by using the midweek sales.
Example: If an average of 60% of sales occur in the first half, and the retailer sold 6/10 by Wed,
forecast total = 10 → no top-up. If sold 8/10, forecast total = 13 → deliver 3 more. In this case,
equipping agents with mobile apps to report sales. Central system sends replenishment
recommendations by Tuesday night.
Key benefits include:
• More accurate than static weekly forecasts, as the regression brings more predictability and
visibility for the forecasted demand

•
•

Reduces the need for safety stock
Can potentially cut (again) total production.

Overall benefit of midweek strategies: achieve partial full pooling benefit with minimal IT
investment

5. What do you think are the organizational challenges that Assaf will have to address?
Assuming we adopt our preferred Strategy 1 of the “hold-back & mid-week balance” model, the
organizational change Assaf is dealing with is key. He will have to define the following:

1. Agent incentive realignment: Current pay is volume-linked; shifting to net-sold + waste bonuses
will need comp plan redesign and clear communication.
2. Data discipline & accuracy: Mid-week counts must be timely and reliable; even small errors
cascade into missed top-ups or unnecessary re-routes. Requires mobile tools, training, and
compliance monitoring.
3. Cross-functional coordination: R&D (forecasting) sets hold-back %, Logistics manages hub stock;
Sales executes re-routes—weekly S&OP cadence and crisp decision rights are essential.
4. Mini hub & run logistics: Adding Thursday van runs and micro-buffers raises complexity and fixed
cost; ROI must be proven quickly in pilot regions.

4

5. Cultural resistance to lower first-ship volumes: Editorial, advertising, and field teams equate “full
racks” with market presence; early success stories and KPI dashboards are needed to build trust.
6. System support & scalability: Simple spreadsheets may work in a pilot, but scaling to 8,000
retailers needs lightweight routing and inventory software.
7. Governance & guardrails: Override limits, sealed-return verification, and exception auditing
prevent gaming and keep the focus on service + waste KPIs.
8. Retailers’ resistance: Retailers may resist changes under the new model, as they have little to gain
directly from more efficient inventory management. They may object to the mid-week removal of
unsold stock based on actual sales, especially if they perceive it as a loss of control or autonomy.
Since their revenue is not typically affected by returns, they may prefer to keep full inventory
throughout the week to avoid stockouts or customer dissatisfaction.
Addressing these seven items—especially incentives, data accuracy, and cross-team
governance—will determine whether the strategy delivers its promised waste reduction without
jeopardizing the 99 % service level.

5

Appendix – Q1

6

Appendix – Q2

7

Appendix – Q3

8

