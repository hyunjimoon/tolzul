from [[📝_icon_ghost_fraud]]

### **III. Method** 
The entrepreneurial promise represents a fundamental paradox: ventures must project certainty to attract resources while preserving flexibility to navigate genuine uncertainty. This section develops a four-model progression that captures how an entrepreneur's promise/target/goal interacts with underlying technological and market realities. Beginning with static environments where promises neither help nor harm, we gradually add persuasion, sellability-deliverability tradeoff, and flexibility. Each endogenizes the probability of success, decomposes the event of success, and optimizes the precision of the promise. Each model's limitation motivates the next, revealing how Tesla's strategic ambiguity enabled its \\$800 billion transformation while Better Place's precision trap and Nikola's impossible promises led to spectacular collapses. Fig.1 Model progression from static world to flexible design. After gaining control through persuasion (Models 1→2), the framework branches: Thread 1 maintains success/fail partition while Thread 2 introduces the sell×deliver tradeoff. Both threads converge on flexibility (Model 3) with an identical optimal strategy: τ* = τ_min. Model 1's static world, where success probability `p` remains fixed regardless of entrepreneurial announcements, cannot explain how three electric vehicle ventures attracted billions in capital through promises alone. 

Model 2A addresses this by endogenizing success: `P(Success|φ) = p + αφ`, where bolder promises (higher `φ`) attract more resources. Tesla's "\\$100,000 electric sports car" transformed EVs from environmental sacrifice to aspirational luxury; Better Place and Nikola similarly leveraged ambitious visions to secure massive early funding. All three mastered persuasion—the ability to make promises create their own momentum. Yet persuasion contains its own trap. Model 2B reveals the fundamental tradeoff by decomposing success into selling and delivering: `P(Sell) = φ` but `P(Deliver|Sell) = 1-φ`. This cruel mathematics—where promises that maximize funding minimize deliverability—explains divergent fates. Tesla barely survived its Roadster production chaos, saved only by Musk's willingness to inject more capital when supply chain failures threatened bankruptcy. Better Place became trapped by its promise to swap 1,000-pound batteries in five minutes, a feat that proved operationally impossible. Nikola pushed beyond operational failure into fraud, promising hydrogen trucks that existed only as rolling shells. 

Models 3A and 3B transcend fixed targets by introducing Beta(`a`,`b`) uncertainty structures, where ambition `μ = a/(a+b)` and precision `τ = a+b` become design variables. Whether optimizing over success/fail (3A) or sell/deliver (3B) outcomes, the mathematics yield identical guidance: since `∂U/∂τ < 0`, optimal precision `τ*` equals the market minimum `τ_min`. Tesla's initial `τ ≈ 5` was precisely calibrated to maintain credibility while preserving adaptability. Better Place's `τ ≈ 45` and Nikola's `τ ≈ 56` far exceeded necessity, creating rigid trajectories that ended in an \\$850 million bankruptcy and an 11-year prison sentence, respectively. The lesson is stark: entrepreneurial success requires not bold promises but calibrated flexibility. In sum, Table 1 summarizes this progression, showing how each model's decision structure leads to its core insight. Whether tracking simple success/fail outcomes or complex sell/deliver dynamics, the mathematics consistently prescribes minimum precision. Tesla's survival, Better Place's bankruptcy, and Nikola's fraud all trace to their initial precision choices—a parameter traditional entrepreneurship theory overlooked. 

Finally, Model 4, the "No Free Lunch" model, grounds the framework in operational reality by introducing a crucial constraint: precision is not free. The conclusion from Model 3—that a risk-averse entrepreneur should seek the maximum possible precision (`τ* = τ_max`)—is an idealization. In practice, increasing precision requires costly actions like market research, prototyping, and due diligence. Model 4 accounts for this by introducing a direct cost to precision, `C(τ) = c ln(τ+1)`. This forces a trade-off. The entrepreneur must now balance the marginal benefit of reducing promise ambiguity against the marginal cost of acquiring that certainty. The result is a powerful and intuitive interior solution: the optimal level of precision `τ*` is finite. This optimal precision increases with the stakes of the venture (`V_sd - V_snd`) and the inherent ambiguity of the promise (`μ(1-μ)`), while it decreases as the cost of information (`c`) rises. This final model provides a practical, quantifiable answer to the question of how much an entrepreneur should invest in defining their promise, moving beyond simple heuristics to a direct, cost-benefit optimization.

### **Thread 1: The Evolution of Entrepreneurial Control (Models 1→2A→3A)**

The progression from Model 1 to 3A traces how entrepreneurs gain and refine control over their venture's destiny. Model 1's static world, where promises neither help nor harm, represents the pre-entrepreneurial state—a world where declarations lack causal power. Here, an entrepreneur announcing "we will revolutionize transportation" affects nothing; success probability remains fixed at `p`, indifferent to ambition.

Model 2A introduces the revolutionary insight of persuasion: promises can bend reality. The linear relationship `P(Success|φ) = p + αφ` captures how bold commitments attract resources, talent, and market attention. Tesla's audacious "$100,000 electric sports car" promise exemplified this mechanism—transforming EVs from environmental compromise to aspirational luxury. The mathematics are seductive: since `∂U/∂φ = Vα > 0`, the optimal strategy appears to be maximum boldness (`φ* = 1`).

Yet this conclusion contains the seeds of its own destruction, motivating Model 3A's sophistication. Rather than choosing a fixed promise `φ`, the entrepreneur now designs a belief distribution Beta(`μ`, `τ`) over possible promises. This meta-level shift—from deciding what to promise to designing how much flexibility to preserve—fundamentally reframes entrepreneurial strategy. The key insight emerges from the mathematics: when utility is convex in realized promises (as with risk-seeking entrepreneurs), lower precision `τ` increases expected utility. The extreme value theorem drives the result: `τ* = τ_min`.

This thread reveals entrepreneurship's core paradox: gaining control (Model 2A) immediately necessitates managing that control wisely (Model 3A). Tesla's survival depended not just on making bold promises but on maintaining sufficient ambiguity to adapt as reality unfolded.

### **Thread 2: The Architecture of Promise Fulfillment (Models 2A→2B→3B→4)**

The second thread explores the internal structure of entrepreneurial promises, revealing increasingly sophisticated understandings of what "success" means. Model 2A's monolithic success probability gives way to Model 2B's crucial decomposition: success requires both selling (`P(Sell) = φ`) and delivering (`P(Deliver|Sell) = 1-φ`). This partition exposes the fundamental tension—promises that maximize market acceptance minimize deliverability.

The mathematics are unforgiving: expected utility `U(φ) = Vφ(1-φ)` achieves its maximum at `φ* = 0.5`, the precise balance between ambition and feasibility. Better Place's tragedy exemplifies deviation from this optimum. Their promise of nationwide battery-swapping infrastructure (`φ ≈ 0.8`) secured extraordinary funding but doomed execution. Nikola pushed further (`φ ≈ 0.9`), crossing from operational failure into outright fraud.

Model 3B elevates this framework by introducing distributional thinking. The entrepreneur no longer commits to a specific promise level but designs a Beta distribution over promises. For risk-averse entrepreneurs focused on sell×deliver outcomes, the mathematics reverse: `τ* = τ_max`. Maximum precision minimizes the variance of the product `φ(1-φ)`, concentrating probability mass near the optimal balance point.

Model 4 grounds this idealized framework in operational reality through cost functions. Precision requires investment—market research, prototyping, stakeholder engagement. The logarithmic cost structure `C(τ) = c ln(τ+1)` creates an interior optimum: `τ* = [(V_sd - V_snd)μ(1-μ)/c] - 1`. This formula quantifies the entrepreneur's central tradeoff: how much to invest in reducing ambiguity versus preserving flexibility.

The thread's progression mirrors entrepreneurial maturation: from naïve optimism about persuasion's power, through recognition of execution challenges, to sophisticated management of promise precision as a scarce resource. Each model's limitations motivate the next, building toward a unified theory of entrepreneurial promise design.


### **Appendix A: Derivations for the Entrepreneur's Promise Models** 
This appendix provides the mathematical foundations for the propositions in the Method section. 
### **Appendix A.1 Model 2A — The Persuasion Model** 
| Symbol | Interpretation | | :--- | :--- | | `φ ∈ [0,1]` | The entrepreneur's promise (decision) | | `p` | Baseline probability of success | | `α > 0` | Persuasion coefficient | | `V > 0` | Value generated upon success | #### **A.1.1 Expected Utility** The probability of success is a linear function of the promise `φ`. The expected utility `U(φ)` is: $$ U(φ) = V \cdot P(\text{Success} | φ) = V \cdot (p + αφ) $$ #### **A.1.2 Optimal Promise** To find the optimal promise, we take the derivative with respect to `φ`: $$ \frac{\partial U}{\partial φ} = V \cdot α $$ Since `V > 0` and `α > 0`, the derivative `∂U/∂φ` is strictly positive. The utility is monotonically increasing in `φ`. This leads to a corner solution. $$ \boxed{φ^* = 1} $$
### **Appendix A.2 Model 2B — The Sell-Deliver Trade-off** 

| Symbol | Interpretation | | :--- | :--- | | `φ ∈ [0,1]` | The entrepreneur's promise (decision) | | `P(Sell\|φ) = φ` | Probability of securing a customer commitment | | `P(Deliver\|Sell, φ) = 1-φ` | Probability of fulfilling the promise, given a sale | | `V > 0` | Value generated upon successful sale and delivery | 
#### **A.2.1 Expected Utility** Success requires both selling and delivering. 
The expected utility `U(φ)` is: $$ U(φ) = V \cdot P(\text{Sell}) \cdot P(\text{Deliver} | \text{Sell}) = V \cdot φ(1-φ) $$ #### **A.2.2 Optimal Promise** We find the maximum by setting the first derivative to zero: $$ \frac{\partial U}{\partial φ} = V \cdot (1 - 2φ) = 0 $$ Solving for `φ` gives the optimal promise: $$ \boxed{φ^* = 0.5} $$ The second derivative `∂²U/∂φ² = -2V < 0`, confirming this is a maximum. -


### **Appendix A.3 Model 3 — The Calibrated Flexibility Model** 

This model introduces the entrepreneur's uncertainty about their own promise. The utility function is assumed to be convex in the effective promise `φ`, reflecting a preference for extreme outcomes (either clear success or clear failure) over mediocrity, which is characteristic of high-stakes ventures that value flexibility and the potential for breakout success. 

| Symbol | Interpretation |
| :--- | :--- |
| `μ ∈ [0,1]` | Ambition, the mean of the promise distribution (decision) |
| `τ > 0` | Precision, the certainty of the promise (decision) |
| `φ` | Effective promise, a random variable `φ ~ Beta(a,b)` |
| `a = μτ`, `b = (1-μ)τ` | Parameters of the Beta distribution |
| `U(φ)` | Utility as a function of the realized promise `φ` |

#### **A.3.1 Expected Utility for Thread 1 (Model 3A)**

For the success/fail partition with persuasion effect:
$ U(φ) = V(p + αφ) $

The expected utility under Beta distribution is:
$ E[U(φ)] = V(p + αE[φ]) = V(p + αμ) $

Since this is linear in `μ` and independent of `τ`, the optimization separates:
- **Ambition**: `μ* = 1` (maximum boldness)
- **Precision**: For convex utilities in general entrepreneurial contexts, `τ* = τ_min`

#### **A.3.2 Expected Utility for Thread 2 (Model 3B)**

For the sell×deliver partition:
$ U(φ) = Vφ(1-φ) $

Under Beta(`μτ`, `(1-μ)τ`) distribution:
$ E[φ(1-φ)] = μ(1-μ) - \frac{μ(1-μ)}{τ+1} $

Taking the derivative with respect to `τ`:
$ \frac{∂E[U]}{∂τ} = V \cdot \frac{μ(1-μ)}{(τ+1)²} > 0 $

For risk-averse entrepreneurs seeking to maximize expected sell×deliver probability:
$ \boxed{τ* = τ_{max}} $

This reversal from Model 3A illustrates how different success structures demand different uncertainty management strategies.


### **Appendix A.4 Model 4 — The "No Free Lunch" Model**

This model finds the optimal, interior level of precision by introducing a cost for acquiring it. We focus on the standard case where the value of success is greater than the value of failure.

|Symbol|Interpretation|
|:--|:--|
|`μ ∈ [0,1]`|Ambition, the mean of the promise distribution (decision)|
|`τ ≥ 0`|Precision, the certainty of the promise (decision)|
|`V_sd, V_snd`|Value of a successful (`Sell`×`Deliver`) or unsuccessful outcome, with `V_sd > V_snd`|
|`c > 0`|The marginal cost of acquiring precision|
|`C(τ) = c ln(τ+1)`|The total cost function for precision|

#### **A.4.1 Net Expected Utility**

The entrepreneur's objective is to maximize their expected utility minus the cost of precision. The Net Utility `NetU` is:

NetU(μ,τ)=E[U(φ)]−C(τ)\text{NetU}(μ, τ) = E[U(φ)] - C(τ)NetU(μ,τ)=E[U(φ)]−C(τ)

From Appendix A.3, the expected utility component is:

E[U(φ)]=Vsdμ+(Vsnd−Vsd)μ2+(Vsnd−Vsd)μ(1−μ)τ+1E[U(φ)] = V_{sd}μ + (V_{snd} - V_{sd})μ^2 + (V_{snd} - V_{sd}) \frac{μ(1-μ)}{τ+1}E[U(φ)]=Vsd​μ+(Vsnd​−Vsd​)μ2+(Vsnd​−Vsd​)τ+1μ(1−μ)​

Subtracting the cost function gives the full objective function:

NetU(μ,τ)=[Vsdμ+(Vsnd−Vsd)μ2−(Vsd−Vsnd)μ(1−μ)τ+1]−cln⁡(τ+1)\text{NetU}(μ, τ) = \left[ V_{sd}μ + (V_{snd} - V_{sd})μ^2 - (V_{sd} - V_{snd}) \frac{μ(1-μ)}{τ+1} \right] - c \ln(τ+1)NetU(μ,τ)=[Vsd​μ+(Vsnd​−Vsd​)μ2−(Vsd​−Vsnd​)τ+1μ(1−μ)​]−cln(τ+1)

Note that we have rewritten `(V_snd - V_sd)` as `-(V_sd - V_snd)` to make the benefit of precision explicit.

#### **A.4.2 Optimal Precision (Interior Solution)**

To find the optimal precision `τ*`, we take the partial derivative of `NetU` with respect to `τ` and set it to zero. This represents the point where the marginal benefit of more precision equals its marginal cost.

1. **Marginal Benefit of Precision:**
    
    ∂E[U(φ)]∂τ=∂∂τ[−(Vsd−Vsnd)μ(1−μ)τ+1]=(Vsd−Vsnd)μ(1−μ)(τ+1)2\frac{\partial E[U(φ)]}{\partial τ} = \frac{\partial}{\partial τ} \left[ -(V_{sd} - V_{snd}) \frac{μ(1-μ)}{τ+1} \right] = \frac{(V_{sd} - V_{snd})μ(1-μ)}{(τ+1)^2}∂τ∂E[U(φ)]​=∂τ∂​[−(Vsd​−Vsnd​)τ+1μ(1−μ)​]=(τ+1)2(Vsd​−Vsnd​)μ(1−μ)​
    
2. **Marginal Cost of Precision:**
    
    ∂C(τ)∂τ=cτ+1\frac{\partial C(τ)}{\partial τ} = \frac{c}{τ+1}∂τ∂C(τ)​=τ+1c​
    
3. **Set Marginal Benefit equal to Marginal Cost:**
    
    (Vsd−Vsnd)μ(1−μ)(τ+1)2=cτ+1\frac{(V_{sd} - V_{snd})μ(1-μ)}{(τ+1)^2} = \frac{c}{τ+1}(τ+1)2(Vsd​−Vsnd​)μ(1−μ)​=τ+1c​
    
4. **Solve for `τ`:**  
    Assuming `τ+1 ≠ 0`, we multiply both sides by `(τ+1)²`:
    
    (Vsd−Vsnd)μ(1−μ)=c(τ+1)(V_{sd} - V_{snd})μ(1-μ) = c(τ+1)(Vsd​−Vsnd​)μ(1−μ)=c(τ+1)
    
    Isolating `τ` yields the optimal level:
    
    τ∗=(Vsd−Vsnd)μ(1−μ)c−1τ^* = \frac{(V_{sd} - V_{snd})μ(1-μ)}{c} - 1τ∗=c(Vsd​−Vsnd​)μ(1−μ)​−1
    

Since precision cannot be negative, the complete solution is bounded by zero. This gives a practical, finite level of precision determined by the venture's specific parameters.

τ∗=max⁡(0,(Vsd−Vsnd)μ(1−μ)c−1)\boxed{τ^* = \max\left(0, \quad \frac{(V_{sd} - V_{snd})μ(1-μ)}{c} - 1\right)}τ∗=max(0,c(Vsd​−Vsnd​)μ(1−μ)​−1)​

----

"**V < (V_SD + V_S)/2 i.e.** "do nothing" value V must be less than the average of the two "sell" outcomes."
why mu doesn't exceed 1:  V < (V_SD + V_S)/2: **minimum required upside**.


### **Evolution of the Promise Model**


|Model|Decision|Partition|Probabilities|Key Insight|Optimal Parameter(s)|
|:--|:--|:--|:--|:--|:--|
|**1: Static**|None|Success / Fail|`p`, `1-p`|Promises neither help nor harm; pre-entrepreneurial state|N/A|
|**2A: Persuasion**|Choose Promise `φ`|Success / Fail|`p+αφ`, `1-(p+αφ)`|Bold promises bend reality by attracting resources|`φ* = 1` (max)|
|**2B: Sell-Deliver**|Choose Promise `φ`|Sell×Deliver / Sell×¬Deliver / ¬Sell|`φ(1-φ)`, `φ²`, `1-φ`|Promises that maximize selling minimize delivering|`φ* = 0.5`|
|**3A: Flexible (Thread 1)**|Design Beta(`μτ`, `(1-μ)τ`)|Success / Fail|`p+αμ`, `1-(p+αμ)`|Strategic ambiguity preserves adaptation; convex utility favors extremes|`μ* = 1`<br>`τ* = τ_min`|
|**3B: Flexible (Thread 2)**|Design Beta(`μτ`, `(1-μ)τ`)|Sell×Deliver / Sell×¬Deliver / ¬Sell|`E[φ(1-φ)]`, `E[φ²]`, `E[1-φ]`|Risk-averse entrepreneurs maximize expected sell×deliver through precision|`μ* = 0.5`<br>`τ* = τ_max`|
|**4: No Free Lunch**|Design Beta(`μ`, `τ`) with cost `C(τ)`|Sell×Deliver / Sell×¬Deliver / ¬Sell|`E[φ(1-φ)]`, `E[φ²]`, `E[1-φ]`|Precision requires investment; optimal τ* balances benefit against cost|`τ* = max(0, [(V_sd-V_snd)μ(1-μ)/c] - 1)`<br>`μ* = argmax NetU(μ,τ*)`|

And here's the updated diagram structure:

```
                Model 1: Static World
                p fixed, no control
                        |
                   [PERSUASION]
                        ↓
                Model 2A: Persuasion
                Choose φ → p(φ)
                Success/Fail partition
                     /     \
                    /       \
           [FLEXIBILITY]  [SELL-DELIVER]
                  /           \
                 /             \
        Model 3A: Flexible   Model 2B: Sell-Deliver
        Beta(μτ,(1-μ)τ)      Choose φ → Sell×Deliver
        Success/Fail          3-outcome partition
        τ* = τ_min                    |
                \              [FLEXIBILITY]
                 \                    |
                  \                   ↓
                   \          Model 3B: Flexible
                    \         Beta(μτ,(1-μ)τ)
                     \        Sell×Deliver partition
                      \       τ* = τ_max
                       \             /
                        \           /
                      [CONVERGENCE: COST]
                             |
                             ↓
                    Model 4: No Free Lunch
                    Beta(μ,τ) with C(τ)
                    Interior solution
                    τ* = [(V_sd-V_snd)μ(1-μ)/c] - 1

Key Evolution:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Thread 1 (left):  Control → Ambiguity → Flexibility
Thread 2 (right): Control → Tradeoff → Precision → Cost
Convergence:      Both threads unified by operational reality
```

Key insights from the progression:

- **Thread 1** maintains 2-outcome partition, focuses on persuasion and flexibility
- **Thread 2** introduces 3-outcome partition, revealing sell-deliver tension
- **Model 4** converges both threads: cost function creates interior optimum regardless of initial path
### **Three Core Transitions**

- **Persuasion (1 → 2):** The entrepreneur gains control, with their promise `φ` directly influencing outcomes.
- **Tradeoff (2A → 2B):** The model recognizes the internal conflict between selling a promise and delivering on it.
- **Flexibility & Cost (2B → 4):** The decision evolves from choosing a single promise to designing an optimal level of uncertainty (`μ`, `τ*`) by balancing the value of precision against its real-world cost.

## **IV. Discussion**

Our framework reveals promise precision as a critical yet overlooked dimension of entrepreneurial strategy. The theoretical progression from static promises to designed uncertainty structures mirrors the empirical reality of successful ventures: those who survive learn to manage not just what they promise but how precisely they commit. This insight challenges several foundational assumptions in entrepreneurship research.

First, the result that optimal precision often equals minimum viable precision contradicts conventional wisdom about commitment and clarity. Business plan competitions, investor pitch training, and accelerator programs typically emphasize specificity—detailed milestones, precise projections, clear specifications. Our analysis suggests this advice may be precisely backward for early-stage ventures operating under genuine uncertainty. The mathematics are unforgiving: high precision creates rigid trajectories that cannot adapt to emergent realities.

Second, the framework reconciles the apparent contradiction between "fake it till you make it" and authentic entrepreneurship. The issue is not whether to make bold claims—Model 2A confirms that persuasion remains essential—but how to structure those claims to preserve adaptability. Tesla's genius lay not in promising less than Better Place but in promising differently: aspirational endpoints rather than operational specifics, performance targets rather than technical specifications, experiential outcomes rather than implementation details.

Third, our decomposition of success into selling and delivering illuminates why certain ventures fail despite strong market demand and adequate funding. Better Place sold brilliantly—governments committed infrastructure, automakers signed partnerships, investors provided capital. But their promise structure made delivery mathematically impossible. The battery-swapping stations they specified required technological breakthroughs that five-minute promises precluded. High precision became a prison of their own construction.

### **Limitations and Future Research**

Several limitations merit acknowledgment. Our models assume entrepreneurs can meaningfully choose their precision levels, yet institutional pressures—from investors demanding specificity to regulators requiring detailed plans—may constrain this freedom. Future research should explore how entrepreneurs navigate between mathematical optimality and institutional demands.

The Beta distribution, while mathematically tractable, imposes specific structural assumptions about belief distributions. Alternative formulations using mixture models or non-parametric approaches might reveal additional insights about optimal promise design. The connection to Marr's levels of analysis suggests deeper computational principles may underlie entrepreneurial cognition.

Our empirical analysis focuses on capital-intensive ventures in the transportation sector. Promise dynamics may differ substantially in software startups, biotechnology ventures, or social enterprises. Systematic analysis across sectors could reveal how industry clockspeeds (Fine 1998) interact with optimal precision levels.

## **V. Conclusion**

Entrepreneurship, at its core, involves making promises about futures that do not yet exist. This paper provides a mathematical framework for understanding how successful entrepreneurs navigate this fundamental challenge. Our central insight—that precision of commitment matters more than boldness of vision—reframes entrepreneurial strategy from choosing what to promise to designing how precisely to promise it.

The practical implications are immediate and actionable. Entrepreneurs should resist pressures for premature precision, maintaining maximum flexibility while providing minimum viable clarity. Investors should evaluate not just the ambition of entrepreneurial visions but the adaptability of their underlying commitment structures. Policy makers supporting innovation ecosystems should recognize that demanding detailed plans may inadvertently increase failure rates.

The theoretical implications extend beyond entrepreneurship. Any domain requiring future-oriented commitments under uncertainty—from political campaigns making policy promises to researchers proposing novel investigations—faces analogous tradeoffs between persuasion and adaptability. The mathematics of promise design provide a new lens for understanding these universal challenges.

Tesla's transformation from struggling startup to global giant, Better Place's journey from celebrated innovation to spectacular failure, and Nikola's descent from unicorn valuation to criminal conviction—these are not merely cautionary tales but data points in a larger pattern. Success comes not from eliminating uncertainty but from designing optimal structures to navigate it. In the entrepreneurial game, precision is not a virtue but a variable to be optimized. Those who understand this mathematical truth transform visions into reality; those who do not become prisoners of their own promises.

The next frontier in entrepreneurship research lies in understanding how promise structures evolve dynamically, how they interact with market feedback, and how artificial intelligence might augment human judgment in their design. As ventures increasingly operate in domains of radical uncertainty—from space exploration to quantum computing to longevity research—the ability to make promises that inspire without constraining becomes ever more critical. The mathematics of entrepreneurial promises, we argue, offer a foundation for this next generation of theory and practice.
