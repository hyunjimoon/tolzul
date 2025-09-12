## ACTIVATION PROTOCOL

When user requests "mss(🫀,markovian(🧠))" and attaches this document:

1. Infer user's goal (🫀) from context, attached documents, and recent conversation
2. Identify knowledge domains (🧠) by combining user's information with AI knowledge
3. Extract minimal sufficient statistics for continuing work across sessions

## OPERATIONAL DEFINITION

MSS(🫀,markovian(🧠)) = {Sₜ, Oₜ, K(g₁,g₂,...,gₙ), D, Sₜ₊₁}

Where:

- 🫀 = Inferred goal the user is trying to accomplish
- 🧠 = Combined knowledge from user + AI domains
- Sₜ = Precise mathematical state of current progress
- Oₜ = Objective function defining success criteria
- K(g₁,g₂,...,gₙ) = Minimal knowledge set for each sub-goal
- D = Required database structure
- Sₜ₊₁ = Transition function to next state

## AI INFERENCE INSTRUCTIONS

When this framework is activated:

1. Analyze all available context to identify user's true goal (🫀)
2. Determine knowledge domains (🧠) relevant to the goal
3. Extract only decision-critical information from these domains
4. Structure as mathematical state-transition process
5. Format output as shown in examples below

## OUTPUT FORMAT

```
# MSS(🫀: [inferred goal], markovian(🧠))

## Current State (Sₜ)
[Precise mathematical description of current progress]

## Objective Function (Oₜ)
[Mathematical formulation of goal and success criteria]

## Knowledge Extraction Matrix
g₁: [Sub-goal 1] → MSS = "[minimal decision rule]"
g₂: [Sub-goal 2] → MSS = "[minimal decision rule]"
g₃: [Sub-goal 3] → MSS = "[minimal decision rule]"

## Required Output
[Database structure capturing minimal sufficient statistics]

## Next State (Sₜ₊₁)
[Precise next steps to continue work]
```

## EXAMPLE APPLICATIONS
### Mathematical Optimization
#### 🗣️in words:
When user's goal involves solving optimization problems, extract constraint structures, current solution candidates, and optimality conditions.

#### 🧮in math:
P: min/max f(x) subject to g(x) ≤ 0, h(x) = 0, extract:
- Feasible region F = {x ∈ ℝⁿ | g(x) ≤ 0, h(x) = 0}
- Current solution candidates X* = {x₁*, x₂*,...} with f(x*)
- KKT conditions: ∇f(x*) + Σλᵢ∇gᵢ(x*) + Σμⱼ∇hⱼ(x*) = 0, λᵢgᵢ(x*) = 0, λᵢ ≥ 0
- Constraint qualifications: LICQ, MFCQ, or CRCQ at x*
- Sufficiency conditions: ∇²L(x*,λ*,μ*) positive definite on tangent space

### Research Synthesis
#### 🗣️in words:
When user's goal involves literature review or research synthesis, extract classification schemas, relationship patterns, and methodological frameworks.
#### 🧮in math:
For literature corpus C = {p₁, p₂, ..., pₙ}, extract:

- Classification matrix M where Mᵢⱼ = p(class j | paper i)
- Citation network G = (V,E) with centrality measures c: V → ℝ
- Hierarchical taxonomy T = (N,E,ω) with weighting function ω: E → [0,1]
- Methodological evolution function f(m,t) = p(method m | time t)
- Comparative advantage tensor A where Aᵢⱼₖ = performance of method i on criterion j in context k

### Statistical Testing
#### 🗣️in words:
Statistical Testing When user's goal involves hypothesis testing, extract null/alternative hypotheses, test statistics, distribution assumptions, and significance thresholds.

#### 🧮in math:
For hypothesis framework H = {H₀, H₁, α, β}, extract:

- Null hypothesis H₀: θ ∈ Θ₀ ⊂ ℝᵏ
- Alternative hypothesis H₁: θ ∈ Θ₁ ⊂ ℝᵏ
- Test statistic T(X) with distribution T ~ F₀ under H₀
- Critical region C = {x | T(x) > c_α} where P_H₀(T > c_α) = α
- Power function π(θ) = P_θ(T(X) ∈ C) with β = 1 - inf{π(θ) | θ ∈ Θ₁}
- Asymptotic properties: consistency, efficiency, robustness metrics

## USAGE NOTES

- The AI should automatically infer goals rather than asking directly
- Mathematical formulation should be prioritized whenever possible
- Information extraction should satisfy min{K | P(correct decision|K) ≥ threshold}
- The framework self-adapts based on detected knowledge domains

This framework enables the AI to infer the user's goal, combine knowledge domains, and extract only what's necessary for efficient knowledge transfer across sessions.

---
2025-05-20
- combining [[MSS(🫀A, 🧠B)]] and [[markovian prompting]] using [cld](https://claude.ai/chat/2a1d7a3f-3da0-4237-b3a3-3032d916186f)
[[scott(🧭🗺️selling entrepreneurial choice-map as Bayes.Entrep)]]