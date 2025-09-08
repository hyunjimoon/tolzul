### Final Grade & Feedback

Q1: 15/15
Q2: 15/15
Q3: 15/15
Q4: 10/15 [No quantitative example provided]
Q5: 10/10
Bonus: 0/10

**Total: 65/80**

---

Yedioth Case
James Wu, Ujjal Dutta, Kosuke Kodera, Zodwa Mlangeni
Question 1
Approach:
We are using the Newsvendor Model to determine the optimal quantity to ship to each
retailer to achieve a 99% in-stock probability. The Newsvendor formula is:
Q=μ +Kxσ
Where:
●

Μ = Mean weekly sales for the retailer

●

σ = Standard deviation of sales

●

K= Z table value for the required service level (for 99%, z=2.326)

Steps:
1. For each retailer, calculate the weekly average and standard deviation of sales.
2. Apply the Newsvendor formula to determine the recommended quantity.
3. Round up results to the nearest whole number.
4. Sum up the outputs per customer.
Assumption:
We assume the sell-throughs are minimal and that suppressed demand is minimised.
Result:
Based on our calculations, we recommend 419 quantities to be provided to the 50
retailers based on the current distribution model. 🚨correct ~419🚨

Yedioth Case
James Wu, Ujjal Dutta, Kosuke Kodera, Zodwa Mlangeni
Question 2: Benefits of Full Pooling Across All Retailers (50 Retailers)
To determine the benefit of full pooling, we followed the process below:
Assumption:
All 50 retailers can be served in real-time from a central inventory pool.
Method:
1. Calculate the overall mean and standard deviation of all sales across all retailers by
date.
2. Use Newsvendor formula to determine pooled recommended quantity per retailer by
date.
3. Multiply by the number of retailers to estimate total production per day.
4. Compare the result to current average production and return levels per day.
Results:
●

Total Production (Full Pooling):

237 magazines/week 🚨correct pooling🚨

●

Estimated Returns (Full Pooling):

47 magazines/week

●

Current Total Production:

419 magazines/week

●

Current Estimated Returns:

111 magazines/week

Interpretation: Based on our calculations above, we have determined that full pooling
method has decreased both the production run and estimated returns by 182 and 64
respectively.

The reduction in estimated returns is particularly significant as returns have a very high
cost to Yedioth.

Yedioth Case
James Wu, Ujjal Dutta, Kosuke Kodera, Zodwa Mlangeni
Question 3: Partial Pooling by Sales Agent
To determine the potential benefit in terms of production levels and returns to 99%
service for a system that pools by retailers serviced by the same sales agent vs the full
pooling system above in question 2, we followed the process below.
Assumption: Pooling is only possible among retailers managed by the same sales agent.
Method:
1. Group retailers by sales agent by date.
2. For each group, compute mean, std dev, count.
3. Apply Newsvendor model at the group level by date.
4. Aggregate recommended quantities.
Results:
●

Total Production (Partial Pooling):

293 magazines/week 🚨acceptable agent pooling🚨

●

Estimated Returns (Partial Pooling):

103 magazines/week

●

Total Production (Full Pooling):

237 magazines/week

●

Estimated Returns (Full Pooling):

47 magazines/week

Comparison to Full Pooling (Q2):
In comparison to full pooling as calculated in question 2 above, partial pooling by
retailers serviced by the same sales agent yields higher production runs and higher
returns which are both 56 units higher, costing Yedioth more.

Yedioth Case
James Wu, Ujjal Dutta, Kosuke Kodera, Zodwa Mlangeni
Question 4: Realistic Mid-Week Replenishment Strategies
Proposal A: Mid-Week Replenishment Using Sales Agent Visit
●

The sales agents already visit retailer’s mid-week (Wednesday).

●

Potential strategy: We could allocate a certain percentage based on further
analytical simulation based on the cost of under and over stocking. For example, we
could recommend allocating only 60% of expected demand at the start of the week.
Then, based on observed sales in the first half example, we replenish the remaining
40% during the mid-week visit.

Benefits:
●

Reduction in initial overproduction and returns.

●

This method allows actual demand signals to drive second-half replenishment.

●

This method also spreads production capacity and aligns with available sales data
provided that the fixed costs can be covered by the first production run.

Proposal B: Predictive Reallocation Based on First-Half Sales
●

We could use early-week sales data to infer total weekly demand using a narrower
standard normal bell shape.

●

We could then reallocate the remaining inventory among nearby retailers.

This method would require technological support such as
-

leveraging EDI with large chains to get real-time inventory data; and
Using RFID/smart stands at select kiosks to track real-time sales

but this could become very expensive for Yedioth.
EDI data from the large chains would help Yedioth predict the mid-week demand
better. This would allow the sales agents to prepare for mid-week sales quantities
based on real-time analytical sales insights from the market. This proposal would
take advantage of weeks with higher news cycle weeks, for example US tariff
introductions, driving higher demand and therefore sales for Yedioth.
Benefit:
This approach can potentially reduce return rates, while maintaining the required 99%
service levels. By taking this approach, Yedioth can expect a reduced production number
between 237 -293 units which is calculated in question 2 and 3. The corresponding
returns would be between 47 and 103.

Yedioth Case
James Wu, Ujjal Dutta, Kosuke Kodera, Zodwa Mlangeni
Question 5: Organizational Challenges for Assaf
1. Cultural Resistance


Yedioth is a conservative, family-run business and it is probable that any
organisational changes will face significant resistance from the family unit and
long serving employees as the “we’ve always done it this way successfully”
mentality may be pervasive.



Any data-driven or tech-based change may face resistance from traditionalists
from the family unit and long-serving and trusted employees. Salespeople could
also fear losing their jobs.

2. Incentive Misalignment


Sales agents are paid based on gross sales and therefore incentivized to push for
higher sales volume at the detriment of production and inventory efficiency and
cost management.



Reduction in shipment quantities may appear as a personal loss to sales agents
and retailers unless compensation schemes are redesigned for these two groups.

3. Buy-in from Research and Distribution Teams


These teams will have to accept changes to shipment models and integrate
analytics into forecasting which goes against what they have done historically.

4. IT and Infrastructure Barriers




Most small kiosks lack EDI or inventory systems.
Smart stands and RFID deployment may not be scalable or cost-effective.
The IT infrastructure required EDI/RFID requires significant investment which we
envision would be difficult for Assaf to convince the internal team.

5. Coordination Across Silos



Replenishment requires tight integration between forecasting, sales agents, and
logistics.
Ensuring that the forecasts based on mid-week data are accurate and reliable to
avoid inventory mismanagement.

6. New System Implementation Risk


Under-quantified demand data due to miscalculation could increase lost sales or
dissatisfaction with retailers.

