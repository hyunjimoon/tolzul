# Table: Performance Metrics Comparison (Learn-only, Act-only, Learn & Act)

This table presents quantitative performance comparisons across three approaches for the G0, G1, and G2 cases.

| Metric | Definition | Learn-only (fix q) | Act-only (fix β) | Learn & Act |
|--------|------------|-------------------|------------------|-------------|
| **Prescription Profitability** | Expected cost savings E[Cost]_baseline - E[Cost]_algorithm | | | |
| G0 | Linear case | 0 | EC at q=1/2 | EC at q=1/2 |
| G1 | Symmetric sigmoid (βr=βc=1) | 0 | EC at ln(3/2) | EC at ln(3/2) |
| G2 | Asymmetric (βr<<βc) | 0 | EC at ln(3/2) | EC at ln(4) |
| **Prediction Accuracy** | 1 - |β_estimated - β_true|/β_true | | | |
| G0 | Linear case | 100% | 0% | 100% |
| G1 | Symmetric sigmoid | 100% | 0% | 100% |
| G2 | Asymmetric | 100% | 0% | 50% |
| **Prediction Effectiveness** | 1 / (|q* - q_t| × |β_t - β_0|) | | | |
| G0 | Linear case | 0 | ∞ | ∞ |
| G1 | Symmetric sigmoid | ln(4) × 4.5 = 2.73 | ∞ | ∞ |
| G2 | Asymmetric | 4.5 × ln(4) | ∞ | ∞ |
| **Update Efficiency** | (E[Cost]_0 - E[Cost]_t) / (|q_t - q_0| + |β_t - β_0|) | | | |
| G0 | Linear case | 0 | Saved/moved | Saved/moved |
| G1 | Symmetric sigmoid | 0 | EC savings/ln(3/2) | EC savings/(ln(3/2)+4) |
| G2 | Asymmetric | 0 | EC savings/ln(3/2) | EC savings/(ln(4)+1) |

Key insights:
- Learn-only approach (🟩D1.1): High accuracy but zero profitability (never optimizes quality)
- Act-only approach (🟩D1.2): Immediate profitability but zero learning (infinite effectiveness)
- Integrated approach (🟥C1/C2): Balances accuracy, profitability, and efficiency