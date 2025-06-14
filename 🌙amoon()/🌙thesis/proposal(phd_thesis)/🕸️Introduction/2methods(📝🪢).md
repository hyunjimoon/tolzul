- [[#2.0 Classic Newsvendor|2.0 Classic Newsvendor]]
	- [[#2.0 Classic Newsvendor#How Step 1 differs from Step 0|How Step 1 differs from Step 0]]
- [[#2.1 Step 1: Linear Quality Model|2.1 Step 1: Linear Quality Model]]
	- [[#2.1 Step 1: Linear Quality Model#2.1.1 Mathematical setup|2.1.1 Mathematical setup]]
	- [[#2.1 Step 1: Linear Quality Model#Proposition 1|Proposition 1]]
	- [[#2.1 Step 1: Linear Quality Model#2.1.2 Business intuition (4A, 4B)|2.1.2 Business intuition (4A, 4B)]]
- [[#2.2 Step 2: Sigmoid Quality Model|2.2 Step 2: Sigmoid Quality Model]]
	- [[#2.2 Step 2: Sigmoid Quality Model#2.2.1 Mathematical setup|2.2.1 Mathematical setup]]
	- [[#2.2 Step 2: Sigmoid Quality Model#Proposition 2|Proposition 2]]
	- [[#2.2 Step 2: Sigmoid Quality Model#2.2.2  Business intuition (5A, 5B)|2.2.2  Business intuition (5A, 5B)]]


# 2 Methods

We incrementally extend the classical newsvendor along two orthogonal dimensions—**decision type** (quantity → quality → quality + quantity) and **stakeholder response** (deterministic → linear Bernoulli → sigmoid).  Naming three progressive models as three step models, step 1 model establishes the core cost-priority principle under quality-linear stakeholder responses. Step 2 model captures realistic choice behavior using quality non-linear responses. Step 3 model extends to joint quality-quantity decisions.

Table 1 situates the three propositions developed in this section.

| Step  | Decision(s)               | Random variable                                                          | New relative to classic newsvendor                                                                                                                | appendix          |
| ----- | ------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| 0     | Supply $s$                | Demand $D$                                                               |                                                                                                                                                   | [[step012-need3]] |
| **1** | quality $q$               | Customer commitment $C(q)$<br><br>Resource partner commitment $R(q)$<br> | Demand–supply asymmetry driven by quality rather than quantity<br><br>$P_c(q)=q$ , $P_r(q)=1-q$                                                   |                   |
| **2** | quality $q$               | Customer commitment $C(q)$<br><br>Resource partner commitment $R(q)$     | Statistically capture stakeholders' responsiveness to quality<br><br>$P_c(q)=\dfrac1{1+e^{-\beta_c * q}}$ , $P_r(q)=\dfrac1{1+e^{\ \beta_r * q}}$ |                   |
| **3** | quality $q$, quantity $Q$ | Customer commitment $C(q)$<br><br>Resource partner commitment $R(q)$     | Joint quality–quantity choice with diminishing–return revenue $R(Q)=aQ-bQ^{2}$                                                                    |                   |

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
