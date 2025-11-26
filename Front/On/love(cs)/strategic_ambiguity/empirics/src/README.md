# src/ - Core Analysis Modules ("The Brain")

## 📂 구조

```
src/
├── __init__.py      # 패키지 초기화
├── features.py      # 데이터 로드 및 기본 피처 엔지니어링
├── models.py        # 통계 모델 (OLS, Logit)
├── vagueness_v2.py  # Vagueness scorer V2
├── plotting.py      # 시각화 (F-series plots)
├── empirical.py     # τ 궤적 및 xarray 분석
├── multiverse.py    # Specification curve analysis
├── cli.py           # 파이프라인 CLI (Steps 1-5)
└── README.md        # 이 문서
```

## 📋 모듈 설명

### 1. `features.py` - 데이터 로드 및 피처 엔지니어링

**역할**: 원천 데이터(`.dat`)를 로드하고 기본 변수를 생성합니다.

**핵심 함수**:
```python
from features import (
    consolidate_company_snapshots,  # 데이터 로드
    engineer_features,               # 피처 생성
    classify_hardware_or_software,   # F (HW/SW) 분류
    create_survival_seriesb_progression,  # Series B 도달 여부
)
```

**사용 예시**:
```python
# 데이터 로드
df = consolidate_company_snapshots('data/raw')

# 피처 생성
df_with_features = engineer_features(df)
```

### 2. `models.py` - 통계 모델

**역할**: 가설 검정을 위한 회귀분석 함수들.

**핵심 함수**:
```python
from models import (
    test_h1_early_funding,  # H1: E ~ V (OLS)
    test_h2_main_growth,    # H2: L ~ V × F (Logit)
)
```

**사용 예시**:
```python
# H1 검정
h1_results = test_h1_early_funding(df)

# H2 검정
h2_results = test_h2_main_growth(df)
```

**원칙**:
- 공식(Formula)은 여기서만 관리
- Pipeline에서 공식을 하드코딩하지 않음

### 3. `vagueness_v2.py` - Vagueness Scorer

**역할**: Strategic Vagueness Score 계산.

**핵심 클래스**:
```python
from vagueness_v2 import StrategicVaguenessScorerV2

scorer = StrategicVaguenessScorerV2()
vagueness_scores = scorer.score(
    df['Description'],
    df['Keywords']
)
```

**공식**:
```
V_raw = 0.5 × max(S_cat, S_concdef) + 0.5 × mean(S_cat, S_concdef)

where:
  S_cat = Categorical vagueness (abstract terms)
  S_concdef = Concreteness deficit
```

### 4. `plotting.py` - 시각화 (NEW!)

**역할**: 논문용 F-series 그림 생성.

**색상 팔레트** (W2 convention):
```python
PALETTE = {
    "E": "red",        # Early funding
    "L": "#0000FF",    # Later success
    "V": "green",      # Vagueness
    "F": "skyblue",    # Flexibility (Software)
    "HW": "gray",      # Hardware
    "C": "orange",     # Credibility
}
```

**핵심 함수**:
```python
from plotting import (
    fig_F3a_L_given_F,      # 핵심: Vagueness × F interaction
    fig_F1_E_vs_V,          # Early funding vs Vagueness
    fig_F2_PrL_vs_V,        # P(Series B) vs Vagueness
    create_F_series,        # 모든 그림 생성
)
```

**사용 예시**:
```python
# F3a만 생성
fig_F3a_L_given_F(df, h2_result, output_dir)

# 전체 F-series 생성
create_F_series(df, {'h2': h2_result}, output_dir)
```

### 5. `empirical.py` - τ 궤적 분석 (NEW!)

**역할**: 단순 피처를 넘어선 복합 지표 계산.

**핵심 함수**:
```python
from empirical import (
    calculate_tau_trajectory,          # τ₀, τ₁, Δτ 계산
    prepare_cohort_tensor,             # xarray 텐서 생성
    compute_productive_ambiguity_index,   # 생산적 모호성 지표
    compute_destructive_ambiguity_index,  # 파괴적 모호성 지표
)
```

**사용 예시**:
```python
# τ 궤적 계산
df_with_tau = calculate_tau_trajectory(df, t0=2021, t1=2024)

# xarray 텐서 생성
ds = prepare_cohort_tensor(
    df,
    cohort_years=[2021, 2022, 2023],
    horizon_years=[1, 2, 3]
)

# 2022 cohort 추출
cohort_2022 = ds.where(ds.snapshot_year == 2022, drop=True)
```

**τ 궤적 의미**:
- τ₀: 초기 전략적 모호성 (Series A 시점)
- τ₁: 나중 모호성 (관찰 종료 시점)
- Δτ: 변화량 (감소? 증가?)

### 6. `multiverse.py` - Specification Curve (NEW!)

**역할**: 여러 사양(specification)을 돌려 강건성 검증.

**핵심 함수**:
```python
from multiverse import (
    build_spec_grid,       # 사양 조합 생성
    run_spec_curve,        # 모든 사양 실행
    plot_spec_curve,       # Spec curve 시각화
    summarize_spec_curve,  # 요약 통계
)
```

**사용 예시**:
```python
# 1. Spec grid 생성
spec_grid = build_spec_grid(
    vagueness_measures=['z_vagueness', 'z_vagueness_winsorized'],
    outcome_windows=[2024, 2025, 2026],
    control_sets=[
        ('z_employees_log', 'founding_cohort'),
        ('z_employees_log', 'founding_cohort', 'sector_fe'),
    ],
)

print(f"Total specifications: {len(spec_grid)}")

# 2. 전체 실행
results = run_spec_curve(df, spec_grid, hypothesis='H2')

# 3. 시각화
plot_spec_curve(results, output_path='outputs/spec_curve.png')

# 4. 요약
summary = summarize_spec_curve(results)
print(f"Significant: {summary['pct_significant_05']:.1f}%")
```

**해석**:
- 사양 curve가 0 위에 있고 대부분 significant → 강건한 결과
- 사양에 따라 sign이 바뀜 → 약한 결과

### 7. `cli.py` - 파이프라인 CLI (NEW!)

**역할**: 전체 분석 파이프라인을 통합한 명령줄 인터페이스.

**사용 가능한 명령어**:
```bash
# 개별 스텝 실행
python -m src.cli load-data            # Step 1: 데이터 로드
python -m src.cli engineer-features    # Step 2: 피처 생성
python -m src.cli filter-datasets      # Step 3: 데이터셋 필터링
python -m src.cli run-models --dataset all  # Step 4: 모델 실행
python -m src.cli generate-plots --dataset quantum  # Step 5: 그림 생성

# 전체 파이프라인 실행
python -m src.cli run-all
```

**옵션**:
```bash
# 도움말
python -m src.cli --help
python -m src.cli run-models --help

# 특정 데이터셋만 실행
python -m src.cli run-models --dataset quantum
python -m src.cli run-models --dataset transportation
python -m src.cli generate-plots --dataset all  # 기본값
```

**장점**:
- 모든 분석 로직이 `src/` 모듈에 통합됨
- Pipeline 스크립트 중복 제거
- 일관된 명령어 인터페이스
- Jupyter notebook에서도 모듈 재사용 가능

## 🔄 모듈 간 관계

```
cli.py (orchestration)
    ↓
┌───────────────────────────────────┐
│  src/ (core logic)                │
│                                   │
│  features.py  →  models.py        │
│       ↓              ↓            │
│  vagueness_v2.py  plotting.py    │
│       ↓              ↓            │
│  empirical.py  →  multiverse.py  │
└───────────────────────────────────┘
```

**데이터 흐름**:
1. `features.py`: 데이터 로드 및 기본 변수 생성
2. `vagueness_v2.py`: Vagueness score 추가
3. `models.py`: H1, H2 통계 모델 실행
4. `plotting.py`: 결과 시각화
5. `empirical.py`: τ 궤적 분석, xarray 텐서
6. `multiverse.py`: Robustness 검증

## 📝 사용 규칙

### ✅ DO:
- 모든 분석 로직을 `src/`에 정의
- Pipeline은 `src/` 함수를 호출만 함
- 새 기능 추가 시 적절한 모듈에 추가

### ❌ DON'T:
- Pipeline에서 직접 분석 로직 구현
- `modules/`의 중복 파일 사용 (archived)
- 여러 곳에 같은 함수 정의

## 🚀 다음 단계

### Step 06: Trajectory Analysis
```python
# pipeline/06_trajectory.py
from features import consolidate_company_snapshots
from empirical import calculate_tau_trajectory, prepare_cohort_tensor
from models import run_trajectory_model  # TODO: 추가 필요
from plotting import plot_tau_evolution  # TODO: 추가 필요
```

### Step 07: Multiverse Analysis
```python
# pipeline/07_multiverse.py
from features import engineer_features
from multiverse import build_spec_grid, run_spec_curve, plot_spec_curve
```

## 📚 참고 문서

- **Vagueness Scorer**: `docs_archive/VAGUENESS_SCORER_V2_GUIDE.md`
- **F-series Plots**: `docs_archive/F_SERIES_PLOTS_GUIDE.md`
- **xarray Design**: `XARRAY_DESIGN_README.md`
- **State-based Cohorts**: `STATE_BASED_COHORTS_README.md`

## 🧹 Archived Files

**`modules/` 폴더**는 이제 archived 상태입니다:
- `modules/modules_features.py` → `src/features.py`
- `modules/modules_models.py` → `src/models.py`
- `modules/modules_plots_F_series.py` → `src/plotting.py`
- `modules/vagueness_v2.py` → `src/vagueness_v2.py`

**절대 `modules/`를 import하지 마세요!** 항상 `src/`를 사용하세요.

---

**장군님, 이제 모든 기능이 `src/` "뇌" 안에 깔끔하게 정리되었습니다!** 🧠✨
