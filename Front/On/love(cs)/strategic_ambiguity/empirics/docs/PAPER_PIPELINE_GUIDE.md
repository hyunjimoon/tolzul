---
modified:
  - 2025-11-22T05:47:44-05:00
---
# 논문 자동 생성 파이프라인 가이드
# Paper Auto-Generation Pipeline Guide

## 🎯 목표

**Input**: 데이터 + 가설
**Output**: 32개 단락 + 표 + 그림으로 구성된 완성된 논문 (PDF)

---

## 🏗️ 아키텍처

```
Raw Data (.dat files)
    ↓
[1] Data Processing (features.py)
    ↓ features_engineered.parquet
[2] Statistical Analysis (models.py)
    ↓ H1/H2 results
[3] Table Generation (scripts/generate_paper_tables.py)
    ↓ table1_h1.tex, table2_h2.tex
[4] Figure Generation (plotting.py)
    ↓ fig2_*.pdf, fig3_*.pdf
[5] Results Section (scripts/generate_paper_results_section.py)
    ↓ results_auto.tex (Module #23-27 완전 자동)
[6] LaTeX Compilation (pdflatex)
    ↓ main.pdf (최종 논문)
```

---

## 🚀 빠른 시작 (5분)

### **전체 파이프라인 한 번에 실행**

```bash
# 1. 전체 파이프라인 실행 (데이터 → 분석 → 논문)
make all

# 결과:
# - paper/output/main.pdf     ← 최종 논문
# - paper/tables/*.tex         ← 테이블 2개
# - paper/figures/*.pdf        ← 그림 2-3개
# - paper/results_auto.tex     ← 자동 생성된 Results 섹션
```

### **이미 데이터 있으면 빠르게**

```bash
# 데이터 처리 건너뛰고 분석만
make quick
```

---

## 📋 단계별 실행

### **Step 1: 데이터 처리** (Module #14-16)

```bash
make data

# 또는 직접:
python -m src.cli load-data
python -m src.cli engineer-features

# Output: data/processed/features_engineered.parquet
```

### **Step 2: 통계 분석** (Module #23-27)

```bash
make analysis

# 또는 직접:
python scripts/generate_paper_results_section.py \
    --data data/processed/features_engineered.parquet \
    --output paper/

# Output:
#   - paper/results_auto.tex       (완전 자동 Results 섹션)
#   - paper/results_values.json    (모든 통계 값)
```

### **Step 3: 테이블 생성**

```bash
make tables

# 또는 직접:
python scripts/generate_paper_tables.py \
    --data data/processed/features_engineered.parquet \
    --output paper/tables/

# Output:
#   - paper/tables/table1_h1.tex   (H1 regression table)
#   - paper/tables/table2_h2.tex   (H2 logit table)
```

### **Step 4: 그림 생성**

```bash
make figures

# 또는 직접:
python -m src.cli generate-plots --dataset all --output paper/figures/

# Output:
#   - paper/figures/fig2_early_funding.pdf
#   - paper/figures/fig3_later_success.pdf
```

### **Step 5: 논문 컴파일**

```bash
make paper

# 또는 직접:
cd paper/output
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex

# Output: paper/output/main.pdf
```

---

## 📐 자동화 레벨

### **Tier 1: 완전 자동 (Results 섹션)**

**Module #23-27**: Results 섹션은 **100% 자동 생성**됩니다.

```latex
% paper/main.tex에 추가
\input{paper/results_auto.tex}  % 완전 자동!
```

**포함 내용:**
- Paragraph 23: H1 결과 해석 (계수, p-value 자동 삽입)
- Paragraph 24: H2 결과 해석 (main effect + interaction)
- Table 1: H1 regression table (LaTeX)
- Table 2: H2 logit table (LaTeX)
- Figure 2-3: 참조 경로 자동 생성

**장점:**
- 데이터 바뀌면 → `make analysis` → Results 섹션 자동 업데이트
- 계수 틀릴 일 없음 (코드에서 직접 추출)
- p-value에 따라 텍스트 자동 변경 ("significant" vs "not significant")

### **Tier 2: 반자동 (Methodology 섹션)**

**Module #14-22**: 데이터 통계를 자동으로 채움

```latex
% paper/templates/methodology.tex.j2
\subsection{Sample Construction}
Our final sample comprises \VAR{descriptive.n_total} ventures,
with \VAR{descriptive.n_software} (\VAR{descriptive.pct_software}\%)
software ventures and \VAR{descriptive.n_hardware} hardware ventures.

The average vagueness score is \VAR{descriptive.vagueness_mean}
(SD = \VAR{descriptive.vagueness_std}).
```

**사용법:**
```bash
python scripts/generate_paper_full.py
# → paper/output/methodology.tex (자동 값 삽입)
```

### **Tier 3: 수동 (나머지)**

**Module #1-13, #28-32**: 수동 작성 필요

- Introduction (#1-7): 스토리텔링 필요
- Literature (#8-10): 문헌 정리 필요
- Theory (#11-13): 이론 전개 필요
- Discussion (#28-32): 해석 및 함의 필요

**하지만** 수치는 자동으로 참조 가능:

```latex
% paper/main.tex
% Introduction에서 Results 값 참조
Our analysis of \input{paper/results_values.json} companies reveals...
```

---

## 🔄 일반적인 워크플로우

### **논문 작성 중**

```bash
# 1. 데이터 업데이트되면
make data

# 2. Results 섹션 재생성
make results-only

# 3. 논문 확인
open paper/output/main.pdf
```

### **논문 제출 전**

```bash
# 1. 전체 파이프라인 실행 (처음부터)
make clean-all
make all

# 2. 테스트 실행 (논문 값 검증)
make test

# 3. 최종 확인
make validate
```

### **리뷰 피드백 후**

```bash
# 1. 코드 수정 (예: H1 formula 변경)
vi src/models.py

# 2. Results 재생성 (데이터는 그대로)
make quick

# 3. 테스트로 검증
make test

# 4. 모두 통과하면 commit
git add . && git commit -m "Update H1 specification"
```

---

## 📊 파일 구조

```
empirics_ent_strat_ops/
├── data/
│   ├── raw/*.dat                      # 원본 데이터
│   └── processed/
│       └── features_engineered.parquet  # 처리된 데이터
├── src/
│   ├── models.py                      # H1/H2 함수
│   ├── features.py                    # 데이터 처리
│   └── plotting.py                    # 그림 생성
├── scripts/
│   ├── generate_paper_results_section.py  # Results 자동 생성
│   ├── generate_paper_tables.py           # 테이블 생성
│   └── generate_paper_full.py             # 전체 논문 생성
├── paper/
│   ├── main.tex                       # 메인 논문 파일 (수동 작성)
│   ├── results_auto.tex               # 자동 생성된 Results ✓
│   ├── results_values.json            # 모든 통계 값
│   ├── tables/
│   │   ├── table1_h1.tex              # 자동 생성 ✓
│   │   └── table2_h2.tex              # 자동 생성 ✓
│   ├── figures/
│   │   ├── fig2_early_funding.pdf     # 자동 생성 ✓
│   │   └── fig3_later_success.pdf     # 자동 생성 ✓
│   ├── templates/                     # Jinja2 템플릿 (선택)
│   │   ├── main.tex.j2
│   │   └── results.tex.j2
│   └── output/
│       └── main.pdf                   # 최종 논문 PDF ✓
├── test/
│   └── integration/
│       └── test_paper_results.py      # 논문 값 검증
├── Makefile                           # 파이프라인 자동화
└── README.md
```

---

## 🎨 main.tex 구조 예시

```latex
\documentclass{article}

\begin{document}

% ============================================
% Tier 3: 수동 작성
% ============================================
\section{Introduction}
% Paragraph 1-7: 직접 작성
In 2008, Tesla Motors approached investors...

\section{Literature Review}
% Paragraph 8-10: 직접 작성
The information economics tradition...

\section{Theory}
% Paragraph 11-13: 직접 작성
Information and Real option value...

% ============================================
% Tier 2: 반자동 (템플릿 + 값)
% ============================================
\section{Empirical Methodology}
% Paragraph 14-22: 템플릿 사용 (선택)
% \input{paper/methodology_auto.tex}

% 또는 수동 + 값 참조
Our final sample comprises \VAR{n_total} ventures...

% ============================================
% Tier 1: 완전 자동 ✓
% ============================================
\section{Results}
\input{paper/results_auto.tex}  % Module #23-27 완전 자동!

% ============================================
% Tier 3: 수동 작성
% ============================================
\section{Discussion}
% Paragraph 28-32: 직접 작성
Our findings reconcile...

\bibliographystyle{plainnat}
\bibliography{references}

\end{document}
```

---

## ⚙️ 고급 기능

### **자동 재빌드 (파일 변경 감지)**

```bash
# 파일 변경 시 자동으로 논문 재컴파일
make watch

# 또는 (entr 필요):
ls paper/*.tex paper/tables/*.tex | entr make paper
```

### **CI/CD 통합**

```yaml
# .github/workflows/paper.yml
name: Build Paper

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: make all
      - uses: actions/upload-artifact@v3
        with:
          name: paper
          path: paper/output/main.pdf
```

### **버전 관리**

```bash
# 논문 버전별로 스냅샷 저장
make all
cp paper/output/main.pdf paper/versions/draft_v1_$(date +%Y%m%d).pdf

# Git에 commit (PDF 제외)
git add paper/results_auto.tex paper/tables/*.tex
git commit -m "Update Results section - H2 interaction now significant"
```

---

## 📈 성과 지표

### **수동 작업 절감**

**Before (수동)**:
- Results 섹션 작성: 2-3시간
- Table 1-2 LaTeX 작성: 1-2시간
- 계수 틀릴 확률: 높음
- 데이터 바뀌면: 처음부터 다시

**After (자동)**:
- Results 섹션: 2분 (`make analysis`)
- Tables: 1분 (`make tables`)
- 계수 오류: 0%
- 데이터 바뀌면: `make quick` → 3분

### **재현성 보장**

```bash
# 리뷰어가 재현 요청하면:
git clone https://github.com/user/paper.git
cd paper
make all

# 5분 후 → 똑같은 논문 PDF 생성 ✓
```

---

## ❓ FAQ

**Q: 모든 32개 단락을 자동 생성할 수 있나요?**
A: 아니요. **Results (Module #23-27)만 100% 자동**입니다.
   Introduction/Discussion은 수동 작성 필요 (스토리텔링/해석).

**Q: 데이터가 바뀌면 어떻게 하나요?**
A:
```bash
make data      # 데이터 재처리
make quick     # 분석+논문 재생성
```
3-5분이면 완료.

**Q: 논문 템플릿을 어떻게 만드나요?**
A: 기존 LaTeX 논문에서 숫자 부분만 `\VAR{변수명}`으로 교체.
   예: `450 ventures` → `\VAR{n_total} ventures`

**Q: Figure는 어떻게 자동화하나요?**
A: `src/plotting.py`에 그림 생성 함수 추가:
```python
def generate_figure2(df):
    # ... plotting code
    plt.savefig('paper/figures/fig2.pdf')
```

**Q: CI/CD에서 논문 자동 빌드할 수 있나요?**
A: 네! GitHub Actions에서 `make all` 실행 → PDF 자동 생성.

---

## 🎓 Best Practices

### **1. Results는 완전 자동, 나머지는 수동**

```latex
% 좋은 예:
\section{Results}
\input{paper/results_auto.tex}  % 자동 ✓

\section{Discussion}
% 직접 작성 (자동화 시도 X)
```

### **2. 중요한 값만 JSON으로 참조**

```latex
% main.tex에서
Our analysis of {{ n_total }} companies reveals
that vagueness reduces early funding by {{ h1_coef_abs }}%.

% 나머지 텍스트는 수동 작성
```

### **3. 버전 관리는 소스만, PDF는 제외**

```bash
# .gitignore
paper/output/*.pdf
paper/output/*.aux
```

### **4. 테스트로 논문 값 검증**

```bash
# 논문 제출 전 항상
make test
make validate
```

---

## 🚀 Next Steps

1. **지금 바로 시도**:
   ```bash
   make all
   ```

2. **Results 섹션 확인**:
   ```bash
   cat paper/results_auto.tex
   ```

3. **논문에 통합**:
   ```latex
   % paper/main.tex에 추가
   \input{paper/results_auto.tex}
   ```

4. **컴파일 & 확인**:
   ```bash
   make paper
   open paper/output/main.pdf
   ```

---

**문의**: 이 가이드는 `docs/PAPER_INTEGRATION_STRATEGY.md`와 함께 읽어주세요.
