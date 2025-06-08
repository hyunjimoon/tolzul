[[2predict(ent, commit(rp_c))|2predict(ent, commit(rp_c))]]
## 2.2 Second Stage: Sequencing Engagement through a Newsvendor Lens

The second stage is organized into three subsections: (i) _Inputs & Cost Architecture, (ii)  Why a single-period Newsvendor backbone is appropriate and (iii) Newsvendor Formulation and Decision Rule.
### 2.2.1 Inputs & Cost Architecture

The only numerical information inherited from Stage 1 are **first-commitment probabilities**: $p_{\mathrm r}$ represents the probability that a resource-partner is the first stakeholder to sign, while $p_{\mathrm c}=1-p_{\mathrm r}$ represents the complementary probability that a customer signs first. The demand uncertainty is about "who commits first". This is encoded in a single binary random variable

$$ D = 2*\operatorname{Bernoulli}(p_{\mathrm c})-1, \qquad D\in{-1,1}. \tag{3} $$

The interpretation is direct: a realization $D=-1$ indicates that commitment "demand'' (viewing supply as negative demand) arrives first from the resource partner side, whereas $D=1$ indicates that demand originates with customers. 

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

This choice is taken _ex ante_—that is, before observing whether $D=-1$ or $D=1$. Consistent with Newsvendor theory, the decision hinges on a **critical ratio ($CR$)**, which balances the costs of the two types of mismatches:
$$ CR = \frac{C_{u}}{C_{u}+C_{o}} \tag{5}$$
This $CR$ serves as the optimal decision threshold. The probability $p_r$ (that the Resource Partner commits first) is compared directly to this ratio. The sequencing rule, which minimizes the expected costs associated with stranded commitments (derived from the equivalence $p_r C_o < p_{c} C_u \Leftrightarrow p_r < CR$), is as follows:

$$\text{If } p_{\mathrm r} < CR \quad\Longrightarrow\quad \text{Engage Resource Partners first (Engage\_RP)};$$
$$\text{Otherwise (if } p_{r} \ge CR) \quad\Longrightarrow\quad \text{Engage Customers first (Engage\_C)}. \tag{6}$$

Eq.(6)'s rule directly applies the Newsvendor logic: the entrepreneur should initiate engagement with resource partners if $p_r$, the probability of resource partners committing first, falls below the critical cost-balancing threshold, $CR$. This is analogous to the standard Newsvendor solution where an optimal quantity $Q^*$ is determined such that $P(\text{Demand} \le Q^*) = CR$. Here, $p_r$ is the specific probability being evaluated against this established optimal threshold for a binary decision. If $C_u$ is high relative to $C_o$, $CR$ approaches 1, making it more likely that $p_r < CR$ and thus favoring early resource partners engagement to mitigate the high cost of a stranded customer. Conversely, if $C_o$ is high relative to $C_u$, $CR$ approaches 0, making $p_r < CR$ less likely and thus favoring early customer engagement to avoid the high cost of a stranded resource partner. Figure below illustrates this decision logic using Tesla Roadster-like parameters (pr​=0.67), demonstrating how different probability structures yield opposing optimal strategies: when the commitment probability ratio is low (pr = 0.5), the rule prescribes engaging resource partners first, whereas a commitment probability ratio (pr = 0.67) recommends to prioritize resource partners. Similar analysis can be done by varying underage and overage ratio. In the discrete Bernoulli case, the "marginal unit" is the entire switch from engaging resource partners (q=0) to engaging customers (q=1), where the continuous condition "marginal revenue = marginal cost" becomes "expected benefit of switching (pc × Cu) = expected cost of switching (pr × Co)", yielding the same critical ratio threshold pr = Cu/(Cu + Co).

![[🖼️(methods(📜🪢)).png|100]]

> **🚗Example 4 (HYPOTHETICAL)**. When the Tesla Roadster entered pilot production, management estimated $p_{\mathrm r}=0.67$ and $p_{\mathrm c}=0.33$. Concurrent engineering studies placed the overage cost ($C_{o}$) at an aggregated \$25,000 per vehicle; this total was understood to sum key irrecoverable expenses for an unsold unit, comprising primarily 1) the direct cost of specialized components (with battery cells noted as exceeding \$17,000 of this portion) plus 2) a share of committed supplier capacity and associated logistics (e.g., with partners like Lotus or Xcellent). 
> Similarly, accounting projections established the underage cost ($C_{u}$) at an aggregated \$40,000 per vehicle; this total was understood to combine 1) the substantial lost profit margin from an unfulfilled \$109,000 Roadster sale with 2) the estimated financial impact of significant factors like reputational damage and other indirect losses stemming from the failure to meet customer commitments. The critical ratio is calculated as:
> $$CR = \frac{C_u}{C_o + C_u} = \frac{40{,}000}{25{,}000 + 40{,}000} = \frac{40{,}000}{65{,}000} = \frac{8}{13} \approx 0.615$$
> Applying the decision rule from Eq. (8): since $p_{\mathrm r} = 0.67 > CR = 0.615$, the model prescribes **engaging customers first**.

In sum, the second stage retains analytical clarity by abstracting from multi-period capacity dynamics and nonlinear utilities while re-introducing complexity only where it deepens insight: interaction modes via slope signs, probability updates after each commitment, and explicit dollar mapping of mismatch risk. This calibrated balance underpins what we term a **prediction-based prescription**: design choices forecast stakeholder behaviour, and the Newsvendor rule provides a cost-minimising sequence for engagement.
