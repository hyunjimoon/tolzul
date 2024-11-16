a.k.a. Rational Meaning Construction in Venture Investment Decisions: A Hierarchical Bayesian Approach
#### abstract
Early-stage venture investors make decisions with limited information, relying on observable startup characteristics to form expectations about potential success. For example, prior research shows that investors often focus on factors like the management team or business model when assessing a firm’s ability to execute its vision. Little is known, however, about how these observable characteristics map onto the perceptions investors use when evaluating deals or how this mapping varies by investor type. Our research investigates this process, drawing on theories of rational meaning creation and lay theory construction to explain how investors interpret observable signals as indicators of unobservable qualities. We develop a hierarchical Bayesian framework that allows us to empirically study how investors with different expertise and focus areas translate deal characteristics into structured beliefs about a venture’s potential.

Our framework models two key perceptual dimensions that emerge from investors' lay theories: beliefs about the business model validity and the team’s ability to execution (i.e., is the idea viable and can the team make it happen). Using a novel experimental design that combines survey research methods with large language models, we elicit these belief structures from archetypical investors (e.g., early-stage software VCs, growth-stage investors). The hierarchical structure allows us to identify both individual-level heterogeneity in how investors evaluate startups and population-level patterns in attribute-to-perception mappings, while the LLM augmentation enables systematic exploration of investor responses across a broad range of startup profiles.

Our approach reveals how the process of heterogeneous rational meaning construction can lead to systematically different valuations of identical startups. We find that investors' domain expertise and investment stage create distinct lay theories about which observable characteristics signal strong execution capability or business model validity. Taken collectively,  our research can help explain several puzzling phenomena in entrepreneurial finance, including persistent valuation disparities and apparent term sheet inefficiencies (todo). Our findings advance a theoretical understanding of meaning construction in high-stakes financial decisions while providing practical guidance for both entrepreneurs and investors in early-stage negotiations.

#### 🗄️table of contents

| Section                                                                                                                                                                                                                             | 🔐 Lock and Key                                                                                     | 🧱 Brick                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 🔑 Key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[#1. Theoretical Foundation\|1. Theoretical Foundation]]                                                                                                                                                                           | How do investors form lay theories about unobservable startup qualities?                            | [[📜Gompers20_💰vc_dm]] shows key VC dimensions to model:<br>- Management assessment (95% important)<br>- Business model (83% important)<br>- Product/technology (74% important)<br>- Market (68% important)<br><br>[[📜Kaplan09_🐎jockey_or_horse]] validates importance of observable vs unobservable attributes:<br>- Only 1 of 50 firms changed core business idea<br>- Management turnover very common (only 44% of CEOs remained)<br>- Business idea/model ("horse") more stable than management ("jockey")<br><br>[[📜Agrawal21_ebl_choice]] explains hierarchical uncertainties: beliefs about business model validity (quality of idea) and team execution capability | Framework for modeling investor inference:<br>- Observable terms → perceptual dimensions<br>- Core business (observable) more stable than management (phantom attributes)<br><br>Investor lay theories can be modeled as phantom attributes:<br>- Observable features → perceptual dimensions<br>- Heterogeneous across investor types<br><br>[[#🧠investor's perceptual attributes on founder and business model\|🧠investor's perceptual attributes on founder and business model]] |
| [[#2. Model\|2. Model]]<br><br>- [[#2. Model#🔡🦸‍♂️LLM based profile\|🔡🦸‍♂️LLM based profile]]<br>- [[#2. Model#📝example data\|📝example data]]<br>- [[#2. Model#🌲hierarchical Bayesian model\|🌲hierarchical Bayesian model]] | How to adapt phantom attributes model from consumer choice to venture investment?                   | [[📜Bell22_👻phantom_att]] provides <br>1. foundational framework<br>- When information is incomplete, decision makers infer missing attributes<br>- These "phantom attributes" expand rather than collapse the attribute space<br>- Shows how identical observable attributes map to different perceptions<br><br>2. methodology<br>- Pick-any-J experimental design<br>- Hierarchical Bayesian modeling<br><br>[[📜Kaplan09_🐎jockey_or_horse]] provides validation approach:<br>- Track observable business elements over time<br>- Document management turnover<br>- ❓Measure value creation                                                                               | Model adaptations needed:<br>- Map pick-any-J design to VC context<br>- Include key VC evaluation dimensions<br>- Account for value creation dynamics<br><br>Model adaptations needed:<br>- Modify perceptual dimensions<br>- Adjust experimental design<br>- Account for equilibrium dynamics<br><br>input of [[#🗼hierarchical Bayesian model\|🗼hierarchical Bayesian model]],  [[#📝example data\|📝example data]] using <br><br>![[Pasted image 20241106011155.png\|300]]        |
| [[#3. Future direction\|3. Future direction]]                                                                                                                                                                                       | What is the meaning of this research in <br>1)  research contribution  <br>2) practical application | [[📜Mackey_bayes_mng]]'s essential heterogeneity is captured<br><br>founder can have more informative population level investor's utility                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### 1. Theoretical Foundation

Early-stage venture investment decisions present a unique challenge in meaning construction, where investors must translate observable startup characteristics into predictions about unobservable future success. Drawing on Gompers et al. (2020), we identify key dimensions that inform these predictions: management team capabilities (cited by 95% of VCs), business model viability (83%), product/technology strength (74%), and market potential (68%). Kaplan and Strömberg's (2009) horse-vs-jockey analysis provides crucial insight into the relative stability of these dimensions - while business models rarely change (only 2% of cases), management teams frequently turn over (56% of cases), suggesting different roles for observable versus phantom attributes in investor decision-making. We extend this work by applying Agrawal's (2021) hierarchical choice framework to formalize how investors construct meaning from these varying signals, particularly focusing on two key perceptual dimensions: business model validity and team execution capability.

[[🗄️🧠investor's perceptual attributes on founder and business model]]

### 2. Model
Our methodology represents a significant evolution in studying venture capital decision-making by moving beyond archetypal investor categories to investor-specific models. We develop these models using comprehensive public records from five influential early-stage investors - Fred Wilson, Bill Gurley, M.G. Siegler, Naval Ravikant, and Ryan Caldbeck - whose extensive writings and interviews provide rich data about their investment philosophies. Building on [[📜Bell22_👻phantom_att]] phantom attributes framework, we employ a novel experimental design where investors evaluate both concrete characteristics (e.g., "Technical founder with 2 prior exits") and latent perceptual qualities (e.g., "Strong execution capability"). Rather than traditional surveys, we leverage large language models trained on investor-specific content to generate synthetic but representative responses at scale. This approach allows us to trace how objective features map to subjective assessments through both direct and mediated pathways in our hierarchical Bayesian framework.

We investigate how early-stage venture investors construct meaning from observable startup characteristics to form investment decisions. It focuses on two key dimensions:
- How observable characteristics map to perceptual dimensions (beliefs about business model validity and team execution ability)
- How this mapping varies by investor type/expertise 

The research aims to uncover how heterogeneous "rational meaning construction" leads different investors to value identical startups differently based on their unique "lay theories" about which observable characteristics signal strong execution or valid business models.

![[Pasted image 20241106011155.png|300]]

| Arrow Type | Description | Role in Model | Implementation |
|-|-|-|-|
| Lay Theory Mapping (Solid) | Observable → Perceptual | Maps concrete characteristics (team composition, technical capabilities) to abstract perceptions (execution capability, market understanding) | - Encoded in β parameters of hierarchical model<br>- Varies by investor characteristics<br>- Primary focus of meaning construction study |
| Utility Formation (Solid) | Perceptual → Decision | Translates perceptions into investment utility/value | - Maps perceptual dimensions to binary invest/don't invest decision<br>- Part of choice model<br>- Could vary by investor type |
| Direct Effects (Dotted) | Observable → Decision | Direct impact of characteristics on decisions beyond perceptual mediation | - Controls for effects not captured by perceptual mapping<br>- Important for model identification<br>- Allows for "ancillary signals" discussed in transcript |


#### 🔡🦸‍♂️LLM based profile

[[🗄️🦸‍♂️profile]] lists five investors with their roles, descriptions, main data source URLs, and how each of the three functions can be learned from their approaches, using [perplexity](https://www.perplexity.ai/search/what-are-some-podcast-where-ne-u8YW1DGdTei24tolkS9okQ)

![[🗄️🦸‍♂️profile]]


for each of them, we'll show invsetor-llms: "Series A startup with: Technical founder, 2 prior exits, $2M ARR, growing 15% month-over-month, Patent-pending ML technology" and ask to check ALL that apply: □ Strong execution capability, □ Good market understanding,  □ Ability to attract talent, □ Product likely to achieve PMF, □ Will require significant operational support, □ Likely to have successful exit

#### 📝example data

| profile_id | investor_type_id | 👁️observable_features<br>(tech_founder, prior_exits, arr_mm, revenue_growth, patent) | responses<br>(response_execution, response_market, response_talent, response_pmf, response_operations, response_exit) |
| ---------- | ---------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 1          | 1                | [1, 2, 2.0, 0.15, 1]                                                                  | [1, 0, 1, 0, 1, 1]                                                                                                    |
| 2          | 2                | [1, 2, 2.0, 0.15, 1]                                                                  | [1, 1, 1, 0, 0, 0]                                                                                                    |
| 3          | 1                | [0, 0, 0.5, 0.25, 0]                                                                  | [0, 1, 0, 1, 1, 0]                                                                                                    |
| 4          | 2                | [0, 0, 0.5, 0.25, 0]                                                                  | [0, 1, 0, 1, 1, 0]                                                                                                    |
| 5          | 1                | [1, 0, 1.0, 0.20, 1]                                                                  | [1, 0, 1, 1, 0, 1]                                                                                                    |

#### 🌲hierarchical Bayesian model
The hierarchical Bayesian model formalizes how investors translate observable startup characteristics into investment decisions through both direct and perceptual pathways (perceptual mediates observable and investment decision). At its core, the model captures two key mappings: first, how observable characteristics ($X$) map to perceptual dimensions (Perceptions) through investor-specific coefficients ($\beta$ modified by $\theta$ based on investor characteristics $Z$); and second, how these perceptions combine with direct effects to influence final investment decisions ($Y$) through a utility function. The model's hierarchical structure, discussed extensively in the transcript, allows for three levels of variation: population-level patterns in $\beta$, investor-type-level effects through $\theta$, and individual-level heterogeneity through the correlation structure $\Omega$. The bernoulli_logit likelihood for investment decisions reflects the binary nature of invest/don't invest choices, while the normal and LKJ priors encode reasonable assumptions about parameter distributions. This structure implements the "lay theory mapping" discussed in the transcript, where different investors can construct different meanings from identical startup characteristics.

using [cld](https://claude.ai/chat/e78a0bff-dd08-456c-b83f-89daae9cf8e2)
```python
data {
  int<lower=0> N;              // Number of investment decisions
  int<lower=0> K;              // Number of observable deal characteristics
  int<lower=0> P;              // Number of perceptual dimensions (2: execution + business model)
  int<lower=0> T;              // Number of investor archetypes
  int<lower=0> M;              // Number of investor characteristics
  
  matrix[N, K] X;              // Observable deal characteristics matrix
  matrix[T, M] Z;              // Investor archetype characteristics
  int<lower=1,upper=T> type[N];// Investor type for each decision
  int<lower=0,upper=1> Y[N];   // Investment decision (1=invest, 0=pass)
}

parameters {
  // Perception formation parameters
  matrix[K, P] Beta;           // Mapping from observables to perceptions
  matrix[M, K] Theta;          // How investor characteristics affect mapping
  
  // Investment decision parameters
  vector[P] Alpha;             // Impact of perceptions on investment decision
  real<lower=0> sigma;         // Decision noise
  
  // Hierarchical parameters
  corr_matrix[K] Omega;        // Correlation between characteristic effects
  vector<lower=0>[K] tau;      // Scaling for characteristic effects
}

transformed parameters {
  matrix[N, P] Perceptions;    // Latent perceptual dimensions
  vector[N] InvestmentUtil;    // Investment utility
  
  // Generate perceptions based on characteristics and investor type
  for (n in 1:N) {
    matrix[K, P] BetaType = Beta + (Theta * Z[type[n]])';
    Perceptions[n] = X[n] * BetaType;
  }
  
  // Calculate investment utility
  InvestmentUtil = Perceptions * Alpha;
}

model {
  // Priors
  to_vector(Beta) ~ normal(0, 1);
  to_vector(Theta) ~ normal(0, 0.5);
  Alpha ~ normal(0, 1);
  tau ~ cauchy(0, 2.5);
  Omega ~ lkj_corr(2);
  
  // Investment decision likelihood
  Y ~ bernoulli_logit(InvestmentUtil);
}
```
---

### 3. Future direction

Our research advances the understanding of meaning construction in decision making. Just as [[📜Wong23_word2world]] framework shows how language comprehension requires mapping from natural language to a probabilistic language of thought, our work reveals how investors construct meaning from startup characteristics through a similar probabilistic translation process. by bridging fixed-state and joint-state inference approaches. Drawing from  [[PC1_w2w.pdf]] .'s framework of rational meaning construction, we demonstrate how investors, like language users more broadly, must translate observable characteristics into latent meanings through context-sensitive inference. Below table shows the motivation of rational meaning construction which is to extend from Known/Fixed States to Joint State Inference.

| Aspect                   | Known/Fixed States                                           | Joint State Inference                                                   |
| ------------------------ | ------------------------------------------------------------ | ----------------------------------------------------------------------- |
| Meaning Function         | Direct mapping from language to program                      | Context-sensitive, handles ambiguity                                    |
| Inference Function       | Operates on fixed state space                                | Reasons about multiple possible states                                  |
| Computational Complexity | Lower - parameters are known                                 | Higher - must infer latent variables                                    |
| Example                  | "John and Mary won tug-of-war" -> direct strength comparison | "Alex brought his bike" -> infer goals, preferences, and likely actions |
| State Space              | Pre-defined, explicit                                        | Dynamic, implicit                                                       |
| Context Dependency       | Low                                                          | High                                                                    |

The key contribution of our work lies in implementing this theoretical insight through a concrete computational architecture that combines:

- A meaning function that maps observable startup features to latent perceptual dimensions, analogous to how Wong et al.'s framework translates natural language to program code
- An inference function that reasons about multiple possible states and handles ambiguity, similar to their probabilistic programming approach
- A hierarchical Bayesian framework that captures investor-specific variations in meaning construction, reflecting their notion of resource-rational translation

This unified framework yields practical benefits for the venture ecosystem:

- Entrepreneurs can better understand how different investors construct meaning from pitch characteristics
- Investors gain systematic tools for examining their own meaning construction patterns and potential biases
- Market designers can develop more efficient matching mechanisms based on understanding how meaning is constructed differently across investor types

By demonstrating how rational meaning construction principles apply to investment decisions, our work provides a stepping stone toward more general theories of how humans translate observable signals into meaningful beliefs and decisions under uncertainty.

This research advances both theoretical understanding and practical applications in venture capital decision-making. Theoretically, we extend phantom attributes theory into high-stakes financial decisions while providing a computational framework for studying rational meaning construction in investment contexts. Our methodology demonstrates how large language models can augment traditional experimental designs to study individual-level heterogeneity at unprecedented scale. Practically, our findings offer actionable insights for multiple stakeholders: entrepreneurs can optimize their pitches based on investor-specific meaning construction patterns, investors can better understand their own decision-making biases, and market designers can develop more efficient matching mechanisms between startups and investors. Most importantly, by revealing how different investors construct meaning from identical startup characteristics, we help explain persistent valuation disparities and apparent inefficiencies in early-stage financing markets.

---
using [crafting research proposal with jeff cld](https://claude.ai/chat/b99f7a8c-37d4-4568-9983-ccf5ff2b809b),  [mapping startup characteristics to investor perceptions cld](https://claude.ai/chat/ab5711fb-6049-46c5-909f-66ffbf480f47)
