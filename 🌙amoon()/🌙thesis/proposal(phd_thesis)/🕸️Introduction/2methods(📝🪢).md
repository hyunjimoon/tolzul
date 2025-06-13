step0 ([[classic]]). given customer's demand $\color{skyblue}D$ , supplier's quantity $\color{red}q$?
step1 (quality). given customer's quality-linear demand $\color{skyblue}Bern(q)$ and resource partner's quality-linear supply $\color{skyblue}Bern(1-q)$, quality of proposed product $\color{red}q$?
step2 (non-linear quality). given customer's quality-nonlinear demand  and resource partner's quality-nonlinear supply
step3 (non-linear quality and quantity). given customer's quality-nonlinear demand  and resource partner's quality-nonlinear supply, quality $\color{red}q$ and quantity $\color{red}Q$?

## 2 Methods  

We incrementally extend the classical newsvendor along two orthogonal dimensions—**decision type** (quantity → quality → quality + quantity) and **stakeholder response** (deterministic → linear Bernoulli → sigmoid).  
Table 1 situates the three propositions developed in this section.

| Step  | Decision(s)               | Commitment probabilities                                                                     | New relative to classic newsvendor                                             | appendix    |
| ----- | ------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------- |
| **1** | quality $q$               | $P_c(q)=q$ , $P_r(q)=1-q$                                                                    | Demand–supply asymmetry driven by quality rather than quantity                 | [[classic]] |
| **2** | quality $q$               | $P_c(q)=\dfrac1{1+e^{-\beta_c(q-\theta_c)}}$ , $P_r(q)=\dfrac1{1+e^{\ \beta_r(q-\theta_r)}}$ | Threshold & saturation effects (S-curves)                                      |             |
| **3** | quality $q$, quantity $Q$ | same sigmoids as Step 2                                                                      | Joint quality–quantity choice with diminishing–return revenue $R(Q)=aQ-bQ^{2}$ |             |

---

### 2.1 Step 1 – Linear-quality commitments  

**Proposition 1 (Optimal quality under linear Bernoulli commitments).**  
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

### 2.2 Step 2 – Non-linear-quality commitments  

**Proposition 2 (Optimal quality under sigmoid commitments).**  
With logistic response curves  

$$
P_c(q)=\frac1{1+e^{-\beta_c(q-\theta_c)}},\qquad
P_r(q)=\frac1{1+e^{\ \beta_r(q-\theta_r)}},
$$

the expected loss  

$$
L(q)=C_uP_c(1-P_r)+C_oP_r(1-P_c)-V P_cP_r
$$

is strictly quasi-convex on $[0,1]$; its derivative $L'(q)=0$ has a *u*

-----



## Appendix A Detailed Mathematical Derivations  
*(To accompany the three propositions in Section 2)*  

The exposition mirrors the level of clarity in our preliminary “classic newsvendor” appendix :contentReference[oaicite:0]{index=0} while extending it to the quality-driven settings introduced in the paper.  We proceed in ascending order of model complexity.

---

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
Only one mismatch cost can realise in any outcome.  Enumerating the four Bernoulli states:

\[
L(q)=C_u\,P_c(1-P_r)+C_o\,P_r(1-P_c)-V\,P_cP_r
      =C_u q^{2}+C_o(1-q)^{2}-V q(1-q).
\]

#### A.1.3 Convexity  
\[
L''(q)=2(C_u+C_o+V)>0\ \Longrightarrow\ L(q)\ \text{strictly convex}.
\]

#### A.1.4 Unique Optimum  
Set $L'(q)=0$:

\[
2(C_u+C_o+V)q-(2C_o+V)=0
\quad\Longrightarrow\quad
q^{*} = \frac{V+2C_o}{2(C_u+C_o+V)}.
\]

#### A.1.5 Comparative Static w.r.t. $V$  

\[
\frac{\partial q^{*}}{\partial V}
      =\frac{C_u-C_o}{2(C_u+C_o+V)^{2}}.
\]

*Interpretation:* $q^{*}$ increases in $V$ iff $C_o<C_u$ and decreases if $C_o>C_u$ (see cost-asymmetry discussion in Section 2).

---

### A.2 Step 2 — Non-Linear Quality (Sigmoid Commitments)  

#### A.2.1 Notation  
| Symbol | Meaning |
|--------|---------|
| $q\in[0,1]$ | product quality |
| $P_c(q)=\dfrac{1}{1+e^{-\beta_c(q-\theta_c)}}$ | customer sigmoid |
| $P_r(q)=\dfrac{1}{1+e^{\ \beta_r(q-\theta_r)}}$ | partner sigmoid (mirrored) |
| $\beta_c,\beta_r>0$ | steepness parameters |
| $\theta_c,\theta_r\in(0,1)$ | inflection points |
| Other symbols $C_u,C_o,V$ as before |

We write the derivatives  
$P_c'(q)=\beta_cP_c(1-P_c)$ and $P_r'(q)=-\beta_rP_r(1-P_r)$ for later use.

#### A.2.2 Expected Loss Function  

\[
L(q)=C_uP_c(1-P_r)+C_oP_r(1-P_c)-V P_cP_r.
\]

#### A.2.3 Monotone-Difference Form of the Gradient  

\[
\begin{aligned}
L'(q)
&=\beta_cP_c(1-P_c)\bigl[C_u(1-P_r)-C_oP_r-VP_r\bigr]  \\
&\quad+\beta_rP_r(1-P_r)\bigl[C_uP_c-C_o(1-P_c)+VP_c\bigr].
\end{aligned}
\tag{A.1}
\]

The two bracketed terms are strictly decreasing and increasing in $q$,
respectively, while the sigmoid prefactors are strictly positive on $(0,1)$.

#### A.2.4 Uniqueness of the Optimum  

Because (A.1) is a weighted sum of functions with opposite monotonicity,
$L'(q)$ can cross zero **at most once**.  Since $L'(0)<0$ and $L'(1)>0$,
it crosses exactly once, implying strict quasi-convexity and a unique minimiser
$q^{\dagger}\in(0,1)$.

#### A.2.5 Comparative Static w.r.t. $V$  

Implicit differentiation of $L'(q^{\dagger},V)=0$ gives  

\[
\frac{\partial q^{\dagger}}{\partial V}
  =-\frac{\partial L'/\partial V}{\partial L'/\partial q}.
\]

Denominator $>0$ by quasi-convexity.  Evaluating the numerator at the root of $L'(q)$ yields $(C_u-C_o)\,[\beta_cP_c(1-P_c)+\beta_rP_r(1-P_r)]$, again delivering $\operatorname{sgn}(\partial q^{\dagger}/\partial V)=\operatorname{sgn}(C_u-C_o)$.

---

### A.3 Step 3 — Joint Quality–Quantity Model  

#### A.3.1 Additional Notation  
| Symbol | Meaning |
|--------|---------|
| $Q\ge0$ | production quantity (new decision) |
| $R(Q)=aQ-bQ^{2}$, $a,b>0$ | diminishing-return revenue when both commit |

#### A.3.2 Expected Profit  

\[
\Pi(q,Q)= R(Q)P_c(q)P_r(q)
          -C_uP_c(q)\bigl[1-P_r(q)\bigr]
          -C_oP_r(q)\bigl[1-P_c(q)\bigr].
\]

#### A.3.3 Optimising Quantity for Fixed Quality  

\[
\frac{\partial \Pi}{\partial Q}=aP_cP_r-2bQP_cP_r
   =P_cP_r\bigl(a-2bQ\bigr)=0
\ \Rightarrow\ 
Q^{*}=\frac{a}{2b}.
\]

This vertex is independent of $q$.

#### A.3.4 Reduced One-Dimensional Quality Problem  

Substituting $Q^{*}$ drops $Q$ from all mismatch terms and scales the revenue
coefficient by $P_cP_r$:

\[
\max_{q\in[0,1]}
\Bigl[\tfrac{a^{2}}{4b}P_c(q)P_r(q)-C_uP_c(1-P_r)-C_oP_r(1-P_c)\Bigr].
\]

The maximiser satisfies the *same* first-order condition $L'(q)=0$ derived in
Step 2, so $q^{\dagger}$ and all its comparative statics carry over.
 
---

### A.4 Summary of Structural Properties  

| Model | Convexity | Closed-form optimum? | Direction of $\partial q/\partial V$ |
|-------|-----------|----------------------|--------------------------------------|
| Step 1 | **Strictly convex** | Yes, $q^{*}$ | $\;$sign$(C_u-C_o)$ |
| Step 2 | Strictly quasi-convex | No (unique root) | $\;$sign$(C_u-C_o)$ |
| Step 3 | Separable: $Q$ concave, $q$ as Step 2 | $Q^{*}=a/2b$, $q^{\dagger}$ via root-finding | $\;$sign$(C_u-C_o)$ |

These formal results justify the managerial insights highlighted in the main
text while supplying POMS scholars with full derivations for replication and
future extensions.
```

## Step 0 

* **Quantity decision** $\color{red}{q}\in\mathbb R_{+}$  
* **Random demand** $\color{skyblue}{D}$ with CDF $\color{skyblue}{F}(\cdot)$ and PDF $\color{skyblue}{f}(\cdot)$  
* Usual critical-fractile solution  
  $\displaystyle \color{skyblue}{F}\!\bigl(\color{red}{q}^{*}\bigr)
  =\frac{\text{under-stock cost}}{\text{under}+\text{over cost}}$  


---

## Step 1 (Bernoulli commitments)

|                                         | $\color{skyblue}{Q}=0$ (partner absent)                                  | $\color{skyblue}{Q}=1$ (partner present)                               |
| --------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| $\color{skyblue}{D}=1$ (customer shows) | $\color{red}{q}^{2}$&nbsp;⟶ **shortage** incurs *opportunity* cost $C_u$ | $(1-\color{red}{q})\color{red}{q}$&nbsp;⟶ **match** gains value $+V$   |
| $\color{skyblue}{D}=0$ (no customer)    | $\color{red}{q}(1-\color{red}{q})$&nbsp;⟶ **match** (no cost)            | $(1-\color{red}{q})^{2}$&nbsp;⟶ **excess** incurs *overage* cost $C_o$ |

\[
\begin{aligned}
\mathrm E[\text{Cost}]
&= C_u\,\Pr(\color{skyblue}{D}=1,\color{skyblue}{Q}=0)
  + C_o\,\Pr(\color{skyblue}{D}=0,\color{skyblue}{Q}=1)
  - V\,\Pr(\color{skyblue}{D}=1,\color{skyblue}{Q}=1)\\[2mm]
&= C_u\,\color{red}{q}^{2}\;+\;C_o\,(1-\color{red}{q})^{2}\;-\;V\,\color{red}{q}(1-\color{red}{q})
\end{aligned}
\]

### Optimal quality $\color{red}{q}^{*}$

\[
\frac{d}{d\color{red}{q}}\mathrm E[\text{Cost}]
= 2C_u\,\color{red}{q}-2C_o(1-\color{red}{q})-V(1-2\color{red}{q})
=0
\]

\[
\boxed{\;
\color{red}{q}^{*}
=\frac{\,V+2C_o\,}{2\,(C_u+C_o+V)}
=\frac12\!\left[\,1+\frac{C_o-C_u}{C_u+C_o+V}\right]
\;}
\]

*When $V=0$: $\displaystyle \color{red}{q}^{*}=1-\text{CR}$ with  
$\text{CR}=\frac{C_u}{C_u+C_o}$ (the classical critical ratio).*

---

### When does $\color{red}{q}^{*}$ land **high**?

1. **High $C_o$, low $C_u$** – you dread leftover stock, so you raise quality to attract customers.  
2. **High $V$** – the upside of a full match is large (e.g., $C_u=p-c>C_o=c$).  
3. **Low $V$** *and* $C_u<C_o$ – risk-averse posture: avoid unsold production.

---

# Newsvendor Model - Complete Derivation

## Notation

- Decision quantity: $\color{red}{q}$
- Random demand: $\color{skyblue}{D}$
- Price per unit: $\color{green}{p}$
- Cost per unit: $\color{green}{c}$
- CDF:  
    $$\color{skyblue}{F}\bigl(\color{red}{q}\bigr) = P\bigl(\color{skyblue}{D}\le\color{red}{q}\bigr)$$
- PDF:  
    $$\color{skyblue}{f}(x) = \frac{d}{dx},\color{skyblue}{F}(x)$$

---

## Derivation

We minimize the expected sum of opportunity- and overage-costs:

$$\begin{aligned} &\mathbb{E}\bigl[\text{opp.\ cost} + \text{ovg.\ cost}\bigr] \[6pt] &= \underbrace{\mathbb{E}!\bigl[(\color{red}{q}-\color{skyblue}{D}),\color{green}{c};\bigm|;\color{skyblue}{D}\le\color{red}{q}\bigr];P!\bigl(\color{skyblue}{D}\le\color{red}{q}\bigr)}_{\text{overage cost}} ;+; \underbrace{\mathbb{E}!\bigl[(\color{skyblue}{D}-\color{red}{q})(\color{green}{p}-\color{green}{c});\bigm|;\color{skyblue}{D}>\color{red}{q}\bigr];P!\bigl(\color{skyblue}{D}>\color{red}{q}\bigr)}_{\text{opportunity cost}} \[6pt] &= \color{green}{c},\mathbb{E}\bigl[\color{red}{q}-\color{skyblue}{D}\mid \color{skyblue}{D}\le \color{red}{q}\bigr],\color{skyblue}{F}(\color{red}{q}) ;+; (\color{green}{p}-\color{green}{c}),\mathbb{E}\bigl[\color{skyblue}{D}-\color{red}{q}\mid \color{skyblue}{D}>\color{red}{q}\bigr],[1-\color{skyblue}{F}(\color{red}{q})] \[6pt] &= \color{green}{c}\Bigl(\color{red}{q},\color{skyblue}{F}(\color{red}{q}) -\int_{x\le\color{red}{q}}x,\color{skyblue}{f}(x),dx\Bigr) +(\color{green}{p}-\color{green}{c})\Bigl(\int_{x>\color{red}{q}}x,\color{skyblue}{f}(x),dx -\color{red}{q},[1-\color{skyblue}{F}(\color{red}{q})]\Bigr) \[6pt] &= \color{green}{p}!\int_{x>\color{red}{q}}x,\color{skyblue}{f}(x),dx -\color{green}{p},\color{red}{q},[1-\color{skyblue}{F}(\color{red}{q})] -\color{green}{c}!\int_{x>\color{red}{q}}x,\color{skyblue}{f}(x),dx +\color{green}{c},\color{red}{q},[1-\color{skyblue}{F}(\color{red}{q})] +\color{green}{c},\color{red}{q},\color{skyblue}{F}(\color{red}{q}) -\color{green}{c}!\int_{x\le\color{red}{q}}x,\color{skyblue}{f}(x),dx \[4pt] &= \color{green}{p}!\int_{x>\color{red}{q}}x,\color{skyblue}{f}(x),dx -\color{green}{p},\color{red}{q} +\color{green}{p},\color{red}{q},\color{skyblue}{F}(\color{red}{q}) +\color{green}{c},\color{red}{q} -\color{green}{c},\mathbb{E}[\color{skyblue}{D}]. \end{aligned}$$

---

## First‐order condition

Differentiate w.r.t. $\color{red}{q}$:

$$\begin{aligned} \frac{\partial}{\partial ,\color{red}{q}}, \mathbb{E}[\dots] &= \frac{\partial}{\partial ,\color{red}{q}} \Bigl[ \color{green}{p}!\int_{x>\color{red}{q}}x,\color{skyblue}{f}(x),dx -\color{green}{p},\color{red}{q} +\color{green}{p},\color{red}{q},\color{skyblue}{F}(\color{red}{q}) +\color{green}{c},\color{red}{q} -\color{green}{c},\mathbb{E}[\color{skyblue}{D}] \Bigr] \[4pt] &= -\color{green}{p},\color{red}{q},\color{skyblue}{f}(\color{red}{q}) -\color{green}{p} +\color{green}{p},\color{skyblue}{F}(\color{red}{q}) +\color{green}{p},\color{red}{q},\color{skyblue}{f}(\color{red}{q}) +\color{green}{c} \[3pt] &= \boxed{,\color{green}{p},\color{skyblue}{F}(\color{red}{q}) +\color{green}{c} -\color{green}{p},}. \end{aligned}$$

Setting this to zero gives the **critical fractile**:

$$\color{skyblue}{F}\bigl(\color{red}{q}^*\bigr) = \frac{\color{green}{p}-\color{green}{c}}{\color{green}{p}}$$
# Dual Newsvendor Model: Opportunity Cost + Overage Cost Formulation

## Problem Setup

The entrepreneur chooses product quality $\color{red}q \in [0,1]$ which affects:

- **Customer demand**: $\color{skyblue}D \sim \text{Bern}(q)$
- **Resource partner supply**: $\color{skyblue}Q \sim \text{Bern}(1-q)$

## Meaning of Adding Randomness to Supply Side

### Classical Newsvendor (Image)

- **Opportunity cost**: $(D-q)(p-c)$ when demand $D$ exceeds **deterministic** quantity $q$
- **Overage cost**: $(q-D)c$ when **deterministic** quantity $q$ exceeds demand $D$

### Our Dual Model Mapping

- **Opportunity cost**: $(D-Q)(p-c)$ when demand $D$ exceeds **stochastic** supply $Q$
- **Overage cost**: $(Q-D)c$ when **stochastic** supply $Q$ exceeds demand $D$

**Key insight**: The supply quantity $Q$ is no longer a decision variable but becomes a random outcome based on resource partner's willingness to supply given quality $q$.

## Cost Structure Following Image.png

If demand $D$ exceeds the supplied quantity $Q$, then an **opportunity cost** of $(D-Q)(p-c)$ represents lost revenue not realized because of shortage of supply from resource partner.

On the other hand, if $D \leq Q$, then (because the items being supplied are perishable), there is an **overage cost** of $(Q-D)c$.

This problem can be posed as one of minimizing the expectation of the sum of the opportunity cost and overage cost, keeping in mind that only one of these is ever incurred for any particular realization of $D$ and $Q$.

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

## Optimization

Taking the derivative with respect to $\color{red}q$:

$$\frac{\partial}{\partial q} \text{E}[\text{opportunity cost + overage cost}] = -2c(1-q) + 2(p-c)q$$

$$= -2c + 2cq + 2(p-c)q = -2c + 2q[c + (p-c)] = -2c + 2pq$$

Setting equal to zero: $$-2c + 2pq^* = 0$$

$$q^* = \frac{c}{p}$$


## Key Distinctions

### **Uncertainty Structure**

- **Model 0**: Single random variable (demand)
- **Model 1**: Binary outcomes for both stakeholders
- **Model 2**: Binary outcomes affecting both demand and supply sides
- **Angie's Model**: Commitment timing and probability

### **Strategic Elements**

- **Model 0**: Passive demand acceptance
- **Model 1**: Quality affects acceptance rates inversely
- **Model 2**: Quality affects both demand and supply capabilities
- **Angie's Model**: Entrepreneur chooses engagement sequence

### **Complexity Progression**

1. **Model 0**: Foundation - single decision, single uncertainty
2. **Model 1**: Adds strategic trade-off with complementary probabilities
3. **Model 2**: Extends to joint quality-quantity optimization
4. **Angie's Model**: Introduces temporal sequencing and stakeholder management

### **Business Context**

- **Models 0-2**: Product-focused (inventory/quality decisions)
- **Angie's Model**: Relationship-focused (stakeholder engagement strategy)

# 2. Model
We propose a two-stage decision framework where entrepreneurs first design value propositions specifying quality attributes that determine resource partners' and customers' commitment probabilities, then strategically prioritize stakeholder engagement by applying a newsvendor model that minimizes expected mismatch costs based on the resulting stochastic commitment demand forecast.
### 2.1 First Stage: Predicting First-Commitment Probabilities given Value Proposition 

The first stage is organized into three subsections: (i) Stakeholder utilities given value proposition, (ii) Classifying stakeholder interaction,  (iii) Predicting first-commitment probabilities. We start by modeling the entrepreneur’s value proposition design as **value-proposition vector**

$$x=[x_1,\dots ,x_K]^{\top}, \tag{0}$$

where, in the illustrative case, $x_1$ denotes **price** (USD) and $x_2$ denotes perceived **quality** (Likert 1–5). The purpose of Stage 1 is to translate x into the probability that either stakeholder (resource partner or customer) will become the first to commit.

### 2.1.1 Stakeholder Utilities given Value Proposition

Each stakeholder $j\in\{\mathrm{\mathrm Resource \; Partner, \mathrm Customer}\}$ evaluates the design through a linear utility function based on these non-financial attributes. For an illustrative case with two attributes, we can define a substitutive component (`x_sub`, e.g., technological novelty) and a complementary component (`x_comp`, e.g., product reliability):

$$Uj​(x)=β_{0j}​+β_{1j}​x_{sub}​+β_{2j}​x_{comp​}. \tag{1}$$

The slopes $\beta_{1j}$ and $\beta_{2j}$ quantify the marginal effects of price and quality on stakeholders' perceived attractiveness of entrepreneur's value proposition.

### 2.1.2 Classifying stakeholder interaction

The sign pattern of the `β` coefficients from Eq. (1, revised) partitions the engagement landscape into empirically testable modes:

| **Mode**          | **Formal criterion**                                    | **Economic interpretation**                                             | **Examples of Value Proposition Attributes**                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------- | ------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Substitutive**  | $\beta_{0j}=\beta_{2j}=0$<br>$\beta_{1RP}*\beta_{1C}<0$ | An attribute that pleases one side repels the other.                    | **- Technological Novelty:** Radical, unproven technology excites early adopters but worries risk-averse manufacturing partners<br><br>- **System Openness:** Customers may prefer open standards for interoperability, while a key partner may demand a proprietary, exclusive ecosystem<br><br>- **Aggressive Timelines:** A rapid development schedule may attract eager customers but repel development partners who see it as increasing risk. |
| **Complementary** | $\beta_{0j}=\beta_{1j}=0$<br>$\beta_{2RP}*\beta_{2C}>0$ | An attribute that moves utilities in the same direction for both sides. | **- Product Reliability:** A dependable product reduces returns and enhances reputation, pleasing both customers and support/supply partners.<br><br>- **Ease of Use (UX):** A simple, intuitive user experience leads to higher customer satisfaction and lower support costs for partners.<br><br>- **Brand Prestige:** Both customers and partners benefit from being associated with a strong, reputable brand.                                 |

> **💡Example 1 (HYPOTHETICAL).** Let's define the substitutive attribute `x_sub` as **Partner Manufacturing Maturity** on a 1-5 scale. Tesla’s choice of Xcellent Manufacturing in Thailand exemplifies this substitutive trade-off. A low-maturity partner like Xcellent—who was "eager to enter the high tech manufacturing sector" but had "virtually no design or quality control capabilities"—gains significant utility from the opportunity. A customer, however, implicitly bears the risk of this choice, which could affect final product quality and delivery.
>
> We can model this with coefficients like `β_1RP = -0.4` (the lower the partner's maturity, the higher their utility from the opportunity) and `β_1C = +0.1` (customers derive some utility from a more mature, less risky partner). A strategic decision to choose a partner with a maturity score of 2 instead of a more established alternative with a score of 4 (a change of -2 points) would raise the partner's utility by `(-0.4 * -2) = 0.8` utils, while lowering the customer's utility by `(0.1 * -2) = -0.2` utils.

### 2.1.3 Predicting first-commitment probabilities

To convert utilities into probabilities we employ a standard logit transformation. First, each utility in (1) is exponentiated to obtain a positive _attractiveness weight_; next, the weights are normalized so they sum to one:

$$p_{\mathrm r}=\frac{\exp[U_{\mathrm{RP}}(x)]}{\exp[U_{\mathrm{RP}}(x)]+\exp[U_{\mathrm C}(x)]}, \qquad p_{\mathrm c}=1-p_{\mathrm r}. \tag{2}$$

Even small utility changes—such as the 0.06-util uplift from **example 1**—alter the exponent and can result in different optimal engaging sequence.

> **💡Example 2.** Let's assume an initial strategic plan for the Roadster yields baseline utilities of $U_{RP} = 1.0$ and $U_C = 1.3$.
>
> Following the strategic decision in **Example 1** to partner with a lower-maturity supplier like Xcellent, the final utilities are updated based on the trade-off identified:
>
> $U_{RP\_final} = 1.0 + 0.8 = 1.8$
>
> $U_{C\_final} = 1.3 - 0.2 = 1.1$
>
> Substituting these final utility values into Eq. (2) produces the desired commitment probability:
>
> $$p_r = \frac{\exp(1.8)}{\exp(1.8) + \exp(1.1)} = \frac{6.050}{6.050 + 3.004} = \frac{6.050}{9.054} \approx \textbf{0.67}$$
>
> This demonstrates how the strategic choice of a specific resource partner—balancing their excitement against their inexperience—leads to the final `p_r = 0.67` and `p_c = 0.33` probabilities used in the subsequent analysis.

[[2methods(📝🪢)|2methods(📝🪢)]]
## 2.2 Second Stage: Sequencing Engagement through a Newsvendor Lens

The second stage is organized into three subsections: (i) _Inputs & Cost Architecture, (ii)  Why a single-period Newsvendor backbone is appropriate and (iii) Newsvendor Formulation and Decision Rule.
### 2.2.1 Inputs & Cost Architecture

The only numerical information inherited from Stage 1 are **first-commitment probabilities**: $p_{\mathrm r}$ represents the probability that a resource-partner is the first stakeholder to sign, while $p_{\mathrm c}=1-p_{\mathrm r}$ represents the complementary probability that a customer signs first. The demand uncertainty is about "who commits first". This is encoded in a single binary random variable

$$ D = \operatorname{Bernoulli}(p_{\mathrm c}), \qquad D\in{0,1}. \tag{3} $$

The interpretation is direct: a realization $D=0$ indicates that commitment "demand'' (viewing supply as negative demand) arrives first from the resource partner side, whereas $D=1$ indicates that demand originates with customers. 

Before a sequencing decision can be made, the entrepreneur must also specify two **mismatch-penalty (cost) parameters**. The parameter $C_{o}$ represents the "overage cost" which is a cost to the organization of making product that wouldn't be sold D = –1. It reflects the economic consequences of an over-commitment to the resource side (e.g., irrecoverable investments, idle dedicated capacity, reputational damage in upstream supply chain). Conversely, $C_{u}$ (measured in dollars) captures the "underage cost" which is a cost to the organization of not being able to deliver the promise.  It reflects the economic consequences of an under-commitment on the resource/supply side when faced with early customer demand (e.g., lost profit, reputational damage to chosen customer segment).

Just as a manager in the Newsvendor framework chooses an inventory level that minimizes expected cost given the prior distribution of future demand, an entrepreneur chooses an engagement sequence that minimizes expected mismatch costs given the prior distribution of stakeholder first-commitment probabilities. To clarify, see table below. 

| **Framework Element**  | **Classic Newsvendor**                     | **Our Application**                                |
| ---------------------- | ------------------------------------------ | -------------------------------------------------- |
| **Decision Variable**  | Inventory level (Q units)                  | Engagement sequence (Resource Partner vs Customer) |
| **Uncertainty Source** | Future customer demand                     | Which stakeholder commits first                    |
| **Cost Structure**     | Overage + Underage costs (Co + Cu)         | Mismatch costs (Co + Cu)                           |
| **Decision Rule**      | Stock more if p(demand > Q) > Cu/(Co + Cu) | Engage customers first if p_c·Cu < p_r·Co          |

### 2.2.2 Why an Inventory Model and Why Newsvendor?

Commitments to the venture are analogous to inventory: securing them can incur up-front costs and create "stickiness," but they are also perishable, as their value diminishes if not promptly matched by a corresponding commitment from the other side. Unmatched early commitments lead to costly errors, akin to obsolescence or holding costs for physical inventory. The Newsvendor model is particularly suitable as it addresses a single decision (engagement sequence) under uncertainty (who commits first) with defined mismatch penalties, mirroring a one-time order for a perishable product.

The framework treats customer and resource-partner commitments as a single "product" type because they represent opposing poles of the same value proposition; one type of commitment effectively neutralizes the mismatch risk posed by the other (like positive and negative charges or acid and base). This decision is also inherently single-period: commitments are time-sensitive ("perishable"), and the critical uncertainty is which _type_ of stakeholder will commit first, not ongoing inventory levels. The model thus focuses on this binary outcome, simplifying the problem by avoiding the need to track multiple inventory positions while still capturing the essential trade-offs through probability distributions and cost parameters.

### 2.2.3 Newsvendor Formulation and Decision Rule

After the probabilities and costs are quantified, the entrepreneur chooses a **binary sequencing action**

$$Q \in \{\text{Engage\_RP},\; \text{Engage\_C}\}. \tag{4}$$

This choice is taken _ex ante_—that is, before observing whether $D=0$ or $D=1$. Consistent with Newsvendor theory, the decision hinges on a **critical ratio ($CR$)**, which balances the costs of the two types of mismatches:
$$ CR = \frac{C_{u}}{C_{u}+C_{o}} \tag{5}$$
This $CR$ serves as the optimal decision threshold. The probability $p_r$ (that the Resource Partner commits first) is compared directly to this ratio. The sequencing rule, which minimizes the expected costs associated with stranded commitments (derived from the equivalence $p_r C_o < p_{c} C_u \Leftrightarrow p_r < CR$), is as follows:

$$\text{If } p_{\mathrm r} < CR \quad\Longrightarrow\quad \text{Engage Resource Partners first (Engage\_RP)};$$
$$\text{Otherwise (if } p_{r} \ge CR) \quad\Longrightarrow\quad \text{Engage Customers first (Engage\_C)}. \tag{6}$$

Eq.(6)'s rule directly applies the Newsvendor logic: the entrepreneur should initiate engagement with resource partners if $p_r$, the probability of resource partners committing first, falls below the critical cost-balancing threshold, $CR$. This is analogous to the standard Newsvendor solution where an optimal quantity $Q^*$ is determined such that $P(\text{Demand} \le Q^*) = CR$. Here, $p_r$ is the specific probability being evaluated against this established optimal threshold for a binary decision. If $C_u$ is high relative to $C_o$, $CR$ approaches 1, making it more likely that $p_r < CR$ and thus favoring early resource partners engagement to mitigate the high cost of a stranded customer. Conversely, if $C_o$ is high relative to $C_u$, $CR$ approaches 0, making $p_r < CR$ less likely and thus favoring early customer engagement to avoid the high cost of a stranded resource partner. Figure below illustrates this decision logic using Tesla Roadster-like parameters (pr​=0.67), demonstrating how different probability structures yield opposing optimal strategies: when the commitment probability ratio is low (pr = 0.5), the rule prescribes engaging resource partners first, whereas a commitment probability ratio (pr = 0.67) recommends to prioritize resource partners. Similar analysis can be done by varying underage and overage ratio. In the discrete Bernoulli case, the "marginal unit" is the entire switch from engaging resource partners (q=0) to engaging customers (q=1), where the continuous condition "marginal revenue = marginal cost" becomes "expected benefit of switching (pc × Cu) = expected cost of switching (pr × Co)", yielding the same critical ratio threshold pr = Cu/(Cu + Co).

![[🖼️(methods(📜🪢)).png|1000]]

> **🚗Example 4 (HYPOTHETICAL)**. When the Tesla Roadster entered pilot production, management estimated $p_{\mathrm r}=0.67$ and $p_{\mathrm c}=0.33$. Concurrent engineering studies placed the overage cost ($C_{o}$) at an aggregated \$25,000 per vehicle; this total was understood to sum key irrecoverable expenses for an unsold unit, comprising primarily 1) the direct cost of specialized components (with battery cells noted as exceeding \$17,000 of this portion) plus 2) a share of committed supplier capacity and associated logistics (e.g., with partners like Lotus or Xcellent). 
> Similarly, accounting projections established the underage cost ($C_{u}$) at an aggregated \$40,000 per vehicle; this total was understood to combine 1) the substantial lost profit margin from an unfulfilled \$109,000 Roadster sale with 2) the estimated financial impact of significant factors like reputational damage and other indirect losses stemming from the failure to meet customer commitments. The critical ratio is calculated as:
> $$CR = \frac{C_u}{C_o + C_u} = \frac{40{,}000}{25{,}000 + 40{,}000} = \frac{40{,}000}{65{,}000} = \frac{8}{13} \approx 0.615$$
> Applying the decision rule from Eq. (8): since $p_{\mathrm r} = 0.67 > CR = 0.615$, the model prescribes **engaging customers first**.

In sum, the second stage retains analytical clarity by abstracting from multi-period capacity dynamics and nonlinear utilities while re-introducing complexity only where it deepens insight: interaction modes via slope signs, probability updates after each commitment, and explicit dollar mapping of mismatch risk. This calibrated balance underpins what we term a **prediction-based prescription**: design choices forecast stakeholder behaviour, and the Newsvendor rule provides a cost-minimising sequence for engagement.
