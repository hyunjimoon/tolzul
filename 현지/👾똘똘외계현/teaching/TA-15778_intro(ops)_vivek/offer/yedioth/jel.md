### Final Grade & Feedback

Q1: 15/15
Q2: 10/15 [Calculated 229, outside ±5% range of 236]
Q3: 15/15
Q4: 10/15 [No quantitative example provided]
Q5: 10/10
Bonus: 0/10

**Total: 60/80**

---

The Yedioth Group Case Study
Report by the Jellyfish Group (Section B): Mimi Kelley, Danilo Medeiros, Yazhini Ravi, Utheswaran
Krishna Moorthy, Paraschos Liadis

1. In the current distribution model, where each retailer is supplied once a week, independently of all
other retailers. What would be a good method to compute the quantity shipped to each retailer if one
wishes to guarantee that 99% of customers will be served? Apply your approach to compute
recommended quantities to the 50 retailers (explain the methodology in the body of the report and
provide the results in appendix).
We can derive the optimal newspaper weekly order quantity for every retailer by applying the Newsvendor
Formula, assuming a normally distributed demand and that each retailer is independently supplied:
𝑞 =𝜇+𝐾∗𝜎
For retailer No 1:
The mean (μ) of all the “sales” for retailer No 1 is: 𝜇1 = 4.27,
𝑡ℎ𝑒 𝑠𝑡𝑎𝑛𝑑𝑎𝑟𝑑 𝑑𝑒𝑣𝑖𝑎𝑡𝑖𝑜𝑛 𝑖𝑠 𝜎1 = 1.76
𝑎𝑛𝑑 𝑘 = 2.33 (𝑠𝑒𝑟𝑣𝑖𝑐𝑒 𝑙𝑒𝑣𝑒𝑙 𝑜𝑓 99%)
So, the recommended weekly order for retailer No1 is:
, which is rounded up to 9 newspapers per week.
We have run the calculations for the 50 retailers and found that the total weekly order for the 50 retailers
would be
newspapers per week for the 50 retailers (using the rounded-up values). 🚨correct ~419🚨
Please refer to Appendix Table 1.

2. If Yedioth could implement full pooling among all of the 50 retailers what would be the estimated
benefit in terms of total production levels and returns (assume that the required service level is 99%).
Note: Full pooling means that somehow all of the retailers could be supplied in real time from the
same pool of inventory.
As mentioned in Q1,
To find the

per week.
we have followed the below procedure:

We have computed the

For

mean demand for the 50 retailers by adding the μ of the 50 retailers.

given that standard deviations cannot be added, we have calculated the sum of the variances (
) and then

Note: correlation is assumed to be 0 as each retailer is operating independently.
So,

newspapers

The qdistributed+added is 315 per week. As such, qT pooling < qdistributed+added.
Hence, total pooling provides opportunities for lower production compared to current actual production and
no pooling option, while still meeting 99% service level.
Clearly, inventory management can be optimized through pooling. Pooling reduces aggregate variability
because, over the long term, individual variabilities in demand tend to offset each other. High demand from
one retailer often coincides with low demand from another, resulting in lower overall variability, and thus
safety stock requirements. This can also be proven analytically.
Nevertheless, in the current setting, pooling 50 retailers and managing inventory centrally would require a
major investment in infrastructure and human capital, as well as a significant shift in organizational culture.

3. Suppose that one could implement full pooling only among retailers that are treated by the same
sales agent, what would be the potential benefit in terms of production levels and returns (assume
99% service level). Compare to your # 2 answer.
In this case, we grouped the retailers treated by the same sale agents, calculated the
to find the

and the aggregated the

and the

and concluded that

newspapers per week. Please refer to Appendix Table 2.
Comparing with results from Q1 and Q2, the below indicates the following:

Pooling among retailers that are treated by the same agent is beneficial, but not as beneficial as pooling
among the 50 retailers.

4. Propose more realistic policies that leverage the fact that the sales agent visits each retailer in the
middle of the week. What would the benefit be of these policies?
We propose the following policies, taking advantage of the fact that sales agents visit each retailer midweek:
•

Experiment with demand by lowering the service level from 99% to 95% and replenishing stock, as
necessary, during a second visit (delivery date).

•

Allow agents to re-distribute inventory among their pool of retailers as needed, rather than sales
agents bringing in fresh inventory.

•

Identify stockouts or low stock levels during mid-week visits and replenish accordingly.

•

If more than 70%+ stock is sold by mid-week, replenish up to a fixed quantity (to restore
availability).

•

Implement RFID technology at selected high-volume retailers to enable centralized inventory
monitoring; utilize centralized dashboard for research department review.

•

Introduce a minimum stock alert system (e.g., through a phones and/or mobile app) which retailers
can use to notify agents when inventory levels reach a ‘low level’

5. What do you think are the organizational challenges that Assaf will have to address?

The Yedioth Group is a company with a conservative and antiquated decision-making and operating
structure. Assaf must overcome the following organizational dynamics:
•

Company culture: The legacy system has been successful over the years, so there is little internal
drive for change.

•

Resistance from sales agents: This is a powerful group within the organization. They have
misaligned incentives as they are compensated by sales volumes. In addition, they may fear that
changes could risk stockouts and damage the company’s reputation. Fewer shipments may seem
threatening.

•

Resistance from the research department: The department is comfortable with traditional ways of
operating and may be hesitant to adopt new methods.

•

Resistance from the IT department: Implementing an updated data acquisition and monitoring system
will require cooperation from IT, which may be difficult to achieve.

Assaf can address these challenges by framing change as modernization not disruption, as well as
introducing an incremental, inclusive, and transparent process. For example:
•

Run small-scale pilot projects/tests and solution designs to demonstrate the benefits of the new
decision-making system.

•

Consider pooling among agent sub-groups and validate the pooling results using real data.

•

Create a cross-functional task force that includes sales agents, research department staff, and IT
experts to build and validate the new decision-making model collaboratively with shared KPIs.

Bottom of Form: Appendix Attached

Appendix
Table 1: Data per retailer

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

Mean of Sales
4.267
5.447
1.609
1.804
3.087
3.609
3.927
14.435
4.733
3.174
4.000
4.067
2.244
2.457
4.561
6.522
4.783
1.860
5.848
3.250
2.783
4.196
5.136
1.565
8.739
3.152
2.163
6.652
1.943
8.000
4.804
2.587
3.674
2.217
3.953
2.674
3.609
3.405
3.043
9.065
3.696
3.735
3.065
3.375
1.478

Standard
Deviation of
Sales
1.763
1.941
0.745
1.185
1.458
1.732
1.603
3.914
1.615
1.371
1.863
1.009
1.111
1.130
1.582
2.008
1.699
0.804
1.763
1.740
1.009
2.146
2.098
1.148
2.389
1.475
1.703
3.107
1.259
2.683
1.939
1.240
1.606
1.298
1.661
1.550
1.584
1.083
1.414
2.507
1.474
2.093
1.467
0.916
0.937

Variance of Sales
3.109
3.767
0.555
1.405
2.126
2.999
2.570
15.318
2.609
1.880
3.471
1.018
1.234
1.276
2.502
4.033
2.885
0.647
3.110
3.029
1.018
4.605
4.400
1.318
5.708
2.176
2.901
9.654
1.585
7.200
3.761
1.537
2.580
1.685
2.760
2.402
2.510
1.174
1.998
6.285
2.172
4.382
2.151
0.839
0.877

Optimal weekly
order quantity
8.375
9.970
3.344
4.566
6.484
7.644
7.662
23.554
8.497
6.369
8.341
6.418
4.833
5.088
8.247
11.201
8.740
3.734
9.957
7.305
5.134
9.196
10.024
4.240
14.306
6.589
6.132
13.892
4.876
14.252
9.323
5.475
7.417
5.242
7.824
6.285
7.300
5.929
6.337
14.906
7.130
8.613
6.483
5.510
3.661

Optimal weekly
order quantity
rounded up
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
5
9
12
9
4
10
8
6
10
10
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

46
47
48
49
50
SUM

6.353
5.512
1.429
2.929
4.000
204.616

1.921
2.026
1.065
1.269
1.225

3.690
4.106
1.134
1.610
1.500
149.262

10.829
10.234
3.910
5.885
6.854

11
11
4
6
7
417

Appendix 2: Pooled Agent Data
Scenario

Total-mean

Pooled-std dev

Required-99%

Savings-%

Full Pooling

200.6156715

12.15574959

229 0.239203

agent 1

24.59687065

4.258266159

35 0.036791

agent 2

16.77345538

3.352090012

25 0.161798

agent 3

12.80434783

2.857907075

20 0.329438

agent 4

18.17363072

3.629285344

27 0.094742

agent 5

26.82608696

4.967144109

39

-0.3076

agent 6

22.72207699

4.084885998

33

-0.10643

agent 7

13.54740077

3.038430316

21

0.29591

agent 8

18.78645939

3.14876833

27 0.094742

agent 9

28.58416149

5.213085704

41

agent 10

17.80118134

3.061321192

25 0.161798

Total Agent Pooling

200.6156715

293

293 0.026578

-0.37465

