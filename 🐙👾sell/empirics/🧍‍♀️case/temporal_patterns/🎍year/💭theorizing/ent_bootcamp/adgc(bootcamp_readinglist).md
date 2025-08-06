# Quick Reference Guide - Paper Classification System

## The Four Categories (MECE)

|Symbol|Category|Key Question|Signal Phrases|Example|
|---|---|---|---|---|
|🟣|**Anomaly**|Does it reveal a puzzle?|"We find that...", "Surprisingly...", "Contrary to..."|"Family CEOs underperform yet 90% are chosen"|
|♻️|**Definition**|Does it frame a challenge?|"The challenge is...", "We need to...", "The gap..."|"Firms must balance X with Y"|
|🟧|**Generation**|Does it solve a problem?|"We model...", "Our method...", "We estimate..."|"RCT shows 5% monthly returns"|
|🔴|**Conception**|Does it reframe thinking?|"We reconceptualize...", "New paradigm...", "Framework..."|"Entrepreneurship as dual phenomena"|

## Decision Tree

```
PRIMARY contribution?
├─ Reveals puzzle → 🟣
├─ Frames need → ♻️ 
├─ Provides solution → 🟧
└─ Changes lens → 🔴
```

## Classification Process

1. **Read**: Abstract + Introduction
2. **Identify**: Primary contribution
3. **Classify**: Into ONE category
4. **Explain**: One-sentence rationale
5. **Aggregate**: Count distribution

## Format Template

```markdown
- **Author(s) (Year).** Title. _Journal_.
  - **The [Type]**: [One-sentence description]
```

## Common Pitfalls

- ❌ Classifying by method (theory/empirical)
- ❌ Multiple categories per paper
- ❌ Focusing on secondary contributions
- ✅ PRIMARY contribution only
- ✅ What would go on author's CV?

## Distribution Benchmarks

- Typical: 20-25% each for 🟣♻️, 35-40% for 🟧, 5-10% for 🔴
- Red flag: 0% in any category (especially 🔴)
- Healthy: Balance across first three, few paradigm shifts

## Promise Vendor Context

- **Cu**: Immediate costs (underfunding)
- **Co**: Future costs (overpromising)
- **P**: Promise level
- **F|P**: Funding probability given promise
- **D|P**: Delivery probability given promise

## File Locations


- **Format example**:  [[day1 david(entfinance)]], [[day3.0 josh(gov-ent)]], [[day4.0 antoinette(entfinance)]], [[day 4.5 scott(Bayesian Entrepreneurship)]]
- **Definitions**: `classifier_core.md`
- **Full instructions**: Project Instructions artifact

_Tested on 23+ papers with 100% classification success_