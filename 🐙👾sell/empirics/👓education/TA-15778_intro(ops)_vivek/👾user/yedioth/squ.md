### Final Grade & Feedback
Q1: 15/15
Q2: 15/15
Q3: 15/15
Q4: 15/15
Q5: 10/10
Bonus: 0/10 [Only censoring mentioned, no distribution assumption]
**Total: 70/80**

Case Report: The Yedioth Group
Group Squirrels
Victor Dong, Yash Jain, Ayaka Tomono, Gursimran Rooprai

August 1, 2025
Questions:
1. In the current distribution model, where each retailer is supplied once a week
independently of all other retailers, what would be a good method to compute the
quantity shipped to each retailer to guarantee that 99% of customers will be served?
Apply your approach to compute recommended quantities to the 50 retailers (explain
the methodology in the body of the report and provide the results in appendix).
2. If Yedioth could implement full pooling among all of the 50 retailers what would be
the estimated benefit in terms of total production levels and returns if the required
service level is 99%? (Note: Full pooling means that somehow all of the retailers could
be supplied in-real-time from the same pool of inventory.)
3. Suppose that one could implement full pooling only among retailers that are treated
by the same sales agent. What would be the potential benefit in terms of production
levels and returns, assuming 99% service level. Compare to your #2 answer.
4. Propose more realistic processes/strategies that leverage the fact that the sales agent
visits each retailer in the middle of the week. What would the benefit be of these
processes/strategies?
5. What do you think are the organizational challenges that Assaf will have to address?
Solutions:
1. In the existing distribution model, each retailer receives a single weekly shipment
without real-time adjustments. For each retailer i, the optimal shipment quantity is
calculated as: Q𝑖 = μ𝑖 + 𝑘 ∗ σ𝑖 , where:
• μi is the average weekly demand at retailer i
• σi is the standard deviation of weekly demand
• k = 2.33 is the z-score corresponding to a 99% service level
We assumed the demand follows a normal distribution, sell-throughs are minimal and
suppressed demand is minimized for the set of Questions.
Using the actual data from the 50 retailers, we computed these parameters and found
the total recommended supply to be: ∑50
𝑖=1 Q 𝑖 = 419
In the current model, each retailer is planned independently using the Newsvendor
formula to achieve a 99% service level. This means supplying the average weekly
demand plus a safety buffer based on individual variability. Applied across 50 retailers,
this approach results in a total of 419 magazines. While simple and reliable, it leads to
high overstock and returns, as it does not take advantage of any risk pooling or demand
aggregation. See Appendix (Table 1) for complete calculations. We expect that due to
uncensored demand, the resulting Q value will be higher.
2. If Yedioth could serve all 50 retailers from a single shared inventory pool and replenish
in real time, demand variability would decrease due to aggregation. The pooled demand
statistics are:

Group Squirrel

1

1 August 2025

50

μ 𝑇𝑜𝑡𝑎𝑙 = ∑50
𝑖=1 μ𝑖 and σ 𝑇𝑜𝑡𝑎𝑙 = (∑𝑖=1 σ𝑖 ) ^ 0.5
Q𝐹𝑢𝑙𝑙 𝑃𝑜𝑜𝑙𝑖𝑛𝑔 = μ 𝑇𝑜𝑡𝑎𝑙 + 𝑘 ∗ σ𝑇𝑜𝑡𝑎𝑙 , Q𝐹𝑢𝑙𝑙 𝑃𝑜𝑜𝑙𝑖𝑛𝑔 = 252
To summarize, full pooling reduces the required weekly supply from 419 to 252 units,
representing a decrease of 167 magazines or 39.9%. This significant drop demonstrates
the efficiency gains from aggregating demand across all 50 retailers and managing
safety stock centrally. By smoothing out individual demand fluctuations, Yedioth can
maintain the same 99% service level with far less overproduction. In addition to
lowering printing and distribution costs, this approach would dramatically reduce the
volume of unsold returns. However, achieving such a model would demand real-time
sales visibility, responsive logistics, and integrated coordination, capabilities that
Yedioth’s current infrastructure does not support. As such, while full pooling offers
the greatest potential for optimization, it remains a strategic objective rather than an
immediate operational option. See Appendix (Table 2) for complete calculations.
Without normalization to 50 retailers, applying the Newsvendor formula at the pooled
level, the total production quantity drops to 237 units, achieving the same 99% service
level with a 43% reduction in total supply compared to the independent model. See
Appendix (Table 2*) for complete calculations.
3. If full pooling is impractical, partial pooling can be done by grouping retailers under
each sales agent. We proceed by applying the same Newsvendor logic at the agent
group level, aggregating demand and variability within each cluster. Each agent's group
was treated as a mini-pooled unit, and recommended quantities were calculated per
agent. The sum across all agents was:
Q𝑃𝑎𝑟𝑡𝑖𝑎𝑙 𝑃𝑜𝑜𝑙𝑖𝑛𝑔 = μ𝑃𝑎𝑟𝑡𝑖𝑎𝑙 + 𝑧 ∗ σ𝑃𝑎𝑟𝑡𝑖𝑎𝑙 and Q𝑃𝑎𝑟𝑡𝑖𝑎𝑙 𝑃𝑜𝑜𝑙𝑖𝑛𝑔 = 308
If full pooling across all retailers is not feasible, Yedioth can implement partial pooling
by grouping retailers under each sales agent. In this model, demand is aggregated within
each agent’s territory, allowing the use of a pooled safety stock buffer per group. We
summed the average demands and combining variances within each group. When the
recommended quantities for all agent groups are totaled, the required production drops
to 308 magazines, compared to 419 in the independent model. This represents a
reduction of 26.5%, offering a substantial improvement over the baseline, though not
as efficient as full pooling, which requires only 252 units. Partial pooling thus strikes
a practical balance between operational feasibility and inventory efficiency. See
Appendix
(Table
3)
for
complete
calculations.
Without normalization to 50 retailers, the resulting total required quantity was 293
units. See Appendix (Table 3*) for complete calculations.
4. Three strategies are proposed further:
Proposal #A: Two-Stage Replenishment (Implemented)
• Initial delivery on Sunday (70% of forecasted demand, lower z-score). Mid-week
replenishment on Wednesday, based on sales progress observed by the sales agent
• Quantities are computed with adjusted service levels to account for split risk (e.g.,
z = 1.04 for Sunday, z = 1.28 for Wednesday)
Total weekly supply under this model was 266 units, achieving the same 99%
service level with a 36.5% reduction from the current model. This model requires no
daily sales data, is operationally simple, and leverages existing sales agent visits
effectively.

Group Squirrel

2

1 August 2025

Proposal #B: Rather than delivering the full weekly quantity on Sunday, the company
can split deliveries into:
• First shipment on Sunday to cover early-week demand
• Second shipment on Wednesday, based on actual sales observed by the sales agent
• This approach reduces inventory risk by splitting the demand coverage into two
parts, each with its own service level target. The key is to test and optimize the
safety stock levels (z-scores) for both deliveries such that the combined weekly
service level still reaches 99%, while minimizing total supply.
Let:
• z1 be the z-score for the Sunday delivery (covering 70% of demand)
• z2 be the z-score for the Wednesday delivery (covering the remaining 30%)
We aim to find z1 and z2 such that the combined service level is 99% and the total
safety stock is minimized. The combined service level can be expressed as:
1−(1−Φ(z1)) * (1−Φ(z2)) = 0.99
We solved this equation and found the optimal combination that minimizes
total Safety Stock = z1 * σ1 + z2 * σ2
Assuming demand splits as:
• σ1 = 0.7 (first 70% of weekly standard deviation)
• σ2 = 0.3 (last 30%)
We found:
• z₁ = 0.50 → service level ≈ 69.1%
• z₂ = 1.85 → service level ≈ 96.8%
The minimum total safety stock (normalized): 0.50⋅0.7+1.85⋅0.3 = 0.9039
To summarize, by adopting a two-stage replenishment strategy, Yedioth can
significantly reduce overall inventory levels while still meeting the weekly 99% service
target. Instead of delivering the full weekly quantity at once with a high safety buffer,
the demand is divided into two parts. The first shipment covers early-week demand
with a lower service level, while the second shipment adjusts based on actual sales
observed mid-week. Through z-score optimization, we found that setting the first
delivery to cover ~69% of likely demand and the second to cover about 97% of the
remaining need achieves the same overall service level. This method shows that it is
more efficient to share the service level requirement between two deliveries rather than
applying a high buffer upfront (99% service level), ultimately reducing safety stock and
improving inventory efficiency without sacrificing availability.
Strategy #C: Predictive Replenishment Using First-Half Sales (Future Option)
In a more advanced operational model, Yedioth could leverage sales data from the
first half of the week (Sunday–Tuesday) to predict second-half demand
(Wednesday–Saturday) using statistical modeling (e.g., linear regression).
Model Concept:
• Weekly demand is split as:
Weekly Sales=H1 Sales (Sun–Tue)+H2 Sales (Wed–Sat)
• Predictive model: H2=α+β⋅H1+ϵ
• Replenishment on Wednesday is based on this forecast, adjusted with a safety
factor to maintain the 99% service level.
Key Requirement: Infrastructure Investment
Implementing Proposal #C requires overcoming several systemic limitations in the
current organization:

Group Squirrel

3

1 August 2025

Challenge
Lack of daily sales
visibility
Data collection lag

Requirement
Deployment of POS systems or mobile reporting
tools at the retailer or sales agent level
Near-real-time data transmission from retailers or
agents
Limited
analytics
Development of internal capabilities for forecasting
capacity
models and inventory algorithms
While Proposal #C has the potential to deliver similar or even better efficiency than
Proposal #A, it relies heavily on the accuracy of the predictive model and the timely
availability of daily sales data. Therefore Proposal #C is not immediately
implementable under the current system but represents a valuable long-term
opportunity if paired with targeted investments in IT, analytics, and process
digitization.
5. Organization challenges for implementation:
Assaf will face several cross-functional and cultural challenges:
Area
Challenge
Sales agents are currently rewarded for volume shipped.
Incentives
Moving to a returns-based or profit-based incentive model is
essential.
The industry is conservative; over-supplying to avoid
Culture
stockouts is ingrained. Shifting toward lean, data-driven
distribution will face resistance.
Proposal #C requires infrastructure to capture daily sales,
Data & IT
which does not currently exist. Investment in POS or mobile
tools is needed.
Collaboration across sales, logistics, IT, and planning teams
Coordination
must be strengthened for implementation to succeed.
We recommend:
• Immediately implement Proposal #A (two-stage replenishment), as it is lowcost, impactful, and feasible with current systems.
• Preparing for Proposal #C by investing in data infrastructure, aligning incentives,
and initiating pilot testing.
• Continuing to evaluate pooling opportunities within realistic operational units (e.g.,
by sales agent) to further optimize production and reduce returns.
This phased strategy allows Yedioth to capture meaningful cost savings now while
building the foundation for longer-term transformation.

Group Squirrel

4

1 August 2025

Appendix:
Table 1: Current distribution model
Customer #
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

Group Squirrel

Sales
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

SD
1.76
1.94
0.74
1.19
1.46
1.73
1.60
3.91
1.62
1.37
1.86
1.01
1.11
1.13
1.58
2.01
1.70
0.80
1.76
1.74
1.01
2.15
2.10
1.15
2.39
1.48
1.70
3.11
1.26
2.68
1.94
1.24
1.61
1.30
1.66
1.55
1.58
1.08
1.41
2.51

k
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33

Q
9.00
10.00
4.00
5.00
7.00
8.00
8.00
24.00
9.00
7.00
9.00
7.00
5.00
6.00
9.00
12.00
9.00
4.00
10.00
8.00
6.00
10.00
11.00
5.00
15.00
7.00
7.00
14.00
5.00
15.00
10.00
6.00
8.00
6.00
8.00
7.00
8.00
6.00
7.00
15.00

5

1 August 2025

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
Grand Total

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

1.47
2.09
1.47
0.92
0.94
1.92
2.03
1.07
1.27
1.22

2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33
2.33

8.00
9.00
7.00
6.00
4.00
11.00
11.00
4.00
6.00
7.00
419.00

Table 2: Pooled distribution model (Normalization to 50 retailers)
Date
14/07/2008
21/07/2008
28/07/2008
11/08/2008
18/08/2008
25/08/2008
01/09/2008
15/09/2008
21/09/2008
27/10/2008
10/11/2008
17/11/2008
24/11/2008
08/12/2008
15/12/2008
22/12/2008
05/01/2009
12/01/2009
19/01/2009
26/01/2009
09/02/2009
16/02/2009
23/02/2009
09/03/2009
16/03/2009
20/04/2009
11/05/2009
18/05/2009

Group Squirrel

Sales
4.05
3.40
4.12
4.07
3.91
3.51
4.17
4.67
4.15
3.77
3.83
4.13
3.77
3.77
4.19
4.00
4.33
3.75
4.10
3.94
3.96
4.83
4.31
4.29
3.44
4.00
4.47
4.52

Sales (Normalized)
203.00
171.00
206.00
204.00
196.00
176.00
209.00
234.00
208.00
189.00
192.00
207.00
189.00
189.00
210.00
200.00
217.00
188.00
206.00
197.00
198.00
242.00
216.00
215.00
172.00
200.00
224.00
227.00

6

1 August 2025

08/06/2009
15/06/2009
22/06/2009
29/06/2009
13/07/2009
20/07/2009
27/07/2009
10/08/2009
17/08/2009
24/08/2009
31/08/2009
12/10/2009
19/10/2009
26/10/2009
09/11/2009
16/11/2009
23/11/2009
30/11/2009

193.00
209.00
224.00
218.00
248.00
225.00
231.00
225.00
225.00
211.00
227.00
247.00
200.00
206.00
205.00
165.00
205.00
186.00

3.85
4.16
4.48
4.36
4.96
4.50
4.60
4.50
4.49
4.21
4.53
4.94
4.00
4.11
4.09
3.29
4.09
3.72
Mean
SD
k
Q

207
19.18
2.33
251.56

Table 2*: Pooled distribution model (Without normalization to 50 retailers)
Date
14/07/2008
21/07/2008
28/07/2008
11/08/2008
18/08/2008
25/08/2008
01/09/2008
15/09/2008
21/09/2008
27/10/2008
10/11/2008
17/11/2008
24/11/2008
08/12/2008
15/12/2008
22/12/2008
05/01/2009

Group Squirrel

Sales
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

7

1 August 2025

12/01/2009
19/01/2009
26/01/2009
09/02/2009
16/02/2009
23/02/2009
09/03/2009
16/03/2009
20/04/2009
11/05/2009
18/05/2009
08/06/2009
15/06/2009
22/06/2009
29/06/2009
13/07/2009
20/07/2009
27/07/2009
10/08/2009
17/08/2009
24/08/2009
31/08/2009
12/10/2009
19/10/2009
26/10/2009
09/11/2009
16/11/2009
23/11/2009
30/11/2009

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

Mean
SD
k
Q

189.59
19.99
2.33
237.00

Table 3: At the level of each Sales Agent (Normalization to 50 retailers)
Date
14/07/2008
21/07/2008
28/07/2008
11/08/2008
18/08/2008
25/08/2008

Group Squirrel

1
21.25
18.75
25.00
20.00
30.00
25.00

2
13.75
12.50
12.50
16.25
16.25
7.50

3
13.00
15.00
13.00
11.00
13.00
10.00

4
22.50
17.50
15.00
25.00
15.00
16.25

8

5
26.25
23.75
32.50
35.00
27.50
22.50

6
33.75
30.00
35.00
23.00
19.00
26.00

7
13.75
8.75
12.50
16.25
13.75
10.00

8
20.00
15.00
18.75
15.00
18.75
16.25

9
30.00
20.00
30.00
28.00
26.00
24.00

1 August 2025

10
7.50
8.75
11.25
13.75
17.00
15.00

01/09/2008
15/09/2008
21/09/2008
27/10/2008
10/11/2008
17/11/2008
24/11/2008
08/12/2008
15/12/2008
22/12/2008
05/01/2009
12/01/2009
19/01/2009
26/01/2009
09/02/2009
16/02/2009
23/02/2009
09/03/2009
16/03/2009
20/04/2009
11/05/2009
18/05/2009
08/06/2009
15/06/2009
22/06/2009
29/06/2009
13/07/2009
20/07/2009
27/07/2009
10/08/2009
17/08/2009
24/08/2009
31/08/2009
12/10/2009
19/10/2009
26/10/2009
09/11/2009
16/11/2009
23/11/2009
30/11/2009

34.00
29.00
28.00
22.00
22.00
24.00
25.00
17.00
24.00
30.00
29.00
21.00
24.00
31.00
19.00
25.00
27.00
26.00
25.00
21.00
23.75
23.00
21.00
25.00
27.50
28.75
34.00
22.00
30.00
28.33
28.33
31.67
21.67
30.00
23.00
20.00
27.50
13.75
28.75
19.00

16.25
15.00
18.00
16.00
15.00
16.00
14.00
17.00
12.00
15.00
16.00
16.00
16.00
15.00
19.00
14.00
16.00
18.00
16.00
21.00
22.00
23.00
10.00
6.00
16.00
18.00
20.00
18.00
18.00
16.00
20.00
18.00
16.00
23.00
18.00
17.00
20.00
11.00
21.00
19.00

10.00
11.00
14.00
8.00
11.00
10.00
9.00
7.00
15.00
9.00
12.00
11.00
16.00
14.00
14.00
18.00
13.00
13.00
16.00
16.00
12.00
15.00
13.00
13.00
13.00
12.00
17.00
14.00
9.00
15.00
17.00
11.00
10.00
19.00
12.00
17.00
11.00
9.00
12.00
16.00

19.00
22.00
22.00
17.00
15.00
22.00
19.00
18.00
13.00
16.00
19.00
16.00
20.00
18.00
13.00
22.00
18.00
18.00
11.00
21.00
18.75
12.50
17.00
22.00
22.50
23.75
22.00
19.00
21.00
15.00
20.00
20.00
26.25
19.00
21.00
19.00
19.00
16.00
22.50
13.75

36.25
40.00
25.00
22.50
36.25
38.75
22.50
32.50
43.75
23.75
37.50
38.75
30.00
28.75
31.25
37.00
35.00
34.00
22.00
26.00
29.00
38.00
37.00
35.00
30.00
37.00
36.00
37.00
38.75
42.50
41.25
32.50
38.75
36.00
32.50
41.25
30.00
23.75
22.50
27.50

19.00
20.00
24.00
25.00
21.00
15.00
25.00
19.00
20.00
22.00
25.00
22.00
19.00
19.00
22.00
28.00
18.00
24.00
18.00
24.00
27.50
23.75
21.00
22.50
17.50
16.25
28.00
29.00
29.00
24.00
19.00
20.00
29.00
33.00
16.00
21.00
19.00
25.00
23.00
22.00

10.00
13.75
13.00
11.00
12.00
11.00
13.00
10.00
17.00
14.00
14.00
10.00
10.00
7.50
13.75
15.00
12.50
13.75
11.25
11.25
15.00
12.50
10.00
16.67
15.00
20.00
15.00
13.75
15.00
20.00
15.00
21.25
18.75
18.75
13.33
13.75
15.00
10.00
13.00
11.00

18.75
20.00
22.50
30.00
11.25
21.25
18.75
18.75
13.75
23.75
21.25
15.00
22.50
18.75
17.50
22.50
26.25
12.50
17.50
17.50
17.50
18.75
21.25
25.00
20.00
16.67
21.25
17.50
20.00
20.00
22.50
15.00
20.00
16.00
20.00
18.00
23.00
16.25
19.00
20.00

26.00
39.00
28.00
28.00
31.00
36.00
29.00
33.00
34.00
29.00
27.00
25.00
29.00
31.00
31.00
36.00
35.00
29.00
17.00
21.00
37.00
36.00
21.00
27.00
38.00
24.00
35.00
32.00
41.25
31.67
33.33
26.25
28.75
31.00
28.75
25.00
28.75
31.25
31.25
27.50

19.00
23.00
14.00
12.00
19.00
16.00
14.00
19.00
20.00
19.00
19.00
16.00
21.00
13.00
18.00
22.00
14.00
23.00
17.00
19.00
19.00
19.00
17.50
16.25
20.00
18.75
17.00
20.00
13.75
21.25
17.00
21.25
21.25
20.00
17.00
17.00
13.75
11.25
15.00
11.25

Mean
SD
k
Q

25.00
4.51
2.33
36.00

16.30
3.55
2.33
25.00

12.80
2.80
2.33
20.00

18.70
3.44
2.33
27.00

32.51
6.28
2.33
48.00

23.07
4.74
2.33
35.00

13.51
3.07
2.33
21.00

19.16
3.53
2.33
28.00

29.71
5.10
2.33
42.00

16.90
3.67
2.33
26.00

Group Squirrel

9

1 August 2025

Total Q = 308
Table 3*: At the level of each Sales Agent (Without normalization to 50 retailers)
Date
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
14/07/2008
17
11
13
18
21
27
11
16
30
6
21/07/2008
15
10
15
14
19
24
7
12
20
7
28/07/2008
20
10
13
12
26
28
10
15
30
9
11/08/2008
16
13
11
20
28
23
13
12
28
11
18/08/2008
24
13
13
12
22
19
11
15
26
17
25/08/2008
25
6
10
13
18
26
8
13
24
15
01/09/2008
34
13
10
19
29
19
8
15
26
19
15/09/2008
29
12
11
22
32
20
11
16
39
23
21/09/2008
28
18
14
22
20
24
13
18
28
14
27/10/2008
22
16
8
17
18
25
11
24
28
12
10/11/2008
22
15
11
15
29
21
12
9
31
19
17/11/2008
24
16
10
22
31
15
11
17
36
16
24/11/2008
25
14
9
19
18
25
13
15
29
14
08/12/2008
17
17
7
18
26
19
10
15
33
19
15/12/2008
24
12
15
13
35
20
17
11
34
20
22/12/2008
30
15
9
16
19
22
14
19
29
19
05/01/2009
29
16
12
19
30
25
14
17
27
19
12/01/2009
21
16
11
16
31
22
10
12
25
16
19/01/2009
24
16
16
20
24
19
10
18
29
21
26/01/2009
31
15
14
18
23
19
6
15
31
13
09/02/2009
19
19
14
13
25
22
11
14
31
18
16/02/2009
25
14
18
22
37
28
12
18
36
22
23/02/2009
27
16
13
18
35
18
10
21
35
14
09/03/2009
26
18
13
18
34
24
11
10
29
23
16/03/2009
25
16
16
11
22
18
9
14
17
17
20/04/2009
21
21
16
21
26
24
9
14
21
19
11/05/2009
19
22
12
15
29
22
12
14
37
19
18/05/2009
23
23
15
10
38
19
10
15
36
19
08/06/2009
21
10
13
17
37
21
6
17
21
14
15/06/2009
20
6
13
22
35
18
10
15
27
13
22/06/2009
22
16
13
18
30
14
9
12
38
16
29/06/2009
23
18
12
19
37
13
12
10
24
15
13/07/2009
34
20
17
22
36
28
12
17
35
17
20/07/2009
22
18
14
19
37
29
11
14
32
20
27/07/2009
18
18
9
21
31
29
12
16
33
11
10/08/2009
17
16
15
15
34
24
16
16
19
17
17/08/2009
17
20
17
20
33
19
12
18
20
17
24/08/2009
19
18
11
20
26
20
17
12
21
17
31/08/2009
13
16
10
21
31
29
15
20
23
17

Group Squirrel

10

1 August 2025

12/10/2009
19/10/2009
26/10/2009
09/11/2009
16/11/2009
23/11/2009
30/11/2009
Mean
SD
k
Q

30
23
16
22
11
23
19

23
18
17
20
11
21
19

19
12
17
11
9
12
16

19
21
19
19
16
18
11

36
26
33
24
19
18
22

33
16
21
19
25
23
22

15
8
11
12
10
13
11

16
20
18
23
13
19
20

31
23
20
23
25
25
22

20
17
17
11
9
12
9

22.43
5.18
2.33
35.00

15.83
3.96
2.33
26.00

12.80
2.80
2.33
20.00

17.61
3.38
2.33
26.00

28.04
6.38
2.33
43.00

22.17
4.32
2.33
33.00

11.22
2.50
2.33
18.00

15.65
3.31
2.33
24.00

27.98
5.70
2.33
42.00

15.85
4.11
2.33
26.00

Total Q = 293

Group Squirrel

11

1 August 2025

