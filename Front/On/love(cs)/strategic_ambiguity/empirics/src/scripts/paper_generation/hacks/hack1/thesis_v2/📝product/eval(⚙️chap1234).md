---
created: 2025-11-29
evaluator: 04_GE🟢 (Claude Code)
virtue: 造 (구축)
role: Manufacturing/Build (MIT Framework)
rally_point: RP2
modified:
  - 2025-11-29T06:08:02-05:00
  - 2025-12-04T15:02:26-05:00
  - 2025-12-04T15:15:00-05:00
---

# 04_GE🟢 논문 협업 회고록

> 통제사님과 전라좌수군 군령에 따라 ✌️U, 🦾C 논문 작성 과정에서 배운 점들을 문서화합니다.
> 🤹N 논문 작성과 후배 연구자들을 위한 지침서입니다.

---

# Part 1: ✌️U 논문 회고

## 1. 핵심 교훈: "H₀를 먼저 세워라"

### 처음 상태
```
V → G?  (vagueness가 growth에 어떤 영향?)
```

### 최종 상태
```
H₀: βGV < 0  (Scott's Null: "정밀할수록 좋다")
    ↓ Rejected
H₁: P(Growth | V extreme) > P(Growth | V middle)  (Quantile-based U-shape)
```

**배운 점**:
- 기존 문헌의 "상식"을 H₀로 명시적으로 세움
- H₀ 기각이 story의 시작점 ("왜 기각되었나?")
- Parametric → Quantile-based: β₁V + β₂V² 수식이 대칭을 강제하므로, quantile 비교로 전환
- 데이터가 말하게 해야 함 — 수식이 현상을 강제하면 안 됨

---

## 2. Gospel → Puzzle → Answer 템플릿의 탄생

### ✌️U에서 확립된 7단계 (📿→🧩→😮→🔎→😆→🗺️→🗄️)

| ¶ | 단계 | 역할 |
|:-:|:-:|:---|
| 1 | 📿 Gospel | Scott's Null 소개 (기존 상식) |
| 2 | 🧩 Puzzle | U-shape 현상 발견 |
| 3 | 😮 RQ | "When is vagueness valuable?" |
| 4 | 🔎 Lens | Audience segmentation framework |
| 5 | 😆 Solution | Two paths: Analyst vs Believer |
| 6 | 🗺️ Closest | 기존 논문 대비 positioning |
| 7 | 🗄️ Organization | Section roadmap |

**원칙**: Abstract = ¶1-5 첫 문장 추출

---

## 3. Feedback 처리의 체계화

### F02: Endogeneity — 가장 어려운 도전

| 문제 | 우리의 해석 |
|:---|:---|
| Precise → polished | Resource confound |
| Abstract → smarter | Ability confound |
| Middle → bad ideas | Quality confound |

### "Mechanism Defense" 전략의 발견

```
완벽한 인과: V → Y (direct, exogenous) — 증명 불가
우리의 방어: V → Investor Match → Y (mediated) — 경로 제시
```

**배운 점**: 인과관계 증명 대신 "이 경로로 작동한다"를 보여주면 된다.

---

## 4. β·V(1-V) 대칭 강제 문제 (F05)

### 시행착오
| 버전 | 수식 | 문제 |
|:---|:---|:---|
| v2.0 | β·V(1-V) | 대칭 강제 |
| **v5.0** | β₁V + β₂V² | 비대칭 허용 |

**배운 점**: 수식이 현상을 강제하면 안 됨. 데이터가 말하게 해야 함.

---

# Part 2: 🦾C 논문 회고

## 1. 핵심 교훈: "Black Box를 열어라"

### 처음 상태
```
E → Y↓  (관찰된 현상)
"더 많은 자금이 왜 나쁜 결과를 낳는가?"
```

### 최종 상태
```
E → |ΔV|↓ → Y↓  (mechanism chain)
dY/dE = dY/d|ΔV| × d|ΔV|/dE = (+)(−) < 0
```

**배운 점**:
- 단순 상관관계 (E↔Y)는 reviewers가 공격하기 쉬움
- Chain을 보여주면 "왜?"에 대한 답이 됨
- 각 link를 별도로 검증하면 mechanism defense가 성립

---

## 2. Notation의 힘

### 시행착오
| 초기 | 문제 | 최종 |
|:---|:---|:---|
| "funding" | 모호함 (early? total?) | **E** = Early, **L** = Later |
| "success" | 측정 불가 | **Y** = L/E (비율) |
| "flexibility" | 추상적 | **|ΔV|** = |V_L - V_E| |

**배운 점**:
- 변수명을 한 글자로 통일하면 수식이 깔끔해짐
- "Money as flow, not stock" — L/E가 Total보다 나은 이유
- 모든 문서에서 같은 notation 사용 → 일관성

---

## 3. Figure-First Approach

### 깨달음
> "논문은 Figure 3개로 설명할 수 있어야 한다"

| Figure | 역할 | 검증 내용 |
|:---|:---|:---|
| **Fig1** | Mechanism | 3-panel: (+)(−) = (−) |
| **Fig2** | Robustness | 모든 decile에서 cost < 0 |
| **Fig3** | Punchline | 8.8× gap (Escape vs Cage) |

**배운 점**:
- 먼저 그림을 그리고, 그 그림을 설명하는 글을 쓴다
- `figures.py`를 replication code로 제공 → 투명성
- `[[ ]]` 링크로 그림과 글을 연결 → 추적성

---

## 4. Limitation은 공격이 아니라 방어

### F02 피드백 처리 예시

**피드백**: "|ΔV|가 학습 자체인가?"

**방어** (Limitation 5):
```
|ΔV| = 학습의 결과 (outcome), 학습 능력 (capacity) 아님

Low |ΔV|는:
(a) 학습 못함 (σ↓)
(b) 학습했지만 못 바꿈 (lock-in)
둘 다 intervention이 다름
```

**배운 점**:
- Limitation을 먼저 인정하면 reviewer가 공격할 여지가 줄어듦
- "Future work" 섹션에서 해결책 제시 → 건설적 마무리
- `feedback🪵.md`로 피드백을 체계적으로 추적

---

# Part 3: ✌️U ↔ 🦾C 비교 및 통합 교훈

## 두 논문의 구조적 대응

| 요소 | ✌️U | 🦾C |
|:---|:---|:---|
| **Core Variable** | V (Vagueness) | E (Early Funding) |
| **Outcome** | G (Growth: Series C+) | Y = L/E (Growth Ratio) |
| **Shape** | U-shape (Quantile-based) | Negative (dY/dE < 0) |
| **Mediator** | Investor Match | |ΔV| (Flexibility) |
| **H₀** | βGV < 0 (Scott's Null) | E↑ → Y↑ (RBV) |

## 공통 패턴

### 1. H₀ 설정 → 기각 → 설명
```
✌️U: Scott's Null → Rejected → U-shape 발견
🦾C: RBV Prediction → Rejected → Mechanism chain 제시
```

### 2. Mechanism Defense
```
✌️U: V → Investor Match → G
🦾C: E → |ΔV|↓ → Y↓
```

### 3. Feedback 체계화
```
feedback🪵.md → F01, F02, ... → ¶ mapping → Resolution
```

---

# Part 4: 🤹N 논문을 위한 시사점

| ✌️U/🦾C에서 배운 것 | 🤹N에 적용 |
|:---|:---|
| H₀ 먼저 세우기 | "k*=1 (one option is optimal)" |
| Mechanism chain | k* = F_D⁻¹(C/(C+F)) chain |
| Figure-first | k* 최적화 그래프 먼저 |
| Notation 통일 | k*, C, F, D 변수 고정 |
| Limitation = Defense | "k* estimation uncertainty" 선제 인정 |
| 3-sentence story | "몇 개 옵션이 최적인가?" |

---

# Part 5: 협업 프로세스 체크리스트

## 잘된 점
- [x] `toc.md` 중심의 구조화
- [x] `[[ ]]` 링크로 문서 간 연결
- [x] `feedback🪵.md`로 피드백 추적
- [x] `figures.py`로 재현 가능한 분석
- [x] Gospel → Puzzle → Answer 템플릿

## 개선할 점
- [ ] 한글/영어 섞임 → 일관성 필요
- [ ] 이모지 인코딩 깨짐 (일부 시스템에서)
- [ ] Figure 생성 시간 → 병렬화 고려

---

## 핵심 메시지 모음

| 논문 | Punchline |
|:---|:---|
| **✌️U** | "Extremes win, middle loses. Analyst vs Believer." |
| **🦾C** | "결핍 → 유연성 → 성공. σ 유지는 Bayesian hygiene." |
| **🤹N** | "k* = F_D⁻¹(C/(C+F)). 옵션 수 최적화." |

---

**서명:** 04_GE🟢 (Claude Code) → 통제사🌙

*"Black box를 열고, H₀를 세우고, Mechanism chain을 보여라."*
