# 📊 One-Touch Analysis & Report Pipeline

완전 자동화된 분석 및 보고서 생성 파이프라인입니다.

## 🚀 빠른 시작

### 원터치 실행

```bash
cd "Front/On/love(cs)/strategic ambiguity/empirics"
./run_full_pipeline.sh
```

이 명령 하나로 다음 모든 작업이 자동으로 실행됩니다:

1. ✅ **데이터 구축**: Company*.dat 파일들로부터 분석용 데이터셋 생성
2. ✅ **통계 분석**: H1, H2, H3, H4 모델 fitting 및 결과 저장
3. ✅ **시각화 생성**: Figure 1, Figure 2a/2b, interaction plots 등
4. ✅ **보고서 렌더링**: 3개 Quarto 보고서 → HTML/PDF 변환
5. ✅ **품질 평가**: Charles Fine & Scott Stern 관점에서 자동 평가

## 📋 사전 요구사항

### 필수

- **Python 3.8+** with packages:
  - pandas
  - numpy
  - matplotlib
  - statsmodels
  - scipy

- **데이터 파일** (다음 중 한 곳에 위치):
  - `/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/Front/On/love(cs)/strategic ambiguity/empirics/data/raw/`
  - `./data/raw/` (상대 경로)

  필요한 파일:
  - `Company20211201.dat`
  - `Company20220101.dat`
  - `Company20220501.dat`
  - `Company20230501.dat`

### 선택 (보고서 렌더링용)

- **Quarto**: https://quarto.org/docs/get-started/
- **LaTeX** (PDF 생성용, 선택사항): https://www.latex-project.org/get/

Quarto 없이도 스크립트는 실행되며, .qmd 파일들은 생성됩니다.

## 📁 출력 파일 구조

```
outputs/
├── h1_coefficients.csv                    # H1 회귀 계수
├── h2_model_architecture.csv              # H2 (architecture) 계수
├── h2_model_architecture_metrics.csv      # H2 (architecture) 모델 적합도
├── h2_model_founder.csv                   # H2 (founder) 계수
├── h2_model_founder_metrics.csv           # H2 (founder) 모델 적합도
├── h3_coefficients.csv                    # H3 interaction 계수
├── h4_coefficients.csv                    # H4 interaction 계수
│
├── figures/
│   ├── Figure_1_Reversal.png              # H1 vs H2 reversal pattern
│   ├── Figure_2a_H3.png                   # H3 interaction plot
│   └── Figure_2b_H4.png                   # H4 interaction plot
│
├── bakeoff/
│   ├── univariate_distributions.png        # 변수 분포
│   ├── moderator_overlap_is_hardware.png   # Hardware 겹침 분석
│   ├── moderator_overlap_is_serial.png     # Serial 겹침 분석
│   ├── h2_interaction_is_hardware.png      # Hardware interaction
│   └── h2_interaction_is_serial.png        # Serial interaction
│
└── reports/                                # Quarto 렌더링 결과
    ├── moderator_bakeoff_lean.html
    ├── moderator_bakeoff_lean.pdf
    ├── Progress_Report_W1_is_serial.html
    ├── Progress_Report_W1_is_serial.pdf
    ├── Progress_Report_W1_is_hardware.html
    └── Progress_Report_W1_is_hardware.pdf
```

## 📊 생성되는 보고서

### 1. `moderator_bakeoff_lean.qmd` → `.html/.pdf`

**목적**: 두 가지 moderator (Architecture vs. Founder Credibility) 비교

**내용**:
- H1 context (reversal pattern)
- Architecture (is_hardware) 분석
- Founder Credibility (is_serial) 분석
- Side-by-side 비교 테이블
- 교수님들께 드리는 핵심 질문
- 의사결정 프레임워크

**핵심 발견**: is_hardware가 더 강한 interaction pattern 보임 (slope 차이 명확)

### 2. `Progress_Report_W1_is_serial.qmd` → `.html/.pdf`

**목적**: Founder Credibility (is_serial) moderator 중심 진행 보고서

**내용**:
- Executive Summary
- 이론적 배경 (reputation-based trust mechanisms)
- Data & Measurement
- DV Validation (Scott Stern's A(t₀) → B+(t₁) framework)
- H1, H2 (founder), H3, H4 전체 결과
- 동적으로 로드된 통계 결과 및 해석
- Figures 임베드
- References (APA format)

### 3. `Progress_Report_W1_is_hardware.qmd` → `.html/.pdf`

**목적**: Architecture (is_hardware) moderator 중심 진행 보고서

**내용**:
- Executive Summary
- Integration cost 이론적 framework (Baldwin & Clark, 2000)
- Data & Measurement
- DV Validation
- H1, H2 (architecture) 전체 결과
- H3/H4 (architecture) 개념적 정의
- Modularity theory 적용
- References

## 🧾 품질 평가 체크리스트

스크립트가 자동으로 다음 기준으로 보고서를 평가합니다:

### 1. 가독성 (Readability)
- ✅ 문장 명확성 & 용어 일관성
- ✅ 논리 흐름 & 시각자료 설명
- ✅ 독자 친화성

### 2. 자족성 (Self-contained)
- ✅ 배경 없이도 이해 가능
- ✅ 모든 표·그림 포함 & 해설
- ✅ 결과 의미 & 시사점 명확

### 평가 관점

**Charles Fine (Operations/Architecture)**:
- Integration cost theory 적용
- Practical relevance
- Empirical rigor

**Scott Stern (Entrepreneurship/Strategy)**:
- Methodological soundness
- Strategic insights
- Causal inference
- Policy implications

## 🔧 트러블슈팅

### 데이터 파일을 찾을 수 없습니다

```bash
✗ Data directory not found
```

**해결**: 데이터 파일 경로를 확인하세요:
- Mac 로컬: `/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/.../data/raw/`
- Docker: `./data/raw/`

### Quarto를 찾을 수 없습니다

```bash
⚠ Quarto not found - reports will not be rendered
```

**해결**: Quarto 설치 (선택사항)
```bash
# macOS
brew install quarto

# 또는 https://quarto.org/docs/get-started/ 에서 다운로드
```

Quarto 없이도 .qmd 파일들은 생성됩니다. 나중에 수동으로 렌더링 가능:
```bash
quarto render moderator_bakeoff_lean.qmd
```

### Python 패키지 오류

```bash
ModuleNotFoundError: No module named 'pandas'
```

**해결**:
```bash
pip install pandas numpy matplotlib statsmodels scipy
```

스크립트가 자동으로 설치를 시도하지만, 실패 시 수동 설치 필요합니다.

### LaTeX 오류 (PDF 생성)

```bash
⚠ PDF rendering skipped (LaTeX may not be installed)
```

**해결**: LaTeX 설치 (선택사항)
```bash
# macOS
brew install --cask mactex-no-gui

# 또는 TinyTeX (Quarto 추천)
quarto install tinytex
```

HTML 렌더링은 LaTeX 없이도 작동합니다.

## 📝 수동 실행 (단계별)

자동 스크립트 대신 수동으로 실행하려면:

```bash
# 1. 분석 실행
python run_analysis.py

# 2. 보고서 렌더링
quarto render moderator_bakeoff_lean.qmd
quarto render Progress_Report_W1_is_serial.qmd
quarto render Progress_Report_W1_is_hardware.qmd

# 3. 평가 (스크립트에서 자동 생성된 Python 스크립트 사용)
# /tmp/evaluate_reports.py 참조
```

## 🎯 다음 단계

1. **보고서 검토**:
   ```bash
   open outputs/reports/moderator_bakeoff_lean.html
   ```

2. **평가 결과 확인**: 스크립트 출력에서 점수 확인

3. **교수님들께 공유**:
   - PDF 또는 HTML 파일 전달
   - 핵심 질문 (moderator_bakeoff_lean.qmd) 강조

4. **피드백 반영**:
   - 필요 시 코드 수정 (`modules/*.py`)
   - 다시 `./run_full_pipeline.sh` 실행

## 📞 문의

문제가 발생하면:
1. 터미널 출력의 에러 메시지 확인
2. 이 README의 트러블슈팅 섹션 참조
3. 필요 시 개발자에게 문의

---

**마지막 업데이트**: 2025-10-29
**버전**: 1.0
