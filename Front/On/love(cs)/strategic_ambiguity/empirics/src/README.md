# src/ - 소스 코드 (Source Code)

## 📝 용도 (Purpose)
**모든 Python 코드**: 라이브러리 모듈 + 실행 스크립트

## 📂 구조 (Structure)

### 핵심 모듈 (Core Modules)
- `cli.py` - CLI 진입점
- `models.py` - 통계 모델 (run_h1, run_h2, run_h3, run_h4)
- `features.py` - 데이터 처리 및 필터링
- `vagueness_v2.py` - Vagueness 점수 계산
- `data_io.py` - NetCDF I/O

### 하위 폴더
- `config/` - YAML 설정 (datasets.yaml)
- `scripts/` - 실행 스크립트 (paper 생성, 변환 등)

## 🚀 사용법
```bash
# CLI 실행
python -m src.cli load-data

# 스크립트 실행
python src/scripts/generate_paper_tables.py
```
