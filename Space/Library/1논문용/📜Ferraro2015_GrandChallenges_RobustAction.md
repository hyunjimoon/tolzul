---
collection:
  - "[[Space/Lab/Papers]]"
author_ids:
  - Fabrizio Ferraro
  - Dror Etzion
  - Joel Gehman
field:
  - 🎯str  # Strategy
  - 🌍env  # Environment/Sustainability
  - 🐅cba  # Causality-Based Action
thesisPaper: U
thesisChapter: T
year: 2015
rank: 8
research_stream:
  - Strategic Ambiguity
  - Grand Challenges
  - Robust Action
  - Wicked Problems
tags:
  - robust-action
  - grand-challenges
  - epistemic-uncertainty
  - wicked-problems
  - theoretical
  - oil-framework
created: 2025-11-05
modified:
  - 2025-11-05T00:00:00-05:00
connections:
  extends:
    - "[[📜Padgett1993_RobustAction_Medici]]"  # Core robust action concept
  applied_in:
    - "[[📜Grodal2017_GrandChallenge_Displacement]]"  # Field-level dynamics
  related_to:
    - "[[📜Abdallah2014_DoubleEdge_Ambiguity]]"  # Temporal aspects
---

# 📜 Tackling Grand Challenges Pragmatically: Robust Action Revisited

## 🗄️1: Core Framework (Q&A Format)

| Section | 🔐Research Question | 🔑Key Message & Framework | 📐Formal Concept | 🧱Literature Brick |
|---------|-------------------|-------------------------|-----------------|-------------------|
| **Main Thesis** | Can robust action solve grand challenges? | **YES**: Grand challenges REQUIRE low τ (ambiguity) because premature precision forecloses valuable exploration paths | **Epistemic Necessity**: τ must be low when true state space unknown | • Rittel & Webber (1973) wicked problems<br>• Knight (1921) uncertainty |
| **Extension** | How does this extend Padgett? | Padgett: Ambiguity as POLITICAL strategy<br>Ferraro: Ambiguity as EPISTEMOLOGICAL necessity | **Wicked Problems**: V → ∞, optimal τ* = low | • Camillus (2008) strategy wicked<br>• Levin et al. (2012) governance |
| **Pragmatism** | Why "pragmatic"? | Action despite uncertainty → Learn by doing → Update beliefs → Robust to initial model misspecification | **Pragmatic τ**: Start low, update as learn | • Dewey (1938) experimentation<br>• Ansell & Gash (2008) collaboration |

## 🗄️2: Theoretical Position

### Extends
- [[📜Padgett1993_RobustAction_Medici]]: From political strategy → epistemological necessity
- **Key Addition**: Why low τ is OPTIMAL (not just strategic), given fundamental uncertainty

### Applied In
- [[📜Grodal2017_GrandChallenge_Displacement]]: Field mobilization around ambiguous challenges
- Sustainability and climate change literature

### **Critical for Your Research**
Provides PHILOSOPHICAL JUSTIFICATION for why τ* should be low (not just empirical observation)

## 🗄️3: Grand Challenges vs Entrepreneurship

| Dimension | Typical Venture | Grand Challenge | Your Research |
|-----------|----------------|-----------------|---------------|
| **V (Uncertainty)** | High | VERY High (V→∞) | Varies by venture type |
| **State Space** | Bounded | Unbounded (unknown unknowns) | Bounded but uncertain |
| **Optimal τ*** | Moderate | Low (necessary) | τ* = f(V, i) |
| **Learning** | Rapid feedback | Slow, ambiguous signals | Bayesian updating |
| **Stakeholders** | Investors, customers | Society, governments, NGOs | Multiple types |

## 💭 Critical Insights for OIL Framework

### Philosophical Foundation for Low τ*

**Ferraro et al.'s Argument**:
```
Wicked Problems (Grand Challenges):
- State space not fully known (unknown unknowns)
- Cause-effect relationships unclear
- Multiple valid problem framings
→ High τ (premature precision) = FALSE CERTAINTY
→ Low τ (appropriate vagueness) = EPISTEMICALLY HONEST
```

**Connection to Your OIL**:
```
When V very high (grand challenge scale):
τ* = max{0, √(V/4i) - 1}

If V → ∞: Should τ* → ∞? NO!
Actually: When V AND i both very high,
τ* remains moderate (both in numerator/denominator)

But: τ* should stay LOWER than for well-defined problems
```

### Extension to Ventures

**Not all ventures face "grand challenges"**

But some do (e.g., climate tech, healthcare, education):
- These ventures SHOULD have lower τ*
- This is OPTIMAL, not suboptimal
- Connects to "mission-driven" ventures

**Testable Prediction**:
Ventures tackling grand challenges (high V) → Lower optimal τ* → Can sustain low τ longer

## 🎯 Research Implications

### For H2 Mechanism
**Ferraro adds EPISTEMIC justification**:

Not just: Low τ → Diverse coalition → Success
But also: Low τ → Preserved exploration → Better solutions → Success

**Two complementary mechanisms**:
1. **Coalition** (Eisenberg): Low τ → Unified diversity
2. **Learning** (Ferraro): Low τ → Preserved optionality in solution space

### Boundary Condition
**When is low τ epistemically justified?**
- High V: True uncertainty (not just risk)
- Complex causality: Non-linear, emergent effects
- Multiple framings: No single "correct" problem definition

**Implication**: Ventures in these domains can justify lower τ to investors as RATIONAL, not wishful thinking

### Potential Moderator
```
Later Success = β₀ + β₁·τ₀ + β₂·GrandChallenge + β₃·(τ₀ × GrandChallenge)

Where:
- β₁ > 0 (general effect of low τ)
- β₃ > 0 (low τ MORE beneficial for grand challenges)
```

## 🔬 Empirical Strategy

### Classification
**Grand Challenge Ventures** (vs Regular):
- Mission-driven (social/environmental)
- Complex causality (multi-stakeholder)
- Long time horizons (generational impact)

**Examples**:
- Climate tech (Tesla early days)
- Healthcare (cure vs treatment)
- Education (systemic reform)

### Testing H2 Heterogeneity
```python
# Test if β₁ differs by venture type
grand_challenge = (mission_driven == True) & (complexity == High)

model = "success ~ τ₀ * grand_challenge + controls"

# Predict: β₁ higher for grand_challenge ventures
```

## ✅ Action Items for 中군님

- [ ] **READ**: Section on epistemic uncertainty (why low τ necessary, not just strategic)
- [ ] **Classify**: Which ventures in your data tackle "grand challenges"?
- [ ] **Test**: Does H2 (β₁ > 0) stronger for these ventures?
- [ ] **Connect to**: Your "mission-driven" ventures analysis

## 📚 Related Reading
**Before**: [[📜Padgett1993_RobustAction_Medici]] - Political robust action
**After**: [[📜Grodal2017_GrandChallenge_Displacement]] - Field-level application

---

**핵심**: Low τ is not just strategic - it's EPISTEMOLOGICALLY NECESSARY for wicked problems
Your OIL framework: Formalizes this intuition mathematically
