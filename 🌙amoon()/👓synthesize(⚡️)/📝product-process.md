1. [[📜Agrawal21_ebl_choice]] is isomorphic to [[🗄️👁️🧠explain_away]]
2. from simulation model, optimal test N choose 1 (TNC1)'s N (y axis of "optimal sample per decision") is proportional to action and sample time-cost ratio (`A2S`)
3. temporally, `A2S` is likely to increase from nail to sail (increase of action time-cost `A2S`); spatially `A2S` is larger for control (than execute) and collaborate (than compete)
4. based on 2, TNC1's N should be larger for control and collaborate
5. based on 1, different observed behavior of TNC1's N (parallel vs sequential) can all be interpreted as rational (environment's `A2S` explains away irrationality given heterogeneous observed behavior)
   
- todo1: would the choice of compete vs collaborate be affected by `A2S`?
## ⚙️Process

[[two_sigma_human_intution]]
using [two sigma_when human intuition cld](https://claude.ai/chat/f9e600f4-749c-43ca-b574-91cd166d77af) and for each row improvement ([enhancing ml with human intuition cld](https://claude.ai/chat/038e3d1d-8200-42bc-9867-5544623728dc)) i was updating the second row. 

| Nature of Mental State Inference \ Level of Analysis                           | Individual (Micro)                                                                                                                               | Multi-agent / Population (Macro)                                          |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| Fixed Planning with Belief Inference<br>(answering how)                        | [[📍focusing on action sample ratio]]<br>[[📝🧭Vectorizing Adaptation]]<br>[[🎲Sampling with and without Replacement]]<br>                       | [[📝🪶Parallel Evolutionary and Sequential Bayesian Startup Adaptations]] |
| Inverse Planning with Belief-Desire Joint Inference <br>(answering (how, why)) | [[📝👻phantom rationalize meaning]]<br>[[🐸Breast Stroke Model of Innovation]]<br>[[📝🤝Conversational Inference of Equity Valuation Agreement]] | [[📝🔴💜physical-digital-institution]]                                    |
The Individual-Population axis distinguishes between single-agent and multi-agent analysis. At individual level, [[📝🧭Vectorizing Adaptation]] models how a single entrepreneur allocates attention between operations and markets through direction and speed of decision vectors. At population level, [[📝🪶Parallel Evolutionary and Sequential Bayesian Startup Adaptations]] examines how multiple firms' search strategies interact through shared uncertainties ($\color{SkyBlue}{\sigma}$) and correlations ($\color{Orange}{\rho}$), while [[📝🔴💜physical-digital-institution]] studies how regulatory effectiveness varies when agents influence each other's beliefs and goals.

Fixed Planning versus Inverse Planning distinguishes between inferring only beliefs (how) versus jointly inferring beliefs and desires (how and why). In Fixed Planning, [[📝🧭Vectorizing Adaptation]] and [[📝🪶Parallel Evolutionary and Sequential Bayesian Startup Adaptations]] infer beliefs ($\color{Green}{p_c}, \color{Purple}{p_r}$) about success probabilities while assuming known utility functions ($\color{Red}{U}$). In Inverse Planning, [[📝👻phantom rationalize meaning]] shows how investors must jointly infer startups' capabilities and strategic intentions, while [[📝🔴💜physical-digital-institution]] demonstrates why this joint inference challenge makes digital regulation (30% AV compliance) harder than physical regulation (85% EV compliance).

[[🐸Breast Stroke Model of Innovation]] bridges these frameworks by showing how cyclical patterns of sweep-thrust-glide help individual firms coordinate their learning about capabilities (belief inference) with discovery of new opportunities (desire inference), revealing spandrels that become crucial advantages during scaling.


## 📝Product

## Executing in 2024
### theory
#### [[📝🧭Vectorizing Adaptation]]
- Evaluators: Charlie, Scott, Josh (class project)
- Duration: 23W-24W
	- Abstract:This paper develops a computational framework for understanding entrepreneurial cognitive resource allocation during venture scaling. Through vector-based modeling of cost-reducing and revenue-growing activities, we demonstrate how seemingly biased allocation patterns emerge as rational adaptations to industry-specific returns and uncertainties. Our framework unifies entrepreneurial decision-making through two key dimensions: directional focus between market and operations, and execution speed in sampling and action.
	
	- ✅ Agree with:
		- Sequential decision-making where each step requires choosing between operations OR market understanding, with Operational capability capping monetization of market knowledge
		- Both "thinker" and "doer" strategies as rational responses to specific industry-entrepreneur contexts
	- ❌ Disagree with:  
		- Traditional decision-making models that don't account for resource constraints in scaling companies  
		- The role of Bayesian inference methods for researchers from Bayesian decision-making by agents should be distinguished

#### [[🐸Breast Stroke Model of Innovation]]

#### [[📝🪶Parallel Evolutionary and Sequential Bayesian Startup Adaptations]]
- Collaborators/Evaluators: Charlie, JB
- Duration: 24S-25, submitted to [complex adaptive systems](https://sites.mit.edu/cas2025/) 
- Abstract: Ventures face a critical choice between sequential and parallel search strategies when testing new opportunities. We synthesize three theoretical perspectives - experimental design theory, adjacent possibility theory, and convergence diagnostics - to understand this choice. Our synthesis reveals that parallel search represents a "low-bar" experiment design emphasizing exaptation through many short chains, while sequential search embodies a "high-bar" approach favoring adaptation through fewer, longer chains. Through computational modeling of Bayesian belief updating, we formalize when each strategy is optimal by analyzing three key dimensions: a) 📍Cost structure, where parallel search becomes optimal when test-to-action cost ratios are low (T4C1 total cost = 4test + $\color{Red}{1choose}$ vs T2C1 total cost = (2test + $\color{Red}{1choose}$) × 2); b) 🎲Uncertainty propagation, where parallel search enables broader exploration of the 'adjacent possible' through simultaneous testing ($\color{Green}{\sigma_c}, \color{Purple}{\sigma_r} \sim \color{SkyBlue}{exp(\sigma)}$), allowing ventures to discover unexpected possibilities (exaptation) rather than committing early to a single path; c) 🧩Correlation effects, both horizontal (across industry) and vertical (within value chain), where parallel search better captures joint distributions and cross-level dependencies ($\color{Green}{\sigma_c}, \color{Purple}{\sigma_r} \sim \color{Orange}{\rho} * \color{SkyBlue}{exp(\sigma)}$). We derive a unified decision rule: choose parallel search when implementation costs and uncertainty are high ($\color{Red}{c_{act}} * \color{SkyBlue}{\sigma} * \color{Orange}{k}$ is large), prefer need (market)-first sequential search when market uncertainty dominates ($\color{Green}{\sigma_c} < \color{Purple}{\sigma_r}$), and default to solution (product)-first sequential search otherwise. This framework reconciles the apparent inefficiency of parallel search with its empirical prevalence by showing how high uncertainty and correlation can make broad exploration through parallel, low-bar experiments more valuable than deep exploitation through sequential, high-bar tests. 
- ✅ Agree with: The exploration of both parallel and sequential approaches to startup adaptation, using probabilistic programming and Bayesian modeling to manage experimentation and reduce cognitive biases in pivoting decisions.
- ❌ Disagree with: The notion that a one-size-fits-all approach to startup adaptation is sufficient, without considering the varying contexts of technological innovation, customer segments, and the relative costs of testing versus pivoting.

### empirical

#### [[📝👻phantom rationalize meaning]]
- Collaborators: Jeff
- Evaluators: Teppo Felin, Todd Zenger, Arnaldo Camuffo at ION lab conference where phds have thesis presentation opportunities (Jan.2025)
- Duration: 24S-24W
- Abstract: Early-stage venture investors make decisions with limited information, relying on observable startup characteristics to form expectations about potential success. For example, prior research shows that investors often focus on factors like the management team or business model when assessing a firm’s ability to execute its vision. Little is known, however, about how these observable characteristics map onto the perceptions investors use when evaluating deals or how this mapping varies by investor type. Our research investigates this process, drawing on theories of rational meaning creation and lay theory construction to explain how investors interpret observable signals as indicators of unobservable qualities. We develop a hierarchical Bayesian framework that allows us to empirically study how investors with different expertise and focus areas translate deal characteristics into structured beliefs about a venture’s potential.
   Our framework models two key perceptual dimensions that emerge from investors' lay theories: beliefs about the business model validity and the team’s ability to execution (i.e., is the idea viable and can the team make it happen). Using a novel experimental design that combines survey research methods with large language models, we elicit these belief structures from archetypical investors (e.g., early-stage software VCs, growth-stage investors). The hierarchical structure allows us to identify both individual-level heterogeneity in how investors evaluate startups and population-level patterns in attribute-to-perception mappings, while the LLM augmentation enables systematic exploration of investor responses across a broad range of startup profiles.
  Our approach reveals how the process of heterogeneous rational meaning construction can lead to systematically different valuations of identical startups. We find that investors' domain expertise and investment stage create distinct lay theories about which observable characteristics signal strong execution capability or business model validity. Taken collectively,  our research can help explain several puzzling phenomena in entrepreneurial finance, including persistent valuation disparities and apparent term sheet inefficiencies (todo). Our findings advance a theoretical understanding of meaning construction in high-stakes financial decisions while providing practical guidance for both entrepreneurs and investors in early-stage negotiations.

## Planning in 2025
### empirical
#### [[📝🤝Conversational Inference of Equity Valuation Agreement]]
- Evaluators: Vikash (class project)
- Duration: 24W-25S
- Abstract: We introduce a prototype toolbox for startup pivoting, employing a cognitive system’s multi-level framework to reconcile tension between action and optimization in entrepreneurship. By modeling founders and investors as resource-rational agents, we interpret inference-based proposals as actions, viewing term sheet negotiations as a convergence process toward optimal solutions. In this context, conversational inference between parties represents an information processing mechanism aimed at maximizing expected utility given shared beliefs. Our approach synthesizes entrepreneurial strategy, Bayesian decision theory, probabilistic programming, and conversational inference across computational, algorithmic, and implementation levels. This toolbox bridges the gap between theoretical optimization objectives with algorithmic actions in entrepreneurial practice.
- ✅ Agree with: The strategic value of parallel search in fundraising, where founders engage multiple investors simultaneously to create alternatives, gain market insights, and optimize term sheet outcomes.
- ❌ Disagree with: The notion that founders should quickly accept the first term sheet or limit their interactions to a single investor, rather than deliberately slowing down the process to create multiple options and gain negotiating leverage.

#### [[📝🔴💜physical-digital-institution]]

- Evaluators: Josh Lerner (class project)
- Duration: 25S-
- Abstract: We introduce a prototype toolbox for startup pivoting, employing a cognitive system’s multi-level framework to reconcile tension between action and optimization in entrepreneurship. By modeling founders and investors as resource-rational agents, we interpret inference-based proposals as actions, viewing term sheet negotiations as a convergence process toward optimal solutions. In this context, conversational inference between parties represents an information processing mechanism aimed at maximizing expected utility given shared beliefs. Our approach synthesizes entrepreneurial strategy, Bayesian decision theory, probabilistic programming, and conversational inference across computational, algorithmic, and implementation levels. This toolbox bridges the gap between theoretical optimization objectives with algorithmic actions in entrepreneurial practice.
- ✅ Agree with: The strategic value of parallel search in fundraising, where founders engage multiple investors simultaneously to create alternatives, gain market insights, and optimize term sheet outcomes.
- ❌ Disagree with: The notion that founders should quickly accept the first term sheet or limit their interactions to a single investor, rather than deliberately slowing down the process to create multiple options and gain negotiating leverage.

how i reach from `ab` to `abde` cell using scientist, artist, judge bridge is explained in [[💠integ(process-product)]]