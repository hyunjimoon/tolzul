
# Module 4: 📏 sampling and optimizing
In this section, we clarify how our simulation approach generates samples and then applies a 4-step optimization to decide among **no test**, **modular**, or **integrated** learning. We break it into two parts:

  1. **Four-Part Sampling**

2. **Four-Step Optimizing**


## Four-Part Sampling

  

1. **Sample 1**: Draw $\color{green}{\phi}'$ from the **prior** distribution for market potential.

2. **Sample 2**: Draw $\color{red}{\theta}'$ from the **prior** distribution for implementation effectiveness.

- Combined, these first two steps mimic using **no additional data**—just $\color{blue}{\mu_0}$—to form $\color{brown}{EU_0}$.

1. **Sample 3**: Draw $\color{green}{\phi}''$ from the **joint true** distribution.

- This represents discovering the **true** market potential if we pay the **modular** cost $\color{brown}{c^\phi}$ and gather real data on $\color{green}{\phi}$.

2. **Sample 4**: Draw $(\color{green}{\phi}''', \color{red}{\theta}'' )$ from the **joint true** distribution.

- Here we simultaneously learn the true $\color{green}{\phi}$ and $\color{red}{\theta}$ if we pay the **integrated** cost $\color{brown}{c^{\phi\theta}}$.

  

**Why This Matters.**

- **No Test**: We rely on $\color{green}{\phi}'$ and $\color{red}{\theta}'$ from the prior, yielding $\color{brown}{EU_0}$.

- **Modular**: We replace our uncertain $\color{green}{\phi}'$ with $\color{green}{\phi}''$ (the real market potential) but still rely on prior-like assumptions about $\color{red}{\theta}'$.

- **Integrated**: We replace both $\color{green}{\phi}'$ and $\color{red}{\theta}'$ with draws $(\color{green}{\phi}''', \color{red}{\theta}'' )$ from the true joint distribution, capturing full knowledge of market potential and implementation feasibility.

  

## Four-Step Optimizing

  

We then determine which action $a \in \{\text{no test}, \text{modular}, \text{integrated}\}$ maximizes expected payoff, net of costs:

  

3. **Compute Expected Utility**:

We define $\color{brown}{EU_0}$, $\color{brown}{EU_1}$, and $\color{brown}{EU_2}$ using the sampled values. For example,

- **No test** ($\color{brown}{EU_0}$) might be $U(\color{green}{\phi}', \color{red}{\theta}')$.

- **Modular** ($\color{brown}{EU_1}$) uses $\color{green}{\phi}''$ and the prior-based approach for $\color{red}{\theta}$.

- **Integrated** ($\color{brown}{EU_2}$) uses $(\color{green}{\phi}''', \color{red}{\theta}'')$.

4. **Approximate with Samples**:

Summations (or means) over multiple samples approximate the integrals $\sum U(\phi,\theta)\, \hat P(\phi,\theta)$.

5. **Incorporate Testing Costs**:

- If choosing **modular**, pay $\color{brown}{c^\phi}$ and update $\phi$ to $\phi''$.

- If choosing **integrated**, pay $\color{brown}{c^{\phi\theta}}$ and update $(\phi,\theta)$ to $(\phi''',\theta'')$.

6. **Argmax over $\{\Delta EU_0, \Delta EU_1, \Delta EU_2\}$**:

We compare

$$

\Delta EU_1 = \color{brown}{EU_1} - \color{brown}{EU_0} - \color{brown}{c^\phi},

\quad

\Delta EU_2 = \color{brown}{EU_2} - \color{brown}{EU_0} - \color{brown}{c^{\phi\theta}},

\quad

\text{and }

\Delta EU_0=0.

$$

Choosing the action with the highest increment ensures we maximize payoff net of cost.

---


Must have sufficient resources for chosen testing approach- Conditions for choosing modular learning

- Conditions for choosing integrated learning

- Resource constraints consideration

specifically,
## Modular Case:
```
ΔEU₁ < 0, ΔEU₂ > 0
```
- Choose modular learning when market test alone provides sufficient information
- Cost-effective for high uncertainty in market potential

## Integrated Case:
```
ΔEU₁ > 0, ΔEU₂ > 0
```
- Choose integrated learning when both market and implementation testing needed
- Necessary for high uncertainty in both dimensions

## Resource Constraint:
```
resource ≥ c_φ (modular)
resource ≥ c_φθ (integrated)
```
Must have sufficient resources for chosen testing approach