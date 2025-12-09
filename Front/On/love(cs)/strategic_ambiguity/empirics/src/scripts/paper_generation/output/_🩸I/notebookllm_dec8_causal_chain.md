---
title: NotebookLLM Input - Causal Chain Visualization
created: 2025-12-08
purpose: 변수로 연결된 인과 사슬의 시각적/청각적 이해
status: 🚨 NUMBERS NEED VERIFICATION FROM REAL DATA
---

# The Thesis Bible v2: Capital-Flexibility Paradox

> **For NotebookLLM**: Use this document to create slides, infographics, podcasts, and videos that explain the interconnected causal chain of this thesis.

---

## 1. THE CORE CAUSAL CHAIN

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      THE VARIABLE CHAIN                                      │
│                                                                              │
│  ┌─────┐      ┌─────┐      ┌─────┐      ┌─────┐      ┌─────┐               │
│  │  V  │ ───► │ S₂  │ ───► │ AOC │ ───► │  C  │ ───► │ k*  │               │
│  └─────┘      └─────┘      └─────┘      └─────┘      └─────┘               │
│  Paper U      Paper U      Paper C      Paper C      Paper N                │
│                  ↓            ↓            ↓            ↓                   │
│  Vagueness → Specificity → Abandon. → Commitment → Optimal                  │
│  (promise)    (=1-V)        Option      Cost       Option                   │
│                             Cost                    Count                   │
│                                                                              │
│  INPUT ─────────────────────────────────────────────────────► OUTPUT        │
│  (Founder's Choice)                              (Venture's Fate)           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### The Chain in Plain English

1. **V (Vagueness)**: How vague or precise is the founder's promise?
   - V = 0: "We will build a Level 4 autonomous taxi for San Francisco by 2025"
   - V = 1: "We are reimagining urban mobility"

2. **S₂ (Specificity)**: The inverse of vagueness (S₂ = 1 - V)
   - High S₂ → Attracts **Analyst** investors (checkers)
   - Low S₂ → Attracts **Believer** investors (dreamers)

3. **AOC (Abandonment Option Cost)**: The price of pivoting
   - More capital invested → More promises made → Higher AOC
   - AOC = f(Capital), where AOC' > 0 and AOC'' > 0

4. **C (Commitment Cost)**: The empirical measure of AOC
   - **⚠️ KEY NUMBER**: ~-2.5× per funding decile (NEEDS VERIFICATION)
   - This means: locked ventures underperform flexible ones by 2.5× on average

5. **k* (Optimal Option Count)**: How many strategic options to maintain
   - k* = F⁻¹(CR), where CR = Cᵤ / (Cᵤ + Cₒ)
   - In deep-tech: CR → 1, so k* → HIGH

---

## 2. THE THREE PAPERS AS ONE STORY

### The Question Each Paper Answers

| Paper | Question | Answer | Key Variable |
|:------|:---------|:-------|:-------------|
| **✌️U** | "Which future should I promise?" | Choose extremes, avoid middle | V (Vagueness) |
| **🦾C** | "What's the cost of being locked in?" | 8.8× gap between flexible and rigid | AOC, \|ΔV\| |
| **🤹N** | "How many options should I maintain?" | Depends on CR; middle has no solution | k*, CR |

### The Story Flow

```
ACT 1 (Paper U): THE CHOICE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Founder faces a decision: How vague should my promise be?

   ┌────────────┐        ┌────────────┐        ┌────────────┐
   │   PRECISE  │        │   MURKY    │        │   VAGUE    │
   │   V ≈ 0    │        │  V ≈ 0.5   │        │   V ≈ 1    │
   │            │        │            │        │            │
   │  "Level 4  │        │ "Smart     │        │"Reimagining│
   │  AV by     │        │  mobility  │        │  urban     │
   │  2025"     │        │  solutions"│        │  mobility" │
   └────────────┘        └────────────┘        └────────────┘
         │                     │                     │
         ▼                     ▼                     ▼
   ┌────────────┐        ┌────────────┐        ┌────────────┐
   │  ANALYST   │        │   NOBODY   │        │  BELIEVER  │
   │  Investors │        │  Invests   │        │  Investors │
   │  (Mobileye)│        │ (Better    │        │  (Tesla)   │
   │            │        │  Place)    │        │            │
   └────────────┘        └────────────┘        └────────────┘

FINDING: U-shaped survival curve — extremes win, middle dies


ACT 2 (Paper C): THE TRAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━
The middle-precision founders who got funding face a worse fate...

   Capital Received
         │
         ▼
   ┌────────────────────────────────────────────┐
   │         THE CALCIFICATION PROCESS          │
   │                                            │
   │  Stage 1: PROMISE (Cognitive)              │
   │     "We told investors we'd do X"          │
   │              ▼                             │
   │  Stage 2: CONTRACT (Legal)                 │
   │     "The term sheet says X"                │
   │              ▼                             │
   │  Stage 3: ASSET (Physical)                 │
   │     "We bought X-specific equipment"       │
   │              ▼                             │
   │  Stage 4: LOCK (Calcified)                 │
   │     "We CAN'T pivot even if we want to"    │
   │                                            │
   │  AOC(V*) > Pivot Value = GOLDEN CAGE       │
   └────────────────────────────────────────────┘

FINDING: ⚠️ 8.8× gap (NEEDS REAL DATA VERIFICATION)
         Escape Velocity (flexible) vs Golden Cage (locked)


ACT 3 (Paper N): THE SOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Given this trap, what's the optimal strategy?

   The Newsvendor Insight:

   Traditional Model: "How much inventory to stock?"
   Our Model: "How many strategic OPTIONS to maintain?"

   ┌─────────────────────────────────────────────┐
   │          THE PROMISE VENDOR MODEL           │
   │                                             │
   │  k* = F⁻¹(CR)                               │
   │                                             │
   │  where CR = Cᵤ / (Cᵤ + Cₒ)                  │
   │                                             │
   │  Cᵤ = Cost of being too PRECISE            │
   │       (can't pivot → venture dies)          │
   │                                             │
   │  Cₒ = Cost of being too VAGUE              │
   │       (confusion → harder fundraising)      │
   │                                             │
   │  In deep-tech: Cᵤ >> Cₒ → CR → 1 → k* HIGH │
   └─────────────────────────────────────────────┘

THE TWIST: In the "Murky Middle" (S₂ ≈ 0.5),
           there is NO EQUILIBRIUM k*!

   Analyst wants: k = 1 (focus!)
   Believer wants: k > 1 (options!)
   At S₂ ≈ 0.5: Neither invests → NO MARKET
```

---

## 3. THE GRAVEYARD: WHY THIS MATTERS

### Real Companies That Died in the Middle

| Company | Funding | Fate | Lesson |
|:--------|:--------|:-----|:-------|
| **Better Place** | $850M | Bankrupt | Too specific (battery swap) + Too vague (global vision) |
| **Proterra** | $1.6B | Bankrupt | Locked into bus manufacturing, couldn't pivot to software |
| **Arrival** | $660M | Collapsed | Promised everything, delivered nothing |

### The Survivors

| Company | Strategy | V Level | k* | Result |
|:--------|:---------|:--------|:---|:-------|
| **Mobileye** | Precise | V ≈ 0.1 | k = 1 | $15B acquisition |
| **Tesla** | Vague | V ≈ 0.9 | k = high | $800B market cap |
| **Waymo** | Precise | V ≈ 0.2 | k = 1 | Survived (with Google backing) |

---

## 4. THE MATH MADE SIMPLE

### For the Podcast Host Who's Not a Mathematician

**The U-Shape (Paper U)**:
- Think of a smile emoji 😊
- Both ends (precise OR vague) are happy (survive)
- The middle is the mouth's dip (death)

**The Golden Cage (Paper C)**:
- Imagine pouring concrete for a building
- Floor 1: Easy to change design
- Floor 10: Can't change without demolishing
- V* = the floor where demolition costs more than your remaining budget

**The Promise Vendor (Paper N)**:
- You're selling lottery tickets, not products
- Analyst investors want: 1 ticket with high odds (k=1)
- Believer investors want: Many tickets with low odds each (k>1)
- Murky Middle: You're selling medium-odds medium-quantity tickets — NOBODY WANTS THIS

---

## 5. CRITICAL NUMBERS TO VERIFY

⚠️ **WARNING**: The following numbers are currently from SIMULATED DATA and need verification from real data:

| Number | Current Source | Verification Needed |
|:-------|:---------------|:--------------------|
| N = 488,381 | toc only | Count from `features_all.parquet` |
| 5.3% survival | Unknown | Calculate from transportation data |
| $15M Series A | Unknown | PitchBook statistics |
| 8.8× gap | Synthetic | Calculate from `vagueness_timeseries.parquet` |
| -2.5× per decile | Synthetic | Calculate from real data |
| ρ = -0.117 | Synthetic | Calculate from real data |
| CR 0.3-0.9 | Hardcoded | Estimate from industry data |

---

## 6. NOTEBOOKLLM PROMPTS

### For Podcast Generation

> "Create a debate podcast between two VCs:
> - VC 1 (Analyst type): Believes in precise milestones, rigorous experiments
> - VC 2 (Believer type): Believes in vision, flexibility, optionality
>
> They should argue about whether Better Place ($850M failure) or Tesla ($800B success) is the better model for mobility startups. Use the 'Murky Middle' concept to explain why Better Place failed — they were neither precise enough for analysts nor vague enough for believers."

### For Infographic

> "Design a 3-panel infographic:
> 1. LEFT: The U-Shape curve (x-axis: Vagueness, y-axis: Survival)
> 2. CENTER: The Calcification Process (4 stages from Promise to Lock)
> 3. RIGHT: The 2x2 Matrix (Funding × Flexibility → 4 cohorts)
>
> Use red for 'death zone' and green for 'success zone'. Mark the 'Murky Middle' in bright red."

### For Video Script

> "Write a 3-minute explainer video script:
>
> HOOK: '$2.5 billion in venture capital. Three dead companies. One lesson.'
>
> BODY: Use Better Place, Proterra, and Arrival as examples. Explain how each fell into the 'Murky Middle' — too specific for believers, too vague for analysts.
>
> TWIST: Introduce the math — the Critical Ratio formula explains why the middle has NO optimal strategy.
>
> CTA: 'Choose your investor type. Commit to your position. Never the murky middle.'"

---

## 7. THE ONE-LINER

**Before (vague thesis statement)**:
"Middle strategies fail in deep-tech ventures."

**After (precise thesis statement)**:
"In deep-tech venturing, the Critical Ratio CR = Cᵤ/(Cᵤ+Cₒ) approaches 1 because pivot failure (Cᵤ) is venture death, making high optionality (k* → HIGH) optimal—but at intermediate specificity S₂ ≈ 0.5, investor heterogeneity causes market failure with no equilibrium k*."

**The Cocktail Party Version**:
"Startups die not from starvation, but from indigestion. The ones that raised just enough capital to lock themselves into a strategy that couldn't pivot—that's the Murky Middle. Tesla survived because they sold a dream. Mobileye survived because they sold a spec. Better Place died because they sold neither."

---

*"Choose your channel, then commit — never the murky middle."*
