preparing for [[Space/Sources/Papers/🐅CompBayes/💻Mansinghka25_9.s/eval(vikash, probcomp_ent)]]
using ![[🎯🧱💻marr 3lev]], 
# 🎯computational level

![[Space/Sources/Papers/🐅CompBayes/💻Mansinghka25_9.s/🗄️1Table of Contents (Q&A&B)]]


## 🧱algorithm level

|Step|Description|
|---|---|
|1. **Elicit**|Entrepreneur provides $\textcolor{purple}{W}$ (stakeholder weights) and $\textcolor{green}{S_0}$ (initial state)|
|2. **Inform**|System provides prior $\textcolor{red}{D}$ (state transition dynamics per action, informed by industry)|
|3. **Calibrate**|System and entrepreneur calibrate $\textcolor{#3399FF}{B}$ (utility per state improvement) and $\textcolor{#3399FF}{C}$ (resource cost per action)|
|4. **Choose**|Entrepreneur selects $\textcolor{red}{a}$ (action) that best increases weighted utility per unit resource cost|
The entrepreneur first provides their stakeholder preference vector $\textcolor{purple}{W}$ and initial state $\textcolor{green}{S_0}$. The system then informs a prior state transition model $\textcolor{red}{D}$, reflecting how each action affects future states depending on industry. The entrepreneur then calibrates the utility gain matrix $\textcolor{#3399FF}{B}$ and action cost vector $\textcolor{#3399FF}{C}$ based on their specific venture conditions. Given $\textcolor{purple}{W}$, $\textcolor{#3399FF}{B}$, $\textcolor{#3399FF}{C}$, and $\textcolor{red}{D}$, they sequentially choose the action $\textcolor{red}{a}$ that maximizes expected utility improvement per cost, adapting dynamically through the decision path.

At each step:
$$
\textcolor{red}{a^*} = \arg\max_{\textcolor{red}{a}} \frac{\textcolor{purple}{W} \cdot \left(\textcolor{#3399FF}{U_{\text{next}}} - \textcolor{#3399FF}{U_{\text{current}}}\right)}{\textcolor{#3399FF}{C}[\textcolor{red}{a}]}
$$

where
- $\textcolor{#3399FF}{U} = \textcolor{#3399FF}{B} \times \textcolor{green}{S}$
- $\textcolor{green}{S_{\text{next}}} \sim \textcolor{red}{D}(\textcolor{green}{S}, \textcolor{red}{a})$

## 💻hardware implementation level 

#### Variable 

- 🟣 WWW is stored as a simple 3-dim vector
    
- 🔵 BBB is 3×3
    
- 🔵 CCC is 3 actions
    
- 🔴 DDD is 3×3×3 tensor
    
- 🟢 S0S_0S0​ is 3-dim state
    
- 📊 Simulation results are stored per decision step.

⭐️Use xarray to **organize your playground**.  Use trace to **record how you played** inside.

| Variable               | Description                                                                   | Type         | Dimension      | Initialization                                        |
| ---------------------- | ----------------------------------------------------------------------------- | ------------ | -------------- | ----------------------------------------------------- |
| `S`                    | Current entrepreneurial state (demand, supply, investor)                      | `np.ndarray` | `(3,)`         | `np.zeros(3)`                                         |
| `A`                    | Action vector (collaborate, segment, capitalize)                              | `np.ndarray` | `(3,)`         | `np.zeros(3)`                                         |
| `W_d`                  | Demand-side weight across model variants                                      | `np.ndarray` | `(3,)`         | `[0.2, 0.5, 0.6]`                                     |
| `W_s`                  | Supply-side weight across model variants                                      | `np.ndarray` | `(3,)`         | `[0.1, 0.3, 0.2]`                                     |
| `W_i`                  | Investor-side weight across model variants                                    | `np.ndarray` | `(3,)`         | `[0.7, 0.2, 0.2]`                                     |
| `W`                    | Combined stakeholder weight matrix                                            | `np.ndarray` | `(3, 3)`       | Aggregated from `W_d`, `W_s`, `W_i`                   |
| `U_d`                  | Demand-side utility scalar                                                    | `float`      | `()`           | `0.0`                                                 |
| `U_s`                  | Supply-side utility scalar                                                    | `float`      | `()`           | `0.0`                                                 |
| `U_i`                  | Investor-side utility scalar                                                  | `float`      | `()`           | `0.0`                                                 |
| `B`                    | Utility coefficient matrix (stakeholder × state)                              | `np.ndarray` | `(3, 3)`       | `[[0.6, 0.2, 0.1], [0.3, 0.5, 0.1], [0.1, 0.2, 0.8]]` |
| `C`                    | Cost per action                                                               | `np.ndarray` | `(3,)`         | `[0.3, 0.5, 1.0]` (example values)                    |
| `D_ext`                | Full state transition tensor (industry, action, ext_state_src, ext_state_dst) | `np.ndarray` | `(3, 3, 8, 8)` | Initialized to zeros, populated per industry          |
| `D`                    | Simplified state transition tensor (industry, action, state_src, state_dst)   | `np.ndarray` | `(3, 3, 3, 3)` | Initialized to zeros                                  |
| `R`                    | Total available resources                                                     | `float`      | `()`           | `2.0`                                                 |
| `current_industry`     | Current selected industry ("ai", "climate", "robotics")                       | `str`        | `()`           | `"ai"`                                                |
| `simulation_states`    | State history across steps and variants                                       | `np.ndarray` | `(3, 10, 3)`   | Zeros                                                 |
| `simulation_actions`   | Actions taken across steps and variants                                       | `np.ndarray` | `(3, 10, 3)`   | Zeros                                                 |
| `simulation_utilities` | Utility per stakeholder across steps                                          | `np.ndarray` | `(3, 10, 3)`   | Zeros                                                 |
| `simulation_resources` | Remaining resources across steps                                              | `np.ndarray` | `(3, 10)`      | Zeros                                                 |


### B Matrix (Uncertainty Reduction)

```python
# Example B matrix structure (to be calibrated with empirical data)
B = jnp.array([
    # Employee uncertainty reduction coefficients for each state
    [-0.8, -0.5, -0.3,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],  # How states reduce employee uncertainty
    
    # Investor uncertainty reduction coefficients for each state
    [ 0.0,  0.0,  0.0, -0.7, -0.6,  0.0,  0.0,  0.0,  0.0,  0.0],  # How states reduce investor uncertainty
    
    # Operational uncertainty reduction coefficients for each state
    [ 0.0,  0.0,  0.0,  0.0,  0.0, -0.5, -0.4, -0.7,  0.0,  0.0],  # How states reduce operational uncertainty
    
    # Customer uncertainty reduction coefficients for each state
    [ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.6, -0.8]   # How states reduce customer uncertainty
])
```

### C Matrix (Resource Consumption)

```python
# Resource consumption for each action
C = jnp.array([
    [0.2, 0.0, 0.0, 0.0],  # Culturate costs $0.2M
    [0.0, 0.3, 0.0, 0.0],  # Collaborate costs $0.3M
    [0.0, 0.0, 1.0, 0.0],  # Capitalize costs $1.0M 
    [0.0, 0.0, 0.0, 0.5]   # Segment costs $0.5M
])
```

### D Tensor (State Transition)

```python
# Example simplified structure of D tensor (probabilities to be calibrated)
# D[action, current_state, next_state] = probability
# For example:
D = jnp.zeros((4, 10, 10))

# Culturate action affects team states
D = D.at[0, 0, 0].set(0.2)  # 20% chance team_culture stays bad
D = D.at[0, 0, 1].set(0.8)  # 80% chance team_culture becomes good
D = D.at[0, 1, 1].set(0.5)  # 50% chance leadership_capability improves
# ... and so on for all state transitions
```



## Simplex Pivot Decision Rule Implementation

```python
def simplex_pivot(S, W, B, C, D, R, available_actions):
    """
    Implements the simplex pivot decision rule to choose the next action
    
    Args:
        S: Current state vector (binary)
        W: Weight vector for different uncertainties
        B: Uncertainty reduction matrix
        C: Resource consumption matrix
        D: State transition tensor
        R: Available resources
        available_actions: List of actions that can be taken
        
    Returns:
        optimal_action: Index of the best action to take
    """
    best_action = None
    best_reduction = 0.0
    
    # Calculate current uncertainty
    U = compute_uncertainty(S, B)
    
    # Find critical bottleneck
    bottleneck_idx = jnp.argmax(W * U)
    
    # Evaluate each action for uncertainty reduction
    for a_idx in available_actions:
        # Check if we have enough resources
        action_cost = C[a_idx, a_idx]
        if action_cost > R:
            continue
            
        # Calculate expected next state
        expected_next_S = compute_expected_next_state(S, a_idx, D)
        
        # Calculate expected uncertainty reduction
        next_U = compute_uncertainty(expected_next_S, B)
        uncertainty_reduction = U[bottleneck_idx] - next_U[bottleneck_idx]
        
        # Normalize by resource cost
        efficiency = uncertainty_reduction / action_cost
        
        if efficiency > best_reduction:
            best_reduction = efficiency
            best_action = a_idx
            
    return best_action
```
