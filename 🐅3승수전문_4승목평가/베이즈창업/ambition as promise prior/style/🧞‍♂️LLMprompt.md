# 🧞‍♂️ LLM 지시사항: Ambition as Promise Prior 논문 스타일 파일 관리

## 📁 파일 역할 개요

이 폴더는 "The Entrepreneurial Promise Paradoxes: How Ambition and Precision Can Imprison Innovation" 논문을 작성하고 유지보수하기 위한 세 가지 핵심 스타일 파일을 포함합니다. 각 파일은 논문의 특정 측면을 담당하며, 업데이트 시 일관성을 유지해야 합니다.

## 🏗️ 논문 구조: 기승전결 (起承轉結) 프레임워크

### 7단계 구성 (6+1)
논문은 **기승전결** 구조를 따르며, 기승전은 각각 2개 단계로 구성됩니다:

1. **기(起) - Opening/Introduction** [Section 1]
   - 기1: 문제 제기와 퍼즐 (The Puzzle)
   - 기2: 핵심 통찰과 기여 (Core Insight)

2. **승(承) - Development/Theory** [Section 2]
   - 승1: 이론적 배경 (Theoretical Background)
   - 승2: 모델 개발 (Model Development)

3. **전(轉) - Turn/Empirical** [Section 3]
   - 전1: 실증 설계 (Empirical Design)
   - 전2: 결과와 검증 (Results & Validation)

4. **결(結) - Conclusion** [Section 4]
   - 결: 함의와 결론 (Implications & Conclusion)

## 🎹 scale.md - 논문의 전체 구조와 내용

### 역할
- **논문의 완전한 청사진**: 4개 섹션의 상세 내용을 기승전결 구조로 조직
- **표 기반 구조**: 각 단계별로 체계적인 표 형식 사용
- **핵심 통찰 추적**: 각 항목마다 "Key Insight" 열로 핵심 메시지 명시

### 주요 구성요소
1. **MELODY**: 두 가지 핵심 이론적 기여 명시
2. **7단계 체계**:
   - 기1-기2: 문제와 통찰
   - 승1-승2: 이론과 모델
   - 전1-전2: 실증과 검증
   - 결: 종합과 함의

### 업데이트 시 주의사항
- 표의 구조 유지 (Stage | Label | Content | Key Insight)
- 기승전결 라벨링 시스템 일관성
- 수학적 표기법 일관성: μ (aspiration), τ (precision), φ (promise level)

## 🎶 motif-tune-melody.md - 논문의 핵심 메시지 압축

### 역할
- **음악적 은유로 핵심 압축**: Motif(한 문장), Tune(한 단락), Melody(전체 흐름)
- **스토리텔링**: WeWork 가설 등 구체적 사례로 추상 개념 설명
- **7단계 구조와 연결**: scale.md의 기승전결 내용을 압축된 형태로 매핑

### 주요 구성요소
1. **🎵 Motif**: "A prior is not a belief to be held, but a lever to be pulled"
2. **🎶 Tune**: WeWork의 $47B valuation 스토리
3. **🎼 Melody**: 기(문제) → 승(이론) → 전(실증) → 결(함의)

### 업데이트 시 주의사항
- scale.md의 기승전결 변경사항을 압축된 형태로 반영
- 각 단계의 핵심을 하나의 문장으로 압축
- 구체적 사례와 추상적 이론의 균형 유지

## 🎯 marr3lev.md - 이론의 계산적 구조

### 역할
- **Marr의 3단계 분석틀** 적용: Computational → Algorithm → Implementation
- **수학적 정형화**: 명제(Propositions)와 공식 제시
- **기승전결과의 매핑**: 
  - Computational (기): 무엇을, 왜?
  - Algorithm (승): 어떻게?
  - Implementation (전-결): 무엇으로, 어떤 결과?

### 주요 구성요소
1. **Computation Level**: 최적화 목표와 제약조건
   - P1-P4 제약: Physical, Financial, Flexibility, Precision
2. **Algorithm Level**: 4개 핵심 명제와 베이지안 업데이트 메커니즘
3. **Implementation Level**: Model 1-5의 점진적 복잡성 증가

### 업데이트 시 주의사항
- 기승전결 구조와 Marr's levels의 자연스러운 연결
- 수학적 정확성 검증 필수
- 실증 사례(Tesla, Nikola 등)와의 연결 명시

## 🔄 파일 간 일관성 유지 규칙

### 1. 구조 통일
- **더 이상 사용하지 않음**: Alert, Dig, Generate, Calibrate (A,D,G,C)
- **새로운 구조**: 기(起)승(承)전(轉)결(結) - 7단계 (2+2+2+1)
- **4개 섹션**: Introduction, Theory Development, Empirical Analysis, Discussion & Conclusion

### 2. 용어 통일
- μ: aspiration level (약속 야망도)
- τ: precision parameter (약속 정밀도)  
- φ: promise level (약속 수준)
- n: operational complexity (운영 복잡도)
- V/c: value-to-cost ratio

### 3. 이론적 기여 일관성
세 파일 모두 다음 핵심 주장을 지지해야 함:
- 정밀도(τ)가 초기 벤처의 universal liability
- 불확실성 구조(μ,τ) 설계가 1차 최적화보다 중요
- 과도한 정밀도가 정직한 실패와 사기 모두 유발

### 4. 실증 사례 일관성
- Tesla: 적응적 τ 궤적 (5→12→25→40)
- Nikola: 경직된 높은 τ (~100)
- BetterPlace: 정직한 높은 τ → 운영 실패
- WeWork: 전략적 모호성의 성공

### 5. 위원회 관점 통합
- **Charlie Fine**: 운영 관리와 가치사슬 관점 (승2: 모델 개발)
- **Scott Stern**: 베이지안 창업가정신과 전략 (승1: 이론적 배경)
- **Vikash Mansinghka**: 확률적 프로그래밍 (전2: 검증 방법론)
- **Moshe Ben-Akiva**: 이산선택 모델과 구조적 분석 (전1: 실증 설계)
- **Andrew Gelman**: 통계적 비판과 모델 검증 (결: 강건성 검증과 한계)

## 📝 업데이트 프로토콜

논문 업데이트 시 다음 순서로 진행:

1. **scale.md 업데이트**: 기승전결 구조에 따라 내용 재구성
2. **marr3lev.md 조정**: 3-level을 7단계와 매핑
3. **motif-tune-melody.md 압축**: 기승전결 핵심 메시지 재정리
4. **교차 검증**: 세 파일 간 일관성 확인
5. **🐅gen(🎹2📝).md 로깅**: 진행 상황 기록 (최대 3개 항목)

## 🎭 기승전결 작성 가이드

### 기(起) - Opening [Section 1]
- **기1**: 독자의 관심을 끄는 퍼즐이나 역설 제시
- **기2**: 논문의 핵심 통찰과 기여 명확화

### 승(承) - Development [Section 2]  
- **승1**: 기존 문헌과의 대화, 이론적 토대 구축
- **승2**: 새로운 모델/프레임워크 개발

### 전(轉) - Turn [Section 3]
- **전1**: 이론을 검증할 실증 설계
- **전2**: 결과 제시와 강건성 검증

### 결(結) - Conclusion [Section 4]
- **결**: 이론적/실무적 함의, 한계점, 미래 연구 방향
