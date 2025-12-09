# 🔥 On - 명량해전 (12척 vs 133척)

> **필사즉생**: 죽고자 하면 살고, 살고자 하면 죽는다.  
> **3개만 선택**. 4번째는 Ongoing으로.

---

## ⚔️ 명량 규칙 (ENFORCE)

### 1. **최대 3개** (Zero-sum)
- 새 항목 추가 → 반드시 1개를 Ongoing으로
- 4개 이상 = 시스템 실패

### 2. **매일 체크** (Daily ritual)
- 매일 아침 9시: `Front.md`에서 오늘의 Top 3 작성
- 각 항목마다:
  - **Next action**: 오늘 할 구체적 행동 1개
  - **Why today**: 왜 오늘 이것인가?

### 3. **3일 규칙** (Auto-demotion)
- 3일 진전 없음 = Ongoing으로 강등
- Weekly review (일요일)에 확인

### 4. **Rank는 1, 2, 3만** (Hard constraint)
- Rank 4+ = 에러
- 우선순위 불명확 = Ongoing

---

## 📝 파일 Metadata 필수 항목

```yaml
---
rank: 1           # 1, 2, 3 중 하나 (REQUIRED)
deadline: 2025-09-15
next_action: "Charlie에게 초안 이메일"
status: "진행중"  # 진행중, 막힘, 완료
created: 2025-11-02
---
```

---

## 🎯 현재 On 항목 (3개)

**Rank 1:**  
**Rank 2:**  
**Rank 3:**  

*→ `Front.md`의 dataview가 자동으로 보여줌*

---

## 📋 새 항목 추가 프로세스

1. **Triage**: 이것이 정말 Top 3에 들어가나?
2. **Eviction**: 현재 3개 중 1개를 Ongoing으로
3. **Create**: 새 파일에 metadata 추가 (rank, deadline, next_action)
4. **Daily**: 내일 아침 9시 ritual에 포함

---

## 🚫 Anti-patterns

❌ "일단 추가하고 나중에 정리"  
✅ 추가 전에 먼저 제거

❌ "rank 4로 임시 추가"  
✅ Ongoing에 넣고 나중에 승격

❌ "진전 없어도 On에 유지"  
✅ 3일 규칙으로 자동 강등

---

## 📚 철학

**이순신의 명량해전**:  
12척의 배로 133척을 이김.

**핵심**: 선택과 집중.  
적은 자원으로 최대 효과 = 명확한 우선순위.

**"필사즉생"**: 죽기를 각오하고 싸우면 살고, 살려고 하면 죽는다.

**적용**: 3개에 전력을 다하면 성공. 10개를 조금씩 하면 실패.

---

**Questions?** [Front.md](../Front.md)로 돌아가기
