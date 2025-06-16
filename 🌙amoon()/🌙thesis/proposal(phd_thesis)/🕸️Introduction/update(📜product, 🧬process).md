### **Prompt 2 – `update(📜product, 🧬process).md`**

```markdown
# update(📜product, 🧬process).md
> **Goal**  
> Use the 32‑sentence “product” summary of a paper to refresh the author’s writing **process**—specifically, to update the NAIL → SCALE → SAIL table and highlight next‑step actions.

## 🔢 INPUT
* The 32‑sentence summary (`S1` … `S32`) generated with Prompt 1.
* The current stage table (see user’s latest version).

## ⚙️ PROCESS  
1. **Sentence‑to‑Module tagging** – assign each `S#` to its module slot (M1…M8) by content.  
2. **Gap analysis** – compare filled modules with empty cells in the existing table. Flag:  
   * missing sentences,  
   * modules that over‑run (too much detail),  
   * logic mismatches between stages.  
3. **Rewrite table rows**  
   * **Mission, Stakeholder Focus, Key Dilemma, Key Output, Strategic Principles, Validation Tests** – update wording to reflect insights from the new paper.  
   * **Module Coverage row** – paint 🟪🟩🟧🟥🟦 squares to show progress.  
4. **Action queue** – list ≤ 5 concrete to‑dos (e.g., “Draft S13–S16 to finish Module 4” or “Validate S24 with reviewer simulations”).

## 📤 OUTPUT  
*Updated stage table* followed by an *“Action Queue”* bullet list.  
Keep citations to the `S#` index (not the original paper) so later tooling can trace provenance.
```


