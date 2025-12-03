2025-05-19, 2025-05-24
using [optimizing dual-metric research system cld](https://claude.ai/chat/d1dbed2c-8666-40d1-b967-d3cba525e086)
productize painpoints, using 👥knowledge, 🗄️structure, 💸evaluation
- spawned to [[🗄️how(🫀need,🧠sol)(2025mit startup)]]

# MSS Bottleneck Optimizer (v2.1)

## Core Notation
$$S_t = \{(s, p_s, \Delta P_s, c_s)\}_{s=1}^5$$
where:

| Variable | Definition                          | Range/Units       |
|----------|-------------------------------------|-------------------|
| $s$      | Section ID                          | 1 (Intro) → 5 (Conclusion) |
| $p_s$    | Current quality score               | [0.0, 1.0]        |
| $\Delta P_s$ | Improvement potential            | 0.8 - $p_s$       |
| $c_s$    | Improvement cost                    | person-hours      |

## Evaluation Engine
1. **Priority Score**  
   $$\rho_s = \frac{\Delta P_s}{c_s}$$
2. **Bottleneck ID**  
   $$s^* = \underset{s}{\arg\max}(\rho_s)$$

## Section Mapping
| $s$ | Name         | Evaluator        | Scoring Focus                   |
| --- | ------------ | ---------------- | ------------------------------- |
| 1   | Introduction | [[👥(📜🪢)cmo]]  | Business impact, case relevance |
| 2   | Methods      | [[🗄️(📜🪢)cto]] | Technical rigor                 |
| 3   | Results      | [[🗄️(📜🪢)cto]] | Analysis depth                  |
| 4   | Discussion   | [[👥(📜🪢)cmo]]  | Actionable insights             |
| 5   | Conclusion   | [[👥(📜🪢)cmo]]  | Implementation clarity          |

## Applied Examples

### Example 1: Weak Methods Section
```python
# Input
s = 2  # Methods
p_s = 0.3  # Basic equations but no stats
c_s = 4  # hours needed

# Calculation
ΔP_s = 0.8 - 0.3 = 0.5
ρ_s = 0.5 / 4 = 0.125

# Output
"Bottleneck": {
  "section": 2,
  "action": "CTO: Add statistical validation (4hr)",
  "expected_gain": "0.3→0.8"
}
```

### Example 2: Strong Intro, Weak Discussion

```python
# Input
s = 4  # Discussion
p_s = 0.4  # Lacks concrete recommendations
c_s = 2  # hours needed

# Calculation
ΔP_s = 0.8 - 0.4 = 0.4
ρ_s = 0.4 / 2 = 0.2  # Higher priority than Example 1

# Output
"Bottleneck": {
  "section": 4,
  "action": "CMO: Add manager action steps (2hr)",
  "expected_gain": "0.4→0.8"
}

```


# Execution Template
```json
{
  "current_state": [
    {"s": 1, "p_s": 0.6, "c_s": 1.5},
    {"s": 2, "p_s": 0.3, "c_s": 4}
  ],
  "output": {
    "bottleneck_section": 2,
    "recommended_action": "CTO: 4hr technical upgrade",
    "priority_ratio": 0.125
  }
}
```
