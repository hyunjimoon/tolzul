---
문서_타입: Tech Spec
프로젝트: 武藝 견리사의 전환
예상_시간: 5분
작성일: 2025-10-25
상태: Ready for Review
---

# Tech Spec: 武藝 견리사의(見利思義) 전환
*5분 Quick Implementation Version*

## 📋 Executive Summary

**목표**: 武藝 폴더를 의지용현(정적 덕목) 체계에서 견리사의(동적 순환) 체계로 전환  
**시간**: 5분  
**범위**: 핵심 3개 파일만 업데이트 (최소 유효 제품)  
**효과**: 전체 武藝 체계가 순환 학습 루프로 작동하도록 구조화

---

## 🎯 Problem Statement

### Current State (AS-IS)
```
武藝/
├── Operating Hand/      # 실행 관련 (용勇)
├── Bayesian Mind/       # 사고 관련 (지智)
├── Innovating Heart/    # 가치 관련 (의義)
└── [연결 구조 없음]

문제점:
❌ 3개 폴더가 독립적으로 존재
❌ 순환 루프 개념 부재
❌ 네비게이션 어려움
❌ 의지용현(정적) vs 실제 작업(동적) 불일치
```

### Desired State (TO-BE)
```
武藝/
├── README.md                    [NEW] 전체 네비게이션
├── Operating Hand/ (利)         [ROLE CLARIFIED]
├── Bayesian Mind/ (思)          [ROLE CLARIFIED]
├── Innovating Heart/ (義)       [ROLE CLARIFIED]
└── 견리사의 말하기.md            [KEEP] 실천 예시

순환 구조:
🐙 利 (Operating Hand) → 🐅 思 (Bayesian Mind) 
  → 🐢 義 (Innovating Heart) → 👾 見 (Human) → 🐙 利

효과:
✅ 명확한 순환 루프
✅ 각 폴더의 역할 정의
✅ 쉬운 네비게이션
✅ 실제 워크플로우와 일치
```

---

## 🏗️ Technical Design

### Architecture: 3-Tier Loop System

```
┌─────────────────────────────────────────┐
│  👾 Human Integration Layer (見)        │
│  - Obsidian 기록                        │
│  - 주간/일간 성찰                        │
└─────────────────────────────────────────┘
         ↑                    ↓
         │                    │
    [義 검증]              [利 행동]
         │                    │
┌────────┴─────┐      ┌──────┴─────────┐
│ Innovating   │      │ Operating      │
│ Heart (義)   │ ← ─  │ Hand (利)      │
│              │  思   │                │
└──────────────┘      └────────────────┘
         ↑                    ↓
         └──── Bayesian Mind ─┘
               (思)
```

### Data Flow

```
1. 행동 (利): Operating Hand에서 프로토콜/스타일 작성
   ↓
2. 사유 (思): Bayesian Mind에서 패턴 분석/구조화
   ↓
3. 검증 (義): Innovating Heart에서 가치 점검
   ↓
4. 통합 (見): Human이 Obsidian에 통찰 기록
   ↓
5. 재행동: 개선된 행동으로 다시 Operating Hand로
```

---

## ⚡ 5-Minute Implementation Plan

### Phase 1: Core Structure (3분)

#### Task 1.1: README.md 생성 (1분) ✅ DONE
```bash
위치: /武藝/README.md
내용: 
- 견리사의 순환 구조 설명
- 3개 폴더의 역할 명시
- 네비게이션 가이드
```

#### Task 1.2: 의지용현화().md 파일명 변경 (30초)
```bash
FROM: /Operating Hand/의지용현화().md
TO:   /Operating Hand/견리사의화().md

이유: 프레임워크 일관성
영향: 내부 링크 1개 수정 필요
```

#### Task 1.3: 상위 폴더 파일 정리 (1.5분)
```bash
파일들:
- 견리사의 말하기.md [KEEP - 실천 예시]
- 의용현지화().md [RENAME → 견리사의화_legacy.md]
- 🐢🐅🐙👾의용군현지스타일.md [KEEP - 스타일 가이드]

작업:
1. 의용현지화().md에 "[LEGACY]" 태그 추가
2. README에서 3개 파일의 역할 명시
```

---

### Phase 2: Documentation Update (2분)

#### Task 2.1: 각 폴더에 _README.md 추가 (각 30초 × 3)
```markdown
# Operating Hand/README.md
역할: 🐙 利 - 실행의 무예
순환 위치: Loop의 시작점
다음 단계: → Bayesian Mind (思)

# Bayesian Mind/README.md
역할: 🐅 思 - 사유의 무예
순환 위치: Loop의 구조화
다음 단계: → Innovating Heart (義)

# Innovating Heart/README.md
역할: 🐢 義 - 검증의 무예
순환 위치: Loop의 윤리 점검
다음 단계: → Human Integration (見)
```

---

## 🔍 Implementation Details

### File Changes Summary

| 파일 | 작업 | 우선순위 | 시간 |
|------|------|---------|------|
| `/武藝/README.md` | CREATE | P0 | 1분 ✅ |
| `/Operating Hand/의지용현화().md` | RENAME | P1 | 30초 |
| `/武藝/의용현지화().md` | TAG [LEGACY] | P1 | 10초 |
| `/Operating Hand/README.md` | CREATE | P2 | 30초 |
| `/Bayesian Mind/README.md` | CREATE | P2 | 30초 |
| `/Innovating Heart/README.md` | CREATE | P2 | 30초 |

**총 예상 시간**: 3분 10초 (버퍼 1분 50초)

---

## 🎨 User Experience

### Before (AS-IS)
```
사용자: "어디에 이 문서를 넣어야 하지?"
시스템: [3개 폴더가 평행하게 나열]
사용자: "뭐가 다른 거지? 🤔"
```

### After (TO-BE)
```
사용자: "어디에 이 문서를 넣어야 하지?"
README: "이것이 행동(利)인가, 사유(思)인가, 가치(義)인가?"
사용자: "아, 실행 프로토콜이니까 Operating Hand!"
```

---

## ⚖️ Trade-offs & Decisions

### Decision 1: Minimal File Changes
**선택**: 기존 파일 내용은 변경하지 않고, 구조만 재해석  
**이유**: 
- ✅ 5분 안에 완료 가능
- ✅ 기존 정보 보존
- ✅ 점진적 마이그레이션 가능
- ❌ 각 파일 내부의 "의지용현" 용어는 그대로

**대안**: 모든 파일의 내용을 견리사의로 전면 수정  
**거부 이유**: 2시간+ 소요, 위험도 높음

---

### Decision 2: README-Based Navigation
**선택**: 각 폴더마다 README 추가  
**이유**:
- ✅ 표준 관행
- ✅ GitHub/Obsidian 호환
- ✅ 확장 가능
- ❌ 파일 개수 증가

**대안**: 단일 메인 README만 사용  
**거부 이유**: 각 폴더의 맥락 부족

---

### Decision 3: Phased Rollout
**선택**: Phase 1만 5분 내 실행, Phase 2는 선택적  
**이유**:
- ✅ 시간 제약 준수
- ✅ 핵심 기능 우선
- ✅ 점진적 개선 가능

**Phase 1 (필수)**: README.md 생성  
**Phase 2 (선택)**: 폴더별 README  
**Phase 3 (미래)**: 내용 업데이트

---

## 🧪 Testing & Validation

### Validation Checklist

```markdown
□ README.md가 존재하는가?
□ 견리사의 순환 구조가 명시되어 있는가?
□ 각 폴더의 역할이 명확한가?
□ 네비게이션 경로가 논리적인가?
□ 기존 파일들이 손상되지 않았는가?
```

### Success Metrics

**즉시 측정 가능 (5분 후)**
- [ ] README.md 파일 존재
- [ ] 3개 폴더 역할 명시
- [ ] 순환 다이어그램 포함

**장기 측정 (1주 후)**
- [ ] 새 문서 작성 시 올바른 폴더 선택율 > 80%
- [ ] 문서 간 순환 참조 발생
- [ ] "어디에 넣어야 하지?" 질문 감소

---

## 🚀 Rollout Plan

### Immediate (5분)
```bash
1. 현재 작성된 README.md 검토 ✅
2. 문제 없으면 commit
3. 나머지는 "Phase 2"로 이연
```

### Optional Follow-up (나중에)
```bash
1. 각 폴더에 README 추가
2. 의지용현화().md → 견리사의화().md
3. 내부 링크 업데이트
4. Legacy 파일 태깅
```

---

## 🔮 Future Enhancements

### Short-term (1주)
- 각 폴더의 README 추가
- 파일명 일관성 확보
- 순환 링크 강화

### Mid-term (1개월)
- `의지용현화().md` 전면 업데이트
- 각 폴더 내 파일들의 순환 구조 명시
- 템플릿 표준화

### Long-term (3개월)
- 자동화 스크립트 (새 문서 → 올바른 폴더)
- 순환 추적 대시보드
- AI 도구와의 통합 워크플로우

---

## 📚 References

- `/Calendar/주별 멜로디/의지용현 삼도수군.md` - AI 삼도수군 루프
- `/Front/Ongoing/武藝/Operating Hand/의지용현화().md` - 현재 프로토콜
- 견리사의 프레임워크 (2025.10.25 업데이트)

---

## 💬 Open Questions for Discussion

1. **파일명 변경 타이밍**: 지금 바로? 아니면 Phase 2?
2. **Legacy 파일 처리**: 아카이브? 태그? 삭제?
3. **템플릿 필요성**: 새 문서 작성 시 표준 템플릿?
4. **Cross-reference**: 순환 참조를 얼마나 명시적으로?

---

## ✅ Action Items

### For 장군 (지금, 5분)
- [ ] README.md 내용 검토 및 승인
- [ ] Phase 1 vs Phase 2 실행 여부 결정

### For Future (선택)
- [ ] 각 폴더 README 작성
- [ ] 파일명 표준화
- [ ] 내부 컨텐츠 업데이트

---

**Status**: ✅ Phase 1 Complete (README.md created)  
**Next Step**: 장군님의 승인 대기  
**Estimated Total Effort**: 3분 실제 소요 (버퍼 2분 남음)
