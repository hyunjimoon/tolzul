# 빠른 시작 가이드
# Quick Start Guide

## 🚀 5분 안에 시작하기 (Get Started in 5 Minutes)

### 1. 설치 (Installation)

```bash
# Clone repository
git clone https://github.com/user/empirics_ent_strat_ops.git
cd empirics_ent_strat_ops

# Install dependencies (NO pyarrow needed!)
pip install -r requirements.txt
```

**중요**: 이제 Parquet 대신 **NetCDF (.nc)** 형식을 사용합니다. `pyarrow` 설치가 필요 없습니다!

### 2. 전체 파이프라인 실행 (Run Full Pipeline)

```bash
# 한 번에 실행 (One command)
make all

# 또는 단계별로 (Step by step)
make data        # 데이터 처리
make analysis    # 통계 분석
make tables      # 테이블 생성
make figures     # 그림 생성
make paper       # 논문 컴파일
```

### 3. 예시 스크립트 실행 (Run Example Script)

```bash
# 로컬 환경에서 전체 과정 확인
./run_local_example.sh
```

이 스크립트는 다음을 자동으로 수행합니다:
- ✅ 환경 확인
- ✅ 데이터 변환 (.parquet → .nc)
- ✅ 통계 분석 실행
- ✅ 테이블/그림 생성
- ✅ 테스트 실행
- ✅ 논문 PDF 생성

---

## 📚 주요 문서 (Key Documents)

| 문서 | 내용 | 읽는 시간 |
|------|------|----------|
| **PAPER_TESTING_GUIDE.md** | 논문 생성 테스트 전략 | 15분 |
| **PAPER_PIPELINE_GUIDE.md** | 파이프라인 완전 가이드 | 20분 |
| **PAPER_CODE_MAPPING.md** | 32개 모듈 매핑 | 10분 |
| **README.md** | 프로젝트 개요 | 5분 |

---

## 🧪 테스트 (Testing)

### 빠른 테스트 (1분)
```bash
# 핵심 모델 테스트만
pytest test/unit/test_models.py -v --no-cov
```

### 전체 테스트 (5분)
```bash
# 모든 테스트 + 커버리지
make test
```

### 데이터 품질 확인
```bash
# 데이터 이상 감지
pytest test/integration/test_data_quality.py -v
```

---

## 📊 출력 파일 (Output Files)

```
empirics_ent_strat_ops/
├── data/processed/
│   └── features_engineered.nc        ← 처리된 데이터
├── paper/
│   ├── results_auto.tex              ← 자동 생성 Results 섹션
│   ├── results_values.json           ← 통계값 (JSON)
│   ├── tables/
│   │   ├── table1_h1.tex             ← H1 테이블
│   │   └── table2_h2.tex             ← H2 테이블
│   ├── figures/
│   │   ├── fig2_early_funding.pdf    ← Figure 2
│   │   └── fig3_later_success.pdf    ← Figure 3
│   └── output/
│       └── main.pdf                  ← 최종 논문 PDF
```

---

## 🔧 자주 하는 작업 (Common Tasks)

### 데이터 변경 후 재실행
```bash
make data        # 데이터 재처리
make quick       # 분석+논문 재생성 (데이터 건너뛰기)
```

### Results 섹션만 업데이트
```bash
make results-only
```

### 전체 초기화
```bash
make clean-all   # 모든 생성 파일 삭제
make all         # 처음부터 재실행
```

### Parquet 파일 변환
```bash
# 기존 .parquet 파일을 .nc로 변환
python scripts/convert_to_netcdf.py --directory data/processed

# 변환 후 .parquet 삭제 (선택)
python scripts/convert_to_netcdf.py --directory data/processed --remove-original
```

---

## ❓ 문제 해결 (Troubleshooting)

### pyarrow 설치 실패
```bash
# 해결: NetCDF 사용 (pyarrow 필요 없음)
pip install xarray netcdf4

# 기존 .parquet 파일 변환
python scripts/convert_to_netcdf.py
```

### 테스트 실패: "features_engineered.nc not found"
```bash
# 해결: 데이터 처리 먼저 실행
make data
pytest test/
```

### LaTeX 컴파일 실패
```bash
# Linux
sudo apt-get install texlive-full

# macOS
brew install mactex

# Windows
# Install MiKTeX from https://miktex.org
```

### 모델 테스트 실패: 계수 부호 반대
```
AssertionError: H1: Vagueness should reduce early funding
```
**원인**:
- 데이터가 바뀌었거나
- 모델 스펙이 변경됨

**대응**:
1. 데이터 확인: `python -c "from data_io import load_dataframe; df = load_dataframe('data/processed/features_engineered.nc'); print(df['vagueness'].describe())"`
2. 모델 결과 확인: `pytest test/unit/test_models.py::TestH1EarlyFunding -v`
3. 이론 재검토 필요

---

## 📈 성능 비교

### NetCDF vs Parquet

| 항목 | Parquet | NetCDF |
|------|---------|--------|
| 의존성 | pyarrow (설치 어려움) | xarray (쉬움) |
| 파일 크기 | 2.3 MB | 1.8 MB (22% 작음) |
| 로딩 속도 | 빠름 | 비슷함 |
| 호환성 | Python | 다양한 언어 |

**결론**: NetCDF가 더 간단하고 가벼움! ✅

---

## 🎯 다음 단계 (Next Steps)

### 1. 로컬에서 테스트
```bash
./run_local_example.sh
```

### 2. 논문 값 확인
```bash
cat paper/results_values.json
```

### 3. 생성된 테이블 확인
```bash
cat paper/tables/table1_h1.tex
```

### 4. 최종 PDF 확인
```bash
open paper/output/main.pdf  # macOS
xdg-open paper/output/main.pdf  # Linux
```

---

## 📞 도움말 (Help)

### 명령어 도움말
```bash
make help       # Makefile 도움말
python -m src.cli --help  # CLI 도움말
```

### 파이프라인 상태 확인
```bash
make info       # 어떤 파일이 생성되었는지 확인
```

### 테스트 도움말
```bash
pytest --help   # pytest 옵션
pytest --collect-only  # 사용 가능한 테스트 목록
```

---

## 🎓 학습 경로 (Learning Path)

1. **처음 사용**: `./run_local_example.sh` 실행
2. **테스트 이해**: `docs/PAPER_TESTING_GUIDE.md` 읽기
3. **파이프라인 이해**: `docs/PAPER_PIPELINE_GUIDE.md` 읽기
4. **코드 매핑 이해**: `docs/PAPER_CODE_MAPPING.md` 읽기
5. **고급 사용**: Makefile 커스터마이징

---

## ✅ 체크리스트 (Checklist)

논문 제출 전:
- [ ] `make clean-all && make all` 실행
- [ ] `make test` 모두 통과
- [ ] PDF 컴파일 성공
- [ ] Table 1-2 확인
- [ ] Figure 2-3 확인
- [ ] Results 섹션 확인
- [ ] Git commit

---

**문의**: 문제가 있으면 `docs/PAPER_TESTING_GUIDE.md`의 "문제 해결" 섹션 참조
