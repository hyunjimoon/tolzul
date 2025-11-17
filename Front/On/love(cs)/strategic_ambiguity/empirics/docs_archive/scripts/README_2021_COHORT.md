# 2021 Cohort Data Preparation

2021년 코호트의 2년, 3년, 4년 후 progression 추적을 위한 데이터 준비 스크립트입니다.

## 목표

**2021.12 baseline** (Company20211201.parquet)에서 Early Stage VC인 회사들을:
- **2년 후** (2023.12)
- **3년 후** (2024.12)
- **4년 후** (2025.11)

시점에서 추적하여 Later Stage VC 진행률을 측정합니다.

## 실행 순서

### 1단계: DAT → Parquet 변환

```bash
python scripts/convert_dat_to_parquet.py
```

**변환 대상:**
- `Company20231201.dat` → `Company20231201.parquet`
- `Company20241201.dat` → `Company20241201.parquet`
- `Company20251101.dat` → `Company20251101.parquet`

**위치:** `data/raw/`

### 2단계: Consolidate (통합)

```bash
python scripts/consolidate_2021_cohort.py
```

**입력:**
- `data/raw/Company20211201.parquet` (baseline)
- `data/raw/Company20231201.parquet` (2년 후)
- `data/raw/Company20241201.parquet` (3년 후)
- `data/raw/Company20251101.parquet` (4년 후)

**출력:**
- `data/processed/companies_21_23-24-25.parquet` (전체 회사)
- `data/processed/companies_21_23-24-25_quantum.parquet` (양자컴퓨팅 회사만)
- `data/processed/companies_21_23-24-25_transportation.parquet` (자율주행/물류 회사만)

### 3단계: 테스트

```bash
python scripts/test_consolidated_data.py
```

**검사 항목:**
1. 파일 존재 확인
2. Row/Column 개수
3. CompanyID 중복 검사
4. DealType 컬럼 populated 비율
5. Cross-year consistency
6. Sample data 확인

## 출력 파일 구조

### companies_21_23-24-25.parquet

| Column | Description |
|--------|-------------|
| CompanyID | 회사 고유 ID |
| CompanyName | 회사 이름 |
| DealType_2021 | 2021.12 LastFinancingDealType |
| DealType_2023 | 2023.12 LastFinancingDealType |
| DealType_2024 | 2024.12 LastFinancingDealType |
| DealType_2025 | 2025.11 LastFinancingDealType |

### companies_21_23-24-25_quantum.parquet

위와 동일하나, CompanyName에 다음 키워드 포함된 회사만:
- quantum
- qubit
- superconducting
- photonic
- trapped
- ion

## 예상 결과

### 2021 Cohort (예상):

```
Baseline (2021.12): ~40,000 companies at Early Stage VC

2년 후 (2023.12): ~6,500 (16%) → Later Stage
3년 후 (2024.12): ~7,200 (18%) → Later Stage
4년 후 (2025.11): ~8,000 (20%) → Later Stage
```

## Troubleshooting

### "File not found" 에러

```bash
# 파일 확인
ls -lh data/raw/Company*.dat
ls -lh data/raw/Company*.parquet

# 파일이 없으면 PitchBook에서 다운로드 필요
```

### "No quantum companies found"

CompanyName 컬럼이 없거나, 키워드 매칭이 안되는 경우입니다.
- 수동으로 양자 회사 리스트를 만들어야 할 수 있습니다.

### Parquet 파일이 너무 큼

```python
# 필요한 컬럼만 선택하여 저장
df = df[['CompanyID', 'CompanyName', 'LastFinancingDealType']]
df.to_parquet('output.parquet', compression='snappy')
```

## 다음 단계: 분석

통합 데이터가 준비되면 분석 스크립트 실행:

### 전체 회사 분석

```bash
python scripts/analyze_2021_cohort.py
```

### 산업별 분석

```bash
# Quantum computing
python scripts/analyze_2021_cohort.py --industry quantum

# Transportation/Autonomous vehicles
python scripts/analyze_2021_cohort.py --industry transportation
```

### 출력 결과

1. **터미널 출력:**
   - Progression rates (2년, 3년, 4년)
   - HW/SW 비교
   - 통계적 유의성 검정 (chi-square test)
   - 가설 검정 결과

2. **CSV 파일:**
   - `outputs/cohort_2021/summary_[industry].csv`
   - `outputs/cohort_2021/hw_sw_comparison_[industry].csv`

3. **Plot (PNG):**
   - `outputs/cohort_2021/hw_sw_comparison_[industry].png`
   - HW vs SW progression rate 막대그래프
   - 통계적 유의성 표시 (*)

### 예상 분석 결과

```
2021 COHORT ANALYSIS - QUANTUM COMPANIES

Cohort: 50 companies at Early Stage VC (2021.12)

Progression by Type:
Year   HW Rate      SW Rate      Diff       p-value
2023   5.0%         25.0%        +20.0%     0.0234*
2024   7.5%         30.0%        +22.5%     0.0156*
2025   10.0%        35.0%        +25.0%     0.0089**

Statistical Summary:
  H0: SW rate = HW rate
  H1: SW rate > HW rate

  Results:
    2023: ✓ REJECT H0 (SW +20.0% faster, p=0.0234)
    2024: ✓ REJECT H0 (SW +22.5% faster, p=0.0156)
    2025: ✓ REJECT H0 (SW +25.0% faster, p=0.0089)
```
