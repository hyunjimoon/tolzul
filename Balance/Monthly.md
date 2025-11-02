---
up: "[[Balance]]"
created: 2025-11-01
rank: 5
---

~ [[Balance]]

> [!calendar] [[Daily]] | [[Weekly]] | **[[Monthly]]**

**Monthly = 월별 화음**

한 달의 패턴을 점검한다.

---

## 🗓️ 분기별 회고

```dataview
TABLE WITHOUT ID
	file.link as "회고",
	file.ctime as "작성일"
FROM "Balance/월별 화음"
WHERE file.name != "Monthly"
SORT file.ctime desc
LIMIT 8
```

---

## 🎼 월간 질문

**어떤 패턴이 보이는가?**  
**여백 V는 적절한가?**  
**다음 달의 방향은?**

---

Back to [[Balance]]
