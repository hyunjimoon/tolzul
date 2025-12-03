# Legacy 8-Section Paper Generation Scripts (ARCHIVED)

**Status**: DEPRECATED — Do not use in new workflows

This directory contains the original 8-section paper generation structure that has been replaced by the new 4-phase 전라좌수군 framework (기승전결).

## Archived Files

### Original 8-Section Structure (Deprecated)

| File | Original Section | Status | Replacement |
|------|------------------|--------|-------------|
| `generate_01_intro.py` | Section 1: Introduction | ❌ Replaced | `generate_01_introduction.py` |
| `generate_02_litreview.py` | Section 2: Literature Review | ❌ Merged | `generate_02_theory_conceptual.py` |
| `generate_03_conceptual.py` | Section 3: Conceptual Model | ❌ Merged | `generate_02_theory_conceptual.py` |
| `generate_04_method.py` | Section 4: Methodology | ❌ Merged | `generate_03_empirics.py` |
| `generate_05_results.py` | Section 5: Results | ❌ Merged | `generate_03_empirics.py` |
| `generate_06_discussion.py` | Section 6: Discussion | ❌ Enhanced | `generate_04_discussion.py` |

## Why Archived?

These files were part of the original fragmented 8-section structure that didn't align with natural narrative flow. They have been replaced by the **4-phase 기승전결 framework**:

### New 4-Phase Structure (Active)

| Phase | Commander | File | Output |
|-------|-----------|------|--------|
| **1. 起 (Introduction)** | 정운 🐢 | `generate_01_introduction.py` | `01_Introduction.md` |
| **2. 승 (Theory & Conceptual)** | 권준 🐅 | `generate_02_theory_conceptual.py` | `02_Theory_Conceptual.md` |
| **3. 轉 (Empirics & Results)** | 김완 🐙 | `generate_03_empirics.py` | `03_Empirics_Results.md` |
| **4. 結 (Discussion & Conclusion)** | 어영담 👾 | `generate_04_discussion.py` | `04_Discussion_Conclusion.md` |

## Migration Completed

**Date**: November 24, 2025
**Commit**: e10b93c - "Refactor paper generation into 4-phase 전라좌수군 framework"

All functionality from these 6 legacy files has been:
- **Preserved**: Core content and logic retained
- **Enhanced**: Better metadata, clearer structure, commander ownership
- **Consolidated**: Literature + Conceptual merged, Methods + Results merged
- **Improved**: META_PROMPTs aligned with 기승전결 philosophy

## File Sizes (Total: 86KB)

```
-rw------- 1 root root 7.3K generate_01_intro.py
-rw------- 1 root root 8.8K generate_02_litreview.py
-rw------- 1 root root  14K generate_03_conceptual.py
-rw------- 1 root root  14K generate_04_method.py
-rw------- 1 root root  22K generate_05_results.py
-rw------- 1 root root  19K generate_06_discussion.py
```

## For Historical Reference Only

These files are kept for:
1. **Historical record**: Document the evolution of the pipeline
2. **Backward compatibility**: If needed for old workflows (not recommended)
3. **Code archaeology**: Understanding design decisions

**DO NOT USE** these files in new projects. Use the 4-phase framework instead.

## See Also

- `../DEPRECATION_NOTICE.md`: Full migration guide
- `../README_4PHASE.md`: New 4-phase documentation
- `../README.md`: General overview

---

**Archived on**: November 24, 2025
**Replaced by**: 4-Phase 전라좌수군 Framework (기승전결)

🐢 정운 → 🐅 권준 → 🐙 김완 → 👾 어영담
