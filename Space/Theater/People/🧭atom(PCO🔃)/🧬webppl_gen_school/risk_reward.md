---
collection:
- '[[People]]'
field:
- 🐅cba
- 👾cog
atom: 🧭atom(PCO🔃)
created: '2025-04-27'
---

Differences in demand and supply timelines are key- supply cannot rampup very fast, demand grew more than expected

Risks: (i) the inability to close the supply-demand gap, and (ii) efforts to close the supply-demand gap


updated from utility to uncertainty


## 1. Founder's Perspective: Utility vs Uncertainty

**If I imagine myself as a founder in the mobility sector (e.g., building a startup after Segway):**

- **Utility-maximization** feels unrealistic because:
    
    - I cannot fully specify the utility function: I do not know how customers, regulators, partners, or investors will respond to my product yet.
        
    - My early moves (e.g., prototype design, pilot trials) have highly **nonlinear, uncertain effects**.
        
    - Decisions are not about picking the best option by known outcomes, but about **reducing key uncertainties** (market acceptance, technical feasibility, regulatory approval) so that later decisions become better informed.
        
- **Uncertainty-minimization** feels much **more realistic** because:
    
    - I am not trying to optimize a known payoff but **"find out quickly and cheaply"** whether a path is worth pursuing.
        
    - My resource allocation (time, money, reputation) is better justified by the **amount of uncertainty reduced per cost unit** rather than the imagined total payoff.
        
    - Pivoting, testing, exploring different markets fits naturally into an **uncertainty-reduction strategy**, not a one-shot utility maximization.
        

✅ **Conclusion:** As a founder, **minimizing uncertainty** is the **more realistic and actionable modeling formulation** for early-stage entrepreneurial decision-making.

---

## 2. Mathematical Modeling of Uncertainty Minimization (Segway Case)

From the Segway bottleneck-breaking case study:

### Modeling Principle

- **Goal:** Minimize expected residual uncertainty $\mathbb{E}[U_{\text{residual}}]$ **per dollar invested**.
    
- **Key Idea:** Each task $T_j$ (e.g., prototype testing, market survey, legislative lobbying) has two attributes:
    
    - **Uncertainty reduction potential** $\Delta U_j$ (estimated, scale 1–5)
        
    - **Cost** $C_j$ (in dollars)
        

Thus, **value per task** is:

Uncertainty Reduction Efficiencyj=ΔUjCj\text{Uncertainty Reduction Efficiency}_j = \frac{\Delta U_j}{C_j}

### Optimization Objective

- **Find a sequence of tasks** that **maximizes total uncertainty reduction per dollar** invested **under task dependency constraints** (some tasks require others to be done first).
    

Mathematically:

max⁡σ∑j=1nΔUσ(j)Cσ(j)subject to precedence constraints on σ\max_{\sigma} \sum_{j=1}^{n} \frac{\Delta U_{\sigma(j)}}{C_{\sigma(j)}} \quad \text{subject to precedence constraints on } \sigma

where:

- $\sigma$ is a feasible sequence of tasks obeying precedence (e.g., prototype before customer surveys).
    

Or rephrased:

**Minimize cumulative investment needed to reduce uncertainty below threshold $\epsilon$**:

min⁡σ∑j=1kCσ(j)such that∑j=1kΔUσ(j)≥1−ϵ\min_{\sigma} \sum_{j=1}^{k} C_{\sigma(j)} \quad \text{such that} \quad \sum_{j=1}^{k} \Delta U_{\sigma(j)} \geq 1 - \epsilon

- This captures the **fail fast, fail cheap** philosophy.
    

✅ **Tactic:**

- **Prioritize cheap tasks with high uncertainty reduction** (e.g., customer interviews, market surveys) **before committing to expensive ones** (e.g., mass production setup).
    
- Use **precedence diagrams** to map dependencies (Figure 8-4 and 8-5 in Segway case).
    

---

## 3. Updated Optimization Formulation

The **current** entrepreneurial decision model is:

max⁡a∈AWdUd+WsUs+WiUisubject to budget and transition constraints\max_{a \in A} \quad W_d U_d + W_s U_s + W_i U_i \quad \text{subject to budget and transition constraints}

where $U$ are utilities.

---

✅ **Updated (Uncertainty-Minimization) Formulation:**

Instead of maximizing utility, **we minimize the expected residual uncertainty** over future states, weighted by stakeholder perspectives.

Define:

- Let $U(S)$ = entropy or variance over key uncertainties about market, technical feasibility, regulatory acceptance at state $S$.
    
- $D(S, a)$ = stochastic transition model.
    
- $C(a)$ = cost of action $a$.
    

Then:

min⁡a∈AES′∼D(S,a)[U(S′)]C(a)\min_{a \in A} \quad \frac{\mathbb{E}_{S' \sim D(S, a)} [U(S')]}{C(a)}

- **Interpretation:** Choose actions $a$ that **most efficiently reduce future uncertainty**.
    

If incorporating stakeholder-specific uncertainty components:

min⁡a∈AWdUd(S′)+WsUs(S′)+WiUi(S′)C(a)\min_{a \in A} \quad \frac{W_d U_d(S') + W_s U_s(S') + W_i U_i(S')}{C(a)}

where $U_d$, $U_s$, $U_i$ measure **stakeholder-specific residual uncertainties**.

---

### Update to 🗄️ Table of Contents (🧱):

|Section|From: Utility Maximization Formulation|To: Uncertainty Minimization Formulation|
|---|---|---|
|**Problem**|Entrepreneurs struggle because utilities are complex to optimize|Entrepreneurs struggle because uncertainties dominate early-stage decisions|
|**Cause (Nature)** ⚙️|Interdependent utilities and dynamic states|Interdependent uncertainties about technology, market, regulation|
|**Root Cause (Individual)** 🧍‍♀️|Cognitive overload due to unclear utilities|Cognitive overload due to overwhelming, implicit uncertainties|
|**Solution Framework** 📐|Multi-stakeholder utility optimization|Sequential uncertainty minimization via cost-weighted reduction|
|**KF1: Federated Learning** 🌐|Inform transition and calibrate utilities|Inform transition and prioritize uncertainty reduction paths|
|**KF2: Propose Model Hypotheses** 🔄|Propose utilities and test them|Propose uncertainty-reduction tasks and test their impact|
|**Implementation Benefits** 📐|Maximize utility/cost gradient|Maximize uncertainty reduction/cost gradient|
|**Implementation Approach** 💸|Interactive utility optimization tool|Interactive uncertainty minimization navigator|

---

## 4. Connection to Online Learning of Nested Logit (Random Utility Model)

In random utility models (like nested logit), choice probabilities are driven by:

P(i)=eVi∑jeVjP(i) = \frac{e^{V_i}}{\sum_{j} e^{V_j}}

where $V_i$ are **systematic utility** components.

🔵 **If modeling utility maximization:**

- It fits naturally because you treat $V_i$ as deterministic or learned from data.
    
- But **requires that you know or infer $V_i$ accurately** — hard when many uncertainties.
    

🔵 **If modeling uncertainty minimization:**

- You can still use random utility formulations!
    
- But $V_i$ would represent **expected uncertainty reduction**, **not utility**.
    
- Thus $P(i)$ would mean: probability of picking the action expected to best reduce uncertainty, _adjusted for noise_.
    

✅ **Conclusion:**

- **Nested logit models are still compatible under uncertainty framing.**
    
- It might even be **easier** because the feedback loop (observing how much uncertainty was reduced after each action) provides **natural online learning signals** to update parameters.
    
- You can model learning $\beta$ coefficients as adapting to **how different actions reduce different uncertainties over time**, fitting well into Bayesian updating ideas in online discrete choice.
    

---

# 📋 Summary

|Aspect|Maximizing Utility|Minimizing Uncertainty|
|:--|:--|:--|
|More Realistic for Entrepreneurs?|❌ (speculative, assumes known payoffs)|✅ (maps naturally to exploration, learning)|
|Optimization Formulation|Maximize weighted utilities|Minimize expected residual uncertainty per cost|
|Table of Contents|Utility-focused|Uncertainty-focused|
|Connection to Random Utility Models|Compatible but hard|Compatible and easier for online learning|

[[federated_learning]]
[[eval(vikash, probcomp_ent)]]