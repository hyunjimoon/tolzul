### Final Grade & Feedback
Q1: 15/15
Q2: 15/15
Q3: 10/15 [Q3 result 247 is outside 5% range of 287]
Q4: 15/15
Q5: 10/10
Bonus: 0/10 [Only censoring mentioned, no distribution assumption]
**Total: 65/80**

Yedioth Case Report by Wolf Pack
1 August 2025
Lkhagvajargal Baasantseren, Manuel Duvignau, Lanre Ojutalayo, Rachmawaty Sudirman, and Steph Wood

Questions:
1. In the current distribution model, where each retailer is supplied once a week independently
of all other retailers, what would be a good method to compute the quantity shipped to each
retailer to guarantee that 99% of customers will be served? Apply your approach to
compute recommended quantities to the 50 retailers (explain the methodology in the body
of the report and provide the results in appendix).
Step 1. Calculate average of weekly sales μ and standard deviation of weekly sales  for
each retailer
Step 2. Calculate service rate k (or use Z table) to guarantee 99% customers will be
served which means the probability of P_stock = 99% to get k = 2.32
Step 3. Calculate the demand for each retailer q* by using formula:
𝑞 ∗ = μ + k.  = μ + (2.32)
Total Q* for all 50 retailers are 393.30 ~ 394 copies per week.
If we round up for each retailer the total Q* will be 🚨419 copies🚨 per week.
Furthermore, we might want to 🚨consider sell-through rate🚨 in the equation because there is
a risk that we not capturing the real demand (we data with sell-through = 1 and no sellthrough = 0). Also, we may calculate the Expected Utilization E(U) for each retailer to find
the demand as an integer value considering that the product is a newspaper – i.e. consider
rounding up or down considering the overstock vs the understock cost.
In our calculation, we are assuming that sell-through is minimal. The calculation results
for each retailer can be seen in Appendix 1.
2. If Yedioth could implement full pooling among all of the 50 retailers what would be the
estimated benefit in terms of total production levels and returns if the required service level
is 99%? (Note: Full pooling means that somehow all of the retailers could be supplied inreal-time from the same pool of inventory.)
Step 1. Calculate total average sales ∑ μ𝑖 = 204.62 from previous calculation in Q1
Step 2. Calculate the standard deviation of sales  for 50 retailers for pooling
Assume we have independent normal distributions
X𝑖 ~ N(μ𝑖 , 𝑖 )
Hence,
∑ X𝑖 = N (∑ μ𝑖 , SQRT(∑ 𝑖 2 ))
Standard deviation 𝑝 = 12.22
Step 3. Use the same k = 2.32 to get the P_stock = 99%
Step 4. Calculate the demand for all retailers using formula:

Yedioth Case Report by Wolf Pack
1 August 2025
Lkhagvajargal Baasantseren, Manuel Duvignau, Lanre Ojutalayo, Rachmawaty Sudirman, and Steph Wood

𝑞 ∗ = μ + k. 
𝑞 ∗ = 204.62 + 2.32 × 12.22 = 𝟐𝟑𝟐. 𝟗𝟔 ~ 🚨233 copies🚨 per week (rounding up to capture
that we cannot sell fractions of magazines, the same is reflected throughout this
assignment).
Yedioth would have the estimated benefit from this pooling by 394 – 233 = 161 copies per
week.
3. Suppose that one could implement full pooling only among retailers that are treated by
the same sales agent. What would be the potential benefit in terms of production levels
and returns, assuming 99% service level. Compare to your #2 answer.
Step 1. Calculate average of weekly sales μ and standard deviation of weekly sales 
pooled by each sales agent
Step 2. Use the same k = 2.32 to get the P_stock = 99%
Step 3. Calculate the demand for each sales agent q* by using formula:
𝑞 ∗ = μ + k.  = μ + (2.32)
Q* pooling by the sales agent are 246.88 ~ 🚨247 copies🚨 per week referred the detail
calculation in Appendix 2.
It is not as optimized as if Yedioth does the full pooling compared to 233 copies per week
from Q2 with 247 copies per week that we get with pooling by sales agent.
4. Propose more realistic processes/strategies that leverage the fact that the sales agent visits
each retailer in the middle of the week. What would the benefit be of these
processes/strategies?
•

•
•

🚨Require sales agents to collect real-time inventory data🚨 while on site to increase
visibility of inventory tracking without requiring RFID tags. This will help demand
forecasting for Yedioth – i.e. assess performance early in the week to more accurately
forecast sales later in the week.
In order to avoid sell-through scenarios, it could be useful for sales agents to help
restock during their weekly visits. This would help the company maximize its profits,
but it will also help it improve its service level and foster retailer satisfaction.
Use sales agents to redistribute overstock from other retailers to retailers at risk of
sell-through.

5. What do you think are the organizational challenges that Assaf will have to address?
•

There will be significant cultural obstacles related to transitioning from the current
business model to the new more analytical structure. Significant training and
education will be required to ensure that the staff (in particular the Research
Department) understand the changes and implement appropriately.

Yedioth Case Report by Wolf Pack
1 August 2025
Lkhagvajargal Baasantseren, Manuel Duvignau, Lanre Ojutalayo, Rachmawaty Sudirman, and Steph Wood

•

•
•

🚨Motivating the sales agents may be difficult because their compensation is
incentivized by number of orders.🚨 The company should consider a different
compensation model to ensure that the right aspects of the business are incentivized
with the sales staff.
Expensive and potentially complex data collection process, considering that the
company works with 8,000 retailers.
Structurally, a 99% service rate implies that the company will still be required to
carry large amounts of safety stock.

Yedioth Case Report by Wolf Pack
1 August 2025
Lkhagvajargal Baasantseren, Manuel Duvignau, Lanre Ojutalayo, Rachmawaty Sudirman, and Steph Wood

Appendix 1 Q* per Retailer
Customer
/ Retailer
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

Average of Sales
Weekly (μ)
STD Sales (𝝈)
4.266666667
1.763261441
5.447368421
1.940985657
1.608695652
0.744707575
1.804347826
1.185459409
3.086956522
1.457945083
3.608695652
1.731771872
3.926829268
1.602969805
14.43478261
3.913805616
4.733333333
1.615268061
3.173913043
1.371201384
4
1.862951485
4.066666667
1.009049958
2.244444444
1.111010096
2.456521739
1.129533271
4.56097561
1.581909929
6.52173913
2.008195768
4.782608696
1.698535886
1.860465116
0.804197185
5.847826087
1.763423329
3.25
1.740422296
2.782608696
1.009137002
4.195652174
2.145999536
5.136363636
2.097516905
1.565217391
1.147987106
8.739130435
2.38918659
3.152173913
1.475238456
2.162790698
1.703361279
6.652173913
3.107105772
1.942857143
1.258917769
8
2.683281573
4.804347826
1.939296152
2.586956522
1.239643084
3.673913043
1.606297991
2.217391304
1.298084803
3.953488372
1.661231448

For 99%
SR
(k=2.32)
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
2.32
2.32
2.32
2.32
2.32

q*
8.35743321
9.950455145
3.336417226
4.554613654
6.469389114
7.626406395
7.645719215
23.51481164
8.480755235
6.355100255
8.322047445
6.40766257
4.821987868
5.077038928
8.231006646
11.18075331
8.72321195
3.726202585
9.938968209
7.287779726
5.123806539
9.174371098
10.00260286
4.228547478
14.28204332
6.574727131
6.114588864
13.8606593
4.863546367
14.22521325
9.303514899
5.462928477
7.400524383
5.228948046
7.807545331

Round Up
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

Yedioth Case Report by Wolf Pack
1 August 2025
Lkhagvajargal Baasantseren, Manuel Duvignau, Lanre Ojutalayo, Rachmawaty Sudirman, and Steph Wood

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

2.673913043
3.608695652
3.404761905
3.043478261
9.065217391
3.695652174
3.735294118
3.065217391
3.375
1.47826087
6.352941176
5.512195122
1.428571429
2.928571429
4

1.549972728
1.58434369
1.083344501
1.413530202
2.506898694
1.473764118
2.093407018
1.466699604
0.916125381
0.936640105
1.920895513
2.026350799
1.065107404
1.268814451
1.224744871

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
2.32
2.32
2.32
2.32
2.32
Total

6.269849773
7.284373013
5.918121147
6.32286833
14.88122236
7.114784928
8.591998398
6.467960473
5.500410885
3.651265913
10.80941877
10.21332898
3.899620605
5.872220954
6.841408102
393.3001803

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

Yedioth Case Report by Wolf Pack
1 August 2025
Lkhagvajargal Baasantseren, Manuel Duvignau, Lanre Ojutalayo, Rachmawaty Sudirman, and Steph Wood

Appendix 2 Q* per Sales Agent
Sum of Sales
Week/Agent
2008-07-14
2008-07-21
2008-07-28
2008-08-11
2008-08-18
2008-08-25
2008-09-01
2008-09-15
2008-09-21
2008-10-27
2008-11-10
2008-11-17
2008-11-24
2008-12-08
2008-12-15
2008-12-22
2009-01-05
2009-01-12
2009-01-19
2009-01-26
2009-02-09
2009-02-16
2009-02-23
2009-03-09
2009-03-16
2009-04-20
2009-05-11
2009-05-18
2009-06-08
2009-06-15
2009-06-22
2009-06-29
2009-07-13
2009-07-20
2009-07-27
2009-08-10
2009-08-17

1
17
15
20
16
24
25
34
29
28
22
22
24
25
17
24
30
29
21
24
31
19
25
27
26
25
21
19
23
21
20
22
23
34
22
18
17
17

2
11
10
10
13
13
6
13
12
18
16
15
16
14
17
12
15
16
16
16
15
19
14
16
18
16
21
22
23
10
6
16
18
20
18
18
16
20

3
13
15
13
11
13
10
10
11
14
8
11
10
9
7
15
9
12
11
16
14
14
18
13
13
16
16
12
15
13
13
13
12
17
14
9
15
17

4
18
14
12
20
12
13
19
22
22
17
15
22
19
18
13
16
19
16
20
18
13
22
18
18
11
21
15
10
17
22
18
19
22
19
21
15
20

5
21
19
26
28
22
18
29
32
20
18
29
31
18
26
35
19
30
31
24
23
25
37
35
34
22
26
29
38
37
35
30
37
36
37
31
34
33

6
27
24
28
23
19
26
19
20
24
25
21
15
25
19
20
22
25
22
19
19
22
28
18
24
18
24
22
19
21
18
14
13
28
29
29
24
19

7
11
7
10
13
11
8
8
11
13
11
12
11
13
10
17
14
14
10
10
6
11
12
10
11
9
9
12
10
6
10
9
12
12
11
12
16
12

8
16
12
15
12
15
13
15
16
18
24
9
17
15
15
11
19
17
12
18
15
14
18
21
10
14
14
14
15
17
15
12
10
17
14
16
16
18

9
30
20
30
28
26
24
26
39
28
28
31
36
29
33
34
29
27
25
29
31
31
36
35
29
17
21
37
36
21
27
38
24
35
32
33
19
20

10
6
7
9
11
17
15
19
23
14
12
19
16
14
19
20
19
19
16
21
13
18
22
14
23
17
19
19
19
14
13
16
15
17
20
11
17
17

Yedioth Case Report by Wolf Pack
1 August 2025
Lkhagvajargal Baasantseren, Manuel Duvignau, Lanre Ojutalayo, Rachmawaty Sudirman, and Steph Wood

2009-08-24
2009-08-31
2009-10-12
2009-10-19
2009-10-26
2009-11-09
2009-11-16
2009-11-23
2009-11-30
Grand Total
Avg of Sales
Sum of Avg Sales

Week/Agent
2008-07-14
2008-07-21
2008-07-28
2008-08-11
2008-08-18
2008-08-25
2008-09-01
2008-09-15
2008-09-21
2008-10-27
2008-11-10
2008-11-17
2008-11-24
2008-12-08
2008-12-15
2008-12-22
2009-01-05
2009-01-12
2009-01-19
2009-01-26
2009-02-09
2009-02-16
2009-02-23
2009-03-09
2009-03-16

19 18 11 20
26
20
13 16 10 21
31
29
30 23 19 19
36
33
23 18 12 21
26
16
16 17 17 19
33
21
22 20 11 19
24
19
11 11
9 16
19
25
23 21 12 18
18
23
19 19 16 11
22
22
1032 728 589 810 1290 1020
22.43478261 16 13 18
28 22.2
189.5869565

StdDev of Sales
1
2
1.50
0.96
1.50
1.73
2.58
1.91
0.82
1.71
1.41
2.22
3.81
1.91
1.30
1.71
1.92
2.45
1.52
1.82
2.19
1.30
2.19
1.73
2.59
0.84
1.87
0.45
1.82
1.82
2.39
1.14
3.24
1.00
1.92
1.79
1.48
1.92
2.95
1.48
2.17
1.87
2.39
1.10
2.35
1.79
3.65
1.79
1.48
1.67
2.35
2.77

3
1.14
0.71
1.52
1.48
0.89
1.00
1.73
1.64
0.84
1.52
1.64
1.22
0.84
1.14
1.22
1.64
1.52
1.64
2.17
1.30
1.64
1.52
1.34
1.82
0.84

4
2.08
3.00
2.71
2.45
1.41
1.89
2.77
2.88
3.51
1.67
2.92
2.88
3.77
2.79
2.07
2.59
3.03
2.77
2.45
1.82
2.30
2.97
2.88
2.41
1.30

5
4.72
2.50
5.00
5.89
5.74
3.32
5.32
5.35
3.56
3.11
4.57
5.56
2.38
6.40
5.12
3.30
4.65
7.04
4.55
2.87
4.19
6.88
5.10
5.26
2.41

17 12
21 17
15 20
23 17
15 16
31 20
8 20
23 17
11 18
20 17
12 23
23 11
10 13
25
9
13 19
25 12
11 20
22
9
516 720 1287 729
11 16
28 16

6
3.86
2.16
4.08
3.36
3.70
3.27
4.60
1.58
2.59
2.74
2.86
2.92
4.00
5.17
2.12
2.07
4.00
3.65
3.11
1.30
5.41
4.93
1.67
3.03
2.51

7
1.50
2.06
1.91
1.89
2.50
2.16
0.82
1.71
1.95
1.92
2.88
2.49
1.52
1.41
1.95
2.59
1.30
1.87
1.87
1.29
1.50
2.16
1.73
0.50
1.50

8
2.00
1.41
1.71
1.63
1.89
1.26
1.26
2.00
0.58
2.16
0.96
2.50
1.50
2.63
1.26
1.50
1.26
1.63
1.73
2.22
1.29
3.32
2.22
1.29
1.29

9
2.92
4.58
3.94
3.91
1.79
1.79
4.44
6.06
4.16
2.97
4.32
3.70
3.35
4.93
2.95
3.27
3.91
4.30
3.19
3.70
4.09
4.92
3.32
3.11
3.44

10
1.29
0.96
1.71
1.26
1.82
2.92
1.48
3.58
2.05
0.55
2.59
1.48
3.03
1.64
1.22
1.30
0.84
1.92
1.48
1.95
2.30
3.51
1.79
2.70
1.52

Yedioth Case Report by Wolf Pack
1 August 2025
Lkhagvajargal Baasantseren, Manuel Duvignau, Lanre Ojutalayo, Rachmawaty Sudirman, and Steph Wood

2009-04-20
2009-05-11
2009-05-18
2009-06-08
2009-06-15
2009-06-22
2009-06-29
2009-07-13
2009-07-20
2009-07-27
2009-08-10
2009-08-17
2009-08-24
2009-08-31
2009-10-12
2009-10-19
2009-10-26
2009-11-09
2009-11-16
2009-11-23
2009-11-30
Grand Total

agent
μ
𝝈
k
q*

1
22.43
2.13
2.32
27.37

1.30
1.50
1.67
0.84
2.45
1.73
2.22
1.79
2.30
1.00
2.52
2.52
1.53
2.08
2.12
1.95
1.41
2.38
2.06
2.06
3.49
2.1258

2
15.83
1.84
2.32
20.08

1.92
2.30
2.07
1.87
0.84
1.79
1.52
2.92
1.95
2.41
2.17
2.35
1.95
1.92
2.70
2.79
1.52
1.00
1.64
3.35
1.30
1.8357

3
12.80
1.45
2.32
16.17

2.05
1.34
2.00
1.14
2.19
1.14
1.52
1.82
1.79
1.48
1.41
1.52
1.10
0.71
1.30
1.67
1.52
0.84
1.92
1.95
1.92
1.4488

4
17.61
2.28
2.32
22.89

Total Q* = 246.88 ~ 247 copies per week

2.39
2.75
1.29
3.85
2.41
2.38
2.36
1.95
1.64
1.64
2.55
2.45
2.00
2.06
2.49
1.92
1.48
2.17
2.28
1.29
1.26
2.2776

5
28.04
4.99
2.32
39.61

6
22.17
3.04
2.32
29.23

2.86
4.71
4.93
6.11
6.82
4.53
6.88
6.61
7.16
8.22
7.77
6.70
3.79
5.50
7.85
6.40
9.46
3.74
4.35
5.92
5.20
4.987

7
11.22
1.81
2.32
15.41

2.68
4.20
4.65
1.92
2.65
4.04
2.63
3.13
3.27
3.11
3.27
2.49
2.24
3.90
3.36
2.86
2.39
2.95
2.65
1.95
2.70
3.0393

8
15.65
1.67
2.32
19.54

1.26
1.41
2.38
1.00
3.21
1.00
3.46
2.00
2.22
2.16
2.58
2.16
1.71
3.40
1.71
0.58
1.50
1.83
1.87
1.14
1.64
1.8092

2.38
1.73
1.71
2.06
2.65
2.65
1.15
1.71
1.29
1.83
1.63
1.73
0.82
2.00
1.79
1.58
1.95
1.14
1.26
0.84
1.22
1.6748

9
27.98
3.51
2.32
36.11

10
15.85
1.99
2.32
20.47

3.11
4.16
4.09
2.39
4.10
4.39
2.49
4.69
5.59
4.92
2.08
1.53
1.71
3.50
3.90
3.10
2.16
4.11
2.99
2.22
4.20
3.5066

1.30
2.17
1.92
1.91
2.50
1.63
1.50
2.07
1.87
2.06
1.89
3.36
3.86
1.71
2.12
2.07
3.21
1.26
0.50
1.41
1.50
1.9925

