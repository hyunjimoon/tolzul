---
collection:
  - "[[Space/Lab/Papers]]"
author_ids:
  - Steve W. J. Kozlowski
  - Georgia T. Chao
  - James A. Grand
  - Michael T. Braun
  - Goran Kuljanin
field:
  - 🧠phi  # Philosophy
  - 🔢sim  # Simulation
  - 🐅cba  # Causality-Based Action
thesisPaper: U
thesisChapter: T
year: 2021
rank: 8
research_stream:
  - Computational Theorizing
  - Multilevel Emergence
  - Process Theory
  - Layered Theory Evaluation
tags:
  - computational-modeling
  - emergence
  - multilevel
  - process-theory
  - foundational
created: 2025-12-06
modified:
  - 2025-12-06T00:00:00-05:00
connections:
  extends:
    - "[[📜bhaskar75_critical_realism]]"  # Stratified reality
    - "[[📜epstein06_generative_social_science]]"  # Generative modeling
  applied_in:
    - Team cognition research
    - Organizational emergence
  related_to:
    - "[[📜Ferraro2015_GrandChallenges_RobustAction]]"  # Complex systems
---

![[📜kozlowski21_LTE_emergence_poster.svg]]

# 📜 Layered Theory Evaluation: Computational Process Theorizing

## 🗄️1: Core Framework (Q&A Format)

| Section | 🔐Research Question | 🔑Key Message & Framework | 📐Formal Concept | 🧱Literature Brick |
|---------|-------------------|-------------------------|-----------------|-------------------|
| **Main Thesis** | How to formalize emergence in organizations? | Theory must specify mechanisms at **three layers**: surface patterns, mediating processes, and **foundational causal drivers** | **Layered Theorizing**: Layer 1 (outcomes) ← Layer 2 (processes) ← Layer 3 (mechanisms) | • Bhaskar (stratified ontology)<br>• Epstein (generative explanation) |
| **Core Claim** | Why computational modeling? | Narrative theories hide logical gaps. **Formal models** expose assumptions and generate testable predictions | **Computational Sufficiency**: If model generates target patterns, theory is internally consistent | • Simon (bounded rationality)<br>• Holland (complex systems) |
| **Key Insight** | What makes Layer 3 special? | "Foundational causal drivers that can be formalized" - the *generative mechanisms* that must exist for patterns to emerge | **Formal Mechanism Specification**: Mathematical/computational representation of causal processes | • Kozlowski & Klein (2000)<br>• Grand et al. (2016) |

## 🗄️2: The Three Layers

```
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 1: OBSERVABLE PATTERNS                                   │
│  ════════════════════════════                                   │
│  • Emergent outcomes at macro level                             │
│  • Statistical regularities and distributions                   │
│  • What we measure in studies                                   │
│  • Examples: Team performance, funding patterns, success rates  │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 2: MEDIATING PROCESSES                                   │
│  ═══════════════════════════                                    │
│  • How Layer 3 mechanisms manifest                              │
│  • Temporal dynamics and sequences                              │
│  • Interaction patterns and networks                            │
│  • Examples: Learning trajectories, coalition formation         │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 3: FOUNDATIONAL CAUSAL DRIVERS                           │
│  ════════════════════════════════════                           │
│  • "Foundational causal drivers that CAN BE FORMALIZED"         │
│  • Generative mechanisms underlying all else                    │
│  • Micro-level decision rules and cognitive processes           │
│  • Examples: Belief updating, threshold decisions, identity     │
└─────────────────────────────────────────────────────────────────┘
```

## 🗄️3: Narrative vs Computational Theory

| Dimension | Narrative Theory | Computational Theory |
|-----------|-----------------|---------------------|
| **Specification** | Verbal descriptions | Formal mathematical/code |
| **Logic** | Implicit, often ambiguous | Explicit, testable |
| **Assumptions** | Hidden, easy to overlook | Exposed, must be stated |
| **Predictions** | Qualitative, directional | Quantitative, distributional |
| **Falsifiability** | Difficult to refute | Precise boundary conditions |
| **Emergence** | Asserted, not demonstrated | Generated, observable |

## 🗄️4: The LTE Framework Applied

### Step 1: Specify Layer 3 Mechanisms
```python
# Example: Precision-Decision Mechanism
def investor_decision(promise_precision, threshold, type):
    if type == "analyst":
        return promise_precision > threshold  # Precise promises preferred
    elif type == "believer":
        return promise_precision < threshold  # Vague promises accepted
```

### Step 2: Formalize Layer 2 Processes
```python
# Coalition Formation Process
def coalition_dynamics(precision, investor_pool):
    coalition = []
    for investor in investor_pool:
        if investor_decision(precision, investor.threshold, investor.type):
            coalition.append(investor)
    return coalition
```

### Step 3: Generate Layer 1 Patterns
```python
# Emergence of Funding/Success Patterns
def simulate_outcomes(n_entrepreneurs, n_periods):
    results = []
    for e in entrepreneurs:
        coalition = coalition_dynamics(e.precision, investors)
        funding = len(coalition) > minimum_threshold
        success = learning_over_time(e, coalition, market_uncertainty)
        results.append((e.precision, funding, success))
    return distribution(results)  # Compare to empirical patterns
```

## 💭 Critical Insights for Dissertation

### Applying LTE to OIL Framework

| Layer | Your Theory Component | Formalization |
|-------|----------------------|---------------|
| **Layer 3** | Belief updating, threshold heterogeneity | `θ* = μ + kσ` (investor thresholds) |
| **Layer 2** | Coalition formation, commitment dynamics | `Coalition(τ) = f(diversity, threshold_dist)` |
| **Layer 1** | Funding patterns, success rates | Emergent distributions from simulation |

### Why Layer 3 is Critical

> "Layer 3: foundational causal drivers that can be formalized"

**For your dissertation**:
- Layer 1: We *observe* that low τ → later success
- Layer 2: We *hypothesize* coalition mechanisms
- Layer 3: We must *formalize* the actual decision rules

```
Without Layer 3 Formalization:
  "Coalition building mediates the effect of τ"
  (Unfalsifiable - what exactly IS coalition building?)

With Layer 3 Formalization:
  "Investors with heterogeneous thresholds θᵢ ~ N(μ, σ²)
   join coalitions when τ < θᵢ (for believers)
   This generates diversity D = Var(types in coalition)
   Diversity enables learning L = f(D, uncertainty)"
  (Testable - specific predictions about D, L distributions)
```

## 🎯 Your Layer 3 Mechanisms to Formalize

| Mechanism | Verbal Description | Formal Specification |
|-----------|-------------------|---------------------|
| **Vagueness Effect** | Vague promises attract diverse stakeholders | `P(join\|τ, θᵢ) = 1 - Φ((τ - θᵢ)/σₑ)` |
| **Learning Dynamics** | Diverse coalitions enable better learning | `Learning = α × Diversity × (1 - τ)` |
| **Commitment Trap** | Identity investment prevents pivoting | `P(pivot) = exp(-β × sunk_identity)` |
| **Optimal Precision** | τ* balances coalition and credibility | `τ* = argmax E[Success(τ)\|V, i]` |

## 📚 Must Read

1. **Kozlowski et al. (2013)**. "Advancing Multilevel Research Design" - Foundation
2. **Kozlowski et al. (2016)**. "Capturing the Multilevel Dynamics of Emergence" - Method
3. **Grand et al. (2016)**. "The Dynamics of Team Cognition" - Application
4. **Kuljanin et al. (2024)**. "Advancing Organizational Science with Computational Process Theories" - Latest

## 🔗 For Your Paper

### How to Cite
> "Following the layered theory evaluation framework (Kozlowski et al., 2021), we specify our theoretical mechanisms at three levels: observable funding patterns (Layer 1), coalition formation processes (Layer 2), and the foundational causal drivers—investor threshold heterogeneity and belief updating—that can be formalized computationally (Layer 3)."

### Strengthens Your Argument By:
1. Organizing OIL framework into explicit theoretical layers
2. Identifying which mechanisms require formalization
3. Justifying computational model as theory test
4. Moving beyond correlational to generative explanation

---

**핵심 통찰**: "Layer 3: foundational causal drivers that can be formalized"
- Observable patterns (Layer 1) are insufficient for explanation
- Mediating processes (Layer 2) must be grounded in...
- Formalizable mechanisms (Layer 3) that *generate* the patterns

*"Computational modeling forces explicit specification of the micro-mechanisms that produce macro-phenomena."*
