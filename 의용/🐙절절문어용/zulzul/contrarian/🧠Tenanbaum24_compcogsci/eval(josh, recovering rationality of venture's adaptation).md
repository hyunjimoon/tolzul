this class project for Josh Tenenbaum's [[966 Computational Cognitive Science]] 

**Research Question:**  **Research Question:** How do entrepreneurs allocate limited cognitive resources between cost-reduction and revenue-growth activities during venture scaling? Like organisms under evolutionary pressure, entrepreneurs face dual uncertainties about their core idea's value and their strategy's effectiveness. What appears as "biased" resource allocation may actually represent rational adaptations to different industry environments i.e. "explaining away" irrationality with environments.

**Methodology:** Drawing on computational rationality and resource-rational decision making theories, we conceptualize entrepreneurial resource allocation as a vector with magnitude (processing speed) and direction (operational cost-reducing vs. market revenue growth). Our computational model captures entrepreneurial decision-making through three core mechanisms:

1. **Belief Updates:** $\color{Green}{p_c} \sim Beta(\alpha_c, \beta_c), \color{#C0A0C0}{p_r} \sim Beta(\alpha_r, \beta_r)$  Entrepreneurs maintain and update beliefs about cost-reduction ($\color{Green}{p_c}$) and revenue-growth ($\color{#C0A0C0}{p_r}$) probabilities through environmental signals.

2. **Processing Speed:** $\color{Green}{pred_c} = exp(N(\color{Green}{p_c}, \sigma)), \color{#C0A0C0}{pred_r} = exp(N(\color{#C0A0C0}{p_r}, \sigma))$ Parameter σ controls the speed-accuracy tradeoff in decision-making, transforming beliefs through log-normal noise.

3. **Action Selection:**   $\color{Red}{a^*} = \underset{\color{Red}{a \in \{a_c, a_r\}}}{\arg\max} \: \Delta\color{Red}{U}(\color{Green}{pred_c}, \color{#C0A0C0}{pred_r}, \color{Red}{a})$ where $\color{Red}{\Delta U} = \color{Green}{pred_c} \cdot \color{Red}{a_c} + \color{#C0A0C0}{pred_r} \cdot \color{Red}{a_r}$ subject to $\color{Red}{a_c} + \color{Red}{a_r} = 1$ Entrepreneurs choose between operational ($\color{Red}{a_c}$) and market ($\color{Red}{a_r}$) focus based on expected change in utility, which is the sum of predicted returns weighted by action allocation.

**Contributions**: This research will advance theory by providing a unified framework for understanding rational adaptation in entrepreneurial decision-making, while offering practical guidelines for context-specific resource allocation optimization. Table of contents:

full paper in [[📝🧭Vectorizing Adaptation]]

1. Bhui, R., Lai, L., & Gershman, S. J. (2021). Resource-rational decision making. _Current Opinion in Behavioral Sciences_, _41_, 15-21.
2. Ching, K., Gans, J., & Stern, S. (2019). Control versus execution: endogenous appropriability and entrepreneurial strategy. _Industrial and Corporate Change_, _28_(2), 389-408. 
3. Gans, J. S. (2023). Experimental choice and disruptive technologies. _Management Science_, _69_(11), 7044-7058.
4. Gershman, S. J., Horvitz, E. J., & Tenenbaum, J. B. (2015). Computational rationality: A converging paradigm for intelligence in brains, minds, and machines. _Science_, _349_(6245), 273-278.
5. Phadnis, S, and C. Fine (2017), “End-to-end Supply Chain Strategies: Parametric Study of the Apparel Industry,” Production and Operations Management, 26(12), 2305-2322.
6. Vul, E., Goodman, N., Griffiths, T. L., & Tenenbaum, J. B. (2014). One and done? Optimal decisions from very few samples. _Cognitive science_, _38_(4), 599-637. Direction