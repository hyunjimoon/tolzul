# Promise Precision and Venture Funding - START HERE

## 🚀 New User? Check These First

1. **[[작전상황판.md]]** - One-page dashboard (현재 상태 빠른 확인)
2. **[[전투일지🩸]]** - Detailed battle log (전체 진행 기록)
3. **This file** - Quick start guide (코드 실행 방법)
4. **[[workflow(hypothesis, data, model)🗺️]]** - Research design (가설, 데이터, 모델)

---

## What We're Doing
Analyze how **vagueness in promises** affects VC funding success using real Pitchbook data.

**Research Question**: When should entrepreneurs be vague vs. precise?

**Answer**: Vague at Series A (preserve flexibility), Precise at Series B (signal readiness) - BUT only in hardware (high integration cost).

---

## Quick Start

### Step 1: Ask Claude Code to Write Scripts

**Two Options:**

**Option A: Claude Code** (uses sample data on GitHub)
```
I have sample Pitchbook data:
- empirics/data/raw/Company2021.dat (30 firms)
- empirics/data/raw/Deal2023.dat (deals for those firms)

Write 01_process_company_data.py that:
- Reads Company2021.dat (pipe-delimited, ~30 rows)
- Filters to AI/ML firms (keywords: 'AI', 'ML', 'artificial intelligence', 'machine learning')
- Scores vagueness using keyword counts:
  * Vague: approximately, around, roughly, flexible, scalable, adaptive
  * Precise: exactly, precisely, guaranteed, specific, certified
  * Formula: 50 + 10*(vague_count - precise_count), capped [0,100]
- Classifies integration cost from Keywords field:
  * High-i (1): chip, asic, robotics, distributed, gpu, hardware
  * Low-i (0): api, saas, software, wrapper, platform, cloud
- Outputs: data/processed/company_master.csv

Print first 5 rows and summary stats for validation.
```

**Option B: Local Execution** (uses full data)
- Same prompt but change path to your local Dropbox location
- Use `Company*.dat` (all 5 files) instead of just Company2021.dat

### Step 2: Run It
**If using Claude Code**: It runs automatically  
**If local**: 
```bash
cd "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Front/On/strategic ambiguity/empirics"
python code/01_process_company_data.py
```

### Step 3: Check Output
Look for: `data/processed/company_master.csv`

Expected: 
- Sample data: ~10-15 AI/ML firms from 30 rows
- Full data: ~60-80 AI/ML firms from all files

### Step 4: Repeat for Scripts 2-5

---

## The 5 Scripts (in order)

| Script | Input | Output | What It Does |
|--------|-------|--------|--------------|
| **01_process_company_data.py** | Company*.dat | company_master.csv | Extract firms, score vagueness |
| **02_process_deal_data.py** | Deal*.dat | deal_panel.csv | Identify Series A/B deals |
| **03_create_panel.py** | company + deal | analysis_panel.csv | Join into panel (each firm × 2) |
| **04_run_analysis.py** | analysis_panel.csv | regression tables | Test hypotheses |
| **05_create_deliverables.py** | analysis_panel.csv | 4 tables + 4 figures | Generate paper outputs |

---

## Key Details

### Vagueness Score (0-100)
**Vague keywords**: approximately, around, roughly, flexible, scalable, adaptive  
**Precise keywords**: exactly, precisely, guaranteed, specific, certified  
Formula: `50 + 10*(vague_count - precise_count)` capped at [0,100]

### Integration Cost (binary)
**High-i (1)**: chip, asic, robotics, distributed, gpu, hardware, semiconductor  
**Low-i (0)**: api, saas, software, wrapper, platform, cloud

### Series A/B Identification (4-step heuristic)
1. Filter: Only "Early Stage VC" or "Later Stage VC" deals
2. Sequence: First = Series A, Second = Series B
3. Size: A = $2-15M, B = $10M+
4. Date: A = 2021-2022, B = 2023-2025

---

## Expected Results

### Success Rates
|  | Low-i (Software) | High-i (Hardware) |
|--|------------------|-------------------|
| **Precise at A** | 65% | 75% |
| **Precise at B** | 70% (+5pp) | 28% (-47pp) ⬇️ |
| **Vague at A** | 55% | 52% |
| **Vague at B** | 60% (+5pp) | 63% (+11pp) ⬆️ |

**Key finding**: In hardware, vague promises flip from disadvantage to advantage. Software shows minimal change.

### Regressions
- **Model 1**: β₁ < 0 (vague hurts at A), β₃ > 0 (reverses at B)
- **Model 2**: β₇ > 0 (reversal 3× stronger in hardware)

---

## Troubleshooting

**Problem**: "File not found"  
**Fix**: Update file paths to match your structure

**Problem**: "Module not found"  
**Fix**: `pip install pandas numpy statsmodels matplotlib seaborn`

**Problem**: Too few firms (<10)  
**Fix**: Expand AI/ML keywords or use full dataset

**Problem**: No Series B matches  
**Fix**: Relax date filter or use full Deal dataset

---

## File Structure
```
/empirics/
├── START_HERE.md                  ← You are here
├── workflow(hypothesis, data, model).md    ← Reference only
├── code/
│   ├── 01_process_company_data.py
│   ├── 02_process_deal_data.py
│   ├── 03_create_panel.py
│   ├── 04_run_analysis.py
│   └── 05_create_deliverables.py
├── data/
│   ├── raw/
│   │   ├── Company2021.dat        ← Sample (30 rows)
│   │   ├── Deal2023.dat           ← Sample (30 rows)
│   │   ├── Company*.dat           ← Full data (5 files)
│   │   └── Deal*.dat              ← Full data (2 files)
│   └── processed/                 ← Generated by scripts 1-3
└── output/                        ← Generated by scripts 4-5
```

---

## That's It!

**Don't overthink it.** Just copy the prompt above, get code from Claude Code (or run locally), iterate through all 5 scripts.

For conceptual details, see: `workflow(hypothesis, data, model).md`

---

Last Updated: 2025-10-22
