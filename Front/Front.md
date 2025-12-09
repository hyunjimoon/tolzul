---
type: dashboard
created: 2025-10-16
modified:
  - 2025-11-01T21:12:50-04:00
  - 2025-11-02T20:48:03-05:00
---

# 👁 Front - 눈 / VOI

> **명료하게 본다. 실행으로 수렴한다.**

---

## 🎶 경로의 멜로디

Front는 프로젝트를 관리하는 곳이다.  
명확한 경로를 보며, Value of Information을 극대화한다.

---

## ☀️ 매일 아침 Ritual (9 AM)

### 오늘의 필사즉생 3가지
1. [ ] **______** | Next: ______ | Why today: ______
2. [ ] **______** | Next: ______ | Why today: ______
3. [ ] **______** | Next: ______ | Why today: ______

**체크포인트**:
- [ ] 어제 Top 3 중 하나라도 완료했나?
- [ ] 오늘 Top 3가 On 폴더 rank 1-3과 일치하나?
- [ ] 3일 이상 진전 없는 항목 → Ongoing 강등했나?

---

## 🏔️ 세 가지 강도

> [!mountain] **[[On|On]]**  
> 현재 실행 — 지금 집중하는 작전

> [!mountain] **[[Ongoing|Ongoing]]**  
> 진행 작전 — 지속 추진하는 프로젝트

> [!mountain] **[[Simmering|Simmering]]**  
> 준비 중 — 천천히 익히는 아이디어


## 🔥 On - 지금 당장 (명량: 12척 vs 133척)

> **필사즉생**: 죽고자 하면 살고, 살고자 하면 죽는다.  
> 3개만 선택. 4번째는 Ongoing으로.

```dataview
TABLE 
  rank as "순위",
  deadline as "⏰",
  next_action as "다음 행동",
  file.mtime as "최근"
FROM "Front/On"
WHERE file.name != "README" 
  AND rank <= 3
SORT rank ASC
LIMIT 3
```

### 📌 오늘의 Top 3
**매일 아침 작성 (9 AM ritual):**
1. [ ] **[항목명]** - 오늘 할 것: ______
2. [ ] **[항목명]** - 오늘 할 것: ______
3. [ ] **[항목명]** - 오늘 할 것: ______

**규칙**:
- 4번째 추가하려면 → 먼저 1개를 Ongoing으로
- 3일 진전 없으면 → 자동 Ongoing 강등
- Rank는 1, 2, 3만 가능 (4 이상은 에러)

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

## 📊 Weekly Review (Every Sunday)

**3가지 질문**:
1. 이번 주 On 항목 3개 중 몇 개 완료? → ____/3
2. 3일 이상 말 없는 On 항목? → Ongoing으로
3. Ongoing 중 On으로 올릴 것? → 준비된 것 선택

```dataview
TABLE 
  file.ctime as "시작",
  date(today) - file.ctime as "경과일"
FROM "Front/On"
WHERE file.name != "README"
  AND date(today) - file.mtime > dur(3 days)
SORT file.mtime ASC
```
*⚠️ 3일 이상 진전 없음 → Ongoing으로 강등 고려*
