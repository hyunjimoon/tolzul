### Final Grade & Feedback

Q1: 15/15
Q2: 15/15
Q3: 15/15
Q4: 10/15 [No quantitative example provided]
Q5: 10/10
Bonus: 0/10

**Total: 65/80**

---

Yedioth case
Owls
Andre Villela
Giacomo Puri Purini
Cameron Heard
Rebecca Koo
Julian Araoz

Question 1

In the current distribution model, where each retailer is supplied once, independently of all other
retailers. What would be a good method to compute the quantity shipped to each retailer if one wishes to
guarantee that 99% of customers will be served? Apply your approach to compute recommended
quantities to the 50 retailers (explain the methodology in the body of the report and provide the results in
appendix).
Calculate the mean 𝜇𝑖 and standard deviation 𝜎𝑖 for weekly sales per customer 𝑖. Assuming the
probability function for demand follows a normal distribution, determine the production quantity based
on a 99% probability that stock exceeds demand (k =2.32). Production quantity 𝑞𝑖 per customer 𝑖 is
expressed as 𝑞𝑖 = 𝜇𝑖 + 𝑘𝜎𝑖
This doesn’t fully account for unknown demand during stockouts – cases where all the magazines are
sold. In these cases, we don’t yet have an indicator of true demand. As such, we should experiment by
increasing the safety stock slightly for retailers who routinely sell out. For this exercise, we assume
suppressed demand is neglectable.
This method results in a weekly production of 419. 🚨correct ~419🚨 Applying this quantity for all weeks in the data
provided, average return would have been of 229.

Question 2

If Yedioth could implement full pooling among all of the 50 retailers what would be the estimated benefit
in terms of total production levels and returns (assume that the required service level is 99%). Note: Full
pooling means that somehow all of the retailers could be supplied in real time from the same pool of
inventory.
If we calculate the total weekly sales across all retailers, we can then calculate the average and standard
deviation. From there, we can apply the same formula for production quantity.
𝐴𝑣𝑒𝑟𝑎𝑔𝑒 𝑡𝑜𝑡𝑎𝑙 𝑤𝑒𝑒𝑘𝑙𝑦 𝑠𝑎𝑙𝑒𝑠 (𝜇) = 189.59
𝑆𝑡𝑎𝑛𝑑𝑎𝑟𝑑 𝑑𝑒𝑣𝑖𝑎𝑡𝑖𝑜𝑛 (𝜎) = 19.99
99% 𝑝𝑟𝑜𝑑𝑢𝑐𝑡𝑖𝑜𝑛 𝑞𝑢𝑎𝑛𝑡𝑖𝑡𝑦 (𝑞∗ ) = 189.59 + (2.32)(19.99)
𝑞∗ = 236 🚨correct pooling🚨
This method results in a weekly production of 236 and return of 47, resulting in a benefit of 183 lower
production and returns.

Question 3

Suppose that one could implement full pooling only among retailers that are treated by the same sales
agent, what would be the potential benefit in terms of production levels and returns (assume 99%
service level). Compare to 2) above.
Following the same methodology, we have:
Calculate the mean 𝜇𝑠 and standard deviation𝜎𝑠 for weekly sales per sales agent 𝑠 . Assuming the
probability function for demand follows a normal distribution, determine the production quantity based
on a 99% probability that stock exceeds demand (k =2.32). Production quantity per sales agent is
expressed as: 𝑞𝑠 = 𝜇𝑠 + 2.32 ⋅ 𝜎𝑠
This option would result in a weekly production of 293 🚨acceptable agent pooling🚨 and returns of 103. The production and returns are
57 units higher per week compared to Question 2’s.

Question 4

Propose more realistic policies that leverage the fact that the sales agent visits each retailer in the
middle of the week. What would the benefit be of these policies?
Assumptions:
• Single weekly production run: Yedioth cannot run multiple productions due to high fixed costs
• Pooling is feasible by sales agent, and incurs minimal redistribution costs
• Real time data feasible: it is feasible to gather and process data from first few days of sales before the
mid-week visits.
Proposed Policies
• Reassess optimal service level: check if the 99% service level is necessary, or if the optimal service
level based on marginal cost and marginal revenue structure would be different.
• Midweek Replenishment/Redistribution Visit: 🚨specific mechanisms🚨 Yedioth currently delivers magazines to each retailer
only once a week, on Sundays. This midweek visit presents a practical opportunity to replenish
inventory for high-demand retailers and redistribute inventory from low-demand retailers. By leveraging
the Wednesday visit, Yedioth could implement a two-phase replenishment/redistribution policy: initial
conservative supply followed by replenishment where needed.
• Demand Forecast Adjustment: Sales data from the first half of the week could be used to estimate
demand for the second half. It allows Yedioth to better match supply to demand and reduce
overproduction and returns.
Benefits of These Policies
• Reduced Returns and Waste: Production run could be smaller, with replenishment/redistribution midweek, thus minimizing excess inventory. In addition, stockouts could be reduced at high-demand
locations by resupplying before the weekend rush.
• Data-Driven Decisions: Midweek sales insights would enhance forecasting accuracy for both the
current and future cycles.
• No Major System Overhaul Required: These policies rely on existing agent visits and sales data
systems.

Question 5

What do you think are the organizational challenges that Assaf will have to address?
• Organizational Culture: Yedioth has a long-standing tradition of loyaltyw to employees and highly
cautious decision-making. This conservative culture may resist fundamental changes, especially those
that challenge the company’s instinctive practices and DNA.
• Infrastructure Constraints: Technologies like RFID or EDI require significant upfront investment and
system integration. While large retailers may already support EDI, most smaller kiosks do not, making
real-time inventory tracking difficult to implement. The IT infrastructure necessary to capture and
transmit sales data from the first half of the week does not currently exist, further limiting Yedioth’s
ability to support midweek replenishment strategies.
• Incentive Misalignment: 🚨multiple stakeholders🚨 Sales agents are compensated based on sales volume. If Yedioth reduces the
initial supply quantities to minimize waste, agents may push back, fearing that lower shipments could
negatively affect their commissions and performance. Adjusting the compensation structure for sales
agents could help achieve alignment to incentivize reducing returns.
• Data Availability: Little to no information was shared between Yedioth and its retailers due to the lack
of IT systems. For example, Yedioth is often unable to observe the true level of customer demand,
particularly in cases where retailers sell out of inventory. This issue, known as censored demand,
makes it difficult to distinguish between accurately met demand and lost demand due to stockouts.
• Logistics and route planning: mid-week redistribution of inventory may incur extra costs and require
careful route planning, to ensure excess inventory retailers are visited before retailers that require
replenishment.
• Retailer resistance: retailers may be unwilling to allow inventory mid-week returns, as it may result in
out of stocks.

Appendix

Full excel file submitted. Summary of results below.

