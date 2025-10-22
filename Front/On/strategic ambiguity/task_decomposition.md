## Workflow - Deliverables Overview

| ☐ | Item | Purpose | Vivid Summary 🎯 |
|---|------|---------|------------------|
| ☐ | **Table 1** | Descriptive stats | 📊 Mean vagueness: Low-i=42, High-i=59 (hardware MORE precise at A!) |
| ☐ | **Table 2** | Model 1 regression | 🔢 β₃ < 0***: Vagueness flips from +0.02 (A) to -0.02 (B) |
| ☐ | **Figure 1** | Bar chart (bins × stage) | 📈 High-vague bar rises, low-vague falls at B |
| ☐ | **Figure 2** | 2 probability curves | 📉 Lines cross between A→B |
| ☐ | **Table 3** | Rates by sector | 💥 58pp swing (hardware) vs 17pp (software) |
| ☐ | **Table 4** | Model 2 (3-way) | ⭐ β₇ = -0.065***: Mechanism confirmed |
| ☐ | **Figure 3** | 4 lines over time | 🎨 Red dashed rises, blue solid crashes (both sectors cross!) |
| ☐ | **Figure 4** | Magnitude bars | 📊 58pp bar towers over 17pp |

---

## Task Decomposition

### Task 1: Table 1 (Descriptive Stats)
**Input**: `df_panel` DataFrame  
**Output**: Markdown table with means by stage  
**Check**: Success rates sum to correct N

### Task 2: Table 2 (Model 1)
**Input**: Fitted logit model `m1`  
**Output**: Regression table with clustered SEs  
**Check**: β₃ < 0, p < 0.05

### Task 3: Figure 1 (Bar Chart)
**Input**: Vagueness bins × stage pivot table  
**Output**: Grouped bar chart PNG (300 DPI)  
**Check**: Reversal visible (high-vague bar taller at B)

### Task 4: Figure 2 (2 Curves)
**Input**: Model 1 predictions  
**Output**: Line plot showing crossover  
**Check**: Lines intersect between vagueness 40-60

### Task 5: Table 3 (Rates by Sector)
**Input**: `df_panel` grouped by integration cost  
**Output**: 4×3 table with change scores  
**Check**: 58pp = 3.4× larger than 17pp

### Task 6: Table 4 (Model 2)
**Input**: Fitted model with 3-way interaction  
**Output**: Regression table highlighting β₇  
**Check**: β₇ < 0, p < 0.01

### Task 7: Figure 3 (MONEY PLOT - CORRECTED)
**Input**: 4 group means over time  
**Output**: 4-line plot (thick hardware, thin software, ALL CROSS)  
**Specs**:
- Solid = Precise, Dashed = Vague
- Blue = Precise, Red = Vague
- Thick = High-i, Thin = Low-i
**Check**: Both pairs cross (software subtly, hardware dramatically)

### Task 8: Figure 4 (Magnitude Bars)
**Input**: Reversal effects (17pp, 58pp)  
**Output**: Side-by-side bar chart  
**Check**: 58pp bar 3.4× taller
