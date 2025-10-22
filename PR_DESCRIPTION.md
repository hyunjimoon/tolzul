# Pitchbook 데이터 분석 Pipeline (xarray 기반)

## 요약

Pitchbook 데이터를 분석하는 5단계 pipeline입니다. 모든 데이터가 하나의 xarray Dataset에 저장되어 쉽게 탐색할 수 있습니다.

## 핵심 기능

### ✅ 하나의 파일에 모든 데이터

```python
import xarray as xr

ds = xr.open_dataset('output/pitchbook_analysis.nc')
print(ds)  # 모든 변수를 한눈에!
```

**포함된 데이터**:
- 📊 **Dimensions**: company (30), deal (61), observation (53)
- 📈 **Variables**: 40+ 개 (company_*, deal_*, panel_*)
- 📝 **Attributes**: git 메타데이터, 처리 단계 정보

### ✅ xarray 구조

**Dimensions (차원)**:
- `company`: 회사별 데이터
- `deal`: 딜별 데이터
- `observation`: 분석 패널 (회사 × 라운드)

**Variables (변수)**:
```python
ds.company_vagueness        # 모호성 점수 (0-100)
ds.company_Employees        # 직원 수
ds.deal_funding_success     # 펀딩 성공 여부
ds.panel_series_b_dummy     # Series B 더미
```

**Attributes (메타데이터)**:
```python
ds.attrs['git_commit_url']    # 재현성: 어떤 코드로 생성?
ds.attrs['n_companies']       # 데이터 요약: 30개 회사
ds.attrs['step_01_status']    # 처리 상태: completed
```

### ✅ 간단한 사용법

```bash
# 실행
python code/pipeline_xarray.py

# 상태 확인
python code/pipeline_xarray.py --summary

# 재실행 (3단계부터)
python code/pipeline_xarray.py --from 3
```

### ✅ 데이터 탐색

```python
# DataFrame으로 변환
df = ds.to_dataframe()

# 변수 선택
subset = ds[['company_vagueness', 'company_Employees']]

# 조건 필터
high_vague = ds.where(ds.company_vagueness > 60, drop=True)

# 평균 계산
print(f"평균 모호성: {ds.company_vagueness.values.mean():.1f}")
```

## Pipeline 5단계

1. **회사 데이터 처리** → AI/ML 회사 필터링, 모호성 점수 계산
2. **딜 데이터 처리** → Series A/B 식별, 펀딩 성공 변수 생성
3. **패널 생성** → 회사+딜 병합 (각 회사 × 2 라운드)
4. **회귀분석** → 2-way/3-way 상호작용
5. **결과물 생성** → 표 4개 + 그림 2개

## Output 파일

```
output/
├── pitchbook_analysis.nc           ← 모든 데이터 여기 있음!
├── table1_descriptives.csv
├── table2_model1.csv
├── table4_model2.csv
├── figure2_vagueness_curves.png
└── model_results.pkl
```

## 재현성 (Git Metadata)

생성된 결과가 어떤 코드로 만들어졌는지 자동 추적:

```python
print(ds.attrs['git_commit_url'])
# → https://github.com/hyunjimoon/tolzul/commit/...

print(ds.attrs['git_branch'])
# → claude/pitchbook-pipeline-updates-011CUNKR6EKWqqHsAjq1cTAG

print(ds.attrs['step_05_timestamp'])
# → 2025-10-22T16:52:57...
```

## 테스트 결과

✅ 샘플 데이터로 성공적으로 테스트:
- 30 AI/ML 회사
- 61 딜 (Series A/B)
- 53 관측치 (패널)
- 5단계 모두 완료

## 파일 변경사항

**추가**:
- `code/pipeline_xarray.py` - 메인 pipeline
- `code/PIPELINE_GUIDE.md` - xarray 구조 설명서

**Output 예시**:
- `output/pitchbook_analysis.nc` - 모든 데이터
- `data/processed/*.parquet` - 중간 파일들

## 다음 단계

1. 실제 Pitchbook 데이터를 `data/raw/`에 복사
2. `python code/pipeline_xarray.py` 실행
3. `output/pitchbook_analysis.nc` 열어서 탐색!

상세 내용은 `code/PIPELINE_GUIDE.md` 참고.
