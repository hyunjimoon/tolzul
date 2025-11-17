# Pipeline Consolidation Plan
## Simplify codebase by removing src/ and modules/, centralizing in pipeline/

## Current Problems

1. **Code Duplication**:
   - `src/features.py` vs `modules/modules_features.py`
   - Unclear which version is used where

2. **Import Complexity**:
   - `sys.path.insert(0, ...)` hacks in every script
   - Hard to track dependencies

3. **Scattered Logic**:
   - Features in src/
   - Models in src/
   - Vagueness scoring in src/
   - Cache manager in src/
   - Duplicates in modules/

## Proposed Structure

```
pipeline/
├── 01_load_data.py           # Pipeline steps (keep as-is)
├── 02_engineer_features.py
├── 03_filter_datasets.py
├── 04_run_models.py
├── 05_generate_plots.py
│
├── lib/                       # Shared utilities (NEW)
│   ├── __init__.py
│   ├── features.py            # Consolidated from src/features.py
│   ├── models.py              # From src/models.py
│   ├── vagueness_v2.py        # From src/vagueness_v2.py
│   ├── cache_manager.py       # From src/cache_manager.py
│   └── data_loader.py         # If needed
│
└── README.md                  # Pipeline documentation
```

**Remove**:
- ❌ `src/` folder entirely
- ❌ `modules/` folder entirely

**Benefits**:
- ✅ Single source of truth
- ✅ No more sys.path hacks
- ✅ Clear dependency tree
- ✅ Easier to navigate

---

## Consolidation Steps

### Phase 1: Discovery & Analysis (CRITICAL - Do First)

**Goal**: Understand exactly what's used where before touching anything

1. **Map all imports**:
   - Which files import from `src/`?
   - Which files import from `modules/`?
   - What functions are actually used?

2. **Identify duplicates**:
   - `src/features.py` vs `modules/modules_features.py`
   - Which is the "canonical" version?
   - Are there meaningful differences?

3. **Check external dependencies**:
   - Does `thesis_figures.py` import from src/?
   - Does `cache_summary.py` import from src/?
   - Any other scripts outside pipeline/?

4. **Find dead code**:
   - What functions are defined but never called?
   - Can we remove them?

### Phase 2: Create Consolidated Library

1. **Create `pipeline/lib/` structure**:
   ```bash
   mkdir -p pipeline/lib
   touch pipeline/lib/__init__.py
   ```

2. **Merge features.py**:
   - Compare `src/features.py` vs `modules/modules_features.py`
   - Identify differences
   - Create single canonical `pipeline/lib/features.py`
   - Keep only actively used functions

3. **Copy other modules**:
   ```bash
   cp src/models.py pipeline/lib/
   cp src/vagueness_v2.py pipeline/lib/
   cp src/cache_manager.py pipeline/lib/
   ```

4. **Update imports in lib/ files**:
   - Change any internal imports to use `from . import ...`

### Phase 3: Update All Imports

1. **Pipeline scripts** (01-05):
   ```python
   # OLD:
   sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))
   from features import engineer_features

   # NEW:
   from lib.features import engineer_features
   ```

2. **Root-level scripts** (thesis_figures.py, cache_summary.py):
   ```python
   # OLD:
   sys.path.insert(0, str(Path(__file__) / 'src'))
   from features import ...

   # NEW:
   from pipeline.lib.features import ...
   ```

3. **Test each script** after updating imports

### Phase 4: Verification & Testing

1. **Run each pipeline step**:
   ```bash
   python pipeline/01_load_data.py
   python pipeline/02_engineer_features.py
   python pipeline/03_filter_datasets.py
   python pipeline/04_run_models.py
   python pipeline/05_generate_plots.py
   ```

2. **Run thesis figures**:
   ```bash
   python thesis_figures.py
   ```

3. **Run cache summary**:
   ```bash
   python cache_summary.py
   ```

4. **Full pipeline test**:
   ```bash
   ./run_all.sh
   ./export_to_thesis.sh
   ```

### Phase 5: Cleanup

1. **Only after everything works**:
   ```bash
   # Rename for safety (don't delete yet!)
   mv src src_DEPRECATED
   mv modules modules_DEPRECATED
   ```

2. **Run full pipeline again** to confirm

3. **After 1 week of successful runs**:
   ```bash
   rm -rf src_DEPRECATED
   rm -rf modules_DEPRECATED
   ```

---

## Risk Mitigation

### Before Starting

1. **Create git branch**:
   ```bash
   git checkout -b consolidate-to-pipeline
   ```

2. **Commit current state**:
   ```bash
   git add -A
   git commit -m "Checkpoint before consolidation"
   ```

### During Consolidation

1. **Test after each change**
2. **Commit frequently**
3. **Keep deprecation copies** until fully verified

### Rollback Plan

```bash
# If things break:
git checkout main
git branch -D consolidate-to-pipeline
```

---

## Decision Tree: Which features.py to Keep?

**Compare files**:
```bash
diff -u src/features.py modules/modules_features.py | head -100
```

**Key questions**:
1. Which has `engineer_features()` that's currently used?
2. Which has `StrategicVaguenessScorerV2` integration?
3. Which has `early_funding_musd` derivation?
4. Which is more recently updated? (`git log`)

**Likely answer**: `src/features.py` is canonical (used by pipeline)

---

## Testing Checklist

After consolidation, verify:

- [ ] `python pipeline/02_engineer_features.py` works
- [ ] `python pipeline/04_run_models.py all` works
- [ ] `python thesis_figures.py` works
- [ ] `python cache_summary.py` works
- [ ] `./run_all.sh` completes successfully
- [ ] `./export_to_thesis.sh` completes successfully
- [ ] All figures generated correctly
- [ ] All tables generated correctly
- [ ] Cache still works
- [ ] No import errors anywhere

---

## Files to Update (Comprehensive List)

### Pipeline Scripts
- `pipeline/01_load_data.py`
- `pipeline/02_engineer_features.py`
- `pipeline/03_filter_datasets.py`
- `pipeline/04_run_models.py`
- `pipeline/05_generate_plots.py`

### Root Scripts
- `thesis_figures.py`
- `cache_summary.py`
- `validate_pipeline.py` (if exists)

### Shell Scripts
- `run_all.sh` (might reference src/ in Python paths)
- `export_to_thesis.sh`

### Documentation
- Update any docs that reference src/ or modules/
- Update README.md with new structure

---

## Expected Outcomes

### Before
```
.
├── src/
│   ├── features.py (5000 lines)
│   ├── models.py
│   └── vagueness_v2.py
├── modules/
│   └── modules_features.py (duplicate!)
└── pipeline/
    ├── 01_load_data.py (sys.path hacks)
    ├── 02_engineer_features.py (sys.path hacks)
    └── ...
```

### After
```
.
└── pipeline/
    ├── 01_load_data.py (clean imports)
    ├── 02_engineer_features.py (clean imports)
    ├── ...
    └── lib/
        ├── features.py (single source)
        ├── models.py
        ├── vagueness_v2.py
        └── cache_manager.py
```

**Lines of code reduced**: ~30-40% (removing duplicates)
**Import complexity**: Eliminated
**Maintainability**: Much improved

---

## Timeline

- **Phase 1 (Discovery)**: 1-2 hours
- **Phase 2 (Consolidation)**: 2-3 hours
- **Phase 3 (Update imports)**: 1-2 hours
- **Phase 4 (Testing)**: 1-2 hours
- **Phase 5 (Cleanup)**: 30 minutes

**Total**: ~6-10 hours for safe, thorough consolidation

---

## Success Criteria

✅ All pipeline steps run without errors
✅ All thesis figures generate correctly
✅ All tests pass
✅ No `sys.path.insert()` hacks
✅ Single canonical version of each module
✅ `src/` and `modules/` deleted
✅ Code is cleaner and easier to navigate
