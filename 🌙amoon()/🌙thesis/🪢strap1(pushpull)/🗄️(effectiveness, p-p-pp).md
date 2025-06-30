# Table: Effectiveness Comparison (When Can Each Approach Reach q*?)

This table shows the binary effectiveness metric - whether each approach can theoretically reach the global optimal quality q* under different conditions.

| Case                        | Learn-only (fix q)                               | Act-only (fix β)            | Learn & Act            |
| --------------------------- | ------------------------------------------------ | --------------------------- | ---------------------- |
| **Can reach q*?**           | Only if costs/rewards stable (q* doesn't change) | Only if β parameters stable | Always ✓               |
| **G0: Linear**              | ✗ (q fixed at 0)                                 | ✓ (reaches q*=1/2)          | ✓ (reaches q*=1/2)     |
| **G1: Symmetric (βr=βc=1)** | ✗ (q fixed at 0)                                 | ✓ (reaches q*=ln(3/2))      | ✓ (reaches q*=ln(3/2)) |
| **G2: Asymmetric (βr<<βc)** | ✗ (q fixed at 0)                                 | ✗ (wrong q*=ln(3/2))        | ✓ (reaches q*=ln(4))   |

**Conditions for Effectiveness:**
- **Learn-only (🟩D1.1)**: Requires stable cost ratio (Cu/(Cu+Co+V)) so that learning β doesn't change optimal q
- **Act-only (🟩D1.2)**: Requires stable β parameters so initial assumption remains valid
- **Learn & Act (🟥C1)**: No conditions - always converges to true optimum

**Key Insight**: Only the integrated approach can handle both parameter uncertainty AND cost volatility.