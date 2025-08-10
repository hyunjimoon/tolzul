## 📞1: Call Center LP

### 🛑 1.1 incorrect LP formulation

The current formulation only ensures that airline has enough employees each day, but it does not account for the regulation ("each employee needs to work consecutively for 5 days and then rest for two days."). The model is minimizing the sum of employee-days per week, not the total number of employees hired. we need to introduce a variable that can capture "working for 5 days then rest two days" 

### 🟢 1.2 Correct LP 
$x_i$ be the number of employees beginning work on day i. given the weekly cycle of 7 days, this captures "working for 5 days then rest two days". e.g. the sum of $x_{1}, x_{4}, x_{5}, x_{6}$ and $x_{7}$ will be the number of employees that will work on Monday. objective function is the the total number of employees that need to be hired, instead of sum of employee-days per week, as in 1.1.
$$
\begin{gather*}
\text { minimize } \sum_{i=1}^{7} x_{i} \\
\text { subject to } \quad x_{1}+x_{4}+x_{5}+x_{6}+x_{7} \geq 50  \\\
x_{1}+x_{2}+x_{5}+x_{6}+x_{7} \geq 45  \\
x_{1}+x_{2}+x_{3}+x_{6}+x_{7} \geq 45  \\
x_{1}+x_{2}+x_{3}+x_{4}+x_{7} \geq 40  \\
x_{1}+x_{2}+x_{3}+x_{4}+x_{5} \geq 50  \\
x_{2}+x_{3}+x_{4}+x_{5}+x_{6} \geq 20  \\
x_{3}+x_{4}+x_{5}+x_{6}+x_{7} \geq 20  \\
x_{i} \geq 0, \forall x_{i} \in\{1,2, \ldots . .7\} 
\end{gather*}
$$


### 💵 1.3 Cost Minimization Model: Extend LP to minimize total weekly cost considering wages and subsidies
Let's define $x_i$ as the number of employees who start working on day $i$. 

Minimize the total weekly pay:
$600x_1 + 620x_2 + 640x_3 + 640x_4 + 640x_5 + 640x_6 + 620x_7$

s.t.

1. At least 45 employees must work on Monday: $x_1 + x_2 + x_5 + x_6 + x_7 \geq 45$
2. At least 45 employees must work on Tuesday: $x_1 + x_2 + x_3 + x_6 + x_7 \geq 45$
3. At least 40 employees must work on Wednesday: $x_1 + x_2 + x_3 + x_4 + x_7 \geq 40$
4. At least 50 employees must work on Thursday: $x_1 + x_2 + x_3 + x_4 + x_5 \geq 50$
5. At least 20 employees must work on Friday: $x_2 + x_3 + x_4 + x_5 + x_6 \geq 20$
6. At least 20 employees must work on Saturday: $x_3 + x_4 + x_5 + x_6 + x_7 \geq 20$
7. Non-negativity constraint: $x_i \geq 0$, for all $i \in \{1, 2, \ldots, 7\}$

The objective function coefficients are determined as follows:
- An employee starting on Monday works Monday to Friday, earning a weekly wage of $100 \times 5 = 500$. Including the $100 bonus, their total weekly pay is $600$.
- An employee starting on Tuesday works Tuesday to Saturday, earning a weekly wage of $100 \times 4 + 120 = 520$. Including the $100 bonus, their total weekly pay is $620$.


## 2: LP

### 📊 2.1 Feasibility and Constraint Plotting: Graphically represent the LP constraints and identify the feasible region.
![[Pasted image 20240501234722.png]]
constraints are matched with colors on the left.
### 🎯 2.2 Graphical Optimization: Solve the LP graphically to find the optimal solution and objective value.
−x + 3y ≥ 0 and 3x + y ≥ 9 are  binding which intersect at (x, y) = (2.7, 0.9) leading to the objective value 4(2.7) + 6(0.9) = 16.2


### 🔄 2.3 Sensitivity Analysis on Constraint Coefficient: Analyze how changes to a constraint coefficient affect the optimal solution.
moving blue line x − y ≥ −3 gives us intuition on sensitivity analysis of a linear programming problem. range of 'r' for which the optimal solution remains valid is (-∞, 1.8].
As long as the line remains below or to the right of the optimal solution point, the solution will not change. The lowest possible position for the line is when it passes through the optimal solution point (2.7, 0.9). By substituting the optimal solution coordinates into the equation of the line, x - y = r, the value of 'r' can be determined as 1.8. 
### 🔍 2.4 Alternative Objective Function Analysis: Explore the impact of a different objective function on the LP solution.
with 2x − 2y as objective, entire green edge (parallel) of the feasible region becomes optimal. optimal solution is {(x, y)|x − y = −3, x ≥ 1.5} considering other constraints.

### 📐 2.5 Objective Function Coefficient Analysis: Determine conditions under which a specific point is the unique optimal solution.

To find a single objective function for which the point (1.5, 4.5) is uniquely optimal, we'll explore how to modify the objective while maintaining this unique optimality. This point is the feasible point with the smallest x value, so minimizing x makes this point the unique optimum. This implies that the coefficient of x, denoted as a, must be positive.

Also, notice that minimizing ax+by has the same optimal solution as minimizing x+ (b/a)y, so we’ll focus on objective functions where the coefficient of x is 1.

The problem then simplifies to selecting the active constraints at the optimal solution (1.5, 4.5) and determining the range of valid hyperplanes between those active constraints that preserve this unique optimality. Assume the objective is to minimize x + b'y with b' > 0. If b' is small, the level sets of the objective function will be nearly vertical, keeping (1.5, 4.5) as the unique optimum. However, as b' increases, the level sets will eventually become parallel to the constraint 3x + y ≥ 9 (purple), and the entire corresponding edge of the feasible region will be optimal. This transition occurs when b' = 1/3. Therefore, as long as b' is within the range (0, 1/3), (1.5, 4.5) remains uniquely optimal.

If b' is negative, a sufficiently small b' (with high magnitude) will improve the objective by increasing y, even at the expense of x. This happens when the level sets of the objective are parallel to the constraint x - y ≥ 3 (green). Thus, (1.5, 4.5) remains uniquely optimal as long as b' is greater than -1.

In summary, (1.5, 4.5) is uniquely optimal for objective functions of the form minimize a(x + b'y) where a > 0 and b' lies in the interval (-1, 1/3). Translating back to the original form, this means a > 0 and b lies in the range (-a, a/3).

### 🛑 2.6 Modified Constraint Analysis: Solve a modified LP with an additional constraint and explore its feasibility.  


![[Pasted image 20240502000115.png]]



When we add x+y ≤ 3 constraint, the problem becomes infeasible.

## 🚌 3: Transit Agency IP

### 📈 3.1 Graphical Solution and Feasibility Analysis: Graphically solve the IP and discuss the solution's feasibility and optimality.
 constraints and feasible region are plotted below
![[Pasted image 20240501232545.png]]

black dot $x^*=\left(x_1^*, x_2^*\right)=\left(\frac{72}{29}, \frac{200}{29}\right)$  is optimal solution as intersections of
$$
\begin{gathered}
10 x_1+8 x_2=80 \\
4 x_1+9 x_2=72
\end{gathered}
$$

with an optimal objective value of $z^*=\frac{7560}{29}$


### ⚙️ 3.2 Simplex Method Application: Solve the LP using the simplex method and detail the steps and solutions.


$$
\begin{array}{c|c|c|c|c|c|c|c}
\text{basic var} & \text{curr} & x_1 & x_2 & x_3 & x_4 & x_5 & \text{Ratio Test} \\
\hline
x_3 & 14 & 2 & 1 & 1 & 0 & 0 & 14/2=7 \\
x_4 & 80 & 10 & 8 & 0 & 1 & 0 & 80/10=8 \\
x_5 & 72 & 4 & 9 & 0 & 0 & 1 & 72/4=18 \\
\text{-Z} & 0 & 30 & 27 & 0 & 0 & 0 & \\
\hline
x_1 & 7 & 1 & 1/2 & 1/2 & 0 & 0 & 7/1=7 \\
x_4 & 10 & 0 & 3 & -5 & 1 & 0 & - \\
x_5 & 44 & 0 & 7 & -2 & 0 & 1 & - \\
\text{-Z} & -210 & 0 & 12 & -15 & 0 & 0 & \\
\hline
x_1 & 16/3 & 1 & 0 & 8/6 & -1/6 & 0 & \\
x_2 & 10/3 & 0 & 1 & -5/3 & 1/3 & 0 & \\
x_5 & 62/3 & 0 & 0 & 29/3 & -7/3 & 1 & \\
\text{-Z} & -250 & 0 & 0 & 5 & -4 & 0 & \\
\hline
x_1 & 72/29 & 1 & 0 & 0 & 9/58 & -4/29 & \\
x_2 & 200/29 & 0 & 1 & 0 & -2/29 & 5/29 & \\
x_3 & 62/29 & 0 & 0 & 1 & -7/29 & 3/29 & \\
\text{-Z} & -7540/29 & 0 & 0 & 0 & -81/29 & -15/29 & \\
\end{array}
$$



### 🌲 3.3 Branch and Bound Technique: Apply the branch and bound method to solve the integer programming problem, using pre-computed solutions.




![[Pasted image 20240501211100.png]]
for graphical purpose (intuition!) , i didn't prune the right tree. 

however,  if the integer solution $(4,5)$ is found (e.g. dfs) since (4,5)’s z = 255 becomes a LB and x1<=2 z_lp is smaller than the LB, we can prune the entire right subtree ( $x_{1} \leq 2$ tree ).


### 💡3.4 opt. bus alloc: Determine the optimal quantity of express and regular buses to maximize ridership.

The optimal solution is 4 express buses and 5 non-express buses.

### 📏 3.5 compare ridership estimates LP vs IP
overestimate in ridership is 5.69 = 269.69 ($Z_{LP}$) - 255 ($Z_{IP}$)
