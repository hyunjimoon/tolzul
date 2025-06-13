
### A.1 Step 1 — Linear-Quality (Two Bernoulli) Model  

#### A.1.1 Notation  
| Symbol | Meaning |
|--------|---------|
| $q\in[0,1]$ | product quality (decision variable) |
| $P_c(q)=q$ | probability customer commits |
| $P_r(q)=1-q$ | probability resource partner commits |
| $C_u$ | unit under-stock (opportunity) cost |
| $C_o$ | unit over-stock cost |
| $V$   | bonus value when both commit |

#### A.1.2 Expected Loss Function  
Only one mismatch cost can realise in any outcome.  Enumerating the four states:

$L(q)=C_u\,P_c(1-P_r)+C_o\,P_r(1-P_c)-V\,P_cP_r =C_u q^{2}+C_o(1-q)^{2}-V q(1-q).$

#### A.1.3 Convexity  
$L''(q)=2(C_u+C_o+V)>0\ \Longrightarrow\ L(q)\ \text{strictly convex}.$

#### A.1.4 Unique Optimum  
Set $L'(q)=0$:

$2(C_u+C_o+V)q-(2C_o+V)=0\quad\Longrightarrow\quad q^{*} = \frac{V+2C_o}{2(C_u+C_o+V)}.$

#### A.1.5 Comparative Static w.r.t. $V$  

$\frac{\partial q^{*}}{\partial V}      =\frac{C_u-C_o}{2(C_u+C_o+V)^{2}}.$

*Interpretation:* $q^{*}$ increases in $V$ iff $C_o<C_u$ and decreases if $C_o>C_u$ (see cost-asymmetry discussion in Section 2).
