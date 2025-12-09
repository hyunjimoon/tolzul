# 📊 Data Inventory

## Overview
이 디렉토리는 "Promise Precision and Venture Funding" 논문의 실증 분석을 위한 원재료 데이터를 보관합니다.

---

## 📁 Files

### `data_pipeline.md`
**Source:** `2💻/features_models_plots.md`

**Description:** 데이터 처리 파이프라인 설명
- Feature engineering 과정
- 모델 선택 로직
- 시각화 전략

**Status:** ✅ Migrated

---

### `quantum_10cases.csv` 
**Source:** W2 Presentation (p.22 table)

**Description:** 양자컴퓨팅 벤처 10개 케이스 스터디
- **Columns (예상):**
  - `company_name`: 회사명
  - `founding_year`: 설립연도
  - `approach`: HW/SW 구분
  - `series_a_amount`: Series A 금액 (만불)
  - `series_b_reached`: Series B 도달 여부 (0/1)
  - `promise_vagueness`: 약속 모호성 지수 (0–1)
  - `pivot_count`: 피벗 횟수

**Status:** 🚧 To be created (W2 슬라이드 데이터 추출 필요)

---

## 🔄 Data Lineage

```
[PitchBook API / Manual Collection]
         ↓
  1️⃣_INPUT/data/
         ↓
  2️⃣_PRODUCTION/Empirics_*/run.py
         ↓
  3️⃣_OUTPUT/tables/ & figures/
```

---

## 📝 Notes

### Expected Data Structure (PitchBook-style)
```csv
company_id,name,founding_year,hq_country,first_deal_type,
series_a_date,series_a_amount,series_b_date,series_b_amount,
hw_sw_flag,vagueness_index,pivot_binary
```

### Vagueness Index Construction
- **Source:** 피칭 문서 / 웹사이트 텍스트
- **Method:** 
  - 정밀한 약속 키워드 (specific, by YYYY, N qubits) → 낮은 점수
  - 모호한 약속 키워드 (explore, potential, future) → 높은 점수
  - 범위: 0 (완전 정밀) ~ 1 (완전 모호)

### HW/SW Classification
- **HW (Hardware-centric):** Superconducting, Ion trap, Photonic
  - 특징: 높은 자본 투자, 긴 개발 주기, 비가역적 선택
- **SW (Software-centric):** Algorithm, Cloud platform, Quantum apps
  - 특징: 낮은 자본 투자, 빠른 반복, 가역적 피벗

---

## ✅ Quality Checks

- [ ] `quantum_10cases.csv` 생성 완료
- [ ] Missing values < 5%
- [ ] Vagueness index validated (inter-rater reliability > 0.8)
- [ ] HW/SW classification validated by domain expert

---

*Last updated: 2025-11-16*
*Maintained by: 권준/나대용 (中軍)*
