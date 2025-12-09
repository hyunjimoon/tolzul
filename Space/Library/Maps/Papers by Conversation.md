---
up: [[Papers MOC]]
type: map
---

# 📚 Papers by Conversation

## Active Conversations

### 🔄 Absorptive Capacity
**Null**: "R&D는 새 지식 창조 전용"
**Break**: "R&D는 타인 지식 흡수용"

```dataview
TABLE authors, year, challenges
FROM "Space/Sources/Papers"
WHERE conversation = "absorptive_capacity"
SORT year ASC
```

---

### 💡 Exaptation
**Null**: "혁신은 계획된 목적으로"
**Break**: "혁신은 예상치 못한 재활용"

```dataview
TABLE authors, year, challenges
FROM "Space/Sources/Papers"
WHERE conversation = "exaptation"
SORT year ASC
```

---

## 새 Conversation 추가하기

1. 위 형식 복사
2. Null → Break 구조로 설명
3. 논문들 conversation property 추가

## 새 논문 추가하기

```yaml
---
conversation: "topic_name"
challenges: "한 문장 요약"
---
```

---

## Related
- [[Papers MOC]]
