# 🟧 Grow: Model Development

## Melody Section

**🟧0:** News vendor baseline: P* = Cu/(Co+Cu)—classical critical ratio where higher underage cost drives higher optimal quantity, setting foundation for promise vendor extensions.

**🟧⏰:** Promise vendor with reward: (2Cu + V)/2(Co + Cu + V)—adding value V shifts optimal promise upward, with both Cu and V pushing toward boldness while Co moderates.

**🟧↕️:** Nonlinear promise vendor: ln((2Cu + V)/(2Co + V))—logit probability models yield logarithmic formula, creating bounded promises from S-shaped probability curves.

**🟧⏰↕️:** With speed and scale: (1/μ2)ln((2Cu + V·δ^(1/μ2))/(2Co·δ^(1/μ2) + V·δ^(1/μ2)))—temporal (μ1) and spatial (μ2) effects combine, showing speed and expansion are dual strategies.

## Full Section

### 🟧0: News Vendor Baseline - P* = Cu/(Co+Cu)

**Point**: Classical newsvendor with uniform [0,1] demand yields the simple critical ratio P* = Cu/(Co+Cu), establishing the baseline for entrepreneurial promise optimization. **Evidence**: Standard inventory theory result where optimal stocking quantity balances underage cost Cu against overage cost Co under uniform demand distribution. **Explanation**: This baseline formula reveals the fundamental insight: higher underage cost Cu drives higher optimal quantity, while overage cost Co moderates it. For entrepreneurs, this translates directly—when dying unfunded (Cu) is worse than failing funded (Co), promise more boldly. The ratio Cu/(Co+Cu) represents the probability threshold where expected marginal benefit equals expected marginal cost. **Transition**: Adding value creation fundamentally changes this calculus.

### 🟧⏰: Promise Vendor with Reward - (2Cu + V)/2(Co + Cu + V)

**Point**: Adding value V to the temporal model shifts optimal promise upward to P* = (2Cu + V)/2(Co + Cu + V), revealing how value creation amplifies the underage cost effect. **Evidence**: When PF = P and PD = 1-P (linear probabilities), the first-order condition from E[π] = -Co·P·(1-(1-P)) - Cu·(1-P)·(1-P) + V·P·(1-P) yields this closed form. **Explanation**: The formula reveals dual effects: both higher underage cost Cu and value V push toward bolder promises, while overage cost Co moderates them. The factor of 2 emerges from probability derivatives—the marginal effect of promise on expected value involves products of probabilities and their complements. Critically, value V enters the numerator alongside Cu, showing that opportunity magnitude matters as much as opportunity cost. **Transition**: Real-world probabilities rarely follow linear patterns.

![[grow_abc_structure.svg]]

*Figure 3: G Module (Grow) - A-B-C Methods Evolution. This diagram traces the progression from simple to complex promise optimization models. A (left): News vendor baseline with critical ratio P* = Cu/(Cu+Co), where linear probabilities (PF = P, PD = 1-P) yield simple balance between underage and overage costs. B (center): Nonlinear dynamics emerge when S-shaped probability curves replace linear assumptions, yielding logarithmic formula P* = ln((2Cu+V)/(2Co+V)) that naturally bounds extreme promises through saturation effects. C (right): Adding clockspeed (μ1) and scale (μ2) parameters creates the full model where both speed and scale reduce optimal promises—revealing them as substitute strategies for overcoming constraints. The evolution shows how each extension captures additional entrepreneurial reality while maintaining mathematical tractability.*

### 🟧↕️: Nonlinear Promise Vendor - ln((2Cu + V)/(2Co + V))

**Point**: Logit probability models yield the logarithmic optimal promise formula P* = ln((2Cu + V)/(2Co + V)), capturing diminishing returns in real-world responses. **Evidence**: Using PD(P) = e^V/(1+e^V) for delivery probability captures how technical difficulty creates natural bounds—promises can't guarantee delivery beyond physical limits. **Explanation**: The log structure emerges from S-shaped probability curves inherent in logistic models. As promises become extreme, natural resistance emerges—investors become skeptical of outlandish claims, technical challenges mount exponentially. This creates bounded optimal promises based on cost-value ratios, preventing infinite promises even when Cu >> Co. The logarithm ensures that doubling the cost ratio less than doubles the optimal promise, capturing real-world saturation effects. **Transition**: Speed and scale parameters add final complexity.

### 🟧⏰↕️: With Speed and Scale - Complex Interactions

**Point**: Combined temporal (μ1) and spatial (μ2) effects yield P* = (1/μ2)ln((2Cu + V·δ^(1/μ2))/(2Co·δ^(1/μ2) + V·δ^(1/μ2))), revealing how speed and scale interact in promise optimization. **Evidence**: Speed parameter μ1 affects time discounting through δ^(1/μ1) transformations, while scale parameter μ2 affects probability sensitivity as the coefficient in logit models. **Explanation**: This formula synthesizes all entrepreneurial complexities. Faster ventures (higher μ1) face steeper discounting, making future costs less relevant and encouraging bolder promises. Larger scale opportunities (higher μ2) paradoxically need smaller promises—when market potential is obvious, moderate promises suffice. The formula shows these aren't independent effects: spatial expansion (μ2) and temporal acceleration (μ1) are dual strategies for overcoming resource constraints. Both reduce optimal promise levels, suggesting speed and scale are substitutes, not complements. **Transition**: These technical results enable practical prescriptions for entrepreneurs navigating uncertainty.