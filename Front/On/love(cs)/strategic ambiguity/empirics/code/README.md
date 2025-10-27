# Code Documentation

## Scripts (execute in order)

### 01_process_company_data.py
**Input**: `data/raw/Company*.dat` (5 files)  
**Output**: `data/processed/company_master.csv`  
**What it does**: Extract AI/ML firms, score vagueness, classify integration cost

### 02_process_deal_data.py
**Input**: `data/raw/Deal*.dat` (2 files)  
**Output**: `data/processed/deal_panel.csv`  
**What it does**: Apply 4-step heuristic to identify Series A/B, create funding success binary

### 03_create_panel.py
**Input**: `company_master.csv` + `deal_panel.csv`  
**Output**: `data/processed/analysis_panel.csv`  
**What it does**: Join data, create panel where each firm appears twice (A, B)

### 04_run_analysis.py
**Input**: `analysis_panel.csv`  
**Output**: `output/table2_model1.csv`, `output/table4_model2.csv`  
**What it does**: Run regressions, test hypotheses

### 05_create_deliverables.py
**Input**: `analysis_panel.csv`  
**Output**: 4 tables + 4 figures  
**What it does**: Generate paper-ready outputs

---

## Development Workflow

1. Ask Claude to generate script N
2. Run script locally
3. Check output
4. Report back to Claude
5. Move to script N+1

See `../START_HERE.md` for detailed instructions.
