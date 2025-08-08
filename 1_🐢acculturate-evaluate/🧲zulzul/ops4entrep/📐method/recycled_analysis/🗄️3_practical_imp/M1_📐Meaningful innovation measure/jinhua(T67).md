# T67
from hyunjimoon on 2024-10-10T16:39:02Z

todo:
- add multithread of each particle
- finalize optimization formulation to argue under original formulation, one could never adopt AV

migrating from #161, closer to operations to prove prob.prog competence

first starting from airport performance (sailer's innovation odyssey). this will synthesize CIVA #249 with existing formulations of airport problems in below
[koo20_airport_gate_assignment.pdf](https://github.com/user-attachments/files/17331495/koo20_airport_gate_assignment.pdf)
[kim_incheon airport.pdf](https://github.com/user-attachments/files/17331497/kim_incheon.airport.pdf)


---

## Reply from hyunjimoon on 2024-10-10T16:52:15Z

using #249 's SAFE comparison interface

| Aspect | Flight A | Flight B | Flight C |
|--------|----------|----------|----------|
| Type | Long-haul | Short-haul | Long-haul |
| Purpose | Passenger | Passenger | Cargo |
| Special Consideration | Many transfer passengers | Crew nearing duty time limits | Critical medical supplies |
| Scheduled Departure | In 45 minutes | In 30 minutes | In 50 minutes |
| Priority Factor | Transfer passengers | Crew time constraints | Medical urgency |
| Flight Duration | Long | Short | Long |
| Cargo Type | Regular passenger luggage | Regular passenger luggage | Critical medical supplies |
| Potential Impact of Delay | Missed connections for passengers | Potential crew overtime or flight cancellation | Delayed delivery of critical medical supplies |


---

### Reply from hyunjimoon on 2024-10-25T20:02:41Z

[dashborad](https://claude.site/artifacts/b3c2a529-bd14-4f2c-a5c2-5dc21deab1b7) using [improving changi airpot operations cld](https://claude.ai/chat/22f4408a-26a0-4532-81f4-31c08a67284a)

<img width="615" alt="image" src="https://github.com/user-attachments/assets/6bb09ded-c858-4a6b-a9ce-ed24d2f2cb6a">

| Entities | Attributes | Operations | Events | Constraints | Probabilistic Elements |
|----------|------------|------------|---------|-------------|----------------------|
| Flight, Crew, Passenger, Gate, Aircraft | Departure Time, Flight Type (Long-haul/Short-haul), Purpose (Passenger/Cargo), Transfer Passenger Count, Crew Time Remaining, Medical Urgency | Prioritize Flights, Assign Gates, Manage Crew Schedules, Handle Passenger Connections | Flight Arrival, Flight Departure, Delay Occurrence, Medical Emergency | Gate Availability, Crew Duty Time Limits, Minimum Connection Times, Aircraft Turnaround Times | Weather-related Delays, Unscheduled Maintenance, Air Traffic Control Restrictions, Passenger Boarding Times |


---

### Reply from hyunjimoon on 2025-02-13T10:59:09Z

building on this, i made This interactive visualization demonstrates the decision boundary between modular and integrated learning strategies for entrepreneurial testing, displayed in a 3D space defined by market potential (μ_ϕ), market certainty (1/σ_ϕ), and implementation capability (μ_θ). The key insight revealed is that startups with lower values across these parameters (shown in green) typically benefit from modular learning - testing the market first before committing to implementation. As these parameters increase and especially when there's higher correlation (ρ) between market potential and implementation capability, the decision boundary shifts to favor integrated learning (shown in blue), suggesting that testing market and implementation together becomes more valuable. The interactive ρ slider allows entrepreneurs to explore how the strength of this correlation affects their optimal testing strategy, providing a practical tool for strategic decision-making in early-stage venture development.
<img width="300" alt="image" src="https://github.com/user-attachments/assets/d8cf2253-5df8-4ba8-815d-fd471023ec3f" />

using [Adapting Airport Allocation Visualization to Entrepreneurial Framework cld](https://claude.ai/chat/5956d7ee-592c-4f91-a886-4663516c2963)

---

## Reply from hyunjimoon on 2024-10-13T03:08:31Z

using [autogp](https://github.com/probsys/AutoGP.jl), [Advancing ChiExpert's Probabilistic Programming for Data Science cld ](https://claude.ai/chat/973885da-d256-46cc-a01f-4c04115ac191), [gist code](https://gist.github.com/hyunjimoon/491d87f3da33f5415ec02b7ea7774c30) with `ops_innov_samp_opt.jl` controlling the use of `samp_var` and `opt_sch_alloc`.  `samp_var` first estimates variability of each subtask when adopting AV_baggage and `opt_sch_alloc` optimizes given the estimated effect of adopting innovation online.

![auto_pred](https://github.com/user-attachments/assets/71001b99-a28c-4f44-aa4c-417c1ae769aa)

size_of_plane | number_of_passengers | weather | distance_to_travel | servicing_time_aircraft_arrival_parking | servicing_time_baggage_unloading | servicing_time_passenger_crew_disembarkation | servicing_time_aircraft_interior_cleaning | servicing_time_fueling | servicing_time_catering | servicing_time_lavatory_services | servicing_time_passenger_crew_boarding | servicing_time_baggage_uploading_first_batch | servicing_time_baggage_uploading_second_batch | servicing_time_baggage_uploading_loose_luggage | servicing_time_connect_tug | servicing_time_final_ramp | servicing_time_push_back | servicing_time_gate_close | departure_urgency | passenger_connections | crew_duty_limits
-- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | --
small | 73 | clear | 13002 | 14.7234321 | 11.0794615 | 17.3740904 | 29.4206184 | 67.4125118 | 37.2851701 | 13.698317 | 30.7277828 | 17.8776168 | 16.3956617 | 14.3600475 | 8.29635909 | 12.3343297 | 12.7976293 | 6.01185514 | 0.06328094 | 77 | 0.09073149 |  
medium | 320 | clear | 11140 | 7.92457319 | 14.0362445 | 15.4837668 | 21.9544612 | 78.9739716 | 32.1940815 | 13.7693444 | 28.7402693 | 18.5003868 | 10.4710035 | 12.2867553 | 7.24458883 | 7.18032014 | 9.21123354 | 11.0436605 | 0.52353481 | 29 | 0.78121967 |  
medium | 134 | stormy | 14529 | 6.40743854 | 11.8772588 | 19.1385668 | 20.7365195 | 78.3571782 | 36.3891498 | 10.8560653 | 32.5345277 | 23.569235 | 15.5402212 | 7.69580446 | 10.4067701 | 10.7340378 | 10.294141 | 5.40462777 | 0.67392858 | 16 | 0.15400962 |  
large | 253 | clear | 10007 | 6.88586482 | 11.9428627 | 16.224446 | 22.0218331 | 66.6867407 | 30.6611875 | 10.8970219 | 26.7896668 | 22.9797549 | 17.8940791 | 14.1049319 | 8.84757035 | 10.9695892 | 13.5192748 | 5.43743246 | 0.71108259 | 0 | 0.26492808 |  

...


---

### Reply from hyunjimoon on 2024-10-13T15:08:30Z

using [auto_bagg_handling perp](https://www.perplexity.ai/search/can-you-search-for-an-optimiza-IYVi7L_7TaWy6xBXHIUVfA)

incorporating autonomous baggage vehicles:

"Create an optimization model for airport resource allocation that incorporates the adoption of autonomous baggage vehicles. The model should:

1. Define key decision variables related to autonomous vehicle deployment, traditional vehicle usage, and human labor allocation.

2. Specify an objective function that minimizes total operational costs while maximizing efficiency.

3. Include constraints on:

   - Total number of bags that must be processed

   - Available autonomous and traditional vehicles

   - Labor hours and shift restrictions

   - Charging/refueling requirements for vehicles

   - Safety protocols and regulatory compliance

4. Account for variability in:

   - Flight schedules and passenger loads

   - Vehicle performance and reliability

   - Integration challenges during the adoption phase

5. Incorporate parameters for:

   - Costs of autonomous vehicles vs. traditional equipment

   - Labor costs for different roles

   - Energy/fuel costs

   - Maintenance requirements

6. Consider both short-term optimization (daily operations) and long-term planning (fleet composition over time).

7. Suggest methods to handle uncertainty in the model, such as stochastic programming or robust optimization techniques.

8. Propose key performance indicators to evaluate the effectiveness of the optimized solution.

Provide a mathematical formulation of this model and explain how it could be solved and implemented in practice."

Citations:

[1] https://www.airport-technology.com/contractors/groundequipment/tcr-international/pressreleases/autonomous-baggage-handler-tested/

[2] https://www.changiairport.com/corporate/media-centre/changijourneys/the-airport-never-sleeps/autonomous_tractor.html

[3] https://aurrigo.com/aurrigo-to-introduce-four-new-autonomous-baggage-handling-vehicles-at-changi-airport/

[4] https://www.passengerterminaltoday.com/news/technology/cincinnati-northern-kentucky-airport-deploys-autonomous-baggage-handling-vehicle.html

[5] https://www.internationalairportreview.com/news/195996/testing-of-autonomous-baggage-handling-technology-continues-at-cvg-airport/

[6] https://www.autonomousvehicleinternational.com/news/testing/aurrigo-conducts-autonomous-baggage-and-cargo-tractor-trial-at-stuttgart-airport-2.html

[7] https://www.airport-technology.com/features/how-new-technology-is-improving-baggage-handling-performance/

[8] https://www.futuretravelexperience.com/2024/04/avinors-high-level-strategy-for-future-baggage-handling-infrastructure-focused-on-robotics-autonomous-vehicles-and-smart-systems-using-ai/

---

## Reply from hyunjimoon on 2024-10-16T15:45:10Z

charlie mentioned synergy marine group in 
[charlie_ai_om_strat.txt](https://github.com/user-attachments/files/17398534/charlie_ai_om_strat.txt) [otter](https://otter.ai/u/UymbNQfoLYnKgUECJwULCNGpIbo?utm_source=copy_url)

Capt. Anurag Gupta seemed [to be at mendaki workshop](https://otter.ai/u/Prc5vLgaW8aR2yeCKpp_FbCrK6g?q=synergy%20marine&i=1&view=transcript&tab=chat) and  introduced their group is evaluating or thinking about how AI can improve ownership operation (didn't hear the rest)

---

## Reply from hyunjimoon on 2024-10-22T20:28:34Z

## angie reflection (summary below)
### 1. Re-identified Tom and Abdullah's research alignment, which was one motivation for taking Abdullah's class
[Tom and Abdullah's paper When Are Combinations of Humans and AI Useful?](https://arxiv.org/abs/2405.06087) accepted in nature was introduced. 

I gave three comments:
1. I’m sure T6 would already know but https://gilbrethnetwork.tripod.com/therbligs.html therblig notation from early 1980 classified and optimized physical task operations
2. What is the format of data input from CAG and synergy-marine? Do they give database? I expect some difficulty from language matching (column names) and wonder what your plans are
3. Perhaps of interest from https://arxiv.org/abs/2408.03943 that compares machine as tool vs thought partner and I think it is important to have a communicable symbolic representation of world model of both human and machine so that assumptions can be checked.
For 1, Robert Laubacher and Jie Gao both verified therblig would be "very useful". let alone usefulness and history of therblig (industrial engineering sci.mng 101), i hypothesize starting sentence with "I'm sure you'd know" creates some fear, increasing learning efficiency

### 2. Charlie's observation on T67 connection - dynamic
> There are useful connections between T7 and T6 Changi issues.  T6 needs to understand dynamics of airplane assignments to gates based on servicing (food, baggage, fuel, etc) capacity and coordination.  Both T6 and T7 need to look at passenger needs. Both need to consider dynamic stochastic nature of scheduling and rescheduling.

I generally agree. One improvement may be, instead of stochastic nature, agent's need for reasoning probabilistically is more useful. But as "nature" is not an agent we can control, I decided to train myself to translate every observation (what's happening) into the language of agent (airport institution, staff, airline, passenger)'s reaction (what agents do in response to new observation given its world model). Moreover, I believe stochasticity is subsumed by dynamics given all agents have the same model of the world. It's lack of agent's modeling resource that abstracts unknown/outside-model as stochasticity (detail in [process vs feature noise in SD](https://amoon.world/%F0%9F%8C%99amoon()/%E2%9A%A1%EF%B8%8Fgenerate(tolzul)/management/1%F0%9F%94%B4BayesSD/5%F0%9F%8C%80workflow/Comp(Prob(Mng(Sys)))/Stat(Mng)/Process+noise+and+Feature+noise)).

Moving forward, how can "useful connection" between task analysis in T6 and resource allocation algorithm in T7 be designed? I view the former as the computation/theory level that defines the `system components` and `goal` of our intervention. Once this mental model on `system component` and `goal` are aligned among different stakeholders, different (probabilistic inference / optimization) algorithms can be assembled to implement the update of `system component` in the direction of given `goal`. 

### 3. CAG's AV adoption process
Discussed AV implementation with CAG: Angie reached out to her friend from CAG (Yanling Liu) for a quick question on how autonomous vehicle adoption affects baggage handling operations. Key points:

**Initial Exchange**:
- You inquired about CAG's AV implementation in baggage handling
- Yanling shared that AVs are in early adoption (pre-scale), mimicking human drivers, with impact not yet measurable. "The very simplistic thing now is to say the AV mimics the human driven vehicle so it assumes they will deliver the bags in line with our current planning norm"

**Context & Proposal**:
- You shared your thesis work and T7's current operations research
- Connected this to Hyundai EV project experience
- Proposed leveraging T6 (human-AI collaboration) insights for T7 (airport operations)
- Asked "Would CAG be interested in exploring how human-machine collaboration framework (how AVs integrate into existing operations - not just mimicking human drivers, but potentially identifying new optimization opportunities in baggage handling processes)can help measure and optimize AV integration as you scale AV adoption?"
- This connects to Charlie's observation about T6/T7 synergies, particularly regarding baggage handling capacity and coordination in airport operations (human-machine collaboration)

- takeaway: evaluation is what matters eventually

----
## [less subjective summary](https://otter.ai/u/5kQn7SakuQWizeQ2N9qOrJhquNQ?utm_source=copy_url) 

T6 Updates (Human-AI collaboration):

Paper "When Are Combinations of Humans and AI Useful?" accepted in Nature Human Behavior
Working on taxonomy of human-AI interaction modes and online platform for ontology content
Collaborating with Changi and Synergy Marine for data collection

T7 Updates (Airport Operations):
![image](https://github.com/user-attachments/assets/238764a2-5756-4b20-b5fb-c298c472650b)

Modeling passenger activity and gate assignments
Developed static assignment algorithm with multiple objectives:

Passenger-oriented: minimize walking distance, optimize transfer times
Airport/airline-oriented: minimize tow operations, satisfy gate preferences

Built visualization tool showing flight connectivity, arrival/departure patterns, and gate utilization

[meeting_saved_chat.txt](https://github.com/user-attachments/files/17508991/meeting_saved_chat.txt)


---

## Reply from hyunjimoon on 2024-11-01T19:08:39Z

based on [chat with Jie (T6 member)](https://otter.ai/u/1NV1VZxLqI51QBrEgT9zCJXE0Ws?utm_source=copy_url), I updated my belief and desire with the following steps. using [Modeling Angie's Evolving Beliefs and Desires in T67 Environment cld](https://claude.ai/chat/49ef64ae-1d28-4d8a-bc17-6032aafd15f0) 

I'll note synergy marine as SM, changi as CAG.

Here's the updated explanation that matches the detail level of your enhanced table:

Based on the chat with Jie (T6 member), I updated my belief and desire with the following steps:

1) 🫀🧠 Desire & Belief: Entered with desire to program operations and innovation management solutions. Initial beliefs modeled different ROIs: cost-saving potential (p_c ~ Beta(2,2)) for investing in dashboard development, and revenue-growth potential (p_r ~ Beta(1,2)) for investing in market expansion through Charlie's T6 connection. Despite personal preference against long SG stays, remained positive about M3S market based on team alignment (Tom-Abdullah-Angie correlation).

2) 👁️ Observation: Collected multiple signals from both dimensions:
   - Cost-saving (2/2 positive): Lower data acquisition cost for SM vs CAG (C1); T6's established process mapping and bottleneck identification aligns with my approach (C2)
   - Revenue-growth (4/4 positive): SM's aggressive fleet expansion plan (R1); procurement solution's replicability beyond SM (R2); Jie's positive response to CAG dashboard's applicability to SM (R3); SM's openness to parallel procurement experimentation (R4)

3) 🧠🔄 Reasoning: Updated beliefs proportional to signal intensity:
   - Cost ROI posterior strengthened: p_c|d_c ~ Beta(2+2,2)
   - Revenue ROI posterior strengthened more: p_r|d_r ~ Beta(1+4,2)
   - Both updates reflected successful observations (all binary signals = 1)

4) 📍 Planning: Optimization shifted from cost-saving (🟩) to revenue-growth (💜) focus as posterior ratio comparison suggested higher ROI (4/6 < 5/7). Action choice maximizes utility increase (Δu) per unit investment, incorporating both updated ROI beliefs and available actions in cost-saving (a_c) and revenue-growth (a_r) dimensions.

| Section                 | Language                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Math                                                                                                                                                                                                                                                                                          | Symbol                                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 1. 🫀🧠 Desire & Belief | Desire: Program ops & innovation mgmt<br><br>Belief: <br>• T67 is interesting for both market/collaboration<br>• Tom-Abdullah-Angie interests correlated<br>• SG/M3S promising (despite location preference)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | <br><br><br>$p_c\sim Beta(2,2)$<br>$p_c$: cost-saving ROI (saved cost if investing in cost-saving action e.g. develop dashboard further)<br><br>$p_r\sim Beta(1,2)$<br>$p_r$: revenue-growth  ROI (gained revenue if investing in revenue gaining action e.g. sync charlie on new info on T6) | <br><br><br><br><br>🟩🔴~Beta(1,1)<br><br>🔴💜~Beta(1,2)<br>                                                               |
| 2. 👁️ Observation      | Cost signals:<br>`C1`: Jie shared data acquisition cost is lower for SM (vs CAG) and angie needs data to validate her desire's product.<br><br>`C1`: T6's procurement process  map (Jie's poster) and its  bottleneck identifying approach is aligned with Angie's desire<br><br>Revenue signals:<br>`R1`: SM plans to increase ships (600→1000) in three years<br><br>`R2`:Jie emphasized developed procurement AI-human collaboration is highly replicable outside SM<br><br>`R3`:Jie liked Angie's dynamic prioritization dashboard (developed for CAG) and verified its applicability for SM <br><br>`R4`:Jie liked Angie's idea on proceeding parallel procurement contract and confirmed SM would be open to this experimentation | <br>$d_c=$ 2 out of 2<br>$d_c$: observation on cost ROI (1 if positive, else 0)<br><br><br><br><br><br><br><br>$d_r=$ 4 out of 4<br>$d_r$: observation on revenue ROI (1 if positive, else 0)                                                                                                 | <br><br>👁️🟩🔴_1 = 1<br>👁️🟩🔴_2 = 1<br><br><br><br>👁️🔴💜_1 = 1<br>👁️🔴💜_2 = 1<br>👁️🔴💜_3 = 1<br>👁️🔴💜_4 = 1<br> |
| 3. 🧠🔄 Reasoning       | Belief on cost & revenue ROI updated propositional to intensity of cost and revenue side signal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | $p_c \| d_c \sim Beta(2+2,2)$<br>$p_r\|d_r \sim Beta(1+4,2)$<br><br>$p_c \| d_c , p_r \| d_r$: posterior on cost,  revenue ROI                                                                                                                                                                | 🟩🔴\|👁️~Beta(4,1)<br>🔴💜\|👁️~Beta(4,2)<br>                                                                             |
| 4. 📍Planning           | Action chosen based on <br> - cost, revenue ROI posterior<br>- utility function<br>- action set (new options appear)<br>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | $a_c$ = $\underset{a \in a_c, a_r} {argmax} \; \Delta u(p_c \|d_c, p_r\|d_r, a)= p_c \|d_c * a_c + p_r\|d_r * a_r$<br><br>$\Delta u$: utility increase per unit investment<br>$p_c, p_r$: cost, revenue ROI posterior<br>$a_c$: cost-saving action <br>$a_r$: revenue-growth action           | 📍changed from 🟩 to 💜<br> <br>as $\frac{2}{4}>\frac{1}{3} \rightarrow$   <br><br>$\frac{4}{6} < \frac{5}{7}$             |

---

[Discussion link](https://github.com/Data4DM/BayesSD/discussions/264)