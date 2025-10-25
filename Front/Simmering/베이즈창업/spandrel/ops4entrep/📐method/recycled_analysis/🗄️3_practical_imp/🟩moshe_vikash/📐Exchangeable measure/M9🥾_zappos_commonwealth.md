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


# Testing Strategy Hypotheses

| Hypothesis                                                                                                                                     | Mathematical Form                                                               | Key Example                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| H1: Higher correlation between market and implementation uncertainties increases the relative value of integrated testing over modular testing | ρ(φ,θ) ↑ → (ΔEU₂ - ΔEU₁) ↑                                                      | Commonwealth Fusion: High ρ(φ,θ) due to magnet performance directly determining market viability led to choice of integrated testing |
| H2: Resource efficiency of testing strategy depends on the ratio of statistical bias costs to opportunity costs                                | ValidStatBiasCost(φ,N)/OpportunityCost(θ,φ,N,M) → min                           | Zappos: Low ValidStatBiasCost through small inventory test with clear exit criteria minimized OpportunityCost                        |
| H3: The optimal testing strategy minimizes the sum of verification and validation costs given resource constraints                             | min[ValidApproxBiasCost(φ) + VerifConvgBiasCost(θ\|φ,M)] s.t. resource ≥ c_test | Tesla: High VerifConvgBiasCost from dispersed collaboration (8-week cycles) forced restructuring to integrated testing               |

*Variables:*
- φ: Market potential
- θ: Implementation effectiveness
- ρ(φ,θ): Correlation between market and implementation uncertainties
- N: Sample size
- M: Testing time/resources
- c_test: Testing cost (cφ for modular, cφθ for integrated)