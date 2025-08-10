# Lecture 2: Capacity Analysis 1 - Predictable Variability (JetBlue)

**Date:** July 22  
**Duration:** 1.5 hours  
**Instructor:** Prof. Vivek Farias
![[2♻️analyze(🔴capacity-variability, ✈️airline) 2025-07-22-8.svg]]
%%[[2♻️analyze(🔴capacity-variability, ✈️airline) 2025-07-22-8|🖋 Edit in Excalidraw]]%%

----
# manual note
product is dynamic (erode), capabilities and how to use capabilities (how to adjust)


supply side levers: capacity and inventory widgets (physical), 
demand side levers : choice modeling

make to stock then make to order 200, 100 (chain)

shybird founder's 🧫experimented with chatgpt + note from shybird founder, tweak is chatgpt 

redesign the process-> importance of D (hardship of changing process? replicated around 5k stores)

⭐️the more aggregated, the lower variability sigma / sqrt(T) 
- clock precision asymmetry: customers in min suppliers in hr
- hourly not min by min basis; no estimate for peak demand per min 
- 💥burst causes delay

paid for expensive machine and people and the utilization is 40% 

two flightes delay (four of them are in process)

predictable variability and unpredictable variability

using jetblue, uber, 

- given no variability, 100 utilization (rho) is idea 
- predictable variability: buildup diagram
- unpredictable variability (queue theory)
- catastrophic variability: war, sudden tariff, deep understanding (restsef levi) on risk management (framework company around the world use)

function of the process, capability, demand -> congestion

process flow, demand capacity, cogenstion, financial decision analysis

demand and supply, work as being liquid

step by step from 
1. deterministic cases, 
2. then adding SEASONAL FISHING 

freshness of fish (delay experienced by fish), 
on avg, how long the fish was in the freezer

⭐️flights have ebb and flow, we have 1.7hr delay
⭐️
1. variability causes delays (quantified from burger king)
2. increase demand by 36% but delay increased by 100% (NONLINEAR effect)

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

## 🔺 The Six Questions Framework

```
        1. Capabilities?          2. Customer?
              🟢                      🟣
       Low-cost carrier         Value seekers
       High utilization         Business + leisure
                \                    /
                 \                  /
                  \                /
        5. Coordinate? ←→ 6. Compel?
                  /                \
                 /                  \
                /                    \
              🟠                      🔴
       Efficiency focus         "Humanity" promise
       Lean operations          Low fares + service
```

### JetBlue Analysis
1. **🟢 Capabilities:** Point-to-point network, high aircraft utilization, lean staffing
2. **🟣 Customer:** Price-sensitive travelers wanting better experience than ultra-low-cost
3. **🟠 Goals:** Maximize asset utilization, minimize costs, maintain service quality
4. **🔴 Offering:** Affordable fares with amenities, "bringing humanity back to air travel"
5. **Coordinate:** Lean operations enable low fares but create vulnerability
6. **Compel:** Better service than competitors at similar price points

### The De-icing Bottleneck
- **Predictable variability:** Winter weather creates recurring capacity constraint
- **Cascade effect:** 4 de-icing positions serve 58→75 flights
- **Nonlinear impact:** 30% demand increase → 100% delay increase
- Shows how efficiency focus (high utilization) reduces resilience

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
