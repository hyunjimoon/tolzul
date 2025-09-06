# ♻️ Dig: Framework Comparison

## Melody Section

**♻️0:** Entrepreneur's promise as core decision variable—promise level P inverts newsvendor's inventory Q, optimizing for delivery capability D instead of demand D, capturing "pursuit of opportunity without regard to resources currently controlled."

**♻️⏰:** Temporal tension: pretty promise fuels funding but delays delivery—min_P Co·PF(1-PD) + Cu·(1-PF)PD shows how higher promises increase funding PF(P)↑ but decrease delivery PD(P)↓, reversing newsvendor's past→present flow.

**♻️⏰↕️:** Spatial tension with new reward V: min_P Co·PF(1-PD) + Cu·(1-PF)PD - V·PF·PD introduces value creation through joint probability, where promise P parameterizes both funding and delivery success.

**♻️x:** Self-fulfilling promise is outside our scope—we exclude reinforcement loops where funding enables delivery (F|P /⊥ D|P), maintaining tractability while acknowledging real-world endogeneity like Tesla's "deep pocket effect."

## Full Section

### ♻️0: Entrepreneur's Promise as Core Decision Variable

**Point**: The promise level P becomes the central optimization variable—inverting newsvendor's inventory Q for demand D to promise P for delivery capability D, fundamentally reframing the decision problem. **Evidence**: Unlike traditional operations that optimize known variables (inventory, capacity, pricing), entrepreneurs must optimize the promise itself as the primary lever for "pursuit of opportunity without regard to resources currently controlled" (Stevenson & Jarillo, 1990). **Explanation**: This inversion uniquely captures both temporal dimensions (resources now vs later) and spatial dimensions (opportunity expansion), making promise P the central mechanism for bridging current constraints with future possibilities. The entrepreneur doesn't ask "how much should I stock?" but "what should I promise to attract resources?" **Transition**: This promise creates specific cost dynamics that shape rational behavior.

### ♻️⏰: Temporal Tension - Pretty Promise Fuels Funding but Delays Delivery

**Point**: Bold promises create a fundamental temporal tradeoff captured by the objective function: min_P Co·PF(1-PD) + Cu·(1-PF)PD. **Evidence**: Higher promise levels increase funding probability PF(P)↑ as investors are attracted to bold visions, but simultaneously decrease delivery probability PD(P)↓ as technical challenges mount—creating the core entrepreneurial dilemma. **Explanation**: The temporal gap means future informs present in a way that reverses newsvendor logic. Where newsvendors use yesterday's demand to inform today's inventory, entrepreneurs use tomorrow's promise to attract today's funding. Increasing promise level increases overage cost Co·PF(1-PD) from funded failures but decreases underage cost Cu·(1-PF)PD from unfunded deaths, with asymmetric costs (Cu > Co) tilting toward boldness. **Transition**: This cost structure must incorporate value creation mechanisms.

![[♻️dig_efg_structure.svg]]

*Figure 2: D Module (Dig) - E-F-G Literature Review Structure. The diagram shows the progression of promise vendor analysis through three stages. E (left): Cost minimization where temporal tension emerges from the trade-off between Co·Po (funded but not delivered) and Cu·Pu (not funded but delivered), with promise level increasing Po while decreasing Pu. F (center): Adding value V transforms the optimization to include V·Pm where Pm = PF(P)·PD(P), creating a 2x2 outcome matrix where value only emerges at joint success. G (right): Self-fulfilling dynamics (excluded from scope) where funding enables delivery through resource mobilization, creating reinforcement loops that would require dynamic analysis. The progression shows how simple cost trade-offs evolve into complex value creation systems.*

### ♻️⏰↕️: Spatial Tension with New Reward V

**Point**: Value V creates spatial complexity in the optimization, transforming the objective to: min_P Co·PF(1-PD) + Cu·(1-PF)PD - V·PF·PD. **Evidence**: Expected profit becomes E[π] = -Co·PF(P)·[1-PD(P)] - Cu·[1-PF(P)]·PD(P) + V·PF(P)·PD(P), where value only materializes through joint success. **Explanation**: The promise P now parameterizes value creation through the joint probability of funding AND delivery. Higher promises may increase PF but decrease PD, creating rich nonlinear dynamics where optimal P* must balance three forces: overage cost (funded failure), underage cost (unfunded death), and value creation (funded success). This spatial expansion from two-outcome (over/under) to four-outcome (funded/unfunded × delivered/undelivered) fundamentally changes the optimization landscape. **Transition**: We deliberately exclude certain feedback dynamics to maintain analytical tractability.

### ♻️x: Self-Fulfilling Promise is Outside Our Scope

**Point**: We exclude reinforcement loops where funding enables delivery, maintaining the independence assumption F|P ⊥ D|P for analytical tractability despite real-world violations. **Evidence**: While funding and delivery are clearly interdependent in practice (F|P /⊥ D|P)—Tesla's funding enabled battery R&D that improved delivery capability—we assume conditional independence given promise level. **Explanation**: Self-fulfilling prophecies where bold promises attract resources that enable delivery would require dynamic analysis beyond our static framework. This simplification allows deriving closed-form solutions while acknowledging that "deep pocket effects" existed in cases like Tesla, where Series D funding directly improved supply chain capabilities. Modeling this endogeneity remains important future work. **Transition**: Within these boundaries, we can derive optimal promise formulas that explain entrepreneurial behavior.
