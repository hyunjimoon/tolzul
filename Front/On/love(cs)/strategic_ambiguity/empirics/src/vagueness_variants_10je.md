# 📊 Vagueness Scorer Variants (Input for 10JE)

## 1. Strategic Vagueness Scorer V2 (`vagueness_v2.py`)
**Philosophy:** "Fluff vs. Facts"
**Core Logic:**
*   **Components:**
    1.  **Categorical Vagueness ($S_{cat}$)**: Density of abstract marketing keywords (e.g., "platform", "synergy"). Weighted by IDF.
    2.  **Concreteness Deficit ($S_{concdef}$)**: Absence of specific signals (Numbers, Dates, Versions, Units, Benchmarks).
*   **Aggregation:** $V_{raw} = 0.5 \times \max(S_{cat}, S_{concdef}) + 0.5 \times \text{mean}(S_{cat}, S_{concdef})$
*   **Hybrid Mode:** Mixes V2 score (50%) with raw concrete feature count (50%).

## 2. Strategic Vagueness Scorer V3 (`vagueness_v3.py`)
**Philosophy:** "Optionality vs. Feasibility" (Thesis Aligned)
**Core Logic:**
*   **Components:**
    1.  **Market Entropy ($V_{market\_entropy}$)**: Shannon entropy of market keyword categories. High entropy = Broad market optionality.
    2.  **Tech Abstractness ($V_{tech\_abstractness}$)**: Inverse of technical specificity density. High abstractness = Low feasibility visibility.
*   **Key Difference:** V3 treats "Vagueness" not just as lack of detail, but as a strategic construct of **Optionality** (Entropy).

## 3. Comparison Table

| Feature | V2 (Legacy) | V3 (Thesis) |
| :--- | :--- | :--- |
| **Primary Metric** | $V_{raw}$ (0-100) | $V_{market\_entropy}$ (0-1) & $V_{tech\_abstractness}$ (0-100) |
| **Focus** | Linguistic Style | Strategic Positioning |
| **Keywords** | Flat list of abstract terms | Categorized market keywords (for Entropy) |
| **Specificity** | Regex for units/dates/nums | Regex for technical specs |
| **Use Case** | General marketing fluff detection | Measuring "Strategic Ambiguity" (Optionality) |
