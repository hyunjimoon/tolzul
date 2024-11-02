## 1. problem definition
Startups has hostile condition from learning perspective. Their organization is versatile and volatile; strategy is personal and less principled; measurement is scarce and noisy, making operation highly contextual. Above all, they are long tail of companies each of which has little resource to invest in processifying the learning. Both success and fail stories abound, but without communities' consistent framework on startup operations, many lessons would be left unextracted. Several processification attempts include: Gans et al (2021)'s constructive approach analyzed the first two steps using a hypothesis test framework (e.g. in what context does choosing two candidate strategies and executing one has lowest cost), Fine et al (2022)'s empirical approach inspected more than 10 case studies under the lens of nail, scale, sail strategic trajectory, Hoffman (2018)'s blitzscaling which advocates prioritize speed over efficiency under uncertainty, based on his experience and observation. These frameworks, which complements each other, have limitations by itself as it is too static to build on, complicated to execute, contextual to adopt. Building on existing frameworks which complement each other, we start from the idea that startup growth is an iteration of assessing current state, executing different strategic actions, measuring performance. Returning to a learning perspective, if we view trajectory of every startup as spatio-temporal process, a good criteria for clustering can boost information pooling within a startup and between startups. First attempt for this criteria is hardness of product during nail and scale it stage. Using the information pooling between and within clusters (structural update mechanism that comes with hierarchical model), our goal is to suggest a framework where startups can learn both from other and its previous stage.[^1]

Below is the classification from spatio-temporal process perspective, with example from existing frameworks
1. spatial-discretization + interaction: intellectual, architectural, value chain, disruption (Gans et al., 2021) -> too static to build on
2. temporal-discretization: nail, scale, sail  (Fine et al., 2022) -> too complicated to execute
3. trajectorial-discretization: focus on certain strategy (blitzscaling, Hoffman 2018) -> too contextual to adopt (bit-centered business)

![[Pasted image 20230628081903.png]]


## 2. hypothesis
How hardness (:= $\frac{\text{value of atoms}}{\text{value of atoms  + value of bits}}$) of the product affect uncertainty of the environment? How startups should strategize its capability building and pivoting strategy? are two main questions. For concreteness, ice-cream scoop's hardness is 1 whereas generative AI services, open source libraries are near 0. I suggest five hypotheses:

### hypothesis 1 (separation strategy). harder product has stricter separation between development and production phase due to high failure cost (nested structure of manufacturing and visibility of catastrophe)

- compared to hardware which has separate development and production phase, software's value add activity is focused in development phase. in git term, most feature development happens in `dev branch` (via branching out and merging `feature branch` to `dev branch`). closest activity to production is deciding to merge `dev branch` to `master branch`. hardware is design plane before flying and software is build plane as we go.
- harder product has higher hierarchy of production due to mold for a mold concept (~ meat is energy inefficient)
- critical ratio(CR := $\frac{(p-c)}{(c-s)+ (p-c)}$) is near 1 (= $\frac{p}{p}$) for pure soft product. this increases inventory (higher CR  increase safety stock coverage and desired inventory coverage, thereby end up with higher inventory) from stock management system dynamics model (Sterman, 2000) below:
- ![[MatchingSupplyDemand.png]]
- #todo how hardness of product affects Charlie's tps mechanism which includes CR ratio
- harder product has lower uncertainty and critical ratio (underage cost/ (underage cost + overage cost)). softer products are easier to produce and less perishable, their cost (c) and salvage cost (s) converge to 0
- 
- ![[sys(tps).png]]
- #todo how lower fixed cost ratio (:= $\frac{c_{fixed}}{c_{fixed} + c_{variable}}$ ) for softer product affects decoupling point (as a measure of demand/supply uncertainty, degree of push/pull)

### hypothesis 2 (capability strategy). softer product has faster co-adaptation speed between need and solution
- especially for soft products, it's beneficial to nurture capability _while_ pivot, not nurture capability _then_ pivot : pivoting diversifies, increasing interaction, hence transform dynamics from converging (black below) to diffusion (red S-curve below) in the scale (storming) stage
- ![[Pasted image 20230628103542.png]]
- to operationalize this observation, attention ratio between the three information syncing (1. internal-internal ($\alpha$), 2. internal-external ($\beta$), 3. external-external ($\gamma$))  is our goal
- ![[dynamic_attention.png]]
- #todo questions remain where internal+external system converge to + could we quantify this with Hippel and Krogh (2006)'s need/solution co-evolve?
![[Pasted image 20230628113356.png]]


### hypothesis 3 (pivot strategy). harder product has higher risk but higher threshold leading to viscous pivot strategy
 - left and right are software and hardware's pivot strategy
   ![[hardness_pivot.png|800]]
   - pivoting with atom-capability is sturdier but viscous due to higher barriers from the slower clock speed of manufacturing
   - pivoting with bit-capability is diverse but insecure
   - hardware company (e.g. manufacturing Angularity) could keep comparative advantage after pivoting
   - softer company is more explorative in pivoting
   - examples from Fine et al (2022)
> - (soft) the research itself was pivoted after 3 years when you and Loredana went to ASB (Jared Diamond's Guns, Germs, and Steel was also pivoted)
> - (soft) Novaconfort's "2008 crisis in the real estate market, the company pivoted beyond construction and went into development and the rental business", capability came from learning, gradudecreas outsource) 
> - (hard) Angularity's "successful repeated pivots, in the context of fast-moving, technology-intensive markets, seemed to be due to its deep manufacturing and technical capabilities rather than to its connection to particular customers, markets, or products"

### hypothesis 4. easier knowledge transfer for harder product
- there is less confusion of correlation and causation in harder products. Physics is harder than statistics; the latter (regression in specific) aggregates over time.

### hypothesis 5. harder product has more centralized organizational structure 
- higher cost to pay when one component fail to comply with another (e.g. Tesla roadster)
- cost to pay for mistake is larger for harder product making it more centralized structure
- below is scheme Angie initiated (and further developed by Cathy DiGennaro and Vicky Yang in SD group - copyright)
- #todo how to measure centralization of an organization?
![[centralization.png]]

### hypothesis 6. strategy to soften is more efficient than harden
- harder product offers palpable and more accurate feedback from which organization can learn more effectively in early period. 
- e.g. aws: Amazon’s retail business is heavily based in atoms; originally outsourced its logistics to Ingram Book Company, but its heavy investment in inventory management systems and warehouses as it grew turned infrastructure limitations from a growth limiter to a growth factor. On the retail side, merchants pay Amazon to manage their inventories and logistics for them, while the massive computer systems that Amazon built to operate its retail business gave it the capabilities to launch its AWS business (which is a high-margin, bits-based business)
- e.g. some recommendations to write in paper the structure or simulation model before jumping into coding or using digital structuring tools
- counter e.g.  "easier for tech firm to make cars than a carmaker to become a tech company" (economist)

## 3. relevant literature
1. blitzscaling: from book blitzscaling, Hoffman (2018) advocates bit-based business (software companies like google and facebook), saying softer product can better
-  serve a global market, which in turn makes it easier to achieve a large market size
- tap into distribution techniques like virality, and their ability to be highly networked provides more opportunities to leverage network effects as bits are far easier to move around than atoms
- iterate quickly on products (many Internet companies release new software daily), making it faster and cheaper to achieve product/market fit
- can have fewer employees than most of their atom-based counterparts (e.g. WhatsApp)
Also, Hoffman mentions power of software has also made it easier to scale up atom-based businesses as well, despite—or perhaps because of—the growing dominance of bits. Below four hypothesis are constructed based on Hoffman (2018) and the above function $\pi()$ formulation.

2. In system dynamics, bits and atoms have different delay models. Sterman (2000) explains this as information not conserved.  which doesn't have as material and information delay, atom which has separate in and outflow whereas bit has single in/out flow which can be both positive and negative (fig.1). Defining model as goal's minimum viable product, it is natural to ask what justifies separate modeling of in and outflow for atom, rather than asking why bit has them combined. 
![[info_mat_delay_atom_bit.png]]

3. [Marginal cost society (Rifkin, 2014)(tbc)](https://ssir.org/books/reviews/entry/no_value) argues collaborative commons” will make anything and everything available for practically nothing -- these developments will overthrow capitalism as the world’s dominant economic model. 


[^1]: For information pooling,  Previous attempts of information pool in spatio-temporal process includes ship engine failure of 31 year time series among six types of engine and GDP, Covid death, hospitalization time series for 51 states in U.S. (collaboration with Hazhir, plenary talk in ISDC conference). 