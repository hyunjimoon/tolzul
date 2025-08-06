### Final Grade & Feedback

Q1: 15/15
Q2: 15/15
Q3: 15/15
Q4: 10/15 [No quantitative example provided]
Q5: 10/10
Bonus: 0/10 [Only censoring mentioned, no distribution assumption]

**Total: 60/80**

---

Learning Team Beaver
Introduction to Operations Management
15.778_SU25
Member:
Ifeoluwa Dare-Johnson
Luis Felipe Rosas Antipa
Norman Yasa Perdana
Ryo Kadono
Stuart Grimshaw
Yedioth Case Analysis Report
Q1. In the current distribution model, each retailer is supplied once, independently of all other
retailers. What would be a good method to compute the quantity shipped to each retailer if one
wishes to guarantee that 99% of customers will be served? Apply your approach to compute
recommended quantities to the 50 retailers (explain the methodology in the body of the report
and provide the results in appendix).
A.
Compute the mean sales quantity (μ) and the weekly standard deviation (σ) of each retailer.
Get 99% guaranteed quantity with the equation below, and P_stock 99% = k=2.33.
q*= μ+2.33σ
Total q* = 419 🚨correct ~419🚨
*See Appendix 1 below for the results for each retailer.
*We didn’t consider the sell-throughs on the original data with presuming that sell-through rates
are low and that unmet demand has been largely addressed.

Q2. If Yedioth could implement full pooling among all of the 50 retailers what would be the
estimated benefit in terms of total production levels and returns (assume that the required service
level is 99%). Note: Full pooling means that somehow all of the retailers could be supplied in real
time from the same pool of inventory.
A.
Compute the average sales of each week across the 50 retailers. See Appendix 2.
Calculate the mean and standard deviation.
Mean
189.6

STD
20.0

Q*
236.0

Q* Roundup
236

Get the delta between the result of Q1 and above, which means the estimated benefit in terms of
total production level and returns from the full pooling.

Learning Team Beaver
Introduction to Operations Management
15.778_SU25
Estimated benefit from the full pooling (Reduction amount)
= (Total quantity from individual model (Q1) ) – (Total quantity from pooled model (Q2) )
= 419 – 236 = 183 copies per week 🚨correct pooling calculation🚨
For the expected return, we observe the reduction from the original data;
Proposed weekly order amount: 236 - Average weekly sales: 190 = Expected return: 46
Mean of weekly return in original data: 103 – Expected return above: 46 = Expected return
reduction: 57

Q3. Suppose that one could implement full pooling only among retailers that are treated by the
same sales agent, what would be the potential benefit in terms of production levels and returns
(assume 99% service level). Compare to 2) above.
A.
Follow the same steps as the answer to Q2 above, but for each sales agent. See the result below:
Sales Agent
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

Total Sales
1032.0
728.0
589.0
810.0
1290.0
1020.0
516.0
720.0
1287.0
729.0

Weekly
Average Sales
22.4
15.8
12.8
17.6
28.0
22.2
11.2
15.7
28.0
15.8

STD
5.1
3.9
2.8
3.3
6.3
4.3
2.5
3.3
5.6
4.1

Q
34.4
25.0
19.3
25.4
42.8
32.1
17.0
23.3
41.1
25.3
Total

Q Roundup
35
25
20
26
43
33
17
24
42
26
291

Comparing to the answer to Q2 above, 291-236=55 copies/week less benefit, but still much better 🚨acceptable agent pooling🚨
than original “no pooling” situation, 419 copies/week.
For the expected return, we still observe the reduction from the original data;
Proposed weekly order amount: 291 - Average weekly sales: 190 = Expected return: 101
Mean of weekly return in original data: 103 – Expected return above: 101 = Expected return
reduction: 2

Learning Team Beaver
Introduction to Operations Management
15.778_SU25
Q4. Propose more realistic policies that leverage the fact that the sales agent visits each retailer
in the middle of the week. What would the benefit be of these policies?
A.
1. Mid-Week Replenishment Policy: Use Wednesday visits to physically replenish inventory
based on sales so far. This would require logistics capability but would reduce initial
overstocking and returns. We could consider that the sales agents can carry additional
inventory on Wednesday, needs planning and logistics support, and could start with large
retailers first.
2. Split Delivery Strategy (50/50): Send only ~50–70% of expected demand on Sunday. On
Wednesday, use actual sales data to decide how much more to deliver. This will result
reducing returns due to more accurate replenishment and avoiding stockouts in highdemand weeks.
3. Experimenting for future weeks: Yedioth can run small experiments to better understand
the true demand of specific retailers by temporarily oversupplying those who frequently sell
out. By ensuring these stores do not run out of stock for a few weeks and tracking their daily
sales, the company can observe how many magazines would have been sold if inventory
had been unlimited. This helps uncover lost sales that are hidden under current stockout
conditions. The insights gained from these experiments can improve forecasting accuracy,
reduce unnecessary overstocking elsewhere, and guide smarter midweek replenishment
decisions—all without requiring a full system overhaul. The second visit in the middle of the
week allows Yedioth to capture real demand more accurately in real time and test how
responsive resupply can reduce lost sales, making the experiment both practical and
insightful for improving future forecasts. 🚨specific mechanisms proposed🚨

Q5. What do you think are the organizational challenges that Assaf will have to address?
A.
1. Resistance to Change from the Research Department: The Research Department is
responsible for setting shipment levels. They are used to conservative, overstocking-based
forecasts. Changing to a pooled or adaptive system may be perceived as risky or disruptive.
2. Sales Agent Incentive Misalignment: Sales agents are compensated based on sales volume.
Reducing initial shipments or experimenting with new models may make them fear reduced
earnings or performance penalties.
3. Lack of IT Infrastructure and Real-Time Data Sharing: Most small retailers do not have EDI
or POS systems. Implementing dynamic inventory models requires new data collection
technologies (e.g., RFID, manual input) and training for field agents. Need to discuss the
budget with the financial department.

Learning Team Beaver
Introduction to Operations Management
15.778_SU25
4. Organizational Culture and Legacy Systems: Yedioth is a conservative, family-owned
company with long-standing processes. Radical operational changes challenge the
company’s DNA and will require strong leadership and cross-functional buy-in.
5. Marginal Cost Research: 🚨multiple stakeholders identified🚨 To consider the safety stock, Assaf should find out the marginal
cost with the information of under-stock cost and over-stock cost, which are not given in
this case. They have to keep monitoring and evaluating to get the optimal number while
coordinating with the operation and financial departments.

Learning Team Beaver
Introduction to Operations Management
15.778_SU25
Appendix 1
Retailer
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

μ
4.3
5.4
1.6
1.8
3.1
3.6
3.9
14.4
4.7
3.2
4.0
4.1
2.2
2.5
4.6
6.5
4.8
1.9
5.8
3.3
2.8
4.2
5.1
1.6
8.7
3.2
2.2
6.7
1.9
8.0
4.8
2.6
3.7
2.2
4.0
2.7
3.6
3.4
3.0
9.1
3.7
3.7
3.1
3.4
1.5
6.4
5.5
1.4
2.9
4.0

σ
1.8
1.9
0.7
1.2
1.5
1.7
1.6
3.9
1.6
1.4
1.9
1.0
1.1
1.1
1.6
2.0
1.7
0.8
1.8
1.7
1.0
2.1
2.1
1.1
2.4
1.5
1.7
3.1
1.3
2.7
1.9
1.2
1.6
1.3
1.7
1.5
1.6
1.1
1.4
2.5
1.5
2.1
1.5
0.9
0.9
1.9
2.0
1.1
1.3
1.2

Total Weeks
45
38
46
46
46
46
41
46
45
46
35
45
45
46
41
46
46
43
46
44
46
46
44
46
46
46
43
46
35
46
46
46
46
46
43
46
46
42
46
46
46
34
46
8
46
34
41
35
14
25
Total

q*
8.4
10.0
3.3
4.6
6.5
7.6
7.6
23.5
8.5
6.4
8.3
6.4
4.8
5.1
8.2
11.2
8.7
3.7
9.9
7.3
5.1
9.2
10.0
4.2
14.3
6.6
6.1
13.9
4.9
14.2
9.3
5.5
7.4
5.2
7.8
6.3
7.3
5.9
6.3
14.9
7.1
8.6
6.5
5.5
3.7
10.8
10.2
3.9
5.9
6.8
393.3

q* Roundup
9
10
4
5
7
8
8
24
9
7
9
7
5
6
9
12
9
4
10
8
6
10
11
5
15
7
7
14
5
15
10
6
8
6
8
7
8
6
7
15
8
9
7
6
4
11
11
4
6
7
419

Learning Team Beaver
Introduction to Operations Management
15.778_SU25
Appendix 2
#
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

Week
Weekly sales
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

