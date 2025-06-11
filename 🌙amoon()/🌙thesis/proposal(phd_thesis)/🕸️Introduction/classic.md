# The Newsvendor Model: A Complete Guide

_Understanding optimal inventory decisions under demand uncertainty_

---

## 🎯 The Problem

A retailer must decide how much inventory to order before knowing actual customer demand. Order too little → miss sales. Order too much → waste money on unsold items.

**The question**: What's the optimal order quantity?

---

## 📊 Key Variables

|Symbol|Meaning|Type|
|---|---|---|
|$\color{red}q$|**Order quantity** (our decision)|🔴 Decision|
|$\color{skyblue}D$|**Customer demand** (random)|🔵 Random|
|$\color{green}p$|**Selling price** per unit|💰 Given|
|$\color{green}c$|**Purchase cost** per unit|💰 Given|

### Probability Distributions

- **Cumulative Distribution**: $\color{skyblue}F(\color{red}q) = P(\color{skyblue}D \leq \color{red}q)$
- **Probability Density**: $\color{skyblue}f(x) = \frac{d}{dx}\color{skyblue}F(x)$

---

## 💸 The Two Types of Costs

### 1. **Overage Cost** (Too much inventory)

- **When**: Demand $\color{skyblue}D$ ≤ Order quantity $\color{red}q$
- **Cost per unit**: $\color{green}c$ (we paid for items we can't sell)
- **Total cost**: $(\color{red}q - \color{skyblue}D) \times \color{green}c$

### 2. **Opportunity Cost** (Too little inventory)

- **When**: Demand $\color{skyblue}D$ > Order quantity $\color{red}q$
- **Lost profit per unit**: $\color{green}p - \color{green}c$
- **Total cost**: $(\color{skyblue}D - \color{red}q) \times (\color{green}p - \color{green}c)$

---

## 🧮 Mathematical Derivation

### Step 1: Expected Cost Framework

We want to minimize the expected total cost:

$$\text{Expected Cost} = \text{Expected Overage} + \text{Expected Opportunity Cost}$$

### Step 2: Breaking Down by Cases

**Overage scenario** ($\color{skyblue}{D} \leq \color{red}{q}$): $\text{Expected Overage} = \mathbb{E}[(\color{red}{q} - \color{skyblue}{D}) \color{green}{c} \mid \color{skyblue}{D} \leq \color{red}{q}] \times P(\color{skyblue}{D} \leq \color{red}{q})$

**Opportunity cost scenario** ($\color{skyblue}{D} > \color{red}{q}$): $\text{Expected Opportunity} = \mathbb{E}[(\color{skyblue}{D} - \color{red}{q})(\color{green}{p} - \color{green}{c}) \mid \color{skyblue}{D} > \color{red}{q}] \times P(\color{skyblue}{D} > \color{red}{q})$

### Step 3: Combining the Terms

$\begin{aligned} \text{Expected Cost} &= \color{green}{c} \cdot \mathbb{E}[\color{red}{q} - \color{skyblue}{D} \mid \color{skyblue}{D} \leq \color{red}{q}] \cdot \color{skyblue}{F}(\color{red}{q}) \ &\quad + (\color{green}{p} - \color{green}{c}) \cdot \mathbb{E}[\color{skyblue}{D} - \color{red}{q} \mid \color{skyblue}{D} > \color{red}{q}] \cdot [1 - \color{skyblue}{F}(\color{red}{q})] \end{aligned}$

### Step 4: Converting to Integrals

$\begin{aligned} \text{Expected Cost} &= \color{green}{c} \left(\color{red}{q} \color{skyblue}{F}(\color{red}{q}) - \int_{x \leq \color{red}{q}} x \color{skyblue}{f}(x) dx\right) \ &\quad + (\color{green}{p} - \color{green}{c}) \left(\int_{x > \color{red}{q}} x \color{skyblue}{f}(x) dx - \color{red}{q}[1 - \color{skyblue}{F}(\color{red}{q})]\right) \end{aligned}$

### Step 5: Simplifying the Expression

After algebraic manipulation:

$\begin{aligned} \text{Expected Cost} &= \color{green}{p} \int_{x > \color{red}{q}} x \color{skyblue}{f}(x) dx - \color{green}{p} \color{red}{q} + \color{green}{p} \color{red}{q} \color{skyblue}{F}(\color{red}{q}) \ &\quad + \color{green}{c} \color{red}{q} - \color{green}{c} \mathbb{E}[\color{skyblue}{D}] \end{aligned}$

---

## 🎯 Finding the Optimal Solution

### Taking the Derivative

To minimize cost, we differentiate with respect to $\color{red}{q}$:

$\frac{\partial}{\partial \color{red}{q}} \text{Expected Cost} = \color{green}{p} \color{skyblue}{F}(\color{red}{q}) + \color{green}{c} - \color{green}{p}$

### Setting Equal to Zero

For the optimal order quantity $\color{red}{q}^*$:

$\color{green}{p} \color{skyblue}{F}(\color{red}{q}^*) + \color{green}{c} - \color{green}{p} = 0$

### **The Critical Fractile Solution**

$\boxed{\color{skyblue}{F}(\color{red}{q}^*) = \frac{\color{green}{p} - \color{green}{c}}{\color{green}{p}}}$

---

## 💡 Business Interpretation

### The Critical Fractile Formula

$$\text{Optimal Service Level} = \frac{\text{Profit Margin}}{\text{Selling Price}}$$

### What This Means:

- **High profit margin** → Order more (higher service level)
- **Low profit margin** → Order less (lower service level)
- **Equal costs** → 50% service level

### Example:

- Selling price: $\color{green}p = $10$
- Purchase cost: $\color{green}c = $6$
- Optimal service level: $\frac{10-6}{10} = 40%$

**Translation**: Order enough to meet 40% of possible demand scenarios.

---

## 🚀 Key Takeaways

1. **Balance is crucial**: Too much inventory wastes money, too little loses sales
2. **Profit margins matter**: Higher margins justify higher inventory levels
3. **It's about probabilities**: We're optimizing against uncertainty, not perfect information
4. **Simple formula, powerful insight**: The critical fractile gives us the exact answer

This model forms the foundation for countless supply chain and inventory management decisions across industries worldwide.