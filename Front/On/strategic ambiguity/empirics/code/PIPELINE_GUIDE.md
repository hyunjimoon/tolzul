# Pitchbook 데이터 분석 Pipeline

## 사용법

```bash
cd "Front/On/strategic ambiguity/empirics"

# 전체 실행
python code/pipeline_xarray.py

# 상태 확인
python code/pipeline_xarray.py --summary

# 3단계부터 재실행
python code/pipeline_xarray.py --from 3
```

## xarray 구조 이해하기

Pipeline 실행 후 생성되는 `output/pitchbook_analysis.nc` 파일:

```python
import xarray as xr

# 데이터 불러오기
ds = xr.open_dataset('output/pitchbook_analysis.nc')

# 전체 구조 보기
print(ds)
```

### 📊 Dimensions (차원)

```python
ds.dims
# {'company': 30, 'deal': 61, 'observation': 53}
```

- **company**: 30개 회사
- **deal**: 61개 딜 (Series A/B)
- **observation**: 53개 분석 데이터 포인트 (각 회사 × 2 라운드)

### 🏷️ Coordinates (좌표)

```python
# 회사 ID 목록
ds.coords['company']

# 딜 ID 목록
ds.coords['deal']

# 관측치 ID 목록
ds.coords['observation']
```

### 📈 Data Variables (변수들)

**회사 데이터** (company dimension):
```python
ds.company_CompanyName       # 회사 이름
ds.company_vagueness         # 모호성 점수 (0-100)
ds.company_Employees         # 직원 수
ds.company_TotalRaised       # 총 투자 금액
```

**딜 데이터** (deal dimension):
```python
ds.deal_round                # 'Series A' or 'Series B'
ds.deal_DealSize             # 딜 규모
ds.deal_funding_success      # 펀딩 성공 여부 (0/1)
```

**분석 패널** (observation dimension):
```python
ds.panel_vagueness           # 모호성 점수
ds.panel_funding_success     # 펀딩 성공 여부
ds.panel_round               # 라운드
ds.panel_series_b_dummy      # Series B 더미변수
```

### 🔍 데이터 접근 예제

```python
# 모든 회사의 모호성 점수
vagueness = ds.company_vagueness.values
print(f"평균 모호성: {vagueness.mean():.1f}")

# Series A vs B 성공률 비교
panel_df = ds.to_dataframe()
success_by_round = panel_df.groupby('panel_round')['panel_funding_success'].mean()
print(success_by_round)

# 특정 회사 정보
company_id = ds.coords['company'].values[0]
print(f"회사: {ds.company_CompanyName.sel(company=company_id).values}")
print(f"모호성: {ds.company_vagueness.sel(company=company_id).values}")
```

### 📝 Attributes (메타데이터)

```python
# Git 정보 (재현성)
print(ds.attrs['git_commit_url'])      # 어떤 코드로 생성했는지
print(ds.attrs['git_branch'])          # 어떤 브랜치에서

# 처리 단계 정보
print(ds.attrs['step_01_status'])      # 'completed'
print(ds.attrs['step_01_timestamp'])   # 언제 완료했는지

# 데이터 요약
print(ds.attrs['n_companies'])         # 30
print(ds.attrs['n_deals'])             # 61
print(ds.attrs['n_observations'])      # 53
```

## Pipeline 5단계

1. **회사 데이터 처리** → `company_*` 변수들 생성
2. **딜 데이터 처리** → `deal_*` 변수들 생성
3. **패널 생성** → `panel_*` 변수들 생성 (회사+딜 병합)
4. **회귀분석 실행** → `table2_model1.csv`, `table4_model2.csv`
5. **결과물 생성** → 표 4개 + 그림 2개

## Output 파일들

```
output/
├── pitchbook_analysis.nc           # 모든 데이터 (여기만 보면 됨!)
├── table1_descriptives.csv         # 기술통계
├── table2_model1.csv               # 회귀분석 1
├── table4_model2.csv               # 회귀분석 2
├── figure2_vagueness_curves.png    # 시각화
└── model_results.pkl               # 상세 회귀결과
```

## 빠른 데이터 탐색

```python
import xarray as xr
import pandas as pd

ds = xr.open_dataset('output/pitchbook_analysis.nc')

# 1. 전체 변수 목록
print(list(ds.data_vars))

# 2. DataFrame으로 변환
df = ds.to_dataframe()

# 3. 특정 변수들만 선택
subset = ds[['company_vagueness', 'company_Employees']]

# 4. 조건으로 필터링
high_vague = ds.where(ds.company_vagueness > 60, drop=True)
```

## 다음 단계

1. 실제 Pitchbook 데이터를 `data/raw/`에 복사
2. `python code/pipeline_xarray.py` 실행
3. `output/pitchbook_analysis.nc` 열어서 결과 확인!
