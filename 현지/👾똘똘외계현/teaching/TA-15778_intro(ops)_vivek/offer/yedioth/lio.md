### Final Grade & Feedback

Q1: 10/15 [Calculated 456, outside ±5% range of 419]
Q2: 10/15 [Calculated 248, outside ±5% range of 236]
Q3: 10/15 [Calculated 320, outside ±5% range of 287]
Q4: 10/15 [No quantitative example provided]
Q5: 10/10
Bonus: 0/10 [Only censoring mentioned, no distribution assumption]

**Total: 50/80**

---

S2_Section B :Team Lions: Hamamoto, Esquivel, Haque, Vole
Case : The Yedioth Group
Question 1: In the current distribution model, where each retailer is supplied once
a week, independently of all other retailers. What would be a good method to
compute the quantity shipped to each retailer if one wishes to guarantee that 99%
of customers will be served? Apply your approach to compute recommended
quantities to the 50 retailers (explain the methodology in the body of the report
and provide the results in appendix).
We can derive the optimal newspaper weekly order quantity for every retailer by applying
the Newsvendor. Assuming a normally distributed demand and that each retailer is
independently supplied, the formula is: 𝑞 = 𝜇 + 𝐾 ∗ 𝜎
For retailer No1: The mean (μ) of all the “sales” for retailer No1 is: 𝜇1 = 4.51 (this considers
not only the sales number but also 11 instances(‘08 7/28, 9/21, 12/22, ‘09 1/5, 1/12, 6/8,
6/22, 6/29, 7/13, 7/27, 8/31) of stockout. For those 11 instances, we added an additional
1 unit to the sales unit to make sure that at a minimum they do not miss opportunity for
an incremental 1 unit of additional sales.
𝑡The standard deviation is σ1 = 2.00 based on the sales + stockout amount 𝑎𝑛𝑑 𝑘 = 2.33
(service level of 99%). So, the recommended weekly order for retailer No1
Q1=4.51+2.32*2.00=9.14 rounded up to 10 newspapers per week.
We have run the calculation of each individual retailer and Q1+Q2+..Q50 = 456
newspapers/week for the 50 retailers 🚨calculated 456, outside range🚨, the mean(μ), std(σ), and Q* value are provided in
the table in the appendix.
Question 2. If Yedioth could implement full pooling among all of the 50 retailers
what would be the estimated benefit in terms of total production levels and
returns (assume that the required service level is 99%). Note: Full pooling means
that somehow all of the retailers could be supplied in real time from the same
pool of inventory.
Generally speaking, pooling allows us to lower the total inventory by reducing the need
for safety stock at each retailer. We avoid local spikes by looking at the larger picture
and can therefore reduce the effect of local variability.
In our case, it will affect the numbers in the following way:
We calculate the Avg and STD of all retailers together and compute a total quantity. To
evaluate the impact of full pooling, we followed the steps below:
We first calculated the average weekly demand by summing the individual means (μ) of
all 50 retailers. Μ1+μ2+..μ50＝215.4 newspapers / week for 50 retailers (In case of
rounded up:216). Next, since standard deviations cannot be added directly, we
calculated the variance (σ²) of each retailer, summed them which is ∑ σ2= 189, and
then took the square root of the total variance to obtain the pooled standard deviation
which is 13.8. (This is based on zero correlation among retailers, as they operate
independently)

S2_Section B :Team Lions: Hamamoto, Esquivel, Haque, Vole
Case : The Yedioth Group
Thus Quantity 99% service level Q with full pooling = 215.4 + 2.32 * 13.8 = 247.3 then
Rounded up 248 newspapers / week for 50 retailers 🚨calculated 248, outside range🚨
In the setting (Q1), the total weekly production is 456 for 50 retailers. Under full pooling,
the total order quantity required to meet the 99% service level 248 newspapers / week
for 50 retailers is less than 456 newspapers / week for 50 retailers , indicating that
pooling allows for lower production. This reflects a key advantage of pooling in inventory
management rather than managing safety stock individually at each retailer—which
leads to redundancy and inefficiency—we treat demand collectively. By aggregating
demand, local demand spikes are smoothed out by offsetting low demand elsewhere,
reducing overall variability and thus the total safety stock required.
Estimated benefit of total production

: 208 units reduction (248 - 456)

Estimated benefit of returns

: 208 units reduction (32-240)

Question 3. Suppose that one could implement full pooling only among retailers
that are treated by the same sales agent. What would be the potential benefit in
terms of production levels and returns, assuming 99% service level. Compare to
your #2 answer.
Pooling by sales agent is a middle “optimal” option between no pooling (Q1) and full
pooling (Q2). We split the retailers into 10 groups based on sales agents and ran the
Newsvendor calculation for each group using their aggregated mean and standard
deviation. Please refer in the table in the appendix.
This resulted in a total weekly production of 320 newspapers 🚨calculated 320, outside range🚨, compared to 456 in Q1
and 248 in Q2. Estimated sales were 216 (vs. 216 in Q1 and 216 in Q2), and returns
dropped to 104, from 240 in Q1 (but higher than 32 in Q2).
This approach captures part of the benefit of pooling while respecting existing structural
boundaries, offering a practical reduction of 136 units in production and returns
compared to the no-pooling model(Q1).
Question 4. Propose more realistic policies that leverage the fact that the sales
agent visits each retailer in the middle of the week. What would the benefit be of
these policies?
There are different policies we can think of to improve the Yedioth process. If we focus
on leveraging the mid-week visit, here are some possible policies:
-

Strategy1. Each agent will identify a limited number of retailers with a high
standard deviation. (These retailers have more variability and, therefore harder to
predict demand for; consequently, they might run out of stock more frequently),
Now each agent will be focused on better demand forecasting for these retailers.
In order to do that, we can consider reducing the number of visits of sales agents
to retailers that have a low standard deviation to once every 2 weeks. That would

S2_Section B :Team Lions: Hamamoto, Esquivel, Haque, Vole
Case : The Yedioth Group
free sales agents’ time for better forecasting of the high-variability cluster. Also
the visit cost will be reduced as an additional benefit.
- Strategy 2. Instead of delivering them all magazines, which have high inventory
and potential losses, we can spread out their delivery over the week; with one
delivery schedule for Sunday that covers 80% of their inventory and refill them
with the remaining amount with an adjustment on Wednesday based on their
inventory status. This way, if there is a sales spike in the first half of the week, it
can be covered, and if there is significant leftover stock, the second delivery can
be reduced accordingly or rebalanced across the retailers in the area. 🚨specific mechanisms🚨This
approach has already been considered by Assaf.
In addition to the above both strategies, we can consider the following two points to
optimize the operation.
- We could also consider adding a financial incentive for sales agents who lower
magazine returns from retailers. The benefit of that would be lowering the cost of
recovering unsold magazines. We should note that such a move could be tricky,
as it might incentivize them to just deliver fewer magazines to retailers and make
sure they do not overstock, resulting in loss of clients/sales. Because of that, we
need to make sure that the incentive they get for sales is significantly higher than
the new incentive for lower stock returns.
- We may consider evaluate a pilot on the service level for Safety Stock from 99%
to 95%, for example, reducing to 98% creates an impact of 5% the size of the
production batch (456-> 433) with a potential minimum impact on Lost Sales.
Using the current visits of the salesman could generate feedback to the next
week production adjustments.

Question 5:
Assaf can prepare for some significant organizational push-backs from different
elements in the firm, as newspapers are an old industry with “know-how” going back
over 100 years.

S2_Section B :Team Lions: Hamamoto, Esquivel, Haque, Vole
Case : The Yedioth Group
Owners & Management: Since Yedioth is family-based and goes back decades, so
even though Assaf is proposing changes that tackle real problems and changes in the
market, and that can increase profit, he might encounter resistance to change, based on
the tendency for the status quo. The industry is changing, but the culture and legacy of
“how we do things” might be hard to deal with.
Sales agents: as explained in Q4, the incentives of the agents are not 100% aligned
with the company’s goals. While the company pays a price for over-stocking, agents
pay no price. It’s a valid tactic for them to ensure that they don’t lose any clients.
Aligning the incentives could be crucial; they can also complain about the reallocation of
their time for other activities.
Production: The production managers might feel uncomfortable with producing fewer
newspapers, since they’re used to running larger batches. Reducing volume could
mean needing fewer workers on the shop floor, which may make them feel like they’re
losing control or influence over company resources.
Distribution: 🚨multiple stakeholders🚨 In case that strategy 3. Or any other policy related to delivery days or
times, Assaf will face some complaints from the distribution department, who may
perceive the changes as an additional tasks for the week(planning and execution),
creating imminent friction.
Research team: Yedioth has a research team. Assaf is suggesting new models and will
need to go through them. He might experience some push back from them. Moreover,
we should remember that the current data is limited and real implementation of the
model will demand much more data collection based on the 8,000 retailers.

S2_Section B :Team Lions: Hamamoto, Esquivel, Haque, Vole
Case : The Yedioth Group
Appendix:
Question Number 1 Table Predicting Means(μ) and q*
Retailer
ID
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
Grand Total

μ
4.51
5.74
1.87
2.04
3.28
3.78
3.98
14.70
4.91
3.41
4.29
4.31
2.31
2.72
4.80
6.74
5.09
2.12
6.04
3.41
3.09
4.39
5.39
1.80
8.83
3.48
2.33
6.80
2.06
8.09
4.91
2.76
3.87
2.43
4.19
2.85
3.87
3.71
3.33
9.15
3.96
3.76
3.30
3.88
1.76
6.44
5.78
1.66
3.14
4.32
215.4

σ
2.00
2.18
1.05
1.49
1.64
1.98
1.65
4.18
1.87
1.59
2.18
1.33
1.18
1.39
1.79
2.27
1.99
1.07
2.00
1.92
1.35
2.40
2.36
1.41
2.54
1.80
1.90
3.29
1.43
2.82
2.07
1.42
1.87
1.61
1.94
1.78
1.83
1.37
1.69
2.66
1.74
2.12
1.77
1.36
1.25
2.06
2.26
1.39
1.23
1.63

k q*(Not Roundup)
2.32
9.14
2.32
10.79
2.32
4.30
2.32
5.50
2.32
7.09
2.32
8.37
2.32
7.80
2.32
24.39
2.32
9.25
2.32
7.09
2.32
9.34
2.32
7.39
2.32
5.06
2.32
5.95
2.32
8.96
2.32
11.99
2.32
9.70
2.32
4.61
2.32
10.68
2.32
7.87
2.32
6.21
2.32
9.96
2.32
10.87
2.32
5.07
2.32
14.72
2.32
7.65
2.32
6.73
2.32
14.44
2.32
5.38
2.32
14.63
2.32
9.73
2.32
6.05
2.32
8.21
2.32
6.18
2.32
8.69
2.32
6.97
2.32
8.12
2.32
6.88
2.32
7.24
2.32
15.32
2.32
7.99
2.32
8.68
2.32
7.42
2.32
7.02
2.32
4.66
2.32
11.23
2.32
11.03
2.32
4.89
2.32
6.00
2.32
8.09

q*(Roundup)
10
11
5
6
8
9
8
25
10
8
10
8
6
6
9
12
10
5
11
8
7
10
11
6
15
8
7
15
6
15
10
7
9
7
9
7
9
7
8
16
8
9
8
8
5
12
12
5
6
9
456

Question Number 3 Pooled by agents data
Aggregate retailors for each Sales Agent 1
Aggregate retailors for each Sales Agent 2
Aggregate retailors for each Sales Agent 3
Aggregate retailors for each Sales Agent 4
Aggregate retailors for each Sales Agent 5
Aggregate retailors for each Sales Agent 6
Aggregate retailors for each Sales Agent 7
Aggregate retailors for each Sales Agent 8
Aggregate retailors for each Sales Agent 9
Aggregate retailors for each Sales Agent 10
9165

μ
25.60
18.08
14.11
19.22
32.17
23.50
14.45
20.05
29.18
19.00
215.37

σ
4.68
3.94
3.49
4.17
5.72
4.49
3.40
3.70
5.57
3.60

σ2
21.94
15.49
12.21
17.38
32.70
20.19
11.58
13.69
30.98
12.94

k Safety Stock
2.32
11
2.32
9
2.32
8
2.32
10
2.32
13
2.32
10
2.32
8
2.32
9
2.32
13
2.32
8
99

q* q*(Roundupup)
36
37
27
28
22
23
29
29
45
46
34
34
22
23
29
29
42
43
27
28
315
320

