- [[#2.0 Classic Newsvendor|2.0 Classic Newsvendor]]
- [[#2.1 Step 1: Linear Quality Model|2.1 Step 1: Linear Quality Model]]
	- [[#2.1 Step 1: Linear Quality Model#2.1.1 Mathematical setup|2.1.1 Mathematical setup]]
	- [[#2.1 Step 1: Linear Quality Model#Proposition 1|Proposition 1]]
	- [[#2.1 Step 1: Linear Quality Model#2.1.2 Business intuition (4A, 4B)|2.1.2 Business intuition (4A, 4B)]]
- [[#2.2 Step 2: Sigmoid Quality Model|2.2 Step 2: Sigmoid Quality Model]]
	- [[#2.2 Step 2: Sigmoid Quality Model#2.2.1 Mathematical setup|2.2.1 Mathematical setup]]
	- [[#2.2 Step 2: Sigmoid Quality Model#Proposition 2|Proposition 2]]
	- [[#2.2 Step 2: Sigmoid Quality Model#2.2.2  Business intuition (5A, 5B)|2.2.2  Business intuition (5A, 5B)]]
	- [[#2.2 Step 2: Sigmoid Quality Model#2.2.2 Business intuition (5A, 5B)|2.2.2 Business intuition (5A, 5B)]]
- [[#2.3 Step 2.3: Four Special Cases of the Sigmoid Model|2.3 Step 2.3: Four Special Cases of the Sigmoid Model]]
	- [[#2.3 Step 2.3: Four Special Cases of the Sigmoid Model#Proposition 2.3.1 (Symmetric Responsiveness)|Proposition 2.3.1 (Symmetric Responsiveness)]]
	- [[#2.3 Step 2.3: Four Special Cases of the Sigmoid Model#Proposition 2.3.2 (Customer‐Dominant Responsiveness)|Proposition 2.3.2 (Customer‐Dominant Responsiveness)]]
	- [[#2.3 Step 2.3: Four Special Cases of the Sigmoid Model#Proposition 2.3.3 (Partner‐Dominant Responsiveness)|Proposition 2.3.3 (Partner‐Dominant Responsiveness)]]
	- [[#2.3 Step 2.3: Four Special Cases of the Sigmoid Model#Proposition 2.3.4 (High‐Match‐Value Limit)|Proposition 2.3.4 (High‐Match‐Value Limit)]]


2025-06-15
- applied [intuitive plots explaining quality FOC cld]()
# 2 Methods

We incrementally extend the classical newsvendor along two orthogonal dimensions—**decision type** (quantity → quality → quality + quantity) and **stakeholder response** (deterministic → linear Bernoulli → sigmoid).  Naming three progressive models as three step models, step 1 model establishes the core cost-priority principle under quality-linear stakeholder responses. Step 2 model captures realistic choice behavior using quality non-linear responses. Step 3 model extends to joint quality-quantity decisions.

Table 1 situates the three propositions developed in this section.

| Step  | Decision(s)               | Random variable                                                          | New relative to classic newsvendor                                                                                                                | appendix          |
| ----- | ------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| 0     | Supply $s$                | Demand $D$                                                               |                                                                                                                                                   | [[appendix0123]] |
| **1** | quality $q$               | Customer commitment $C(q)$<br><br>Resource partner commitment $R(q)$<br> | Demand–supply asymmetry driven by quality rather than quantity<br><br>$P_c(q)=q$ , $P_r(q)=1-q$                                                   |                   |
| **2** | quality $q$               | Customer commitment $C(q)$<br><br>Resource partner commitment $R(q)$     | Statistically capture stakeholders' responsiveness to quality<br><br>$P_c(q)=\dfrac1{1+e^{-\beta_c * q}}$ , $P_r(q)=\dfrac1{1+e^{\ \beta_r * q}}$ |                   |


## 2.0 Classic Newsvendor

Step 0 (classic newsvendor) treats supply quantity as a **decision variable** that the entrepreneur directly controls before observing demand. The entrepreneur minimizes expected cost by choosing quantity $q$ to balance opportunity cost $(D-q)(p-c)$ when demand exceeds supply against overage cost $(q-D)c$ when supply exceeds demand. This yields the familiar critical fractile solution $F(q^*) = (p-c)/p$. Detail in  Appendix A.0.
## 2.1 Step 1: Linear Quality Model

Step 1 fundamentally transforms Step 0's framework by making supply a **stochastic outcome** dependent on quality decisions. The entrepreneur now chooses product quality $q \in [0,1]$, which influences both customer willingness to buy (probability $P_c(q) = q$) and resource partner willingness to supply (probability $P_r(q) = 1-q$). This creates a 2×2 probability grid with four possible outcomes: successful matches generate revenue $V$, mismatches incur either opportunity cost $C_u$ (customer wants but partner can't deliver) or overage cost $C_o$ (partner can deliver but customer doesn't want), and the no-transaction case incurs no cost. Unlike Step 0's single mismatch channel (quantity vs demand), Step 1 introduces dual mismatch risks through quality-driven stakeholder responses, fundamentally changing the optimization from a critical fractile to a dual-cost balancing rule that incorporates the match bonus $V$.

### 2.1.1 Mathematical setup

Quality choice $q\in[0,1]$ influences two stakeholders' commitments, $C(q)$ for customer and $R(q)$ for resource partner. This gives the mismatch‑loss function in Appendix A.1. This reframes newsvendor's underage cost: opportunity cost from lost sales now stem from _lack of partner supply_ rather than under‑ordering.

### Proposition 1

_Optimal quality under linear commitment probabilities_

$$
q^{*}=\frac{V+2C_o}{2\,(C_u+C_o+V)},
\qquad
\frac{\partial q^{*}}{\partial V}=\frac{C_u-C_o}{2\,(C_u+C_o+V)^{2}} .
$$

### 2.1.2 Business intuition (4A, 4B) 
> **When is $q^{*}$ high?**  
> (i) $C_o\!\gg\!C_u$—expensive surplus; managers raise quality to pull demand.  
> (ii) $V$ large *and* $C_u>C_o$—opportunity seekers court customers even at surplus risk.  
> (iii) $V$ small *and* $C_o>C_u$—risk avoiders still favour higher quality to dodge leftovers.

Throughout this paper, we call proposition 1's result "Quality adjusts to avoid the more expensive type of mismatch", **cost-priority principle**.

*Why interesting?*  
Unlike the classic critical-fractile, which moves with a single cost ratio, here the *direction* of $V$’s impact flips when the cheaper mismatch changes, highlighting a dual-cost amplification mechanism absent in quantity-only settings.

1. **Dual‑cost amplification** – raising the cheaper mismatch cost tilts $q^{*}$ toward avoiding the more expensive side. 
2. **Match bonus effect** – a larger $V$ pulls $q^{*}$ in the direction of the *scarcer* party, explaining why Step 1 departs from the pure cost ratio of Step 0. 

```
### 🚨ADD MORE to Business intuition (4A, 4B) 
$\frac{d}{d\color{red}{q}}\mathrm E[\text{Cost}]= 2C_u\,\color{red}{q}-2C_o(1-\color{red}{q})-V(1-2\color{red}{q})=0$
$\boxed{\;\color{red}{q}^{*}=\frac{\,V+2C_o\,}{2\,(C_u+C_o+V)}=\frac12\!\left[\,1+\frac{C_o-C_u}{C_u+C_o+V}\right]\;}$
*When $V=0$: $\displaystyle \color{red}{q}^{*}=1-\text{CR}$ with  
$\text{CR}=\frac{C_u}{C_u+C_o}$ (the classical critical ratio).*

### When does $\color{red}{q}^{*}$ land **high**?
1. **High $C_o$, low $C_u$** – you dread leftover stock, so you raise quality to attract customers.  
2. **High $V$** – the upside of a full match is large (e.g., $C_u=p-c>C_o=c$).  
3. **Low $V$** *and* $C_u<C_o$ – risk-averse posture: avoid unsold production.
- **Opportunity Seeker** (Cu​>Co​): Focused on **capturing every potential high-profit sale.** This person's primary fear is missing out on the high margin of a sale, so they invest in quality (q) to maximize customer demand, even if it increases production risk.    
- **Risk Avoider** (Cu​<Co​): Focused on **preventing the creation of an unsold product.** This person's primary fear is the cost of wasted production, so they adopt strategies that minimize this risk, even if it means forgoing potential low-margin sales.''
```


---
## 2.2 Step 2: Sigmoid Quality Model 
### 2.2.1 Mathematical setup 
Commitment functions become logistic: $P_c,P_r$ in Appendix A.2. This preserves the Bernoulli‐state logic while reflecting empirically observed *S‑shaped* responsiveness to quality signals. 
### Proposition 2

_Optimal quality under sigmoid commitment probabilities_

With logistic response curves $P_c(q) = \frac{1}{1+e^{-q}}$ and $P_r(q) = \frac{1}{1+e^{q}}$, the expected loss function $L(q) = C_u P_c(1-P_r) + C_o P_r(1-P_c) - V P_c P_r$ is strictly quasi-convex. The unique optimal quality is:

$$q^* = \ln\left(\frac{2C_o + V}{2C_u + V}\right)$$

The comparative static with respect to match bonus $V$ is:

$$\frac{\partial q^*}{\partial V} = \frac{2(C_u - C_o)}{(2C_u + V)(2C_o + V)}$$

### 2.2.2  Business intuition (5A, 5B)
- Behavioural steepness $(\beta_c,\beta_r)$ moderates the cost‑priority principle: when one side reacts sharply to quality, its preferences weigh more heavily in $q^{\dagger}$, potentially overriding small cost asymmetries. 

### 2.2.2 Business intuition (5A, 5B)

The sigmoid model preserves Step 1's cost-priority principle while capturing realistic S-shaped stakeholder responses. The closed-form solution $q^* = \ln\left(\frac{2C_o + V}{2C_u + V}\right)$ reveals several key insights:

**Cost-priority mechanism**: When $C_o > C_u$, we have $q^* > 0$ (positive log), pushing quality higher to avoid expensive overage. Conversely, when $C_u > C_o$, we get $q^* < 0$, lowering quality to avoid costly shortages. The match bonus $V$ moderates this effect—larger $V$ compresses the ratio toward 1, pulling $q^*$ toward 0 (the symmetric point where $P_c = P_r = 0.5$).

**Stakeholder's symmetric responsiveness to quality**: With $\beta_c = 1$ and $\beta_r = -1$, the model captures mirror-image behaviors—customers become more willing as quality rises while partners become less willing at the same rate. This symmetry enables the elegant logarithmic solution and ensures that the direction of $V$'s impact depends purely on the cost differential: $\operatorname{sgn}(\partial q^*/\partial V) = \operatorname{sgn}(C_u - C_o)$. Unlike the general case where asymmetric responsiveness parameters can override cost considerations, this special case isolates the fundamental trade-off between avoiding shortage versus overage.

**Stakeholder's asymmetric responsiveness to quality**: In the general case with arbitrary $\beta_c$ and $\beta_r$, these steepness parameters fundamentally alter the optimization landscape. Larger $|\beta_c|$ makes customers more sensitive to quality changes near their indifference point, creating a sharper transition from rejection to acceptance. Similarly, larger $|\beta_r|$ intensifies partner responsiveness. When $\beta_c \gg \beta_r$, customers react more dramatically to quality adjustments than partners, giving customer preferences greater "weight" in determining $q^*$—potentially overriding small cost differences. For instance, if $C_u$ slightly exceeds $C_o$ (suggesting lower quality), but customers are extremely responsive ($\beta_c$ very large) while partners are gradual responders ($\beta_r$ small), the optimal $q^*$ might still be high to capture the steep customer response curve. This asymmetry breaks the clean cost-priority principle: rather than $\operatorname{sgn}(\partial q^*/\partial V) = \operatorname{sgn}(C_u - C_o)$, the direction now depends on the interplay of $\beta_c P_c(1-P_c)P_r + \beta_r P_r(1-P_r)P_c$. Thus, stakeholder responsiveness asymmetries can dominate pure cost considerations, making the general case require numerical methods as no closed-form solution exists.

## 2.3 Step 2.3: Four Special Cases of the Sigmoid Model

We now present four propositions giving closed‐form $q^*$ in tractable limits of Proposition 2. Each result bundles costs and bonus into a single “net‐penalty” log‐ratio.

---

### Proposition 2.3.1 (Symmetric Responsiveness)

**Regime:** $\beta_c = \beta_r = \beta$.  
**Result:**
$$
q^* = \frac{1}{\beta}
\ln\Bigl(\frac{C_u + V}{C_o + V}\Bigr).
$$

**Intuition:**  
When both stakeholder buy‐in curves rise at the same steepness, you choose quality so that the **net penalty of under‐committing** $(C_u+V)$ balances the **net penalty of over‐committing** $(C_o+V)$. A larger match bonus $V$ raises both penalties equally, shifting $q^*$ only through their ratio.

---

### Proposition 2.3.2 (Customer‐Dominant Responsiveness)

**Regime:** $\beta_c \gg \beta_r$.  
**Result:**
$$
q^* = \frac{1}{\beta_r}
\ln\Bigl(\frac{C_o + V}{C_u}\Bigr).
$$

**Intuition:**  
With a very steep customer response, even small changes in $q$ drive customer buy‐in. The optimal $q$ trades off the **partner’s net over‐commit penalty** $(C_o+V)$ against the **under‐commit cost** $C_u$, since the customer side is effectively “all‐or‐nothing.”

---

### Proposition 2.3.3 (Partner‐Dominant Responsiveness)

**Regime:** $\beta_r \gg \beta_c$.  
**Result:**
$$
q^* = \frac{1}{\beta_c}
\ln\Bigl(\frac{C_o}{C_u + V}\Bigr).
$$

**Intuition:**  
Here the partner’s acceptance threshold is razor‐sharp, so quality is chosen to balance the **customer’s net under‐commit penalty** $(C_u+V)$ against the **partner’s over‐commit cost** $C_o$. The partner side “pins down” $q$ through its steep sigmoid.

---

### Proposition 2.3.4 (High‐Match‐Value Limit)

**Regime:** $V \gg C_u, C_o$.  
**Result:**
$$
q^* = \frac{1}{\beta_c + \beta_r}
\ln\Bigl(\frac{\beta_r}{\beta_c}\Bigr).
$$

**Intuition:**  
When the bonus for both committing dwarfs any one‐sided penalty, you maximize $P_cP_r$ directly. The optimum equalizes the **marginal gain** in each sigmoid, yielding a simple $\ln$–ratio of their slopes.

---

The table shows how the optimal quality choice depends on which stakeholder has steeper responsiveness or when the match bonus dominates individual costs. Each formula represents a different balance between commitment penalties and bonuses.

| Case                                 | Regime                      | Optimal Quality ($q^*$)                                               | Key Trade-off                                                      |
| ------------------------------------ | --------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Symmetric Responsiveness**         | $\beta_c = \beta_r = \beta$ | $\frac{1}{\beta} \ln\left(\frac{C_u + V}{C_o + V}\right)$             | Net penalty of under-committing vs. net penalty of over-committing |
| **Customer-Dominant Responsiveness** | $\beta_c \gg \beta_r$       | $\frac{1}{\beta_r} \ln\left(\frac{C_o + V}{C_u}\right)$               | Partner's net over-commit penalty vs. under-commit cost            |
| **Partner-Dominant Responsiveness**  | $\beta_r \gg \beta_c$       | $\frac{1}{\beta_c} \ln\left(\frac{C_o}{C_u + V}\right)$               | Customer's net under-commit penalty vs. partner's over-commit cost |
| **High-Match-Value Limit**           | $V \gg C_u, C_o$            | $\frac{1}{\beta_c + \beta_r} \ln\left(\frac{\beta_r}{\beta_c}\right)$ | Marginal gains in each sigmoid (maximizing $P_c P_r$)              |

To sum, when stakeholders have different sensitivities to your product quality, success often means deliberately under-serving your most responsive stakeholders. In symmetric markets where both customers and partners respond equally to quality improvements, you simply balance the costs of under- versus over-delivering. But when one group becomes highly quality-sensitive while the other remains indifferent, counterintuitively, you should cater to the less sensitive group—because the picky customers will likely commit anyway due to their steep response curve, while pushing quality too high risks losing the indifferent partners entirely. Similarly, when the reward of earning commitments from both is enormous, aiming for maximum joint buy-in probability leads to less sensitive party favoring policy.  to avoid losing the massive mutual reward. (need improvement) For entrepreneurs, this means if your tech-savvy customers demand cutting-edge features (hence $\beta_c \gg \beta_r$) but your distribution partners prefer simple, reliable products, you're better off building the simpler version—you'll keep both groups rather than losing your entire go-to-market strategy for marginal customer satisfaction gains.
