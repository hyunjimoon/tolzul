# P1: U-Shape - When Vagueness Pays

## Core Theory: Signaling x Real Options

### 권준 🐅 (承 - Structure Builder)

---

## 1. Theoretical Foundation

### 1.1 Information Economics: Vagueness as Adverse Selection

**Akerlof (1970)** "Market for Lemons" predicts that information asymmetry leads to adverse selection.
**Spence (1973)** signaling theory: costly signals separate high-types from low-types.

**However**, this perspective overlooks **strategic flexibility**.

### 1.2 Real Options: Vagueness as Strategic Flexibility

**McGrath (1997)** advocated for sequential commitments under uncertainty.
**Kogut & Kulatilaka (2001)**: By deferring specification, entrepreneurs retain the right to pivot.

**However**, real options theory implicitly assumes **costless switching** - valid for software but not for hardware.

### 1.3 Modularity Theory: When is Flexibility Valuable?

**Baldwin & Clark (2000)**: Modularity = degree to which components can be separated and recombined.
**Ethiraj & Levinthal (2004)**: Modularity's benefits depend on landscape ruggedness.

---

## 2. Hypotheses

### H1: U-shaped relationship
Vagueness has U-shaped relationship with survival: `V(1-V)` coefficient > 0

### H2: Modularity moderates
- **H2a (Software)**: High modularity → vagueness positive (cheap pivots)
- **H2b (Hardware)**: Low modularity → vagueness negative (costly pivots)

---

## 3. Key Variables

| Variable | Symbol | Definition |
|----------|--------|------------|
| Vagueness Score | `V` | `0.6 * S_cat + 0.4 * S_concdef` |
| Survival | `Y` | Binary: survived 3+ years |
| Funding | `F` | Log(total funding amount) |
| Exercisability | `E` | Modularity index (HW/SW) |

### Vagueness Score Formula
```
V_i = 0.6 * S_cat(i) + 0.4 * S_concdef(i)

where:
- S_cat: Categorical term density ("solutions", "platform", etc.)
- S_concdef: Concreteness deficit (1 - Brysbaert norms)
```

---

## 4. Empirical Specifications

### H1 Model (OLS):
```
log(Funding)_i = β₀ + β₁V_i + β₂V_i² + γ'X_i + δ_s + θ_t + ε_i
```

### H2 Model (Logit with interaction):
```
Pr(Survival_i = 1) = Λ(β₀ + β₁V_i + β₂H_i + β₃(V_i × H_i) + ...)
```

Where:
- `V_i`: Vagueness score (z-standardized)
- `H_i`: Hardware indicator (1 = hardware, 0 = software)
- `X_i`: Controls (age, size, sector)
- `δ_s, θ_t`: Sector and time fixed effects

---

## 5. Expected Results

| Hypothesis | Expected Sign | Interpretation |
|------------|--------------|----------------|
| H1: β₁ | Negative | Base vagueness penalty |
| H1: β₂ | Positive | U-shape (extremes outperform) |
| H2: β₃ | Negative | Hardware amplifies penalty |

---

*Commander: 권준 🐅 | Virtue: 思 (Structure) | Bayesian Role: Likelihood π(y|θ)*
