---
type: dashboard
created: 2025-10-16
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

---

## 🎯 저녁 체크리스트

### 5분 루틴
1. **On 확인** (1분)
   - 오늘 진전?
   - 내일 다음 행동?

2. **Ongoing 스캔** (2분)
   - 일주일 안 건드린 것?
   - 상태 변화 필요?

3. **흐름 판단** (2분)
   - 전체적으로 건강한가?
   - On이 너무 많지 않나?
   - 막힌 곳은?

---

## 🚦 건강 신호

### 🟢 건강함
- On: 1-2개
- 매일 On 작업
- Ongoing 주 1회 이상 터치
- 명확한 다음 행동

### 🟡 주의
- On: 3개
- On 작업 주 3-4회
- Ongoing 일부 정체
- 다음 행동 모호

### 🔴 문제
- On: 4개 이상
- On 작업 주 1-2회
- Ongoing 대부분 정체
- 다음 행동 불명확

---

## 🔄 주간 회고 (일요일 저녁)

### 질문들
1. **성과**: 이번 주 가장 큰 진전은?
2. **막힘**: 무엇이 나를 막았나?
3. **조정**: 
   - On → 완료/Ongoing/Simmering
   - Ongoing → On/Simmering
   - Simmering → Ongoing/삭제

### 실행
```
- [ ] On 정리 (최대 3개로)
- [ ] Ongoing 상태 업데이트
- [ ] Simmering 재검토
- [ ] 다음 주 On 선택
```

---

## 💡 패턴 인식

### 좋은 흐름
```
On (2개) 
  ↓ 매일 작업
  ↓ 진전 있음
  ↓ 완료
Ongoing으로
  ↓ 숙성
  ↓ 기회 포착
  ↓ On으로 승격
```

### 막힌 흐름
```
On (5개)
  ↓ 분산됨
  ↓ 진전 없음
  ↓ 스트레스
→ 정리 필요!
```

---

## 🎨 시각화 아이디어

### 프로젝트 상태
```
🔥🔥    On (2개)      ← 집중!
♻️♻️♻️♻️ Ongoing (4개) ← 적당
🌱🌱    Simmering (2개) ← 준비
```

### 나이별
```
On:
  - 논문A (7일) ← 빨리 처리
  - 논문B (3일)

Ongoing:
  - 프로젝트C (45일) ← 정체?
  - 프로젝트D (12일)
```

---

## Related
- [[Front/On/README|On 사용법]]
- [[Front/Ongoing/README|Ongoing 관리]]
- [[Balance/주별 멜로디|주간 회고]]
- [[Home|홈으로]]

---

*"매일 5분, 흐름을 보면 길을 잃지 않는다"*
