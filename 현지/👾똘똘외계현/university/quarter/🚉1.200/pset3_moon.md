- [[#🚗1: Autonomous electric delivery vehicle|🚗1: Autonomous electric delivery vehicle]]
	- [[#🚗1: Autonomous electric delivery vehicle#1.1 define s-a-p-r-d MDP components for vehicle routing|1.1 define s-a-p-r-d MDP components for vehicle routing]]
		- [[#1.1 define s-a-p-r-d MDP components for vehicle routing#👀s.state set|👀s.state set]]
		- [[#1.1 define s-a-p-r-d MDP components for vehicle routing#🤜a.action set|🤜a.action set]]
		- [[#1.1 define s-a-p-r-d MDP components for vehicle routing#🗄️p. transition matrix|🗄️p. transition matrix]]
			- [[#🗄️p. transition matrix#🗄️|🤜action `search`|🗄️|🤜action `search`]]
			- [[#🗄️p. transition matrix#🗄️|🤜action `stay`|🗄️|🤜action `stay`]]
			- [[#🗄️p. transition matrix#🗄️|🤜action `change`|🗄️|🤜action `change`]]
		- [[#1.1 define s-a-p-r-d MDP components for vehicle routing#💰r. rewards|💰r. rewards]]
		- [[#1.1 define s-a-p-r-d MDP components for vehicle routing#🖼️d.diagram|🖼️d.diagram]]
- [[#✈️2: Dynamic Programming (Deterministic)|✈️2: Dynamic Programming (Deterministic)]]
	- [[#✈️2: Dynamic Programming (Deterministic)#2.1 define s-a-p-r-d for plane loading|2.1 define s-a-p-r-d for plane loading]]
		- [[#2.1 define s-a-p-r-d for plane loading#👀s. state set|👀s. state set]]
		- [[#2.1 define s-a-p-r-d for plane loading#🤜a. action set|🤜a. action set]]
		- [[#2.1 define s-a-p-r-d for plane loading#🗄️p. transition matrix|🗄️p. transition matrix]]
		- [[#2.1 define s-a-p-r-d for plane loading#💰r. rewards|💰r. rewards]]
	- [[#✈️2: Dynamic Programming (Deterministic)#2.2 draw dynamic programming graph|2.2 draw dynamic programming graph]]
		- [[#2.2 draw dynamic programming graph#🖼️d. diagram|🖼️d. diagram]]
		- [[#2.2 draw dynamic programming graph#2.3 IP math model and three algorithms to solve|2.3 IP math model and three algorithms to solve]]
		- [[#2.2 draw dynamic programming graph#2.3.M|2.3.M]]
			- [[#2.3.M#decision variables:|decision variables:]]
			- [[#2.3.M#objective function:|objective function:]]
			- [[#2.3.M#constraints:|constraints:]]
		- [[#2.2 draw dynamic programming graph#2.3.A|2.3.A]]
			- [[#2.3.A#2.3.A1 IP solver tool|2.3.A1 IP solver tool]]
			- [[#2.3.A#2.3.A2 brute force|2.3.A2 brute force]]
			- [[#2.3.A#2.3.A3 build dp(state, action) table|2.3.A3 build dp(state, action) table]]
				- [[#2.3.A3 build dp(state, action) table#1: Initializing base case|1: Initializing base case]]
				- [[#2.3.A3 build dp(state, action) table#2. making decision rule for state and action|2. making decision rule for state and action]]
				- [[#2.3.A3 build dp(state, action) table#3.filling in DP table|3.filling in DP table]]
				- [[#2.3.A3 build dp(state, action) table#4. Tracing back to find optimal solution.|4. Tracing back to find optimal solution.]]
- [[#🚕3: Dynamic Programming (with Uncertainty)|🚕3: Dynamic Programming (with Uncertainty)]]
	- [[#🚕3: Dynamic Programming (with Uncertainty)#3.1: define s-a-p-r-d for ride-hailing pricing|3.1: define s-a-p-r-d for ride-hailing pricing]]
		- [[#3.1: define s-a-p-r-d for ride-hailing pricing#👀s. state set|👀s. state set]]
		- [[#3.1: define s-a-p-r-d for ride-hailing pricing#🤜a. action set|🤜a. action set]]
		- [[#3.1: define s-a-p-r-d for ride-hailing pricing#p. Transition matrix|p. Transition matrix]]
			- [[#p. Transition matrix#🗄️|🤜action F (Follow forecast)|🗄️|🤜action F (Follow forecast)]]
			- [[#p. Transition matrix#🗄️|🤜action N (Ignore forecast)|🗄️|🤜action N (Ignore forecast)]]
			- [[#p. Transition matrix#🗄️|🤜action I (Invest)|🗄️|🤜action I (Invest)]]
		- [[#3.1: define s-a-p-r-d for ride-hailing pricing#r. Rewards|r. Rewards]]
	- [[#🚕3: Dynamic Programming (with Uncertainty)#beq. Bellman's equation|beq. Bellman's equation]]
	- [[#🚕3: Dynamic Programming (with Uncertainty)#🖼️3.2: transition diagram|🖼️3.2: transition diagram]]
- [[#4: Reinforcement Learning|4: Reinforcement Learning]]
	- [[#4: Reinforcement Learning#🧮  4.1: tabular Q-learning updates for given values|🧮  4.1: tabular Q-learning updates for given values]]
		- [[#🧮  4.1: tabular Q-learning updates for given values#Q(3, -1)|Q(3, -1)]]
		- [[#🧮  4.1: tabular Q-learning updates for given values#Q(2, 1)|Q(2, 1)]]
		- [[#🧮  4.1: tabular Q-learning updates for given values#Q(3, 1)|Q(3, 1)]]
	- [[#4: Reinforcement Learning#💡 4.2: greedy policy optimal?|💡 4.2: greedy policy optimal?]]
	- [[#4: Reinforcement Learning#🧮 4.3: linear function approximation with Q-learning for given values|🧮 4.3: linear function approximation with Q-learning for given values]]
	- [[#4: Reinforcement Learning#💡 4.4: updated greedy policy's optimality?|💡 4.4: updated greedy policy's optimality?]]

## 🚗1: Autonomous electric delivery vehicle

### 1.1 define s-a-p-r-d MDP components for vehicle routing

#### 👀s.state set  
$S=\{High, Low, Dead\}$
State can be represented by the battery level. If battery level is above the threshold, then we can say state is High and if battery below a threshold then state is Low. No battery is Dead state.

#### 🤜a.action set 
$A = \{move, stay, charge\}$
#### 🗄️p. transition matrix
As $s' \sim P(\cdot|s,a)$, state transition matrix is a function of action, below are state $s_t$ (row) to the next state $s_{t+1}$ transition matrix. 
##### 🗄️|🤜action `search`

|     | H   | L   | D   |
| --- | --- | --- | --- |
| H   | p   | 1-p |     |
| L   |     | q   | 1-q |
| D   |     |     |     |

- **From High (H):**
    - Stays High (H) with probability 𝑝
    - Goes to Low (L) with probability 1−𝑝
- **From Low (L):**
    - Stays Low (L) with probability 𝑞
    - Goes to Dead (D) with probability 1−𝑞
- **From Dead (D):** Remains Dead (absorbing state at Dead state)
#####  🗄️|🤜action `stay`

|     | H   | L   | D   |
| --- | --- | --- | --- |
| H   | 1   |     |     |
| L   |     | 1   |     |
| D   |     |     |     |

- **From any state (H, L, D):** Stays in the same state (no transition to other states)
#####  🗄️|🤜action `change`

|     | H   | L   | D   |
| --- | --- | --- | --- |
| H   | 1   |     |     |
| L   |     | 1   |     |
| D   |     |     | 1   |

- **From Dead (D) to High (H):** Always transitions to High (H) with probability 1
#### 💰r. rewards
$$
\begin{cases}r_{\text {stay }=B} & \text { expected number of package while staying } \\ r_{\text {search }=A} & \text { expected number of package while searching } \\ -10 & \text { AV is dead and need rescue }\end{cases}
$$
- Package delivery yields a unit reward
- Being rescued (transition from Dead to High) results in a penalty of -10.
- as we'd like to incentivize AV to move,  $r_{\text {search }}>$ $r_{\text {wait }}$. Each may denote the expected number of package the robot will deliver (and hence the expected reward from package delivery if chosen the action) while searching and while waiting.  

#### 🖼️d.diagram

probability and reward are noted as (prob, reward) e.g. (p,A), (1-p,A)

![[Pasted image 20240420110108.png|400]]

## ✈️2: Dynamic Programming (Deterministic)
recalling the Shortest Path Problem which uses Bellman's principle of optimality (an optimal policy has the property that whatever the initial state and the initial decision are, the remaining decision must constitute an optimal policy with regard to the state resulting from the first decision) to modularize the optimization. 

Deterministic DP and the same action set across time reduces general RL (1) to (2)
- (1) $V_t(s_t)$ = $\underset{a_t \in \mathcal{A}_t\left(s_t\right)}{max} \mathbb{E}_{s_{t+1} \sim f\left(s_t, a_t, \epsilon_t\right)}\left[r_t\left(s_t, a_t\right)+V_{t+1}\left(s_{t+1}\right)\right.$
- (2) $V_t(s_t) = \underset{a \in A(s_t)}{max} \; r(s, a)$ + $V_{t+1}(s_{t+1})$ . For knapsack problem, state = (remaining weight, value).
### 2.1 define s-a-p-r-d for plane loading
Sure, let's define the state, action, state transition matrix, and reward for the plane loading problem in the requested format.

#### 👀s. state set

$S_t = \{(w, v) | w \in [0, W], v \in [0, V]\}$ $t \in [1, 5]$

The state is represented by a tuple (w, v) where:
- w: remaining weight capacity of the plane
- v: current total value of loaded items
- t: time step (going backward from t=5)

Q. difference btw (w, v, t) vs (w, v) state space - only notation difference? or gradient descent is impossible for (w,v) as we don't have t?
#### 🤜a. action set
$A = \{\text{Load i} | i \in [1, 5]\}$

The action set consists of loading a specific product i onto the plane.

#### 🗄️p. transition matrix

Usually, the next state (remaining weight capacity, total value) is stochastic function of current state and action (as $s' \sim P(\cdot|s,a)$). However, now, if we choose action (which product to load, the next state), the state transition matrix is deterministically set as -W[i] of remaining weight capacity (first slot state) and +V [i] (second slot state). State transition matrices for each action:

|        | (w - W[i], v + V[i]) |
| ------ | -------------------- |
| (w, v) | 1                    |

Note: If the action `Load i` is not feasible due to insufficient remaining weight capacity, then that action is not included in the action set for that state.

#### 💰r. rewards
$$
r((w, v, t), \text{Load i}) = V[i]
$$

- The reward for loading item i is the value of item i (V[i]).
- The objective is to maximize the total value of loaded items while satisfying the weight capacity constraint and the maximum number of loading chances.

### 2.2 draw dynamic programming graph
#### 🖼️d. diagram
![[Pasted image 20240420000710.png|600]]

I was exhausted drawing until T = 2, and Dingyi kindly allowed me to submit with the current version, saying this is enough to illustrate algorithm. The algorithm is to update value according to an action that maximizes current value + value of chosen action (among feasible actions that satisfies weight constraint. So this is primal method which first impose feasibility then solve optimality.

(x_1 = 1, x_2 = 1, x_3 = 0, x_4 = 0, x_5 = 1) is optimal value with 13.5 as optimal value
#### 2.3 IP math model and three algorithms to solve
#### 2.3.M
Maximize:
9x_1 + 4x_2 + 3x_3 + 2x_4 + (1/2)x_5

Subject to:
7x_1 + 5x_2 + 4x_3 + 3x_4 + x_5 = 13
x_i ∈ Z+ for i = 1, 2, 3, 4, 5

##### decision variables: 
Let x_i be a binary decision variable, where x_i = 1 if product i is loaded into the plane, and x_i = 0 otherwise, for i = 1, 2, 3, 4, 5.

##### objective function:
The goal is to maximize the total value of the loaded products. So, the objective function to maximize is 9x_1 + 4x_2 + 3x_3 + 2x_4 + (1/2)x_5

##### constraints:
1. Weight Capacity Constraint:
The total weight of the loaded products equals the plane's weight capacity of 13 units.

7x_1 + 5x_2 + 4x_3 + 3x_4 + x_5 ≤ 13

2. Non-negativity Integer Constraints:
The decision variables x_i must be non-negative integer constrain.
#### 2.3.A
##### 2.3.A1 IP solver tool
```{python}
from itertools import product
from pulp import LpProblem, LpVariable, LpMaximize, lpSum, LpInteger

# Create the problem variable to contain the problem data
model = LpProblem("Maximize_Expression", LpMaximize)

# Variables: x1 to x5 are integer and non-negative
x1 = LpVariable('x1', lowBound=0, cat=LpInteger)
x2 = LpVariable('x2', lowBound=0, cat=LpInteger)
x3 = LpVariable('x3', lowBound=0, cat=LpInteger)
x4 = LpVariable('x4', lowBound=0, cat=LpInteger)
x5 = LpVariable('x5', lowBound=0, cat=LpInteger)

# Objective Function
model += 9*x1 + 4*x2 + 3*x3 + 2*x4 + 0.5*x5

# Constraints
model += 7*x1 + 5*x2 + 4*x3 + 3*x4 + x5 == 13

# Solve the problem
model.solve()

# Output the results
solution = {
    'Status': LpProblem.status[model.status],
    'Objective': model.objective.value(),
    'Variables': {v.name: v.value() for v in model.variables()}
}
solution

```

##### 2.3.A2 brute force
```{python}
# Define the constraint equation coefficients and the right hand side value
coefficients = [7, 5, 4, 3, 1]
rhs = 13

# Define the objective function coefficients
objective_coeffs = [9, 4, 3, 2, 0.5]

# We will generate feasible solutions by varying the values of x1 to x5
# and checking if they satisfy the constraint.

# First, we need to limit the range of each variable to reduce the search space.
# A simple bound is to use the maximum possible value for each x_i given the smallest coefficient
# in the constraint, which would be x5 in this case (since 1*x <= 13)

max_values = [rhs // c for c in coefficients]

# Generate all combinations of x1 to x5 within these limits
feasible_solutions = []
for x1 in range(max_values[0] + 1):
    for x2 in range(max_values[1] + 1):
        for x3 in range(max_values[2] + 1):
            for x4 in range(max_values[3] + 1):
                for x5 in range(max_values[4] + 1):
                    # Check if this combination satisfies the constraint
                    if 7*x1 + 5*x2 + 4*x3 + 3*x4 + x5 == rhs:
                        # Calculate the objective function value for this combination
                        obj_value = 9*x1 + 4*x2 + 3*x3 + 2*x4 + 0.5*x5
                        feasible_solutions.append((obj_value, x1, x2, x3, x4, x5))

# Now find the combination that maximizes the objective function
max_solution = max(feasible_solutions, key=lambda x: x[0]) if feasible_solutions else None
max_solution

```

##### 2.3.A3 build dp(state, action) table
###### 1: Initializing base case
 base cases with dp[0, w] = 0 for all w (no items, no value), dp[i, 0] = 0 for all i (zero capacity, no value)
###### 2. making decision rule for state and action
dp[i,w] the maximum value that can be obtained by considering items 1 to i and total weight capacity w and we 
1. Include item i: dp[i, w] = v[i] + dp[i-1, w-w[i]] (if w_i ≤ w)
2. Exclude item i: dp[i, w] = dp[i-1, w]
###### 3.filling in DP table
(Q. not sure about the outer for loops)
for i = 1 to n:
    for w = 1 to W:
        if w_i ≤ remaining weight capa:
            dp[i, w] = $\underset{i}{max}$(v_i + dp[i-1, w-w_i], dp[i-1, w])
        else:
            dp[i, w] = dp[i-1, w]

|      | w=0 | w=1  | w=2  | w=3 | w=4 | w=5 | w=6  | w=7 | w=8  | w=9  | w=10 | w=11 | w=12 | w=13 |
|------|-----|------|------|-----|-----|-----|------|-----|------|------|------|------|------|------|
| i=0  | 0   | 0    | 0    | 0   | 0   | 0   | 0    | 0   | 0    | 0    | 0    | 0    | 0    | 0    |
| i=1  | 0   | 0    | 0    | 0   | 0   | 0   | 0    | 9   | 9    | 9    | 9    | 9    | 9    | 9    |
| i=2  | 0   | 0    | 0    | 0   | 0   | 4   | 4    | 9   | 9    | 9    | 9    | 9    | 13   | 13   |
| i=3  | 0   | 0    | 0    | 0   | 3   | 4   | 4    | 9   | 9    | 9    | 9    | 12   | 13   | 13   |
| i=4  | 0   | 0    | 0    | 2   | 3   | 4   | 4    | 9   | 9    | 9    | 11   | 12   | 13   | 13   |
| i=5  | 0   | 0.5  | 0.5  | 2   | 3   | 4   | 4.5  | 9   | 9.5  | 9.5  | 11   | 12   | 13   | 13.5 |
###### 4. Tracing back to find optimal solution.
- Start from dp[5, W], which gives the maximum value
- If dp[i, w] ≠ dp[i-1, w], include item i in the solution and move to dp[i-1, w-w[i]]
- Else, exclude item i and move to dp[i-1, w]
The optimal solution is:
x₁ = 1, x₂ = 1, x₃ = 0, x₄ = 0, x₅ = 1, with a maximum value of 13.5.

## 🚕3: Dynamic Programming (with Uncertainty)

###  3.1: define s-a-p-r-d for ride-hailing pricing
 infinite horizon discounted revenue problem 
#### 👀s. state set
$S = \{C, S, O\}$

The states represent the market presence and decisions of RWS:

- C: Competitive in the market
- S: Stop adjusting prices (combining the previous P and S states)
- O: Other state (competing service drawing away riders or invested in alternative transportation projects)
#### 🤜a. action set

$A = \\{F, N, I\\}$

- F: Follow the demand forecast and choose price s_i (only available in state C)
- N: Ignore the demand forecast and do not adjust the price (only available in state C)
- I: Invest in alternative transportation projects (only available in state O)

#### p. Transition matrix

##### 🗄️|🤜action F (Follow forecast)

|     | C              | S            | O   |
| --- | -------------- | ------------ | --- |
| C   | 1-$\sum_i p_i$ | $\sum_i p_i$ | 0   |
| S   | 0              | 1            | 0   |
| O   | 0              | 0            | 1   |

##### 🗄️|🤜action N (Ignore forecast)

|   | C   | S   | O   |
|---|-----|-----|-----|
| C | 1-β | 0   | β   |
| S | 0   | 1   | 0   |
| O | 0   | 0   | 1   |

- From C to C with probability $1-\beta$ (remain competitive)
- From C to O with probability $\beta$ (competing service emerges)

##### 🗄️|🤜action I (Invest)

|   | C   | S     | O   |
|---|-----|-------|-----|
| C | 1   | 0     | 0   |
| S | 0   | 1     | 0   |
| O | α   | 1-α   | 0   |

- From O to C with probability $\alpha$ (regain competitiveness)
- From O to S with probability $1-\alpha$ (stop adjusting prices)

#### r. Rewards

$$r(s, a) = \begin{cases}
\sum_{i=1}^{n} s_i p_i & \text{if } a = F \\
0 & \text{if } a = N \\
-c & \text{if } a = I
\end{cases}$$

- If action F is taken, the reward is the expected revenue based on the chosen prices and demand probabilities
- If action N is taken, no revenue is generated (reward of 0)
- If action I is taken, an investment cost of $c$ is incurred

### beq. Bellman's equation
Let $V^*(s)$ denote the optimal discounted revenue starting from state $s$. The Bellman's equation for this problem is:

For state C: $V^*(C) = \max \{s_i, \gamma (\beta V^*(O) + (1-\beta) \sum_{j=1}^{n} p_j V^*(S))\}$
For state S: $V^{*}(S) = \max \{0, \gamma ((1-p_i) V^{*}(C) + p_i V^{*}(S))\}$
For state O: $V^{*}(O) = \max\{0, -c + \gamma ((1-\alpha) V^{*}(O) + \alpha V^{*}(C))\}$

where:

- $s_i$ is the chosen price in state C when following the demand forecast
- $p_j$ is the probability of stopping price adjustment (transition from C to S) when following the demand forecast
- $\beta$ is the probability of a competing service emerging (transition from C to O) when ignoring the demand forecast
- $\alpha$ is the probability of regaining competitiveness (transition from O to C) when investing in alternative transportation projects
- $\gamma$ is the discount factor

Let $V(s)$ denote the optimal discounted revenue starting from state $s$. The Bellman's equation for this problem is:

$V(s) = \max_{a \in A(s)} \left\{ r(s,a) + \gamma \sum_{s' \in S} p(s'|s,a) V(s') \right\}$

where:
- $A(s)$ is the set of actions available in state $s$
- $r(s,a)$ is the reward for taking action $a$ in state $s$
- $p(s'|s,a)$ is the transition probability from state $s$ to state $s'$ when taking action $a$
- $\gamma$ is the discount factor

The optimal policy $\pi^*(s)$ specifies the optimal action to take in each state to maximize the discounted expected revenue:

$\pi^*(s) = \arg\max_{a \in A(s)} \left\{ r(s,a) + \gamma \sum_{s' \in S} p(s'|s,a) V(s') \right\}$

### 🖼️3.2: transition diagram 
The diagram shows the states, actions, and transitions with their respective probabilities and rewards (in the format of (transition probability|action).
![[Pasted image 20240420144315.png]]
![[Pasted image 20240424155942.png]]
## 4: Reinforcement Learning

### 🧮  4.1: tabular Q-learning updates for given values

- **TD target** for the state-action pair is $(r + \gamma \max_{a'} Q(s', a')$
- **TD error** is the difference between the TD target and the current Q-value for that state-action pair.
- Using the Q-learning update rule with α = 1/2, γ = 1:

#### Q(3, -1)
, the next state-action pair in the trajectory is (2, 1), but since the Q-value for all state-action pairs is initially 0, the max Q-value for the next state will also be 0. Therefore, the 
- TD target = -1 + 1 $\cdot$ 0 = -1
- TD error is the TD target minus the current Q-value, which is -1 - 0 = -1
- With $\alpha = 1/4$ updated Q-value for (3, -1) is 0 + $1/4 \cdot (-1)$ = -1/4

#### Q(2, 1)
- the next state-action pair is (3, 1), with an initial Q-value of 0. 
- TD target = -1 + 1 $\cdot$ 0 = -1
- TD error = -1 - 0 = -1
- updated Q-value for (2, 1) = -1/4
#### Q(3, 1)
- the next state-action pair is (4, 1) with a reward of 0, and the episode terminates since state 4 is the goal state. max Q-value for the next state is 0 (as it's the end of the episode).
- TD target -1 + 1 $\cdot$ 0 = -1
- TD error = -1 - 0 = -1
- updated Q-value for (3, 1) =  -1/4

### 💡 4.2: greedy policy optimal?
suggested greedy policy Q is suboptimal. It is know that at state 3, action 1 is optimal but from 4.1, Q(3,1) = Q(3,-1)= -1/4
 
### 🧮 4.3: linear function approximation with Q-learning for given values

Representing state-action pair as [s, a, 1]ᵀ, approximate Q-value is
q̂(s, a; w) = wᵀ[s, a, 1] = w₀s + w₁a + w₂

 w = [-1, 1, 1]ᵀ, w⁻ = [1, -1, -2]ᵀ and plugging (s,a,r,s') sample value (s=2, a=-1, r=-1, s'=1) is 
 
 $\nabla_w J(w) =\underset{a \in {-1, 1}}{max} (-1+ q̂(s', a'; w⁻) - q̂(s, a; w)) [s, a, 1]$ 

$\begin{aligned} w^{\prime} & \leftarrow w-\alpha \nabla_w J(w) \\ & =w-\frac{1}{4}\left(r+\max _{a^{\prime}}\left(w^{-}\right)^T\left[\begin{array}{l}s^{\prime} \\ a^{\prime} \\ 1\end{array}\right]-w^T\left[\begin{array}{l}s \\ a \\ 1\end{array}\right]\right)\left[\begin{array}{l}s \\ a \\ 1\end{array}\right]\end{aligned}$
 = -1/4 * [2,-1,1]
      = [-1, 1, 1]ᵀ - 1/4 [2, -1, 1]ᵀ 
      = [-3/2, 5/4, 3/4]ᵀ

### 💡 4.4: updated greedy policy's optimality?
Short answer may be, if the policy in 4.2 is sub-optimal, policy approximating this non-optimal policy is sub-optimal.

One example is even though optimal action at 5 is -1 (going to state 4), q̂(5,1)=2  and  q̂(5,-1)=1. This means best action computed from  q̂ at state 5 is 1 which is suboptimal
