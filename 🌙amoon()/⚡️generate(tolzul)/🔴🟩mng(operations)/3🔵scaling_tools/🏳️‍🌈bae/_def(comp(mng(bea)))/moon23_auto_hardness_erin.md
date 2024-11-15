## 1. problem definition
Startups has hostile condition from learning perspective. Their organization is versatile and volatile; strategy is personal and less principled; measurement is scarce and noisy, making operation highly contextual. Above all, they are long tail of companies each of which has little resource to invest in processifying the learning. Both success and fail stories abound, but without communities' consistent framework on startup operations, many lessons would be left unextracted. Several processification attempts include: Gans et al (2021)'s constructive approach analyzed the first two steps using a hypothesis test framework (e.g. in what context does choosing two candidate strategies and executing one has lowest cost), Fine et al (2022)'s empirical approach inspected more than 10 case studies under the lens of nail, scale, sail strategic trajectory, Hoffman (2018)'s blitzscaling which advocates prioritize speed over efficiency under uncertainty, based on his experience and observation. These frameworks, which may complement each other, have limitations by itself as it is too static to build on, complicated to execute, contextual to adopt. Building on existing frameworks which complement each other, we start from the idea that startup growth is an iteration of assessing current state, executing different strategic actions, measuring performance. Returning to a learning perspective, if we view trajectory of every startup as spatio-temporal process, a good criteria for clustering can boost information pooling within a startup and between startups. First attempt for this criteria is hardness of product (supply) and industry (demand) during nail and scale it stage. Using the information pooling between and within clusters (structural update mechanism that comes with hierarchical model[^1]), our goal is to suggest a framework where startups can strategize development and production, pivot, organization scaling according to the hardness of their supply and demand.

Table.1 classifying literature from spatio-temporal process perspective
1. spatial-discretization + interaction: intellectual, architectural, value chain, disruption (Gans et al., 2021) -> too static to build on
2. temporal-discretization: nail, scale, sail  (Fine et al., 2022) -> too complicated to execute
3. trajectorial-discretization: focus on certain strategy (blitzscaling, Hoffman 2018) -> too contextual to adopt (bit-centered business)

## 2. hypothesis
product's hardness is defined as  $\frac{\text{value of atoms}}{\text{value of atoms  + value of bits}}$. e.g. ice-cream scoop's hardness is 1 whereas generative AI services and open source libraries are near 0.
hypotheses:
1. product's hardness affects nature of separation between development and production, pivot, organization scaling
2. bottleneck flips from software to hardware and this subversion is faster if the industry is softer 
3. strategy exist at the level of one company, that coordinate different evolution speed of product and industry hardness

to elaborate,
1. hardware evolve slower than software due to separation, co-adaption, pivot
	1. (separation) harder product has stricter separation between development and production phase due to high failure cost from nested structure of manufacturing and catastrophe visibility
		- compared to hardware which has separate development and production phase, software's value add activity is focused in development phase. in git term, most feature development happens in `dev branch` (via branching out and merging `feature branch` to `dev branch`). closest activity to production is deciding to merge `dev branch` to `master branch`. hardware is design plane before flying and software is build plane as we go.
		- harder product has high failure cost due to nested structure of manufacturing. mold of a mold of a mold... needs to be manufactured for hardwares, but this is nested structure is less in software (e.g. citation for research, library import for coding are faster, easier, able to do alone than  ) i.e. every product stands on the shoulder of giant but harder the product is, the more visible and costly giant's shoulder becomes (~ meat is energy inefficient?). 
		- ref: [cusumano](https://trello.com/c/hl12zijg) (toyota lean vs microsoft agile), causal loops for (commodity vs service) + [safety stock and backlog policy around critical ratio in supply chain](https://trello.com/c/8iFiecUP)
	2. (co-adaptation) harder product has slower co-adaptation speed between demand and supply (need and solution)
		- for soft products, it's beneficial to nurture capability _while_ pivot, not nurture capability _then_ pivot : pivoting diversifies, increasing interaction, hence transform dynamics from converging (black below) to diffusion (red S-curve below) in the scale (storming) stage
		- ref: [hippel (user-innovation, need-solution pair)](https://trello.com/c/pZh9zvkQ)
	3. (pivot) softer product has lower risk but lower threshold leading to less viscous pivot strategy
		- software (green) and hardware (red)'s pivot strategy
		   ![[hardness_pivot.png|300]]
		   - softer solutions are more adhesive to needs in different domain (ready, fire, aim by Neil Gershenfeld)
			   - fluidic ribosome (create biology for nonbiological) -> genome transplantation
			   - rfid tag (can't read one at a time, nonlinearity in material, spin resonance) -> spin-spin exchange quantum computing
			   - glue composite parts -> snap parts, modulus ultralight material
			   - weak yo-yo ma hand protection (hand tomography)-> auto safety sensor for infants
			   - apply principles of internet into device physics -> iot
		
	1.  (organization structure) harder product has more centralized organizational structure which is integrated hence less generalizable and harder to copy
		- high failure cost of hardware induce more centralized organizational structure
		- ![[centralization.png|500]]
2. industry's bottleneck flips from software to hardware due to slower evolution speed of hardware in 1
	1. temporal disaggregation: bottleneck analysis
		![[bottleneck.png|900]]
	2. spatial disaggregation: comparing S|S, H|S, S|H, H|H ratio for industry with different hardness
	![[industry_hardness.png|500]]
3. for startup to operationalize 1, 2
	1. soften is better than harden
	2. dynamic attention ratio between the three information sync(1. internal-internal ($\alpha$), 2. internal-external ($\beta$), 3. external-external ($\gamma$)) exists
![[dynamic_attention.png|500]]

## 3. future work
- how to separate value of bits for two sided market (platform) - same sided, network etc
- where internal (one company) +external (industry) system converge to 
- how to connect with Hippel and Krogh (2006)'s need/solution co-evolove, especially how hardness affects + coevovle? (agree or understand converge?)
![[Pasted image 20230628113356.png|800]]

- how to connect [Marginal cost society (Rifkin, 2014)(tbc)](https://ssir.org/books/reviews/entry/no_value) argues collaborative commons” will make anything and everything available for practically nothing -- these developments will overthrow capitalism as the world’s dominant economic model. 
- how does same production but different recovery period affect clockspeed? e.g. similar (re)production ratio of covid and chronic waste disease (2~5) vs different recovery speed (1 week vs 1.5 yr)

[^1]: For information pooling,  Previous attempts of information pool in spatio-temporal process includes ship engine failure of 31 year time series among six types of engine + GDP, Covid death, hospitalization time series for 51 states in U.S. (collaboration with Hazhir Rahmandad).