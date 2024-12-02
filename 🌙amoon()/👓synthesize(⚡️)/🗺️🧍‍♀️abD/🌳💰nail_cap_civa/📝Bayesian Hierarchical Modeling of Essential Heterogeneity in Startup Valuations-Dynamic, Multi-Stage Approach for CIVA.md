- with  [📐the metrics team cld pj](https://claude.ai/project/83715869-5764-4521-883e-9842b10a85eb)  [[jeff_dotson]], [[amir_sariri]],
- EMP grow faster vs control  https://docs.google.com/document/d/1aoByFRg7NBwgg6hWTYhzQnLd6mZUZreyz84yiNlAZ4Q/edit?tab=t.0#heading=h.omjz0330srqr
# making baseline hierarchical bayes models for CIVA
from hyunjimoon on 2024-09-21T18:20:07Z


1. Model Structure:

   Level 1 (Individual Startup):
   log(Valuation_it) = β_0i + β_1i * Stage_it + β_2i * Revenue_it + β_3i * Employees_it + ε_it
   
   Where:
   i = individual startup
   t = time period
   ε_it ~ N(0, σ^2)

   Level 2 (Startup-specific parameters):
   β_0i = γ_00 + γ_01 * Industry_i + γ_02 * FounderExperience_i + u_0i
   β_1i = γ_10 + γ_11 * Industry_i + u_1i
   β_2i = γ_20 + u_2i
   β_3i = γ_30 + u_3i

   Where:
   u_0i, u_1i, u_2i, u_3i ~ MVN(0, Σ)

2. Prior Distributions:
   γ_00, γ_01, γ_02, γ_10, γ_11, γ_20, γ_30 ~ N(0, 10) 
   σ^2 ~ InvGamma(0.01, 0.01)
   Σ ~ InvWishart(I, 5)

This model structure allows for:

1. Firm-specific effects: Each startup has its own intercept and slopes, capturing heterogeneity.
2. Industry effects: The impact of industry on both the baseline valuation and the effect of funding stage.
3. Founder experience: Incorporated at the startup level to affect baseline valuation.
4. Time-varying covariates: Stage, Revenue, and Employees can change over time for each startup.
5. Correlated random effects: The multivariate normal distribution for the u terms allows for correlation between the random effects.

1. Captures heterogeneity across startups and industries.
2. Allows for both startup-specific and population-level inferences.
3. Can handle unbalanced panel data (startups observed at different time points).
4. Incorporates prior knowledge through the prior distributions.
5. Can be easily extended to include more covariates or levels as needed.


```julia
using Gen

@gen function startup_valuation_model(num_startups, num_timepoints, industry, founder_experience, stage, revenue, employees)
    # Hyperparameters
    γ_00 ~ normal(0, 10)
    γ_01 ~ normal(0, 10)
    γ_02 ~ normal(0, 10)
    γ_10 ~ normal(0, 10)
    γ_11 ~ normal(0, 10)
    γ_20 ~ normal(0, 10)
    γ_30 ~ normal(0, 10)

    σ² ~ inv_gamma(0.01, 0.01)
    Σ ~ inv_wishart(4, eye(4))

    # Startup-level parameters
    for i in 1:num_startups
        β_0i ~ mvnormal([
            γ_00 + γ_01 * industry[i] + γ_02 * founder_experience[i],
            γ_10 + γ_11 * industry[i],
            γ_20,
            γ_30
        ], Σ)
    end

    # Observations
    for i in 1:num_startups
        for t in 1:num_timepoints
            μ = β_0i[1] + β_0i[2] * stage[i, t] + β_0i[3] * revenue[i, t] + β_0i[4] * employees[i, t]
            log_valuation = {:log_valuation => (i, t)} ~ normal(μ, sqrt(σ²))
        end
    end
end

# Data preparation (you'd replace this with your actual data)
num_startups = 100
num_timepoints = 5
industry = rand(1:5, num_startups)
founder_experience = rand(0:20, num_startups)
stage = rand(1:4, num_startups, num_timepoints)
revenue = rand(LogNormal(10, 2), num_startups, num_timepoints)
employees = rand(LogNormal(3, 1), num_startups, num_timepoints)

# Observed log valuations (you'd replace this with your actual data)
observed_log_valuations = rand(Normal(15, 2), num_startups, num_timepoints)

# Create observations dictionary
observations = Dict()
for i in 1:num_startups
    for t in 1:num_timepoints
        observations[(:log_valuation, i, t)] = observed_log_valuations[i, t]
    end
end

# Perform inference
traces, weights = importance_resampling(startup_valuation_model, (num_startups, num_timepoints, industry, founder_experience, stage, revenue, employees), observations, 1000)

# Extract and analyze results
# (You would add code here to extract parameter estimates, calculate credible intervals, etc.)
```

[BMEV with Marr3 cld](https://claude.ai/chat/71e6e283-f339-4616-9013-da51127464fe) reports `inv_wishart` function is not built into Gen, so we might need to use Stan.

```stan
data {
  int<lower=0> N; // Number of startups
  int<lower=0> T; // Number of time points
  int<lower=0> I; // Number of industries
  
  vector[N] industry; // Industry indicator for each startup
  vector[N] founder_experience; // Founder experience for each startup
  int<lower=1, upper=4> stage[N, T]; // Funding stage for each startup at each time point
  vector[N * T] revenue; // Revenue for each startup at each time point
  vector[N * T] employees; // Number of employees for each startup at each time point
  
  vector[N * T] log_valuation; // Observed log valuations
}

parameters {
  vector[7] gamma; // Population-level effects
  real<lower=0> sigma; // Residual SD
  
  matrix[4, N] z; // Matrix for non-centered parameterization
  cholesky_factor_corr[4] L_Omega; // Cholesky factor of correlation matrix
  vector<lower=0>[4] tau; // SDs of random effects
}

transformed parameters {
  matrix[4, N] beta; // Startup-specific effects
  
  // Non-centered parameterization of random effects
  beta = diag_pre_multiply(tau, L_Omega) * z;
  
  // Adding population-level effects
  beta[1] += gamma[1] + gamma[2] * industry + gamma[3] * founder_experience;
  beta[2] += gamma[4] + gamma[5] * industry;
  beta[3] += gamma[6];
  beta[4] += gamma[7];
}

model {
  vector[N * T] mu;
  
  // Priors
  gamma ~ normal(0, 10);
  sigma ~ inv_gamma(0.01, 0.01);
  tau ~ cauchy(0, 2.5);
  L_Omega ~ lkj_corr_cholesky(2);
  
  to_vector(z) ~ normal(0, 1);
  
  // Likelihood
  for (i in 1:N) {
    for (t in 1:T) {
      int idx = (i-1)*T + t;
      mu[idx] = beta[1, i] + beta[2, i] * stage[i, t] + beta[3, i] * revenue[idx] + beta[4, i] * employees[idx];
    }
  }
  
  log_valuation ~ normal(mu, sigma);
}

generated quantities {
  matrix[4, 4] Omega;
  Omega = multiply_lower_tri_self_transpose(L_Omega);
}
```

---

## Reply from hyunjimoon on 2024-09-29T17:30:24Z

preparing meeting
## 1. goal: illustrating essential heterogeneity to bayesian entrepreneurship scholars (#234) 
hypothesis: due to lines of research on choice
- test two choose one [Gans et al 19_found_es.pdf](https://github.com/user-attachments/files/17192400/Gans.et.al.19_found_es.pdf)
 
- choosing technology [Gans20_chooset.pdf](https://github.com/user-attachments/files/17192389/Gans20_chooset.pdf), 
- [Enabling Entrepreneurial Choice](https://pubsonline.informs.org/doi/abs/10.1287/mnsc.2020.3920) 
- [textbook: ent.strat and choice](https://seagull.wwnorton.com/entrepreneurship) 
it would be great if there exist some summary statistics of term sheet that captures essential heterogeneity from 
[MackeyDotson24_Bayesian Stats in Mangement.pdf](https://github.com/user-attachments/files/17180164/MackeyDotson24_Bayesian.Stats.in.Mangement.pdf)

Essential heterogeneity extends beyond simple heterogeneity by recognizing that variations in effects are not just random differences between units, but are systematically related to the units' choices. This correlation between choice and effect poses significant challenges for estimation, invalidating traditional methods like instrumental variables or simple regression approaches. 

In the context of strategy research, such as studying diversification's impact on firm performance, essential heterogeneity acknowledges that firms choose to diversify based on their expected benefits. This necessitates a more complex modeling approach that jointly considers both the choice to adopt a strategy and its subsequent effects. 

Bayesian methods, particularly hierarchical models, are well-suited for this task as they allow researchers to explicitly model the data-generating process, including the decision-making mechanism and its relationship to outcomes. This approach provides a more accurate representation of strategic decision-making and its consequences, overcoming the limitations of methods that assume randomization or independence between choices and their effects.

| Aspect                    | Heterogeneity                       | Essential <br> Heterogeneity                                       |
| :------------------------ | :---------------------------------------- | :----------------------------------------------------------------------- |
| Definition                | Varying <br> effects across <br> units    | Varying <br> effects <br> correlated <br> with choice                    |
| Cause                     | Natural unit <br> differences             | Strategic <br> selection                                                 |
| Relation <br> to choice   | Independent                               | Correlated                                                               |
| Impact on <br> estimation | Addressable <br> with random <br> effects | Invalidates <br> traditional IV <br> and <br> regression <br> approaches |
| Key <br> implication      | Effects differ <br> by unit               | Units choose <br> based on <br> expected <br> effects                    |
| Modeling                  | Random <br> effects <br> sufficient       | Joint choice- <br> outcome <br> modeling <br> required                   |



---

### Reply from hyunjimoon on 2024-09-30T15:08:39Z

## 2. data to collect
based on [Applying Essential Heterogeneity to Early-Stage Startup Valuations cld](https://claude.ai/chat/6a5e9ed2-3fba-47ad-a6f1-5520424c70a1)

three types of data: 
- 🔢`Quantitative startup metrics`: Collect data on easily measurable factors such as revenue, number of employees, founder experience (in years), funding stage, and industry sector. This data would serve as the baseline for the valuation model.

- 😎`Qualitative startup information`: Gather textual data from startup profiles, pitch decks, and company descriptions. This could include information about the startup's mission, market opportunity, competitive advantage, and team background. An LLM could be used to parse this text data and identify common themes or characteristics across startups.

- 💰`Investor decision`: Collect information on investor decisions, including which startups they chose to invest in, the terms of the investments (e.g., SAFE agreement details), and any public statements or rationales provided for their investment decisions. This data would help model the investor decision-making process, which is crucial for capturing the essential heterogeneity in startup valuations.

---

for 😎, 💰

table is sorted from the most efficient persuasion (high 💡/💰) to the least efficient (low 💡/💰), considering our goal of illustrating essential heterogeneity to Bayesian entrepreneurs. The top rows represent data categories that provide the most valuable information relative to the cost of collecting that data.

i built based on info on YC's SAFE document [here](url)

| Data Category | Specific Data Points | Rationale | Cost | Info Amount | Persuasiveness per Unit Cost |
|---------------|----------------------|-----------|------|-------------|------------------------------|
| Future Financing Provisions | - Equity Financing conversion terms<br>- Liquidity Event payout terms<br>- Dissolution Event payout terms<br>- Most Favored Nation clause (if present) | These provisions indicate how the startup plans to handle future funding rounds and exit scenarios. | 💰 | 💡💡💡 | 💡💡💡/💰 |
| Quantitative Startup Metrics | - Purchase Amount (from SAFE)<br>- Post-Money Valuation Cap (from SAFE)<br>- Revenue (last 12 months)<br>- Burn rate<br>- Number of employees<br>- Total addressable market (TAM) size<br>- User/customer growth rate | These metrics provide objective, measurable data points that serve as a baseline for valuation models. The SAFE document directly provides some of these metrics. | 💰 | 💡💡💡 | 💡💡💡/💰 |
| Qualitative Startup Information | - Company stage (inferred from use of SAFE)<br>- Funding strategy (use of SAFE vs. priced round)<br>- Exit strategy options (from Liquidity Event definition)<br>- Intellectual property status (from Company Representations)<br>- Competitive advantage description (inferred from IP rights)<br>- Governance structure (from amendment and voting provisions)<br>- Risk factors (inferred from representations and warranties)<br>- Corporate structure (e.g., state of incorporation) | This qualitative data, much of which can be extracted or inferred from the SAFE, captures nuanced aspects of a startup that influence investor decisions. | 💰 | 💡💡💡 | 💡💡💡/💰 |
| Capital Structure | - Existing Capital Stock composition<br>- Converting Securities details<br>- Liquidity Capitalization breakdown | Understanding the current and potential future capital structure provides insights into the company's financing strategy and potential dilution. | 💰 | 💡💡 | 💡💡/💰 |
| Legal and Regulatory Context | - Governing law jurisdiction (from miscellaneous section)<br>- SEC compliance status (inferred from securities law references)<br>- Tax treatment of SAFE (from section 5g)<br>- Transferability restrictions (from section 5d) | The legal and regulatory context can impact the startup's operations and future funding options. | 💰 | 💡💡 | 💡💡/💰 |
| Founders and Team Information | - Founder names and titles (from signature page)<br>- Board structure (inferred from voting rights and amendment provisions)<br>- Option pool size (from Unissued Option Pool definition)<br>- Promised Options (from definitions) | Information about the team and its structure provides insights into the startup's human capital and governance. | 💰💰 | 💡💡💡 | 💡💡/💰💰 |
| Investor Information | - Investor name and type (from signature page and representations)<br>- Investor rights (e.g., information rights, pro-rata rights if mentioned)<br>- Investor accreditation status (from Investor Representations)<br>- Previous investors (if mentioned in capitalization table) | Understanding the investors involved can provide context about the startup's network and perceived potential. | 💰💰 | 💡💡 | 💡/💰 |
| Market and Industry Context | - Industry sector (if specified in company description)<br>- Comparable company valuations<br>- Recent exits in the sector<br>- Regulatory environment specific to the company's industry | This data provides context for the valuations and helps account for sector-specific trends. | 💰💰💰 | 💡💡 | 💡/💰💰 |
| Post-Investment Performance Tracking | - Milestone achievements post-SAFE issuance<br>- Follow-on funding success<br>- Product/feature launches<br>- Key hires made<br>- Changes in metrics (revenue, users, etc.) since SAFE issuance | While not directly from the SAFE, tracking these points helps validate the model by comparing predicted outcomes with actual performance. | 💰💰💰 | 💡💡 | 💡/💰💰 |



---

## Reply from hyunjimoon on 2024-09-30T14:48:43Z

### info on SAFE 
current practice is post money safe with valuation cap 🧢 without discount according to [here](https://www.wyrick.com/news-insights/safe-financing-a-deep-dive-on-the-evolution-of-the-safe)

I think SAFE which started from paul graham's spirit of [high resolution funding](https://www.paulgraham.com/hiresfund.html), increasing the optimization dimension based on conversational inference is a good place to start.

> Events
	(a)	Equity Financing. If there is an Equity Financing before the termination of this Safe, on the initial closing of such Equity Financing, this Safe will automatically convert into the greater of: (1) the number of shares of Standard Preferred Stock equal to the Purchase Amount divided by the lowest price per share of the Standard Preferred Stock; or (2) the number of shares of Safe Preferred Stock equal to the Purchase Amount divided by the Safe Price.   
	In connection with the automatic conversion of this Safe into shares of Standard Preferred Stock or Safe Preferred Stock, the Investor will execute and deliver to the Company all of the transaction documents related to the Equity Financing; provided, that such documents (i) are the same documents to be entered into with the purchasers of Standard Preferred Stock, with appropriate variations for the Safe Preferred Stock if applicable, and (ii) have customary exceptions to any drag-along applicable to the Investor, including (without limitation) limited representations, warranties, liability and indemnification obligations for the Investor.
	(b)	Liquidity Event.  If there is a Liquidity Event before the termination of this Safe, the Investor will automatically be entitled (subject to the liquidation priority set forth in Section 1(d) below) to receive a portion of Proceeds, due and payable to the Investor immediately prior to, or concurrent with, the consummation of such Liquidity Event, equal to the greater of (i) the Purchase Amount (the “Cash-Out Amount”) or (ii) the amount payable on the number of shares of Common Stock equal to the Purchase Amount divided by the Liquidity Price (the “Conversion Amount”).  If any of the Company’s securityholders are given a choice as to the form and amount of Proceeds to be received in a Liquidity Event, the Investor will be given the same choice, provided that the Investor may not choose to receive a form of consideration that the Investor would be ineligible to receive as a result of the Investor’s failure to satisfy any requirement or limitation generally applicable to the Company’s securityholders, or under any applicable laws.
	Notwithstanding the foregoing, in connection with a Change of Control intended to qualify as a tax-free reorganization, the Company may reduce the cash portion of Proceeds payable to the Investor by the amount determined by its board of directors in good faith for such Change of Control to qualify as a tax-free reorganization for U.S. federal income tax purposes, provided that such reduction (A) does not reduce the total Proceeds payable to such Investor and (B) is applied in the same manner and on a pro rata basis to all securityholders who have equal priority to the Investor under Section 1(d).
	(c)	Dissolution Event. If there is a Dissolution Event before the termination of this Safe, the Investor will automatically be entitled (subject to the liquidation priority set forth in Section 1(d) below) to receive a portion of Proceeds equal to the Cash-Out Amount, due and payable to the Investor immediately prior to the consummation of the Dissolution Event. 

recommended video: 
- https://youtu.be/Dk6JNTDec9I?si=WCi9Z-e1rKokVh42
- https://youtu.be/KLz5CY3jOEo?si=T_262726ycc5lXD3

---

### Reply from hyunjimoon on 2024-09-30T15:13:53Z

![image](https://github.com/user-attachments/assets/ddb94753-6287-4fba-ad2d-283801fd84a9)

---

## Reply from hyunjimoon on 2024-10-06T00:16:42Z

after getting jeff's input, will continue with [getting vikash's input for CIVA baseline models cld](https://claude.ai/chat/de613f47-1251-486f-9b41-c0a0d52bf8a4) to ask vikash for his input

---

## Reply from hyunjimoon on 2024-10-08T02:23:58Z

using [Startup Valuation Model with jeff cld](https://claude.ai/chat/1861dbc1-0b53-45fc-8eda-d01ff554bb14) 
```{stan}
data {
  int<lower=0> N_startups;  // Number of startups
  int<lower=0> N_timepoints;  // Number of time points
  int<lower=0> N_stages;  // Number of funding stages (e.g., 5 for Seed, A, B, C, D)
  int<lower=0> N_criteria;  // Number of decision criteria

  // Startup characteristics
  vector[N_startups] founder_experience;
  int<lower=1, upper=5> industry[N_startups];

  // Time-varying covariates
  int<lower=1, upper=N_stages> stage[N_startups, N_timepoints];
  vector[N_startups * N_timepoints] revenue;
  vector[N_startups * N_timepoints] employees;
  vector[N_startups * N_timepoints] term_sheet_sentiment;
  vector[N_startups * N_timepoints] liquidity_event_protection;

  // Observed log valuations
  vector[N_startups * N_timepoints] log_valuation;

  // Decision criteria importance (from discrete choice experiments)
  matrix[N_criteria, N_stages] criteria_importance;
}

parameters {
  // Global parameters
  vector[N_criteria] beta_global;
  real<lower=0> sigma_global;

  // Stage-specific parameters
  matrix[N_criteria, N_stages] beta_stage;
  vector<lower=0>[N_stages] sigma_stage;

  // Startup-specific parameters
  matrix[N_criteria, N_startups] beta_startup;
  vector<lower=0>[N_startups] sigma_startup;

  // Industry effects
  vector[5] industry_effect;

  // Time trend
  real time_trend;

  // Uncertainty reduction parameter
  real<lower=0, upper=1> uncertainty_reduction;
}

transformed parameters {
  vector[N_startups * N_timepoints] mu;
  
  for (i in 1:N_startups) {
    for (t in 1:N_timepoints) {
      int idx = (i-1) * N_timepoints + t;
      int current_stage = stage[i, t];
      
      mu[idx] = 0;
      
      // Global effects
      mu[idx] += beta_global[1] * founder_experience[i];
      mu[idx] += beta_global[2] * revenue[idx];
      mu[idx] += beta_global[3] * employees[idx];
      mu[idx] += beta_global[4] * term_sheet_sentiment[idx];
      mu[idx] += beta_global[5] * liquidity_event_protection[idx];
      
      // Stage-specific effects
      for (c in 1:N_criteria) {
        mu[idx] += beta_stage[c, current_stage] * criteria_importance[c, current_stage];
      }
      
      // Startup-specific effects
      for (c in 1:N_criteria) {
        mu[idx] += beta_startup[c, i] * criteria_importance[c, current_stage];
      }
      
      // Industry effect
      mu[idx] += industry_effect[industry[i]];
      
      // Time trend
      mu[idx] += time_trend * (t - 1);
    }
  }
}

model {
  // Priors
  beta_global ~ normal(0, 5);
  sigma_global ~ cauchy(0, 2.5);
  
  for (s in 1:N_stages) {
    beta_stage[:, s] ~ normal(0, 1);
    sigma_stage[s] ~ cauchy(0, 2.5);
  }
  
  for (i in 1:N_startups) {
    beta_startup[:, i] ~ normal(0, 1);
    sigma_startup[i] ~ cauchy(0, 2.5);
  }
  
  industry_effect ~ normal(0, 1);
  time_trend ~ normal(0, 0.1);
  uncertainty_reduction ~ beta(2, 2);

  // Likelihood
  for (i in 1:N_startups) {
    for (t in 1:N_timepoints) {
      int idx = (i-1) * N_timepoints + t;
      real sigma_total = sigma_global + sigma_stage[stage[i, t]] + sigma_startup[i];
      sigma_total *= (1 - uncertainty_reduction * (stage[i, t] - 1) / (N_stages - 1));
      log_valuation[idx] ~ normal(mu[idx], sigma_total);
    }
  }
}

generated quantities {
  vector[N_startups * N_timepoints] log_valuation_pred;
  
  for (i in 1:N_startups) {
    for (t in 1:N_timepoints) {
      int idx = (i-1) * N_timepoints + t;
      real sigma_total = sigma_global + sigma_stage[stage[i, t]] + sigma_startup[i];
      sigma_total *= (1 - uncertainty_reduction * (stage[i, t] - 1) / (N_stages - 1));
      log_valuation_pred[idx] = normal_rng(mu[idx], sigma_total);
    }
  }
}
```

| Parameter               | Explanation                                                                                                                                                             |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `beta_stage`            | Captures how the effects of different decision criteria change across funding stages (Seed, Series A, B, C, D). Critical for understanding evolving valuation dynamics. |
| `criteria_importance`   | Input matrix reflecting the importance of different factors at each stage. Directly interacts with beta_stage to determine stage-specific effects on valuation.         |
| `uncertainty_reduction` | Quantifies how the variance in valuations decreases in later stages. Key for understanding risk profiles across different investment stages.                            |
| `beta_startup`          | Captures startup-specific effects, accounting for unique characteristics of each company. Explains consistent over- or under-performance relative to peers.             |
| `industry_effect`       | Accounts for systematic differences in valuations across industries. Important for benchmarking and comparative analysis across sectors.                                |


 `liquidity_event_protection`?, `founder_experience` and `revenue` are input data, while `beta_global` and `sigma_startup` are estimated by the model

| Parameter | Definition |
|-----------|------------|
| `beta_global` | Global effects of various factors on valuation across all startups and stages |
| `sigma_global` | Global variance in valuations |
| `beta_stage` | Stage-specific effects of decision criteria on valuation |
| `sigma_stage` | Stage-specific variance in valuations |
| `beta_startup` | Startup-specific effects, capturing the unique characteristics of each startup |
| `sigma_startup` | Startup-specific variance in valuations |
| `industry_effect` | Effect of different industries on startup valuation |
| `time_trend` | Overall trend in valuations over time |
| `uncertainty_reduction` | Parameter capturing how uncertainty in valuations decreases in later stages |
| `founder_experience` | Measure of the founding team's prior experience |
| `industry` | Categorical variable indicating the industry of each startup |
| `stage` | Current funding stage of the startup (e.g., Seed, Series A, B, C, D) |
| `revenue` | Revenue of the startup at each time point |
| `employees` | Number of employees in the startup at each time point |
| `term_sheet_sentiment` | Measure of the favorability of the term sheet |
| `liquidity_event_protection` | Measure of protections against liquidity events in the funding agreement |
| `criteria_importance` | Matrix capturing the importance of different decision criteria at each funding stage |
| `mu` | Predicted log valuation for each startup at each time point |
| `log_valuation` | Observed log valuation for each startup at each time point |
| `log_valuation_pred` | Predicted log valuation for model checking and future predictions |


---

[Discussion link](https://github.com/Data4DM/BayesSD/discussions/253)