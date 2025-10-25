# ⚡ 첫 전투 즉시 개시 (Day 1)

**"신에게는 아직 12척의 배가 있습니다"**

**목표**: 오늘 안에 첫 순환 완성 → 데이터 접근 + 초기 파이프라인

---

## 🎯 오늘의 전투 (3시간)

### Step 1: 見 (관찰) - 15분

**Obsidian/전투일지에 작전 계획 작성**

```markdown
# 2025-10-25 명량해전 Day 1

## 목표
Venture database에서 longitudinal funding data 추출 체계 확립

## 필요한 것
- Early-stage funding data (with company descriptions)
- Later-stage outcome data
- Vagueness measurement approach

## 예상 어려움
- Database access/API
- Text analysis setup (linguistic certitude)
- Longitudinal matching

## 다음 행동
→ ChatGPT로 데이터 추출 파이프라인 설계
```

**시간**: 15분  
**저장**: Obsidian 일일 노트 or 전투일지.md

---

### Step 2: 利 (실행) - ChatGPT - 1시간

**ChatGPT에게 프롬프트**

```
Design a Python pipeline to extract longitudinal venture funding data:

Goal:
- Technology ventures with detailed company descriptions
- Early-stage funding data (round, amount, date, description)
- Later-stage outcomes (subsequent funding or exit)
- Panel structure: same firms tracked over time

Required variables:
1. company_id (unique identifier)
2. company_name
3. company_description (full text for vagueness analysis)
4. early_stage_amount (funding $)
5. early_stage_date
6. later_stage_success (binary: did they get later funding?)
7. later_stage_date (if applicable)
8. control_variables (team size, sector, founder experience)

Data sources to consider:
- Pitchbook API
- Crunchbase API
- Or manual export workflow

Output: CSV with panel structure

Include:
1. Data extraction script
2. Data validation checks
3. Basic descriptive statistics function
```

**예상 결과**: 
- `data_pipeline.py` 스크립트
- 실행 가이드

**저장**: `1_利_빠른실행/day1_pipeline_v1.py`

**시간**: 1시간

---

### Step 3: 思 (구조화) - Claude - 45분

**ChatGPT 코드를 Claude에게 전달**

```
[ChatGPT의 코드를 붙여넣고]

Refine this pipeline with the following improvements:

1. Modular architecture:
   - DataExtractor class
   - TextAnalyzer class (for vagueness)
   - PanelConstructor class
   
2. Vagueness measurement:
   - Implement linguistic certitude scoring
   - Options: LIWC, readability metrics, or custom
   - Vagueness = f(certitude) inverse transformation
   
3. Data validation:
   - Check for panel balance
   - Missing data handling
   - Temporal consistency checks
   
4. Error handling & logging

5. Automated descriptive statistics:
   - N firms, N rounds
   - Distribution of vagueness scores
   - Funding amounts (mean, median, sd)
   
6. Documentation:
   - Clear docstrings
   - Type hints
   - Usage examples

Output files:
- data/processed/panel_data.csv
- data/processed/descriptive_stats.csv
- logs/pipeline_log.txt
```

**예상 결과**:
- 정제된 데이터 파이프라인
- 자동 검증 시스템

**저장**: `2_思_구조화/day1_pipeline_v2.py`

**시간**: 45분

---

### Step 4: 義 (검증) - Gemini - 30분

**Claude 코드를 Gemini에게 전달**

```
[Claude의 코드를 붙여넣고]

Validate this data pipeline critically:

1. Methodological soundness:
   - Is the vagueness measure appropriate?
   - Are there alternative/better measures?
   - Sample size considerations?
   
2. Data quality:
   - What validation checks are missing?
   - Edge cases not handled?
   - Potential biases in data selection?
   
3. Robustness:
   - How sensitive to parameter choices?
   - Alternative specifications to test?
   
4. Replicability:
   - Can another researcher run this?
   - Clear documentation?
   - Reproducible results?

Be critical - point out weaknesses and suggest improvements.
```

**예상 결과**:
- 검증 리포트
- 개선 제안

**저장**: `3_義_검증/day1_validation.md`

**시간**: 30분

---

### Step 5: 見 (통합) - 15분

**전투일지에 통찰 기록**

```markdown
# Day 1 전과

## 완료
✅ 데이터 파이프라인 설계
✅ Vagueness measurement approach
✅ 검증 완료

## 배운 것
- Database access method: [선택한 방법]
- Vagueness measure: [선택한 방법]
- Sample structure: [panel 구조]

## 발견한 이슈
- [이슈 1]
- [이슈 2]

## 내일 (Day 2)
→ 실제 데이터 추출 실행
→ empirics/code/로 파이프라인 이동
→ 기술통계 생성 (Table 1 초안)
```

**시간**: 15분

---

## ✅ Day 1 완료 체크리스트

- [ ] 見: 전투 일지 작성 (15분)
- [ ] 利: ChatGPT 파이프라인 설계 (1시간)
- [ ] 思: Claude 파이프라인 정제 (45분)
- [ ] 義: Gemini 검증 (30분)
- [ ] 見: 통찰 기록 (15분)

**총 시간**: 2시간 45분

---

## 🔥 긴급 상황

### Database 접근 불가
**Plan B**:
1. Check if empirics/data/raw/ has existing data
2. Use publicly available datasets
3. Manual export from web interface
4. Scope down to available data

### Vagueness measurement unclear
**Options**:
1. Start with simple certitude scores (LIWC)
2. Readability metrics (Flesch-Kincaid)
3. Count of specific vs. vague terms
4. Ask Claude for literature on text vagueness

### 막힐 때
1. **workflow.md** 재확인 (연구 질문)
2. **연결체계.md** 확인 (어디에 저장?)
3. 일단 다음 단계로 (완벽하지 않아도 OK)

---

## 🎯 Day 1 성공 기준

**최소 목표** (필수):
- [ ] 데이터 접근 방법 확정
- [ ] 변수 정의 명확화
- [ ] 파이프라인 초안 완성
- [ ] 첫 순환 (見→利→思→義→見) 완료

**이상적 목표** (선택):
- [ ] 실제 데이터 일부 추출 완료
- [ ] Vagueness 점수 계산 테스트
- [ ] 기술통계 예시 생성

---

## 📍 다음 단계 미리보기

### Day 2 (내일)
```
1. 파이프라인 실행 → 실제 데이터 추출
2. empirics/code/01_process_data.py로 이동
3. Table 1 (기술통계) 생성
```

### Day 3-4
```
Model 1 (OLS) 구현:
Early_Funding ~ Vagueness + Controls
```

---

## 💡 팁

### ChatGPT (利) 사용법
- 구체적 요구사항 제시
- 예시 출력 형식 보여주기
- "작동하는 최소 버전" 요청

### Claude (思) 사용법
- 충분한 맥락 제공
- 원하는 구조 명시
- "production-ready" 요청

### Gemini (義) 사용법
- "Be critical" 명시
- "What could go wrong?" 질문
- 대안 요구

---

## 🔗 참고 문서

- **workflow.md** - 연구 설계
- **연결체계.md** - 폴더 관리
- **전투일지.md** - 일일 기록
- **삼도수군_맹세.md** - AI 프롬프트

---

**"必死卽生, 必生卽死"**

**"죽고자 하면 살고, 살고자 하면 죽는다"**

**지금 바로 전투일지를 열고 Day 1을 시작하세요!** ⚔️

---

**시작 시간**: ___:___  
**목표 완료**: ___:___ (3시간 후)  
**실제 완료**: ___:___ 

**Day 1 상태**: [ ] 시작 전 → [ ] 진행 중 → [ ] 완료
