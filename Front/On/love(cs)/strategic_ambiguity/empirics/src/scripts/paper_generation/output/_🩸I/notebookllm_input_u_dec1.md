---
modified:
  - 2025-12-01T05:51:08-05:00
---

## Abstract

The Action School holds that startups should embrace ambiguity—staying vague preserves flexibility and accelerates learning. Yet survival follows a U-shape: both extremely vague and extremely precise ventures outperform those in between. When is vagueness valuable, and when does it backfire? Combining signaling theory with real options logic, we argue that vagueness affects two investor audiences differently. Concrete promises attract Analysts who verify; abstract visions attract Believers who project—but moderate ambiguity satisfies neither. Founders must choose a playbook: signal competence through precision, or signal vision through strategic ambiguity—never land in the middle.

---

## The Puzzle

**Tesla (2003)**: "We're going to make electric cars desirable." No specs, no timeline, no unit economics. Raised $7.5M Series A. Now worth $800B.

**Bosch (same year)**: "48V mild-hybrid systems, 15% efficiency gains, C-segment, Q2 2024, €850/unit." Struggled to raise.

**Why does the vague one win?**

---

## The Answer: U-Shape

```
Survival
   ↑
   │    *                           *
   │     *                         *
   │      *                       *
   │       *                     *
   │        *       DEATH       *
   │         *      ZONE       *
   │          *               *
   │           *             *
   │            *     *     *
   │             *   *   *
   └──────────────────────────────→ Vagueness (V)
        Low V              High V
       (precise)          (vague)
```

---

## Two Channels, Two Audiences

|V Level|Channel|Investor Type|Mechanism|Outcome|
|---|---|---|---|---|
|**Low** (precise)|Signaling|Analyst|Verifies claims|Funded if credible|
|**High** (vague)|Projection|Believer|Projects own vision|Funded if inspiring|
|**Middle**|Neither|—|Fails both tests|**Death zone**|

---

## The Model

Founder chooses V ∈ [0,1].

**Signaling Channel (Low V)**:

- Concrete promises invite verification
- Analysts check feasibility
- Funded if claims pass scrutiny

**Projection Channel (High V)**:

- Abstract visions create Rorschach test
- Believers fill gaps with their priors
- Funded if vision resonates

**Death Zone (Middle V)**:

- Too vague for Analysts to verify
- Too concrete for Believers to project
- Neither audience served

---

## Hypotheses

**Null (Action School)**: Vagueness uniformly helps. β_V > 0.

**H1 (U-Shape)**: Extremes outperform middle. β_{V(1-V)} < 0.

**H2 (Tech × Vagueness)**: Tech leaders who stay vague get trapped. β_{VT} < 0.

---

## H2 Explained: Tech Readiness × Vagueness

T = **Technological Readiness** (breakthrough level)

|Venture|T (Tech)|V (Vagueness)|Outcome|
|---|---|---|---|
|Waymo|High (L4 선도)|High (grand vision)|**Trapped**|
|Tesla|Medium|High|Escaped|
|Bosch|High|Low (precise specs)|Survived|

**β_{VT} < 0 의미**: 기술 선도자가 모호하면 Believer만 모여 trap 가속

---

## Closest Papers

|Paper|What They Do|How We Differ|
|---|---|---|
|**Guzman & Stern (2020)**|Predict growth from registration data|We ask if **clarity** matters|
|**El-Zayaty et al. (2024)**|Vagueness → lower funding (linear)|We find **U-shape**|

**Positioning**:

> "El-Zayaty et al. find vague language reduces investor interest unless founders have communication skills. We show vagueness can be _unconditionally_ beneficial—but only at extremes, producing a U-shape their linear model would miss."

---

## Data

- **130,000+ startups** from Pitchbook
- **Mobility/Transportation** industry
- **V measure**: NLP-based promise precision
- **T measure**: Technological breakthrough indicators
- **Outcomes**: Series A (early), survival/exit (late)

---

## Key Results

|Hypothesis|Coefficient|Finding|
|---|---|---|
|H1|β_{V(1-V)}|< 0 ✓ (U-shape confirmed)|
|H2|β_{VT}|< 0 ✓ (tech leaders + vague = trapped)|

---

## The Prescription

**For Founders**:

1. **Know your audience**: Analysts or Believers?
2. **Go to extremes**: The middle kills

**The Punchline**:

> "Choose your audience—Analysts or Believers, never both."

---

## 32-Paragraph Structure

|Chap|¶|Content|
|---|---|---|
|**1. Intro**|1-7|Gospel → Puzzle → RQ → Lens → Solution → Positioning → Roadmap|
|**2. Theory**|8-16|Lit (signaling) → Lit (options) → Position → Setup → Signaling Ch → Projection Ch → U-derivation → Hypotheses → Tech Readiness|
|**3. Empirics**|17-27|Context → Sample → DV → IV → Measurement → Stats → ID → H1 → H2 → H2a → Robustness|
|**4. Discussion**|28-32|π(D) → **Modularity** → Cost → Limits → Conclusion|

_Note: Modularity는 Discussion(¶29)에서만 논의_

---

## Figures & Tables

|ID|Location|Description|
|---|---|---|
|🖼️ Fig1_LV|¶14|L vs V curve (U-shape)|
|🖼️ Fig2|¶25|E vs V|
|🖼️ Fig3_VT|¶26|V × Tech Readiness interaction|
|🗄️ T1|¶24|H1 regression|
|🗄️ T2|¶25|H2 regression|
|🗄️ T_SpecCurve|¶27|Robustness|

---

## NotebookLLM Audio Guidance

**Key phrases**:

- "U-shape, not linear"
- "Analysts verify, Believers project"
- "The middle kills you"
- "Choose your audience"
- "Tech leaders who stay vague get trapped"

**Emotional arc**:

1. Open with Tesla vs Bosch puzzle
2. Build tension with death zone
3. Explain two-audience framework
4. Warning: Waymo trap (high T + high V)

---

_통제사: ⚓ 이순신_ _Generated by 권준 🐅_