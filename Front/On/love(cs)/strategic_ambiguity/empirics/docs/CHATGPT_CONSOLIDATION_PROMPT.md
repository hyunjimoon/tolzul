# Prompt for ChatGPT: Pipeline Consolidation Analysis

Copy and paste this prompt to ChatGPT-4 or Claude to help with the consolidation:

---

## PROMPT START

I need help consolidating a Python empirics analysis pipeline that has grown organically and now has code duplication between `src/`, `modules/`, and `pipeline/` folders.

**Goal**: Remove `src/` and `modules/` folders, consolidate everything into `pipeline/lib/`, making `pipeline/` the single source of truth.

**Current structure**:
```
empirics_ent_strat_ops/
├── src/
│   ├── features.py
│   ├── models.py
│   ├── vagueness_v2.py
│   └── cache_manager.py
├── modules/
│   └── modules_features.py
├── pipeline/
│   ├── 01_load_data.py
│   ├── 02_engineer_features.py
│   ├── 03_filter_datasets.py
│   ├── 04_run_models.py
│   └── 05_generate_plots.py
├── thesis_figures.py
└── cache_summary.py
```

**Target structure**:
```
empirics_ent_strat_ops/
├── pipeline/
│   ├── 01_load_data.py
│   ├── 02_engineer_features.py
│   ├── 03_filter_datasets.py
│   ├── 04_run_models.py
│   ├── 05_generate_plots.py
│   └── lib/
│       ├── __init__.py
│       ├── features.py      # Consolidated
│       ├── models.py
│       ├── vagueness_v2.py
│       └── cache_manager.py
├── thesis_figures.py
└── cache_summary.py
```

---

## PHASE 1: ANALYSIS (What I need you to do first)

Please analyze the attached files and create a comprehensive report with:

### 1. Import Map
Create a table showing:
- Which files import from `src/`?
- Which files import from `modules/`?
- Which specific functions/classes are imported?

**Format**:
```
File                        | Imports From   | What's Imported
----------------------------|----------------|------------------
pipeline/02_...py           | src/features   | engineer_features, consolidate_company_snapshots
pipeline/04_...py           | src/models     | test_h1_early_funding, test_h2_main_growth
thesis_figures.py           | src/...        | ...
```

### 2. Duplicate Detection
Compare `src/features.py` vs `modules/modules_features.py`:
- Are they identical?
- If different, what are the key differences?
- Which appears to be the "canonical" version (more recent, more used)?
- Can they be safely merged?

### 3. Dead Code Analysis
For each file in `src/` and `modules/`:
- List all functions/classes defined
- Mark which are actually imported/used by other files
- Identify dead code that can be removed

**Format**:
```
src/features.py:
  ✅ engineer_features() - Used by: pipeline/02_engineer_features.py
  ✅ derive_early_funding() - Used internally by engineer_features()
  ❌ old_function() - NOT USED - candidate for removal
```

### 4. External Dependencies
Check if anything outside the pipeline imports from `src/` or `modules/`:
- Shell scripts?
- Jupyter notebooks?
- Test files?
- Documentation that hard-codes paths?

### 5. Import Pattern Analysis
Show current import patterns:
```python
# Pattern 1 (in pipeline scripts):
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))
from features import engineer_features

# Pattern 2 (in root scripts):
sys.path.insert(0, str(Path(__file__) / 'src'))
from models import test_h1_early_funding
```

And recommend new patterns after consolidation.

---

## PHASE 2: EXECUTION PLAN (What I need you to create)

Based on your Phase 1 analysis, create a detailed, **step-by-step execution plan** with:

### 1. File Operations
Exact commands to:
- Create `pipeline/lib/` structure
- Copy/merge files from `src/` and `modules/` into `pipeline/lib/`
- Handle duplicates (which to keep, how to merge)

### 2. Import Rewrites
For EACH file that needs updating, show:
```python
# File: pipeline/02_engineer_features.py

# OLD (lines 14-19):
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))
from features import consolidate_company_snapshots, engineer_features
from vagueness_v2 import StrategicVaguenessScorerV2
from cache_manager import CacheManager

# NEW:
from lib.features import consolidate_company_snapshots, engineer_features
from lib.vagueness_v2 import StrategicVaguenessScorerV2
from lib.cache_manager import CacheManager
```

### 3. Testing Checklist
Create a testing script or checklist I can use after each change:
```bash
# Test after updating pipeline/02_engineer_features.py:
python pipeline/02_engineer_features.py
# Expected: No import errors, features generated

# Test after updating pipeline/04_run_models.py:
python pipeline/04_run_models.py all
# Expected: Models run successfully
```

### 4. Risk Assessment
For each step, identify:
- What could go wrong?
- How to detect if something broke?
- How to rollback?

---

## PHASE 3: VERIFICATION (What I need you to generate)

Create a comprehensive verification script that:

1. **Checks imports**:
   ```python
   # verify_imports.py
   import sys
   import importlib

   # Try importing from new locations
   try:
       from pipeline.lib import features
       from pipeline.lib import models
       print("✅ All imports work")
   except ImportError as e:
       print(f"❌ Import failed: {e}")
   ```

2. **Validates structure**:
   ```bash
   # Check no old imports remain
   grep -r "sys.path.insert" pipeline/
   grep -r "from src" .
   grep -r "from modules" .
   ```

3. **Tests functionality**:
   - Run each pipeline step
   - Verify outputs match before/after
   - Check no regressions

---

## CONSTRAINTS & REQUIREMENTS

1. **Preserve git history**: Don't delete files immediately, rename to `*_DEPRECATED` first
2. **Zero downtime**: Pipeline must work at every commit
3. **No functionality changes**: Pure refactor, behavior must be identical
4. **Backward compatibility**: Consider if external tools depend on current structure
5. **Documentation**: Update all README/docs that reference old paths

---

## FILES TO ANALYZE

Please analyze these files in order of priority:

**Priority 1 (Core Pipeline)**:
1. `pipeline/02_engineer_features.py`
2. `pipeline/04_run_models.py`
3. `src/features.py`
4. `src/models.py`

**Priority 2 (Supporting Code)**:
5. `src/vagueness_v2.py`
6. `src/cache_manager.py`
7. `modules/modules_features.py`

**Priority 3 (Consumers)**:
8. `thesis_figures.py`
9. `cache_summary.py`
10. `pipeline/01_load_data.py`
11. `pipeline/03_filter_datasets.py`
12. `pipeline/05_generate_plots.py`

---

## DELIVERABLES

I need you to produce:

1. **Analysis Report** (Markdown):
   - Import map table
   - Duplicate comparison
   - Dead code list
   - External dependency warnings

2. **Execution Plan** (Markdown):
   - Numbered steps
   - Exact commands to run
   - Import rewrite patterns for each file
   - Rollback procedures

3. **Verification Script** (Python):
   - Tests all imports work
   - Validates no old paths remain
   - Checks functionality preserved

4. **Risk Matrix** (Table):
   ```
   Change                | Risk Level | Mitigation
   ----------------------|------------|------------
   Move features.py      | Medium     | Test after each file update
   Merge duplicates      | High       | Compare diffs carefully first
   Update imports        | Low        | Automated with grep/sed
   ```

5. **Rollback Plan** (Bash script):
   - How to undo changes if needed
   - Restore from backup/git

---

## QUESTIONS TO ANSWER

Before proceeding, please answer:

1. Is there any code in `modules/` that's not in `src/` (or vice versa)?
2. Are there circular dependencies that would break with new structure?
3. Are there any hard-coded absolute paths that reference `src/`?
4. Do any shell scripts (`run_all.sh`, etc.) modify PYTHONPATH?
5. Are there any compiled files (.pyc, __pycache__) that might cause issues?
6. Do any config files (YAML, JSON) reference src/ or modules/ paths?

---

## OUTPUT FORMAT

Please structure your response as:

```markdown
# Pipeline Consolidation Analysis & Plan

## Phase 1: Analysis

### 1.1 Import Map
[Table here]

### 1.2 Duplicate Files
[Comparison here]

### 1.3 Dead Code
[List here]

### 1.4 External Dependencies
[Analysis here]

### 1.5 Answers to Questions
[Answers here]

## Phase 2: Execution Plan

### Step 1: Create directory structure
[Commands here]

### Step 2: Copy files
[Commands with explanations]

### Step 3: Update imports in X.py
[Before/after code blocks]

[Continue for all steps...]

## Phase 3: Verification

### Testing Checklist
[Checklist here]

### Verification Script
[Python code here]

## Risk Assessment

[Table here]

## Rollback Plan

[Bash script here]
```

---

## ADDITIONAL CONTEXT

- This is a research pipeline for analyzing startup vagueness and funding
- Key components: feature engineering (vagueness scoring), statistical models (OLS/Logit), plotting
- Uses pandas, numpy, statsmodels, matplotlib
- Codebase is ~10k lines across all files
- Currently works but is hard to maintain due to duplication
- Goal is to simplify without breaking anything

## PROMPT END

---

## How to Use This Prompt

1. **Copy the entire prompt** from "PROMPT START" to "PROMPT END"

2. **Attach relevant files** when you paste into ChatGPT:
   - `src/features.py`
   - `modules/modules_features.py`
   - `pipeline/02_engineer_features.py`
   - `pipeline/04_run_models.py`

3. **ChatGPT will analyze** and give you:
   - Detailed import map
   - Duplicate detection
   - Step-by-step execution plan
   - Verification scripts

4. **Review the plan** before executing

5. **Execute step-by-step**, testing after each change

6. **Use verification scripts** ChatGPT provides

---

## Expected ChatGPT Response Time

- Analysis: ~5 minutes
- Execution plan: ~10 minutes
- Verification scripts: ~5 minutes
- **Total: ~20 minutes**

Then you'll have a comprehensive, safe plan to execute the consolidation!
