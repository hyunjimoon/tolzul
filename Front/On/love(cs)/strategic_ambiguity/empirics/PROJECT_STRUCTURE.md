# 프로젝트 구조 (5개 폴더)
# Project Structure (5 Folders)

## 📁 최종 구조 (Final Structure - 5 Folders)

```
empirics_ent_strat_ops/
├── src/          # 모든 코드 (All code: library + scripts)
├── test/         # 테스트 (Tests)
├── data/         # 모든 데이터 (All data: raw + processed + outputs)
├── docs/         # 핵심 문서 (Core documentation)
└── archive/      # 아카이브 (Archived files)
```

---

## 📊 상세 구조 (Detailed Structure)

### 1. src/ - 소스 코드
```
src/
├── cli.py                 # CLI 진입점
├── models.py              # 통계 모델 (run_h1, run_h2, run_h3, run_h4)
├── features.py            # 데이터 처리
├── vagueness_v2.py        # Vagueness scorer
├── data_io.py             # NetCDF I/O
├── config/                # 설정 파일
│   └── datasets.yaml      # outputs → data/outputs
└── scripts/               # 실행 스크립트
    ├── generate_paper_results_section.py
    ├── generate_paper_tables.py
    ├── convert_to_netcdf.py
    └── ...
```

### 2. test/ - 테스트
```
test/
├── conftest.py            # Shared fixtures
├── unit/
│   ├── test_models.py     # 53 tests
│   ├── test_features.py   # 25 tests
│   └── test_data_io.py    # 15 tests
└── integration/
    ├── test_paper_results.py
    └── test_data_quality.py  # 20 tests
```

### 3. data/ - 모든 데이터
```
data/
├── raw/                   # 원본 데이터
├── processed/             # 처리된 데이터
│   └── features_engineered.nc
└── outputs/               # 분석 결과 (from outputs/)
    ├── all/
    ├── quantum/
    └── transportation/
```

### 4. docs/ - 핵심 문서
```
docs/
├── PAPER_TESTING_GUIDE.md
├── PAPER_PIPELINE_GUIDE.md
├── PAPER_CODE_MAPPING.md
└── PAPER_INTEGRATION_STRATEGY.md
```

### 5. archive/ - 아카이브
```
archive/
├── old_docs/
├── experimental/
└── notebooks/
```

---

## 🔄 주요 변경사항 (7→5 Folders)

### 통합된 폴더
| 이전 | 새 위치 | 이유 |
|-----|--------|-----|
| `scripts/` | `src/scripts/` | 코드 통합 |
| `outputs/` | `data/outputs/` | 데이터 통합 |

### 함수명 변경 (Pytest 오류 해결)
| 이전 | 새 이름 |
|-----|--------|
| `test_h1_early_funding` | `run_h1_early_funding` |
| `test_h2_main_growth` | `run_h2_main_growth` |
| `test_h3_early_funding_interaction` | `run_h3_early_funding_interaction` |
| `test_h4_growth_interaction` | `run_h4_growth_interaction` |

---

## 🚀 빠른 명령어

```bash
# 전체 파이프라인
make all

# 단계별
make data              # 데이터 처리
make analysis          # 분석
make test              # 테스트 (93개)

# 정보
make info              # 상태 확인
```

---

**버전**: 3.0 (5-folder structure)  
**업데이트**: 2025-11-20
