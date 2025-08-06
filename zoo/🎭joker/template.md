# 🎭 Joker Model Template

## 📋 File Metadata
```yaml
---
# Joker Model Metrics
deliverability: [1-10]    # 실행 가능성 점수
sellability: [1-10]       # 판매 가능성 점수
value_per_time: [$/hr]    # 시간당 가치
chain: [capability/user/fulfillment]
status: [explore/exploit]
---
```

## 🎯 Evaluation Questions

### Deliverability Check (🟢 Capability × 🔴 Fulfillment)
- [ ] Do we have the technical capability?
- [ ] Can we produce it consistently?
- [ ] Is the supply chain reliable?
- [ ] Can we scale if needed?

### Sellability Check (🟣 User × 🔴 Fulfillment)  
- [ ] Does it solve a real user problem?
- [ ] Is the value proposition clear?
- [ ] Can we reach the target users?
- [ ] Will users pay the price?

## 📊 Balance Score
```
Success Probability = Deliverability × Sellability / 100
```

## 🔄 Action Items
1. If low deliverability → Move to 🐢can/📐method/
2. If low sellability → Move to 👾user/🧍‍♀️case/
3. If balanced → Move to 🐙offer/🗺️project/
4. If proven → Move to respective 🟢🟣🔴 folders

---
*Remember: "Marketing sells the promise, Operations delivers it"*
