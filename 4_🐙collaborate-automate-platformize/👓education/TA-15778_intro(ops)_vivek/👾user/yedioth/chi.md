### Final Grade & Feedback

Q1: 10/15 [Calculated 393, outside ±5% range of 419]
Q2: 15/15
Q3: 15/15
Q4: 10/15 [No quantitative example provided]
Q5: 5/10 [Generic points without specific stakeholders]
Bonus: 0/10

**Total: 55/80**

---

‭15.778 Introduction to Operations Management‬

‭Section B‬

‭Yedioth Case‬
‭Raghavendra Polanki‬
‭Alexey Ershov‬
‭Brendan Owen‬
‭SiTing Han‬
‭Susana Tamayo‬

‭1.‬ ‭In‬ ‭the‬ ‭current‬ ‭distribution‬ ‭model,‬ ‭where‬ ‭each‬ ‭retailer‬ ‭is‬ ‭supplied‬ ‭once,‬
‭independently‬‭of‬‭all‬‭other‬‭retailers.‬‭What‬‭would‬‭be‬‭a‬‭good‬‭method‬‭to‬‭compute‬‭the‬
‭quantity‬ ‭shipped‬ ‭to‬ ‭each‬ ‭retailer‬ ‭if‬ ‭one‬ ‭wishes‬ ‭to‬ ‭guarantee‬ ‭that‬ ‭99%‬ ‭of‬
‭customers‬ ‭will‬ ‭be‬ ‭served?‬ ‭Apply‬ ‭your‬ ‭approach‬ ‭to‬ ‭compute‬ ‭recommended‬
‭quantities‬ ‭to‬ ‭the‬ ‭50‬ ‭retailers‬ ‭(explain‬ ‭the‬ ‭methodology‬ ‭in‬ ‭the‬ ‭body‬ ‭of‬‭the‬‭report‬
‭and provide the results in appendix).‬
‭The method we used to determine the quantity shipped to each retailer was as follows:‬
‭●‬ ‭We created a pivot table to consolidate the complete sales data for each retailer.‬
‭●‬ ‭For each retailer, we calculated the sum, average, and standard deviation of‬
‭sales.‬
‭●‬ ‭We then applied the formula for the optimal order quantity‬ ‭q* =‬‭μ + K‬‭σ‬ ‭, where‬
‭K corresponds to the desired service level (99%).‬
‭●‬ ‭Finally, we summed the‬‭q*‬‭values across all retailers‬‭to obtain the total‬
‭recommended quantity.‬
‭This approach gives the following outputs:‬
‭Mean: 204.6‬ ‭|

Standard Deviation: 81.3

|‬ ‭99% stock level: 393 magazines‬ 🚨calculated 393, outside range🚨

‭2.‬‭If‬‭Yedioth‬‭could‬‭implement‬‭full‬‭pooling‬‭among‬‭all‬‭of‬‭the‬‭50‬‭retailers‬‭what‬‭would‬
‭be‬ ‭the‬ ‭estimated‬ ‭benefit‬ ‭in‬ ‭terms‬‭of‬‭total‬‭production‬‭levels‬‭and‬‭returns‬‭(assume‬
‭that‬‭the‬‭required‬‭service‬‭level‬‭is‬‭99%).‬‭Note:‬‭Full‬‭pooling‬‭means‬‭that‬‭somehow‬‭all‬
‭of the retailers could be supplied in real time from the same pool of inventory.‬
‭Full‬‭pooling‬‭means‬‭that‬‭all‬‭50‬‭retailers‬‭are‬‭treated‬‭as‬‭a‬‭single‬‭entity,‬‭and‬‭inventory‬‭can‬
‭be‬‭moved‬‭between‬‭them‬‭in‬‭real-time‬‭to‬‭meet‬‭demand.‬‭To‬‭estimate‬‭the‬‭benefit‬‭in‬‭terms‬
‭of total production levels and returns for a 99% service level, we will:‬
‭1.‬ ‭Aggregate the sales data for all 50 retailers for each week to get the total sales.‬
‭2.‬ ‭Calculate average of weekly sales aggregate data.‬
‭3.‬ ‭Calculate standard deviation of the weekly sales data aggregate.‬

‭15.778 Introduction to Operations Management‬

‭Section B‬

‭4.‬ ‭Using the optimal quantity formula‬‭q* =‬‭μ + K‬‭σ‬‭we know mean, standard‬
‭deviation K = 2.32 for 99%, we calculate q*.‬
‭This approach gives the following outputs:‬
‭Mean: 189.6‬ ‭|

Standard Deviation: 19.9

|‬ ‭99% stock level: 236.1 magazines‬ 🚨correct pooling🚨

‭3.‬ ‭Suppose‬ ‭that‬ ‭one‬ ‭could‬ ‭implement‬ ‭full‬ ‭pooling‬ ‭only‬ ‭among‬ ‭retailers‬ ‭that‬ ‭are‬
‭treated‬ ‭by‬ ‭the‬ ‭same‬ ‭sales‬ ‭agent,‬ ‭what‬‭would‬‭be‬‭the‬‭potential‬‭benefit‬‭in‬‭terms‬‭of‬
‭production levels and returns (assume 99% service level). Compare to 2) above.‬
‭Full pooling among retailers served by the same sales agent can be simulated via the‬
‭following approach:‬
‭-‬ ‭For each of the 46 weeks, sum up the total sales (across each salesperson’s five‬
‭stores serviced) for each of the 10 sales agents‬
‭-‬ ‭Calculate the mean and standard deviation across weeks for each sales agent‬
‭-‬ ‭Sum these numbers for an overall mean and standard deviation across agents‬
‭-‬ ‭99% service level can then be computed using the formula‬‭q* =‬‭μ + K‬‭σ‬‭for the‬
‭“agent pooling” setup‬
‭This approach gives the following outputs:‬
‭Mean: 189.6‬ ‭|

Standard Deviation: 41.7

|‬ ‭99% stock level: 286.49 magazines‬ 🚨correct agent pooling🚨

‭This is a clear improvement in all metrics from our original approach. Compared to‬
‭question 2:‬‭mean is the same‬‭(makes sense, as we are‬‭still looking at total sales per‬
‭week) but the‬‭standard deviation has increased‬‭due‬‭to the variation between agents.‬

‭4.‬‭Propose‬‭more‬‭realistic‬‭policies‬‭that‬‭leverage‬‭the‬‭fact‬‭that‬‭the‬‭sales‬‭agent‬‭visits‬
‭each‬ ‭retailer‬ ‭in‬ ‭the‬ ‭middle‬ ‭of‬ ‭the‬ ‭week.‬ ‭What‬ ‭would‬ ‭the‬ ‭benefit‬ ‭be‬ ‭of‬ ‭these‬
‭policies?‬
‭When‬‭analyzing‬‭inventory‬‭requirements‬‭under‬‭the‬‭current‬‭distribution‬‭model,‬‭the‬‭central‬
‭pooling‬‭model,‬‭and‬‭the‬‭distributed‬‭pooling‬‭model‬‭for‬‭each‬‭sales‬‭agent,‬‭we‬‭observed‬‭that‬
‭reducing‬ ‭the‬‭standard‬‭deviation‬‭of‬‭demand‬‭across‬‭the‬‭week‬‭can‬‭significantly‬‭decrease‬
‭variability.‬ ‭This,‬ ‭in‬ ‭turn,‬ ‭reduces‬ ‭the‬ ‭amount‬ ‭of‬ ‭inventory‬ ‭required‬ ‭to‬ ‭meet‬ ‭customer‬
‭demand without increasing the risk of stockouts.‬
‭Given‬ ‭that‬ ‭each‬ ‭sales‬ ‭agent‬ ‭visits‬ ‭retailers‬ ‭midweek,‬ ‭a‬ ‭more‬ ‭realistic‬ ‭and‬ ‭effective‬
‭policy‬‭would‬‭be‬‭to‬‭leverage‬‭these‬‭visits‬‭to‬‭gather‬‭real-time‬‭insights‬‭on‬‭inventory‬‭levels.‬

‭15.778 Introduction to Operations Management‬

‭Section B‬

‭Specifically,‬ ‭sales‬ ‭agents‬ ‭could‬ ‭report‬ ‭whether‬ ‭inventory‬ ‭is‬ ‭accumulating‬ ‭(indicating‬
‭lower-than-expected‬‭demand)‬‭or‬‭if‬‭retailers‬‭anticipate‬‭higher‬‭demand‬‭than‬‭current‬‭stock‬
‭levels can support.‬
‭This‬ ‭midweek‬ ‭feedback‬ ‭provides‬ ‭valuable‬ ‭data‬ ‭that‬ ‭can‬ ‭be‬ ‭used‬ ‭by‬ ‭headquarters‬ ‭to‬
‭reduce‬ ‭uncertainty‬ ‭for‬‭the‬‭remainder‬‭of‬‭the‬‭week.‬‭Using‬‭this‬‭information,‬‭headquarters‬
‭could‬ ‭reallocate‬ ‭inventory‬ ‭dynamically—shifting‬ ‭stock‬ ‭from‬ ‭sales‬ ‭agents‬ ‭with‬ ‭excess‬
‭inventory‬‭to‬‭those‬‭facing‬‭potential‬‭shortages.‬‭This‬‭approach‬‭helps‬‭avoid‬‭overproduction‬
‭and‬ ‭minimizes‬ ‭the‬ ‭risk‬ ‭of‬ ‭underserving‬ ‭customers,‬ ‭all‬ ‭without‬ ‭the‬ ‭need‬ ‭to‬ ‭print‬
‭additional copies.‬ 🚨reallocation mechanism🚨

‭5.‬ ‭What‬ ‭do‬ ‭you‬ ‭think‬ ‭are‬ ‭the‬ ‭organizational‬ ‭challenges‬ ‭that‬ ‭Assaf‬ ‭will‬ ‭have‬ ‭to‬
‭address?‬
‭He needs to build a centralized pool system and establish a distribution process from the pool to‬
‭the points of sale. One of the key challenges is how to ensure regular circulation of magazines‬
‭from the pool to the sales outlets. The more frequently this distribution occurs each week, the‬
‭lower the standard deviation in demand, which means the company can print fewer excess‬
‭copies.‬
‭The ideal scenario would be real-time supply, but that is not feasible because each sales agent‬
‭is responsible for about 10 sales points. On the positive side, the agents are motivated to‬
‭increase sales, which aligns well with this approach. However, increasing the number of agents‬
‭is not an option because it would reduce the average income per agent.‬

‭-‬
‭-‬
‭-‬
‭-‬

‭The agents don’t have incentive to optimize a stock.‬
‭Hove to collect information from all points of sales‬
‭Need to be close connection with agent and redistribution team‬
‭We need to rely on integrity of agent about information from point of sales‬ 🚨generic challenges🚨

‭15.778 Introduction to Operations Management‬

‭Section B‬

‭Appendix 1: data for mean, standard deviation, 99% supply level across customers (Q1)‬

‭15.778 Introduction to Operations Management‬
‭Appendix 2: total sales per week under pooling system (Q2)‬

‭Section B‬

‭15.778 Introduction to Operations Management‬

‭Section B‬

‭Appendix 3: total sales per week per sales agent under agent pooling system (Q3)‬

