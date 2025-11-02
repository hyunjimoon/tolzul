---
up: "[[Space]]"
created: 2025-11-01
rank: 5
---

~ [[Space]]

> [!globe] [[Maps]] | [[Papers]] | **[[Dots]]**

**Dots = 지식의 점들**

개념, 아이디어, 통찰을 연결한다.

---

## 🔗 최근 생성된 Dots

```dataview
TABLE WITHOUT ID
	"🧩 " + file.link as "Dots",
	file.folder as "영역",
	length(file.inlinks) as "연결수"
FROM "Space/Dots"
SORT file.ctime desc
LIMIT 20
```

---

## 🌐 가장 많이 연결된 Dots

```dataview
TABLE WITHOUT ID
	"🧩 " + file.link as "Dots",
	length(file.inlinks) as "연결수"
FROM "Space/Dots"
SORT length(file.inlinks) desc
LIMIT 10
```

---

Back to [[Space]]
