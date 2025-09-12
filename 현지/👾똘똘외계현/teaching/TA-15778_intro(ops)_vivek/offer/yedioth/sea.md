### Final Grade & Feedback
Q1: 10/15 [Q1 result 394 is outside 5% range of 419]
Q2: 15/15
Q3: 15/15
Q4: 10/15 [No quantitative example provided]
Q5: 10/10
Bonus: 0/10 [Only censoring mentioned, no distribution assumption]
**Total: 60/80**

Team Seals: Yuki Matsumoto, Colin McGonigle, Nyari Nain, Pavel Tkachyk, Sophia Yang
OPS MGMT: Section A
Question 1: Independent Retailer Optimization
A good method would be the newsvendor model as it determines optimal order quantities
under demand uncertainties. For each retailer i, mean demand μᵢ and standard deviation σᵢ,
for achieving a 99% service level,
Qᵢ = μᵢ + Kσᵢ, where K= 2.32 for a 99th percentile of the standard normal distribution.
Results Analysis
Applying this formula across 50 retailers yields total weekly production of 🚨394 magazines🚨
against expected demand of 205 magazines. Safety stock requirements total 190
magazines, representing 48% of production volume. This creates substantial operational
inefficiency where nearly two magazines are produced for every one sold.
The independent model achieves 99% service level performance but generates substantial
return volume. Weekly returns of 190 magazines create reverse logistics costs including
collection labor, transportation expenses, and disposal fees. At $3 total cost per returned
magazine, weekly waste reaches $568 or $29,536 annually.
Question 2: Full Pooling Analysis
Full pooling aggregates demand across all retailers, leveraging the principle that individual
demand variations offset each other. Aggregate mean demand remains 205 magazines, but
pooled standard deviation equals √(Σσᵢ²) = 12 magazines.
Performance Results
Pooled order quantity equals 205 + 2.33(12) = 🚨233 magazines🚨 weekly. This represents a
41% reduction from independent ordering. Safety stock drops from 190 to 28 magazines, an
85% improvement. Expected returns fall to 28 magazines, reducing the return rate from
48% to 12%. This is a significant improvement not only internally, but also relative to the
industry norm of approximately 25% returns, as noted by Yedioth’s CEO.
Economic benefits include $322 weekly production cost savings and $161 return handling
cost reduction. Total benefit of $483 weekly equals $25,116 annually. Full pooling
represents theoretical maximum efficiency while maintaining service level performance.

Implementation requires real-time inventory visibility, instant redistribution capability, and
sophisticated coordination systems that exceed current organizational capabilities.
Question 3: Sales Agent Pooling
Sales agent pooling creates 10 inventory pools corresponding to existing agent territories.
Each agent manages approximately 5 retailers, enabling demand aggregation within
established organizational boundaries.
Quantitative Results
Agent-level pooling reduces total weekly production to 🚨292.60 magazines🚨, a 26%
improvement over independent ordering. Expected returns drop to 87.98 magazines,
representing 54% reduction from current levels. This approach captures 74% of full
pooling's production benefits while requiring minimal organizational restructuring.
Individual agent requirements range from 21 magazines (Agent 7) to 43 magazines (Agent
5), reflecting territory-specific demand patterns. The pooling effect reduces safety stock
requirements within each territory while maintaining agent autonomy and retailer
relationships.
Sales agent pooling offers practical implementation advantages. Existing organizational
structures remain intact while mathematical benefits emerge through natural demand
aggregation. Technology requirements remain minimal since agents already coordinate
inventory within their territories.
Question 4: Mid-Week Strategy Options
Rebalancing Strategy
Mid-week rebalancing utilizes existing Wednesday sales agent visits to 🚨redistribute
inventory🚨 within routes. Agents assess stock levels and transfer magazines from slowselling to fast-selling locations, creating virtual pooling for remaining demand uncertainty.
However, due to the highly automated nature of printing operations, Yedioth is currently
constrained to a single weekly production batch, with shipment quantities determined well in
advance by the research department.
This approach requires minimal technology investment beyond basic inventory tracking.
Expected benefits reach 60-70% of agent pooling performance through operational process
improvement. Implementation builds on existing agent relationships and route structures.
Given that most retailers are small shops lacking IT infrastructure, inventory redistribution
decisions would rely primarily on the judgment of sales agents during their store visits.

Dynamic Replenishment Strategy
Dynamic replenishment reduces initial Sunday allocations to conservative levels, then
delivers additional inventory Thursday based on Wednesday demand observations. This
two-stage approach aligns production more closely with real-time demand patterns.
Implementation requires communication systems for replenishment requests and additional
delivery capacity. The strategy can approach full pooling performance by converting fixed
allocation into responsive supply based on early demand signals.
Hybrid Strategy
Optimal implementation combines reduced initial allocation (90% of historical average), midweek rebalancing within routes, and selective replenishment for high-velocity locations. This
hybrid approach can achieve 25-30% production reduction while maintaining 99% service
levels and reducing returns by 50-60%. Technology requirements remain moderate through
incremental enhancement of current systems.
A phased implementation—starting with agent-led manual rebalancing in selected
territories—can offer a low-risk path toward broader adoption.
Question 5: Implementation Challenges for Assaf to address
Compensation Misalignment leading to agent distress
Sales agents earn volume-based commissions, creating resistance to allocation reductions.
Current 🚨incentive structure makes efficiency improvements appear as income threats🚨.
Resolution requires compensation redesign incorporating efficiency metrics alongside
volume measures.
Recommended changes include sell-through rates and return minimization in performance
evaluation. Transition periods need income protection guarantees to enable pilot
participation and reduce change resistance.
Technology Infrastructure challenges
Current systems lack real-time inventory visibility. Most retailers use paper-based tracking,
limiting coordination capability. Technology requirements vary across implementation
strategies, from basic mobile applications for rebalancing to sophisticated coordination
systems for dynamic replenishment.
Investment should proceed incrementally, proving operational benefits before advancing to
complex technological solutions. Initial implementations can succeed with minimal
technology through process improvement rather than system transformation.

Organizational Culture
Yedioth’s long seated inertia in operating in a certain way with family-based values —where
printing, distribution, and sales operate with limited cross-functional planning—pose a major
barrier. As described in the case, efforts to align departments often require independent
persuasion, illustrating the lack of integrated strategic planning.
Established culture emphasizes quantity over efficiency. Decades of over-supply have
normalized high return rates among agents and retailers. Allocation reductions challenge
fundamental assumptions about market coverage and customer service reliability.
This cultural bias is further reinforced by the business model, where print ad revenues
depend heavily on circulation. As a result, stakeholders equate stockouts with lost ad
impressions, making under-allocation politically risky.
Research and Development concerns
Research Department at Yedioth centers on individual retailer forecasting rather than
optimization mathematics. This will pose challenges around executing risk pooling and in
general acceptance of real-time decision and demand management. Old staff and sales
agents working styles may be a hindrance to acceptance of these new skills and
methodologies as well.
Some Strategic Recommendations for Assaf
Primary Strategy: Implement sales agent pooling with mid-week rebalancing as the core
optimization approach.
Implementation Approach: Begin with pilot involving 2-3 willing sales agents covering 1015 retailers. Successful pilot results provide proof points for broader organizational adoption
while identifying implementation challenges.
Compensation Redesign: Modify agent compensation to include efficiency metrics
accounting for 25-30% of performance evaluation and volume incentives.
Technology Investment: Start with basic mobile tracking applications enabling inventory
visibility and rebalancing coordination. Advance to sophisticated systems only after proving
operational benefits through initial implementations.
Capability Building: Training staff and agents in such a way that it would align with their
goals and help them position better in the industry. Setting clear expectations and
awareness of company’s broader goals helps even out employee turnover or resistances in
general.

Appendix:
Note: we did not exclude sell-through data because the 🚨experimental design explicitly
addressed censored demand concerns🚨 through daily sales agent visits that captured
"uncensored demand" and the “exact in-week demand information.”This aligns with the
experimental setting described by Asaf Avrami, in which agents regularly monitored store
activity, making demand censoring minimal.Since fractional magazines cannot be sold, all
computed order quantities are rounded up to the nearest integer to ensure feasibility.
Reference for Question 1 & 2
Question 2: Pooling
Independent Total Production
Expected demand (𝜇)
Safety Stock
Total

205
189
393

Pooled Total Production
Expected demand (𝜇)
Safety Stock
Total

205
28
233

Returns
Returns - Independent
Returns - Pooled
Total

189
28
160

Note for Question 3
Grouping five retailers per sales agent is supported by multiple considerations. First, the
case experiment was designed with ten agents managing five stores each, providing a
natural unit of analysis. Second, these stores are likely to share geographic and behavioral
similarities. Third, this approach aligns with the existing operational routines of the sales
team."

