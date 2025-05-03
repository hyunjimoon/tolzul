prior_abstract: Entrepreneurs in dynamic markets face the challenge of balancing exploration and commitment, particularly when deciding when to pivot based on new information. Pivots— strategic shifts in direction - are essential for adapting to market changes, but excessive or poorly timed pivots can hinder learning and harm long-term performance. The concept of exaptation (the repurposing of existing resources for new uses), offers two key strategies for structured experimentation: parallel pivots, which involve broad exploration of simultaneously tested ideas, and sequential pivots, a methodical approach where each experiment informs the next. However, there are risks inherent in these strategic decisions. In this study, we explore how they can be mitigated by using probabilistic programming and Bayesian modeling, which offer a structured framework for managing experimentation. We compare "test-four-choose-one" parallel and "test-two-choose-one-twice" sequential approaches across varying contexts of technological innovation and customer segments. Our initial results reveal that parallel search outperforms sequential search when test costs are low relative to pivoting costs, uncertainty is high, and true values of innovations and customer segments have low correlation.

---
# Understanding When to Test in Parallel vs Sequence

## Baseline: Independent Option Testing

When testing options independently, we build on [[📜Vul14_onedone]] which proves optimal sample per decision ratio is proportional to the time cost ratio of action to sampling. Learning, testing, sampling are used interchangeably and so are choosing, acting, deciding. Decision quality depends on how many samples we take ($\color{orange}{k}$) and the true probability of success ($\color{skyblue}{p}$). The quality improves with more samples but faces diminishing returns. This relationship is captured by our decision quality function: $Q(\color{orange}{k}, \color{skyblue}{p}\color{white}{)} = \color{skyblue}{p} \color{white}{\cdot (1 - B(}\color{orange}{\frac{k}{2}}, \color{orange}{k}, \color{skyblue}{p} \color{white}{))} + (1-\color{skyblue}{p}\color{white}{)} \color{white}{\cdot B(}\color{orange}{\frac{k}{2}}, \color{orange}{k}, \color{skyblue}{p} \color{white}{)}$ The time cost combines both action time and sampling time: $T(\color{orange}{k}, \color{red}{r}\color{white}{)} = \color{red}{r} \color{white}{+} \color{orange}{k}$, where $\color{red}{r}$ represents the ratio of action time-cost to sample time-cost. Higher $\color{lightgreen}{r}$ values indicate that actions are more expensive relative to sampling, pushing us toward more careful testing. The optimal strategy maximizes utility rate: $R(\color{orange}{k}, \color{red}{r}\color{white}{)} = \frac{Q(\color{orange}{k}, \color{skyblue}{p}\color{white}{)}}{T(\color{orange}{k}, \color{red}{r}\color{white}{)}}$ and we denote optimal number of samples per decision as $\color{orange}{k^*} = \underset{\color{orange}{k}}{\color{white}{argmax}} \color{white}{R(}\color{orange}{k}, \color{red}{r}\color{white}{)}$. The following plot (fig.7 from [[📜Vul14_onedone]]) shows  $\color{orange}{k^*}$ is proportional to $\color{red}{r}$.
 ![[Pasted image 20241119073540.png|100]]
This model reveals several key insights:
1. When $\color{red}{r}$ is high (either due to high action time cost (e.g. expensive actions like VC investments compared to public equity) OR due to low sample time cost (e.g. learn fast due to probabilistic reasoning training or have access to high fidelity signal), more samples per decision (higher N in test N choose 1) is optimal
2. When $\color{red}{r}$ is low (e.g. lower action time cost for high frequency trading firms with automated infrastructure), fewer samples per decision (lower N in test N choose 1) is optimal

This explains phenomena like:
- VCs taking extensive samples (longer due diligence time) before major investments (high $\color{red}{r}$)
- HFT firms making rapid decisions with minimal sampling (low $\color{red}{r}$)
- Individuals who got less analytical education or in environment full of misinformation,  makes faster decisions due to high sampling costs

## Correlated Case: Production and Market Testing

When options become correlated, we must consider both the production strategy (US vs Japan) and market choice (Texas vs California) simultaneously. The quality function now incorporates correlations: $Q(\color{orange}{k}, \color{skyblue}{μ}, \color{purple}{σ}, \color{red}{ρ}\color{white}{)} = \sum_i \color{skyblue}{p_i}\color{white}{(1-Φ(}\frac{x-\color{skyblue}{μ_i}}{\color{purple}{σ_i}}\color{white}{))} + \color{red}{ρ}\color{white}{ΔQ}$

Our testing matrix reveals four distinct scenarios:

US batteries in Texas represent our low-bar production and market test, showing consistent high performance (μ=4.0, σ=0.5) but providing limited learning when successful. A failed test here would strongly indicate fundamental issues with the product.

Japanese batteries in Texas exemplify a high-bar test in both dimensions with lower average satisfaction (μ=2.5) but higher variance (σ=1.5). Success here would provide strong evidence of product excellence by overcoming cultural barriers, while failure might simply reflect market bias.

US batteries in California present a mixed case - low-bar production but high-bar market - where environmental and technological preferences create uncertainty (μ=3.5, σ=1.0). The higher variance indicates valuable learning opportunities about market fit.

Japanese batteries in California offer a technology-focused validation (μ=3.5, σ=0.8) with fewer cultural barriers, making it ideal for pure product quality assessment.

The optimal testing strategy depends on three key factors: the correlation between options ($\color{red}{ρ}$), the relative cost of action versus sampling ($\color{green}{r}$), and the value of learning from interactions ($\color{white}{ΔQ}$). When these factors align - high correlation, low sampling costs, and valuable interaction effects - parallel testing becomes the superior choice.

This analysis demonstrates why parallel testing often becomes optimal in early-stage product development where correlations are high and the cost of missing critical interaction effects outweighs the expense of simultaneous testing.

----
 
2024-11-18
# 0. Model

 - [ 4,4,5,2,2,2 ]: [1,3,5, 3,4,5]  VS [ 4,4,5,3,4,5 ]: [1,3,5, 2,2,2]
- manufacture in [japan, us] X test in [Texas, CA]
- angie thinks 
japan's battery in Texas -  japan's battery in CA != us's battery in Texas -  us's battery in CA 
japan's battery in Texas -  us' battery in CA != japan's battery in Texas -  us's battery in CA 

![[🎞️🪶.png|1000]]

----

angie's proposal (open to acceptance/rejection)
# 1. Breaststroke Model of Innovation: An Evolutionary Approach

The breaststroke swimming technique offers profound insights into how startups can navigate market uncertainty. Just as breaststroke demonstrates remarkable adaptability across diverse water conditions, successful startups must maintain resilience while exploring new opportunities. This natural rhythm manifests in three distinct phases that mirror the evolutionary cycles of innovation.

# 2. Theoretical Foundation: The Breast Stroke Model of Innovation

We establish theoretical foundation for breast stroke model of innovation. Experiment design theory and adjacent possibility theory are two pillars supporting this concept. After understanding the dynamics of breast stroke where sweep fuels thrust and glide enables sweep, we apply this to natural iteration between exploration and exploitation. Our key argument in organizational terms is, parallel exploration during early stages ("nail it") generates unexpected discoveries—spandrels—that become crucial advantages during scaling phases. 

**Experimental Design Theory (EDT)** reveals fundamental error management trade-offs in organizational validation structures. [[📜Heimann93_challenger_org]] demonstrates through NASA's experience how parallel validation prevents catastrophic false negatives while sequential checks protect against dangerous false positives. [[📜gans23_expchoice]] extends this insight by showing how firms optimally choose unbalanced experiments - either high-bar or low-bar - rather than balanced approaches, particularly when prior beliefs are optimistic. Like a swimmer's wide sweep creating maximum surface contact, [[📜DOW10_parallel_prototyping]] proves empirically that parallel prototyping leads to better design outcomes and higher self-efficacy by enabling rapid feedback cycles across multiple solution paths. [[🗄️🪶product2]] [[🗄️product2_EDT]]

**Adjacent Possibility Theory (APT)** demonstrates how parallel exploration enables unexpected discoveries - spandrels - that become crucial scaling advantages. [[📜Kauffman22_theory_of_adj_possible]] establishes how the world "bubbles forth" creating new possibilities through combinations, with sudden explosive transitions marking key breakthroughs. [[📜Mokyr92_evoldyn_tech]] reinforces this through technological evolution, showing how macroinventions create new "species" that enable subsequent microinventions. Like a swimmer's spreading legs building tension, [[📜Andriani_exaptation_creativity_source]] reveals how discontinuous evolution occurs through functional shifts of existing traits. [[🗄️🪶product2_TAP]]

The breast stroke's three-phase rhythm reveals how organizations naturally cycle between innovation modes. This mechanism bridges EDT's error management with APT's evolutionary dynamics through coordinated movement patterns:

**Wide Sweep (NAIL IT)**: [[📜Mokyr92_evoldyn_tech]]'s concept of macroinventions demonstrates how radical innovation requires parallel "hopeful monsters" - multiple simultaneous experiments that might create new technological species. [[📜Heimann93_challenger_org]]'s parallel validation prevents false negatives in these experiments, while [[📜Kauffman22_theory_of_adj_possible]]'s adjacent possible expands through simultaneous testing. Like a swimmer's arms creating maximum surface contact, organizations cast wide nets seeking breakthrough innovations that can spawn subsequent microinventions.

**Focused Thrust (SCALE IT)**: This phase embodies [[📜Mokyr92_evoldyn_tech]]'s microinventions - the essential refinements that realize macroinventions' economic potential. [[📜Codini23_bmi_exapt_sme]] shows how firms transform experimental insights into standardized processes, just as the swimmer's powerful thrust converts scattered explorations into directed force. Like Mokyr's observation that "without microinventions, most macroinventions would not be implemented," organizations must convert broad market insights into targeted segments and crystallize flexible systems into efficient standards.

**Glide (SAIL IT)**: The streamlined glide represents the crucial transition period [[📜Mokyr92_evoldyn_tech]] identifies between innovation cycles. Just as evolution is path-dependent - "selection operates on what exists, not what could have been" - organizations must optimize current advantages while positioning for the next wave of macroinventions. Like a swimmer gathering momentum for the next stroke, firms balance system optimization with preparation for future wide sweeps, maintaining the natural rhythm between radical change and incremental improvement.
# 3. The Spandrel Effect: How Initial Exploration Enables Scaling

The parallel exploration during early stages creates unexpected advantages (spandrels) that become crucial during scaling phases. 


| Phase                                                                         | Swimming Action                                                                                                                                  | Innovation Action                                                                                                                                                  | Nail to scale strategy (靜中動1)                                                                                 |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **Wide Sweep (NAIL IT)** <br>![[Pasted image 20241114081056.png\|100]]        | <font color="#C0A0C0">**Arms:** Sweep wide for maximum surface area</font><br><font color="green">**Legs:** Spread wide, building tension</font> | <font color="#C0A0C0">**Marketing:** Cast wide net for market exploration</font><br><font color="green">**Operations:** Establish flexible, minimal systems</font> | **Spandrel Effect:**<br>Wide exploration creates scaling options<br>Customer insights enable future targeting |
| **Focused Thrust (SCALE IT)** 💥<br>![[Pasted image 20241114081116.png\|100]] | <font color="#C0A0C0">**Arms:** Pull inward forcefully then push forward</font><br><font color="green">**Legs:** Snap together powerfully</font> | <font color="#C0A0C0">**Marketing:** Convert insights to targeted segments</font><br><font color="green">**Operations:** Standardize successful processes</font>   | **Growth Execution:**<br>Leverage nail-stage learnings<br>Transform experiments into standards                |
|                                                                               |                                                                                                                                                  |                                                                                                                                                                    | ⭐️key: spandrel in nail enables thrust in scale                                                               |

The parallel-sequential distinction manifests in two fundamental trade-offs:

**Error Management (EDT)**
```
Parallel (Low-bar): 1-∏(fi)  "Only need one winner"
Serial (High-bar): ∏(1-fi)   "Chain as strong as weakest link"
```

**Growth Dynamics (APT)**
```
Sequential: Mt+1 = Mt(1-μ) + α1Mt           [Linear growth]
Parallel:   Mt+1 = Mt(1-μ) + α(2^Mt - Mt - 1) [Explosive growth]
```

TODO: choose between two math models:
- 📍🧠a2s: [action sample time cost ratio]( https://amoon.world/%F0%9F%8C%99amoon()/%F0%9F%91%93synthesize(%E2%9A%A1%EF%B8%8F)/%E2%9B%B0%EF%B8%8F%F0%9F%92%A0scale_seg_collab/%F0%9F%90%B8Breast+Stroke+Model+of+Innovation#3.1+baseline+model+1)
- 🔴💜o_m: [investment decision in operation vs market](https://amoon.world/%F0%9F%8C%99amoon()/%F0%9F%91%93synthesize(%E2%9A%A1%EF%B8%8F)/%E2%9B%B0%EF%B8%8F%F0%9F%92%A0scale_seg_collab/%F0%9F%90%B8Breast+Stroke+Model+of+Innovation#3.2+baseline+model+2) 

[[🐸Breast Stroke Model of Innovation]]
# 4. Strategic Implications

Organizations should consciously design their innovation cycles to mirror this natural rhythm. During wide sweep phases, maintain flexible systems while running parallel experiments across market segments. In focused thrust phases, convert market insights into standardized processes while leveraging unexpected advantages discovered earlier. During glide phases, optimize current systems while preparing for the next cycle of exploration.


----
posterior_abstract: 

- [ ] choose math models (📍🧠a2s vs 🔴💜o_m)
- [ ] parallel better in low vs high correlation
- [ ] decide to remove/include vertical correlation in [[🗄️🪶product2_TAP]] (internal value chain dependencies)
- [ ] decide to remove/include vertical correlation in [[🗄️🪶product2_TAP]] (shared environmental uncertainty)