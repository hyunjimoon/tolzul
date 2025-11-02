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

```dataview
TABLE 
  file.folder as "영역",
  file.mtime as "최근 수정"
FROM "Front/Ongoing"
WHERE file.name != "README"
SORT file.mtime DESC
LIMIT 10
```

**질문**:
- [ ] 일주일 이상 안 건드린 것?
- [ ] On으로 승격할 것?
- [ ] Simmering으로 내릴 것?

---

## 🌱 Simmering - 준비 중

```dataview
LIST
FROM "Front/Simmering"
WHERE file.name != "README"
SORT file.name ASC
LIMIT 5
```

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
