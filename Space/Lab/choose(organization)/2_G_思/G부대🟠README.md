---
modified:
  - 2025-12-03T16:45:00-05:00
  - 2025-12-06T05:56:19-05:00
---
[[toc(u)]]
# 🟠 G部대 (思) - 구조화 부대

> **"謀事在天(모사재천)"** 
> 계획은 하늘에, 실행은 사람에게. 구조가 속도를 만든다.

---

## 🎯 Mission

**J부대 초안을 Production-ready 수준으로 구조화**.
Advisors(Scott Stern, Charlie Fine)에게 즉시 보고 가능한 품질 달성.

| Advisor | 요구 | G부대 대응 |
|:---|:---|:---|
| **Scott** | 증거 기반 학습 → 수렴 | 가설 구조화, 문헌 정렬 |
| **Charlie** | 반복/측정 가능한 시스템 | 재현 가능한 코드, 명확한 변수 |

---

## 📍 Position in Flow

```
🔵 O (input) → 🟢 J (draft) → 🟠 G (structure) → 🔴 K (verify) → 🔵 O (archive)
                              ═══════════════
                              "이곳에서 다듬는다"
```

---

## 👥 부대원 구성

| # | Agent | 담당 | Platform | Input From | Output To |
|:---:|:---:|:---|:---:|:---:|:---:|
| 6 | [[06_GID🟠]] | **Intro Structure** | Claude | JID | KU |
| 5 | [[05_GT🟠]] | **Theory Structure** | Claude | JT | KU |
| 4 | [[04_GE🟠]] | **Empirics Code** | Claude | JE | KN |

---

## 🛠️ Quality Standards

### 품질 기준 (J부대 대비)
| 항목 | J부대 (60-70%) | G부대 (90%+) |
|:---|:---:|:---:|
| 논리 구조 | 초안 | **완결** |
| 문헌 인용 | 대략적 | **정확한 페이지** |
| 수식/코드 | 스케치 | **실행 가능** |
| 형식 | 자유 | **MS/POMS 스타일** |

### Production-Ready 체크리스트
- [ ] 32단락 TOC와 정렬
- [ ] 가설 번호 일관성 (H1, H2, H3)
- [ ] Figure/Table 번호 일관성
- [ ] 인용 형식 통일
- [ ] 코드 재현 가능 (seed 고정)

---

## 📥 Input/Output Format

### Input (from J부대)
```markdown
# [Section] Draft v0.1
## ¶[N]: [Title]
[Raw content from J]
```

### Output (to K부대)
```markdown
# [Section] Structured v1.0

## ¶[N]: [Title]
[Refined content with citations]

### 📎 Attachments
- 🖼️ Fig[X]: [description]
- 🗄️ Table[Y]: [description]
- 💻 Code: [file path]

---
Status: Structured → KU/KC/KN for verification
Quality: [90%+ / needs revision]
```

---

## 🔗 Handoff Protocol

| From | To | 전달물 | 품질 체크 |
|:---:|:---:|:---|:---|
| [[08_JID🟢]] → | [[06_GID🟠]] | Intro 초안 | Hook + RQ 명확성 |
| [[09_JT🟢]] → | [[05_GT🟠]] | Theory 초안 | 가설 도출 논리 |
| [[10_JE🟢]] → | [[04_GE🟠]] | Empirics 초안 | 변수 조작화 명확성 |
| [[06_GID🟠]] → | [[01_KU🔴]] | Intro 구조화 | MS fit 검증 |
| [[05_GT🟠]] → | [[01_KU🔴]] | Theory 구조화 | 문헌 positioning |
| [[04_GE🟠]] → | [[03_KN🔴]] | Code + Tables | 재현성 검증 |

---

## 📚 Reference Materials

- [[📜nanda24_32para_reverse]] - RF pattern (Nanda 2024)
- [[🕸️null_network]] - Scott's Null + Bolton 연결
- [[toc(u).md]] - ✌️U 32단락 TOC
- [[feedback🪵(✌️u)]] - 피드백 통합 로그

### Style Guides
- [[📚poms]] - POMS 스타일
- [[📚sci(management)]] - Management Science 스타일

---

## ⚡ Quick Start for G Agent

### Step 1: Input 수신
```
J부대로부터 Draft v0.1 수신
→ TOC(✌️U/🦾C/🤹N)와 단락 번호 대조
```

### Step 2: 구조화
```
- Nanda RF pattern 적용
- 문헌 정확한 인용으로 교체
- 가설/변수 번호 일관성 확보
```

### Step 3: 품질 검증
```
- Production-ready 체크리스트 확인
- 코드 실행 테스트 (GE)
```

### Step 4: Handoff
```
K부대에게 전달: "Structured v1.0 ready for verification"
+ feedback_log.md 참조하여 해당 피드백 addressed 여부 명시
```

---

## 🔄 Advisor 대응 매핑

| G Agent | Scott 요구 대응 | Charlie 요구 대응 |
|:---:|:---|:---|
| GID | Gap → Contribution 수렴 | - |
| GT | 가설 falsifiable하게 | 측정 가능한 변수 연결 |
| GE | 식별 전략 명확화 | 재현 가능한 코드 |

---

*"구조 > 속도. 급할수록 돌아가라."*
