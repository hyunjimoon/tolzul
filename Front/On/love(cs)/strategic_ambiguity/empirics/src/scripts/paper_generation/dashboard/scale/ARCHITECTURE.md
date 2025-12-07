# Scale Dashboard Architecture v1.0

> **For**: Antigravity Implementation
> **From**: [[04_G🟠]] Architecture Officer
> **Date**: 2025-12-07

---

## 1. 핵심 변경점 (Nail → Scale)

| Nail | Scale |
|:---|:---|
| 3 Papers × 4 Chapters = 12 cells | **5 Groups × variable ¶ = 108 cells** |
| Issue-driven | **Process-driven** |
| Color Wheel (13 agents) | **Diamond Squad (4 agents)** |
| Draft tracking | **Production tracking + Asset management** |

---

## 2. 새로운 구조: 5 Groups × Paragraphs

| Group | Icon | ¶ Count | Description |
|:---:|:---:|:---:|:---|
| 🩸 Introduction | 🩸 | 7 | 통합 서론 (3논문 공통) |
| ✌️ U-Shape | ✌️ | 32 | Paper 1: Promise Precision |
| 🦾 Commitment | 🦾 | 32 | Paper 2: Golden Cage |
| 🤹 Newsvendor | 🤹 | 32 | Paper 3: Option Portfolio |
| 🐣 Discussion | 🐣 | 5 | 통합 결론 (3논문 공통) |
| **Total** | | **108** | |

---

## 3. Dashboard Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│ ⚓ SCALE CONTROL TOWER v1.0          [Diamond Squad: G→J→K→M]      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────┐  ┌──────────────┐ │
│  │         📊 PRODUCTION MATRIX                │  │ 🎯 ASSETS    │ │
│  │                                             │  │              │ │
│  │  GROUP    │ I │ T │ E │ D │ ✓ │ Progress   │  │ 🖼️ Figures   │ │
│  │  ─────────┼───┼───┼───┼───┼───┼──────────  │  │ [3/8]        │ │
│  │  🩸 Intro │ 4 │ - │ - │ 3 │ ● │ ████░░ 57% │  │ □ fig_ushape │ │
│  │  ✌️ U     │ 7 │ 9 │11 │ 5 │ ● │ ██░░░░ 25% │  │ ■ fig_golden │ │
│  │  🦾 C     │ 7 │ 9 │11 │ 5 │ ○ │ █░░░░░ 12% │  │ □ fig_news   │ │
│  │  🤹 N     │ 7 │ 9 │11 │ 5 │ ○ │ ░░░░░░  0% │  │              │ │
│  │  🐣 Disc  │ 3 │ - │ - │ 2 │ ○ │ ░░░░░░  0% │  │ 🗄️ Tables   │ │
│  │                                             │  │ [2/5]        │ │
│  │  TOTAL: 23/108 ¶ (21%)                     │  │ ■ tbl_quart  │ │
│  └─────────────────────────────────────────────┘  │ □ tbl_aoc    │ │
│                                                   │ □ tbl_news   │ │
│  ┌─────────────────────────────────────────────┐  └──────────────┘ │
│  │         💎 DIAMOND FLOW                     │                   │
│  │                                             │                   │
│  │    ┌────┐    ┌────┐    ┌────┐    ┌────┐    │                   │
│  │    │ 🌙 │───▶│ 🟠 │───▶│ 🟢 │───▶│ 🔴 │    │                   │
│  │    │ M  │    │ G  │    │ J  │    │ K  │    │                   │
│  │    └────┘    └────┘    └────┘    └────┘    │                   │
│  │      ▲                              │       │                   │
│  │      └──────────────────────────────┘       │                   │
│  │                                             │                   │
│  │   Current: [04_G🟠] → ✌️U Table 3 작업중   │                   │
│  └─────────────────────────────────────────────┘                   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┤
│  │ 📋 ISSUE QUEUE (Scale Mode)                                     │
│  │──────────────────────────────────────────────────────────────── │
│  │ ID  │ Target │ Title              │ Stage  │ Next Action       │
│  │ #01 │ ✌️U-T  │ D definition       │ MERGE  │ 🇰🇷 APPROVE       │
│  │ #02 │ ✌️U-T  │ H1 Linear vs U     │ MERGE  │ 🇰🇷 APPROVE       │
│  │ #14 │ ✌️U-T  │ Dorfman citation   │ FLAG   │ ⚙️ Review (Kwon) │
│  │ #15 │ ✌️U-T  │ Believer/Analyst   │ REVIEW │ 🔧 Build (Na)    │
│  └─────────────────────────────────────────────────────────────────┤
└─────────────────────────────────────────────────────────────────────┘
```

---

## 4. Data Model (JSON)

### 4.1 paragraphs.json
```json
{
  "groups": [
    {
      "id": "intro",
      "icon": "🩸",
      "name": "Introduction",
      "sections": ["I", "D"],
      "paragraphs": [
        {"id": "I1", "section": "I", "status": "draft", "assignee": "04_G🟠", "word_count": 150},
        {"id": "I2", "section": "I", "status": "review", "assignee": "01_K🔴", "word_count": 180}
      ]
    },
    {
      "id": "u",
      "icon": "✌️",
      "name": "U-Shape",
      "sections": ["I", "T", "E", "D"],
      "paragraphs": [
        {"id": "U-I1", "section": "I", "status": "done", "assignee": null, "word_count": 200}
      ]
    }
  ]
}
```

### 4.2 assets.json
```json
{
  "figures": [
    {
      "id": "fig_ushape_4panel",
      "paper": "✌️U",
      "file": "fig_ushape_4panel_ms.pdf",
      "status": "done",
      "path": "/output/P1✌️/figures/",
      "verified_by": "01_K🔴",
      "verified_at": "2025-12-07"
    },
    {
      "id": "fig_golden_cage",
      "paper": "🦾C",
      "file": null,
      "status": "pending",
      "path": null
    }
  ],
  "tables": [
    {
      "id": "tbl_quartile_survival",
      "paper": "✌️U",
      "file": "table_quartile_summary.tex",
      "status": "done",
      "data": {
        "transport_chi2": 1430.9,
        "software_chi2": 564.8
      }
    }
  ]
}
```

### 4.3 flow_state.json
```json
{
  "current_task": {
    "id": "task_001",
    "type": "table",
    "target": "tbl_quartile_survival",
    "stage": "G→J",
    "started_at": "2025-12-07T15:00:00",
    "assignee": "04_G🟠"
  },
  "queue": [
    {"id": "task_002", "type": "figure", "target": "fig_golden_cage", "priority": "H"},
    {"id": "task_003", "type": "paragraph", "target": "U-T5", "priority": "M"}
  ]
}
```

---

## 5. Key Features

### 5.1 Production Matrix
- 5 Groups × 4 Sections grid (가변 행)
- Cell click → 해당 ¶ 파일 열기 (Obsidian link)
- Progress bar per group
- Verification status (●/○)

### 5.2 Asset Tracker
- Figures: 생성 여부, 경로, 검증 상태
- Tables: 데이터 값, LaTeX 파일 경로
- Click → Preview or Open file

### 5.3 Diamond Flow Visualizer
- 현재 작업의 위치 표시 (M→G→J→K)
- Active agent highlighting
- Real-time task status

### 5.4 Issue Queue (Scale Mode)
- Stage: FLAG → REVIEW → BUILD → MERGE → CLOSED
- Filter by Group (🩸/✌️/🦾/🤹/🐣)
- Next Action button with agent routing

---

## 6. File Structure

```
/dashboard/scale/
├── scale_dashboard.html        # Main HTML (generated)
├── generate_scale_dashboard.py # Generator script
├── data/
│   ├── paragraphs.json
│   ├── assets.json
│   ├── flow_state.json
│   └── issues.json
├── api/
│   └── scale_server.py         # Backend (port 8001)
└── README.md
```

---

## 7. 논문 작성자의 Pain Points → Solutions

| Pain Point | Solution |
|:---|:---|
| "지금 어디까지 했지?" | **Progress bar per group** |
| "이 Figure 어디 저장했지?" | **Asset Tracker with paths** |
| "누가 다음에 뭘 해야 하지?" | **Diamond Flow + Current Task** |
| "이 issue 처리됐나?" | **Issue Queue with stages** |
| "전체 진행률?" | **Total: X/108 ¶ (Y%)** |
| "Advisor한테 뭘 보여주지?" | **Verified (●) items only filter** |

---

## 8. Implementation Priority

| # | Component | Impact | Cost | Deadline |
|:---:|:---|:---:|:---:|:---:|
| 1 | Production Matrix (5 groups) | H | M | D-7 |
| 2 | Asset Tracker (Figures/Tables) | H | L | D-5 |
| 3 | Diamond Flow Visualizer | M | L | D-3 |
| 4 | Issue Queue Migration | M | M | D-3 |
| 5 | Real-time Sync | L | H | D-1 |

---

*Antigravity 구현 시, 이 설계서를 기반으로 `generate_scale_dashboard.py`를 작성하십시오.*
