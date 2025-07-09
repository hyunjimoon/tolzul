# 🧠💻🧮phantom rmc

### 🧠 computation level

| Section                                                                                                                                                                                                                             | 🔐 Lock and Key                                                                                     | 🧱 Brick                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 🔑 Key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[#1. Theoretical Foundation\|1. Theoretical Foundation]]                                                                                                                                                                           | How do investors form lay theories about unobservable startup qualities?                            | [[📜Gompers20_💰vc_dm]] shows key VC dimensions to model:<br>- Management assessment (95% important)<br>- Business model (83% important)<br>- Product/technology (74% important)<br>- Market (68% important)<br><br>[[📜Kaplan09_🐎jockey_or_horse]] validates importance of observable vs unobservable attributes:<br>- Only 1 of 50 firms changed core business idea<br>- Management turnover very common (only 44% of CEOs remained)<br>- Business idea/model ("horse") more stable than management ("jockey")<br><br>[[📜Agrawal21_ebl_choice]] explains hierarchical uncertainties: beliefs about business model validity (quality of idea) and team execution capability | Framework for modeling investor inference:<br>- Observable terms → perceptual dimensions<br>- Core business (observable) more stable than management (phantom attributes)<br><br>Investor lay theories can be modeled as phantom attributes:<br>- Observable features → perceptual dimensions<br>- Heterogeneous across investor types<br><br>[[#🧠investor's perceptual attributes on founder and business model\|🧠investor's perceptual attributes on founder and business model]] |
| [[#2. Model\|2. Model]]<br><br>- [[#2. Model#🔡🦸‍♂️LLM based profile\|🔡🦸‍♂️LLM based profile]]<br>- [[#2. Model#📝example data\|📝example data]]<br>- [[#2. Model#🌲hierarchical Bayesian model\|🌲hierarchical Bayesian model]] | How to adapt phantom attributes model from consumer choice to venture investment?                   | [[📜Bell22_👻phantom_att]] provides <br>1. foundational framework<br>- When information is incomplete, decision makers infer missing attributes<br>- These "phantom attributes" expand rather than collapse the attribute space<br>- Shows how identical observable attributes map to different perceptions<br><br>2. methodology<br>- Pick-any-J experimental design<br>- Hierarchical Bayesian modeling<br><br>[[📜Kaplan09_🐎jockey_or_horse]] provides validation approach:<br>- Track observable business elements over time<br>- Document management turnover<br>- ❓Measure value creation                                                                               | Model adaptations needed:<br>- Map pick-any-J design to VC context<br>- Include key VC evaluation dimensions<br>- Account for value creation dynamics<br><br>Model adaptations needed:<br>- Modify perceptual dimensions<br>- Adjust experimental design<br>- Account for equilibrium dynamics<br><br>input of [[#🗼hierarchical Bayesian model\|🗼hierarchical Bayesian model]],  [[#📝example data\|📝example data]] using <br><br>![[Pasted image 20241106011155.png\|300]]        |
| [[#3. Future direction\|3. Future direction]]                                                                                                                                                                                       | What is the meaning of this research in <br>1)  research contribution  <br>2) practical application | [[📜Mackey_bayes_mng]]'s essential heterogeneity is captured<br><br>founder can have more informative population level investor's utility                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
 
### 💻algroithm level: example data and coding level

| profile_id | investor_type_id | 👁️observable_features<br>(tech_founder, prior_exits, arr_mm, revenue_growth, patent) | responses<br>(response_execution, response_market, response_talent, response_pmf, response_operations, response_exit) |
| ---------- | ---------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 1          | 1                | [1, 2, 2.0, 0.15, 1]                                                                  | [1, 0, 1, 0, 1, 1]                                                                                                    |
| 2          | 2                | [1, 2, 2.0, 0.15, 1]                                                                  | [1, 1, 1, 0, 0, 0]                                                                                                    |
| 3          | 1                | [0, 0, 0.5, 0.25, 0]                                                                  | [0, 1, 0, 1, 1, 0]                                                                                                    |
| 4          | 2                | [0, 0, 0.5, 0.25, 0]                                                                  | [0, 1, 0, 1, 1, 0]                                                                                                    |
| 5          | 1                | [1, 0, 1.0, 0.20, 1]                                                                  | [1, 0, 1, 1, 0, 1]                                                                                                    |
|            |                  | (discretization)                                                                      |                                                                                                                       |

#### 🌲hierarchical Bayesian model code
The hierarchical Bayesian model formalizes how investors translate observable startup characteristics into investment decisions through both direct and perceptual pathways (perceptual mediates observable and investment decision). At its core, the model captures two key mappings: first, how observable characteristics ($X$) map to perceptual dimensions (Perceptions) through investor-specific coefficients ($\beta$ modified by $\theta$ based on investor characteristics $Z$); and second, how these perceptions combine with direct effects to influence final investment decisions ($Y$) through a utility function. The model's hierarchical structure, discussed extensively in the transcript, allows for three levels of variation: population-level patterns in $\beta$, investor-type-level effects through $\theta$, and individual-level heterogeneity through the correlation structure $\Omega$. The bernoulli_logit likelihood for investment decisions reflects the binary nature of invest/don't invest choices, while the normal and LKJ priors encode reasonable assumptions about parameter distributions. This structure implements the "lay theory mapping" discussed in the transcript, where different investors can construct different meanings from identical startup characteristics.

full factorial (founding team)design (individual models); no imputation needed. model flow through perception, 
using [cld](https://claude.ai/chat/e78a0bff-dd08-456c-b83f-89daae9cf8e2)


```stan
data {
  int<lower=0> N;              // Number of investment decisions
  int<lower=0> O;              // Number of observable deal char.
  int<lower=0> P;              // Number of perceptual dims. (2groups:idea+exec.)
  int<lower=0> A;              // Number of investor archetypes
  int<lower=0> M;              // Number of investor char.
  
  matrix[N, O] X;              // Observable deal char. matrix
  matrix[A, M] Z;              // Investor archetype char.
  int<lower=1,upper=A> type[N];// Investor type for each decision
  int<lower=0,upper=1> Y[N];   // Investment decision (1=invest, 0=pass)
}

parameters {
  // Perception formation parameters
  matrix[O, P] alpha;           // Mapping from observables to perceptions
  matrix[M, O] Theta;          // How investor char. affect mapping
  
  // Investment decision parameters
  vector[P] beta;             // Impact of perceptions on investment decision
  real<lower=0> sigma;         // Decision noise
  
  // Hierarchical parameters
  corr_matrix[O] Omega;        // Correlation between char. effects
  vector<lower=0>[O] tau;      // Scaling for char. effects
}

transformed parameters {
  matrix[N, P] Perceptions;    // Latent perceptual dimensions
  vector[N] InvestmentUtil;    // Investment utility
  
  // Generate perceptions based on char. and investor type
  for (n in 1:N) {
    matrix[O, P] alphaType = alpha + (Theta * Z[type[n]])';
    Perceptions[n] = X[n] * alphaType;
  }
  
  // Calculate investment utility
  InvestmentUtil = Perceptions * beta;
}

model {
  // Priors
  to_vector(alpha) ~ normal(0, 1);
  to_vector(Theta) ~ normal(0, 0.5);
  beta ~ normal(0, 1);
  tau ~ cauchy(0, 2.5);
  Omega ~ lkj_corr(2);
  
  // Investment decision likelihood
  Y ~ bernoulli_logit(InvestmentUtil);
}

```

### 🧮implementation