### Final Grade & Feedback
Q1: 15/15
Q2: 15/15  
Q3: 15/15
Q4: 15/15
Q5: 10/10
Bonus: 0/10
**Total: 70/80**

Yedioth Case Report
Rhinos: Sho Akama, Jack Barry, Shira Rotem Kaftzan, Alex Salazar, Cristina
Sunley

1. In the current distribution model, where each retailer is supplied once,
independently of all other retailers. What would be a good method to compute
the quantity shipped to each retailer if one wishes to guarantee that 99% of
customers will be served? Apply your approach to compute recommended
quantities to the 50 retailers (explain the methodology in the body of the report
and provide the results in appendix).
Methodology:

We applied the Newsvendor model, treating each retailer’s weekly demand as a
normally distributed random variable, and used historical sales data to estimate:
•
•
•

μ = average weekly sales for each retailer
σ = standard deviation of weekly sales for each retailer
k = the z-score corresponding to a 99% in-stock probability

For each retailer i, let D(i) the past sales for each retailer(customer).
·

i={1,2,3,…,50}

If D(i) follow the normal distribution D(i)~N(μ(i),σ(i)), then optimal quantities to
distribute will follow this formula: q*(i) =μ(i)+k x σ(i). This quantity (q*) minimizes the
expected cost of understocking and overstocking, given the 99% service level. We
applied this formula across the 50 pilot retailers.
We computed μ(i) (mean of sum of sales per week for each retailer) and σ(i) (standard
deviation for sum of sales per week for each retailer) for all the retailer’s past data and
insert it to the formula above.
Since we are computing the quantity shipped to each retailer to guarantee 99% of the
customers, k would be 2.32.
Recommended Q for all 50 retailers at 99% service level is 🚨419🚨 (Roundup the calculated
number for each week and then added together).

(See Appendix and attached xls for the calculations and outcomes)

2. If Yedioth could implement full pooling among all of the 50 retailers what
would be the estimated benefit in terms of total production levels and returns
(assume that the required service level is 99%). Note: Full pooling means that
somehow all of the retailers could be supplied in real time from the same pool of
inventory.
We next evaluated whether pooling demand across retailers could lead to inventory
efficiency gains.
Methodology
We modeled full pooling using again the Newsvendor framework, this time treating
the combined demand across all 50 retailers as a single random variable.
•
•
•

μ pooled= ∑μ i , the mean of the pooled demand
σ = standard deviation of the pooled demand
k = the z-score corresponding to a 99% in-stock probability, i.e. 2.32

Recommended pooled Q for all 50 retailers at 99% service level is 🚨236🚨.

If Yedioth could implement full pooling, treating all 50 retailers as a single, centrally
managed inventory pool with real-time replenishment, the company could unlock
significant operational efficiencies. The benefit Yedioth can get will be 183. Still, this
could be operationally complex to implement.

Print Production
Return (Subtract
estimated
demand from Q)

Current
Operation
(From Q1)
419 per week
230 per week

With Pooling
(service level 99%)
236 per week
(mean=189.6 per
week, STD=20)
47 per week

Benefit in terms of total
production levels and
return
183 (=419 - 236), i.e.
aprox 43% reduction in
optimum Q
183 (=230 - 47)

Benefit of Return decrease
= (Production from Q1 - Estimated Demand) - (Production from Q2 - Estimated
demand) = (Production Q from Q1) - (Production Q from Q2)
= Benefit of Production decrease
(See Appendix and attached xls for the calculations and outcomes)

3. Suppose that one could implement full pooling only among retailers that are
treated by the same sales agent, what would be the potential benefit in terms of
production levels and returns (assume 99% service level). Compare to 2) above.
We evaluated whether pooling demand across retailers treated by the same sales
agent could lead to inventory efficiency gains.
Methodology:

•
•
•

We grouped retailers by Sales Agent ID
We aggregated their weekly demand and recalculated mean (μ) and standard
deviation (σ) of the pooled demand for each agent
We then re-applied the Newsvendor model using the same service level (99%)
to find the optimal pooled inventory for each group of retailers

Findings:

Roundup
Avearge Sales/
Total Sales
week (46 weeks
Agent
/Agent
considered)
1
2
3
4
5
6
7
8
9
10

1032
728
589
810
1290
1020
516
720
1287
729

22.43
15.83
12.80
17.61
28.04
22.17
11.22
15.65
27.98
15.85

K
2.32
2.32
2.32
2.32
2.32
2.32
2.32
2.32
2.32
2.32

Final Q at
StdDev of Q at 99%
99% service
Sales
service level
level
5.18
3.96
2.80
3.38
6.38
4.32
2.50
3.31
5.70
4.11

34.44
25.02
19.30
25.46
42.85
32.19
17.02
23.34
41.21
25.39
286.23

35.00
26.00
20.00
26.00
43.00
33.00
18.00
24.00
42.00
26.00
293

Recommended Q across all 50 retailers pooled by sales agent at 99% service level is 🚨293🚨.

Compared to Q1: optimal production in the agent pool scenario is 293 which is lower
than the optimal production of 419 in the individual pool scenario (126 reduction per
week)
Compared to Q2: optimal production in the agent pool scenario is 293 which is higher
than the optimal production of 236 in full pooling scenario (57 addition per week)

Current Operation
(From Q1)
Print
Production

419 per week

With Pooling with
Retailer (From Q2)
236 per week

With Pooling between
the same Sales Agent
(From Q3)
293 per week

With lower optimal production levels we will have lower return levels.
While not as powerful as full pooling, partial pooling by agent captures a significant
portion of the benefit. It is also much more realistic to implement operationally, given
the shared oversight by the agent, geographic proximity of retailers and opportunity
for midweek adjustments based on localized observations.
(See attached xls for the calculations and outcomes)

4. Propose more realistic policies that leverage the fact that the sales agent visits
each retailer in the middle of the week. What would the benefit be of these
policies?
Most efficient policies will be full network pooling but, based on the limitations on
reality, we would propose the policies below:
1. Two-stage replenishment:
Set Sunday service level around 90% with top up on Wednesday based on actual
weekly demand.
Example:
Let’s say Retailer #2 usually sells 5 copies/week with σ = 2
In the current model (1-shot delivery at 99% service level) this retailer gets 10 copies
on Monday.
In the two-stage model:

On Sunday, the retailer will get just enough for 90% service level (z = 1.28), which is 8
copies.
On Wednesday, if sales are high (say they already sold 7 copies), replenish this
retailer with +2 copies.
Benefit:
•
•
•
•

Use real-time signals to forecast demand
Initial print is lower
Only some retailers will need replenishment and that’s where we get the
efficiency and savings
Reduce over-ordering for low-demand weeks

2. Collect-and-shift:
Start the week with a 99% target service level and during the mid-week visit, the agent
pulls unsold copies from slow sellers and 🚨shifts them to hot sellers🚨 on the same
route. No extra printing unless the route stock is exhausted.
Example:
Retailer #10 got 6 copies on Sunday and sold 4 copies by Wednesday.
Forecast total weekly demand by the fraction of the week: Predicted sales = 7
Retailer #9 got 8 copies on Sunday (based on previous demand), but by Wednesday
only sold 4 copies. Their expected weekly demand will be 6 (based on the assumption
that by Wednesday they sold %60 of the copies for the entire week’s demand).
Take 2 copies from retailer #9 and shift them to retailer #10.
Benefit:
•
•
•

Use real-time signals to forecast demand
Reduce stockouts for unexpectedly high demand
Less waste and returns with similar customer service level

5. What do you think are the organizational challenges that Assaf will have to
address?
Assaf would need to address the following organizational challenges:
1. 🚨Sales Agent incentives misaligned🚨 with efficiency => consider realigning
incentives for sales agents. Currently, sales agents are compensated based on units
sold, not profitability or return minimization; they have therefore no incentive to
reduce shipment or minimize returns. For a sales agent, a stock out is the worst
possible scenario. As a result, there is a gap between organizational incentives and
sales agent incentives, which creates inefficiency in the ordering process. We
recommend reshaping sales agent compensation to reward low quantity returned
and stockout situations.
2. Cultural resistance to change => Assaf will have to address the old-school culture
of preferring overproduction to stockouts. This method of thinking wasn’t as
damaging historically, but in the digital era and low margins, Yedioth must change
their priorities and make efficiency a non-negotiable, or they could risk going out of
business.
3. Lack of digital capabilities => Consider implementing low-tech standardized paper
tracking procedures so that data is still reliably collected even for retailers with no
technological capabilities. This will ensure quality information is used to inform
production levels.

Appendix

Retailer
number
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50

（Result of Question1）

Average
of Sales
4.27
5.45
1.61
1.80
3.09
3.61
3.93
14.43
4.73
3.17
4.00
4.07
2.24
2.46
4.56
6.52
4.78
1.86
5.85
3.25
2.78
4.20
5.14
1.57
8.74
3.15
2.16
6.65
1.94
8.00
4.80
2.59
3.67
2.22
3.95
2.67
3.61
3.40
3.04
9.07
3.70
3.74
3.07
3.38
1.48
6.35
5.51
1.43
2.93
4.00

q*(i) =μ(i)+k x σ(i) Roundup
K at 99%
StdDev of Q at 99% service Final Q at 99%
service
Sales
level
service level
level
2.32
1.76
8.36
9
2.32
1.94
9.95
10
2.32
0.74
3.34
4
2.32
1.19
4.55
5
2.32
1.46
6.47
7
2.32
1.73
7.63
8
2.32
1.60
7.65
8
2.32
3.91
23.51
24
2.32
1.62
8.48
9
2.32
1.37
6.36
7
2.32
1.86
8.32
9
2.32
1.01
6.41
7
2.32
1.11
4.82
5
2.32
1.13
5.08
6
2.32
1.58
8.23
9
2.32
2.01
11.18
12
2.32
1.70
8.72
9
2.32
0.80
3.73
4
2.32
1.76
9.94
10
2.32
1.74
7.29
8
2.32
1.01
5.12
6
2.32
2.15
9.17
10
2.32
2.10
10.00
11
2.32
1.15
4.23
5
2.32
2.39
14.28
15
2.32
1.48
6.57
7
2.32
1.70
6.11
7
2.32
3.11
13.86
14
2.32
1.26
4.86
5
2.32
2.68
14.23
15
2.32
1.94
9.30
10
2.32
1.24
5.46
6
2.32
1.61
7.40
8
2.32
1.30
5.23
6
2.32
1.66
7.81
8
2.32
1.55
6.27
7
2.32
1.58
7.28
8
2.32
1.08
5.92
6
2.32
1.41
6.32
7
2.32
2.51
14.88
15
2.32
1.47
7.11
8
2.32
2.09
8.59
9
2.32
1.47
6.47
7
2.32
0.92
5.50
6
2.32
0.94
3.65
4
2.32
1.92
10.81
11
2.32
2.03
10.21
11
2.32
1.07
3.90
4
2.32
1.27
5.87
6
2.32
1.22
6.84
7
393.30
419
Recommended Q to be shipped at 99% service level

(Result for Question2)

Week
2008/07/14
2008/07/21
2008/07/28
2008/08/11
2008/08/18
2008/08/25
2008/09/01
2008/09/15
2008/09/21
2008/10/27
2008/11/10
2008/11/17
2008/11/24
2008/12/08
2008/12/15
2008/12/22
2009/01/05
2009/01/12
2009/01/19
2009/01/26
2009/02/09
2009/02/16
2009/02/23
2009/03/09
2009/03/16
2009/04/20
2009/05/11
2009/05/18
2009/06/08
2009/06/15
2009/06/22
2009/06/29
2009/07/13
2009/07/20
2009/07/27
2009/08/10
2009/08/17
2009/08/24
2009/08/31
2009/10/12
2009/10/19
2009/10/26
2009/11/09
2009/11/16
2009/11/23
2009/11/30
Grand Total

Estimated
Demand
170
143
173
175
172
158
192
215
199
181
184
198
181
181
201
192
208
180
197
185
186
232
207
206
165
192
201
208
177
179
188
183
238
216
198
189
193
181
195
242
184
189
184
148
184
171
8721
189.6

Each Retailer pooling(Q1)
Production
q*
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
419.0
19274.0
419.0

Returns
249.0
276.0
246.0
244.0
247.0
261.0
227.0
204.0
220.0
238.0
235.0
221.0
238.0
238.0
218.0
227.0
211.0
239.0
222.0
234.0
233.0
187.0
212.0
213.0
254.0
227.0
218.0
211.0
242.0
240.0
231.0
236.0
181.0
203.0
221.0
230.0
226.0
238.0
224.0
177.0
235.0
230.0
235.0
271.0
235.0
248.0
10553.0
229.4

With full pooling
Production
q*
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
236.0
10854.2
236.0

Returns
66.0
93.0
63.0
61.0
64.0
78.0
44.0
21.0
37.0
55.0
52.0
38.0
55.0
55.0
35.0
44.0
28.0
56.0
39.0
51.0
50.0
4.0
29.0
30.0
71.0
44.0
35.0
28.0
59.0
57.0
48.0
53.0
-2.0
20.0
38.0
47.0
43.0
55.0
41.0
-6.0
52.0
47.0
52.0
88.0
52.0
65.0
2133.2
46.4

