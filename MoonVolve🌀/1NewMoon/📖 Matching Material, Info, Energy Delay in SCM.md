- [[#0. Managing Material and Information Delay with SCM examples|0. Managing Material and Information Delay with SCM examples]]
- [[#1. Intro. to three echelon supply chain|1. Intro. to three echelon supply chain]]
- [[#2. Delay|2. Delay]]
- [[#3. Forecasting accuracy|3. Forecasting accuracy]]
	- [[Donohue18_ForecastDecisions.pdf]]
- [[#4. Information sharing|4. Information sharing]]
- [[#5. Length of delay vs Delay deviation|5. Length of delay vs Delay deviation]]
- [[#6. Local vs Global optimization|6. Local vs Global optimization]]
- [[#7. Supply chian strategies|7. Supply chian strategies]]
- [[#8. Resilient supply chain|8. Resilient supply chain]]
- [[#9. Emergency supply chain|9. Emergency supply chain]]
- [[#10. Games in supply chian|10. Games in supply chian]]
- [[#11. Data Science in supply chain manamegment|11. Data Science in supply chain manamegment]]
	



### 0. Managing Material and Information Delay with SCM examples
a. 제목 어떠신가요? 
	- delay와 uncertainty의 perception이 agent의 behavioral를 결정한다. 
	- 해당 behavior는 bias를 초래한다 [[Behavioral2Prior]] .                                                                                                                                                                                                      
	- aI는 전역최적화를 고려한 prior설계를 자동화해 이런 bias를 최소한다.

b. Matching vs managing material (e.g. lead time), info (e.g. expected demand)중 뭐가 더 적확한 표현이라 보시나요? 전 다음과 같이 생각해요. 

mismatch between inventory and expected demand (observed) are delayed mismatch of supply and demand (latent) which are accumulated mismatch between supply rate and demand rate. 

![[Pasted image 20220827233213.png]]



c. 언어는 영어인가요? 책쓰면 공부도 자동으로 하게되고 정말 좋은거 같아요!


matching expected demand with inventory each of which are delayed cumulation of demand and 

### 1. Intro. to three echelon supply chain
a. 굳이 3단계를 잡은 이유? 3, 6 order delay를 주로 많이 다룬다던데  관련있나요?
b. Tom의 [Bathtub statistics](https://metasd.com/2012/05/bathtub-statistics/)글 중 그림 분석에서 차근히 시작해보는 것도 의미있을듯요. Process noise관련.

![[Mng(Stock)withUncertainty.jpeg]]

c. [[Yaman Barlas]]링크 중 1,2,high order system (유추) 목차에 매료돼 유사형태로 써보고 싶어요.
Systems Science and Engineering (IE 350)

$$\begin{aligned}
&\text { WEEK }\\
&\begin{array}{ll}
\hline 1 & \text { Course Objective, Organization and Overview } \\
1 & \text { "Systems" concepts, philosophy and history } \\
2 & \text { Systems analogies: } 1^{\text {st }} \text { order dynamic systems } \\
2,3 & \text { Electrical-hydraulic-mechanical analogies } \\
3 & \text { Industrial, socio-economic, managerial analogies } \\
4 & \text { Systems analogies: 2 nd order dynamic systems } \\
4,5 & \text { Electrical-hydraulic-mechanical analogies } \\
5 & \text { Industrial, socio-economic, managerial examples } \\
6 & \text { Higher order linear dynamic systems } \\
6 & \text { Midterm exam 1 (April 29, at 18:00) } \\
7 & \text { Non-linear systems and limits of mathematical analysis } \\
7,8 & \text { Simulation method and software } \\
8,9 & \text { Equilibrium and stability analysis } \\
10 & \text { Typical non-linear structures and formulations } \\
11 & \text { Midterm exam 2 (June 04, at 18:00) } \\
11 & \text { Time delays in dynamic systems } \\
12 & \text { Formulation principles for large-scale socio-technical systems } \\
13 & \text { Large scale stock-flow modeling examples } \\
13 & \text { Systems Science and Systems Approach in a Complex World }
\end{array}
\end{aligned}$$


## 2. Delay
a. oscilation, uncertainty, resilience..무슨 내용을, 어떤 예시를 다루면 좋을까요?

## 3. Forecasting accuracy

a. 다음 발표 참고할만한가요?                                                                                                                                                                                                                                                             
- [lecture](https://www.youtube.com/watch?v=YsjsqkogNhU&ab_channel=BurakKandemir)for Burak Kandemir's work on analyzing the impact of forecasting and demand pattenrs in SCM ([[Kandemir22_ForecastingDmdPattern.pdf]]) with summary:
	- The simulation results indicate; 
		- Accuracy of forecasts have a direct impact on supply chain performance in terms of inventory and service levels 
		- Inventory policies try to stabilize the supply chain system even in low forecast accuracy
		- Stock adjustment takes more time in demand decrease scenarios
		
![[Pasted image 20220827212144.png]]

## 4. Information sharing
a. pooling이라 부르나요? 전통적인 재고관린에서 전통적으로 pooling이 공급과 수요의 불확실성 중 뭘 대상으로 할까요? 


## 5. Length of delay vs Delay deviation
a. supply side of "uncertainty from delay  (information)" affecting the flow


## 6. Local vs Global optimization

(tbc)

## 7. Supply chian strategies



## 8. Resilient supply chain


## 9. Emergency supply chain


## 10. Games in supply chian


## 11. Data Science in supply chain manamegment

- [Supply chain optimization with python](https://towardsdatascience.com/supply-chain-optimization-with-python-23ae9b28fd0b) uses lp-based optimization
- 
a. AI와 Data science 중 뭐가 나을까요? [[3 Bayequentist Dynamics with SBC]]의 
b. 전체적이 excellent로 번역되는 이유는? 왜 이 맥락에서 꼭 전체적 공급사슬이어야하나요?


---
Demand-Supply (DS)
<img width="1210" alt="image" src="https://user-images.githubusercontent.com/30194633/182761909-83a6c6dd-c683-4fec-9cf8-5f302be4209c.png">

DS has 8 parameters to estimate and 5 parameters that is assumed

8 = 6 (2 * 3) stock-related

	- `latent_state_init`, `msr_error_scale` for each stock `Supply Line`, `Inventory`, `Backlog`

plus 2 estimated params 

	- `supply_lead_time`, `shipment_lead_time`,

and

5 `assumed params`

	- const: `supply_line_adj_time`, `inventory_adj_time`, `backlog_adj_time` , `demand_adj_time`
	- series: `demand`