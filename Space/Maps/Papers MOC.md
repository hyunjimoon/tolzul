---
up: [[Maps]]
type: map
created: 2025-10-16
tags:
  - map
---

# 📚 Papers MOC

논문 지식 관리의 중심 허브입니다.

---

## 🎯 Quick Access

### By Organization
- **[[Papers by Conversation]]** ⭐ - Posen Framework 기반 conversation threads
- [[Papers by Topic]] - 주제별 분류
- [[Papers by Author]] - 저자별 분류
- [[Papers by Year]] - 연도별 분류

### By Status
- [[Papers - Reading]] - 현재 읽는 중
- [[Papers - To Read]] - 읽을 예정
- [[Papers - Key Papers]] - 핵심 논문
- [[Papers - My Citations]] - 내가 인용한 논문

---

## 📊 Overview

```dataview
TABLE 
  authors as "Authors",
  year as "Year",
  conversation as "Conversation",
  status as "Status"
FROM "Space/Sources/Papers"
SORT year DESC
LIMIT 20
```

---

## 🔍 Quick Stats

### Papers by Conversation
```dataview
TABLE 
  length(rows) as "Count"
FROM "Space/Sources/Papers"
WHERE conversation
GROUP BY conversation
SORT length(rows) DESC
```

### Recent Additions
```dataview
TABLE 
  authors,
  title,
  year
FROM "Space/Sources/Papers"
SORT file.ctime DESC
LIMIT 10
```

### High Priority
```dataview
TABLE 
  authors,
  title,
  conversation
FROM "Space/Sources/Papers"
WHERE rating >= 4
SORT rating DESC, year DESC
```

---

## 🎭 Active Conversations

### 🔄 Absorptive Capacity
**Core**: R&D의 이중 역할 (창조 + 흡수)
- [[Cohen1989]] - Foundational
- [[Zahra2002]] - Process model
- [[Lane2006]] - Multi-level

### 💡 Exaptation
**Core**: 예상치 못한 재활용을 통한 혁신
- [[Andriani2017]] - Concept
- [[Felin2023]] - Extensions

### 🤝 Transaction Costs
**Core**: 거래비용이 조직 형태 결정
- [[Williamson1975]] - Foundational
- [[Rindfleisch1997]] - Marketing

→ [[Papers by Conversation]] 에서 전체 보기

---

## 🏗 System Structure

```
Papers/
├── By Conversation ⭐    # Posen Framework
├── By Topic             # Traditional
├── By Author            # Reference
└── By Year              # Timeline
```

---

## 🚀 Workflows

### Adding New Paper
1. Create note in `Space/Sources/Papers/`
2. Use [[Paper Template]]
3. Add to conversation: `conversation: "topic_name"`
4. Fill Posen Framework
5. Link related papers

### Writing Literature Review
1. Open [[Papers by Conversation]]
2. Select conversation thread
3. Follow paper timeline
4. Identify your position
5. Write contribution

### Finding Related Work
```dataview
TABLE authors, title, year
FROM "Space/Sources/Papers"
WHERE contains(conversation, "YOUR_TOPIC")
SORT year ASC
```

---

## 📝 Templates

- [[Paper Template]] - 새 논문 노트
- [[Conversation Template]] - 새 conversation
- [[Literature Review Template]] - 문헌 리뷰

---

## 🎯 Best Practices

### When Reading
- [ ] Fill Posen Framework first
- [ ] Identify conversation thread
- [ ] Link to related papers
- [ ] Note key quotes
- [ ] Think about your contribution

### When Writing
- [ ] Start with conversation thread
- [ ] Follow paper timeline
- [ ] Position your contribution
- [ ] Use quick reference sections
- [ ] Update as you write

---

## 🔗 Related Maps

- [[Research Framework]] - 연구 방법론
- [[Writing Projects]] - 진행 중인 글쓰기
- [[Concepts]] - 핵심 개념
- [[Ideas]] - 아이디어

---

## 💡 Why This System?

### Traditional Approach ❌
```
Papers/
├── JournalA/
│   ├── Paper1.pdf
│   └── Paper2.pdf
└── JournalB/
    └── Paper3.pdf
```
- 폴더에 갇힘
- 연결 안 보임
- 흐름 파악 어려움

### Conversation Approach ✅
```
Conversation: Absorptive Capacity
├── Cohen1989 → Zahra2002 → Lane2006 → [My Work]
└── Null → Break → My Contribution
```
- 논쟁 흐름 파악
- 내 위치 명확
- 논문 쓰기 쉬움

---

## 🎓 Core Philosophy

> "Papers are not isolated islands. They are conversations happening over time."

핵심은:
1. **Conversations** - 논문들은 대화
2. **Connections** - 시간 흐름으로 연결
3. **Contribution** - 내 기여 명확화

---

## Related
- [[Papers by Conversation]] ⭐
- [[Research Framework]]
- [[Home]]
