## Tactical planning model for automotive manufacturing: how stochasticity flows from time parameter estimation to lot size prescription to lead time planning

keyword: planning inbound shipments, planned lead time, stochasticity in manufacturing system, lean manufacturing

This project would be a mix of critical literature review and research project. I am sure this will be a good preparation for Tesla project aiming to design and validate their automated electric vehicle factory with a high  5 seconds takt time.

Narrative of three causal loops is effective in proposing process improvemnet system-dynamically. The story starts with an incumbent balancing loop that is limiting the growth of a system. Then reinforcement mechanism is introduced which defies this limit, often though increased capability or design of complimentary market. We end our story with how the exponential growth from our proposal, reinforcement loop, would eventually be curbed by the next balancing loop to emerge.

1. incumbent trade-off (balancing loop)
- One key trade-off for planning Tesla inbound shipment is ideal lot size for each input, or equivalently the time between replenishment. The larger the lot size, the longer the time between replenishment and possibly greater savings in transportation and handling. However, inventory will be larger, as will the need for space, and flow will be more variable due to lumpiness.
- I think pushing the model boundary e.g. extending time horizon to include in-factory rework or refurbish, may have great effect on optimal lot size. My assumption is this would lower the optimal lot size. Two causal mechanisms are explained in 2.
 
2. reinforcing loop
- From diagram below where lower inventory e.g. from smaller lot size makes problems more visible making fault-cause finding more responsive through corrective or preventive actions and thereby increasing system quality and controllability. Improved quality brings down a. system failure's mean, b. system failure's variance, c. setup time, d. setup cost. Decreased four components contribute to lower levels of inventory based on EOQ, newsvendor, queueing models.
![[../../../../../../ref/Pasted image 20230407235310.png]]

3. emerging balancing loop
- Even with the reinforcing loop above, lot size should be optimized, if not fixed, as an non-negative integer. This last step can start by understanding the counteracting force which keeps lot size from near-zero, no buffer, and adding this constraint to our MIP model.

- If time permits, I wish to further investigate how the lot-sizing connects with another trade-off: investment in work-in-progress inventory and capacity. Using linear control rule, Fine and Graves (1989) investigate this and give guidelines to set planned lead itmes, determine benifits of eliminating variability in the shop, understand how changes in production mix, volumne, or routing affect inventory and capacity requirements.

- If time permits, I can try using data from Fine and Graves (1989) to experiment my MIP model.  Revisiting their analysis on planned lead time and variability would be interesting with added formulation from 2 that incentives lean inventory.

Reference
- Fine, C. H., and S. C. Graves. 1989. “A Tactical Planning Model for Manufacturing Subcomponents of Mainframe Computers.” Journal of Manufacturing and Operations Management 2 (1): 4–34
- Graves, S. C. 1986. “A Tactical Planning Model for a Job Shop.”Operations Research 34 (4): 522–53
- Graves, S. C. 2011. “Uncertainty and Production Planning.” In Planning Production and Inventories in the Extended Enterprise, edited by Karl G. Kempf, Pınar Keskinocak, and Reha Uzsoy, 83–101. New York: Springe
- Graves, S.C., 2022. How to think about planned lead times. _International Journal of Production Research_, _60_(1), pp.231-241.
- Haeussler, S., S. Matthias, M. Schneckenreither, and A. Onay. 2021. “The Lead Time Updating Trap: Analyzing Human Behavior in Capacitated Supply Chains.” International Journal of Production Economics 234: 10803