## Abstract
Ventures face a critical choice between sequential and parallel search strategies when testing new opportunities. We synthesize three theoretical perspectives - experimental design theory, adjacent possibility theory, and convergence diagnostics - to understand this choice. Our synthesis reveals that parallel search represents a "low-bar" experiment design emphasizing exaptation through many short chains, while sequential search embodies a "high-bar" approach favoring adaptation through fewer, longer chains. Through computational modeling of Bayesian belief updating, we formalize when each strategy is optimal by analyzing three key dimensions: a) 📍Cost structure, where parallel search becomes optimal when test-to-action cost ratios are low (T4C1 total cost = 4test + $\color{Red}{1choose}$ vs T2C1 total cost = (2test + $\color{Red}{1choose}$) × 2); b) 🎲Uncertainty propagation, where parallel search enables broader exploration of the 'adjacent possible' through simultaneous testing ($\color{Green}{\sigma_c}, \color{Purple}{\sigma_r} \sim \color{SkyBlue}{exp(\sigma)}$), allowing ventures to discover unexpected possibilities (exaptation) rather than committing early to a single path; c) 🧩Correlation effects, both horizontal (across industry) and vertical (within value chain), where parallel search better captures joint distributions and cross-level dependencies ($\color{Green}{\sigma_c}, \color{Purple}{\sigma_r} \sim \color{Orange}{\rho} * \color{SkyBlue}{exp(\sigma)}$). We derive a unified decision rule: choose parallel search when implementation costs and uncertainty are high ($\color{Red}{c_{act}} * \color{SkyBlue}{\sigma} * \color{Orange}{k}$ is large), prefer need (market)-first sequential search when market uncertainty dominates ($\color{Green}{\sigma_c} < \color{Purple}{\sigma_r}$), and default to solution (product)-first sequential search otherwise. This framework reconciles the apparent inefficiency of parallel search with its empirical prevalence by showing how high uncertainty and correlation can make broad exploration through parallel, low-bar experiments more valuable than deep exploitation through sequential, high-bar tests. 

## 0. table of contents:
![[🗄️🪶product2]]



## 1. Theoretical Background

### 1.1 experiment design theory

![[🗄️product2_EDT]]

### 1.2 Adjacent Possible theory
![[🗄️🪶product2_APT]]

Exaptation plays a critical role in expanding the **adjacent possible**—the set of all future innovations that become accessible based on current conditions (Kauffman, 1995). By repurposing existing resources or technologies, startups can unlock previously unforeseen opportunities and strategically pivot into new markets. In **parallel search**, startups running multiple experiments simultaneously are more likely to encounter exaptive opportunities, especially for resources or technologies that were not originally designed for their current use. For instance, **CRISPR Therapeutics** began as a tool for bacterial immune systems but was rapidly exapted for use in human gene-editing therapies, enabling the startup to address a variety of diseases from cancer to genetic disorders. This broad exploration uncovers hidden possibilities and allows startups to pivot in response to new market data. In **sequential search**, exaptive opportunities emerge more gradually, often following a deeper understanding of the technology being repurposed. **Waymo**, Google’s autonomous vehicle project, initially focused on self-driving technology for ride-hailing services. Over time, as the technology evolved, Waymo incrementally expanded into autonomous delivery, reflecting how sequential pivots uncover new applications over time, grounded in methodical learning.

 [felin_kauffman_zenger21-resource_origins_search.pdf](https://github.com/user-attachments/files/17530303/Strategic.Management.Journal.-.2021.-.Felin.-.Resource.origins.and.search.pdf) on 'Resource Origins and Search.' Their concept of 'search images' - firm-specific ways of seeing and identifying valuable resources that others might miss - offers valuable insights for our work. Rather than conducting exhaustive search or relying solely on existing endowments, they argue firms can search more effectively by starting with a functional need or problem they aim to solve. This framework could enhance our understanding of when parallel search is optimal, particularly in situations with low test costs (when the search image clearly guides what to look for), low variance (when the search image helps identify specific resource properties), and low correlation (when the search image enables recognition of novel resource combinations). Their perspective on how firms recognize dormant value in resources could help us better formalize the conditions under which parallel search strategies outperform sequential approaches, especially in evolving market environments.
### 2. Model

| Model Type     | Sample-Action Ratio | Search Space |
| -------------- | ------------------- | ------------ |
| Product→Market | 2:1 + 2:1           | 2+2 options  |
| Market→Product | 2:1 + 2:1           | 2+2 options  |
| Full Search    | 4:1                 | 4 options    |
#### 2.1📍 low cost ratio of sampling to action

compared to four sampling and two actions to choose for T2C1_p
#### 2.2 🎲 high Uncertainty
#### 2.3🧩 low correlation

 ![[🗄️ 🧩correlation examples]]



### 3. TODO/Future Work

##### **Visualization of Pivot Dynamics and Exaptive Opportunities**

Visualization tools can play a crucial role in tracking how exaptive processes drive entrepreneurial pivots. By visualizing the **adjacent possible**, entrepreneurs can identify emerging opportunities and make informed decisions about how to reconfigure their existing resources. **Mansinghka (2021)** and **Chen et al. (2020)** recommend using dynamic visualizations to track the emergence of exaptive opportunities during parallel and sequential search strategies.

**Monika Blattmeier (2023)** delves deeper into the aestheticization of business processes, emphasizing how visualizing their **Gestalt** can enhance collective decision-making. This visualization approach helps entrepreneurs see the holistic potential of their business models and innovation pathways. Such tools foster collective thinking in startups, helping teams make more informed decisions when navigating pivot dynamics.

