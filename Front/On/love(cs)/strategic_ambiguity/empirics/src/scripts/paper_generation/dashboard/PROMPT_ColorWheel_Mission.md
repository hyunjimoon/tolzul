# 🛸 Antigravity Mission Brief: Color Wheel Interface

---

## WHY (목적)

현재 `battle_dashboard.html`의 그리드 뷰는 **정보 흐름(J→G→O→K)**을 직관적으로 보여주지 못함.

**목표**: Obsidian Local Graph를 **보완**하는 **색상환 기반 실시간 협업 시각화**
- Obsidian Graph = 정적 링크 관계
- MFS Color Wheel = **동적 생산 흐름 + Agent 상태**

---

## WHAT (무엇을)

### 핵심 시각화 요소

```
              12:00 🔴 K (평가)
                  1,2,3
           11              1
     🔵 O                      🟠 G
   (DB)  10      🌙 M(7)        2  (구조)
          9      통제사          3
           8                4
              🟢 J (실행)
                 6:00
```

| 위치 | Agent | 역할 |
|:---:|:---:|:---|
| 12시 | K (1,2,3) | 🔴 평가/출력 |
| 3시 | G (4,5,6) | 🟠 구조화 |
| 6시 | J (8,9,10) | 🟢 빠른실행 |
| 9시 | O (11,12,13) | 🔵 DB |
| 중앙 | M (7) | 🌙 통제사 |

### 정보 흐름 애니메이션
```
J(6시) → G(3시) → O(9시) → K(12시) → M(중앙)
  🟢        🟠        🔵        🔴       🌙
```

---

## HOW (어떻게)

### 기술 스택
- **SVG** 기반 원형 렌더링 (Option B 채택)
- 기존 CSS Variables 유지 (`--jeong-green`, `--na-orange`, etc.)
- `spawnSignal()` → 원형 경로로 수정

### 유지할 기능 ✅
| 기능 | 상태 |
|:---|:---:|
| **Issue Tracker** (FLAG→MERGE) | ✅ 유지 |
| **Stamp Collection** (도장) | ✅ 유지 |
| Agent onClick → launchApp | ✅ 유지 |
| File Metrics (X/Y ¶) | ✅ 유지 |

### 신규 기능
1. **Agent 노드 클릭** → 해당 Agent 담당 파일 목록
2. **Product 필터** (U/C/N) → 색상환 내 해당 라인만 하이라이트
3. **3모니터 Zone 매핑** 표시

---

## WHAT IF (확장/예외)

### 확장 가능성
- [ ] Agent별 진행률 (arc length로 표현)
- [ ] Rally Point 통과 시 불꽃 애니메이션
- [ ] Obsidian 연동 (Deep Link로 파일 열기)

### 예외 처리
- Agent 비활성 시 → 회색 처리 + opacity 0.3
- Issue 0건 시 → "All Clear 🎉" 메시지
- 서버 오프라인 → 색상환 전체 dim + 경고

---

## 📎 참고 자료

- 폴더 구조: `/Space/Lab/choose(organization)/README.md`
- Agent 코드: `BRIEFING_ColorWheel_Request.md`
- 기존 대시보드: `battle_dashboard.html`

---

**🛸 Antigravity, 전례 없는 색상환 인터페이스를 구축하라.**

*필사즉생 - 12척으로 133척을 이기듯, 13 Agent로 3논문을 완성한다*
