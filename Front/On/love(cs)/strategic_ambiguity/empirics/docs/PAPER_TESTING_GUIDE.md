# 논문 자동 생성 테스트 가이드
# Paper Auto-Generation Testing Guide

## 1. 필수 테스트 (Essential Tests)

논문 자동 생성 파이프라인의 신뢰성을 보장하기 위한 **3단계 테스트 전략**:

### Tier 1: 핵심 통계 테스트 (Critical - Must Pass)

**목적**: 논문에 들어가는 모든 숫자가 정확한지 검증

#### 1.1 모델 계수 테스트 (H1/H2 Coefficients)
```python
# test/integration/test_paper_results.py

def test_h1_vagueness_coefficient_sign():
    """H1: Vagueness 계수가 음수인지 확인 (정보비용 가설)"""
    result = test_h1_early_funding(df)
    coef = result.params['z_vagueness']
    assert coef < 0, "H1: Vagueness should reduce early funding"

def test_h2_interaction_exists():
    """H2: V×F 상호작용 항이 모델에 포함되었는지 확인"""
    result = test_h2_main_growth(df)
    interaction_terms = [p for p in result.params.index
                        if 'vagueness' in p and 'hardware' in p]
    assert len(interaction_terms) > 0, "H2: V×F interaction must exist"
```

**이것이 중요한 이유**:
- 논문의 핵심 주장이 데이터에서 실제로 나오는지 확인
- 계수 부호가 바뀌면 논문 전체 내러티브가 바뀜
- 리뷰어가 재현할 때 같은 결과가 나와야 함

#### 1.2 테이블 값 일치 테스트 (Table Validation)
```python
def test_table1_matches_h1_model():
    """Table 1의 계수가 H1 모델 결과와 정확히 일치하는지"""
    result = test_h1_early_funding(df)

    # Generate table
    from scripts.generate_paper_tables import generate_table1_h1
    latex_table = generate_table1_h1(df, output_path='/tmp/table1.tex')

    # Extract coefficient from LaTeX
    import re
    coef_match = re.search(r'Vagueness.*?(-?\d+\.\d+e[+-]\d+)', latex_table)
    table_coef = float(coef_match.group(1))
    model_coef = result.params['z_vagueness']

    # Must match to at least 3 significant figures
    assert abs(table_coef - model_coef) < 1e-10
```

**이것이 중요한 이유**:
- 사람이 손으로 LaTeX 테이블을 만들면 오타 발생
- 자동 생성 스크립트가 올바르게 값을 추출하는지 확인
- 데이터가 바뀌어도 테이블이 자동으로 업데이트되는지 확인

#### 1.3 Figure 생성 테스트 (Figure Generation)
```python
def test_figure2_file_created():
    """Figure 2 (Early Funding vs Vagueness)가 생성되는지"""
    from src.cli import cmd_generate_plots

    # Run plotting
    args = type('obj', (object,), {'dataset': 'all'})
    cmd_generate_plots(args)

    # Check file exists
    fig_path = Path('paper/figures/fig2_early_funding.pdf')
    assert fig_path.exists(), "Figure 2 PDF must be created"
    assert fig_path.stat().st_size > 1000, "Figure 2 must not be empty"
```

**이것이 중요한 이유**:
- LaTeX 컴파일 시 그림이 없으면 오류 발생
- 그림이 빈 파일이면 논문에 아무것도 안 나옴
- 자동화 스크립트가 끝까지 실행되는지 확인

---

### Tier 2: 데이터 품질 테스트 (Important - Should Pass)

**목적**: 입력 데이터가 분석에 적합한지 확인

#### 2.1 샘플 크기 테스트
```python
def test_sample_size_sufficient():
    """최소 샘플 크기 확인 (통계적 검정력)"""
    df = load_dataframe('data/processed/features_engineered.nc')

    # H1 requires at least 30 observations (rule of thumb)
    assert len(df) >= 30, f"Sample too small: {len(df)} < 30"

    # H2 requires balanced classes
    growth_counts = df['growth'].value_counts()
    minority_class = growth_counts.min()
    assert minority_class >= 10, f"Minority class too small: {minority_class}"
```

#### 2.2 결측치 테스트
```python
def test_no_missing_values_in_key_vars():
    """핵심 변수에 결측치가 없는지 확인"""
    df = load_dataframe('data/processed/features_engineered.nc')

    key_vars = ['vagueness', 'early_funding_musd', 'is_hardware', 'growth']
    for var in key_vars:
        missing_pct = df[var].isna().sum() / len(df) * 100
        assert missing_pct < 5, f"{var} has {missing_pct:.1f}% missing"
```

#### 2.3 이상치 테스트
```python
def test_vagueness_range():
    """Vagueness 점수가 유효한 범위 내에 있는지"""
    df = load_dataframe('data/processed/features_engineered.nc')

    assert df['vagueness'].min() >= 0, "Vagueness cannot be negative"
    assert df['vagueness'].max() <= 100, "Vagueness cannot exceed 100"

    # Check for unrealistic values
    extreme_high = (df['vagueness'] > 95).sum()
    assert extreme_high < len(df) * 0.01, "Too many extreme vagueness scores"
```

---

### Tier 3: 파이프라인 통합 테스트 (Good to Have)

**목적**: 전체 파이프라인이 처음부터 끝까지 실행되는지 확인

#### 3.1 End-to-End 테스트
```python
def test_full_pipeline_runs():
    """전체 파이프라인 실행 (데이터 → 분석 → 논문)"""
    import subprocess

    # Clean previous outputs
    subprocess.run(['make', 'clean-all'], check=True)

    # Run full pipeline
    result = subprocess.run(['make', 'all'], capture_output=True)

    # Check all outputs exist
    assert Path('data/processed/features_engineered.nc').exists()
    assert Path('paper/results_auto.tex').exists()
    assert Path('paper/tables/table1_h1.tex').exists()
    assert Path('paper/figures/fig2_early_funding.pdf').exists()
```

#### 3.2 재현성 테스트
```python
def test_results_are_reproducible():
    """동일한 데이터로 두 번 실행하면 같은 결과가 나오는지"""
    df = load_dataframe('data/processed/features_engineered.nc')

    # Run H1 twice
    result1 = test_h1_early_funding(df)
    result2 = test_h1_early_funding(df)

    # Coefficients must be identical
    np.testing.assert_array_almost_equal(
        result1.params.values,
        result2.params.values,
        decimal=10,
        err_msg="H1 results not reproducible"
    )
```

---

## 2. 테스트 파일 구조 (Test Organization)

```
test/
├── unit/                          # Tier 1: 단위 테스트
│   ├── test_models.py            # H1/H2/H3/H4 모델 함수 테스트 (53 tests)
│   ├── test_features.py          # Vagueness scorer 테스트 (25 tests)
│   └── test_data_io.py           # NetCDF I/O 테스트 (NEW)
│
├── integration/                   # Tier 2: 통합 테스트
│   ├── test_paper_results.py     # 논문 결과 검증 (Table/Figure 일치)
│   ├── test_data_quality.py      # 데이터 품질 검사 (NEW)
│   └── test_pipeline.py          # 전체 파이프라인 실행 (NEW)
│
├── fixtures/                      # 테스트 데이터
│   ├── sample_data.nc            # 샘플 데이터 (50 companies)
│   └── expected_outputs/         # 기대 출력값
│       ├── table1_expected.tex
│       └── h1_expected_coef.json
│
└── conftest.py                   # 공유 fixtures (pytest)
```

---

## 3. 테스트 실행 방법 (How to Run Tests)

### 빠른 테스트 (Quick - 1분)
```bash
# 핵심 모델 테스트만 (계수가 맞는지)
pytest test/unit/test_models.py::TestH1EarlyFunding -v --no-cov

# 논문 결과 검증 (테이블 일치하는지)
pytest test/integration/test_paper_results.py -v --no-cov
```

### 전체 테스트 (Full - 5분)
```bash
# 모든 테스트 실행 + 커버리지 리포트
make test

# 또는
pytest test/ -v --cov=src --cov-report=html
```

### 논문 제출 전 검증 (Before Submission - 10분)
```bash
# 1. 전체 파이프라인 재실행
make clean-all
make all

# 2. 모든 테스트 실행
make test

# 3. 논문 값 검증
make validate

# 4. PDF 컴파일
make paper
```

---

## 4. 로컬 환경 테스트 예시 (Local Testing Example)

### 4.1 설치 (Installation)
```bash
# 1. Clone repository
git clone https://github.com/user/empirics_ent_strat_ops.git
cd empirics_ent_strat_ops

# 2. Install dependencies (NO pyarrow needed!)
pip install -r requirements.txt

# 3. Verify installation
python -c "import xarray; import pandas; import statsmodels; print('✓ All dependencies OK')"
```

### 4.2 데이터 변환 (Convert existing Parquet to NetCDF)
```bash
# If you have existing .parquet files:
python scripts/convert_to_netcdf.py --directory data/processed

# Expected output:
# Converting features_engineered.parquet...
#   ✓ features_engineered.parquet (2.3 MB)
#     → features_engineered.nc (1.8 MB)
#     Ratio: 0.78x
```

### 4.3 전체 파이프라인 실행 (Run Full Pipeline)
```bash
# Step-by-step (recommended for first time)
make data                # → data/processed/features_engineered.nc
make analysis            # → paper/results_auto.tex
make tables              # → paper/tables/*.tex
make figures             # → paper/figures/*.pdf
make paper               # → paper/output/main.pdf

# Or all at once:
make all
```

### 4.4 테스트 실행 (Run Tests)
```bash
# Quick test (핵심만)
pytest test/unit/test_models.py -v --no-cov

# Expected output:
# test_h1_negative_vagueness_effect PASSED
# test_h2_interaction_term_exists PASSED
# ...
# ======================== 53 passed in 2.34s ========================

# Full test (전체)
make test

# Expected output:
# test/unit/test_models.py .................... [ 68%]
# test/unit/test_features.py ............. [ 84%]
# test/integration/test_paper_results.py .... [100%]
# ======================== 78 passed in 4.12s ========================
```

---

## 5. 테스트 실패 시 대응 (Troubleshooting)

### Case 1: H1 계수 부호가 바뀜
```
FAILED test_h1_negative_vagueness_effect
AssertionError: H1: Vagueness should reduce early funding
```

**원인**:
- 데이터가 바뀜
- 모델 스펙 변경 (변수 추가/제거)
- 코딩 오류

**대응**:
1. 데이터 확인: `df['vagueness'].describe()` - 분포가 이상한가?
2. 모델 확인: `test_h1_early_funding(df).summary()` - 어떤 변수가 문제?
3. 이론 재검토: H1 가설이 틀렸을 수도 있음

### Case 2: 테이블 값 불일치
```
FAILED test_table1_matches_h1_model
AssertionError: Table coefficient -0.234 != Model coefficient -0.235
```

**원인**:
- LaTeX 생성 스크립트에서 반올림 차이
- 테이블 생성 시 다른 데이터 사용

**대응**:
1. `scripts/generate_paper_tables.py` 확인
2. `format_coef_se()` 함수의 소수점 자리수 확인
3. 테스트의 허용 오차 조정 (`decimal=3` → `decimal=2`)

### Case 3: Figure 생성 실패
```
FileNotFoundError: paper/figures/fig2_early_funding.pdf not found
```

**원인**:
- 그림 생성 스크립트 오류
- 경로 오타
- 데이터 부족 (빈 그림)

**대응**:
1. 직접 실행: `python -m src.cli generate-plots --dataset all`
2. 로그 확인: 어느 단계에서 실패?
3. 샘플 크기 확인: 그림 그릴 데이터가 충분한가?

---

## 6. CI/CD 통합 (GitHub Actions)

### 자동 테스트 (Every Push)
```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Run unit tests
        run: pytest test/unit/ -v
      - name: Run integration tests
        run: pytest test/integration/ -v
```

### 논문 자동 빌드 (On Main Branch)
```yaml
# .github/workflows/paper.yml
name: Build Paper

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run pipeline
        run: make all
      - name: Upload PDF
        uses: actions/upload-artifact@v3
        with:
          name: paper
          path: paper/output/main.pdf
```

---

## 7. 체크리스트 (Checklist)

### 논문 제출 전 (Before Submission)
- [ ] 모든 테스트 통과 (`make test`)
- [ ] 전체 파이프라인 실행 완료 (`make all`)
- [ ] PDF 컴파일 성공 (`paper/output/main.pdf` 존재)
- [ ] Table 1-2 값이 모델 결과와 일치
- [ ] Figure 2-3 파일 생성됨
- [ ] Results section 자동 생성됨 (`paper/results_auto.tex`)
- [ ] Git commit에 모든 변경사항 포함
- [ ] README에 재현 방법 명시

### 리뷰 피드백 후 (After Review)
- [ ] 데이터 변경 시 `make clean-all && make all` 재실행
- [ ] 모델 스펙 변경 시 테스트 업데이트
- [ ] 새로운 가설 추가 시 테스트 추가
- [ ] 모든 테스트 재검증

---

## 요약 (Summary)

**3가지 핵심 테스트**:
1. **모델 계수 테스트**: 논문의 핵심 주장이 데이터에서 나오는가?
2. **테이블 검증 테스트**: 자동 생성된 테이블이 모델 결과와 일치하는가?
3. **파이프라인 E2E 테스트**: 처음부터 끝까지 오류 없이 실행되는가?

**테스트 실행 순서**:
```bash
# 1. 빠른 검증 (1분)
pytest test/unit/test_models.py -v --no-cov

# 2. 전체 파이프라인 (5분)
make all

# 3. 모든 테스트 (5분)
make test

# 4. 논문 확인 (수동)
open paper/output/main.pdf
```

**성공 기준**:
- 모든 테스트 통과 (78/78 passed)
- PDF 생성 성공
- 테이블/그림 자동 생성
- Git에 모든 변경사항 commit

이제 데이터가 바뀌어도 `make all`만 실행하면 논문이 자동으로 업데이트됩니다! 🎉
