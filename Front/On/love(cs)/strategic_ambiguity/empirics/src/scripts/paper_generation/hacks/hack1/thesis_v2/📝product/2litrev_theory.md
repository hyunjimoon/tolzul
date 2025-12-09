# Literature Review: From Static Signals to Dynamic Construction

## 1. Information Economics: The Orthodoxy of Precision

### 1.1 The Signaling Paradigm

The information economics tradition treats entrepreneurial promises as costly signals that separate high-quality ventures from pretenders (Spence, 1973). In this framework, precision serves three functions: it enables **screening** by investors (Stiglitz & Weiss, 1981), establishes **verifiable milestones** for governance (Kaplan & Strömberg, 2003), and creates **reputational bonds** that align incentives (Diamond, 1989). Empirical work strongly supports this logic. Hsu (2004) finds ventures with specific patents attract 40% higher valuations, while Stuart et al. (1999) demonstrate that precise technological claims facilitate alliance formation. Zuckerman's (1999) seminal work on the "categorical imperative" shows that ventures failing to fit established categories face an average 18% "illegitimacy discount" in IPO valuations.

### 1.2 Application to Mobility Ventures

In the mobility sector, this tradition predicts severe penalties for vagueness. Consider two contrasting cases: Waymo publishes detailed technical specifications including "Level 4 autonomy with 99.99% reliability in defined operational domains," attracting $5.5 billion from informed investors. Meanwhile, Nikola's vague promises about "revolutionary hydrogen technology" ultimately revealed fraudulent claims, destroying $30 billion in market value. The information view suggests that **rational investors should universally prefer precision** as it reduces adverse selection, enables performance monitoring, and signals entrepreneurial competence. Yet this perspective cannot explain why ventures like Uber thrived with deliberately ambiguous platform strategies or why Tesla's perpetually delayed "Full Self-Driving" maintains investor enthusiasm.

## 2. Real Options Theory: The Value of Strategic Flexibility

### 2.1 Options Thinking in Entrepreneurship

Real options theory reconceptualizes ventures not as fixed projects but as **portfolios of future opportunities** (McGrath, 1997). Under this framework, commitment becomes a liability when environments are uncertain. McGrath and MacMillan's (1995) discovery-driven planning shows that preserving flexibility enables "failing fast and cheaply" while maintaining upside potential. Theoretical models by Roberts and Weitzman (1981) prove that under technical uncertainty, the option value of waiting can exceed the cost of delayed entry. Baldwin and Clark's (2000) modular design theory extends this logic: architectural flexibility creates compound options across multiple dimensions—technical, market, and organizational.

### 2.2 Flexibility Premium in Dynamic Markets

Empirical evidence supports significant flexibility premiums. Eisenhardt's (1990) study of successful ventures reveals systematic use of "strategic ambiguity" to enable rapid pivoting. Santos and Eisenhardt (2009) document how unclear boundaries facilitate resource acquisition in nascent markets by allowing ventures to claim membership in multiple categories. In mobility, this manifests powerfully: Uber's initial ambiguity about being a "technology platform" versus "transportation company" enabled expansion from ride-sharing to delivery, freight, and autonomous vehicles—creating a $75 billion ecosystem. Tesla's vague "sustainable transport" mission justified pivots from sports cars to mass market vehicles to energy storage. The options perspective suggests **ambiguity creates value by preserving adaptive capacity**.

## 3. Toward a Synthesis: Endogenous Quality and Earned Precision

### 3.1 The False Dichotomy

Both traditions assume **idea quality exists independently** of execution—ventures either have it (and should signal) or lack it (and should pivot). But operational research challenges this assumption. Fine's (1986) learning curve models show that quality emerges through production experience, with high-capability firms learning 30% faster. Cohen and Levinthal's (1990) absorptive capacity framework demonstrates that prior knowledge enables recognition of new opportunity value. Christensen's (1997) disruption theory reveals how "low quality" technologies improve through market iteration. These insights suggest **quality is constructed through the interaction between promises and market feedback**, not revealed through precision.

### 3.2 Our Integration: The Consideration Set Framework

We propose that vagueness represents the founder's **consideration set size**—the range of strategic trajectories they preserve for future selection. This reframes the precision decision from "signaling quality" versus "preserving options" to **optimizing the learning-commitment sequence**:

| Phase | High Exercisability (Software) | Low Exercisability (Hardware) |
|-------|--------------------------------|------------------------------|
| **Early Stage** | Large consideration set → Parallel experiments → Market selection | Small consideration set → Sequential validation → Technical commitment |
| **Mechanism** | A/B testing, rapid iteration, user feedback | Prototype refinement, supplier contracts, regulatory approval |
| **Later Stage** | Convergence to discovered optimum | Lock-in to pre-specified design |
| **Example** | Uber: Ride → Food → Freight | Waymo: L4 autonomy only |

### 3.3 Exercisability as Boundary Condition

Critically, the value of a large consideration set depends on **exercisability**—the operational cost of exploring alternatives. We identify four dimensions:

1. **Technical Architecture**: Modular (high F) vs Integral (low F) - Tesla's OTA updates vs Boeing's certified systems
2. **Resource Commitment**: Variable (high F) vs Fixed (low F) - Cloud computing vs Manufacturing plants  
3. **Partner Specificity**: Platform (high F) vs Bilateral (low F) - App stores vs OEM contracts
4. **Regulatory Regime**: Permissionless (high F) vs Licensed (low F) - Software vs Medical devices

When exercisability is high, vagueness enables **efficient parallel search** across the consideration set. When low, vagueness creates **coordination failures** without learning benefits.

## 4. Literature Gaps and Our Contributions

### 4.1 What's Missing

Existing literature exhibits three critical gaps:

1. **Static Analysis**: Both traditions analyze precision at a single point, ignoring temporal dynamics
2. **Binary Outcomes**: Studies examine either funding or failure, not the complete lifecycle
3. **Assumed Quality**: Research treats idea quality as exogenous rather than emergent

### 4.2 Our Contributions

This paper addresses these gaps through three innovations:

**Contribution 1: Temporal Decomposition**  
We show that information economics and real options apply to different lifecycle stages rather than representing contradictory theories. Early investors face screening problems requiring precision; later investors face adaptation challenges valuing flexibility.

**Contribution 2: Endogenous Quality Model**  
We develop a formal model where idea quality τ* emerges from the interaction between initial vagueness V and market learning rate λ: τ* = V·λ·F where F represents exercisability. This explains why identical vagueness levels produce different outcomes.

**Contribution 3: Empirical Measurement**  
We introduce computational linguistics methods to quantify promise vagueness across 137,597 ventures, creating the first large-scale dataset linking communication precision to funding outcomes.

## 5. Positioning Our Theory

Our "Entrepreneur's Partial Commitment" (EPC) framework synthesizes insights from:

- **Strategic Management**: Dynamic capabilities (Teece et al., 1997) meet entrepreneurial judgment (Foss & Klein, 2012)
- **Operations**: Flexible manufacturing (Fine, 1998) meets lean startup methodology (Ries, 2011)
- **Finance**: Staged financing (Gompers, 1995) meets control rights allocation (Kaplan & Strömberg, 2003)

We argue that optimal vagueness V* balances information costs against coordination savings:

```
V* = argmax[Information Value(V) - Coordination Cost(V|F)]
```

Where coordination costs decrease with exercisability F, explaining why software ventures can sustain higher vagueness without penalty.