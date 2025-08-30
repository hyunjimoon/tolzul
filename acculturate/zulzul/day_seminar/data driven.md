![[data driven 2025-05-29-10.svg]]
%%[[data driven 2025-05-29-10|🖋 Edit in Excalidraw]]%%
different knowledge

ai vs human

ai: min total distrance/time (system)
human: min late rate (individual)

findings: rookie drives follow ai rec (sm, experimence drives autonomous routing (low late rate)

| **Driver Type**       | **Routing Behavior**         | **Route Difference**                                   | **Late Rate**         |
|-----------------------|------------------------------|--------------------------------------------------------|------------------------|
| Rookie Drivers        | Follow AI recommendation     | Small difference between actual and recommended routes | High late rate         |
| Experienced Drivers   | Use autonomous routing       | Large difference between actual and recommended routes | Low late rate          |

[[jinhua_zhao]]'s question: rookie dropped and whether experienced dropped enough?

### 🧠 **Problem Definition**

Platforms (e.g., delivery/logistics) aim to minimize **system-wide cost** (e.g., total distance or time), for which AI routing is optimal. However, **human drivers**, especially experienced ones, optimize for **individual performance** (e.g., minimizing late deliveries), often deviating from AI routes.

This creates a tension:

- Should platforms **enforce** AI-optimal routing and risk noncompliance or mistrust?
    
- Or should they **adapt** AI recommendations to be more interpretable/trustworthy to humans—even if suboptimal from a system view—to gain better compliance?
    
### 🧩 **Comparison Table: Platform Solutions to Align Human Behavior**

|**Solution**|**Mechanism**|**Target Group**|**Pros**|**Cons**|
|---|---|---|---|---|
|1. **Force human to follow AI (optimize system)**|Make AI recommendations strict / default / enforced|Rookie drivers|Fast convergence to system-optimal path; easy to implement|Trust issues; performance gap remains with experienced drivers|
|2. **Adapt AI to be closer to human routes**|Calibrate AI recommendations to mimic experienced routes|Experienced drivers|Increases trust; leads to better compliance and eventual convergence|Slower convergence to system optimum; may encode suboptimal heuristics|

> "Suggest a route closer to human... humans have more trust... and will move this way — which is actually better for the platform."

This suggests a **strategic hybrid**: in early driver stages (rookies), enforce AI learning; in later stages (experienced), adapt AI to be interpretable and trust-enhancing — **aligning incentives over time**.

---
- compliance rate decline from aggressiveness

⭐️Related to Jinhua’s q "do human value the fact that they are in control?"
“Do scientists pay to be scientist” Is the paper I’m aware of that measures monetary value on “freedom of (job) choice”

https://pubsonline.informs.org/doi/10.1287/mnsc.1040.0241

- platform operations and we also have individual human behavior. What's the difference between the platform operation and human behavior.
- rooting is the means, right? I mean, it helps, maybe the new drivers to follow a path, but also is what the platform uses, I would think, to establish the expected delivery time or arrival time. Oh, yeah. And that is probably the most important driver force for the driver. So when you change the parameters in the algorithm, 

⭐️I think tradeoff is happening on the investment on data collection (unit:\$) VS improved decision from added data (unit:\$)e.g. from ICU setting,  it costs me $10 dollar to install new sensor (increase precision) but it’d have $100 benefit from optimizing the time to measure

- learning by climbing 

[What large language models know and what people think they know](https://www.nature.com/articles/s42256-024-00976-7)

automation, not augmentation task

zoom chat saving : ![[haiwang seminar 1.txt]]