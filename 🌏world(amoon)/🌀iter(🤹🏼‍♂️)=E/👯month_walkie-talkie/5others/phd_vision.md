
#### Vision

Building startups is challenging and demands substantial investment in tangible (physical, financial) and intangible (cognitive, and emotional) resources. Over 90% of startups are known to fail, showing a commonly known “boom and bust” behavior in dynamical systems, and they can fail for reasons unrelated to the idea's merit (reference to 90%). We have conducted case studies on startups (e.g. Unity Homes, NxStage) that faced challenges in growing and sustaining their market size, and their production and delivery capabilities, despite their product being proven worthy. Our analysis revealed that these startups struggled primarily due to a lack of strategic planning and adaptability in their initial growth phase, often due to misalignment of their product development with the market's needs and their operational capabilities. Success depends on effectively aligning the product, organizational, and business models together. Based on this, our hypothesis is that the sequence and frequency of startup actions can make or break the enterprise, regardless of product type or industry. Our sub hypothesis is, sequence, frequency, action of start actions can be defined.

My vision is inspired by this misalignment and hypotheses: 

1. **Comparison of Rejection and Importance Sampling on Efficiency:**
Rejection sampling and importance sampling are two probabilistic methods used to approximate distributions, but they differ significantly in efficiency. Rejection sampling operates by randomly generating samples from a distribution and then rejecting those that do not meet the criteria, leading to a high number of wasted computations, especially when the acceptance probability is low. This inefficiency becomes pronounced in high-dimensional spaces where the probability of acceptance decreases exponentially. On the other hand, importance sampling improves efficiency by weighting samples according to their likelihood under the target distribution. This method allows for the focused sampling of areas with higher probabilities, reducing the number of samples needed to achieve an accurate approximation. The efficiency of importance sampling lies in its ability to reduce variance and increase the representativeness of samples, making it particularly suitable for scenarios where obtaining samples is costly or difficult.

2. **Enhancing Learning from Rejection to Importance Sampling for Individual Startup's Learning:**
For individual startups, transitioning from rejection to importance sampling can significantly enhance learning and decision-making processes. Startups often grapple with the challenge of effectively distinguishing between high- and low-impact variables in hypothesis testing, leading to a scattergun approach. This is inefficient as it consumes valuable resources on less impactful activities. By adopting importance sampling, startups can prioritize their experiments based on the potential impact, focusing resources on areas with the highest probability of success. This targeted approach not only optimizes resource allocation but also accelerates the learning curve, enabling startups to quickly identify and scale successful strategies while minimizing time and capital spent on less fruitful avenues. Thus, importance sampling provides a structured framework for startups to navigate the complex landscape of market dynamics and product development efficiently.

3. **Enhancing Learning from Rejection to Importance Sampling for Startup Institution's Learning:**
At the institutional level, embracing importance sampling can foster a more strategic and efficient ecosystem for startups. The prevalent culture of rapid experimentation often leads to a lack of strategic focus, with startups engaging in a trial-and-error process that can perpetuate inefficient testing practices. By shifting towards importance sampling, startup institutions can promote a culture where learning is optimized through strategic sampling. This approach not only conserves resources but also generates more relevant and actionable insights, facilitating a deeper understanding of market needs and operational challenges. Advocating for importance sampling, supported by success stories and case studies, can encourage startups to adopt these more efficient practices, leading to a healthier, more sustainable ecosystem where startups can thrive through focused learning and innovation. This strategic shift can enhance the collective learning within the startup community, driving progress and success across the sector.



Bridging [bayesian entrepreneurship](https://www.entrepreneurial-strategy.net/) (BE) with [probabilistic computing](https://en.wikipedia.org/wiki/Probabilistic_programming) (PC). This presents a novel approach towards navigating startup ventures through the complex business landscape using data-driven decision-making and strategic planning. BE, drawing from the research of Professors Scott Stern and Charlie Fine, emphasizes strategic decision-making in startups across four critical domains: i-Customer, ii-Technology, iii-Organization, and iv- Competition, with a focus on selecting among disruptor, architectural, value chain, and IP strategies for a phase-based, learning-driven path to success. (Joshua, 2025) 

This strategic idea is complemented by the PC, based on the software ecosystem led by Vikash Mansinghka ([Gen](https://www.gen.dev/)) and Andrew Gelman ([Stan](https://mc-stan.org/)). PC aims to [democratize data science](https://news.mit.edu/2019/nonprogrammers-data-science-0115) by enabling non-experts to generate and use sophisticated statistical models for data analysis through user-friendly tools. By integrating PC's capabilities to automatically model data and predict trends with BE's strategic insights for startups, this research envisions a data-informed platform that not only guides startups through personalized strategic decisions but also offers adaptive paths to achieve long-term success. I organized two teams on [this](https://github.com/orgs/Data4DM/projects) board for an abductive approach. The first team develops technology that models how agent, environment, goal, belief, action, experiment interact as startups evolve. This technology is productized by the second team which builds prototypes and minimum viable products to measure its use and to choose a beachhead market.  

##### Bayesian Entrepreneurship

Supported by Profs. Charles Fine, Scott Stern, and JB Labrune, our first goal is to theorize how startups experiment with an idea during its early stage. As illustrated in Figure1, a startup implements its idea by choosing a market and technology given limited resources before scaling. Specifically, it formulates hypotheses about the market based on its product's potential. Then, it chooses the target market. Next, after setting hypotheses on its prototype in the chosen market, the startup builds a prototype with its technology to receive feedback. Based on this feedback, it updates its prior on both the prototype and the market. Finally it decides whether to keep the prototype and scale up, change the chosen market, or keep refining its prototype. 

![[Pasted image 20240401104214.png|1000]]
Figure 1. A startup with limited resource updates how it chooses market technology prototype before scaling. 

Simulation is possible by implementing this with a probabilistic programming language (work in progress).

I’m planning two improvements on this theory. First is on representing endogenous appropriability. Upcoming textbook on… by Gans et. al. (2025) will explain how startups’ decision of technology, customers, organization, and competition should revolve around their decision on types of investment and orientation. Despite its importance to understand how startups decide between protecting their ideas through patents (control) or moving fast to beat competitors (execution), the abstractness of this endogenous appropriability concept made it challenging to explain. By representing this with a simulation model in Figure 1 can be a first step in understanding how these different choices interact. To be specific, tweaking hyperparameters of the model (e.g. initial prior on market, technology give market, initial capital, threshold of remaining capital to abort experimentation and pivot, unit experiment cost) may give us a visual understanding of how startup’s willingness to execute affects its experiment trajectory. The authors' efforts in classifying case studies based on endogenous appropriability, e.g. Netflix, Amazon, Foxconn, PayPal who executed vs  Facebook, eBay, Harry Potter, Intellectual Ventures who controlled, would be a great source of insight. Once this is nailed, I plan to also explore the optimism and overconfidence of entrepreneurs by experimenting with prior's mean and tightness on market and technology. 


Second idea is to extend startups’ scope from an early stage to the entire life cycle. In their 2022 paper, Fine and colleagues adopted a succinct three phase framework—nail it, scale it, sail it—to analyze the startup’s evolution. "Nailing" is described as crafting a value proposition that satisfies every stakeholder in the proposed value chain, including customers, employees, suppliers, distributors, and investors. This concept resonates with the definitions provided by Osterwalder and Pigneur (2010) and others. "Scaling" involves expanding the market size, production, and delivery capabilities simultaneously, while "Sailing" focuses on achieving sustainable growth.

##### Probabilistic Computing (PC)

With probabilistic computing software like support, one can translate the BE theory into interactive tools that startups can play with and learn from. This representation enables a systematic and rigorous approach to updating beliefs in response to new evidence. Stan's ability to handle complex statistical models and compute log densities, gradients, and Hessians makes it particularly suited for modeling the iterative process of hypothesis testing and belief updating in entrepreneurship. Entrepreneurs can specify models that reflect their hypotheses about the market and use data from experiments to update their beliefs, thus facilitating a more data-driven and analytical approach to navigating the uncertainties of new venture creation. (More explanation on BayesDB and AutoGP)

Probabilistic computing, which includes programming languages like [Stan](https://mc-stan.org/), [Pyro](https://pyro.ai/), and [Gen](http://probcomp.csail.mit.edu/software/gen/); higher level interface with specific purpose like [SBC](https://hyunjimoon.github.io/SBC/articles/rank_visualizations.html) (rank visualization on simulated data), [BayesDB](http://probcomp.csail.mit.edu/software/bayesdb/#:~:text=BayesDB%20is%20a%20probabilistic%20programming,using%20an%20SQL%2Dlike%20language.) (AI-assisted collaborative science), and [AutoGP](https://probsys.github.io/AutoGP.jl/stable/index.html) (automated Bayesian model discovery for time series data); translates Bayesian Entrepreneurship theory into interactive simulation tools. This ensemble offers a methodological framework for startups, predicated on a Bayesian approach, to iteratively refine hypotheses and adapt strategies based on empirical data. Stan is a versatile tool for statistical modeling, used in fields like social sciences, biology, and engineering, offering interfaces for R, Python, and Julia, among others. It supports methods like Markov Chain Monte Carlo (MCMC) sampling, variational inference, and optimization for tasks ranging from linear modeling to cross-validation. BayesDB simplifies data exploration and model generation for non-experts through SQL-like commands, leveraging non-parametric Bayesian methods for collaborative AI-assisted science, including probabilistic searches and virtual experiments, supported by DARPA. AutoGP complements this by automating the discovery and application of Gaussian processes for time series analysis, streamlining predictive modeling. 

In summary, the application of probabilistic computing languages to Bayesian entrepreneurship empowers entrepreneurs with a data-informed compass for navigating venture creation.

#### Prototype

Finally, with Doug William and MIT Martin Trust Center, I plan to continuously integrate tested theories on [orbit](https://orbit.mit.edu/) which is an MIT digital platform with 5,000 beta users. I envision three components of GPS: Startup Genome, Industry Map, and Startup Compass as in Figure 2. Startup Genome is a database of historical startup data, organized by the sequence of actions and outcomes, to analyze relationships between actions and success. Industry Map uses data analysis to validate business hypotheses and identify industry-specific patterns in successful startup actions. Startup Compass is a tool that provides guidance to individual early-stage startups, suggesting action sequences based on the Industry Map, the startup's beliefs and goals, and the target need and solution.

![](https://lh7-us.googleusercontent.com/Xv6zX68tXQW5nTYpLrk-0fuLS6UUZEXaU31LJJCP1TMyWRYeQgR7w4s04HsRxvbYGINxpRiAqDU-ObRS8NidXXvAL5yiNYsRhWCQSp2TWdW-wcKAOu2Ezadl0z8IkPol5ulzmcv8Q30fi2ks10U5qUc)

Figure 2. Three modules of GPS

#### Minimum viable product

Current [minimum viable product 📹](https://drive.google.com/file/d/1gJgNtHNIGARhQx3AYS0GIbhMmjphE77i/view?usp=drive_link) shows how different steps of startup can be generated based on Aulet (2004)’s theory and description of an idea. We plan to add more structure with Genome, Map, Compass modules and also by adding training data and statistical models.

  

#### Beachhead market

Q .  

| Mentors in Academia                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Team                                                                                                                                                                                                                                                                                                                                        | Network in Industry                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BE experts<br><br>Prof.[Charles Fine](https://www.charles-fine.com/) (MIT)  <br>Prof.[Scott Stern](https://scholar.google.com/citations?user=5opEOuMAAAAJ&hl=en&oi=ao) (MIT)<br><br>[JB Labrune](https://jblabrune.com/) (MIT Research Affiliate)<br><br>Prof. [Abdullah Almaatouq](https://amaatouq.io/) (MIT)<br><br>Prof.[Shi Ying Lim](https://www.shiyinglim.net/) (NUS)<br><br>PC experts<br><br>Prof.[Vikash Mansinghka](http://probcomp.csail.mit.edu/principal-investigator/) (MIT)<br><br>Prof.[Andrew Gelman](http://www.stat.columbia.edu/~gelman/) (Columbia) | Modelers with domain experts<br><br>Anup Sreekumar (RA, [CV](https://drive.google.com/file/d/1mdd1vQnZOFFJ1N-W2CvclM3crw1P8la1/view?usp=sharing))<br><br>YiChen Sun (Ph.D.candidate, NUS)<br><br>  <br><br>Platform manager<br><br>[Doug Williams (MIT Martin trust center staff)](https://entrepreneurship.mit.edu/profile/doug-williams/) | [Natalie Kuldell](https://www.linkedin.com/in/natalie-kuldell-9947408) (biotech)<br><br>[Hyukjeen Suh](https://www.linkedin.com/in/hyukjeensuh/) (semiconductor) |

  

References 

Modrák, M., Moon, A. H., Kim, S., Bürkner, P., Huurre, N., Faltejsková, K., ... & Vehtari, A. (2023). Simulation-based calibration checking for Bayesian computation: The choice of test quantities shapes sensitivity. Bayesian Analysis, 1(1), 1-28.

  

Moon, H., & Choi, J. (2021). Hierarchical spline for time series prediction: An application to naval ship engine failure rate. Applied AI Letters, 2(1), e22.

  

Almaatouq, A., Griffiths, T. L., Suchow, J. W., Whiting, M. E., Evans, J., & Watts, D. J. (2024). Beyond playing 20 questions with nature: Integrative experiment design in the social and behavioral sciences. Behavioral and Brain Sciences, 47, e33.

Aulet, Bill. (2013). Disciplined Entrepreneurship: 24 Steps to a Successful Startup . Hoboken, New Jersey.

  

Fine, C. H., Padurean, L., & Naumov, S. (2022). Operations for entrepreneurs: Can Operations Management make a difference in entrepreneurial theory and practice?. Production and Operations Management, 31(12), 4599-4615.

  

Osterwalder, A., & Pigneur, Y. (2010). Business model generation: a handbook for visionaries, game changers, and challengers (Vol. 1). John Wiley & Sons.

  

Gans, J., Scott, E.L., & Stern, S. (2025). Entrepreneurship: Choice and Strategy. W.W. Norton, Incorporated.

  

Repenning, N. P. (2001). Understanding fire fighting in new product development⋆. Journal of Product Innovation Management: An International Publication Of The Product Development & Management Association, 18(5), 285-300.

**