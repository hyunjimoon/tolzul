[[2025-07-28|25-07-28-11]]

using [[🎯🧱💻marr 3lev]], 

## 1. Three-Level BMC Expression

**Computation Level**

- **Goal**: Optimize entrepreneurial promise strategy under uncertainty
- **Input**: Value (V), Costs (C)
- **Output**: Optimal prior Beta(a,b) on promise level φ
- **Computation**: argmax_{a,b} E[Utility] given promise-market dynamics

**Algorithmic Level**

- **Process**: Simulate forward belief updates from initial Beta(a,b)
- **Update Rules**:
    - Not sold: Beta(a, b+1)
    - Sold not delivered: Beta(a+2, b)
    - Sold and delivered: Beta(a+1, b+1)
- **Decision**: Choose (a,b) maximizing expected utility over simulated trajectories

**Implementation Level**

- **Model**: Conjugate Beta-Binomial
- **Code**: Gen/Stan implementation 
- **Interface**: probabilistic program → optimal (a,b)

