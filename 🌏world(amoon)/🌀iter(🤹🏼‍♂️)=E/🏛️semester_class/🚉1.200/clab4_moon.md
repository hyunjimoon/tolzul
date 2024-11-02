## Question 1

### 1.1 🧳 Brute-force TSP
generate all possible tours and finding the one with the minimum total distance. Plot the number of vertices vs execution time and analyze the trend.

![[Pasted image 20240510144944.png|400]]
### 1.2 📈 analyze complexity

total complexity is 🕒  $O((N-1)! + (N-1)^2)$
- complexity of retrieving all (N-1)! permutations of N nodes (including the warehouse) is $O((N-1)!)$. 
- computational complexity of retrieving the cost of each route is $O((N-1)^2)$, since the function requires 2 for loops.
- plot  below shows similar ratio $\frac{permutation\_exp\_time}{complexity} \approx 10^{-6}$ for n = 10, 11 and 12.

![[Pasted image 20240510145421.png|400]]
## Question 2

### 2.1 🎯 Dynamic Programming TSP
![[Pasted image 20240510155557.png|500]]
### 2.2 📉 Analyze DP graph
- DP is ⏱️ Faster than permutation + 🐌 Slower growth than permutation
The graph obtained in question 2.1 is on number of vertices and the computation time for solving the Traveling Salesman Problem using dynamic programming. As the number of vertices increases, the computation time also increases, but the growth in computation time is not as rapid as one might expect. 

This observed trend can be attributed to the efficiency of the dynamic programming approach. By breaking down the problem into smaller subproblems and storing the results to avoid redundant calculations, dynamic programming can solve the Traveling Salesman Problem more efficiently than the brute-force permutation method.

### 2.3 ⚔️ Compare runtimes
 The time complexity of the dynamic programming approach is approximately O(n^2 * 2^n), where n is the number of vertices. While still exponential, it is significantly better than the factorial time complexity of the permutation method, O(n!). As a result, the computation time increases more gradually with the number of vertices for DP.

## Question 3

### 3.1 🙅‍♂️ Eliminate sub-tours
➕ add constraint: $\sum_{i, j \in S, i \neq j} x_{i j} \leq|S|-1 \quad \forall S \subset V, S \neq \emptyset$
third constraint specifies that the total number of links connecting any subset S of V with $|S|$ number of cities has to be equal to or smaller than$|S| - 1$. this is saying that no subset can form a cycle.
### 3.2 💸 Computationally expensive?
😓 computationally expensive, because the constraint actually requires not just one, but $2^n - 2$ number of equations to cover all possible subsets of V.
## Question 4
I tried with both Gurobi and MOSEK.
### 4.1 😴 Lazy constraints ILP

![[Pasted image 20240510223957.png|600]]
⏱️ ilp with lazy constraint is Similar to DP, faster than permutation.
### 4.2 🏁 Compare all runtimes
🤝 ILP ≈ DP (O(n^2 * 2^n)) << Permutation (O(n!))
ILP's computational time is comparable to using dynamic programming, and is much shorter than permutation.  ILP method relies on solving the problem as an Integer Linear Programming formulation, which can be computationally expensive. Nevertheless, the ILP method still provides better performance than the permutation method.

ILP's  effort below is additional factor that makes this method not very worth it in high number of vehicles
- to verify the existence of subtours in the solutions provided by ILP (`checking` function) and 
- to add lazy constraints one by one may

## Question 5
### 5.1 😵 Sub-tours in LP relaxation
∞ With LP, the subtour elimitation would require  many constraints, because there are many possible subsets S. In the LP relaxation, the decision variables are continuous and can take fractional values between 0 and 1. This means that the solution can contain fractional edges that form subtours, which are not feasible for the original TSP problem (example below). 
![[Pasted image 20240510214707.png|300]]

Eliminating all possible subtours would require considering all subsets of vertices, leading to an exponential number of constraints, which is computationally intractable.
### 5.2 🎯 Optimal solution with LP?
🚫 No because we are not eliminating subtours, optimal solution of LP relaxed problem may be in fact infeasible in original ILP problem. so the optimal solution can not be obtained.  i.e. we cannot obtain a valid lower bound for the optimal TSP solution using the LP relaxation method meaning objective value of the LP relaxation can be lower than the optimal TSP solution. The presence of subtours in the LP solution makes it an infeasible solution for the original TSP problem.
### 5.3 📈 LP relaxation times
![[Pasted image 20240510185247.png|300]]
The plot shows that the computation time increases gradually with the number of vertices, following a relatively linear trend with some fluctuations. It's ⏱️  very fast!
### 5.4 📏 Gap: ILP vs LP
at lower number of nodes gaps are low but nodes increases as gap increases.

| Instance n = | Q4 output (with sub tour) | Q4 output (no sub tour) | Q5 output | Gap (Q4 no tour/Q5) |
|--------------|---------------------------|-------------------------|-----------|---------------------|
| 3            | 156.0                     | 156                     | 156       | 1.00                |
| 4            | 222.0                     | 250                     | 222       | 1.126               |
| 5            | 292.0                     | 328                     | 292       | 1.123               |
| 7            | 162.0                     | 220                     | 162       | 1.358               |
| 9            | 324.0                     | 376                     | 324       | 1.160               |
| 10           | 130.0                     | 230                     | 130       | 1.77                |
| 11           | 292                       | 418                     | 292       | 1.431               |
| 12           | 358                       | 420                     | 358       | 1.173               |
![[Pasted image 20240510230748.png|300]]
