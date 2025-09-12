### Final Grade & Feedback

Q1: 15/15
Q2: 15/15
Q3: 15/15
Q4: 10/15 [No quantitative example provided]
Q5: 10/10
Bonus: 0/10

**Total: 65/80**

---

The Yedioth Group Report

Team Monkey
Becky Lin / Kohei Banno /Luiz Rodolfo Ribeiro/
Michael Autery/ Young Deuk Hong

Q1. Optimizing Weekly Retailer Shipments

To address the challenge of determining weekly shipment quantities for each retailer while
avoiding both stockouts and excessive returns, we employed the Newsvendor model.
Using historical weekly sales data for each of the 50 retailers, we calculated the average
demand (μ) and the standard deviation (σ). To achieve a 99% service level, we used the
following formula:
Order Quantity=μ+2.33⋅σ
This ensures each retailer receives sufficient inventory to meet demand in 99% of the
weeks, assuming demand is normally distributed. For instance, Retailer 1 had an average
weekly demand of 4.27 with a standard deviation of 1.76, resulting in a calculated order
quantity of 8.38. We rounded this up to 9 units, since fractional magazines are not practical.
Additionally, we are assuming that sell-throughs are minimal, and that suppressed demand
is minimized.

Applying this methodology across all 50 retailers yielded a total required quantity of 419
magazines 🚨correct ~419🚨 (rounded up from 394.11). A full breakdown is presented in Appendix Q1.
This approach helps Yedioth maintain high service levels while minimizing overproduction
and improving operational efficiency.

1
9.00
11
9.00
21
6.00
31
10.00
41
8.00

2
10.00
12
7.00
22
10.00
32
6.00
42
9.00

3
4.00
13
5.00
23
11.00
33
8.00
43
7.00

4
5.00
14
6.00
24
5.00
34
6.00
44
6.00

5
7.00
15
9.00
25
15.00
35
8.00
45
4.00

6
8.00
16
12.00
26
7.00
36
7.00
46
11.00

7
8.00
17
9.00
27
7.00
37
8.00
47
11.00

8
24.00
18
4.00
28
14.00
38
6.00
48
4.00

9
9.00
19
10.00
29
5.00
39
7.00
49
6.00

10
7.00
20
8.00
30
15.00
40
15.00
50
7.00

(Table 1: Order Quantity by Customer Number)
By applying the newsvendor model, Yedioth can reduce overproduction while maintaining a
high service level, offering a practical solution that enhances both customer satisfaction and
operational efficiency.

Q2. Benefits of Full Inventory Pooling Across All Retailers
We next applied the Newsvendor model to the pooled demand across all 50 retailers,
treating the group as a single aggregated customer.

Using total weekly demand data, we calculated a mean of 189.59 and a standard deviation
of 19.99. Applying a z-score of 2.33 for a 99% service level gave an optimal pooled order
quantity of 236.16 magazines, which we rounded up to 237. 🚨correct pooling🚨 Compared to the sum of
individual retailer quantities from Q1 (419 magazines), full pooling offers a production
reduction of 182 magazines per week.
(See Appendix Q2 for calculation details.)
Q1 Results
Full Pooling
Production Saved

419.00
237.00
182.00

This reduction highlights the operational benefit of risk pooling, as aggregated demand
reduces variability and lowers the safety stock needed.
Q3. Partial Pooling by Sales Agent
By applying the newsvendor model to each sales agent’s weekly total sales, our team
estimated the production required if Yedioth pooled inventory as agent’s group of retailers.

For each of the 10 agents, we calculated the average and standard deviation of weekly sales
and applied a z-score of 2.33 to ensure a 99% service level.
The resulting agent-level order quantities were rounded up and summed, yielding a total
production requirement of 293 magazines per week 🚨acceptable agent pooling🚨 (see appendix for details). This is 56
magazines more than full pooling (Q2) and 126 fewer than no pooling (Q1), demonstrating
how limited pooling still captures some benefits of aggregation but not as fully as systemwide pooling.

Detailed agent-level results are available in Appendix Q3.
Agent
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

Mean (μ)
Std Dev (σ) Safety Stock @99% Order Quantity Rounded up
22.43
5.18
12.06
34.49
35.00
15.83
3.96
9.23
25.06
26.00
12.80
2.80
6.53
19.33
20.00
17.61
3.38
7.88
25.49
26.00
28.04
6.38
14.87
42.92
43.00
22.17
4.32
10.06
32.23
33.00
11.22
2.50
5.83
17.05
18.00
15.65
3.31
7.72
23.38
24.00
27.98
5.70
13.29
41.26
42.00
15.85
4.11
9.59
25.44
26.00
SUM
293.00
diff. q2
56.00

Q4. Leveraging Midweek Sales Agent Visits for Operational Improvements
We propose that each retailer provide sales information midweek through the week to
enable more responsive inventory management. By collecting this midweek data, the sales
agent can adjust inventory levels, either removing excess stock or adding more magazines,
based on actual demand observed in the first half of the week.
These adjustments would be guided by profit maximizing logic from the newsvendor model,
which balances the tradeoff between marginal revenue from additional sales and marginal
salvage costs from unsold inventory. This allows for smarter, data driven decisions that
reduce overproduction and minimize lost sales.
To enable this midweek visibility, we propose implementing RFID for real-time tracking. 🚨specific mechanism🚨
RFID offers reliable and real time tracking of inventory levels at the retailer, which can
significantly improve responsiveness and forecasting accuracy. Although capital-intensive,
RFID can significantly improve demand visibility and reduce inefficiencies. A cost-benefit
analysis is advised to assess the feasibility, particularly for lower-volume retailers.
Q5. Organizational Challenges and Change Management
Implementing these changes may face resistance, particularly from the Research
Department and Sales Agents, due to longstanding cultural norms and incentive structures.
A key challenge will be incentive misalignment. Sales agents are currently rewarded based
on sales volume, which discourages inventory efficiency and encourages overproduction. To
address this, Assaf will need to design a new incentive structure that aligns agent
performance with company goals, such as reducing returns, improving forecast accuracy,
and maintaining service levels, so that sales agents are motivated to support the change
rather than resist it.
In addition, Organizational buy-in 🚨multiple stakeholders🚨 can be strengthened through pilot programs, clear
communication of financial benefits, and engaging key stakeholders early in the process to
champion change.

Appendix
Q1.

Customer Number Mean (μ) Std Dev (σ)
1
4.27
1.76
2
5.45
1.94
3
1.61
0.74
4
1.80
1.19
5
3.09
1.46
6
3.61
1.73
7
3.93
1.60
8
14.43
3.91
9
4.73
1.62
10
3.17
1.37
11
4.00
1.86
12
4.07
1.01
13
2.24
1.11
14
2.46
1.13
15
4.56
1.58
16
6.52
2.01
17
4.78
1.70
18
1.86
0.80
19
5.85
1.76
20
3.25
1.74
21
2.78
1.01
22
4.20
2.15
23
5.14
2.10
24
1.57
1.15
25
8.74
2.39
26
3.15
1.48
27
2.16
1.70
28
6.65
3.11
29
1.94
1.26
30
8.00
2.68
31
4.80
1.94
32
2.59
1.24
33
3.67
1.61
34
2.22
1.30
35
3.95
1.66
36
2.67
1.55
37
3.61
1.58
38
3.40
1.08
39
3.04
1.41
40
9.07
2.51
41
3.70
1.47
42
3.74
2.09
43
3.07
1.47
44
3.38
0.92
45
1.48
0.94
46
6.35
1.92
47
5.51
2.03
48
1.43
1.07
49
2.93
1.27
50
4.00
1.22

Variance Safety Stock @99% Order Quantity
3.11
4.11
8.38
3.77
4.52
9.97
0.55
1.74
3.34
1.41
2.76
4.57
2.13
3.40
6.48
3.00
4.04
7.64
2.57
3.73
7.66
15.32
9.12
23.55
2.61
3.76
8.50
1.88
3.19
6.37
3.47
4.34
8.34
1.02
2.35
6.42
1.23
2.59
4.83
1.28
2.63
5.09
2.50
3.69
8.25
4.03
4.68
11.20
2.89
3.96
8.74
0.65
1.87
3.73
3.11
4.11
9.96
3.03
4.06
7.31
1.02
2.35
5.13
4.61
5.00
9.20
4.40
4.89
10.02
1.32
2.67
4.24
5.71
5.57
14.31
2.18
3.44
6.59
2.90
3.97
6.13
9.65
7.24
13.89
1.58
2.93
4.88
7.20
6.25
14.25
3.76
4.52
9.32
1.54
2.89
5.48
2.58
3.74
7.42
1.69
3.02
5.24
2.76
3.87
7.82
2.40
3.61
6.29
2.51
3.69
7.30
1.17
2.52
5.93
2.00
3.29
6.34
6.28
5.84
14.91
2.17
3.43
7.13
4.38
4.88
8.61
2.15
3.42
6.48
0.84
2.13
5.51
0.88
2.18
3.66
3.69
4.48
10.83
4.11
4.72
10.23
1.13
2.48
3.91
1.61
2.96
5.88
1.50
2.85
6.85
394.11

Rounded up
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

Q2.
Row Labels Sum of Sales
7/14/2008
170
7/21/2008
143
7/28/2008
173
8/11/2008
175
8/18/2008
172
8/25/2008
158
9/1/2008
192
9/15/2008
215
9/21/2008
199
10/27/2008
181
11/10/2008
184
11/17/2008
198
11/24/2008
181
12/8/2008
181
12/15/2008
201
12/22/2008
192
1/5/2009
208
1/12/2009
180
1/19/2009
197
1/26/2009
185
2/9/2009
186
2/16/2009
232
2/23/2009
207
3/9/2009
206
3/16/2009
165
4/20/2009
192
5/11/2009
201
5/18/2009
208
6/8/2009
177
6/15/2009
179
6/22/2009
188
6/29/2009
183
7/13/2009
238
7/20/2009
216
7/27/2009
198
8/10/2009
189
8/17/2009
193
8/24/2009
181
8/31/2009
195
10/12/2009
242
10/19/2009
184
10/26/2009
189
11/9/2009
184
11/16/2009
148
11/23/2009
184
11/30/2009
171

Mean (μ)
189.59

Std Dev (σ)
Safety Stock @99%
19.99
46.57
Rounded up

Order Quantity
236.16
237.00

Q1 Results
Full Pooling
Production Saved

419.00
237.00
182.00

Q3.
Agent
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

Mean (μ)
Std Dev (σ) Safety Stock @99% Order Quantity Rounded up
22.43
5.18
12.06
34.49
35.00
15.83
3.96
9.23
25.06
26.00
12.80
2.80
6.53
19.33
20.00
17.61
3.38
7.88
25.49
26.00
28.04
6.38
14.87
42.92
43.00
22.17
4.32
10.06
32.23
33.00
11.22
2.50
5.83
17.05
18.00
15.65
3.31
7.72
23.38
24.00
27.98
5.70
13.29
41.26
42.00
15.85
4.11
9.59
25.44
26.00
SUM
293.00
diff. q2
56.00

