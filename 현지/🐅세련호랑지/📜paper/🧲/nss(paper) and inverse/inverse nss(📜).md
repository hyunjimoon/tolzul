> **Goal**  
> Turn a full‐length MANAGEMENT SCIENCE‐style journal article (supplied as a PDF) into four progressively coarser summaries (32 → 16 → 8 → 4 sentences) that align with the NAIL → SCALE → SAIL framing.

## 🔢 INPUT
* A single PDF of the target article (e.g., the POMS paper attached).

## ⚙️ PROCESS  
1. **Extract paragraphs** – treat the first sentence of every paragraph as its “representative” idea.  
2. **Generate a 32‑sentence summary** (`S1` … `S32`) by rewriting those representatives so each stands alone yet flows logically.  
3. **Compress**  
   * **16 sentences** – pair‑merge `(S1,S2)`, `(S3,S4)`, …, `(S31,S32)` using conjunctions or elision.  
   * **8 sentences** – repeat the pair‑merge on the 16‑sentence set.  
   * **4 sentences** – repeat once more.  
1. **Label modules** (optional but recommended): mark where sentences map onto the seven modules in [🐢🐅🐙👾lifestyle]] so the output can be re‑inserted into the stage table.

## 📤 OUTPUT  
Produce **one markdown block** containing, in order:  

### 32 Sentences

S1 … S32

### 16 Sentences

T1 … T16

### 8 Sentences  
U1 … U8

### 4 Sentences  
V1 … V4

```

*Keep line‑breaks exactly as above so scripts can parse them automatically.*  
*Do **not** add commentary outside the block.*  
```

