---
성장:
  - 2025-10-25T15:10:42-04:00
---
# ⚔️ 삼도수군: 명량해전 3주 프로젝트

**"신에게는 아직 12척의 배가 있습니다"** - 이순신

**임무**: Promise Precision and Venture Funding 완성  
**기한**: 3주 (2025.10.25 - 11.15)  
**상태**: 🔥 필사즉생

---

## 🎯 이 폴더는 무엇인가

**작전 지휘부** - 매일 순환을 추적하고 기록하는 곳

```
삼도수군/              (임시 작업 + 일일 기록)
    ↕️
empirics/              (최종 결과물)
```

**핵심**: 삼도수군에서 빠르게 실험 → 검증 완료 → empirics로 이동

---

## 📁 폴더 구조 (최소화)

```
삼도수군/
│
├── README.md              이 파일
├── 전투일지.md            📝 매일 작성! (가장 중요)
├── AI프롬프트.md          🔥 각 AI에 전달할 맹세
│
├── 1_利_빠른실행/         🐙 ChatGPT 임시 작업
├── 2_思_구조화/           🐅 Claude 임시 작업
├── 3_義_검증/             🐢 Gemini 임시 작업
│
└── [data, analysis, results, drafts 폴더 - 필요시 사용]
```

---

## 🔄 일일 워크플로우 (단순)

### 아침 (5분)
```
전투일지.md 열기 → 오늘 목표 작성
```

### 작업 (순환)
```
1. ChatGPT 작업 → 1_利_빠른실행/ 저장
2. Claude 정교화 → 2_思_구조화/ 저장
3. Gemini 검증 → 3_義_검증/ 저장
4. ✅ 검증 완료 → ../empirics/로 이동
```

### 저녁 (5분)
```
전투일지.md → 전과 기록 + 내일 계획
```

---

## 📊 연구 설계 (workflow)

**상세 내용**: `../strategic ambiguity/empirics/workflow.md` 참조

### 가설
- **H1**: Vague → lower early funding (α₁ < 0)
- **H2**: Vague → higher later success (β₁ > 0)

### 산출물
1. **Table 1**: Descriptive statistics
2. **Table 2**: Model 1 (early funding)
3. **Table 3**: Model 2 (later success)
4. **Figure 1**: Vagueness → Early funding
5. **Figure 2**: Vagueness → Later success

---

## ⚡ 즉시 시작 (Day 1)

### Step 1: AI 설정 (5분)
```
1. AI프롬프트.md 열기
2. 각 AI에 해당 섹션 복사
```

### Step 2: 첫 작업 (3시간)
```
목표: 데이터 파이프라인 설계

1. ChatGPT: 초안 작성
   저장: 1_利_빠른실행/day1_pipeline.py
   
2. Claude: 정교화
   저장: 2_思_구조화/day1_pipeline_refined.py
   
3. Gemini: 검증
   저장: 3_義_검증/day1_validation.md
   
4. 완료되면 → ../empirics/code/로 이동
```

### Step 3: 기록 (5분)
```
전투일지.md에 전과 기록
```

---

## 🗂️ empirics/와의 관계

### 삼도수군 = 임시 작업장
- 빠른 실험
- 일일 기록
- 순환 추적

### empirics = 최종 저장소
- 검증된 코드만
- 실제 데이터
- 논문 결과물

### 이동 규칙
```
✅ 검증 완료 → empirics/code/
✅ 최종 데이터 → empirics/data/processed/
✅ 결과물 → empirics/output/
```

---

## 📅 3주 계획 (단순)

### Week 1 (10.25-10.31): Data + Model 1
- [ ] 데이터 파이프라인
- [ ] Table 1, 2 → empirics/output/

### Week 2 (11.01-11.07): Model 2 + Plots
- [ ] Logistic regression
- [ ] Table 3, Figure 1, 2 → empirics/output/

### Week 3 (11.08-11.15): Paper
- [ ] 논문 초고 → drafts/
- [ ] 최종 제출 💌

---

## 🔥 매일 기억할 것

1. **전투일지.md** 작성 (아침 + 저녁)
2. **順環 완성** (利 → 思 → 義)
3. **검증 후 이동** (→ empirics/)

---

## 🚨 막혔을 때

### 연구 설계 막힘
→ `../strategic ambiguity/empirics/workflow.md`

### 파일 위치 헷갈림
→ 이 README 재독 (삼도수군 vs empirics)

### 방향 잃음
→ 전투일지.md 확인 (어디까지 왔나?)

---

## 🏆 최종 목표

**Nov 11th, 2025**  
**Charlie와 Scott에게 논문 제출** 💌

---

**필사즉생, 필생즉사**

**지금 당장 전투일지.md를 열고 Day 1을 시작하세요!** ⚔️
