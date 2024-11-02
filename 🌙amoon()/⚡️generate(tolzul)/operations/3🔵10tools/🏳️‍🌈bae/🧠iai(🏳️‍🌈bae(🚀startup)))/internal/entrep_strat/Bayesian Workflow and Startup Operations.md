## 1. Analogy between Bayesian workflow and Startup operations
The Bayesian workflow is a principled approach to statistical modeling and decision-making, consisting of three main steps: model building, inference, and model checking/improvement. The Bayesian community has evolved from focusing on Bayesian inference to embracing a more comprehensive Bayesian workflow (Gelman et al, 2022). This shift parallels the transition in entrepreneurship from focusing on entrepreneurial compass, which suggests directions, to a more operational approach that provides the tools to move towards certain direction. This paper aims to draw an analogy between Bayesian workflows and startup operations, exploring how quick, easy, reliable model growth enabled by Bayesian workflow can be applied for entrepreneurial growth. Key analogy is, just as computational representation of mathematical model evolves to pair itself with observed data in Bayesian workflow, organizational representation of business model adapt itself with data from demand. This pair is also known as market-product or need-solution pair. Co-evolution of pair has been raised in Von Hippel and Von Krogh (2016). 

## 2: Bayesian Workflow Components and Models
The Bayesian workflow is organized around three main components: P (joint probability distribution), A (posterior approximator), and D (observed data). **P** represents the joint distribution over observable quantities $\tilde{y}$ and latent parameters $\theta$. Examples include Gaussian Mixture Models and Bayesian linear regression. **A** is the tools, methods, algorithms used to approximate the true posterior distribution, such as Hamiltonian Monte Carlo or Variational Inference. **D** refers to the actual data points observed, like measurements in a scientific experiment or user interaction data in a machine learning application. These components can be assembled to make different types of model: P, PD, PA, and PAD. **P Models** represent the foundational models describing data generation. **PD Models** combine P with observed data \(D\), yielding an analytic posterior. **PA Models** combine P with a posterior approximator \(A\). **PAD Models** integrate all three components to approximate the true posterior distribution. Formal definitions, details, examples in Appendix.

## 3: Startup Operations Components 
In the context of startups, P, A, and D components can be mapped to business model, scaling tool, and observed market data, respectively. P represents business model, starting from long term planning on orientation and investment to short term control on customer, technology, competition, product, organization. A represents scaling tools that can implement business models. D would be real-world market data, such as customer behavior and sales figures. These components can also be combined into different models in startup operations: P, PD, PA, and PAD. P Models could represent different business strategies. PD Models would combine the business model with real-world market data. PA Models would combine the business model with analytical tools. PAD Models would integrate the business model, scaling tools, and real-world market data. PAD is the ideal destination for a scaling startup but different evolutionary paths exist, so strategies could be dynamically adjusted along one's lifecycle.

![image](https://github.com/Data4DM/BayesSD/assets/30194633/982e0642-b133-4b94-816d-32e02f27fb0f)
Figure 1: Analogy between Bayesian workflow and startup operations

#### P - Business Model
- **P** in startups could represent the core business model, including elements like product features, market strategy, and organizational structure. For example, a startup in the renewable energy sector might focus on solar panel efficiency, government subsidies, and partnerships with construction firms. A health tech startup's P model may include variables like patient engagement, telehealth features, and partnerships with healthcare providers. SaaS startup might have a P model that includes variables like subscription pricing, feature sets, and target customer demographics. 
- can be represented in three tier tree format from entrepreneurial strategy, business model feature, product feature. Entrepreneurial strategies are investment (execute or control) and orientation (collaborate or compete) and business model features are technology (length 4 vector), customer (length 4 vector), organization (length 4 vector), competition (length 4 vector). 
- e.g. of parameter space of organization (with @chasfine) are size, location (geographical - sitting in the office), direct report to ceo (decentralization), percentage of technical degree and college education (what kind of people you hire (mit vs macdonalds)), what is the average compensation relative to industry (investing in your people / churn a lot, turnover, pay more, lower turnover / good or bad job), average turn or tenure, how much money they've been funded, round of funding, gone through ipo? which needs to be segmented into 4.

#### A - Scaling Tools
- **A** could represent tools that help refine or approximate the optimal business model. This includes data analytics platforms, customer relationship management (CRM) systems, and even decision-making frameworks like SWOT or PESTLE analysis.

#### D - Observed Market Data
- **D** would be the real-world market data that the startup collects. This could include customer behavior, sales figures, and market trends. For instance, a fintech startup might look at user engagement metrics, transaction volumes, and regulatory changes.

## 4: Growth Path to PAD model in Startup Operations 
To scale well, three components (business model P, scaling tools A, and real-world data D) should be harmoniously orchestrated.  Starting from one nailed component (among P, A, D), different growth paths exists to reach PAD. Principled guideline on when to focus on which component could enable quick, easy, reliable growth toward PAD.

<img width="910" alt="image" src="https://github.com/Data4DM/BayesSD/assets/30194633/a1dda66e-1a57-4418-b2e8-58c5a4010740">

Figure 2: Growth Path in Startup Operations 

- **PAD Models** would integrate the business model (P), scaling tools (A), and real-world market data (D). For instance, a startup might use machine learning algorithms (A) to analyze customer behavior data (D) and dynamically adjust its product recommendation engine (P). Also, a startup can simulate the impact of platformization (A) on their existing customer base (D) and overall business strategy (P).

- **PD Models** would combine the business model (P) with real-world market data (D). For instance, if a startup in the e-commerce sector observes that organic traffic is not converting well, the PD model would adjust to focus more on paid traffic and customer retention strategies. 
- would combine the business model with real-world data, such as customer churn rates and Lifetime Value (LTV) calculations. For instance, if a startup observes higher churn rates than expected, the PD model would adjust the expected LTV of a customer downward.

- **PA Models** would combine the business model (P) with scaling tools (A) to approximate the success of different strategies without yet incorporating real-world data. For example, a startup might use predictive analytics to model the impact of a price change on customer acquisition rates. 
- would be hypothetical scenarios where the startup explores how different scaling strategies (A) would impact their existing business model (P). For example, they might model the effects of expanding into a new market or launching a new product line.

## 5: Future Work and Research Questions
### Ex-Ante
1. Designing surveys for 700 participants and 150 startups in delta-v to extract P, A, D components.
2. Classifying the evolution of their business models, such as transitioning from P to PA to PAD or D to PD to PAD.
### Ex-Post
3. Extracting P, A, D components from existing case studies.
4. Classifying the business model evolution from existing case studies.

5. finding 4~10 dims. representation of high dimension business model features (technology, customer, organization, competition) 

By exploring these research questions, we can further validate and refine the analogy between Bayesian workflows and startup operations, providing a robust framework for both statistical modeling and entrepreneurial decision-making.

## References
- [Gelman, A., Vehtari, A., Simpson, D., Margossian, C. C., Carpenter, B., Yao, Y., ... & Modrák, M. (2020). Bayesian workflow. arXiv preprint arXiv:2011.01808.](https://arxiv.org/pdf/2011.01808.pdf)
- [Modrák, M., Moon, A. H., Kim, S., Bürkner, P., Huurre, N., Faltejsková, K., ... & Vehtari, A. (2022). Simulation-based calibration checking for Bayesian computation: The choice of test quantities shapes sensitivity. arXiv preprint arXiv:2211.02383.](https://arxiv.org/pdf/2211.02383.pdf)
- [ Bürkner, P. C., Scholz, M., & Radev, S. T. (2022). Some models are useful, but how do we know which ones? towards a unified bayesian model taxonomy. arXiv preprint arXiv:2209.02439 ](https://arxiv.org/pdf/2209.02439.pdf)
- [Von Hippel, E., & Von Krogh, G. (2016). Crossroads—Identifying viable “need–solution pairs”: Problem solving without problem formulation. Organization Science, 27(1), 207-221](https://pubsonline.informs.org/doi/pdf/10.1287/orsc.2015.1023)

## Appendix
Formal definition and examples of component and model in Bayesian Workflow for further analogy. Refer to sections from Burkner et al (2022) for detail.

### P component - $p(y,θ)$ 
- joint probability distribution  over observable quantities y and unobservable parameters θ
- often factorize into a likelihood p(y|θ) and a prior p(θ) and are generative, allowing random sampling from the joint distribution.
- can have explicit likelihoods (P_E models) or implicit likelihoods (P_I models) requiring simulation.
- e.g. linear regression model with likelihood p(y|θ) and prior p(θ) where likelihood could be Gaussian, and the prior could be a normal distribution centered around zero (Section 2.2), Gaussian Mixture Model, \(P\) would define how data points are generated from multiple Gaussian distributions.

### A component - Posterior Approximator $P_A(\theta|y)$
- mechanism used to approximate the true posterior distribution. For instance, Hamiltonian Monte Carlo (HMC) is often used for complex models where traditional MCMC methods like Metropolis-Hastings are inefficient.
- Markov chain Monte Carlo (MCMC) samplers like Metropolis-Hastings or Hamiltonian Monte Carlo (Section 2.3)
- Variational inference (VI) methods that find an optimal parametric posterior approximation (Section 2.3)
- Neural density estimators like normalizing flows or sequential neural posterior estimation (Section 2.3)

### D component - Observed Data  $\tilde{y}$
- D can comprise any number of observations with arbitrary structure (Section 2.2)
- In PD models, D is the observed data ̃y combined with the P model (Section 2.2)
- In PAD models, D is the actual observed data ̃y used by the posterior approximator A (Section 2.4)

### PD Models $(p(y,θ), \tilde{y})$
- P models combined with observed data \(D\). They yield the analytic posterior, which is the updated belief about the model parameters after observing data
- yield the analytic posterior p(θ| ̃y) which integrates the joint distribution p(y,θ) with the data ̃y.
-e.g. in a Bayesian A/B test, the PD model would combine the prior beliefs about conversion rates with the observed conversion data.

### PA Models
- theoretical constructs that combine a P model with a posterior approximator \(A\) but do not yet include observed data
- allow studying the scope of a P model before observed data is collected.
- useful for understanding the behavior of different approximators. 
- can utilize amortized or non-amortized approximator.
- e.g. one might use a PA model to compare the efficiency of Variational Inference against MCMC methods for a given P model.

### PAD Models
- **PAD Models** integrate all three components—P, A, and D. 
- Aim to approximate the PD model using the approximator A
- Properties depend on the data ̃y which may not come from P itself (model misspecification).
- e.g. in a Bayesian neural network, the PAD model would include the network architecture (P), the observed training data (D), and a method like Variational Inference for approximation (A).
![[Pasted image 20230918132339.png]]a
![[Pasted image 20230918132425.png]]