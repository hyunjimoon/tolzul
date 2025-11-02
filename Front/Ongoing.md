---
up: "[[Front]]"
created: 2025-11-01
rank: 5
---

~ [[Front]]

> [!mountain] [[On]] | **[[Ongoing]]** | [[Simmering]]

**Ongoing = 진행 작전**

지속적으로 추진하는 프로젝트.

---

## 🔄 진행 중인 프로젝트

```dataview
TABLE WITHOUT ID
	"⚗️ " + file.link as "Project",
	rank as "Rank",
	status as "상태"
FROM "Front/Ongoing"
WHERE file.name != "Ongoing"
SORT rank desc
LIMIT 10
```

---

## 🌊 균형 원칙

**지속 가능성** — 장기전을 고려한다  
**점진적 진전** — 작은 진전을 축적한다  
**유연성** — 상황에 따라 조율한다

---

Back to [[Front]]
