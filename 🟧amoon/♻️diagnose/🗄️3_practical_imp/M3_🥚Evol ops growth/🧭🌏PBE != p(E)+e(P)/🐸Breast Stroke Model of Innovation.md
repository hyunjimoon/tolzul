## 1. The Resilience and Rhythm of Breaststroke

In uncertain environments, survival demands adaptability over pure efficiency. Breaststroke, while slower than freestyle (another swimming technique), demonstrates remarkable resilience across diverse challenges. In murky waters, it enables navigation while maintaining visibility. During rough conditions, its symmetrical motion provides stability. When energy conservation is crucial, its natural glide phase allows recovery. This adaptability across varied conditions mirrors the challenges of innovation in uncertain markets.

More importantly, breaststroke's three-phase rhythm—wide sweep, focused thrust, glide—provides a profound model for innovation cycles. Unlike freestyle's continuous rotation or butterfly's explosive bursts, breaststroke's distinct phases illuminate how parallel exploration (sweep) creates the conditions for focused scaling (thrust), followed by systematic optimization (glide). This natural progression, refined over centuries of human swimming evolution, offers unique insights into managing innovation under uncertainty.

## 2. Theoretical Foundation: The Breast Stroke Model of Innovation

We establish theoretical foundation for breast stroke model of innovation. Experiment design theory and adjacent possibility theory are two pillars supporting this concept. After understanding the dynamics of breast stroke where sweep fuels thrust and glide enables sweep, we apply this to natural iteration between exploration and exploitation. Our key argument in organizational terms is, parallel exploration during early stages ("nail it") generates unexpected discoveries—spandrels—that become crucial advantages during scaling phases. 

**Experimental Design Theory (EDT)** reveals fundamental error management trade-offs in organizational validation structures. [[📜Heimann93_challenger_org]] demonstrates through NASA's experience how parallel validation prevents catastrophic false negatives while sequential checks protect against dangerous false positives. [[📜gans23_choose(ent, exp)]] extends this insight by showing how firms optimally choose unbalanced experiments - either high-bar or low-bar - rather than balanced approaches, particularly when prior beliefs are optimistic. Like a swimmer's wide sweep creating maximum surface contact, [[📜DOW10_parallel_prototyping]] proves empirically that parallel prototyping leads to better design outcomes and higher self-efficacy by enabling rapid feedback cycles across multiple solution paths. [[📜planning with theory of mind for few shot adaptation in sequential social dilemmas]]

**Adjacent Possibility Theory (APT)** demonstrates how parallel exploration enables unexpected discoveries - spandrels - that become crucial scaling advantages. [[📜Kauffman22_theory_of_adj_possible]] establishes how the world "bubbles forth" creating new possibilities through combinations, with sudden explosive transitions marking key breakthroughs. [[📜Mokyr92_evoldyn_tech]] reinforces this through technological evolution, showing how macroinventions create new "species" that enable subsequent microinventions. Like a swimmer's spreading legs building tension, [[📜Andriani_exaptation_creativity_source]] reveals how discontinuous evolution occurs through functional shifts of existing traits.

The breast stroke's three-phase rhythm reveals how organizations naturally cycle between innovation modes. This mechanism bridges EDT's error management with APT's evolutionary dynamics through coordinated movement patterns:

**Wide Sweep (NAIL IT)**: [[📜Mokyr92_evoldyn_tech]]'s concept of macroinventions demonstrates how radical innovation requires parallel "hopeful monsters" - multiple simultaneous experiments that might create new technological species. [[📜Heimann93_challenger_org]]'s parallel validation prevents false negatives in these experiments, while [[📜Kauffman22_theory_of_adj_possible]]'s adjacent possible expands through simultaneous testing. Like a swimmer's arms creating maximum surface contact, organizations cast wide nets seeking breakthrough innovations that can spawn subsequent microinventions.

**Focused Thrust (SCALE IT)**: This phase embodies [[📜Mokyr92_evoldyn_tech]]'s microinventions - the essential refinements that realize macroinventions' economic potential. [[📜Codini23_bmi_exapt_sme]] shows how firms transform experimental insights into standardized processes, just as the swimmer's powerful thrust converts scattered explorations into directed force. Like Mokyr's observation that "without microinventions, most macroinventions would not be implemented," organizations must convert broad market insights into targeted segments and crystallize flexible systems into efficient standards.

**Glide (SAIL IT)**: The streamlined glide represents the crucial transition period [[📜Mokyr92_evoldyn_tech]] identifies between innovation cycles. Just as evolution is path-dependent - "selection operates on what exists, not what could have been" - organizations must optimize current advantages while positioning for the next wave of macroinventions. Like a swimmer gathering momentum for the next stroke, firms balance system optimization with preparation for future wide sweeps, maintaining the natural rhythm between radical change and incremental improvement.

## 3. Mathematical Model (choose between the two)

### 3.1 baseline model 1

Three components determine optimal sampling behavior when balancing accuracy versus speed:

🎯 Q. Decision Quality:
$Q(\color{orange}{k}, \color{skyblue}{p}\color{white}{)} = \color{skyblue}{p} \color{white}{\cdot (1 - Binomial_{cdf}(}\color{orange}{\frac{k}{2}}, \color{orange}{k}, \color{skyblue}{p} \color{white}{))} + (1-\color{skyblue}{p}\color{white}{)}  \color{white}{\cdot Binomial_{cdf}(}\color{orange}{\frac{k}{2}}, \color{orange}{k}, \color{skyblue}{p} \color{white}{)}$

binomial CDF for P(X ≤ floor(k/2)) where X ~ Binomial(k,p)

Where:
- $\color{orange}{k}$ = number of samples taken
- $\color{skyblue}{p}$ = true probability (uniformly distributed between 0.5 and 1.0)
- Decision quality improves with diminishing returns as samples increase

⏰ T. Time Cost:
$T(\color{orange}{k}, \color{green}{r}\color{white}{)} = \color{green}{r} \color{white}{+}  \color{orange}{k}$

Where:
- $\color{green}{r}$ = 📍action time / 🧠sample time (A2S ratio)
- Higher $\color{green}{r}$ means actions are more expensive relative to sampling
- Total time combines fixed action cost and linear sampling cost

📊 R. Utility Rate:
$R(\color{orange}{k}, \color{green}{r}\color{white}{)} = \frac{Q(\color{orange}{k}, \color{skyblue}{p}\color{white}{)}}{T(\color{orange}{k}, \color{green}{r}\color{white}{)}}$

Optimal number of samples per decision $\color{orange}{k^*} = \underset{\color{orange}{k}}{\color{white}{argmax}} R(\color{orange}{k}, \color{green}{r}\color{white}{)}$

This model reveals several key insights:
1. When $\color{green}{r}$ is high (expensive actions like VC investments), more samples become optimal
2. When $\color{green}{r}$ is low (cheap actions like HFT), fewer samples are optimal
3. Optimal $\color{orange}{k}$ jumps from 1 to odd numbers (3,5,7) to ensure clear majorities
4. "One-and-done" sampling is rational across many realistic $\color{green}{r}$ values
5. No penalty for incorrect decisions makes zero samples optimal when $\color{green}{r}=1$

This explains phenomena like:
- VCs taking extensive samples before major investments (high $\color{green}{r}$)
- HFT firms making rapid decisions with minimal sampling (low $\color{green}{r}$)
- Poor individuals making faster decisions due to high sampling costs
- Desert-dwellers optimally taking fewer samples than city-dwellers

### 3.2 baseline model 2
Three iterative steps characterize how entrepreneurs adapt strategy through learning:

🧠 B. Believing:
$\color{Green}{p_c} \sim Beta(\alpha_c, \beta_c), \color{Purple}{p_r} \sim Beta(\alpha_r, \beta_r)$

Entrepreneurs form beliefs about operational efficiency ($\color{Green}{p_c}$) and market potential ($\color{Purple}{p_r}$) through Beta distributions.

🏎️ P. Predicting:
$\color{Green}{pred_c} = exp(N(\color{Green}{p_c}, \sigma)), \color{Purple}{pred_r} = exp(N(\color{Purple}{p_r}, \sigma))$

These beliefs transform into actionable predictions through log-normal noise (σ).

📍 U. Utility-based action:
$\color{Red}{a^*} = \underset{\color{Red}{a \in \{a_c, a_r\}}}{\arg\max} \: \Delta\color{Red}{U}(\color{Green}{pred_c}, \color{Purple}{pred_r}, \color{Red}{a})$

Optimal action ($\color{Red}{a^*}$) maximizes expected utility gains based on operational ($\color{Green}{pred_c}$) and market ($\color{Purple}{pred_r}$) predictions. This model maps directly onto parallel experimentation in both marketing and operations domains. In marketing, entrepreneurs  test market segments (urban vs rural) and product configurations (roadster vs model s OR model 2 vs cyber truck OR model 2 vs robo taxi (NEED HELP CHOOSING)). Similarly in operations, they test product configurations and production strategies (insource vs outsource). Their performance measures are combinations of total addressable market, market adoption potential, production cost, degree of competition. 

 We design a situation where high and low bar experiment is possible in both production strategy and market segment. The tradeoff between higher mean for lowbar but higher sigma for highbar experiments manifests in three dimensions: (1) Market size dynamics - Model 2 targets larger but saturated market vs Cybertruck/Robotaxi's uncertain but potentially larger new segments; (2) Competitive landscape - Model 2 faces intense competition from other EVs and used vehicles leading to lower margins, while Cybertruck/Robotaxi occupy less competitive niches enabling higher margins despite uncertainty; (3) Unit economics - Model 2 offers predictable but lower per-unit returns vs Cybertruck's higher variance but potentially higher per-unit returns due to premium pricing in novel segment. Market expansion during growth. Tesla's evolution from Roadster to mass market vehicles exemplifies this dual exploration: their early wide-sweeping experiments in both luxury segments and manufacturing approaches generated crucial insights that enabled focused scaling. This parallel exploration, like a swimmer's coordinated arm and leg movements, creates unexpected advantages - spandrels - that become critical during the scaling phase.

### 3.2 Sweep Fuels Thrust - Spandrel Effect

The parallel exploration during wide sweep creates unexpected advantages (spandrels) that become crucial during focused thrust. Tesla's evolution illustrates how this manifests in both high-bar and low-bar experiments. High-bar experiments (like Cybertruck) have higher uncertainty (σ) but potentially larger payoffs through three mechanisms:

1. Market Size: While low-bar experiments (Model 2) target larger existing markets, high-bar experiments explore potentially larger but uncertain new segments
2. Competition: High-bar segments face lower competition, enabling higher margins despite uncertainty
3. User Value: Novel products have higher variance in user satisfaction but potential for breakthrough appeal

This parallel exploration generates spandrels - unexpected insights and capabilities that become competitive advantages during scaling. The higher uncertainty in high-bar experiments (σ ~ exp(σ)) amplifies the value of parallel exploration by enabling simultaneous testing of correlated solution spaces (ρh ~ exp(kh)). Like a swimmer's coordinated arm-leg movements building momentum, these correlated explorations create emergent opportunities that would be missed by sequential testing.

| Phase                                                                         | Swimming Action                                                                                                                                  | Innovation Action                                                                                                                                                  | Nail to scale strategy (靜中動1)                                                                                 |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **Wide Sweep (NAIL IT)** <br>![[Pasted image 20241114081056.png\|100]]        | <font color="#C0A0C0">**Arms:** Sweep wide for maximum surface area</font><br><font color="green">**Legs:** Spread wide, building tension</font> | <font color="#C0A0C0">**Marketing:** Cast wide net for market exploration</font><br><font color="green">**Operations:** Establish flexible, minimal systems</font> | **Spandrel Effect:**<br>Wide exploration creates scaling options<br>Customer insights enable future targeting |
| **Focused Thrust (SCALE IT)** 💥<br>![[Pasted image 20241114081116.png\|100]] | <font color="#C0A0C0">**Arms:** Pull inward forcefully then push forward</font><br><font color="green">**Legs:** Snap together powerfully</font> | <font color="#C0A0C0">**Marketing:** Convert insights to targeted segments</font><br><font color="green">**Operations:** Standardize successful processes</font>   | **Growth Execution:**<br>Leverage nail-stage learnings<br>Transform experiments into standards                |
|                                                                               |                                                                                                                                                  |                                                                                                                                                                    | ⭐️key: spandrel in nail enables thrust in scale                                                               |

The parallel-sequential distinction manifests in two fundamental trade-offs:

exaptation [[🛠️exaptation_spandrel]]:  
- sequential: radio to podcast to recording (new function)
- parallel: environment (no function at the beginning)
**TAP**
```
Sequential: Mt+1 = Mt(1-μ) + α1Mt           [Linear growth]
Parallel:   Mt+1 = Mt(1-μ) + α(2^Mt - Mt - 1) [Explosive growth]
```

**experiment  Management (EDT)**
```
Parallel (Low-bar): 1-∏(fi)  "Only need one winner"
Serial (High-bar): ∏(1-fi)   "Chain as strong as weakest link"
```


(math spandrel in  [[🗄️product2_EDT]], [[🗄️🪶product2_TAP]] waiting for selection)

Three key mechanisms drive parallel advantage:

1. **Uncertainty Handling**
```
σc, σr ~ exp(σ)
predc = exp(N(pc, σc))
```
Higher uncertainty (σ) amplifies value of parallel exploration's broad sampling
Like a swimmer's wide sweep creating surface contact, parallel exploration expands the sampling space. Institutional support (s) amplifies belief formation by enabling broader exploration.

2. **Vertical Correlation**
```
ρh ~ exp(kh)
σc ~ ρh * exp(σ)
```
Market dynamics create correlations across solution spaces, better captured by simultaneous testing
Similar to coordinated arm-leg movement, horizontal correlation (ρh) captures how market dynamics link solution spaces. Higher uncertainty (σ) increases the value of parallel "hopeful monsters."

3. **Institutional herding: Horizontal Correlation**
```
ρv ~ exp(kv)
pc ~ Beta(αc, βc * ρv)
```
Value chain dependencies require clean cross-level samples
Like the transfer of momentum through glide, vertical correlation (ρv) shows how discoveries propagate through organizational levels, enabling spandrels to become competitive advantages.



### 4. Future work: glide enables sweep - ? effect 

| Phase                                                                  | Swimming Action                                                                                                                                  | Innovation Action                                                                                                                                                  | Sail to nail strategy (靜中動2)                                                            |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| **Glide (SAIL IT)**<br>![[Pasted image 20241114081200.png\|100]]       | <font color="#C0A0C0">**Arms:** Streamline forward</font><br><font color="green">**Legs:** Maintain position, prepare for next cycle</font>      | <font color="#C0A0C0">**Marketing:** Maintain market position, focus on loyalty</font><br><font color="green">**Operations:** Optimize existing systems</font>     | **Sustainable Growth:**<br>Maintain advantage<br>Prepare for next cycle i.e. wide sweep |
| **Wide Sweep (NAIL IT)** <br>![[Pasted image 20241114081056.png\|100]] | <font color="#C0A0C0">**Arms:** Sweep wide for maximum surface area</font><br><font color="green">**Legs:** Spread wide, building tension</font> | <font color="#C0A0C0">**Marketing:** Cast wide net for market exploration</font><br><font color="green">**Operations:** Establish flexible, minimal systems</font> | ?                                                                                       |
|                                                                        |                                                                                                                                                  |                                                                                                                                                                    | ⭐️key: glide in sail enables sweep in nail                                              |


---


todo: [[🗄️ 🧩correlation examples]] [[➰loop(market, ops)]], [🧬evolutionary learning/Breaststroke Analogy for Technological Progress cld](https://claude.ai/chat/6fae925c-d0e6-49c6-9add-df18e9279f1d) comparing breaststroke analogy with organizational evolution and Mokyr's theory, using [[🏊‍♀️swim]]