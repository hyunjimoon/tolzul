# 2. Need Analysis and Mathematical Foundation

This section introduces the core mathematical insight at the heart of STRAP: the duality between uncertainty minimization and success probability maximization. I begin with a brief analysis of the challenges in entrepreneurial decision-making, then develop the formal mathematical framework that transforms how we understand and address these challenges.

## 2.1 The Tractability-Reality Gap in Entrepreneurial Decision-Making

Entrepreneurial decision models face an inherent tension between tractability and reality. Simple models are computationally manageable but fail to capture the complex, multi-stakeholder, dynamic nature of real ventures. Comprehensive models better reflect reality but quickly become computationally intractable.

| Model Type                    | Multi-stakeholder Complexity | Dynamic operational Complexity | Tractability | Reality Fit | Key Need                       | Reference                                                          |
| ----------------------------- | ---------------------------- | ------------------------------ | ------------ | ----------- | ------------------------------ | ------------------------------------------------------------------ |
| Single-Stakeholder Static     | No                           | No                             | High         | Poor        | More realistic representation  | Sarasvathy (2001); McMullen & Shepherd (2006)                      |
| Single-Stakeholder Dynamic    | No                           | Yes                            | Medium       | Medium      | Multiple stakeholder view      | Håkansson (1971); McGrath (1999)                                   |
| Multi-Stakeholder Static      | Yes                          | No                             | Medium       | Medium      | Sequential decision capability | Van den Steen (2016); Gans, Hsu & Stern (2002)                     |
| **Multi-Stakeholder Dynamic** | Yes                          | Yes                            | Low→Medium   | High        | **Computational tractability** | Schindehutte & Morris (2009); Garud & Karnøe (2003); Roundy (2018) |

The STRAP framework addresses this tension through a novel mathematical approach: using primal-dual optimization to transform an otherwise intractable planning problem into a series of manageable decisions guided by a clear threshold rule.

## 2.2 The Primal Formulation: Uncertainty Minimization

At its core, entrepreneurial decision-making involves reducing critical uncertainties with limited resources. I formalize this as an optimization problem where the entrepreneur seeks to minimize a weighted sum of stakeholder-specific uncertainties:

$$\begin{aligned} \min_{\textcolor{red}{a} \in \textcolor{red}{A}} \quad & \textcolor{violet}{W_d}\cdot\textcolor{#3399FF}{U_d} + \textcolor{violet}{W_s}\cdot\textcolor{#3399FF}{U_s} + \textcolor{violet}{W_i}\cdot\textcolor{#3399FF}{U_i} \ \text{subject to} \quad & \sum_{j} c_j \textcolor{red}{a_j} \leq \textcolor{#3399FF}{R} \end{aligned}$$

Where:

- $\textcolor{#3399FF}{U_d}$, $\textcolor{#3399FF}{U_s}$, $\textcolor{#3399FF}{U_i}$ represent uncertainties facing demand-side, supply-side, and investor stakeholders
- $\textcolor{violet}{W_d}$, $\textcolor{violet}{W_s}$, $\textcolor{violet}{W_i}$ are the weights reflecting each stakeholder's importance
- $\textcolor{red}{a_j}$ indicates whether action/experiment $j$ is chosen
- $c_j$ is the cost of action $j$
- $\textcolor{#3399FF}{R}$ is the available resource budget

This primal formulation captures the essence of entrepreneurial decision-making: systematically reducing the most important uncertainties given limited resources. Each uncertainty $\textcolor{#3399FF}{U_j}$ can be mathematically represented as the entropy of a stakeholder's belief distribution: $\textcolor{#3399FF}{U_j} = H(p_j(\textcolor{red}{a})|\textcolor{red}{a})$, where $p_j$ is stakeholder $j$'s probability distribution over possible outcomes.

NEED EXAMPLE!!
## 2.3 The Dual Formulation: Success Probability Maximization

Through mathematical transformation, this primal problem yields a revealing dual formulation:

$$\begin{aligned} \max_{\lambda, \beta, \gamma} \quad & \sum_{j \in {d,s,i}} \textcolor{violet}{w_j}[\lambda_j + \beta_j^T \textcolor{#3399FF}{\mu_j}(\textcolor{red}{a_j}) - \log Z_j(\beta_j)] - \gamma \textcolor{#3399FF}{R} \ \text{subject to} \quad & \gamma \geq 0 \end{aligned}$$

Where:

- $\lambda_j$ is the dual variable for stakeholder $j$'s normalization constraint
- $\beta_j$ is the dual variable for stakeholder $j$'s expectation constraint
- $\gamma$ is the dual variable for the resource constraint
- $\textcolor{#3399FF}{\mu_j}(\textcolor{red}{a_j})$ is stakeholder $j$'s expected outcome given action $a_j$
- $Z_j(\beta_j)$ is the partition function (normalizer) of stakeholder $j$'s decision model

**The key insight**: This dual formulation represents **maximizing the weighted log-likelihood that all stakeholders will be satisfied** with the venture's outcome, minus the opportunity cost of resources. In other words, the primal goal of minimizing uncertainty is mathematically equivalent to maximizing the probability of success.

This duality transforms how we understand entrepreneurial decision-making:

1. Reducing a stakeholder's uncertainty directly increases the probability they will be satisfied
2. The more important a stakeholder (higher $\textcolor{violet}{w_j}$), the more their satisfaction influences overall success probability
3. Resource constraints ($\textcolor{#3399FF}{R}$) create an opportunity cost ($\gamma$) that must be balanced against information gains

## 2.4 The Decision Rule: When to Run an Experiment

From the dual formulation emerges a practical decision rule for experiment selection. Action $j$ should be chosen (set $\textcolor{red}{a_j^*} = 1$) if and only if:

$$\textcolor{violet}{w_j}[\lambda_j + \beta_j^T \textcolor{#3399FF}{\mu_j}(1) - \log Z_j(\beta_j)] > \gamma c_j$$

In plain language: **Run an experiment when its contribution to stakeholder satisfaction likelihood exceeds its resource cost**.

Breaking down this rule:

- Left side: The weighted increase in satisfaction likelihood for stakeholder $j$ if action $j$ is performed
- Right side: The opportunity cost of the resources consumed by action $j$
- $\lambda_j$: How far stakeholder $j$ is from being satisfied (higher = more convincing needed)
- $\beta_j^T \textcolor{#3399FF}{\mu_j}(1) - \log Z_j(\beta_j)$: How much action $j$ improves stakeholder $j$'s satisfaction probability
- $\gamma$: The "exchange rate" between resources and likelihood improvement (shadow price)

This decision rule operationalizes the uncertainty-probability duality, providing entrepreneurs with a clear threshold for action: pursue experiments that deliver sufficient information value relative to their cost, prioritizing actions that address the "bottleneck" stakeholder (highest weighted uncertainty).

## 2.5 Three Challenges Reframed Through the Duality

The uncertainty-probability duality reframes the three core challenges of entrepreneurial decision-making:

1. **Perception Challenge**: Understanding stakeholder uncertainties becomes equivalent to modeling their satisfaction probabilities. Different stakeholders (investors, customers, partners) perceive venture attributes differently, creating an information asymmetry problem that can be addressed through Bayesian modeling of their satisfaction conditions.
    
2. **Sequencing Challenge**: Choosing which experiment to run next becomes equivalent to maximizing the increase in success probability per resource unit. This transforms an otherwise intractable planning problem into a tractable threshold-based decision rule.
    
3. **Confirmation Challenge**: Aligning stakeholder expectations becomes equivalent to maximizing their joint satisfaction probability. Circular dependencies (each stakeholder waiting for others) can be broken by targeting experiments that create information spillovers across multiple stakeholders.
    
By recasting entrepreneurial decision-making through this mathematical duality, STRAP provides both theoretical insight and practical guidance. The next section details how this duality is implemented through the three components of the STRAP framework.
$$ \begin{aligned} \min_{\textcolor{red}{a} \in \textcolor{red}{A}} \quad & \textcolor{purple}{W_d}\cdot\textcolor{#3399FF}{U_d} + \textcolor{purple}{W_s}\cdot\textcolor{#3399FF}{U_s} + \textcolor{purple}{W_i}\cdot\textcolor{#3399FF}{U_i} && \text{(Objective)} \ \text{s.t.} \quad & B,\textcolor{green}{S} = [\textcolor{#3399FF}{U_d},,\textcolor{#3399FF}{U_s},,\textcolor{#3399FF}{U_i}] && \text{(Uncertainty-State Mapping)} \ & C,\textcolor{red}{A} \leq \textcolor{#3399FF}{R} && \text{(Resource Budget)} \ & D(\textcolor{green}{S},,\textcolor{red}{A}) = \textcolor{green}{S'} && \text{(State Transition)} \end{aligned} $$

We explain how this formulation captures the three challenges: reducing uncertainty for individual stakeholders (📽️ perception), aligning multi-stakeholder dynamics (🔄 coordination), and selecting actions under resource limits (⚡ bottleneck-breaking).

### 2.4 Primal-Dual Optimization Formulation

We also present the primal-dual optimization formulation that provides complementary insights into the entrepreneurial decision problem:

**Primal (Uncertainty Minimization):** $$ \begin{aligned} \min_{p,\textcolor{red}{a}} \quad & \sum_{j \in {d,s,i}} \textcolor{purple}{w_j} H(p_j|\textcolor{red}{a}) \ \text{s.t.} \quad & \sum_{k} p_{jk} = 1, \quad \forall j \ & \sum_{k} p_{jk} f_{jk} = \textcolor{green}{\mu_j}(\textcolor{red}{a}), \quad \forall j \ & p_{jk} \geq 0, \quad \forall j,k \ & \sum_{j} c_j \textcolor{red}{a_j} \leq \textcolor{#3399FF}{R} \ & \textcolor{red}{a_j} \in {0,1}, \quad \forall j \end{aligned} $$

**Dual (Likelihood Maximization):** $$ \begin{aligned} \max_{\lambda, \beta, \gamma} \quad & \sum_{j \in {d,s,i}} \textcolor{purple}{w_j}[\lambda_j + \beta_j^T \textcolor{green}{\mu_j}(\textcolor{red}{a_j}) - \log Z_j(\beta_j)] - \gamma \textcolor{#3399FF}{R} \ \text{s.t.} \quad & \gamma \geq 0 \ & \text{where } \textcolor{red}{a_j^*} = \begin{cases} 1 & \text{if } \textcolor{purple}{w_j}[\lambda_j + \beta_j^T \textcolor{green}{\mu_j}(1) - \log Z_j(\beta_j)] > \gamma c_j \ 0 & \text{otherwise} \end{cases} \end{aligned} $$

This dual formulation provides critical insights by transforming the uncertainty minimization problem into a likelihood maximization problem—revealing how entrepreneurs can maximize the probability of stakeholder satisfaction while optimizing resource allocation.
