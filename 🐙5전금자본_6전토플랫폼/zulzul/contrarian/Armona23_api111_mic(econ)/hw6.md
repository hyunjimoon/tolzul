
## 1. 
### A)
![[Pasted image 20231130120235.png]]
when consumer when consumer 1($O_1$) is given more $x_2$, the overall amount of $x_2$ in the economy increases. The length of $X_2$ axis increases. As a result, while $O_2$ 's endowment is unchanged it's indifference curve shifts up. $O_1$'s  indifference curve doesn't change so it's no longer on equilibrium. As utilities are quasilinear, slopes only depend on X2, indifference curves are horizontal shifts of each other. 

To get to a new equilibrium, shifting indifference curve of both $\mathrm{O}_1,  \mathrm{O}_2$ to the right would lead to the budget line not being tangent regardless of price. A new equilibrium could look like lines in blue. O1's indifference shifts left so their utility is lower.

### B) 
Since O1 has 0 endowment of $O_{1}$. O2 has a monopoly over $O_{1}$, and they "set" pries to mere 0 is demand is elastic.

### C)
mis is to edgewerth box with original endowment, price, and production set more consumption of $x_{2}$ will be equal.
![[Pasted image 20231130131521.png]]

Knowing that in quasilinear cases $\frac{\partial u}{\partial x_{2}}=P$ will always be constant across the pareto set and consumption of x2 will be equal under any transfer. the endowment would shift right from E0 to E1 but the slope of the budget line will be the same. Because of monotone preferences, we know that E1 will be preferred to E0.

## 2. 
happiness function is sufficient summary statistics of one's utility function, meaning happiness $h(x_i)$ as a statistics of $n$th consumer's consumption (which is input for altruistic utility function) holds the same amount of information as $x_i$ the original consumption.  

we need to understand the concept of Pareto optimality and apply it to both utility functions.

An allocation $\{x_i\}$ is Pareto optimal if there is no other feasible allocation $\{y_i\}$ such that at least one individual is better off and no individual is worse off. to show that if an allocation $\{x_i\}$ is Pareto optimal with respect to the altruistic utility function $u_i(x_1, \ldots, x_N) = u_i(h_1(x_1), \ldots, h_N(x_N))$, then $\{x_{1..N}\}$ is also Pareto optimal with respect to the happiness function, we need to show the inexistence of feasible allocation ${y_i^u}$ that is better off for one person without making the others worse off in terms of altruistic function)( i.e. $\not\exists$ ${y_{1..N}^u}$  s.t. $u_1(y_1^u) > u_1(x_1^u), u_2(y_2^u) \geq u_1(x_2^u), ... ,  u_N(y_N^u) \geq u_1(x_N^u)$ ) implies the inexistence of feasible allocation ${y_i^h}$ that is better off for one person without making the others worse off in terms of happiness function (i.e. $\not\exists$ ${y_{1..N}^h}$  s.t. $u_1(y_1^h) > u_1(x_1^h), u_2(y_2^h) \geq u_1(x_2^h), ... ,  u_N(y_N^h) \geq u_1(x_N^h)$).

It is easier to prove the existence, so let us use proof by contradiction. meaning instead of assuming nonexistence, assume existence of allocation that makes happiness function better off without making the others worse off in terms of happiness function. using this, disprove that x is pareto optimal. Specifically,
1. **Assumption for Contradiction**: Assume there exists a feasible allocation $\{y_i^h\}$ such that $h_j(y_j^h) > h_j(x_j^h)$ for some $j$ and $h_k(y_k^h) \geq h_k(x_k^h)$ for all $k \neq j$. This means at least one individual is better off in terms of happiness, and no one is worse off.
2. **Implication for Altruistic Utility**: Given the relationship between $u_i$ and $h_i$, the improvement in $h_j$ implies an improvement in $u_j$, i.e., $u_j(y_j^h) > u_j(x_j^h)$. Since no one's happiness decreases, no one's utility decreases either, i.e., $u_k(y_k^h) \geq u_k(x_k^h)$ for all $k \neq j$.
3. **Contradiction**: This finding contradicts our initial assumption that $\{x_i\}$ is Pareto optimal with respect to $u_i$. If $\{x_i\}$ were truly Pareto optimal, there could not exist any other allocation $\{y_i^h\}$ that makes at least one individual strictly better off without making anyone worse off.
4. **Conclusion**: Therefore, our initial assumption must be false. It is not possible for there to exist a feasible allocation $\{y_i^h\}$ that improves the happiness of at least one individual without reducing the happiness of others. Hence, if $\{x_i\}$ is Pareto optimal with respect to the altruistic utility function, it must also be Pareto optimal with respect to the happiness function $h_i$.

(b) 
CORRECT ANSWER SHOULD SUGGEST COUNTER EXAMPLE, but below I described some logic behind why we CANNOT use altruists's happiness function based utility to find competitive equilibrium.

if h is identity function, we can use welfare thm1 to bring competitive equilibrium to pareto equilibrium (since  pareto equilibrium for x and  pareto equilibrium for h(x) are the same).

Suppose N = 2 and the economy is an exchange economy (edgeworth box). Determine whether the altruists could could use a competitive equilibrium to obtain a pareto optimal allocation.
interdependence of utility may create some challenge. consider an exchange economy with two individuals, $A$ and $B$, each with altruistic preferences. let's analyze whether a competitive equilibrium in this setting can lead to a Pareto optimal allocation. With $\omega_A$ and $\omega_B$ be the initial endowments of goods for individuals $A$ and $B$, altruistic utility functions are $U_A(x_A, x_B)$ for individual $A$ and $U_B(x_A, x_B)$ for individual $B$ where $x_A$ and $x_B$ are the consumption bundles of $A$ and $B$, respectively.

In a competitive equilibrium, each individual maximizes their utility subject to their budget constraint, and the market clears i.e.
1. $\max U_A(x_A, x_B)$ subject to $p \cdot x_A \leq p \cdot \omega_A$
2. $\max U_B(x_A, x_B)$ subject to $p \cdot x_B \leq p \cdot \omega_B$
   where $p$ is the vector of prices.
3. $x_A + x_B = \omega_A + \omega_B$

$(x_A^*, x_B^*)$ is Pareto optimal if there is no other feasible allocation $(x_A, x_B)$ such that $U_A(x_A, x_B) \geq U_A(x_A^*, x_B^*)$ and $U_B(x_A, x_B) \geq U_B(x_A^*, x_B^*)$ with at least one strict inequality.

In standard settings, competitive equilibria are Pareto optimal due to the First Welfare Theorem. However, this theorem assumes that individuals' utilities are independent of each other which is not the case for altrustic utility. Interdependence might prevent the competitive equilibrium from being Pareto optimal. Also, when marginal rate of substitution (MRS) between goods for each individual are the same and also equal to the ratio of prices, solving utility maximization (lagrangian) in competitive equilibrium lead to Pareto optimal.

Let's consider a simple case with two goods $x$ and $y$ for both individuals. The MRS for individual $A$ is:

$MRS_{xy}^A = -\frac{\partial U_A / \partial x_A}{\partial U_A / \partial y_A}$

However, since $U_A$ depends on both $x_A$ and $x_B$, this derivative is also a function of $x_B$. Similarly, for $B$:

$MRS_{xy}^B = -\frac{\partial U_B / \partial x_B}{\partial U_B / \partial y_B}$

which is a function of $x_A$.

In a standard model, the MRS for each individual is independent of the other's consumption, making it straightforward to align each individual's MRS with the price ratio. However, in the case of altruistic preferences, the interdependence of utilities means that the MRS for one individual is affected by the consumption choices of the other. This interdependence can prevent the MRS of the two consumers from easily aligning with the price ratio, complicating the attainment of a competitive equilibrium that is also Pareto optimal. The specific outcome depends on the exact functional forms of the altruistic utility functions and how they interact with each other's consumption choices.

## 3. GE and Taxes
two goods (L, C), two agents (consumer, firm), endowment of labor is 1.
utility of consumes: $u(c, e)=\log (c)+\log (1-c)$, producer functions: $f(c)=\sqrt{l}$ ,  
 leisure enjoyed by consumer is $1-l$ and firm is owned by consumer

A) Solve firm PMP

$$
\begin{aligned}
& \max _{L C} f(L) \cdot P_{C}-P_{L} L \\
& =\sqrt{L} \cdot P_{C}-P_{L} L \\
& \frac{\partial \mathbf{L}}{\partial L}=P_{C} \cdot \frac{1}{2} L^{-1 / 2}-P_{L}=0 \\
& P_{C}\left(L^{-1 / 2}\right)=P_{L} \\
& L^{-12}=\left(\frac{2 P_{L}}{P_{C}}\right)^{-2} \\
& L_{j}^{*}=\frac{P_{c}^{2}}{4 P_{L}^{2}} \\
& \operatorname{Given} C_{j}^{+}=f(L)= \sqrt{L} \\
& c_{j}^{*}=\sqrt{\frac{P_{C}^{2}}{4 P_{L}^{2}}}=\frac{P_{C}}{2 P_{L}}
\end{aligned}
$$

B) Set up UMP 

Since the budget constraint binds,

$$
\begin{aligned}
& =\log (c)+\log (1-L)+\lambda\left[p_{c} \cdot Q_{c}^{\prime}+\phi^{\prime}(p \cdot y(p))-p_{c} c-p_{L}(1-L)\right] \\
& =\log (c)+\log (1-L)+\lambda(\pi-p_{C}+p_{L} L).
\end{aligned}
$$

solve for $C^{*}$and $L^{*}$ :

$$
\begin{aligned}
& \frac{d f}{d c}=\frac{1}{c} \cdot \lambda P C=0 \rightarrow \lambda=\frac{1}{C P C} \\
& P_{C C}=P_{L}(1-2) \\
& \frac{\partial f}{\partial l}=-\frac{1}{1-L}+\lambda P_{L}=0 \rightarrow \lambda=\frac{1}{P_{L}(1-L)} \\
& c_{i}^{*}=\frac{P_{h}(1-L)}{P_{c}}
\end{aligned}
$$

solve for $L^*$ by plugging $C^*$ into budget contstraint

$$
\begin{aligned}
& \pi=P_L\left[\frac{P_{L}(1-L)}{P_{L}}\right]+P_{L} L=0 \\
& \pi-P_{L}+2 P_{L} L=0 \\
& L_i^*=\frac{P_{L}-\pi}{2 P_{L}}
\end{aligned}
$$



$$
\begin{aligned}
C_{i}^{*} & =\frac{P_{L}}{P_{L}}\left[1-\left[\frac{P_{L}-\pi}{2 P_{L}}\right]\right] \\
& =\frac{P_{C}}{P_{C}}\left[\frac{2 P_{L}+\pi-P_{L}}{2 P_{C}}\right] \\
C_{i}^{*} & =\frac{P_{L}+\pi}{2 P_{C}}
\end{aligned}
$$

substituting $\pi$ :

$$
\begin{array}{rlr}
\pi & =P_{C} C_{s}^{*}-P_{L} L_{s}^{*} \\
& =P_{C}\left[\frac{P_{C}}{2 P_{L}}\right]-P_{C}\left[\frac{P_{C}^{2}}{4 P_{L}^{2}}\right] \\
& =\frac{2 P_{C}^{2}-P_{c}^{2}}{4 P_{L}} \\
\pi & =\frac{P_{C}^{2}}{4 P_{L}} \\
L_{i}^{*} & =\frac{P_{1}}{2 P_{L}}-\left(\frac{P_{C}^{2}}{4 P_{L}}\right)\left(\frac{1}{2 P_{L}}\right) & C_{i}^{*}=\frac{P_{1}}{2 P_{C}}+\left(\frac{P_{C}^{2}}{4 P_{L}}\right)\left(\frac{1}{2 P_{C}}\right) \\
& =\frac{4 P_{L}^{2}}{8 P_{L}^{2}}-P_{C^{2}} & =\frac{4 P_{2}^{2}+P_{C}^{2}}{8 P_{L} P_{C}}
\end{array}
$$
c) solve for equillibrium price

Normalize $P_{C}=1$, so we any have $P_{L}$ (wage).

Find market clearing price for consumption is just equal to demand and supply of consumption since we nave 1 producer and 1 firm and no endowment.

$$
\begin{aligned}
& \frac{1}{2 P L}=\frac{4 P_{L}^{2}+1}{48 P_{L}} \\
& 4=4 P_{L}^{2}+1 \\
& 3=4 P_{L}^{2} \\
& P_{L}^{*}=\left(\frac{3}{4}\right)^{1 / 2}
\end{aligned}
$$

D) Solve for equilibrium $L_{i}^{*}$ and $C_{i}^{*}$

Plug in $P_{L}^{*}$ and $P_{C}^{*}$ into $L_{i}^{*}$ and $C_{i}^{*}$ find above:

$$
\begin{aligned}
c_{i}^{*} & =\frac{4(3 / 4)+1}{8(3 / 4)^{1 / 2}} \\
& =\frac{1}{2 \sqrt{3 / 4}}=0.58 \\
L_{i}^{*} & =\frac{4(3 / 4)-1}{8(3 / 4)}=\frac{2}{6}=\frac{1}{3}
\end{aligned}
$$

E) Snow how social planner problem (max $U(L, C)$ st. tech Constrain) leads to some $L^{*}$ and $C^{*}$

Max $\log (c)+\log (1-L)$ st. $f(L) \geq C$ and $L \leqslant 1$

$$
\begin{aligned}
& \mathcal{L}=\log (c)+\log (1-L)+\lambda(\sqrt{L}-C) \\
& \frac{d f}{d c}=\frac{1}{c}-\lambda=0 \quad \lambda=\frac{1}{c} \\
& \frac{\partial L}{\partial L}=-\frac{1}{1-L}+\frac{1}{2} L^{-1 / 2} \lambda=0 \quad \lambda=\frac{\partial}{1-L}\left(L^{-1 / 2}\right) \\
& \frac{1}{C}=\frac{a L^{1 / 2}}{1-L} \\
& C^{*}=\frac{1-1}{2 L^{1 / 2}} \\
& L^{*}: \quad L^{\prime / 2}-\left[\frac{1-L}{2 L / 2}\right]=0 \\
& L^{12}=\frac{1-L}{2 L^{1 / 2}} \\
& 2 L=1-L \\
& 3 L=1 \\
& L^{*}=1 / 3 \\
& C^{*}=\frac{1-1 / 3}{2 \sqrt{1 / 3}}=\frac{2}{3 \bar{x} \sqrt{7 / 3}} \\
& =\frac{1}{3 \sqrt{1 / 3}} \approx 0.58
\end{aligned}
$$

F) Introduce tax on labor
(got tired of typing so the solutions are going to be shortened... sorry🥲)
Market cleaning conditions same as before, except: labor supplied at $(\omega(1-\tau)$ : labor demanded at w)
- Tax revenue: Nat given back to cosies/ produces (would enos ins budget constraint, but weir igniting for now)

Since the budget constraint binds, ne con uni problem as:

$$
\begin{aligned}
& \log (c)+\log (1-e)+\lambda\left[P C \cdot a_{f}+e(p f(p))-p C-P(T-L)\right] \text { *NOW } P_{2}=\omega(1-T) \\
& \log (c)+\log (1-L)+\lambda\left[\pi-P_{C} C+\omega(1-r) L\right]
\end{aligned}
$$

solve fo $C^{+}$and $L^{*}$ by substituting $\omega(1-r)=P_{L}$ :

$$
\begin{aligned}

& L_{i}{ }^{*}=\frac{\omega(1-r)-\pi}{2 P L}=\frac{\omega-T_{W}-\pi}{2 P L} \\
& C_{i}{ }^{*}=\frac{\omega(1-r)+\pi}{2 P C}=\frac{\omega-T \omega+\pi}{2 P C}
\end{aligned}
$$

$\pi$  is the same as only consumers face tax:

$$
\begin{aligned}
& L_{1}^{*}=\frac{4 P_{1}^{2}-P_{c}^{2}}{8 P_{L}{ }^{2}}: \frac{4(\omega(1-r))^{2}-P_{C^{2}}}{8(\omega(1-r))^{2}} \\
& C_{1}^{*}=\frac{4 P_{L^{2}}{ }^{2}+P_{c}{ }^{2}}{8 P_{L} P_{C}}=\frac{4(\omega(1-r))^{2}+P_{C}{ }^{2}}{8(\omega(1-r)) P_{C}}
\end{aligned}
$$

solve for $w^{*}$ based on normalized price

$$
\begin{aligned}
& w=\left(\frac{2(1-T)^{2}+1}{4(1-T)^{2}}\right)^{1 / 2} \text { when } T=0 \; \text {same answer as above } 
\end{aligned}
$$

g) estimate $dc/d\tau$

- calculate eq. $C^{*}$ by plugging eq. $w$ into aggregate demand equals aggregate demand constraint. $C_{S}$ and $C_{D}$ accounting for $w^{*}$ :

$$
\begin{aligned}
& \frac{\partial c}{\partial t}\left[\frac{1}{2 W}=\frac{4 w^{2}+1}{8 W}\right] \\
& c=\frac{1}{2 W}=\frac{1}{\alpha}\left(\frac{4(1-T)^{2}}{2(1-T)^{2}+1}\right)^{1 / 2} \\
& \frac{\partial c}{\partial t}=-\frac{1-t}{(1-t)\left(2(1-t)^{2}+1\right)^{3 / 2}}
\end{aligned}
$$

which is negative

h) $\frac{\partial c}{\partial y} \cdot \frac{y}{c} \quad w=\left(\frac{2(1-T)^{2}+1}{4(1-T)^{2}}\right)^{1 / 2}$

$$
\begin{aligned}
& L=\frac{1}{4 w^{2}}=\frac{1}{4\left(\frac{2 y^{2}+1}{4 y^{2}}\right)}=\frac{y^{2}}{2 y^{2}+1} \\
& \frac{\partial L}{\partial y}=\frac{2 y}{(2 y+1)^{2}} \\
& \frac{2 y}{\left(2 y^{2}+1\right)^{2}} \cdot y \cdot \frac{2 y^{2}+1}{y^{2}}=\frac{2}{2 y^{2}+1}
\end{aligned}
$$

i) Evaluate at $y=1$

$$
\begin{aligned}
& \frac{\partial L}{\partial y} \cdot y=\frac{2}{3} \\
& \frac{\partial c}{\partial y} \cdot \frac{y}{c}=\frac{4}{9}
\end{aligned}
$$


## 4

(a) $\max p \cdot q_{j}-c\left(q_{j}, \theta\right)$ st. $Q=\sum_{k=1}^{n} Q_{k}$

FOC: $p-c_{q_{j}}^{\prime}\left(q_{j}, \theta\right)-c_{i}\left(q_{j}, \theta \right)=0$

Unique equilibrium output: Apply some " $q$ " for all firms $q^{*} \cdot J=Q^{*} \Rightarrow q^{*}=\frac{Q^{*}}{J}$

FOC: $P=C_{Q_{j}}^{\prime}\left(\frac{Q^{*}}{J}, Q^{*}\right)+C_{Q}\left(\frac{Q^{*}}{J}, Q^{*}\right)$

We assume that $C_{i}>0$ and $C_{a}^{\prime}<0$ and $i_{q_{1}}+J \cdot C_{Q}^{\prime}>0$.

This implies that $c_{i_{j}}+c_{Q}^{\prime}>0$, so there exists a unique solution when $P>0$.

(b) Maximize Total Social Surplus:

Let $P(x)$ be the inverse aggregate demand function

$$
\operatorname{Max}_{q} \text { Surplus }=\int_{0}^{Q} P(x) d x-\sum_{j=1}^{\sigma} c\left(q_{j}, Q\right)
$$

First Order Condition:

$$
\begin{aligned}
& \frac{d[\text { Surplus] }}{d q_{j}}=P(Q)-C_{q_{j}}^{\prime}\left(q_{j}, Q\right)-\underbrace{J}_{j=1} C_{Q}\left(q_{j}, Q\right)=0 \\
& \text { Optimal Level of Output: }
\end{aligned}
$$

$$
\begin{aligned}
J \cdot q^{*} & =Q^{*} \\
q^{*} & =\frac{Q^{*}}{J}
\end{aligned}
$$

FOC

$$
P\left(Q^{*}\right)=C_{q_{j}}^{\prime}\left(\frac{Q^{+}}{q}, Q^{*}\right)+J \cdot C_{Q}^{\prime}\left(\frac{Q^{*}}{q}, Q^{*}\right)
$$

as $C_{2 j}^{\prime}+J \cdot C_{2}^{\prime}>0$, so there exists a solution for $P\left(Q^{*}\right)$.

(c)
a -> $P_a=C_{q_j}^{\prime}\left(\frac{Q^*}{J}, Q^*\right)+C_Q^{\prime}\left(\frac{Q}{J}, Q^*\right)$
b-> $P_{b}=C_{q_{j}}\left(\frac{a^{*}}{q}, a^{*}\right)+J \cdot C_{Q}^{\prime}\left(\frac{Q^{*}}{q}, a^{*}\right)$ 
$\left.P_{a}-P_{b}=(1-J) C_{Q}^{\prime}\left(\frac{Q^{*}}{J}, Q^{+}\right)\right]$ should be the subsidy
