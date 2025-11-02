---
up: "[[Front]]"
created: 2025-11-01
rank: 5
---

~ [[Front]]

> [!mountain] **[[On]]** | [[Ongoing]] | [[Simmering]]

**On = 현재 실행**

지금 당장 집중하는 작전.

---

## ⚡ 활성 프로젝트

```dataview
TABLE WITHOUT ID
	"⚗️ " + file.link as "Project",
	rank as "Rank",
	status as "상태"
FROM "Front/On"
WHERE file.name != "On"
SORT rank desc
LIMIT 5
```

---

## 🎯 집중 원칙

**하나에 집중** — 여러 전선을 동시에 열지 않는다  
**명료하게** — VOI를 극대화한다  
**완료까지** — 시작한 것은 끝맺는다

---

Back to [[Front]]
