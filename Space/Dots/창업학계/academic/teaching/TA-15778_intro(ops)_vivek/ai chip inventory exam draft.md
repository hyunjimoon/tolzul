## 3 Inventory Management: NeuralCore's AI Chip Decisions (45 points)

NeuralCore designs AI accelerator chips and, like NVIDIA, depends entirely on TSMC for manufacturing. They face two distinct inventory decisions:

**Decision 1 - Special Production Run (Newsvendor):** For a new customer (Tesla), NeuralCore must decide how many chips to produce in a one-time run. These chips are custom-designed and become obsolete after Tesla's model year ends.

**Decision 2 - Regular Operations ((R,Q) Policy):** For standard AI chips sold to multiple customers, NeuralCore maintains ongoing inventory. They order in batches of Q = 50,000 chips and reorder when inventory hits level R.

**Why This Matters:** Single-source dependency on TSMC means any disruption affects both decisions differently.

**Current Operating Parameters:**

- Daily demand: μ = 1,000 chips, σ = 1,000 chips (high uncertainty due to AI market volatility)
- Selling price: $1,000/chip
- Manufacturing cost: $200/chip
- End-of-life value: $0 (obsolete chips cannot be resold)
- TSMC lead time: 10 days currently
- Required service level: 97.7% (k = 2.0) due to customer contracts

### Part A: Understanding Both Models (15 points)

1. **(3 points)** For the Tesla one-time run, calculate the critical ratio α. What does this ratio represent in business terms?
    
2. **(3 points)** Using k = 2.0, how many chips should NeuralCore produce for Tesla? (newsvendor q*)
    
3. **(3 points)** For regular operations with Q = 50,000, what is the expected demand during TSMC's lead time?
    
4. **(3 points)** Calculate the reorder point R* for regular operations.
    
5. **(3 points)** Of the inventory at the reorder point, how much is buffer stock versus expected demand?
    

### Part B: Supply Chain Disruptions (20 points)

_Each scenario below affects NeuralCore's decisions differently:_

6. **(4 points)** **AI Boom Scenario:** ChatGPT-5 launch quadruples daily demand (μ = 4,000, σ = 1,000).
    
    - Calculate new quantities for both Tesla run (q*) and regular operations (R*)
    - Explain why the impacts differ
7. **(4 points)** **Market Chaos:** Crypto mining demand creates volatility (μ = 1,000, σ = 2,500).
    
    - How does this change the Tesla one-time production quantity?
8. **(4 points)** **Premium Pricing:** Chip shortage allows $2,000/chip pricing.
    
    - Does this affect the one-time run quantity? The reorder point? Explain.
9. **(4 points)** **Taiwan Tensions:** Shipping disruptions extend TSMC lead time to 27 days.
    
    - Which decision model is affected and by how much?
10. **(4 points)** Based on your calculations: "To double inventory levels requires: mean demand to increase __×, OR volatility to increase __×, OR lead time to increase __×"
    

### Part C: Product Mix Strategy (9 points)

NeuralCore sells two products with identical demand patterns (μ = 1,000, σ = 1,000):

- **AI Accelerator:** Price $1,000, Cost $200, Obsolete value $0
- **Basic GPU:** Price $100, Cost $80, Obsolete value $0

11. **(3 points)** Calculate the service level (α) each product should target.
    
12. **(3 points)** Which product justifies carrying more safety stock? Show calculations.
    
13. **(3 points)** A manager suggests: "Since Basic GPU has lower margins, we should set a lower reorder point." Is this correct for (R,Q) policy? Explain.
    

### Part D: Strategic Implementation (8 points)

14. **(5 points)** Your CFO asks: "Why does doubling volatility have more impact than doubling average demand?" Write a 100-word explanation using your calculations from Part B.
    
15. **(3 points)** **Nightmare Scenario:** AI demand doubles AND Taiwan blockade doubles lead time. Calculate the combined impact on reorder point.
    

### Bonus: Breaking TSMC Dependency (10 points)

16. **(10 points)** NeuralCore evaluates Intel Foundry as a second source:
    
    **Proposed Split:**
    
    - TSMC: 70% of volume, 10-day lead time, reliable
    - Intel: 30% of volume, 20-day lead time, new partner
    
    a) Calculate separate reorder points for each supplier b) Compare total safety stock to current single-source approach  
    c) Beyond the math: What risk does this strategy NOT address?
    


-----
## Model Answer - NeuralCore's AI Chip Decisions

### Part A: Understanding Both Models (15 points)

**1. (3 points)**

- Critical ratio α = (r-c)/(r-c+c-s) = (1000-200)/(1000-200+200-0) = 800/1000 = **0.8**
- Business meaning: NeuralCore should produce enough chips to meet demand 80% of the time. The 20% stockout risk is economically optimal given the high margins.

**2. (3 points)**

- Newsvendor q* = μ + k·σ = 1,000 + 2(1,000) = **3,000 chips**

**3. (3 points)**

- E[DDLT] = μ × LT = 1,000 × 10 = **10,000 chips**

**4. (3 points)**

- σ[DDLT] = σ × √LT = 1,000 × √10 = 3,162 chips
- R* = E[DDLT] + k·σ[DDLT] = 10,000 + 2(3,162) = **16,324 chips**

**5. (3 points)**

- Buffer stock = k·σ[DDLT] = 6,324 chips
- Expected demand = 10,000 chips
- Buffer stock percentage = 6,324/16,324 = **38.7%**

### Part B: Supply Chain Disruptions (20 points)

**6. (4 points)**

- Tesla run: q* = 4,000 + 2(1,000) = **6,000 chips** (2× increase)
- Regular ops: R* = 40,000 + 2(3,162) = **46,324 chips** (2.84× increase)
- **Why different:** Newsvendor doubles because both mean and safety stock terms scale with demand. R* doesn't double because safety stock (k·σ·√LT) remains unchanged when only μ increases.

**7. (4 points)**

- New q* = 1,000 + 2(2,500) = **6,000 chips**
- This doubles the original quantity (3,000 → 6,000)

**8. (4 points)**

- New α = (2000-200)/(2000-200+200-0) = 1800/2000 = 0.9
- For α = 0.9, k ≈ 1.28 (not 2.0)
- **One-time run:** Affected but doesn't double (need k ≈ 4 to double)
- **Reorder point:** Unaffected - R* stays at 16,324 because (R,Q) doesn't depend on prices

**9. (4 points)**

- Only affects (R,Q) model
- New R* = 1,000(27) + 2(1,000√27) = 27,000 + 10,392 = **37,392 chips**
- Factor increase = 37,392/16,324 = **2.29×**

**10. (4 points)**

- Mean demand: **4×**
- Volatility: **2.5×**
- Lead time: **2.7×**

### Part C: Product Mix Strategy (9 points)

**11. (3 points)**

- AI Accelerator: α = 800/1000 = **0.8**
- Basic GPU: α = 20/100 = **0.2**

**12. (3 points)**

- AI Accelerator: k = 0.84, safety stock = 0.84(3,162) = **2,656 chips**
- Basic GPU: k = -0.84, safety stock = **-2,656 chips**
- **AI Accelerator needs more** - high margins justify holding safety stock

**13. (3 points)**

- **Manager is incorrect.** R* = μ·LT + k·σ·√LT doesn't include price/cost terms. Both products have R* = 16,324 if using same service level (k = 2.0). The (R,Q) model separates inventory decisions from economics.

### Part D: Strategic Implementation (8 points)

**14. (5 points)** _Sample answer:_ "Volatility has more leverage because it enters inventory formulas directly through safety stock (k·σ), while mean demand is 'diluted' by the constant safety stock term. In newsvendor: q* = μ + k·σ, doubling σ adds 2,000 units, but doubling μ only adds 1,000. With k=2, volatility has twice the marginal impact. In (R,Q), the √LT factor further amplifies volatility's effect while mean scales linearly."

**15. (3 points)**

- New R* = 2,000(20) + 2(1,000√20) = 40,000 + 8,944 = **48,944 chips**
- Factor increase = 48,944/16,324 = **3.0×** (multiplicative risk)

### Bonus: Breaking TSMC Dependency (10 points)

**16a. (4 points)**

- TSMC (70%): R* = 700(10) + 2(√700√10) = 7,000 + 1,674 = **8,674 chips**
- Intel (30%): R* = 300(20) + 2(√300√20) = 6,000 + 1,342 = **7,342 chips**

**16b. (3 points)**

- Dual-source safety stock: 1,674 + 1,342 = 3,016 chips
- Single-source safety stock: 6,324 chips
- **Reduction: 52%** due to risk pooling

**16c. (3 points)** Risks NOT addressed:

- **Correlated failures:** Both suppliers could face simultaneous disruptions (e.g., global chip shortage)
- **Quality risk:** Intel's new process might have yield issues
- **Capacity risk:** If TSMC fails completely, Intel can't handle 100% volume

---

**Grading Notes:**

- Full credit for correct formulas even with minor calculation errors
- Partial credit for right approach with wrong numbers
- Emphasis on explaining intuition, not just calculations
- Bonus requires understanding beyond formulas