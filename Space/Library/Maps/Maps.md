---
up: "[[Space]]"
created: 2025-11-01
rank: 5
modified:
  - 2025-11-02T10:07:12-05:00
---

~ [[Space]]

> [!globe] **[[Space/Library/Maps/Maps]]** | [[Space/Papers]] | [[Space/Library/Maps/Dots]]

**Maps = 지식의 지형도**

연결의 지도를 만들고, 생각의 경로를 탐색한다.

---

## 📍 핵심 Maps

```dataview
TABLE WITHOUT ID
	"🗺️ " + file.link as "Maps",
	rank as "Rank",
	file.folder as "위치"
FROM "Space/Maps"
WHERE file.name != "Maps"
SORT rank desc
LIMIT 20
```

---

## 🔄 최근 생성된 Maps

```dataview
TABLE WITHOUT ID
	"🗺️ " + file.link as "Maps",
	file.ctime as "생성일"
FROM "Space/Maps"
WHERE file.name != "Maps"
SORT file.ctime desc
LIMIT 10
```

---

Back to [[Space]]
