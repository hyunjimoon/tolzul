---
type: dashboard
created: 2025-10-16
성장:
  - 2025-11-01T21:12:50-04:00
---

# 👁 Front Dashboard - 흐름 확인

> **"저녁 5분, 전체 흐름을 본다"**

---

## 🔥 On - 지금 당장 (최대 3개)

```dataview
TABLE 
  rank as "긴급도",
  deadline as "데드라인",
  file.mtime as "최근 수정"
FROM "Front/On"
WHERE file.name != "README"
SORT rank ASC, deadline ASC
```

**질문**: 
- [ ] 오늘 진전이 있었나?
- [ ] 내일 다음 행동은?
- [ ] 데드라인 괜찮나?

---

## ♻️ Ongoing - 진행 중

### 🎯 武藝 (AI 3함대 시스템) 🔥
**배치:** 見(人) → 利(ChatGPT) → 思(Claude) → 義(Gemini) → 見

#### 🐙 1_利_빠른실행_ChatGPT
- **역할**: 빠른 프로토타입 생성
- **핵심**: [leadership 가이드](./Ongoing/武藝/1_利_빠른실행_ChatGPT/leadership.md)
- **상태**: 🔥 Active

#### 🐅 2_思_구조화_Claude
- **역할**: 리팩토링, 구조화
- **핵심**: [log.md](./Ongoing/武藝/2_思_구조화_Claude/log.md) | [과학자의 생각법](./Ongoing/武藝/2_思_구조화_Claude/과학자의 생각법.md)
- **상태**: 🔥 Active

#### 🐢 3_義_검증_Gemini
- **역할**: 검증, 피드백, 가치 점검
- **핵심**: [BENT_ActPartner](./Ongoing/武藝/3_義_검증_Gemini/BENT_ActPartner/)
- **상태**: 🌿 Developing

📌 **프레임워크**: [TECH_SPEC_견리사의전환.md](./Ongoing/武藝/TECH_SPEC_견리사의전환.md)

---

**질문**:
- [ ] 일주일 이상 안 건드린 것?
- [ ] On으로 승격할 것?
- [ ] Simmering으로 내릴 것?

---

## 🌱 Simmering - 준비 중

### 🎓 베이즈창업 (Qualifying Exam 핵심)
**테마:** Promise Precision & Venture Operations

#### 🌿 spandrel (Operations Management Theory)
- **핵심**: [15.774 Analytical Operations Management](./Simmering/베이즈창업/spandrel/operations_management/15774_analytical_operations_management.md)
- **주제**: 🏳️‍🌈 managing bit-energy-atom 프레임워크
- **상태**: 🌿 Developing - 이론 구조화 중

#### 🌱 mmi_community (Mobility Venture Analysis)
- **핵심**: [jinhua(mobility venture)](./Simmering/베이즈창업/mmi_community/jinhua(mobility venture).md)
- **데이터**: [mmi2023](./Simmering/베이즈창업/mmi_community/mmi2023.md) | [mmi2024](./Simmering/베이즈창업/mmi_community/mmi2024.md)
- **상태**: 🌱 Early - 데이터 수집 단계

---

**질문**:
- [ ] 시작할 준비된 것?
- [ ] 완전히 버릴 것?

---

## 📊 Flow Metrics

### 이번 주 활동
```dataview
TABLE 
  length(file.outlinks) as "연결",
  length(file.inlinks) as "인용됨"
FROM "Front"
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
```

### 프로젝트 나이
```dataview
TABLE 
  file.ctime as "시작일",
  date(today) - file.ctime as "경과일"
FROM "Front/On" OR "Front/Ongoing"
WHERE file.name != "README"
SORT file.ctime ASC
```
