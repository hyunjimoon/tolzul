# Paper-to-Code Mapping
# 논문 32개 모듈과 코드베이스 연동 맵

## Module #14-16: Data Overview (데이터 개관)

### #14: Context - Quantum Computing Industry
**논문 내용:** 양자컴퓨팅 산업 배경 설명
**코드 위치:**
- `src/features.py::consolidate_company_snapshots()`
- Filter: `df[df.sector_fe == 'quantum']`
**테스트:**
```python
# test/unit/test_features.py
def test_quantum_sector_filtering():
    """Verify quantum sector companies are correctly identified"""
```

### #15: Sample Construction
**논문 내용:** 표본 구성 (출처/코호트/필터)
**코드 위치:**
- `src/features.py::consolidate_company_snapshots()`
- `src/features.py::engineer_features()`
**생성 아티팩트:** 🗄️ 표본구성표
**테스트:**
```python
# test/integration/test_sample_construction.py
def test_sample_size_matches_paper():
    """Verify final sample size matches paper Table X"""
    df = consolidate_company_snapshots('data/raw')
    assert len(df) == PAPER_REPORTED_N
```

### #16: Variables Overview (E/L/V/F)
**논문 내용:**
- E: Early event (Series A at baseline)
- L: Later success (Series B+ at endpoint)
- V: Vagueness score
- F: Flexibility (1 - is_hardware)
**코드 위치:**
- `src/features.py::engineer_features()`
- `src/vagueness_v2.py::StrategicVaguenessScorerV2`
**생성 아티팩트:** 🗄️ 변수정의·요약통계
**테스트:**
```python
# test/integration/test_variables.py
def test_table_descriptive_stats():
    """Generate Table X: Descriptive Statistics and compare with paper"""
    df = load_and_engineer_features()
    stats = df[['E', 'L', 'V', 'F']].describe()
    # Compare with paper-reported values
```

---

## Module #17-22: Empirical Methodology (실증 방법론)

### #17: Measurements
**논문 내용:** V (vagueness), F (flexibility) 측정 방법
**코드 위치:**
- `src/vagueness_v2.py::StrategicVaguenessScorerV2.score()`
- `src/features.py::engineer_features()` (F = 1 - is_hardware)
**테스트:**
```python
# test/unit/test_vagueness.py
def test_vagueness_measurement_validity():
    """Validate vagueness scoring against hand-coded examples"""
```

### #19: Identification Strategy
**논문 내용:** 내생성 논의, 식별 전략
**코드 위치:**
- `src/models.py` (주석 참조)
- Controls selection logic
**문서화:** `docs/identification_strategy.md`

### #20: Main Specifications
**논문 내용:** E ~ V (OLS), L ~ V × F (Logit)
**코드 위치:**
- `src/models.py::run_HEV()` - H1 for E ~ V
- `src/models.py::run_HLVF()` - H2 for L ~ V × F
**생성 아티팩트:** 🗄️ T_MainSpecs
**테스트:**
```python
# test/integration/test_main_specs.py
def test_h1_specification_matches_paper():
    """Verify H1 formula matches paper equation (X)"""
    # Run model
    result = run_HEV(df)
    # Check formula includes correct controls
    assert 'z_V' in result.params
```

---

## Module #23-27: Results (결과)

### #23: H1 - Early Funding Penalty
**논문 내용:** Vagueness reduces early funding
**코드 위치:**
- `src/models.py::test_h1_early_funding()`
- OR `src/models.py::run_HEV()` (two-snapshot mode)
**생성 아티팩트:** 🖼️ Fig2_EVF, 🗄️ T1
**테스트:**
```python
# test/integration/test_paper_results.py
def test_table1_h1_results():
    """Reproduce Table 1: H1 regression coefficients"""
    df = load_analysis_data()
    result = test_h1_early_funding(df)

    # Compare with paper-reported values (with tolerance)
    PAPER_COEF_VAGUENESS = -0.234  # From paper Table 1
    PAPER_SE = 0.089

    assert abs(result.params['z_vagueness'] - PAPER_COEF_VAGUENESS) < 0.01
    assert abs(result.bse['z_vagueness'] - PAPER_SE) < 0.01

def test_figure2_evf_plot():
    """Reproduce Figure 2: E-V-F relationship"""
    df = load_analysis_data()
    fig_path = plot_figure2_evf(df)

    # Check file exists and is non-trivial
    assert Path(fig_path).exists()
    assert Path(fig_path).stat().st_size > 10000
```

### #24: H2 - Later Success Benefit
**논文 内容:** Vagueness beneficial for later success (moderated by F)
**코드 위치:**
- `src/models.py::test_h2_main_growth()`
- OR `src/models.py::run_HLVF()` (two-snapshot mode)
**생성 아티팩트:** 🖼️ Fig3_LVF, Fig4_STV, 🗄️ T2
**테스트:**
```python
def test_table2_h2_results():
    """Reproduce Table 2: H2 logit regression"""
    df = load_analysis_data()
    result = test_h2_main_growth(df)

    # Main effect (vagueness)
    PAPER_COEF_MAIN = 0.456
    assert abs(result.params['z_vagueness'] - PAPER_COEF_MAIN) < 0.01

    # Interaction (vagueness × hardware)
    PAPER_COEF_INTERACTION = -0.321
    interaction_param = [p for p in result.params.index
                         if 'z_vagueness' in p and 'is_hardware' in p][0]
    assert abs(result.params[interaction_param] - PAPER_COEF_INTERACTION) < 0.01
```

### #25: H2a - V×F Interaction
**논문 내용:** 상호작용 효과 (flexibility amplifies vagueness benefit)
**코드 위치:** Same as #24
**생성 아티팩트:** 🖼️ Fig3_LVF (interaction plot)
**테스트:**
```python
def test_figure3_interaction_plot():
    """Reproduce Figure 3: V×F interaction visualization"""
    df = load_analysis_data()
    result = test_h2_main_growth(df)

    # Generate interaction plot
    fig_path = plot_figure3_interaction(df, result)

    # Visual regression test (compare with reference image)
    # assert image_similarity(fig_path, 'test/fixtures/fig3_reference.png') > 0.95
```

### #26: Mechanisms - Pivot/Learning
**논문 내용:** 메커니즘 분석 (피벗 빈도, 학습 속도)
**코드 위치:**
- ⚠️ **새로 작성 필요:** `src/models.py::test_mechanism_pivot()`
**생성 아티팩트:** 🗄️ T_Mech
**테스트:**
```python
# test/unit/test_mechanisms.py
def test_pivot_frequency_analysis():
    """Mechanism: Companies with higher V pivot more frequently"""
    # TODO: Implement pivot detection logic
    # df['pivot_count'] = detect_pivots(df)
    # model = smf.ols('pivot_count ~ z_vagueness + controls', df).fit()
    # assert model.params['z_vagueness'] > 0
```

### #27: Robustness - Spec Curve
**논문 내용:** 강건성 검증 (스펙 커브, 안정성)
**코드 위치:**
- `src/multiverse.py` (already exists)
**생성 아티팩트:** 🗄️ T_SpecCurve
**테스트:**
```python
# test/integration/test_robustness.py
def test_specification_curve():
    """Run multiverse analysis across 100+ specifications"""
    from multiverse import run_specification_curve

    results = run_specification_curve(df)

    # Check majority of specs support main hypothesis
    significant_positive = sum((r.params['z_vagueness'] > 0) & (r.pvalues['z_vagueness'] < 0.05)
                                for r in results)
    assert significant_positive / len(results) > 0.8  # 80%+ support
```

---

## Module #11-13: Conceptual Model (개념틀)

### #11: Framework (2×2)
**논문 내용:** 2×2 framework (시간×레벨)
**생성 아티팩트:** 🖼️ Fig1_LV (conceptual figure)
**코드 위치:** Manual illustration (not code-generated)
**문서화:** `docs/conceptual_framework.md`

### #13: Hypotheses (H1/H2/H2a)
**논문 내용:** 가설 정식화
**코드 위치:**
- Documented in `src/models.py` docstrings
- Each hypothesis test function has detailed docstring
**테스트:**
```python
# test/meta/test_hypothesis_documentation.py
def test_h1_docstring_matches_paper():
    """Verify H1 docstring matches paper hypothesis statement"""
    import inspect
    from models import test_h1_early_funding

    docstring = inspect.getdoc(test_h1_early_funding)
    assert "vagueness reduces early funding" in docstring.lower()
```

---

## Summary Table: Code-Paper Mapping

| Module | 논문 섹션 | 코드 파일 | 테스트 파일 | 아티팩트 | 상태 |
|--------|----------|----------|------------|---------|-----|
| #14 | Context | features.py | test_features.py | - | ✅ |
| #15 | Sample | features.py | test_sample_construction.py | 🗄️표본구성 | ⚠️ |
| #16 | Variables | features.py, vagueness_v2.py | test_variables.py | 🗄️요약통계 | ⚠️ |
| #17 | Measurements | vagueness_v2.py | test_vagueness.py | - | ✅ |
| #20 | Specifications | models.py | test_main_specs.py | 🗄️MainSpecs | ⚠️ |
| #23 | H1 Results | models.py::test_h1 | test_paper_results.py | 🖼️Fig2, 🗄️T1 | ⚠️ |
| #24 | H2 Results | models.py::test_h2 | test_paper_results.py | 🖼️Fig3-4, 🗄️T2 | ⚠️ |
| #25 | Interaction | models.py::test_h2 | test_paper_results.py | 🖼️Fig3 | ⚠️ |
| #26 | Mechanisms | models.py (new) | test_mechanisms.py | 🗄️T_Mech | ❌ |
| #27 | Robustness | multiverse.py | test_robustness.py | 🗄️SpecCurve | ❌ |

Legend:
- ✅ = 코드 & 테스트 완료
- ⚠️ = 코드 있음, 테스트 필요
- ❌ = 코드 or 테스트 모두 필요
