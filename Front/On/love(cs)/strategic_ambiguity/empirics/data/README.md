# data/ - 데이터 (Data)

## 📝 용도 (Purpose)
**모든 데이터 파일**: 원본 + 처리됨 + 분석 결과

## 📂 구조 (Structure)

### raw/ - 원본 데이터
- 절대 수정 금지!
- .dat 파일들
- Crunchbase 원본 데이터

### processed/ - 처리된 데이터
- `features_engineered.nc` - 특징 엔지니어링 완료 데이터
- NetCDF 형식 (.nc)

### outputs/ - 분석 결과
- `all/` - 전체 데이터셋 결과
- `quantum/` - Quantum 데이터셋
- `transportation/` - Transportation 데이터셋
- `hardware/` - Hardware 데이터셋
- `software/` - Software 데이터셋
- `medtech/` - MedTech 데이터셋
- `pharma/` - Pharmaceutical 데이터셋

각 폴더 구조:
```
outputs/dataset_name/
├── models/          # 회귀 결과 (.csv)
├── figures/         # 그림 (.pdf, .png)
└── dataset.nc       # 필터링된 데이터
```

## ⚠️ 중요
- raw/는 읽기 전용
- processed/는 재생성 가능
- outputs/는 자동 생성
