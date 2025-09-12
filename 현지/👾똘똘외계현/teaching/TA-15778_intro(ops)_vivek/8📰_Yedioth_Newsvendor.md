# Class 8: Yedioth Newsvendor Model (📰)
*Aug 1, 2025 | [Transcript](8nv(📰)15778_intro_ops_otter_ai.md)*

## 🎯 Teaching Arc
**Hook**: "14,000 SKUs, weekly delivery, unpredictable demand"  
**Puzzle**: How optimize inventory when demand is censored?  
**Resolution**: Pool data + newsvendor model with service levels  
**Model**: Q* = √(2DF/H) + safety stock for uncertainty

## 🗣️ Quality Participation

**Joe** ⭐: "Can update Q after first cycle vs online learning"
- Prof: Appreciated complexity awareness
- Impact: ⭐️"Changing Q complicates policy, makes fragile"

**Key Discussion**: Service level trade-offs
- u/(u+o) formula for target service (95%)
- "Hate runout AND hate inventory"

## 📊 Quick Scores
Focus on students who:
- Question model assumptions
- Identify implementation challenges
- Connect theory to practical constraints

## 🔗 421 Diagram

### Yedioth Model
```
    🟢 Weekly delivery      🟣 Small retailers
       Sales data             14,000 SKUs
            \                    /
              Coordinate ←→ Compel
            /                    \
    🟠 Min returns          🔴 95% availability
       Reduce waste            One-stop shop
```

## 📚 Exam Essentials
**Concepts**: 
- Newsvendor with censored demand
- Service level: u/(u+o) where u=underage, o=overage
- Lead time uncertainty (DDLT as random variable)

**EOQ Components**:
- D: Demand rate
- F: Fixed order cost ($500)
- H: Holding cost ($0.45)
- C: Unit cost ($45)

**Strategy**: Pool similar products for better demand estimates

**Traps**: 
❌"Optimize each SKU separately" 
✅"Pool data across similar items"

## 🎓 Recitation Points
- ⭐️"Updating Q frequently makes system fragile"
- "5-day lead time adds complexity"
- "Balance stockout cost vs holding cost"

---
*Previous: [Zara Continued](7👗_Zara_Continued.md) | Next: [Risk Pooling](9🏊‍♀️🚚_Pool_Walmart_Amazon.md)*