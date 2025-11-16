---
collection:
  - "[[Space/Lab/Papers]]"
author_ids:
  - Giulia Cappellaro
  - Andrea Compagni
  - Eero Vaara
field:
  - 🎯str  # Strategy
  - 👾cog  # Cognition
  - 🌑dar  # Dark side
year: 2020
rank: 7
research_stream:
  - Strategic Ambiguity
  - Organizational Defense
  - Dark Side
tags:
  - opacity
  - protective-ambiguity
  - concealment
  - boundary-conditions
  - dark-side
  - empirical-qualitative
  - case-study
created: 2025-11-05
modified:
  - 2025-11-05T00:00:00-05:00
connections:
  extends:
    - "[[📜Eisenberg1984_Ambiguity_Communication]]"  # Strategic ambiguity
  applied_in:
    - Organizational defense literature
  related_to:
    - "[[📜Abdallah2014_DoubleEdge_Ambiguity]]"  # Another form of destructive
  contradicts:
    - Benign strategic ambiguity narrative
---

# 📜 Maintaining Strategic Ambiguity for Protection: Sicilian Mafia

## 🗄️1: Core Framework (Q&A Format)

| Section | 🔐Research Question | 🔑Key Message & Framework | 📐Formal Concept | 🧱Literature Brick |
|---------|-------------------|-------------------------|-----------------|-------------------|
| **Main Thesis** | Can ambiguity serve PROTECTIVE (not productive) functions? | **YES**: Organizations deliberately maintain low τ to CONCEAL problems, not preserve options | **Defensive τ**: Low precision for protection, not flexibility | • Vaughan (1999) concealment<br>• Weick & Sutcliffe (2007) opacity |
| **Three Mechanisms** | How is protective ambiguity achieved? | 1. **Opacity**: Hide information<br>2. **Equivocality**: Create confusion<br>3. **Absurdity**: Contradict signals | τ ↓ for defensive reasons | • Alvesson (1993) ambiguity types<br>• Eisenberg (1984) protection |
| **Dark Side** | When is low τ malicious? | When intent is CONCEALMENT (hide problems) not EXPLORATION (preserve options) | **Intent matters**: Adaptive vs Protective ambiguity | • Greve et al. (2010) misconduct<br>• Palmer (2012) organizational wrongdoing |

## 🗄️2: Theoretical Position

### Extends
- [[📜Eisenberg1984_Ambiguity_Communication]]: Strategic ambiguity → Can also be defensive

### Related To
- [[📜Abdallah2014_DoubleEdge_Ambiguity]]: Another form of destructive ambiguity
- Organizational wrongdoing literature

### Critical for Your Research
**BOUNDARY CONDITION**: Low τ beneficial when intent is ADAPTIVE, harmful when PROTECTIVE

## 🗄️3: Adaptive vs Protective Ambiguity

| Dimension | Adaptive Ambiguity | Protective Ambiguity | Your Research |
|-----------|-------------------|---------------------|---------------|
| **Intent** | Preserve options, enable learning | Conceal problems, avoid accountability | Need to distinguish |
| **τ Level** | Low (vague promises) | Low (vague communications) | Same observable |
| **Mechanism** | Coalition formation, flexibility | Hide negative information | Different |
| **Outcome** | Success (if executed well) | Failure (eventually exposed) | Opposite |
| **Stakeholder Impact** | Diverse interpretations (positive) | Confusion and suspicion (negative) | Different |

## 💭 Critical Insights for OIL Framework

### CRITICAL BOUNDARY CONDITION

**Your OIL Framework Assumes**:
```
Low τ → Preserved optionality → Learning → Adaptation → Success
```

**Cappellaro et al. Shows**:
```
Low τ → Concealment → Delayed problems → Crisis → Failure
```

**Both use LOW τ, but different INTENT and OUTCOME**

### Mathematical Formulation

**Need to distinguish TWO types of low τ**:

```
τᵃᵈᵃᵖᵗⁱᵛᵉ: Low precision for optionality
τᵖʳᵒᵗᵉᶜᵗⁱᵛᵉ: Low precision for concealment

OIL Framework applies to τᵃᵈᵃᵖᵗⁱᵛᵉ
Cappellaro applies to τᵖʳᵒᵗᵉᶜᵗⁱᵛᵉ

H2 (β₁ > 0) valid ONLY for τᵃᵈᵃᵖᵗⁱᵛᵉ
For τᵖʳᵒᵗᵉᶜᵗⁱᵛᵉ: β₁ < 0 (concealment → eventual failure)
```

### Empirical Challenge

**Problem**: Both types have low τ - how to distinguish in data?

**Possible Indicators of PROTECTIVE ambiguity**:
1. **Pattern**: τ decreases over time (more secretive)
2. **Contradictions**: Multiple conflicting statements
3. **Opacity**: Reduced transparency alongside ambiguity
4. **Context**: Known problems in domain (fraud, misconduct)
5. **Outcome**: Eventual scandals or sudden failures

**Indicators of ADAPTIVE ambiguity**:
1. **Pattern**: τ eventually increases (clarifies after learning)
2. **Coherence**: Vague but internally consistent
3. **Transparency**: Ambiguous but open to questions
4. **Context**: High uncertainty industry (tech, biotech)
5. **Outcome**: Successful pivots or strategic shifts

## 🎯 Research Implications

### For H2 Conditional Model

**Current H2**: Vague promises (low τ₀) → Higher later success (β₁ > 0)

**With Cappellaro insight**:
```
Later Success = β₀ + β₁ᵃᵈᵃᵖᵗⁱᵛᵉ·τ₀·Adaptive + β₁ᵖʳᵒᵗᵉᶜᵗⁱᵛᵉ·τ₀·Protective

Where:
- β₁ᵃᵈᵃᵖᵗⁱᵛᵉ > 0 (your hypothesis)
- β₁ᵖʳᵒᵗᵉᶜᵗⁱᵛᵉ < 0 (Cappellaro's finding)
- Need to classify ventures as Adaptive vs Protective
```

### Identification Strategy

**How to identify protective ambiguity in your data?**

```python
# Risk factors for protective (not adaptive) ambiguity
protective_risk = (
    (decreasing_transparency_over_time == True) |
    (inconsistent_statements == True) |
    (industry_fraud_risk == High) |
    (sudden_failure_unexplained == True) |
    (regulatory_issues == True)
)

# Test H2 separately for low vs high risk
model = "success ~ tau_0 * protective_risk + controls"

# Predict: β₁ > 0 for low risk, β₁ ≤ 0 for high risk
```

### Sample Selection

**Consider excluding**:
- Ventures with known fraud/misconduct
- Industries with high opacity (cryptocurrency pre-regulation?)
- Companies that failed with scandals

**Or**: Explicitly model as moderator

## 🔬 Practical Implications

### For Investors

**Red Flags** (Protective ambiguity):
- Vague + Decreasing transparency
- Inconsistent messaging across channels
- Defensiveness about details
- Changes in accounting/reporting practices

**Green Flags** (Adaptive ambiguity):
- Vague + Open to questions
- "We're exploring options" with evidence of testing
- Coherent vision despite lack of specifics
- Increasing transparency over time

### For Entrepreneurs

**Don't Cross the Line**:
- Adaptive ambiguity: "We're testing multiple approaches"
- Protective ambiguity: "Our technology is proprietary" (when it doesn't exist)

**Maintain Trust**:
- Low τ OK if paired with high transparency
- Vague promises + hidden information = protective (bad)

## 🖼️ Visual Framework

```
Ambiguity Type by Intent & Outcome:

                    TRANSPARENCY
                    High    Low
                    
INTENT   Adaptive   ✓ OK    ⚠️ Risk
         τ↓        (H2)    (Could flip)
                    
         Protective ⚠️ Weak  ✗ Bad
         τ↓        defense  (Failure)
                    
    Adaptive Ambiguity = Low τ + High transparency
    Protective Ambiguity = Low τ + Low transparency
```

## ✅ Action Items for 中군님

- [ ] **Classify**: Are any ventures in your data "protective"?
- [ ] **Indicators**: Look for decreasing transparency patterns
- [ ] **Robustness**: Test H2 excluding high-risk ventures
- [ ] **Moderator**: Model intent (adaptive vs protective) as interaction

## 📚 Related Reading

**Contrast with**: [[📜Eisenberg1984_Ambiguity_Communication]] - Benign strategic ambiguity
**Parallel to**: [[📜Denis2011_EscalatingIndecision]] - Another failure mode

---

**핵심 for 필사즉생**: 
Intent matters: Low τ can be adaptive (your H2) OR protective (Cappellaro)
Need to distinguish in empirical work
Consider as boundary condition or sample selection criterion
