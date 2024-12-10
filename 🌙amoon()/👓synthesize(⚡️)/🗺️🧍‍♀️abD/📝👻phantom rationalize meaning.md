a.k.a. Rational Meaning Construction in Venture Investment Decisions: A Hierarchical Bayesian Approach
marginnote3app://note/5478BD5E-6BCE-4D4B-8982-CF9B847960B3
- [[👻_profile_coding.png]]
- 🪵([[🗺️abD.agent's belief and desire to equity valuation]] is in [[🪵(🗺️)]] in the format of one mural per meeting.

| Component<br>[🔄🌏👻UTB_W2W_phantom cld](https://claude.ai/chat/f1a93000-f58a-4842-a38e-5c6b7a3b48ed) | [[🔄UTB_understanding-theory-body]]      | Definition                                       | BYD vs Hotel                                                               | 🧠W2W Framework                        | 👻Phantom Framework              |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------- | -------------------------------------- | -------------------------------- |
| **Stocks**                                                                                            |                                          |                                                  |                                                                            |                                        |                                  |
| 👁️Quality of Perceptive Understanding                                                                | Understanding through testing & feedback | Current level of insight, decays via 🍃rejecting | Battery safety understanding<br><br>Hotel brand-price perception           | Statistical pattern recognition        | Observable attribute perception  |
| 🧠Quality of Integrative Theory                                                                       | Theory development via testing           | Validated theories, decays via 🗑️retiring       | Blade battery design theory<br><br>Price-quality relationship theory       | Probabilistic program construction     | Latent attribute mapping         |
| 💪Quality of Implemented Body                                                                         | Implementation & execution               | Actual implementations                           | Production system<br><br>Hotel bookings                                    | World model inference                  | Action/choice outcomes           |
|                                                                                                       |                                          |                                                  |                                                                            |                                        |                                  |
| **Flow Functions**                                                                                    |                                          |                                                  |                                                                            |                                        |                                  |
| 👓testing                                                                                             | Maps understanding → theory (1/α2)       | 🧠Theory/time_to_test                            | Safety validation (0.5 week)<br><br>Brand-price testing (0.5 week)         | Meaning function (language → programs) | O2P matrix mapping               |
| 👆implementing                                                                                        | Maps theory → commitments                | 💪Body/time_to_implement                         | Factory setup (5x test time)<br><br>Booking process (same as test time)    | Inference function (program execution) | P2A matrix mapping               |
| 🔄receiving feedback                                                                                  | Updates understanding (1/α1)             | Commitment/time_to_feedback                      | Market response (2 weeks)<br><br>Guest reviews (2 weeks)                   | Program-world evaluation               | Choice-based learning            |
|                                                                                                       |                                          |                                                  |                                                                            |                                        |                                  |
| **Decay Rates**                                                                                       |                                          |                                                  |                                                                            |                                        |                                  |
| 🍃rejecting (μ1)                                                                                      |                                          | 0.5/week (understanding decay)                   | Invalidated safety assumptions<br><br>Outdated brand perceptions           |                                        |                                  |
| 🗑️retiring (μ2)                                                                                      |                                          | 0.1/week (theory decay)                          | Obsolete manufacturing methods<br><br>Outdated pricing models              |                                        |                                  |
| **Feedback Loops**                                                                                    |                                          |                                                  |                                                                            |                                        |                                  |
| R1: Learning                                                                                          | 👁️→🧠→🤜→👁️ (learns)                   | Understanding → Theory → Body                    | Safety focus reveals cost benefits<br><br>Price signals reveal quality     | Neural → symbolic → neural             | Observable → perceptual → action |
| R2: Refining                                                                                          | 👓→🧠→👆 (refines)                       | Theory improvement through testing               | Manufacturing process optimization<br><br>Brand-price model refinement     | Language → program → inference         | Feature → attribute → choice     |
| B1: Rejecting                                                                                         | Decays outdated understanding            | Understanding fitness decay                      | Invalid safety assumptions drop<br><br>Bad perceptions fade                | Invalid program rejection              | Mismatched perception pruning    |
| B2: Retiring                                                                                          | Retires obsolete theories                | Theory effectiveness decay                       | Old manufacturing methods retire<br><br>Outdated pricing models fade       | Obsolete inference removal             | Invalid attribute decay          |
|                                                                                                       |                                          |                                                  |                                                                            |                                        |                                  |
| **Time Ratios**                                                                                       |                                          |                                                  |                                                                            |                                        |                                  |
| Test:Implement                                                                                        |                                          | 1:10 for BYD, 1:1 for Hotels                     | Long factory setup vs quick tests<br><br>Quick booking vs quick validation |                                        |                                  |
| Reject:Retire                                                                                         |                                          | 5:1 (faster to reject understanding)             | Fast safety validation failure<br><br>Quick brand perception updates       |                                        |                                  |

Key Differences:
- BYD has high implementation:test ratio (10:1) due to factory setup; BYD: Long implementation time (factory setup) vs. quick testing → parallel development optimal
- Hotels have low implementation:test ratio (1:1) due to quick booking; Hotels: Quick implementation (booking) vs. slower testing → sequential adaptation works well
- Both share same feedback time (2 weeks) but different decay implications

#### abstract
Early-stage venture investors make decisions with limited information, relying on observable startup characteristics to form expectations about potential success. For example, prior research shows that investors often focus on factors like the management team or business model when assessing a firm’s ability to execute its vision. Little is known, however, about how these observable characteristics map onto the perceptions investors use when evaluating deals or how this mapping varies by investor type. Our research investigates this process, drawing on theories of rational meaning creation and lay theory construction to explain how investors interpret observable signals as indicators of unobservable qualities. We develop a hierarchical Bayesian framework that allows us to empirically study how investors with different expertise and focus areas translate deal characteristics into structured beliefs about a venture’s potential.

Our framework models two key perceptual dimensions that emerge from investors' lay theories: beliefs about the business model validity and the team’s ability to execution (i.e., is the idea viable and can the team make it happen). Using a novel experimental design that combines survey research methods with large language models, we elicit these belief structures from archetypical investors (e.g., early-stage software VCs, growth-stage investors). The hierarchical structure allows us to identify both individual-level heterogeneity in how investors evaluate startups and population-level patterns in attribute-to-perception mappings, while the LLM augmentation enables systematic exploration of investor responses across a broad range of startup profiles.

Our approach reveals how the process of heterogeneous rational meaning construction can lead to systematically different valuations of identical startups. We find that investors' domain expertise and investment stage create distinct lay theories about which observable characteristics signal strong execution capability or business model validity. Taken collectively,  our research can help explain several puzzling phenomena in entrepreneurial finance, including persistent valuation disparities and apparent term sheet inefficiencies (todo). Our findings advance a theoretical understanding of meaning construction in high-stakes financial decisions while providing practical guidance for both entrepreneurs and investors in early-stage negotiations.

#### 🗄️table of contents
![[🗄️👻]]
### 1. Theoretical Foundation

Early-stage venture investment decisions present a unique challenge in meaning construction, where investors must translate observable startup characteristics into predictions about unobservable future success. Drawing on Gompers et al. (2020), we identify key dimensions that inform these predictions: management team capabilities (cited by 95% of VCs), business model viability (83%), product/technology strength (74%), and market potential (68%). Kaplan and Strömberg's (2009) horse-vs-jockey analysis provides crucial insight into the relative stability of these dimensions - while business models rarely change (only 2% of cases), management teams frequently turn over (56% of cases), suggesting different roles for observable versus phantom attributes in investor decision-making. We extend this work by applying Agrawal's (2021) hierarchical choice framework to formalize how investors construct meaning from these varying signals, particularly focusing on two key perceptual dimensions: business model validity and team execution capability.

[[🗄️🧠investor's perceptual attributes on founder and business model]]

### 2. Model
Our methodology represents a significant evolution in studying venture capital decision-making by moving beyond archetypal investor categories to investor-specific models. We develop these models using comprehensive public records from five influential early-stage investors - Fred Wilson, Bill Gurley, M.G. Siegler, Naval Ravikant, and Ryan Caldbeck - whose extensive writings and interviews provide rich data about their investment philosophies. Building on [[📜Bell22_👻phantom_att]] phantom attributes framework, we employ a novel experimental design where investors evaluate both concrete characteristics (e.g., "Technical founder with 2 prior exits") and latent perceptual qualities (e.g., "Strong execution capability"). Rather than traditional surveys, we leverage large language models trained on investor-specific content to generate synthetic but representative responses at scale. This approach allows us to trace how objective features map to subjective assessments through both direct and mediated pathways in our hierarchical Bayesian framework.

We investigate how early-stage venture investors construct meaning from observable startup characteristics to form investment decisions. It focuses on two key dimensions:
- How observable characteristics map to perceptual dimensions (beliefs about business model validity and team execution ability)
- How this mapping varies by investor type/expertise 

The research aims to uncover how heterogeneous "rational meaning construction" leads different investors to value identical startups differently based on their unique "lay theories" about which observable characteristics signal strong execution or valid business models.

![[Pasted image 20241106011155.png|600]]

| Arrow Type                   | Description                  | Role in Model                                                                                                                                 | Implementation                                                                                                                                                |
| ---------------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 👓Lay Theory Mapping (Solid) | 👁️Observable → 🧠Perceptual | Maps concrete characteristics (team composition, technical capabilities) to abstract perceptions (execution capability, market understanding) | - Encoded in β parameters of hierarchical model<br>- Varies by investor characteristics<br>- Primary focus of meaning construction study                      |
| 🫀Utility Formation (Solid)  | 🧠Perceptual → 🤜Decision    | Translates perceptions into investment utility/value                                                                                          | - Maps perceptual dimensions to binary invest/don't invest decision<br>- Part of choice model<br>- Could vary by investor type                                |
| Direct Effects (Dotted)      | Observable → Decision        | Direct impact of characteristics on decisions beyond perceptual mediation                                                                     | - Controls for effects not captured by perceptual mapping<br>- Important for model identification<br>- Allows for "ancillary signals" discussed in transcript |


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
|            |                  | (discretization)                                                                      |                                                                                                                       |

#### 🌲hierarchical Bayesian model
The hierarchical Bayesian model formalizes how investors translate observable startup characteristics into investment decisions through both direct and perceptual pathways (perceptual mediates observable and investment decision). At its core, the model captures two key mappings: first, how observable characteristics ($X$) map to perceptual dimensions (Perceptions) through investor-specific coefficients ($\beta$ modified by $\theta$ based on investor characteristics $Z$); and second, how these perceptions combine with direct effects to influence final investment decisions ($Y$) through a utility function. The model's hierarchical structure, discussed extensively in the transcript, allows for three levels of variation: population-level patterns in $\beta$, investor-type-level effects through $\theta$, and individual-level heterogeneity through the correlation structure $\Omega$. The bernoulli_logit likelihood for investment decisions reflects the binary nature of invest/don't invest choices, while the normal and LKJ priors encode reasonable assumptions about parameter distributions. This structure implements the "lay theory mapping" discussed in the transcript, where different investors can construct different meanings from identical startup characteristics.

full factorial (founding team)design (individual models); no imputation needed. model flow through perception, 
using [cld](https://claude.ai/chat/e78a0bff-dd08-456c-b83f-89daae9cf8e2)
```python
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

| System Component                       | 🔄UTC Framework                          | 🧠W2W Framework                        | 👻Phantom Framework              |
| -------------------------------------- | ---------------------------------------- | -------------------------------------- | -------------------------------- |
| 👁️Quality of Perceptive Understanding | Understanding through testing & feedback | Statistical pattern recognition        | Observable attribute perception  |
| 🧠Quality of Programmatic Theory       | Theory development via testing           | Probabilistic program construction     | Latent attribute mapping         |
| 🤜Quality of Strategic Commitments     | Implementation & execution               | World model inference                  | Action/choice outcomes           |
|                                        |                                          |                                        |                                  |
| Key Functions                          |                                          |                                        |                                  |
| 👓Testing                              | Maps understanding → theory (1/α2)       | Meaning function (language → programs) | O2P matrix mapping               |
| 👆Implementing                         | Maps theory → commitments                | Inference function (program execution) | P2A matrix mapping               |
| 💨Receiving Feedback                   | Updates understanding (1/α1)             | Program-world evaluation               | Choice-based learning            |
|                                        |                                          |                                        |                                  |
| Dynamics                               |                                          |                                        |                                  |
| R1: Learning Loop                      | 👁️→🧠→🤜→👁️ (learns)                   | Neural → symbolic → neural             | Observable → perceptual → action |
| R2: Refining Loop                      | 👓→🧠→👆 (refines)                       | Language → program → inference         | Feature → attribute → choice     |
| B1: Rejecting Loop                     | Decays outdated understanding            | Invalid program rejection              | Mismatched perception pruning    |
| B2: Retiring Loop                      | Retires obsolete theories                | Obsolete inference removal             | Invalid attribute decay          |

| Aspect                 | Parallel Approach                                                                                                                  | Sequential Approach                                                                                                             |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Cost Structure         | • Lower relative testing costs<br>• Resource-intensive upfront<br>• Enables multiple concurrent experiments                        | • Higher per-test costs<br>• Resources spread over time<br>• Each test builds on previous learnings                             |
| Industry Fit           | • Fast-paced industries (biotech, software)<br>• Digital-first companies<br>• Platform technologies (e.g., Moderna's mRNA)         | • Traditional manufacturing<br>• Hardware-focused industries<br>• High individual test costs (aerospace, automotive)            |
| Uncertainty Management | • Better for high uncertainty environments<br>• Handles rapid market/tech changes<br>• Good for non-convex solution spaces         | • Better for stable environments<br>• Works well when path dependencies matter<br>• Suits predictable innovation cycles         |
| Learning Style         | • Broad but potentially shallow learning<br>• Quick identification of opportunities<br>• Simultaneous feedback across options      | • Deep understanding of each option<br>• Methodical knowledge building<br>• Clear cause-effect relationships                    |
| Risk Profile           | • Spreads risk across multiple options<br>• Higher upfront investment risk<br>• Better for avoiding missed opportunities           | • Concentrated risk on chosen path<br>• Lower initial resource commitment<br>• Higher risk of path dependence                   |
| Example Cases          | • Moderna: Multiple mRNA applications<br>• CRISPR: Various therapeutic applications<br>• Uber: Testing service models concurrently | • Tesla: Sequential battery development<br>• Waymo: Gradual autonomous capability expansion<br>• Traditional pharma development |
| Decision Making        | • Requires robust parallel decision frameworks<br>• Benefits from strong data infrastructure<br>• Needs clear comparative metrics  | • Simpler decision points<br>• Clear stage-gate process<br>• Easier to track progress                                           |

| Factor       | Parallel                                 | Sequential                              |
| ------------ | ---------------------------------------- | --------------------------------------- |
| Cost         | Low per-test, high total upfront         | High per-test, spread over time         |
| Best Context | High uncertainty, fast-changing markets  | Stable environments, clear pathways     |
| Example      | Moderna: Multiple mRNA trials at once    | Tesla: Step-by-step battery development |
| Learning     | Broad but shallow across options         | Deep understanding of chosen path       |
| Risk         | Hedged across options, high initial cost | Concentrated risk, lower upfront cost   |
| Speed        | Fast initial insights, shorter timeframe | Slower but thorough understanding       |
| Resources    | Needs large concurrent capacity          | Can manage with limited resources       |
