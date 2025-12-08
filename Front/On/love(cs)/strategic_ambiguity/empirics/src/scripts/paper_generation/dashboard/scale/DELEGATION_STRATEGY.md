# Diamond Squad Delegation Strategy: Papers U, C, N

> **Objective**: Efficiently delegate the 108-paragraph development of Papers U, C, and N to J, G, and K squads.
> **Context**: Based on file identity definitions (`toc` vs `1-pager`) and the Diamond Squad Protocol.

---

## 1. File Identity & Agent Alignment

Based on your directive and the provided screenshot:

| Document Type | File Pattern | Purpose | Primary Owner | Audience |
|:---|:---|:---|:---|:---|
| **Blueprint** | `toc(u/c/n).md` | **32¶ Detailed Scaffold**<br>(Formulas, Logic, Code Specs) | **🟠 G-Squad**<br>(Architect) | G (Self), K (Audit) |
| **Vision** | `U✌️/C🦾/N🤹.md` | **Core Message 1-Pager**<br>(Metaphors, Impact, Narrative) | **🟢 J-Squad**<br>(Execution) | J, K, External |
| **Process Eval** | `eval(⚙️chap1234).md` | **Methodology Retrospective**<br>(Lessons, "How-To", Logic) | **🟠 G-Squad**<br>(Engineer) | All Squads |
| **Theory Eval** | `eval(📝chap1234).md` | **Consistency Audit**<br>(Hypothesis, Concepts, Logic) | **🔴 K-Squad**<br>(Auditor) | G, J |
| **Master Plan** | `toc(iucnd).md` | **108¶ Full Control** | **🌙 Commander** | All Squads |

---

## 2. Task Delegation Matrix

### 🟠 G-Squad (Structure & Logic) - "The Architect"
**Mission**: Translate the Commander's intent into executable blueprints.
-   **[Code] Logic Design**: Write the pseudo-code and logic flow in `toc(u/c/n).md`.
-   **[Table] Schema Definition**: Define the exact columns and rows for required tables (e.g., "Table 3 needs columns A, B, C").
-   **[Figure] Spec Design**: Specify the axes, data sources, and visual style for figures in the `toc` files.
-   **[Scaffold] Paragraph Outlining**: detailed breakdown of what each of the 32 paragraphs must contain (H0, H1 hypotheses).

### 🟢 J-Squad (Execution & Production) - "The Builder"
**Mission**: Turn blueprints into reality and maintain the "Soul" of the paper.
-   **[Vision] Narrative Alignment**: Ensure every output aligns with the "Madness Metaphors" in `U✌️/C🦾/N🤹.md`.
-   **[Figure] Asset Generation**: Run the Python scripts to generate `fig_*.png`.
-   **[Table] Data Filling**: Execute the analysis code to populate the tables defined by G.
-   **[Text] Drafting**: Write the actual prose for the paragraphs based on G's scaffold.

### 🔴 K-Squad (Evaluation & Quality) - "The Auditor"
**Mission**: Kill weak arguments and enforce the "Analyst's Checklist".
-   **[QC] Blueprint Audit**: Review `toc(u/c/n).md` *before* J starts building. "Is this logic sound?"
-   **[QC] Asset Verification**: Check generated figures/tables against the `toc` specs. "Does Figure 3 match the hypothesis?"
-   **[QC] Vision Check**: Ensure the final text captures the essence of `U✌️/C🦾/N🤹.md`.
-   **[Mgmt] Issue Flagging**: Raise flags in the Dashboard Issue Queue if standards are not met.

---

## 3. Deliverables & Interfaces (The "Handover")

### 🔄 Interface: The "Code-to-Text" Pipeline

| From | To | Deliverable | Location |
|:---|:---|:---|:---|
| **🟠 G-Squad** | **🟢 J-Squad** | **1. Executable Code**<br>(`figures.py`, `tables.py`)<br>**2. Blueprints**<br>(`toc.md` with placeholders) | `src/scripts/`<br>`toc(u/c/n).md` |
| **🟢 J-Squad** | **🔴 K-Squad** | **1. Drafted Text**<br>(Markdown with embedded assets)<br>**2. Generated Assets**<br>(PNGs, CSVs from G's code) | `output/P*/chap*.md`<br>`output/figures/` |
| **🔴 K-Squad** | **🌙 Commander** | **1. Verified Product**<br>(Green-lit Dashboard)<br>**2. Audit Report**<br>(`eval(📝).md`) | `scale_dashboard.html`<br>`eval(📝).md` |

### 🏭 Asset Production Responsibility

*   **Code Generation**: **🟠 G-Squad** (Claude Code)
    *   *Responsibility*: Writes the Python scripts to generate figures and tables.
    *   *Standard*: Must be reproducible and strictly follow the `toc.md` specs.
*   **Asset Execution**: **🟢 J-Squad** (Builder)
    *   *Responsibility*: Runs G's scripts to produce the actual `.png` and `.csv` files.
    *   *Recording*: Updates `assets.json` to mark items as "Done" in the Dashboard.
*   **Asset Verification**: **🔴 K-Squad** (Auditor)
    *   *Responsibility*: Checks if the generated image matches the hypothesis in `eval(📝)`.

---

## 4. Workflow Implementation (The "Relay")

For each Paper (U, C, N):

1.  **Phase 1: Blueprinting (G)**
    *   **Input**: `toc(iucnd).md` (Master Plan)
    *   **Action**: G expands `toc(x).md` with detailed formulas and code specs.
    *   **Gate**: K reviews `toc(x).md`.

2.  **Phase 2: Production (J)**
    *   **Input**: `toc(x).md` (Specs) + `X.md` (Vision)
    *   **Action**: J writes code, generates assets, and drafts text.
    *   **Output**: `chapX_*.md` files and `output/figures/*.png`.

3.  **Phase 3: Audit (K)**
    *   **Input**: J's Output + `X.md` (Vision)
    *   **Action**: K verifies statistical significance (p-values) and narrative consistency.
    *   **Gate**: K marks "Verified" in the Dashboard.

---

## 4. Recommended Next Actions

1.  **Assign G**: "Update `toc(u).md` with the exact regression model for the U-shape test."
2.  **Assign J**: "Read `U✌️.md` and generate the 'Murky Middle' figure based on G's new spec."
3.  **Assign K**: "Verify if J's figure actually shows the U-shape described in `U✌️.md`."
