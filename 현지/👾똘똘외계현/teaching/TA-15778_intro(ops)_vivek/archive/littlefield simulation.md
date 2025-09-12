## **Office Hour FAQ – Inventory, Capacity, and Littlefield Strategy**

- contract2 optimal right
- c/v; 
- using ggn (c_a, c_s) to calculate - 
- 150m highest score

### **1. How does the (R, Q) inventory policy work?**

- **Q (Order Quantity)**: Set using **EOQ formula**:
    
    $Q^* = \sqrt{\frac{2 D F}{H}}$
    
    where:  
    D = demand rate (units/day)  
    F = fixed order cost  
    H = annual holding cost per unit
    
- **R (Reorder Point)**: Set using **Newsvendor formula**:
    
    $R= E[DDLT] + k \cdot \sigma[DDLT]$
    
    where:  
    DDLT = demand during lead time  
    k from z-table for desired service level α, e.g., α=95% → k=1.64
    

---

### **2. How do I estimate demand for R and Q?**

- **Historical demand** → run **linear regression** on orders/day vs. day.
    
- Extrapolate to forecast **average demand** for the upcoming period.
    
- For Littlefield: Demand rises until ~day 90–110, stabilizes until day 180, then falls to zero.
    

---

### **3. How do I analyze capacity and lead time?**

- **Lead time** = **Sum of service time + wait time** at each stage. = 
    
- **Wait times** can be estimated with the **G/G/N queueing formula**:
    
    $Wq≈(Ca2+Cs2)2⋅ρ2(N+1)−1N(1−ρ)⋅1μW_q \approx \frac{(C_a^2 + C_s^2)}{2} \cdot \frac{\rho^{\sqrt{2(N+1)}-1}}{N(1-\rho)} \cdot \frac{1}{\mu}$
    
    where:  
    $C_a$ = coefficient of variation of interarrival times  
    $C_s$ = coefficient of variation of service times  
    $\rho$ = utilization  
    N = number of machines  
    μ = service rate per machine
    
- In Littlefield:
    
    - Stage 2 & 4 have fixed times.
        
    - Stage 1 & 3 have random service times (CV = 1).
        

---

### **4. How does lot size affect performance?**

- Smaller lots → more **parallel processing**, shorter lead time.
    
- But each lot at Station 3 has a **fixed setup cost/time**, so too many lots increase total cost.
    

---

### **5. What’s the trade-off in machine purchases?**

- More machines reduce queue wait times → helps meet contract lead times.
    
- But each machine costs **$1M** and has **$0 salvage value**.
    
- For Stages 2 & 4, treat machines as **separate pools** for analysis.
    

---

### **6. Which contract should I choose?**

- **Contract 1**: Easier lead time target (48 hrs), lower revenue/job ($35k).
    
- **Contract 2**: Harder target (32 hrs), higher revenue/job ($50k).  
    → Only choose Contract 2 if **predicted lead time ≤ quoted lead time** with high confidence.
    

---

### **7. How should I think about Max WIP?**

- WIP cap avoids overwhelming the factory but can **censor demand** (lost revenue).
    
- Default = 1000 jobs; adjust if queues are small and capacity is high.
    

---

### **8. Key Littlefield decision priorities**

1. **Forecast demand** and set (R, Q).
    
2. **Check capacity** and buy machines if queues are growing.
    
3. **Select contract** only when confident in meeting lead time.
    
4. Adjust **lot size** to balance speed and cost.
    
