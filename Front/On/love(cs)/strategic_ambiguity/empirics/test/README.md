# test/ - 테스트 (Tests)

## 📝 용도 (Purpose)
**모든 Pytest 테스트**: 단위 테스트 + 통합 테스트

## 📂 구조 (Structure)

### 파일
- `conftest.py` - 공유 fixtures (pytest)

### unit/ - 단위 테스트
개별 함수/모듈 테스트
- `test_models.py` - 53 tests (H1/H2/H3/H4)
- `test_features.py` - 25 tests (vagueness scorer)
- `test_data_io.py` - 15 tests (NetCDF I/O)

### integration/ - 통합 테스트
전체 파이프라인 테스트
- `test_paper_results.py` - 논문 결과 검증
- `test_data_quality.py` - 20 tests (데이터 품질)

## 🚀 사용법
```bash
# 전체 테스트
pytest test/

# 특정 테스트
pytest test/unit/test_models.py -v
```

## ✅ 총 테스트 수
93 tests (unit: 93, integration: varies)
