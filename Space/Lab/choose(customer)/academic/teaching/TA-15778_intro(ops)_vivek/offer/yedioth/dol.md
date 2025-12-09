### Final Grade & Feedback

Q1: 15/15
Q2: 15/15
Q3: 15/15
Q4: 15/15
Q5: 10/10
Bonus: 5 [Censoring discussion in Method 3 + Distribution analysis in Method 2]

**Total: 75/80**

---

15.778 Introduction to Operations
Management

Dolphins Study Group, Section A

Group Members: Hanyun Li, Daigo
Ito, Ademir Xavier, Mamdouh
Almutairi, Eze Burts III

The Yedioth Group Case Questions
1. In the current distribution model, where each retailer is supplied once a week
independently of all other retailers, what would be a good method to compute the quantity
shipped to each retailer to guarantee that 99% of customers will be served? Apply your
approach to compute recommended quantities to the 50 retailers.
Methodology 1: With simple assumptions:
Current distribution model requires Yedioth to estimate the distribution of the “weekly
demand” of each retailer individually. To estimate the distribution, we made two assumptions:
1. Weekly sales are independent observations;
2. The sales figures are the best representation of demand;
3. For each retailer, the weekly sales follows normal distribution
With the assumption, we will calculate the supply that guarantees 99% service level. That is:
P (D<=Supply) = 99%
Given D follows normal distribution, we have Supply_i = mu_i + 2.32 * sigma_i. Where Supply_i
is the number of magazines to be distributed to ith retailer, mu_i and sigma_i are mean and
standard deviation estimated with the observed sales records from previous years.

Using the method, we calculated the distribution of magazine (see detailed breakdown in
appendix I). In total, we need 419 magazines per week. 🚨correct ~419🚨

--------------------------------------------------------------------------------------------------------------------------Note: Method 2 and Method 3 are 2 different approaches we tried, in order to relax the
assumptions made in Method 1. Due to time constraint, we didn’t solve the final answer for
Method 2 and didn’t validate the final number for Method 3.

Methodology 2: Violation of “normal distribution” assumption
In reality, demand (for simplicity, we assume demand = sales) doesn’t follow normal
distribution. In fact it might even have some seasonality. Here we will ignore the time effect on
the demand.

15.778 Introduction to Operations
Management

Dolphins Study Group, Section A

Group Members: Hanyun Li, Daigo
Ito, Ademir Xavier, Mamdouh
Almutairi, Eze Burts III

For example, using the histogram of retailer 1’s weekly sales as the proxy of PDF (the bar chart),
CDF (the line chart) of the demand’s distribution:

Given the histogram, using the empirical distribution, we can estimate that supply of 8 could
provide 99% service level (approximately).
Using this method, we estimated the supply per each retailer (see appendix II), in total weekly
supply is 370 🚨empirical distribution analysis🚨 (see detailed breakdown in appendix II).

Methodology 3: Violation of assumption “The sales figures are the best representation of
demand;”
When the retailer has a “sold-out”, we don’t know if the full demand is met, because there
might be customers that haven’t been fully served. So the observed sales numbers are not the
actual demand (lower or equal to). 🚨censoring awareness🚨 In this case, we will not know the distribution of the actual
Demand, thus cannot use observed data to estimate the ideal supply at 99% service level.
Meaning, we won’t know the actual mu of demand, and std of demand. Below is how we think
the problem can be tackled with some “additional” assumptions who are less critical as the
assumption of “sales = demand”.

15.778 Introduction to Operations
Management

Dolphins Study Group, Section A

Group Members: Hanyun Li, Daigo
Ito, Ademir Xavier, Mamdouh
Almutairi, Eze Burts III

At high-level, we will use the current “service level” to estimate the actual mean of demand:
Under the situation of “sold-out”, Supply <= Demand, in the situation of “return”: Supply >
Demand. That means, through the observation data, we know empirically:
P (Demand <= Supply) which is equal to 1 – “Sell Through rate”
Here we apply two assumptions:
•
•

Actual demand follows normal distribution
We use variance of the observed sales as the proxy for the variances of demand

Then we have: P (Demand <= Supply) = P ((Demand – mu) / sigma <= (Supply – mu) / sigma) =
P(Z<= (Supply – mu) / sigma)
Here, sigma = variance of observed sales for each retailer, Supply = actual supply which is the
Distributed + Added.
Given, P(Z<= (Supply – mu) / sigma) = (1-sell through rate) => (Supply – mu) / sigma = Φ⁻¹(1 sell through rate) => mu = Supply - sigma * Φ⁻¹(1 - sell through rate, mu, sigma)
We can solve mu with the function above (however we don’t know how to calculate mu with
excel so we didn’t finish the calculation), as all the parameters above are known except for mu.
With the adjusted mu, we can calculate
Supply to serve at 99% service level = Supply - sigma * Φ⁻¹(1 - sell through rate, mu, sigma)
+ 2.32 * sigma

2. If Yedioth could implement full pooling among all of the 50 retailers what would be the
estimated benefit in terms of total production levels and returns if the required service level
is 99%?
For simplicity, the calculations for Q2 and Q3 will use: Methodology 1: With simple
assumptions.
Under this perfect pooling scenario, we will be able to pool all the weekly observations from 50
retails to estimate the distribution of weekly demand (in total).
We first calculated the weekly total sales, then calculated the mean and standard deviation for
the weekly total sales. With the statistics, we can calculate the number of magazines to be
distributed to the entire 50 retailers (as one pool). Below are the statistics and the final answer:

15.778 Introduction to Operations
Management

Dolphins Study Group, Section A

Group Members: Hanyun Li, Daigo
Ito, Ademir Xavier, Mamdouh
Almutairi, Eze Burts III

Mean of the weekly total sales: 189.59
Standard deviation of the weekly total sales: 19.99
Solving the equation:
P(D<=Supply) = 99%, where D is the total demand (across all the 50 retailers) and Supply is the
total supply to the entire 50 retailers,
We have Supply = mean(observed demand) + 2.32*std(observed demand) = 235.9600782 (236
rounded). 🚨correct pooling🚨
Comparing the result from question 1: 419, we concluded that using the “perfect pooling”, we
estimate the result through improved prediction of variability. Therefore we can reach the
same customer service level with way lower production levels,, therefore less returns of unsold
goods (we can compare the results actual sales, which is about 190 per week, the new
estimation is much closer to the 190).

3. Suppose that one could implement full pooling only among retailers that are treated by the
same sales agent. What would be the potential benefit in terms of production levels and
returns, assuming 99% service level. Compare to your #2 answer.
With the new setting, instead of 1 pool of 50 retailers, we will end up with 10 pools of 5
retailers. The methodology of calculating supply per agent (or per 5 retailers managed by agent
i) stay the same as 2.
By calculating the mean and standard deviation of weekly total sales, of ith pool (5 retailers
managed by agent i), we got the supply to ith pool. In total, the 10 pools (50 retailers) require
293 magazines per week. 🚨acceptable agent pooling🚨 (see details in Appendix III)
Although method 3 requires more magazines, 287, the increased number of magazines (287236=51) is manageable, especially when there’re 10 agents in total (so 5 magazines wasted per
agent). Operational wise, method 3 is also more doble than method 2. Potentially method 3 has
a lower operational cost than method 2 as well. So if full pooling is achievable among retailers
managed by the same agent, method 3 is the best choice among 1-3.

15.778 Introduction to Operations
Management

Dolphins Study Group, Section A

Group Members: Hanyun Li, Daigo
Ito, Ademir Xavier, Mamdouh
Almutairi, Eze Burts III

4. Propose more realistic processes/strategies that leverage the fact that the sales agent visits
each retailer in the middle of the week. What would the benefit be of these
processes/strategies?
•

•

•

•

•

Delayed Two-Phase Distribution: Initiate a first shipment based on projected demand.
During a mid-week visit, the sales agent assesses on-site inventory levels and sales
performance. A follow-up delivery is then made to replenish fast-moving or sold-out
items.
Enhance Tight Feedback Loops and Early-Week Sales Data Reporting: Sales agents
report real-time or near-real-time sales data early-to-mid week to a central dispatch
system. This will trigger targeted replenishment based on actual demand trends.
Predictive Restocking Using Historical Sales Data: Leverage historical sales trends,
seasonality, and regional demand patterns to anticipate inventory needs in advance.
This data-driven approach enables proactive shipment planning and minimizes both
stockouts and excess inventory without requiring real-time field updates.
Pilot a Vendor-Managed Inventory Model with Key Retailers: Let sales agents directly
manage their order quantities based on past and midweek sales data. This would
transfer forecasting responsibility to those who have the best real-time knowledge. 🚨multiple specific mechanisms🚨
Segment the Retailers Based on Sales Patterns: Use mid-week visits

5. What do you think are the organizational challenges that Assaf will have to address?
•

•

•
•
•

Cultural Resistance and Change Management: Addressing resistance to shifting longstanding distribution and production practices, particularly within a traditional, familyrun business culture.
Employee and Agent Buy-In: Convincing staff to move away from buffer inventory and
personal judgment toward data-driven decision-making over intuition or reliance on
excess inventory will be critical.
IT Investment: Deploying systems for sales tracking, mid-week data reporting, and
inventory visibility across the supply chain.
Process Redesign: Realigning roles, workflows, and incentive structures to support
multi-phase distribution and pooled inventory strategies.
Collaboration Barriers and Resistance to Change: Building trust and information sharing
among decentralized retail partners who may be hesitant to engage with centralized
planning efforts will be essential.

15.778 Introduction to Operations
Management

•

Dolphins Study Group, Section A

Group Members: Hanyun Li, Daigo
Ito, Ademir Xavier, Mamdouh
Almutairi, Eze Burts III

Lack of Retailer Incentives: Retailers currently have no incentive to improve their
forecasting accuracy or reduce returns. This perpetuates a culture of over-ordering and
inefficiency. New penalty / incentive structures are needed. 🚨multiple stakeholders and barriers🚨

Appendix I:

Retailer #

Count of
Count of Months
Average of Sales StdDev of Sales Date
(Date)

Rounded
Supply at 99% SL Supply

1
2

4.266666667
5.447368421

1.763261441
1.940985657

45
38

45
38

8.35743321
9.950455145

9
10

3
4
5
6

1.608695652
1.804347826
3.086956522
3.608695652

0.744707575
1.185459409
1.457945083
1.731771872

46
46
46
46

46
46
46
46

3.336417226
4.554613655
6.469389115
7.626406395

4
5
7
8

7
8
9
10
11

3.926829268
14.43478261
4.733333333
3.173913043
4

1.602969805
3.913805616
1.615268061
1.371201384
1.862951485

41
46
45
46
35

41
46
45
46
35

7.645719216
23.51481164
8.480755235
6.355100254
8.322047445

8
24
9
7
9

12
13
14
15
16

4.066666667
2.244444444
2.456521739
4.56097561
6.52173913

1.009049958
1.111010096
1.129533271
1.581909929
2.008195768

45
45
46
41
46

45
45
46
41
46

6.40766257
4.821987867
5.077038928
8.231006645
11.18075331

7
5
6
9
12

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

4.782608696
1.860465116
5.847826087
3.25
2.782608696
4.195652174
5.136363636
1.565217391
8.739130435
3.152173913
2.162790698

1.698535886
0.804197185
1.763423329
1.740422296
1.009137002
2.145999536
2.097516905
1.147987106
2.38918659
1.475238456
1.703361279

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

8.723211952
3.726202585
9.93896821
7.287779727
5.123806541
9.174371098
10.00260286
4.228547477
14.28204332
6.574727131
6.114588865

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

28
29

6.652173913
1.942857143

3.107105772
1.258917769

46
35

46
35

13.8606593
4.863546367

14
5

15.778 Introduction to Operations
Management

Dolphins Study Group, Section A

Group Members: Hanyun Li, Daigo
Ito, Ademir Xavier, Mamdouh
Almutairi, Eze Burts III

30
31
32
33
34
35

8
4.804347826
2.586956522
3.673913043
2.217391304
3.953488372

2.683281573
1.939296152
1.239643084
1.606297991
1.298084803
1.661231448

46
46
46
46
46
43

46
46
46
46
46
43

14.22521325
9.303514899
5.462928477
7.400524382
5.228948047
7.807545331

15
10
6
8
6
8

36
37
38
39
40

2.673913043
3.608695652
3.404761905
3.043478261
9.065217391

1.549972728
1.58434369
1.083344501
1.413530202
2.506898694

46
46
42
46
46

46
46
42
46
46

6.269849772
7.284373013
5.918121147
6.32286833
14.88122236

7
8
6
7
15

41
42
43
44
45

3.695652174
3.735294118
3.065217391
3.375
1.47826087

1.473764118
2.093407018
1.466699604
0.916125381
0.936640105

46
34
46
8
46

46
34
46
8
46

7.114784928
8.5919984
6.467960472
5.500410884
3.651265914

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

6.352941176
5.512195122
1.428571429
2.928571429
4

1.920895513
2.026350799
1.065107404
1.268814451
1.224744871

34
41
35
14
25

34
41
35
14
25

10.80941877
10.21332898
3.899620606
5.872220955
6.841408101

11
11
4
6
7

Grand
Total

4.137096774

2.939137332

2108

2108

393.3001803

419

Appendix II:
Retailer Supply estimation using CDF:
Supply = 99
percentile of
Customer Number Sales
CDF Percentile Count <= Value Total Observations P_99_Flag
1
2
3
4
5

8
10
3
5
7

1
1
1
1
1

100
100
100
100
100

45
38
46
46
46

45
38
46
46
46

TRUE
TRUE
TRUE
TRUE
TRUE

6
7
8

7
7
22

1
1
1

100
100
100

46
41
46

46
41
46

TRUE
TRUE
TRUE

15.778 Introduction to Operations
Management

Dolphins Study Group, Section A

Group Members: Hanyun Li, Daigo
Ito, Ademir Xavier, Mamdouh
Almutairi, Eze Burts III

9
10
11
12
13
14

8
5
8
6
4
4

1
1
1
1
1
1

100
100
100
100
100
100

45
46
35
45
45
46

45
46
35
45
45
46

TRUE
TRUE
TRUE
TRUE
TRUE
TRUE

15
16
17
18
19

7
10
8
4
10

1
1
1
1
1

100
100
100
100
100

41
46
46
43
46

41
46
46
43
46

TRUE
TRUE
TRUE
TRUE
TRUE

20
21
22
23
24

8
4
8
9
6

1
1
1
1
1

100
100
100
100
100

44
46
46
44
46

44
46
46
44
46

TRUE
TRUE
TRUE
TRUE
TRUE

25
26
27
28
29
30
31
32
33

15
6
6
15
4
13
9
6
8

1
1
1
1
1
1
1
1
1

100
100
100
100
100
100
100
100
100

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
46
43
46
35
46
46
46
46

TRUE
TRUE
TRUE
TRUE
TRUE
TRUE
TRUE
TRUE
TRUE

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

4
7
6
6
5
6
14
6
9
5
5

1
1
1
1
1
1
1
1
1
1
1

100
100
100
100
100
100
100
100
100
100
100

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

TRUE
TRUE
TRUE
TRUE
TRUE
TRUE
TRUE
TRUE
TRUE
TRUE
TRUE

45
46

4
10

1
1

100
100

46
34

46
34

TRUE
TRUE

15.778 Introduction to Operations
Management

47
48
49
50
Total Supply

8
3
6
6

Dolphins Study Group, Section A

1
1
1
1

100
100
100
100

Group Members: Hanyun Li, Daigo
Ito, Ademir Xavier, Mamdouh
Almutairi, Eze Burts III

41
35
14
25

41
35
14
25

TRUE
TRUE
TRUE
TRUE

8

9

370

Appendix III:
Agent

1

2

3

4

5

6

7

10 (blank) Grand Total

Average Weekly Sales

22.43 15.83 12.80 17.61 28.04 22.17 11.22 15.65 27.98

15.85

Std Weekly Sales
Supply at 99% SL
Supply at 99% SL rounded

5.18 3.96 2.80 3.38 6.38 4.32 2.50 3.31 5.70
34.44 25.02 19.30 25.46 42.85 32.19 17.02 23.34 41.21
35
26
20
26
43
33
18
24
42

4.11
25.39 286.2318357
26
293

