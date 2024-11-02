inspection paradox: Bus arrives at the stop every EX time on average, but the expected waiting time of prospective riders is larger than EX/2. Smaller the variance, smaller the gap (between local agent’s and global agent’s average) becomes. Inspection paradox happens when the probability of observing a quantity is related to the quantity being observed. This paradox can shed light on the degree of similarity between internal and external or local and global agent. To be specific, the more EV deviates from EX/2, EX (for $\sigma_x^2 = (EX)^2$) to sometimes larger than EX (for Bern(1, p) with p<.5), the larger the gap between time then space average ($\int$ dTdS) vs space then time average ($\int$ dSdT). (i.e. we can't apply Fubini theorem)
Ultimately, I'd use the result to understand "Perception Gap between Internal Actor and External Evaluator" whose mechanism is explained in [[15_357_proposal_MoonZhang.pdf]].  

The probability of observing misalignment is related to the observed misalignment. The more misaligned two evaluators are, it's easier to mutually identify differences. It’s because each evaluator has evaluation measure uncertainty (i.e.  doubt about their rulers 📏 at hand hence ruler uncertainty). What may be "aligned close enough" with current rulers may change to misaligned with finer rulers. Hence, the more misaligned the two are, the higher the probability of observing misalignment.



|   |   |   |   |   |
|---|---|---|---|---|
|inspection paradox|local agent|quantity being observed by local agent 🔴|probability of observing a quantity by global agent 🟩|variance|
|bus example|rider|rider observing bus’ arrival (unit: m)|probability of observing bus’ arrival|variance of bus’ arrival|
|evaluation example<br><br>(how many monthly users needed to scale successfully)|evaluator|evaluator observing misalignment (unit: person)|probability of observing misalignment|variance of misalignment|

  
  ![[Pasted image 20240228170859.png|400]]
  


| Person  | Key Insights                                                                                                                                                                                                                                                             | Surprising Elements                                                           |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| Charlie | - Emphasized the tradeoff between expected return and variability<br>- Highlighted the importance of value creation vs. value capture<br>- Suggested focusing on grow faster vs. control more as a key tradeoff                                                          | The focus on the founder's perspective rather than just the investor's view   |
| Tom     | - Introduced the concept of a "checksum equation" for modeling complex systems<br>- Discussed the importance of reality checks in system dynamics models<br>- Emphasized the need to consider both the financial and operational aspects of a startup                    | The application of system dynamics concepts to financial modeling of startups |
| Shakul  | - Discussed the decomposition of future valuation into market growth and company-specific factors<br>- Introduced the concept of information asymmetry between founders and investors<br>- Highlighted the importance of considering the probability of getting invested | The focus on information asymmetry and its impact on negotiations             |



| Chapter | Main Concept | Application to Angie's Situation |
|---------|--------------|----------------------------------|
| Importance Sampling to SMC | Using weighted samples to approximate target distributions, with resampling to address weight degeneracy in sequential settings | Angie could use SMC to track the evolution of ideas/approaches in probabilistic programming over time, using the nine experts as "particles" and resampling based on how influential their ideas become |
| Learning Proposals and Twisting Targets | Adapting proposal distributions and intermediate target distributions to improve SMC performance | Angie could learn proposal distributions for predicting each expert's next contribution based on their past work. She could also design intermediate targets that incorporate information about future developments to guide the sampling |
| Nested Monte Carlo | Using layers of Monte Carlo sampling to approximate intractable ideal algorithms | Angie could use nested MC to handle uncertainty at multiple levels - e.g. uncertainty in each expert's contributions nested within uncertainty about overall field directions |
| Conditional SMC | Conditioning SMC on a reference trajectory to construct MCMC algorithms targeting the original distribution | Angie could use conditional SMC to explore alternative histories of probabilistic programming development, conditioning on the actual observed trajectory but allowing variations to study counterfactuals |
