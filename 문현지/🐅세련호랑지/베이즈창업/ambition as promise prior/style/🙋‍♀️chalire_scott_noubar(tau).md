[[09-16|25-09-16]]

[[day 4.5 scott(Bayesian Entrepreneurship)]]
# 🙋‍♀️QnA - tau 매개변수 핵심 질문과 답변

## 🙋‍♀️Q1: McElreath의 부분풀링 네 효과 중 tau와 가장 가까운 것은?

**답변: (3) To study variation이 가장 적합합니다.**

**이유:**

- tau는 founder-venture 간의 **변동(variation)을 명시적으로 모델링**하는 매개변수
- 창업자 개인의 확신 수준과 벤처의 실제 성과 간의 불일치를 포착
- 단일 수준 모델로는 이러한 계층적 변동을 제대로 반영할 수 없음
- tau가 클수록 그룹 간 변동이 크고, 작을수록 변동이 작음

**부차적 연결:**

- (4) To avoid averaging도 관련됨 - tau는 평균화로 인한 정보 손실을 방지
- 높은 tau = 개별 벤처의 특수성 보존
- 낮은 tau = 전체 패턴으로의 수렴

---

## 🙋‍♀️Q2: Bayesian Entrepreneurship 진영의 Scott은 tau를 어떻게 설명할까?

**Scott의 관점에서 tau 해석:**

**"tau는 prior의 concentration parameter로서 belief updating의 속도를 결정한다"**

1. **Prior Specification 측면:**
    
    - 낮은 tau = diffuse prior (약한 초기 믿음)
    - 높은 tau = concentrated prior (강한 초기 믿음)
    - Better Place: 과도하게 concentrated prior → 새로운 증거 무시
2. **Bayesian Learning 측면:**
    
    - tau가 낮을수록 posterior가 데이터에 민감하게 반응
    - tau가 높을수록 prior에 고착되어 학습 속도 저하
    - Tesla: 낮은 tau로 시작 → 빠른 belief updating → 시장 적응
3. **Information Value 측면:**
    
    - tau는 새로운 정보의 가치를 결정
    - 높은 tau에서는 정보 획득의 한계효용 체감
    - "실험의 가치" 계산에 직접적 영향

---

## 🙋‍♀️Q3: Hybrid Entrepreneurship 진영의 Charlie는 tau를 어떻게 설명할까?

**Charlie의 관점에서 tau 해석:**

**"tau는 조직의 entropy 증가율과 acculturation cost의 균형점이다"**

1. **Acculturation Cost 프레임:**
    
    - 높은 tau = 높은 문화 고착 비용
    - "조직 entropy는 항상 증가" → tau가 entropy 증가 속도 조절
    - Better Place: 초기 높은 tau로 인한 문화 경직 → 적응 실패
2. **Hybrid Structure 측면:**
    
    - tau는 exploration과 exploitation의 균형 매개변수
    - 낮은 tau = 더 많은 hybrid 실험 가능
    - 높은 tau = early commitment trap
3. **Organizational Learning:**
    
    - tau가 "unlearning cost"를 결정
    - 높은 tau 조직은 기존 루틴 버리기 어려움
    - Tesla: 낮은 tau → 지속적 재구성 가능
4. **Dynamic Capability 연결:**
    
    - tau는 sensing-seizing-reconfiguring 사이클의 속도 결정
    - 낮은 tau = 빠른 사이클, 높은 적응력
    - 높은 tau = 느린 사이클, path dependency 위험

---

## 🙋‍♀️Q4: Evolutionary Entrepreneurship의 Noubar Afeyan은 tau를 어떤 변수에 대응시킬까?

**Noubar Afeyan의 Flagship Pioneering 프레임워크에서 tau 해석:**

**"tau는 Emergent Discovery 과정의 'Evolutionary Pressure' 강도다"**

1. **Origination Platform 관점:**
    
    - tau = "hypothesis space의 제약 정도"
    - 낮은 tau = 넓은 탐색 공간, 많은 변이 허용
    - 높은 tau = 좁은 탐색 공간, 빠른 수렴 압력
2. **ProtoCo → NewCo 전환에서:**
    
    - tau는 "graduation threshold"의 엄격성
    - Better Place: 너무 이른 graduation (높은 tau)
    - Tesla: 점진적 graduation (낮은 tau)
3. **Evolutionary Algorithm 측면:**
    
    - tau = selection pressure / mutation rate 비율
    - 높은 tau = 강한 선택, 약한 변이 → premature convergence
    - 낮은 tau = 약한 선택, 강한 변이 → 지속적 진화
4. **"What if it's possible?" 철학과 연결:**
    
    - tau는 "가능성 공간의 개방성"
    - 낮은 tau = 더 많은 "what if" 질문 허용
    - 높은 tau = 조기 답변 고착

---

## 🙋‍♀️Q5: 🧠접근과 🤜접근의 명명법

**제안: 세 가지 명명 체계**

### 1. **인지적 차원 (Cognitive Dimension)**

- 🧠접근 = **"Deliberative Approach"** (숙고적 접근)
- 🤜접근 = **"Adaptive Approach"** (적응적 접근)

### 2. **학파적 차원 (School Dimension)**

- 🧠접근 = **"Planning School"** (계획 학파)
- 🤜접근 = **"Effectuation School"** (실현 학파)

### 3. **통합적 명명 (추천)**

- 🧠접근 = **"Bayesian-Deliberative School"**
    
    - Prior 설정과 belief updating에 중점
    - 정보의 체계적 통합
    - Scott의 Bayesian entrepreneurship 대표
- 🤜접근 = **"Evolutionary-Adaptive School"**
    
    - 변이와 선택을 통한 적응
    - Emergent strategy와 exaptation
    - Charlie의 hybrid approach + Noubar의 evolutionary approach 통합

### 추가 제안: **"Tau Spectrum Framework"**

- Low tau zone = "Adaptive Zone" (적응 영역)
- Medium tau zone = "Optimal Learning Zone" (최적 학습 영역)
- High tau zone = "Commitment Trap Zone" (고착 함정 영역)

이를 통해:

- Planning vs Action의 이분법 극복
- Bayesian vs Evolutionary의 통합
- Partial pooling의 중간 지점 강조