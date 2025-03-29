
| Section                | 🧍‍♀️ Agent Question                                     | 🌏 Context                                                                            | 🧭 Method/Model                                                                                                                                                                                 | 🗺️ Key Finding                                                                                                                      |
| ---------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Model Setup            | When should an investor exit a deteriorating project?    | Investment project with uncertain returns following Brownian motion                   | • Brownian motion with drift μ and volatility σ²<br>• Drift switches from μH > 0 to μL < 0 at random exponential time T<br>• Only observable variable is cumulative return Xt = ∫₀ᵗ μ dt + B(t) | Optimal to exit when posterior probability of being in high state falls below threshold p*                                           |
| Optimal Stopping       | How to determine the optimal stopping threshold?         | Need to balance Type I error (quitting too early) vs Type II error (staying too late) | • Derives stochastic differential equation for posterior probability:<br>dPt = -ηPt dt + κPt(1-Pt) dB̃t<br>• Uses smooth pasting conditions                                                     | p* given implicitly by integral equation involving model parameters                                                                  |
| Key Parameters         | What drives optimal exit timing?                         | Tradeoff between information quality and state transition speed                       | • η: rate of regime change<br>• σ: noise in returns<br>• μH: high state drift<br>• μL: low state drift                                                                                          | • Higher η or σ → higher p* (more conservative)<br>• Higher μH → lower p* (more aggressive)<br>• Larger μH-μL gap → easier detection |
| Mathematical Core      | What is the value function?                              | Dynamic optimization under uncertainty                                                | Value function V(p) satisfies ODE:<br>κ²/2 p²(1-p)²V''(p) - ηpV'(p) + (μH-μL)p + μL = 0<br>with boundary conditions:<br>V(p*) = 0, V'(p*) = 0, V'(1) = μH/η                                     | Value approaches μHp₀/η as μL → ∞ (perfect information case)                                                                         |
| Practical Implications | How quickly should managers respond to negative signals? | Historical examples show technology transitions can be slow or fast                   | • Models profit stream as key information source<br>• Uses posterior probability threshold rule                                                                                                 | Exit threshold depends on:<br>• Information quality<br>• Transition speed<br>• Potential losses<br>• Potential gains                 |

Key Equations:
1. Return Process: dXt = μt dt + σdBt
2. State Transition: μt = μH → μL at exponential time T
3. Posterior Process: dPt = -ηPt dt + κPt(1-Pt) dB̃t
4. Value Function ODE: κ²/2 p²(1-p)²V''(p) - ηpV'(p) + (μH-μL)p + μL = 0

Intuition:
- Higher noise (σ) or faster transitions (η) require more conservative exit thresholds
- Larger profit differential (μH-μL) makes optimal timing easier to detect
- Value approaches perfect information case as low state becomes very negative
- Optimal policy balances risks of premature exit vs delayed exit

[[john_chen]]