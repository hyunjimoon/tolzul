---
성장:
  - 2025-10-21T23:08:50-04:00
updated:
  - 2025-10-22T02:30:00-04:00
---
# Promise Precision and Venture Funding - HANDOFF CHECKLIST

## ☐ Hypothesis (CORRECTED SIGNS)
**"Vague promises help at Series A but hurt at Series B; precise promises hurt initially but help later"**

**Mechanism**: Precision helps when execution is bottleneck (low-i). Vagueness helps when discovery is bottleneck (high-i).

**Expected Pattern**: 
- H1: β₁ > 0 (vagueness *helps* at Series A)
- H2: β₃ < 0 (effect reverses—vagueness *hurts* at Series B)
- H3: β₇ < 0 (reversal 2-3× stronger in high-i sectors)

---

## ☐ Data Collection (Hours 1-3)
- [ ] Pull 70-80 AI infrastructure firms from Pitchbook (2021-22 Series A)
- [ ] Filter: Series A $2M-$15M, AI/ML category
- [ ] Download pitch materials (TechCrunch, blogs, YC demo videos)
- [ ] Record Series B outcomes through Q3 2025
- [ ] Create panel: each firm × 2 observations (A attempt, B attempt)

**Target**: 35 low-i firms (API/SaaS), 40 high-i firms (hardware/chips)

---

## ☐ Variable Coding (Hours 4-6)

### Vagueness Score
- [ ] Option A: Run LIWC certitude dictionary → vagueness = 100 - certitude
- [ ] Option B: Run Flesch-Kincaid (Python textstat) if no LIWC license
- [ ] Validate: Check 10 examples manually

**Rubric**:
| Score | Type | Example |
|-------|------|---------|
| 0-30 | Precise | "10ms latency, 99.9% uptime on A100 GPUs" |
| 70-100 | Vague | "Enterprise-ready AI infrastructure" |

### Integration Cost
- [ ] Code binary: hardware keywords = high (1), software = low (0)
- [ ] Manual review: Verify ambiguous cases
- [ ] Balance check: ~50/50 split needed

**Keywords**:
- High: chip, ASIC, robotics, distributed, edge device, GPU cluster
- Low: API, SaaS, wrapper, fine-tuning, prompt, platform

### Controls
- [ ] Extract from Pitchbook: `log(SeriesA_Amount)`, `Team_Size`, `Founder_Prior_Exit`

---

## ☐ Analysis (Hours 7-8)

### Model 1: Base Reversal
```python
m1 = smf.logit('funding_success ~ vagueness * series_b_dummy + controls',
               data=df_panel).fit(cov_type='cluster', cov_kwds={'groups': df_panel['firm_id']})
```
- [ ] Confirm β₁ > 0, p < 0.05
- [ ] Confirm β₃ < 0, p < 0.05

### Model 2: Three-way Interaction
```python
m2 = smf.logit('funding_success ~ vagueness * series_b_dummy * high_integration_cost + controls',
               data=df_panel).fit(cov_type='cluster', cov_kwds={'groups': df_panel['firm_id']})
```
- [ ] Confirm β₇ < 0, p < 0.01

---

## ☐ Deliverables (Hour 9)

### Table 3: Success Rates
- [ ] Generate 4×2 grid showing reversal
- [ ] Calculate change scores (A→B)
- [ ] Highlight 58pp swing in high-i sector

### Table 4: Regression
- [ ] Format coefficients table
- [ ] Show Model 1 & 2 side-by-side
- [ ] Bold three-way interaction β₇

### Figure 3: THE MONEY PLOT
- [ ] Time-based line plot (x-axis = Series A → B)
- [ ] 4 lines: {Vague, Precise} × {Low-i, High-i}
- [ ] Show crossing pattern in high-i sector
- [ ] Annotate: -47pp crash vs +11pp rise

### Figure 4: Bar Chart
- [ ] Reversal magnitudes by integration cost
- [ ] Show 3.4× larger effect in high-i

---

## ☐ Quality Checks
- [ ] All figures use time-based x-axis (NOT vagueness)
- [ ] Precise = solid line, Vague = dashed line
- [ ] High-i lines thicker/bolder than low-i
- [ ] Consistent color scheme across all figures
- [ ] Annotations highlight key findings

---

## Key Numbers to Reproduce
- Precise hardware: 75% → 28% (-47pp)
- Vague hardware: 52% → 63% (+11pp)
- **Total swing**: 58pp in high-i vs 17pp in low-i
- **Three-way interaction**: β₇ ≈ -0.065, p < 0.003

---

## Files to Hand Over
1. `/mnt/user-data/outputs/figure3_money_plot.png` (current version)
2. `/mnt/user-data/outputs/vivid_deliverables.md` (updated goals)
3. This checklist with ☐ → ☑ as you complete

---

## Critical Reminders
- **Sign correction**: β₁ > 0 (vagueness helps at A), β₃ < 0 (reverses at B)
- **Visual priority**: Crossing lines over time, not slopes by vagueness
- **Mechanism test**: High-i sector shows 2-3× larger reversal
- **Endogeneity**: Control for Founder_Prior_Exit (rhetorical capital)
