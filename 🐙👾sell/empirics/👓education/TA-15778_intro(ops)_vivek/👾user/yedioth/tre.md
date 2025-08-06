### Final Grade & Feedback
Q1: 15/15
Q2: 15/15
Q3: 15/15
Q4: 15/15
Q5: 10/10
Bonus: 0/10 [Only censoring mentioned, no distribution assumption]
**Total: 70/80**

Yedioth Case Report
15.778 Introduction to Operations Management

Sloan Fellows Section A Group T-Rex

Alecia Asiamigbe
Rahul Bandekar
Ido Levy
Christie Lucagbo
Marco Musazzi

July 31, 2025

1. In the current distribution model, where each retailer is supplied once a week
independently of all other retailers, what would be a good method to compute
the quantity shipped to each retailer to guarantee that 99% of customers will be
served? Apply your approach to compute recommended quantities to the 50
retailers (explain the methodology in the body of the report and provide the
results in appendix).
We took the following approach:
• First, we grouped the data by retailer using the values in the column
“Customer Number” (from retailer 1 to retailer 50). Then, we calculated the
expected value (or mean) of the weekly demand per retailer using the
historical data in column “Sales”.
• Next, we calculated the standard deviation of weekly demand per customer
• We calculated Q*i or the target quantity to be shipped to each retailer i
per week at 99% service levels and rounded up the quantity:
Q*i for retaileri = Meani + (K* StDevi )
where: K = 2.326, which is ~Z-score for 99% service levels
• We calculated the estimated Returnsi for each retailer i, which is given by
2.326*StDev i and rounded up the quantity
• Finally, we summed up (1) Q*i and (2) Returnsi for each retailer i=1 to 50 to
arrive at the total production requirements and total expected returns to meet
99% service levels.
This gave us the following results:
• Total Production Quantity without pooling: ~🚨419 units🚨
• Projected Returns without pooling: ~213 units
Note that we are 🚨underestimating the expected value of demand, because we do not
know what the actual value of demand would’ve been for weeks where a retailer had
a sell-through🚨 (this number can be estimated through statistical modeling but would
require additional assumptions on the demand curve shape). See Appendix A.
2. If Yedioth could implement full pooling among all of the 50 retailers what would
be the estimated benefit in terms of total production levels and returns if the
required service level is 99%? (Note: Full pooling means that somehow all of
the retailers could be supplied in-real-time from the same pool of inventory.)
If Yedioth could implement full pooling among all 50 retailers, then we would take the
following approach to calculate total production quantity Q* at 99% service levels:
• Calculate the expected value (or mean) of total weekly demand by grouping
the data in column “Sales” on a weekly basis
• Calculate the standard deviation of total weekly demand
• Calculate the Q*:
Q* = Mean + (K*StDev)
where: Mean = 189.59, K = 2.326, StDev = 19.99
• Calculate estimated Returns, which is given by 2.326*StDev
This gives us the following results:
• Total Production Quantity Q* with full pooling = ~🚨237 units🚨
• Projected Returns with full pooling= ~47 units
Therefore, by implementing full pooling, Yedioth could reduce total production
quantity by ~182 units (419 units minus 237 units) and reduce returns by 166
units (213 units minus 47 units). See Appendix B.

3. Suppose that one could implement full pooling only among retailers that are
treated by the same sales agent. What would be the potential benefit in terms
of production levels and returns, assuming 99% service level. Compare to your
#2 answer.
Assuming that Yedioth could implement pooling only for retailers handled by the
same sales agent, then we would take the following approach to calculate total
production quantity at 99% service levels:
• Group the data by sales agent using the values in the column “Sales Agent”
(from sales agent 1 to 10). Then, we calculated the expected value (or mean)
of the weekly demand of all retailers handled by each agent using the
historical data in column “Sales”.
• Next, we calculated the standard deviation of weekly demand per sales agent
• We calculated Q*j or the target quantity to be handled by each sales
agent j per week at 99% service levels:
Q*j for sales agentj = Meanj + (K* StDevj )
where: K = 2.326, which is ~Z-score for 99% service levels
• We calculated the estimated Returnsj for each sales agent j, which is given by
2.326*StDev i
• Finally, we summed up (1) Q*j and (2) Returnsj for each Sales Agent j=1 to 10
to arrive at the total production requirements and total expected returns to
meet 99% service levels.
This gives us the following results:
• Total Production Quantity for pooling per Sales Agent only = ~🚨287 units🚨
• Projected Returns for pooling per Sales Agent only= ~97 units
If Yedioth could only implement pooling among retailers handled by the same sales
agent, then total production quantity increases by ~50 units (287 units minus 237
units) and total returns increase by ~50 units (97 units minus 47 units) vs if
Yedioth could implement full pooling across all 50 retailers. Pooling by sales
agent gives partial benefits, i.e. better than independent, not as efficient as full
pooling. See Appendix C.
4. Propose more realistic processes/strategies that leverage the fact that the
sales agent visits each retailer in the middle of the week. What would the
benefit be of these processes/strategies?
•

Only deliver safety stock for the first half of the week, and then use midweek
visits to deliver safety stock for the second half of the week based on actual sales
from the first half.
Presently, only 6% of all weekly orders had added quantities beyond what was
originally distributed (127 of 2108). This indicates that the initial distributed
amount is usually sufficient to serve as safety stock for the entire week.
Let X = demand for first half of the week and Y = demand for second half of the
week. When we allocate safety stock for the entire week upfront, we are
protecting against the combined uncertainty of total weekly demand, or allocating
for the Variance of (X+Y) combined.
However, if we already know what the value is for the first half of the week
(during the sales agents’ visits), then there is no uncertainty in the value of X, and

we only have to estimate for Y. Since the total uncertainty in the second half is
less than the uncertainty we face before the week began, the safety stock
required for the second half will always be lower than what we would have
needed had we forecasted the full week in one go.
This is why, by stocking only for the first half of the week upfront and allocating
additional inventory midweek to meet the variance for the second half, we can
expect returns to be lower and sellouts more unlikely. This helps Yedioth lower
costs associated with collecting and transporting surplus magazines from the
retailers, especially if there is not much “seasonality” in sales through the week.
•

Shared safety stock per sales agent. We already know that the required safety
by pooling together the demand of all retailers under the same agent is lower
than preparing safety stocks for each retail store. Rather than allocating safety
stock for each store, Yedioth can allocate safety stock for each agent and train
agents to understand how best to deploy their safety stocks between the stores.

5. What do you think are the organizational challenges that Assaf will have to
address?
•

🚨Change resistance from agents🚨. Sales agents will be worried about the overall
lower safety stock. They may interpret this as an increased risk of missing out on
sales, and therefore missing out on their sales incentives. Assaf will need to
spend considerable time explaining to the agents why the pooling scheme (and
mid-week replenishment scheme) are better. Assaf may also want to think about
introducing incentives to agents for not overstocking.

•

Change resistance from retailers. Likewise, retailers may worry that lower
inventory levels delivered to them might mean an increased risk of missing out on
sales, and therefore missing out on profit.

•

Information management. Optimizing the sales process would require the
company to create a well-functioning information management system that
constantly and accurately informs distribution decisions. This may potentially
pose a challenge for a small business relying on traditional ways of
communication. Furthermore, an information system might be costly and/or
impractical (training/time).

Appendix A (Question 1)

Appendix B (Question 2)

Appendix C (Question 3)

