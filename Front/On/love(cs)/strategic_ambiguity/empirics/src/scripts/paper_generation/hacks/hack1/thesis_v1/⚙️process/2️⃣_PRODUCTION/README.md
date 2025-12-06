---
modified:
  - 2025-11-16T14:45:12-05:00
---
# 2️⃣_PRODUCTION README

## Structure

```
2️⃣_PRODUCTION/
├── VARIABLES.md          ← Variable definitions & measurement protocols
├── Theory/
│   ├── draft.md         ← Theoretical framework
│   ├── run.py           ← Generate fig1-2 (VOI vs RO)
│   └── TO_EMPIRICS.txt
├── Empirics_Early/
│   ├── draft.md         ← H1 test specification
│   ├── run.py           ← H1 OLS: E ~ V + controls
│   └── TO_LATER.txt
├── Empirics_Later/
│   ├── draft.md         ← H2a/b test specification
│   ├── run.py           ← H2 Logit: L ~ V×H + controls
│   └── TO_DISCUSSION.txt
└── Discussion/
    ├── draft.md         ← Implications & conclusion
    └── DONE.txt
```

---

## Usage

### **Quick Start**
```bash
# From thesis/ root
bash run_all.sh
```

### **Individual Sections**
```bash
cd 2️⃣_PRODUCTION/Theory && python3 run.py
cd 2️⃣_PRODUCTION/Empirics_Early && python3 run.py
cd 2️⃣_PRODUCTION/Empirics_Later && python3 run.py
```

- [ ] translate empiric folder files 
```
empirics/
├── run_all.sh                 # ⭐ Master pipeline script
├── validate_pipeline.py       # Quick validation without full run
├── PIPELINE_GUIDE.md          # Complete usage guide
│
├── pipeline/                  # 5-step modular pipeline
│   ├── 01_load_data.py
│   ├── 02_engineer_features.py
│   ├── 03_filter_datasets.py
│   ├── 04_run_models.py
│   ├── 05_generate_plots.py
│   └── README.md
│
├── src/                       # Core modules
│   ├── features.py           # ✨ Added filter_transportation_companies()
│   ├── vagueness_v2.py       # StrategicVaguenessScorerV2
│   └── models.py             # H1/H2 hypothesis tests
│
├── config/
│   └── datasets.yaml         # Dataset configuration
│
└── outputs/                  # Results for each dataset
    ├── all/
    ├── quantum/
    └── transportation/
```

---

## Variable Reference

**All run.py files use variables defined in `VARIABLES.md`:**

- **V (vagueness_zscore):** Standardized promise vagueness [-3, 3]
  - Calculation: V = 0.5×max(S_cat, S_concdef) + 0.5×mean(S_cat, S_concdef)
  - Components: Categorical abstractness (S_cat) + Concreteness deficit (S_concdef)

- **H (hardware):** Binary architecture indicator [0=SW, 1=HW]
  - Classification: Industry codes + keyword detection + manual validation
  - Inter-rater reliability: κ = 0.87

- **E (series_a_amount):** Early funding in millions USD
  - Transform: log(E+1) for OLS

- **L (series_b_plus):** Later success binary [0=No, 1=Yes]
  - Window: 17 months post-Series A

- **V×H (vague_x_hw):** Interaction term for architecture moderation

See `VARIABLES.md` for full operationalization, validation stats, and measurement protocols.

---

## Expected Outputs

| Section | Figures | Tables | Notes |
|---------|---------|--------|-------|
| Theory | fig1_tradeoff.pdf, fig2_architecture.pdf | — | Conceptual |
| Empirics_Early | fig3_H1_scatter.pdf | table1_H1_regression.txt | β₁<0 expected |
| Empirics_Later | fig4_vxh_interaction.pdf | table2_H2_logit.txt | β₃<0 expected |

All outputs → `3️⃣_OUTPUT/`

---

## Dependencies

**Required:**
- Python 3.8+
- pandas, numpy, matplotlib, statsmodels

**Install:**
```bash
pip install pandas numpy matplotlib statsmodels --break-system-packages
```

---

*Maintained by: 권준/나대용 (中軍)*
