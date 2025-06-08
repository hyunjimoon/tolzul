
# 2. Model
We model a two stage value proposition design then stakeholder prioritization problem Sec.2.1. explains the first stage which maps a value-proposition vector into Bernoulli distribution prediction on which stakeholder will commit first. Given this demand forecast, Sec.2.2 then chooses which stakeholder to engage with first by minimizing expected cost of a mismatch.
### 2.1 First Stage: Predicting First-Commitment Probabilities given Value Proposition 

The first stage is organized into three subsections: (i) Stakeholder utilities given value proposition, (ii) Classifying stakeholder interaction,  (iii) Predicting first-commitment probabilities. We start by modeling the entrepreneur’s value proposition design as **value-proposition vector**

$$x=[x_1,\dots ,x_K]^{\top}, \tag{0}$$

where, in the illustrative case, $x_1$ denotes **price** (USD) and $x_2$ denotes perceived **quality** (Likert 1–5). The purpose of Stage 1 is to translate x into the probability that either stakeholder (resource partner or customer) will become the first to commit.

### 2.1.1 Stakeholder Utilities given Value Proposition

Each stakeholder $j\in\{\mathrm{\mathrm Resource \; Partner, \mathrm Customer}\}$ evaluates the design through a linear utility function

$$U_j(x)=\beta_{0j}+\beta_{1j}\,{\text{price}}+\beta_{2j}\,{\text{quality}}. \tag{1}$$

The slopes $\beta_{1j}$ and $\beta_{2j}$ quantify the marginal effects of price and quality on stakeholders' perceived attractiveness of entrepreneur's value proposition.

### 2.1.2 Classifying stakeholder interaction (- low priority)

Sign pattern of price and quality coefficient from Eq. (1)  partitions the engagement landscape into three empirically testable modes:

| Mode              | Formal criterion                                        | Economic interpretation                                                                                    |
| ----------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Substitutive**  | $\beta_{0j}=\beta_{2j}=0$<br>$\beta_{1RP}*\beta_{1C}<0$ | An attribute that pleases one side repels the other (high price helps resource partners, hurts customers). |
| **Complementary** | $\beta_{0j}=\beta_{1j}=0$<br>$\beta_{2RP}*\beta_{2C}>0$ | An attribute that moves utilities in the same direction for both sides (higher quality pleases all).       |
| **Independent**   | $\beta_{1j}=\beta_{2j}=0$                               | The attribute is inconsequential for at least one side; engagement depends on other factors.               |

> **🚗Example1 (HYPOTHETICAL).** For the Tesla Roadster (2006–08) data,  $\beta_{1\mathrm{RP}}=+0.015$ implies that a \$ 5k price reduction lowers resource partner's utility by 0.075 utils, whereas $\beta_{1\mathrm C}=-0.012$ raises customer utility by $5\times0.012=0.06$ utils. Different signs verify price attribute's substitutive effect. Decreasing price makes it more likely, customer commit before resource partner.

### 2.1.3 Predicting first-commitment probabilities

To convert utilities into probabilities we employ a standard logit transformation. First, each utility in (1) is exponentiated to obtain a positive _attractiveness weight_; next, the weights are normalized so they sum to one:

$$p_{\mathrm r}=\frac{\exp[U_{\mathrm{RP}}(x)]}{\exp[U_{\mathrm{RP}}(x)]+\exp[U_{\mathrm C}(x)]}, \qquad p_{\mathrm c}=1-p_{\mathrm r}. \tag{2}$$

Even small utility changes—such as the 0.06-util uplift from **example 1**—alter the exponent and can result in different optimal engaging sequence.

> **🚗Example2.** Applying Eq. (1) to the Roadster’s \$109k list price and quality = 5 positioning yields $U_{\mathrm{RP}}=1.64$ and $U_{\mathrm C}=0.78$. Substituting these values into Eq. (2) produces $p_{\mathrm r}=0.67$ and $p_{\mathrm c}=0.33$. 

