---
collection:
  - "[[Space/Lab/Papers]]"
author_ids:
  - Stine Grodal
  - Siobhan O'Mahony
field:
  - 🎯str  # Strategy
  - 🌍env  # Field-level
  - 🐙ops  # Operations
thesisPaper: U
thesisChapter: T
year: 2017
rank: 8
research_stream:
  - Strategic Ambiguity
  - Field Mobilization
  - Goal Displacement
  - Grand Challenges
tags:
  - goal-displacement
  - field-mobilization
  - governance
  - grand-challenges
  - empirical-field-study
  - boundary-conditions
created: 2025-11-05
modified:
  - 2025-11-05T00:00:00-05:00
connections:
  extends:
    - "[[📜Ferraro2015_GrandChallenges_RobustAction]]"  # Grand challenges + ambiguity
    - "[[📜Eisenberg1984_Ambiguity_Communication]]"  # Unified diversity
  applied_in:
    - Field-level strategy literature
  related_to:
    - "[[📜Abdallah2014_DoubleEdge_Ambiguity]]"  # Temporal dynamics
    - "[[📜Denis2011_EscalatingIndecision]]"  # Organizational failure
---

# 📜 How Does a Grand Challenge Become Displaced?

## 🗄️1: Core Framework (Q&A Format)

| Section | 🔐Research Question | 🔑Key Message & Framework | 📐Formal Concept | 🧱Literature Brick |
|---------|-------------------|-------------------------|-----------------|-------------------|
| **Main Thesis** | Why do some ambiguous challenges get displaced? | Low τ enables INITIAL mobilization BUT can lead to GOAL DISPLACEMENT without governance | **Duality**: τ ↓ → Mobilization + Displacement risk | • Maguire et al. (2004) field creation<br>• Zietsma & Lawrence (2010) boundaries |
| **Mechanism** | How does displacement happen? | Multiple interpretations → Divergent actions → Original goal sidetracked by sub-goals | **Goal Drift**: τ stays low, goals diverge | • Suchman (1995) legitimacy<br>• Battilana & D'Aunno (2009) change |
| **Moderator** | When is displacement avoided? | Strong GOVERNANCE structures manage ambiguity → Maintain coherence despite diverse interpretations | **Governance Quality** moderates τ effects | • Ostrom (1990) governance<br>• Ansell & Gash (2008) collaboration |

## 🗄️2: Theoretical Position

### Extends
- [[📜Ferraro2015_GrandChallenges_RobustAction]]: Grand challenges need ambiguity → But can be displaced
- [[📜Eisenberg1984_Ambiguity_Communication]]: Unified diversity → Can become "fractured diversity"

### Related To
- [[📜Abdallah2014_DoubleEdge_Ambiguity]]: Productive→Destructive timing
- [[📜Denis2011_EscalatingIndecision]]: Organizational-level displacement

### Critical for Your Research
**KEY MODERATOR**: Governance quality moderates H2 (β₁ > 0)

## 🗄️3: Ambiguity Outcomes by Governance

| Governance Quality | Low τ (Ambiguous Challenge) | High τ (Clear Challenge) |
|-------------------|---------------------------|------------------------|
| **Strong** | ✓ Coalition + Coherence → Success | ✓ Focused effort → Success |
| **Weak** | ✗ Coalition + Displacement → Failure | Mixed (narrow focus) |

## 💭 Critical Insights for OIL Framework

### CRITICAL MODERATOR for H2

**Your H2**: Vague promises (low τ₀) → Higher later success (β₁ > 0)

**Grodal & O'Mahony add**: **CONDITIONAL on governance quality**

### Mathematical Formulation

```
Later Success = β₀ + β₁·τ₀ + β₂·Governance + β₃·(τ₀ × Governance)

Where:
- β₁ might be ≤ 0 (unconditional effect can be negative)
- β₂ > 0 (governance directly helps)
- β₃ > 0 (INTERACTION: low τ more beneficial WITH strong governance)

Interpretation:
- Low τ + Strong governance → High success (β₁ + β₃·High)
- Low τ + Weak governance → Low success (β₁ + β₃·Low)
```

### Two Pathways from Low τ

**Positive Path** (Strong Governance):
```
Low τ → Diverse coalition forms
      ↓
Strong governance maintains coherence
      ↓
Diverse coalition + Aligned action
      ↓
Success (H2: β₁ > 0)
```

**Negative Path** (Weak Governance):
```
Low τ → Diverse coalition forms
      ↓
Weak governance → Interpretations diverge
      ↓
Goal displacement (original purpose lost)
      ↓
Failure (displacement)
```

## 🎯 Research Implications

### For H2 Refinement

**Unconditional H2** may find:
- β₁ ≈ 0 or weak positive

**Why?**: Mixing ventures with strong and weak governance

**Conditional H2** should find:
- β₁ + β₃·Governance > 0 for strong governance
- β₁ + β₃·Governance < 0 for weak governance

### Governance Measurement

**What constitutes "strong governance" for ventures?**

```python
governance_quality = f(
    board_independence,      # Independent directors?
    board_experience,        # Relevant expertise?
    strategic_clarity,       # Clear milestones?
    stakeholder_alignment,   # Regular alignment meetings?
    decision_processes,      # Formal decision mechanisms?
    accountability           # Clear responsibilities?
)
```

**Observable Proxies**:
- Board composition (independence, diversity)
- Investor quality (tier 1 VCs have governance expertise)
- Strategic planning artifacts (OKRs, milestones)
- Meeting frequency (board, strategic reviews)

### Empirical Test

```python
# Test interaction
model = """
success ~ tau_0 + governance_quality + 
          tau_0:governance_quality + 
          controls
"""

# Predict:
# Simple slope for high governance: positive
# Simple slope for low governance: negative or zero
```

### Sample Split Analysis

```python
# Split by governance quality
high_gov = ventures.loc[ventures.governance > median]
low_gov = ventures.loc[ventures.governance < median]

# Test H2 separately
model_high = "success ~ tau_0 + controls"  # Expect β₁ > 0
model_low = "success ~ tau_0 + controls"   # Expect β₁ ≤ 0

# Compare coefficients
```

## 🔬 Practical Implications

### For Entrepreneurs (Design Choice)

**If you choose low τ (vague promise)**:
- MUST invest in governance structures
- Regular strategic alignment sessions
- Clear decision-making processes
- Don't just "stay flexible" - manage flexibility

**If governance weak**:
- Consider higher τ (more specific promise)
- Reduces need for coordination
- Narrower coalition but more coherent

### For Investors (Due Diligence)

**Red Flag Combination**:
- Vague vision (low τ) 
- + Weak governance
- = High displacement risk

**Green Light Combination**:
- Vague vision (low τ)
- + Strong governance
- = Coalition + Coherence → Potential success

**Investment Decision**:
```
If (tau_low AND governance_weak):
    → Either: Require governance improvements as condition
    → Or: Pass on investment (displacement risk)
    
If (tau_low AND governance_strong):
    → Proceed (can manage ambiguity)
```

## 🖼️ Visual Framework

```
Goal Displacement Model:

Initial State (t=0):
    Ambiguous Challenge (low τ)
           ↓
    Diverse Coalition Forms
           |
           |----→ [GOVERNANCE]
           |
    Strong              Weak
      ↓                  ↓
  Managed Diversity   Fractured Diversity
      ↓                  ↓
  Coherent Action    Displaced Goals
      ↓                  ↓
   SUCCESS            FAILURE
   (H2 works)         (H2 fails)
```

### Displacement Process

```
Time →

t=0:  Single ambiguous challenge
      "Improve energy sustainability"
      
t=1:  Multiple interpretations emerge
      "Solar" vs "Wind" vs "Efficiency" vs "Behavior change"
      
t=2:  With Strong Governance:
      All interpretations coordinated
      → Comprehensive approach → Success
      
      With Weak Governance:
      Interpretations compete
      → Original goal lost → Displacement
```

## 🗺️ Examples from Paper

### 1. **Energy Challenge**
- **Initial** (low τ): "Address energy sustainability"
- **Divergence**: Solar advocates vs efficiency advocates
- **Strong Governance**: Both pursued in coordinated way
- **Weak Governance**: Groups compete, original goal displaced

### 2. **Healthcare Access**
- **Initial** (low τ): "Improve healthcare access"
- **Divergence**: Quality vs Cost vs Coverage
- **Displacement**: Focus shifts to cost reduction only
- **Result**: Original broad goal displaced by narrow sub-goal

## ✅ Action Items for 中군님

- [ ] **Measure**: Governance quality for 29 ventures
- [ ] **Test Interaction**: τ₀ × Governance → Success
- [ ] **Expect**: H2 (β₁ > 0) ONLY for strong governance ventures
- [ ] **Robustness**: Sample split analysis by governance level

## 📚 Related Reading

**Before**: [[📜Ferraro2015_GrandChallenges_RobustAction]] - Ambiguity needed for grand challenges
**This Paper**: But needs governance to avoid displacement
**After**: Apply to your venture data

---

**핵심 for 필사즉생**: 
Governance is THE moderator for H2
Low τ₀ → Success ONLY WITH strong governance
Without governance: Low τ₀ → Goal displacement → Failure
Must measure and control for governance quality in empirical tests
