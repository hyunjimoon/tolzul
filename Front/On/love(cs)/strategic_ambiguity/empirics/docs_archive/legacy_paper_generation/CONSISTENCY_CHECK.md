# 일관성 체크: 업데이트된 논문 구조 vs 현재 4-Phase Framework

**분석일**: 2025-11-24
**대상**: `src/scripts/paper_generation/` 4-Phase 전라좌수군 Framework

---

## ✅ 일치하는 부분 (Consistent)

### 1. **챕터-Phase 매핑**
| 업데이트된 구조 | 현재 4-Phase | 상태 |
|----------------|-------------|------|
| Chapter 1: Introduction | Phase 1 (起 - 정운 🐢) | ✅ 일치 |
| Chapter 2: Literature & Theory | Phase 2 (承 - 권준 🐅) | ✅ 일치 |
| Chapter 3: Empirical | Phase 3 (轉 - 김완 🐙) | ⚠️ 부분 일치 |
| Chapter 4: Discussion & Implications | Phase 4 (結 - 어영담 👾) | ✅ 일치 |

### 2. **Four-Module Framework (C-T-O-C)**
- ✅ Phase 2에서 **Customer, Technology, Organization, Competition** 4개 모듈 모두 다룸
- ✅ Module 2 (Technology Modularity)를 core focus로 설정
- ✅ Real Options 이론과 Information Economics 대비 구조 유지

### 3. **Real Options Logic**
- ✅ "Vagueness preserves option value" 논리 일관됨
- ✅ Modularity → pivot cost → vagueness effectiveness 인과 체인 명확

---

## ❌ 불일치하는 부분 (Inconsistent)

### 1. **개념 프레임워크 명시성 부족**

**업데이트된 구조가 강조하는 2×2 구조**:
```
Axis 1: Value Creation (Customer, Technology) vs Value Capture (Organization, Competition)
Axis 2: Resource Support vs Flexibility
```

**현재 코드 상태**:
- ❌ "Value creation vs Value capture" 구분이 **명시적이지 않음**
- ❌ Customer/Technology가 value creation에, Organization/Competition이 value capture에 속한다는 설명 없음
- ❌ "Resource support vs Flexibility" 2×2 축이 개념틀에 등장하지 않음

**문제점**:
Phase 2 (`generate_02_theory_conceptual.py`)의 Section 2.4에서:
> "This framework synthesizes insights from information economics (Module 1: Customer Heterogeneity), real options theory (Module 2: Technology Modularity), resource-based view (Module 3: Organizational Slack), and competitive dynamics (Module 4: Competitive Intensity)."

→ 4개 모듈을 나열하지만, **value creation/capture 구분**과 **resource support/flexibility 축**이 보이지 않음.

---

### 2. **핵심 용어 불일치**

| 업데이트된 구조 | 현재 코드 | 상태 |
|----------------|----------|------|
| "vague promise" | "strategic vagueness" | ❌ 불일치 |
| "When does a vague promise pay" | "strategic vagueness succeeds or fails" | ❌ 불일치 |

**영향**:
- 연구 질문의 프레이밍이 다름
- "promise"는 **commitment와 대비**되는 개념 (entrepreneur가 stakeholder에게 하는 약속)
- "vagueness"는 **specificity와 대비**되는 개념 (텍스트/언어적 모호함)

"Vague promise"가 더 **행위자 중심**(entrepreneur의 전략적 선택),
"Strategic vagueness"는 더 **속성 중심**(텍스트의 특성).

---

### 3. **AV Industry Focus 부족**

**업데이트된 구조**:
> "이 논문은 특히 **AV(autonomous vehicle) industry를 중심**으로"

**현재 코드**:
- ✅ Tesla, Waymo 사례는 Phase 1 Introduction에 등장
- ⚠️ Phase 2 Theory에서 AV-specific 특성 설명 부족
- ❌ Phase 3 Empirics에서 AV industry subsample 분석 없음 (quantum, transportation은 있지만 "AV"로 특정하지 않음)

**문제점**:
- General "hardware vs software" 또는 "transportation" 수준에서 다루고 있음
- AV industry의 **특수성**(regulatory uncertainty, sensor fusion complexity, safety-critical nature, ecosystem dependencies)이 드러나지 않음

---

### 4. **Chapter 3 구조 불일치**

**업데이트된 구조 - Chapter 3**:
```
Part 1: AV industry의 4가지 예시(case)로
        customer / technology / organization / competition 별 모호한 선택을 보여줌.

Part 2: Empirics – 실제 데이터/코딩/분석으로
        vague promise와 investment outcome의 관계를 검증.
```

**현재 Phase 3 (`generate_03_empirics.py`)**:
```
PART A: EMPIRICAL STRATEGY
- 3.1 Data Sources & Sample
- 3.2 Measurement Strategy
- 3.3 Empirical Specifications

PART B: RESULTS
- 3.4 H1 Results
- 3.5 H2 Results
- 3.6 Robustness Checks
```

**문제점**:
- ❌ **Part 1 (Case studies)가 완전히 누락**됨
- 업데이트된 구조는 "4가지 AV 예시"를 통해 개념을 illustrate하길 원함
- 현재는 바로 quantitative empirics로 들어감 (descriptive → inferential stats)

---

### 5. **Hypothesis Framing 차이**

**업데이트된 구조**:
- Value creation과 value capture의 **joint optimization** 관점
- 4가지 choice (customer, tech, org, comp)의 **조합**과 trade-off

**현재 코드 (Phase 2, Section 2.9)**:
```python
H1 (Main Effect): Vagueness → Early Funding (negative)
H2 (Moderation): Vagueness × Hardware → Growth (interaction)
```

**문제점**:
- H1/H2는 **Technology Modularity (Module 2)에만 집중**
- Customer heterogeneity, Organizational slack, Competitive intensity는 "future work"로 밀림
- **Joint optimization** 관점 (예: customer vagueness + technology specificity 조합)이 empirically tested되지 않음

---

## ⚠️ 애매한 부분 (Ambiguous)

### 1. **"Commit vs Keep Vague" 선택 조합**

**업데이트된 구조**:
> "customer / technology / organization / competition 영역 각각에서
> 'commit vs keep vague'라는 네 가지 선택 조합이 어떻게 나타나는지"

**현재 코드**:
- Phase 2에서 4개 module을 **독립적으로** 설명 (2.5, 2.6, 2.7, 2.8)
- 하지만 **조합(combination)** 관점의 분석은 없음
- 예: "Customer vague + Technology specific" vs "Customer specific + Technology vague"

**불명확**:
- 업데이트된 구조가 4개 choice의 **조합 효과**를 원하는지,
- 아니면 각각의 **독립 효과**를 원하는지 명확하지 않음

---

## 📋 수정 필요 사항 요약

### Priority 1 (High): 개념적 일관성

1. **Phase 2 Section 2.4를 수정**하여:
   - ✅ 기존: "Four-module framework"
   - ➕ 추가: **2×2 구조 명시**
     - **Axis 1**: Value Creation (Customer, Technology) vs Value Capture (Organization, Competition)
     - **Axis 2**: Resource Support (commit resources) vs Flexibility (preserve options)

2. **용어 통일**:
   - "strategic vagueness" → "vague promise" (또는 둘 다 사용하되 관계 명시)
   - Phase 1 Introduction에서 연구 질문을:
     - "Why does strategic vagueness help some but hurt others?"
     - → "**When does a vague promise pay** in venture funding?"

3. **Phase 3에 Case Study Part 추가**:
   ```
   PART 1: ILLUSTRATIVE CASES (NEW)
   - 3.1 AV Industry Context
   - 3.2 Case 1: Customer Vagueness (Waymo vs Cruise)
   - 3.3 Case 2: Technology Vagueness (Tesla vs Rivian)
   - 3.4 Case 3: Organizational Vagueness (Aurora vs Argo AI)
   - 3.5 Case 4: Competition Vagueness (Platform vs Point Solution)

   PART 2: QUANTITATIVE EMPIRICS (EXISTING)
   - 3.6 Data & Methods
   - 3.7 Results
   - ...
   ```

### Priority 2 (Medium): AV Industry Specificity

4. **Phase 1 Introduction**:
   - Tesla vs Bosch 사례 유지하되, **AV industry context** 강화
   - "Why autonomous vehicles?" 1-2 문단 추가

5. **Phase 2 Theory**:
   - Module 2 (Technology)에서 **AV-specific modularity** 논의
   - 예: Sensor fusion, HD maps, L4/L5 autonomy levels, regulatory constraints

6. **Phase 3 Empirics**:
   - Subsample analysis에 **"AV ventures" subset** 추가
   - Transportation → AV로 좁히기

### Priority 3 (Low): Hypothesis Expansion

7. **Phase 2 Hypotheses**:
   - H1/H2 유지 (Technology focus)
   - H3~H6 추가 (Customer, Organization, Competition) — 또는 "future work"로 명시

---

## 🔄 제안하는 수정 로드맵

### Step 1: Terminology Fix (빠른 수정)
```bash
# Phase 1, 2, 3, 4 모든 파일에서
sed -i 's/strategic vagueness/vague promise/g' generate_*.py
# (실제로는 context-aware replacement 필요)
```

### Step 2: Phase 2 Conceptual Framework 강화
- `generate_02_theory_conceptual.py` Section 2.4 수정
- 2×2 구조 (Value Creation/Capture × Resource Support/Flexibility) 명시
- 4개 module이 이 2×2 공간에서 어디에 위치하는지 설명

### Step 3: Phase 3 Case Study Part 추가
- `generate_03_empirics.py`를 두 부분으로 분리:
  - Part 1: Qualitative cases (new content)
  - Part 2: Quantitative empirics (existing content)
- 또는 별도 generator `generate_03a_cases.py` + `generate_03b_empirics.py` 생성

### Step 4: AV Industry Contextualization
- Phase 1, 2, 3 전체에 AV-specific 논의 추가
- Subsample analysis에 AV ventures 포함

---

## 🎯 결론

**현재 4-Phase framework는**:
- ✅ **구조적으로 잘 설계**되어 있음 (기승전결, 4 commanders)
- ✅ **Core logic (Technology Modularity → Vagueness effectiveness)** 견고함
- ❌ 하지만 **업데이트된 논문 구조의 새로운 강조점**들을 반영하지 못함:
  1. Value creation vs Value capture 프레임
  2. "Vague promise" 용어
  3. AV industry centrality
  4. Case study part in Chapter 3
  5. 2×2 conceptual space (Resource Support × Flexibility)

**권장 사항**:
1. **Phase 2 (권준)를 먼저 수정** → 개념 프레임워크 강화
2. **Phase 3 (김완)에 Case Part 추가** → Qualitative + Quantitative 구조
3. **Terminology 통일** → "Vague promise" 중심으로
4. **AV context 강화** → Phase 1, 2, 3 모두

이렇게 하면 **4-Phase 기승전결 구조는 유지**하면서도, **업데이트된 논문 구조의 요구사항을 충족**할 수 있습니다.
