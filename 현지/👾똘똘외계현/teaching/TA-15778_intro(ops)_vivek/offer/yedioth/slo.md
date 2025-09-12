### Final Grade & Feedback
Q1: 15/15
Q2: 15/15
Q3: 15/15
Q4: 10/15 [No quantitative example provided]
Q5: 10/10
Bonus: 0/10
**Total: 65/80**

15.778 Operations Management

Yedioth Case Report
Sloth Study Group in Section A

Members:
Kenji Igawa, Minato Kichise, Mwanaidi Kitondo, Zuansah Munggraran, Nicolas Musalem

Questions:
​
1. In the current distribution model, where each retailer is supplied once, independently
of all other retailers, what would be a good method to compute the quantity shipped to
each retailer if one wishes to guarantee that 99% of customers will be served? Apply
your approach to compute recommended quantities to the 50 retailers (explain the
methodology in the body of the report and provide the results in appendix).
To guarantee that 99% of the customers will be served, we used the following approach:
We are assuming that the sales have a normal distribution for each retailer. 99% is
equivalent to k=2.33 for the normal distribution. So we used q*=Mu+k*sigma for each
retailer. Finally, we added all the projected deliveries for the 50 retailers and arrived at
🚨419🚨 as the optimal delivery quantity. ​
See Figure 1 below for Excel solution utilized. ​

2. If Yedioth could implement full pooling among all of the 50 retailers what would be the
estimated benefit in terms of total production levels and returns (assume that the
required service level is 99%). Note: Full pooling means that somehow all of the
retailers could be supplied in real time from the same pool of inventory.
We first sorted the data by sales by week, then summed up the sales for that week.
Next, we took the averages of the quantity of sales across each week as well as its
standard deviation and the results were 189.69 and 19.98 respectively. We then took
q*=meu+k*sigma, with k being 2.33 to reflect 99%, and the result is 236.16, or 🚨237🚨
rounded up for delivery quantity per week for all 50 retailers. This quantity is lower than
the 419 value compared to #1 which will mean decreased production. ​
See Figure 2A below for Excel solution utilized.

Regarding assessing returns, we first calculated the weekly average returns for all
retailers which is 110.79. For full pooling, we first came up with the expected returns by
subtracting from quantity supplied (237) the expected demand or mean (190) and
arrived at 47. The difference between the initial return and the expected returns from
pooling is 64. Therefore there will be 64 fewer expected returns when pooling compared
to allocating by retailer. There will be a reduction of returns from 26.5%(111/419) to
19.8% (47/237) of quantity supplied. ​
See Figure 2B below for Excel solution utilized.

3. Suppose that one could implement full pooling only among retailers that are treated
by the same sales agent, what would be the potential benefit in terms of production
levels and returns (assume 99% service level). Compare to 2) above.
We started by sorting data by sales per week and by sales agent. We took the average
sales each agent made across all 46 weeks as well its standard deviation. We then
calculated the expected delivery quantity q* for each agent utilizing the formula
meu+k*sigma, with k being 2.33 to reflect 99% service level. Next, we took the sum of
all the q* for all the agents and arrived at 🚨293🚨, which is the quantity supplied. We then
determined the expected demand or meu, by adding the average quantity each agent
supplied and arrived at 190. We arrived at the expected returns to be 103 by subtracting
the expected demand of 190 from the quantity supplied of 293.​
See Figure 3 below for Excel solution utilized.
Compared to 2, the production of 293 is more than #2’s 237, and the expected return of
103 is greater than #2’s expected return of 47. This option is not the preferred option
compared to 2 since it more than doubles the number of returns.

4. Propose more realistic policies that leverage the fact that the sales agent visits each
retailer in the middle of the week. What would the benefit be of these policies?
-​ 🚨Maintain safety stock with the sales agent🚨 instead at the 50 retailers. This would
be a full polling at an intermediate level. The sales agent can stock the retailers
as needed when they visit in the middle of the week. This would reduce variability
and returns, as showed in question 2.
-​ For larger retailers utilize EDIs to provide real-time data on stocks and replenish
them as necessary. Utilize RFID system at smaller retailers where EDI is
unavailable so that sales agents have real-time data on stocks and replenish
them at retailers as necessary. With this solution, we can avoid the weekly visit to

check inventory and have real-time demand data to better predict next
production.
-​ Experiment with predicted stock values at lower percentages than 99% to
determine optimal safety stock levels and maximize profit, utilizing unit cost (c),
unit revenue (r), and unit salvage value (b) to inform desired predicted stock
levels (%). This could result in a figure different from 99% of safety stock as an
optimal solution.

5. What do you think are the organizational challenges that Assaf will have to address?

-​ Investment: A significant investment will be required to introduce new
technologies, and this must be weighed against the benefits of improved
inventory control.
-​ Resistance to Change: Yedioth has a culture of loyalty and caution in
decision-making. Any initiative that reduces print volumes may be perceived as a
threat by employees accustomed to traditional practices. This resistance is
common in an established industry with a history of low innovation.
-​ 🚨Sales Agent Incentives🚨: Sales agents are compensated based on sales volume,
which may make them resistant to reduced supply strategies, even if these
strategies improve overall efficiency.
-​ Coordination with the Research Department: The Research Department,
responsible for determining shipment quantities, may resist relinquishing control
to a new data-driven system or model.
-​ Technological Readiness: Implementing pooling or mid-week replenishment
strategies may require better IT infrastructure, especially for data collection from
small retailers.
-​ Cross-Department Collaboration: Ensuring successful implementation will require
collaboration across distribution, research, sales, and IT departments, which can
be organizationally complex.
-​ Training and Communication: Staff will need training to understand the benefits
and rationale behind the new system. Without strong internal communication,
resistance and misunderstandings could derail the process.

Figure 1

Figure 2a

Figure 2.b

Figure 3

Sum of Sales
Row Labels

Column Labels
1
2 3 4 5 6 7 8 9

10 Grand Total

7/14/08

17

11

13 18 21

27

11 16 30

6

170

7/21/08

15

10

15 14 19

24

7

12 20

7

143

7/28/08

20

10

13 12 26

28

10 15 30

9

173

8/11/08

16

13

11 20 28

23

13 12 28

11 175

8/18/08

24

13

13 12 22

19

11 15 26

17 172

8/25/08

25

6

10 13 18

26

8

13 24

15 158

9/1/08

34

13

10 19 29

19

8

15 26

19 192

9/15/08

29

12

11 22 32

20

11 16 39

23 215

9/21/08

28

18

14 22 20

24

13 18 28

14 199

10/27/08

22

16

8

17 18

25

11 24 28

12 181

11/10/08

22

15

11 15 29

21

12 9

31

19 184

11/17/08

24

16

10 22 31

15

11 17 36

16 198

11/24/08

25

14

9

19 18

25

13 15 29

14 181

12/8/08

17

17

7

18 26

19

10 15 33

19 181

12/15/08

24

12

15 13 35

20

17 11 34

20 201

12/22/08

30

15

9

16 19

22

14 19 29

19 192

1/5/09

29

16

12 19 30

25

14 17 27

19 208

1/12/09

21

16

11 16 31

22

10 12 25

16 180

1/19/09

24

16

16 20 24

19

10 18 29

21 197

1/26/09

31

15

14 18 23

19

6

15 31

13 185

2/9/09

19

19

14 13 25

22

11 14 31

18 186

2/16/09

25

14

18 22 37

28

12 18 36

22 232

2/23/09

27

16

13 18 35

18

10 21 35

14 207

3/9/09

26

18

13 18 34

24

11 10 29

23 206

3/16/09

25

16

16 11 22

18

9

17 165

14 17

4/20/09

21

21

16 21 26

24

9

14 21

19 192

5/11/09

19

22

12 15 29

22

12 14 37

19 201

5/18/09

23

23

15 10 38

19

10 15 36

19 208

6/8/09

21

10

13 17 37

21

6

17 21

14 177

6/15/09

20

6

13 22 35

18

10 15 27

13 179

6/22/09

22

16

13 18 30

14

9

12 38

16 188

6/29/09

23

18

12 19 37

13

12 10 24

15 183

7/13/09

34

20

17 22 36

28

12 17 35

17 238

7/20/09

22

18

14 19 37

29

11 14 32

20 216

7/27/09

18

18

9

21 31

29

12 16 33

11 198

8/10/09

17

16

15 15 34

24

16 16 19

17 189

8/17/09

17

20

17 20 33

19

12 18 20

17 193

8/24/09

19

18

11 20 26

20

17 12 21

17 181

8/31/09

13

16

10 21 31

29

15 20 23

17 195

10/12/09

30

23

19 19 36

33

15 16 31

20 242

10/19/09

23

18

12 21 26

16

8

20 23

17 184

10/26/09

16

17

17 19 33

21

11 18 20

17 189

11/9/09

22

20

11 19 24

19

12 23 23

11 184

11/16/09

11

11

9

16 19

25

10 13 25

9

11/23/09

23

21

12 18 18

23

13 19 25

12 184

11/30/09

19

19

16 11 22

22

11 20 22

9

Average Sales

22

16

13 18 28

22.2 11 16 28

Std Deviation

5

4

2.8 3.4 6.38 4.32 2.5 3.3 5.7

4.1

q*=Mu+2.33*sigma 35

26

20 26 43

26 293

Grand Total

1032

148

171

728 589 810 1290 1020 516 720 1287 729 8721

33

18 24 42

16 190

Expected returns 103

