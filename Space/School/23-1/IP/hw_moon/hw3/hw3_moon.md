## 1. Generalized lifting procedure
a. 
i) valid: when x1=1, only one of the rest variables are 1 which makes x3+x4 $\leq$ 1 valid
ii) facet defining: knapsack polytope's dimension is 4, and with two implied equality (x1=1, x2=0) we need to find 2 (=4-1-2+1) affinely independent vectors that are locally tight to prove $x3+x4 \leq 1$ is facet defing for the entire polytope (we can start from projected polytope with dimension 2, and get the same conclusion in (x3, x4) space, instead of entire (x1,x2,x3,x4) space). (1,0,1,0), (1,0,0,1) are two such vectors: i) satisfy $x3+x4 \leq 1$. 

b.  
for a =1, the inequality is **still** valid and facet defining. 
i) valid: when x2=0, ax2 + x3+x4 is valid for all a (from a.). when \, x3+x4 $\leq$ 1-a is valid for a $\leq$ 1 (with x1=1, x2=1, we can have no one among x3,4).

ii) facet defining: two vectors (1,0,1,0), (1,0,0,1) from a. satisfies the inequality with equality and in addition (1,1,0,0) also satisfies the inequality with equality and affinely independent from the other two vectors. 

c. 
with a =1,  b=2, the inequality is **still** valid and facet-defining
i) valid: when $x_1=1$ , $x_2 + x_3 + x_4 ≤ 1$ is valid from b. when  x1 = 0, $x_2 + x_3 + x_4 ≤ 1+b$ is  valid if b $\geq$ 2. This is from the definition of $\mathcal{F}_0$ where x2,3,4 are binary and should satisfy x 2+ x 3+ x 4≤ 4 when x1=0. 
**lesson1: binary conditions can also provide bound.** 
**lesson2: x2=0 is easy for b, x1=1 is easy due to original partion. this causes different direcation of coefficient from validity (**  a $\leq$ 1  vs  b $\geq$ 2).

ii) facet defining: three vectors (1,1,0,0) (1,0,1,0), (1,0,0,1) from b. satisfies the inequality with equality and in addition, affinely independent new vector (0,1,1,1) also satisfies the inequality with equality as a+2 = 1+b. 

d. 
since x1=1 is being lifted, validity from x1=0 gives bound for new coefficient which is $\alpha \leq \sum_{j=2}^n \pi_j x_j^*-\pi_0$ where $x^*$ is argmax among $x \in F_1 := F \cap \{ x \in \{0, 1\}^n| x 1= 1 \}$

the thm below (thm.2.2 from textbook) provides modular algorithm for keeping the inequality **still** valid and facet-defining (by adding one dimension from (b)) after lifting one variable. 
![[../../../../../../../ref/Pasted image 20230322080226.png]]


e. 
we can use d. as a building block when adding x1 ... x_p (k = 1..p) sequentially (for loop). Only thing that needs care is each variable's partition which is given. Hence we should add an if statement which detects whether the new variable to be lifted is in partition $\mathcal{N}_0$ or $\mathcal{N}_1$  then calculate the new $Z_k, \alpha_k$ accordingly as below. $I(x_k \in N_1)$ is an indicator function.

$Z_k := max_{x \in \mathcal{F}_{I(x_k \in N_1)}} \Sigma_{j \in \{1... k-1\} \cup \{p+1.. n\}}a_jx_j$

and $\alpha_k =  (\pi_0' - Z_k) * (-1)^{I(x_k \in N_1) + 1}$  

where  $\mathcal{F}, \mathcal{F}_0, \mathcal{F}_1$ are updated sequentially as the full dimension polytope in the previous stage and its projection to $x_k =0 \; (\rightarrow \mathcal{F}_0), x_k =1 \; (\rightarrow  \mathcal{F}_1)$ space. $\pi_0'$ is also updated as LHS of the previous facet-defining inequality.

## 2. knapsack facets
### a. 
what we call cover inequality is as follows. hence when floor(a_j/a_k1 ) = 0, we have validity. for j not in C and floor(a_j/a_k1 ) $\geq 1$ , a_j is larger than the heaviest item in C. if we imagine starting from a cover and 1:1 swapping its member with only the heavy $j$ s (1, 2 in the example) it is clear the total number of item number (right hand side) cannot increase i.e. cannot exceed C-1 .

$\sum_{j \in C} x_j\leq|C|-1$.  

to illustrate, for the given example where (3,5,6) is a minimal cover, let's assume (a_1, ..., 5) = (35, 25, 10, 9,8). floor(a_1/a_3) = 3, floor(a_2/a_3) = 2. To include the first item, at least three original items should be put out as a_k1 is largest. To include the second item, at least two original items should be put out. hence we have: 

$\sum_{j \in C} x_j+\sum_{j \notin C}\lfloor\frac{a_j}{a_{k_1}}\rfloor x_j \leq|C|-1$

### b.
logic is same with a. -- we cannot have more number of items if the candidates are heavier than the heaviest member of the cover. starting from a cover, we can use one to one swapping argument as in a.
   
### c. 
   ![[../../../../../../../ref/Pasted image 20230326123828.png]]

## 3. disjunctive cuts
   a. compared to having cut 1 (from $\mathcal{D_1}, \mathcal{D_2}$), having cut 1,2,3 (from $\mathcal{D_1}, \mathcal{D_2}, \mathcal{D_3}, \mathcal{D_4}$) is tighter. Although this may be what $\mathcal{P_D}$ is doing (as intersection of the origianal polytope and disjoint regions), if $D_t x \leq d_t$ includes $Ax \leq b$, we can bound $\mathcal{D_t}$ within $\mathcal{F}$.
   ![[../../../../../../../ref/Pasted image 20230326081054.png]]
   
b. 
$P_0 = P \cap (\cup_{t=1..T} D_t) = Proj_x(Q)$ where higher dimension polyhedron Q is defined as follows. Due to the decrease of degree of freedom from summation of $x_i$ equals x and summation of $\lambda_i$ equals 1, dimesntion is 2T+1 -1 = 2T -1
   $$
\begin{gathered}
Q:\left\{\left(x, x_1 \cdots x_T, \lambda_1, \cdots \lambda_T\right): \\ \sum_{i=1} x_i =x\right. \\
A_i x_i \leq \lambda_i b_i, \forall i=1 \cdots T \\
0 \leq x_i, \forall i=1 \cdots T \\
\left.\sum_{i=1}^T \lambda_i=1 ; \lambda_i \geq 0, \forall i=1 \cdots T\right\} \\
\end{gathered}
$$

c. 
when polyhedrons are one of the three, we can express the convex hull of their union as projection of higher dimension polyhedron.
 1. bounded
 2. share recession cone
 3. disjunction

primal problem (min) is:
$$
\begin{gathered}
A_1 x_1-\lambda_1 b_1 \leq 0 \quad\left(u_1\right) \\
\vdots \\
A_T x_T-\lambda_T b_T \leq 0 \quad\left(u_T\right) \\
x-x_1-x_2 \cdots x_T=0 \quad(\alpha) \\
\lambda_1+\lambda_2+\lambda_3 \cdots +\lambda_T=1 \quad(\beta) \\
x_1, \cdots ,x_T \geqslant 0 \\
\lambda_1, \cdots ,\lambda_T \geqslant 0
\end{gathered}
$$
dual problem (max) is

$$
\begin{aligned}
& P_j=\left\{\alpha^{\top} x\leqslant \beta\right\} \\
& -\alpha+u_1^{\top} A_1 \geqslant 0\left(x_1\right) \\
& -\alpha+u_2^{\top} A_2 \geqslant 0\left(x_2\right) . \\
& \vdots \\
& -\alpha+u_T^{\top} A_T \geqslant 0\left(x_T\right) \\
& \beta-u_1^{\top} b_1 \geqslant 0\left(\lambda_1\right) \\
& \vdots \\
& \beta-u_T^{\top} b_T \geq 0\left(\lambda_T\right) \\
& u_t \geq 0  \quad \forall t \in [1..T]
\end{aligned}
$$

cut generation linear programming for this problem is as follows. the last constraint is for normalization and the number of constraints is 2*T*(2n+ m)+  1.  (because each x_t, lambda_t, u_t is dimension n, n, m). The number of variables is n (from alpha) +1 (from beta).
$$
\begin{aligned}
max \quad \alpha'x^* - \beta \\
& s.t. (\alpha, \beta) \in P_j \\
& ||\alpha || \leq 1
\end{aligned}
$$

## 4. cut game
![[../../../../../../../ref/Pasted image 20230326110803.png]]
example of nice shots: circle + gomory cut can be effective when extreme point is close to integer points. e.g.  chavatal-gomory rank of red is larger than 1 as its upper part is pointed. If circle cut is applied, cut the integer point near the pointed head, gomory cut can be applied next to form a ideal formulation in the region.
![[../../../../../../../ref/Pasted image 20230322084432.png]]


- Cutting plane algorithms are an effective tool for shrinking the size of the feasible region of LP relaxation, which increases the computation time of the branch-cut-bound algorithm for mixed integer linear programming. split cut (which is in theory equivalent to Gomory's mixed integer and mixed integer rounding) is the most effective. However, cutting plane aigiritimm is specific to problem and instance, and how it is engineered (e.g. gomory cut only worked well with many engineering choices like multi-cut and cut management).
- Depending on the size of the feasible region, the order of applied cuts on the effectiveness of the cuting-plane algorithm is great. However, there are no general guidelines for when and what cuts to use except there is a tradeoff between the strength and easiness of the cut. an example of a family of cuts seen in class that is not considered in the game but could have been helpful is split cut as only horizontal and vertical split cuts was possible i.e. rotation was impossible.
