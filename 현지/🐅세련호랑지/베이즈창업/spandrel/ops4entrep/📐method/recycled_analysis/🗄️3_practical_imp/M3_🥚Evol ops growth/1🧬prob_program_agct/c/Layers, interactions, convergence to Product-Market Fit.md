Optimism as a catalyst
## Abstract

My model captures early stage startup's trade off between optimism and understanding. With simulation model, we show how self-optimism serves engine for executing experiments. However, it transitioned to better understanding of the environment through experiments. It shows two mechanisms of how self-optimism affects learning. Learning is defined as how the startup attributes the gap between predicted and observed profitability to its belief on production feasibility and market's acceptance on different product. 

Initial dose of optimism catalyzes experiments but addiction to this impairs startup's ability to update its belief on product market  signal interpretation. 

without gradual diminish of dose,  and lame update of belief components suboptimally.

By framing experiment as iteration of predict, observe, update belief and environment) and treating as missing variable we use EM algorithm

Execution is first galvanized by 

## Intro

Extending the three layer (technology, product module, market) concept from technology roadmapping  (Bruce & Fine, 2007), we construct four layers (belief, product's expected profitability, product-market, market's signal) as table below. Experiments can be framed as interaction between the layers and EM algorithm lends framework for optimal experiment strategy.


![[Pasted image 20240604022837.png|500]]

 
| EM Algorithm                                   | Pivot to Product-Market Fit              |
| ---------------------------------------------- | ---------------------------------------- |
| **Layer 3 (Market's signal)**                  | Observed Data $y$                        |
| **Layer 2 (Product-Market)**                   | Missing Data/Latent Variables $\gamma^2$ |
| **Layer 1 (Product's expected profitability)** | Parameters $\phi$                        |
| **Layer 0 (Belief)**                           | Missing Data/Latent Variables $\gamma^1$ |

- Directly finding the product $\phi$ that maximizes $p(\phi | y)$ based on market signal $y$ is difficult.
- Introducing latent variables: belief $\gamma^1$ and product-market $\gamma^2$ makes it easier to work with:
  - $p(\phi | \gamma^1, \gamma^2, y)$: Predicting product's expected profitability given belief, product-market, and market signal.
  - $p(\gamma^1, \gamma^2 | \phi, y)$: Updating belief and product-market given product's expected profitability and market signal.
  - EM algorithm which is an iterative method for finding the mode of the marginal posterior density, $p(\phi | y)$  (Gelman et. al. , 2015 [[📜BDA(alg(EM))]]. ) can be of aid. It is useful for models where maximizing $p(\phi | y)$ directly is difficult, but working with $p(\gamma | \phi, y)$ and $p(\phi | \gamma, y)$ is easier. Here, $\phi$ represents the parameters in our problem, and $\gamma$ represents missing data. The EM algorithm formalizes the process of handling missing data: 1. **Start with a guess of the parameters \(\phi\).** 2. **Expectation Step**: Replace missing values by their expectations given the guessed parameters \(\phi\). 3. **Maximization Step**: Estimate parameters assuming the missing data are equal to their estimated values. 4. **Iterate**: Re-estimate the missing values and parameters until convergence.

### 4 layers
### 4 Actions:
1. **Predict (BAL)**:
   - **From Latent Belief to Product**:
     - The latent beliefs (L[0]) are used to predict the outcomes for the products (A[0], A[1], A[2], ...).
     - In the context of the code, this is where `mu_b_b`, `mu_c_b`, and `mu_a` are used to predict the `profit_b` for different product-market combinations.
     - This corresponds to the line in the code:
       ```python
       for i, product in enumerate(products):
           for j, market in enumerate(markets):
               exPMN['profit_b'][i, j, e] = (
                   exPMN['mu_a'][e] +
                   pow(-1, e2p[product]+1) * exPMN['mu_b_b'][e]/2 +
                   pow(-1, e2m[market]+1) * exPMN['mu_c_b'][e]/2
               )
       ```

2. **Observe (CIA)**:
   - **From Product to Market**:
     - The product outcomes (A[0], A[1], A[2], ...) are observed in the market (C[A[1]], C[A[2]], C[A[3]], ...).
     - In the context of the code, this is where the `profit_obs` is observed from the actual market.
     - This corresponds to the line in the code:
       ```python
       exPMN['profit_obs'][e] = sample_profit_obs(e, exPMN)
       ```

3. **Update A (ABC)**:
   - **From Product to Product-Market**:
     - The product outcomes (A[0], A[1], A[2], ...) are updated based on the observations, and this impacts the product-market combinations (B[0], B[1], B[2], ...).
     - In the context of the code, this is where the `action` is decided and updates to the product-market combinations are made.
     - This corresponds to the line in the code:
       ```python
       exPMN['action'][e] = decide_action(exPMN['profit_obs'][e], exPMN['low_profit_b'][e], exPMN['high_profit_b'][e])
       ```

4. **Update L (LBC)**:
   - **From Latent Belief to Product-Market**:
     - The latent beliefs (L[0]) are updated based on the new product-market outcomes (B[0], B[1], B[2], ...), which in turn affect the product-market combinations (C[A[1]], C[A[2]], C[A[3]], ...).
     - In the context of the code, this is where the posterior samples are used to update the latent beliefs (`mu_a_post`, `mu_b_b_post`, `mu_c_b_post`).
     - This corresponds to the lines in the code:
       ```python
       exPMN['mu_a_post'][e] = fit.stan_variable('mu_a')
       exPMN['mu_b_b_post'][e] = fit.stan_variable('mu_b_b')
       if e > 0:
           exPMN['mu_c_b_post'][e] = exPMN['mu_c_b_post'][e-1]
       else:
           exPMN['mu_c_b_post'][e] = exPMN['mu_c_b'][e]
       ```

### Interaction Between Layers:
- The arrows show the flow of information and updates across layers:
  1. **Predict**: Latent beliefs are used to predict product outcomes.
  2. **Observe**: Product outcomes are observed in the market.
  3. **Update A**: Observations are used to update product and market combinations.
  4. **Update L**: Latent beliefs are updated based on new product-market outcomes.

This iterative process reflects the feedback loop between beliefs, products, and market outcomes, driving continuous adaptation and optimization of product-market strategies. The framework visually represents how each layer influences and updates the other layers through the key actions.


### Visualizing EM Algorithm with Belief Updates

The updated plot will illustrate how each belief component (\(\mu_b_b\), \(\mu_c_b\), \(\mu_a\)) and the profit beliefs evolve over time, highlighting the interaction between the layers through the key actions.


The diagram illustrates the interactions between different layers (market, product-market, product, and latent belief) through the four key actions: predict, observe, update A, and update L. 

EM algorithm is useful when it's hard to maximize p( φ| y) directly but easy to work with p( γ|φ , y) and p( φ|γ , y). 

The name ‘EM’ comes from the two alternating steps: ﬁnding the expectation of the needed functions (the suﬃcient statistics) of the missing values, and maximizing the resulting posterior density to estimate the parameters as if these functions of the missing data were observed.

Finding marginal posterior modes using EM

The EM algorithm can be viewed as an iterative method for ﬁnding the mode of the marginal posterior density, p( φ| y), and is extremely useful for many common models for which it is hard to maximize p( φ| y) directly but easy to work with p( γ|φ , y) and p( φ|γ , y). If we think of φ as the parameters in our problem and γ as missing data, the EM algorithm formalizes the idea of handling missing data: start with a guess of the parameters and then (1) replace missing values by their expectations given the guessed parameters, (2) estimate parameters assuming the missing data are equal to their estimated values, (3) re-estimate the missing values assuming the new parameter estimates are correct, (4) re-estimate parameters, and so forth, iterating until convergence. In fact, the EM algorithm is more eﬃcient than these four steps would suggest since each missing value is not estimated separately; instead, those functions of the missing data that are needed to estimate the model parameters are estimated jointly.

| EM Algorithm                                   | Pivot to Product-Market Fit                |
| ---------------------------------------------- | ------------------------------------------ |
| **Layer 3 (Market's signal)**                  | Observed Data (y)                          |
| **Layer 2 (Product-Market)**                   | Missing Data/Latent Variables ($\gamma^2$) |
| **Layer 1 (Product's expected profitability)** | Parameters ($\phi$)                        |
| **Layer 0 (Belief)**                           | Missing Data/Latent Variables ($\gamma^1$) |
directly finding product $\phi$ maximizing  p( φ| y) based on market signal $y$ is hard so we introduce latent variables: belief ($\gamma^1$) and product-market ($\gamma^2$). It's easier to work with 
 - $p( φ|\gamma^1, \gamma^2, y)$ : predicting product's expected profitability given belief, product-market, market's signal
 - $p( \gamma^1, \gamma^2|φ , y)$ : updating belief and product market given product's expected profitability and market's signal

may need a variant as $p( \gamma^1, \gamma^2|φ , y)$  is in fact  $p( \gamma^1_{t+1}, \gamma^2_{t+1}|\gamma^1_t, \gamma^2_t, φ , y)$ where $p( \gamma^2_{t+1}|\gamma^2_{t}φ , y)$ is deterministic mapping with heuristic decision rule (low and high bar setting given k). $p( \gamma^1_{t+1}|\gamma^1_{t}φ , y)$ is also deterministic mapping with bayes rule.
 

### Layers:
1. **Layer 0 (Latent Belief)**:
   - This layer represents the underlying beliefs about costs (mu_b_b), revenues (mu_c_b), and baseline profit (mu_a).

2. **Layer 1 (Product)**:
   - This layer represents the products being developed based on the latent beliefs.

3. **Layer 2 (Product-Market)**:
   - This layer represents the product-market combinations, where each product is associated with different markets.

4. **Layer 3 (Market)**:
   - This layer represents the markets or applications driving the products' development.

### Key Actions:
1. **Predict (BAL)**:
   - **From Latent Belief to Product**:
     - The latent beliefs (L[0]) are used to predict the outcomes for the products (A[0], A[1], A[2], ...).
     - In the context of the code, this is where `mu_b_b`, `mu_c_b`, and `mu_a` are used to predict the `profit_b` for different product-market combinations.
     - This corresponds to the line in the code:
       ```python
       exPMN['profit_b'][i, j, e] = (
           exPMN['mu_a'][e] +
           pow(-1, e2p[product]+1) * exPMN['mu_b_b'][e]/2 +
           pow(-1, e2m[market]+1) * exPMN['mu_c_b'][e]/2
       )
       ```

2. **Observe (CIA)**:
   - **From Product to Market**:
     - The product outcomes (A[0], A[1], A[2], ...) are observed in the market (C[A[1]], C[A[2]], C[A[3]], ...).
     - In the context of the code, this is where the `profit_obs` is observed from the actual market.
     - This corresponds to the line in the code:
       ```python
       exPMN['profit_obs'][e] = sample_profit_obs(e, exPMN)
       ```

3. **Update A (ABC)**:
   - **From Product to Product-Market**:
     - The product outcomes (A[0], A[1], A[2], ...) are updated based on the observations, and this impacts the product-market combinations (B[0], B[1], B[2], ...).
     - In the context of the code, this is where the `action` is decided and updates to the product-market combinations are made.
     - This corresponds to the line in the code:
       ```python
       exPMN['action'][e] = decide_action(exPMN['profit_obs'][e], exPMN['low_profit_b'][e], exPMN['high_profit_b'][e])
       ```

4. **Update L (LBC)**:
   - **From Latent Belief to Product-Market**:
     - The latent beliefs (L[0]) are updated based on the new product-market outcomes (B[0], B[1], B[2], ...), which in turn affect the product-market combinations (C[A[1]], C[A[2]], C[A[3]], ...).
     - In the context of the code, this is where the posterior samples are used to update the latent beliefs (`mu_a_post`, `mu_b_b_post`, `mu_c_b_post`).
     - This corresponds to the lines in the code:
       ```python
       exPMN['mu_a_post'][e] = fit.stan_variable('mu_a')
       exPMN['mu_b_b_post'][e] = fit.stan_variable('mu_b_b')
       if e > 0:
           exPMN['mu_c_b_post'][e] = exPMN['mu_c_b_post'][e-1]
       else:
           exPMN['mu_c_b_post'][e] = exPMN['mu_c_b'][e]
       ```

### Interaction Between Layers:
- The arrows show the flow of information and updates across layers:
  1. **Predict**: Latent beliefs are used to predict product outcomes.
  2. **Observe**: Product outcomes are observed in the market.
  3. **Update A**: Observations are used to update product and market combinations.
  4. **Update L**: Latent beliefs are updated based on new product-market outcomes.

This iterative process reflects the feedback loop between beliefs, products, and market outcomes, driving continuous adaptation and optimization of product-market strategies. The framework visually represents how each layer influences and updates the other layers through the key actions.