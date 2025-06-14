## Appendix A.0 Step 0 — Classic Newsvendor Model

| Symbol              | Interpretation                        |
| ------------------- | ------------------------------------- |
| $q\in\mathbb R_{+}$ | order quantity (decision)             |
| $D$                 | stochastic demand with CDF $F(\cdot)$ |
| $p,c$               | selling price / purchase cost         |

### A.0.1 Expected Cost

$\operatorname{EC}(q)=c\int_{0}^{q}(q-x)\,f(x)\,dx \;+\;(p-c)\int_{q}^{\infty}(x-q)\,f(x)\,dx .$

### A.0.2 Optimal Quantity (Critical Fractile)

$q^∗=\frac{p−c}{p}$

### A.0.3 Business Intuition

_Balance_ overage and opportunity loss. A higher gross margin $(p-c)$ shifts the critical fractile upward, justifying more aggressive stocking.

---

## Appendix A.1 Step 1 — Linear‑Quality Commitments

|Symbol|Interpretation|
|---|---|
|$q!\in![0,1]$|product quality (decision)|
|$P_c(q)=q$|customer commitment probability|
|$P_r(q)=1-q$|resource‑partner commitment probability|
|$C_u,C_o$|under‑ / over‑mismatch unit costs|
|$V$|match bonus when both commit|

### A.1.1 Expected Loss

|                                         | $\color{skyblue}{Q}=0$ (partner absent)                                  | $\color{skyblue}{Q}=1$ (partner present)                               |
| --------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| $\color{skyblue}{D}=1$ (customer shows) | $\color{red}{q}^{2}$&nbsp;⟶ **shortage** incurs *opportunity* cost $C_u$ | $(1-\color{red}{q})\color{red}{q}$&nbsp;⟶ **match** gains value $+V$   |
| $\color{skyblue}{D}=0$ (no customer)    | $\color{red}{q}(1-\color{red}{q})$&nbsp;⟶ **match** (no cost)            | $(1-\color{red}{q})^{2}$&nbsp;⟶ **excess** incurs *overage* cost $C_o$ |


$L(q)=C_uq^{2}+C_o(1-q)^{2}-Vq(1-q).$

### A.1.2 Optimal Quality

$$
q^{*}=\frac{V+2C_o}{2\,(C_u+C_o+V)},
$$


---

## Appendix A.2 Step 2 — Non‑Linear (Sigmoid) Commitments

| Symbol                                            | Meaning              |
| ------------------------------------------------- | -------------------- |
| $q\in[0,1]$                                       | quality              |
| $P_c(q)=\dfrac{e^{\beta_c q}}{1+e^{\beta_c q}}$   | customer sigmoid     |
| $P_r(q)=\dfrac{e^{-\beta_r q}}{1+e^{-\beta_r q}}$ | partner sigmoid      |
| $\beta_c,\beta_r >0$                              | steepness parameters |
| other symbols                                     | as in Step 1         |

### A.2.1 Expected Loss

$L(q)=C_uP_c(1-P_r)+C_oP_r(1-P_c)-V\,P_cP_r.$

### A.2.2 Optimal Quality

$L(q)$ is strictly quasi‑convex; its derivative crosses zero **once**, so the unique minimiser $q^{\dagger}$ is found by root‑solving $L'(q)=0$.

## 3. Updated ## Appendix A.2 Step 2

## Appendix A.2 Step 2 — Non-Linear (Sigmoid) Commitments

|Symbol|Meaning|
|---|---|
|$q \in \mathbb{R}$|quality level (decision)|
|$P_c(q) = \frac{1}{1+e^{-q}}$|customer commitment probability|
|$P_r(q) = \frac{1}{1+e^{q}}$|partner commitment probability|
|$C_u, C_o$|under-/over-mismatch unit costs|
|$V$|match bonus when both commit|

### A.2.1 Expected Loss

$$L(q) = C_u P_c(q)[1-P_r(q)] + C_o P_r(q)[1-P_c(q)] - V P_c(q)P_r(q)$$

### A.2.2 Optimal Quality

The first-order condition $L'(q) = 0$ yields:

$$C_u P_c(1-P_c)(1-P_r) - C_u P_c P_r(1-P_r) + C_o P_r(1-P_r)(1-P_c) - C_o P_r P_c(1-P_c) - V P_c(1-P_c)P_r - V P_c P_r(1-P_r) = 0$$

Factoring and simplifying with $P_c = \frac{e^{-q}}{1+e^{-q}}$ and $P_r = \frac{1}{1+e^{-q}}$:

$$P_c(V + 2C_o) = P_r(V + 2C_u)$$

Substituting the sigmoid forms and solving:

$$q^* = \ln\left(\frac{2C_o + V}{2C_u + V}\right)$$

This closed-form solution exists due to the symmetric responsiveness parameters ($\beta_c = 1, \beta_r = -1$).

----

### A.3 Step 3 — Joint Quality–Quantity Model  

#### A.3.1 Additional Notation  
| Symbol                    | Meaning                                     |
| ------------------------- | ------------------------------------------- |
| $Q\ge0$                   | production quantity (new decision)          |
| $R(Q)=aQ-bQ^{2}$, $a,b>0$ | diminishing-return revenue when both commit |
| other symbols             | as in Step 1                                |

#### A.3.2 Expected Profit  

$\Pi(q,Q)= R(Q)P_c(q)P_r(q)        -C_uP_c(q)\bigl[1-P_r(q)\bigr] -C_oP_r(q)\bigl[1-P_c(q)\bigr]$

#### A.3.3 Optimising Quantity for Fixed Quality  

$\frac{\partial \Pi}{\partial Q}=aP_cP_r-2bQP_cP_r =P_cP_r\bigl(a-2bQ\bigr)=0\ \Rightarrow\ Q^{*}=\frac{a}{2b}.$

This vertex is independent of $q$.

#### A.3.4 Reduced One-Dimensional Quality Problem  

Substituting $Q^{*}$ drops $Q$ from all mismatch terms and scales the revenue
coefficient by $P_cP_r$:

$\max_{q\in[0,1]}\Bigl[\tfrac{a^{2}}{4b}P_c(q)P_r(q)-C_uP_c(1-P_r)-C_oP_r(1-P_c)\Bigr].$

The maximiser satisfies the *same* first-order condition $L'(q)=0$ derived in
Step 2, so $q^{\dagger}$ and all its comparative statics carry over.
 