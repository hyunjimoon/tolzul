---
up:
  - - Home
type: map
created: 2025-10-16
성장:
  - 2025-10-16T22:10:58-04:00
tags:
  - map
---

# 📚 Collections

5개 주요 컬렉션 중심 대시보드

---

## 📄 Papers - Conversation Threads

```base
papers
```

**특징**: 👂✋👁 3질문 기반
- Conversation으로 그룹화
- Gap + Important 컬럼

---

## 👥 People - By Field

```base
people
```

**특징**: 분야별 정렬
- Field → Name
- Affiliation + Atom

---

## 📖 Books - Rating First

```base
books
```

**특징**: ⭐ 평점 우선
- 최고 평점부터
- Genre 포함

---

## 🎬 Movies - Rating First

```base
movies
```

**특징**: ⭐ 평점 우선
- Director + Genre
- 최신순

---

## 🎯 Balance - Rhythms

```base
home-balance
```

**특징**: Balance 폴더
- 리듬 이름
- 경로

---

## Quick Stats

```dataview
TABLE 
  length(rows) as "Count"
FROM ""
WHERE type IN ["paper", "person", "book", "movie"]
GROUP BY type
```

---

## Related
- [[Papers by Conversation]]
- [[Papers MOC]]
- [[Home]]
