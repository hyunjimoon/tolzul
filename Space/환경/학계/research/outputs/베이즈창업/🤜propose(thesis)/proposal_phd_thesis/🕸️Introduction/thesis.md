[[2025-07-30|25-07-30-16]]
to cite in [[📝(👾🐢🐅🐙)_한글]], 
### 1.2 Literature Foundations

Fine et al. (2022) architectured multiple operational tools and systematically weaved them with entrepreneurial decision cases but didn’t provide instructions on why, how, and when entrepreneurs should use each tool. Bayesian entrepreneurship oﬀers a quantitative lens to entrepreneurial decision making (Agrawal et al., 2024; Camuﬀo et al., 2024), but unsettled confusion of the ﬁeld on normative and positive approaches, makes the usefulness of model questionable. Frameworks like the Business Model Canvas (Osterwalder and Pigneur, 2010), Lean Startup (Ries, 2011; Eisenmann et al., 2012), articulate hypotheses without systematic updating but is not dynamic enough to capture feedbacks and don’t provide decision making rule under uncertainty with constrained resource. Strategy research proposes some dynamic stopping rules (Gans et al., 2019; Chavda et al., 2024) but lacks integration with resource rationality Bhui et al. (2021) or cognitive developments Ullman and Tenenbaum (2020).

STRAP aims to ﬁll these gaps. Section 2 details the STRAP framework and mathematical formulations for both modules. Section 3 presents a comparative case study of STRAP guided vs. non-guided trajectories. Section 4 discusses implications for operations, strategy, and real options theory.
## 4 Discussion

STRAP not only bridges multiple stakeholders (customer, operations partner, investor) and methods (inference and optimization) but also academic domains (operations, strategy, ﬁnance). This is not surprising given entrepreneurial decision making’s universality.

4.1 Connections to Entrepreneurial Operations

STRAP aligns with (Fine et al., 2022)’s work on avoiding "naked scaling" by introducing structured operational processes. While Fine et al. propose ten scaling tools (e.g., processiﬁcation), STRAP complements this by quantifying which tool to deploy ﬁrst based on uncertainty reduction. Their observation that ventures adopt "capability-ﬁrst" or "customer-ﬁrst" modes is captured in STRAP through adjustable stakeholder weights (w j ) and initial states (S 0 ), enabling personalized, contextaware recommendations. This addresses the technical challenge of adaptive guidance raised in the introduction, oﬀering long-term utility as ventures transition between operational modes during scaling.

4.2 Synergy with Entrepreneurial Strategy

Gans et al. (2019)’s recommendation for explore-exploit stopping rule in entrepreneurial settings is called “Test two choose one,” providing insight that multiple equally viable alternatives exist (especially for high-quality ideas). STRAP speciﬁes this multiplicity as multiple stakeholders and actions targeting to lower their uncertainty, formalizing the trade-oﬀ between learning and commitment through the dual variable of resource constraint γ . When the value of additional tests falls below γ , STRAP triggers commitment–a quantitative enhancement to Gans et al.’s qualitative stopping rule. Interpreting resource constraint axiom from their paper as constraining one action per timestep (Σa j = 1) Equation 6 provides stopping rule. It’d be interesting to explore their connection to unify j diﬀerent perspectives on sequential versus parallel actions in entrepreneurship (Dow et al., 2010; Ott and Eisenhardt, 2020).

4.3 Real Options Theory for Entrepreneur-centered ﬁnancing

STRAP advances entrepreneur’s usability of real options theory by synthesizing it with three established theories. First, using ABSTRACTION principle from model developing theory (Tenenbaum

9 et al., 2011; Bernstein, 2023), STRAP explicitly models interdependencies among multiple stakeholders. Its abstracted mapping between observable venture attributes and stakeholders’ choice probability in perception module enables actions targeted to one stakeholder to be spilled over to increase the acceptance probability of others. Uber’s strategy to focus on customer popularity eventually eased regulatory approval and incentivized driver participation. STRAP can capture the tradeoﬀ on the number of stakeholder (J): maintaining a larger value grid (size JK) increases computational costs but creates more options. This advances traditional real option theory where risk is analyzed in isolation.

Second, using DUALITY from optimization theory Boyd and Vandenberghe (2004); Schrijver (1998), it replaces static thresholds with a dynamic primal-dual optimization framework that continuously recalculates the cost-beneﬁt tradeoﬀ of experiments through shadow prices γ , leveraging primal-dual convergence to enable adaptive scaling as uncertainties evolve.

Through AGENCY, STRAP models stakeholders’ commitment states (reject, consider, accept), positioning entrepreneurs at the center of decision-making rather than as passive recipients of investor preferences, enabling multiple paths to success through active coordination of stakeholder commitments. This approach diﬀers signiﬁcantly from the investor-led experimentation paradigm described by Nanda (2024), which emphasizes staged, investor-driven learning as the primary mechanism for uncertainty reduction. Instead, STRAP recognizes that successful ventures require coordinated uncertainty resolution across all key stakeholders simultaneously, with entrepreneur at the center and investor as one stakeholder.




# Key Questions Comparison Table

|Big Questions|Small Questions|
|---|---|
|**Moral Hazard in Experimental Design**|• What is the nature of the moral hazard problem in Bolton et al.? <br> • How do entrepreneurs' incentives differ from investors'? <br> • Why are traditional "skin-in-the-game" incentives ineffective? <br> • How does this compare to uncertainty management in Moon's STRAP framework?|
|**Impact of Different Experimental Design Scenarios**|• How does moral hazard manifest in independent tasks scenarios? <br> • How does moral hazard change when sensitivity and specificity are substitutes? <br> • How does moral hazard change when sensitivity and specificity are complements? <br> • Under what conditions does the entrepreneur's design align with the investor's preferred "killer experiment"? <br> • How does this compare to STRAP's optimization approach?|
|**Effects of Multiple Milestones or Dimensions**|• How would multiple sequential milestones affect moral hazard in experiment design? <br> • Would serial correlation between experiments emerge? <br> • How would multiple dimensions create trade-offs in information gathering? <br> • Could stage-specific incentives help resolve the moral hazard? <br> • How does this relate to Moon's multi-stakeholder coordination approach?|
|**Evaluation of Model Assumptions**|• How realistic is the assumption of no information asymmetry? <br> • When is the unverifiable experiment design assumption most valid? <br> • How would reintroducing private information affect the model insights? <br> • How would effort diversion impact experimental outcomes? <br> • How could STRAP's framework complement Bolton's approach to moral hazard?|

# Variable Mapping Between Papers

|Bolton et al. Concept|Bolton Variable|Moon Concept|Moon Variable|
|---|---|---|---|
|Venture value if successful|V|Venture value|fjs (stakeholder state values)|
|Prior probability of success|p0|Prior probability|Various, captured in ~pj (choice probabilities)|
|Cost of experiment|C|Cost of experiment|cj (cost coefficient)|
|Cost of full development|K|Budget constraint|R (total budget)|
|Experiment specificity|s1|Experiment parameters|Not directly equivalent, but affects stakeholder choice probabilities|
|Experiment sensitivity|s2|Experiment parameters|Not directly equivalent, but affects stakeholder choice probabilities|
|Entrepreneur's private benefit|Z|Not explicitly modeled|N/A|
|Investor ownership stake|α|Not explicitly modeled|N/A|
|Expected payoff from experiment|πs1,s2|Uncertainty reduction|ΔHj (entropy reduction)|
|Investor utility function|UI|Investor expected value|Σs fjspjs (expected value for stakeholder j)|
|Proof-of-failure payment|X|Not explicitly modeled|N/A|
|N/A|N/A|Threshold targets|μj (minimum acceptable expected value)|
|N/A|N/A|Dual variable for threshold|λj (marginal value of relaxing threshold constraint)|
|N/A|N/A|Dual variable for resource|γ (marginal value of additional budget)|
|N/A|N/A|Weighted aggregate uncertainty|Σj wjHj(~pj)|

The key difference is that Bolton et al. focus on a principal-agent framework with moral hazard in experiment design, while Moon's STRAP framework focuses on uncertainty reduction across multiple stakeholders without addressing moral hazard. Bolton uses probability variables to model experiment information content, while Moon uses information-theoretic entropy to quantify uncertainty.