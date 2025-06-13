
```
2.1 Step 1: Linear Quality Model
    - Mathematical setup
    - Proposition 1 (Optimal quality under quality-linear commitment probabilities)
    - Business intuition paragraphs 4A, 4B

2.2 Step 2: Sigmoid Quality Model  
    - Mathematical setup
    - Proposition 2 (Optimal quality under quality-nonlinear commitments)
    - Business intuition paragraphs 5A, 5B

2.3 Step 3: Joint Quality-Quantity Model
    - Mathematical setup
    - Proposition 3 (Insight on Quality and Quantity)
    - Business intuition paragraphs 6A, 6B
```
## 2 Methods  

We incrementally extend the classical newsvendor along two orthogonal dimensions—**decision type** (quantity → quality → quality + quantity) and **stakeholder response** (deterministic → linear Bernoulli → sigmoid).  Naming three progressive models as three step models, step 1 model establishes the core cost-priority principle under quality-linear stakeholder responses. Step 2 model captures realistic choice behavior using quality non-linear responses. Step 3 model extends to joint quality-quantity decisions.

Table 1 situates the three propositions developed in this section.

| Step  | Decision(s)               | Random variable                                                          | New relative to classic newsvendor                                                                                                                | appendix  |
| ----- | ------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| 0     | Supply $s$                | Demand $D$                                                               |                                                                                                                                                   | [[step0]] |
| **1** | quality $q$               | Customer commitment $C(q)$<br><br>Resource partner commitment $R(q)$<br> | Demand–supply asymmetry driven by quality rather than quantity<br><br>$P_c(q)=q$ , $P_r(q)=1-q$                                                   | [[step1]] |
| **2** | quality $q$               | Customer commitment $C(q)$<br><br>Resource partner commitment $R(q)$     | Statistically capture stakeholders' responsiveness to quality<br><br>$P_c(q)=\dfrac1{1+e^{-\beta_c * q}}$ , $P_r(q)=\dfrac1{1+e^{\ \beta_r * q}}$ | [[step2]] |
| **3** | quality $q$, quantity $Q$ | Customer commitment $C(q)$<br><br>Resource partner commitment $R(q)$     | Joint quality–quantity choice with diminishing–return revenue $R(Q)=aQ-bQ^{2}$                                                                    |           |

---
# 2.0 Classic news vendor

## Meaning of Adding Randomness to Supply Side

Classic newsvendor minimizes expected cost which is weighted average of  i) **Opportunity cost**: $(D-q)(p-c)$ when demand $D$ exceeds **deterministic** quantity $q$ and ii) **Overage cost**: $(q-D)c$ when **deterministic** quantity $q$ exceeds demand $D$.

The entrepreneur chooses product quality $\color{red}q \in [0,1]$ which affects:

Our model also minimize the expected cost. We define D as ?? and Q as ??. P(S>q) becomes supplier who can produce more than q quality, P(D<q) becomes customer willing to pay lower than quality q.
There are four partitions of probability space: P(Q<q, D>q), P(Q<q, D<q), P(Q>q, D>q), P(Q>q, D<q). Among the four,  P(Q<q, D<q) and P(Q>q, D>q) have cost and  P(Q>q, D<q) has negative costs (reward)

Think of quality $q$ as a **threshold** on a continuous scale (hardness of a catheter tube, purity of a chemical, refresh rate of a screen, …).  
Both sides of the transaction are uncertain:

- **Demand side** – the _customer’s requirement_ $D$ is a r.v. with CDF $F_D(\cdot)$. The customer buys only if $D!\le!q$ (they are satisfied with this or lower quality) or, in the opposite framing, only if $D!\ge!q$ (they insist on at least this quality). In the sketch the upper row is the event $P(D!\ge!q)$ and the lower row $P(D!<!q)$.
    
- **Supply side** – the _partner’s capability_ $S$ is a r.v. with CDF $F_S(\cdot)$. They can deliver at least $q$ only with probability $P(S!\ge!q)$ (right-hand columns); otherwise they top out below $q$ (left-hand columns).
    

That yields the **2 × 2 grid** :

| **Supplier can’t reach $q$**$S<q$     | **Supplier can reach $q$**$S\ge q$                                                    |                                                                                                          |
| ------------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Customer needs ≥ $q$**$D!\ge!q$     | _Opportunity-loss_ cell (upper-left). Demand exists but the partner can’t meet spec.  | _Match / revenue_ cell (upper-right). Both sides align at or above $q$.                                  |
| **Customer settles for < $q$**$D!<!q$ | _No transaction_ cell (lower-left). Neither side wants or can deliver higher quality. | _Overage-cost_ cell (lower-right). Partner can do more than necessary, so excess capability is “wasted.” |

The black-hatched bars in each box illustrate the _unused_ potential:  
– in the opportunity cell the shaded part is **foregone demand**,  
– in the overage cell it is **idle capability**.

Formally, letting $\mathbf 1_{(\cdot)}$ be an indicator:

- **Revenue term** $V,\mathbb E[\mathbf 1_{(D\ge q)},\mathbf 1_{(S\ge q)}]$
    
- **Opportunity cost** $C_u,\mathbb E[\mathbf 1_{(D\ge q)},\mathbf 1_{(S< q)}]$
    
- **Overage cost** $C_o,\mathbb E[\mathbf 1_{(D< q)},\mathbf 1_{(S\ge q)}]$
    

Setting the derivative of the total expected payoff with respect to $q$ to zero reproduces the critical-fractal conditions in **Step 1** (linear Bernoulli when $D,S$ are uniformly distributed on $[0,1]$) and in **Step 2** (sigmoid response after logistic transforms). Thus the sketch is a probabilistic Venn diagram: each quadrant corresponds to one term in our objective, and changing $q$ shrinks one shaded region while enlarging another until their marginal costs balance.

![[Pasted image 20250613181204.png|100]]
- **Opportunity cost**: $(D-Q)(p-c)$ when demand $D$ is larger than quality q, supply $Q$ is smaller than quality q
- **Overage cost**: $(Q-D)c$ when **stochastic** supply $Q$ exceeds demand $D$
- **Reward (negative cost)**: V when supply Q is larger than q and demand D is smaller than quality q.

**Key insight**: The supply quantity $Q$ is no longer a decision variable but becomes a random outcome based on resource partner's willingness to supply given quality of entrepreneur's value proposition $q$. If demand $D$ exceeds the supplied quantity $Q$, then an **opportunity cost** of $(D-Q)(p-c)$ represents lost revenue not realized because of shortage of supply from resource partner. On the other hand, if $D \leq Q$, then (because the items being supplied are perishable), there is an **overage cost** of $(Q-D)c$. This problem can be posed as one of minimizing the expectation of the sum of the opportunity cost and overage cost, keeping in mind that only one of these is ever incurred for any particular realization of $D$ and $Q$.

## Mathematical Derivation

$$\text{E}[\text{opportunity cost + overage cost}]$$

$$= \text{E}[\text{overage cost} | D \leq Q] P(D \leq Q) + \text{E}[\text{opportunity cost} | D > Q] P(D > Q)$$

$$= \text{E}[(Q-D)c | D \leq Q] P(D \leq Q) + \text{E}[(D-Q)(p-c) | D > Q] P(D > Q)$$

### Case Analysis for Bernoulli Variables

| $\color{skyblue}D$ | $\color{skyblue}Q$ | Probability         | Condition | Cost                 |
| ------------------ | ------------------ | ------------------- | --------- | -------------------- |
| 0                  | 0                  | $(1-q) \cdot q$     | $D = Q$   | 0                    |
| 0                  | 1                  | $(1-q) \cdot (1-q)$ | $D < Q$   | $(1-0)c = c$         |
| 1                  | 0                  | $q \cdot q$         | $D > Q$   | $(1-0)(p-c) = (p-c)$ |
| 1                  | 1                  | $q \cdot (1-q)$     | $D = Q$   | 0                    |

### Expected Cost Calculation

$$\text{E}[\text{opportunity cost + overage cost}]$$

$$= c \cdot (1-q)^2 + (p-c) \cdot q^2$$

$$= c(1-q)^2 + (p-c)q^2$$

# 2.1 Step 1 – Linear-quality commitments  

**Proposition 1 (Optimal quality under quality-linear commitment probabilities).**  
Let mismatch loss be  
$L(q)=C_u q^{2}+C_o(1-q)^{2}-V q(1-q)$ with $q\in[0,1]$,
$C_u,C_o>0$, and match bonus $V\ge0$.  
Then  

$$
q^{*}=\frac{V+2C_o}{2\,(C_u+C_o+V)},
\qquad
\frac{\partial q^{*}}{\partial V}=\frac{C_u-C_o}{2\,(C_u+C_o+V)^{2}} .
$$

> **When is $q^{*}$ high?**  
> (i) $C_o\!\gg\!C_u$—expensive surplus; managers raise quality to pull demand.  
> (ii) $V$ large *and* $C_u>C_o$—opportunity seekers court customers even at surplus risk.  
> (iii) $V$ small *and* $C_o>C_u$—risk avoiders still favour higher quality to dodge leftovers.

*Why interesting?*  
Unlike the classic critical-fractile, which moves with a single cost ratio,
here the *direction* of $V$’s impact flips when the cheaper mismatch changes,
highlighting a dual-cost amplification mechanism absent in quantity-only
settings.

---

# 2.2 Step 2 – Non-linear-quality commitments  

**Proposition 2 (Optimal quality under quality-nonlinear commitments).**  
With logistic response curves  

$$
P_c(q)=\frac1{1+e^{-\beta_c *q}},\qquad
P_r(q)=\frac1{1+e^{\ \beta_r*q}},
$$

the expected loss  

$$
L(q)=C_uP_c(1-P_r)+C_oP_r(1-P_c)-V P_cP_r
$$

is strictly quasi-convex on $[0,1]$; its derivative $L'(q)=0$ has a 



#### Simplified Case: βc = 1, βr = -1

**First-order condition becomes:** $$L'(q) = C_u P_c'(q)[1-P_r(q)] + C_u P_c(q)P_r'(q) + C_o P_r'(q)[1-P_c(q)] - C_o P_r(q)P_c'(q) - V[P_c'(q)P_r(q) + P_c(q)P_r'(q)] = 0$$

**With your parameters:**

- $P_c'(q) = P_c(1-P_c)$
- $P_r'(q) = -P_r(1-P_r)$
## General Case: Arbitrary βc, βr

**First-order condition becomes:** $$L'(q) = \beta_c P_c(1-P_c)[C_u(1-P_r) - C_o P_r - V P_r] + \beta_r P_r(1-P_r)[C_u P_c - C_o(1-P_c) + V P_c] = 0$$

**Key differences from your simplified case:**

### 1. **No Closed-Form Solution**

- General case requires numerical methods
- Your $\beta_c = 1, \beta_r = -1$ case somehow gives explicit solution (need clarification on derivation)

### 2. **Steepness Effects**

- Larger $|\beta_c|$: Customer responses more sensitive to quality near $\theta_c$
- Larger $|\beta_r|$: Resource partner responses more sensitive near $\theta_r$
- Different $\beta$ values change the relative "weight" of each stakeholder in the optimization

### 3. **Comparative Static Complexity**

Using implicit differentiation: $$\frac{\partial q^*}{\partial V} = -\frac{\partial L'/\partial V}{\partial L'/\partial q}$$

**Numerator:** $\frac{\partial L'}{\partial V} = -\beta_c P_c(1-P_c)P_r - \beta_r P_r(1-P_r)P_c$

**Denominator:** $\frac{\partial L'}{\partial q}$ involves second derivatives of sigmoids and is generally positive (quasi-convexity)

**Result:** $$\operatorname{sgn}\left(\frac{\partial q^*}{\partial V}\right) = \operatorname{sgn}(\beta_c P_c(1-P_c)P_r + \beta_r P_r(1-P_r)P_c)$$

Since all probability terms are positive, this depends on the signs and magnitudes of $\beta_c$ and $\beta_r$.

### Key Changes When Relaxing Constraints:

#### **Economic Intuition:**

- **Your case**: Clean cost-priority principle $\operatorname{sgn}(\partial q^*/\partial V) = \operatorname{sgn}(C_u - C_o)$
- **General case**: Cost-priority modulated by responsiveness parameters $\beta_c, \beta_r$

#### **Strategic Implications:**

- General case allows for scenarios where stakeholder responsiveness asymmetries override pure cost considerations
- Your simplified case isolates the pure cost-priority effect

-----


---

### A.3 Step 3 — Joint Quality–Quantity Model  

#### A.3.1 Additional Notation  
| Symbol | Meaning |
|--------|---------|
| $Q\ge0$ | production quantity (new decision) |
| $R(Q)=aQ-bQ^{2}$, $a,b>0$ | diminishing-return revenue when both commit |

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
 
---

### A.4 Summary of Structural Properties  

| Model | Convexity | Closed-form optimum? | Direction of $\partial q/\partial V$ |
|-------|-----------|----------------------|--------------------------------------|
| Step 1 | **Strictly convex** | Yes, $q^{*}$ | $\;$sign$(C_u-C_o)$ |
| Step 2 | Strictly quasi-convex | No (unique root) | $\;$sign$(C_u-C_o)$ |
| Step 3 | Separable: $Q$ concave, $q$ as Step 2 | $Q^{*}=a/2b$, $q^{\dagger}$ via root-finding | $\;$sign$(C_u-C_o)$ |


----


## Step 0 

* **Quantity decision** $\color{red}{q}\in\mathbb R_{+}$  
* **Random demand** $\color{skyblue}{D}$ with CDF $\color{skyblue}{F}(\cdot)$ and PDF $\color{skyblue}{f}(\cdot)$  
* Usual critical-fractile solution  
  $\displaystyle \color{skyblue}{F}\!\bigl(\color{red}{q}^{*}\bigr)=\frac{\text{under-stock cost}}{\text{under}+\text{over cost}}$  


---

## Step 1 (quality-linear commitments)

|                                         | $\color{skyblue}{Q}=0$ (partner absent)                                  | $\color{skyblue}{Q}=1$ (partner present)                               |
| --------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| $\color{skyblue}{D}=1$ (customer shows) | $\color{red}{q}^{2}$&nbsp;⟶ **shortage** incurs *opportunity* cost $C_u$ | $(1-\color{red}{q})\color{red}{q}$&nbsp;⟶ **match** gains value $+V$   |
| $\color{skyblue}{D}=0$ (no customer)    | $\color{red}{q}(1-\color{red}{q})$&nbsp;⟶ **match** (no cost)            | $(1-\color{red}{q})^{2}$&nbsp;⟶ **excess** incurs *overage* cost $C_o$ |



$\mathrm E[\text{Cost}] = C_u\,\Pr(\color{skyblue}{D}=1,\color{skyblue}{Q}=0)  + C_o\,\Pr(\color{skyblue}{D}=0,\color{skyblue}{Q}=1)- V\,\Pr(\color{skyblue}{D}=1,\color{skyblue}{Q}=1)= C_u\,\color{red {q}^{2}\;+\;C_o\,(1-\color{red}{q})^{2}\;-\;V\,\color{red}{q}(1-\color{red}{q})$

### Optimal quality $\color{red}{q}^{*}$

$\frac{d}{d\color{red}{q}}\mathrm E[\text{Cost}]= 2C_u\,\color{red}{q}-2C_o(1-\color{red}{q})-V(1-2\color{red}{q})=0$

$\boxed{\;\color{red}{q}^{*}=\frac{\,V+2C_o\,}{2\,(C_u+C_o+V)}=\frac12\!\left[\,1+\frac{C_o-C_u}{C_u+C_o+V}\right]\;}$

*When $V=0$: $\displaystyle \color{red}{q}^{*}=1-\text{CR}$ with  
$\text{CR}=\frac{C_u}{C_u+C_o}$ (the classical critical ratio).*

---

### When does $\color{red}{q}^{*}$ land **high**?

1. **High $C_o$, low $C_u$** – you dread leftover stock, so you raise quality to attract customers.  
2. **High $V$** – the upside of a full match is large (e.g., $C_u=p-c>C_o=c$).  
3. **Low $V$** *and* $C_u<C_o$ – risk-averse posture: avoid unsold production.


