---
성장:
  - 2025-10-21T22:36:26-04:00
  - 2025-10-22T05:41:49-04:00
---

```
Vagueness = 100 - Certitude_Score
```

**Where:**

- `Certitude_Score` = % of words from LIWC "certitude" dictionary
- Certitude words express: clarity, specificity, resoluteness, definiteness
- Examples: "always", "never", "certainly", "definitely", "complete", "entirely"

**Calculation:**

1. Run pitch text through LIWC software
2. LIWC counts words matching certitude dictionary
3. Certitude_Score = (certitude_words / total_words) × 100
4. Vagueness = 100 - Certitude_Score
5. Rescale to start near zero

**Interpretation:**

- Higher score = more vague language
- Lower score = more certain/precise language

**For your regression:**

```R
# Using LIWC output
Vagueness = 100 - liwc$certitude
```

**Example:**

- Pitch with 5% certitude words → Vagueness = 95
- Pitch with 8% certitude words → Vagueness = 92 (less vague)