# hyper-meritocratic selecting for wealth not talent

Do entrepreneurial ecosystems select for talent or wealth? We extend the promise vendor framework to reveal how society's selection mechanism systematically transforms capital access into apparent merit. The model's core insight lies in the integral p(D|φ) = ∫ p(F|φ) p(D|φ, F) dF, which shows delivery probability inseparably combines funding access with execution ability. Through comparative statics, we demonstrate that two founders with identical promises φ and equal execution ability p(D|φ,F) achieve vastly different outcomes based solely on their initial p(F|φ)—itself determined by parental wealth, network effects, and social signals. Intuitively, ivy league dropouts with wealthy parents exhibit higher "success rates" than community college graduates, not through superior execution but through funding probability differentials. The math shows successful founders aren't necessarily the most talented—they're the ones who started with money. The system transforms 'my parents are rich' into 'I'm a visionary.' What looks like merit-based selection is actually wealth-based selection in mathematical disguise.

**Promise: Revolutionary AI startup (same φ for both founders)**

| **Component**         | **Ivy league Dropout (Rich Parents)**                                       | **Community College Genius (Poor)**                                            |
| --------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Funding Scenarios** | F₀ = $0<br>F₁ = $500K seed<br>F₂ = $5M Series A                             | F₀ = $0<br>F₁ = $500K seed<br>F₂ = $5M Series A                                |
| **p(F\|φ)**           | p(F₀\|φ) = 0.1<br>p(F₁\|φ) = 0.3<br>p(F₂\|φ) = 0.6                          | p(F₀\|φ) = 0.7<br>p(F₁\|φ) = 0.2<br>p(F₂\|φ) = 0.1                             |
| **p(D\|φ,F)**         | p(D\|φ,F₀) = 0.3 (family money)<br>p(D\|φ,F₁) = 0.5<br>p(D\|φ,F₂) = 0.7     | p(D\|φ,F₀) = 0.05 (no resources)<br>p(D\|φ,F₁) = 0.6<br>p(D\|φ,F₂) = 0.8       |
| **Calculation**       | p(D\|φ) = 0.1×0.3 + 0.3×0.5 + 0.6×0.7<br>= 0.03 + 0.15 + 0.42<br>= **0.60** | p(D\|φ) = 0.7×0.05 + 0.2×0.6 + 0.1×0.8<br>= 0.035 + 0.12 + 0.08<br>= **0.235** |

- Same promise φ
- Similar or better execution ability when funded (genius has higher p(D|φ,F₂))
- But 2.5x difference in delivery probability due to funding access

**The Degeneracy:** Society observes 60% vs 23.5% success rates and concludes the wealthy dropout is "2.5x better" 
                       - but it's mostly just p(F|φ) differences driven by parental wealth, network effects, and signaling.

# principal-agent between present-self and future-self

| **Dimension**       | **Traditional Principal-Agent**                                | **Promise Vendor**                                                                                                                                                                     |
| ------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Who's in charge** | Investor (Principal) → Founder (Agent)                         | Present-self (Principal) → Future-self (Agent)                                                                                                                                         |
| **Degeneracy**      | Contribution of agent's labor can't be inferred from delivered | Contribution of agent's labor P(Deliver\|Funded, φ) can't be inferred from delivered P(Deliver\|φ)                                                                                     |
| **What's Hidden**   | How hard agent works                                           | How hard agent works on P(D\|F,φ) to increase P(D\|φ)<br><br>$P(Deliver\|φ) = \int \underbrace{P(Funded\|φ)}_{\text{capital}} \; \underbrace{P(Deliver\|Funded, φ)}_{\text{labor}} dF$ |
|                     |                                                                |                                                                                                                                                                                        |
