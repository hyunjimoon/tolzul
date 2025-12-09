### Final Grade & Feedback

Q1: 10/15 [Calculated 393, outside ±5% range of 419]
Q2: 15/15
Q3: 15/15
Q4: 10/15 [No quantitative example provided]
Q5: 10/10
Bonus: 0/10 [Only censoring mentioned, no distribution assumption]

**Total: 60/80**

---

Yedioth case
Team Ostrich: Abdulla Alqahtani, Leyla Khanahmad, Peggy Poon, James Watson, Kaz
Takagi
1.
The following standard service level formula was used to ensure that 99% of customer
demand would be met:
Q∗=Average Sales+K99% * (σ) Standard Deviation
We need to find the average sales and standard deviation σ for each customer over the
weeks (data provided in the excel).
-

The constant K for a 99% service level is 2.33
We are assuming No Lost Sales for Sell Through
Our calculation is based on the sales, which is smaller than the actual demand
(the actual demand is not captured in the raw data)

Row Labels

Average of Sales

StdDev of Sales

Recommended
Quantity at 99%

1

4,27

1,76

8,36

2

5,45

1,94

9,95

3

1,61

0,74

3,34

4

1,80

1,19

4,55

5

3,09

1,46

6,47

6

3,61

1,73

7,63

7

3,93

1,60

7,65

8

14,43

3,91

23,51

9

4,73

1,62

8,48

10

3,17

1,37

6,36

11

4,00

1,86

8,32

12

4,07

1,01

6,41

13

2,24

1,11

4,82

14

2,46

1,13

5,08

15

4,56

1,58

8,23

16

6,52

2,01

11,18

17

4,78

1,70

8,72

18

1,86

0,80

3,73

19

5,85

1,76

9,94

20

3,25

1,74

7,29

21

2,78

1,01

5,12

22

4,20

2,15

9,17

23

5,14

2,10

10,00

24

1,57

1,15

4,23

25

8,74

2,39

14,28

26

3,15

1,48

6,57

27

2,16

1,70

6,11

28

6,65

3,11

13,86

29

1,94

1,26

4,86

30

8,00

2,68

14,23

31

4,80

1,94

9,30

32

2,59

1,24

5,46

33

3,67

1,61

7,40

34

2,22

1,30

5,23

35

3,95

1,66

7,81

36

2,67

1,55

6,27

37

3,61

1,58

7,28

38

3,40

1,08

5,92

39

3,04

1,41

6,32

40

9,07

2,51

14,88

41

3,70

1,47

7,11

42

3,74

2,09

8,59

43

3,07

1,47

6,47

44

3,38

0,92

5,50

45

1,48

0,94

3,65

46

6,35

1,92

10,81

47

5,51

2,03

10,21

48

1,43

1,07

3,90

49

2,93

1,27

5,87

50

4,00

1,22

6,84

Grand Total

4,14

2,94

393,30

Total safety stock (Q*) is calculated at 393,30.

2.
To calculate whether Yedioth can implement full pooling across all 50 retailers, we followed
these steps:
-

Filtered the sales data by date and aggregated total sales
Using this data, we applied the standard service level formula to calculate the
recommended order quantity needed to achieve a 99% service level
We then repeated the process for the returns data

3.
To assess the impact of implementing full pooling among retailers managed by the same sales
agent, we organized the 50 retailers into groups according to their assigned agent. For each
agent group, we combined their sales and returns data and used the standard service level
formula to determine the production quantity needed to achieve a 99% service level. We then
calculated the total production required and the expected returns for this agent-based pooling
strategy, and compared these outcomes with those from a scenario where sales and returns are
fully pooled across all retailers (as described in section #2).
-

We are able to see the differences in efficiency and the potential for overproduction
when pooling is limited to agent groupings rather than the entire retailer network.

4.
There are several processes/strategies that Yedioth Group can implement and leverage the
face that the sales agents visits each retailer in the middle of the week. Examples:
-

With 99%, we are overstocked. We lower the overstock.

To minimize excess inventory while maintaining product availability, we explored modifying
the weekly shipment strategy. One approach involves sending a smaller, more cautious initial
shipment to each retailer at the beginning of the week (covering approximately 60–70% of
the anticipated demand). Mid-week, the sales agent would visit each store in their territory to
assess inventory levels. Based on these observations, the agent could identify stores that are
running low or have surplus stock and help facilitate transfers between locations as needed.
This mid-week redistribution would help balance inventory more effectively across stores,
reducing both stockouts and overstock situations.
Alternatively, we considered splitting the weekly delivery into two separate shipments. Under
this model, retailers would receive enough product on Sunday to last for the first half of the
week. Mid-week, after reviewing updated inventory levels, the sales agent could place a
second order for stores requiring replenishment, ensuring adequate stock for the remainder of
the week. Making restocking decisions later in the week based on actual sales data could lead
to improved inventory management overall.

-

Future shipping tuning

We propose using sales data from Monday and Tuesday to refine shipment planning for
future weeks. The process begins with collecting early-week sales figures from each retailer,
which can be done either during the sales agent’s regular visits or through simple check-ins
over the phone or by SMS. By analyzing how products perform at the start of the week, we
can adjust each retailer’s demand forecast for the following week, tailoring shipments more
closely to their actual needs. As this process is repeated over time and more sales data
becomes available, the forecasting model is able to learn and improve, resulting in
increasingly accurate shipment quantities and more efficient inventory management overall.
-

Reallocating within region

Mid-week, typically on Wednesday, the sales agent could visit each of their assigned stores to
check current inventory levels. If some retailers have excess stock while others are running
low or have already experienced stockouts, the agent can step in to physically redistribute
products among stores. By shifting inventory from oversupplied locations to those in need,
this method helps ensure better product availability across the region while minimizing both
shortages and unnecessary surplus.

5.
Some of the organizational challenges that Assaf may need to address include:
-

Limited buy-in from the R&D team

Assaf needs to engage with the R&D team and align closely with them, as they are the ones
responsible for making decisions around distribution and production. It is important to secure
their buy-in and coordinate efforts to ensure successful implementation.
-

Misaligned Incentive Structure for Sales Agents

Assaf needs to align agent incentives with desired outcomes. Currently, agents are
compensated based on gross sales, which can lead to overshipping. To encourage more
accurate ordering and reduce excess inventory, incentives should be tied to actual sellthrough performance.
-

Limited IT Infrastructure

Most small retailers, such as kiosks, do not have real-time inventory tracking or Electronic
Data Interchange (EDI) systems in place. Sales agents gather data manually, and data is often
delayed or inconsistent. Assaf could for example roll out lightweight tech solutions such as
SMS reporting, agent apps, tablet tools etc. to capture inventory snapshots.
-

Cultural resistance to change

As a family-owned business, Yedioth may adopt a more conservative approach to operations,
placing strong emphasis on employee loyalty and organizational stability. This culture can

create resistance to change, especially when introducing new processes or technologies that
challenge long-standing practices. Some stakeholders may perceive data-driven optimization
as a threat to traditional business intuition and long-held practices.
Efforts to improve efficiency, particularly those that involve reducing print volumes, could be
met with internal resistance. Some employees associate high production volumes with
business success and job security. As a result, even well-intentioned changes may be seen as
disruptive or threatening.
-

Institutional Inertia

Significant operational changes, like updating delivery methods, adopting pooling strategies,
or introducing real-time inventory redistribution, are often met with resistance stemming
from entrenched habits and established mindsets. The common mindset of “this is how we’ve
always done things” can hinder or even prevent effective change from taking root.

