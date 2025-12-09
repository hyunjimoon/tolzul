# DEPRECATION NOTICE

## Old 8-Section Structure → New 4-Phase Structure

The paper generation pipeline has been refactored to follow the **전라좌수군 (Jeonla Naval Fleet) 4-Phase Framework** based on 기승전결 (起承轉結).

### Migration Map

| **OLD FILES** | **NEW FILES** | **Phase** | **Commander** |
|---------------|---------------|-----------|---------------|
| `generate_01_intro.py` | `generate_01_introduction.py` | Phase 1 (起 - Introduction) | 정운 🐢 |
| `generate_02_litreview.py` + `generate_03_conceptual.py` | `generate_02_theory_conceptual.py` | Phase 2 (承 - Theory & Conceptual) | 권준 🐅 |
| `generate_04_method.py` + `generate_05_results.py` | `generate_03_empirics.py` | Phase 3 (轉 - Empirics & Results) | 김완 🐙 |
| `generate_06_discussion.py` | `generate_04_discussion.py` | Phase 4 (結 - Discussion & Conclusion) | 어영담 👾 |

### Deprecated Files (Legacy 8-Section Structure)

The following files are **deprecated** and should not be used in new workflows:

1. ❌ `generate_01_intro.py` → Use `generate_01_introduction.py` instead
2. ❌ `generate_02_litreview.py` → Merged into `generate_02_theory_conceptual.py`
3. ❌ `generate_03_conceptual.py` → Merged into `generate_02_theory_conceptual.py`
4. ❌ `generate_04_method.py` → Merged into `generate_03_empirics.py`
5. ❌ `generate_05_results.py` → Merged into `generate_03_empirics.py`
6. ❌ `generate_06_discussion.py` → Enhanced as `generate_04_discussion.py`

### Files Retained (Supplementary Materials)

The following files remain active as **supplementary sections** outside the main 4-phase narrative:

- ✅ `generate_07_poster.py` — Visual poster (전라좌수군 4-phase structure)
- ✅ `generate_08_industry_comparison.py` — Industry-specific analysis (PR #13 integration)

### New 4-Phase Architecture

#### Phase 1: 起 (Introduction) — 정운 🐢 "The Door Opener"
- **File**: `generate_01_introduction.py`
- **Output**: `01_Introduction.md`
- **Content**: Hook (Tesla vs Bosch), Puzzle, Preview of findings, Contributions, Roadmap
- **Color**: Teal (#20B2AA)

#### Phase 2: 承 (Theory & Conceptual Model) — 권준 🐅 "The Structure Builder"
- **File**: `generate_02_theory_conceptual.py`
- **Output**: `02_Theory_Conceptual.md`
- **Content**: Literature review (Info Econ, Real Options, Modularity), Four-module framework (C-T-O-C), Hypotheses, Table 1 (Descriptive stats)
- **Color**: Orange (#FF8C00)

#### Phase 3: 轉 (Empirics & Results) — 김완 🐙 "The Righteousness Prover"
- **File**: `generate_03_empirics.py`
- **Output**: `03_Empirics_Results.md`
- **Content**: Data & methods, H1/H2 results with tables, Devil's Advocate (4 alternatives), Specification curve, Subsample analyses
- **Color**: Crimson (#DC143C)

#### Phase 4: 結 (Discussion & Conclusion) — 어영담 👾 "The Story Closer"
- **File**: `generate_04_discussion.py`
- **Output**: `04_Discussion_Conclusion.md`
- **Content**: Theoretical implications, Managerial implications (Tesla Rule, Waymo Rule), Policy implications, Limitations, Future research, Conclusion
- **Color**: Purple (#9370DB)

### Why the Change?

The 8-section structure was fragmented and didn't align with the narrative flow. The new 4-phase structure:

1. **Clearer narrative arc**: 기승전결 (setup → development → turn → resolution) mirrors traditional Korean storytelling
2. **Better modularity**: Each phase is self-contained with clear responsibilities
3. **Commander ownership**: Each phase has a designated "commander" (정운·권준·김완·어영담) who owns that narrative role
4. **Reduced redundancy**: Literature + Conceptual merged; Methods + Results merged
5. **Easier maintenance**: 4 files instead of 6 (for core paper)

### Migration Guide

If you have existing workflows using old files:

**Option 1: Use new generate_all.py (Recommended)**
```bash
python generate_all.py --mode 4phase
# Generates all 4 phases with new structure
```

**Option 2: Run individual phases**
```bash
python generate_01_introduction.py
python generate_02_theory_conceptual.py
python generate_03_empirics.py
python generate_04_discussion.py
```

**Option 3: Keep legacy behavior (Not recommended)**
```bash
python generate_all.py --mode legacy
# Uses old 8-section structure (deprecated)
```

### Timeline

- **Old structure active until**: This commit
- **Migration period**: Old files kept for reference, not deleted
- **Full deprecation**: After verifying all downstream systems work with new structure

### Questions?

See `README.md` for updated documentation on the 4-phase framework.
