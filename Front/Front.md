---
created: 2025-11-01
type: hub
rank: 5
---

# 👁 Front - 눈 / VOI

> **명료하게 본다. 실행으로 수렴한다.**

---

## 🎶 경로의 멜로디

Front는 프로젝트를 관리하는 곳이다.  
명확한 경로를 보며, Value of Information을 극대화한다.

---

## 🏔️ 세 가지 강도

> [!mountain] **[[Front/On|On]]**  
> 현재 실행 — 지금 집중하는 작전

> [!mountain] **[[Front/Ongoing|Ongoing]]**  
> 진행 작전 — 지속 추진하는 프로젝트

> [!mountain] **[[Front/Simmering|Simmering]]**  
> 준비 중 — 천천히 익히는 아이디어

---

## 🎯 Front 사용법

**매일 저녁**:
- On: 오늘 무엇을 진전시켰는가?
- Ongoing: 어떤 프로젝트가 정체되었는가?
- Simmering: 어떤 아이디어가 무르익었는가?

**주간**:
- 프로젝트 간 우선순위 조정
- On ↔ Ongoing ↔ Simmering 이동
- Rank 재평가

---

## 🌊 흐름의 원칙

**On**: 하나에 집중 (VOI 극대화)  
**Ongoing**: 지속 가능하게 (균형 유지)  
**Simmering**: 여유롭게 (RO 보존)

---

## 🔥 빠른 현황 (저녁 5분)

### On - 지금 당장 (최대 3개)
```dataview
TABLE 
  rank as "긴급도",
  deadline as "데드라인"
FROM "Front/On"
WHERE file.name != "On" AND file.name != "README"
SORT rank ASC
LIMIT 3
```

### Ongoing - 진행 중
```dataview
TABLE WITHOUT ID
  "진행중: " + length(rows) as "프로젝트 수"
FROM "Front/Ongoing"
WHERE file.name != "Ongoing" AND file.name != "README"
```

### Simmering - 준비 중
```dataview
TABLE WITHOUT ID
  "준비중: " + length(rows) as "아이디어 수"
FROM "Front/Simmering"
WHERE file.name != "Simmering" AND file.name != "README"
```

---

Back to [[Home]]
