# 🗄️Table 1: Newsvendor ⇄ Promise-Vendor Crosswalk

| Dimension | Newsvendor Model | → | Promise-Vendor Model |
|-----------|------------------|---|---------------------|
| **Core Question** | How much inventory Q to stock given uncertain demand D? | ⟳ | What promise level P to declare given uncertain delivery capability? |
| **Decision Variable** | Quantity Q (continuous, bounded by capacity) | ⟳ | Promise level P (affects both Pc(q) and Pr(q)) |
| **Uncertainty Source** | Demand D ~ F(x) (exogenous, historically observable) | ⟳ | Delivery capability (endogenous, future-dependent) |
| **Objective Function** | Min E[Cost] = Cu·E[(D-Q)+] + Co·E[(Q-D)+] | ⟳ | Max E[π] = Pc(q)·Pr(q)·V - Pc(q)·[1-Pr(q)]·Co - [1-Pc(q)]·Pr(q)·Cu |
| **⏰ Time** | Past → Present information flow | ⟳ | Future → Present information flow |
|  | Learn from historical demand patterns | ⟳ | Share tomorrow's vision to attract today's resources |
|  | Forecast future from past data | ⟳ | Reverse-engineer present from imagined future |
| **↕️ Space** | Continuous variables (0 ≤ Q ≤ ∞) | ⟳ | Discrete states (4 Bernoulli outcomes) |
|  | Smooth optimization landscape | ⟳ | Discontinuous value jumps at alignment |
|  | Parameters given by market | ⟳ | Parameters created by promises |
| **♻️ Interaction** | Q doesn't affect D (independence) | ⟳ | P shapes delivery capability (endogeneity) |
|  | One-way causality: D → profit | ⟳ | Two-way coupling: P ⟷ capability ⟷ value |
|  | Static optimization problem | ⟳ | Dynamic belief-resource-capability spiral |
| **Key Trade-off** | Underage cost vs Overage cost | ⟳ | Die unfunded (Cu) vs Fail funded (Co) vs Win big (V) |
| **Solution Form** | Q* = F⁻¹(Cu/(Cu+Co)) | ⟳ | q* = ln[(2Cu+V)/(2Co+V)] |
| **Risk Management** | Buffer with safety stock | ⟳ | Buffer with strategic ambiguity |
| **Success Metric** | Minimize mismatch costs | ⟳ | Maximize alignment probability × value |

*Note: The ⟳ symbol represents transformation across three orthogonal axes (time, space, interaction), not simple substitution. Each dimension inverts fundamental assumptions about information flow, variable structure, and causal relationships.*