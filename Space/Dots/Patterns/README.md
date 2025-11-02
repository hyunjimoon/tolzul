# 📚 Conversation Threads System

## 🎯 목표

논문을 **Posen Framework** 기반의 **conversation threads**로 조직화하여:
1. 학계 논쟁의 흐름 파악
2. 자신의 기여 위치 명확화
3. 논문 작성시 빠른 참조

---

## 🏗 시스템 구조

```
Space/
├── Dots/
│   └── Conversations/          # Conversation 설명 문서들
│       ├── Absorptive Capacity.md
│       ├── Exaptation.md
│       └── Transaction Costs.md
├── Sources/
│   └── Papers/                 # 개별 논문 노트
│       ├── Cohen1989.md
│       ├── Zahra2002.md
│       └── ...
└── Maps/
    └── Papers by Conversation.md  # 메인 대시보드
```

---

## 🚀 사용법

### 1. 새 논문 추가하기

**Step 1**: Papers 폴더에 논문 노트 생성
```bash
# 템플릿 사용
/Users/.../Papers/[Author][Year].md
```

**Step 2**: 필수 properties 추가
```yaml
---
conversation: "absorptive_capacity"
challenges: "R&D는 창조가 아닌 흡수"
builds_on: [[Cohen1989]]
---
```

**Step 3**: Posen Framework 작성
- Audience: 누구에게?
- Null: 그들이 믿는 것
- Interesting: 가정 깨기
- Important: 왜 중요?
- Valid: 신뢰성

### 2. Conversation 만들기

**Step 1**: Conversations 폴더에 새 파일 생성
```markdown
Space/Dots/Conversations/[Topic Name].md
```

**Step 2**: Conversation Template 사용
- 핵심 논쟁 정의
- Null → Break 구조 설명
- 주요 논문 타임라인

**Step 3**: Papers by Conversation에 섹션 추가

### 3. 논문 작성시 활용

**Step 1**: [[Papers by Conversation]] 열기

**Step 2**: 관련 conversation 찾기

**Step 3**: 논문 흐름 파악
```
Cohen89 → Zahra02 → Lane06 → [내 논문]
```

**Step 4**: 자신의 위치 명확화
- 어떤 가정을 깨는가?
- 누구의 연구를 발전시키는가?

---

## 🎨 Posen Framework

모든 논문/conversation은 이 프레임워크를 따릅니다:

```
Audience (누구에게?)
    ↓
Null Assumption (그들이 믿는 것)
    ↓
Interesting (가정 깨기 - Surprise)
    ↓
Important (왜 중요한가 - Consequence)
    ↓
Valid (믿을 만한가 - Plausibility)
```

### 예시: Cohen & Levinthal (1989)

- **Null**: "R&D는 새 지식 창조 전용"
- **Break**: "R&D는 타인 지식 흡수용"
- **Important**: 높은 spillover에도 R&D 하는 이유 설명
- **Valid**: 우리도 논문 쓰며 남의 논문 읽기 능력 향상

---

## 💡 핵심 원칙

### 1. 간결함 (Simplicity)
- 복잡한 구조 NO
- 필수 정보만
- 빠른 검색 가능

### 2. 연결성 (Connectivity)
- 논문 간 링크
- Conversation 간 링크
- 시간순 흐름

### 3. 실용성 (Practicality)
- 논문 쓸 때 바로 사용
- 참고문헌 빠른 검색
- 기여점 명확화

---

## 📊 Properties 가이드

### Paper Properties
```yaml
conversation: "topic_name"        # 필수
challenges: "한 문장 요약"         # 필수
builds_on: [[Paper1], [Paper2]]  # 권장
cited_by: [[Paper3]]             # 선택
rating: 5                        # 선택
status: reading/done             # 선택
```

### Conversation Properties
```yaml
type: conversation               # 필수
status: active/archived          # 필수
related_conversations: []        # 권장
```

---

## 🎯 Best Practices

### 논문 읽을 때
1. 먼저 conversation 파악
2. Posen Framework 작성
3. 기존 논문과 연결

### 글 쓸 때
1. conversation thread 선택
2. 논문 흐름 확인
3. 자신의 기여 명확화

### 정리할 때
1. 주기적으로 링크 확인
2. conversation 업데이트
3. 새로운 연결 찾기

---

## 🔍 Quick Reference

### 자주 쓰는 Dataview Queries

**Conversation별 논문 수**:
```dataview
TABLE length(rows) as "Papers"
FROM "Space/Sources/Papers"
WHERE conversation
GROUP BY conversation
```

**최근 읽은 논문**:
```dataview
TABLE authors, year, conversation
FROM "Space/Sources/Papers"
SORT file.ctime DESC
LIMIT 10
```

**특정 conversation 논문들**:
```dataview
TABLE authors, year, challenges
FROM "Space/Sources/Papers"
WHERE conversation = "absorptive_capacity"
SORT year ASC
```

---

## 📚 Templates

- **Paper Template**: `/x/Templates/Paper Template.md`
- **Conversation Template**: `/x/Templates/Conversation Template.md`

---

## 🎓 참고자료

- Posen, H. E. (2015). "Riddles in strategy research"
- LYT System: Maps of Content (MOCs)
- Zettelkasten: Atomic notes + Links

---

## 📝 Notes

이 시스템은:
- ✅ 단순하고 실용적
- ✅ 확장 가능
- ✅ 검색 가능
- ✅ 논문 작성에 직접 활용

핵심은 **conversation의 흐름**을 파악하는 것입니다.
