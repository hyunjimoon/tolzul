---
collection:
  - "[[Space/Lab/Papers]]"
author_ids:
  - stan
field:
  - 🐢inv
created: 2024-11-13
---

Warmup Epochs Figure. Adaptation during warmup occurs in three stages: an initial fast adaptation interval (I), a series of expanding slow adaptation intervals (II), and a final fast adaptation interval (III). For HMC, both the fast and slow intervals are used for adapting the step size, while the slow intervals are used for learning the (co)variance necessitated by the metric. Iteration numbering starts at 1 on the left side of the figure and increases to the right.
