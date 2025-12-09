Done with Alexander Kuptel, Sarah Baum, Josh Mak
# 1. 
(a) $u(x, c)=\sqrt{c}+ \alpha \sqrt{x}, c+p_c x=w(1-\tau)$
 $\mathcal{L}(x \cdot c)=\sqrt{c}+\alpha \sqrt{x}+\lambda\left(w(1-z)-c-p_x x\right)$
 $\left.\begin{array}{l}\frac{\partial L}{\partial x}=\frac{\alpha}{2 \sqrt{x}}-\lambda \cdot p_x=0 \\ \frac{\partial L}{\partial c}=\frac{1}{2 \sqrt{c}}-\lambda=0 \\ \frac{\partial L}{\partial \lambda}=w(1-\tau)-c-p_x x=0\end{array}\right] \begin{aligned} & \lambda=\frac{1}{2 \sqrt{c}} \\ & =\frac{\alpha}{2 p_x \sqrt{x}}\end{aligned}$

(b) $c = \frac{p_x^2 x}{\alpha^2}, x = \frac{w(1-\tau)}{p_x(p_x/\alpha^2 + 1)}$
(c) hicksian demand
max 1c + px  s.t. $\sqrt{c}+\alpha \sqrt{x} \geq u_0$
... lagrangian dc, dx ...
Q2. $c = \frac{p_x^2 x}{\alpha^2}, x = \frac{e}{p_x(p_x/\alpha^2 + 1)}$ (need checking)
plug in (c*, x*) to utility to get v(p,w), and mutiply them by (1,p) to get e(p,u).

(d) Since food voucher is dep on tax fond, $g=\tau w$.
consumer gets extra $g$ in wealth,
$$
\left.\begin{array}{l}
\max _{x, c} \sqrt{c}+\alpha \sqrt{x} \\ \text { s.t. } c+p_x w=w(1-\tau)+g \\
\quad c+p_x x=w(1-\tau)+\tau w=w \\
\frac{\partial L}{\partial x}=\frac{\alpha}{2 \sqrt{x}}-\lambda p_x=0 \\
\frac{\partial L}{\partial c}=\frac{1}{2 \sqrt{c}}-\lambda=0 \\
\frac{\partial L}{\partial x}=w-c-p_x x=0
\end{array}\right] \begin{aligned}
& \text { budget constraint is same } \\
& \text { as tax. voucher are canceled out. }
\end{aligned}
$$
interpretation differs: Collected tax is returned to consumer as fond vouchers

(e) both budget constraint and utility are same so Marshallian and Hicksion demand from $a . b$ remains the same

portion of expenditure is financed by ford voucher.

(f) to determine the effect on consumer utility from marginal change in $\tau$, we need to consider how $\tau$ change affects customer's optimal bundle and utility level. however as budget constraint doesn't include $\tau$, $\frac{\partial\left(c+p_x x\right)}{\partial \tau}=0$ optimal bundle doesn't charge utility revel also. is the same. Hence the optimal val function indirect utility $\frac{\partial V}{\partial \tau}$ is also 0 . There might be a corner solution which returns solution of $=\frac{\sqrt{w}}{2 \sqrt{(1-\gamma) p_x^\tau}}\left(\sqrt{1-\tau}-\sqrt{p_x \tau}\right)$

(g) $C V(E V)$ measures chan in wealth that makes consumer indifferent btw new situation and original under new(old) price.


(h) Given the "true" utility function according to the government:
$$
\tilde{u}(x, c)=\sqrt{c}+(\alpha+\beta) \sqrt{x}
$$
To determine for what values of $\beta$ tax-transfer scheme would improve consumer welfare we need to compare the consumer's utility under the "true" utility function with and without the tax-transfer scheme. If the utility with the tax-transfer scheme is higher than without it, then the scheme improves welfare.

Given that the tax and voucher cancel out, the consumer's choices of $x$ and $c$ remain unchanged. Therefore, we need to find the value of $\beta$ for which:
$$
\sqrt{c^*}+(\alpha+\beta) \sqrt{x^*}>\sqrt{c^*}+\alpha \sqrt{x^*}
$$
Where $\left(x^*, c^*\right)$ is the optimal consumption bundle without the tax-transfer scheme. hence
$$
\beta \sqrt{x^*}>0
$$
and as $x^*$ is positive, $\beta$ must be positive for the tax-transfer scheme to improve consumer welfare according to the "true" utility function.

(i) Solve for the optimal $\tau$ in terms of maximizing compensating variation when the consumer under-accounts for the nutritional value of food, as a function of the exogenous variables

I failed to compute the specific value of $\tau$, but below is a conceptual workflow. To solve for the optimal  $\tau$, we need to consider the difference between the consumer's perceived utility and the "true" utility that accounts for the nutritional value of food. The goal is to find $\tau$ that maximizes the compensating variation (CV) when the consumer under-accounts for the nutritional value of food.

Step 1: Express $x^{**}$ and $c^{**}$ as functions of $\tau$

Given the consumer's perceived utility function and the budget constraint:

$u(x, c) = \sqrt{c} + \alpha \sqrt{x}, c + p_x x = w$

The Marshallian demand functions $x(\tilde{p}, w)$ and $c(\tilde{p}, w)$ can be derived from this utility maximization problem. For simplicity, let's denote these demand functions as $x^*(\tau)$ and $c^*(\tau)$ since they will depend on $\tau$ through the effective wealth.

Step 2: Determine the Compensating Variation (CV)

The CV is the amount of money that would make the consumer indifferent between their perceived utility and the "true" utility given the tax and voucher scheme: $u(x^*(\tau), c^*(\tau)) = \tilde{u}(x^{**}, c^{**} + CV)$ Where $\tilde{u}(x, c) = \sqrt{c} + (\alpha + \beta) \sqrt{x}$ is the "true" utility function.

Rearrange to express CV in terms of $x^*(\tau)$, $c^*(\tau)$, $x^{**}$, and $c^{**}$.

Step 3: Differentiate CV with respect to $\tau$

To find the $\tau$ that maximizes CV, differentiate CV with respect to $\tau$ and set the derivative equal to zero: $\frac{dCV}{d\tau} = 0$

This will give us an equation in terms of $\tau$, $x^*(\tau)$, $c^*(\tau)$, $x^{**}$, $c^{**}$, $\alpha$, and $\beta$.

Step 4: Solve for $\tau$

Rearrange the equation from Step 3 to solve for $\tau$. This will give us the value of $\tau$ that maximizes the compensating variation.

Given the complexity of the utility functions and constraints, finding a closed-form solution for $\tau$ might be challenging. Depending on the specific forms of the functions, numerical methods might be required to solve for the optimal $\tau$.


## 2.

2.(a)
Given quasilinear utility, increasing $x_1$ by $\epsilon$ units will increase the utility by $\epsilon$.  $h(\vec{p}, \vec{u} + \epsilon)$ gives the bundle of goods that minimizes expenditure subject to achieving a utility level of $\vec{u} + \epsilon$. As bundle $x(\vec{p}, w)+\overrightarrow{\epsilon_1}$  achieves the utility level $\bar{u}+\epsilon$ while still minimizing expenditure (given the prices $\vec{p}$ ). it will now be the Hicksian demand for the utility level $\bar{u}+\epsilon$.  hence 
$$
x(\vec{p}, w)+\overrightarrow{\epsilon_1}=h(\vec{p}, \bar{u}+\epsilon)
$$
we need to show $x(\vec{p}, w)+\overrightarrow{\epsilon_1}$   minimize expenditure in more detail (Q1)

2.(b)
if Q1 (achieving utility change via x1 is optimal in terms of expenditure minimization)  is resolved, we can use (a) to argue (b) as any desired change of utility can be achieved by tweaking x1. 

2.(c)
The expenditure function gives the minimum expenditure required to achieve a certain utility level $\bar{u}$ given prices $\vec{p}$.
2. Quasilinear Utility:
Given our quasilinear utility function, the utility derived from $x_1$ is linear. This means that any increase in $\bar{u}$ can be achieved by a corresponding increase in $x_1$, given that the price of $x_1$ is 1 (as stated in the problem).
3. Effect of $\bar{u}$ on Expenditure:
For a quasilinear utility function, an increase in $\bar{u}$ by a certain amount will lead to an equivalent increase in expenditure on $x_1$ (since $p_1=1$ ). This is because the utility derived from $x_1$ is linear, so any desired increase in utility can be directly translated into an increase in expenditure on $x_1$.
4. Additive Separability:
Given the nature of the utility function, the expenditure required to achieve utility $\bar{u}$ can be broken down into two parts:
- The expenditure required to achieve the utility derived from $v\left(x_2, \ldots, x_L\right)$, which is $\tilde{e}(\vec{p})$.
- The expenditure on $x_1$ to achieve the remaining utility, which is $\bar{u}$ (since $p_1=1$ ).
Combining these two components, we get:
$$
e(\vec{p}, \bar{u})=\tilde{e}(\vec{p})+\bar{u}
$$

# 3. 
summation of CV over every participants is non-negative means $\sum w_i>\sum e\left(\vec{p}_1, v\left(\vec{p}_0, w_i\right)\right)$. As expenditure is the price vector multiplied to optimal bundle whose utility $\geq u_0$ , there exist wealth allocation that increases the utility than the current level. To be specific, set $\tilde{w_i} = p_i * x_i^{*}$ .

# 4.
![[Pasted image 20231003102717.png]]
### (a) Show that $V (\tilde{p}, w_{agg})$ is the optimal value of the SWF for the latter problem.

Given the social planner's problem over wealth, the objective is to maximize the social welfare function \( W \) subject to the aggregate wealth constraint. In the alternative problem, the objective is to maximize \( W \) subject to the aggregate expenditure constraint.

The indirect utility function v_n for consumer  n is the maximum utility they can achieve given prices $\tilde{p}$ and wealth $w_n$. Therefore, the value of the social welfare function when consumers are allocated wealth $w_n$ is: $W(v_1(\tilde{p}, w_1), \dots, v_N(\tilde{p}, w_N))$

This is equivalent to the value of the social welfare function when consumers are allocated bundles \( x_n \) that they would choose given their wealth allocations: $W(u_1(x_1), \dots, u_N(x_N))$

Where \( x_n \) is the bundle consumer \( n \) would choose given wealth \( w_n \) and prices \( \tilde{p} \).

Since the two problems are maximizing the same objective function subject to equivalent constraints (aggregate wealth in the first problem and aggregate expenditure in the second), the optimal values of the social welfare function for both problems are the same. Therefore: $V (\tilde{p}, w_{agg})$ is the optimal value of the SWF for the latter problem.

### (b)

Given: $\tilde{x}_n(\tilde{p}, w_{agg}) = x_n(\tilde{p}, w^*_n(\tilde{p}, w_{agg}))$, where $w^*_n(\tilde{p}, w_{agg})$ is the optimal wealth allocation for consumer \( n \) and $x_n(\tilde{p}, w)$ is the consumer's Marshallian demand function. By definition, the Marshallian demand function gives the bundle that maximizes a consumer's utility given prices and wealth. Therefore, the bundle $x_n(\tilde{p}, w^*_n(\tilde{p}, w_{agg}))$ is the one that maximizes consumer n 's utility given prices $\tilde{p}$ and their optimal wealth allocation $w^*_n(\tilde{p}, w_{agg})$. Thus, $\tilde{x}_n(\tilde{p}, w_{agg})$ is the optimal consumption bundle for consumer \( n \) given prices $\tilde{p}$ and aggregate wealth $w_{agg}$.

### (c) Implications for a social planner wishing to optimize \( W \):

social planner need not control consumption directly but need only distribute wealth optimally and allow consumers to make consumption decision indecently given price p. To be specific
1. The results show that the social planner can achieve the same level of social welfare by either allocating wealth or directly allocating consumption bundles to consumers.
2. If the social planner knows the consumers' preferences and the price vector, they can determine the optimal wealth allocations that will lead to the desired consumption bundles.
3. The social planner does not need to know the details of each consumer's utility function or solve each consumer's utility maximization problem. Instead, they can use the indirect utility functions and Marshallian demand functions to determine the optimal allocations.
4. This simplifies the social planner's problem and allows for a more tractable solution. (or can make the optimization problem more parallel as we can solve in individual level simultaneously)



## appendix
proof of study session!

![[Pasted image 20231002110111.png]]