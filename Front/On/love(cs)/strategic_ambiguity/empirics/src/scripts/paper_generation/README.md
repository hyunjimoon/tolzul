# 전라좌수군 견리사의 군령
## Paper Generation System for PhD Thesis

> 견리사의 (見利思義): 이익을 보면 의로움을 생각하라
> 필사즉생 (必死卽生): 죽으려 하면 살 것이요, 살려 하면 죽을 것이다

---

## Directory Structure

```
paper_generation/
├── README.md                    # This file
├── __init__.py                  # Module initialization
├── generate_all_chapters.py     # Main entry point
├── paper_magnet.py              # Paper search system
├── chap1_introduction.py        # 起 정운
├── chap2_theory.py              # 承 권준
├── chap3_empirics.py            # 轉 김완 + 나대용
├── chap4_discussion.py          # 結 어영담
│
├── P1_vagueness/                # P1: U-Shape Analysis
│   ├── theory.md                # 권준의 이론 정리
│   ├── empirics.py              # OLS/Logit 분석 코드
│   ├── figures.py               # Figure 생성 코드
│   └── output/                  # 생성된 Figure (.png)
│
├── P2_trap/                     # P2: Competency Trap
│   ├── theory.md                # 권준의 이론 정리
│   ├── simulation.py            # Bayesian 시뮬레이션 코드
│   ├── figures.py               # Figure 생성 코드
│   └── output/                  # 생성된 Figure (.png)
│
├── P3_newsvendor/               # P3: Newsvendor Optimization
│   ├── theory.md                # 권준의 이론 정리
│   ├── model.py                 # Newsvendor 모델 코드
│   ├── figures.py               # Figure 생성 코드
│   └── output/                  # 생성된 Figure (.png)
│
└── output/                      # Generated markdown files
    ├── chap1_introduction.md
    ├── chap2_theory.md
    ├── chap3_empirics.md
    └── chap4_discussion.md
```

---

## Quick Start

```bash
# Generate all chapters
python generate_all_chapters.py

# Check status
python generate_all_chapters.py --status

# Generate specific chapter
python generate_all_chapters.py --chapter 1

# View expectation management
python generate_all_chapters.py --expect

# Search for relevant papers
python paper_magnet.py --paper P2
```

---

## The Fleet (전라좌수군)

| Chapter | 한자 | Commander | Virtue | Bayesian Role |
|---------|------|-----------|--------|---------------|
| **1. Introduction** | 起 | 정운 🐢 | 利 (Speed) | Prior π(θ) |
| **2. Theory** | 承 | 권준 🐅 | 思 (Structure) | Likelihood π(y\|θ) |
| **3. Empirics** | 轉 | 김완 🐙 + 나대용 🐅 | 義 (Criticism) | Calibration |
| **4. Discussion** | 結 | 어영담 👾 | 見 (Observation) | Generator |

---

## Three Papers (P1/P2/P3)

Each chapter generates content for three papers simultaneously:

| Paper | Emoji | Title | Domain Focus |
|-------|-------|-------|--------------|
| **P1** | ✌️ | U-Shape: When Vagueness Pays | Technology |
| **P2** | 🦾 | Competency Trap: When Success Kills Options | Organization |
| **P3** | 🤹 | Execution Gap: Optimal Number of Options | Competition |

---

## Paper Magnet (논문 자석)

Search for theoretically resonant papers from `/Users/hyunjimoon/tolzul/Space/Library/1논문용/`:

```bash
# Top resonant papers
python paper_magnet.py

# Papers for specific theory
python paper_magnet.py --paper P1   # U-Shape
python paper_magnet.py --paper P2   # Competency Trap
python paper_magnet.py --paper P3   # Execution Gap

# Scott-Charlie tension papers
python paper_magnet.py --tension

# Keyword search
python paper_magnet.py --keyword "real option"
```

---

## Workflow (견리사의 순환)

```
利 → 思 → 義 → 見 → 利
↓
정운(Draft) → 권준(Structure) → 김완(Verify) → 어영담(Record)
     ↑                                              ↓
     └──────────── Generator (다음 Prior) ←─────────┘
```

---

## Output Format

Each generated markdown file contains:
- P1 section (U-Shape)
- P2 section (Competency Trap)
- P3 section (Execution Gap)
- Cross-Synthesis section

---

## Legacy Code

Old code has been archived to:
`/Users/hyunjimoon/tolzul/Front/On/love(cs)/strategic_ambiguity/empirics/docs_archive/legacy_paper_generation/`

---

## P1/P2/P3 Empirics & Figures (나대용 임무)

### Quick Start: Generate All Figures

```bash
# P1: U-Shape Analysis
cd P1_vagueness
python empirics.py      # Run OLS/Logit analysis
python figures.py       # Generate figures

# P2: Competency Trap
cd P2_trap
python simulation.py    # Run Bayesian simulation
python figures.py       # Generate figures

# P3: Newsvendor
cd P3_newsvendor
python model.py         # Run newsvendor optimization
python figures.py       # Generate figures
```

### P1: U-Shape - When Vagueness Pays

**Variables:**
- `vagueness_score (V)`: 0.6 * S_cat + 0.4 * S_concdef
- `survival`: Binary (survived 3+ years)
- `funding`: Log(total funding amount)
- `exercisability`: Hardware/Software classification

**Models:**
- H1: OLS regression `log(Funding) = β₀ + β₁V + β₂V² + controls`
- H2: Logit with interaction `Pr(Survival) = Λ(β₀ + β₁V + β₂H + β₃(V×H) + ...)`

**Output Figures:**
- `P1_u_shape_survival.png`: U-shape survival vs vagueness
- `P1_hw_sw_comparison.png`: Hardware vs Software interaction
- `P1_coefficient_table.png`: Coefficient table visualization

### P2: Competency Trap - When Success Kills Options

**Variables:**
- `prior (μ₀, σ₀)`: Initial beliefs about current path
- `evidence_strength`: Strength of disconfirming signal
- `believer_ratio`: Proportion of like-minded investors
- `switching_threshold (τ)`: Evidence threshold for pivot

**Model:** Bayesian update simulation
```
μ_post = (σ_e² * μ₀ + σ₀² * y) / (σ₀² + σ_e²)
τ = f(σ₀, believer_ratio)
```

**Output Figures:**
- `P2_belief_lockin_diagram.png`: μ,σ → threshold heatmap
- `P2_pivot_threshold_curve.png`: Pivot threshold vs σ curve
- `P2_case_comparison.png`: Waymo vs Comma.ai case study

### P3: Newsvendor - Optimal Number of Options

**Variables:**
- `D`: Demand ~ Poisson(λ) or Normal(μ,σ²)
- `C`: Commitment cost
- `F`: Flexibility cost
- `CR`: Commitment ratio = C / (C + F)

**Model:** Newsvendor optimization
```
k* = μ_D + σ_D * Φ⁻¹(CR)
```

**Output Figures:**
- `P3_cr_kstar_curve.png`: CR vs k* policy curve
- `P3_sensitivity_heatmap.png`: Sensitivity to σ(D)
- `P3_industry_calibration.png`: Industry-specific CR calibration
- `P3_unified_framework.png`: P1/P2/P3 unified on CR-k* plane

---

## Requirements

```bash
pip install numpy pandas scipy statsmodels matplotlib
```

## Reproducibility

- All scripts use `SEED = 42` for reproducibility
- Dummy data generated internally (no external data required)
- Relative paths used for output

---

*통제사: 이순신 문현지 (Moon)*
*공병대장: 나대용 (Builder)*
