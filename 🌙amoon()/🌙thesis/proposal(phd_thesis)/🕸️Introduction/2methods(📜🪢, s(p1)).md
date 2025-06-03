[[🗄️(methods(📜🪢))]]
## 2. Model

We develop a model of entrepreneurial stakeholder sequencing where an entrepreneur must decide whether to engage resource partners or customers first under uncertainty about acceptance probabilities and interdependence effects.

### 2.1 Model Setup

#### 2.1.1 Players and Timing

Consider an entrepreneur (E) who needs to secure both a resource partner (R) and customers (C) to create value. The model unfolds over three periods:

- **Period 0**: The entrepreneur decides the sequence of stakeholder engagements
- **Period 1**: The entrepreneur engages with the first chosen stakeholder
- **Period 2**: The entrepreneur engages with the second stakeholder (if first succeeds)

The entrepreneur has limited resources to engage stakeholders sequentially, not simultaneously.

#### 2.1.2 Technology and Payoffs

Let $s_i \in {0, 1}$ denote stakeholder $i$'s acceptance state, where $i \in {R, C}$:

- $s_i = 1$: Stakeholder $i$ accepts the venture's value proposition
- $s_i = 0$: Stakeholder $i$ rejects the venture's value proposition

The venture state is characterized by the tuple $(s_R, s_C)$, with four possible states:

- $(0,0)$: No stakeholder acceptance
- $(1,0)$: Only resource partner accepts
- $(0,1)$: Only customer accepts
- $(1,1)$: Both stakeholders accept

**Value Creation**: The venture creates value $V > 0$ if and only if $(s_R, s_C) = (1,1)$.

**Mismatch Costs**: Being in states $(1,0)$ or $(0,1)$ generates costs:

- <span style="color:green">C_o</span>: Overage cost when $(s_R, s_C) = (1,0)$ - having resources but no customers
- <span style="color:violet">C_u</span>: Underage cost when $(s_R, s_C) = (0,1)$ - having customers but no resources

These costs capture inefficiencies from stakeholder mismatch (e.g., idle capacity, unmet demand).

#### 2.1.3 Entrepreneur's Decision Problem

The entrepreneur chooses a sequence $\sigma \in {RC, CR}$:

- $\sigma = RC$: Engage resource partner first, then customer
- $\sigma = CR$: Engage customer first, then resource partner

Let $\tau_i$ denote the period when stakeholder $i$ is engaged under sequence $\sigma$.

### 2.2 Analysis: Deterministic Environment

We begin with the baseline case where acceptance is deterministic: if the entrepreneur engages stakeholder $i$, then $s_i = 1$ with certainty.

#### 2.2.1 Entrepreneur's Optimization Problem

The entrepreneur's problem is:

$$\max_{\sigma \in {RC, CR}} \pi(\sigma)$$

where the payoff from sequence $\sigma$ is:

$$\pi(RC) = V - C_o$$ $$\pi(CR) = V - C_u$$

**Proposition 1** (Deterministic Sequencing): In the deterministic environment, the optimal sequence is:

- $\sigma^* = CR$ if <span style="color:green">C_o</span> > <span style="color:violet">C_u</span>
- $\sigma^* = RC$ if <span style="color:green">C_o</span> < <span style="color:violet">C_u</span>

_Proof_: Direct comparison of $\pi(RC)$ and $\pi(CR)$ yields: $$\pi(CR) > \pi(RC) \iff \text{<span style="color:green">}C_o\text{</span>} > \text{<span style="color:violet">}C_u\text{</span>}$$

**Economic Intuition**: The entrepreneur minimizes the larger mismatch cost by avoiding the stakeholder more likely to create costly imbalance.

