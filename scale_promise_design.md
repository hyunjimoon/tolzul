# 🎹 Growing Venture with Precision: Optimal Ignorance Level (OIL)

## 🐢 서론 (Introduction)

### 1. Hook: Tale of Two Ventures
- Tesla와 Better Place: 같은 비전(리튬이온 배터리로 자동차 산업 전기화)
- 하나는 1조원 가치, 하나는 10억 소진 후 소멸
- 차이는 τ(정밀도) 관리: Better Place는 높은 τ로 시작해 학습 함정에 갇힘, Tesla는 낮은 τ에서 시작해 점진적으로 증가

### 2. Problem: Exogenous Success Probability
- 기존 문헌: 벤처 성공 확률(P) 또는 증거의 정보성(informativeness)을 외생적으로 취급
- Bayesian Entrepreneurship: 주관적 사전분포 강조하지만 업데이트 크기는 미고려
- 실험/금융 문헌: 우도(likelihood) 중심, 사전분포는 공통지식으로 가정

### 3. Solution: Optimal Ignorance Level (OIL)
- τ* = max{0, √(V/4i) - 1}
- V: 벤처 가치 (성공 시 수익)
- i: 정보 통합 비용 (조직 클락스피드의 역수)
- τ: 정밀도 (약속의 구체성/경직성)

### 4. Why Ent Scholar and Practitioner Should Care
- "Fake it till you make it" 모델의 한계
- 정밀도 긴장: 너무 높으면 학습 불가, 너무 낮으면 자원 동원 불가
- OIL은 effectuation→design→scientific→causal 스펙트럼 통합

### 5. Contribution Summary
1. **Prescriptive Theory**: τ 최적화 공식
2. **Multi-Level Theory**: τ의 3층 의미 (확률/인지/진화)
3. **Dynamic Framework**: nail it → scale it 전환 관리

### 6. Paper Structure
- Section 2: 이론적 배경 (정밀도 선택, 의미 통합, 성장)
- Section 3: 모델 (복잡성, 열망, 정밀도)
- Section 4: 적용 (Tesla vs Better Place)
- Section 5: 비전과 함의

## 🐅 이론 (Theory)

### 1. Selecting Precision
- Beta-Binomial 모델: ϕ ~ Beta(μτ, (1-μ)τ)
- 업데이트 용량: Δ(μ; τ) = μ/(1 + τ)
- 기존 문헌과 차별점:
  - Bayesian Entrepreneurship: 업데이트 크기 미고려
  - Experimentation/Finance: P를 고정으로 취급
  - Operations/Learning: P를 기술적 산물로 취급

### 2. Integrating Meanings
#### τ Spectrum (인식론적 논리 통합)
- τ = 0: Effectuation (완전 유연성)
- τ 낮음: Design thinking
- τ 중간: Scientific entrepreneurship  
- τ → ∞: Causal logic (완전 계획)

#### τ Hierarchy (3층 의미)
1. **확률층**: 정밀도 모수 (베이지안 통계)
2. **표본층**: 유사-표본 크기 (인지과학)
3. **진화층**: 변이-선택 균형 (진화동학)

### 3. Growing Precision
- Nail it → Scale it 전환
- 병렬 성장: 시장 규모(V)와 역량(1/i) 동시 증가
- 운영 도구:
  - i 감소: Acculturate, Processify, (Platformize)
  - V 증가: Segment, Replicate, Capitalize, (Platformize)

## 🐙 모델 (Model)

### 1. M1 & M1': Complexity
- M1 (Naive): max P(S|ϕ) = ϕ → ϕ* = 1
- M1' (Complexity): max ϕ(1-ϕ)^c → ϕ* = 1/(c+1)
- 복잡성이 열망을 규율

### 2. M2: Aspiration (Empirical Bayes)
- ϕ ~ Beta(μ, 1)으로 사전분포 도입
- max ∫P(S∧D|ϕ)p(ϕ|μ)dϕ
- μ* ≈ 1/(log c + γ)

### 3. M2': Precision (Optimal Ignorance)
- ϕ ~ Beta(μτ, (1-μ)τ)
- max V·E[ϕ(1-ϕ)^c] - iτ
- **Proposition**: c=1일 때, μ*=1/2, τ*=max{√(V/4i)-1, 0}

### 4. Interpretation
- M1 vs M2: 결정론적 vs 확률론적
- 고정 τ (Better Place) vs 동적 τ (Tesla)
- τ 증가의 두 이유:
  1. 품질 제어 (변이 생성 후 선택)
  2. 시뮬레이션과 최적화

## 🦓 시험 (Test)

### 1. Describe: Tesla vs Better Place Case
- **Better Place**: τ=4로 시작, 경직된 약속 (배터리 교환, 판매 목표)
  - 이스라엘과 긴밀 결합 → 철수 시 대안 없음
  - 높은 복잡성(c≈10): 로봇공학, 부동산, 표준, OEM
- **Tesla**: τ≈1로 시작, 단계적 실험
  - Roadster → Model S → Model 3 (세분화와 협업)
  - "Production hell"로 i 감소, 문화 구축
  - 고객이 지연 수용 (전도사 역할)

### 2. Prescribe: How to Use OIL
**Nail Stage (V < 4i)**
- τ = 0 유지 (최적 무지)
- Segment & Collaborate로 초기 고객/파트너 확보
- 실험과 피벗 반복

**Scale Stage (V ≥ 4i)**  
- τ 증가 시작: τ* = √(V/4i) - 1
- i 감소: Acculturate, Processify
- V 증가: Replicate, Capitalize, Platformize
- 주의: Automate은 신중히 (Tesla의 과도한 자동화 실패 교훈)

### 3. Predict: Staged Precision Hypothesis
**예측 1**: τ 증가 궤적을 가진 벤처가 시장에서 선택됨
- 낮은 τ → 높은 τ 전환 = 생존
- 높은 τ 시작 = 붕괴

**예측 2**: τ 증가 속도
- 양면 균형(sellability = deliverability) 시 더 빠른 τ 증가
- 언어 분석으로 τ 측정 가능 (모호함 vs 구체성)

## 👾 비전 (Vision)

### 1. What+Why+How for Practitioners
**What**: OIL = 정보 통합 비용 대비 벤처 가치의 함수
**Why**: 자원 동원과 학습 능력의 균형점 제공
**How**: 
- 단계적 약속 관리
- 문화 구축 후 프로세스화
- 복잡성 제어하며 시장 확대

### 2. Why for Scholars
- 미시 실험과 거시 선택 연결
- 주관적 사전분포의 형태를 설계 변수로
- 기업가를 베이지안 모델링 에이전트로 재정의

### 3. So What for Scholars
**이론적 함의**:
- 정보성의 내생화
- 진화적 기업가정신과 베이지안 의사결정 통합
- 조직 클락스피드와 정밀도의 연결

**실증적 기회**:
- 창업자 언어에서 τ 측정
- 계층적 베이지안 모델로 이질적 궤적 추정
- 생존과 τ 궤적의 관계 검증

### 4. So What for Practitioners
**투자자를 위한 체크리스트**:
- 창업자의 약속 구체성 평가
- i 감소 노력의 증거
- V/i 비율 추적

**창업자를 위한 원칙**:
- "Simplify to aspire, acculturate to concentrate"
- 약속은 벌어들이는 것 (earned precision)
- 모호함은 초기 단계의 전략적 자산

---

## 핵심 메시지
> "성장은 τ의 단계적 증가이며, 이는 정보 통합 비용(i)을 낮추고 벤처 가치(V)를 높여 '벌어들여야' 한다."