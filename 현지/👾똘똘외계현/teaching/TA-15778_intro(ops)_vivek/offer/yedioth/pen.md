### Final Grade & Feedback

Q1: 15/15
Q2: 15/15
Q3: 15/15
Q4: 10/15 [No quantitative example provided]
Q5: 10/10
Bonus: 0/10

**Total: 65/80**

---

15.778 OPERATIONS MANAGEMENT
Case 2 Yedioth
Team Penguins
Section B

Dmitry Shikhov
Joe Suh
Michael Ben Aharon
Sandra Liu
Shota Furukawa

1.​ In the current distribution model, where each retailer is supplied once (a week)
independently of all other retailers, what would be a good method to compute the
quantity shipped to each retailer to guarantee that 99% of customers will be
served? Apply your approach to compute recommended quantities to the 50
retailers (explain the methodology in the body of the report and provide the
results in appendix).
As magazines are distributed only once a week and not replenished within a week, each
retailer has to manage their own stock level. Therefore, the stocks of magazines at each
retailer must be computed to ensure sufficient stock levels with 99% confidence.

Chart 1-1
As shown in Chart 1-1, each retailer has different expected sales with variance. We
assume that the distribution of sales across retailers conforms to a normal distribution.
Also, given that the dataset is uncensored, we assume that sales in the dataset reflect
both realized and unrealized demand, including lost sales opportunities. Accordingly,
Sell-through is considered to be negligible for the purpose of this analysis. We compute

1

each q* (average sales + safety stock) with the following steps and calculations detailed
in Chart 1-2.
Firstly, we compute the Average Sales μ and the Standard deviation σ of each retailer.
Secondly, we compute Z based on the required confidence level, which is 99% in this
case: Z is 2.33. q* can be calculated by q* =μ + Z⋅σ. As q* is the stock for retailers, q*
should be an integer and should be rounded up. Lastly, we sum up the q* of all retailers,
which is the safety stocks for the entirety of Yedioth's magazine business.
Therefore, the required stock (q*) should be 419 magazines per week. 🚨correct ~419🚨

Chart 1-2
2

2.​ If Yedioth could implement full pooling among all of the 50 retailers what would be
the estimated benefit in terms of total production levels and returns (assume that
the required service level is 99%). Note: Full pooling means that somehow all of
the retailers could be supplied in real time from the same pool of inventory.
In full pooling, we can consider the whole process as one single stock pool and ignore
the variability of each retailer. The required stock (q*) should be determined to cover the
variability of the total number of magazines as a whole system. As shown in Chart 2-1,
the total number of magazines sold per week follows a normal distribution, and the same
calculation as Q1 is applicable.
As shown in Chart 2-2, the required stock q* = μ + Z⋅σ, which is equivalent to 237
magazines per week. 🚨correct pooling🚨 Yedioth should produce this amount to cover the variance, and the
estimated returns will be 47.4 magazines per week, given the expected sales amount is
189.6 magazines per week.
Compared to the retailer model in Q1, the production levels reduction and the returns
reduction are expected to be less, as follows (Chart 2-3):
●​ Production levels reduction: 419 - 237 = 182 magazines per week
●​ Returns reduction: 214.4 - 47.4 = 167 magazines per week

Chart 2-1

Chart 2-2

3

Expected Sales
(1) Mean (μ)

Expected Return
(1) Safety Stock

(1) + (2) Production
(q*)

Original

189.6

102.8

292

Retailer

204.6

214.4

419

Full Pool

189.6

47.4

237

Sales Agent*

189.6

103.4

293

Chart 2-3
3.​ Suppose that one could implement full pooling only among retailers that are
treated by the same sales agent, what would be the potential benefit in terms of
production levels and returns (assume 99% service level). Compare to 2) above.
This solution should be the middle ground between the distribution models in Q1 and Q2
because Yedioth will stock up magazines with the sales agents model, between the full
pool and retailers. As with the Q1 computation, it is required to compute the required
stocks with a 99% confidence level for each sales agent.
Firstly, we need to aggregate the sales by sales agent, and then compute the Average
Sales μ, the Standard deviation σ, and the required stock q* of each sales agent. As in
Q1, q* should also be rounded up, as partial magazines cannot be sold. (Shown in chart
3-1)
As a result, the required stock q* should be 293 magazines per week. 🚨acceptable agent pooling🚨
The impact of production and expected returns compared to the retailer model in Q1 can
be computed as follows.
●​ Production levels reduction: 419 - 293 = 126 magazines per week
●​ Returns reduction: 214.4 - 103.4 = 111 magazines per week
As calculated in Q2, the benefits of the Sales agent model are below.
●​ Production levels reduction: 419 - 237 = 182 magazines per week
●​ Returns reduction: 214.4 - 47.4 = 167 magazines per week
Compared to the full pooling model in Q2, the benefits diminished, while it improves the
production efficiency and reduces returns.

4

Chart 3-1a
4.​ Propose more realistic policies that leverage the fact that the sales agent visits
each retailer in the middle of the week. What would the benefit be of these
policies?
Leveraging the sales agents' mid-week visits for replenishment is a realistic and effective
strategy for Yedioth as it can significantly reduce required inventory levels and improve
overall operational efficiency over Yedioth’s current supply of each retailer only once at
the beginning of the week. Since sales agents already visit retailers mid-week, we can
use this visit to deliver additional inventory: one forecasted at the start of the week, and
another based on updated sales information gathered mid-week.
Replenishing mid-week helps absorb sales variability and enables a reduction in safety
stock as a whole. Hence, this can also reduce the return rate (currently at 36%).
Realistically, Yedioth can apply the stock pooling at the sales agent level (system in Q3)
and ask them to replenish in the middle of the week. 🚨specific mechanisms🚨 This reduces the uncertainty in
each forecast because the standard deviation of demand increases with the length of the
forecast period, with shorter forecast intervals leading to lower demand variability. The
Newsvendor model accounts for this variability when determining optimal stock levels, so
less variability means we need less safety stock to achieve the same 99% service level.
This approach also delivers several additional benefits:
●​ Lower return rates: Fewer unsold magazines need collection and scrapping,
reducing waste and reverse logistics costs.​
●​ Lower production levels: Less safety stock is required upfront, so printing large
buffer quantities to cover weekly uncertainty is no longer necessary.​
●​ Improved data quality: Mid-week visits generate uncensored demand data,
improving forecasts and enabling better initial shipment planning in future weeks.​

5

●​ Revenue protection: Topping up stock mid-week minimizes stock-outs,
protecting advertising-driven revenue and aligning with sales agents’ incentives.​
●​ Retailer relationships: Proactive replenishment strengthens partnerships with
retailers by ensuring consistent availability and responsiveness.
Moreover, these improvements free up printing capacity for other business and
revenue-generating opportunities. We can enhance this approach further by combining it
with sales agent-level pooling. Pooling reduces variability across retailers within each
agent’s group, and mid-week replenishment allows us to refine stock decisions using
real-time data. These strategies create a responsive, efficient system leveraging existing
infrastructure without the need to adopt the greater complexity of full central pooling.
5.​ What do you think are the organizational challenges that Assaf will have to
address?
Assaf faces significant organizational challenges 🚨multiple stakeholders🚨 as he works to implement changes that
go against Yedioth's long-standing practices and culture of overproduction. A key
obstacle is overcoming resistance from sales agents and retailers. Sales agents are
currently compensated based on sales volume, which creates a strong incentive to
oversupply in order to ensure every potential sale is covered. For both agents and
retailers, the perceived cost of understocking is much higher than the cost of
overstocking, so Assaf must revisit the salary and incentive structures to encourage
minimizing returns and accepting occasional opportunity loss in the case of unexpected
demand spikes. This could include redesigning compensation schemes to better balance
the costs of understocking and overstocking. Since Yedioth provides full refunds for
unsold inventory and bears the cost of scrapping, retailers and agents currently have
little financial risk or “skin in the game,” reinforcing their tendency to over-order.
Assaf should promote mid-week replenishment as a realistic and efficient solution.
Adjusting inventory mid-week based on updated sales information allows Yedioth to
reduce safety stock, decrease total production, and lower return volumes. Implementing
technologies such as EDI for larger retailers and RFID or smart stands for smaller ones
can support this transition by providing timely sales data and improving forecast
accuracy. However, for these tools to have impact, sales agents and retailers must be
empowered not just to report demand but to actively adjust inventory levels in response.
In parallel, Assaf should reassess the current 99% service level target. Because the
relationship between service level and safety stock is non-linear, even a small reduction
in the target service level can yield a disproportionately large drop in required safety
stock and overall costs. Combined with changes to incentive structures, optimizing the
service level can help align operational targets with the true cost trade-offs of
understocking versus overstocking.

6

Another organizational challenge lies with the Research Department, which sets
shipment quantities. Their bias toward overproduction is driven by fear of lost sales and
the difficulty of forecasting demand accurately, especially when true demand is hidden
by censored data during frequent stockouts. This instinct to oversupply is reinforced
because sell-through events often mask unmet demand, prompting them to inflate
quantities as a precaution.
When comparing models, the full pooling scenario stands out as the optimal target. It
maintains the same expected sales as the current system but achieves them with
significantly lower production levels and fewer returns, resulting in a substantial
improvement in costs. If partial pooling by a sales agent produces results similar to the
current system, it highlights that this approach alone delivers little variance reduction,
making mid-week replenishment or a move toward fuller pooling essential to capture
meaningful benefits. To gain buy-in across the organization, Assaf must communicate
the operational and financial benefits of these changes clearly and with data.
Demonstrating how reduced production and lower returns can free up printing capacity
and improve overall company costs will be critical (i.e., by conveying the calculations and
strategies demonstrated above).

7

