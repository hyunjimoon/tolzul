---
collection:
  - "[[Papers]]"
author_ids:
field:
  - 🐅cba
created: 2024-12-25
---

# 5. Bayesian Learning Through Experiments

## 5.1 Experiments to Test and Update Prior Beliefs

Given a prior belief, an entrepreneur may choose to resolve uncertainty before launching their venture. Experiments surface signals of the underlying state variable, updating the probability distribution $\mu_\Theta(\theta)$ to $\mu'_\Theta(\theta)$, and consequently updating $V_\Theta$, $\tilde{V}_\Theta$, and $V$ (their prior belief).

### Key Equations
1. Expected value under the updated theory:

   $$E_{\theta \in \Theta}[v(\theta) | \mu'_\Theta] = V'_\Theta = \int_{\theta \in \Theta} v(\theta) \mu'_\Theta(\theta) d\theta$$

2. Updated expected value:

   $$V' = \omega' V'_\Theta + (1 - \omega') V'_\tilde{\Theta}$$

### Threshold for Updating Prior-on-Prior
When the distance $\| \mu' - \mu \|$ between distributions exceeds a threshold $\mu^*$, entrepreneurs also update their prior-on-prior $\omega$ to $\omega'$. This indicates a shift in perspective on both the opportunity and the underlying conceptual structure.

### Conceptual vs Real Experiments
- **Conceptual**: Use hypothetical observations and reasoning.
- **Real**: Collect quantitative or qualitative data.

## 5.2 Experimenting With Alternative Theories

Entrepreneurs may explore alternative theories characterized by a different state space and causal links. The unconditional expected value $Q$ of an alternative theory is calculated similarly to $V$.

- **Exploration Zones**: Figure 2 (described below) illustrates zones of exploration for both the main and alternative theories.

#### Figure 2 Description
"Value of Experimentation and Exploration Zones"
- X-axis: Experiment stages.
- Y-axis: Expected value.
- Two exploration zones: One for theory $\Theta$, another for an alternative theory.
- Indicates scenarios where experimenting with more uncertain theories adds value.

## 5.3 Prior Belief Updating

Bayesian entrepreneurs update their prior beliefs using Bayes' theorem. Upper-level updating occurs in two ways:

1. **Reverse Bayesianism**:
   - Proportional shifts in probabilities for unforeseen contingencies.
2. **Hypothesis-Testing Model**:
   - Standard Bayesian updating, but with non-Bayesian reactions to low-probability events.

## 5.4 Illustrative Example

### Original Theory
- Attributes: $X_d$, $X_e$, $X_s$, $X_h$.
- Causal structure:

  $$p(x_d, x_e, x_s, x_h | \theta) = p(x_d | \theta_{des}, x_e, x_s)p(x_e | \theta_e)p(x_s | \theta_{sh}, x_h)p(x_h | \theta_h)$$

- Linear approximation:

  $$v(\theta) = \theta_{de} \theta_e + \theta_{ds} \theta_{sh} \theta_h$$

### Alternative Theory
- Attributes: $X_p$, $X_d$, $X_s$, $X_i$.
- Causal structure:

  $$p(x_p, x_d, x_s, x_i | \theta) = p(x_p | \theta_{pds}, x_d, x_s)p(x_i | \theta_i)p(x_s | \theta_{si}, x_i)p(x_d | \theta_d)$$

- Linear approximation:

  $$v(\theta) = \theta_{pd} \theta_d + \theta_{ps} \theta_{si} \theta_i$$

The founder explores the alternative theory by testing parameters, updating $\mu'(\theta)$, and increasing $V'$ and $V'_\Theta$.
