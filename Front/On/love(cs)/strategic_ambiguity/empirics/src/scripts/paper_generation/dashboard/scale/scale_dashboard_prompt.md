# 🚀 Scale Dashboard 구현 프롬프트 (Antigravity용)

## 📋 Mission Brief

PhD thesis "The Promise Vendor" 프로젝트의 **4일 강행군 (Dec 9-12)** 진행 상황을 실시간 추적하는 **Scale Dashboard**를 구현해주세요.

---

## 🎯 Dashboard 목적

1. **3 Papers 병렬 진행 상황** 실시간 모니터링
2. **Bottleneck 해소 여부** 시각적 확인
3. **Gatekeeper (K🔴) 승인/반려** 상태 추적
4. **Rally Point 진행률** 표시

---

## 📊 Required Components

### 1. Header Section

```
┌─────────────────────────────────────────────────────────────────┐
│  🏴 4차 전투: 수습(收拾) — Scale Phase                            │
│  Period: Dec 9-12, 2025 (4 Days)                                │
│  Current: Day [X] of 4 | [HH:MM] remaining                      │
│  Motto: "Prove It or Kill It"                                   │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Paper Status Cards (3개 병렬)

각 Paper에 대해 카드 형태로 표시:

```
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│  ✌️ Paper U       │  │  🦾 Paper C       │  │  🤹 Paper N       │
│  E&I Target       │  │  Strategy Target  │  │  OM Target        │
├──────────────────┤  ├──────────────────┤  ├──────────────────┤
│  Progress: 75%    │  │  Progress: 70%    │  │  Progress: 55%    │
│  ████████░░       │  │  ███████░░░       │  │  █████░░░░░       │
├──────────────────┤  ├──────────────────┤  ├──────────────────┤
│  Bottleneck:      │  │  Bottleneck:      │  │  Bottleneck:      │
│  🔴 Bolton 연결    │  │  🔴 Nanda 포지셔닝 │  │  🔴 CR Calibration│
│  🟡 Contribution  │  │  🟡 AOC 수식화     │  │  🔴 U,C 연결      │
├──────────────────┤  ├──────────────────┤  ├──────────────────┤
│  Key Metric:      │  │  Key Metric:      │  │  Key Metric:      │
│  χ²=1430.9***     │  │  ρ=0.159***       │  │  k* fit: TBD      │
│  ✅ Verified      │  │  ✅ Verified      │  │  ⚠️ Pending       │
└──────────────────┘  └──────────────────┘  └──────────────────┘
```

### 3. Daily Timeline (Gantt-style)

```
       │ D1 (Dec 9)  │ D2 (Dec 10) │ D3 (Dec 11) │ D4 (Dec 12) │
───────┼─────────────┼─────────────┼─────────────┼─────────────┤
✌️U    │ ████ Bolton │ ████ Draft  │ ██ Review   │ █ Final     │
🦾C    │ ████ Nanda  │ ████ Draft  │ ██ Review   │ █ Final     │
🤹N    │ ████ CR Cal │ ████ Draft  │ ██ Review   │ █ Final     │
Ch5    │             │             │ ████ Integ  │ ██ Final    │
───────┼─────────────┼─────────────┼─────────────┼─────────────┤
Gate   │ K🔴 Check   │ K🔴 Check   │ M RP4       │ M RP5       │
```

### 4. Bottleneck Resolution Tracker

| Paper | Bottleneck | Priority | Status | Owner | Due |
|:---:|:---|:---:|:---:|:---:|:---:|
| ✌️U | Bolton s₂↔V 매핑 | 🔴 | ⬜ Pending | G🟠 | D1 PM |
| ✌️U | Hook 서사 강화 | 🔴 | ⬜ Pending | G🟠 | D2 AM |
| ✌️U | Contribution 명시 | 🟡 | ⬜ Pending | G🟠 | D2 PM |
| 🦾C | Nanda 포지셔닝 | 🔴 | ⬜ Pending | G🟠 | D1 PM |
| 🦾C | AOC 수식화 | 🔴 | ⬜ Pending | G🟠 | D1 PM |
| 🦾C | H3 해석 강화 | 🟡 | ⬜ Pending | G🟠 | D2 PM |
| 🤹N | CR Calibration | 🔴 | ⬜ Pending | J🟢 | D1 PM |
| 🤹N | U,C 연결 시각화 | 🔴 | ⬜ Pending | G🟠 | D2 AM |
| 🤹N | Murky Middle Fig | 🟡 | ⬜ Pending | G🟠 | D1 PM |

**Status Icons:** ⬜ Pending → 🔄 In Progress → ✅ Done → 🚨 Blocked

### 5. Rally Point Progress

```
RP3 (QA)        RP4 (Integration)    RP5 (Submit)
[██████░░░░]    [░░░░░░░░░░]        [░░░░░░░░░░]
   60%              0%                  0%
Gate: K🔴        Gate: M              Gate: M
```

### 6. Gatekeeper Panel

```
┌─────────────────────────────────────────────────────────────────┐
│  🔴 K (Gatekeeper) — Latest Decisions                           │
├─────────────────────────────────────────────────────────────────┤
│  [Timestamp] ✌️U Section 3: 🇰🇷 승인 — χ² verified              │
│  [Timestamp] 🦾C H1-H3: 🇰🇷 승인 — ρ values confirmed           │
│  [Timestamp] 🤹N CR Cal: 🚨 반려 — Data source unclear           │
└─────────────────────────────────────────────────────────────────┘
```

### 7. Key Metrics Panel

| Metric | Paper | Target | Current | Status |
|:---|:---:|:---|:---|:---:|
| χ² (Transportation) | ✌️U | >300*** | 1430.9*** | ✅ |
| χ² (Software) | ✌️U | >300*** | 564.8*** | ✅ |
| χ² (Hardware) | ✌️U | >300*** | 398.6*** | ✅ |
| χ² (Pharma) | ✌️U | >300*** | 305.7*** | ✅ |
| ρ(Y, \|ΔV\|) | 🦾C | >+0.15*** | +0.159*** | ✅ |
| Flexibility Gap | 🦾C | >2.5x | 2.7x | ✅ |
| CR_AV | 🤹N | ~0.9 | TBD | ⚠️ |
| CR_Fleet | 🤹N | ~0.3 | TBD | ⚠️ |
| k* fit | 🤹N | >90% | TBD | ⚠️ |

### 8. Signal Log

실시간 의사결정 신호 로그:

```
[Dec 9 09:30] 🟢 Normal — G🟠 시작: U Section 2 Bolton 연결
[Dec 9 11:45] 🟡 Important — J🟢 발견: CR 데이터 Scott (2019) 활용 가능
[Dec 9 14:20] 🔴 Critical — K🔴 요청: N CR Calibration 재검토
[Dec 9 16:00] 😆 돌파 — G🟠 완료: Bolton s₂↔V 매핑 정리
```

---

## 🎨 Design Specifications

### Color Scheme

| Element | Color | Hex |
|:---|:---|:---|
| Background | Dark Navy | #1a1a2e |
| Card Background | Dark Gray | #16213e |
| Primary Accent | Gold | #f4d03f |
| Success | Green | #27ae60 |
| Warning | Orange | #f39c12 |
| Critical | Red | #e74c3c |
| Text Primary | White | #ffffff |
| Text Secondary | Light Gray | #a0a0a0 |

### Typography

- Header: Bold Sans-serif, 24px
- Card Title: Bold, 18px
- Body: Regular, 14px
- Metrics: Monospace, 16px

### Layout

- Responsive grid (3 columns for paper cards)
- Sticky header with countdown timer
- Collapsible sections for detailed views
- Dark mode default (night work optimization)

---

## 🔧 Technical Requirements

### Data Sources

```javascript
const dataFiles = {
  paperU: '/output/✌️U/',
  paperC: '/output/🦾C/',
  paperN: '/output/🤹N/',
  bulletin: '/output/📢BULLETIN.md',
  registry: '/output/🗄️REGISTRY.md'
};
```

### State Management

```javascript
const dashboardState = {
  currentDay: 1, // 1-4
  papers: {
    U: { progress: 75, bottlenecks: [...], metrics: {...} },
    C: { progress: 70, bottlenecks: [...], metrics: {...} },
    N: { progress: 55, bottlenecks: [...], metrics: {...} }
  },
  rallyPoints: {
    RP3: { progress: 60, gate: 'K🔴', status: 'in_progress' },
    RP4: { progress: 0, gate: 'M', status: 'pending' },
    RP5: { progress: 0, gate: 'M', status: 'pending' }
  },
  signals: [...],
  gatekeeperDecisions: [...]
};
```

### Update Mechanism

- Manual update via JSON file edit
- Auto-refresh every 5 minutes
- Manual refresh button

---

## 📁 Output Location

```
.../dashboard/scale/
├── scale_dashboard.html      ← Main dashboard
├── dashboard_state.json      ← State file (editable)
├── style.css                 ← Styles
└── dashboard.js              ← Logic
```

---

## 🎯 Priority Features

1. **Must Have:**
   - 3 Paper status cards
   - Bottleneck tracker table
   - Day indicator + countdown
   - Gatekeeper decision log

2. **Should Have:**
   - Timeline Gantt view
   - Rally Point progress bars
   - Key metrics panel

3. **Nice to Have:**
   - Signal log with timestamps
   - Animation on status change
   - Export to PDF for reporting

---

## 📝 Sample JSON State

```json
{
  "meta": {
    "battle": "4차 전투",
    "codename": "수습(收拾)",
    "startDate": "2025-12-09",
    "endDate": "2025-12-12",
    "currentDay": 1
  },
  "papers": {
    "U": {
      "name": "Paper U: Vague Promise",
      "target": "E&I (MS)",
      "progress": 75,
      "keyMetric": {
        "name": "χ² (Transportation)",
        "target": ">300***",
        "current": "1430.9***",
        "verified": true
      },
      "bottlenecks": [
        { "id": "U1", "desc": "Bolton s₂↔V 매핑", "priority": "critical", "status": "pending", "owner": "G🟠", "due": "D1 PM" },
        { "id": "U2", "desc": "Hook 서사 강화", "priority": "critical", "status": "pending", "owner": "G🟠", "due": "D2 AM" },
        { "id": "U3", "desc": "Contribution 명시", "priority": "important", "status": "pending", "owner": "G🟠", "due": "D2 PM" }
      ],
      "sections": {
        "S1": { "name": "Introduction", "status": "draft", "progress": 70 },
        "S2": { "name": "Theory", "status": "draft", "progress": 60 },
        "S3": { "name": "Empirics", "status": "verified", "progress": 100 },
        "S4": { "name": "Discussion", "status": "draft", "progress": 50 }
      }
    },
    "C": {
      "name": "Paper C: Commitment Trap",
      "target": "Strategy (SMJ/MS)",
      "progress": 70,
      "keyMetric": {
        "name": "ρ(Y, |ΔV|)",
        "target": ">+0.15***",
        "current": "+0.159***",
        "verified": true
      },
      "bottlenecks": [
        { "id": "C1", "desc": "Nanda 포지셔닝", "priority": "critical", "status": "pending", "owner": "G🟠", "due": "D1 PM" },
        { "id": "C2", "desc": "AOC 수식화", "priority": "critical", "status": "pending", "owner": "G🟠", "due": "D1 PM" },
        { "id": "C3", "desc": "H3 해석 강화", "priority": "important", "status": "pending", "owner": "G🟠", "due": "D2 PM" }
      ],
      "sections": {
        "S1": { "name": "Introduction", "status": "draft", "progress": 60 },
        "S2": { "name": "Theory", "status": "draft", "progress": 65 },
        "S3": { "name": "Empirics", "status": "verified", "progress": 100 },
        "S4": { "name": "Discussion", "status": "draft", "progress": 50 }
      }
    },
    "N": {
      "name": "Paper N: Promise Vendor",
      "target": "OM (M&SOM)",
      "progress": 55,
      "keyMetric": {
        "name": "k* fit",
        "target": ">90%",
        "current": "TBD",
        "verified": false
      },
      "bottlenecks": [
        { "id": "N1", "desc": "CR Calibration", "priority": "critical", "status": "pending", "owner": "J🟢", "due": "D1 PM" },
        { "id": "N2", "desc": "U,C 연결 시각화", "priority": "critical", "status": "pending", "owner": "G🟠", "due": "D2 AM" },
        { "id": "N3", "desc": "Murky Middle Fig", "priority": "important", "status": "pending", "owner": "G🟠", "due": "D1 PM" }
      ],
      "sections": {
        "S1": { "name": "Introduction", "status": "draft", "progress": 70 },
        "S2": { "name": "Theory", "status": "complete", "progress": 90 },
        "S3": { "name": "Calibration", "status": "weak", "progress": 30 },
        "S4": { "name": "Discussion", "status": "draft", "progress": 40 }
      }
    }
  },
  "rallyPoints": {
    "RP3": { "name": "QA & Stress Test", "gate": "K🔴", "progress": 60, "status": "in_progress" },
    "RP4": { "name": "Integration", "gate": "M", "progress": 0, "status": "pending" },
    "RP5": { "name": "Submit", "gate": "M", "progress": 0, "status": "pending" }
  },
  "signals": [
    { "timestamp": "2025-12-09T09:00:00", "level": "normal", "message": "4차 전투 개시" }
  ],
  "gatekeeperDecisions": [
    { "timestamp": "2025-12-08T22:30:00", "paper": "U", "section": "S3", "decision": "approved", "note": "χ² verified" },
    { "timestamp": "2025-12-08T22:30:00", "paper": "C", "section": "S3", "decision": "approved", "note": "ρ values confirmed" }
  ]
}
```

---

## ✅ Acceptance Criteria

1. [ ] 3 Paper cards가 병렬로 표시됨
2. [ ] Bottleneck 상태가 실시간 반영됨
3. [ ] Day countdown이 정확히 동작함
4. [ ] Gatekeeper 결정 로그가 표시됨
5. [ ] Rally Point 진행률이 시각화됨
6. [ ] JSON 파일 수정으로 상태 업데이트 가능
7. [ ] Dark mode로 가독성 확보

---

*필사즉생 — Dashboard로 전장을 장악하라*
