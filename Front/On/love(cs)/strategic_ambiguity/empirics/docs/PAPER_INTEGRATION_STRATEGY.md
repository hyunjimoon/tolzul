# 논문-코드 연동 전략
# Paper-Code Integration Strategy

## 🎯 목표 (Goal)

32개 논문 모듈을 코드베이스와 완전히 연동하여:
1. **재현성 보장**: 논문의 모든 테이블/그림을 코드로 재현
2. **자동 검증**: 코드 변경 시 논문 결과가 깨지지 않는지 자동 체크
3. **문서화**: 각 모듈이 어떤 코드에 매핑되는지 명확히 기록

---

## 📋 4-Phase 접근법

### **Phase 1: Results-First (가장 중요) - 2주**

논문의 핵심 결과부터 코드와 연동 → 가장 빠른 ROI

#### Week 1: Main Results (Module #23-25)
```bash
# 1. 논문 테이블 상수 정의
# test/integration/test_paper_results.py에 실제 논문 값 입력

class PaperConstants:
    TABLE1_VAGUENESS_COEF = -0.234  # ← 논문 Table 1에서 복사
    TABLE1_VAGUENESS_SE = 0.089
    # ...

# 2. 실제 데이터로 테스트 실행
pytest test/integration/test_paper_results.py::TestTable1_H1_EarlyFunding -v

# 3. 불일치 발견 → 코드 또는 논문 수정 필요
```

**체크리스트:**
- [ ] Table 1 (H1) 계수 ±1% 이내 재현
- [ ] Table 2 (H2) 계수 ±1% 이내 재현
- [ ] 상호작용 항 (V×F) 유의성 확인
- [ ] 샘플 크기 일치 확인

#### Week 2: Figures (Module #23-25)
```bash
# plotting.py에 논문 그림 생성 함수 추가
def generate_figure2_evf(df, output_path='outputs/fig2_evf.pdf'):
    """Generate Figure 2: E-V-F relationship"""
    # ... plotting code
    return output_path

def generate_figure3_lvf(df, h2_result, output_path='outputs/fig3_lvf.pdf'):
    """Generate Figure 3: L-V-F interaction"""
    # ... interaction plot
    return output_path

# 테스트에서 자동 생성 검증
pytest test/integration/test_paper_results.py::TestFigureReproduction -v
```

**체크리스트:**
- [ ] Figure 2 (E-V-F) 자동 생성
- [ ] Figure 3 (L-V-F interaction) 자동 생성
- [ ] Figure 4 (S-T-V trajectory) 자동 생성
- [ ] PDF + PNG 포맷 모두 출력

---

### **Phase 2: Methodology Validation (중간) - 1주**

통계 방법론이 논문과 일치하는지 검증

#### Module #17-22: Measurements & Specifications

```python
# test/unit/test_measurements.py
def test_vagueness_measurement_procedure():
    """Verify vagueness scoring matches paper description (Module #17)"""
    # 논문에 예시로 든 회사 3개로 테스트
    examples = [
        ("AI-powered medical imaging, 50 hospitals, FDA approved", 25.3),
        ("Next-gen innovation platform", 78.9),
        ("Hardware sensors for aerospace", 42.1),
    ]

    scorer = StrategicVaguenessScorerV2()
    for description, expected_score in examples:
        actual = scorer.score(description)
        assert abs(actual - expected_score) < 5.0  # ±5 tolerance

def test_h1_specification_complete():
    """Verify H1 includes all controls mentioned in paper (Module #20)"""
    df = load_test_data()
    result = test_h1_early_funding(df)

    # 논문에 명시된 control variables 확인
    required_controls = ['z_employees_log', 'founder_serial',
                         'is_hardware', 'z_firm_age',
                         'sector_fe', 'founding_cohort']

    for control in required_controls:
        assert control in str(result.model.formula)
```

**체크리스트:**
- [ ] Vagueness 측정 방식 문서화 및 검증
- [ ] Flexibility (F) 분류 로직 검증
- [ ] H1 specification 완전성 확인
- [ ] H2 specification 완전성 확인
- [ ] Control variables 일치 확인

---

### **Phase 3: Data Pipeline (기초) - 1주**

데이터 준비 과정이 논문과 일치하는지 검증

#### Module #14-16: Data Overview

```python
# test/integration/test_sample_construction.py
def test_sample_size_matches_paper():
    """Module #15: Verify sample construction"""
    # 논문 Table X에 명시된 샘플 크기
    PAPER_REPORTED_N = 450
    PAPER_QUANTUM_N = 450
    PAPER_TRANSPORTATION_N = 320

    df = consolidate_company_snapshots('data/raw')
    df = engineer_features(df)

    # 필터 적용 전
    assert len(df) >= PAPER_REPORTED_N

    # Quantum 섹터만
    df_quantum = df[df.sector_fe == 'quantum']
    assert abs(len(df_quantum) - PAPER_QUANTUM_N) < 10  # ±10 tolerance

def test_descriptive_statistics_table():
    """Module #16: Generate Table X (Descriptive Statistics)"""
    df = load_analysis_data()

    # 논문 Table X의 요약통계 재현
    stats = df[['E', 'L', 'V', 'F', 'z_vagueness']].describe()

    # 평균값 비교 (논문 값 vs 코드 값)
    PAPER_MEAN_V = 45.2
    assert abs(stats.loc['mean', 'V'] - PAPER_MEAN_V) < 1.0
```

**체크리스트:**
- [ ] 샘플 크기 일치 (±10 이내)
- [ ] 요약통계 일치 (평균 ±1%, 표준편차 ±5%)
- [ ] 섹터 분포 일치
- [ ] 코호트 분포 일치

---

### **Phase 4: Robustness & Extensions (심화) - 2주**

강건성 검증 및 추가 분석

#### Week 3: Mechanisms (Module #26)

```python
# src/models.py에 추가
def test_mechanism_pivot_frequency(df, formula="pivot_count ~ z_vagueness + controls"):
    """
    Module #26: Test mechanism - pivot frequency

    H_mechanism: Companies with higher vagueness pivot more frequently
    """
    # Detect pivots from description changes over time
    df['pivot_count'] = detect_pivot_events(df)

    model = smf.ols(formula, data=df).fit()
    return model

def test_mechanism_learning_speed(df, formula="time_to_productmarket ~ z_vagueness * F_flexibility + controls"):
    """
    Module #26: Test mechanism - learning speed

    H_mechanism: Vague+flexible companies learn faster
    """
    model = smf.ols(formula, data=df).fit()
    return model
```

#### Week 4: Robustness (Module #27)

```python
# test/integration/test_robustness.py
def test_specification_curve_h2():
    """Module #27: Run 100+ specifications for H2"""
    from multiverse import run_specification_curve

    # Define specification space
    specs = {
        'controls': [
            ['z_employees_log'],
            ['z_employees_log', 'founder_serial'],
            ['z_employees_log', 'founder_serial', 'z_firm_age'],
        ],
        'fixed_effects': [
            [],
            ['sector_fe'],
            ['sector_fe', 'founding_cohort'],
        ],
        'sample': [
            'all',
            'quantum_only',
            'post_2015',
        ],
    }

    results = run_specification_curve(df, specs)

    # 80% 이상의 spec에서 유의한 양의 계수
    significant_positive = sum(
        (r.params['z_vagueness'] > 0) & (r.pvalues['z_vagueness'] < 0.05)
        for r in results
    )

    assert significant_positive / len(results) > 0.80
```

**체크리스트:**
- [ ] Pivot 메커니즘 구현 및 테스트
- [ ] Learning 메커니즘 구현 및 테스트
- [ ] Specification curve 실행 (100+ specs)
- [ ] Alternative measurements 테스트
- [ ] Subsample robustness 검증

---

## 🛠️ 실용적 워크플로우

### **일일 루틴 (Daily Workflow)**

```bash
# 1. 논문 작업 전: 현재 상태 확인
pytest test/integration/test_paper_results.py -v

# 2. 코드 수정 (예: models.py)
# ... edit code ...

# 3. 테스트 실행: 논문 결과 깨졌나?
pytest test/integration/test_paper_results.py::TestTable1_H1_EarlyFunding -v

# 4. 실패하면 → 코드 수정 or 논문 업데이트
# 5. 성공하면 → git commit
git add .
git commit -m "Update H1 specification - all paper tests pass"
```

### **논문 제출 전 체크리스트**

```bash
# 1. 모든 테이블 재현
pytest test/integration/test_paper_results.py::TestTable1 -v
pytest test/integration/test_paper_results.py::TestTable2 -v

# 2. 모든 그림 재생성
python -m src.cli generate-all-figures --output outputs/

# 3. LaTeX 테이블 자동 생성
python scripts/generate_paper_tables.py

# 4. 최종 검증
pytest test/integration/ -v --cov=src
```

---

## 📊 진행 상황 추적

### **Current Status (2024-01-20)**

| Phase | Module | Status | Priority |
|-------|--------|--------|----------|
| 1 | #23 (H1) | 🟡 코드 완료, 테스트 템플릿 있음 | HIGH |
| 1 | #24 (H2) | 🟡 코드 완료, 테스트 템플릿 있음 | HIGH |
| 1 | #25 (V×F) | 🟡 코드 완료, 테스트 템플릿 있음 | HIGH |
| 2 | #17 (Measurements) | 🟢 코드 + 테스트 완료 | MEDIUM |
| 2 | #20 (Specifications) | 🟡 코드 완료, 검증 필요 | MEDIUM |
| 3 | #15 (Sample) | 🟡 코드 완료, 검증 필요 | MEDIUM |
| 3 | #16 (Variables) | 🟡 코드 완료, 검증 필요 | MEDIUM |
| 4 | #26 (Mechanisms) | 🔴 코드 필요 | LOW |
| 4 | #27 (Robustness) | 🟡 코드 있음, 테스트 필요 | LOW |

Legend:
- 🟢 = 완료
- 🟡 = 진행 중
- 🔴 = 시작 전

### **Next 3 Actions (우선순위)**

1. **논문 값 입력** (30분):
   - `test/integration/test_paper_results.py`의 `PaperConstants` 클래스에 실제 논문 테이블 값 복사

2. **Table 1 재현 테스트** (1시간):
   ```bash
   # 실제 데이터로 H1 실행
   pytest test/integration/test_paper_results.py::TestTable1_H1_EarlyFunding -v

   # 불일치 발견 → 원인 파악
   # - 데이터 필터링 문제?
   # - Control variables 누락?
   # - 논문 오타?
   ```

3. **Figure 2 생성 스크립트** (2시간):
   ```python
   # src/plotting.py에 추가
   def generate_figure2_evf(df):
       """Generate Figure 2 for paper"""
       # ... plotting code
   ```

---

## 💡 Best Practices

### **1. 논문 값은 별도 파일로 관리**

```python
# test/fixtures/paper_values.py
class PaperTable1:
    """Values from Table 1 in published paper"""
    VAGUENESS_COEF = -0.234
    VAGUENESS_SE = 0.089
    N_OBS = 450

class PaperTable2:
    """Values from Table 2 in published paper"""
    VAGUENESS_COEF = 0.456
    INTERACTION_COEF = -0.321
```

### **2. 테스트는 관대하게 (Tolerance)**

```python
# Bad: 완전 일치 요구 (불가능)
assert result.params['z_vagueness'] == -0.234

# Good: ±1% tolerance (현실적)
assert abs(result.params['z_vagueness'] - (-0.234)) < 0.01
```

### **3. 실패 시 유용한 에러 메시지**

```python
# Bad
assert coef == paper_coef

# Good
assert abs(coef - paper_coef) < 0.01, \
    f"Coefficient mismatch: code={coef:.3f}, paper={paper_coef:.3f}, " \
    f"diff={coef-paper_coef:.3f} ({(coef-paper_coef)/paper_coef*100:.1f}%)"
```

### **4. 논문 Figure는 별도 디렉토리**

```
outputs/
├── paper_figures/          # 논문에 들어갈 최종 그림
│   ├── fig2_evf.pdf
│   ├── fig2_evf.png
│   ├── fig3_lvf.pdf
│   └── fig4_stv.pdf
├── paper_tables/           # LaTeX 테이블
│   ├── table1_h1.tex
│   ├── table2_h2.tex
│   └── table_descriptive.tex
└── diagnostics/            # 진단용 임시 그림
    └── ...
```

---

## 🚀 Quick Start (지금 바로 시작)

### **10분 안에 첫 테스트 실행**

```bash
# 1. 논문 Table 1에서 계수 하나만 복사
# test/integration/test_paper_results.py 열기
# PaperConstants.TABLE1_VAGUENESS_COEF = -0.234  ← 실제 값 입력

# 2. 단일 테스트 실행
pytest test/integration/test_paper_results.py::TestTable1_H1_EarlyFunding::test_table1_vagueness_coefficient -v

# 3. 결과 확인
# PASSED → 코드 정확 ✓
# FAILED → 불일치 원인 파악 필요
```

---

## 📚 References

- **Paper Mapping**: `docs/PAPER_CODE_MAPPING.md`
- **Test Code**: `test/integration/test_paper_results.py`
- **Hypothesis Tests**: `src/models.py`
- **CI/CD**: `.github/workflows/test.yml`

---

## ❓ FAQ

**Q: 논문 값이 정확히 재현 안 되면?**
A: 3가지 가능성:
1. 데이터 필터링 차이 (가장 흔함)
2. Control variables 차이
3. 논문 오타 (드물지만 있음)

→ ±1-2% 이내면 괜찮음. 더 크면 원인 파악 필요.

**Q: 모든 모듈을 다 연동해야 하나?**
A: No! **Results (Module #23-27)만 100% 연동**하면 충분. Introduction/Discussion은 코드 없어도 됨.

**Q: 그림은 자동으로 업데이트되나?**
A:
```bash
# 그림 자동 재생성
python -m src.cli generate-all-figures

# Git hook으로 자동화 가능
# .git/hooks/pre-commit에 추가
```

**Q: 논문 수정 시 매번 테스트 돌려야?**
A: Results 섹션 수정 시만 필요. Introduction/Discussion 수정은 테스트 불필요.
