### Final Grade & Feedback

Q1: 15/15
Q2: 15/15
Q3: 15/15
Q4: 10/15 [No quantitative example provided]
Q5: 10/10
Bonus: 0/10 [Only censoring mentioned, no distribution assumption]

**Total: 65/80**

---

15.778 Introduction to Operations Management
Summer 2025
Yedioth Case assignments by Adetola Adeleke, Josh Cohen, Masakazu Kobayashi
and Assaf Shtalrid
1. In the current distribution model, where each retailer is supplied once a week
independently of all other retailers, what would be a good method to compute
the quantity shipped to each retailer to guarantee that 99% of customers will
be served? Apply your approach to compute recommended quantities to the
50 retailers (explain the methodology in the body of the report and provide the
results in appendix).
We made the following assumptions in our approach:
 We assumed the historical sales data contained in the EXCEL file to be equal
to the historical demand. We recognize the possibility that the demand could
have been higher than the sales numbers when the retailers sold through;
however, considering the data limitations and the fact that the number of soldthrough cases was not significant, we think our assumptions are reasonable
and realistic.
 We assumed that the demand follows a normal distribution.
Based on the above assumptions, our recommended approach is to calculate and
ship the quantity Q for each retailer so that the quantity is sufficient to serve all the
customers with 99% probability. We can solve this by finding quantity Q for each
retailer that satisfies the following formula:
Probability (Sales=<Q)=99%
Given that the Z-value for 99% probability is 2.326, the above formula can be
converted to below:
(Q – Mean of Sales)/Standard Deviation of Sales = 2.326
This then can be converted to:
Q=Mean of Sales + Standard Deviation of Sales*2.326
Using the historical sales data in EXCEL, we can compute the Mean and Standard
Deviation for each retailer across the weeks and derive Q for each retailer. Our
summary result is shown below, while the full results are shown in Appendix I.

SUM of all the retailers
Q at service level 99% (*)
419 🚨correct ~419🚨
Expected Return (**)
214
(*) When calculating the quantity Q, we rounded up the numbers to the nearest
integer because we cannot deliver fraction of magazines
(**) Expected Return = Q at service level 99% - Mean
2. If Yedioth could implement full pooling among all of the 50 retailers what
would be the estimated benefit in terms of total production levels and returns
if the required service level is 99%? (Note: Full pooling means that somehow
all of the retailers could be supplied in-real-time from the same pool of
inventory.)
Implementing full pooling means that Yedioth can calculate the quantity Q based on
the sales numbers aggregating all the retailers for each week. Below is the summary
of the results we obtained by applying the same formula with #1.

Mean
Standard Deviation
Q at service level 99%
Expected Return

SUM of all the
retailers (#1)
205
N.A.
419
214

Full Pooling (#2)
190
20
237 🚨correct pooling🚨
47

Difference
(Benefit)
N.A.
N.A.
183
168

The estimated benefit would be 183 less production and 168 less expected return
compared to the situation where there is no pooling at all (#1).
3. Suppose that one could implement full pooling only among retailers that are
treated by the same sales agent. What would be the potential benefit in terms
of production levels and returns, assuming 99% service level. Compare to
your #2 answer.
Implementing pooling only among retailers that are treated by the same sales agent
means that Yedioth can calculate the quantity Q based on the sales numbers for
each sales agent (aggregating the sales numbers treated by the same sales agent)
for each week. Below is the summary of the results we obtained by applying the
same formula with #1. Our full results are shown in Appendix II.

Mean
Standard Deviation
Q at service level 99%
Expected Return

SUM of all the
retailers (#1)
205
N.A.
419
214

Sales Agent
Pooling (#3)
190
N.A.
293 🚨acceptable agent pooling🚨
103

Difference
(Benefit)
N.A.
N.A.
126
111

Because Yedioth is only able to aggregate quantities on sales agent levels, the
estimated benefits would be less compared to full pooling (#2).
4. Propose more realistic processes/strategies that leverage the fact that the
sales agent visits each retailer in the middle of the week. What would the
benefit be of these processes/strategies?
To begin with, we made below assumptions:
 Given that the sales agent distributes magazines to each retailer, we assume
that pooling among retailers that are treated by the same sales agent, which
we have already discussed in #3, is feasible.
 We note that the production of a second run of magazine is not feasible due
to the high fixed costs, so we assumed that Yedioth has to make all
production decisions ahead of time and distribute magazines to each sales
agent at the beginning of each week.
 We assumed that the demand is not generally concentrated in either of the
first or latter half of the week.
Based on these, our proposal is as below:
1. Calculate quantity Q at service level 99%(the results are already shown in #3)
and distribute magazines to each sales agent.
2. At the beginning of each week, each sales agent calculates quantity Q at service
level 99.9% (as opposed to 99%) for each retailer and distributes half the
amount of that to each retailer.
3. When the sales agent visits each retailer in the middle of the week, calculate the
amount below for each retailer and supply that as an additional supply.
Additional supply amount = actual sales quantity by the middle of the week +
half of the quantity Q at service level 90% - existing stock at the retailer 🚨specific mechanism🚨
By doing this, the sales agents can expect to capture 99.9% of customers demand in
the first half of week, and they can also adjust the distribution quantity for the latter

half of the week depending on the actual results from the first half of the week to
reduce the risk of over-supply.
In addition, the sales agents' midweek visit can provide an opportunity to redistribute
magazines among retailers/vendors based on observed performance for the first
part of the week. If perhaps at the start of the week only 75% of the anticipated
demand is served, and the remaining 25% is kept aside for midweek adjustments
based on this observed performance. ( 25% is the approximate volume of
anticipated returns). The benefit of this would be a more dynamic response to
observations in sales and savings due to a potential reduction in returns if the
system is well run.
Midweek visits can also be used to collect data such as seasonality of demand
within the week, market intelligence, which may affect demand in the coming weeks.
5. What do you think are the organizational challenges that Assaf will have to
address?
We think that the key organizational challenges are below:
 Calculating the optimal service level: Yedioth should recalculate the optimal
service level based on the estimated amount of lost sales and balance this with the
salvage cost, which reduces their overall profit. There is a wide disparity between
when the vendors sell through and when they have returns. Perhaps reducing this
will improve profit margins.
 Convincing Research Department: 🚨multiple stakeholders🚨 Since they are currently deciding on the
printing and shipment quantities, Assaf would need them to understand the
mechanism and benefit of the new method of pooling to optimize production and
inventory management. This may prove difficult due to their long standing history
and traditional ways of doing business.
 Convincing sales agents: It would be challenging to convince sales agents to
because they are compensated based on sales, and optimizing production and
inventory management means foregoing a small number of perceived potential
sales opportunities for the sake of increasing profits. It may be beneficial to adjust
the compensation mechanism of sales agents and incentivize them based on
generated profits in addition to or rather than sales; however, we assume that may
also be a challenging task for Assaf.

 Educating sales agents and retailers: To implement any change to the current
distribution process, Assaf would need to educate the sales agents and retailers
beforehand and make sure they understand the new process and are willing to
support implementing it.
 Incentivize sales agents: It would be beneficial to incentivize sales agents to sell
through the number of magazines supplied to reduce the collection costs of
returned magazines. Yedioth could achieve this by sharing the cost-saving benefits
of fewer returns with the agents. This will drive the agents to find create ways to
obtain information/data that would bring the weekly estimates closer to the actual
demand for each vendor.
 Data Collection: The EXCEL data Assaf collected for 50 retailers is only a small
portion considering that Yedioth has approximately 8,000 retailers network. While it
would be beneficial to collect more data to improve the accuracy of the demand
estimate, it could require significant cooperation from sales agents and/or retailers.
And perhaps deploying a more sophisticated data collection and analysis
mechanism

<Appendix I>

Note) Q is rounded up to the nearest integer
<Appendix II>

Note) Q is rounded up to the nearest integer

