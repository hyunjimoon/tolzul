# Lecture 2: Capacity Analysis 1 - Predictable Variability (JetBlue)

**Date:** July 22  
**Duration:** 1.5 hours  
**Instructor:** Prof. Vivek Farias
![[2♻️analyze(🔴capacity-variability, ✈️airline) 2025-07-21-9.svg]]
%%[[2♻️analyze(🔴capacity-variability, ✈️airline) 2025-07-21-9.md|🖋 Edit in Excalidraw]]%%
product managment cirriculum, 

[[2025-07-21|25-07-21-08]]

should have been more 
- theme of better to be lucky rather than to be smart
- quantative hedge fund, 
- consulting (fixed income portion of the fund) - consider academia, two years at mit (vacation of mit continues), 
- mens et manus (be able to build and do things)
- nike's second largest compny (celect), seer bio (ai protein;), cimulate (customer gpt)
- lp in different firms, care about deep intellectual idea -> but need to do things. ETHOS

---

steve blank, epiphany (crm company - mid 90s), 

agricultural startup 

1. **Give funding and connections**: "Brilliant idea, you know, here's 50k right? And I'm going to write emails introducing you to a bunch of folks."
2. **Pass/refer to others**: "You know what, not for me, but here's somebody else at, you know, thinks about agriculture and so on and so forth. Maybe, maybe they're interested."
3.  **Ask them to reconsider and return**: "Well, you know, have you thought of x, right? And go, think of x, and then come back."

survey is bullshit response (overly rosy). framer doesn't ;

what do you want to do with cash? 50k, (doing one industry is difficult)

go build bunch of drones 
right season with the farmer (modular camera) ; how do we minize effort but maximize learning

which problem are they solving?? prove low yeld 

time unit of cost, increase yield is data; root cause analysis (soil, ) - 

⭐️PROBLEM STATEMENT giving farmer data that improves yield

collect all data manually and give it to farmer whether they can use it?

manage products
🙋‍♀️the data was the product, not drone (disagree)
1. define product - how are you adding value? (selling signals (advice) that improves yield), why should the farmer come to you (strategic value positioning). WHAT & WHY ME?
2. managing two bubbles - product (what's the problem and why should that come to you) and capabilities (my resources; financial organization, tech, supply chain, distribution)
3. 🔄capability and product 
	1. capability to product: unique product (novel for market place)
	2. product to capability (make that investment in that capability); capability for product (resource change)
	3. 
one check per card (multiple checks)

expressing added value consistent offering really fast VS 

how'd you be aware of this 

queue -> feeling, 

time, quality, flexibility, price

the way you experience time matters (mirrors behind the bartendar) 2,3,4 minutes it's ok


⭐️don't measure of time in units of time (but in utility; capability invested to lower time) -> should be mapped with dollars

market share, money based utility metric, no fast food options, i'm ok to be slower

shave off seven seconds, lower 3% for macdonalds, 

🙋‍♀️why seven second rules leads to heavy price for flexbility ?

being 30secs off (leaving money off the table) in the product they are putting together

1. 🔺triangle (inventory), 
2. 🟧square(process - stead chain, mate, table (too long, trash), assembly (condamets ketcup),  micro, counter  ), 
3. ↔️arrow (physical flows) 
4. ↕️dashed line (information flows)

macdonalds (human inventory manager)
slips (i don't want pickle), lindy

macdonald's local point is much earlier

mac don't have ♨️steam table (burger kingpull based )

macdonald is make to stock, burger is hybrid (up to steam table, it's make to stock, but then it's mto) 

burger king allows flexibility (whereas macdonalds makes cutomer stand aside for customized), 

how much capacity? - set up a 🧩puzzle for next time

🍾IDENTIFY BOTTLENECK. 8 burgers 480 burgers/hr , assembly (200 burgers per hr and 100 w) - capacity (200b/hr, 100w/hr VS peak demand (Friday lunch))

---
## Learning Objectives
- Understand capacity analysis techniques for predictable variability
- Apply queuing theory basics to operational bottlenecks
- Analyze the impact of capacity constraints on system performance
- Evaluate operational risk management strategies

## Case Studies
- **Primary Case:** [[Lec2_JetBlue_Airways__Deicing_at_Logan_Airport.pdf]]
- **Supporting Case:** [[Lec2_JetBlue_Airways__Valentines_Day_2007.pdf]] (SKIM)

## Required Readings
- **External Reading:** [NYTimes Article on JetBlue Valentine's Day Crisis](https://www.nytimes.com/2007/02/19/business/19jetblue.html) (SKIM)
  - **Access via MIT:** Navigate to MIT Factiva subscription for full access
  - **Key Points from Article:**
    - JetBlue faced massive operational meltdown during Valentine's Day 2007 ice storm
    - Poor communication and decision-making led to passengers being stranded on planes
    - Crisis damaged JetBlue's reputation and customer loyalty
    - Led to industry-wide discussions about passenger rights

## Key Concepts

### Capacity Analysis Framework
1. **Theoretical Capacity:** Maximum possible output under ideal conditions
2. **Effective Capacity:** Realistic capacity accounting for normal inefficiencies
3. **Actual Output:** Real-world performance including all disruptions

### Predictable Variability Types
- **Seasonal patterns** (winter weather, holiday travel)
- **Daily cycles** (rush hours, meal times)
- **Weekly patterns** (business vs. leisure travel)

### Bottleneck Analysis
- **Identification:** Finding the limiting resource
- **Impact Assessment:** Quantifying system-wide effects
- **Mitigation Strategies:** Capacity expansion vs. demand management

## Case Analysis Framework

### JetBlue's Value Proposition
- **Low-cost carrier** with premium service elements
- **Point-to-point network** (vs. hub-and-spoke)
- **Customer service focus:** "bringing humanity back to air travel"
- **Operational characteristics:** High aircraft utilization, lean operations

### De-icing Capacity Challenge at Logan
- **Weather-dependent bottleneck:** De-icing becomes critical constraint in winter
- **Shared resource:** Limited de-icing positions at Logan Airport
- **Predictable pattern:** Winter weather creates recurring capacity issues

### Operational Impact Analysis
- **Queue formation:** Aircraft waiting for de-icing services
- **Cascading delays:** Single bottleneck affects entire network
- **Cost implications:** Fuel costs, crew overtime, passenger compensation
- **Service degradation:** On-time performance, customer satisfaction

## Discussion Questions for Class

1. **Value Proposition:** What is JetBlue's value proposition and operational characteristics? How do these create vulnerabilities?

2. **Capacity Constraint Impact:** What is the operational impact of de-icing capacity limitations at Logan? How severe was the 2009-2010 winter problem?

3. **Theoretical Capacity:** Under ideal conditions, what is the maximum number of planes per hour that can be processed by four de-icing teams?

4. **Queuing Analysis:** How do weather delays create queues, and what are the implications for:
   - Passenger wait times
   - Aircraft utilization
   - Crew scheduling
   - Network connectivity

## Quantitative Analysis Tools

### Build-up Diagrams
- Map capacity requirements vs. available capacity over time
- Identify peak demand periods vs. capacity constraints
- Visualize capacity gaps and surpluses

### Basic Queuing Concepts
- **Arrival rate (λ):** Aircraft needing de-icing per hour
- **Service rate (μ):** De-icing capacity per hour
- **Utilization (ρ):** λ/μ ratio
- **Queue length:** Expected number waiting
- **Wait time:** Expected delay before service

## Risk Management Strategies

### Proactive Approaches
- **Capacity investment:** Additional de-icing equipment/positions
- **Demand management:** Schedule adjustments during peak periods
- **Alternative routing:** Diverting flights to less congested airports

### Reactive Approaches
- **Communication protocols:** Keeping passengers informed
- **Recovery planning:** Rebooking and compensation procedures
- **Crew management:** Avoiding duty time violations

## Key Takeaways
- **Strategic Message:** In a tightly coupled operational network, localized capacity constraints and disruptions can cascade into system-wide failure; proactive risk management and robust recovery plans are critical.

- **Capacity Planning:** Understanding predictable variability patterns enables better capacity decisions and contingency planning.

- **System Thinking:** Individual bottlenecks can paralyze entire operational networks, requiring holistic capacity management.

## Preparation for Next Class
- Review unpredictable variability concepts
- Prepare [[Lec3_The_Effects_of_Uber_s_Surge_Pricing__A_Case_Study.pdf]]
- Consider demand-supply matching challenges in two-sided markets

## Recitation Support
- **Date:** July 22, 4:00 PM - 5:30 PM (Cohort A) / 2:30 PM - 4:00 PM (Cohort B)
- **Topics:** Capacity analysis techniques, PATA case preparation
- **Focus:** Quantitative methods for bottleneck identification

## Teaching Notes
- Emphasize the interconnected nature of airline operations
- Use concrete calculations for de-icing capacity analysis
- Connect theoretical concepts to real-world operational challenges
- Highlight the importance of contingency planning for predictable disruptions
