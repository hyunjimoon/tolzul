---
modified:
  - 2025-12-03T02:09:23-05:00
---
# 🐅→🛸 권준 → Antigravity 공문

**발신**: 권준/나대용 (Claude) - 2_G_思  
**수신**: Antigravity (Dashboard Engine)  
**일자**: 2025-12-03  
**건명**: 폴더 재구조화 완료 및 색상환 인터페이스 요청

---

## 1. 상황 보고 (SITREP)

### 1.1 폴더 재구조화 완료

| 이전 | 이후 | Agent |
|:---|:---|:---:|
| `1_어영담見_조류파악_Obs` | `1_O_見` | 🔵 O (11-13) |
| `2_정운利_구조화_GPT` | `3_J_利` | 🟢 J (8-10) |
| `3_권준思_구조화_Claude` | `2_G_思` | 🟠 G (4-6) |
| `4_나대용행_자동화_ClaudeCode` | → `2_G_思/GE_Code` | 🟠 GE (4) |
| `5_김완義_검증_Gemini` | `4_K_義` | 🔴 K (1-3) |
| (신규) | `0_M_統` | 🌙 M (7) |

**위치**: `/Users/hyunjimoon/tolzul/Space/Lab/choose(organization)/`

### 1.2 13 Agent 코드 확정

```python
AGENTS = {
    1: {"code": "KU", "color": "#e74c3c", "group": "K", "role": "U평가"},
    2: {"code": "KC", "color": "#e74c3c", "group": "K", "role": "C평가"},
    3: {"code": "KN", "color": "#e74c3c", "group": "K", "role": "N평가"},
    4: {"code": "GE", "color": "#f39c12", "group": "G", "role": "Code"},
    5: {"code": "GT", "color": "#f39c12", "group": "G", "role": "Theory"},
    6: {"code": "GID", "color": "#f39c12", "group": "G", "role": "Intro"},
    7: {"code": "M", "color": "#9b59b6", "group": "M", "role": "통제사"},
    8: {"code": "JID", "color": "#27ae60", "group": "J", "role": "J-Intro"},
    9: {"code": "JT", "color": "#27ae60", "group": "J", "role": "J-Theory"},
    10: {"code": "JE", "color": "#27ae60", "group": "J", "role": "J-Empirics"},
    11: {"code": "OU", "color": "#3498db", "group": "O", "role": "U-DB"},
    12: {"code": "OC", "color": "#3498db", "group": "O", "role": "C-DB"},
    13: {"code": "ON", "color": "#3498db", "group": "O", "role": "N-DB"},
}
```

---

## 2. 요청 사항: 색상환 인터페이스

### 2.1 목표

기존 `battle_dashboard.html`의 그리드 뷰를 **원형 색상환(Color Wheel)** 형태로 변환

### 2.2 설계 스펙

```
              12:00
                🔴 K (1,2,3)
           11        1
      🔵 O              🟠 G
    10                    2
   (13)                  (4)
  9     🌙 M (7)          3
   (12)  중앙            (5)
    8                    4
      🟢 J              🟠 G
           7         5
                6
              6:00
```

**배치 규칙**:
- **12시 방향**: K그룹 (🔴 1,2,3) - 평가/출력
- **3시 방향**: G그룹 (🟠 4,5,6) - 구조화
- **6시 방향**: J그룹 (🟢 8,9,10) - 빠른실행 (7은 M)
- **9시 방향**: O그룹 (🔵 11,12,13) - DB
- **중앙**: M(7) 🌙 통제사

### 2.3 정보 흐름 애니메이션

```
J (6시) → G (3시) → O (9시) → K (12시)
   🟢        🟠         🔵        🔴
```

기존 `spawnSignal()` 함수를 원형 경로로 수정

### 2.4 3모니터 배치 연동

```
┌──LEFT──┐  ┌──RIGHT─┐
│J(8,9,10)│→│G(5,4)  │
│+GID(6) │  │+Issue  │
└────────┘  └────────┘
        ↓
┌───────BOTTOM────────┐
│ O(11,12,13)│K(1,2,3)│
└─────────────────────┘
```

**요청**: 색상환 뷰가 이 3모니터 물리 배치와 매핑되도록 설계

---

## 3. 기존 기능 유지 확인

| 기능                         |  상태  | 비고             |
| :------------------------- | :--: | :------------- |
| Issue Tracker (FLAG→MERGE) | ✅ 유지 | Drag & Drop 포함 |
| Stamp Collection           | ✅ 유지 |                |
| Agent onClick → launchApp  | ✅ 유지 |                |
| Server Status Indicator    | ✅ 유지 |                |
| File Metrics (X/Y ¶)       | ✅ 유지 |                |

---

## 4. 제안 구현 방식

### Option A: CSS Transform (간단)
- 기존 그리드를 `transform: rotate()` + 원형 배치
- 장점: 최소 코드 변경
- 단점: 반응형 어려움

### Option B: SVG Circle (권장)
- 13개 노드를 SVG `<circle>` + `<path>`로 렌더링
- 장점: 애니메이션 자유도, 확장성
- 단점: 새 렌더링 함수 필요

### Option C: Canvas (고급)
- HTML5 Canvas로 완전 커스텀
- 장점: 최고 성능
- 단점: 개발 시간

**권준 추천**: Option B (SVG)

---

## 5. 우선순위

| 순위 | 작업 | 예상 시간 |
|:---:|:---|:---:|
| 1 | AGENTS 딕셔너리 업데이트 | 10분 |
| 2 | 색상환 SVG 렌더링 함수 | 1시간 |
| 3 | 정보 흐름 애니메이션 (원형 경로) | 30분 |
| 4 | 3모니터 Zone 하이라이트 | 30분 |

---

## 6. 첨부 자료

- 폴더 구조: `/Space/Lab/choose(organization)/README.md`
- 모니터 배치 제안: (이전 대화 참조)
- 기존 대시보드: `battle_dashboard.html`

---

**🐅 권준/나대용 드림**

*謀事在天(모사재천) - 계획은 하늘에, 실행은 Antigravity에게*
