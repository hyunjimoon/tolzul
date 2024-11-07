a.k.a. Rational Meaning Construction in Venture Investment Decisions: A Hierarchical Bayesian Approach
#### abstract
We examine how venture capital investors construct meaning from observable startup characteristics through lay theories that guide their investment decisions. While prior research demonstrates that investors heavily weight management teams and business models in their evaluations, we lack systematic understanding of how different types of investors translate observable features into beliefs about unobservable venture qualities. We propose a hierarchical Bayesian framework that formalizes this meaning construction process, capturing how investors with different expertise and focus areas form distinct perceptual mappings.

Our framework models two key perceptual dimensions that emerge from investors' lay theories: beliefs about business model validity and team execution capability. Using a novel experimental design that combines pick-any-J methods with large language models, we elicit these belief structures from prototypical investor archetypes (e.g., early-stage software VCs, growth-stage investors). The hierarchical structure allows us to identify both individual-level heterogeneity in how investors evaluate startups and population-level patterns in attribute-to-perception mappings, while the LLM augmentation enables systematic exploration of investor responses across a broad range of startup profiles.

The results reveal how rational meaning construction processes can lead to systematically different valuations of identical startups across investor types. We find that investors' domain expertise and investment stage create distinct lay theories about which observable characteristics signal strong execution capability or business model validity. These heterogeneous perceptual mappings help explain several puzzling phenomena in entrepreneurial finance, including persistent valuation disparities and apparent term sheet inefficiencies (todo). Our findings advance the theoretical understanding of meaning construction in high-stakes financial decisions while providing practical guidance for both entrepreneurs and investors in early-stage negotiations.

#### 🗄️table of contents

| Section                                                   | 🔐 Lock and Key                                                                                     | 🧱 Brick                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 🔑 Our Key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[#1. Theoretical Foundation\|1. Theoretical Foundation]] | How do investors form lay theories about unobservable startup qualities?                            | [[📜Gompers20_💰vc_dm]] shows key VC dimensions to model:<br>- Management assessment (95% important)<br>- Business model (83% important)<br>- Product/technology (74% important)<br>- Market (68% important)<br><br>[[📜Kaplan09_🐎jockey_or_horse]] validates importance of observable vs unobservable attributes:<br>- Only 1 of 50 firms changed core business idea<br>- Management turnover very common (only 44% of CEOs remained)<br>- Business idea/model ("horse") more stable than management ("jockey")<br><br>[[📜Agrawal21_ebl_choice]] explains hierarchical uncertainties: beliefs about business model validity (quality of idea) and team execution capability | Framework for modeling investor inference:<br>- Observable terms → perceptual dimensions<br>- Core business (observable) more stable than management (phantom attributes)<br><br>Investor lay theories can be modeled as phantom attributes:<br>- Observable features → perceptual dimensions<br>- Heterogeneous across investor types<br><br>[[#🧠investor's perceptual attributes on founder and business model\|🧠investor's perceptual attributes on founder and business model]]                                                                                        |
| [[#2. Model\|2. Model]]                                   | How to adapt phantom attributes model from consumer choice to venture investment?                   | [[📜Bell22_👻phantom_att]] provides <br>1. foundational framework<br>- When information is incomplete, decision makers infer missing attributes<br>- These "phantom attributes" expand rather than collapse the attribute space<br>- Shows how identical observable attributes map to different perceptions<br><br>2. methodology<br>- Pick-any-J experimental design<br>- Hierarchical Bayesian modeling<br><br>[[📜Kaplan09_🐎jockey_or_horse]] provides validation approach:<br>- Track observable business elements over time<br>- Document management turnover<br>- ❓Measure value creation                                                                               | Model adaptations needed:<br>- Map pick-any-J design to VC context<br>- Include key VC evaluation dimensions<br>- Account for value creation dynamics<br><br>Model adaptations needed:<br>- Modify perceptual dimensions<br>- Adjust experimental design<br>- Account for equilibrium dynamics<br><br>input of [[#🗼hierarchical Bayesian model\|🗼hierarchical Bayesian model]],  [[#📝example data\|📝example data]] using  [[#🔡LLM\|🔡LLM]] and [[#🔬pick-any-J experimental design\|🔬pick-any-J experimental design]]<br><br>![[Pasted image 20241106011155.png\|300]] |
| [[#3. Vision\|3. Vision]]                                 | What is the meaning of this research in <br>1)  research contribution  <br>2) practical application | [[📜Mackey_bayes_mng]]'s essential heterogeneity is captured<br><br>founder can have more informative population level investor's utility                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### 1. Theoretical Foundation

#### 🧠investor's perceptual attributes on founder and business model

| founder          | Description                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| Ability          | They're self-aware, understand their strengths and weaknesses, and self-curious.                |
| Attitude         | They'll do whatever it takes, envision success, and energize others.                            |
| Aptitude         | They're a fast learner, adaptable, and can handle the unknown.                                  |
| Athlete          | They're a team player, are willing to do the work, and have the grit to get through challenges. |
| Attractor        | They can attract the best talent, customers, investors, advisors—today and in the future.       |
| Authentic        | The dots connect between their past and present motivations and aspirations.                    |
| Ability (Domain) | They are entrepreneurial, visionary, and have proven, unique domain expertise.                  |

| business model            | Opportunity Positives                                                              | Rating  | Opportunity Detractors                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------- |
| Stage/Structure           | Early stage, large ownership, large potential MoIC, value added syndicate          | Yes\|No | Later stage, small ownership, small potential MoIC, weak syndicate                        |
| Team                      | Entrepreneurial, visionary, proven, unique domain expertise, complete              | A\|B\|C | Not entrepreneurial, small thinkers, unproven, limited expertise, incomplete              |
| Market Opportunity        | Massive revenue potential ($B), rapidly growing market, clear timing drivers       | A\|B\|C | Small revenue potential ($M), decaying market, timing is early/late or unclear            |
| Product Value Proposition | Solving acute pain, easy to adopt, clearly attributable ROI, innovative/disruptive | A\|B\|C | Unproven pain, hard to adopt, hard to attribute ROI, incremental feature/product          |
| Competition               | Whitespace, defensible, clear basis to disrupt, define, and/or lead category       | A\|B\|C | Agile and well-capitalized big players with enduring advantage or ecosystem               |
| Business Model            | Scalable, sustainable, aligned value transfer, differentiated, clear               | A\|B\|C | Limited scalability, not sustainable, unaligned value transfer, undifferentiated, unclear |
| Milestones - Risk/Reward  | Well articulated, value-creating, de-risking, realistic, achievable, measurable    | A\|B\|C | Poorly articulated, does not create value, unrealistic, not achievable, unmeasurable      |
| Investment Profile        | Capital efficient, proportionate time investment to drive desired outcome          | A\|B\|C | Capital inefficient business, large time investment to drive desired outcome              |
| ESG Factors               | Favorable environmental impact, diverse team, pass negative ESG screen             | A\|B\|C | Harmful to environment, governance risk, misalignment with our core principles            |
| Conviction                | Current investment likely to return fund, would put your own mother's $ behind it  | A\|B\|C | Too risky, unlikely to move the needle, would not put your own mother's $ behind it       |

### 2. Model
#### 🔬pick-any-J experimental design
Show investors: "Series A startup with:
- Technical founder, 2 prior exits
- $2M ARR, growing 15% month-over-month
- Patent-pending ML technology"

Ask them to check ALL that apply:
□ Strong execution capability 
□ Good market understanding
□ Ability to attract talent
□ Product likely to achieve PMF
□ Will require significant operational support
□ Likely to have successful exit

#### 🔡LLM

1. Generate many such startup profiles systematically varying characteristics
2. Create prototypical investor personas (e.g., early-stage software VC, growth-stage fintech VC)
3. Help analyze patterns in how different investor types map observable features to inferred qualities

Example Profile Variations:

Profile A: Technical Focus
- Technical co-founders (both with PhDs)
- Early product, pre-revenue
- Strong IP portfolio
- Deep tech market

Profile B: Commercial Focus
- Mixed founding team (1 technical, 1 business)
- $1M ARR, 20% MoM growth
- SaaS product
- Enterprise market

This design allows us to:
1. Isolate effects of specific characteristics
2. Test interaction effects
3. Measure preference heterogeneity across investor types

#### 📝example data

| profile_id | investor_type_id | 👁️observable_features<br>(tech_founder, prior_exits, arr_mm, revenue_growth, patent) | responses<br>(response_execution, response_market, response_talent, response_pmf, response_operations, response_exit) |
| ---------- | ---------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 1          | 1                | [1, 2, 2.0, 0.15, 1]                                                                  | [1, 0, 1, 0, 1, 1]                                                                                                    |
| 2          | 2                | [1, 2, 2.0, 0.15, 1]                                                                  | [1, 1, 1, 0, 0, 0]                                                                                                    |
| 3          | 1                | [0, 0, 0.5, 0.25, 0]                                                                  | [0, 1, 0, 1, 1, 0]                                                                                                    |
| 4          | 2                | [0, 0, 0.5, 0.25, 0]                                                                  | [0, 1, 0, 1, 1, 0]                                                                                                    |
| 5          | 1                | [1, 0, 1.0, 0.20, 1]                                                                  | [1, 0, 1, 1, 0, 1]                                                                                                    |

#### 🗼hierarchical Bayesian model
Our model captures three levels of heterogeneity:

1. Investor Type Level
- Early-stage vs. growth-stage preferences
- Domain expertise effects (e.g., software vs. hardware)
- Investment thesis variation

2. Individual Level
- Personal experience effects
- Prior investment outcomes
- Domain-specific knowledge

3. Population Level
- Common patterns across all investors
- Industry-wide evaluation norms
- Shared mental models of success

```python
data {
  int<lower=0> N;  // Number of profiles (5 in our example)
  int<lower=0> K;  // Number of observable features (5: tech_founder, prior_exits, arr_mm, revenue_growth, patent)
  int<lower=0> R;  // Number of responses (6: execution, market, talent, pmf, operations, exit)
  int<lower=0> T;  // Number of investor types (2: early_sw_vc=1, growth_fin_vc=2)
  
  matrix[N, K] X;  // Observable features matrix [N×K]
                   // Each row contains: [tech_founder, prior_exits, arr_mm, revenue_growth, patent]
  
  int<lower=1,upper=T> investor_type[N];  // Investor type for each profile
                                         // Vector of length N containing 1 or 2
  
  int<lower=0,upper=1> Y[N, R];  // Binary response matrix [N×R]
                                 // Each row contains: [response_execution, response_market, 
                                 //                    response_talent, response_pmf,
                                 //                    response_operations, response_exit]
}

parameters {
  // Population level parameters
  matrix[K, R] W;  // Base mapping from features to responses
  
  // Investor-type specific parameters
  matrix[T, K] type_effect;  // How each type deviates from population
  
  // NEW: Add investor-specific random effects
  matrix[N, R] investor_effect;  // Individual investor deviations
}

model {
  // Hierarchical priors
  to_vector(W) ~ normal(0, 1);  // Population level effects
  to_vector(type_effect) ~ normal(0, 0.5);  // Type-specific deviations
  to_vector(investor_effect) ~ normal(0, 0.25);  // Individual variations
  
  // Likelihood
  for (n in 1:N) {
    for (r in 1:R) {
      real logit_p = 0;
      
      // Base effect from features
      for (k in 1:K) {
        logit_p += X[n,k] * W[k,r];
      }
      
      // Add investor type effect
      logit_p += type_effect[type[n], r];
      
      Y[n,r] ~ bernoulli_logit(logit_p);
    }
  }
}
```
---

### 3. Vision

#### Research Contributions:
1. Theoretical
   - Extends phantom attributes theory to high-stakes financial decisions
   - Formalizes investor lay theory formation
   - Links rational meaning construction to investment decisions

2. Methodological
   - Novel application of pick-any-J design to VC context
   - Integration of LLMs for experimental scale
   - Hierarchical Bayesian framework for investor heterogeneity

#### Practical Applications:
1. For Entrepreneurs
   - Optimize pitch characteristics for different investor types
   - Better understand investor evaluation process
   - More effective term sheet negotiations

2. For Investors
   - Systematic framework for evaluation
   - Understanding of own potential biases
   - Better pattern matching across investments

3. For Market Design
   - More efficient matching mechanisms
   - Better term sheet structures
   - Improved information sharing protocols

---
using [crafting research proposal with jeff cld](https://claude.ai/chat/b99f7a8c-37d4-4568-9983-ccf5ff2b809b)