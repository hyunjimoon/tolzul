Table compares **Sec. 2.1 (Coffee: Peet’s vs Starbucks)**, **Sec. 2.2 (EV: Better Place vs Tesla)**, and **Sec. 2.3 (EV: Toyota vs Tesla)**. Each row references the relevant “🔑table titles” from #🗄️scott to highlight how these examples differ in terms of the Four Axioms, Strategy Compass, key uncertainties, etc.

[[[M1_🗄️ Variable Table]]]

[[scott(🧭🗺️selling entrepreneurial choice-map as Bayes.Entrep)]]

ZAPPOS CASE:
- Founder background: Nick Swinburne had no experience in retail, shoes, or internet
- Initial belief: Selling shoes online when everyone said it was a "loser business" due to fit/try-on needs
- Team formation: Found three others who shared same contrarian belief (co-founders) 
- Test design: "Best Foot Forward experiment"
  * Used all remaining money to buy inventory for rapid turnaround
  * Founders handled customer service directly
  * Goal: "If it doesn't work here, it's never going to work. But if it works here, maybe it'll work in general"
  * Not meant to make money but to validate or kill quickly
- Success criteria: Clear exit signal if experiment fails
- Test outcome: Worked, leading to VC funding from previously skeptical Sequoia

COMMONWEALTH FUSION CASE:
- Context: MIT startup attempting fusion energy breakthrough
- Key choice between two $100M+ experiments:
  1. Build tokamak reactor with current-performance magnets
  2. Focus on developing 20 Tesla magnet first
- Test design considerations:
  * MIT had to allow facility use
  * Same cost and timeframe for both options
  * If magnet works, tokamak design "pretty straightforward"
  * If magnet fails, doesn't necessarily invalidate whole concept
- Institutional context: MIT supported magnet-first approach despite controversy
- Success metric: Technical feasibility must be definitively proven
- Test outcome: Successful magnet test in September 2021 changed industry perspectives


| Hypothesis                                                | Mathematical Form                                                                                          | Key Example                                                                                                                                                                 | criticality,     | phenomena to explain                                                                                                             |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| H1: Higher idea value belief leads to integrated learning | $\text{If }\mu_0=\text{Beta}(a^\phi>b^\phi)\text{ then }EU_2>EU_1$                                         | - Te (Tesla): Started with strong belief in pure EV market ($a^\phi>b^\phi$), chose full implementation despite high costs<br><br>- entrant > incumbent for disruptive tech | critical         | tesla vs better place?                                                                                                           |
| H3:                                                       | $\text{If }\sum(a^\phi+b^\phi)_{\text{incumbent}}\gg\sum(a^\phi+b^\phi)_{\text{entrant}}$ then $EU_1>EU_2$ | To (Toyota): Used existing hybrid knowledge ($\text{high }\sum(a^\phi+b^\phi)$) to test EV market incrementally before full commitment                                      |                  | H2a: Entrants (with higher idea value) prefer integrated learning<br><br>H2b: Incumbents prefer modular over integrated learning |
| H3: Higher test cost ratio needs stronger market signals  | $\uparrow\frac{c^{\phi\theta}}{c^\phi}\implies\uparrow\text{ threshold for }EU_2>EU_1$                     | Juicero: Failed by ignoring high cost ratio ($\frac{c^{\phi\theta}}{c^\phi}\approx\frac{\$120M}{\$100K}$), rushed to implementation without market validation               | opportunity cost |                                                                                                                                  |
| sample size                                               |                                                                                                            |                                                                                                                                                                             |                  |                                                                                                                                  |


what scott found interesting in zappos:
1. ppl entering believ in the opportunity (subjective prior)
2. eric vandensteen (attract of their own - crazy subjective belief - cult) disagreed with others agree with themselves; 
3. experiment (best foot fowrard; “convice us to EXIT” -

---

The Stan code structure suggests we need to revise our hypotheses since it's focused on:
2. Single parameter phi (not theta)
3. Beta prior with mean mu_phi
4. Binomial likelihood for success counts
5. Expected value calculation

More consistent hypotheses would be:

| Hypothesis | Stan-Compatible Form | Example |
|------------|-----------------|---------|
| H1: Prior mean effect | `mu_phi` higher → larger `expected_value` | Te's high prior mean leading to aggressive EV investment |
| H2: Sample size vs cost | Higher `n_obs` needed as `value_multiplier` increases | Juicero needed more extensive testing given high stakes (`value_multiplier`) |
| H3: Success rate threshold | `successes/n_obs` threshold increases with `value_multiplier` | To requiring higher success rate in hybrid tests before EV commitment |


\paragraph{The CFO Interpretation.}
Despite these limitations, the “criticality–fidelity–opportunity cost” perspective remains a practical organizing principle. 
\begin{itemize}
\item \textit{Criticality} ensures you focus on the \emph{most important} unknown. 
\item \textit{Fidelity} gauges how much new insight the test truly provides. 
\item \textit{Opportunity Cost} quantifies the time and resources diverted by that test. 
\end{itemize}
While real ventures involve more nuance than our simplified two-parameter model, 
CFO helps entrepreneurs evaluate whether a low-fidelity but cheap test suffices 
or if a high-fidelity pilot justifies its steeper cost. 
In short, decisions about which experiment to run first—and whether to test idea vs.\ strategy—hinge on balancing these three factors within a Bayesian view of updating beliefs.


## 1) Fundamental Difference (Sec. 2.2 vs Sec. 2.3) in Scott’s Terms

In **Sec. 2.2 (Better Place vs Tesla)**, both players are _entrants_ attempting to deliver new “system innovations” (to use Table 2’s language) for EV technology. This scenario reflects a _Disruptor or Architectural orientation_—no incumbent is dominating, so each entrant is searching for an advantage in a relatively open market structure. According to Scott’s **Four Axioms** (Table 1), there is significant _Uncertainty_ about which new EV approach (battery-swap vs. integrated battery + charger network) will best create and capture value, and both must manage _Noisy Learning_ about consumer acceptance.

By contrast, **Sec. 2.3 (Toyota vs Tesla)** pits an _incumbent_ (Toyota) against a _disruptive entrant_ (Tesla). The market for “electrified vehicles” is partially established (Toyota’s hybrids), so there is _Constraint_ (Axiom 2) from Toyota’s existing capabilities and brand. Meanwhile, Tesla is embracing a _Disruptor strategy_ (Table 2) and invests heavily in _Execution_ on integrated capabilities. The fundamental difference is that Toyota’s large existing assets and brand shape its risk posture and ability to adapt, while Tesla’s path is riskier but can yield a novel architectural advantage. Thus, from Scott’s perspective, the **core contrast** in Sec. 2.3 is _incumbent vs. disruptor strategies_ under more direct head-to-head competition, whereas Sec. 2.2 is _two entrants_ vying to shape a still-emerging EV market.

Below is one **crisp table** aligning each section’s example (Coffee vs. two EV scenarios) with the “🔑table titles” from #🗄️scott. We highlight how each example maps to the Four Axioms, Strategy Compass, key uncertainties, etc.


_Coffee_  
(Peet’s vs. Starbucks) | Two _alternative_ expansions of a high-quality coffee idea:  
– Peet’s invests in artisanal beans  
– Starbucks invests in café model | 1) **Freedom**: More than one path to create value (retail café or premium beans).  
2) **Constraint**: Couldn’t do both at scale simultaneously. | Both lean toward _Value Chain_ or partial _IP_ (they focus on functional resources— sourcing/roasting vs. cafe ops).  
(See “The Partners” in Table 2 if collaborating with supply chain) | Mostly **Epistemic**— uncertain how American consumers adopt new coffee habits. Historical data were scant for “Italian bar” concept. | Each tested, _to some extent_, a pilot. Starbucks did a “pop-up cafe.” Peet’s stuck with careful expansions. Demonstrates how parallel testing clarifies which route is more viable before committing large resources. |
| **Sec. 2.2**  
_EV: entrant vs. entrant_  
(Better Place vs. Tesla) | Two _newcomers_ in the EV space:  
– Better Place tries battery-swap infrastructure  
– Tesla invests in integrated battery + charging network | 1) **Uncertainty**: No clear track record for pure EV approach  
2) **Noisy Learning**: Pilots reveal viability of swap stations vs. integrated superchargers. | Both are closer to _Disruptor_ or _Architectural_ (Table 2). They are exploring “new users, new system innovations.” They differ in **execution** approach: infrastructure vs. integrated. | Primarily **Epistemic**— no established demand data for large-scale EV, plus partial _Aleatoric_ from unknown consumer tastes & battery tech. | Each must “test 2 choose 1” early. Better Place invests heavily in physical swap stations, Tesla invests in battery R&D + superchargers. In parallel, they validate different system designs to see which best scales. |
| **Sec. 2.3**  
_EV: incumbent vs. entrant_  
(Toyota vs. Tesla) | An established automaker with hybrid success (Toyota)  
vs. a pure-EV disruptor (Tesla) | 1) **Constraint**: Toyota’s existing brand, supply chain, & incremental approach.  
2) **Uncertainty**: Whether Tesla’s radical integrated EV can outpace Toyota’s “hybrid-first” stance. | Toyota may lean _Value Chain_ or _IP_ to protect existing capabilities. Tesla uses a _Disruptor_ strategy, investing in integrated capabilities for new customers. | Mixed **Epistemic** and **Aleatoric**. Toyota has partial data from hybrids. Tesla faces unknown scale-up and competitive response. | Toyota can do “learn while scaling hybrids.” Tesla “goes all-in” on pure EV. Each has to weigh cost of large pilot expansions. Testing multiple approaches is restricted for Toyota by legacy constraints, while Tesla’s approach is a high-stakes single path. |

**Key Takeaway**:

- **Sec. 2.1**: Two _alternative expansions_ from the _same idea_ (quality coffee).
    
- **Sec. 2.2**: Two _entrant_ startups racing to define a new EV approach.
    
- **Sec. 2.3**: Incumbent (Toyota) vs. disruptor (Tesla) contending with legacy constraints and radically new system design.