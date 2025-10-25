---
성장:
  - 2025-10-22T07:39:20-04:00
---
### Data Source Ranking

1. **YC Public Data + Pitchbook (Hybrid)**
    
    - **Text Source:** YC public company profiles (e.g., from YCDB or Kaggle).
        
    - **Funding Source:** Pitchbook.
        
    - **Rank:** 1 (Strongly Recommended)
        
    - **Reasoning:** This hybrid model is the clear winner. It directly replicates the **El-Zayaty et al. (2025)** methodology by using high-quality, time-stamped, promissory text. YC provides a large, consistent sample across multiple batches. You can then use Pitchbook for its core strength: providing robust, clean funding (DV) and founder (control) data. This approach is high-quality, methodologically sound, and feasible.
        
2. **TechCrunch Disrupt + Pitchbook (Hybrid)**
    
    - **Text Source:** TechCrunch pitch transcripts.
        
    - **Funding Source:** Pitchbook.
        
    - **Rank:** 2 (Good, but less practical)
        
    - **Reasoning:** This also follows the **El-Zayaty et al. (2025)** precedent. The text quality is excellent (high-stakes pitches). However, the sample is smaller and more specific (only competition finalists). Systematically collecting this data is much harder than using the well-structured YC lists.
        
3. **Whitepapers / Litepapers + Pitchbook (Hybrid)**
    
    - **Text Source:** Public whitepapers (e.g., for Web3, deep tech).
        
    - **Funding Source:** Pitchbook.
        
    - **Rank:** 3 (High Potential, High Risk)
        
    - **Reasoning:** This provides the richest, most detailed promissory text, far exceeding a simple pitch. It's perfect for analyzing deep technical promises. The risk is that "vagueness" in a 30-page whitepaper is a completely different construct than vagueness in a 3-sentence pitch. It may be confounded with technical complexity, and the LIWC "certitude" measure may not be valid.
        
4. **Crowdfunding Sites (Standalone)**
    
    - **Text Source:** Campaign descriptions (e.g., Crowdcube).
        
    - **Funding Source:** The platform itself.
        
    - **Rank:** 4 (Methodologically Sound, Poor Fit)
        
    - **Reasoning:** This follows the **Kleinert (2024)** precedent and is a self-contained ecosystem. The text is promissory, and the funding data is built-in. However, it's a poor fit for your research question. Crowdfunding (retail investors, rewards/equity) is a different phenomenon than VC (professional investors, Series A/B). The results would not be comparable or generalizable to your core interest.
        
5. **Pitchbook Only (Your Original Plan)**
    
    - **Text Source:** Pitchbook `Company Description`.
        
    - **Funding Source:** Pitchbook.
        
    - **Rank:** 5 (Not Recommended)
        
- **Reasoning:** This is the least viable option. The `Company Description` field in Pitchbook is not a time-stamped, promissory document. It's a descriptive summary, often written by Pitchbook staff or updated by the company _after_ funding. Analyzing this text would introduce severe endogeneity and measurement error, as the text is a _result_ of funding, not a _cause_ of it.