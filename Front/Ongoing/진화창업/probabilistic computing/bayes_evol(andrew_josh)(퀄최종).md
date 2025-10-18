from [[bayes_evol(andrew_josh)]]
# Bayesian Evolution Literature Classification (우리 논문 "불확실한 약속설계" 관점)
## Based on Double Reparameterization Framework: P(success) → φ(promise) → (μ, τ)

### 핵심 프레임워크: 창업가의 불확실성 설계
- **첫 번째 재매개변수화**: P(success) → φ(promise) + n (자연의 복잡성)
- **두 번째 재매개변수화**: φ → (μ, τ) where μ = aspiration, τ = concentration
- **Strategic Ignorance**: τ* = max(0, V/ic - 1) when information cost exceeds value
- **From Player to Designer**: 불확실성을 제약에서 자원으로 전환

---

## 🚀 Space Food (우주식량) Literature Classification

| Paper | Core Concept | 🟢 AGREE | 🔴 DISAGREE | 🔵 Our Extension |
|-------|--------------|----------|-------------|------------------|
| **[[📜👾_vul14_one_done]]** | 1-3 samples sufficient for near-optimal decision | **Strong Agreement**: Low τ (sparse sampling) = adaptive optimality | Oversampling always better (우리: τ→∞ causes learning trap) | Our τ* formula explains when to stop sampling |
| **[[📜👾_stern24_model(beliefs, experimentation)]]** | Entrepreneurs test low-prior strategies first for better signals | Heterogeneous priors drive contrarian experiments | All experiments equally informative | τ modulates experiment informativeness |
| **[[📜👾_gans23_choose(entrepreneurship, experimentation)]]** | Entrepreneurial choice under uncertainty with strategic experiments | Experiments reveal both idea quality and strategy fit | Experiments are neutral (우리: τ affects bias) | Promise design (φ, τ) shapes what experiments reveal |
| **[[📜👾_tenanbaum11_grow(minds, cognition)]]** | Hierarchical Bayesian models of cognitive development | **Deep Resonance**: Learning as hierarchical prior updates | Learning is passive reception | τ controls active forgetting vs integration |
| **[[📜👾_gershman15_compute(rationality, resources)]]** | Bounded rationality as optimal given computational constraints | **Perfect Match**: Resource-rational = our V/ic framework | More computation always better | Strategic ignorance (τ=0) can be optimal |
| **[[📜👾_busenitz97_recognize(entrepreneurs, biases)]]** | Entrepreneurs use heuristics and biases more than managers | Biases as features not bugs when τ low | Biases are mistakes to eliminate | "Biases" = rational low-τ strategies |
| **[[📜👾_arrow69_classify(production, knowledge)]]** | Learning by doing creates knowledge spillovers | Production generates information (reduces n) | Knowledge always reduces uncertainty | Sometimes preserving uncertainty (low τ) valuable |
| **[[📜👾_meehl67_test(theory, method)]]** | Theory testing requires strong inference | Strong tests need precise predictions (high τ) | Always maximize test precision | Optimal τ depends on V/ic ratio |
| **[[📜👾_peng21_overload(information, decisions)]]** | Information overload degrades decision quality | **Strong Support**: High i (integration cost) → lower τ optimal | More information always helps | Rational ignorance when i > V/c |
| **[[📜👾_johnston02_caution(startups, scaling)]]** | Premature scaling is #1 cause of startup failure | High τ too early = scaling trap | Fast scaling always good if funded | τ should increase gradually with V/ic |
| **[[📜👾_nejad22_model(mentorship, accelerators)]]** | Accelerators help calibrate entrepreneurial beliefs | External calibration of μ and τ | One-size-fits-all mentorship | Mentors help optimize personal τ* |
| **[[📜👾_bhui21_optimize(decisions, resources)]]** | Resource-rational decision-making under constraints | Optimization given cognitive costs = our framework | Unbounded rationality ideal | Bounded optimality through τ choice |
| **[[📜👾_mansinghka25_automate(formalization, programming)]]** | Probabilistic programming automates Bayesian inference | Reduces i (integration cost) dramatically | Automation eliminates uncertainty | Lower i → higher optimal τ, not elimination |
| **[[📜👾_xuan24_plan(instruction, cooperation)]]** | Planning helps coordinate but constrains adaptation | Planning = high τ for coordination | Always plan thoroughly | τ* depends on coordination needs |

---

## 🎯 Bayesian Statistical Methods Integration

| Method | Application to Promise Design | Our Innovation |
|--------|-------------------------------|----------------|
| **Prior Predictive Check** | Test if φ ~ Beta(μτ, (1-μ)τ) generates realistic success rates | Before promising, simulate outcomes |
| **Posterior Predictive** | Validate updated beliefs match observed pivots | τ controls update magnitude |
| **Simulation-Based Calibration** | Recover true (μ, τ) from observed promises | Validate double reparameterization |
| **Hierarchical Modeling** | Industry → Founder → Venture nested structure | τ varies across hierarchy levels |
| **Model Comparison** | Test double vs single reparameterization | WAIC shows double superior |

---

## 🌊 Synthesis: From Decision Under to On Uncertainty

### 🤠 채찍과거: The Tyranny of Information Maximization
**What We Must Destroy:**
- "More information = better decisions" dogma that created analysis paralysis
- Prediction-Based Prescription's rigid "predict then prescribe" sequence ignoring endogeneity
- Prior Predictive Checks that validate but never question the prior itself
- The delusion that uncertainty is always the enemy to be eliminated
- Better Place's $850M funeral: the price of information addiction

### 🥕 당근미래: The Dawn of Uncertainty Design
**What We Must Build:**
- **Bayesian Cringe** (Gelman): Healthy skepticism of over-precision
- **Strategic Ignorance**: τ* = max(0, V/ic - 1) mathematically defines when not knowing beats knowing
- **Endogenous PBP**: Prediction and prescription become one when τ is chosen
- **Prior as Design**: Not what you believe but what you choose to believe
- **Tesla's Triumph**: "Roughly 200 miles" beats "Exactly 5 minutes"

### Key Falsifiable Predictions
1. **Industries with higher n → lower average τ** (complexity forces flexibility)
2. **Lower i (e.g., AI era) → bimodal τ distribution** (all-or-nothing strategies)
3. **V/ic ratio determines optimal promise precision** (not market maturity)
4. **Successful founders show τ trajectory: low → high** (not monotonic increase)

---

## 💡 Philosophical Foundation: Negative Capability

Building on Keats's "negative capability" - the ability to remain comfortable in uncertainty:

**NC = 1/(τ+1)**

- High NC (low τ): Tesla's "roughly 200 miles"
- Low NC (high τ): Better Place's "exactly 5 minutes"
- Zero NC (τ→∞): Theranos's impossible precision

This quantifies what poets knew intuitively: **comfort with uncertainty is strength, not weakness**.

---

## 🔬 Methodological Contributions

### For Bayesian Statistics (Andrew's Lens)
- **Endogenous uncertainty**: τ as chosen parameter
- **Double reparameterization**: Computational elegance
- **Rational meaning construction cost**: i as digestion cost

### For Innovation Policy (Josh's Lens)  
- **Stage-appropriate τ**: Different policies for different V/ic
- **Market failures from τ mismatch**: Over/under-specification
- **Policy as n-reducer, markets as τ-optimizer**: Clear roles

### For Entrepreneurship Theory (Scott's Lens)
- **Unifies Planning vs Action schools**: Both right at different τ
- **Explains contrarian success**: Low τ preserves option value
- **Strategic ignorance as capability**: Not bias but feature

---

## 🎭 The Promise Paradox Resolution

우리의 핵심 역설: **정밀한 약속은 왜 실패하고 모호한 약속은 왜 성공하는가?**

해답: **τ* = max(0, V/ic - 1)**

- Better Place: High τ despite high c → Learning trap → Failure
- Tesla: Low initial τ → Adaptive evolution → Success
- Optimal strategy: Let τ grow with V/ic ratio

**"불확실성은 극복할 제약이 아니라 설계할 자원이다"**

---

*Last updated: Based on deep synthesis of Space Food papers and our double reparameterization framework*