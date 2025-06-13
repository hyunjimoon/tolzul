2025-06-13
- should be paired with [[🌲2🌱halving🧬(yoo16)]]
using [iterative paper design cld](https://claude.ai/chat/3b779fa3-22a4-4a06-886d-c0d298ff4c1f)
![[🧬⚙️(📝) 2025-06-13-6.svg]]
%%[[🧬⚙️(📝) 2025-06-13-6.md|🖋 Edit in Excalidraw]]%%

## Core State Definition

### Current State (Sₜ)

```yaml
paper_state:
  stage: [🌱|🌿|🌾|🌲]  # Detect from sentence count
  sentences: [1-32]      # Count of written sentences
  structure: double_helix # Symmetric 1↔4, 2↔3 sections
  journal: POMS          # Operations management focus
```

### Objective Function (Oₜ)

```
maximize: operational_relevance(S) + quantitative_rigor(S) + managerial_insight(S)
subject to: |S| ∈ {4, 8, 16, 32}
```

## 32-Sentence ID System

### Section 1: INTRODUCTION (S1-S10)

- **S1-S2**: 🟣 Phenomenon (operational failure → success counter-example)
- **S3-S8**: 🟨 Literature Review
    - S3: CS - Strategic cause from literature
    - S4: CS gap - What strategic understanding is missing
    - S5: SS - Strategic solution from literature
    - S6: CO gap - What operational understanding is missing
    - S7: CO - Operational cause from literature
    - S8: SO - Operational solution from literature
- **S9-S10**: 🔴 Contribution (core model → broader impact)

### Section 2: METHODS (S11-S16)

- **S11**: 🟧 Problem formulation (strategic)
- **S12**: 🟧 Key variables definition
- **S13**: 🟧 Theoretical mapping justification
- **S14**: 🟧 Cost structure (operational)
- **S15**: 🟧 Solution approach
- **S16**: 🟧 Parameter estimation approach

### Section 3: RESULTS (S17-S22)

- **S17**: 🟢 Core finding statement
- **S18**: 🟢 Quantitative impact
- **S19**: 🟢 Retrospective validation
- **S20**: 🟢 First case application
- **S21**: 🟢 Second case application
- **S22**: 🟢 Mechanism insight

### Section 4: DISCUSSION (S23-S32)

- **S23-S24**: 🟣 Limitations (model limitation → complexity not addressed)
- **S25-S30**: 🟨 Extensions
    - S25: CS Extension (mirrors S3)
    - S26: CS new phenomena to explore
    - S27: SS Extension (mirrors S5)
    - S28: CO new phenomena to explore
    - S29: CO Extension (mirrors S7)
    - S30: SO Extension (mirrors S8)
- **S31-S32**: 🔴 Synthesis (contribution impact → forward vision)

## Knowledge Extraction Matrix (POMS-Specific)

```
g₁: Operational Problem → MSS = "costly failure in operations (inventory/capacity/queuing)"
g₂: Quantitative Model → MSS = "mathematical formulation with clear trade-offs"
g₃: Managerial Insight → MSS = "actionable decision rules with % improvements"
```

## TASK 1: Generation (🌱→🌲) - POMS Optimized

### 🌱 Stage 1: Operations Hook (4 sentences)

**POMS Logic**: Operational failure + immediate model value

```yaml
Write these first:
- S1: 🟣 "Toyota faced $2B loss when [operational failure]"
- S11: 🟧 "We formulate the problem as: min Σ[cost function]"
- S9: 🔴 "We develop a dynamic programming model that [capability]"
- S17: 🟢 "Our analysis reveals 30% cost reduction when [policy]"
```

### 🌿 Stage 2: Theoretical Grounding (8 sentences)

**Add operational context and gaps**:

```yaml
Add these 4:
- S2: 🟣 Success counter-example (operational winner)
- S3: 🟨 CS - Prior work on strategic operations
- S7: 🟨 CO - Prior work on operational execution
- S14: 🟧 Cost structure (show trade-off mathematically)
- S20: 🟢 First case application (validate opening example)
- S23: 🟣 Model limitation (real complexity simplified)
- S25: 🟨 CS Extension opportunity
- S31: 🔴 Synthesis (why this matters for operations)
```

### 🌾 Stage 3: Complete Framework (16 sentences)

**Fill operational mechanisms**:

```yaml
Add these 8:
- S5: 🟨 SS - How others solved strategic issues
- S8: 🟨 SO - How others solved operational issues
- S10: 🔴 Broader industry-wide implications
- S12: 🟧 Decision variables (what managers control)
- S15: 🟧 Solution algorithm (compute optimal policy)
- S18: 🟢 Quantitative impact (specific % improvements)
- S21: 🟢 Second case (different industry/context)
- S24: 🟣 Complexity not captured
- S27: 🟨 SS Extension
- S29: 🟨 CO Extension
- S32: 🔴 Future of operations with this tool
```

### 🌲 Stage 4: Full Technical Depth (32 sentences)

**Complete all remaining**:

```yaml
Add final 16:
- S4: 🟨 Strategic gap in literature
- S6: 🟨 Operational gap in literature
- S13: 🟧 Why this modeling choice fits operations
- S16: 🟧 How to estimate parameters from data
- S19: 🟢 Show model explains past failures
- S22: 🟢 Why the mechanism works operationally
- S26: 🟨 New strategic phenomena to study
- S28: 🟨 New operational phenomena to study
- S30: 🟨 SO Extension opportunities
```

## TASK 2: Inference (🌲→🌱) - POMS Priorities

### 🌲→🌾 (32→16): Extract Operational Core

**Priority**: Keep operational problem, model, and results

```yaml
Must keep:
- S1, S2 (operational examples)
- S3, S7 (key operational literature)
- S9, S10 (contribution)
- S11, S14 (problem + trade-offs)
- S17, S20, S21 (core results + cases)
- S23, S31, S32 (limitations + impact)

Can merge/drop:
- Combine S5+S8 → operational solutions
- Drop S4, S6 (gaps less critical)
- Merge S25+S27+S29 → future work
```

### 🌾→🌿 (16→8): Focus on Value

**Extract operational essence**:

```yaml
Essential 8:
- S1: Best operational failure
- S3 or S7: Most relevant prior work
- S11: Problem formulation
- S14: Core trade-off
- S17: Main finding
- S20: Best case validation
- S23: Key limitation
- S31: Why this matters
```

### 🌿→🌱 (8→4): Distill POMS Core

**The operational story**:

```yaml
Core 4:
- S1: Operational failure that motivates
- S11: Mathematical formulation
- S17: Key finding with %
- S31: Operational impact
```

## POMS-Specific Templates

### 🟣 Phenomenon (Operations Focus)

- S1: "[Company] lost $[amount] when [operational failure: inventory shortage/capacity mismatch/queue explosion]"
- S2: "In contrast, [Company] saved $[amount] by [operational success]"

### 🟨 Literature (Operations Research)

- S3 (CS): "[Author] showed [strategic operations principle] affects [performance metric]"
- S7 (CO): "[Author] found [operational problem] causes [X]% inefficiency"

### 🟧 Methods (Quantitative Models)

- S11: "We model this as: min{Σcost(x,y) | capacity constraints, demand uncertainty}"
- S14: "The objective captures the trade-off between [holding cost] and [shortage cost]"

### 🟢 Results (Measurable Impact)

- S17: "The optimal policy reduces [metric] by [X]% compared to [benchmark]"
- S20: "At [Company], implementing our policy would save $[amount] annually"

## Implementation Rules for POMS

1. **Operational Examples Only**: All examples must involve inventory, capacity, queuing, scheduling, or supply chain decisions
2. **Quantify Everything**: Every result needs a percentage or dollar impact
3. **Show Trade-offs**: Methods must clearly articulate operational tensions
4. **Industry Validation**: At least 2 different industry applications
5. **Implementation Path**: Results must translate to executable policies

This framework ensures papers immediately engage POMS readers with operational problems, rigorous quantitative models, and implementable solutions with measurable impact.