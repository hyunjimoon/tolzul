---
modified:
  - 2025-11-07T17:36:11-05:00
---
# 📚 Strategic Ambiguity Literature - Research Library Index

**중군님의 OIL Framework 연구를 위한 9개 핵심 논문**

---

## 🎯 Research Question Mapping

### H1: Vague promises → Lower early funding (α₁ < 0)
**지원 논문**:
- [[📜Abdallah2014_DoubleEdge_Ambiguity]]: Double edge - early phase ambiguity challenges
- 📜 Eisenberg1984: Communication uncertainty penalty
- 📜 Sillince2012: Rhetorical construction → measurable precision

### H2: Vague promises → Higher later success (β₁ > 0)  
**지원 논문**:
- 📜 Padgett1993: Robust action enables coalition formation
- 📜 Ferraro2015: Pragmatic ambiguity for exploration
- 📜 Eisenberg1984: Unified diversity mechanism

### Boundary Conditions & Moderators
**지원 논문**:
- 📜 Cappellaro2020: Intent matters (adaptive vs. protective)
- 📜 Denis2011: Timing of commitment (escalating indecision)
- 📜 Grodal2017: Governance quality moderates H2
- 📜 Reinecke2025: Temporal trajectory (not static precision)

---

## 📖 Recommended Reading Order

### Phase 1: Foundations (읽어야 할 순서)
1. **📜 Eisenberg1984** - 기초 이론 (가장 먼저)
   - Strategic ambiguity의 foundational concept
   - Unified diversity mechanism
   - 30분 예상

2. **📜 Padgett1993** - 고전 case
   - Robust action의 empirical demonstration  
   - Medici case: τ 전략의 역사적 증거
   - 1시간 예상

3. **📜 Abdallah2014** - H1 & H2 직접 연결
   - Double edge: 왜 early/late effects가 다른가
   - OIL framework의 이론적 정당화
   - 45분 예상

### Phase 2: Mechanisms & Extensions (두 번째 독서)
4. **📜 Ferraro2015** - Grand challenges extension
   - 왜 low τ가 OPTIMAL인가 (epistemic argument)
   - Wicked problems → high V
   - 45분 예상

5. **📜 Sillince2012** - Operationalization
   - 어떻게 τ를 측정할 것인가
   - Rhetorical analysis → computational measurement
   - **CRITICAL for empirical paper**
   - 1시간 예상

### Phase 3: Boundary Conditions (세 번째 독서)  
6. **📜 Denis2011** - Failure mode
   - Escalating indecision: low τ too long
   - Timing of commitment
   - 45분 예상

7. **📜 Grodal2017** - Governance moderator
   - Goal displacement risk
   - β₁ conditional on governance
   - 1시간 예상

8. **📜 Cappellaro2020** - Dark side
   - Protective vs. adaptive ambiguity
   - Intent as boundary condition
   - 45분 예상

### Phase 4: Temporal Dynamics (최종 독서)
9. **📜 Reinecke2025** - Trajectory model
   - Constructive ambiguity → escalating commitment
   - τ dynamics, not static τ
   - **CHANGES the empirical model** (Δτ not just τ₀)
   - 1.5시간 예상

**Total reading time**: ~8 hours

---

## 🔄 Three Key Theoretical Contributions

### 1. **Mechanism** (how H2 works)
- Eisenberg1984: Unified diversity
- Padgett1993: Network flexibility  
- Ferraro2015: Exploration preservation

**Your addition**: Bayesian formalization
- Low τ → Broad posterior → Diverse stakeholders
- Coalition breadth → Resource access → Success

### 2. **Boundary Conditions** (when H2 fails)
- Denis2011: Timing failure (stay low too long)
- Grodal2017: Governance failure (displacement)
- Cappellaro2020: Intent failure (concealment)

**Your addition**: Optimal Ignorance Level
- τ* = max{0, √(V/4i) - 1}
- Below τ*: escalating indecision
- Above τ*: premature commitment
- At τ*: optimal flexibility

### 3. **Temporal Dynamics** (how τ evolves)
- Abdallah2014: Double edge over lifecycle
- Reinecke2025: Trajectory from ambiguity to commitment

**Your addition**: Dynamic OIL
- τ*(t) not constant
- Optimal path: Low → Medium → High
- Success = following optimal trajectory

---

## 🎨 Visual Synthesis (for qualifying exam)

```
Theoretical Framework:

                    Eisenberg (1984)
                    Unified Diversity
                          |
                          v
    Padgett (1993) ←→ [OIL Framework] ←→ Ferraro (2015)
    Robust Action        τ* = f(V,i)    Grand Challenges
                          |
                          v
                    Abdallah (2014)
                    Double Edge
                          |
              /-----------+-----------\
              |                       |
        Early Phase              Late Phase
        (H1: α₁ < 0)            (H2: β₁ > 0)
              |                       |
              v                       v
    Sillince (2012)          Moderators:
    Measurement              - Denis (2011): Timing
                            - Grodal (2017): Governance  
                            - Cappellaro (2020): Intent
                                    |
                                    v
                            Reinecke (2025)
                            Trajectory Model
```

---

## 🔬 Empirical Strategy Implications

### From Sillince2012:
**Measure τ through linguistic analysis**:
```python
τ = (concrete + specific + definitive) / (abstract + hedge + modal)
```

### From Reinecke2025:
**Need trajectory measurement**:
- τ₀: Initial precision (company descriptions at founding)
- τ₁: Precision at first funding round  
- τ₂: Precision at later rounds
- Δτ = τ₂ - τ₀: Precision evolution

### New Model Specification:
```
Early Funding = α₀ + α₁·τ₀ + controls
Later Success = β₀ + β₁·τ₀ + β₂·Δτ + β₃·(τ₀ × Governance) + controls
```

Where Governance could be:
- Board independence
- Investor quality
- Strategic clarity metrics

---

## 📊 Table/Figure Ideas from Literature

### Table 1: Theoretical Synthesis
| Paper | Mechanism | Boundary | Temporal |
|-------|-----------|----------|----------|
| Eisenberg1984 | ✓ | | |
| Padgett1993 | ✓ | | |
| Abdallah2014 | ✓ | | ✓ |
| Ferraro2015 | ✓ | | |
| Denis2011 | | ✓ | ✓ |
| Grodal2017 | | ✓ | |
| Cappellaro2020 | | ✓ | |
| Reinecke2025 | | | ✓ |
| Sillince2012 | [Operationalization] | | |

### Figure 1: Temporal Model (inspired by Reinecke2025)
```
Promise Precision (τ)
      ^
      |           Optimal Path
      |          /
  τ₂  |         / (Tesla)
      |        /
  τ₁  |       /
      |      /_____ Too slow (Better Place)
  τ₀  |_____/     
      |
      +-------------------------> Time
      t₀    t₁         t₂
```

### Figure 2: Double Edge (Abdallah2014 + your framework)
```
Effect Size
      ^
      |    H2: β₁ > 0
      |      ___
      |     /   \
    0 +----/-----\-------
      |   /       \
      |  /         \  H1: α₁ < 0
      | /___________\_____
      +-------------------------> Venture Stage
      Early                 Late
      (Funding)         (Success)
```

---

## 🐅 이순신 전략과의 연결

각 논문을 이순신의 4대 전투에 매핑:

1. **옥포해전** (초기 승리): Eisenberg1984, Padgett1993
   - 기초 확립
   - Robust action의 증명

2. **한산도대첩** (결정적 승리): Abdallah2014, Ferraro2015  
   - 핵심 메커니즘
   - Double edge + Grand challenges

3. **부산포해전** (지속적 압박): Denis2011, Grodal2017, Cappellaro2020
   - Boundary conditions
   - 실패 메커니즘 이해

4. **명량해전** (최후의 승리): Reinecke2025
   - 시간 동학
   - Trajectory model

**Sillince2012** = 전략 기록 (측정 방법)

---

## ✅ Action Items for 중군님

### Immediate (이번 주):
1. Read Eisenberg1984 (30분) - conceptual foundation
2. Read Abdallah2014 (45분) - H1/H2 connection
3. Skim Sillince2012 (30분) - measurement strategy

### Next Week:
4. Deep read Reinecke2025 (1.5시간) - **may change your model**
5. Read Sillince2012 fully (1시간) - operationalization
6. Draft measurement section using Sillince framework

### Following Week:
7. Read boundary condition papers (Denis, Grodal, Cappellaro)
8. Revise hypotheses based on moderators
9. Update empirical strategy for τ trajectory

---

## 📌 Critical Insights for Charlie & Scott

1. **For Charlie** (Operations):
   - Reinecke2025: Dynamic τ* optimization  
   - Denis2011: Commitment timing
   - Connection to real options theory

2. **For Scott** (Strategy):
   - Padgett1993: Network effects of ambiguity
   - Ferraro2015: Grand challenges applicability  
   - Grodal2017: Field-level implications

3. **For Both**:
   - Sillince2012: Computational measurement
   - Abdallah2014: Theoretical integration
   - Your contribution: Bayesian formalization

---

**Created**: 2025-11-05
**Status**: Ready for review
**Location**: `/Users/hyunjimoon/tolzul/Space/Lab/`
