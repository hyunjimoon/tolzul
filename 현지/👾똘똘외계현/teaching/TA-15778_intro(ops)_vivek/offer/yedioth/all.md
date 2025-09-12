### Final Grade & Feedback

Q1: 15/15
Q2: 15/15  
Q3: 15/15
Q4: 15/15
Q5: 10/10
Bonus: 0/10 [Only censoring mentioned, no distribution assumption]

**Total: 65/80**

---

Alligators (Section A): Operations Management HW2
Linds Colton, Astrid Ericsson, Akira Nasu, Pedro Rodriguez, Weizhao Tan
# Q1. In the current distribution model, where each retailer is supplied once, independently of all other
retailers. What would be a good method to compute the quantity shipped to each retailer if one wishes to
guarantee that 99% of customers will be served? Apply your approach to compute recommended
quantities to the 50 retailers (explain the methodology in the body of the report and provide the results in
appendix).
Step 1: For each of the 50 retailers, we calculated the weekly mean sales quantity (μ) and the weekly
standard deviation (σ).
Note: Logically it seems that including sell-through could result in an underestimate of the total
demand, as we will not know if another customer wanted to buy the magazine, after the retailer
was sold out. 🚨sales data underestimates true demand due to stockouts🚨
However when checking the numbers, in the scenario where we exclude the sell-through
retailers, compared to the scenario where we include them, we find that including them actually
results in a higher average.
(a) Sell-through could have happened because of supply constraints (e.g. if the retailer who
sold out had only 1 magazine that week). If this was the more common case, the mean
would be lower when including sell-through retailers.
(b) Sell-through could also have happened because of unusually high demand (e.g. if the
retailer who sold out already had a lot of magazines, but still sold out). If this was the
more common case, the mean would be higher when including sell-through retailers. This
is because excluding these data-points means excluding higher than average sales.
Therefore, we chose to include the data point (the week for that retailer) with sell-through, as we
calculated both cases, and the mean increased when including sell-through (i.e., we are at least
closer to actual demand than if we didn’t include retailers with sell-through).
Step 2: We counted the number of weeks listed per retailer. Almost all the 50 customers had data for
more than 30 weeks, therefore we assume (based on Central Limit Theorem) that the weekly data for
each retailer would approximate to a normal distribution.
Step 3: To get the 99% guaranteed quantity, we first use the standard normal distribution Z.
P(Z≧b) ＝ F(2.33)＝0.9901
The level to stock our individual retailers is:
Z ≧ 2.33

⇒ (X-μ) / σ ≧ 2.33
X＝μ + 2.33σ

This means that we should stock each of our individual retailers to 2.33 s.d. above their mean
sales. We also round up to the nearest integer.
(Results found in Appendix 1. For example, Retailer 1 should stock 9 copies per week, Retailer 2 should
stock 10 copies per week etc.)
# Q2. If Yedioth could implement full pooling among all of the 50 retailers what would be the estimated
benefit in terms of total production levels and returns (assume that the required service level is 99%).
Note: Full pooling means that somehow all of the retailers could be supplied in real time from the same
pool of inventory.
Step 1: Consider the available data for each of the 46 weeks across the 50 retailers, and assume that
missing data means that the retailer sold zero copies that week.

1

Alligators (Section A): Operations Management HW2
Linds Colton, Astrid Ericsson, Akira Nasu, Pedro Rodriguez, Weizhao Tan
Step 2: For each of the 46 weeks, sum up the total copies sold across the 50 retailers. Data is in
Appendix 2.
Step 3: Calculate the mean and s.d. for the dataset of 46 weeks’ total sales.
Mean sales
(n=46)
189.6

STD
20.0

X for
P(Z<2.33)
236.2

X
(roundup)
237.0

This full pooling results in 237 copies per week.
Estimated benefit of production levels from full pooling (reduction amount)

= 419 - 237
= 182 copies per week

Step 4: Estimate the expected number of returns using the safety stock portion of the shipment. Since the
total shipment is set to μ + 2.33σ and the expected sales are μ, the difference (2.33σ) represents the
expected number of returns.
Estimated returns

= 237 - 190 (or 2.33 * 20.0) = 47.0

Step5: Calculate the total number of returns under Q1, which results in a total of 229 units (=419 - 190).
Based on this figure, estimate the benefit of returns from full pooling.
Estimated benefit of returns from full pooling (reduction amount)

= 229 - 47
= 182 returns per week 🚨correct calculation ~237🚨

# Q3. Suppose that one could implement full pooling only among retailers that are treated by the same
sales agent, what would be the potential benefit in terms of production levels and returns (assume 99%
service level). Compare to Question 2 above.
We do a partial pooling for retailers handled by the same sales agent, i.e. each sales agent contributes to
a separate pooled risk.
Under this structure, the total recommended production level and returns to meet a 99% service level
are
● 293 copies per week (we got 286.5, and rounded each one up). See Appendix 3.
●

103 returns per week (=production levels 293 – average sales 190).

This is to be compared to:
● 237 copies and 47 returns/week under full pooling.
→ Pooling among retailers handled by the same sales agent, partial pooling (293 copies and 103
returns / week) is not as optimal as full pooling (237 copies and 47 returns / week). 🚨compares to both extremes🚨

2

Alligators (Section A): Operations Management HW2
Linds Colton, Astrid Ericsson, Akira Nasu, Pedro Rodriguez, Weizhao Tan
# Q4. Propose more realistic policies that leverage the fact that the sales agent visits each retailer in
the middle of the week. What would the benefit be of these policies?
●

●

By using the Wednesday sales agent visit to assess first-half sales and inventory levels at each
retailer, Yedioth can reduce the shipment volume from the guaranteed quantity for each retailer to
the guaranteed quantity for each agent’s retailer.
There is also the opportunity to divert excess stock from retailers who have many remaining
copies to retailers who are close to running out, or have already sold out.
Note: We have chosen to release all the magazines to the retailers at the beginning of the week
to avoid missed sales, and to minimise coordination between the 10 sales agents. We could
alternatively choose to withhold a portion of the safety stock at a centralized location and take
advantage of the full pooling (i.e. reduced amount of safety stock), but this will require
coordination between the 10 sales agents.

●
●

Reallocating inventory based on actual midweek data allows for more accurate restocking,
compared to only stocking on Sunday.
By reallocating unsold copies to retailers who need more inventory, we reduce the risk of sellthrough and thereby capture more demand and ultimately revenue.
○ On the other hand, by reducing inventory at retailers not moving magazines for the week
and transferring them to the high-moving retailers, we reduce overall refund costs (2535% of magazines are returned in the current structure) and scrapping costs, as well as
reduce collection and reverse supply chain logistic costs, which thereby reduces the
firm’s expenses.
○ By increasing revenue and reducing expenses, we increase the bottom line: profit. 🚨rebalancing mechanism proposed🚨

Example, for sales agent 1 (who is in charge of retailers 1, 15, 16, 42, 47):
Retailer Number

1

15

16

42

47

99% demand
level (no pooling,
from Q1)

9
magazine
s

9
magazine
s

12
magazine
s

9
magazine
s

11
magazines

Agent distributes
on Sunday

9 / 50 *
35
= 6.3

9 / 50 *
35
= 6.3

12 / 50 *
35
= 8.4

9 / 50 *
35
= 6.3

11 / 50 *
35
= 7.7

≈ 6 mags

≈ 6 mags

≈ 9 mags

≈ 6 mags

≈ 8 mags

Total = 50
magazines

Total = 35
magazines (from
Q3, agent pooling)

On Wednesday, the agent will call each of the 5 retailers to ask for the quantity of unsold magazines. He
will then redistribute the unsold magazines.
Some ways to redistribute the unsold stock on Wed are as follows:
(a) Based on the 99% demand level proportions again - 2nd half sales independent of 1st half
(demonstrated below)
(b) Based on the proportion of sales from Monday to Wednesday - 2nd half sales dependent on 1st
half
(c) A hybrid with a fixed minimum quantity and a variable quantity based on first half sales. - hybrid
The chosen option will require more data that splits Mon-Wed sales from the rest of the week.

3

Alligators (Section A): Operations Management HW2
Linds Colton, Astrid Ericsson, Akira Nasu, Pedro Rodriguez, Weizhao Tan
By having inventory available in stores that would have otherwise experienced sell-through, the firm can
collect more accurate demand data, which can be used in future stocking decisions → less reliance on
reallocation of inventory moving forward.

Q5. What do you think are the organizational challenges that Assaf will have to address?
Uncertainty of Demand - Safety Stock
●

●

If Assaf does indeed decide to go with a 99% service level, that means that the Yedioth will end
up refunding and scrapping a lot of their “safety stock” as the result of a high service level. This is
because of the following principle:
○ Uncertainty (standard deviation) is the mismatch that causes friction between supply and
demand → uncertainty drives inventory costs
○ For increasing safety stock (k) to meet the high moving customers, the amount of
inventory the firm will have to produce will grow non-linearly
○ In other words, the “cost of doing business” is a potentially a large price to pay for
uncertainty
Margins impact decisions to “under” or “over” stock and Assaf will need to start finding the
optimal k, by analysing the per unit cost of producing one unit, the per unit cost of sale, and the
per unit cost to return and scrap. These values needed for k were not given in the case. Optimal k
may be less than 2.33 (correspond to less than 99%).

Align Sales Agent Incentives
●

●

The key organizational challenges are:
○ The need to shift Yedioth’s conservative culture, which emphasizes employee loyalty and
cautious decision making;
○ The resistance from the research department and sales agents, who may be reluctant to
accept any operational change that could negatively impact sales.
To overcome these challenges, Assaf should introduce a revised incentive model that rewards
not only higher sales but also lower return rates. This would help align the interests of the sales
agents with company-wide efficiency goals. 🚨agent incentives🚨

Invest in Technology
●

●

They need to make better predictions: the research department should consider investing in
technologies like EDI and RFID to enable timely access to sales data, which would support more
accurate forecasting and replenishment decisions. Also, by analysing the sales trend on a daily
basis, centralizing some magazines left in an office on Monday, and adjusting how to redistribute
the remaining magazines among agents on Wednesday, they can reduce the shipment volume
from Question 3 to Question 2. It is one of the solutions for them to reduce the standard deviation
from 41.7(sum of each agent’s retailer) to 20.0.
Assaf will most likely face push-back for technology investments if the stakeholders don’t
understand the benefit OR they will want to pass on the cost to retailers, many of which are small
retailers who don’t yet have EDI connections and are unlikely to invest on their own.

Creates Alignments with Research
●

Through better incentives and improved data systems, both the research and sales teams can be
encouraged to actively participate in reducing waste and improving operational performance.

4

Alligators (Section A): Operations Management HW2
Linds Colton, Astrid Ericsson, Akira Nasu, Pedro Rodriguez, Weizhao Tan
Appendix 1: (Retailers Supplied Independently)
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

Step 1
μ

σ

Step 2
Total weeks (i.e.
number of samples)

X

Step 3
X (roundup)

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

8.4
10.0
3.3
4.6
6.5
7.6
7.7
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

9.0
10.0
4.0
5.0
7.0
8.0
8.0
24.0
9.0
7.0
9.0
7.0
5.0
6.0
9.0
12.0
9.0
4.0
10.0
8.0
6.0
10.0
11.0
5.0
15.0
7.0
7.0
14.0
5.0
15.0
10.0
6.0
8.0
6.0
8.0
7.0
8.0
6.0
7.0
15.0
8.0
9.0
7.0
6.0
4.0
11.0
11.0
4.0
6.0
7.0

Total:

393.8

419.0

5

Alligators (Section A): Operations Management HW2
Linds Colton, Astrid Ericsson, Akira Nasu, Pedro Rodriguez, Weizhao Tan
Appendix 2: (Full Pooling Amongst Retailers)
Week
14/7/2008
21/7/2008
28/7/2008
11/8/2008
18/8/2008
25/8/2008
1/9/2008
15/9/2008
21/9/2008
27/10/2008
10/11/2008
17/11/2008
24/11/2008
8/12/2008
15/12/2008
22/12/2008
5/1/2009
12/1/2009
19/1/2009
26/1/2009
9/2/2009
16/2/2009
23/2/2009
9/3/2009
16/3/2009
20/4/2009
11/5/2009
18/5/2009
8/6/2009
15/6/2009
22/6/2009
29/6/2009
13/7/2009
20/7/2009
27/7/2009
10/8/2009
17/8/2009
24/8/2009
31/8/2009
12/10/2009
19/10/2009
26/10/2009
9/11/2009
16/11/2009
23/11/2009
30/11/2009

Sales per week
170.0
143.0
173.0
175.0
172.0
158.0
192.0
215.0
199.0
181.0
184.0
198.0
181.0
181.0
201.0
192.0
208.0
180.0
197.0
185.0
186.0
232.0
207.0
206.0
165.0
192.0
201.0
208.0
177.0
179.0
188.0
183.0
238.0
216.0
198.0
189.0
193.0
181.0
195.0
242.0
184.0
189.0
184.0
148.0
184.0
171.0

6

Alligators (Section A): Operations Management HW2
Linds Colton, Astrid Ericsson, Akira Nasu, Pedro Rodriguez, Weizhao Tan
Appendix 3: (Partial Pooling of Retailers, Handled by Same Sales Agent)

Sales Agent

Avg Sales

STD

X if P(Z<2.33)

X (roundup)

1

22.4

5.2

34.5

35.0

2

15.8

4.0

25.1

26.0

3

12.8

2.8

19.3

20.0

4

17.6

3.4

25.5

26.0

5

28.0

6.4

42.9

43.0

6

22.2

4.3

32.2

33.0

7

11.2

2.5

17.0

18.0

8

15.7

3.3

23.4

24.0

9

28.0

5.7

41.3

42.0

10

15.8

4.1

25.4

26.0

TOTAL

189.5

41.7

286.6

293.0

7

