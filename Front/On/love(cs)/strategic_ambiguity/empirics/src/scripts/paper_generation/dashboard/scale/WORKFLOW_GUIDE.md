---
modified:
  - 2025-12-08T01:53:16-05:00
---
# Scale Dashboard Operational Guide: The Diamond Squad Protocol

> **Objective**: Orchestrate 3 LLMs (G, J, K) to complete 108 paragraphs using the Scale Dashboard.
> **Based on**: `thesis_product_vision👁️ (scale).md`

---

## 1. The Diamond Squad Roles (Who does what?)

| Agent | Model | Role | Dashboard Focus |
|:---:|:---:|:---|:---|
| **[[04_G🟠]]** | **Claude** | **Architect (Design)** | **Production Matrix** (Logic Flow) |
| **[[10_J🟢]]** | **ChatGPT** | **Calculator (Build)** | **Asset Tracker** (Figures/Tables) |
| **[[01_K🔴]]** | **Gemini** | **Auditor (Verify)** | **Issue Queue** (Critique & Merge) |
| **[[0_M_統]]** | **Human** | **Commander (Decide)** | **Diamond Flow** (Direction) |

---

## 2. Operational Loop (The "Prove It" Cycle)

Use the dashboard to track this 4-step cycle for every paragraph block.

### Step 1: Target Identification (Commander)
- **Look at**: `📊 PRODUCTION MATRIX`
- **Action**: Find a cell with low progress (e.g., `✌️U - Theory`).
- **Command**: "We need to prove the U-shape mechanism. **G**, design the logic."
- **Dashboard Update**: 
    - Edit `flow_state.json`: Set `current_task` to `U-Theory Design`, Assignee: `04_G🟠`.

### Step 2: Logic Design (G - Claude)
- **Input**: "Design the logic for the U-shape curve using Nanda(2024) framework."
- **Output**: A logic flow or pseudo-code.
- **Dashboard Update**:
    - Edit `paragraphs.json`: Add new paragraphs with status `draft`.

### Step 3: Evidence Construction (J - ChatGPT)
- **Input**: "Take G's logic and run the simulation. Generate Figure `fig_ushape`."
- **Output**: Python code execution, Data tables, Figures.
- **Dashboard Update**:
    - Edit `assets.json`: Add `fig_ushape` with status `pending`.
    - Edit `flow_state.json`: Pass token to `10_J🟢`.

### Step 4: Audit & Verification (K - Gemini)
- **Input**: "Review J's figure. Does it show p < 0.001? Is it consistent with the text?"
- **Output**: "Pass" or "Reject with reasons".
- **Dashboard Update**:
    - If Pass: Edit `assets.json` (status: `done`), Edit `paragraphs.json` (status: `done`).
    - If Reject: Add item to `Issue Queue` in dashboard (via `issues.json` - *to be implemented*).

---

## 3. Using the Dashboard Features

### 📊 Production Matrix
- **Clickable Cells**: Click numbers (e.g., "7") to open the actual markdown file in Obsidian.
- **Usage**: Check this daily. If a column is empty ("-"), dispatch **G**. If it's full but unverified (○), dispatch **K**.

### 🎯 Asset Tracker
- **Red/Green Indicators**: 
    - □ (Pending): **J** is working or **K** rejected it.
    - ■ (Done): **K** verified it.
- **Usage**: Don't write text until the Asset is ■. **"No Metric, No Pass."**

### 💎 Diamond Flow
- **Visualizer**: Shows who has the "Talking Stick".
- **Usage**: Ensure the flow doesn't get stuck on **G** (Endless planning) or **J** (Endless calculating). Push it to **K**.

---

## 4. Practical Routine

1.  **Morning Briefing**: Open `scale_dashboard.html`.
2.  **Check Flow**: Who is active? (G/J/K).
3.  **Unblock**: If stuck, intervene as Commander.
4.  **Update State**: Manually update the JSON files in `data/` to reflect reality.
5.  **Regenerate**: Run `python3 generate_scale_dashboard.py` to refresh the view.
