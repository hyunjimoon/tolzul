# 🛸 MFS View Architecture Summary for Claude

To assist in designing the **Prismatic Interface**, here are the two most critical files that currently power the `mfs_view` (Battle Dashboard).

## 1. The Architect: `visualize_spaceship.py`
**Role:** Static Site Generator & Frontend Logic
**Location:** `.../dashboard/visualize_spaceship.py`

This script generates the `battle_dashboard.html`. It contains the entire **HTML structure, CSS styling, and JavaScript logic**.

*   **Key Data Structures:**
    *   `jeong_agents`, `na_agents`, `kim_agents`: Defines the 13 deputies (Name, Role, Icon, OnClick).
    *   `papers`: Defines the 3 papers (U, C, N) and their chapters.
*   **Key Functions:**
    *   `generate_matrix_row()`: Renders the 4x3 grid (Intro/Theory/Empirics/Discuss) with metrics (`X/Y ¶`) and issue flags.
    *   `generate_agent_html()`: Renders the agent cards.
    *   `generate_issue_queue_html()`: Renders the issue tracker table.
    *   `generate_stamp_panel_html()`: Renders the new Stamp Collection.
*   **Frontend Tech:**
    *   **CSS**: Glassmorphism, Grid/Flexbox, CSS Variables for "Jeong Green", "Tiger Orange", "Kim Red".
    *   **JS**: `updateIssue()` (fetch), `launchApp()` (fetch), `spawnSignal()` (animation).

## 2. The Engine: `tolzul_link.py`
**Role:** Backend Server & System Bridge
**Location:** `.../dashboard/tolzul_link.py`

This script serves the dashboard and handles **interactive requests** from the frontend.

*   **Server:** `SimpleHTTPRequestHandler` on port 8000.
*   **API Endpoints:**
    *   `POST /update_issue`: Updates `issue_queue.json` (Advance stage, Close issue).
    *   `POST /launch`: Executes system commands (e.g., `open -a "Claude"`) to launch apps.
*   **Data Management:**
    *   Reads/Writes to `issue_queue.json`.

---

**Current Workflow:**
1.  User runs `python3 tolzul_link.py`.
2.  `visualize_spaceship.py` is run (manually or via script) to regenerate `battle_dashboard.html` when data changes.
3.  Browser loads `http://localhost:8000/`.
4.  User clicks Agent -> JS calls `/launch` -> Python runs `open -a`.
