# 🚀 Quick Start Guide - 로컬 실행

## 📋 목차
1. [환경 설정](#1-환경-설정)
2. [빠른 테스트 (5분)](#2-빠른-테스트-5분)
3. [전체 파이프라인 (30분-2시간)](#3-전체-파이프라인-30분-2시간)
4. [생성되는 출력물](#4-생성되는-출력물)
5. [트러블슈팅](#5-트러블슈팅)

---

## 1. 환경 설정

### 1.1 브랜치 가져오기

```bash
# 현재 master 브랜치에서 작업 중이라면
cd "/path/to/tolzul/Front/On/love(cs)/strategic ambiguity/empirics"

# 작업 내용 백업 (선택사항)
cp -r . ~/backup_$(date +%Y%m%d_%H%M%S)

# 최신 변경사항 가져오기
git fetch origin claude/moderator-bakeoff-analysis-011CUbKc3dAVgd5eU3SXn7k8
git merge origin/claude/moderator-bakeoff-analysis-011CUbKc3dAVgd5eU3SXn7k8
```

**또는 특정 파일만 가져오기:**
```bash
git fetch origin claude/moderator-bakeoff-analysis-011CUbKc3dAVgd5eU3SXn7k8
git checkout origin/claude/moderator-bakeoff-analysis-011CUbKc3dAVgd5eU3SXn7k8 -- \
  modules/models.py \
  modules/plots.py \
  modules/features.py \
  run_analysis.py \
  test_one_touch.py
```

### 1.2 Python 환경

**필수 패키지 확인:**
```bash
pip list | grep -E "pandas|numpy|matplotlib|statsmodels|scikit-learn|seaborn|scipy"
```

**없으면 설치:**
```bash
pip install pandas numpy matplotlib statsmodels scikit-learn seaborn scipy
```

---

## 2. 빠른 테스트 (5분) ⚡ **추천!**

기존 데이터셋(`outputs/h2_analysis_dataset.csv`)을 사용하여 빠르게 테스트

### 2.1 테스트 실행

```bash
cd "/path/to/tolzul/Front/On/love(cs)/strategic ambiguity/empirics"
python test_one_touch.py
```

### 2.2 예상 출력

```
================================================================================
ONE-TOUCH EXECUTION TEST
================================================================================

✓ Loading dataset: outputs/h2_analysis_dataset.csv
  Rows: 5,000

H1: EARLY FUNDING ────────────────
✓ H1 fitted: R² = 0.002

H2: GROWTH × ARCHITECTURE ───────
✓ H2 fitted: Pseudo R² = 0.019

H3: EARLY FUNDING × FOUNDER ─────
✓ H3 fitted: R² = 0.003
✓ Saved: outputs/h3_coefficients.csv

H4: GROWTH × FOUNDER ─────────────
✓ H4 fitted: Pseudo R² = 0.016
✓ Saved: outputs/h4_coefficients.csv

GENERATING FIGURES ───────────────
✓ Saved: outputs/figures/Figure_1_Reversal.png
✓ Saved: outputs/figures/Figure_2a_H3.png
✓ Saved: outputs/figures/Figure_2b_H4.png

TEST COMPLETE
```

### 2.3 생성된 파일 확인

```bash
ls -lh outputs/h*.csv
ls -lh outputs/figures/*.png
```

**예상 파일:**
- `outputs/h1_coefficients.csv`
- `outputs/h3_coefficients.csv` ← NEW
- `outputs/h4_coefficients.csv` ← NEW
- `outputs/figures/Figure_1_Reversal.png` ← NEW
- `outputs/figures/Figure_2a_H3.png` ← NEW
- `outputs/figures/Figure_2b_H4.png` ← NEW

---

## 3. 전체 파이프라인 (30분-2시간)

실제 PitchBook 데이터부터 처음부터 끝까지 실행

### 3.1 데이터 준비

**데이터 위치 확인:**
```bash
ls -lh data/raw/Company*.dat
```

**필요한 파일:**
- `data/raw/Company20211201.dat` (baseline, t0)
- `data/raw/Company20220101.dat` (mid1, tm1)
- `data/raw/Company20220501.dat` (mid2, tm2)
- `data/raw/Company20230501.dat` (endpoint, t1)

**데이터가 없으면:**
```bash
# 합성 데이터 생성 (테스트용)
python generate_synthetic_data.py
```

### 3.2 전체 파이프라인 실행

```bash
python run_analysis.py
```

**실행 시간:**
- 합성 데이터 (5K rows): ~5분
- 실제 데이터 (50K+ rows): ~30분-2시간

### 3.3 예상 출력

```
W1 HYPOTHESIS TESTING (CLEAN)
════════════════════════════════

Loading 4 snapshots...
✓ Baseline: 45,234 companies
✓ Mid1: 46,891 companies
✓ Mid2: 48,123 companies
✓ Endpoint: 51,456 companies

Feature engineering...
  ℹ️ Early funding filtered to Series A / Early Stage VC: 23,456 of 45,234

DV creation (Series B+ progression)...
  📅 Applying as-of date capping...
  🎯 At-risk cohort: 23,456 companies
  📊 Base rate: 13.8%

H1: EARLY FUNDING ────────────────
✓ Saved: outputs/h1_coefficients.csv

H2: GROWTH × ARCHITECTURE ───────
✓ Saved: outputs/h2_main_coefficients.csv

H3: EARLY FUNDING × FOUNDER ─────
✓ Saved: outputs/h3_coefficients.csv

H4: GROWTH × FOUNDER ─────────────
✓ Saved: outputs/h4_coefficients.csv

BAKE-OFF: Architecture vs Credibility
✓ Saved: outputs/h2_model_architecture.csv
✓ Saved: outputs/h2_model_founder.csv

GENERATING FIGURES ───────────────
✓ Saved: outputs/figures/Figure_1_Reversal.png
✓ Saved: outputs/figures/Figure_2a_H3.png
✓ Saved: outputs/figures/Figure_2b_H4.png

ONE-TOUCH EXECUTION COMPLETE
```

---

## 4. 생성되는 출력물

### 4.1 계수표 (CSV)

```bash
outputs/
├── h1_coefficients.csv           # H1: Early Funding ~ Vagueness
├── h2_main_coefficients.csv      # H2: Growth ~ Vagueness × Architecture
├── h3_coefficients.csv           # H3: Early Funding ~ Vagueness × Founder
├── h4_coefficients.csv           # H4: Growth ~ Vagueness × Founder
├── h2_model_architecture.csv     # Bake-off: Architecture moderator
├── h2_model_architecture_ame.csv
├── h2_model_architecture_metrics.csv
├── h2_model_founder.csv          # Bake-off: Founder moderator
├── h2_model_founder_ame.csv
└── h2_model_founder_metrics.csv
```

### 4.2 시각화 (PNG)

```bash
outputs/figures/
├── Figure_1_Reversal.png         # H1 + H2 dual-axis plot
├── Figure_2a_H3.png              # Early Funding × Founder (scatter + OLS)
└── Figure_2b_H4.png              # Growth × Founder (scatter + logistic)
```

### 4.3 데이터셋

```bash
outputs/
└── h2_analysis_dataset.csv       # 분석용 최종 데이터셋
```

---

## 5. 트러블슈팅

### 문제 1: ModuleNotFoundError

**증상:**
```
ModuleNotFoundError: No module named 'pandas'
```

**해결:**
```bash
pip install pandas numpy matplotlib statsmodels scikit-learn seaborn scipy
```

### 문제 2: 데이터 파일 없음

**증상:**
```
FileNotFoundError: data/raw/Company20211201.dat not found
```

**해결 옵션:**

**A. 합성 데이터 사용 (빠름):**
```bash
python generate_synthetic_data.py
python test_one_touch.py  # 빠른 테스트
```

**B. 실제 데이터 경로 확인:**
```bash
find . -name "Company*.dat" -type f
# 파일을 data/raw/로 이동
```

### 문제 3: 메모리 부족 (대용량 데이터)

**증상:**
```
MemoryError: Unable to allocate array
```

**해결:**
```bash
# 샘플링하여 실행
python run_analysis.py --sample 0.1  # 10% 샘플
```

**또는 run_analysis.py 수정:**
```python
# Line 58 근처
df = pd.read_csv(path, sep='|', encoding=encoding, low_memory=False, nrows=50000)
                                                                    ^^^^^^^^^^^^
```

### 문제 4: 그림이 생성되지 않음

**증상:**
```
WARNING: Could not plot H1 predictions
```

**확인:**
```bash
# 필요한 컬럼이 있는지 확인
python -c "
import pandas as pd
df = pd.read_csv('outputs/h2_analysis_dataset.csv')
print(df.columns.tolist())
"
```

**필수 컬럼:**
- `z_vagueness`, `z_employees_log`, `founding_cohort`
- `early_funding_musd`, `growth`
- `founder_serial` (또는 `founder_credibility`)

### 문제 5: Convergence 실패 (Logit)

**증상:**
```
PerfectSeparationError: Perfect separation detected
```

**해결:** 코드가 자동으로 처리합니다
```python
# models.py Line 85, 173
try:
    model = smf.logit(formula, data=d).fit(disp=False)
except Exception:
    model = smf.logit(formula, data=d).fit_regularized(method='l2', alpha=0.01)
```

---

## 6. 추가 분석 스크립트

### 6.1 Follow-up Period 분석

```bash
python test_followup_period.py
```

**출력:**
- Base rate 분석
- Right censoring 영향
- Statistical power 평가

### 6.2 Series A 필터링 검증

```bash
python test_series_a_filter.py
```

**출력:**
- FirstFinancingDealType 분포
- "Early Stage VC" 매칭 수
- 필터링 전후 비교

---

## 7. 빠른 체크리스트 ✅

실행 전:
- [ ] Python 3.7+ 설치
- [ ] 필수 패키지 설치 (pandas, statsmodels, etc.)
- [ ] 브랜치 업데이트 또는 파일 복사
- [ ] 작업 디렉토리 이동

빠른 테스트 (추천):
- [ ] `python test_one_touch.py` 실행
- [ ] outputs/ 폴더 확인
- [ ] 그림 파일 열어보기

전체 파이프라인:
- [ ] 데이터 파일 준비 (data/raw/)
- [ ] `python run_analysis.py` 실행
- [ ] 생성된 CSV/PNG 확인
- [ ] 계수표와 그림 비교 분석

---

## 8. 다음 단계

### 분석 결과 확인:

```bash
# 계수표 확인
head outputs/h3_coefficients.csv
head outputs/h4_coefficients.csv

# 상호작용 p-value 확인
grep "vagueness.*founder_serial" outputs/h3_coefficients.csv
grep "vagueness.*founder_serial" outputs/h4_coefficients.csv

# 그림 열기 (macOS)
open outputs/figures/Figure_1_Reversal.png
open outputs/figures/Figure_2a_H3.png
open outputs/figures/Figure_2b_H4.png

# 그림 열기 (Linux)
xdg-open outputs/figures/Figure_1_Reversal.png
```

### Python에서 결과 로드:

```python
import pandas as pd
import matplotlib.pyplot as plt

# 계수표 읽기
h3 = pd.read_csv('outputs/h3_coefficients.csv')
h4 = pd.read_csv('outputs/h4_coefficients.csv')

# 상호작용 항만 필터
h3_interaction = h3[h3['variable'].str.contains('vagueness.*founder_serial', regex=True)]
h4_interaction = h4[h4['variable'].str.contains('vagueness.*founder_serial', regex=True)]

print("H3 Interaction:")
print(h3_interaction[['variable', 'coefficient', 'p_value']])

print("\nH4 Interaction:")
print(h4_interaction[['variable', 'coefficient', 'p_value']])
```

---

## 📞 도움말

**문제가 계속되면:**
1. 로그 파일 확인
2. Python 버전 확인: `python --version`
3. 패키지 버전 확인: `pip list`
4. GitHub Issue 열기 또는 문의

**성공적으로 실행되면:**
- 생성된 그림들을 논문에 사용
- 계수표를 바탕으로 통계 검정
- Robustness checks 실행 (robustness_followup.md 참조)
