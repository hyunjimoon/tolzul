# Archived Files - Do Not Use

These files are deprecated and kept only for historical reference.

**Status**: ❌ Deprecated - Do not use!
**Reason**: Replaced by simpler, working implementation
**Date Archived**: October 28, 2025

---

## What's in This Archive

### 1. Old 2-Snapshot Pipeline (Broken)

**run_pipeline.py**
- Old approach using only 2 snapshots (baseline + followup)
- Problem: 98% survival rate → singular matrix error
- Replaced by: `run_h2_seriesb.py` (4-snapshot approach)

---

### 2. Old Modular Approach (Overly Complex)

**01_process_company_data.py**
**02_process_deal_data.py**
**03_create_panel.py**
**04_run_analysis.py**
**05_create_deliverables.py**

- Old approach requiring 5 separate scripts run in sequence
- Problem: Too fragmented, hard to maintain, error-prone
- Replaced by: Single `run_h2_seriesb.py` script

---

### 3. Old xarray Prototypes (Overly Complex)

**pipeline_xarray.py**
**xarray_quick_start.py**

- Early prototypes using xarray for data management
- Problem: Unnecessary complexity, pandas is sufficient
- Replaced by: Simple pandas-based approach in `run_h2_seriesb.py`

---

## Why Were These Archived?

### Problems with Old Approach

1. **Singular Matrix Error**
   - 2-snapshot design had 98% survival rate
   - No statistical variation → models failed

2. **Fragmentation**
   - 5 separate scripts that had to be run in order
   - Easy to make mistakes in workflow

3. **Over-engineering**
   - xarray added complexity without benefits
   - pandas is sufficient for this analysis

4. **Maintenance Burden**
   - Multiple files to update for each change
   - Confusing for new users

### What Replaced Them

**Single file**: `run_h2_seriesb.py`

**Benefits**:
- ✅ 4-snapshot design (12-15% progression rate)
- ✅ Single script does everything
- ✅ Simple pandas-based approach
- ✅ Properly handles singular matrix issues
- ✅ Easy to understand and maintain

---

## Migration Guide

If you were using the old files, here's how to migrate:

### Old Way (Don't use):
```bash
# OLD: 2-snapshot approach
python code/hypothesis_testing_pipeline/run_pipeline.py \
    --baseline data/raw/Company20220101.dat \
    --followup data/raw/Company20230501.dat
```

### New Way (Use this):
```bash
# NEW: 4-snapshot approach
python run_h2_seriesb.py --output outputs/
```

**Everything else is automatic!**

---

## Historical Notes

### Timeline

- **Phase 1** (Early 2024?): Modular 5-script approach
  - Files: 01-05_*.py
  - Status: Overly complex

- **Phase 2** (Mid 2024?): Single pipeline with xarray
  - Files: run_pipeline.py, pipeline_xarray.py
  - Status: Singular matrix error

- **Phase 3** (October 2025): 4-snapshot approach ✓
  - File: run_h2_seriesb.py
  - Status: **Production ready**

---

## Can I Delete These?

**Short answer**: Yes, but keep for now.

**Why keep**:
- Historical reference
- May contain useful code snippets
- Academic documentation (show evolution)

**Safe to delete if**:
- You've confirmed new approach works
- Results are published
- 6+ months have passed

---

## Recovery Instructions

If you somehow need to restore these files:

```bash
# View what was archived
git log --follow archive_deprecated/run_pipeline.py

# Restore a specific file
git checkout <commit-hash> -- path/to/file.py
```

**But seriously, you shouldn't need to!** The new approach is better in every way.

---

**Archived by**: Claude Code
**Date**: October 28, 2025
**Reason**: Code cleanup and simplification
**Replacement**: run_h2_seriesb.py

---

## Questions?

**Q**: "Can I still use these old files?"
**A**: No! They're broken or deprecated. Use `run_h2_seriesb.py`.

**Q**: "What if the new file breaks?"
**A**: These old files won't help - they have the same bugs. Fix the new file instead.

**Q**: "Why keep them then?"
**A**: Historical documentation. Shows the evolution of the analysis.

**Q**: "Should I read these to understand the new approach?"
**A**: No! Read the docstrings in `run_h2_seriesb.py` instead.

---

**Do not use files in this archive!**
**Use**: `run_h2_seriesb.py` (one level up)
