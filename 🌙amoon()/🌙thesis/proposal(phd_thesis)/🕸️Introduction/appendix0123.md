- [[#Appendix A.0 Step 0 — Classic Newsvendor Model|Appendix A.0 Step 0 — Classic Newsvendor Model]]
	- [[#Appendix A.0 Step 0 — Classic Newsvendor Model#A.0.1 Expected Cost|A.0.1 Expected Cost]]
	- [[#Appendix A.0 Step 0 — Classic Newsvendor Model#A.0.2 Optimal Quantity (Critical Fractile)|A.0.2 Optimal Quantity (Critical Fractile)]]
	- [[#Appendix A.0 Step 0 — Classic Newsvendor Model#A.0.3 Business Intuition|A.0.3 Business Intuition]]
- [[#Appendix A.1 Step 1 — Linear‑Quality Commitments|Appendix A.1 Step 1 — Linear‑Quality Commitments]]
	- [[#Appendix A.1 Step 1 — Linear‑Quality Commitments#A.1.1 Expected Loss|A.1.1 Expected Loss]]
	- [[#Appendix A.1 Step 1 — Linear‑Quality Commitments#A.1.2 Optimal Quality|A.1.2 Optimal Quality]]
- [[#Appendix A.2 Step 2 — Non‑Linear (Sigmoid) Commitments|Appendix A.2 Step 2 — Non‑Linear (Sigmoid) Commitments]]
	- [[#Appendix A.2 Step 2 — Non‑Linear (Sigmoid) Commitments#A.2.1 Expected Loss|A.2.1 Expected Loss]]
	- [[#Appendix A.2 Step 2 — Non‑Linear (Sigmoid) Commitments#A.2.2 Optimal Quality|A.2.2 Optimal Quality]]
- [[#3. Updated ## Appendix A.2 Step 2|3. Updated ## Appendix A.2 Step 2]]
- [[#Appendix A.2 Step 2 — Non-Linear (Sigmoid) Commitments|Appendix A.2 Step 2 — Non-Linear (Sigmoid) Commitments]]
	- [[#Appendix A.2 Step 2 — Non-Linear (Sigmoid) Commitments#A.2.1 Expected Loss|A.2.1 Expected Loss]]
	- [[#Appendix A.2 Step 2 — Non-Linear (Sigmoid) Commitments#A.2.2 Optimal Quality|A.2.2 Optimal Quality]]
- [[#Appendix A.3 Step 3 — General Sigmoid with Arbitrary $β$ Parameters|Appendix A.3 Step 3 — General Sigmoid with Arbitrary $β$ Parameters]]
	- [[#Appendix A.3 Step 3 — General Sigmoid with Arbitrary $β$ Parameters#A.3.1 Expected Loss|A.3.1 Expected Loss]]
	- [[#Appendix A.3 Step 3 — General Sigmoid with Arbitrary $β$ Parameters#A.3.2 First-Order Condition|A.3.2 First-Order Condition]]
	- [[#Appendix A.3 Step 3 — General Sigmoid with Arbitrary $β$ Parameters#A.3.3 Special Limits — Closed-Form Solutions|A.3.3 Special Limits — Closed-Form Solutions]]
		- [[#A.3.3 Special Limits — Closed-Form Solutions#1. Symmetric Responsiveness ($β_c=β_r=β$)|1. Symmetric Responsiveness ($β_c=β_r=β$)]]
		- [[#A.3.3 Special Limits — Closed-Form Solutions#2. Customer-Dominant Responsiveness ($β_c\gg β_r$)|2. Customer-Dominant Responsiveness ($β_c\gg β_r$)]]
		- [[#A.3.3 Special Limits — Closed-Form Solutions#3. Partner-Dominant Responsiveness ($β_r\gg β_c$)|3. Partner-Dominant Responsiveness ($β_r\gg β_c$)]]
		- [[#A.3.3 Special Limits — Closed-Form Solutions#4. High-Match-Value Limit ($V\gg C_u,C_o$)|4. High-Match-Value Limit ($V\gg C_u,C_o$)]]


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


## Appendix A.3 Step 3 — General Sigmoid with Arbitrary $β$ Parameters

| Symbol                                      | Meaning                                           |
|---------------------------------------------|---------------------------------------------------|
| $q\in\mathbb R$                             | quality level (decision)                          |
| $P_c(q)=\dfrac1{1+e^{-β_c q}}$               | customer commitment probability                   |
| $P_r(q)=\dfrac1{1+e^{+β_r q}}$               | partner commitment probability                    |
| $β_c,β_r>0$                                 | steepness of each sigmoid                         |
| $C_u,C_o,V>0$                               | under-commit cost; over-commit cost; match bonus  |

### A.3.1 Expected Loss

We define
$$
L(q)
= C_u\,P_c(q)\bigl[1 - P_r(q)\bigr]
+ C_o\,P_r(q)\bigl[1 - P_c(q)\bigr]
- V\,P_c(q)\,P_r(q).
$$

### A.3.2 First-Order Condition

1. Compute the derivatives
   $$
   P_c'(q) = β_c\,P_c(1-P_c),
   \quad
   P_r'(q) = -β_r\,P_r(1-P_r).
   $$
2. Differentiate $L(q)$ term-by-term:
   $$
   \frac{d}{dq}\bigl[C_uP_c(1-P_r)\bigr]
   = C_u\bigl[P_c'(1-P_r) - P_c\,P_r'\bigr],
   $$
   $$
   \frac{d}{dq}\bigl[C_oP_r(1-P_c)\bigr]
   = C_o\bigl[P_r'(1-P_c) - P_r\,P_c'\bigr],
   $$
   $$
   \frac{d}{dq}\bigl[-V\,P_cP_r\bigr]
   = -V\bigl[P_c'P_r + P_c\,P_r'\bigr].
   $$
3. Assemble $L'(q)$:
   $$
   L'(q)
   = P_c'\Bigl[C_u(1-P_r) - (C_o+V)P_r\Bigr]
     + P_r'\Bigl[C_o(1-P_c) - (C_u+V)P_c\Bigr].
   $$
4. Substitute $P_c',P_r'$ and set $L'(q)=0$:
   $$
   β_cP_c(1-P_c)\bigl[C_u(1-P_r) - (C_o+V)P_r\bigr]
   -β_rP_r(1-P_r)\bigl[(C_u+V)P_c - C_o(1-P_c)\bigr]
   =0.
   $$
5. Rearranged into the implicit equation
   $$
   \boxed{
   \frac{β_c\,P_c(1-P_c)}{β_r\,P_r(1-P_r)}
   = \frac{\,C_o(1-P_c)\;-\;(C_u+V)P_c\,}
          {\,C_u(1-P_r)\;-\;(C_o+V)P_r\,}
   }.
   $$

🚨🚨 _Please verify the sign conventions in the numerator and denominator when cross-multiplying._

### A.3.3 Special Limits — Closed-Form Solutions

We now derive the four tractable cases step by step.

---

#### 1. Symmetric Responsiveness ($β_c=β_r=β$)

- Let $x = e^{βq}$. Then
  $$
  P_c = \frac{x}{1+x},\quad P_r = \frac{1}{1+x}.
  $$
- Implicit FOC becomes
  $$
  (1-P_c)(C_u+V) \;=\; P_c\,(C_o+V).
  $$
- Substitute $1-P_c = 1/(1+x)$ and $P_c=x/(1+x)$:
  $$
  \frac{1}{1+x}(C_u+V)
  = \frac{x}{1+x}(C_o+V)
  \;\Longrightarrow\;
  x = \frac{C_u+V}{C_o+V}.
  $$
- Hence
  $$
  \boxed{
  q^* = \frac{1}{β}\,
    \ln\!\Bigl(\frac{C_u+V}{C_o+V}\Bigr).
  }
  $$

---

#### 2. Customer-Dominant Responsiveness ($β_c\gg β_r$)

- As $ε = β_r/β_c \to 0$, the left ratio $\to ∞$, so the right denominator must vanish:
  $$
  C_u(1-P_r) - (C_o+V)P_r = 0
  \;\Longrightarrow\;
  P_r = \frac{C_u}{C_u + C_o + V}.
  $$
- Since $P_r = 1/(1+e^{β_r q})$, solve
  $$
  \frac{1}{1+e^{β_r q}} = \frac{C_u}{C_u+C_o+V}
  \;\Longrightarrow\;
  e^{β_r q} = \frac{C_o+V}{C_u}.
  $$
- Thus
  $$
  \boxed{
  q^* = \frac{1}{β_r}\,
    \ln\!\Bigl(\frac{C_o + V}{C_u}\Bigr).
  }
  $$

---

#### 3. Partner-Dominant Responsiveness ($β_r\gg β_c$)

- By symmetry, swap roles:
  $$
  C_o(1-P_c) - (C_u+V)P_c = 0
  \;\Longrightarrow\;
  P_c = \frac{C_o}{C_u+C_o+V}.
  $$
- With $P_c = 1/(1+e^{-β_c q})$, we get
  $$
  e^{-β_c q} = \frac{1-P_c}{P_c}
  = \frac{C_u+V}{C_o}
  \;\Longrightarrow\;
  q^* = \frac{1}{β_c}\,
    \ln\!\Bigl(\frac{C_o}{C_u+V}\Bigr).
  $$
- Hence
  $$
  \boxed{
  q^* = \frac{1}{β_c}\,
    \ln\!\Bigl(\frac{C_o}{C_u+V}\Bigr).
  }
  $$

---

#### 4. High-Match-Value Limit ($V\gg C_u,C_o$)

- Approximate $L(q)\approx -V\,P_cP_r$, so FOC becomes
  $$
  β_c P_c(1-P_c) = β_r P_r(1-P_r).
  $$
- Solving this logistic marginal equality yields
  $$
  \boxed{
  q^* = \frac{1}{β_c + β_r}\,
    \ln\!\Bigl(\frac{β_r}{β_c}\Bigr).
  }
  $$

