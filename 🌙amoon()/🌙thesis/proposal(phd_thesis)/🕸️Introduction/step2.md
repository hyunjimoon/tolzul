
### A.2 Step 2 — Non-Linear Quality (Sigmoid Commitments)  

#### A.2.1 Notation  
| Symbol                                | Meaning                    |
| ------------------------------------- | -------------------------- |
| $q\in[0,1]$                           | product quality            |
| $P_c(q)=\dfrac{1}{1+e^{-\beta_c* q}}$ | customer sigmoid           |
| $P_r(q)=\dfrac{1}{1+e^{\ \beta_r*q}}$ | partner sigmoid (mirrored) |
| $\beta_c,\beta_r>0$                   | steepness parameters       |
| $\theta_c,\theta_r\in(0,1)$           | inflection points          |
| Other symbols $C_u,C_o,V$ as before   |                            |

We write the derivatives  
$P_c'(q)=\beta_cP_c(1-P_c)$ and $P_r'(q)=-\beta_rP_r(1-P_r)$ for later use.

#### A.2.2 Expected Loss Function  

$L(q)=C_uP_c(1-P_r)+C_oP_r(1-P_c)-V P_cP_r.$

#### A.2.3 Monotone-Difference Form of the Gradient  


$$
L'(q)
&=\beta_cP_c(1-P_c)\bigl[C_u(1-P_r)-C_oP_r-VP_r\bigr]  \\
&\quad+\beta_rP_r(1-P_r)\bigl[C_uP_c-C_o(1-P_c)+VP_c\bigr].
\tag{A.1}
$$

The two bracketed terms are strictly decreasing and increasing in $q$,
respectively, while the sigmoid prefactors are strictly positive on $(0,1)$.

#### A.2.4 Uniqueness of the Optimum  

Because (A.1) is a weighted sum of functions with opposite monotonicity,
$L'(q)$ can cross zero **at most once**.  Since $L'(0)<0$ and $L'(1)>0$,
it crosses exactly once, implying strict quasi-convexity and a unique minimiser
$q^{\dagger}\in(0,1)$.

#### A.2.5 Comparative Static w.r.t. $V$  

Implicit differentiation of $L'(q^{\dagger},V)=0$ gives  

$\frac{\partial q^{\dagger}}{\partial V}=-\frac{\partial L'/\partial V}{\partial L'/\partial q}$

Denominator $>0$ by quasi-convexity.  Evaluating the numerator at the root of $L'(q)$ yields $(C_u-C_o)\,[\beta_cP_c(1-P_c)+\beta_rP_r(1-P_r)]$, again delivering $\operatorname{sgn}(\partial q^{\dagger}/\partial V)=\operatorname{sgn}(C_u-C_o)$.
