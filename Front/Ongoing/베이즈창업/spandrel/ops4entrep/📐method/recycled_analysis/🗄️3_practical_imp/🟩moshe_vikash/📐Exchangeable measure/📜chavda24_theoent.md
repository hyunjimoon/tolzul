2025-05-21
as i was grading demand modeling final exam3 in [[grade(eval(1202))]],
**Context:**  
Entrepreneurs often toggle between **modular** (value-chain) and **integrated** (architectural) strategies as they learn which approach pays off. We model each founder $n$ over $T$ periods choosing mode $m\in\{\mathrm{Mod},\mathrm{Int}\}$ with latent payoffs $U_{mnt}$, under two pure regimes—**Theory-Driven** (softmax) vs. **Practice-Based** (random)—and their mixtures.

_Definitions for founder $n$, period $t=1\ldots T$, modes $m\in\{\mathrm{Mod},\mathrm{Int}\}$:_  
$$
P_{mnt|\mathrm{thy}}=\frac{e^{αU_{mnt}}}{e^{αU_{\mathrm{Mod},nt}}+e^{αU_{\mathrm{Int},nt}}},
\quad
P_{mnt|\mathrm{rnd}}=\tfrac12.
$$

**(a)** Pure theory-driven likelihood:  
$$
L_{\mathrm{thy}}^{(n)}=\prod_{t=1}^T\prod_{m}[P_{mnt|\mathrm{thy}}]^{y_{mnt}}.
$$

**(b)** Pure random likelihood:  
$$
L_{\mathrm{rnd}}^{(n)}=(\tfrac12)^T.
$$

**(c)** Global mixture ($\pi\in[0,1]$):  
$$
P_{mnt}=\pi\,P_{mnt|\mathrm{thy}}+(1-\pi)\,\tfrac12,\quad
L_{\mathrm{mix}}^{(n)}=\prod_{t,m}[\pi\,P_{mnt|\mathrm{thy}}+(1-\pi)\,\tfrac12]^{y_{mnt}}.
$$

**(d)** Individual-specific weights ($B_n$ belief index):  
$$
P_{n,\mathrm{thy}}=\frac{e^{γB_n}}{e^{γB_n}+1},\quad
P_{n,\mathrm{rnd}}=1-P_{n,\mathrm{thy}}.
$$  
_Versus fixed $\pi$, $P_{n,\mathrm{thy}}$ captures each founder’s theory-orientation._

**(e)** Individual mixture likelihood:  
$$
L_{\mathrm{mix}_n}^{(n)}
=\prod_{t,m}[P_{n,\mathrm{thy}}\,P_{mnt|\mathrm{thy}}+P_{n,\mathrm{rnd}}\,\tfrac12]^{y_{mnt}}.
$$

> **Purpose:** Tests likelihood derivations for pure vs. mixture regimes and understanding of heterogeneity in entrepreneurial strategy search.  

2025-03
## **Comparative Table: Theory-Based vs. Practice-Based Entrepreneurial Search**

| **Key Distinction**                               | **🧠 Theory-Based Search**                                                             | **🤜 Practice-Based Search**                                                                         |
|----------------------------------------------------|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **1. Guiding Principle**                           | Guided by formal hypotheses or conceptual frameworks (theories)                         | Guided by on-the-ground actions, routines, and emergent adaptations                                   |
| **2. Primary Search Approach**                     | Structured, hypothesis-driven tests across multiple domains or markets                  | Iterative, trial-and-error learning driven by local insights, tacit knowledge, and incremental tweaks |
| **3. Role of Large Sample or Data**               | Tends to rely on broader, more systematic data (e.g., “big” samples such as Amazon’s)    | Often works with smaller, situation-specific data; draws on direct practice in local contexts         |
| **4. How Learning Updates Occur**                  | Learns globally via formal updating (akin to hierarchical Bayesian: pooling across many) | Learns locally; each new venture or action is treated as a distinct experiment with limited pooling   |
| **5. Overfitting/Underfitting Trade-off**          | More emphasis on generalizable findings; risk is missing local nuances (underfitting)    | More emphasis on local fit, but risk of being siloed or ignoring global patterns (overfitting)        |
| **6. Example Contexts**                            | Large platforms systematically testing new ideas (e.g., A/B testing at scale)            | Small-scale entrepreneurs iterating prototypes and pivoting based on direct feedback                  |
| **7. Relation to Hierarchical Modeling**           | Naturally maps onto multilevel models: each idea/venture is partially pooled via a global theory | May not explicitly pool across contexts; tends to treat each action as unique unless aggregated later |

This table encapsulates how **Theory-Based Entrepreneurial Search** (left column) naturally aligns with the **hierarchical Bayesian** perspective from “Models With Memory,” pooling evidence systematically from many contexts. In contrast, **Practice-Based Search** (right column) learns from smaller, direct experiments and is less likely to use an aggregate theory across multiple data clusters—though it can still benefit from partial-pooling ideas when insights from different local experiments must eventually be combined. 

