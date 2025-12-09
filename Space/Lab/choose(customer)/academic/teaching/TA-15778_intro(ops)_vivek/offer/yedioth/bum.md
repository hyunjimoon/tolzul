### Final Grade & Feedback

Q1: 10/15 [Calculated 394, outside ±5% range of 419]
Q2: 15/15
Q3: 15/15
Q4: 10/15 [No quantitative example provided]
Q5: 10/10
Bonus: 0/10 [Only censoring mentioned, no distribution assumption]
[[🗄️🧠scott]]
**Total: 60/80**

---

15.778 Operations Management
Yedioth Case
1 August 2025
Team:
Alexandra Diaz Arias
Michael Fischer
Kwame Owusu Arhin
Tshung Yu Lim
Derek Wilson
1. In the current distribution model, where each retailer is supplied once a week independently
of all other retailers, what would be a good method to compute the quantity shipped to each
retailer to guarantee that 99% of customers will be served? Apply your approach to compute
recommended quantities to the 50 retailers (explain the methodology in the body of the report
and provide the results in appendix).
When each retailer (n) is supplied independently once a week, we should look at the mean (μn)
and standard deviation (σn) for each retailer across the historical data that we have.
With this information, we can determine the optimal quantity (q*) for each retailer:
qn*= μn+ k99 × σn (where k99 ≈ 2.32)
See Appendix 1 for the recommended quantities for all 50 retailers to ensure 99% service level at
each location. Totaling these recommended quantities, we would need to print 393.3 (round up to
394) magazines. 🚨calculated 394, outside range🚨

This method of calculating q* for each retailer assumes that when there is a sell-through, the
amount sold exactly matches demand for that week. We understand that this does not reflect the
true demand of the week and demand may have been higher than the amount sold. 🚨censoring awareness🚨
2. If Yedioth could implement full pooling among all of the 50 retailers, what would be the
estimated benefit in terms of total production levels and returns if the required service level is
99%? (Note: Full pooling means that somehow all of the retailers could be supplied in-real-time
from the same pool of inventory.)
As shown in Appendix 2, based on the method of full pooling effect of 50 retailers,
the expected weekly sales (μn) is 189.59 with a standard deviation (σn) of 19.77.
The required service level of 99% the stock level (qn*) is: 235.65 🚨correct pooling ~236🚨
The estimated benefit of implementing full pooling among all the retailers is that we reduce the
service inventory to 236 (rounded up to the nearest whole number) and reduce the number of
expected returns to 46.

1

This shows that pooling reduces the standard deviation significantly, which resulted in a lower q
based on qn*= μn+ k99 × σn
As compared to when stocking individually, the stock of each location is calculated with a separate
standard deviation which induces higher variability and a wider spread of standard deviation
resulting in a much higher inventory level required as compared to pooling. When pooling, there
is a probability that one location has a high week of sales; it is likely to be offset by another location
having low weekly sales.
3. Suppose that one could implement full pooling only among retailers that are treated by the same
sales agent. What would be the potential benefit in terms of production levels and returns,
assuming 99% service level? Compare to your #2 answer.
Implementing full pooling per sales agent will still result in significant improvement compared to
stocking each location individually (question 1), although the magnitude of improvement will be
lower than full pooling across the entire portfolio (question 2).
To maintain 99% service level when pooling by sales agent, Yedioth should produce 286.23 (round
up to 287) magazines each week. 🚨correct agent pooling🚨 See Appendix 3 for the calculation of 99% safety stock for each
sales agent.
In Table 1 below, we can compare the benefits in production levels and returns across the three
scenarios: no pooling, pooling all retailers, and pooling by sales agent. This assumes that Yedioth
distributes all magazines that are produced, such that:
Expected Returns = Total Production - Expected Sales.
Pooling by sales agent results allows Yedioth to reduce production by 107 (394-287) magazines
each week and will result in 107 fewer expected returns (204-97) compared to the no pooling
scenario (question 1).
When compared to full pooling of all retailers (question 2), pooling by sales agent will require
production of an additional 51 (287-236) to maintain a 99% service level and result in 51 more
expected returns (97 - 46).
Table 1. Comparisons between 3 scenarios
99% Service
Stock

Production
Savings vs
No Pooling

Expected
Sales

Expected
Returns

Return
Savings vs
No Pooling

No pooling (Q1)

394

-

190

204

-

Pooling Across all Retailers
(Q2)

236

158

190

46

158

Pooling by Sales Agent (Q3)

287

107

190

97

107

2

4. Propose more realistic processes/strategies that leverage the fact that the sales agent visits each
retailer in the middle of the week. What would the benefit be of these processes/strategies?
A more realistic process that can leverage the visits that the sales agents make in the middle of the
week is the checking and restocking of that week based on the sales in the first half of the week.
Visits by the sales agents midweek will lower the probability of stock out, because it lowers
standard deviation and reduces the variability. The variability is lower because it reflects the
consumer purchase flow more accurately or closer to it by adjusting from the first half of the week
to the second half. This is done by adjusting inventory levels, q and top up accordingly based on
sales trends in the first half of the week. At mid-week, the trends at the beginning of the week can
inform quantities during the 2nd half of that week. This strategy will need to ensure that sales are
distributed evenly throughout the week.

As shown in the figure above, a smaller standard deviation would result in a narrower distribution
curve.
This shows that for 1 standard deviation away from the mean, the probability of stockout would
be lower due to the area under the curve being larger with a narrower curve. This explains that the
probability of a stockout is lower p(D>C). This would result in a lower required inventory for a
99% stock level, resulting in better control with less financial stress on cash flow.
Moreover, with the assistance of RFID on inventory tracking, 🚨specific mechanisms🚨 this real time tracking supplies stock
updates to sales rep in an efficient way which allows them to understand the demand more
accurately and carry inventory with them during mid-week visits to prevent any stockouts.

3

5. What do you think are the organizational challenges that Assaf will have to address?
Assaf will primarily need to overcome resistance to change from the two key stakeholder groups
affected by the change in management. The first is the R&D department, which currently makes
decisions regarding stocking and distribution quantities. Their main concern will likely be a
perceived loss of influence on decision-making and the potential impact on their strategic
relevance. To address this, it is recommended for Asaf to frame their optimization initiative as to
unlock additional cash flow and budget flexibility. These benefits can directly enhance the
department’s innovative capacity and impact.
On the other hand, sales agents who are responsible for (and compensated based on) sales levels
may perceive this shift as a risk of meeting demand and fear potential lost sales. To address this
concern, it will be important to communicate that the optimization model is designed to align
production more closely with actual demand patterns.
Secondly, 🚨multiple stakeholders🚨 in the past, sales representatives were compensated based on sales and as such were
incentivized to sell as much as possible. Going forward Asaf will have to review the compensation
mechanism and add some form of penalization to the compensation structure - if there is sell
through. Our recommendation is that bonuses should be made to keep low production levels while
having a sell-through rate of less than 1%.
The final organizational challenge is overcoming the aversion to technology. Assaf will have to
get the sales agents to embrace the use of technology to make work more efficient and to develop
strategies that help aggregate data quickly, making them more useful and easily adaptable.

4

Appendix 1. 99% Service Stock When Stocking Each Customer Independently (No Pooling)
Customer (n)

Avg Sales (u)

Std. Dev (σ)

99% Service Stock (q*)

1

4.27

1.76

8.36

2

5.45

1.94

9.95

3

1.61

0.74

3.34

4

1.80

1.19

4.55

5

3.09

1.46

6.47

6

3.61

1.73

7.63

7

3.93

1.60

7.65

8

14.43

3.91

23.51

9

4.73

1.62

8.48

10

3.17

1.37

6.36

11

4.00

1.86

8.32

12

4.07

1.01

6.41

13

2.24

1.11

4.82

14

2.46

1.13

5.08

15

4.56

1.58

8.23

16

6.52

2.01

11.18

17

4.78

1.70

8.72

18

1.86

0.80

3.73

19

5.85

1.76

9.94

20

3.25

1.74

7.29

21

2.78

1.01

5.12

22

4.20

2.15

9.17

23

5.14

2.10

10.00

24

1.57

1.15

4.23

25

8.74

2.39

14.28

26

3.15

1.48

6.57

27

2.16

1.70

6.11

28

6.65

3.11

13.86

29

1.94

1.26

4.86

30

8.00

2.68

14.23

31

4.80

1.94

9.30

5

32

2.59

1.24

5.46

33

3.67

1.61

7.40

34

2.22

1.30

5.23

35

3.95

1.66

7.81

36

2.67

1.55

6.27

37

3.61

1.58

7.28

38

3.40

1.08

5.92

39

3.04

1.41

6.32

40

9.07

2.51

14.88

41

3.70

1.47

7.11

42

3.74

2.09

8.59

43

3.07

1.47

6.47

44

3.38

0.92

5.50

45

1.48

0.94

3.65

46

6.35

1.92

10.81

47

5.51

2.03

10.21

48

1.43

1.07

3.90

49

2.93

1.27

5.87

50

4.00

1.22

6.84

Total Stock (99% Service)

393.30

6

Appendix 2. 99% Service Stock When Pooling effect based on weekly sales.
Date

Summary of
Sales

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
7

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

8

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

(blank)
Grand Total

8721

Average weekly sales

189.59

standard deviation

19.77

99% stock level with pooling

235.65

9

Appendix 3. 99% Service Stock when Pooling by Sales Agent

Sales Agent

Avg Weekly Sales

Std Dev

99% Service Stock

1

22.43

5.18

34.44

2

15.83

3.96

25.02

3

12.80

2.80

19.30

4

17.61

3.38

25.46

5

28.04

6.38

42.85

6

22.17

4.32

32.19

7

11.22

2.50

17.02

8

15.65

3.31

23.34

9

27.98

5.70

41.21

10

15.85

4.11

25.39

Total Stock (99% Service)

286.23

10

