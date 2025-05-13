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