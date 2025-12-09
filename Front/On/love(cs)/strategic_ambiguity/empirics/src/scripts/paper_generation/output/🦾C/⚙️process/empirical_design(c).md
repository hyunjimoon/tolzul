---
modified:
  - 2025-12-04T15:00:00-05:00
status: consolidated-v2
---
# 🦾C Empirical Design - The Cruel Optimism of Commitment

## Vision Alignment

```
✌️U (Distribution D)  →  "어떤 미래가 가능한가?" (Signal vs Projection)
         ↓ informs
🦾C (Costs C, F)      →  "옵션 유지/포기 비용은?" (Commitment Trap)  ← THIS PAPER
         ↓ feeds
🤹N (Optimum k*)      →  "몇 개 옵션이 최적인가?" (Pure vs Mixture)
```

**핵심 질문**: 옵션 포기 비용(Cost of Commitment)을 어떻게 측정하는가?

---

## Data Infrastructure

### Primary Dataset: `vagueness_timeseries.nc` + `.parquet`

| Attribute | Value |
|:---|:---|
| **Companies** | 408,784 |
| **Years** | 2021, 2023, 2024, 2025 (4 snapshots) |
| **Panel Structure** | Balanced (all companies have all years) |
| **Total Observations** | 1,635,136 company-year records |
| **File Size** | ~65 MB (NetCDF) + ~140 MB (Parquet with text) |

### Key Variables

| Variable | Description |
|:---|:---|
| `V` | Vagueness score [0-100] via HybridVaguenessScorerV2 |
| `delta_V` | ΔV = V_t - V_{t-1} (year-over-year change) |
| `abs_delta_V` | \|ΔV\| = Strategic flexibility measure |
| `total_delta_V` | V_2025 - V_2021 (cumulative drift) |
| `first_financing_size` | Early funding amount (M$) |
| `total_raised_2025` | Cumulative funding by 2025 |
| `funding_growth` | total_raised_2025 / first_financing_size |

### ΔV Time Windows (Not Just Scalar!)

| Window | Period | Interpretation |
|:---|:---|:---|
| `delta_V_1` | 2021→2023 | Early exploration phase |
| `delta_V_2` | 2023→2024 | Mid-course adjustment |
| `delta_V_3` | 2024→2025 | Late stabilization |

---

## Core Findings (Confirmed)

### Finding 1: Lock-in Effect (ρ = -0.117***)

**More early funding → Less strategic flexibility**

```
Early Funding Decile    Mean |ΔV|
1 (Lowest)              4.1
2                       4.1
3                       3.9
...
9                       3.2
10 (Highest)            3.7
```

Spearman correlation: ρ = -0.117, p < 0.001

### Finding 2: Escape Velocity vs Golden Cage

| Path | Definition | Median Funding Growth |
|:---|:---|:---:|
| **Escape Velocity** | Low Early Funding + High \|ΔV\| | **4.7×** |
| **Golden Cage** | High Early Funding + Low \|ΔV\| | **1.4×** |
| **Ratio** | | **3.4× better** |

### Finding 3: Multi-Variable Lock-in

| Variable | Spearman r | Interpretation |
|:---|:---:|:---|
| Early Funding | -0.117*** | Funding LOCKS |
| Employees | -0.075*** | Team size LOCKS |
| Valuation | -0.069*** | Valuation LOCKS |
| **Company Age** | **-0.257***| **Age LOCKS most strongly** |
| Investors | +0.122*** | More investors = MORE flexible (surprising!) |

### Finding 4: Pivot Timing Matters

| Pattern | Definition | Mean Funding Growth |
|:---|:---|:---:|
| **Early Pivot** | Max \|ΔV\| in 2021-23 | **417×** |
| Mixed | No dominant window | 125× |
| Late Pivot | Max \|ΔV\| in 2024-25 | 350× |

**Insight**: 빨리 피봇하는 게 최선!

---

## Research Questions (Prioritized)

### 🥇 Priority 1: Cohort Analysis - Cost of Commitment

**Question**: "성공한 회사들 중, 많이 피봇한 회사는 초기 결핍을 경험했는가?"

**인생 비유**:
> "나중에 잘 된 사람들 중, positioning을 많이 바꿨던 사람은 어릴 적 결핍을 경험했던 사람?"

이것은 **대기만성**(late bloomer without conditioning)이 아니라,
**Double-conditioned counterfactual**:
1. 성공 조건 (later-stage funding 받음)
2. 유연성 관찰 (|ΔV| 측정)
3. 질문: 초기 결핍이 있었나?

**Why Priority 1?**
- Directly measures **Cost of Commitment (C)**
- Controls for survivorship bias via cohort conditioning
- Clear causal story: Deprivation → Low switching cost → Flexibility → Success

#### Counterfactual Framework

$$
\text{Cost of Commitment}(f) = \mathbb{E}[Y_{2025} \mid F_{2021} = f, |\Delta V| < \text{med}] - \mathbb{E}[Y_{2025} \mid F_{2021} = f, |\Delta V| > \text{med}]
$$

Where:
- $Y_{2025}$ = Later funding (outcome)
- $F_{2021}$ = Early funding (conditioning variable)
- $|\Delta V|$ = Strategic flexibility (treatment)

**Interpretation**:
| Cost | Meaning |
|:---|:---|
| **Cost > 0** | Locked companies underperform → Commitment hurts |
| **Cost < 0** | Locked companies outperform → Commitment helps (consistency value) |
| **Cost ≈ 0** | Flexibility doesn't matter |

#### Cohort Definitions

| Cohort | Definition | Purpose |
|:---|:---|:---|
| **2021→2023** | Early VC in 2021, Later VC by 2023 | Short-term flexibility payoff |
| **2021→2025** | Early VC in 2021, Later VC by 2025 | Long-term flexibility payoff |

#### Implementation

```python
def estimate_commitment_cost(df, funding_bin):
    """
    Measure |ΔV| effect on later funding,
    conditioned on same early funding level.
    """
    cohort = df[df['funding_bin'] == funding_bin]
    delta_v_median = cohort['abs_delta_V'].median()

    flexible = cohort[cohort['abs_delta_V'] > delta_v_median]
    locked = cohort[cohort['abs_delta_V'] <= delta_v_median]

    # Counterfactual difference
    cost = locked['later_funding'].mean() - flexible['later_funding'].mean()
    return cost  # Negative = commitment hurts

# Each funding level의 commitment cost
for funding_level in ['Q1_Low', 'Q2', 'Q3', 'Q4_High']:
    cost = estimate_commitment_cost(df, funding_level)
    print(f"Cost of Commitment at {funding_level}: {cost:.2f}")
```

#### Expected Visualization

```
                Cost of Commitment by Early Funding Level

    Cost
     ↑
     │                                          ████
     │                              ████        ████
     │                  ████        ████        ████
     │      ████        ████        ████        ████
     0 ─────────────────────────────────────────────────
     │
     └──────────────────────────────────────────────────→
           Q1(Low)      Q2          Q3        Q4(High)
                     Early Funding Level

    해석: High early funding에서 commitment cost가 가장 크다
         = 돈 많이 받으면 경직될 때 손해가 더 크다
```

### 🥈 Priority 2: Direction of Pivot (ΔV Sign)

**Question**: "성공한 회사들은 더 구체화(ΔV<0) vs 더 모호화(ΔV>0)?"

| Direction | Meaning | Hypothesis |
|:---|:---|:---|
| ΔV > 0 | Analyst → Believer (더 모호해짐) | Still exploring, no PMF |
| ΔV < 0 | Believer → Analyst (더 구체화) | Found PMF, scaling up |

**Why Priority 2?**
- Measures **option transition cost** (direction-dependent)
- Connects to Product U (which future was chosen? = distribution collapse)
- Informs Product N (optimal k* may be direction-dependent)

**인생 비유**: "방황 끝에 길을 찾은 사람" vs "계속 방황하는 사람"

### 🥉 Priority 3: Timing of Pivot

**Question**: "빨리 피봇 vs 늦게 피봇 - 누가 더 성공?"

Already partially confirmed (see Finding 4 above).

**인생 비유**:
- Early pivot = "20대에 진로 바꾼 사람"
- Late pivot = "40대에 진로 바꾼 사람"

### Priority 4: Type of Deprivation

**Question**: "자금/팀/네트워크 중 어떤 결핍이 가장 유연성을 만드는가?"

| Deprivation Type | Variable | Lock-in Effect |
|:---|:---|:---|
| **Time (Age)** | Company age | r = -0.257*** (strongest!) |
| Funding | Early financing | r = -0.117*** |
| Team | Employees | r = -0.075*** |
| Network | Investors | r = +0.122*** (opposite!) |

**인생 비유**: "가난했던 것" vs "외로웠던 것" vs "늦게 시작한 것" - 뭐가 더 강한 동기?

---

## Regression Framework

### Model 1: Main Effects

$$
Y_{2025} = \beta_0 + \beta_1 F_{2021} + \beta_2 |\Delta V| + \epsilon
$$

### Model 2: Interaction (Golden Cage Test)

$$
Y_{2025} = \beta_0 + \beta_1 F_{2021} + \beta_2 |\Delta V| + \beta_3 (F_{2021} \times |\Delta V|) + \epsilon
$$

**Key prediction**: $\beta_3 < 0$
- High funding × Low |ΔV| = especially bad (Golden Cage)

### Model 3: Full with Controls

$$
Y_{2025} = \beta_0 + \beta_1 F_{2021} + \beta_2 |\Delta V| + \beta_3 (F \times |\Delta V|) + \beta_4 \text{Employees} + \beta_5 \text{Age} + \beta_6 \text{Industry FE} + \epsilon
$$

---

## Transportation Deep Dive (From Original Design)

### Why Transportation?

- High capital intensity → 초기 commitment 강제
- High uncertainty → paradigm shift 빈번
- **Interaction**: 커밋한 뒤 바꿔야 할 때 가장 고통스러움

### Transportation Results (Confirmed)

- **Stopped Optionality**: r = -0.12*** (more funding → less |ΔV|)
- **Funded Trap**: Middle V × High Funding = most locked (trap effect = +3.40)

---

## Visualization Gallery

### Plot 1: Lock-in Effect (Gradient Bar Chart)
- X: Early Funding Decile (1-10)
- Y: Mean |ΔV|
- Color: Green → Red gradient
- Shows: Downward slope (ρ = -0.12***)

### Plot 2: Escape Velocity vs Golden Cage
- Simple 2-bar comparison
- Escape: 4.7× (green)
- Cage: 1.4× (red)
- "3.4× better" annotation

### Plot 3: Cost of Commitment by Funding Level
- X: Funding Quartile
- Y: Cost (locked - flexible outcome)
- Shows: Cost increases with funding level

### Plot 4: ΔV Trajectory by Funding
- X: Time window (1, 2, 3)
- Y: Mean |ΔV|
- Lines: Low funding (green) vs High funding (red)
- Shows: Gap persists over time

---

## Implementation Files

| File | Purpose |
|:---|:---|
| `build_vagueness_timeseries.py` | Builds panel dataset |
| `vagueness_v2.py` | HybridVaguenessScorerV2 |
| `analyze_funding_trajectories.py` | Escape vs Cage analysis |
| `analyze_multivariable_lockin.py` | Multi-variable lock-in |
| `analyze_transportation_commitment.py` | Industry-specific analysis |
| `plot_cruel_optimism_flagship.py` | Publication-ready plots |

---

## Theoretical Predictions Summary

| Prediction | Operationalization | Expected | Confirmed? |
|:---|:---|:---:|:---:|
| Early funding → lock-in | Corr(funding, \|ΔV\|) | **-** | ✓ r=-0.117 |
| Lock-in hurts outcomes | Escape vs Cage growth | **Escape > Cage** | ✓ 3.4× |
| Age is strongest lock-in | Corr(age, \|ΔV\|) | **-** | ✓ r=-0.257 |
| Early pivot > late pivot | Pivot timing → outcome | **Early > Late** | ✓ 417× vs 350× |
| High funding amplifies trap | Interaction β₃ | **-** | TBD |
| Transportation trap strongest | Industry comparison | **Transport > Others** | ✓ |

---

## Next Steps

1. [ ] Implement cohort-based Cost of Commitment analysis
2. [ ] Test ΔV direction effect (구체화 vs 모호화)
3. [ ] Run full regression with interactions
4. [ ] Generate final publication-ready figures

---

## Appendix: Loading the Dataset

```python
import xarray as xr
import pandas as pd

# Load numeric panel
ds = xr.open_dataset('data/processed/vagueness_timeseries.nc')
print(ds)  # View structure

# Load full data with text
df = pd.read_parquet('data/processed/vagueness_timeseries.parquet')
```

---

*🦾C Empirical Design Consolidated v2.0 — 2025-12-04*
