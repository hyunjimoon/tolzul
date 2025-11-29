---
modified:
  - 2025-11-18T15:36:38-05:00
---
```
"concurrent engineering of inference and decision module"?

"This meta-cognitive problem—changing objectives during execution—appears across 
industries (Christensen's disk drives: capacity → miniaturization). What distinguishes 
entrepreneurship is the COUPLING of three factors: (1) extreme outcome uncertainty 
(90% failure rate), (2) severe resource constraints (limited capital for experiments), 
and (3) compressed timelines (36-month Series A→B window). This forces MORE FREQUENT 
objective revision under TIGHTER constraints than established firms face."
```

### C. Layered Pairing: Marr's Dual Hierarchy

**Needs Hierarchy** (from customers):
- **Computational**: *What goal?* Reduce uncertainty in entrepreneurial decisions
- **Algorithmic**: *How to achieve?* Probabilistic programming for belief updating
- **Implementation**: *Physical realization?* Resource-rational heuristics (threshold rules)

**Solutions Hierarchy** (from suppliers):
- **Computational**: Program synthesis theory (automated inference goals)
- **Algorithmic**: Stan (HMC sampler) + Arviz (diagnostic processes)  
- **Implementation**: Operational tools (Processify, Collaborate, etc.)

**The Pairing Problem**:
This creates a 3×3 bipartite matching with hierarchical constraints:

┌─────────────────┐         ┌─────────────────┐
│ NEEDS           │         │ SOLUTIONS       │
├─────────────────┤         ├─────────────────┤
│ Computational   │ ←────→  │ Computational   │  (Goal alignment)
│ ↓ constrains    │         │ ↓ constrains    │
│ Algorithmic     │ ←────→  │ Algorithmic     │  (Process compatibility)
│ ↓ constrains    │         │ ↓ constrains    │
│ Implementation  │ ←────→  │ Implementation  │  (Practical feasibility)
└─────────────────┘         └─────────────────┘

**Within-level matching** (horizontal arrows):
- Computational ↔ Computational: Does inference goal match decision goal?
- Algorithmic ↔ Algorithmic: Can HMC process serve belief updating?
- Implementation ↔ Implementation: Do threshold rules map to operational tools?

**Cross-level dependencies** (vertical arrows):
- Computational goals → constrain algorithmic choices → constrain implementation
- Implementation constraints → feedback to algorithmic → feedback to computational

**OR Formulation**:
max Σᵢⱼ p(match_ij) · V_ij
s.t. Hierarchical consistency: If level k matched, level k+1 must be compatible
     Resource constraints: Budget for building each solution layer
     Ordering constraints: Computational before algorithmic before implementation