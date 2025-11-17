---
modified:
  - 2025-11-16T13:20:14-05:00
---
# Placeholder 치환 레지스트리

## 계수 (Coefficients)

### β_EV (Early Funding)
- **위치**: `05-Results-1_EarlyFundingPenalty.md:3`
- **형식**: "V 1 SD ↑ → **X–Y%** ↓ in Series A"
- **출처**: `_OUTPUT/regression/modelA_results.csv`
- **상태**: ⏳ 대기중

### a-b%p (Later Success)
- **위치**: `05-Results-2_LaterSuccessBenefit.md:2`
- **형식**: "V 1 SD ↑ → **a–b%p** ↑ in L"
- **출처**: `_OUTPUT/regression/modelB_marginal_effects.csv`
- **상태**: ⏳ 대기중

### V×F 상호작용
- **위치**: `05-Results-3_VxF_Interaction.md:1`
- **형식**: "V×F = **0.XXX***"
- **출처**: `_OUTPUT/regression/modelB_interaction.csv`
- **상태**: ⏳ 대기중

---

## 표 (Tables)

### T1_ModelA_EarlyFunding
- **위치**: `_OUTPUT/tables/T1_ModelA_EarlyFunding.md`
- **치환 대상**: 모든 `0.XXX`, `(0.0XX)`, `XXX` (N, R²)
- **출처**: `_OUTPUT/regression/table1_formatted.csv`
- **상태**: 템플릿 완료

### T2_ModelB_LaterSuccess
- **위치**: `_OUTPUT/tables/T2_ModelB_LaterSuccess.md`
- **치환 대상**: 계수, SE, Pseudo-R², Baseline Prob
- **출처**: `_OUTPUT/regression/table2_formatted.csv`
- **상태**: 템플릿 완료

---

## 치환 프로세스

### 1단계: 회귀 실행
```python
# empirics/analysis/run_regressions.py
python run_regressions.py --output _OUTPUT/regression/
```

### 2단계: 수치 추출
```python
# 예시
import pandas as pd
results = pd.read_csv('_OUTPUT/regression/modelA_results.csv')
beta_EV = results.loc['Vagueness', 'coef']
se_EV = results.loc['Vagueness', 'se']
```

### 3단계: 파일 치환
```bash
# 05-Results-1_EarlyFundingPenalty.md
sed -i 's/X–Y%/12.3–18.7%/g' 05-Results-1_EarlyFundingPenalty.md
```

또는 수동:
1. status_tracker.md에서 "대기중" 항목 확인
2. 해당 .md 파일 열기
3. `X–Y%`, `a–b%p`, `0.XXX` 검색
4. 회귀 결과에서 복사→붙여넣기

---

**다음 작업**: 회귀 실행 → 계수 추출 → placeholder 치환