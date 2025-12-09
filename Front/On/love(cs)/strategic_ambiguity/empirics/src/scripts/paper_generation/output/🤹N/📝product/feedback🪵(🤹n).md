---
title: 🤹N Feedback Log
purpose: Mechanism (why) - formal rules and derivations
modified:
  - 2025-12-06T10:00:00-05:00
---

# 🤹N Feedback Integration Log

## 📥 Active Feedback Queue

| ID | Date | Source | Category | Feedback | Impact | Status | Resolution |
|:---:|:---:|:---|:---:|:---|:---:|:---:|:---|
| N01 | Dec 6 | 🐅권준 | Asset Specificity | "전용자산: 초기비용↓, 전환비용↑" | k* model | 🟡 Open | Link to Williamson TCE |
| N02 | Dec 6 | 🐅권준 | Literature | "Capital Kills Variety" (Loch et al. 2001) | k* model | 🟡 Open | Cite as direct ancestor |

---

## 🟡 Open Issues

### N01: 전용 자산과 전환 비용 (Dec 6)

**핵심 인사이트**:
> "전용 자산(Dedicated Asset, High Specificity)은 초기 비용은 싸지만, 수요 변화 시 전환 비용(Switching Cost)이 막대하다."

**이론적 연결**:

| 개념 | Asset Specificity | Promise Precision |
|:---|:---|:---|
| **높음** | 전용 자산 (site-specific) | Precise promise (V=Q1) |
| **낮음** | 범용 자산 (general purpose) | Vague promise (V=Q4) |
| **초기 비용** | 전용 ↓, 범용 ↑ | Precise: signaling ↑, Vague: screening cost ↑ |
| **전환 비용** | 전용 ↑↑, 범용 ↓ | Precise: pivot cost ↑↑, Vague: flexibility ↓ |

**Williamson (1985) TCE 연결**:
- Asset specificity → hold-up problem → governance structure choice
- **우리의 확장**: Promise specificity → investor lock-in → funding outcome

**수식화 가능성**:
$$\text{Total Cost}(V) = C_{\text{signal}}(V) + C_{\text{switch}}(V) \cdot P(\text{pivot})$$

- High V (precise): $C_{\text{signal}} \downarrow$, $C_{\text{switch}} \uparrow$
- Low V (vague): $C_{\text{signal}} \uparrow$, $C_{\text{switch}} \downarrow$

**Integration Point**: Paper N, k* model justification

---

### N02: "Capital Kills Variety" 증거 (Dec 6)

**문헌**: Loch, Terwiesch & Thomke (2001)

**핵심 개념**: Parallel vs. Sequential Testing

**논리 구조**:
```
실험 비용 ($c$) ↑  →  병렬 실험 ($k$) ↓  →  다양성 상실
```

| 조건 | 실험 전략 | 옵션 개수 |
|:---|:---|:---|
| Low cost ($c$ ↓) | Parallel testing | $k \uparrow$ |
| High cost ($c$ ↑) | Sequential testing | $k = 1$ |

**Paper N 연결** (k* 모델의 직접적 조상):
- Loch et al.: "비용이 오르면 병렬 실험 수가 준다"
- Paper N: "자본이 늘면 옵션 개수($k^*$)가 준다"

**동일한 구조, 다른 맥락**:
$$k^* = \arg\max_k \left[ \sum_{i=1}^{k} p_i \cdot V_i - c \cdot k \right]$$

**인용 전략**:
> "Our k* framework builds directly on the parallel testing literature (Loch, Terwiesch, and Thomke 2001), which showed that testing costs inversely determine the number of simultaneous options. We extend this to venture funding: capital intensity functions analogously to testing costs, reducing the optimal number of strategic options a founder can maintain."

**Integration Point**: Paper N ¶14 (Model Lineage), Literature Review

---

## ✅ Resolved Issues

| ID | Date | Resolution | Integrated Into |
|:---:|:---:|:---|:---|
| — | — | — | — |

---

## 📊 Feedback-to-Paper Mapping

| Category | Paper | Section | Mechanism |
|:---|:---:|:---|:---|
| Asset Specificity | N | k* model | Switching cost → optionality value |
| Parallel Testing | N | Literature | c → k inverse relationship |
| Newsvendor | N | Core model | CR = C/(C+F) → k* |

---

*Next review: Integration into Paper N draft*
